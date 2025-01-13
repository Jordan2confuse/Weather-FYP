import streamlit as st
import pickle

# Streamlit App
def main():
    st.title("WeatherWise Alerts")
    st.write("Get your latest weather prediction here!")

    # File uploader for the PKL model
    model_file = st.file_uploader("View your model", type=["pkl"])

    if model_file:
        # Load the pickle model
        model = pickle.load(model_file)
        st.success("Model uploaded successfully!")

        # Display the type of model or some basic details about it
        st.write(f"Model Type: {type(model)}")
        st.write(f"Model details: {model}")

if __name__ == "__main__":
    main()
