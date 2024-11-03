# importing packages
import streamlit as st
import pandas as pd
from PIL import Image
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

def data_exp():
    # Load data
    df = pd.read_csv("heart.csv")
    dt = pd.read_csv("renamed_heart.csv")

    # Sidebar submenu for EDA options
    submenu = ["Dataset Overview", "Data Visualizations"]
    choice = st.sidebar.selectbox("EDA Options", submenu)

    if choice == "Dataset Overview":
        st.title("🔍 Dataset Overview")
        st.markdown("""
        Explore the heart health dataset with a detailed overview, statistical summaries, and data type analysis.
        """)
        st.subheader("📊 Data Preview")
        st.dataframe(df)

        st.subheader("📈 Statistical Summary")
        st.markdown("Detailed statistics for numerical columns.")
        st.dataframe(df.describe())

        col1, col2 = st.columns(2)

        with col1:
            st.subheader("🔎 Data Types")
            st.markdown("Overview of data types for each feature.")
            st.dataframe(df.dtypes)

        with col2:
            st.subheader("ℹ️ Data Information")
            img = Image.open("info.jpeg")
            st.image(img, caption="Detailed Data Info", use_column_width=True)

        with col1:
            with st.expander("🔸 Distribution by Sex"):
                st.write("Frequency distribution for the 'Sex' feature.")
                st.dataframe(dt["sex"].value_counts())

            with st.expander("🔸 Distribution by Rest ECG"):
                st.write("Frequency distribution for the 'Rest ECG' feature.")
                st.dataframe(dt["rest_ecg"].value_counts())

        with col2:
            with st.expander("🔸 Distribution by Chest Pain Type"):
                st.write("Frequency distribution for the 'Chest Pain Type' feature.")
                st.dataframe(dt["chest_pain_type"].value_counts())

            with st.expander("🔸 Distribution by ST Slope"):
                st.write("Frequency distribution for the 'ST Slope' feature.")
                st.dataframe(dt["st_slope"].value_counts())

    elif choice == "Data Visualizations":
        st.title("📊 Interactive Data Visualizations")
        st.markdown("""
        Gain deeper insights into the dataset through a series of interactive charts and plots.
        """)
        img = Image.open("chart.png")
        st.image(img, caption="Overview of Visual Data Analysis", use_column_width=True)
        with st.expander("🔹 Histogram and Bar Plots"):
            choose = st.selectbox("Choose Plot", ["Distribution of Target", "Target vs Sex", "Target vs Fasting Blood Sugar", "Target vs Exercise Induced Angina"])
            if choose == "Distribution of Target":
                fig = px.histogram(dt, x="target", color="target", title="Distribution of Target Variable")
                st.plotly_chart(fig)

            elif choose == "Target vs Sex":
                fig = px.histogram(dt, x="target", color="sex", barmode="group", title="Target vs Sex")
                st.plotly_chart(fig)

            elif choose == "Target vs Fasting Blood Sugar":
                fig = px.histogram(dt, x="target", color="fasting_blood_sugar", title="Target vs Fasting Blood Sugar")
                st.plotly_chart(fig)

            elif choose == "Target vs Exercise Induced Angina":
                fig = px.histogram(dt, x="target", color="exercise_induced_angina", barmode="group", title="Target vs Exercise Induced Angina")
                st.plotly_chart(fig)

        with st.expander("🔹 Frequency Distribution Plots"):
            choose = st.selectbox("Choose Plot", ["By Chest Pain Type", "By Max Heart Rate Achieved", "By Age"])
            if choose == "By Chest Pain Type":
                fig = px.pie(dt, names="chest_pain_type", title="Distribution by Chest Pain Type")
                st.plotly_chart(fig)

            elif choose == "By Max Heart Rate Achieved":
                fig, ax = plt.subplots(figsize=(10, 8))
                sns.histplot(dt["max_heart_rate_achieved"], bins=10, kde=True, ax=ax)
                st.pyplot(fig)

            elif choose == "By Age":
                fig, ax = plt.subplots(figsize=(10, 8))
                sns.histplot(dt["age"], bins=10, kde=True, color="red", ax=ax)
                st.pyplot(fig)

        with st.expander("🔹 Scatter Plots"):
            choose = st.selectbox("Choose Plot", ["Age vs Resting Blood Pressure", "Age vs Cholesterol", "Cholesterol vs Max Heart Rate"])
            if choose == "Age vs Resting Blood Pressure":
                fig, ax = plt.subplots(figsize=(10, 8))
                sns.scatterplot(x="age", y="resting_blood_pressure", data=dt, ax=ax)
                st.pyplot(fig)

            elif choose == "Age vs Cholesterol":
                fig = px.scatter(dt, x="age", y="cholesterol", title="Age vs Cholesterol")
                st.plotly_chart(fig)

            elif choose == "Cholesterol vs Max Heart Rate":
                fig, ax = plt.subplots(figsize=(10, 8))
                ax.scatter(dt["cholesterol"], dt["max_heart_rate_achieved"])
                ax.set_title("Cholesterol vs Max Heart Rate")
                ax.set_xlabel("Cholesterol")
                ax.set_ylabel("Max Heart Rate Achieved")
                st.pyplot(fig)

        with st.expander("🔹 Outlier Detection"):
            choose = st.selectbox("Choose Plot", ["Age", "Resting Blood Pressure", "Cholesterol", "Max Heart Rate Achieved", "ST Depression"])
            if choose == "Age":
                fig = px.box(dt, x="age", title="Box Plot for Age")
                st.plotly_chart(fig)

            elif choose == "Resting Blood Pressure":
                fig, ax = plt.subplots(figsize=(10, 8))
                sns.boxplot(x=dt["resting_blood_pressure"], ax=ax)
                ax.set_title("Box Plot for Resting Blood Pressure")
                st.pyplot(fig)

            elif choose == "Cholesterol":
                fig, ax = plt.subplots(figsize=(10, 8))
                sns.boxplot(x=dt["cholesterol"], ax=ax)
                ax.set_title("Box Plot for Cholesterol")
                st.pyplot(fig)

            elif choose == "Max Heart Rate Achieved":
                fig = px.box(dt, x="max_heart_rate_achieved", title="Box Plot for Max Heart Rate Achieved")
                st.plotly_chart(fig)

            else:
                fig, ax = plt.subplots(figsize=(10, 8))
                sns.boxplot(x=dt["st_depression"], ax=ax)
                ax.set_title("Box Plot for ST Depression")
                st.pyplot(fig)

        with st.expander("🔹 Correlation Heatmap and Pair Plot"):
            choose = st.selectbox("Choose Plot", ["Heat Map", "Pair Plot"])
            if choose == "Heat Map":
                corr_matrix = df.corr()
                fig = px.imshow(corr_matrix, title="Correlation Heat Map")
                st.plotly_chart(fig)

            else:
                img = Image.open("pairplot.jpeg")
                st.image(img, caption="Pair Plot Analysis", use_column_width=True)
