# API Reference

This file summarizes each class, its constructor parameters, properties, and key methods.

---

## Class: Patient
**Purpose:** Represents a student or patient profile.

**Constructor**
```python
Patient(patientid, firstname, lastname, dob, weight_kg=None, height_m=None)
Key Properties

patientid, firstname, lastname, dob

symptoms, allergies, severity, duration_days

weight_kg, height_m

Methods

add_symptom_text(text) – Parse and store symptoms.

add_allergies(items) – Add allergies from a list.

age(today) – Calculate approximate age.

bmi() – Return BMI if height and weight available.

to_query() – Build dictionary query for searches.

summary() – Generate readable patient summary.

Class: Doctor
Purpose: Represents a doctor.

Constructor

python
Copy code
Doctor(doctorid, docfirstname, doclastname)
Properties

doctorid, docfirstname, doclastname

Methods

full_name() – Return "Firstname Lastname".

Standard __str__() and __repr__() for readable output.

Class: ConditionSearch
Purpose: Performs ranking and formatting of possible conditions.

Constructor

python
Copy code
ConditionSearch(knowledge_base=None)
Methods

rank(symptoms, top_n=5) – Return ranked list of conditions.

as_cards(ranked_items) – Format ranked results for display.

search_notes(query_terms, docs, top_n=5) – Keyword search across notes.

Class: AlertSystem
Purpose: Checks for medical red-flags and allergy conflicts.

Constructor

python
Copy code
AlertSystem(alerts_rules=None)
Methods

check(symptoms, duration_days, severity) – Return list of alert messages.

allergy_conflict(allergies, medications) – True if overlap found.

update_rules(new_rules) – Replace internal rule dictionary.

Class: RecordsManager
Purpose: Manage stored patient records and query logs.

Constructor

python
Copy code
RecordsManager()
Methods

add_record(record_dict) – Append new record.

search(keyword) – Search across records.

log_query(query) – Add to search log.

top_queries() – Return most frequent queries.

condition_counts(conditions) – Summarize condition frequencies.

Example Usage
python
Copy code
from src.patient import Patient
from src.condition_search import ConditionSearch
from src.alert_system import AlertSystem

kb = {"Flu": {"symptoms": ["fever","cough"], "self_care": "Rest"}}
rules = {"keywords": ["chest pain"], "long_duration_days": 3}

p = Patient("P001", "Ada", "Lovelace", "2000-01-01", weight_kg=60, height_m=1.65)
p.add_symptom_text("fever, cough")
engine = ConditionSearch(kb)
alerts = AlertSystem(rules)

ranked = engine.rank(p.symptoms)
print(ranked)
print(alerts.check(p.symptoms, 4, "moderate"))
