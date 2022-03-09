import streamlit as st
import requests

URL = 'https://bck-fail.herokuapp.com/'

st.title("aplikasi predisksi serangan jantung")

Age = st.number_input('Age', min_value=20, max_value=100, step=1)
Sex = st.selectbox(
    'Sex',('M', 'F')
)

ChestPainType = st.selectbox('ChestPainType', ('TA', 'ATA', 'NAP', 'ASY'))
RestingBP = st.number_input('RestingBP', min_value=0, max_value=500, step=1)
Cholesterol = st.number_input('Cholesterol',min_value=40, max_value=1000, step=1)
FastingBS = st.selectbox('FaatingBS', (1, 0))
RestingECG = st.selectbox('RestingECG',('Normal', 'ST', 'LVH'))
MaxHR = st.number_input('MaxHR', min_value=60, max_value=400, step=1)
ExerceseAngina = st.selectbox('Exercase Angina', ('Y', 'N'))
Oldpeak = st.number_input('Oldpeak')
ST_Slope = st.selectbox('ST_Slope', ('Up', 'Flat', 'Down'))


data = {
    'Age' : Age ,
    'Sex' : Sex,
    'ChestPainType' : ChestPainType,
    'RestingBP' : RestingBP,
    'Cholesterol' : Cholesterol,
    'FastingBS' : FastingBS,
    'RestingECG' : RestingECG,
    'MaxHR' : MaxHR,
    'ExerciseAngina' : ExerceseAngina,
    'Oldpeak' : Oldpeak,
    'ST_Slope' : ST_Slope,}

#print(data)

r = requests.post(URL, json=data)
#a = pd.DataFrame(data, index=[0])

#st.write(a)
res = r.json()

#st.write(res)


st.write(f"Result Prediction : {res['data']['result']}")
