/**
 * ReadFlow Academic Journal - Master Application Logic
 * Integrates 300 passages, wordtest1 22,000+ Master DB, Word Test quiz, and Wrong Answers Notebook.
 */

// 22,000+ 마스터 단어 DB 맵 초기화
const WORDTEST_MAP = new Map();
if (typeof defaultWords !== "undefined" && Array.isArray(defaultWords)) {
  for (const item of defaultWords) {
    if (item.word) {
      WORDTEST_MAP.set(item.word.toLowerCase(), item.meanings || []);
    }
  }
}

// 모바일 및 사파리 시크릿 모드 대응 무결성 로컬 스토리지 래퍼
const safeStorage = {
  getItem: function(key) {
    try {
      if (typeof window !== "undefined" && window.localStorage) {
        return window.localStorage.getItem(key);
      }
    } catch (e) {
      console.warn("Storage access restricted:", key);
    }
    return null;
  },
  setItem: function(key, val) {
    try {
      if (typeof window !== "undefined" && window.localStorage) {
        window.localStorage.setItem(key, val);
      }
    } catch (e) {
      console.warn("Storage write restricted:", key);
    }
  },
  removeItem: function(key) {
    try {
      if (typeof window !== "undefined" && window.localStorage) {
        window.localStorage.removeItem(key);
      }
    } catch (e) {
      console.warn("Storage remove restricted:", key);
    }
  },
  getParsed: function(key, fallback) {
    try {
      const val = safeStorage.getItem(key);
      return val ? JSON.parse(val) : fallback;
    } catch (e) {
      return fallback;
    }
  }
};

// 기본 지문 데이터셋 방어적 확보
const defaultPassages = (typeof SAMPLE_PASSAGES !== "undefined" && Array.isArray(SAMPLE_PASSAGES))
  ? SAMPLE_PASSAGES
  : ((typeof window !== "undefined" && window.SAMPLE_PASSAGES) ? window.SAMPLE_PASSAGES : []);

// 전역 상태
const state = {
  passages: [...defaultPassages],
  currentPassageId: defaultPassages[0] ? defaultPassages[0].id : "passage-001",
  filterLevel: safeStorage.getItem("readflow_filter_level") || "All",
  passageLengthMode: safeStorage.getItem("readflow_passage_length_mode") || "full",
  directTranslation: false,
  chunkMode: false,
  clozeMode: false,
  fontSize: 18,
  lineHeight: 1.85,
  ttsSpeed: 1.0,
  ttsVoice: null,
  availableVoices: [],
  isPlayingTTS: false,
  currentSentenceIdx: -1,
  savedWords: safeStorage.getParsed("readflow_saved_words", []),
  completedPassages: safeStorage.getParsed("readflow_completed_passages", []),
  learnedWordIds: safeStorage.getParsed("readflow_learned_words", []),
  wrongQuizzes: safeStorage.getParsed("readflow_wrong_quizzes", []),
  wrongWords: safeStorage.getParsed("readflow_wrong_words", []),
  geminiApiKey: safeStorage.getItem("readflow_gemini_api_key") || "",
  translationCache: safeStorage.getParsed("readflow_trans_cache", {}),
  activeTab: "vocab",
  flashcardIdx: 0,
  flashcardFlipped: false,
  currentWordTest: [],
  wrongNotesFilter: "all",
  quizFilter: "all",
  currentEnrichedQuizzes: [],
  logicLabFilter: "all",
  logicLabAnswers: {}
};

// TTS 객체 안전 참조 (일부 모바일 브라우저/인앱 브라우저 미지원 대비)
const speechSynth = (typeof window !== "undefined" && "speechSynthesis" in window) ? window.speechSynthesis : null;
let currentUtterance = null;

// ==========================================
// INITIALIZATION
// ==========================================
document.addEventListener("DOMContentLoaded", () => {
  // 1. 기초 데이터 및 테마 복원
  try { loadCustomPassages(); } catch (e) { console.warn("Custom passages load warn:", e); }
  try { initTheme(); } catch (e) { console.warn("Theme init warn:", e); }

  // 2. [핵심] 지문 본문 최우선 즉시 렌더링 (모바일 화면 지연 및 타 모듈 에러 영향 원천 차단)
  try {
    loadPassage(state.currentPassageId);
  } catch (e) {
    console.error("Critical: Initial loadPassage failed:", e);
  }

  // 3. 서브 모듈 초기화 (각각 독립 try-catch로 격리하여 1개 실패 시에도 타 기능 및 지문 정상 작동)
  try { initVoices(); } catch (e) { console.warn("Voice init warn:", e); }
  try { initMasterVocabUI(); } catch (e) { console.warn("Master Vocab init warn:", e); }
  try { initQuickPassageSelector(); } catch (e) { console.warn("Quick Selector warn:", e); }
  try { updateLevelTabUI(); } catch (e) { console.warn("Level Tab warn:", e); }
  try { updatePassageModeUI(); } catch (e) { console.warn("Passage Mode warn:", e); }
  try { initLogicLabControls(); } catch (e) { console.warn("Logic Lab warn:", e); }
  try { initQuickCatalogPanel(); } catch (e) { console.warn("Quick Catalog warn:", e); }
  try { setupEventListeners(); } catch (e) { console.warn("Event Listeners warn:", e); }
  try { setupKeyboardShortcuts(); } catch (e) { console.warn("Shortcuts warn:", e); }
  try { initDictionaryTab(); } catch (e) { console.warn("Dictionary tab warn:", e); }
  try { updateProgressUI(); } catch (e) { console.warn("Progress UI warn:", e); }
});

function initMasterVocabUI() {
  const count = typeof defaultWords !== "undefined" && Array.isArray(defaultWords)
    ? defaultWords.length
    : WORDTEST_MAP.size;
  const countFormatted = count > 0 ? count.toLocaleString() : "15,000";

  const headerBadge = document.getElementById("header-wordtest-count-badge");
  if (headerBadge) headerBadge.textContent = `${countFormatted} DB`;

  const searchDbCount = document.getElementById("search-db-count");
  if (searchDbCount) searchDbCount.textContent = countFormatted;

  const testPoolDbCount = document.getElementById("test-pool-db-count");
  if (testPoolDbCount) testPoolDbCount.textContent = countFormatted;

  const popupDbLabel = document.getElementById("popup-db-label");
  if (popupDbLabel) popupDbLabel.textContent = `${countFormatted} DB`;

  const footerDbCount = document.getElementById("footer-db-count");
  if (footerDbCount) footerDbCount.textContent = `${countFormatted} WORDS`;
}

function loadCustomPassages() {
  const custom = safeStorage.getItem("readflow_custom_passages");
  if (custom) {
    try {
      const parsed = JSON.parse(custom);
      state.passages = [...defaultPassages, ...parsed];
    } catch (e) {
      console.error("Failed to parse custom passages", e);
    }
  }
}

function initTheme() {
  const saved = safeStorage.getItem("readflow_theme") || "light";
  setTheme(saved);
}

function setTheme(theme) {
  if (typeof document === "undefined" || !document.documentElement) return;
  document.documentElement.classList.remove("dark", "sepia");
  if (theme === "dark") {
    document.documentElement.classList.add("dark");
  } else if (theme === "sepia") {
    document.documentElement.classList.add("sepia");
  }
  safeStorage.setItem("readflow_theme", theme);

  const btnLight = document.getElementById("theme-btn-light");
  const btnSepia = document.getElementById("theme-btn-sepia");
  const btnDark = document.getElementById("theme-btn-dark");
  if (btnLight && btnSepia && btnDark) {
    btnLight.className = theme === "light" 
      ? "px-2 py-0.5 rounded transition font-bold bg-white text-zinc-900 shadow-xs" 
      : "px-2 py-0.5 rounded transition hover:text-zinc-900 dark:hover:text-white";
    btnSepia.className = theme === "sepia" 
      ? "px-2 py-0.5 rounded transition font-bold bg-amber-100 text-amber-900 shadow-xs" 
      : "px-2 py-0.5 rounded transition hover:text-zinc-900 dark:hover:text-white";
    btnDark.className = theme === "dark" 
      ? "px-2 py-0.5 rounded transition font-bold bg-zinc-900 text-white shadow-xs" 
      : "px-2 py-0.5 rounded transition hover:text-zinc-900 dark:hover:text-white";
  }
}

function initVoices() {
  if (!speechSynth) {
    console.warn("speechSynthesis is not available on this platform.");
    return;
  }

  function populateVoiceList() {
    try {
      if (!speechSynth) return;
      const voices = speechSynth.getVoices() || [];
      state.availableVoices = voices.filter(v => v && v.lang && v.lang.startsWith("en"));
      const voiceSelect = document.getElementById("select-tts-voice");
      if (!voiceSelect) return;

      if (state.availableVoices.length === 0) {
        voiceSelect.innerHTML = `<option value="">Default Voice</option>`;
        return;
      }

      state.availableVoices.sort((a, b) => {
        const aName = a.name || "";
        const bName = b.name || "";
        const aScore = (aName.includes("Natural") || aName.includes("Google") || aName.includes("Online")) ? 1 : 0;
        const bScore = (bName.includes("Natural") || bName.includes("Google") || bName.includes("Online")) ? 1 : 0;
        return bScore - aScore;
      });

      voiceSelect.innerHTML = state.availableVoices.map((v, i) => {
        const label = (v.name || "Voice").replace("Microsoft", "").replace("Desktop", "").trim();
        return `<option value="${i}">${label} (${v.lang})</option>`;
      }).join("");

      state.ttsVoice = state.availableVoices[0];
    } catch (e) {
      console.warn("populateVoiceList error:", e);
    }
  }

  populateVoiceList();
  try {
    if (speechSynth && speechSynth.onvoiceschanged !== undefined) {
      speechSynth.onvoiceschanged = populateVoiceList;
    }
  } catch (e) {
    console.warn("speechSynth onvoiceschanged binding error:", e);
  }
}

// ==========================================
// ==========================================
// CURRICULUM FILTERS & NAVIGATION HELPERS
// ==========================================
function getFilteredPassages() {
  if (!state.filterLevel || state.filterLevel === "All") {
    return state.passages;
  }
  return state.passages.filter(p => p.level.toLowerCase() === state.filterLevel.toLowerCase());
}

function setLevelTab(level) {
  state.filterLevel = level;
  safeStorage.setItem("readflow_filter_level", level);
  updateLevelTabUI();
  initQuickPassageSelector();

  const activeList = getFilteredPassages();
  const currentInList = activeList.some(p => p.id === state.currentPassageId);
  if (!currentInList && activeList.length > 0) {
    loadPassage(activeList[0].id);
  } else {
    updatePassageNavIndicators();
  }
}

function setPassageLengthMode(mode) {
  state.passageLengthMode = mode;
  safeStorage.setItem("readflow_passage_length_mode", mode);
  updatePassageModeUI();
  const current = state.passages.find(p => p.id === state.currentPassageId) || state.passages[0];
  if (current) {
    renderPassageContent(current);
    updatePassageMetaBadges(current);
  }
}

function updateLevelTabUI() {
  const current = state.filterLevel || "All";
  const tabs = [
    { id: "level-tab-all", lvl: "All", activeClass: "border-zinc-900 bg-zinc-900 text-white dark:border-white dark:bg-white dark:text-zinc-900 shadow-xs" },
    { id: "level-tab-b", lvl: "Beginner", activeClass: "border-emerald-600 bg-emerald-600 text-white shadow-xs font-bold" },
    { id: "level-tab-i", lvl: "Intermediate", activeClass: "border-blue-600 bg-blue-600 text-white shadow-xs font-bold" },
    { id: "level-tab-a", lvl: "Advanced", activeClass: "border-purple-600 bg-purple-600 text-white shadow-xs font-bold" }
  ];

  tabs.forEach(t => {
    const el = document.getElementById(t.id);
    if (!el) return;
    if (t.lvl.toLowerCase() === current.toLowerCase()) {
      el.className = `level-tab-btn px-2.5 py-1 rounded text-[11px] transition border ${t.activeClass}`;
    } else {
      el.className = "level-tab-btn px-2.5 py-1 rounded text-[11px] font-semibold transition border border-zinc-200 dark:border-zinc-800 text-zinc-600 dark:text-zinc-400 hover:text-zinc-900 dark:hover:text-white";
    }
  });
}

function updatePassageModeUI() {
  const mode = state.passageLengthMode || "full";
  const btnClause = document.getElementById("btn-mode-clause");
  const btnFull = document.getElementById("btn-mode-full");
  if (!btnClause || !btnFull) return;

  if (mode === "clause") {
    btnClause.className = "passage-mode-btn px-2.5 py-1 rounded bg-white dark:bg-zinc-700 text-blue-700 dark:text-blue-300 font-bold shadow-xs transition border border-blue-300 dark:border-blue-700";
    btnFull.className = "passage-mode-btn px-2.5 py-1 rounded text-zinc-600 dark:text-zinc-400 font-semibold hover:text-zinc-900 dark:hover:text-white transition";
  } else {
    btnClause.className = "passage-mode-btn px-2.5 py-1 rounded text-zinc-600 dark:text-zinc-400 font-semibold hover:text-zinc-900 dark:hover:text-white transition";
    btnFull.className = "passage-mode-btn px-2.5 py-1 rounded bg-white dark:bg-zinc-700 text-zinc-900 dark:text-white font-bold shadow-xs transition border border-zinc-300 dark:border-zinc-600";
  }
}

