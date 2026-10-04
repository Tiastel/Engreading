# -*- coding: utf-8 -*-
"""
merge_all_passages.py
Combines Beginner (30), Intermediate (30), and Advanced (30) into js/data.js
Total: 90 authentic, high-quality reading passages
"""

import json
from generate_beginner_30 import build_dataset as build_b
from generate_intermediate_30 import build_intermediate_dataset as build_i
from generate_advanced_30 import build_advanced_dataset as build_a

print("Collecting passages...")
b_list = build_b()
i_list = build_i()
a_list = build_a()

all_passages = b_list + i_list + a_list
print(f"Total passages gathered: {len(all_passages)} (Beginner: {len(b_list)}, Intermediate: {len(i_list)}, Advanced: {len(a_list)})")

# Dump as JavaScript file
js_content = "/**\n * ReadFlow Pro - Master Reading Passage Dataset (90 Passages)\n * Curated from authoritative sources with comprehension quizzes, sentence chunks, and vocabulary.\n */\n\nconst SAMPLE_PASSAGES = " + json.dumps(all_passages, ensure_ascii=False, indent=2) + ";\n"

with open("js/data.js", "w", encoding="utf-8") as f:
    f.write(js_content)

print("Successfully written to js/data.js!")
