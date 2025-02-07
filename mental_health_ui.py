import streamlit as st
import joblib
import numpy as np

# Load the trained model
model_filename = "best_model.joblib"
best_model = joblib.load(model_filename)

# Define feature columns
feature_cols = ['Age', 'Gender', 'family_history', 'benefits', 'care_options', 'anonymity', 'leave', 'work_interfere']

def predict_anxiety_level(features):
    prob = best_model.predict_proba([features])[0][1]  # Get probability of needing treatment
    anxiety_level = int(round(prob * 10))  # Scale to 1-10
    return best_model.predict([features])[0], anxiety_level

# Streamlit UI
st.title("Mental Health Prediction")
st.write("Fill in the details to predict mental health treatment need and anxiety level.")

# User input fields
age = st.slider("Age", 18, 65, 25)
gender = st.selectbox("Gender", ["male", "female", "trans"])
family_history = st.selectbox("Family History of Mental Illness", ["Yes", "No"])
benefits = st.selectbox("Does your employer provide mental health benefits?", ["Yes", "No"])
care_options = st.selectbox("Do you know the care options provided by your employer?", ["Yes", "No", "Not Sure"])
anonymity = st.selectbox("Is anonymity protected if you seek mental health treatment?", ["Yes", "No", "Not Sure"])
leave = st.selectbox("Ease of taking mental health leave", ["Very Easy", "Somewhat Easy", "Neutral", "Somewhat Difficult", "Very Difficult"])
work_interfere = st.selectbox("Does mental health interfere with work?", ["Never", "Rarely", "Sometimes", "Often", "Always"])

# Encode categorical inputs
encoding_dict = {
    "gender": {"male": 0, "female": 1, "trans": 2},
    "family_history": {"No": 0, "Yes": 1},
    "benefits": {"No": 0, "Yes": 1},
    "care_options": {"No": 0, "Yes": 1, "Not Sure": 2},
    "anonymity": {"No": 0, "Yes": 1, "Not Sure": 2},
    "leave": {"Very Easy": 0, "Somewhat Easy": 1, "Neutral": 2, "Somewhat Difficult": 3, "Very Difficult": 4},
    "work_interfere": {"Never": 0, "Rarely": 1, "Sometimes": 2, "Often": 3, "Always": 4},
}

features = [
    age,
    encoding_dict["gender"][gender],
    encoding_dict["family_history"][family_history],
    encoding_dict["benefits"][benefits],
    encoding_dict["care_options"][care_options],
    encoding_dict["anonymity"][anonymity],
    encoding_dict["leave"][leave],
    encoding_dict["work_interfere"][work_interfere]
]

if st.button("Predict"):
    prediction, anxiety_level = predict_anxiety_level(features)
    st.subheader("Prediction Result:")
    if prediction == 1:
        st.write("The model predicts that mental health treatment is needed.")
    else:
        st.write("The model predicts that mental health treatment is not needed.")
    
    st.subheader("Anxiety Level:")
    st.write(f"Anxiety Level (1-10): {anxiety_level}")
    st.progress(anxiety_level / 10)
