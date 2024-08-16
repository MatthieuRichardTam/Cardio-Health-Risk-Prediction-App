# importing packages
import streamlit as st
from PIL import Image

# importing the files 
from eda import eda
from ml import ml

def main():
    st.title("This is the Heart app")

    menu = ["Home", "Exploratory Data Analysis Section", "Prediction Section", "About"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home":
        st.write("# Early Stage heart attack risk predictor app")
        img = Image.open("heart.jpg")
        st.image(img)

        st.write("""
        The data that we use in this particular app contain the features of a newly heart disease patient 
        or a diabetic patient.

        ### DataSource

        - https://archive.ics.uci.edu/ml/datasets/heart+disease

        ### App Content

        - This app has four sections
        1) Home Page - The page you are currently in

        2) Exploratory Data Analysis - The page in which you will find all the Data Analysis and Visualization Parts

        3) Prediction - The page in which you will be asked to give the information on all the medical aspects
           and we will predict the desired output

        4) About - This Page is about me
        """)
    
    elif choice == "Exploratory Data Analysis Section":
        eda()
    
    elif choice == "Prediction Section":
        ml()
    
    else: 
        st.header("This is about me")

main()
