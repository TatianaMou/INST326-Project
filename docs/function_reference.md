Function Reference - Health Information Retrieval Tool 
This document provides descriptions and usage examples for every function in our Health Information Retrieval system. 

Each functions solves a real problem within our domain, helping students enter, validate, search, and amalyze health data. 

Patient & Data Validation Functions
1. calculate_age(dob)

Calculates age from a patient’s date of birth.

Args: dob (str) — date of birth in "YYYY-MM-DD" format

Returns: int — patient’s age in years

Example:

print(calculate_age("2000-01-01"))

2. validate_date(date_string)

Checks if a date follows the correct format and is valid.

Args: date_string (str)

Returns: True or False

3. validate_severity(severity)

Ensures severity input is one of "mild", "moderate", or "severe".

Returns: Boolean

4. extract_year(date_string)

Pulls the year from a date string.

Example: "2000-05-03" → 2000

Patient Information & Input Functions
5. input_new_patient()

Creates a new patient record.

Uses variables: patientid, firstname, lastname, dob

Adds new patients to your stored list or dictionary.

6. generate_patient_summary(patient)

Returns a one-line summary of a patient’s record.

Args: patient (dict) — includes first name, last name, dob, symptoms

Returns: str

Example:

p = {"firstname":"ada","lastname":"lovelace","dob":"2000-01-01","symptoms":["fever","cough"]}
print(generate_patient_summary(p))

7. normalize_patient_fields(patientid, firstname, lastname, dob)

Formats and cleans basic patient info for consistency.

Returns a dictionary with lowercase, trimmed names.

Doctor Mangement Functions
8. input_new_doctor()

Adds a new doctor to the system.

Uses variables: doctorid, docfirstname, doclastname

9. doctorinformation()

Displays or retrieves information from the doctors dictionary.

Sympton & Query Functions
10. parse_symptom_list(symptom_text)

Cleans a text input of symptoms into a simple list.

Input: "fever, cough, sore throat"

Output: ["fever", "cough", "sore throat"]

11. count_symptoms(symptoms)

Counts how many symptoms the user entered.

Returns: Integer

12. build_patient_query(patientid, firstname, lastname, dob, symptom_text, severity, duration_days, allergies)

Creates a unified dictionary of all patient and symptom information.

Returns: patient_query dictionary

Health Alert Functions
13. has_allergy_conflict(allergies, medications)

Checks if any medication conflicts with known allergies.

Returns: Boolean

14. red_flag_alerts(symptoms, duration_days, severity, alerts_rules)

Identifies warning conditions that suggest professional medical attention.

Returns: List of alert messages

Condition Retrieval & Ranking Functions
15. rank_conditions_basic(symptoms, knowledge_base, top_n)

Ranks possible illnesses based on symptom overlap.

Returns: List of dictionaries with condition name, score, and explanation

16. summarize_condition_stats(conditions)

Counts how often each condition appears in results.

Returns: Dictionary of {condition: count}

17. format_condition_result_card(condition_name, matched, score, info)

Formats ranked results into easy-to-read cards for display

Search & Analytics Functions
18. search_patient_records(records, keyword)

Searches through all patient records for a specific keyword.

Args: list of patient dictionaries, search keyword

Returns: list of matching records

19. top_ranked_searches(log_list)

Shows which searches are most common (requires log of searches).

20. og_search_activity(log_list, query)

Adds a search query to the ongoing search history list.

21. search_notes_and_assignments(query_terms, docs, top_n)

Finds matches in stored student notes or assignments.

Prevention & Guidance Functions
22. suggest_prevention_tips(symptoms, prevention_rules)

Returns a list of prevention or hygiene tips based on entered symptoms.

Utility Functions
23. summarize_condition_stats(conditions)

Counts and summarizes all conditions that appear across searches.

24. generate_patient_summary(patient)

Creates short readable summaries for displaying results.