function updatePassageNavIndicators() {
  const activeList = getFilteredPassages();
  const pIdx = activeList.findIndex(p => p.id === state.currentPassageId);
  const indEl = document.getElementById("passage-index-indicator");
  if (indEl) {
    if (pIdx >= 0) {
      indEl.textContent = `${pIdx + 1} / ${activeList.length}`;
    } else {
      const gIdx = state.passages.findIndex(p => p.id === state.currentPassageId);
      indEl.textContent = `${gIdx + 1} / ${state.passages.length}`;
    }
  }
  const quickSelect = document.getElementById("quick-passage-select");
  if (quickSelect) {
    quickSelect.value = state.currentPassageId;
  }
}

function updatePassageMetaBadges(passage) {
  if (!passage || !passage.sentences) return;
  const mode = state.passageLengthMode || "full";
  const clauseSents = passage.sentences.filter(s => s.paragraph === 0 || typeof s.paragraph === "undefined");
  const clauseWords = clauseSents.reduce((acc, s) => acc + (s.en || "").split(/\s+/).filter(Boolean).length, 0);

  const wordCountEl = document.getElementById("passage-word-count");
  const timeEl = document.getElementById("passage-time");

  if (mode === "clause") {
    if (wordCountEl) wordCountEl.textContent = `${clauseWords} WORDS (구문·단문)`;
    if (timeEl) timeEl.textContent = "1 MIN";
  } else {
    if (wordCountEl) wordCountEl.textContent = `${passage.wordCount || 180} WORDS (실전 장문)`;
    if (timeEl) timeEl.textContent = passage.readingTime || "2 MIN";
  }
}

// ==========================================
// LOAD PASSAGE
// ==========================================
function loadPassage(passageId) {
  try {
    stopTTS();
    let passage = state.passages.find(p => p.id === passageId);
    if (!passage && state.passages.length > 0) {
      passage = state.passages[0];
    }
    if (!passage) {
      console.warn("No passage found in state.passages");
      const container = document.getElementById("passage-text-container");
      if (container) {
        container.innerHTML = `
          <div class="p-6 text-center text-zinc-500 font-mono text-sm">
            <p class="font-bold text-base text-zinc-800 dark:text-zinc-200 mb-2">지문 데이터를 준비하는 중입니다...</p>
            <p>잠시 후 화면이 나타나지 않으면 페이지를 새로고침해 주세요.</p>
          </div>
        `;
      }
      return;
    }

    state.currentPassageId = passage.id;
    state.currentSentenceIdx = -1;
    state.flashcardIdx = 0;
    state.flashcardFlipped = false;

    try { updatePassageNavIndicators(); } catch (e) {}

    const headerCountBadge = document.getElementById("header-passage-count-badge");
    if (headerCountBadge) {
      headerCountBadge.textContent = `${state.passages.length}편`;
    }

    const compStatus = document.getElementById("passage-completion-status");
    if (compStatus) {
      compStatus.classList.toggle("hidden", !state.completedPassages.includes(passage.id));
    }

    // 헤더 정보 갱신
    const titleEl = document.getElementById("passage-title");
    if (titleEl) titleEl.textContent = passage.title || "Academic Reading";
    const koTitleEl = document.getElementById("passage-korean-title");
    if (koTitleEl) koTitleEl.textContent = passage.koreanTitle || "";
    const lvlEl = document.getElementById("passage-level-badge");
    if (lvlEl) lvlEl.textContent = passage.levelLabel || passage.level || "GENERAL";
    const catEl = document.getElementById("passage-category-badge");
    if (catEl) catEl.textContent = passage.category || "ACADEMIC";
    const srcEl = document.getElementById("passage-source");
    if (srcEl) srcEl.textContent = passage.source || "Academic Journal";
    const sumEl = document.getElementById("passage-summary");
    if (sumEl) sumEl.textContent = passage.summary || "";
    
    try { updatePassageMetaBadges(passage); } catch (e) {}

    // 본문 렌더링 최우선 실행
    renderPassageContent(passage);

    // 사이드바 탭 렌더링 (각각 독립 try-catch)
    try { renderVocabTab(passage); } catch (e) { console.warn("Vocab tab render warn:", e); }
    try { renderQuizTab(passage); } catch (e) { console.warn("Quiz tab render warn:", e); }
    try { renderNotesTab(passage); } catch (e) { console.warn("Notes tab render warn:", e); }
    try { renderFlashcardTab(passage); } catch (e) { console.warn("Flashcard tab render warn:", e); }
    try { updateReadingProgressBar(); } catch (e) {}
  } catch (err) {
    console.error("Critical error in loadPassage:", err);
    const container = document.getElementById("passage-text-container");
    if (container && passage && passage.sentences) {
      container.innerHTML = `<div class="p-4 leading-relaxed">${passage.sentences.map(s => s.en).join(' ')}</div>`;
    }
  }
}

// 본문 렌더링
function renderPassageContent(passage) {
  const container = document.getElementById("passage-text-container");
  if (!container) return;
  container.style.fontSize = `${state.fontSize}px`;
  container.style.lineHeight = state.lineHeight;

  if (!passage || !Array.isArray(passage.sentences) || passage.sentences.length === 0) {
    container.innerHTML = `<div class="p-6 text-center text-zinc-400 font-mono text-sm">지문 문장 데이터를 불러올 수 없습니다. 페이지를 새로고침해 주세요.</div>`;
    return;
  }

  const mode = state.passageLengthMode || "full";
  // 구문·단문 모드에서는 0번 문단(핵심 4~6문장)만 발췌하여 집중 훈련
  let sentencesToRender = mode === "clause" 
    ? passage.sentences.filter(s => s && (s.paragraph === 0 || typeof s.paragraph === "undefined"))
    : passage.sentences;

  if (!sentencesToRender || sentencesToRender.length === 0) {
    sentencesToRender = passage.sentences;
  }

  let html = "";

  // 모드 안내 상단 배너
  if (mode === "clause") {
    html += `
      <div class="mb-4 p-2.5 bg-blue-50/80 dark:bg-blue-950/40 border border-blue-200 dark:border-blue-900 rounded text-xs font-mono text-blue-900 dark:text-blue-200 flex flex-wrap items-center justify-between gap-2 shadow-2xs">
        <div class="flex items-center space-x-1.5">
          <span class="font-bold text-sm">🔍</span>
          <span><b>구문·단문 집중 훈련</b> (핵심 ${sentencesToRender.length}문장 직독직해 · 청크 문법 집중)</span>
        </div>
        <button id="btn-banner-switch-full" class="font-bold underline hover:text-blue-700 dark:hover:text-white transition">실전 중·장문 전체 펼치기 →</button>
      </div>
    `;
  } else {
    html += `
      <div class="mb-4 p-2.5 bg-zinc-100/80 dark:bg-zinc-800/60 border border-zinc-200 dark:border-zinc-700 rounded text-xs font-mono text-zinc-700 dark:text-zinc-300 flex flex-wrap items-center justify-between gap-2 shadow-2xs">
        <div class="flex items-center space-x-1.5">
          <span class="font-bold text-sm">📖</span>
          <span><b>실전 중·장문 심층 독해</b> (3개 문단 · ${passage.wordCount || 180}단어 정통 학술 에세이)</span>
        </div>
        <button id="btn-banner-switch-clause" class="font-bold underline hover:text-zinc-900 dark:hover:text-white transition">구문·단문만 집중 보기 →</button>
      </div>
    `;
  }

  let currentParagraph = -1;

  sentencesToRender.forEach((s, idx) => {
    // 끊어읽기 모드가 아닐 때는 혹시 문장에 슬래시(/)가 있어도 완전 무결하게 공백으로 치환
    const cleanEn = (s.en || "").replace(/\s*\/\s*/g, " ").replace(/\s+/g, " ").trim();
    const sentenceText = state.chunkMode && s.chunks ? s.chunks : cleanEn;
    const wordsHtml = formatSentenceWords(sentenceText, passage, idx);

    // 자연스러운 학술 문단 구분
    const paraIdx = typeof s.paragraph === "number" ? s.paragraph : Math.floor(idx / 4);

    if (!state.directTranslation) {
      if (paraIdx !== currentParagraph) {
        if (currentParagraph !== -1) html += `</p>`;
        html += `<p class="mb-5 leading-relaxed text-justify">`;
        currentParagraph = paraIdx;
      }
      html += `
        <span class="sentence-item inline" data-idx="${idx}" title="문장 클릭 시 낭독 청취">${wordsHtml}</span>${" "}
      `;
    } else {
      // 직독직해 모드: 문장별 깔끔한 구분
      html += `
        <div class="mb-3.5 pb-2 border-b border-zinc-100 dark:border-zinc-800/60">
          <span class="sentence-item inline" data-idx="${idx}" title="문장 클릭 시 낭독 청취">${wordsHtml}</span>
          <div class="sentence-translation-inline font-sans text-xs text-zinc-600 dark:text-zinc-400 mt-1 pl-2.5 border-l-2 border-amber-500/70">↳ ${s.ko}</div>
        </div>
      `;
    }
  });

  if (!state.directTranslation && currentParagraph !== -1) {
    html += `</p>`;
  }

  container.innerHTML = html;

  // 배너 버튼 클릭 연결
  document.getElementById("btn-banner-switch-full")?.addEventListener("click", () => setPassageLengthMode("full"));
  document.getElementById("btn-banner-switch-clause")?.addEventListener("click", () => setPassageLengthMode("clause"));

  container.querySelectorAll(".sentence-item").forEach(el => {
    el.addEventListener("click", (e) => {
      if (!e.target.classList.contains("clickable-word") && !e.target.classList.contains("cloze-blank")) {
        const idx = parseInt(el.getAttribute("data-idx"), 10);
        speakSentence(idx);
      }
    });
  });

  container.querySelectorAll(".clickable-word").forEach(el => {
    el.addEventListener("click", (e) => {
      e.stopPropagation();
      const rawWord = el.getAttribute("data-word");
      const sentenceIdx = parseInt(el.getAttribute("data-sidx") || "0", 10);
      const sentenceObj = passage.sentences[sentenceIdx];
      const sentenceContext = sentenceObj ? sentenceObj.en : "";
      showWordPopup(rawWord, sentenceContext, e);
    });
  });

  container.querySelectorAll(".cloze-blank").forEach(el => {
    el.addEventListener("click", (e) => {
      e.stopPropagation();
      el.classList.toggle("cloze-revealed");
    });
  });
}

function formatSentenceWords(text, passage, sentenceIdx) {
  if (state.chunkMode) {
    text = text.replace(/\s*\/\s*/g, ' <span class="chunk-slash">/</span> ');
  } else {
    // 끊어읽기가 꺼져있으면 모든 슬래시(/)를 완전히 제거하여 하나의 자연스러운 문장으로 결합
    text = text.replace(/\s*\/\s*/g, ' ');
  }

  const targetWords = (passage.vocabulary || []).map(v => v.word.toLowerCase());
  const tokens = text.split(/(\s+|<span.*?<\/span>)/);
  let wordCounter = 0;

  return tokens.map(token => {
    if (!token || token.trim() === "" || token.startsWith("<span")) {
      return token;
    }

    const match = token.match(/^([^\w]*)([\w'-]+)([^\w]*)$/);
    if (match) {
      wordCounter++;
      const leading = match[1];
      const word = match[2];
      const trailing = match[3];
      const lower = word.toLowerCase();

      const isTarget = targetWords.includes(lower);
      const isCloze = state.clozeMode && (isTarget || (word.length >= 6 && wordCounter % 4 === 0));

      if (isCloze) {
        return `${leading}<span class="cloze-blank font-serif" data-word="${lower}" data-sidx="${sentenceIdx}">${word}</span>${trailing}`;
      } else {
        return `${leading}<span class="clickable-word" data-word="${lower}" data-sidx="${sentenceIdx}">${word}</span>${trailing}`;
      }
    }
    return token;
  }).join("");
}

// ==========================================
// 8,000 DICTIONARY POPUP WITH AI CONTEXT
// ==========================================
async function showWordPopup(word, sentenceContext, event) {
  const popup = document.getElementById("word-popup");
  const currentPassage = state.passages.find(p => p.id === state.currentPassageId);

  document.getElementById("popup-word").textContent = word;
  document.getElementById("popup-pos").textContent = "";
  document.getElementById("popup-korean-meaning").textContent = "사전 조회 중...";
  document.getElementById("popup-eng-meaning").textContent = "Loading definition...";

  const aiBox = document.getElementById("popup-ai-context-box");
  const aiContextEl = document.getElementById("popup-ai-context");
  aiBox.classList.add("hidden");

  const rect = event.target.getBoundingClientRect();
  const scrollTop = window.pageYOffset || document.documentElement.scrollTop;
  const scrollLeft = window.pageXOffset || document.documentElement.scrollLeft;
  popup.style.top = `${rect.bottom + scrollTop + 8}px`;
  popup.style.left = `${Math.min(window.innerWidth - 380, Math.max(10, rect.left + scrollLeft - 50))}px`;
  popup.style.display = "block";

  document.getElementById("popup-pronounce-btn").onclick = () => speakWord(word);

  const saveBtn = document.getElementById("popup-save-btn");
  const isSaved = state.savedWords.some(w => w.word.toLowerCase() === word.toLowerCase());
  saveBtn.textContent = isSaved ? "★ 저장됨" : "☆ 단어장 저장";

  // 1. wordtest1 Master DB 검색
  const wordtestMeanings = WORDTEST_MAP.get(word.toLowerCase());
  let koreanMeaning = "";

  if (wordtestMeanings && wordtestMeanings.length > 0) {
    koreanMeaning = wordtestMeanings.join(", ");
    document.getElementById("popup-korean-meaning").textContent = koreanMeaning;
    const dbSize = WORDTEST_MAP.size > 0 ? `${WORDTEST_MAP.size.toLocaleString()} DB` : "Master DB";
    document.getElementById("popup-pos").textContent = dbSize;
  } else {
    // 지문 어휘 체크
    const foundInVocab = currentPassage && currentPassage.vocabulary
      ? currentPassage.vocabulary.find(v => v.word.toLowerCase() === word.toLowerCase())
      : null;
    if (foundInVocab) {
      koreanMeaning = foundInVocab.meaning;
      document.getElementById("popup-korean-meaning").textContent = koreanMeaning;
      document.getElementById("popup-pos").textContent = foundInVocab.pos;
    } else {
      fetchSmartTranslation(word).then(tr => {
        document.getElementById("popup-korean-meaning").textContent = tr;
      });
    }
  }

  saveBtn.onclick = () => {
    toggleSaveWord(word, document.getElementById("popup-korean-meaning").textContent);
  };

  fetchEnglishDefinition(word);

  // AI 문맥 분석
  if (sentenceContext && state.geminiApiKey) {
    fetchAIContextAnalysis(word, sentenceContext).then(analysis => {
      if (analysis) {
        aiBox.classList.remove("hidden");
        aiContextEl.innerHTML = analysis;
      }
    });
  }
}

async function fetchAIContextAnalysis(word, sentence) {
  if (!state.geminiApiKey) return null;
  const prompt = `문장: "${sentence}"\n단어: "${word}"\n위 문장에서 이 단어의 문맥상 실제 의미와 뉘앙스를 한국어로 간결하게 1~2줄로 설명해줘.`;
  try {
    const url = `https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key=${state.geminiApiKey}`;
    const res = await fetch(url, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ contents: [{ parts: [{ text: prompt }] }] })
    });
    if (res.ok) {
      const data = await res.json();
      return data.candidates[0].content.parts[0].text.trim();
    }
  } catch (e) {}
  return null;
}

