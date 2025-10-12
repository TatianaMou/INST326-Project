"""
=======================================================
 Health Information Retrieval Tool — Function Library
=======================================================

All functions are beginner-friendly:
- variables, lists, dicts
- loops, if/elif
- clear docstrings
- simple input checks with prints (no advanced typing)

These utilities will become methods in Project 2 classes.
"""

# ----------------------------------------------------
# 0) Small Helpers (kept minimal to stay beginner-friendly)
# ----------------------------------------------------

def _to_lower_list(items):
    out = []
    if type(items) != list:
        return out
    for x in items:
        if type(x) == str:
            s = x.strip().lower()
            if s != "":
                out.append(s)
    return out


# ----------------------------------------------------
# 1) Validation & Simple Data Helpers
# ----------------------------------------------------

def validate_date(date_string):
    """Very basic date check 'YYYY-MM-DD' (no calendar logic)."""
    if type(date_string) != str:
        return False
    parts = date_string.split("-")
    if len(parts) != 3:
        return False
    if len(parts[0]) != 4 or len(parts[1]) != 2 or len(parts[2]) != 2:
        return False
    try:
        y = int(parts[0]); m = int(parts[1]); d = int(parts[2])
    except ValueError:
        return False
    if y < 1900 or m < 1 or m > 12 or d < 1 or d > 31:
        return False
    return True


def extract_year(date_string):
    """Return the year as int from 'YYYY-MM-DD'; 0 if invalid."""
    if not validate_date(date_string):
        return 0
    return int(date_string.split("-")[0])


def validate_severity(severity):
    """Return True if severity is 'mild', 'moderate', or 'severe'."""
    return severity in ["mild", "moderate", "severe"]


def calculate_age(dob, today="2025-10-12"):
    """Very rough age (year difference only)."""
    if not (validate_date(dob) and validate_date(today)):
        return 0
    y1 = extract_year(dob)
    y2 = extract_year(today)
    return max(0, y2 - y1)


def count_symptoms(symptoms):
    """Return number of symptoms (list length)."""
    if type(symptoms) != list:
        return 0
    return len(symptoms)


# ----------------------------------------------------
# 2) Patient & Doctor Records
# ----------------------------------------------------

def normalize_patient_fields(patientid, firstname, lastname, dob):
    """Return normalized patient dict (lowercased names, trimmed)."""
    if type(patientid) != str or type(firstname) != str or type(lastname) != str or type(dob) != str:
        print("All patient fields must be strings.")
        return {}
    return {
        "patientid": patientid.strip(),
        "firstname": firstname.strip().lower(),
        "lastname": lastname.strip().lower(),
        "dob": dob.strip()
    }


def input_new_patient():
    """Create a simple new patient dict by prompting (beginner I/O)."""
    pid = input("Enter patient id: ").strip()
    first = input("Enter first name: ").strip().lower()
    last = input("Enter last name: ").strip().lower()
    dob = input("Enter DOB (YYYY-MM-DD): ").strip()
    return {"patientid": pid, "firstname": first, "lastname": last, "dob": dob, "symptoms": []}


def input_new_doctor():
    """Create a simple new doctor dict by prompting (beginner I/O)."""
    did = input("Enter doctor id: ").strip()
    first = input("Enter doctor first name: ").strip()
    last = input("Enter doctor last name: ").strip()
    return {"doctorid": did, "docfirstname": first, "doclastname": last}


def doctorinformation(doctors):
    """Return a basic string summary of doctors dictionary."""
    if type(doctors) != dict:
        return "No doctor data."
    lines = []
    for did in doctors:
        info = doctors[did]
        lines.append(did + ": " + str(info.get("docfirstname","")) + " " + str(info.get("doclastname","")))
    return "\n".join(lines)


def generate_patient_summary(patient):
    """Create a one-line patient summary."""
    if type(patient) != dict:
        return ""
    first = str(patient.get("firstname","")).capitalize()
    last = str(patient.get("lastname","")).capitalize()
    dob = str(patient.get("dob","unknown"))
    syms = patient.get("symptoms", [])
    if type(syms) == list:
        sym_text = ", ".join(syms)
    else:
        sym_text = str(syms)
    return first + " " + last + " (DOB: " + dob + ") - Symptoms: " + sym_text


