Medical Symptoms Information Retrieval & Analysis Tool — Function Library (P01)

Course: INST326
Section: 0201
Team: Information Retrieval and Analysis Tool
Members:

Andrew Koster — Project Manager & Lead Developer

Chimezia Okwosha — Data Specialist

Darren Esangbedo — UI/UX Designer

Tatiana Moubray — Testing & Documentation Lead

Domain Focus and Problem Statement

Our project focuses on the medical information retrieval domain.
Students and patients often struggle to interpret their symptoms and determine whether professional help is needed.

We created a function library that allows patients and doctors to:

Register patient and doctor information,

Input symptoms and contextual data,

Retrieve and rank possible conditions,

Receive guidance and red-flag alerts on when to seek care.

This function library forms the foundation for Project 2, where the same logic will be turned into object-oriented classes.

Installation and Setup Instructions

This project was developed using Python 3 (tested in Google Colab).
All example data and test calls are contained within the notebook and demo script.

To run locally:

# 1. Create a virtual environment
python -m venv .venv
source .venv/bin/activate        # Mac/Linux
.venv\Scripts\activate           # Windows

# 2. Install requirements (no external dependencies)
pip install -r requirements.txt

# 3. Run the demo script
python examples/demo_script.py


If you’re using Google Colab, simply open the notebook version and run each cell to test the functions.

Usage Examples

Example of how to import and run the function library:

from src.library_name import *

# Knowledge base for testing
kb = {"Influenza": {"symptoms": ["fever","cough","fatigue"]}}

# Parse and process symptoms
symptoms = parse_symptom_list("fever, cough")
query = build_patient_query("P001","Ada","Lovelace","2000-01-01","fever, cough","moderate",3,["penicillin"])

# Rank conditions
ranked = rank_conditions_basic(symptoms, kb)
print(ranked)


For more examples, see
docs/usage_examples.md

Function Library Overview and Organization

Our source folder (src/) includes four key files:

File	Purpose
irlib.py	Contains all main domain functions (validation, alerts, ranking, search).
utils.py	Helper utilities for cleaning text, validating IDs, and formatting output.
library_name.py	Connects irlib and utils into a single importable library.
__init__.py	Marks the folder as a package so it can be imported as src.

Supporting materials:

docs/function_reference.md — detailed explanation of every function.

docs/usage_examples.md — runnable code examples for each function.

examples/demo_script.py — shows the full workflow end-to-end.

Contribution Guidelines

Each team member completed four functions: one simple, one medium, one complex, and one of their choice.

All contributions were committed via branches and reviewed through pull requests.

Consistent PEP 8 style and detailed docstrings were required for every function.

Each teammate documented their individual work in the AI Collaboration Journal.

Project Summary

The final library now includes 17 domain-relevant functions that together handle:

Input and validation

Symptom parsing and condition ranking

Red-flag alerts and prevention tips

Search, analytics, and summarization

This codebase demonstrates Information Science principles of retrieval, filtering, ranking, and decision-support.
It serves as the foundation for the next stage of the project — developing an object-oriented system that uses these functions as class methods.
