import csv
import json
from pathlib import Path
from typing import Dict, Any


class DataRetriever:
    """
    Loads and normalizes condition datasets from CSV or JSON files.
    """

    def __init__(self):
        self.errors: list[str] = []

    def load_knowledge_base(self, path: Path) -> Dict[str, Dict[str, Any]]:
        if not isinstance(path, Path):
            raise TypeError("path must be a pathlib.Path")

        if not path.exists():
            raise FileNotFoundError(f"File not found: {path}")

        suffix = path.suffix.lower()
        if suffix == ".csv":
            return self._load_csv(path)
        elif suffix == ".json":
            return self._load_json(path)
        else:
            raise ValueError("Unsupported file type (must be CSV or JSON)")

    def _load_csv(self, path: Path) -> Dict[str, Dict[str, Any]]:
        kb: Dict[str, Dict[str, Any]] = {}

        with path.open("r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                name = row.get("condition", "").strip()
                if not name:
                    self.errors.append("Missing condition name")
                    continue

                symptoms = [
                    s.strip().lower()
                    for s in row.get("symptoms", "").split(",")
                    if s.strip()
                ]

                kb[name] = {
                    "symptoms": symptoms,
                    "self_care": row.get("self_care", "").strip(),
                    "seek_care": row.get("seek_care", "").strip(),
                }

        return kb

    def _load_json(self, path: Path) -> Dict[str, Dict[str, Any]]:
        with path.open("r", encoding="utf-8") as f:
            data = json.load(f)

        if not isinstance(data, dict):
            raise ValueError("JSON root must be an object")

        return data
