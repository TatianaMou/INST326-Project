"""
=======================================================
 Utilities Module — src/utils.py
=======================================================

This file contains small helper functions used across
our Health Information Retrieval project.

All utilities are written in Python and
can be imported by other files (like irlib.py or demo_script.py).

Example:
    from src.utils import clean_text, print_divider
"""

# ----------------------------------------------------
# Basic String & Formatting Utilities
# ----------------------------------------------------

def clean_text(text):
    """Lowercase and remove extra spaces from text."""
    if type(text) != str:
        return ""
    text = text.strip().lower()
    return text


def capitalize_name(name):
    """Capitalize a first or last name safely."""
    if type(name) != str:
        return ""
    name = name.strip().capitalize()
    return name


def print_divider(title=""):
    """Print a visual divider line (for console readability)."""
    print("\n" + "=" * 60)
    if title != "":
        print(" " + title.upper())
        print("=" * 60 + "\n")


# ----------------------------------------------------
# Basic Math & Counting Utilities
# ----------------------------------------------------

def safe_divide(num, den):
    """Safely divide two numbers without crashing on zero."""
    if den == 0:
        return 0
    return num / den


def average(values):
    """Compute average of a list of numbers."""
    if type(values) != list or len(values) == 0:
        return 0
    total = 0
    for v in values:
        total = total + v
    return total / len(values)


def percent(part, whole):
    """Return a simple percent (0–100)."""
    if whole == 0:
        return 0
    return (part / whole) * 100


# ----------------------------------------------------
# Validation Utilities
# ----------------------------------------------------

def is_empty(value):
    """Check if a variable is empty or None."""
    if value is None:
        return True
    if value == "":
        return True
    if type(value) == list and len(value) == 0:
        return True
    return False


def is_valid_id(identifier):
    """Quickly check if an ID like P001 or D002 is formatted correctly."""
    if type(identifier) != str:
        return False
    identifier = identifier.strip().upper()
    if len(identifier) < 2:
        return False
    if not identifier[0].isalpha():
        return False
    if not identifier[1:].isdigit():
        return False
    return True


# ----------------------------------------------------
# Display & Debug Helpers
# ----------------------------------------------------

def preview_dict(d, limit=3):
    """Show first few key-value pairs from a dictionary (for debugging)."""
    if type(d) != dict:
        print("Not a dictionary.")
        return
    count = 0
    for k in d:
        print(k, ":", d[k])
        count += 1
        if count >= limit:
            break


def list_to_string(items):
    """Convert a list to a comma-separated string."""
    if type(items) != list:
        return str(items)
    text = ""
    for i in range(len(items)):
        text = text + str(items[i])
        if i < len(items) - 1:
            text = text + ", "
    return text


# ----------------------------------------------------
# End of utils.py
# ----------------------------------------------------