# ----------------------------------------------------
# 3) Symptoms & Query Building
# ----------------------------------------------------

def parse_symptom_list(symptom_text):
    """Turn a comma/space separated symptom string into a clean list."""
    if type(symptom_text) != str:
        return []
    text = symptom_text.strip().lower()
    if "," in text:
        parts = text.split(",")
    else:
        parts = text.split(" ")
    items = []
    for p in parts:
        p = p.strip()
        if p != "":
            items.append(p)
    return items


def build_patient_query(patientid, firstname, lastname, dob,
                        symptom_text, severity, duration_days, allergies):
    """Create a simple patient query dict (normalized fields + parsed symptoms)."""
    if severity not in ["mild", "moderate", "severe"]:
        print("Invalid severity. Use 'mild', 'moderate', or 'severe'.")
    if type(duration_days) != int or duration_days < 0:
        print("duration_days should be a non-negative integer.")

    symptoms = parse_symptom_list(symptom_text)
    # normalize allergies list
    a = []
    if type(allergies) == list:
        for it in allergies:
            if type(it) == str and it.strip() != "":
                a.append(it.strip().lower())

    return {
        "patientid": str(patientid).strip(),
        "firstname": str(firstname).strip().lower(),
        "lastname": str(lastname).strip().lower(),
        "dob": str(dob).strip(),
        "symptoms": symptoms,
        "severity": severity,
        "duration_days": duration_days,
        "allergies": a
    }


# ----------------------------------------------------
# 4) Alerts & Safety
# ----------------------------------------------------

def has_allergy_conflict(allergies, medications):
    """Return True if any med appears in allergies (very simple)."""
    a = _to_lower_list(allergies)
    m = _to_lower_list(medications)
    for med in m:
        if med in a:
            return True
    return False


def red_flag_alerts(symptoms, duration_days, severity, alerts_rules):
    """Return list of red-flag messages using simple rules."""
    s = _to_lower_list(symptoms)
    alerts = []

    # keyword urgent list
    keywords = alerts_rules.get("keywords", [])
    for kw in keywords:
        if kw in s:
            alerts.append("Urgent symptom detected: " + kw + " — seek medical attention.")

    # long duration
    long_days = alerts_rules.get("long_duration_days", 0)
    if long_days > 0 and duration_days > long_days:
        alerts.append("Symptoms lasting more than " + str(long_days) + " days: consider professional evaluation.")

    # fever duration
    fever_kw = alerts_rules.get("high_fever_keyword", "")
    fever_days = alerts_rules.get("high_fever_threshold_days", 0)
    if fever_kw != "" and fever_days > 0 and fever_kw in s and duration_days >= fever_days:
        alerts.append("Fever lasting more than " + str(fever_days) + " days: consider professional evaluation.")

    # severity
    if severity == "severe":
        alerts.append("Severity marked as severe: seek professional care.")

    return alerts


# ----------------------------------------------------
# 5) Condition Ranking (Beginner Version)
# ----------------------------------------------------

def rank_conditions_basic(symptoms, knowledge_base, top_n=5):
    """
    Rank conditions by simple overlap score.
    score = overlap / union + tiny bonus for exact phrase matches.
    """
    s = _to_lower_list(symptoms)
    results = []

    for condition in knowledge_base:
        info = knowledge_base[condition]
        kb_symptoms = info.get("symptoms", [])
        canon = _to_lower_list(kb_symptoms)

        # unique lists
        unique_s = []
        for item in s:
            if item not in unique_s:
                unique_s.append(item)
        unique_canon = []
        for item in canon:
            if item not in unique_canon:
                unique_canon.append(item)

        # matches
        matched = []
        for item in unique_s:
            if item in unique_canon:
                matched.append(item)

        # union count
        union_list = unique_s[:]
        for item in unique_canon:
            if item not in union_list:
                union_list.append(item)
        union_count = len(union_list)

        if union_count == 0:
            base = 0.0
        else:
            base = float(len(matched)) / float(union_count)

        # small phrase bonus
        bonus_count = 0
        for ph in s:
            if ph in canon:
                bonus_count += 1
        score = base + 0.05 * bonus_count

        exp = "Matched " + str(len(matched)) + " symptoms out of " + str(len(canon)) + "."
        if bonus_count > 0:
            exp += " Extra bonus for exact phrase matches."

        results.append({
            "condition": condition,
            "score": float(score),
            "matched": matched,
            "explanation": exp
        })

    # sort and slice
    results = sorted(results, key=lambda d: d["score"], reverse=True)
    if len(results) > top_n:
        results = results[:top_n]
    return results


