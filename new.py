import streamlit as st
import pickle
import numpy as np

# Load the model
model = pickle.load(open('Sample.pkl', 'rb'))

def predict_diabetes(gender, age, hypertension, heart_disease, smoking_history, bmi, HbA1c_level, blood_glucose_level):
    # Convert inputs to float
    input_data = np.array([[gender, age, hypertension, heart_disease, smoking_history, bmi, HbA1c_level, blood_glucose_level]], dtype=np.float64)
    # Predict probability
    prediction = model.predict_proba(input_data)
    pred = '{0:.{1}f}'.format(prediction[0][1], 2)
    return float(pred)

def main():
    st.title('Diabetes Prediction')
    html_temp = """    
    <div style="background-color:#825246 ;padding:10px">
    <h2 style="color:white;text-align:center;">Diabetes Prediction ML </h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    gender = st.radio("Gender", ["Male", "Female"])  # Use radio buttons instead of text input
    age = st.text_input("Age")
    hypertension = st.text_input("Hypertension")
    heart_disease = st.text_input("Heart Disease")
    smoking_history = st.radio("Smoking History", ["Yes", "No"])  # Use radio buttons instead of text input
    bmi = st.text_input("BMI")
    HbA1c_level = st.text_input("HBA1C_level")
    blood_glucose_level = st.text_input("Blood Glucose")
    
    
    if st.button("Predict"):
        try:
            # Ensure inputs are float (except for gender and smoking history)
            age = float(age)
            hypertension = float(hypertension)
            heart_disease = float(heart_disease)
            bmi = float(bmi)
            HbA1c_level = float(HbA1c_level)
            blood_glucose_level = float(blood_glucose_level)
            
            # Map gender and smoking history to numeric values
            gender_map = {"Male": 1, "Female": 0}
            smoking_map = {"Yes": 1, "No": 0}
            gender = gender_map[gender]
            smoking_history = smoking_map[smoking_history]
            
            # Predict
            output = predict_diabetes(gender, age, hypertension, heart_disease, smoking_history, bmi, HbA1c_level, blood_glucose_level)
            st.success('The probability of having diabetes is {}'.format(output))
            if output>0.5:
                st.error("Diabetes is found")
            else:
                st.success("Diabetes doesn't found")
        except ValueError:
            st.error("Please enter valid numeric values for age, hypertension, BMI, HbA1c level, and blood glucose level.")


if __name__ == '__main__':
    main()