async function fetchSmartTranslation(text) {
  const key = text.trim().toLowerCase();
  if (state.translationCache[key]) return state.translationCache[key];

  try {
    const url = `https://api.mymemory.translated.net/get?q=${encodeURIComponent(text)}&langpair=en|ko`;
    const res = await fetch(url);
    if (res.ok) {
      const data = await res.json();
      if (data && data.responseData && data.responseData.translatedText) {
        const tr = data.responseData.translatedText;
        state.translationCache[key] = tr;
        safeStorage.setItem("readflow_trans_cache", JSON.stringify(state.translationCache));
        return tr;
      }
    }
  } catch (e) {}
  return "사전 뜻 검색 불가";
}

async function fetchEnglishDefinition(word) {
  try {
    const res = await fetch(`https://api.dictionaryapi.dev/api/v2/entries/en/${encodeURIComponent(word)}`);
    if (res.ok) {
      const data = await res.json();
      if (data && data[0] && data[0].meanings && data[0].meanings[0]) {
        const def = data[0].meanings[0].definitions[0].definition;
        document.getElementById("popup-eng-meaning").textContent = def;
        return;
      }
    }
  } catch (e) {}
  document.getElementById("popup-eng-meaning").textContent = "No definition found.";
}

function closeWordPopup() {
  const popup = document.getElementById("word-popup");
  if (popup) popup.style.display = "none";
}

function toggleSaveWord(word, meaning) {
  const idx = state.savedWords.findIndex(w => w.word.toLowerCase() === word.toLowerCase());
  const saveBtn = document.getElementById("popup-save-btn");

  if (idx > -1) {
    state.savedWords.splice(idx, 1);
    if (saveBtn) saveBtn.textContent = "☆ 단어장 저장";
    showToast(`단어 '${word}'가 단어장에서 제외되었습니다.`);
  } else {
    state.savedWords.push({ word, meaning, date: new Date().toLocaleDateString() });
    if (saveBtn) saveBtn.textContent = "★ 저장됨";
    showToast(`단어 '${word}'가 저장되었습니다.`);
  }
  safeStorage.setItem("readflow_saved_words", JSON.stringify(state.savedWords));
  updateProgressUI();
}

// ==========================================
// TABS RENDERING
// ==========================================
function renderVocabTab(passage) {
  const container = document.getElementById("tab-vocab-content");
  if (!container) return;

  if (!passage.vocabulary || passage.vocabulary.length === 0) {
    container.innerHTML = `<p class="text-xs text-zinc-400 font-mono py-8 text-center">등록된 핵심 어휘가 없습니다.</p>`;
    return;
  }

  container.innerHTML = `
    <div class="space-y-3">
      <div class="flex items-center justify-between text-xs font-mono text-zinc-500 pb-1 border-b border-zinc-100 dark:border-zinc-800">
        <span>ESSENTIAL LEXICON (${passage.vocabulary.length})</span>
        <button id="btn-listen-all-vocab" class="hover:text-zinc-900 dark:hover:text-white underline">ALL AUDIO</button>
      </div>
      ${passage.vocabulary.map(v => `
        <div class="p-3 bg-zinc-50 dark:bg-zinc-900/40 border border-zinc-200 dark:border-zinc-800 rounded-sm">
          <div class="flex items-center justify-between">
            <div class="flex items-center space-x-2">
              <span class="font-serif font-bold text-base text-zinc-900 dark:text-zinc-100">${v.word}</span>
              <span class="text-[10px] font-mono px-1 py-0.2 bg-zinc-200 dark:bg-zinc-800 text-zinc-600 dark:text-zinc-400 rounded-xs">${v.pos || 'v.'}</span>
            </div>
            <button class="vocab-speak-btn text-zinc-400 hover:text-zinc-900 dark:hover:text-white" data-word="${v.word}">
              <svg class="w-3.5 h-3.5" fill="currentColor" viewBox="0 0 24 24"><path d="M8 5v14l11-7z"/></svg>
            </button>
          </div>
          <div class="text-xs font-bold text-zinc-700 dark:text-zinc-300 mt-1">${v.meaning}</div>
          ${v.example ? `<div class="text-[11px] font-serif italic text-zinc-500 dark:text-zinc-400 mt-1.5 pl-2 border-l border-zinc-300 dark:border-zinc-700">"${v.example}"</div>` : ''}
        </div>
      `).join("")}
    </div>
  `;

  container.querySelectorAll(".vocab-speak-btn").forEach(btn => {
    btn.onclick = () => speakWord(btn.getAttribute("data-word"));
  });

  const allBtn = document.getElementById("btn-listen-all-vocab");
  if (allBtn) {
    allBtn.onclick = () => {
      if (!speechSynth) {
        showToast("음성 낭독(TTS)이 지원되지 않는 브라우저입니다.");
        return;
      }
      stopTTS();
      let i = 0;
      function next() {
        if (i < passage.vocabulary.length) {
          const u = new SpeechSynthesisUtterance(passage.vocabulary[i].word);
          u.lang = "en-US";
          u.rate = 0.9;
          if (state.ttsVoice) u.voice = state.ttsVoice;
          u.onend = () => { i++; setTimeout(next, 350); };
          speechSynth.speak(u);
        }
      }
      next();
    };
  }
}

// 퀴즈 렌더링 & 파생 퀴즈(독해, 빈칸, 순서, 편입 논리) 통합
function renderQuizTab(passage) {
  const container = document.getElementById("tab-quiz-content");
  if (!container) return;

  if (typeof DerivativeQuizEngine !== "undefined") {
    state.currentEnrichedQuizzes = DerivativeQuizEngine.getEnrichedQuizzesForPassage(passage);
  } else {
    state.currentEnrichedQuizzes = (passage.quiz || []).map(q => ({ ...q, type: "comprehension", typeLabel: "독해 일치" }));
  }

  const quizzes = state.currentEnrichedQuizzes;
  if (!quizzes || quizzes.length === 0) {
    container.innerHTML = `<p class="text-xs text-zinc-400 font-mono py-8 text-center">출제된 문제가 없습니다.</p>`;
    return;
  }

  container.innerHTML = `
    <div class="space-y-4">
      <div class="flex items-center justify-between text-xs font-mono text-zinc-500 pb-2 border-b border-zinc-100 dark:border-zinc-800">
        <span>COMPREHENSIVE ASSESSMENT (${quizzes.length} QUESTIONS)</span>
        <span id="quiz-score-badge" class="hidden font-bold text-zinc-900 dark:text-zinc-100 font-mono">SCORE: <span id="quiz-score-num">0</span> / ${quizzes.length}</span>
      </div>

      <!-- 문제 리스트: 유형 힌트 및 단서 배제, 순수 실전 시험으로 출제 -->
      <div class="space-y-4" id="quiz-blocks-list">
        ${quizzes.map((q, idx) => renderSingleQuizCard(q, idx)).join("")}
      </div>
    </div>
  `;

  // 선지 클릭 이벤트
  container.querySelectorAll(".quiz-option").forEach(btn => {
    btn.onclick = () => {
      const qIdx = parseInt(btn.getAttribute("data-qidx"), 10);
      const optIdx = parseInt(btn.getAttribute("data-optidx"), 10);
      handleQuizAnswer(passage, qIdx, optIdx);
    };
  });
}

function renderSingleQuizCard(q, qIdx) {
  let bodyContent = "";

  if (q.type === "order") {
    bodyContent = `
      <div class="mb-3 p-3 bg-zinc-100/70 dark:bg-zinc-800/50 rounded border border-zinc-200 dark:border-zinc-700 text-xs font-serif leading-relaxed">
        <span class="font-mono font-bold text-zinc-500 block mb-1 text-[10px]">[주어진 글]</span>
        <div class="text-zinc-900 dark:text-zinc-100">${q.leadIn.en}</div>
        ${q.leadIn.ko ? `<div class="text-[11px] text-zinc-500 mt-1">🇰🇷 ${q.leadIn.ko}</div>` : ''}
      </div>
      <div class="space-y-2 mb-3 text-xs font-serif leading-relaxed">
        ${q.blocks.map(b => `
          <div class="p-2.5 border border-zinc-200 dark:border-zinc-800 rounded bg-white dark:bg-zinc-900">
            <strong class="font-mono text-zinc-700 dark:text-zinc-300 mr-1 font-bold">${b.label}</strong>
            <span class="text-zinc-800 dark:text-zinc-200">${b.en}</span>
          </div>
        `).join("")}
      </div>
    `;
  } else if (q.type === "cloze") {
    bodyContent = `
      <div class="mb-3 p-3 bg-zinc-50 dark:bg-zinc-900/60 border border-zinc-200 dark:border-zinc-800 rounded text-xs font-serif leading-relaxed">
        <div class="text-zinc-900 dark:text-zinc-100">
          ${q.contextSentence.replace('[          ]', '<span class="font-mono font-bold underline decoration-2 px-1 text-zinc-900 dark:text-zinc-100">[ ________ ]</span>')}
        </div>
        ${q.contextSentenceKo ? `<div class="text-[11px] text-zinc-500 mt-1">🇰🇷 ${q.contextSentenceKo}</div>` : ''}
      </div>
    `;
  }

  return `
    <div class="quiz-block p-4 border border-zinc-200 dark:border-zinc-800 rounded-sm bg-zinc-50/50 dark:bg-zinc-900/30" data-qidx="${qIdx}">
      <div class="flex items-center space-x-2 mb-2">
        <span class="font-mono text-xs font-bold text-zinc-400">[0${qIdx + 1}]</span>
        <span class="text-[10px] font-mono uppercase text-zinc-400">QUESTION</span>
      </div>

      <div>
        <p class="font-serif font-bold text-sm text-zinc-900 dark:text-zinc-100 leading-snug">${q.question}</p>
      </div>

      ${bodyContent ? `<div class="mt-3">${bodyContent}</div>` : ''}

      <div class="mt-3 space-y-2">
        ${q.options.map((opt, optIdx) => `
          <button 
            class="quiz-option w-full text-left p-2.5 rounded-sm text-xs text-zinc-800 dark:text-zinc-200 flex items-start space-x-2 font-serif"
            data-qidx="${qIdx}"
            data-optidx="${optIdx}"
          >
            <span class="font-mono font-bold text-zinc-400 flex-shrink-0">${String.fromCharCode(65 + optIdx)}.</span>
            <span>${opt}</span>
          </button>
        `).join("")}
      </div>

      <div class="quiz-feedback hidden mt-3 p-3.5 rounded-sm text-xs font-serif leading-relaxed">
        <div class="feedback-status font-bold mb-1.5"></div>
        <div class="feedback-explanation text-zinc-600 dark:text-zinc-400"></div>
      </div>
    </div>
  `;
}