# ----------------------------------------------------
# 6) Search & Analytics
# ----------------------------------------------------

def search_patient_records(records, keyword):
    """Search across simple patient dicts for keyword (very basic)."""
    if type(records) != list or type(keyword) != str:
        return []
    k = keyword.lower()
    matches = []
    for r in records:
        text = ""
        for key in r:
            text = text + str(r[key]).lower() + " "
        if k in text:
            matches.append(r)
    return matches


def summarize_condition_stats(conditions):
    """Return dict condition -> count."""
    stats = {}
    if type(conditions) != list:
        return stats
    for c in conditions:
        name = str(c).lower()
        if name in stats:
            stats[name] = stats[name] + 1
        else:
            stats[name] = 1
    return stats


def log_search_activity(log_list, query):
    """Append a cleaned query to the search log list."""
    if type(log_list) != list or type(query) != str:
        return log_list
    clean = query.strip().lower()
    if clean != "":
        log_list.append(clean)
    return log_list


def top_ranked_searches(log_list):
    """Return list of (query, count) sorted by count desc."""
    stats = summarize_condition_stats(log_list)
    items = []
    for q in stats:
        items.append((q, stats[q]))
    items = sorted(items, key=lambda t: t[1], reverse=True)
    return items


def search_notes_and_assignments(query_terms, docs, top_n=5, snippet_width=80):
    """Rank simple docs by keyword overlap and return id/title/score/snippet."""
    if type(query_terms) != list or type(docs) != list:
        return []
    q = _to_lower_list(query_terms)
    results = []
    for d in docs:
        title = str(d.get("title",""))
        body = str(d.get("body",""))
        text_lower = (title + " " + body).lower()

        score = 0
        for t in q:
            score = score + text_lower.count(t)

        snippet = ""
        first_pos = -1
        for t in q:
            pos = text_lower.find(t)
            if pos != -1 and (first_pos == -1 or pos < first_pos):
                first_pos = pos
        if first_pos != -1:
            start = max(0, first_pos - snippet_width // 4)
            end   = min(len(text_lower), first_pos + snippet_width // 4 * 3)
            snippet = text_lower[start:end]
            # uppercase first term occurrence (basic emphasis)
            for t in q:
                if text_lower.find(t) == first_pos:
                    snippet = snippet.replace(t, t.upper(), 1)
                    break
            if start > 0:
                snippet = "... " + snippet
            if end < len(text_lower):
                snippet = snippet + " ..."

        results.append({
            "id": d.get("id",""),
            "title": title,
            "score": float(score),
            "snippet": snippet
        })

    results = sorted(results, key=lambda r: r["score"], reverse=True)
    if len(results) > top_n:
        results = results[:top_n]
    return results


# ----------------------------------------------------
# 7) Display Helpers
# ----------------------------------------------------

def format_condition_result_card(condition_name, matched, score, info):
    """Return a small dict for display of a ranked condition."""
    if type(condition_name) != str:
        return {}
    if type(matched) != list:
        matched = []
    if type(info) != dict:
        info = {}
    matched_text = ", ".join(matched) if len(matched) > 0 else "none"
    self_care = info.get("self_care", "See general care guidance.")
    seek_care = info.get("seek_care", "")
    card = {
        "title": condition_name,
        "subtitle": "Matched symptoms: " + matched_text,
        "details": "Relevance score: " + str(round(float(score), 2)),
        "advice": "Self-care: " + self_care
    }
    if seek_care != "":
        card["advice"] = card["advice"] + " | When to seek care: " + seek_care
    return card


def suggest_prevention_tips(symptoms, prevention_rules):
    """Return unique prevention tips for given symptoms from a simple rule map."""
    s = _to_lower_list(symptoms)
    tips = []
    if type(prevention_rules) != dict:
        return tips
    for sym in s:
        rule_list = prevention_rules.get(sym, [])
        if type(rule_list) == list:
            for tip in rule_list:
                if type(tip) == str:
                    t = tip.strip()
                    if t != "" and t not in tips:
                        tips.append(t)
    return tips
