/**
 * ReadFlow Academic Journal - Derivative Quiz & Transfer Logic Engine
 * Provides Sentence Cloze, Paragraph Ordering, and Transfer Exam Logic Completion (Single & Double Blank).
 */

const DerivativeQuizEngine = (function() {

  // 편입 영어 논리완성 폴백 문제 은행 (js/logic_bank.js 300문항 우선 연동)
  const FALLBACK_LOGIC_BANK = [
    {
      id: "tl-01",
      theme: "Medical Science & Longevity",
      category: "단일 빈칸 (Single Blank)",
      logicType: "역접 / 대조 (Contrast)",
      clue: "rather than resorting to aggressive, artificial regimens",
      direction: "인위적·격렬함(-) ↔ 자연스러운 습관화(+)",
      question: "Although modern urban culture often glorifies intense, sporadic physical exhaustion, centenarians in long-lived communities demonstrate that enduring vitality is achieved through ________ integration of movement into daily chores rather than resorting to aggressive, artificial regimens.",
      questionKo: "현대 도시 문화는 종종 강렬하고 산발적인 육체적 탈진을 미화하지만, 장수촌의 100세인들은 지속적인 활력이 공격적이고 인위적인 운동 요법에 의존하기보다는 일상 가사 속에 움직임을 ________ 통합함으로써 달성된다는 것을 보여준다.",
      options: [
        "seamless",
        "precarious",
        "sporadic",
        "superficial"
      ],
      answer: 0,
      vocabBreakdown: [
        { word: "seamless", meaning: "아주 매끄러운, 단절이 없는 (adj.)" },
        { word: "precarious", meaning: "불안정한, 위태로운 (adj.)" },
        { word: "sporadic", meaning: "산발적인, 이따금 일어나는 (adj.)" },
        { word: "superficial", meaning: "피상적인, 표면적인 (adj.)" },
        { word: "glorify", meaning: "미화하다, 찬양하다 (v.)" },
        { word: "vitality", meaning: "활력, 생명력 (n.)" }
      ],
      explanation: "역접 접속사 Although와 대조 표현 'rather than resorting to aggressive, artificial regimens(인위적인 요법에 의존하기보다)'를 통해, 빈칸에는 일상 속에 자연스럽게 녹아든 긍정적 수식어가 와야 합니다. 따라서 '매끄럽고 자연스러운' 뜻을 지닌 seamless가 가장 논리적입니다. precarious(불안정한), sporadic(산발적인), superficial(피상적인)은 논리적으로 어긋납니다."
    },
    {
      id: "tl-02",
      theme: "Ecology & Agriculture",
      category: "더블 빈칸 (Double Blank)",
      logicType: "인과 / 귀결 (Causality)",
      clue: "Because honeybees provide an irreplaceable pollination service... decline would severely [A]... and yield [B] consequences",
      direction: "원인(핵심 수분 매개자 붕괴) → 결과([A] 농작물 타격[-] + [B] 파국적 결과[-])",
      question: "Because pollinators provide an irreplaceable ecological service to terrestrial flora, their sudden population collapse would severely ________ agricultural yields and trigger ________ disruptions across international commodity markets.",
      questionKo: "수분 매개자들은 육상 식물군에 대체 불가능한 생태학적 서비스를 제공하기 때문에, 그들의 갑작스러운 개체수 붕괴는 농업 수확량을 심각하게 ________시키고 국제 원자재 시장 전반에 ________ 혼란을 촉발할 것이다.",
      options: [
        "jeopardize — catastrophic",
        "bolster — negligible",
        "proliferate — transient",
        "stabilize — unprecedented"
      ],
      answer: 0,
      vocabBreakdown: [
        { word: "jeopardize", meaning: "위태롭게 하다, 위험에 빠뜨리다 (v.)" },
        { word: "catastrophic", meaning: "파국적인, 대참사의 (adj.)" },
        { word: "bolster", meaning: "강화하다, 북돋우다 (v.)" },
        { word: "negligible", meaning: "무시해도 될 정도의, 하찮은 (adj.)" },
        { word: "proliferate", meaning: "급증하다, 확산시키다 (v.)" },
        { word: "transient", meaning: "일시적인, 덧없는 (adj.)" }
      ],
      explanation: "인과 접속사 Because와 'population collapse(개체수 붕괴)'라는 마이너스 원인이 제시되었으므로, 빈칸 [A]와 [B]는 모두 심각한 부정적 결과를 나타내는 어휘가 와야 합니다. 수확량을 '위태롭게 하고(jeopardize)', '파국적인(catastrophic)' 혼란을 초래한다는 (A)가 완벽한 대구를 이룹니다."
    },
    {
      id: "tl-03",
      theme: "Neuroscience & Brain Plasticity",
      category: "단일 빈칸 (Single Blank)",
      logicType: "역접 / 대조 (Contrast)",
      clue: "Contrary to the long-held dogma that the mature adult brain is biologically rigid and immutable",
      direction: "과거 통념(딱딱하게 고정됨, immutable) ↔ 최신 신경과학(가역적이고 적응력 있음, +)",
      question: "Contrary to the long-held neurological dogma that the adult central nervous system is structurally immutable, contemporary neuroplasticity research demonstrates that synaptic architecture remains remarkably ________ even in late senescence.",
      questionKo: "성인의 중추신경계가 구조적으로 불변한다는 오랜 신경학적 도그마와는 반대로, 현대의 신경가소성 연구는 시냅스 구조가 노년기 후반에조차 현저하게 ________ 상태를 유지함을 보여준다.",
      options: [
        "malleable",
        "ossified",
        "immutable",
        "stagnant"
      ],
      answer: 0,
      vocabBreakdown: [
        { word: "malleable", meaning: "가소성이 있는, 유연한, 영향을 받기 쉬운 (adj.)" },
        { word: "ossified", meaning: "경직된, 뼈처럼 굳은 (adj.)" },
        { word: "immutable", meaning: "불변의, 변치 않는 (adj.)" },
        { word: "stagnant", meaning: "침체된, 흐르지 않는 (adj.)" },
        { word: "senescence", meaning: "노화, 노쇠기 (n.)" },
        { word: "dogma", meaning: "독단적 신념, 도그마 (n.)" }
      ],
      explanation: "전치사구 'Contrary to ~ structurally immutable(구조적으로 불변이라는 통념과 반대로)'가 역접의 기준선(Pivot)입니다. 따라서 빈칸에는 immutable의 정반대 개념인 '형태를 바꿀 수 있는, 가소성이 있는'을 뜻하는 malleable이 와야 합니다."
    },
    {
      id: "tl-04",
      theme: "Quantum Physics & Computing",
      category: "더블 빈칸 (Double Blank)",
      logicType: "양보 / 전환 (Concession)",
      clue: "While theoretical quantum algorithms promise exponential processing advantages, quantum decoherence remains a ________ impediment that continues to ________ large-scale commercial realization.",
      direction: "이론적 가능성(+) vs 현실적 장애물(-)",
      question: "While theoretical quantum algorithms promise exponential processing advantages, quantum decoherence remains a ________ obstacle that continues to ________ large-scale commercial realization.",
      questionKo: "이론적 양자 알고리즘이 기하급수적인 연산상 이점을 약속하지만, 양자 결맞음 상실은 대규모 상용화를 지속적으로 ________하는 ________ 장애물로 남아 있다.",
      options: [
        "formidable — thwart",
        "trivial — expedite",
        "negligible — accelerate",
        "transient — facilitate"
      ],
      answer: 0,
      vocabBreakdown: [
        { word: "formidable", meaning: "만만찮은, 극복하기 힘든 (adj.)" },
        { word: "thwart", meaning: "좌절시키다, 방해하다 (v.)" },
        { word: "trivial", meaning: "사소한, 대수롭지 않은 (adj.)" },
        { word: "expedite", meaning: "신속히 처리하다, 촉진하다 (v.)" },
        { word: "decoherence", meaning: "결맞음 상실 (양자역학) (n.)" }
      ],
      explanation: "양보절 접속사 While이 이끄는 절에서 양자 알고리즘의 긍정적 잠재력이 제시되었으므로, 주절은 현실적인 기술적 난관과 한계를 지적해야 합니다. 장애물을 수식하는 '극복하기 힘든(formidable)'과 상용화를 '좌절시키다/가로막다(thwart)'가 짝을 이룬 (A)가 정답입니다."
    },
    {
      id: "tl-05",
      theme: "Behavioral Economics",
      category: "단일 빈칸 (Single Blank)",
      logicType: "재진술 / 상술 (Restatement)",
      clue: "rational agents are presumed to maximize utility; however, real human decision-makers exhibit systematic cognitive biases, leading to choices that are fundamentally ________.",
      direction: "완전한 합리성(rational utility) 가정의 붕괴 → 비합리적/모순적 선택(-)",
      question: "Classical macroeconomic theory presupposes perfectly rational agents acting in self-interest; empirical behavioral observations, however, reveal deeply ingrained cognitive heuristics that render human economic decisions inherently ________.",
      questionKo: "고전 거시경제학 이론은 사리사욕에 따라 행동하는 완벽히 합리적인 행위자를 상정하지만, 실증적 행동 관찰은 인간의 경제적 결정을 본질적으로 ________하게 만드는 깊이 뿌리박힌 인지적 휴리스틱을 밝혀낸다.",
      options: [
        "sub-optimal",
        "infallible",
        "omniscient",
        "immaculate"
      ],
      answer: 0,
      vocabBreakdown: [
        { word: "sub-optimal", meaning: "최적이 아닌, 차선의, 비효율적인 (adj.)" },
        { word: "infallible", meaning: "결코 틀리지 않는 (adj.)" },
        { word: "omniscient", meaning: "전지의, 박식한 (adj.)" },
        { word: "immaculate", meaning: "오점 없는, 완벽한 (adj.)" },
        { word: "heuristics", meaning: "어림셈, 휴리스틱 (n.)" }
      ],
      explanation: "however 뒤에서 인지적 편향과 휴리스틱(cognitive heuristics)이 인간의 결정을 어떻게 만드는지 서술하고 있으므로, 합리적 최적 선택과 대비되는 '최선에 미치지 못하는, 차선의(sub-optimal)'가 논리적 귀결입니다."
    },
    {
      id: "tl-06",
      theme: "Philosophy of Science & Epistemology",
      category: "더블 빈칸 (Double Blank)",
      logicType: "역접 / 대조 (Contrast)",
      clue: "Scientific progress does not proceed through the mere ________ of immutable dogmas; rather, it thrives on the systematic ________ of entrenched paradigms through empirical anomalies.",
      direction: "단순 보존/유지(-) ↔ 경험적 변칙을 통한 기존 패러다임의 전복/해체(+)",
      question: "Scientific progress does not proceed via the unquestioning ________ of traditional axioms; rather, it advances through the rigorous ________ of established hypotheses in the face of counter-evidence.",
      questionKo: "과학적 진보는 전통적 공리의 의심 없는 ________을 통해 진행되지 않는다. 오히려 반증에 직면하여 확립된 가설들을 엄격하게 ________함으로써 전진한다.",
      options: [
        "preservation — refutation",
        "skepticism — endorsement",
        "demolition — perpetuation",
        "dismissal — replication"
      ],
      answer: 0,
      vocabBreakdown: [
        { word: "preservation", meaning: "보존, 지속 (n.)" },
        { word: "refutation", meaning: "반박, 논박 (n.)" },
        { word: "skepticism", meaning: "회의주의 (n.)" },
        { word: "perpetuation", meaning: "영속화 (n.)" },
        { word: "axiom", meaning: "자명한 이치, 공리 (n.)" }
      ],
      explanation: "'not A but B' (not proceed via... rather advances through...) 구문입니다. 첫 빈칸에는 교조를 무비판적으로 '보존(preservation)'하는 것이 아니라는 내용이, 두 번째 빈칸에는 반증 사례를 통해 가설을 비판적으로 '반박/검증(refutation)'한다는 내용이 들어가야 대구가 완성됩니다."
    },
    {
      id: "tl-07",
      theme: "Epigenetics & Genetics",
      category: "단일 빈칸 (Single Blank)",
      logicType: "부연 / 상술 (Elaboration)",
      clue: "DNA sequence itself remains unaltered; nevertheless, environmental factors induce chemical tags that ________ gene expression.",
      direction: "염기서열 불변에도 불구하고 유전자 발현을 조절/변조함",
      question: "While genetic determinism posits that DNA sequences irrevocably dictate biological destiny, epigenetics demonstrates that environmental exposures produce molecular tags capable of ________ gene transcription without altering the underlying nucleotide sequence.",
      questionKo: "유전 결정론은 DNA 서열이 생물학적 운명을 바꿀 수 없이 지배한다고 상정하지만, 후성유전학은 환경적 노출이 기저 뉴클레오티드 서열을 변경하지 않고도 유전자 전사를 ________할 수 있는 분자 표지를 생성함을 입증한다.",
      options: [
        "modulating",
        "annihilating",
        "petrifying",
        "sanctifying"
      ],
      answer: 0,
      vocabBreakdown: [
        { word: "modulating", meaning: "조절하는, 조율하는 (part.)" },
        { word: "annihilating", meaning: "전멸시키는 (part.)" },
        { word: "petrifying", meaning: "돌처럼 굳히는 (part.)" },
        { word: "irrevocably", meaning: "돌이킬 수 없이 (adv.)" },
        { word: "transcription", meaning: "전사 (유전정보) (n.)" }
      ],
      explanation: "후성유전학의 본질은 유전자 서열 자체를 파괴하거나 변경하는 것이 아니라 유전자의 발현을 켜고 끄는 방식으로 '조절(modulate)'하는 것입니다. 따라서 modulating이 가장 정밀한 학술적 정답입니다."
    },
    {
      id: "tl-08",
      theme: "Artificial Intelligence & Ethics",
      category: "더블 빈칸 (Double Blank)",
      logicType: "역접 / 대조 (Contrast)",
      clue: "far from being purely objective instruments, algorithms often ________ human prejudices, thereby producing outcomes that are fundamentally ________.",
      direction: "객관적이라는 오해(-) ↔ 실제로는 인간의 편견을 증폭[A]하여 부당한[B] 결과를 냄",
      question: "Far from being inherently neutral arbiters, automated algorithms frequently ________ historical prejudices embedded in training data, producing automated verdicts that are disturbingly ________.",
      questionKo: "본질적으로 중립적인 중재자이기는커녕, 자동화된 알고리즘은 훈련 데이터에 내재된 역사적 편견을 빈번하게 ________하여, 충격적일 정도로 ________한 자동 판정을 낳는다.",
      options: [
        "perpetuate — discriminatory",
        "rectify — equitable",
        "eradicate — impartial",
        "attenuate — egalitarian"
      ],
      answer: 0,
      vocabBreakdown: [
        { word: "perpetuate", meaning: "영속화하다, 끊임없이 지속시키다 (v.)" },
        { word: "discriminatory", meaning: "차별적인, 불공평한 (adj.)" },
        { word: "rectify", meaning: "바로잡다, 교정하다 (v.)" },
        { word: "equitable", meaning: "공정한, 공평한 (adj.)" },
        { word: "attenuate", meaning: "약화시키다, 희석하다 (v.)" },
        { word: "arbiter", meaning: "중재자, 판정자 (n.)" }
      ],
      explanation: "'Far from being neutral(중립적이기는커녕)'이라는 역접 시그널이 주어졌으므로, 알고리즘이 기존 편견을 '영속화(perpetuate)'하고 '차별적인(discriminatory)' 결정을 도출한다는 (A)가 성립합니다. 나머지 선택지들은 편견을 바로잡거나 공정하다는 긍정적 방향이므로 모순입니다."
    },
    {
      id: "tl-09",
      theme: "History & Geopolitics",
      category: "단일 빈칸 (Single Blank)",
      logicType: "인과 / 귀결 (Causality)",
      clue: "Economic disparity and institutional corruption combined to erode social trust, making the collapse of the dynasty virtually ________.",
      direction: "내부 부패와 격차의 심화 → 정권 붕괴의 불가피성",
      question: "Prolonged fiscal insolvency combined with rampant administrative venality so thoroughly undermined the regime's legitimacy that political implosion became virtually ________.",
      questionKo: "만연한 행정적 부패와 결합된 장기적인 재정 파탄은 정권의 정통성을 너무나 철저하게 약화시켜, 정치적 내부 붕괴는 사실상 ________한 것이 되었다.",
      options: [
        "inevitable",
        "avoidable",
        "contentious",
        "auspicious"
      ],
      answer: 0,
      vocabBreakdown: [
        { word: "inevitable", meaning: "불가피한, 필연적인 (adj.)" },
        { word: "venality", meaning: "돈에 매수됨, 부패 (n.)" },
        { word: "implosion", meaning: "내부 붕괴 (n.)" },
        { word: "insolvency", meaning: "파산, 지급 불능 (n.)" },
        { word: "auspicious", meaning: "길조의, 상서로운 (adj.)" }
      ],
      explanation: "'so ~ that ...' (너무 ~해서 ...하다) 인과 구문입니다. 재정 파탄과 행정 부패로 정통성이 완전히 무너졌으므로 붕괴는 피할 수 없는 '필연적인(inevitable)' 상태가 됩니다."
    },
    {
      id: "tl-10",
      theme: "Environmental Science & Climate",
      category: "더블 빈칸 (Double Blank)",
      logicType: "인과 / 대조 (Cause & Contrast)",
      clue: "Failing to implement emissions reductions will not only ________ ecological degradation but also ________ long-term socioeconomic stability.",
      direction: "온실가스 감축 실패(-) → 생태계 파괴 악화[A] & 사회경제적 안정성 침식[B]",
      question: "Failing to adopt rigorous carbon abatement strategies will not only ________ existing environmental degradation but also severely ________ global macroeconomic stability.",
      questionKo: "엄격한 탄소 감축 전략을 채택하지 않는 것은 기존의 환경 파괴를 ________시킬 뿐만 아니라 전 세계 거시경제적 안정성을 심각하게 ________시킬 것이다.",
      options: [
        "exacerbate — undermine",
        "alleviate — fortify",
        "mitigate — consolidate",
        "rectify — revitalize"
      ],
      answer: 0,
      vocabBreakdown: [
        { word: "exacerbate", meaning: "악화시키다, 가중시키다 (v.)" },
        { word: "undermine", meaning: "약화시키다, 기반을 무너뜨리다 (v.)" },
        { word: "alleviate", meaning: "완화하다, 덜어주다 (v.)" },
        { word: "consolidate", meaning: "통합하다, 공고히 하다 (v.)" },
        { word: "abatement", meaning: "감소, 완화 (n.)" }
      ],
      explanation: "'not only A but also B' 병렬 구조이며 부정적 조건(Failing to adopt...)에서 출발하므로, 두 빈칸 모두 부정적 영향력인 '악화시키다(exacerbate)'와 '약화시키다/침식하다(undermine)'가 결합된 (A)가 완벽한 정답입니다."
    },
    {
      id: "tl-11",
      theme: "Linguistics & Semiotics",
      category: "단일 빈칸 (Single Blank)",
      logicType: "역접 / 대조 (Contrast)",
      clue: "far from being static or fixed, language is fundamentally ________, constantly adapting to cultural shifts.",
      direction: "고정되어 있음(static/fixed) ↔ 끊임없이 변화함(+)",
      question: "Far from being an immutable repository of calcified rules, human natural language is fundamentally ________, continuously shifting its semantic boundaries to accommodate novel cultural paradigms.",
      questionKo: "인간의 자연어는 굳어진 규칙들의 불변의 저장소이기는커녕 근본적으로 ________하여, 새로운 문화적 패러다임을 수용하기 위해 자신의 의미론적 경계를 끊임없이 이동시킨다.",
      options: [
        "dynamic",
        "dogmatic",
        "moribund",
        "monotonous"
      ],
      answer: 0,
      vocabBreakdown: [
        { word: "dynamic", meaning: "역동적인, 변화무쌍한 (adj.)" },
        { word: "calcified", meaning: "석회화된, 굳어버린 (adj.)" },
        { word: "moribund", meaning: "소멸해 가는, 빈사 상태의 (adj.)" },
        { word: "semantic", meaning: "의미론의, 의미의 (adj.)" },
        { word: "repository", meaning: "저장소, 보고 (n.)" }
      ],
      explanation: "'Far from being an immutable repository...(불변의 저장소이기는커녕)' 뒤에 이어지며, 'continuously shifting(끊임없이 이동하는)'과 동의어 관계를 형성해야 하므로 dynamic(역동적인)이 유일하게 적합합니다."
    },
    {
      id: "tl-12",
      theme: "Psychology & Cognitive Science",
      category: "더블 빈칸 (Double Blank)",
      logicType: "양보 / 대조 (Concession & Contrast)",
      clue: "Although intuitive heuristics often provide ________ practical solutions in routine survival, they frequently generate ________ errors when applied to complex probabilistic reasoning.",
      direction: "일상적 상황에서의 유용성(+) vs 복잡한 확률 문제에서의 치명적 오류(-)",
      question: "Although evolutionary heuristics provide ________ cognitive shortcuts in routine survival scenarios, they produce remarkably ________ biases when evaluating complex statistical probabilities.",
      questionKo: "비록 진화적 휴리스틱이 일상적 생존 상황에서는 ________ 인지적 지름길을 제공하지만, 복잡한 통계적 확률을 평가할 때는 현저하게 ________ 편향을 낳는다.",
      options: [
        "pragmatic — pernicious",
        "detrimental — benign",
        "superfluous — negligible",
        "cumbersome — salutary"
      ],
      answer: 0,
      vocabBreakdown: [
        { word: "pragmatic", meaning: "실용적인, 실제적인 (adj.)" },
        { word: "pernicious", meaning: "치명적인, 해로운 (adj.)" },
        { word: "detrimental", meaning: "해로운, 유해한 (adj.)" },
        { word: "benign", meaning: "온화한, 무해한 (adj.)" },
        { word: "cumbersome", meaning: "다루기 힘든, 성가신 (adj.)" },
        { word: "salutary", meaning: "유익한, 효과가 좋은 (adj.)" }
      ],
      explanation: "Although가 이끄는 양보절은 휴리스틱의 긍정적 가치('실용적인' pragmatic 지름길)를 인정하지만, 주절은 복잡한 통계 문제에서의 부정적 결함('치명적인' pernicious 편향)을 지적해야 논리적 대구가 완성됩니다."
    },
    {
      id: "tl-13",
      theme: "Aesthetics & Art Criticism",
      category: "단일 빈칸 (Single Blank)",
      logicType: "역접 / 대조 (Contrast)",
      clue: "Instead of dismissing modern abstraction as chaotic, perceptive critics possess an acute aesthetic [   ] capable of deciphering non-representational nuance.",
      direction: "혼돈으로 묵살하기보다(-) ↔ 예리한 심미안/안목으로 해독함(+)",
      question: "Rather than dismissing radical modernist abstraction as mere chaotic scribbling, perceptive art critics demonstrate an acute aesthetic ________ capable of deciphering subtle chromatic and formal harmonies.",
      questionKo: "급진적인 모더니즘 추상을 단순한 혼란스러운 낙서로 치부하기보다는, 통찰력 있는 미술 비평가들은 미묘한 색채와 형태적 조화를 해독할 수 있는 예리한 미적 ________을 보여준다.",
      options: [
        "discernment",
        "complacency",
        "indifference",
        "indignation"
      ],
      answer: 0,
      vocabBreakdown: [
        { word: "discernment", meaning: "안목, 식견, 분별력 (n.)" },
        { word: "complacency", meaning: "자기만족, 안주 (n.)" },
        { word: "indifference", meaning: "무관심 (n.)" },
        { word: "indignation", meaning: "분개, 의분 (n.)" },
        { word: "chromatic", meaning: "색채의, 유채색의 (adj.)" }
      ],
      explanation: "'Rather than dismissing...(치부하기보다는)'에 대비되어, 작품의 조화를 해독할 줄 아는 긍정적 능력을 수식해야 하므로 '안목, 분별력'을 뜻하는 discernment가 정답입니다."
    },
    {
      id: "tl-14",
      theme: "Monetary Economics & Inflation",
      category: "더블 빈칸 (Double Blank)",
      logicType: "인과 / 귀결 (Causality)",
      clue: "Excessively expansionary monetary policy triggers runaway inflation that can severely [A] purchasing power and [B] public confidence.",
      direction: "통화 팽창과 인플레이션 → 구매력 침식[A] & 대중 신뢰 약화[B]",
      question: "When central banks pursue unchecked quantitative easing, runaway inflationary spikes can severely ________ household purchasing power and steadily ________ public confidence in fiat currency.",
      questionKo: "중앙은행이 무분별한 양적 완화를 추진할 때, 걷잡을 수 없는 인플레이션 급등은 가계 구매력을 심각하게 ________시키고 법정 통화에 대한 대중의 신뢰를 꾸준히 ________시킬 수 있다.",
      options: [
        "erode — undermine",
        "enhance — bolster",
        "amplify — solidify",
        "generate — reconcile"
      ],
      answer: 0,
      vocabBreakdown: [
        { word: "erode", meaning: "침식하다, 서서히 깎아먹다 (v.)" },
        { word: "undermine", meaning: "밑을 파다, 약화시키다 (v.)" },
        { word: "fiat currency", meaning: "불환 지폐, 법정 통화 (n.)" },
        { word: "quantitative easing", meaning: "양적 완화 (n.)" }
      ],
      explanation: "인플레이션 급등이 가져오는 가계 구매력과 통화 신뢰에 대한 악영향을 다루고 있으므로, 두 빈칸 모두 부정적 동사인 '침식하다(erode)'와 '약화시키다(undermine)'가 들어가야 합니다."
    },
    {
      id: "tl-15",
      theme: "Bioethics & Genetic Engineering",
      category: "단일 빈칸 (Single Blank)",
      logicType: "역접 / 경계 (Warning & Concession)",
      clue: "While CRISPR gene editing holds immense therapeutic promise, the prospect of germline modification raises profound dilemmas that must not be approached with ethical [   ].",
      direction: "치료적 잠재력(+) vs 가볍게 넘겨서는 안 될 도덕적 위험성(-)",
      question: "While genetic scissors offer unprecedented therapeutic potential for hereditary diseases, germline genetic editing introduces perilous societal ramifications that must never be treated with moral ________.",
      questionKo: "유전자 가위가 유전 질환에 전례 없는 치료적 잠재력을 제공하지만, 생식세포 유전자 편집은 도덕적 ________로 다루어져서는 결코 안 될 위험한 사회적 파장을 불러일으킨다.",
      options: [
        "levity",
        "solemnity",
        "vigilance",
        "prudence"
      ],
      answer: 0,
      vocabBreakdown: [
        { word: "levity", meaning: "경솔함, 경망, 가벼움 (n.)" },
        { word: "solemnity", meaning: "엄숙함 (n.)" },
        { word: "vigilance", meaning: "경계, 조심 (n.)" },
        { word: "prudence", meaning: "신중함 (n.)" },
        { word: "ramifications", meaning: "파장, 결과 (n.)" }
      ],
      explanation: "'must never be treated with...(결코 ~하게 다루어져서는 안 된다)'라는 부정 금지 명령형입니다. 위험한 사회적 파장(perilous ramifications)에 직면하여 절대 취해서는 안 될 태도는 '경솔함(levity)'입니다. solemnity, vigilance, prudence는 오히려 반드시 지켜야 할 덕목이므로 오답입니다."
    },
    {
      id: "tl-16",
      theme: "Urban Sociology & Demographics",
      category: "더블 빈칸 (Double Blank)",
      logicType: "인과 / 귀결 (Causality)",
      clue: "Rapid and chaotic urbanization outpaces municipal infrastructure, causing sanitization to [A] and leaving informal settlers [B] to epidemic outbreaks.",
      direction: "인프라 부족 → 위생 악화[A] & 전염병에 취약[B]",
      question: "Unregulated suburban sprawl rapidly outpaces civic municipal capabilities, causing municipal sanitation to ________ and leaving informal settlement populations extraordinarily ________ to waterborne contagion.",
      questionKo: "규제 없는 교외 스프롤 현상은 도시 행정 역량을 빠르게 앞지르며, 이로 인해 도시 위생은 ________되고 무허가 정착지 주민들은 수인성 전염병에 극도로 ________해지게 된다.",
      options: [
        "deteriorate — vulnerable",
        "flourish — impervious",
        "stabilize — immune",
        "recover — resistant"
      ],
      answer: 0,
      vocabBreakdown: [
        { word: "deteriorate", meaning: "악화되다, 저하되다 (v.)" },
        { word: "vulnerable", meaning: "취약한, 상처받기 쉬운 (adj.)" },
        { word: "impervious", meaning: "영향을 받지 않는, 불투과성의 (adj.)" },
        { word: "contagion", meaning: "전염병, 감염 (n.)" }
      ],
      explanation: "인프라가 인구 팽창을 따라가지 못해(outpaces capabilities) 위생이 '악화되고(deteriorate)' 주민들이 질병에 '취약해진다(vulnerable)'는 인과 논리가 성립합니다."
    },
    {
      id: "tl-17",
      theme: "Metaphysics & Free Will",
      category: "단일 빈칸 (Single Blank)",
      logicType: "재진술 / 상술 (Restatement)",
      clue: "Hard determinists argue that human agency is merely an illusion, asserting that all voluntary choices are inexorably [   ] by prior physical causes.",
      direction: "자유의지는 착각이며, 모든 선택은 이전의 물리적 원인에 의해 미리 정해져 있음",
      question: "Rigid determinists dismiss libertarian free will as an evolutionary illusion, maintaining that every subjective decision is inexorably ________ by preceding biochemical and environmental antecedents.",
      questionKo: "엄격한 결정론자들은 자유의지를 진화론적 착각으로 일축하며, 모든 주관적 결정은 앞선 생화학적·환경적 선행 조건들에 의해 불가피하게 ________된다고 주장한다.",
      options: [
        "preordained",
        "fortuitous",
        "arbitrary",
        "extemporaneous"
      ],
      answer: 0,
      vocabBreakdown: [
        { word: "preordained", meaning: "미리 정해진, 운명지어진 (adj./part.)" },
        { word: "fortuitous", meaning: "우연한, 행운의 (adj.)" },
        { word: "arbitrary", meaning: "자의적인, 멋대로인 (adj.)" },
        { word: "extemporaneous", meaning: "즉흥적인 (adj.)" },
        { word: "antecedents", meaning: "선행 요인, 전례 (n.)" }
      ],
      explanation: "결정론(determinism)은 모든 사건과 선택이 과거의 인과 고리에 의해 이미 결정되어 있다고 봅니다. 따라서 '미리 결정된(preordained)'이 정답입니다. 우연(fortuitous)이나 즉흥성(extemporaneous)은 결정론의 반대 개념입니다."
    },
    {
      id: "tl-18",
      theme: "Cognitive Psychology & Confirmation Bias",
      category: "더블 빈칸 (Double Blank)",
      logicType: "역접 / 대조 (Contrast)",
      clue: "Confirmation bias impels individuals to eagerly [A] facts corroborating their dogmas while casually [B] rigorous counter-evidence.",
      direction: "자기 생각과 맞는 증거는 수용[A] ↔ 반대 증거는 배척/묵살[B]",
      question: "Confirmation bias impels dogmatic ideologues to voraciously ________ anecdotal data corroborating their worldview, while cavalierly ________ robust empirical data that refutes their core assumptions.",
      questionKo: "확증 편향은 교조주의적 이데올로그들로 하여금 자신의 세계관을 확증하는 일화적 데이터를 탐욕스럽게 ________하게 만드는 반면, 핵심 가정을 반박하는 강력한 실증적 데이터는 무신경하게 ________하게 만든다.",
      options: [
        "embrace — dismissing",
        "dispute — celebrating",
        "fabricate — authenticating",
        "suppress — propagating"
      ],
      answer: 0,
      vocabBreakdown: [
        { word: "embrace", meaning: "기꺼이 받아들이다, 포용하다 (v.)" },
        { word: "dismiss", meaning: "묵살하다, 일축하다 (v.)" },
        { word: "cavalierly", meaning: "무신경하게, 거만하게 (adv.)" },
        { word: "voraciously", meaning: "탐욕스럽게, 열렬히 (adv.)" }
      ],
      explanation: "접속사 while을 기준으로 앞선 '자신의 세계관을 지지하는 데이터'는 열렬히 '수용(embrace)'하고, 뒤의 '반증 데이터'는 가볍게 '묵살(dismissing)'하는 대조적 행동 양식이 성립합니다."
    },
    {
      id: "tl-19",
      theme: "Astrophysics & Cosmology",
      category: "단일 빈칸 (Single Blank)",
      logicType: "역접 / 대조 (Contrast)",
      clue: "Although dark matter emits no detectable electromagnetic radiation, its pervasive gravitational presence is deduced from the [   ] velocity curves of peripheral stars.",
      direction: "직접 관측 불가 ↔ 비정상적으로 빠른 회전 속도라는 변칙적 현상(+)",
      question: "Although dark matter emits no detectable photons across the electromagnetic spectrum, astrophysicists deduce its pervasive gravitational footprint from the ________ orbital velocity curves of peripheral galactic disks.",
      questionKo: "비록 암흑 물질은 전자기 스펙트럼 전반에 걸쳐 검출 가능한 광자를 방출하지 않지만, 천체물리학자들은 외곽 은하 원반의 ________ 궤도 속도 곡선으로부터 그 만연한 중력적 흔적을 추론해 낸다.",
      options: [
        "anomalous",
        "negligible",
        "pedestrian",
        "monotonous"
      ],
      answer: 0,
      vocabBreakdown: [
        { word: "anomalous", meaning: "변칙적인, 이상한, 파격적인 (adj.)" },
        { word: "negligible", meaning: "하찮은 (adj.)" },
        { word: "pedestrian", meaning: "평범한, 진부한 (adj.)" },
        { word: "electromagnetic spectrum", meaning: "전자기 스펙트럼 (n.)" }
      ],
      explanation: "기존 뉴턴/케플러 법칙으로 설명되지 않는 '변칙적인(anomalous)' 외곽 회전 속도 때문에 미지의 중력원인 암흑물질을 추론하게 되었다는 천체물리학의 역사적 맥락에 부합하는 단어는 anomalous입니다."
    },
    {
      id: "tl-20",
      theme: "Evolutionary Biology & Sociobiology",
      category: "더블 빈칸 (Double Blank)",
      logicType: "양보 / 역접 (Concession & Contrast)",
      clue: "Altruistic sacrifice, while personally [A], ultimately serves to [B] shared gene copies across kin networks.",
      direction: "개체에게는 손해[A] ↔ 유전자 수준에서는 영속화/보존[B]",
      question: "Kin selection resolves the longstanding evolutionary riddle of altruism by revealing that self-sacrificing behaviors, while personally ________, ultimately function to ________ shared genetic copies across biological progeny.",
      questionKo: "혈연 선택설은 자기희생적 행동이 개인적으로는 비록 ________할지라도, 궁극적으로는 생물학적 자손에 걸쳐 공유된 유전자 복제본을 ________하는 기능을 한다는 점을 밝힘으로써 이타주의라는 오랜 진화론적 수수께끼를 해결한다.",
      options: [
        "disadvantageous — perpetuate",
        "lucrative — extinguish",
        "negligible — obliterate",
        "innocuous — eradicate"
      ],
      answer: 0,
      vocabBreakdown: [
        { word: "disadvantageous", meaning: "불리한, 손해가 되는 (adj.)" },
        { word: "perpetuate", meaning: "영속시키다, 지속되게 하다 (v.)" },
        { word: "progeny", meaning: "자손, 후예 (n.)" },
        { word: "altruism", meaning: "이타주의 (n.)" }
      ],
      explanation: "'while personally [A]'는 개체 수준에서의 손실('불리한' disadvantageous)을 의미하며, 'ultimately function to [B]'는 유전자 수준에서의 이익('영속화하다' perpetuate)을 설명하는 양보-대조 구문입니다."
    }
  ];

  /**
   * 1. 문단 순서 맞추기 생성기 (Paragraph & Sentence Ordering)
   * 지문의 문장들을 분석하여 표준 수능/편입형 순서 배열 문제 생성
   */
  function generateOrderingQuiz(passage) {
    const s = passage.sentences || [];
    if (s.length < 4) {
      return null;
    }

    // 주어진 글: 도입 문장
    const leadInEn = s[0].en;
    const leadInKo = s[0].ko;

    // A, B, C 블록 분할
    // 원본 순서: B(1~2번째 문장), A(3번째 문장), C(마지막 문장들)
    // 화면에 표기되는 (A), (B), (C)를 섞어서 출제
    let part1 = s[1].en;
    let part2 = s[2].en + (s[3] ? " " + s[3].en : "");
    let part3 = s[s.length - 1].en;

    // (A)에 part2, (B)에 part1, (C)에 part3 배치 -> 정답 순서: (B) - (A) - (C)
    const blockA = part2;
    const blockB = part1;
    const blockC = part3;

    const options = [
      "(A) — (C) — (B)",
      "(B) — (A) — (C)",
      "(B) — (C) — (A)",
      "(C) — (A) — (B)"
    ];
    const answerIndex = 1; // (B) -> (A) -> (C)

    return {
      id: `ord-${passage.id}`,
      type: "order",
      typeLabel: "문단 순서",
      category: "문단 / 문장 논리 순서 배열",
      question: "주어진 글 다음에 이어질 글의 순서로 가장 적절한 것을 고르시오.",
      questionKo: "도입 글에 이어지는 논리적 인과 및 담화 흐름에 맞추어 (A), (B), (C)의 순서를 배열하시오.",
      leadIn: {
        en: leadInEn,
        ko: leadInKo
      },
      blocks: [
        { label: "(A)", en: blockA },
        { label: "(B)", en: blockB },
        { label: "(C)", en: blockC }
      ],
      options: options,
      answer: answerIndex,
      explanation: `[논리적 전개 분석]
1. [주어진 글]에서 중심 화제("${leadInEn.slice(0, 40)}...")를 먼저 제시합니다.
2. 이어지는 (B)("${blockB.slice(0, 40)}...")가 도입부의 핵심 명제를 가장 직접적으로 부연하며 글을 전개합니다.
3. 그 뒤 (A)("${blockA.slice(0, 40)}...")에서 구체적인 세부 사항이나 근거를 상세히 상술합니다.
4. 마지막으로 (C)("${blockC.slice(0, 40)}...")가 논리적 결론 및 시사점을 도출하며 글을 마무리하므로, 가장 자연스러운 순서는 **(B) — (A) — (C)**입니다.`
    };
  }

  /**
   * 2. 빈칸 추론 생성기 (Sentence Cloze / Blank)
   * 핵심 문장의 핵심 어휘를 마스킹하고 문맥 단서 및 오답 선지 구성
   */
  function generateClozeQuiz(passage) {
    const vocabList = passage.vocabulary || [];
    const s = passage.sentences || [];
    if (vocabList.length === 0 || s.length < 2) return null;

    // 지문 속 단어와 일치하는 문장 탐색
    let targetVocab = vocabList[0];
    let targetSentence = s[1];
    let foundWord = "";

    for (let v of vocabList) {
      const regex = new RegExp(`\\b${v.word}\\b`, 'i');
      const matchS = s.find(sent => regex.test(sent.en));
      if (matchS) {
        targetVocab = v;
        targetSentence = matchS;
        foundWord = v.word;
        break;
      }
    }

    if (!foundWord) {
      targetVocab = vocabList[0];
      foundWord = targetVocab.word;
      targetSentence = s[Math.min(2, s.length - 1)];
    }

    // 빈칸으로 교체
    const regex = new RegExp(`\\b${foundWord}\\b`, 'i');
    const blankSentenceEn = targetSentence.en.replace(regex, "[          ]");

    // 매력적인 오답 어휘 풀
    const distractorBank = [
      { word: "superfluous", meaning: "불필요한, 중복된" },
      { word: "detrimental", meaning: "해로운, 유해한" },
      { word: "ephemeral", meaning: "일시적인, 덧없는" },
      { word: "redundant", meaning: "잉여의, 쓸모없는" },
      { word: "precarious", meaning: "위태로운, 불안정한" },
      { word: "arbitrary", meaning: "임의적인, 제멋대로인" }
    ].filter(d => d.word.toLowerCase() !== foundWord.toLowerCase());

    const distractors = distractorBank.slice(0, 3);
    const correctOpt = foundWord;
    const optionPool = [
      correctOpt,
      ...distractors.map(d => d.word)
    ];

    // 셔플
    const shuffled = [
      { text: optionPool[0], isCorrect: true },
      { text: optionPool[1], isCorrect: false },
      { text: optionPool[2], isCorrect: false },
      { text: optionPool[3], isCorrect: false }
    ].sort(() => 0.5 - Math.random());

    const answerIdx = shuffled.findIndex(item => item.isCorrect);

    return {
      id: `clz-${passage.id}`,
      type: "cloze",
      typeLabel: "빈칸 추론",
      category: "문맥 어휘 빈칸 추론 (Sentence Cloze)",
      question: "다음 지문의 흐름으로 보아, 밑줄 친 빈칸에 들어갈 가장 적절한 어휘를 고르시오.",
      questionKo: "문맥상의 인과와 수식 관계를 고려하여 빈칸에 가장 알맞은 어휘를 선택하시오.",
      contextSentence: blankSentenceEn,
      contextSentenceKo: targetSentence.ko,
      options: shuffled.map(item => item.text),
      answer: answerIdx,
      vocabBreakdown: [
        { word: foundWord, meaning: targetVocab.meaning || "정답 의미" },
        ...distractors
      ],
      explanation: `[문맥 근거 및 풀이]
지문의 전반적인 주제와 해당 문장의 문맥을 종합해 볼 때, 빈칸에는 '${foundWord}'(${targetVocab.meaning || '정답'})가 들어가야 자연스럽습니다.
다른 선택지들은 문맥상 정반대이거나(detrimental, superfluous) 글의 취지에 부합하지 않는 오답입니다.`
    };
  }

  function getEffectiveLogicBank() {
    if (typeof window !== "undefined" && window.MASTER_LOGIC_BANK && window.MASTER_LOGIC_BANK.length > 0) {
      return window.MASTER_LOGIC_BANK;
    }
    return FALLBACK_LOGIC_BANK;
  }

  /**
   * 3. 편입 논리완성 생성기 (Transfer Logic Completion)
   * 지문의 주제와 레벨에 맞는 300제 전문 편입 논리 문항 매핑
   */
  function generateTransferLogicQuiz(passage, indexOffset = 0) {
    const bank = getEffectiveLogicBank();
    const bankIndex = Math.abs(hashCode(passage.id || passage.title) + indexOffset) % bank.length;
    const baseLogic = bank[bankIndex];

    return {
      id: `tlogic-${passage.id}-${bankIndex}`,
      type: "logic",
      typeLabel: "편입 논리",
      level: baseLogic.level || 3,
      levelLabel: baseLogic.levelLabel || "Lv.3 상급",
      category: baseLogic.category,
      theme: baseLogic.theme,
      logicType: baseLogic.logicType,
      clue: baseLogic.clue,
      direction: baseLogic.direction,
      question: baseLogic.question,
      questionKo: baseLogic.questionKo,
      options: baseLogic.options,
      answer: baseLogic.answer,
      vocabBreakdown: baseLogic.vocabBreakdown,
      explanation: baseLogic.explanation
    };
  }

  function hashCode(str) {
    let hash = 0;
    for (let i = 0; i < str.length; i++) {
      hash = (hash << 5) - hash + str.charCodeAt(i);
      hash |= 0;
    }
    return hash;
  }

  return {
    /**
     * 특정 지문에 대한 독해 + 파생 퀴즈 통합 세트 (지문 당 2~4문제 표준화)
     * [01]: 기본 독해 이해 / 주제 파악 (Comprehension)
     * [02]: 세부 내용 일치 / 문맥 추론 (Inference / Detail)
     * [03]: 학술 빈칸 추론 (Sentence Cloze)
     * [04]: (고급/심화) 편입 논리완성 (Transfer Logic Completion)
     */
    getEnrichedQuizzesForPassage: function(passage) {
      if (!passage) return [];

      const result = [];
      const baseQuizzes = passage.quiz || [];
      const level = (passage.level || 'Intermediate').toLowerCase();

      // 결정론적 타겟 문항 수 (2~4문제 엄격 준수)
      // Beginner: 2~3문제, Intermediate: 3문제, Advanced: 3~4문제
      const hash = Math.abs(hashCode(passage.id || passage.title || "passage"));
      let targetCount = 3;
      if (level === 'beginner') {
        targetCount = (hash % 2 === 0) ? 2 : 3;
      } else if (level === 'intermediate') {
        targetCount = 3;
      } else { // advanced
        targetCount = (hash % 2 === 0) ? 3 : 4;
      }

      // 1. 기본 독해 이해 문제 (1~2문항 우선 배치)
      const numComprehension = targetCount === 2 ? 1 : (targetCount === 4 ? 2 : (baseQuizzes.length >= 2 ? 2 : 1));
      for (let i = 0; i < Math.min(numComprehension, baseQuizzes.length); i++) {
        result.push({
          ...baseQuizzes[i],
          type: "comprehension",
          typeLabel: "독해 일치/추론"
        });
      }

      // 2. 학술 문맥 빈칸 추론 (Sentence Cloze)
      if (result.length < targetCount) {
        const clozeQuiz = generateClozeQuiz(passage);
        if (clozeQuiz) {
          result.push(clozeQuiz);
        }
      }

      // 3. 편입 논리완성 또는 문단 순서 문제 (목표 문항 수 충족)
      if (result.length < targetCount) {
        if (level === 'advanced' || hash % 2 === 0) {
          const logicQuiz = generateTransferLogicQuiz(passage);
          if (logicQuiz) result.push(logicQuiz);
        } else {
          const orderQuiz = generateOrderingQuiz(passage);
          if (orderQuiz) result.push(orderQuiz);
        }
      }

      // 만약 생성기가 null을 반환하여 목표에 미달하면 남은 기본 퀴즈로 보충
      if (result.length < targetCount && baseQuizzes.length > result.length) {
        for (let i = result.length; i < baseQuizzes.length && result.length < targetCount; i++) {
          result.push({
            ...baseQuizzes[i],
            type: "comprehension",
            typeLabel: "독해 일치"
          });
        }
      }

      // 안전 장치: 최소 2문제 보장
      if (result.length < 2 && baseQuizzes.length > 0) {
        baseQuizzes.forEach((q, idx) => {
          if (result.length < 2 && !result.some(r => r.question === q.question)) {
            result.push({ ...q, type: "comprehension", typeLabel: "독해 일치" });
          }
        });
      }

      // 엄격한 범위 보장: 2 <= 문항 수 <= 4
      return result.slice(0, 4);
    },

    /**
     * 상단 헤더 [편입 논리 특훈 랩] 전용 문제 세트 반환 (300제 지원)
     */
    getMasterLogicBank: function() {
      return getEffectiveLogicBank();
    }
  };

})();

// Node 환경 호환 수출
if (typeof module !== "undefined" && module.exports) {
  module.exports = DerivativeQuizEngine;
}
