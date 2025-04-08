import streamlit as st
import numpy as np
import json
import joblib

model = joblib.load("banglore_home_prices_model.pkl")
with open("columns.json", "r") as f:
    data_columns = json.load(f)['data_columns']
locations = data_columns[3:]

def predict_price(location, sqft, bath, bhk):
    try:
        loc_index = data_columns.index(location.lower())
    except:
        loc_index = -1

    x = np.zeros(len(data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index >= 0:
        x[loc_index] = 1

    return model.predict([x])[0]

st.set_page_config(page_title="Bangalore House Price Predictor", layout="centered")

st.title("🏙️ Bangalore House Price Prediction")

st.markdown("🏡Thinking of buying or selling a home in Bangalore? Get reliable price estimates in seconds!!")

st.markdown("### Enter property details:")

location = st.selectbox("Location", sorted(locations))
sqft = st.number_input("Total Square Feet", min_value=300, max_value=10000, value=1000)
bath = st.slider("Bathrooms", 1, 10, 2)
bhk = st.slider("BHK", 1, 10, 3)

if st.button("Predict Price"):
    result = predict_price(location, sqft, bath, bhk)
    st.success(f"💰 Estimated Price: ₹ {round(result, 2)} Lakhs")

st.markdown("<p style='text-align: center; font-style: italic; color: #888;'>“An investment in knowledge pays the best interest.” – Anjaneya Sharma Jr.</p>", unsafe_allow_html=True)

st.markdown("---")
st.markdown("<p style='text-align: center; font-size: 14px;'>Created with ❤️ by <strong>Mulukutla Sai Krishna</strong></p>", unsafe_allow_html=True)