function handleQuizAnswer(passage, qIdx, selectedOptIdx) {
  const quizzes = state.currentEnrichedQuizzes || [];
  const quiz = quizzes[qIdx];
  if (!quiz) return;

  const block = document.querySelector(`.quiz-block[data-qidx="${qIdx}"]`);
  if (!block) return;

  const options = block.querySelectorAll(".quiz-option");
  const feedback = block.querySelector(".quiz-feedback");
  const statusEl = feedback.querySelector(".feedback-status");
  const explanationEl = feedback.querySelector(".feedback-explanation");

  options.forEach(b => b.disabled = true);

  const isCorrect = selectedOptIdx === quiz.answer;
  options[selectedOptIdx].classList.add(isCorrect ? "correct" : "incorrect");
  if (!isCorrect) {
    options[quiz.answer].classList.add("correct");

    // 오답노트에 자동 기록 (단서 및 어휘 분석표 포함)
    saveToWrongNotes({
      passageId: passage.id,
      passageTitle: passage.title,
      type: quiz.type || "comprehension",
      typeLabel: quiz.typeLabel || "독해 일치",
      logicType: quiz.logicType || null,
      clue: quiz.clue || null,
      direction: quiz.direction || null,
      vocabBreakdown: quiz.vocabBreakdown || null,
      question: quiz.question,
      questionKo: quiz.questionKo,
      selected: quiz.options[selectedOptIdx],
      correct: quiz.options[quiz.answer],
      explanation: quiz.explanation,
      date: new Date().toLocaleDateString()
    });
  }

  feedback.classList.remove("hidden");
  if (isCorrect) {
    feedback.className = "quiz-feedback mt-3 p-3.5 rounded-sm text-xs font-serif bg-emerald-50 dark:bg-emerald-950/40 text-emerald-900 dark:text-emerald-200 border border-emerald-200 dark:border-emerald-800";
    statusEl.textContent = "✓ 정답입니다.";
  } else {
    feedback.className = "quiz-feedback mt-3 p-3.5 rounded-sm text-xs font-serif bg-rose-50 dark:bg-rose-950/40 text-rose-900 dark:text-rose-200 border border-rose-200 dark:border-rose-800";
    statusEl.textContent = `✕ 오답입니다. (정답: ${String.fromCharCode(65 + quiz.answer)}: ${quiz.options[quiz.answer]}) · 오답노트에 자동 기록됨`;
  }

  let expHtml = "";
  if (quiz.questionKo) {
    expHtml += `
      <div class="mb-2.5 p-2 bg-white/80 dark:bg-zinc-900/80 rounded border border-zinc-200 dark:border-zinc-800 text-xs font-serif text-zinc-700 dark:text-zinc-300">
        <strong class="text-zinc-900 dark:text-zinc-100">[질문 한국어 해석]</strong> ${quiz.questionKo}
      </div>
    `;
  }
  // 채점 후에만 공개되는 논리 단서 및 축 분석
  if (quiz.logicType || quiz.clue) {
    expHtml += `
      <div class="mb-2 p-2.5 bg-white/70 dark:bg-zinc-900/70 rounded border border-zinc-200 dark:border-zinc-800 text-[11px] font-mono space-y-1">
        <div><strong class="text-purple-700 dark:text-purple-300">[논리 관계]</strong> ${quiz.logicType || '문맥 추론'}</div>
        <div><strong class="text-purple-700 dark:text-purple-300">[결정적 단서(Clue)]</strong> <span class="bg-purple-100 dark:bg-purple-950 px-1 rounded">${quiz.clue || '본문 논리 흐름'}</span></div>
        ${quiz.direction ? `<div><strong class="text-purple-700 dark:text-purple-300">[논리 방향성]</strong> ${quiz.direction}</div>` : ''}
      </div>
    `;
  }

  expHtml += `<div class="leading-relaxed"><strong>해설:</strong> ${quiz.explanation.replace(/\n/g, '<br>')}</div>`;

  // 선택지 어휘 정밀 분석표 (채점 후 공개)
  if (quiz.vocabBreakdown && quiz.vocabBreakdown.length > 0) {
    expHtml += `
      <div class="mt-2.5 pt-2 border-t border-zinc-200 dark:border-zinc-800">
        <span class="font-mono text-[10px] uppercase font-bold text-zinc-600 dark:text-zinc-400 block mb-1.5">선택지 어휘 정밀 분석 (Lexical Breakdown)</span>
        <div class="grid grid-cols-1 sm:grid-cols-2 gap-1.5 text-[11px] font-mono">
          ${quiz.vocabBreakdown.map(v => `<div class="p-1.5 bg-white dark:bg-zinc-900 border border-zinc-200 dark:border-zinc-800 rounded"><strong>${v.word}</strong>: ${v.meaning}</div>`).join('')}
        </div>
      </div>
    `;
  }

  explanationEl.innerHTML = expHtml;
  checkAllQuizCompleted(passage);
}

function checkAllQuizCompleted(passage) {
  let correct = 0;
  let count = 0;
  const quizzes = state.currentEnrichedQuizzes || [];

  document.querySelectorAll(".quiz-block").forEach(b => {
    const chosen = b.querySelector(".quiz-option.correct, .quiz-option.incorrect");
    if (chosen) {
      count++;
      if (chosen.classList.contains("correct") && !b.querySelector(".quiz-option.incorrect")) {
        correct++;
      }
    }
  });

  const badge = document.getElementById("quiz-score-badge");
  const num = document.getElementById("quiz-score-num");
  if (badge && num) {
    badge.classList.remove("hidden");
    num.textContent = correct;
  }

  if (count === quizzes.length && quizzes.length > 0) {
    if (!state.completedPassages.includes(passage.id)) {
      state.completedPassages.push(passage.id);
      safeStorage.setItem("readflow_completed_passages", JSON.stringify(state.completedPassages));
      const compStatus = document.getElementById("passage-completion-status");
      if (compStatus) compStatus.classList.remove("hidden");
      updateProgressUI();
    }
    showToast(`전체 평가 완료: ${correct} / ${quizzes.length} 정답 👏`);
  }
}

function saveToWrongNotes(wrongItem) {
  const exists = state.wrongQuizzes.some(item => item.question === wrongItem.question);
  if (!exists) {
    state.wrongQuizzes.unshift(wrongItem);
    safeStorage.setItem("readflow_wrong_quizzes", JSON.stringify(state.wrongQuizzes));
    updateProgressUI();
  }
}

// 구문 해설 렌더링
function renderNotesTab(passage) {
  const container = document.getElementById("tab-notes-content");
  if (!container) return;

  const notesHtml = (passage.grammarNotes || []).map(g => `
    <div class="p-3 bg-zinc-50 dark:bg-zinc-900/40 border border-zinc-200 dark:border-zinc-800 rounded-sm">
      <h4 class="font-serif font-bold text-xs text-zinc-900 dark:text-zinc-100 flex items-center space-x-1.5">
        <span class="w-1.5 h-1.5 bg-zinc-800 dark:bg-zinc-200 rounded-full"></span>
        <span>${g.title}</span>
      </h4>
      <p class="mt-1 text-xs text-zinc-600 dark:text-zinc-400 leading-relaxed font-serif">${g.desc}</p>
    </div>
  `).join("");

  const fullTransHtml = passage.sentences.map((s, i) => `
    <div class="mb-3 text-xs font-serif leading-relaxed">
      <span class="font-mono font-bold text-zinc-400 mr-1">[0${i + 1}]</span>
      <span class="text-zinc-800 dark:text-zinc-200">${s.ko}</span>
    </div>
  `).join("");

  container.innerHTML = `
    <div class="space-y-6">
      <div>
        <h3 class="text-xs font-mono uppercase text-zinc-500 mb-2">COMPLETE KOREAN TRANSLATION</h3>
        <div class="p-4 bg-zinc-50 dark:bg-zinc-900/40 border border-zinc-200 dark:border-zinc-800 rounded-sm">
          ${fullTransHtml}
        </div>
      </div>
      <div>
        <h3 class="text-xs font-mono uppercase text-zinc-500 mb-2">SYNTACTIC & GRAMMATICAL NOTES</h3>
        <div class="space-y-2">
          ${notesHtml}
        </div>
      </div>
    </div>
  `;
}

// 플래시카드 렌더링
function renderFlashcardTab(passage) {
  const container = document.getElementById("tab-flashcard-content");
  if (!container) return;

  const list = [...(passage.vocabulary || [])];
  state.savedWords.forEach(sw => {
    if (!list.some(v => v.word.toLowerCase() === sw.word.toLowerCase())) {
      list.push({ word: sw.word, meaning: sw.meaning, pos: "saved", example: "" });
    }
  });

  if (list.length === 0) {
    container.innerHTML = `<p class="text-xs text-zinc-400 font-mono py-8 text-center">암기할 단어가 없습니다.</p>`;
    return;
  }

  if (state.flashcardIdx >= list.length) state.flashcardIdx = 0;
  const current = list[state.flashcardIdx];

  container.innerHTML = `
    <div class="space-y-4">
      <div class="flex items-center justify-between text-xs font-mono text-zinc-500">
        <span>CARD ${state.flashcardIdx + 1} / ${list.length}</span>
        <span>CLICK TO FLIP</span>
      </div>

      <div id="flashcard-box" class="p-8 border border-zinc-300 dark:border-zinc-700 bg-zinc-50 dark:bg-zinc-900 rounded-sm cursor-pointer min-h-[180px] flex flex-col items-center justify-center text-center select-none transition shadow-2xs">
        ${state.flashcardFlipped ? `
          <span class="text-[10px] font-mono uppercase text-zinc-400 mb-1">KOREAN MEANING</span>
          <h4 class="text-xl font-serif font-black text-zinc-900 dark:text-zinc-100">${current.meaning}</h4>
          ${current.example ? `<p class="mt-3 text-xs italic font-serif text-zinc-500 max-w-xs">"${current.example}"</p>` : ''}
        ` : `
          <span class="text-[10px] font-mono uppercase text-zinc-400 mb-1">${current.pos || 'VOCAB'}</span>
          <h3 class="text-2xl font-serif font-black text-zinc-900 dark:text-zinc-100">${current.word}</h3>
          <p class="text-[11px] text-zinc-400 mt-2 font-mono">[CLICK TO REVEAL MEANING]</p>
        `}
      </div>

      <div class="flex items-center justify-between text-xs font-mono pt-2">
        <button id="btn-prev-fc" class="px-3 py-1.5 border border-zinc-300 dark:border-zinc-700 rounded-sm hover:bg-zinc-100 dark:hover:bg-zinc-800">← PREV</button>
        <button id="btn-fc-speak" class="px-3 py-1.5 border border-zinc-300 dark:border-zinc-700 rounded-sm hover:bg-zinc-100 dark:hover:bg-zinc-800">PRONOUNCE 🔊</button>
        <button id="btn-next-fc" class="px-3 py-1.5 border border-zinc-300 dark:border-zinc-700 rounded-sm hover:bg-zinc-100 dark:hover:bg-zinc-800">NEXT →</button>
      </div>
    </div>
  `;

  document.getElementById("flashcard-box").onclick = () => {
    state.flashcardFlipped = !state.flashcardFlipped;
    renderFlashcardTab(passage);
  };
  document.getElementById("btn-prev-fc").onclick = () => {
    state.flashcardFlipped = false;
    state.flashcardIdx = (state.flashcardIdx - 1 + list.length) % list.length;
    renderFlashcardTab(passage);
  };
  document.getElementById("btn-next-fc").onclick = () => {
    state.flashcardFlipped = false;
    state.flashcardIdx = (state.flashcardIdx + 1) % list.length;
    renderFlashcardTab(passage);
  };
  document.getElementById("btn-fc-speak").onclick = () => speakWord(current.word);
}

// 탭 5: Master DB 사전 직접 검색
function initDictionaryTab() {
  const input = document.getElementById("dict-tab-search-input");
  const btn = document.getElementById("dict-tab-search-btn");
  const container = document.getElementById("dict-tab-result-container");
  if (!input || !btn || !container) return;

  function doSearch() {
    const q = input.value.trim().toLowerCase();
    if (!q) return;

    const meanings = WORDTEST_MAP.get(q);
    const dbCountLabel = WORDTEST_MAP.size > 0 ? `${WORDTEST_MAP.size.toLocaleString()} DB` : "Master DB";
    if (meanings && meanings.length > 0) {
      const meaningStr = meanings.join(", ");
      container.innerHTML = `
        <div class="p-4 border border-zinc-200 dark:border-zinc-800 rounded-sm bg-white dark:bg-zinc-900 shadow-xs space-y-3">
          <div class="flex items-center justify-between">
            <div class="flex items-baseline space-x-2">
              <h4 class="font-serif font-black text-xl text-zinc-900 dark:text-zinc-100">${q}</h4>
              <span class="text-[10px] font-mono px-1.5 py-0.5 bg-emerald-100 text-emerald-800 dark:bg-emerald-950 dark:text-emerald-300 font-bold rounded-xs">${dbCountLabel}</span>
            </div>
            <button id="dict-search-speak-btn" class="p-1.5 text-zinc-500 hover:text-zinc-900 dark:hover:text-white" title="발음 청취">
              🔊
            </button>
          </div>
          <div>
            <span class="text-[10px] font-mono uppercase text-zinc-400">KOREAN MEANINGS</span>
            <p class="font-serif text-sm font-bold text-zinc-900 dark:text-zinc-100 mt-0.5 leading-snug">${meaningStr}</p>
          </div>
          <div class="pt-2 border-t border-zinc-100 dark:border-zinc-800 flex justify-end">
            <button id="dict-search-save-btn" class="text-xs font-mono px-3 py-1 bg-zinc-900 text-white dark:bg-white dark:text-zinc-900 rounded-xs hover:opacity-90 font-bold">
              ★ 단어장 저장
            </button>
          </div>
        </div>
      `;
      document.getElementById("dict-search-speak-btn").onclick = () => speakWord(q);
      document.getElementById("dict-search-save-btn").onclick = () => {
        toggleSaveWord(q, meaningStr);
      };
    } else {
      container.innerHTML = `
        <div class="p-4 text-center border border-zinc-200 dark:border-zinc-800 rounded-sm bg-white dark:bg-zinc-900 text-xs font-mono text-zinc-500">
          '${q}' 단어는 마스터 어휘 DB(${dbCountLabel})에 등록되어 있지 않습니다.
          <p class="mt-2 text-zinc-400 font-serif">철자를 확인하거나 다른 표제어를 검색해 보세요.</p>
        </div>
      `;
    }
  }

  btn.onclick = doSearch;
  input.onkeydown = e => { if (e.key === "Enter") doSearch(); };
}

