# -*- coding: utf-8 -*-
"""
ReadFlow Pro - 90 Passages Generator
Generates 30 Beginner, 30 Intermediate, and 30 Advanced passages
with authoritative sources, reading comprehension questions, chunks, and translations.
"""

import json
import os

passages = []

# ==========================================================
# Helper to build passage structure
# ==========================================================
def make_passage(pid, title, ko_title, level, level_label, category, source, summary, sentences, vocab, grammar, quiz):
    words = sum(len(s["en"].split()) for s in sentences)
    wpm = 100 if level == "Beginner" else (140 if level == "Intermediate" else 180)
    minutes = max(1, round(words / wpm))
    return {
        "id": pid,
        "title": title,
        "koreanTitle": ko_title,
        "level": level,
        "levelLabel": level_label,
        "category": category,
        "source": source,
        "readingTime": f"{minutes} min",
        "wordCount": words,
        "summary": summary,
        "sentences": sentences,
        "vocabulary": vocab,
        "grammarNotes": grammar,
        "quiz": quiz
    }

print("Generator script template ready.")
