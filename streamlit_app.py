import streamlit as st
import pandas as pd
import rpy2.robjects as robjects
from rpy2.robjects import pandas2ri
from rpy2.robjects.conversion import localconverter

# Page configuration
st.set_page_config(
    page_title="Random Forest Classifier",
    page_icon="🌲",
    layout="wide"
)

# Title and description
st.title("Random Forest Classifier Prediction")
st.markdown("This app predicts using a Random Forest model trained in R")

@st.cache_resource
def load_model():
    """Load the saved R model"""
    r = robjects.r
    model = r.readRDS("model/random_forest_model.rds")
    return model

def make_prediction(model, input_data):
    """Make predictions using the R model"""
    with localconverter(robjects.default_converter + pandas2ri.converter):
        r_input = pandas2ri.py2rpy(input_data)
    
    # Make prediction
    prediction = robjects.r.predict(model, r_input)
    
    # Convert back to Python
    with localconverter(robjects.default_converter + pandas2ri.converter):
        py_prediction = pandas2ri.rpy2py(prediction)
    
    return py_prediction

def main():
    # Create two columns
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.header("Input Features")
        
        # Add your input fields here - customize according to your model's features
        feature1 = st.number_input("Feature 1", min_value=0.0, max_value=100.0, value=50.0)
        feature2 = st.number_input("Feature 2", min_value=0.0, max_value=100.0, value=50.0)
        # Add more features as needed
        
        # Create input dataframe
        input_data = pd.DataFrame({
            'feature1': [feature1],
            'feature2': [feature2]
            # Add more features as needed
        })
        
        if st.button("Predict", type="primary"):
            try:
                # Load model and make prediction
                model = load_model()
                prediction = make_prediction(model, input_data)
                
                with col2:
                    st.header("Prediction Results")
                    st.success(f"The predicted class is: {prediction[0]}")
                    
                    # Display input data
                    st.subheader("Input Summary")
                    st.dataframe(input_data)
                    
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")
                
    # Add footer
    st.markdown("---")
    st.markdown("Created with ❤️ using Streamlit")

if __name__ == "__main__":
    main()
