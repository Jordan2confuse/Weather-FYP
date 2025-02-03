import streamlit as st
import json
import pandas as pd
import tensorflow as tf
import pickle
import matplotlib.pyplot as plt
import io

def display_cnn_model(model):
    """Display CNN model architecture."""
    st.subheader("CNN Model Summary")
    string_io = io.StringIO()
    model.summary(print_fn=lambda x: string_io.write(x + "\n"))
    summary_string = string_io.getvalue()
    st.text(summary_string)

    # Plot model architecture
    st.subheader("Model Architecture")
    plot_filename = "model_plot.png"
    tf.keras.utils.plot_model(model, to_file=plot_filename, show_shapes=True, show_layer_names=True)
    st.image(plot_filename, caption="CNN Model Architecture", use_column_width=True)

def main():
    st.title("WeatherWise Alerts")
    st.write("Upload a JSON, Pickle, or Notebook model file")

    model_file = st.file_uploader("Upload your file", type=["json", "pkl", "ipynb"])
    model = None  # Placeholder for the loaded model

    if model_file:
        try:
            if model_file.name.endswith('.json'):
                model_data = json.load(model_file)
                st.success("JSON file uploaded successfully!")
                st.json(model_data)
                st.write("Model successfully loaded from JSON file!")

            elif model_file.name.endswith('.pkl'):
                model = pickle.load(model_file)
                st.success("Pickle file uploaded successfully!")
                st.write(f"Model Type: {type(model)}")
                st.write(f"Model Details: {model}")

                if isinstance(model, tf.keras.Model):
                    display_cnn_model(model)

            elif model_file.name.endswith('.ipynb'):
                model_data = model_file.read().decode("utf-8")
                st.success("Notebook file uploaded successfully!")
                st.write("Contents of the notebook:")
                st.text(model_data[:1000])

            else:
                st.error("Unsupported file format!")

        except Exception as e:
            st.error(f"An error occurred while processing the file: {e}")

if __name__ == "__main__":
    main()
