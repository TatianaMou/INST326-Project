Usage Examples - Health Information Retrieval Tool 
This document shows short examples of how to use each function from our function library. 
Each example can be run directly in Google Colab or Python

Patient & Data Validation
calculate_age()
print(calculate_age("2000-01-01"))

validate_date()
print(validate_date("2024-03-15"))

validate_severity()
print(validate_severity("moderate"))

extract_year()
print(extract_year("2000-05-03"))

Doctor & Patient Management
input_new_patient()
new_patient = input_new_patient()
print(new_patient)

generate_patient_summary()
patient = {"firstname":"ada","lastname":"lovelace","dob":"2000-01-01","symptoms":["fever","cough"]}
print(generate_patient_summary(patient))

normalize_patient_fields()
print(normalize_patient_fields(" P001 "," Ada "," Lovelace ","2000-01-01"))

input_new_doctor()
new_doctor = input_new_doctor()
print(new_doctor)

doctorinformation()
print(doctorinformation())

Symptom & Query Functions
parse_symptom_list()
symptom_text = "Sore throat, cough, fever"
print(parse_symptom_list(symptom_text))

count_symptoms()
symptoms = ["fever", "cough", "sore throat"]
print(count_symptoms(symptoms))

build_patient_query()
query = build_patient_query("P001","Ada","Lovelace","2000-01-01","Cough, fever","moderate",2,["Penicillin"])
print(query)

Health Alerts
has_allergy_conflict()
print(has_allergy_conflict(["penicillin"], ["amoxicillin"]))

red_flag_alerts()
rules = {"keywords":["chest pain"],"long_duration_days":3,"high_fever_keyword":"fever","high_fever_threshold_days":3}
print(red_flag_alerts(["fever","cough"],4,"moderate",rules))

Condition Retrieval & Ranking
rank_conditions_basic()
kb = {
    "Influenza": {"symptoms":["fever","cough","fatigue"]},
    "Common Cold": {"symptoms":["cough","sore throat","congestion"]}
}
print(rank_conditions_basic(["fever","cough"], kb))

summarize_condition_stats()
print(summarize_condition_stats(["flu","cold","flu"]))

format_condition_result_card()
info = {"self_care":"rest and fluids","seek_care":"if fever lasts 3+ days"}
print(format_condition_result_card("Influenza", ["fever","cough"], 0.6, info))

Search & Analytics
search_patient_records()
records = [
  {"firstname":"Ada","lastname":"Lovelace","notes":"Fever and cough"},
  {"firstname":"Alan","lastname":"Turing","notes":"Headache and fatigue"}
]
print(search_patient_records(records, "fever"))

log_search_activity()
log = ["fever","cold"]
log = log_search_activity(log, "cough")
print(log)

top_ranked_searches()
print(top_ranked_searches(["fever","cold","fever"]))

Prevention & Guidance
suggest_prevention_tips()
rules = {"cough":["cover mouth","stay hydrated"], "fever":["wash hands"]}
print(suggest_prevention_tips(["cough","fever"], rules))
