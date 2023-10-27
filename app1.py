import streamlit as st
import pickle
import numpy as np

model = pickle.load(open('placed.pkl', 'rb'))
scaler = pickle.load(open('preprocess.pkl', 'rb'))

st.title('Placement Predictor')

gender = st.selectbox('Gender', ('Female', 'Male'))
ssc = st.number_input('SSC Percentage', min_value=0.0, max_value=100.0)
hse = st.number_input('HSE Percentage', min_value=0.0, max_value=100.0)
hsep = st.selectbox('HSE Percentage Type', ('Commerce', 'Science', 'Other'))
dp = st.number_input('Diploma Percentage', min_value=0.0, max_value=100.0)
df = st.selectbox('Degree Field', ('Commerce & Management', 'Science & Technology', 'Other'))
we = st.number_input('Work Experience', min_value=0)
etp = st.number_input('Employability Test Percentage', min_value=0.0, max_value=100.0)
mbasp = st.selectbox('MBA Specialization', ('Marketing & HR', 'Other'))
mbap = st.number_input('MBA Percentage', min_value=0.0, max_value=100.0)

if gender == 'Female':
    gender = 0
else:
    gender = 1

if hsep == 'Commerce':
    hsep = 1
elif hsep == 'Science':
    hsep = 2
else:
    hsep = 0

if df == 'Commerce & Management':
    df = 0
elif df == 'Science & Technology':
    df = 2
else:
    df = 1

if mbasp == 'Marketing & HR':
    mbasp = 1
else:
    mbasp = 0

t = [[int(gender), float(ssc), float(hse), int(hsep), float(dp), int(df), float(we), float(etp), int(mbasp), float(mbap)]]

output = model.predict(t)

if output[0] == 1:
    output = "Placed"
    models_1 = pickle.load(open('model.pkl', 'rb'))
    x = [[int(gender), int(hsep), int(df), float(etp), float(mbap)]]
    scaled_t = scaler.transform(x)
    output2 = models_1.predict(scaled_t)

    st.write("The verdict is: Placed and salary is", np.round(output2[0]))
else:
    output = "Not Placed"
    output2 = "Need to work Hard!!"

    st.write("The verdict is:", output, "and", output2)
