"""
library_name.py — Main Function Library Export

Convenience imports for the Health Information Retrieval system.

Usage:
    from src.library_name import *
    # or, to view complexity buckets:
    #   for item in list_functions(): print(item)
"""

from .irlib import (
    validate_date,
    extract_year,
    validate_severity,
    calculate_age,
    count_symptoms,
    normalize_patient_fields,
    input_new_patient,
    input_new_doctor,
    doctorinformation,
    generate_patient_summary,
    parse_symptom_list,
    build_patient_query,
    has_allergy_conflict,
    red_flag_alerts,
    rank_conditions_basic,
    summarize_condition_stats,
    format_condition_result_card,
    search_patient_records,
    log_search_activity,
    top_ranked_searches,
    search_notes_and_assignments,
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

FUNCTION_CATALOG = [
    ("validate_date", "Simple", "irlib"),
    ("extract_year", "Simple", "irlib"),
    ("validate_severity", "Simple", "irlib"),
    ("calculate_age", "Simple", "irlib"),
    ("count_symptoms", "Simple", "irlib"),
    ("clean_text", "Simple", "utils"),
    ("capitalize_name", "Simple", "utils"),
    ("safe_divide", "Simple", "utils"),
    ("average", "Simple", "utils"),
    ("percent", "Simple", "utils"),
    ("is_empty", "Simple", "utils"),
    ("is_valid_id", "Simple", "utils"),
    ("list_to_string", "Simple", "utils"),
    ("normalize_patient_fields", "Simple", "irlib"),
    ("input_new_patient", "Complex", "irlib"),
    ("input_new_doctor", "Simple", "irlib"),
    ("doctorinformation", "Simple", "irlib"),
    ("generate_patient_summary", "Simple", "irlib"),
    ("parse_symptom_list", "Simple", "irlib"),
    ("build_patient_query", "Medium", "irlib"),
    ("has_allergy_conflict", "Simple", "irlib"),
    ("red_flag_alerts", "Medium", "irlib"),
    ("rank_conditions_basic", "Complex", "irlib"),
    ("search_patient_records", "Medium", "irlib"),
    ("summarize_condition_stats", "Simple", "irlib"),
    ("log_search_activity", "Simple", "irlib"),
    ("top_ranked_searches", "Simple", "irlib"),
    ("search_notes_and_assignments", "Complex", "irlib"),
    ("format_condition_result_card", "Medium", "irlib"),
    ("suggest_prevention_tips", "Simple", "irlib"),
]

def list_functions(by_complexity: str | None = None):
    """Return a list of (name, complexity, module) for exported functions."""
    if by_complexity is None:
        return FUNCTION_CATALOG[:]
    wanted = str(by_complexity).strip().capitalize()
    return [t for t in FUNCTION_CATALOG if t[1] == wanted]

__all__ = [
    "validate_date",
    "extract_year",
    "validate_severity",
    "calculate_age",
    "count_symptoms",
    "normalize_patient_fields",
    "input_new_patient",
    "input_new_doctor",
    "doctorinformation",
    "generate_patient_summary",
    "parse_symptom_list",
    "build_patient_query",
    "has_allergy_conflict",
    "red_flag_alerts",
    "rank_conditions_basic",
    "summarize_condition_stats",
    "format_condition_result_card",
    "search_patient_records",
    "log_search_activity",
    "top_ranked_searches",
    "search_notes_and_assignments",
    "suggest_prevention_tips",
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
    "validation_tools",
    "search_tools",
    "alert_tools",
    "utility_tools",
    "FUNCTION_CATALOG",
    "list_functions",
]
