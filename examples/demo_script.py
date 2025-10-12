"""
=======================================================
 Health Information Retrieval Tool — Demo Script
=======================================================

This script demonstrates how to use our function library
for the "Student Symptom Self-Diagnosis" project.

It shows:
- Parsing user symptom input
- Building a patient query
- Ranking likely conditions
- Showing red flag alerts
- Searching patient records
- Tracking search history
- Displaying summaries and statistics
"""

# ----------------------------------------------------
# Import functions from the library (adjust path as needed)
# ----------------------------------------------------
from src.irlib import (
    parse_symptom_list,
    build_patient_query,
    rank_conditions_basic,
    red_flag_alerts,
    generate_patient_summary,
    search_patient_records,
    log_search_activity,
    summarize_condition_stats,
    suggest_prevention_tips
)

# ----------------------------------------------------
# Step 1. Example Knowledge Base and Rules
# ----------------------------------------------------
knowledge_base = {
    "Influenza": {
        "symptoms": ["fever", "cough", "fatigue", "sore throat"],
        "self_care": "Rest, fluids, and over-the-counter medicine.",
        "seek_care": "If fever lasts more than 3 days or breathing problems occur."
    },
    "Common Cold": {
        "symptoms": ["cough", "sore throat", "congestion"],
        "self_care": "Stay hydrated and get enough sleep.",
        "seek_care": "If symptoms persist for more than a week."
    },
    "Migraine": {
        "symptoms": ["headache", "nausea", "light sensitivity"],
        "self_care": "Rest in a dark room and avoid loud noise."
    }
}

alerts_rules = {
    "keywords": ["chest pain", "shortness of breath"],
    "long_duration_days": 3,
    "high_fever_keyword": "fever",
    "high_fever_threshold_days": 3
}

# ----------------------------------------------------
# Step 2. Simulated Patient Input
# ----------------------------------------------------
symptom_text = "Fever, cough"
symptoms = parse_symptom_list(symptom_text)

patient_query = build_patient_query(
    patientid="P001",
    firstname="Ada",
    lastname="Lovelace",
    dob="2000-01-01",
    symptom_text=symptom_text,
    severity="moderate",
    duration_days=4,
    allergies=["penicillin"]
)

# ----------------------------------------------------
# Step 3. Rank Conditions
# ----------------------------------------------------
ranked = rank_conditions_basic(symptoms, knowledge_base, top_n=3)

# ----------------------------------------------------
# Step 4. Generate Alerts
# ----------------------------------------------------
alerts = red_flag_alerts(symptoms, 4, "moderate", alerts_rules)

# ----------------------------------------------------
# Step 5. Display Results
# ----------------------------------------------------
print("\n=======================================================")
print(" PATIENT SUMMARY")
print("=======================================================\n")
print(generate_patient_summary(patient_query))
print()

print("=======================================================")
print(" CONDITION RANKING RESULTS")
print("=======================================================\n")
for item in ranked:
    print(f"{item['condition']} - Score: {round(item['score'],2)}")
    print("Matched:", ", ".join(item["matched"]))
    print("Explanation:", item["explanation"])
    print()

print("=======================================================")
print(" ALERT MESSAGES")
print("=======================================================\n")
if len(alerts) == 0:
    print("No red-flag alerts detected.")
else:
    for alert in alerts:
        print("-", alert)
print()

# ----------------------------------------------------
# Step 6. Search Records & Track Activity
# ----------------------------------------------------
records = [
    {"firstname": "Ada", "lastname": "Lovelace", "notes": "Fever and cough"},
    {"firstname": "Alan", "lastname": "Turing", "notes": "Headache and fatigue"}
]
search_results = search_patient_records(records, "fever")

print("=======================================================")
print(" PATIENT RECORD SEARCH")
print("=======================================================\n")
for result in search_results:
    print(result)
print()

log_list = ["fever", "cold"]
log_list = log_search_activity(log_list, "cough")

print("Search Log:", log_list)
print()

# ----------------------------------------------------
# Step 7. Condition Statistics & Prevention Tips
# ----------------------------------------------------
conditions = ["influenza", "cold", "influenza"]
stats = summarize_condition_stats(conditions)
print("Condition Counts:", stats)

rules = {
    "cough": ["cover your mouth when coughing", "stay hydrated"],
    "fever": ["wash your hands often", "avoid close contact"]
}
tips = suggest_prevention_tips(symptoms, rules)

print("\n=======================================================")
print(" PREVENTION TIPS")
print("=======================================================\n")
for t in tips:
    print("-", t)

# ----------------------------------------------------
# End of Demo
# ----------------------------------------------------
print("\nDemo complete. All core functions have been successfully demonstrated.")