// ==========================================
// MODAL 1: 서재 라이브러리 브라우저
// ==========================================
function openLibraryModal() {
  const allCount = state.passages.length;
  const bCount = state.passages.filter(p => p.level === "Beginner").length;
  const iCount = state.passages.filter(p => p.level === "Intermediate").length;
  const aCount = state.passages.filter(p => p.level === "Advanced").length;
  document.querySelectorAll(".lib-filter-btn").forEach(btn => {
    const lvl = btn.getAttribute("data-level");
    if (lvl === "All") btn.textContent = `전체 (${allCount})`;
    else if (lvl === "Beginner") btn.textContent = `초급 (${bCount})`;
    else if (lvl === "Intermediate") btn.textContent = `중급 (${iCount})`;
    else if (lvl === "Advanced") btn.textContent = `고급 (${aCount})`;
  });
  renderLibraryGrid(state.filterLevel, "");
  document.getElementById("library-modal").classList.remove("hidden");
}

function renderLibraryGrid(level, searchQuery) {
  const container = document.getElementById("library-passage-grid");
  if (!container) return;

  let filtered = state.passages;
  if (level !== "All") {
    filtered = filtered.filter(p => p.level === level);
  }
  if (searchQuery && searchQuery.trim() !== "") {
    const q = searchQuery.toLowerCase();
    filtered = filtered.filter(p => 
      p.title.toLowerCase().includes(q) || 
      (p.koreanTitle && p.koreanTitle.toLowerCase().includes(q)) ||
      (p.category && p.category.toLowerCase().includes(q))
    );
  }

  if (filtered.length === 0) {
    container.innerHTML = `<div class="col-span-2 text-center py-12 text-xs font-mono text-zinc-400">조건에 맞는 지문이 없습니다.</div>`;
    return;
  }

  container.innerHTML = filtered.map(p => {
    const isCompleted = state.completedPassages.includes(p.id);
    return `
      <div class="lib-card p-3.5 border border-zinc-200 dark:border-zinc-800 rounded-sm bg-white dark:bg-zinc-900/60 hover:border-zinc-900 dark:hover:border-zinc-400 cursor-pointer transition flex flex-col justify-between shadow-2xs" data-pid="${p.id}">
        <div>
          <div class="flex items-center justify-between text-[11px] font-mono text-zinc-400 mb-1">
            <span class="px-1.5 py-0.2 border border-zinc-200 dark:border-zinc-700 uppercase font-bold text-zinc-700 dark:text-zinc-300 rounded-xs">${p.level}</span>
            <div class="flex items-center space-x-1">
              ${isCompleted ? `<span class="text-emerald-600 font-bold">✓ 완독</span>` : ''}
              <span>${p.source || 'Journal'}</span>
            </div>
          </div>
          <h4 class="font-serif font-bold text-sm text-zinc-900 dark:text-zinc-100 leading-snug">${p.title}</h4>
          <p class="font-serif text-xs text-zinc-500 dark:text-zinc-400 mt-0.5">${p.koreanTitle || ''}</p>
        </div>
        <div class="mt-3 pt-2 border-t border-zinc-100 dark:border-zinc-800/80 flex items-center justify-between text-[10px] font-mono text-zinc-400">
          <span>${p.wordCount || 150} WORDS</span>
          <span class="underline text-zinc-700 dark:text-zinc-300 font-bold">READ ESSAY →</span>
        </div>
      </div>
    `;
  }).join("");

  container.querySelectorAll(".lib-card").forEach(c => {
    c.onclick = () => {
      const pid = c.getAttribute("data-pid");
      loadPassage(pid);
      document.getElementById("library-modal").classList.add("hidden");
    };
  });
}

// ==========================================
// MODAL 2: wordtest1 연동 단어 시험 (Word Test)
// ==========================================
function openWordTestModal() {
  generateNewWordTest();
  document.getElementById("wordtest-modal").classList.remove("hidden");
}

function generateNewWordTest() {
  const container = document.getElementById("wordtest-container");
  const scoreDisp = document.getElementById("wordtest-score-display");
  scoreDisp.textContent = "점수: - / 10";

  let pool = [];
  if (typeof defaultWords !== "undefined" && Array.isArray(defaultWords) && defaultWords.length > 50) {
    pool = defaultWords;
  } else {
    pool = [
      { word: "abandon", meanings: ["버리다", "포기하다"] },
      { word: "abate", meanings: ["줄이다", "완화하다"] },
      { word: "resilient", meanings: ["회복력 있는", "탄력적인"] },
      { word: "sustainability", meanings: ["지속 가능성"] },
      { word: "essential", meanings: ["필수적인"] },
      { word: "ubiquitous", meanings: ["어디에나 존재하는"] },
      { word: "paradox", meanings: ["역설"] },
      { word: "consequence", meanings: ["결과", "영향"] },
      { word: "clarity", meanings: ["명료함"] },
      { word: "mitigate", meanings: ["완화하다"] }
    ];
  }

  const testItems = [];
  const shuffled = [...pool].sort(() => 0.5 - Math.random());
  for (let i = 0; i < 10; i++) {
    const target = shuffled[i];
    const correctMeaning = (target.meanings || ["뜻"]).join(", ");

    const wrongOptions = [];
    while (wrongOptions.length < 3) {
      const rand = pool[Math.floor(Math.random() * pool.length)];
      const m = (rand.meanings || ["다른 뜻"]).join(", ");
      if (rand.word !== target.word && !wrongOptions.includes(m) && m !== correctMeaning) {
        wrongOptions.push(m);
      }
    }

    const options = [correctMeaning, ...wrongOptions].sort(() => 0.5 - Math.random());
    testItems.push({
      id: i + 1,
      word: target.word,
      correct: correctMeaning,
      options: options,
      selectedIndex: -1
    });
  }

  state.currentWordTest = testItems;

  container.innerHTML = testItems.map((item, idx) => `
    <div class="wt-item p-3.5 border border-zinc-200 dark:border-zinc-800 rounded-sm bg-zinc-50/50 dark:bg-zinc-900/40" data-idx="${idx}">
      <div class="flex items-center justify-between">
        <span class="font-serif font-black text-base text-zinc-900 dark:text-zinc-100">${idx + 1}. ${item.word}</span>
        <button class="wt-speak-btn text-zinc-400 hover:text-zinc-800 dark:hover:text-white" data-word="${item.word}">🔊</button>
      </div>
      <div class="mt-2.5 grid grid-cols-1 sm:grid-cols-2 gap-2 text-xs font-serif">
        ${item.options.map((opt, optIdx) => `
          <button class="wt-opt-btn text-left p-2 border border-zinc-200 dark:border-zinc-700 rounded-sm bg-white dark:bg-zinc-800 hover:border-zinc-900 dark:hover:border-zinc-400 transition" data-itemidx="${idx}" data-optidx="${optIdx}">
            <span class="font-mono text-zinc-400 mr-1">${String.fromCharCode(65 + optIdx)}.</span>
            <span>${opt}</span>
          </button>
        `).join("")}
      </div>
      <div class="wt-feedback hidden mt-2 text-xs font-serif"></div>
    </div>
  `).join("");

  container.querySelectorAll(".wt-speak-btn").forEach(btn => {
    btn.onclick = () => speakWord(btn.getAttribute("data-word"));
  });

  container.querySelectorAll(".wt-opt-btn").forEach(btn => {
    btn.onclick = () => {
      const itemIdx = parseInt(btn.getAttribute("data-itemidx"), 10);
      const optIdx = parseInt(btn.getAttribute("data-optidx"), 10);
      state.currentWordTest[itemIdx].selectedIndex = optIdx;

      const parent = document.querySelectorAll(".wt-item")[itemIdx];
      parent.querySelectorAll(".wt-opt-btn").forEach(b => b.classList.remove("border-zinc-900", "bg-zinc-100", "font-bold", "dark:border-white", "dark:bg-zinc-700"));
      btn.classList.add("border-zinc-900", "bg-zinc-100", "font-bold", "dark:border-white", "dark:bg-zinc-700");
    };
  });
}

function submitWordTest() {
  let correctCount = 0;
  state.currentWordTest.forEach((item, idx) => {
    const parent = document.querySelectorAll(".wt-item")[idx];
    const feedback = parent.querySelector(".wt-feedback");
    const selectedOpt = item.options[item.selectedIndex];
    const isCorrect = selectedOpt === item.correct;

    feedback.classList.remove("hidden");
    if (isCorrect) {
      correctCount++;
      feedback.className = "wt-feedback mt-2 text-xs font-serif text-emerald-600 font-bold";
      feedback.textContent = `✓ 정답! (${item.correct})`;
    } else {
      feedback.className = "wt-feedback mt-2 text-xs font-serif text-rose-600 font-bold";
      feedback.textContent = `✕ 오답 (정답: ${item.correct})`;

      if (!state.wrongWords.some(w => w.word === item.word)) {
        state.wrongWords.unshift({ word: item.word, meaning: item.correct, date: new Date().toLocaleDateString() });
        safeStorage.setItem("readflow_wrong_words", JSON.stringify(state.wrongWords));
      }
    }
  });

  document.getElementById("wordtest-score-display").textContent = `점수: ${correctCount} / 10`;
  updateProgressUI();
  showToast(`단어 테스트 완료: 10문제 중 ${correctCount}문제 정답!`);
}

// ==========================================
// MODAL 3: 독해 오답노트 (Wrong Answers Notebook)
// ==========================================
function openWrongNotesModal() {
  renderWrongNotes(state.wrongNotesFilter);
  document.getElementById("wrongnotes-modal").classList.remove("hidden");
}

