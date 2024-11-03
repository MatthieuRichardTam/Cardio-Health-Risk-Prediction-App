# Import necessary packages
import streamlit as st
import joblib
import numpy as np

attribute = ("""
## 📝 Attribute Information
Below is a description of the medical attributes used for prediction:
- **Age**: Age of the patient in years.
- **Sex**: 1 = Male, 0 = Female.
- **Chest Pain Type (cp)**:
  - 1: Typical angina
  - 2: Atypical angina
  - 3: Non-anginal pain
  - 4: Asymptomatic
- **Resting Blood Pressure (trestbps)**: mm Hg on admission.
- **Serum Cholesterol (chol)**: mg/dl.
- **Fasting Blood Sugar (fbs)**: > 120 mg/dl (1 = true; 0 = false).
- **Resting ECG (restecg)**:
  - 0: Normal
  - 1: ST-T wave abnormality
  - 2: Probable left ventricular hypertrophy
- **Max Heart Rate Achieved (thalach)**: Maximum beats per minute.
- **Exercise Induced Angina (exang)**: 1 = Yes, 0 = No.
- **ST Depression (oldpeak)**: ST depression induced by exercise relative to rest.
- **ST Slope**:
  - 1: Upsloping
  - 2: Flat
  - 3: Downsloping
- **Number of Major Vessels (ca)**: 0-3, colored by fluoroscopy.
- **Thalassemia (thal)**:
  - 3: Normal
  - 6: Fixed defect
  - 7: Reversible defect.
""")

encoded_values = {
    "Female": 0, "Male": 1, 'typical angina': 0, 'atypical angina': 1,
    "non-anginal pain": 2, "asymptomatic": 3, "lower than 120mg/ml": 0,
    "greater than 120mg/ml": 1, 'normal': 0, 'ST-T wave abnormality': 1,
    'left ventricular hypertrophy': 2, "no": 0, "yes": 1, "upsloping": 0,
    "flat": 1, "downsloping": 2, "normal": 1, "fixed defect": 2, "reversable defect": 3
}

# Function for encoding values
def encod_val(val, my_dict):
    return my_dict.get(val)

def risk_predic():
    st.header("💡 Heart Disease Risk Prediction")
    st.markdown(attribute)

    st.subheader("🔢 Enter Patient Details")
    col1, col2 = st.columns(2)

    with col1:
        age = st.number_input("Age", 29, 80, 54)
        chest_pain_type = st.selectbox("Chest Pain Type", ['typical angina', 'atypical angina', "non-anginal pain", "asymptomatic"])
        cholestrol = st.number_input("Cholesterol Level (mg/dl)", 120, 575, 245)
        rest_ecg = st.selectbox("Rest ECG Type", ['normal', 'ST-T wave abnormality', 'left ventricular hypertrophy'])
        exercise_induced_angina = st.radio("Exercise Induced Angina", ["yes", "no"])
        st_slope = st.selectbox("ST Slope Type", ['upsloping', 'flat', 'downsloping'])

    with col2:
        sex = st.radio("Gender", ["Male", "Female"])
        resting_blood_pressure = st.number_input("Resting Blood Pressure (mm Hg)", 90, 200, 131)
        fasting_blood_sugar = st.radio("Fasting Blood Sugar Level", ["lower than 120mg/ml", 'greater than 120mg/ml'])
        max_heart_rate_achieved = st.number_input("Max Heart Rate Achieved", 70, 210, 109)
        st_depression = st.number_input("ST Depression", 0.0, 7.0, 1.0, step=0.1)
        num_major_vessels = st.number_input("Number of Major Vessels (0-3)", 0, 3, 1)

    thalassemia = st.selectbox("Thalassemia Type", ["normal", "fixed defect", "reversable defect"])

    with st.expander("🔍 Review Your Input"):
        input_data = {
            "Age": age, "Gender": sex, "Chest Pain Type": chest_pain_type, "Resting BP": resting_blood_pressure,
            "Cholesterol": cholestrol, "Fasting Blood Sugar": fasting_blood_sugar, "Rest ECG": rest_ecg,
            "Max Heart Rate": max_heart_rate_achieved, "Exercise Induced Angina": exercise_induced_angina,
            "ST Depression": st_depression, "ST Slope": st_slope, "Major Vessels": num_major_vessels,
            "Thalassemia": thalassemia
        }
        st.write(input_data)

        result = [encod_val(val, encoded_values) if isinstance(val, str) else val for val in input_data.values()]

    with st.expander("📊 Prediction Results"):
        model_input = np.array(result).reshape(1, -1)
        model = joblib.load("lr_model")

        prediction = model.predict(model_input)
        st.write("Prediction:", "⚠️ High Risk" if prediction == 1 else "✅ Low Risk")

        prob = model.predict_proba(model_input)
        st.write("Probability Score:", {"Positive Risk": prob[0][1], "Negative Risk": prob[0][0]})
        if prediction == 1:
            st.warning("⚠️ High risk detected. Please consult a healthcare professional.")
        else:
            st.success("✅ Low risk. Keep up a healthy lifestyle!")
