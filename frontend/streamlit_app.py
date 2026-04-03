import streamlit as st
import requests

st.title("📩 Spam vs Ham Classifier (Best Model)")

user_input = st.text_area("Enter your message:")

if st.button("Predict"):
    if user_input.strip() == "":
        st.warning("Please enter a message")
    else:
        response = requests.post(
            "http://127.0.0.1:5000/predict",
            json={"message": user_input}
        )

        result = response.json()['prediction']

        if result == "Spam":
            st.error("🚨 Spam Detected")
        else:
            st.success("✅ Ham Message")