function renderWrongNotes(filterType = "all") {
  state.wrongNotesFilter = filterType;
  const container = document.getElementById("wrongnotes-container");
  if (!container) return;

  // 필터 버튼 활성화 스타일
  const filterButtons = [
    { id: "filter-wn-all", type: "all" },
    { id: "filter-wn-quiz", type: "quiz" },
    { id: "filter-wn-cloze", type: "cloze" },
    { id: "filter-wn-order", type: "order" },
    { id: "filter-wn-logic", type: "logic" },
    { id: "filter-wn-words", type: "words" }
  ];

  filterButtons.forEach(btnInfo => {
    const el = document.getElementById(btnInfo.id);
    if (el) {
      if (filterType === btnInfo.type) {
        el.className = btnInfo.type === "logic"
          ? "px-2 py-0.5 border border-purple-700 bg-purple-700 text-white rounded-xs font-bold"
          : "px-2 py-0.5 border border-zinc-800 bg-zinc-800 text-white dark:border-white dark:bg-white dark:text-zinc-900 rounded-xs font-bold";
      } else {
        el.className = btnInfo.type === "logic"
          ? "px-2 py-0.5 border border-purple-300 dark:border-purple-700 text-purple-700 dark:text-purple-300 rounded-xs"
          : "px-2 py-0.5 border border-zinc-300 dark:border-zinc-700 rounded-xs";
      }
    }
  });

  if (state.wrongQuizzes.length === 0 && state.wrongWords.length === 0) {
    container.innerHTML = `
      <div class="text-center py-12 text-xs font-mono text-zinc-400">
        <p>오답노트가 비어 있습니다.</p>
        <p class="mt-1">독해 퀴즈, 빈칸 추론, 순서 배열, 편입 논리 문제를 풀며 틀린 문항이 이곳에 자동 누적됩니다.</p>
      </div>
    `;
    return;
  }

  let html = "";

  // 퀴즈 항목 필터링
  let filteredQuizzes = [];
  if (filterType === "all") {
    filteredQuizzes = state.wrongQuizzes;
  } else if (filterType === "quiz") {
    filteredQuizzes = state.wrongQuizzes.filter(q => !q.type || q.type === "comprehension");
  } else if (filterType === "cloze") {
    filteredQuizzes = state.wrongQuizzes.filter(q => q.type === "cloze");
  } else if (filterType === "order") {
    filteredQuizzes = state.wrongQuizzes.filter(q => q.type === "order");
  } else if (filterType === "logic") {
    filteredQuizzes = state.wrongQuizzes.filter(q => q.type === "logic");
  }

  if (filterType !== "words" && filteredQuizzes.length > 0) {
    html += `<h4 class="text-xs font-mono uppercase text-zinc-500 mb-2">WRONG QUESTIONS (${filteredQuizzes.length})</h4>`;
    html += filteredQuizzes.map((item) => {
      const idx = state.wrongQuizzes.indexOf(item);
      let badgeHtml = "";
      if (item.type === "logic") {
        badgeHtml = `<span class="px-1.5 py-0.5 text-[9px] font-mono bg-purple-100 text-purple-800 dark:bg-purple-950/60 dark:text-purple-300 font-bold rounded">편입 논리</span>`;
      } else if (item.type === "cloze") {
        badgeHtml = `<span class="px-1.5 py-0.5 text-[9px] font-mono bg-emerald-100 text-emerald-800 dark:bg-emerald-950/60 dark:text-emerald-300 font-bold rounded">빈칸 추론</span>`;
      } else if (item.type === "order") {
        badgeHtml = `<span class="px-1.5 py-0.5 text-[9px] font-mono bg-amber-100 text-amber-800 dark:bg-amber-950/60 dark:text-amber-300 font-bold rounded">문단 순서</span>`;
      } else {
        badgeHtml = `<span class="px-1.5 py-0.5 text-[9px] font-mono bg-blue-100 text-blue-800 dark:bg-blue-950/60 dark:text-blue-300 font-bold rounded">독해 일치</span>`;
      }

      return `
        <div class="p-3.5 border border-rose-200 dark:border-rose-900/60 rounded-sm bg-rose-50/30 dark:bg-rose-950/20 text-xs font-serif space-y-1.5 mb-3" data-wn-qidx="${idx}">
          <div class="flex items-center justify-between text-[11px] font-mono text-zinc-400">
            <div class="flex items-center space-x-1.5">
              ${badgeHtml}
              <span class="font-bold text-zinc-700 dark:text-zinc-300">${item.passageTitle}</span>
            </div>
            <div class="flex items-center space-x-2">
              <span>${item.date}</span>
              <button class="btn-remove-wrong-quiz text-rose-500 hover:text-rose-700 font-mono" data-idx="${idx}" title="삭제">✕</button>
            </div>
          </div>

          ${item.logicType ? `
            <div class="text-[10px] font-mono text-purple-700 dark:text-purple-400">
              [논리 유형: ${item.logicType}] · [단서 Clue: ${item.clue || '문맥 대조'}]
            </div>
          ` : ''}

          <p class="font-bold text-zinc-900 dark:text-zinc-100">${item.question}</p>
          ${item.questionKo ? `<p class="text-zinc-500">${item.questionKo}</p>` : ''}

          <div class="mt-2 pt-2 border-t border-rose-100 dark:border-rose-900/40 text-[11px] space-y-1">
            <div class="text-rose-600"><strong>내가 골랐던 오답:</strong> ${item.selected}</div>
            <div class="text-emerald-700 dark:text-emerald-400"><strong>실제 정답:</strong> ${item.correct}</div>
            <div class="text-zinc-600 dark:text-zinc-400 mt-1 pl-2 border-l-2 border-zinc-300"><strong>해설:</strong> ${item.explanation}</div>
            
            ${item.vocabBreakdown && item.vocabBreakdown.length > 0 ? `
              <div class="mt-2 pt-1.5 border-t border-rose-100 dark:border-rose-900/30">
                <span class="font-mono text-[10px] uppercase font-bold text-zinc-500 block mb-1">선택지 어휘 복습</span>
                <div class="grid grid-cols-1 sm:grid-cols-2 gap-1 text-[10px] font-mono">
                  ${item.vocabBreakdown.map(v => `<div class="p-1 bg-white dark:bg-zinc-900 rounded border border-rose-100 dark:border-zinc-800"><strong>${v.word}</strong>: ${v.meaning}</div>`).join('')}
                </div>
              </div>
            ` : ''}
          </div>
        </div>
      `;
    }).join("");
  }

  // 어휘 오답 항목
  if ((filterType === "all" || filterType === "words") && state.wrongWords.length > 0) {
    html += `<h4 class="text-xs font-mono uppercase text-zinc-500 mt-4 mb-2">WRONG VOCABULARY (${state.wrongWords.length})</h4>`;
    html += `<div class="grid grid-cols-1 sm:grid-cols-2 gap-2">`;
    html += state.wrongWords.map((w, wIdx) => `
      <div class="p-2.5 border border-zinc-200 dark:border-zinc-800 rounded-sm bg-zinc-50 dark:bg-zinc-900 flex items-center justify-between text-xs font-serif">
        <div>
          <span class="font-bold text-zinc-900 dark:text-zinc-100">${w.word}</span>
          <p class="text-zinc-500 text-[11px]">${w.meaning}</p>
        </div>
        <div class="flex items-center space-x-1">
          <button class="speak-wn-word text-zinc-400 hover:text-zinc-800" data-word="${w.word}">🔊</button>
          <button class="btn-remove-wrong-word text-zinc-400 hover:text-rose-600 font-mono text-xs px-1" data-widx="${wIdx}" title="삭제">✕</button>
        </div>
      </div>
    `).join("");
    html += `</div>`;
  }

  container.innerHTML = html;

  container.querySelectorAll(".speak-wn-word").forEach(btn => {
    btn.onclick = () => speakWord(btn.getAttribute("data-word"));
  });

  container.querySelectorAll(".btn-remove-wrong-quiz").forEach(btn => {
    btn.onclick = () => {
      const idx = parseInt(btn.getAttribute("data-idx"), 10);
      state.wrongQuizzes.splice(idx, 1);
      safeStorage.setItem("readflow_wrong_quizzes", JSON.stringify(state.wrongQuizzes));
      renderWrongNotes(filterType);
      updateProgressUI();
      showToast("오답 항목이 삭제되었습니다.");
    };
  });

  container.querySelectorAll(".btn-remove-wrong-word").forEach(btn => {
    btn.onclick = () => {
      const idx = parseInt(btn.getAttribute("data-widx"), 10);
      state.wrongWords.splice(idx, 1);
      safeStorage.setItem("readflow_wrong_words", JSON.stringify(state.wrongWords));
      renderWrongNotes(filterType);
      updateProgressUI();
      showToast("단어가 오답노트에서 삭제되었습니다.");
    };
  });
}

// ==========================================
// LOGIC LAB (편입 논리완성 실전 훈련 뷰) CONTROLLER
// ==========================================
// ==========================================
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
}

function exportWrongNotes() {
  if (state.wrongQuizzes.length === 0 && state.wrongWords.length === 0) {
    showToast("내보낼 오답 데이터가 없습니다.");
    return;
  }
  let text = "# READFLOW 오답노트 정리\n\n";
  if (state.wrongQuizzes.length > 0) {
    text += "## [독해 퀴즈 오답]\n";
    state.wrongQuizzes.forEach((q, i) => {
      text += `${i + 1}. [${q.passageTitle}] ${q.question}\n`;
      text += `   - 내가 고른 답: ${q.selected}\n`;
      text += `   - 실제 정답: ${q.correct}\n`;
      text += `   - 해설: ${q.explanation}\n\n`;
    });
  }
  if (state.wrongWords.length > 0) {
    text += "## [틀린 어휘]\n";
    state.wrongWords.forEach(w => {
      text += `- ${w.word}: ${w.meaning}\n`;
    });
  }

  navigator.clipboard.writeText(text).then(() => {
    showToast("오답노트가 클립보드에 복사되었습니다! 📋");
  }).catch(() => {
    showToast("클립보드 복사 실패");
  });
}

function backupJSONData() {
  const data = {
    wrongQuizzes: state.wrongQuizzes,
    wrongWords: state.wrongWords,
    savedWords: state.savedWords,
    completedPassages: state.completedPassages,
    timestamp: new Date().toISOString()
  };
  const blob = new Blob([JSON.stringify(data, null, 2)], { type: "application/json" });
  const url = URL.createObjectURL(blob);
  const a = document.createElement("a");
  a.href = url;
  a.download = `readflow_backup_${new Date().toISOString().slice(0, 10)}.json`;
  a.click();
  URL.revokeObjectURL(url);
  showToast("오답 및 학습 백업 파일이 저장되었습니다. 💾");
}

function restoreJSONData(event) {
  const file = event.target.files?.[0];
  if (!file) return;
  const reader = new FileReader();
  reader.onload = e => {
    try {
      const data = JSON.parse(e.target.result);
      if (Array.isArray(data.wrongQuizzes)) {
        state.wrongQuizzes = data.wrongQuizzes;
        safeStorage.setItem("readflow_wrong_quizzes", JSON.stringify(state.wrongQuizzes));
      }
      if (Array.isArray(data.wrongWords)) {
        state.wrongWords = data.wrongWords;
        safeStorage.setItem("readflow_wrong_words", JSON.stringify(state.wrongWords));
      }
      if (Array.isArray(data.savedWords)) {
        state.savedWords = data.savedWords;
        safeStorage.setItem("readflow_saved_words", JSON.stringify(state.savedWords));
      }
      if (Array.isArray(data.completedPassages)) {
        state.completedPassages = data.completedPassages;
        safeStorage.setItem("readflow_completed_passages", JSON.stringify(state.completedPassages));
      }
      renderWrongNotes(state.wrongNotesFilter);
      renderSavedWords();
      updateProgressUI();
      showToast("백업 데이터가 성공적으로 복원되었습니다! ✅");
    } catch (err) {
      showToast("올바른 백업 파일 형식이 아닙니다.");
    }
  };
  reader.readAsText(file);
}

// ==========================================
// TTS & AUDIO
// ==========================================
function speakSentence(idx) {
  if (!speechSynth) {
    showToast("음성 낭독(TTS)이 지원되지 않는 브라우저입니다.");
    return;
  }
  stopTTS();
  const passage = state.passages.find(p => p.id === state.currentPassageId);
  if (!passage || !passage.sentences[idx]) return;

  state.currentSentenceIdx = idx;
  highlightSentence(idx);
  updateReadingProgressBar();

  const text = passage.sentences[idx].en;
  currentUtterance = new SpeechSynthesisUtterance(text);
  currentUtterance.lang = "en-US";
  currentUtterance.rate = state.ttsSpeed;
  if (state.ttsVoice) currentUtterance.voice = state.ttsVoice;

  currentUtterance.onend = () => {
    unhighlightSentence();
    state.currentSentenceIdx = -1;
    updateTTSPlayButton(false);
    updateReadingProgressBar();
  };
  currentUtterance.onerror = () => {
    unhighlightSentence();
    state.currentSentenceIdx = -1;
    updateTTSPlayButton(false);
    updateReadingProgressBar();
  };

  updateTTSPlayButton(true);
  try {
    speechSynth.speak(currentUtterance);
  } catch (e) {
    console.warn("speechSynth.speak error:", e);
    stopTTS();
  }
}

function playEntirePassage() {
  if (!speechSynth) {
    showToast("음성 낭독(TTS)이 지원되지 않는 브라우저입니다.");
    return;
  }
  const passage = state.passages.find(p => p.id === state.currentPassageId);
  if (!passage) return;

  if (state.isPlayingTTS) {
    stopTTS();
    return;
  }

  let idx = 0;
  state.isPlayingTTS = true;
  updateTTSPlayButton(true);

  function next() {
    if (!state.isPlayingTTS) return;
    if (idx < passage.sentences.length) {
      state.currentSentenceIdx = idx;
      highlightSentence(idx);
      updateReadingProgressBar();
      currentUtterance = new SpeechSynthesisUtterance(passage.sentences[idx].en);
      currentUtterance.lang = "en-US";
      currentUtterance.rate = state.ttsSpeed;
      if (state.ttsVoice) currentUtterance.voice = state.ttsVoice;
      currentUtterance.onend = () => {
        if (!state.isPlayingTTS) return;
        idx++;
        setTimeout(next, 300);
      };
      currentUtterance.onerror = () => stopTTS();
      try {
        speechSynth.speak(currentUtterance);
      } catch (e) {
        console.warn("speechSynth.speak error:", e);
        stopTTS();
      }
    } else {
      stopTTS();
      showToast("지문 낭독 완료");
    }
  }
  next();
}

function stopTTS() {
  if (speechSynth) speechSynth.cancel();
  state.isPlayingTTS = false;
  state.currentSentenceIdx = -1;
  unhighlightSentence();
  updateTTSPlayButton(false);
  updateReadingProgressBar();
}

function speakWord(word) {
  if (!speechSynth) return;
  speechSynth.cancel();
  const u = new SpeechSynthesisUtterance(word);
  u.lang = "en-US";
  u.rate = 0.9;
  if (state.ttsVoice) u.voice = state.ttsVoice;
  speechSynth.speak(u);
}

function highlightSentence(idx) {
  unhighlightSentence();
  const target = document.querySelector(`.sentence-item[data-idx="${idx}"]`);
  if (target) {
    target.classList.add("speaking-active");
    target.scrollIntoView({ behavior: "smooth", block: "nearest" });
  }
}

function unhighlightSentence() {
  document.querySelectorAll(".sentence-item.speaking-active").forEach(el => {
    el.classList.remove("speaking-active");
  });
}

function updateTTSPlayButton(isPlaying) {
  const playIcon = document.getElementById("tts-play-icon");
  const playText = document.getElementById("tts-play-text");
  const audioWave = document.getElementById("tts-audio-wave");
  if (!playText) return;

  if (isPlaying) {
    if (playIcon) playIcon.innerHTML = `<rect x="6" y="4" width="4" height="16"/><rect x="14" y="4" width="4" height="16"/>`;
    playText.textContent = "PAUSE";
    if (audioWave) audioWave.classList.remove("hidden");
  } else {
    if (playIcon) playIcon.innerHTML = `<path d="M8 5v14l11-7z"/>`;
    playText.textContent = "PLAY AUDIO";
    if (audioWave) audioWave.classList.add("hidden");
  }
}

