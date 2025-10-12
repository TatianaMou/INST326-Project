"""
=======================================================
 Health Information Retrieval Tool — Function Library
=======================================================

"""

def _to_lower_list(items):
    out = []
    if not isinstance(items, list):
        return out
    for x in items:
        if isinstance(x, str):
            s = x.strip().lower()
            if s:
                out.append(s)
    return out


def validate_date(date_string):
    """Very basic date check 'YYYY-MM-DD' (no calendar logic)."""
    if not isinstance(date_string, str):
        return False
    parts = date_string.split("-")
    if len(parts) != 3:
        return False
    if len(parts[0]) != 4 or len(parts[1]) != 2 or len(parts[2]) != 2:
        return False
    try:
        y = int(parts[0]); m = int(parts[1]); d = int(parts[2])
    except ValueError:
        return False
    if y < 1900 or m < 1 or m > 12 or d < 1 or d > 31:
        return False
    return True


def extract_year(date_string):
    """Return the year as int from 'YYYY-MM-DD'; 0 if invalid."""
    if not validate_date(date_string):
        return 0
    return int(date_string.split("-")[0])


def validate_severity(severity):
    """Return True if severity is 'mild', 'moderate', or 'severe'."""
    return severity in ["mild", "moderate", "severe"]


def calculate_age(dob, today="2025-10-12"):
    """Very rough age (year difference only)."""
    if not (validate_date(dob) and validate_date(today)):
        return 0
    y1 = extract_year(dob)
    y2 = extract_year(today)
    return max(0, y2 - y1)


def count_symptoms(symptoms):
    """Return number of symptoms (list length)."""
    if not isinstance(symptoms, list):
        return 0
    return len(symptoms)


def normalize_patient_fields(patientid, firstname, lastname, dob):
    """Return normalized patient dict (lowercased names, trimmed)."""
    if not all(isinstance(x, str) for x in [patientid, firstname, lastname, dob]):
        print("All patient fields must be strings.")
        return {}
    return {
        "patie
