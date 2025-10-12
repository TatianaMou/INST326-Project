"""
library_name.py — Main Function Library Export

Convenience imports for the Health Information Retrieval system.
Usage:
    from src.library_name import *
"""

from .irlib import (
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
    # condition ranking / stats / display
    rank_conditions_basic,
    summarize_condition_stats,
    format_condition_result_card,
    # search & analytics
    search_patient_records,
    log_search_activity,
    top_ranked_searches,
    search_notes_and_assignments,
    # prevention
    suggest_prevention_tips,
)

from .utils import (
    clean_text,
    capitalize_name,
    print_divider,
    safe_divide,
    average,
    percent,
    is_empty,
    is_valid_id,
    preview_dict,
    list_to_string,
)

validation_tools = {
    "validate_date": validate_date,
    "extract_year": extract_year,
    "validate_severity": validate_severity,
    "calculate_age": calculate_age,
}

search_tools = {
    "rank_conditions_basic": rank_conditions_basic,
    "search_patient_records": search_patient_records,
    "search_notes_and_assignments": search_notes_and_assignments,
}

alert_tools = {
    "has_allergy_conflict": has_allergy_conflict,
    "red_flag_alerts": red_flag_alerts,
}

utility_tools = {
    "clean_text": clean_text,
    "capitalize_name": capitalize_name,
    "is_valid_id": is_valid_id,
}

__all__ = [
    # validation
    "validate_date",
    "extract_year",
    "validate_severity",
    "calculate_age",
    "count_symptoms",
    # patient & doctor
    "normalize_patient_fields",
    "input_new_patient",
    "input_new_doctor",
    "doctorinformation",
    "generate_patient_summary",
    # symptoms & query
    "parse_symptom_list",
    "build_patient_query",
    # alerts
    "has_allergy_conflict",
    "red_flag_alerts",
    # condition ranking / stats / display
    "rank_conditions_basic",
    "summarize_condition_stats",
    "format_condition_result_card",
    # search & analytics
    "search_patient_records",
    "log_search_activity",
    "top_ranked_searches",
    "search_notes_and_assignments",
    # prevention
    "suggest_prevention_tips",
    # utils
    "clean_text",
    "capitalize_name",
    "print_divider",
    "safe_divide",
    "average",
    "percent",
    "is_empty",
    "is_valid_id",
    "preview_dict",
    "list_to_string",
    # grouped tool maps
    "validation_tools",
    "search_tools",
    "alert_tools",
    "utility_tools",
]
