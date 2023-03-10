# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 20:58:32 2023

@author: bhanu
"""

import numpy as np
import pickle
import streamlit as st
from sklearn.preprocessing import StandardScaler

#loaded_model = pickle.load(open('trained_model.sav', 'rb'))
loaded_model = pickle.load(open('diabetes_model.sav', 'rb'))

# creating a function prediction
def diabetics_prediction(input_data):
    # input_data = (5,166,72,19,175,25.8,0.587,51)

    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
    
    # extra added
    # scaler = StandardScaler()
    # input_data_reshaped = scaler.fit_transform(input_data_reshaped)
    

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
      return 'The person is not diabetic'
    else:
      return 'The person is diabetic'
  
    
def main():
    
    
    # giving a title for web page
    st.title("Diabetics prediction website")
    
    # getting the input data from the user
    Pregnancies = st.text_input('Number of Pregnancies')
    Glucose = st.text_input('Glucose Level')
    BloodPressure = st.text_input('Blood Pressure value')
    SkinThickness = st.text_input('Skin Thickness value')
    Insulin = st.text_input('Insulin Level')
    BMI = st.text_input('BMI value')
    DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    Age = st.text_input('Age of the Person')
    
    
    # code for Prediction
    diagnosis = ''
 
    # creating a button for Prediction
 
    if st.button('Diabetes Test Result'):
     diagnosis = diabetics_prediction([Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age])
     
     
     st.success(diagnosis)
    
if __name__ == '__main__':
    main()

    
    
    
    
    
    
    