import streamlit as st
import pickle
import numpy as np



# Load the model and scalers
loaded_model = pickle.load(open('cropRecomendation/model.pkl', 'rb'))
loaded_minmax_scaler = pickle.load(open('cropRecomendation/minmaxscaler.pkl', 'rb'))
loaded_stand_scaler = pickle.load(open('cropRecomendation/standscaler.pkl', 'rb'))

# Create a function for prediction
def predict_crop(N, P, k, temperature, humidity, ph, rainfall):
    # Preprocess the input features using the loaded scalers
    features = np.array([N, P, k, temperature, humidity, ph, rainfall]).reshape(1, -1)
    features_scaled = loaded_stand_scaler.transform(loaded_minmax_scaler.transform(features))

    # Make a prediction using the loaded model
    prediction = loaded_model.predict(features_scaled)

    return prediction

# Streamlit appstre
def main():
    st.title("Crop Recommendation App")

    # Input fields for user input
    N = st.text_input("Enter Nitrogen (N):", 50)
    P = st.text_input("Enter Phosphorus (P):", 50)
    k = st.text_input("Enter Potassium (k):", 50)
    temperature = st.text_input("Enter Temperature:", 80.0)
    humidity = st.text_input("Enter Humidity:", 50)
    ph = st.text_input("Enter pH:", 200)
    rainfall = st.text_input("Enter Rainfall:", 100)

    # Convert user input to numeric values
    try:
        N = float(N)
        P = float(P)
        k = float(k)
        temperature = float(temperature)
        humidity = float(humidity)
        ph = float(ph)
        rainfall = float(rainfall)
    except ValueError:
        st.warning("Please enter valid numeric values.")

    # Make prediction
    if st.button("Predict"):
        prediction = predict_crop(N, P, k, temperature, humidity, ph, rainfall)
        crop_dict = {1: "Rice", 2: "Maize", 3: "Jute", 4: "Cotton", 5: "Coconut", 6: "Papaya", 7: "Orange",
                     8: "Apple", 9: "Muskmelon", 10: "Watermelon", 11: "Grapes", 12: "Mango", 13: "Banana",
                     14: "Pomegranate", 15: "Lentil", 16: "Blackgram", 17: "Mungbean", 18: "Mothbeans",
                     19: "Pigeonpeas", 20: "Kidneybeans", 21: "Chickpea", 22: "Coffee"}

        if prediction[0] in crop_dict:
            st.session_state.crop=prediction[0]
            recommended_crop = crop_dict[prediction[0]]
            st.success(f"The recommended crop is: {recommended_crop}")

            if(st.session_state.crop==10):
                with st.sidebar:
                 image='9.jpg'
                 st.image(image, caption=f"{recommended_crop} Image", use_column_width=True)
                 st.title("Watermelon Farming Essentials")
                 st.write("Climate: Thrives in temperate climates with distinct seasons.")
                 st.write("Soil: Requires well-drained soil with a slightly acidic to slightly alkaline pH")
                 st.write("Consistent watering, avoiding waterlogged soil.")
                 st.write("Climate: Thrives in temperate climates with distinct seasons.")
                 st.button("See more")
        else:
            st.warning("Sorry, we are not able to recommend a proper crop for this environment.")

if __name__ == "__main__":
    main()
