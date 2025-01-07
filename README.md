# Random Forest Classifier Web App

This is a Streamlit web application that serves predictions from a Random Forest model trained in R.
import streamlit as st
import pandas as pd

st.title(' 🌀🌡☁ Weather Alert System')

st.info('Get your latest weather updates!')

with st.expander('Data'):
    st.write('*Raw data*')    
    df = pd.read_csv('https://raw.githubusercontent.com/Jordan2confuse/boo-weather/refs/heads/master/weather_prediction_dataset.csv')
    df

## Setup

1. Install the required packages:
2. Make sure you have R installed on your system
3. Place your trained model file (`random_forest_model.rds`) in the `model` folder
4. Run the application:


streamlit run streamlit_app.py

## Features
- Interactive web interface
- Real-time predictions
- Input validation
- Error handling

## Requirements
- Python 3.7+
- R installation
- Packages listed in requirements.txt
