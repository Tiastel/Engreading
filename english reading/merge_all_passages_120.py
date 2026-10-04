# -*- coding: utf-8 -*-
"""
merge_all_passages_120.py
Combines:
- 40 Beginner (30 base + 10 expansion)
- 40 Intermediate (30 base + 10 expansion)
- 40 Advanced (30 base + 10 expansion)
Total: 120 authentic, rigorous, verified passages.
"""

import json
from generate_beginner_30 import build_dataset as build_b
from generate_intermediate_30 import build_intermediate_dataset as build_i
from generate_advanced_30 import build_advanced_dataset as build_a

from generate_expansion_passages import get_expansion_passages
from generate_expansion_intermediate import get_intermediate_expansion
from generate_expansion_advanced import get_advanced_expansion

def format_extra(raw_list, level, level_label, wpm):
    result = []
    for pid, title, kt, cat, src, summ, sents, vocabs, grammars, quizzes in raw_list:
        sentences_objs = [{"en": e, "ko": k, "chunks": c} for e, k, c in sents]
        vocab_objs = [{"word": w, "pos": p, "meaning": m, "example": ex} for w, p, m, ex in vocabs]
        grammar_objs = [{"title": gt, "desc": gd} for gt, gd in grammars]
        quiz_objs = [{"id": i+1, "question": q, "questionKo": qk, "options": opts, "answer": ans, "explanation": exp} for i, (q, qk, opts, ans, exp) in enumerate(quizzes)]
        
        words = sum(len(e.split()) for e, k, c in sents)
        result.append({
            "id": pid,
            "title": title,
            "koreanTitle": kt,
            "level": level,
            "levelLabel": level_label,
            "category": cat,
            "source": src,
            "readingTime": f"{max(1, round(words / wpm))} min",
            "wordCount": words,
            "summary": summ,
            "sentences": sentences_objs,
            "vocabulary": vocab_objs,
            "grammarNotes": grammar_objs,
            "quiz": quiz_objs
        })
    return result

print("Loading base 90 passages...")
b_base = build_b()
i_base = build_i()
a_base = build_a()

print("Formatting expansion passages...")
b_exp = format_extra(get_expansion_passages(), "Beginner", "초급 (A2-B1)", 110)
i_exp = format_extra(get_intermediate_expansion(), "Intermediate", "중급 (B1-B2)", 130)
a_exp = format_extra(get_advanced_expansion(), "Advanced", "고급 (B2-C1)", 140)

all_b = b_base + b_exp
all_i = i_base + i_exp
all_a = a_base + a_exp

all_passages = all_b + all_i + all_a
print(f"Total passages gathered: {len(all_passages)} (Beginner: {len(all_b)}, Intermediate: {len(all_i)}, Advanced: {len(all_a)})")

# Dump as JavaScript file
js_content = "/**\n * ReadFlow Academic Journal - Master Reading Passage Dataset (120 Passages)\n * Curated from authoritative sources with comprehension quizzes, sentence chunks, and vocabulary.\n */\n\nconst SAMPLE_PASSAGES = " + json.dumps(all_passages, ensure_ascii=False, indent=2) + ";\n"

with open("js/data.js", "w", encoding="utf-8") as f:
    f.write(js_content)

print("Successfully written to js/data.js!")
