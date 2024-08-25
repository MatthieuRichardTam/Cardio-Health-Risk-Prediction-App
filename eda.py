import streamlit as st
import pandas as pd 
from PIL import Image

def eda():
    
    df = pd.read_csv("heart.csv")
    dt = pd.read_csv("renamed_data.csv")
    
    submenu = ["Descriptive", "Plots"]
    choice = st.sidebar.selectbox("Submenu", submenu)

    if choice == "Descriptive":
        st.subheader("This is our data")
        st.dataframe(df)

        st.subheader("Here are the statistical values for all the numerical columns")
        st.dataframe(df.describe())

        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Data Types")
            st.dataframe(df.dtypes)
        
        with col2:
            st.subheader("Basic Information about the data")
            simg = Image.open("info.jpeg")
            st.image(simg)
        
        with col1:
            with st.expander("Column Sex"):
                st.dataframe(dt["sex"].value_counts())

    else : 
        pass

