import streamlit as st
import pandas as pd 

def eda():
    dfp = pd.read_csv("heart.csv")
    st.subheader("This is our data")
    st.dataframe(dfp)