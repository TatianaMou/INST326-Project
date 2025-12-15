def _normalize_text(x: Any) -> str:
    if x is None:
        return ""
    # Support Symptom objects that have `.name`
    if hasattr(x, "name"):
        x = getattr(x, "name")
    if not isinstance(x, str):
        x = str(x)
    return x.strip().lower()

# =========================
# FINAL: analyzer.py
# =========================
from __future__ import annotations
from typing import Any, Dict, List, Tuple, Union

# expects Condition from the FINAL condition cell
# from condition import Condition

def _normalize_text(x: Any) -> str:
    if x is None:
        return ""
    # Support Symptom objects that have `.name`
    if hasattr(x, "name"):
        x = getattr(x, "name")
    if not isinstance(x, str):
        x = str(x)
    return x.strip().lower()

class Analyzer:
    """
    Symptom -> Condition analyzer.
    Accepts:
      - list[str] symptoms OR
      - list[Symptom] objects (anything with .name)
    """
    def __init__(self, conditions: List["Condition"]) -> None:
        if not isinstance(conditions, list) or not conditions:
            raise ValueError("conditions must be a non-empty list of Condition objects")
        self._conditions = conditions

    def analyze(self, user_symptoms: List[Union[str, Any]], top_n: int = 5) -> Dict[str, Any]:
        if not isinstance(user_symptoms, list):
            raise ValueError("user_symptoms must be a list")

        normalized = [_normalize_text(s) for s in user_symptoms]
        normalized = [s for s in normalized if s]
        if not normalized:
            return {"input_symptoms": [], "ranked_conditions": []}

        user_set = set(normalized)
        ranked: List[Tuple[float, Dict[str, Any]]] = []

        for cond in self._conditions:
            keywords = [_normalize_text(k) for k in cond.symptom_keywords if k]
            if not keywords:
                continue

            keyword_set = set(keywords)
            matched = sorted(user_set.intersection(keyword_set))
            unmatched = sorted(keyword_set.difference(user_set))

            proportion = len(matched) / max(1, len(keyword_set))
            score = proportion + (0.01 * len(matched))

            ranked.append((
                score,
                {
                    "condition": cond.name,
                    "score": round(score, 4),
                    "matched_symptoms": matched,
                    "unmatched_keywords": unmatched,
                    "description": cond.description,
                    "severity": getattr(cond, "severity", "unknown"),
                }
            ))

        ranked.sort(key=lambda x: x[0], reverse=True)
        results = [item for _, item in ranked[: max(0, int(top_n))]]

        return {"input_symptoms": sorted(user_set), "ranked_conditions": results}
