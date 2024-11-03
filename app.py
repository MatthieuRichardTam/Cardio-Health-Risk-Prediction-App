# importing the packages
import streamlit as st
from PIL import Image

# importing external modules
from data_exp import data_exp
from risk_predic import risk_predic

def main():
    # Sidebar menu
    menu = ["Home", "Data Exploration", "Risk Prediction"]
    choice = st.sidebar.selectbox("Navigation", menu)

    if choice == "Home":
        st.markdown("<h2 style='text-align: center; font-size: 40px;'>💖 Heart Health Risk Prediction App</h2>", unsafe_allow_html=True)
        img = Image.open("cardio.jpg")
        st.image(img, caption="Monitor Your Heart Health", use_column_width=True)

        st.markdown("""
        Welcome to the **Heart Health Risk Prediction App**! This tool allows you to explore heart disease data and assess risk levels based on patient information using machine learning.

        ### 📚 Data Source
        - The dataset is sourced from the [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/heart+disease).

        ### 🗂️ App Features
        - **Home**: Overview of the app and its purpose.
        - **Data Exploration**: Dive into the dataset with interactive visualizations and analyses.
        - **Risk Prediction**: Input patient data and predict the risk of heart disease using a trained ML model.
        """)
        
    elif choice == "Data Exploration":
        st.header("🔍 Explore the Data")
        st.markdown("""
        Navigate through different visualizations and analyses to understand the data and uncover trends in heart health.
        """)
        data_exp()
        
    elif choice == "Risk Prediction":
        st.header("🧪 Heart Disease Risk Assessment")
        st.markdown("""
        Enter the patient's medical details and receive a prediction for the risk of heart disease.
        """)
        risk_predic()

if __name__ == "__main__":
    main()
