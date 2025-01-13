import streamlit as st
import json

# Streamlit App
def main():
    st.title("WeatherWise Alerts")
    st.write("Get your latest weather prediction here!")

    # File uploader for the JSON model
    model_file = st.file_uploader("View your model", type=["json"])

    
    if model_file:
        # Load and display the JSON model
        model_components = json.load(model_file)
        st.success("Model uploaded successfully!")
        st.json(model_components)

if __name__ == "__main__":
    main()
