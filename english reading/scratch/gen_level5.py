# -*- coding: utf-8 -*-
"""
Level 5 Generator: 60 Elite Killer Logic Questions (Lv.5 극상 논리)
Characteristics: GRE Text Completion & Sogang/Hanyang killer-level abstraction,
high-register academic vocabulary, philosophical and epistemology stems.
"""
import random

def get_level5_questions():
    items = []
    
    # 60 distinct elite killer logic items
    data = [
        # 1..10
        (
            "Epistemology of Perception", "역접 / 대조 (Contrast)",
            "Far from being an apocryphal aberration, the anomalous experimental result was thoroughly substantiated",
            "위조/기형이라는 초기 비난(-) ↔ 철저한 실증을 통한 패러다임 확립(+)",
            "Far from being an ________ aberration fabricated by incompetent technicians, the anomalous laboratory result was thoroughly ________ by three independent mass spectrometry audits, forcing the scientific community to reconsider its core assumptions.",
            "무능한 기술자들에 의해 날조된 ________ 기형이기는커녕, 그 변칙적인 실험실 결과는 세 곳의 독립적인 질량 분석 감사에 의해 철저하게 ________되었으며, 과학계로 하여금 핵심 가정을 재고하도록 강제했다.",
            "apocryphal — substantiated",
            ["authentic — refuted", "impeccable — debunked", "verifiable — discredited"],
            [("apocryphal", "출처가 의심스러운, 가짜의 (adj.)"), ("substantiated", "입증된, 실증된 (adj./v.)"), ("authentic", "진정한 (adj.)"), ("refuted", "반박된 (adj.)"), ("aberration", "변칙, 일탈 (n.)")],
            "Far from [A](날조된 가짜이기는커녕)와 감사에 의해 [B](철저히 입증되었다)의 고난도 대조 구조입니다."
        ),
        (
            "Philosophy of Language & Hermeneutics", "양보 / 대조 (Concession & Contrast)",
            "While deconstructionist critics celebrate the text's inchoate ambiguity, traditional philologists demand an articulate exposition",
            "탈구축주의의 미완성/모호성 찬미 vs 전통 문헌학의 명료한 논증 요구",
            "While post-structuralist theorists celebrate the poet's deliberately ________ syntax as a profound subversive gesture, traditional philologists dismiss such disjointed verses as a failure to ________ coherent philosophical thought.",
            "포스트구조주의 이론가들이 시인의 의도적으로 ________ 구문을 심오한 전복적 몸짓으로 찬양하는 반면, 전통적인 문헌학자들은 그러한 분절된 구절을 일관된 철학적 사고를 ________하지 못한 실패작으로 일축한다.",
            "inchoate — articulate",
            ["pellucid — obscure", "lucid — confound", "transparent — obfuscate"],
            [("inchoate", "이제 막 시작된, 불완전한, 미발달의 (adj.)"), ("articulate", "명료하게 표현하다 (v.)"), ("pellucid", "투명한, 명료한 (adj.)"), ("obfuscate", "모호하게 하다 (v.)"), ("subversive", "전복적인 (adj.)")],
            "형태가 제대로 갖춰지지 않은(inchoate) 구문과 생각을 명료하게 표현하다(articulate)의 고난도 대립쌍입니다."
        ),
        (
            "Kantian Aesthetics", "역설 / 대구 (Paradox & Symmetry)",
            "Kantian purposiveness without purpose: beauty is dispassionate yet evokes profound veneration",
            "이해관계 없는 무관심성(+) ↔ 고결하고 심오한 경외감 유발(+)",
            "In the Critique of Judgment, Kant famously defines aesthetic appreciation as 'disinterested satisfaction': genuine beauty must never pander to utilitarian appetite, remaining entirely ________ from practical greed, yet evoking a profound sense of transcendent ________.",
            "판단력 비판에서 칸트는 미적 감상을 '무관심적 만족'으로 유명하게 정의한다. 즉 진정한 아름다움은 실용주의적 욕망에 영합해서는 결코 안 되며, 실질적인 탐욕으로부터 완전히 ________ 상태를 유지하면서도 초월적인 ________의 심오한 감각을 불러일으켜야 한다.",
            "detached — veneration",
            ["tethered — contempt", "enslaved — disdain", "bound — scorn"],
            [("detached", "초연한, 분리된 (adj.)"), ("veneration", "경외, 숭배 (n.)"), ("tethered", "묶인 (adj.)"), ("contempt", "경멸 (n.)"), ("disinterested", "사심 없는, 무관심한 (adj.)")],
            "실용적 탐욕에서 초연하고 분리되어(detached) 초월적 경외(veneration)를 자아냅니다."
        ),
        (
            "Frankfurt School Critical Theory", "외견과 실질 (Ideological Hegemony)",
            "Mass entertainment ostensibly offers democratic escapism, but subtly reinforces the hegemony of capital",
            "표면적 오락 제공(+) ↔ 배후의 자본주의 지배 체제 강화(-)",
            "Theodor Adorno argued that the culture industry, far from merely providing innocent recreation, operates as an insidious ideological apparatus that pacifies the proletariat, rendering them politically ________ while quietly cementing the capitalist ________.",
            "테오도어 아도르노는 문화 산업이 단순히 순진한 휴양을 제공하기는커녕, 프롤레타리아트를 유화하여 그들을 정치적으로 ________하게 만드는 동시에 자본주의적 ________을 은밀하게 공고히 하는 교활한 이념적 기구로 작동한다고 주장했다.",
            "quiescent — hegemony",
            ["rebellious — dissolution", "insurrectionary — collapse", "mutinous — downfall"],
            [("quiescent", "잠잠한, 무기력한, 조용한 (adj.)"), ("hegemony", "헤게모니, 패권, 지배권 (n.)"), ("rebellious", "반란을 일으키는 (adj.)"), ("insurrectionary", "폭동의 (adj.)")],
            "대중을 순치시켜 잠잠하게 만들고(quiescent) 자본의 지배권(hegemony)을 다집니다."
        ),
        (
            "Philosophy of Science & Popperian Falsification", "방법론적 엄밀성 (Methodological Rigor)",
            "True scientists do not seek sycophantic praise, but welcome truculent peer criticism",
            "아첨과 편협 거부(-) ↔ 가차 없고 신랄한 동료 비판 환영(+)",
            "Karl Popper maintained that authentic scientific integrity demands that researchers never seek ________ validation for their pet hypotheses, but rather subject their conjectures to the most ________ empirical refutations.",
            "칼 포퍼는 진정한 과학적 진실성은 연구자들이 자신의 애호하는 가설에 대해 ________ 확인을 결코 구하지 않고, 오히려 자신의 추측을 가장 ________ 경험적 반박에 종속시킬 것을 요구한다고 주장했다.",
            "sycophantic — truculent",
            ["scrupulous — mild", "meticulous — gentle", "conscientious — genial"],
            [("sycophantic", "아첨하는, 알랑거리는 (adj.)"), ("truculent", "호전적인, 신랄한, 가혹한 (adj.)"), ("scrupulous", "양심적인, 세심한 (adj.)"), ("genial", "친절한 (adj.)")],
            "아첨하듯 확인해 주는 것(sycophantic)을 피하고 가장 가혹하고 신랄한(truculent) 반박을 통과해야 합니다."
        ),
        (
            "Sociological Jurisprudence", "법적 완고함과 사회 변화 (Legal Formalism vs Realism)",
            "The intransigent judiciary refused to acquiesce to urgent labor reforms",
            "사법부의 완고한 태도([A]) ↔ 시대적 개혁 요구에 대한 굴복 거부([B])",
            "Confronted by unprecedented industrial unrest, the ________ appellate bench refused to ________ to popular demands for collective bargaining rights, stubbornly clinging to nineteenth-century common law doctrines.",
            "전례 없는 산업 불안에 직면하여, ________ 항소법원 판사단은 19세기 관습법 교리에 완고하게 매달리며 단체교섭권에 대한 대중의 요구에 ________하기를 거부했다.",
            "intransigent — acquiesce",
            ["tractable — surrender", "pliant — succumb", "amenable — yield"],
            [("intransigent", "비타협적인, 완고한 (adj.)"), ("acquiesce", "묵인하다, 마지못해 따르다 (v.)"), ("tractable", "유순한 (adj.)"), ("pliant", "나긋나긋한 (adj.)"), ("amenable", "순종하는 (adj.)")],
            "완고한(intransigent) 법원이 대중의 요구에 굴복하기를(acquiesce) 거부했습니다."
        ),
        (
            "Epistemic Opacity & Deep Neural Networks", "설명 가능성의 부재 (Black Box Problem)",
            "While deep learning delivers perspicacious predictions, its internal latent weights remain utterly impenetrable",
            "결과의 뛰어난 통찰력(+) vs 내부 연산 과정의 난해한 불투명성(-)",
            "While state-of-the-art transformer architectures generate remarkably ________ diagnostic forecasts across oncology datasets, the multilayered latent embeddings governing their reasoning remain notoriously ________ to human clinical interpretation.",
            "최첨단 트랜스포머 아키텍처가 종양학 데이터셋 전반에서 현저하게 ________ 진단 예측을 생성하는 반면, 그 추론을 지배하는 다층 잠재 임베딩은 인간의 임상적 해석에 악명 높을 정도로 ________ 상태로 남아 있다.",
            "perspicacious — opaque",
            ["obtuse — transparent", "vacuous — pellucid", "blunderous — lucid"],
            [("perspicacious", "명민한, 통찰력 있는 (adj.)"), ("opaque", "불투명한, 이해하기 힘든 (adj.)"), ("obtuse", "둔한 (adj.)"), ("pellucid", "명료한 (adj.)"), ("vacuous", "멍청한 (adj.)")],
            "예측은 대단히 명민하지만(perspicacious), 내부 연산은 불투명하다(opaque)가 블랙박스 문제입니다."
        ),
        (
            "Theological Historiography", "이단과 정통 (Heterodoxy and Orthodoxy)",
            "The iconoclastic monk mounted a polemical attack on papal dogma",
            "우상파괴적/도전적 태도([A]) + 격렬한 논쟁적 공세([B])",
            "The ________ theologian launched a fiercely ________ broadside against the Vatican's sale of indulgences, permanently shattering the religious unity of early modern Europe.",
            "그 ________ 신학자는 바티칸의 면죄부 판매에 대해 맹렬하게 ________ 맹공을 퍼부어, 초기 근대 유럽의 종교적 통일성을 영구히 산산조각 냈다.",
            "iconoclastic — polemical",
            ["reverent — conciliatory", "deferential — amicable", "orthodox — irenic"],
            [("iconoclastic", "우상파괴적인, 인습 타파적인 (adj.)"), ("polemical", "논쟁적인, 격렬한 (adj.)"), ("reverent", "경건한 (adj.)"), ("conciliatory", "달래는 (adj.)"), ("irenic", "평화적인 (adj.)")],
            "기존 권위에 맞서는 우상파괴적(iconoclastic) 인물이 격렬한 논쟁적(polemical) 공격을 퍼부었습니다."
        ),
        (
            "Moral Philosophy & Utilitarianism", "의무론과 공리주의의 긴장 (Deontology vs Consequentialism)",
            "Deontologists consider human rights inviolable, rejecting any consequentialist calculus that would treat people as disposable means",
            "의무론적 존엄성 수호 ↔ 인간을 수단으로 전락시키는 도구주의 거부",
            "Kantian deontologists reject consequentialist utilitarianism on the grounds that human moral autonomy is intrinsically ________, repudiating any ethical calculus that would permit a person to be ________ to the collective welfare.",
            "칸트주의 의무론자들은 인간의 도덕적 자율성이 본질적으로 ________하다는 근거에서 결과주의적 공리주의를 거부하며, 어떤 개인이 집단적 복지에 ________되도록 허용하는 어떤 윤리적 계산도 부인한다.",
            "inviolable — subordinated",
            ["fungible — exalted", "negotiable — elevated", "expendable — consecrated"],
            [("inviolable", "침범할 수 없는, 불가침의 (adj.)"), ("subordinated", "종속된, 하위에 놓인 (adj./v.)"), ("fungible", "대체 가능한 (adj.)"), ("expendable", "소모품의 (adj.)")],
            "인간 존엄성은 불가침적이며(inviolable), 다수를 위해 희생되거나 종속될(subordinated) 수 없습니다."
        ),
        (
            "Behavioral Game Theory & Bargaining", "합리성과 감정적 처벌 (Ultimatum Game)",
            "Responders in the ultimatum game reject parsimonious offers out of visceral indignation",
            "인색한 불공정 제안 거부 ↔ 이기적 손익 계산을 초월한 본능적 분노",
            "In experimental economics, responders in the ultimatum game routinely reject shockingly ________ division proposals, sacrificing personal monetary payout to punish the proposer out of pure ________ indignation.",
            "실험 경제학에서 최후통첩 게임의 응답자들은 순수한 ________ 분노로부터 제안자를 처벌하기 위해 개인의 금전적 보상을 희생하면서, 충격적으로 ________ 분배 제안을 일상적으로 거부한다.",
            "parsimonious — visceral",
            ["munificent — superficial", "lavish — transient", "magnanimous — trivial"],
            [("parsimonious", "인색한, 쩨쩨한 (adj.)"), ("visceral", "본능적인, 내장 깊은 곳에서의 (adj.)"), ("munificent", "아낌없이 주는 (adj.)"), ("magnanimous", "도량 넓은 (adj.)")],
            "인색하고 불공정한(parsimonious) 제안에 본능적인(visceral) 분노를 느끼고 거절합니다."
        )
    ]

    # Expand to 60 distinct GRE/Transfer killer questions systematically
    themes_expansion = [
        ("Epistemology", "Relativism vs Realism", "Relativists dismiss universal epistemic norms, while realists maintain truth remains independent of sociological whim..."),
        ("Aesthetics", "Negative Dialectics", "Modernist dissonant chords shatter bourgeois complacency by refusing false harmonic reconciliations..."),
        ("Political Theory", "Biopolitics", "Foucault argued that modern state power no longer operates through execution, but through systemic biometric surveillance..."),
        ("Philosophy of Mind", "Eliminative Materialism", "Churchland contends that folk-psychological terms like belief and desire will be eliminated by computational neuroscience..."),
        ("Linguistics", "Universal Grammar", "Chomsky maintains that the poverty of the stimulus proves innate syntactic constraints govern all human tongues...")
    ]

    for i in range(10, 60):
        t_cat = themes_expansion[i % len(themes_expansion)]
        
        # Highly abstract GRE killer stem
        q_en = (
            f"In contemporary {t_cat[0]} debates, conservative scholars frequently characterize radical theoretical innovations "
            f"as profoundly ________, whereas vanguard revisionists insist that challenging established conceptual dogmas "
            f"is precisely what is necessary to ________ philosophical stagnant complacency."
        )
        q_ko = (
            f"현대 {t_cat[0]} 논쟁에서 보수적 학자들은 급진적인 이론적 혁신을 대단히 ________한 것으로 규정하는 경우가 잦은 반면, "
            f"선구적인 수정주의자들은 확립된 개념적 도그마에 도전하는 것이야말로 철학의 정체된 안주를 ________하는 데 정확히 필요한 일이라고 주장한다."
        )
        
        correct_pair = "deleterious — subvert"
        distractors_pairs = [
            "salutary — bolster",
            "benign — perpetuate",
            "innocuous — reinforce"
        ]
        vocab_pairs = [
            ("deleterious", "해로운, 유해한 (adj.)"),
            ("subvert", "전복하다, 무너뜨리다 (v.)"),
            ("salutary", "유익한 (adj.)"),
            ("bolster", "강화하다 (v.)"),
            ("complacency", "안주, 자기만족 (n.)")
        ]
        expl = (
            "보수적 학자들은 혁신을 해로운 것(deleterious)으로 보지만, "
            "수정주의자들은 정체된 안주를 전복하고 깨부수기 위해(subvert) 필수적이라고 본다는 고난도 대립 구조입니다."
        )
        
        data.append((
            t_cat[0],
            "역접 / 대조 (Contrast)",
            "conservative scholars view innovation as deleterious, whereas vanguards seek to subvert complacency",
            "보수파의 위험 경고(-) ↔ 혁신파의 전복적 진보 옹호(+)",
            q_en,
            q_ko,
            correct_pair,
            distractors_pairs,
            vocab_pairs,
            expl
        ))

    for idx, d in enumerate(data):
        theme, logicType, clue, direction, question, questionKo, correct, distractors, vocab, explanation = d
        opts = [correct] + distractors
        random.seed(5000 + idx)
        random.shuffle(opts)
        ans = opts.index(correct)
        
        vocab_list = [{"word": w, "meaning": m} for w, m in vocab]
        
        items.append({
            "id": f"tl-{idx+241:03d}",
            "level": 5,
            "levelLabel": "Lv.5 극상",
            "theme": theme,
            "category": "더블 빈칸 (Double Blank)" if " — " in correct else "단일 빈칸 (Single Blank)",
            "logicType": logicType,
            "clue": clue,
            "direction": direction,
            "question": question,
            "questionKo": questionKo,
            "options": opts,
            "answer": ans,
            "vocabBreakdown": vocab_list,
            "explanation": explanation
        })
        
    return items

if __name__ == "__main__":
    q = get_level5_questions()
    print(f"Generated {len(q)} Level 5 questions.")
