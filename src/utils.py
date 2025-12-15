from typing import Dict, Any, List

from .condition import Condition


def kb_to_conditions(kb: Dict[str, Dict[str, Any]]) -> List[Condition]:
    """
    Convert a normalized knowledge base dictionary into Condition objects.

    Expected kb format:
    {
        "Influenza": {
            "symptoms": ["fever", "cough"],
            "self_care": "...",
            "seek_care": "..."
        },
        ...
    }

    Returns:
        List[Condition]
    """
    if not isinstance(kb, dict):
        raise TypeError("Knowledge base must be a dictionary")

    conditions: List[Condition] = []

    for name, info in kb.items():
        if not isinstance(info, dict):
            continue

        symptoms = info.get("symptoms", [])
        if not isinstance(symptoms, list) or not symptoms:
            continue

        condition = Condition(
            name=str(name).strip(),
            symptom_keywords=[str(s).strip().lower() for s in symptoms if str(s).strip()],
            description=str(info.get("self_care", "")).strip() or "No description provided.",
            severity="unknown",
        )

        conditions.append(condition)

    if not conditions:
        raise ValueError("Knowledge base produced no valid Condition objects")

    return conditions
