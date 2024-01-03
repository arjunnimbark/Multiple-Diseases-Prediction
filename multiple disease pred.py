import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Load the saved models
diabetes_model = pickle.load(open('G:/MACHINE LEARNING/MULTIPLE DISEASES/diabetes_model.sav', 'rb'))
heart_disease_model = pickle.load(open('G:/MACHINE LEARNING/MULTIPLE DISEASES/heart_disease_model.sav', 'rb'))
parkinsons_model = pickle.load(open('G:/MACHINE LEARNING/MULTIPLE DISEASES/parkinsons_model.sav', 'rb'))



# Sidebar for navigation
with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System',
                           ['Diabetes Prediction', 'Heart Disease Prediction', 'Parkinsons Prediction'],
                           icons=['activity', 'heart', 'person'],
                           default_index=0)

# Diabetes Prediction Page
if selected == 'Diabetes Prediction':
    # Page title and header
    st.title('Diabetes Prediction using ML')
  

    # Input fields
    st.subheader('Input Features:')
    col1, col2, col3 = st.columns(3)
    with col1:
        pregnancies = st.text_input('Number of Pregnancies')
        glucose = st.text_input('Glucose Level')
        blood_pressure = st.text_input('Blood Pressure value')
        skin_thickness = st.text_input('Skin Thickness value')
    with col2:
        insulin = st.text_input('Insulin Level')
        bmi = st.text_input('BMI value')
        diabetes_pedigree_function = st.text_input('Diabetes Pedigree Function value')
    with col3:
        age = st.text_input('Age of the Person')

    # Code for Prediction
    diab_diagnosis = ''
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree_function, age]])
        diab_diagnosis = 'The person is diabetic' if diab_prediction[0] == 1 else 'The person is not diabetic'

    # Display result
    st.subheader('Prediction Result:')
    st.success(diab_diagnosis)



# Heart Disease Prediction Page
if selected == 'Heart Disease Prediction':
    # Page title and header
    st.title('Heart Disease Prediction using ML')


    # Input fields
    st.subheader('Input Features:')
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        age = st.text_input('Age')
        sex = st.text_input('Sex')
        cp = st.text_input('Chest Pain types')
        trestbps = st.text_input('Resting Blood Pressure')
        chol = st.text_input('Serum Cholestoral in mg/dl')
    with col2:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')
        restecg = st.text_input('Resting Electrocardiographic results')
        thalach = st.text_input('Maximum Heart Rate achieved')
        exang = st.text_input('Exercise Induced Angina')
        oldpeak = st.text_input('ST depression induced by exercise')
    with col3:
        slope = st.text_input('Slope of the peak exercise ST segment')
        ca = st.text_input('Major vessels colored by flourosopy')
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')
    
    # Code for Prediction
    heart_diagnosis = ''
    if st.button('Heart Disease Test Result'):
        heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
        heart_diagnosis = 'The person is having heart disease' if heart_prediction[0] == 1 else 'The person does not have any heart disease'

    # Display result
    st.subheader('Prediction Result:')
    st.success(heart_diagnosis)



# Parkinson's Prediction Page
if selected == "Parkinsons Prediction":
    # Page title and header
    st.title("Parkinson's Disease Prediction using ML")


    # Input fields
    st.subheader('Input Features:')
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')
        fhi = st.text_input('MDVP:Fhi(Hz)')
        flo = st.text_input('MDVP:Flo(Hz)')
        Jitter_percent = st.text_input('MDVP:Jitter(%)')
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')
    with col2:
        RAP = st.text_input('MDVP:RAP')
        PPQ = st.text_input('MDVP:PPQ')
        DDP = st.text_input('Jitter:DDP')
        Shimmer = st.text_input('MDVP:Shimmer')
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')
    with col3:
        APQ3 = st.text_input('Shimmer:APQ3')
        APQ5 = st.text_input('Shimmer:APQ5')
        APQ = st.text_input('MDVP:APQ')
        DDA = st.text_input('Shimmer:DDA')
        NHR = st.text_input('NHR')
    with col4:
        HNR = st.text_input('HNR')
        RPDE = st.text_input('RPDE')
        DFA = st.text_input('DFA')
        spread1 = st.text_input('spread1')
        spread2 = st.text_input('spread2')
    with col5:
        D2 = st.text_input('D2')
        PPE = st.text_input('PPE')

    # Code for Prediction
    parkinsons_diagnosis = ''
    if st.button("Parkinson's Test Result"):
        parkinsons_prediction = parkinsons_model.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ, DDP, Shimmer, Shimmer_dB, APQ3, APQ5, APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]])
        parkinsons_diagnosis = "The person has Parkinson's disease" if parkinsons_prediction[0] == 1 else "The person does not have Parkinson's disease"

    # Display result
    st.subheader('Prediction Result:')
    st.success(parkinsons_diagnosis)
