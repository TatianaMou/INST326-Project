from src.patient import Patient
from src.doctor import Doctor
from src.condition_search import ConditionSearch
from src.alert_system import AlertSystem
from src.records_manager import RecordsManager

# Tiny KB and rules
kb = {
    "Influenza": {
        "symptoms": ["fever", "cough", "fatigue", "sore throat"],
        "self_care": "Rest, fluids, OTC meds",
        "seek_care": "If fever >3 days or breathing issues"
    },
    "Common Cold": {
        "symptoms": ["cough", "sore throat", "congestion"],
        "self_care": "Hydration and rest"
    }
}
rules = {
    "keywords": ["chest pain", "shortness of breath"],
    "long_duration_days": 3,
    "high_fever_keyword": "fever",
    "high_fever_threshold_days": 3
}

# Make objects
p = Patient("P001", "Ada", "Lovelace", "2000-01-01", weight_kg=60, height_m=1.65)
p.add_symptom_text("fever, cough")
p.severity = "moderate"
p.duration_days = 4

d = Doctor("D001", "Jane", "Doe")
engine = ConditionSearch(kb)
alerts = AlertSystem(rules)
rm = RecordsManager()

print("PATIENT:", p.summary())
print("DOCTOR:", str(d))
print("AGE:", p.age(), "BMI:", round(p.bmi(), 2))

ranked = engine.rank(p.symptoms, top_n=3)
cards = engine.as_cards(ranked)
print("\nRANKED CONDITIONS:")
for c in cards:
    print("-", c["title"], "|", c["details"], "|", c["subtitle"])

print("\nALERTS:", alerts.check(p.symptoms, p.duration_days, p.severity))

rm.add_record({"firstname":"Ada","lastname":"Lovelace","notes":"Fever and cough"})
print("\nRECORD SEARCH (fever):", rm.search("fever"))
rm.log_query("fever"); rm.log_query("cough"); rm.log_query("fever")
print("TOP QUERIES:", rm.top_queries())
print("CONDITION COUNTS:", rm.condition_counts([x["condition"] for x in ranked]))
