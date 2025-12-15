from typing import List


class Symptom:
    """
    Represents a user-provided symptom.
    """
    def __init__(self, name: str, severity: int = 1):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Symptom name must be a non-empty string")
        if not isinstance(severity, int) or not 1 <= severity <= 5:
            raise ValueError("Severity must be an integer between 1 and 5")

        self.name = name.strip().lower()
        self.severity = severity

    def to_dict(self) -> dict:
        return {"name": self.name, "severity": self.severity}

    @classmethod
    def from_dict(cls, data: dict) -> "Symptom":
        return cls(data["name"], data.get("severity", 1))

    def __repr__(self) -> str:
        return f"Symptom(name='{self.name}', severity={self.severity})"


def parse_symptoms(symptom_input: str) -> List[Symptom]:
    """
    Parse comma-separated symptom text into Symptom objects.
    """
    if not isinstance(symptom_input, str):
        raise TypeError("Symptom input must be a string")

    if not symptom_input.strip():
        return []

    symptoms: List[Symptom] = []
    for token in symptom_input.split(","):
        token = token.strip()
        if token:
            symptoms.append(Symptom(token))
    return symptoms
