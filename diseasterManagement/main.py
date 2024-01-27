import streamlit as st
import tensorflow as tf
import numpy as np

# Function to load the trained model
def load_model():
    # Load the model here
    model = tf.keras.models.load_model("diseasterManagement/potatoes.h5")
    return model

# Function to preprocess the input image
def preprocess_image(image):
    # Preprocess the image (resize, normalize, etc.)
    # Replace this with your actual preprocessing steps
    return image

# Function to make a prediction
def predict(model, image):
    # Preprocess the image
    processed_image = preprocess_image(image)

    # Make a prediction using the loaded model
    predictions = model.predict(np.expand_dims(processed_image, axis=0))

    # Get the predicted class and confidence
    predicted_class = class_names[np.argmax(predictions[0])]
    confidence = round(100 * np.max(predictions[0]), 2)

    return predicted_class, confidence

# Load the model and class names
model = load_model()
class_names = ['Tomato___Bacterial_spot', 'Tomato___Early_blight', 'Tomato___Late_blight', 'Tomato___Leaf_Mold', 'Tomato___Septoria_leaf_spot', 'Tomato___Spider_mites_Two-spotted_spider_mite', 'Tomato___Target_Spot', 'Tomato___Tomato_Yellow_Leaf_Curl_Virus', 'Tomato___Tomato_mosaic_virus', 'Tomato___healthy']

def diseaster():
    # Streamlit app
 st.title("Tomato Leaf Disease Identification App")
 st.header("Upload an image for disease identification")

# File uploader
 uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

 if uploaded_file is not None:
    # Display the uploaded image
    st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)

    # Make a prediction when the user clicks the "Predict" button
    if st.button("Predict"):
        # Convert the image to a format suitable for the model
        input_image = tf.keras.preprocessing.image.load_img(uploaded_file, target_size=(256, 256))
        input_image = tf.keras.preprocessing.image.img_to_array(input_image)

        # Get the prediction
        prediction, confidence = predict(model, input_image)

        # Display the prediction result
        st.success(f"Prediction: {prediction}\nConfidence: {confidence}%")