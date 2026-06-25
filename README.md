# Health Prediction Application

## Project Overview

Health Prediction Application is a Python-based healthcare management system built using Streamlit, SQLite, and AI integration (Groq API).

The application allows users to:

* Add patient records
* View patient records
* Update patient information
* Delete patient records
* Generate AI-powered health risk predictions based on blood test values

---

## Features

### Patient Management

* Add new patient records
* Store patient details in SQLite database
* View all patient records
* Update existing patient information
* Delete patient records

### Data Validation

* Email format validation
* Date of birth validation
* Required field validation

### AI Health Prediction

The application analyzes:

* Glucose Level
* Haemoglobin Level
* Cholesterol Level

Using AI, it generates health insights and possible risk assessments.

---

## Technologies Used

* Python
* Streamlit
* SQLite
* Groq API (LLM Integration)
* Pandas
* dotenv

---

## Project Structure

health_prediction_app/

├── main.py

├── database.py

├── ai_service.py

├── models.py

├── requirements.txt

├── .gitignore

├── README.md

└── patient.db

---

## Installation

1. Clone the repository

git clone https://github.com/PrachiBangre/health-prediction-app.git

2. Navigate to project folder

cd health-prediction-app

3. Create virtual environment

python -m venv venv

4. Activate virtual environment

Windows:

venv\Scripts\activate

5. Install dependencies

pip install -r requirements.txt

---

## Environment Variables

Create a .env file:

GROQ_API_KEY=your_api_key_here

---

## Run Application

streamlit run main.py

---

## Database

SQLite database is used to store patient information.

Database Table:

patients

Columns:

* id
* full_name
* dob
* email
* glucose
* haemoglobin
* cholesterol
* remarks

---

## Author

Prachi Naresh Bangre

Nagpur, Maharashtra, India
