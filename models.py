class Patient:
    def __init__(
        self,
        full_name,
        dob,
        email,
        glucose,
        haemoglobin,
        cholesterol,
        remarks
    ):
        self.full_name = full_name
        self.dob = dob
        self.email = email
        self.glucose = glucose
        self.haemoglobin = haemoglobin
        self.cholesterol = cholesterol
        self.remarks = remarks