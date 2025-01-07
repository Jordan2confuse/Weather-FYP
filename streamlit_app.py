import streamlit as st
import json

# Streamlit App
def main():
    st.title("Upload Random Forest Model")
    st.write("Upload your Random Forest model (JSON format) to view its contents.")

    # File uploader for the JSON model
    model_file = st.file_uploader("Upload Random Forest Model (JSON File):", type=["json"])
    
    if model_file:
        # Load and display the JSON model
        model_components = json.load(model_file)
        st.success("Model uploaded successfully!")
        st.json(model_components)

if _name_ == "_main_":
    main()
