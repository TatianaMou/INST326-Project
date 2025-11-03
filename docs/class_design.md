# Class Design Documentation

## Overview
This document explains the architecture and design rationale for the **Medical Symptoms Information Retrieval & Analysis Tool (P02)**.

Our Project 2 goal was to convert the function library from Project 1 into an **object-oriented system**.  
Each class models a key real-world concept from our health-information domain and integrates related Project 1 functions for code reuse and cohesion.

---

## Class List
| Class Name | Purpose | Related Project 1 Functions |
|-------------|----------|-----------------------------|
| `Patient` | Represents a student/patient. Stores identifying information, symptoms, and computes derived data like BMI or age. | `parse_symptom_list`, `build_patient_query`, `generate_patient_summary`, `validate_date`, `validate_severity`, `calculate_age` |
| `Doctor` | Represents a medical professional. Provides identity and formatted output. | *(none – simple encapsulation)* |
| `ConditionSearch` | Handles condition ranking, formatting, and searching of medical notes. | `rank_conditions_basic`, `format_condition_result_card`, `search_notes_and_assignments` |
| `AlertSystem` | Generates red-flag alerts and allergy warnings. | `red_flag_alerts`, `has_allergy_conflict` |
| `RecordsManager` | Stores and searches patient records, tracks query logs, and summarizes results. | `search_patient_records`, `log_search_activity`, `top_ranked_searches`, `summarize_condition_stats` |

---

## Encapsulation and Validation
Each class uses:
- **Private attributes** (e.g., `_firstname`, `_severity`)  
- **Properties** for controlled read/write access  
- **Validation** in constructors and setters to ensure correct data types  
- **Readable representations** via `__str__()` and `__repr__()`

---

## Relationships Between Classes
- A `Patient` creates data consumed by `ConditionSearch` for ranking.
- `AlertSystem` reviews a patient’s symptoms to generate red-flag messages.
- `RecordsManager` stores patients and search histories for later analysis.
- `Doctor` objects may later connect to patients via consultation records (future extension for Project 3).

---

## Design Rationale
We modeled classes after the real workflow of a symptom-checking tool:
1. **Input & storage** → `Patient`, `Doctor`
2. **Processing & retrieval** → `ConditionSearch`
3. **Safety & validation** → `AlertSystem`
4. **Persistence & analytics** → `RecordsManager`

This mirrors information-science principles of data collection, retrieval, filtering, ranking, and decision support.

---

## Future Inheritance (for Project 3)
Potential subclass examples:
- `Specialist(Doctor)` for customized alert logic  
- `PediatricPatient(Patient)` overriding BMI or severity scales  
- `ConditionSearchAdvanced(ConditionSearch)` implementing improved ranking

---

## Summary
These five classes transform the procedural functions from Project 1 into modular, testable, and extensible objects.  
They now provide a clear foundation for inheritance in Project 3.
