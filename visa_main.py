import pandas as pd
import numpy as np
import streamlit as st
import joblib
LR_Model = joblib.load("visa.pkl")
input1 = st.text_input("Enter University")
input1 = st.text_input("Enter Program")
input1 = st.text_input("Enter Degree")
input1 = st.text_input("Who is your sponsor?")
input1 = st.text_input("Did you get any loan (yes/no) ?")
input1 = st.text_input("Did you get scholarship (yes/no) ?")

button_clicked = st.button("Predict")
if button_clicked:
    user_input = [input1, input2, input3, input4,input5,input6]
    prediction = LR_Model.predict([user_input])
    if prediction[0] == 1:
        st.write('You have high chance of getting F1 visa')
    else:
        st.write("You have low chance of getting F1 visa")
