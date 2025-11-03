from src.library_functions import (
    search_patient_records, log_search_activity, top_ranked_searches, summarize_condition_stats
)

class RecordsManager:
    """Stores simple records + query logs and provides analytics."""

    def __init__(self):
        self._records = []
        self._search_log = []

    @property
    def records(self): return list(self._records)
    @property
    def search_log(self): return list(self._search_log)

    def add_record(self, record_dict):
        if not isinstance(record_dict, dict):
            raise ValueError("record must be a dict")
        self._records.append(record_dict)

    def search(self, keyword):
        return search_patient_records(self._records, keyword)

    def log_query(self, query):
        self._search_log = log_search_activity(self._search_log, query)
        return list(self._search_log)

    def top_queries(self):
        return top_ranked_searches(self._search_log)

    def condition_counts(self, conditions):
        return summarize_condition_stats(conditions)

    def __str__(self):
        return f"RecordsManager(records={len(self._records)}, log={len(self._search_log)})"

    def __repr__(self):
        return f"RecordsManager(records={len(self._records)}, log_entries={len(self._search_log)})"
