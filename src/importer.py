from dataclasses import dataclass
from pathlib import Path
from typing import Optional, Dict, Any

from .data_retriever import DataRetriever


@dataclass
class ImportResult:
    ok: bool
    data: Optional[Dict[str, Dict[str, Any]]]
    message: str
    errors: list[str]


def import_data(path: Path) -> ImportResult:
    retriever = DataRetriever()

    try:
        kb = retriever.load_knowledge_base(path)
    except Exception as e:
        return ImportResult(
            ok=False,
            data=None,
            message=f"Import failed: {e}",
            errors=retriever.errors,
        )

    if not kb:
        return ImportResult(
            ok=False,
            data=None,
            message="Import failed: dataset empty",
            errors=retriever.errors,
        )

    return ImportResult(
        ok=True,
        data=kb,
        message=f"Import successful: loaded {len(kb)} condition(s).",
        errors=retriever.errors,
    )
