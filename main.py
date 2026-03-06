# main.py

import streamlit as st
import pandas as pd
import pickle

st.title("Classification Model")
st.write("Will they hire an attorney?")

# -------------------------
# Create Input Form
# -------------------------
def create_page():

    st.sidebar.title("Enter Client Details")

    age = st.sidebar.slider("Age", min_value=18, max_value=100)

    sex = st.sidebar.radio("Gender", ["Male", "Female"])

    seat = st.sidebar.checkbox("Seatbelt Worn")

    insur = st.sidebar.selectbox("Life Insurance", ["Yes", "No"])

    amt = st.sidebar.number_input("Enter claim amount", min_value=0.0)

    # Convert categorical to numeric
    sex = 1 if sex == "Male" else 0
    insur = 1 if insur == "Yes" else 0
    seat = 1 if seat else 0

    # Create dataframe
    data = {
        "CLMSEX": sex,
        "CLMINSUR": insur,
        "SEATBELT": seat,
        "CLMAGE": age,
        "LOSS": amt
    }

    inp_df = pd.DataFrame(data, index=[0])
    return inp_df


# Get features
features = create_page()

# -------------------------
# Prediction
# -------------------------
if st.sidebar.button("Submit"):

    try:
        # Load trained model
        model = pickle.load(open("clf.pkl", "rb"))

        # Predict
        res = model.predict(features)

        if res[0] == 0:
            st.success("NO, they will NOT hire an attorney")
        else:
            st.success("YES, they WILL hire an attorney")

    except FileNotFoundError:
        st.error("Model file 'clf.pkl' not found. Make sure it is in the same folder.")