function updateReadingProgressBar() {
  const p = state.passages.find(x => x.id === state.currentPassageId);
  const progressBar = document.getElementById("reading-progress-bar");
  if (!p || !progressBar) return;

  if (state.currentSentenceIdx >= 0) {
    const pct = Math.min(100, Math.round(((state.currentSentenceIdx + 1) / p.sentences.length) * 100));
    progressBar.style.width = `${pct}%`;
  } else {
    const totalHeight = document.documentElement.scrollHeight - window.innerHeight;
    if (totalHeight > 0) {
      const scrollPct = Math.min(100, Math.max(0, (window.scrollY / totalHeight) * 100));
      progressBar.style.width = `${scrollPct}%`;
    }
  }
}
window.addEventListener("scroll", updateReadingProgressBar);

// ==========================================
// KEYBOARD SHORTCUTS
// ==========================================
function setupKeyboardShortcuts() {
  document.addEventListener("keydown", e => {
    if (["INPUT", "TEXTAREA", "SELECT"].includes(document.activeElement.tagName)) {
      return;
    }

    if (e.key === "Escape") {
      document.querySelectorAll(".fixed.inset-0:not(.hidden)").forEach(el => el.classList.add("hidden"));
      closeWordPopup();
      return;
    }

    if (e.key === "?") {
      const modal = document.getElementById("shortcuts-modal");
      if (modal) modal.classList.toggle("hidden");
      return;
    }

    if (e.code === "Space") {
      e.preventDefault();
      playEntirePassage();
      return;
    }

    if (e.key === "j" || e.key === "J") {
      const passage = state.passages.find(p => p.id === state.currentPassageId);
      if (passage) {
        let nextIdx = state.currentSentenceIdx + 1;
        if (nextIdx >= passage.sentences.length) nextIdx = 0;
        speakSentence(nextIdx);
      }
      return;
    }

    if (e.key === "k" || e.key === "K") {
      const passage = state.passages.find(p => p.id === state.currentPassageId);
      if (passage) {
        let prevIdx = state.currentSentenceIdx - 1;
        if (prevIdx < 0) prevIdx = passage.sentences.length - 1;
        speakSentence(prevIdx);
      }
      return;
    }

    if (e.key === "n" || e.key === "N") {
      navigatePassage(1);
      return;
    }

    if (e.key === "p" || e.key === "P") {
      navigatePassage(-1);
      return;
    }

    // 1-4 퀴즈 번호 키
    if (["1", "2", "3", "4"].includes(e.key)) {
      const optIdx = parseInt(e.key, 10) - 1;
      const unansweredBlock = Array.from(document.querySelectorAll(".quiz-block")).find(b => !b.querySelector(".quiz-option.correct, .quiz-option.incorrect"));
      if (unansweredBlock) {
        const qIdx = parseInt(unansweredBlock.getAttribute("data-qidx"), 10);
        const passage = state.passages.find(p => p.id === state.currentPassageId);
        if (passage) {
          handleQuizAnswer(passage, qIdx, optIdx);
        }
      }
    }
  });
}

// ==========================================
// EVENT LISTENERS SETUP
// ==========================================
function setupEventListeners() {
  // 테마 전환 버튼들
  document.getElementById("theme-btn-light")?.addEventListener("click", () => setTheme("light"));
  document.getElementById("theme-btn-sepia")?.addEventListener("click", () => setTheme("sepia"));
  document.getElementById("theme-btn-dark")?.addEventListener("click", () => setTheme("dark"));

  // 단축키 모달
  document.getElementById("btn-open-shortcuts")?.addEventListener("click", () => {
    document.getElementById("shortcuts-modal").classList.remove("hidden");
  });
  document.getElementById("btn-close-shortcuts-modal")?.addEventListener("click", () => {
    document.getElementById("shortcuts-modal").classList.add("hidden");
  });
  document.getElementById("shortcuts-modal-overlay")?.addEventListener("click", () => {
    document.getElementById("shortcuts-modal").classList.add("hidden");
  });

  // 독해 난이도 탭 클릭 (전체, 초급, 중급, 고급)
  document.getElementById("level-tab-all")?.addEventListener("click", () => setLevelTab("All"));
  document.getElementById("level-tab-b")?.addEventListener("click", () => setLevelTab("Beginner"));
  document.getElementById("level-tab-i")?.addEventListener("click", () => setLevelTab("Intermediate"));
  document.getElementById("level-tab-a")?.addEventListener("click", () => setLevelTab("Advanced"));

  // 독해 분량/형식 모드 스위치 (구문·단문 vs 실전 중·장문)
  document.getElementById("btn-mode-clause")?.addEventListener("click", () => setPassageLengthMode("clause"));
  document.getElementById("btn-mode-full")?.addEventListener("click", () => setPassageLengthMode("full"));

  // 이전/다음 지문
  document.getElementById("btn-prev-passage")?.addEventListener("click", () => navigatePassage(-1));
  document.getElementById("btn-next-passage")?.addEventListener("click", () => navigatePassage(1));

  // TTS
  document.getElementById("btn-tts-play")?.addEventListener("click", playEntirePassage);
  document.getElementById("btn-tts-stop")?.addEventListener("click", stopTTS);
  document.getElementById("select-tts-speed")?.addEventListener("change", e => state.ttsSpeed = parseFloat(e.target.value));
  document.getElementById("select-tts-voice")?.addEventListener("change", e => {
    state.ttsVoice = state.availableVoices[parseInt(e.target.value, 10)] || null;
  });

  // 독해 모드 토글
  document.getElementById("toggle-chunk-mode")?.addEventListener("change", e => {
    state.chunkMode = e.target.checked;
    refreshPassage();
  });
  document.getElementById("toggle-direct-trans")?.addEventListener("change", e => {
    state.directTranslation = e.target.checked;
    refreshPassage();
  });
  document.getElementById("toggle-cloze-mode")?.addEventListener("change", e => {
    state.clozeMode = e.target.checked;
    refreshPassage();
    if (e.target.checked) showToast("빈칸 모드 활성화: [···] 클릭 시 정답 공개");
  });

  // 글자 크기
  const sizeInd = document.getElementById("font-size-indicator");
  document.getElementById("btn-font-decrease")?.addEventListener("click", () => {
    if (state.fontSize > 14) {
      state.fontSize -= 2;
      document.getElementById("passage-text-container").style.fontSize = `${state.fontSize}px`;
      if (sizeInd) sizeInd.textContent = `${state.fontSize}px`;
    }
  });
  document.getElementById("btn-font-increase")?.addEventListener("click", () => {
    if (state.fontSize < 30) {
      state.fontSize += 2;
      document.getElementById("passage-text-container").style.fontSize = `${state.fontSize}px`;
      if (sizeInd) sizeInd.textContent = `${state.fontSize}px`;
    }
  });

  // 탭 전환
  document.querySelectorAll(".tab-link").forEach(btn => {
    btn.onclick = () => switchTab(btn.getAttribute("data-tab"));
  });

  // 서재 모달
  document.getElementById("btn-open-library-modal")?.addEventListener("click", openLibraryModal);
  document.getElementById("btn-close-library-modal")?.addEventListener("click", () => document.getElementById("library-modal").classList.add("hidden"));
  document.getElementById("library-modal-overlay")?.addEventListener("click", () => document.getElementById("library-modal").classList.add("hidden"));

  // 서재 필터 & 검색
  document.querySelectorAll(".lib-filter-btn").forEach(btn => {
    btn.onclick = () => {
      document.querySelectorAll(".lib-filter-btn").forEach(b => b.className = "lib-filter-btn px-3 py-1 border border-zinc-300 dark:border-zinc-700 rounded-xs");
      btn.className = "lib-filter-btn px-3 py-1 border border-zinc-900 bg-zinc-900 text-white dark:border-white dark:bg-white dark:text-zinc-900 rounded-xs font-bold";
      state.filterLevel = btn.getAttribute("data-level");
      renderLibraryGrid(state.filterLevel, document.getElementById("input-search-library").value);
    };
  });
  document.getElementById("input-search-library")?.addEventListener("input", e => {
    renderLibraryGrid(state.filterLevel, e.target.value);
  });

  // 단어 시험 모달
  document.getElementById("btn-open-wordtest-modal")?.addEventListener("click", openWordTestModal);
  document.getElementById("btn-close-wordtest-modal")?.addEventListener("click", () => document.getElementById("wordtest-modal").classList.add("hidden"));
  document.getElementById("wordtest-modal-overlay")?.addEventListener("click", () => document.getElementById("wordtest-modal").classList.add("hidden"));
  document.getElementById("btn-new-wordtest")?.addEventListener("click", generateNewWordTest);
  document.getElementById("btn-submit-wordtest")?.addEventListener("click", submitWordTest);

  // 오답노트 모달
  document.getElementById("btn-open-wrongnotes-modal")?.addEventListener("click", openWrongNotesModal);
  document.getElementById("btn-close-wrongnotes-modal")?.addEventListener("click", () => document.getElementById("wrongnotes-modal").classList.add("hidden"));
  document.getElementById("wrongnotes-modal-overlay")?.addEventListener("click", () => document.getElementById("wrongnotes-modal").classList.add("hidden"));
  document.getElementById("filter-wn-all")?.addEventListener("click", () => renderWrongNotes("all"));
  document.getElementById("filter-wn-quiz")?.addEventListener("click", () => renderWrongNotes("quiz"));
  document.getElementById("filter-wn-cloze")?.addEventListener("click", () => renderWrongNotes("cloze"));
  document.getElementById("filter-wn-order")?.addEventListener("click", () => renderWrongNotes("order"));
  document.getElementById("filter-wn-logic")?.addEventListener("click", () => renderWrongNotes("logic"));
  document.getElementById("filter-wn-words")?.addEventListener("click", () => renderWrongNotes("words"));
  document.getElementById("btn-export-wrongnotes")?.addEventListener("click", exportWrongNotes);
  document.getElementById("btn-backup-json")?.addEventListener("click", backupJSONData);
  document.getElementById("input-restore-json")?.addEventListener("change", restoreJSONData);
  document.getElementById("btn-clear-wrongnotes")?.addEventListener("click", () => {
    state.wrongQuizzes = [];
    state.wrongWords = [];
    safeStorage.removeItem("readflow_wrong_quizzes");
    safeStorage.removeItem("readflow_wrong_words");
    renderWrongNotes(state.wrongNotesFilter);
    updateProgressUI();
    showToast("오답노트가 초기화되었습니다.");
  });

  // 편입 논리 특훈 뷰 전환 (모달이 아닌 메인 사이트 인시튜 뷰 전환)
  document.getElementById("btn-toggle-logic-view")?.addEventListener("click", () => {
    document.getElementById("main-reading-view")?.classList.add("hidden");
    document.getElementById("main-logic-view")?.classList.remove("hidden");
    renderLogicLabContent();
    window.scrollTo({ top: 0, behavior: "smooth" });
  });

  document.getElementById("btn-return-journal")?.addEventListener("click", () => {
    document.getElementById("main-logic-view")?.classList.add("hidden");
    document.getElementById("main-reading-view")?.classList.remove("hidden");
    window.scrollTo({ top: 0, behavior: "smooth" });
  });

  document.getElementById("btn-refresh-logiclab")?.addEventListener("click", refreshLogicLabQuestions);

  // 지문 추가 모달
  document.getElementById("btn-open-add-modal")?.addEventListener("click", () => document.getElementById("add-passage-modal").classList.remove("hidden"));
  document.getElementById("btn-close-modal")?.addEventListener("click", () => document.getElementById("add-passage-modal").classList.add("hidden"));
  document.getElementById("modal-overlay")?.addEventListener("click", () => document.getElementById("add-passage-modal").classList.add("hidden"));
  document.getElementById("form-add-passage")?.addEventListener("submit", handleAddPassageSubmit);

  // AI 모달
  document.getElementById("btn-open-ai-modal")?.addEventListener("click", () => {
    document.getElementById("input-gemini-key").value = state.geminiApiKey;
    document.getElementById("ai-settings-modal").classList.remove("hidden");
  });
  document.getElementById("btn-close-ai-modal")?.addEventListener("click", () => document.getElementById("ai-settings-modal").classList.add("hidden"));
  document.getElementById("ai-settings-modal-overlay")?.addEventListener("click", () => document.getElementById("ai-settings-modal").classList.add("hidden"));
  document.getElementById("btn-save-ai-key")?.addEventListener("click", () => {
    const k = document.getElementById("input-gemini-key").value.trim();
    state.geminiApiKey = k;
    safeStorage.setItem("readflow_gemini_api_key", k);
    document.getElementById("ai-settings-modal").classList.add("hidden");
    showToast("Gemini API 설정 저장 완료");
  });
  document.getElementById("btn-clear-ai-key")?.addEventListener("click", () => {
    state.geminiApiKey = "";
    safeStorage.removeItem("readflow_gemini_api_key");
    document.getElementById("input-gemini-key").value = "";
    showToast("API 키 삭제 완료");
  });

  // 사전 팝업 닫기
  document.addEventListener("click", e => {
    const popup = document.getElementById("word-popup");
    if (popup && !popup.contains(e.target) && !e.target.classList.contains("clickable-word")) {
      closeWordPopup();
    }
  });
}

function refreshPassage() {
  const p = state.passages.find(x => x.id === state.currentPassageId);
  if (p) renderPassageContent(p);
}

