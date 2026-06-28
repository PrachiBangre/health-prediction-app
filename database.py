import sqlite3

def create_table():
    conn = sqlite3.connect("patient.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS patients(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        full_name TEXT,
        dob TEXT,
        email TEXT,
        glucose REAL,
        haemoglobin REAL,
        cholesterol REAL,
        remarks TEXT
    )
    """)

    conn.commit()
    conn.close()


def patient_exists(full_name, dob, email):

    conn = sqlite3.connect("patient.db")
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT * FROM patients
        WHERE full_name=? AND dob=? AND email=?
        """,
        (full_name, dob, email)
    )

    record = cursor.fetchone()

    conn.close()

    return record is not None

def add_patient(
        full_name,
        dob,
        email,
        glucose,
        haemoglobin,
        cholesterol,
        remarks):

    conn = sqlite3.connect("patient.db")
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO patients
    (full_name,dob,email,glucose,haemoglobin,cholesterol,remarks)
    VALUES (?,?,?,?,?,?,?)
    """,
    (
        full_name,
        dob,
        email,
        glucose,
        haemoglobin,
        cholesterol,
        remarks
    ))

    conn.commit()
    conn.close()


def get_patients():

    conn = sqlite3.connect("patient.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM patients ORDER BY id")

    records = cursor.fetchall()

    conn.close()

    return records

def update_patient(
        patient_id,
        full_name,
        dob,
        email,
        glucose,
        haemoglobin,
        cholesterol,
        remarks):

    conn = sqlite3.connect("patient.db")
    cursor = conn.cursor()

    cursor.execute("""
    UPDATE patients
    SET
        full_name=?,
        dob=?,
        email=?,
        glucose=?,
        haemoglobin=?,
        cholesterol=?,
        remarks=?
    WHERE id=?
    """,
    (
        full_name,
        dob,
        email,
        glucose,
        haemoglobin,
        cholesterol,
        remarks,
        patient_id
    ))

    conn.commit()
    conn.close()


def delete_patient(patient_id):

    conn = sqlite3.connect("patient.db")
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM patients WHERE id=?",
        (patient_id,)
    )

    conn.commit()
    conn.close()