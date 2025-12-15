# =========================
# FINAL: condition.py
# =========================
from __future__ import annotations
from dataclasses import dataclass
from typing import List, Dict, Any

@dataclass(frozen=True)
class Condition:
    """
    Canonical Condition object used across the system.
    - symptom_keywords is the single source of truth for matching.
    """
    name: str
    symptom_keywords: List[str]
    description: str = "No description provided."
    severity: str = "unknown"

    def matches_symptom(self, symptom_name: str) -> bool:
        s = (symptom_name or "").strip().lower()
        return s in {k.strip().lower() for k in self.symptom_keywords}

    def to_dict(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "description": self.description,
            "symptom_keywords": list(self.symptom_keywords),
            "severity": self.severity,
        }

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> "Condition":
        return Condition(
            name=str(data.get("name", "")).strip(),
            description=str(data.get("description", "No description provided.")),
            symptom_keywords=list(data.get("symptom_keywords", data.get("symptoms", [])) or []),
            severity=str(data.get("severity", "unknown")),
        )
