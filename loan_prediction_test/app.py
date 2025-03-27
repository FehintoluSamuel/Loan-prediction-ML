import streamlit as st
import joblib
import pandas as pd

# Load the trained pipeline
pipeline = joblib.load('loan_eligibility_pipeline.pkl')

# Streamlit App Title
st.title("Loan Eligibility Predictor")

# Collect user input
st.header("Enter Applicant Details")

# Define input fields (modify according to your dataset)
gender = st.selectbox("Gender", ["Male", "Female"])
married = st.selectbox("Marital Status", ["Yes", "No"])
dependents = st.selectbox("Number of Dependents", ["0", "1", "2", "3+"])
education = st.selectbox("Education", ["Graduate", "Not Graduate"])
self_employed = st.selectbox("Self Employed?", ["Yes", "No"])
applicant_income = st.number_input("Applicant Income", min_value=0)
coapplicant_income = st.number_input("Coapplicant Income", min_value=0)
loan_amount = st.number_input("Loan Amount", min_value=0)
loan_term = st.number_input("Loan Term (in months)", min_value=0)
credit_history = st.selectbox("Credit History", ["Yes", "No"])
property_area = st.selectbox("Property Area", ["Urban", "Semiurban", "Rural"])

# Convert categorical inputs to match training data
input_data = pd.DataFrame({
    'Gender': [gender],
    'Married': [married],
    'Dependents': [dependents],
    'Education': [education],
    'Self_Employed': [self_employed],
    'ApplicantIncome': [applicant_income],
    'CoapplicantIncome': [coapplicant_income],
    'LoanAmount': [loan_amount],
    'Loan_Amount_Term': [loan_term],
    'Credit_History': [1 if credit_history == "Yes" else 0],
    'Property_Area': [property_area]
})

# Predict when the user clicks the button
if st.button("Check Loan Eligibility"):
    prediction = pipeline.predict(input_data)[0]
    result = "Eligible" if prediction == 1 else "Not Eligible"
    st.subheader(f"Loan Status: {result}")