import streamlit as st
import numpy as np
import pickle

# Load model
model = pickle.load(open("model/newmodel.pkl", "rb"))
columns = pickle.load(open("model/columns.pkl", "rb"))

st.title("🏠 Bangalore House Price Prediction")

st.sidebar.header("Enter Property Details")

# Inputs
sqft = st.slider("Total Sqft", 500, 5000, 1000)
bath = st.selectbox("Bathrooms", [1, 2, 3, 4, 5])
balcony = st.selectbox("Balcony", [0, 1, 2, 3])
bhk = st.selectbox("BHK", [1, 2, 3, 4, 5])

# Location dropdown
locations = [col.replace("location_", "") for col in columns if "location_" in col]
location = st.selectbox("Location", locations)

# Prediction
if st.button("Predict Price"):

    input_data = np.zeros(len(columns))

    input_data[columns.get_loc("total_sqft")] = sqft
    input_data[columns.get_loc("bath")] = bath
    input_data[columns.get_loc("balcony")] = balcony
    input_data[columns.get_loc("bhk")] = bhk

    loc_col = "location_" + location
    if loc_col in columns:
        input_data[columns.get_loc(loc_col)] = 1

    prediction = model.predict([input_data])

    st.success(f" Estimated Price: ₹ {prediction[0]:.2f} Lakhs")