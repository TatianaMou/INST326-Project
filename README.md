# Health Information Retrieval & Analysis Tool (INST326)

## Overview
This project is a student-focused health information retrieval system that accepts user symptom input,
retrieves relevant conditions from a structured dataset, ranks likely matches, and supports exporting
and persistence (save/load) between sessions.

**Disclaimer:** This tool is for educational purposes only and does not provide medical advice.

## Team
- Andrew Koster
- Chimezia Okwosha
- Darren Esangbedo
- Tatiana Moubray

## Key Features
- Import knowledge base from CSV or JSON
- Symptom parsing and validation
- Condition ranking with explanations
- Export results to JSON and TXT
- Save/load program state
- Comprehensive tests (unit, integration, system)

## Repository Structure
- `src/` Core application modules
- `tests/` Unit, integration, and system tests
- `demo/` Demo script for end-to-end workflow
- `docs/` Architecture and testing documentation
- `data/` Sample datasets (optional)

## Quick Start
Run the demo:
```bash
python demo/demo_script.py
