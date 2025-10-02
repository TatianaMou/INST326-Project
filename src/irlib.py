"""Information Retrieval & Analysis Tool — Function Library (P01)
Run doctests:
    python -m doctest -v src/irlib.py
"""
from __future__ import annotations
from typing import Any
import re
from collections import Counter

Doc = dict[str, Any]

# -------------------- Simple functions --------------------

def normalize_text(text: str) -> str:
    """Lowercase and collapse whitespace.

    Examples:
        >>> normalize_text("  Fever  AND  Cough ")
        'fever and cough'
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    return " ".join(text.split()).lower()


def validate_symptom_input(symptom: str) -> bool:
    """Return True if symptom looks like a valid term.

    Examples:
        >>> validate_symptom_input("fever")
        True
        >>> validate_symptom_input("   ")
        False
    """
    if not isinstance(symptom, str):
        raise TypeError("symptom must be a string")
    s = symptom.strip()
    return bool(s) and bool(re.search(r"[A-Za-z]", s))


def filter_by_year(docs: list[Doc], year: int) -> list[Doc]:
    """Filter documents by exact year.

    Examples:
        >>> docs = [{"id":"1","year":2024},{"id":"2","year":2023}]
        >>> [d['id'] for d in filter_by_year(docs, 2024)]
        ['1']
    """
    return [d for d in docs if d.get("year") == year]

# -------------------- Medium functions --------------------

def parse_search_query(q: str) -> dict:
    """Parse a query into terms and filters.

    Examples:
        >>> parse_search_query('"chest pain" fever year:2024')
        {'terms': ['fever'], 'phrases': ['chest pain'], 'filters': {'year': 2024}}
    """
    terms, phrases, filters = [], [], {}
    tokens = q.split()
    for t in tokens:
        if t.startswith('"') and t.endswith('"'):
            phrases.append(t.strip('"'))
        elif t.startswith("year:"):
            try:
                filters["year"] = int(t.split(":")[1])
            except ValueError:
                pass
        else:
            terms.append(t)
    return {"terms": terms, "phrases": phrases, "filters": filters}

# -------------------- Complex functions --------------------

def rank_documents(query: str, corpus: list[Doc], top_k: int = 5) -> list[tuple[Doc, float]]:
    """Rank docs by simple frequency overlap.

    Examples:
        >>> corpus = [{'id':'1','body':'fever and cough'}, {'id':'2','body':'headache'}]
        >>> [d['id'] for d,_ in rank_documents('fever', corpus)]
        ['1']
    """
    q = parse_search_query(query)
    q_terms = [t.lower() for t in q["terms"]]
    scored = []
    for d in corpus:
        text = (d.get("title","") + " " + d.get("body","")).lower()
        score = sum(text.count(t) for t in q_terms)
        scored.append((d, score))
    return sorted(scored, key=lambda x: x[1], reverse=True)[:top_k]
