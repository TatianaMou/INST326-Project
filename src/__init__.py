"""
Health Information Retrieval Tool — Package Init

This makes the `src` folder a Python package and re-exports
our public functions so you can do:

    from src import irlib
    # or directly
    from src.irlib import parse_symptom_list, rank_conditions_basic, ...

"""

__version__ = "0.1.0"

# Re-export everything from irlib so users can import from src.irlib
from . import irlib  # noqa: F401
