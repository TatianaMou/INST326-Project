from src.library_functions import (
    validate_date, validate_severity, calculate_age,
    parse_symptom_list, build_patient_query, generate_patient_summary
)

class Patient:
    """Represents a student/patient using the system."""

    def __init__(self, patientid, firstname, lastname, dob, weight_kg=None, height_m=None):
        if not isinstance(patientid, str) or patientid.strip() == "":
            raise ValueError("patientid must be a non-empty string")
        if not isinstance(firstname, str) or not isinstance(lastname, str):
            raise ValueError("firstname/lastname must be strings")
        if not isinstance(dob, str) or not validate_date(dob):
            raise ValueError("dob must be 'YYYY-MM-DD'")

        self._patientid = patientid.strip()
        self._firstname = firstname.strip().lower()
        self._lastname = lastname.strip().lower()
        self._dob = dob.strip()
        self._symptoms = []
        self._allergies = []
        self._severity = "mild"
        self._duration_days = 0
        self._weight_kg = weight_kg if isinstance(weight_kg, (int, float)) or weight_kg is None else None
        self._height_m = height_m if isinstance(height_m, (int, float)) or height_m is None else None

    # Properties
    @property
    def patientid(self): return self._patientid
    @property
    def firstname(self): return self._firstname
    @property
    def lastname(self): return self._lastname
    @property
    def dob(self): return self._dob
    @property
    def symptoms(self): return list(self._symptoms)
    @property
    def allergies(self): return list(self._allergies)

    @property
    def severity(self): return self._severity
    @severity.setter
    def severity(self, value):
        if not isinstance(value, str) or not validate_severity(value):
            raise ValueError("severity must be 'mild', 'moderate', or 'severe'")
        self._severity = value

    @property
    def duration_days(self): return self._duration_days
    @duration_days.setter
    def duration_days(self, value):
        if not isinstance(value, int) or value < 0:
            raise ValueError("duration_days must be an int >= 0")
        self._duration_days = value

    @property
    def weight_kg(self): return self._weight_kg
    @weight_kg.setter
    def weight_kg(self, value):
        if value is not None and (not isinstance(value, (int, float)) or value <= 0):
            raise ValueError("weight_kg must be positive number or None")
        self._weight_kg = value

    @property
    def height_m(self): return self._height_m
    @height_m.setter
    def height_m(self, value):
        if value is not None and (not isinstance(value, (int, float)) or value <= 0):
            raise ValueError("height_m must be positive number or None")
        self._height_m = value

    # Methods
    def add_symptom_text(self, text):
        items = parse_symptom_list(text)
        for s in items:
            if s not in self._symptoms:
                self._symptoms.append(s)

    def add_allergies(self, items):
        if not isinstance(items, list):
            raise ValueError("allergies must be a list")
        for a in items:
            if isinstance(a, str):
                a2 = a.strip().lower()
                if a2 and a2 not in self._allergies:
                    self._allergies.append(a2)

    def age(self, today="2025-10-12"):
        return calculate_age(self._dob, today=today)

    def bmi(self):
        if self._weight_kg and self._height_m:
            return self._weight_kg / (self._height_m * self._height_m)
        return None

    def to_query(self):
        symptom_text = ", ".join(self._symptoms)
        return build_patient_query(
            self._patientid, self._firstname, self._lastname, self._dob,
            symptom_text, self._severity, self._duration_days, self._allergies
        )

    def summary(self):
        data = {"firstname": self._firstname, "lastname": self._lastname, "dob": self._dob, "symptoms": list(self._symptoms)}
        return generate_patient_summary(data)

    def __str__(self):
        return f"{self._firstname.capitalize()} {self._lastname.capitalize()} (ID: {self._patientid})"

    def __repr__(self):
        return f"Patient(patientid='{self._patientid}', firstname='{self._firstname}', lastname='{self._lastname}', dob='{self._dob}')"
