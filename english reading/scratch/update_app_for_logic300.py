# -*- coding: utf-8 -*-
"""
Update app.js for 300 Transfer Logic Questions:
1. Strips Korean question translations from unsolved quiz cards (both reader quiz tab and logic lab).
2. Puts Korean translations strictly inside post-answer explanations.
3. Implements 5-Level difficulty filtering, search, set pagination (20 items/set), and view-all toggle in Logic Lab.
"""

import re

target_file = r"c:\english reading\js\app.js"

with open(target_file, "r", encoding="utf-8") as f:
    content = f.read()

# 1. In renderQuizTab: remove questionKo from unsolved card
# Original:
# <div>
#   <p class="font-serif font-bold text-sm text-zinc-900 dark:text-zinc-100 leading-snug">${q.question}</p>
#   ${q.questionKo ? `<p class="text-xs text-zinc-500 mt-1 font-serif">${q.questionKo}</p>` : ''}
# </div>
target_quiz_text = """      <div>
        <p class="font-serif font-bold text-sm text-zinc-900 dark:text-zinc-100 leading-snug">${q.question}</p>
        ${q.questionKo ? `<p class="text-xs text-zinc-500 mt-1 font-serif">${q.questionKo}</p>` : ''}
      </div>"""

replacement_quiz_text = """      <div>
        <p class="font-serif font-bold text-sm text-zinc-900 dark:text-zinc-100 leading-snug">${q.question}</p>
      </div>"""

if target_quiz_text in content:
    content = content.replace(target_quiz_text, replacement_quiz_text, 1)
    print("1. Successfully removed questionKo from renderQuizTab unsolved card.")
else:
    print("Warning: target_quiz_text not found in app.js, checking regex...")
    content = re.sub(
        r'<p class="font-serif font-bold text-sm text-zinc-900 dark:text-zinc-100 leading-snug">\$\{q\.question\}<\/p>\s*\$\{q\.questionKo \? `<p class="text-xs text-zinc-500 mt-1 font-serif">\$\{q\.questionKo\}<\/p>` : \'\'\}',
        '<p class="font-serif font-bold text-sm text-zinc-900 dark:text-zinc-100 leading-snug">${q.question}</p>',
        content,
        count=1
    )

# 2. In handleQuizSelect: add questionKo to explanation
old_exp_start = '  let expHtml = "";\n  // 채점 후에만 공개되는 논리 단서 및 축 분석'
new_exp_start = '''  let expHtml = "";
  if (quiz.questionKo) {
    expHtml += `
      <div class="mb-2.5 p-2 bg-white/80 dark:bg-zinc-900/80 rounded border border-zinc-200 dark:border-zinc-800 text-xs font-serif text-zinc-700 dark:text-zinc-300">
        <strong class="text-zinc-900 dark:text-zinc-100">[질문 한국어 해석]</strong> ${quiz.questionKo}
      </div>
    `;
  }
  // 채점 후에만 공개되는 논리 단서 및 축 분석'''

if old_exp_start in content:
    content = content.replace(old_exp_start, new_exp_start, 1)
    print("2. Successfully added questionKo to handleQuizSelect explanation.")

# 3. Replace renderLogicLabContent and handleLogicLabAnswer and wire up level filters
old_logiclab_block = re.search(r'function refreshLogicLabQuestions\(\) \{[\s\S]*?function handleLogicLabAnswer\(qid, optIdx\) \{[\s\S]*?renderLogicLabContent\(\);\s*\}', content)

