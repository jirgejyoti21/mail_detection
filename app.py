import streamlit as st
import re
import string
import joblib
 # Load model and vectorizer once at the top of app.py
model = joblib.load("model.pkl")
vectorizer = joblib.load("vectorizer.pkl")


def clean_text(text):
    text=text.lower()
    text=re.sub(r'\d+','',text)
    text=re.sub(r'[^\w\s]','',text)
    return text

st.title("Email Spam Detector")
user_input=st.text_area("Enter your email message:")

if st.button("check"):
    cleaned=clean_text(user_input)
    vector=vectorizer.transform([cleaned])
    result=model.predict(vector)[0]
    if result==1:
        st.error("Spam Email")
    else:
        st.success("Ham(Not Spam)")


