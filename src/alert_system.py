from src.library_functions import red_flag_alerts, has_allergy_conflict

class AlertSystem:
    """Wraps red-flag rules and allergy checks."""

    def __init__(self, alerts_rules=None):
        if alerts_rules is None:
            alerts_rules = {}
        if not isinstance(alerts_rules, dict):
            raise ValueError("alerts_rules must be a dict")
        self._alerts_rules = alerts_rules

    @property
    def alerts_rules(self): return dict(self._alerts_rules)

    def update_rules(self, new_rules):
        if not isinstance(new_rules, dict):
            raise ValueError("new_rules must be a dict")
        self._alerts_rules = new_rules

    def check(self, symptoms, duration_days, severity):
        return red_flag_alerts(symptoms, duration_days, severity, self._alerts_rules)

    def allergy_conflict(self, allergies, medications):
        return has_allergy_conflict(allergies, medications)

    def __str__(self):
        return f"AlertSystem(rules={list(self._alerts_rules.keys())})"

    def __repr__(self):
        return f"AlertSystem({self._alerts_rules})"
