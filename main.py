import streamlit as st
import pandas as pd
import re
from datetime import date

from database import (
    create_table,
    add_patient,
    get_patients,
    update_patient,
    delete_patient
    )


from ai_service import predict_health

# Create database table
create_table()

# Validation Function FOR EMAIL AND DOB

def validate_inputs(full_name, email, dob):

    if not full_name:
        return False, "Full name is required"

    email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'

    if not re.match(email_pattern, email):
        return False, "Invalid email address"

    if dob > date.today():
        return False, "Date of birth cannot be in the future"

    return True, ""


# Page Configuration
st.set_page_config(
    page_title="Health Prediction App",
    page_icon="🩺",
    layout="wide"
)

# CREATE PATIENT

st.header("Add Patient")

full_name = st.text_input("Full Name")

dob = st.date_input(
    "Date of Birth",
    value=date(2000, 1, 1),
    min_value=date(1900, 1, 1),
    max_value=date.today()
)

email = st.text_input("Email Address")

glucose = st.number_input(
    "Glucose",
    min_value=0.0,
    value=0.0,
    step=1.0
)

haemoglobin = st.number_input(
    "Haemoglobin",
    min_value=0.0,
    value=0.0,
    step=1.0
)

cholesterol = st.number_input(
    "Cholesterol",
    min_value=0.0,
    value=0.0,
    step=1.0
)

if st.button("Save"):

    valid, message = validate_inputs(
        full_name,
        email,
        dob
    )

    if not valid:
        st.error(message)

    else:

        remarks = predict_health(
            glucose,
            haemoglobin,
            cholesterol
        )

        add_patient(
            full_name,
            str(dob),
            email,
            glucose,
            haemoglobin,
            cholesterol,
            remarks
        )

        st.success("Patient saved successfully")


# READ PATIENTS

st.header("Patient Records")

records = get_patients()

df = pd.DataFrame(
    records,
    columns=[
        "ID",
        "Full Name",
        "DOB",
        "Email",
        "Glucose",
        "Haemoglobin",
        "Cholesterol",
        "Remarks"
    ]
)

st.dataframe(
    df,
    use_container_width=True
)


# UPDATE PATIENT
st.header("Update Patient")

update_id = st.number_input(
    "Patient ID",
    min_value=1,
    step=1,
    key="update_id"
)

update_name = st.text_input(
    "New Full Name",
    key="update_name"
)

update_dob = st.date_input(
    "New Date of Birth",
    value=date(2000, 1, 1),
    min_value=date(1900, 1, 1),
    max_value=date.today(),
    key="update_dob"
)

update_email = st.text_input(
    "New Email Address",
    key="update_email"
)

update_glucose = st.number_input(
    "New Glucose",
    min_value=0.0,
    key="update_glucose"
)

update_haemoglobin = st.number_input(
    "New Haemoglobin",
    min_value=0.0,
    key="update_haemoglobin"
)

update_cholesterol = st.number_input(
    "New Cholesterol",
    min_value=0.0,
    key="update_cholesterol"
)

if st.button("Update Patient"):

    valid, message = validate_inputs(
        update_name,
        update_email,
        update_dob
    )

    if not valid:
        st.error(message)

    else:

        remarks = predict_health(
            update_glucose,
            update_haemoglobin,
            update_cholesterol
        )

        update_patient(
            update_id,
            update_name,
            str(update_dob),
            update_email,
            update_glucose,
            update_haemoglobin,
            update_cholesterol,
            remarks
        )

        st.success("Patient updated successfully")


# DELETE PATIENT

st.header("Delete Patient")

delete_id = st.number_input(
    "Patient ID to Delete",
    min_value=1,
    step=1,
    key="delete_id"
)

if st.button("Delete Patient"):

    delete_patient(delete_id)

    st.success("Patient deleted successfully")
