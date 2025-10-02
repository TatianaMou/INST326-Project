# Information Retrieval & Analysis Tool — Function Library (P01)

**Course:** INST326 • **Section:** 0201
**Team:** Information Retrieval and Analysis Tool
**Members:** Andrew Koster • Chimezia Okwosha • Darren Esangbedo • Tatiana Moubray

## Overview
This library provides core functions for an Information Retrieval & Analysis Tool that helps students and researchers:
- Search notes, assignments, and question banks by keyword, symptom, or subject.
- Filter results by year or subject.
- Rank results with a simple relevance score.
- Track and display most searched queries for analytics.


These functions form the foundation for future object-oriented development in Project 02.


## Features
- Text cleaning & normalization
- Query parsing (phrases, operators, filters)
- Filtering by subject/year
- Ranking by TF-IDF-lite scoring
- Analytics: frequency tracking and top queries


## Installation
```bash
python -m venv .venv
source .venv/bin/activate # Linux/Mac
.venv\\Scripts\\activate # Windows
pip install -r requirements.txt
