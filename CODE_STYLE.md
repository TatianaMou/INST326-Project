# Code Style Guide


Our team follows **PEP8** and Python best practices.


## Key Conventions
- **Type hints** required on all function signatures.
- **Docstrings** follow Google/PEP257 style:
- Args, Returns, Raises, Examples.
- **Naming**:
- Functions: `snake_case`
- Constants: `UPPER_CASE`
- Variables: `lower_case`
- **Line length**: ≤ 88 chars (Black default).
- **Error handling**:
- Validate inputs, raise `TypeError` or `ValueError` with clear messages.
- **Examples**:
```python
def example_function(x: int) -> int:
"""Return x doubled.


Args:
x (int): Input number.


Returns:
int: x multiplied by 2.


Raises:
TypeError: If x is not an int.


Examples:
>>> example_function(3)
6
"""
if not isinstance(x, int):
raise TypeError("x must be an int")
return 2 * x
