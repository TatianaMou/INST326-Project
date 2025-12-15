# =========================
# FINAL: io_export.py
# =========================
from __future__ import annotations
import json
from pathlib import Path
from typing import Dict, Any

class ExportError(Exception):
    pass

def export_results_json(results: Dict[str, Any], output_path: Path) -> Path:
    if not isinstance(results, dict):
        raise ExportError("Results must be a dictionary")
    if not isinstance(output_path, Path):
        raise ExportError("output_path must be a pathlib.Path")

    try:
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with output_path.open("w", encoding="utf-8") as f:
            json.dump(results, f, indent=2, ensure_ascii=False)
        return output_path
    except (OSError, TypeError) as e:
        raise ExportError(f"Failed to export JSON: {e}") from e

def export_results_txt(results: Dict[str, Any], output_path: Path) -> Path:
    if not isinstance(results, dict):
        raise ExportError("Results must be a dictionary")
    if not isinstance(output_path, Path):
        raise ExportError("output_path must be a pathlib.Path")

    try:
        output_path.parent.mkdir(parents=True, exist_ok=True)
        lines = [
            "Medical Symptom Analysis Report",
            "=" * 32,
            f"Input symptoms: {', '.join(results.get('input_symptoms', []))}",
            ""
        ]
        ranked = results.get("ranked_conditions", [])
        if not ranked:
            lines.append("No matching conditions found.")
        else:
            for i, row in enumerate(ranked, start=1):
                lines.append(f"{i}. {row.get('condition')} (score: {row.get('score')})")
                lines.append(f"   Matched: {', '.join(row.get('matched_symptoms', []))}")
                if row.get("description"):
                    lines.append(f"   Notes: {row.get('description')}")
                lines.append("")
        with output_path.open("w", encoding="utf-8") as f:
            f.write("\n".join(lines).strip() + "\n")
        return output_path
    except OSError as e:
        raise ExportError(f"Failed to export TXT: {e}") from e
