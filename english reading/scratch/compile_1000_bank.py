# -*- coding: utf-8 -*-
"""
Compiler script to assemble 1,000 academic transfer English logic questions
across 5 difficulty levels into c:\english reading\js\logic_bank.js
"""

import os
import json
import re
from expand_level1 import get_level1_200
from expand_level2 import get_level2_200
from expand_level3 import get_level3_200
from expand_level4 import get_level4_200
from expand_level5 import get_level5_200

def main():
    print("Compiling all 1,000 questions across 5 difficulty levels...")
    q1 = get_level1_200()
    q2 = get_level2_200()
    q3 = get_level3_200()
    q4 = get_level4_200()
    q5 = get_level5_200()

    print(f"Level 1 (기초): {len(q1)} items")
    print(f"Level 2 (중급): {len(q2)} items")
    print(f"Level 3 (상급·2빈칸): {len(q3)} items")
    print(f"Level 4 (장문논리): {len(q4)} items")
    print(f"Level 5 (극상킬러): {len(q5)} items")

    all_questions = q1 + q2 + q3 + q4 + q5
    print(f"Total compiled questions: {len(all_questions)}")

    assert len(all_questions) == 1000, f"Expected 1000 questions, got {len(all_questions)}"

    # Verification checks
    korean_regex = re.compile(r'[\uac00-\ud7a3]')
    ids_seen = set()

    for idx, q in enumerate(all_questions):
        expected_id = f"tl-{idx+1:04d}"
        q["id"] = expected_id
        assert expected_id not in ids_seen, f"Duplicate ID: {expected_id}"
        ids_seen.add(expected_id)

        assert len(q["options"]) == 4, f"{expected_id} does not have 4 options"
        assert 0 <= q["answer"] < 4, f"{expected_id} invalid answer index: {q['answer']}"

        # Check that options contain NO Korean
        for opt in q["options"]:
            if korean_regex.search(opt):
                raise ValueError(f"Option in {expected_id} contains Korean: {opt}")

    target_file = r"c:\english reading\js\logic_bank.js"
    json_data = json.dumps(all_questions, ensure_ascii=False, indent=2)

    js_code = f"""/**
 * ReadFlow Academic Transfer Logic Question Bank (1,000 Verified Questions)
 * Distributed across 5 difficulty levels:
 * - Level 1 (0001~0200): Lv.1 기초 논리 (단일 빈칸, 인과/순접/정의, 수능 1등급 / 편입 기초 200제)
 * - Level 2 (0201~0400): Lv.2 중급 논리 (단일 빈칸, 역접/대조/양보, 서강대/중앙대 기본 200제)
 * - Level 3 (0401~0600): Lv.3 상급 논리 (더블 빈칸 2빈칸 대구, 성균관대/한양대 2빈칸 200제)
 * - Level 4 (0601~0800): Lv.4 장문 논리 (80~140단어 심층 단락 종합 추론, 장문 빈칸 200제)
 * - Level 5 (0801~1000): Lv.5 극상 논리 (GRE & 최상위권 편입 킬러, 고난도 추상철학 200제)
 */

const _MASTER_LOGIC_BANK = {json_data};

if (typeof window !== "undefined") {{
  window.MASTER_LOGIC_BANK = _MASTER_LOGIC_BANK;
}}

if (typeof module !== "undefined" && module.exports) {{
  module.exports = _MASTER_LOGIC_BANK;
}}
"""

    with open(target_file, "w", encoding="utf-8") as f:
        f.write(js_code)

    file_size_mb = os.path.getsize(target_file) / (1024 * 1024)
    print(f"Successfully wrote {len(all_questions)} questions to {target_file} ({file_size_mb:.2f} MB)")

if __name__ == "__main__":
    main()
