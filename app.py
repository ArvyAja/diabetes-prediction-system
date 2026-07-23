import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("model_diabetes.pkl")

st.set_page_config(
    page_title="Diabetes Prediction System",
    page_icon="🩺",
    layout="centered"
)

st.title("🩺 Diabetes Prediction System")
st.write("Masukkan data pasien untuk memprediksi kemungkinan diabetes menggunakan model Random Forest.")

st.markdown("---")

age = st.number_input("Age", min_value=1, max_value=120, value=30)

bmi = st.number_input("BMI", min_value=10.0, max_value=60.0, value=25.0)

glucose = st.number_input(
    "Glucose Fasting",
    min_value=50.0,
    max_value=300.0,
    value=100.0
)

hba1c = st.number_input(
    "HbA1c",
    min_value=3.0,
    max_value=15.0,
    value=5.5
)

family = st.selectbox(
    "Family History Diabetes",
    ["No", "Yes"]
)

hypertension = st.selectbox(
    "Hypertension History",
    ["No", "Yes"]
)

family = 1 if family == "Yes" else 0
hypertension = 1 if hypertension == "Yes" else 0

if st.button("🔍 Prediksi"):

    data = pd.DataFrame({
        "age":[age],
        "bmi":[bmi],
        "glucose_fasting":[glucose],
        "hba1c":[hba1c],
        "family_history_diabetes":[family],
        "hypertension_history":[hypertension]
    })

    hasil = model.predict(data)

    st.markdown("---")

    if hasil[0] == 1:
        st.error("⚠️ Hasil Prediksi: Terdiagnosis Diabetes")
    else:
        st.success("✅ Hasil Prediksi: Tidak Terdiagnosis Diabetes")