function navigatePassage(dir) {
  const activeList = getFilteredPassages();
  const idx = activeList.findIndex(p => p.id === state.currentPassageId);
  const next = idx + dir;
  if (next >= 0 && next < activeList.length) {
    loadPassage(activeList[next].id);
  }
}

function switchTab(name) {
  state.activeTab = name;
  document.querySelectorAll(".tab-link").forEach(btn => {
    btn.classList.toggle("active", btn.getAttribute("data-tab") === name);
  });
  document.getElementById("tab-vocab-content").classList.toggle("hidden", name !== "vocab");
  document.getElementById("tab-quiz-content").classList.toggle("hidden", name !== "quiz");
  document.getElementById("tab-notes-content").classList.toggle("hidden", name !== "notes");
  document.getElementById("tab-flashcard-content").classList.toggle("hidden", name !== "flashcard");
  document.getElementById("tab-dict-content").classList.toggle("hidden", name !== "dict");

  if (name === "flashcard") {
    const p = state.passages.find(x => x.id === state.currentPassageId);
    if (p) renderFlashcardTab(p);
  }
}

// 지문 추가 처리
async function handleAddPassageSubmit(e) {
  e.preventDefault();
  const title = document.getElementById("input-passage-title").value.trim();
  const koreanTitle = document.getElementById("input-passage-korean-title").value.trim();
  const level = document.getElementById("input-passage-level").value;
  const rawText = document.getElementById("input-passage-content").value.trim();
  const submitBtn = document.getElementById("btn-submit-passage");

  if (!title || !rawText) return;

  submitBtn.disabled = true;
  submitBtn.innerHTML = `<span>분석 및 퀴즈 출제 중...</span>`;

  try {
    const sentenceStrings = rawText.match(/[^.!?]+[.!?]+(\s|$)|[^.!?]+$/g) || [rawText];
    const sentences = [];

    for (let s of sentenceStrings) {
      const trimmed = s.trim();
      if (!trimmed) continue;
      const trans = await fetchSmartTranslation(trimmed);
      sentences.push({
        en: trimmed,
        ko: trans,
        chunks: trimmed.replace(/,\s*/g, ' , / ').replace(/\s+(that|which|when|because|while)\s+/gi, ' / $1 ')
      });
    }

    const words = rawText.match(/\b[A-Za-z]{5,}\b/g) || [];
    const unique = [...new Set(words.map(w => w.toLowerCase()))].slice(0, 5);
    const vocabulary = [];
    for (let w of unique) {
      const meaning = (WORDTEST_MAP.get(w) || []).join(", ") || await fetchSmartTranslation(w);
      vocabulary.push({ word: w, pos: "v./n.", meaning, example: "" });
    }

    const first = sentences[0] ? sentences[0].en : "";
    const mid = sentences[Math.floor(sentences.length / 2)] ? sentences[Math.floor(sentences.length / 2)].en : "";
    const last = sentences[sentences.length - 1] ? sentences[sentences.length - 1].en : "";

    const quiz = [
      {
        id: 1,
        question: `What is the primary subject addressed in the text?`,
        questionKo: `이 글의 중심 주제는 무엇인가요?`,
        options: [
          `Key perspectives concerning: ${first.slice(0, 45)}...`,
          "Outdated mechanical engineering techniques",
          "Rules of medieval European court etiquette",
          "Methods for preserving domestic fresh produce"
        ],
        answer: 0,
        explanation: `지문의 도입부('${first.slice(0, 40)}...')에서 전체 담론의 핵심 주제가 전개됩니다.`
      },
      {
        id: 2,
        question: `Which fact is directly corroborated by the author?`,
        questionKo: `작가가 직접적으로 언급한 사실은 무엇인가요?`,
        options: [
          "The phenomenon is completely impossible to observe.",
          mid.slice(0, 55) + (mid.length > 55 ? "..." : ""),
          "Governments have made this inquiry entirely illegal.",
          "Every living cell dissolves within one millisecond."
        ],
        answer: 1,
        explanation: `지문 본문 중 '${mid.slice(0, 50)}...'에 해당하는 내용이 서술되었습니다.`
      },
      {
        id: 3,
        question: `What insight does the conclusion provide?`,
        questionKo: `글의 결론부가 제시하는 시사점은?`,
        options: [
          "The topic holds zero importance for contemporary readers.",
          "No scientific consensus can ever be attained.",
          `Core dynamics regarding '${last.slice(0, 40)}...' remain decisive.`,
          "All ongoing research must cease immediately."
        ],
        answer: 2,
        explanation: `결론부('${last.slice(0, 40)}...')를 통해 핵심 결론을 파악할 수 있습니다.`
      }
    ];

    const wordCount = rawText.split(/\s+/).length;
    const newPassage = {
      id: `custom-${Date.now()}`,
      title,
      koreanTitle: koreanTitle || "사용자 기고 지문",
      level,
      levelLabel: `${level} (User)`,
      category: "User Contribution",
      source: "User Reader",
      readingTime: `${Math.max(1, Math.ceil(wordCount / 120))} MIN`,
      wordCount,
      summary: sentences[0] ? sentences[0].ko : "사용자 등록 독해 지문",
      sentences,
      vocabulary,
      grammarNotes: [
        { title: "접속사와 구문 호응", desc: "주요 접속사 앞뒤의 의미 단위를 기준으로 직독직해 훈련을 진행하세요." }
      ],
      quiz
    };

    state.passages.unshift(newPassage);
    const existing = JSON.parse(safeStorage.getItem("readflow_custom_passages") || "[]");
    existing.unshift(newPassage);
    safeStorage.setItem("readflow_custom_passages", JSON.stringify(existing));

    submitBtn.disabled = false;
    submitBtn.innerHTML = `<span>지문 분석 및 저장</span>`;
    document.getElementById("form-add-passage").reset();
    document.getElementById("add-passage-modal").classList.add("hidden");

    loadPassage(newPassage.id);
    showToast("새 독해 지문이 등록되었습니다.");
  } catch (err) {
    submitBtn.disabled = false;
    submitBtn.innerHTML = `<span>지문 분석 및 저장</span>`;
    alert("지문 처리 중 오류가 발생했습니다.");
  }
}

function updateProgressUI() {
  const badge = document.getElementById("wrong-count-badge");
  if (badge) {
    const totalWrong = state.wrongQuizzes.length + state.wrongWords.length;
    badge.textContent = totalWrong;
  }
}

function showToast(msg) {
  let toast = document.getElementById("editorial-toast");
  if (!toast) {
    toast = document.createElement("div");
    toast.id = "editorial-toast";
    toast.className = "fixed bottom-5 right-5 z-50 bg-zinc-900 text-white dark:bg-white dark:text-zinc-900 text-xs font-mono px-4 py-2.5 rounded shadow-xl transition-all duration-200 transform translate-y-8 opacity-0";
    document.body.appendChild(toast);
  }
  toast.textContent = msg;
  toast.classList.remove("translate-y-8", "opacity-0");
  toast.classList.add("translate-y-0", "opacity-100");
  setTimeout(() => {
    toast.classList.remove("translate-y-0", "opacity-100");
    toast.classList.add("translate-y-8", "opacity-0");
  }, 2200);
}


// ==========================================
// 300편 빠른 지문 선택기 & 카탈로그 패널
// ==========================================
function initQuickPassageSelector() {
  const select = document.getElementById("quick-passage-select");
  if (!select) return;

  const currentLevel = state.filterLevel || "All";
  const activeList = getFilteredPassages();

  let html = "";
  if (currentLevel === "All") {
    const beginner = state.passages.filter(p => p.level === "Beginner");
    const intermediate = state.passages.filter(p => p.level === "Intermediate");
    const advanced = state.passages.filter(p => p.level === "Advanced");

    if (beginner.length > 0) {
      html += `<optgroup label="🌱 초급 (Beginner 1~100)">`;
      beginner.forEach((p, i) => {
        html += `<option value="${p.id}">#${String(i + 1).padStart(3, '0')} ${p.title} (${p.source || 'Journal'})</option>`;
      });
      html += `</optgroup>`;
    }
    if (intermediate.length > 0) {
      html += `<optgroup label="🌿 중급 (Intermediate 101~200)">`;
      intermediate.forEach((p, i) => {
        html += `<option value="${p.id}">#${String(i + 101).padStart(3, '0')} ${p.title} (${p.source || 'Journal'})</option>`;
      });
      html += `</optgroup>`;
    }
    if (advanced.length > 0) {
      html += `<optgroup label="🌳 고급 (Advanced 201~300)">`;
      advanced.forEach((p, i) => {
        html += `<option value="${p.id}">#${String(i + 201).padStart(3, '0')} ${p.title} (${p.source || 'Journal'})</option>`;
      });
      html += `</optgroup>`;
    }
  } else {
    const label = currentLevel === "Beginner" ? "🌱 초급 A2-B1 (100편)" : currentLevel === "Intermediate" ? "🌿 중급 B1-B2 (100편)" : "🌳 고급 B2-C1 (100편)";
    html += `<optgroup label="${label}">`;
    activeList.forEach((p, i) => {
      html += `<option value="${p.id}">#${String(i + 1).padStart(3, '0')} ${p.title} (${p.source || 'Journal'})</option>`;
    });
    html += `</optgroup>`;
  }

  select.innerHTML = html;
  select.value = state.currentPassageId;

  select.onchange = () => {
    loadPassage(select.value);
  };
}

function initQuickCatalogPanel() {
  const btnToggle = document.getElementById("btn-toggle-quick-catalog");
  const btnClose = document.getElementById("btn-close-quick-catalog");
  const panel = document.getElementById("quick-catalog-panel");
  const searchInput = document.getElementById("quick-catalog-search");
  if (!btnToggle || !panel) return;

  btnToggle.onclick = () => {
    panel.classList.toggle("hidden");
    if (!panel.classList.contains("hidden")) {
      renderQuickCatalogList("all", searchInput ? searchInput.value : "");
    }
  };

  if (btnClose) {
    btnClose.onclick = () => panel.classList.add("hidden");
  }

  document.querySelectorAll(".qc-filter-btn").forEach(btn => {
    btn.onclick = () => {
      document.querySelectorAll(".qc-filter-btn").forEach(b => {
        b.className = "qc-filter-btn px-2.5 py-0.5 border border-zinc-300 dark:border-zinc-700 rounded-xs";
      });
      btn.className = "qc-filter-btn px-2.5 py-0.5 bg-zinc-900 text-white dark:bg-white dark:text-zinc-900 rounded-xs font-bold";
      const lvl = btn.getAttribute("data-level");
      renderQuickCatalogList(lvl, searchInput ? searchInput.value : "");
    };
  });

  if (searchInput) {
    searchInput.oninput = () => {
      const activeBtn = document.querySelector(".qc-filter-btn.bg-zinc-900, .qc-filter-btn.dark\\:bg-white");
      const lvl = activeBtn ? activeBtn.getAttribute("data-level") : "all";
      renderQuickCatalogList(lvl, searchInput.value);
    };
  }
}

function renderQuickCatalogList(level = "all", query = "") {
  const container = document.getElementById("quick-catalog-list");
  if (!container) return;

  const q = query.trim().toLowerCase();
  let list = state.passages;
  if (level !== "all") {
    list = list.filter(p => p.level === level);
  }
  if (q) {
    list = list.filter(p => 
      p.title.toLowerCase().includes(q) || 
      (p.koreanTitle && p.koreanTitle.toLowerCase().includes(q)) ||
      (p.category && p.category.toLowerCase().includes(q)) ||
      (p.source && p.source.toLowerCase().includes(q))
    );
  }

  if (list.length === 0) {
    container.innerHTML = `<p class="col-span-2 text-center py-4 text-xs font-mono text-zinc-400">일치하는 지문이 없습니다.</p>`;
    return;
  }

  container.innerHTML = list.map((p) => {
    const globalIdx = state.passages.indexOf(p) + 1;
    const isCurrent = p.id === state.currentPassageId;
    const isCompleted = state.completedPassages.includes(p.id);

    return `
      <div 
        class="qc-item p-2 rounded border cursor-pointer transition flex items-center justify-between gap-2 ${isCurrent ? 'bg-zinc-900 text-white dark:bg-white dark:text-zinc-900 font-bold border-transparent' : 'bg-white dark:bg-zinc-800 border-zinc-200 dark:border-zinc-700 hover:border-zinc-900 dark:hover:border-zinc-300'}"
        data-pid="${p.id}"
      >
        <div class="flex items-center space-x-2 truncate">
          <span class="font-mono text-[10px] ${isCurrent ? 'text-zinc-300 dark:text-zinc-700' : 'text-zinc-400'} flex-shrink-0">#${String(globalIdx).padStart(3, '0')}</span>
          <span class="text-xs truncate">${p.title}</span>
        </div>
        <div class="flex items-center space-x-1.5 flex-shrink-0 text-[10px] font-mono">
          <span class="${isCurrent ? 'text-zinc-300 dark:text-zinc-700' : 'text-zinc-400'}">${p.readingTime || '2m'}</span>
          ${isCompleted ? `<span class="text-emerald-500 font-bold">✓</span>` : ''}
        </div>
      </div>
    `;
  }).join("");

  container.querySelectorAll(".qc-item").forEach(el => {
    el.onclick = () => {
      const pid = el.getAttribute("data-pid");
      loadPassage(pid);
      document.getElementById("quick-catalog-panel")?.classList.add("hidden");
    };
  });
}
