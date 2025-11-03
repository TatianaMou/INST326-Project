class Doctor:
    """Represents a doctor in the system (simple identity + encapsulation)."""

    def __init__(self, doctorid, docfirstname, doclastname):
        if not isinstance(doctorid, str) or doctorid.strip() == "":
            raise ValueError("doctorid must be a non-empty string")
        if not isinstance(docfirstname, str) or not isinstance(doclastname, str):
            raise ValueError("names must be strings")
        self._doctorid = doctorid.strip()
        self._docfirstname = docfirstname.strip().capitalize()
        self._doclastname = doclastname.strip().capitalize()

    @property
    def doctorid(self): return self._doctorid
    @property
    def docfirstname(self): return self._docfirstname
    @property
    def doclastname(self): return self._doclastname

    def full_name(self):
        return f"{self._docfirstname} {self._doclastname}"

    def __str__(self):
        return f"Dr. {self._docfirstname} {self._doclastname} (ID: {self._doctorid})"

    def __repr__(self):
        return f"Doctor(doctorid='{self._doctorid}', docfirstname='{self._docfirstname}', doclastname='{self._doclastname}')"
