Medical Symptoms Information Retrieval & Analysis Tool — Function Library

Course: INST326  
Section: 0201  
Team: Information Retrieval and Analysis Tool  

Members:  
Andrew Koster — Project Manager & Lead Developer  
Chimezia Okwosha — Data Specialist  
Darren Esangbedo — UI/UX Designer  
Tatiana Moubray — Testing & Documentation Lead  

------------------------------------------------------------

Domain Focus and Problem Statement  
Our project focuses on the medical information retrieval domain.  
Students and patients often struggle to interpret their symptoms and determine whether professional help is needed.

We created a function library that allows patients and doctors to:  
- Register patient and doctor information  
- Input symptoms and contextual data  
- Retrieve and rank possible conditions  
- Receive guidance and red-flag alerts on when to seek care  

------------------------------------------------------------

Installation and Setup Instructions  
This project was developed using Python 3 (tested in Google Colab).  
All example data and test calls are contained within the notebook and demo script.

To run locally:  
1. Create a Virutal Environment
python -m venv .venv  
source .venv/bin/activate        # Mac/Linux  
.venv\Scripts\activate           # Windows  

2. Install requirements (no external dependencies)  
pip install -r requirements.txt  

3. Run the demo script 
python examples/demo_script.py  

If you’re using Google Colab, simply open the notebook version and run each cell to test the functions.

------------------------------------------------------------

Usage Examples  
Example of how to import and run the function library:

from src.library_name import *  

Knowledge base for testing  
kb = {"Influenza": {"symptoms": ["fever", "cough", "fatigue"]}}  

Parse and process symptoms  
symptoms = parse_symptom_list("fever, cough")  

Build a sample patient query 
query = build_patient_query("P001", "Ada", "Lovelace", "2000-01-01", "fever, cough", "moderate", 3, ["penicillin"])  

Rank conditions  
ranked = rank_conditions_basic(symptoms, kb)  
print(ranked)  

For more examples, see `docs/usage_examples.md`.

------------------------------------------------------------

Function Library Overview and Organization  
Our source folder (`src/`) includes four key files:

| File | Purpose |
|------|----------|
| irlib.py | Contains all main domain functions (validation, alerts, ranking, search) |
| utils.py | Helper utilities for cleaning text, validating IDs, and formatting output |
| library_name.py | Connects irlib and utils into a single importable library |
| __init__.py | Marks the folder as a package so it can be imported as `src` |

Supporting materials:  
- `docs/function_reference.md` — detailed explanation of every function  
- `docs/usage_examples.md` — runnable code examples for each function  
- `examples/demo_script.py` — shows the full workflow end-to-end  

------------------------------------------------------------

Medical Staff Hierarchy

    classDiagram
    class MedicalStaff {
        <<abstract>>
        - staff_id
        - first_name
        - last_name
        + calculate_daily_tasks()* 
        + display_info()
        + full_name
    }

    class Doctor {
        + calculate_daily_tasks()
        + display_info()
    }

    class Nurse {
        + calculate_daily_tasks()
        + display_info()
    }

    class Surgeon {
        + calculate_daily_tasks()
        + display_info()
    }

    class HospitalDepartment {
        - staff_members : List[MedicalStaff]
        + add_staff()
        + list_staff()
        + show_all_daily_tasks()
    }

    MedicalStaff <|-- Doctor
    MedicalStaff <|-- Nurse
    Doctor <|-- Surgeon
    HospitalDepartment o-- MedicalStaff

    classDiagram
    class PatientProfile {
        <<abstract>>
        + follow_up_window_days()* 
        + risk_score()
        - _base_risk()
    }

    PediatricPatient <|-- PatientProfile
    AdultPatient <|-- PatientProfile
    GeriatricPatient <|-- PatientProfile

Patient Domain Hierarchy
    
     class Registry {
        - patients : Dict
        + add()
        + get()
        + all()
    }

    class AbstractAnalyzer {
        <<abstract>>
        + analyze()* 
    }

    class SymptomAnalyzer {
        + analyze()
    }

    class AllergyConflictAnalyzer {
        + analyze()
    }

    class RiskAnalyzer {
        + analyze()
    }

    class AnalyticsEngine {
        - analyzers : List[AbstractAnalyzer]
        + run()
    }

    Registry o-- PatientProfile
    AnalyticsEngine o-- AbstractAnalyzer
    AbstractAnalyzer <|-- SymptomAnalyzer
    AbstractAnalyzer <|-- RiskAnalyzer
    AbstractAnalyzer <|-- AllergyConflictAnalyzer

------------------------------------------------------------

Usage Guide
This application allows users to analyze possible conditions based on reported symptoms. Users can import datasets, enter symptoms, run analyses, and persist system state between sessions.

Basic Workflow
1. Import or load a dataset of conditions and symptoms
2. Enter one or more symptoms
3. Run the analysis to identify matching conditions
4. Save results or export the summaries

------------------------------------------------------------

Contribution Guidelines  
Each team member completed four functions: one simple, one medium, one complex, and one of their choice.  
All contributions were committed via branches and reviewed through pull requests.  
Consistent PEP 8 style and detailed docstrings were required for every function.  

The original development and testing for this project was done in Google Colab.  
For transparency, the notebook is included here:

- `/Project_01_Functions.ipynb` (authoritative development log)
