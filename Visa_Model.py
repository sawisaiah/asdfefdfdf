import warnings
from sklearn.exceptions import UndefinedMetricWarning

# Suppress the warning
warnings.filterwarnings("ignore", category=UndefinedMetricWarning)

# import the streamlit library

import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn.preprocessing import LabelEncoder 
from sklearn.model_selection import train_test_split


from sklearn.linear_model import LogisticRegression


import seaborn as sns
import matplotlib.pyplot as plt


import streamlit as st
import joblib

# App's Title
st.title('Your Chance of USA Student Visa Success Rate?')
Visa_Model= joblib.load("Visa_Model.pkl")


name = st.text_input('May I Know Your Name', '')

if name:

    st.success(f" **Hi {name}!This prediction is just for fun. For prediction, Please provide your pursuing degree, person who will sponsor your study, any loan or grant and scholarship, if applicable.**")
    

    # Create selectbox
    d= st.selectbox("So, what degree are you pursuing?", ("Graduate", "Undergraduate"))
    if d=="Graduate":
        degree=0
    else:
        degree=1
        
    s= st.selectbox("Who will be sponsoring your study", ("Parents", "Father","Mother","Spouse"))
    if s=="Father":
        sponsor=0
    elif s=="Mother":
        sponsor=1
    elif s=="Parents":
        sponsor=2
    else:
        sponsor=3
    
    #Create radio button
    l = st.radio ("Have you secured any loan?",("Yes","No"))
    if l=="Yes":
        loan=1
    else:
        loan=0
    
    scholar = st.radio ("Have you been granted any scholarship?",("Yes","No"))
    if scholar=="Yes":
        scholarship=1
    else:
        scholarship=0
    data= [degree, sponsor, loan, scholarship]
    
    result=Visa_Model.predict([data])
    
    button_clicked = st.button("Apply")
    if button_clicked:
        
        if result==0:
            st.success(f"Congratulation {name}. I am approving your visa and will be keeping your passport and come pick your visa and passport within 7 days")
        else:
            st.success(f"I'm sorry {name}. You are not qualify for the visa. Do apply again")