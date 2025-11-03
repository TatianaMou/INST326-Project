from src.library_functions import (
    rank_conditions_basic, format_condition_result_card, search_notes_and_assignments
)

class ConditionSearch:
    """Wraps knowledge base operations: ranking + cards + notes search."""

    def __init__(self, knowledge_base=None):
        if knowledge_base is None:
            knowledge_base = {}
        if not isinstance(knowledge_base, dict):
            raise ValueError("knowledge_base must be a dict")
        self._knowledge_base = knowledge_base

    @property
    def knowledge_base(self): return dict(self._knowledge_base)

    def update_knowledge_base(self, new_kb):
        if not isinstance(new_kb, dict):
            raise ValueError("new_kb must be a dict")
        self._knowledge_base = new_kb

    def rank(self, symptoms, top_n=5):
        return rank_conditions_basic(symptoms, self._knowledge_base, top_n=top_n)

    def as_cards(self, ranked_items):
        cards = []
        for item in ranked_items:
            name = item.get("condition", "")
            score = item.get("score", 0.0)
            matched = item.get("matched", [])
            info = self._knowledge_base.get(name, {})
            cards.append(format_condition_result_card(name, matched, score, info))
        return cards

    def search_notes(self, query_terms, docs, top_n=5):
        return search_notes_and_assignments(query_terms, docs, top_n=top_n)

    def __str__(self):
        return f"ConditionSearch(kb_size={len(self._knowledge_base)})"

    def __repr__(self):
        return f"ConditionSearch(knowledge_base_keys={list(self._knowledge_base.keys())})"
