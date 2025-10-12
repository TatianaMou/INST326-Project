"""
Health Information Retrieval Tool — Package Init

This makes the `src` folder a Python package.

Usage:
    from src import irlib
    # or import directly from the module:
    from src.irlib import parse_symptom_list, rank_conditions_basic, ...
"""

__version__ = "0.1.0"

# Expose the irlib module at the package level
from . import irlib

__all__ = ["irlib", "__version__"]