if old_logiclab_block:
    new_logiclab_block = """// ==========================================
// THE TRANSFER LOGIC LABORATORY (300제 & 5등급 난이도 체계)
// ==========================================
function refreshLogicLabQuestions() {
  state.logicLabAnswers = {};
  renderLogicLabContent();
  showToast("새로운 논리완성 문제 세트가 갱신되었습니다.");
}

function initLogicLabControls() {
  // 5등급 난이도 버튼 이벤트
  document.querySelectorAll(".logic-lvl-btn").forEach(btn => {
    btn.onclick = () => {
      document.querySelectorAll(".logic-lvl-btn").forEach(b => {
        b.className = "logic-lvl-btn px-2 py-1 border border-zinc-300 dark:border-zinc-700 rounded-xs hover:bg-zinc-100 dark:hover:bg-zinc-800";
      });
      btn.className = "logic-lvl-btn px-2.5 py-1 bg-zinc-900 text-white dark:bg-white dark:text-zinc-900 rounded-xs font-bold";
      state.logicLabLevel = btn.getAttribute("data-lvl") || "all";
      state.logicLabPage = 1;
      renderLogicLabContent();
    };
  });

  // 실시간 검색
  const searchInput = document.getElementById("logiclab-search");
  if (searchInput) {
    searchInput.oninput = () => {
      state.logicLabSearch = searchInput.value;
      state.logicLabPage = 1;
      renderLogicLabContent();
    };
  }

  // 세트 선택 드롭다운
  const setSelect = document.getElementById("logiclab-set-select");
  if (setSelect) {
    setSelect.onchange = () => {
      state.logicLabPage = parseInt(setSelect.value, 10) || 1;
      renderLogicLabContent();
      window.scrollTo({ top: document.getElementById("main-logic-view")?.offsetTop || 0, behavior: "smooth" });
    };
  }

  // 이전/다음 세트
  document.getElementById("btn-logic-prev-set")?.addEventListener("click", () => {
    if (state.logicLabPage > 1) {
      state.logicLabPage--;
      renderLogicLabContent();
      window.scrollTo({ top: document.getElementById("main-logic-view")?.offsetTop || 0, behavior: "smooth" });
    }
  });

  document.getElementById("btn-logic-next-set")?.addEventListener("click", () => {
    const bank = DerivativeQuizEngine.getMasterLogicBank();
    const filtered = filterLogicBank(bank);
    const totalPages = Math.max(1, Math.ceil(filtered.length / (state.logicLabPageSize || 20)));
    if (state.logicLabPage < totalPages) {
      state.logicLabPage++;
      renderLogicLabContent();
      window.scrollTo({ top: document.getElementById("main-logic-view")?.offsetTop || 0, behavior: "smooth" });
    }
  });

  // 전체 펼쳐보기 토글
  document.getElementById("btn-logic-view-all")?.addEventListener("click", () => {
    state.logicLabViewAll = !state.logicLabViewAll;
    const btn = document.getElementById("btn-logic-view-all");
    if (btn) {
      btn.textContent = state.logicLabViewAll ? "세트별로 보기 (20문항)" : "전체 펼쳐보기";
    }
    renderLogicLabContent();
  });
}

function filterLogicBank(bank) {
  let list = bank;
  const lvl = state.logicLabLevel || "all";
  if (lvl !== "all") {
    const lvlNum = parseInt(lvl, 10);
    list = list.filter(q => q.level === lvlNum);
  }
  const qStr = (state.logicLabSearch || "").trim().toLowerCase();
  if (qStr) {
    list = list.filter(q =>
      q.question.toLowerCase().includes(qStr) ||
      (q.theme && q.theme.toLowerCase().includes(qStr)) ||
      (q.questionKo && q.questionKo.toLowerCase().includes(qStr)) ||
      (q.options && q.options.some(opt => opt.toLowerCase().includes(qStr)))
    );
  }
  return list;
}

function renderLogicLabContent() {
  const container = document.getElementById("logiclab-container");
  if (!container || typeof DerivativeQuizEngine === "undefined") return;

  const rawBank = DerivativeQuizEngine.getMasterLogicBank();
  const filtered = filterLogicBank(rawBank);

  const answeredCountEl = document.getElementById("logiclab-answered-count");
  const totalCountEl = document.getElementById("logiclab-total-count");
  if (totalCountEl) totalCountEl.textContent = rawBank.length;

  let totalAnswered = 0;
  rawBank.forEach(q => {
    if (state.logicLabAnswers && state.logicLabAnswers[q.id] !== undefined) {
      totalAnswered++;
    }
  });
  if (answeredCountEl) answeredCountEl.textContent = totalAnswered;

  // 페이지네이션 세팅
  const pageSize = state.logicLabPageSize || 20;
  const totalPages = Math.max(1, Math.ceil(filtered.length / pageSize));
  if (state.logicLabPage > totalPages) state.logicLabPage = 1;
  const curPage = state.logicLabPage || 1;

  // 세트 드롭다운 갱신
  const setSelect = document.getElementById("logiclab-set-select");
  if (setSelect) {
    let setHtml = "";
    for (let p = 1; p <= totalPages; p++) {
      const sStart = (p - 1) * pageSize + 1;
      const sEnd = Math.min(filtered.length, p * pageSize);
      setHtml += `<option value="${p}" ${p === curPage ? "selected" : ""}>Set ${p} (${sStart}~${sEnd}번)</option>`;
    }
    setSelect.innerHTML = setHtml;
  }

  // 페이지 인디케이터
  const pageIndicator = document.getElementById("logiclab-page-indicator");
  if (pageIndicator) {
    const sStart = (curPage - 1) * pageSize + 1;
    const sEnd = Math.min(filtered.length, curPage * pageSize);
    pageIndicator.textContent = state.logicLabViewAll 
      ? `전체 ${filtered.length}문항 모두 표시 중` 
      : `${sStart}~${sEnd}번 표시 중 (전체 ${filtered.length}문항)`;
  }

  if (filtered.length === 0) {
    container.innerHTML = `
      <div class="text-center py-12 text-xs font-mono text-zinc-400">
        <p>조건과 일치하는 논리완성 문항이 없습니다.</p>
        <p class="mt-1">검색어를 지우거나 난이도 필터를 변경해 보세요.</p>
      </div>
    `;
    return;
  }

  // 표시할 아이템 추출
  const displayItems = state.logicLabViewAll 
    ? filtered 
    : filtered.slice((curPage - 1) * pageSize, curPage * pageSize);

  container.innerHTML = displayItems.map((q) => {
    const globalIdx = rawBank.indexOf(q) + 1;
    const isAnswered = state.logicLabAnswers && state.logicLabAnswers[q.id] !== undefined;
    const chosenIdx = isAnswered ? state.logicLabAnswers[q.id] : null;

    // 난이도별 뱃지 컬러
    let lvlBadgeClass = "bg-purple-100 text-purple-800 dark:bg-purple-950 dark:text-purple-300";
    if (q.level === 1) lvlBadgeClass = "bg-emerald-100 text-emerald-800 dark:bg-emerald-950 dark:text-emerald-300";
    else if (q.level === 2) lvlBadgeClass = "bg-blue-100 text-blue-800 dark:bg-blue-950 dark:text-blue-300";
    else if (q.level === 3) lvlBadgeClass = "bg-purple-100 text-purple-800 dark:bg-purple-950 dark:text-purple-300";
    else if (q.level === 4) lvlBadgeClass = "bg-amber-100 text-amber-800 dark:bg-amber-950 dark:text-amber-300";
    else if (q.level === 5) lvlBadgeClass = "bg-rose-100 text-rose-800 dark:bg-rose-950 dark:text-rose-300";

    return `
      <div class="logic-item-card p-6 border border-zinc-200 dark:border-zinc-800 rounded-sm bg-zinc-50/40 dark:bg-zinc-900/30" data-qid="${q.id}">
        <!-- 문제 헤더 (난이도 및 번호 표기, 사전 힌트 없이 실전 시험 스타일) -->
        <div class="flex items-center justify-between mb-3 text-xs font-mono text-zinc-400">
          <div class="flex items-center space-x-2">
            <span class="font-bold text-zinc-800 dark:text-zinc-200 text-sm">[문제 #${String(globalIdx).padStart(3, '0')}]</span>
            <span class="px-2 py-0.5 text-[10px] font-bold rounded ${lvlBadgeClass}">${q.levelLabel || 'Lv.' + q.level}</span>
            <span class="text-zinc-300 dark:text-zinc-700">·</span>
            <span>${q.category || '논리완성'}</span>
          </div>
          <span class="font-serif italic text-zinc-500">${q.theme || 'Academic Discourse'}</span>
        </div>

        <!-- 순수 영문 문제 본문 (한글 번역 노출 금지) -->
        <div class="text-base font-serif font-bold text-zinc-900 dark:text-zinc-100 leading-relaxed mb-4">
          ${q.question}
        </div>

        <!-- 4지선다형 순수 영문 선택지 (단어 뜻 사전 미표시) -->
        <div class="grid grid-cols-1 sm:grid-cols-2 gap-2.5">
          ${q.options.map((opt, optIdx) => {
            let btnClass = "logic-opt-btn p-3 rounded-xs text-xs font-serif border border-zinc-200 dark:border-zinc-800 text-left transition flex items-start space-x-2";
            if (isAnswered) {
              if (optIdx === q.answer) {
                btnClass += " bg-emerald-100 dark:bg-emerald-950/60 border-emerald-500 text-emerald-900 dark:text-emerald-200 font-bold";
              } else if (optIdx === chosenIdx) {
                btnClass += " bg-rose-100 dark:bg-rose-950/60 border-rose-500 text-rose-900 dark:text-rose-200 line-through";
              }
            } else {
              btnClass += " hover:border-zinc-900 dark:hover:border-zinc-300 bg-white dark:bg-zinc-800";
            }
            return `
              <button 
                class="${btnClass}" 
                data-qid="${q.id}" 
                data-optidx="${optIdx}"
                ${isAnswered ? 'disabled' : ''}
              >
                <span class="font-mono font-bold text-zinc-400 flex-shrink-0">${String.fromCharCode(65 + optIdx)}.</span>
                <span>${opt}</span>
              </button>
            `;
          }).join("")}
        </div>

        <!-- 채점 후에만 공개되는 단서, 논리 유형, 어휘 분석, 지문 번역 -->
        ${isAnswered ? `
          <div class="mt-4 p-4 rounded-xs text-xs font-serif ${chosenIdx === q.answer ? 'bg-emerald-50 dark:bg-emerald-950/40 border border-emerald-200 dark:border-emerald-800 text-emerald-900 dark:text-emerald-200' : 'bg-rose-50 dark:bg-rose-950/40 border border-rose-200 dark:border-rose-800 text-rose-900 dark:text-rose-200'}">
            <div class="font-bold mb-2 text-sm">${chosenIdx === q.answer ? '✓ 정답입니다!' : `✕ 오답입니다. (정답: ${String.fromCharCode(65 + q.answer)}: ${q.options[q.answer]})`}</div>

            ${q.questionKo ? `
              <div class="mb-2.5 p-2 bg-white/70 dark:bg-zinc-900/70 rounded border border-zinc-200 dark:border-zinc-800 text-xs font-serif text-zinc-700 dark:text-zinc-300">
                <strong class="text-zinc-900 dark:text-zinc-100">[지문 한국어 번역]</strong> ${q.questionKo}
              </div>
            ` : ''}

            <div class="mb-2 p-2.5 bg-white/70 dark:bg-zinc-900/70 rounded border border-zinc-200 dark:border-zinc-800 text-[11px] font-mono space-y-1">
              <div><strong class="text-purple-700 dark:text-purple-300">[논리 관계]</strong> ${q.logicType || '문맥 추론'}</div>
              <div><strong class="text-purple-700 dark:text-purple-300">[결정적 단서(Clue)]</strong> <span class="bg-purple-100 dark:bg-purple-950 px-1 rounded">${q.clue || '핵심 문맥'}</span></div>
              <div><strong class="text-purple-700 dark:text-purple-300">[논리 방향성]</strong> ${q.direction || '순접/인과'}</div>
            </div>

            <div class="text-zinc-700 dark:text-zinc-300 leading-relaxed mb-3"><strong>해설:</strong> ${q.explanation}</div>
            
            ${q.vocabBreakdown && q.vocabBreakdown.length > 0 ? `
              <div class="pt-2 border-t border-zinc-200 dark:border-zinc-800/80">
                <span class="font-mono text-[10px] uppercase font-bold text-zinc-600 dark:text-zinc-400 block mb-1.5">선택지 어휘 정밀 분석 (Lexical Breakdown)</span>
                <div class="grid grid-cols-1 sm:grid-cols-2 gap-1.5 text-[11px] font-mono">
                  ${q.vocabBreakdown.map(v => `<div class="p-1.5 bg-white dark:bg-zinc-900 border border-zinc-200 dark:border-zinc-800 rounded"><strong>${v.word}</strong>: ${v.meaning}</div>`).join("")}
                </div>
              </div>
            ` : ''}
          </div>
        ` : ''}
      </div>
    `;
  }).join("");

  container.querySelectorAll(".logic-opt-btn").forEach(btn => {
    btn.onclick = () => {
      const qid = btn.getAttribute("data-qid");
      const optIdx = parseInt(btn.getAttribute("data-optidx"), 10);
      handleLogicLabAnswer(qid, optIdx);
    };
  });
}

function handleLogicLabAnswer(qid, optIdx) {
  state.logicLabAnswers = state.logicLabAnswers || {};
  state.logicLabAnswers[qid] = optIdx;

  const bank = DerivativeQuizEngine.getMasterLogicBank();
  const q = bank.find(item => item.id === qid);
  if (q && optIdx !== q.answer) {
    saveToWrongNotes({
      passageId: `logic-${qid}`,
      passageTitle: `[편입 논리 ${q.levelLabel || 'Lv.' + q.level}] ${q.theme}`,
      type: "logic",
      typeLabel: "편입 논리",
      logicType: q.logicType,
      clue: q.clue,
      direction: q.direction,
      vocabBreakdown: q.vocabBreakdown,
      question: q.question,
      questionKo: q.questionKo,
      selected: `${String.fromCharCode(65 + optIdx)}: ${q.options[optIdx]}`,
      correct: `${String.fromCharCode(65 + q.answer)}: ${q.options[q.answer]}`,
      explanation: q.explanation
    });
    showToast("틀린 문항이 [오답노트] 편입 논리 탭에 기록되었습니다.");
  }

  renderLogicLabContent();
}"""

    content = content[:old_logiclab_block.start()] + new_logiclab_block + content[old_logiclab_block.end():]
    print("3. Successfully updated renderLogicLabContent with 300 questions & 5-level filtering.")
else:
    print("Error: Could not locate old_logiclab_block in app.js")

# 4. In DOMContentLoaded, call initLogicLabControls()
if "initLogicLabControls();" not in content:
    init_call_target = "initQuickPassageSelector();"
    if init_call_target in content:
        content = content.replace(init_call_target, init_call_target + "\n  initLogicLabControls();", 1)
        print("4. Successfully added initLogicLabControls() to DOMContentLoaded.")

with open(target_file, "w", encoding="utf-8") as f:
    f.write(content)

print("Finished updating app.js successfully.")
