import streamlit as st
import numpy as np 
import tensorflow as tf

def model_prediction(test_image):
    model = tf.keras.models.load_model("insectidentify/farmInsect1.h5")
    image = tf.keras.preprocessing.image.load_img(test_image, target_size=(64, 64))
    input_arr = tf.keras.preprocessing.image.img_to_array(image)
    input_arr = np.array([input_arr])
    predictions = model.predict(input_arr)
    return np.argmax(predictions)



def insect():
    st.header("Predict insect")
    test_image = st.file_uploader("Choose an image")

    if st.button("Show image"):
        st.image(test_image)

    if st.button("Predict"):
        st.write("Prediction")
        result_index = model_prediction(test_image)

        # Map numeric index to class names
        class_names = ['Africanized Honey Bees (Killer Bees)','Aphids','Armyworms','Brown Marmorated Stink Bugs', 'Cabbage Loopers','Citrus Canker','Colorado Potato Beetles','Corn Borers','Corn Earworms', 'Fall Armyworms','Fruit Flies','Spider Mites','Thrips','Tomato Hornworms','Western Corn Rootworms']
        predicted_class = class_names[result_index]

        st.success("It is a " + predicted_class)
