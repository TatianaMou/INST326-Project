import json
from pathlib import Path
from typing import List, Tuple

from .symptom import Symptom
from .condition import Condition


class PersistenceError(Exception):
    pass


def save_state(
    path: Path,
    symptoms: List[Symptom],
    conditions: List[Condition],
) -> Path:
    try:
        data = {
            "symptoms": [s.to_dict() for s in symptoms],
            "conditions": [c.to_dict() for c in conditions],
        }
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
        return path
    except OSError as e:
        raise PersistenceError(f"Failed to save state: {e}") from e


def load_state(path: Path) -> Tuple[List[Symptom], List[Condition]]:
    try:
        with path.open("r", encoding="utf-8") as f:
            data = json.load(f)

        symptoms = [Symptom.from_dict(d) for d in data.get("symptoms", [])]
        conditions = [Condition.from_dict(d) for d in data.get("conditions", [])]
        return symptoms, conditions
    except (OSError, KeyError, TypeError) as e:
        raise PersistenceError(f"Failed to load state: {e}") from e
