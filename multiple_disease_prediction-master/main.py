import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(page_title="CSE0247 - DISEASE PREDICTION",
                   layout="wide",
                   page_icon="🧑‍⚕")

working_dir = os.path.dirname(os.path.abspath(__file__))

def load_model(filename):
    path = os.path.join(working_dir, 'saved_models', filename)
    if os.path.exists(path):
        return pickle.load(open(path, 'rb'))
    else:
        st.error(f"Error: {filename} not found in saved_models folder.")
        return None

diabetes_model = load_model('diabetes_model.sav')
heart_disease_model = load_model('heart_disease_model.sav')
parkinsons_model = load_model('parkinsons_model.sav')
liver_disease_model = load_model('liver_disease_model.sav')

with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System',
                           ['Diabetes Prediction',
                            'Heart Disease Prediction',
                            'Parkinson’s Prediction',
                            'Liver Disease Prediction'],
                           menu_icon='hospital-fill',
                           default_index=0)

if selected == 'Diabetes Prediction' and diabetes_model:
    st.title('Diabetes Prediction using ML')
    col1, col2, col3 = st.columns(3)
    with col1:
        Pregnancies = st.number_input('Number of Pregnancies', min_value=0)
    with col2:
        Glucose = st.number_input('Glucose Level', min_value=0)
    with col3:
        BloodPressure = st.number_input('Blood Pressure', min_value=0)
    with col1:
        SkinThickness = st.number_input('Skin Thickness', min_value=0)
    with col2:
        Insulin = st.number_input('Insulin Level', min_value=0)
    with col3:
        BMI = st.number_input('BMI', min_value=0.0)
    with col1:
        DiabetesPedigreeFunction = st.number_input('Diabetes Pedigree Function', min_value=0.0)
    with col2:
        Age = st.number_input('Age', min_value=0)

    if st.button('Diabetes Test Result'):
        user_input = [[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]]
        diab_prediction = diabetes_model.predict(user_input)
        result = 'The person is diabetic' if diab_prediction[0] == 1 else 'The person is not diabetic'
        st.success(result)

elif selected == 'Heart Disease Prediction' and heart_disease_model:
    st.title('Heart Disease Prediction using ML')
    col1, col2, col3 = st.columns(3)
    with col1:
        Age = st.number_input('Age', min_value=0)
    with col2:
        Sex = st.selectbox('Sex', ['Male', 'Female'])
    with col3:
        ChestPain = st.number_input('Chest Pain Type', min_value=0)
    with col1:
        RestingBP = st.number_input('Resting Blood Pressure', min_value=0)
    with col2:
        Cholesterol = st.number_input('Cholesterol Level', min_value=0)
    with col3:
        FastingBS = st.number_input('Fasting Blood Sugar (1=True, 0=False)', min_value=0, max_value=1)
    with col1:
        RestingECG = st.number_input('Resting ECG', min_value=0)
    with col2:
        MaxHeartRate = st.number_input('Maximum Heart Rate', min_value=0)
    with col3:
        ExerciseAngina = st.number_input('Exercise Induced Angina (1=True, 0=False)', min_value=0, max_value=1)
    with col1:
        Oldpeak = st.number_input('Oldpeak', min_value=0.0)
    with col2:
        Slope = st.number_input('Slope of Peak Exercise ST', min_value=0)
    with col3:
        MajorVessels = st.number_input('Number of Major Vessels', min_value=0)
    with col1:
        Thal = st.number_input('Thalassemia', min_value=0)

    if st.button('Heart Disease Test Result'):
        user_input = [[Age, 1 if Sex == 'Male' else 0, ChestPain, RestingBP, Cholesterol, FastingBS, RestingECG, MaxHeartRate, ExerciseAngina, Oldpeak, Slope, MajorVessels, Thal]]
        heart_prediction = heart_disease_model.predict(user_input)
        result = 'The person has heart disease' if heart_prediction[0] == 1 else 'The person does not have heart disease'
        st.success(result)

elif selected == "Parkinson’s Prediction" and parkinsons_model:
    st.title("Parkinson's Disease Prediction using ML")
    col1, col2, col3 = st.columns(3)
    with col1:
        inputs = [st.number_input(label) for label in [
            'MDVP:Fo (Hz)', 'MDVP:Fhi (Hz)', 'MDVP:Flo (Hz)', 'MDVP:Jitter (%)', 'MDVP:Jitter (Abs)',
            'MDVP:RAP', 'MDVP:PPQ', 'Jitter:DDP', 'MDVP:Shimmer', 'MDVP:Shimmer (dB)',
            'Shimmer:APQ3', 'Shimmer:APQ5', 'MDVP:APQ', 'Shimmer:DDA', 'NHR', 'HNR',
            'RPDE', 'DFA', 'Spread1', 'Spread2', 'D2', 'PPE']]
    
    if st.button("Parkinson’s Test Result"):
        parkinsons_prediction = parkinsons_model.predict([inputs])
        result = "The person has Parkinson’s disease" if parkinsons_prediction[0] == 1 else "The person does not have Parkinson’s disease"
        st.success(result)

elif selected == "Liver Disease Prediction" and liver_disease_model:
    st.title("Liver Disease Prediction using ML")
    col1, col2, col3 = st.columns(3)
    with col1:
        Age = st.number_input('Age', min_value=0)
    with col2:
        Gender = st.selectbox('Gender', ['Male', 'Female'])
    with col3:
        Total_Bilirubin = st.number_input('Total Bilirubin', min_value=0.0)
    with col1:
        Direct_Bilirubin = st.number_input('Direct Bilirubin', min_value=0.0)
    with col2:
        Alkaline_Phosphatase = st.number_input('Alkaline Phosphatase', min_value=0)
    with col3:
        ALT = st.number_input('Alanine Aminotransferase (ALT)', min_value=0)
    with col1:
        AST = st.number_input('Aspartate Aminotransferase (AST)', min_value=0)
    with col2:
        Total_Proteins = st.number_input('Total Proteins', min_value=0.0)
    with col3:
        Albumin = st.number_input('Albumin', min_value=0.0)
    with col1:
        Albumin_Globulin_Ratio = st.number_input('Albumin and Globulin Ratio', min_value=0.0)

    if st.button('Liver Disease Test Result'):
        user_input = [[Age, 1 if Gender == 'Male' else 0, Total_Bilirubin, Direct_Bilirubin, Alkaline_Phosphatase, ALT, AST, Total_Proteins, Albumin, Albumin_Globulin_Ratio]]
        liver_prediction = liver_disease_model.predict(user_input)
        result = 'The person has liver disease' if liver_prediction[0] == 1 else 'The person does not have liver disease'
        st.success(result)
