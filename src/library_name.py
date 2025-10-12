"""
=======================================================
 library_name.py — Main Function Library Export
=======================================================

This file connects all major parts of our Health Information
Retrieval system into one easy-to-import module.

Students can import this single file to access all
functions without digging into submodules.

Example:
    from src.library_name import *

    # then call directly
    patient = build_patient_query("P001", "Ada", "Lovelace", "2000-01-01",
                                  "fever, cough", "moderate", 3, ["penicillin"])
    print(rank_conditions_basic(patient["symptoms"], knowledge_base))
"""

# ----------------------------------------------------
# Import everything from our core library and utils
# ----------------------------------------------------

from src.irlib import (
    # validation
    validate_date,
    extract_year,
    validate_severity,
    calculate_age,
    count_symptoms,
    # patient & doctor
    normalize_patient_fields,
    input_new_patient,
    input_new_doctor,
    doctorinformation,
    generate_patient_summary,
    # symptoms & query
    parse_symptom_list,
    build_patient_query,
    # alerts
    has_allergy_conflict,
    red_flag_alerts,
    # condition ranking
    rank_conditions_basic,
    summarize_condition_stats,
    format_condition_result_card,
    # search & analytics
    search_patient_records,
    log_search_activity,
    top_ranked_searches,
    search_notes_and_assignments,
    # prevention
    suggest_prevention_tips
)

from src.utils import (
    clean_text,
    capitalize_name,
    print_divider,
    safe_divide,
    average,
    percent,
    is_empty,
    is_valid_id,
    preview_dict,
    list_to_string
)

# ----------------------------------------------------
# Optional: Create simple grouped dictionaries for easy access
# ----------------------------------------------------

validation_tools = {
    "validate_date": validate_date,
    "extract_year": extract_year,
    "validate_severity": validate_severity,
    "calculate_age": calculate_age
}

search_tools = {
    "rank_conditions_basic": rank_conditions_basic,
    "search_patient_records": search_patient_records,
    "search_notes_and_assignments": search_notes_and_assignments
}

alert_tools = {
    "has_allergy_conflict": has_allergy_conflict,
    "red_flag_alerts": red_flag_alerts
}

utility_tools = {
    "clean_text": clean_text,
    "capitalize_name": capitalize_name,
    "is_valid_id": is_valid_id
}

# ----------------------------------------------------
# End of library_name.py
# ----------------------------------------------------

