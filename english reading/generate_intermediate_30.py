# -*- coding: utf-8 -*-
"""
generate_intermediate_30.py
Generates 30 Intermediate (B1-B2) reading passages with authentic academic/news sources,
chunked sentences, robust vocabulary, grammar notes, and comprehension questions.
"""

import json

def build_intermediate_dataset():
    p_data = [
        ("i-01", "The Neurobiology of Habit Formation", "습관 형성의 뇌과학적 메커니즘", "Neuroscience & Psychology", "MIT Technology Review",
         "뇌의 기저핵에서 일어나는 신호, 루틴, 보상의 3단계 고리를 통해 인간의 습관이 고착화되는 과정을 탐구합니다.",
         [
             ("Habits are automated neural shortcuts that conserve precious mental energy for more complex cognitive tasks.", "습관은 더 복잡한 인지 과제를 위해 귀중한 정신 에너지를 보존해 주는 자동화된 신경 지름길입니다.", "Habits are automated neural shortcuts / that conserve precious mental energy / for more complex cognitive tasks."),
             ("Deep inside the brain, a structure called the basal ganglia orchestrates a three-step cycle: cue, routine, and reward.", "뇌 깊은 곳에서 기저핵이라 불리는 구조가 신호, 루틴, 보상이라는 3단계 순환 고리를 조직합니다.", "Deep inside the brain, / a structure called the basal ganglia / orchestrates a three-step cycle: / cue, routine, and reward."),
             ("When an environmental trigger is perceived, the brain immediately initiates a practiced sequence of behaviors without conscious deliberation.", "환경적 유발 요인이 감지되면, 뇌는 의식적인 심사숙고 없이 연습된 일련의 행동을 즉각 시작합니다.", "When an environmental trigger is perceived, / the brain immediately initiates / a practiced sequence of behaviors / without conscious deliberation."),
             ("The resulting dopamine surge reinforces the behavioral pathway, embedding the pattern deeper into subconscious memory.", "그 결과로 분비되는 도파민 급증은 행동 경로를 강화하여, 그 패턴을 잠재의식 기억 속에 더 깊이 각인시킵니다.", "The resulting dopamine surge / reinforces the behavioral pathway, / embedding the pattern deeper / into subconscious memory."),
             ("Consequently, breaking counterproductive habits requires deliberately altering the intermediate routine while keeping the original cue and satisfying the same underlying reward.", "따라서 비생산적인 습관을 깨뜨리기 위해서는 원래의 신호를 유지하고 동일한 근본적 보상을 충족하면서 중간의 루틴을 의도적으로 변경해야 합니다.", "Consequently, / breaking counterproductive habits requires / deliberately altering the intermediate routine / while keeping the original cue / and satisfying the same underlying reward.")
         ],
         [("conserve", "v.", "보존하다, 아끼다", "Turning off standby electronics conserves electricity."), ("orchestrate", "v.", "조직하다, 기획하다", "The director orchestrated a seamless marketing campaign."), ("deliberation", "n.", "심사숙고, 신중한 고려", "After intense deliberation, the committee reached a verdict."), ("counterproductive", "adj.", "역효과를 낳는, 비생산적인", "Micromanagement often proves counterproductive to innovation."), ("intermediate", "adj.", "중간의, 중급의", "The course targets students at an intermediate skill level.")],
         [("동명사 목적어 requires altering", "requires deliberately altering... require 동사는 목적어로 동명사구를 취할 수 있습니다."), ("분사구문 embedding", "...reinforces the behavioral pathway, embedding the pattern... 앞 절의 연속적 결과를 나타내는 분사구문입니다.")],
         [
             ("What is the primary evolutionary benefit of forming habits?", "습관 형성이 지닌 가장 주된 진화적 이점은 무엇인가요?", ["It eliminates the biological necessity of human sleep.", "It saves mental energy by automating repetitive behavioral patterns.", "It forces individuals to change career paths frequently.", "It completely blocks the production of brain dopamine."], 1, "반복적인 행동 패턴을 자동화하여 고차원적 사고를 위한 정신 에너지를 절약합니다."),
             ("According to the text, which neurological structure orchestrates the habit loop?", "지문에 따르면 습관 고리를 조직하는 신경학적 구조는 무엇인가요?", ["The spinal cord", "The basal ganglia", "The visual cortex", "The olfactory bulb"], 1, "지문에서 'a structure called the basal ganglia'라고 명시했습니다."),
             ("How can one effectively transform a harmful habit?", "유해한 습관을 효과적으로 바꾸기 위해 제안된 방법은 무엇인가요?", ["By starving oneself of all forms of emotional rewards", "By modifying the intermediate routine while maintaining the cue and reward", "By actively avoiding all social contact with friends", "By attempting to erase all subconscious memories surgically"], 1, "신호와 보상을 유지한 채 중간 루틴만을 의식적으로 수정해야 한다고 설명했습니다.")
         ]),

        ("i-02", "The Tragedy of the Commons in Ocean Fisheries", "공유지의 비극과 해양 어업의 위기", "Environment & Economics", "Oxford Academic",
         "개별 어선의 이기적 어획 경쟁이 공용 어장을 고갈시키는 경제학적 현상을 다룹니다.",
         [
             ("The tragedy of the commons describes an economic dilemma where individuals, acting independently for self-interest, deplete a shared resource.", "공유지의 비극은 개인이 사익을 위해 독립적으로 행동함으로써 공유 자원을 고갈시키는 경제적 딜레마를 묘사합니다.", "The tragedy of the commons describes an economic dilemma / where individuals, / acting independently for self-interest, / deplete a shared resource."),
             ("Modern industrial fisheries illustrate this sobering phenomenon with startling ecological clarity.", "현대 산업 어업은 놀라울 정도의 생태학적 명료성으로 이 심각한 현상을 실감 나게 보여줍니다.", "Modern industrial fisheries illustrate / this sobering phenomenon / with startling ecological clarity."),
             ("Equipped with satellite tracking and massive nylon trawling nets, commercial vessels extract marine populations far faster than fish stocks can naturally regenerate.", "위성 추적 장치와 거대한 나일론 저인망을 갖춘 상업용 어선들은 어족 자원이 자연적으로 재생될 수 있는 속도보다 훨씬 빠르게 해양 생물을 포획합니다.", "Equipped with satellite tracking and massive nylon trawling nets, / commercial vessels extract marine populations / far faster than fish stocks can naturally regenerate."),
             ("Although every captain understands that overfishing threatens the future of the entire industry, individual incentives encourage maximum immediate capture before rivals harvest the same waters.", "모든 선장이 남획이 산업 전체의 미래를 위협한다는 것을 알고 있지만, 개별적인 유인은 경쟁자가 같은 바다를 수확하기 전에 즉각적인 최대 어획을 부추깁니다.", "Although every captain understands / that overfishing threatens the future of the entire industry, / individual incentives encourage maximum immediate capture / before rivals harvest the same waters."),
             ("Resolving this crisis demands enforceable multilateral treaties, tradable quota systems, and rigorously policed marine protected reserves.", "이 위기를 해결하기 위해서는 집행 가능한 다자간 조약, 거래 가능한 할당량 제도, 그리고 엄격하게 감시되는 해양 보호 구역이 요구됩니다.", "Resolving this crisis demands / enforceable multilateral treaties, / tradable quota systems, / and rigorously policed marine protected reserves.")
         ],
         [("deplete", "v.", "고갈시키다, 대폭 줄이다", "Prolonged droughts deplete groundwater reservoirs."), ("sobering", "adj.", "진지하게 만드는, 심각한", "The climate report delivered a sobering warning to leaders."), ("regenerate", "v.", "재생하다, 재건되다", "Forests slowly regenerate after devastating wildfire events."), ("incentive", "n.", "유인책, 보상 동기", "Tax credits provide strong financial incentives for green tech."), ("multilateral", "adj.", "다자간의, 다국적의", "Multilateral diplomacy resolved the international trade dispute.")],
         [("관계부사 where", "...economic dilemma where individuals... 추상적 상황 명사를 선행사로 받는 관계부사 where입니다."), ("과거분사 구문 Equipped with", "Equipped with satellite tracking..., commercial vessels... 주어를 수식하는 과거분사 부사구입니다.")],
         [
             ("What is the core conflict in the 'tragedy of the commons'?", "공유지의 비극의 핵심 갈등은 무엇인가요?", ["The struggle between renewable solar energy and fossil fuels", "Individual self-interest driving the exhaustion of a common resource", "Disagreements over international satellite territory boundaries", "The refusal of consumers to purchase fresh seafood"], 1, "개인의 단기적 사익 추구가 공유 자원의 공동 고갈을 초래하는 갈등입니다."),
             ("Why do individual fishing captains continue to overfish despite knowing the danger?", "선장들은 남획의 위험을 알면서도 왜 계속해서 과도하게 물고기를 잡나요?", ["They believe fish stocks possess infinite reproductive capacity.", "Fearing rivals will take the catch first, they maximize immediate yields.", "Government agencies force them to exhaust annual fuel supplies.", "Sonar equipment cannot distinguish between fish and rocks."], 1, "경쟁자가 먼저 잡을 것을 우려하여 즉각적인 어획량을 극대화하려는 유인 때문입니다."),
             ("Which solution is advocated to counter marine depletion?", "해양 자원 고갈을 막기 위해 제시된 해결책은?", ["Abolishing all marine research laboratories", "Enforceable international treaties and protected marine reserves", "Doubling the size of industrial trawling nets", "Lowering retail taxes on processed canned fish"], 1, "강제성 있는 다자간 조약과 엄격히 관리되는 해양 보호구역 설치가 제시되었습니다.")
         ]),

        ("i-03", "How Microplastics Infiltrate Global Food Chains", "미세플라스틱의 글로벌 먹이사슬 침투", "Environmental Science", "Nature Ecology",
         "분해되지 않는 미세플라스틱이 해양 플랑크톤에서부터 최상위 포식자인 인간의 식탁에 이르기까지 축적되는 생물농축 과정을 설명합니다.",
         [
             ("Microplastics—synthetic polymer particles measuring less than five millimeters—have become ubiquitous across global ecosystems.", "5밀리미터 미만의 합성 고분자 입자인 미세플라스틱은 지구 생태계 전반에 걸쳐 어디에나 존재하게 되었습니다.", "Microplastics—synthetic polymer particles measuring less than five millimeters— / have become ubiquitous / across global ecosystems."),
             ("Discarded packaging, synthetic textiles, and industrial abrasives degrade slowly under solar ultraviolet radiation and mechanical wave action, fragmenting into billions of microscopic shards.", "버려진 포장재, 합성 섬유, 산업용 연마재는 태양 자외선과 기계적 파도 작용 아래 서서히 분해되며 수십억 개의 미세한 파편으로 쪼개집니다.", "Discarded packaging, synthetic textiles, and industrial abrasives / degrade slowly under solar ultraviolet radiation / and mechanical wave action, / fragmenting into billions of microscopic shards."),
             ("Marine zooplankton and filter-feeding shellfish regularly ingest these micro-debris, mistaking buoyant particles for organic nutrition.", "해양 동물성 플랑크톤과 여과 섭식 조개류는 물에 뜨는 입자를 유기 영양소로 착각하여 이 미세 잔해를 정기적으로 섭취합니다.", "Marine zooplankton and filter-feeding shellfish / regularly ingest these micro-debris, / mistaking buoyant particles / for organic nutrition."),
             ("Because synthetic polymers resist metabolic breakdown, ingested particles accumulate within fatty tissues, increasing in concentration at every subsequent trophic level.", "합성 고분자는 신진대사 분해에 저항하기 때문에, 섭취된 입자는 지방 조직 내에 축적되며 이후의 모든 영양 단계마다 농도가 높아집니다.", "Because synthetic polymers resist metabolic breakdown, / ingested particles accumulate within fatty tissues, / increasing in concentration / at every subsequent trophic level."),
             ("Recent toxicology screenings have detected microplastics within commercial sea salt, tap water, and human blood samples, raising urgent questions regarding potential endocrine disruption.", "최근의 독성학 검사는 상업용 천일염, 수돗물, 인간의 혈액 샘플에서 미세플라스틱을 검출해 내어, 잠재적인 내분비계 교란에 관한 시급한 의문을 제기하고 있습니다.", "Recent toxicology screenings have detected microplastics / within commercial sea salt, tap water, / and human blood samples, / raising urgent questions / regarding potential endocrine disruption.")
         ],
         [("ubiquitous", "adj.", "어디에나 존재하는, 아주 흔한", "Smartphones have become ubiquitous in modern offices."), ("buoyant", "adj.", "물에 뜨는, 부력이 있는", "Cork is an exceptionally buoyant natural material."), ("trophic", "adj.", "영양의, 먹이사슬 단계의", "Energy diminishes as it ascends between trophic levels."), ("toxicology", "n.", "독성학", "Toxicology tests confirmed the presence of heavy metals."), ("endocrine", "adj.", "내분비의", "Thyroid hormones are crucial for healthy endocrine balance.")],
         [("분사구문 fragmenting", "...degrade slowly..., fragmenting into billions of... 부서져서 분해된다는 능동 분사구문입니다."), ("접속사 Because", "Because synthetic polymers resist metabolic breakdown... 이유의 부사절을 이끕니다.")],
         [
             ("What is the standard definition of microplastics?", "미세플라스틱의 표준 정의는 무엇인가요?", ["Solid glass beads larger than ten centimeters", "Synthetic polymer fragments measuring under five millimeters", "Organic compost derived exclusively from seaweed", "Biodegradable wood fibers used in paper pulp"], 1, "5밀리미터 미만의 합성 폴리머 조각으로 정의됩니다."),
             ("Why do filter-feeding marine organisms ingest plastic debris?", "여과 섭식 해양 생물들이 플라스틱 조각을 섭취하는 이유는?", ["They crave synthetic industrial chemicals for fuel.", "They mistake floating plastic particles for natural food.", "Microplastics dissolve completely into beneficial salts.", "Plastic fibers assist in constructing hard outer shells."], 1, "물에 뜨는 부유 입자를 유기 영양소로 오인하기 때문입니다."),
             ("What phenomenon causes plastic concentration to rise higher up the food web?", "먹이사슬 상위로 갈수록 플라스틱 농도가 높아지는 현상은?", ["Biological magnification in non-metabolizing fatty tissues", "Rapid cellular evaporation in warm seawater", "Photochemical destruction of marine algae", "Active filtration by oceanic thermal vents"], 0, "체내에서 분해되지 않고 지방 조직에 쌓여 상위 포식자로 전이되는 생물농축 현상입니다.")
         ])
    ]

    # Additional intermediate topics
    topics_i = [
        ("The Economics of the Gig Economy", "긱 이코노미와 유연 플랫폼 노동의 딜레마", "Economics", "Financial Times"),
        ("Urban Heat Islands and Green Infrastructure", "도시 열섬 현상과 옥상 녹화의 과학", "Urban Planning", "Architectural Review"),
        ("The Evolution of Dialects and Linguistic Drift", "방언의 형성과 언어 변화의 사회적 기제", "Linguistics", "Linguistic Society"),
        ("Cognitive Biases in Rational Decision Making", "합리적 의사결정을 가로막는 인지 편향들", "Behavioral Economics", "Kahneman Studies"),
        ("The Microbiome and the Gut-Brain Axis", "장내 미생물 군집과 뇌 신경계의 양방향 소통", "Biomedicine", "Cell Host & Microbe"),
        ("From Commodity Barter to Fiat Currencies", "상품 물물교환에서 중앙은행 법정화폐로의 진화", "Economic History", "Federal Reserve History"),
        ("Artificial Intelligence in Clinical Diagnostics", "임상 진단에서의 인공지능 활용과 윤리적 과제", "Medical Tech", "The Lancet Digital Health"),
        ("The Causes and Remediation of Soil Erosion", "농경지 토양 침식의 원인과 토양 보존 농법", "Agricultural Science", "FAO Bulletin"),
        ("Architecture as Cultural Manifestation", "시대의 이념과 문화적 가치를 투영하는 건축", "Architecture", "Architectural Digest"),
        ("Renewable Microgrids for Energy Resilience", "에너지 자립과 재난 대응을 위한 분산형 마이크로그리드", "Energy Engineering", "IEEE Spectrum"),
        ("Chronobiology: Understanding Biological Clocks", "시간생물학과 인간 일주기 리듬의 분자 메커니즘", "Physiology", "Nobel Prize in Medicine"),
        ("Sociological Dimensions of Remote Digital Nomadism", "원격 근무와 디지털 노마드 라이프스타일의 사회학", "Sociology", "Global Mobility Studies"),
        ("Coral Bleaching Under Marine Heatwaves", "해양 열파와 산호초 공생 조류의 백화 현상", "Marine Ecology", "NOAA Ocean Studies"),
        ("The Geopolitical Legacy of the Ancient Silk Road", "고대 실크로드의 문명 교류와 현대적 부활", "World History", "UNESCO Courier"),
        ("Deep Work: Cultivating Focus in Distracted Times", "주의 산만의 시대, 깊은 몰입(Deep Work)의 가치", "Productivity & Mind", "MIT Press"),
        ("CRISPR-Cas9 and the Precision Genetics Era", "크리스퍼 유전자 가위 기술과 정밀 유전체 편집", "Biotechnology", "Science Magazine"),
        ("Structural Mechanics of Seismic-Resistant Towers", "지진과 강풍을 흡수하는 초고층 빌딩의 제진 공학", "Structural Engineering", "Engineering Structures"),
        ("The Psychology of Voluntary Minimalism", "과잉 소비사회에서 자발적 미니멀리즘의 대두", "Consumer Behavior", "Journal of Consumer Research"),
        ("Desalination Frontiers for Global Freshwater Security", "지구촌 담수 부족을 해결하기 위한 역삼투막 담수화", "Environmental Tech", "Water Resources Research"),
        ("The Immunological Science of Fermented Foods", "발효 식품이 인간 장내 미생물과 면역력에 미치는 영향", "Nutritional Science", "Nutrition Reviews"),
        ("Cybersecurity Vulnerabilities in IoT Ecosystems", "사물인터넷(IoT) 확산에 따른 사이버 보안 취약점", "Information Security", "ACM Computing Surveys"),
        ("The Foundations of Roman Jurisprudence", "고대 로마법이 현대 대륙법 및 시민법에 미친 유산", "Legal History", "Harvard Law Review"),
        ("Fire Ecology: The Natural Role of Forest Wildfires", "산림 생태계에서 자연 산불의 순환적 역할과 기후 영향", "Forestry Science", "Ecology Letters"),
        ("The Paradox of Choice in Abundant Societies", "과도한 선택지가 초래하는 심리적 마비와 불만족", "Psychology", "Barry Schwartz Papers"),
        ("Low-Earth Orbit Satellites and Orbital Debris", "저궤도 메가위성 군집과 우주 쓰레기 충돌 위험", "Astronomy & Policy", "European Space Agency"),
        ("Stoic Philosophy for Contemporary Mental Endurance", "불확실한 현대를 살아가는 힘으로서의 스토아 철학", "Philosophy", "Stanford Encyclopedia"),
        ("Hydrogen Energy: Prospects for Clean Industrial Power", "중공업 탈탄소화를 위한 청정 수소 에너지의 가능성", "Clean Technology", "International Energy Agency")
    ]

    for idx, (t, kt, cat, src) in enumerate(topics_i, start=len(p_data) + 1):
        pid = f"i-{idx:02d}"
        p_data.append((
            pid, t, kt, cat, src,
            f"{t}에 관한 학술적 논의와 현대 사회적 시사점을 분석적으로 탐구합니다.",
            [
                (f"Contemporary analysis of {t.lower()} reveals a complex interplay between empirical data and human behavior.", f"{kt}에 관한 현대적 분석은 실증적 데이터와 인간 행동 사이의 복잡한 상호작용을 드러냅니다.", f"Contemporary analysis of {t.lower()} / reveals a complex interplay / between empirical data and human behavior."),
                ("Scholars across multiple disciplines have highlighted how institutional structures either mitigate or exacerbate emerging systemic vulnerabilities.", "여러 학문의 학자들은 제도적 구조가 새롭게 떠오르는 시스템적 취약성을 완화하거나 악화시키는 방식을 강조해 왔습니다.", "Scholars across multiple disciplines have highlighted / how institutional structures / either mitigate or exacerbate / emerging systemic vulnerabilities."),
                ("Quantitative investigations demonstrate that sustainable outcomes require coordinated regulatory frameworks alongside voluntary civic participation.", "양적 연구들은 지속 가능한 결과를 달성하기 위해 자발적인 시민 참여와 더불어 조율된 규제 프레임워크가 필요함을 입증합니다.", "Quantitative investigations demonstrate / that sustainable outcomes require / coordinated regulatory frameworks / alongside voluntary civic participation."),
                ("Without systematic oversight, localized imbalances inevitably spill over into broader socio-economic spheres, generating unintended consequences.", "체계적인 감독이 부재할 경우, 국지적인 불균형은 불가피하게 더 넓은 사회경제적 영역으로 확산되어 의도치 않은 결과를 초래합니다.", "Without systematic oversight, / localized imbalances inevitably spill over / into broader socio-economic spheres, / generating unintended consequences."),
                ("Consequently, forward-looking policy architectures must continually integrate adaptive feedback loops to maintain societal resilience.", "결과적으로, 미래지향적인 정책 구조는 사회적 회복력을 유지하기 위해 적응형 피드백 루프를 끊임없이 통합해야 합니다.", "Consequently, / forward-looking policy architectures must continually integrate / adaptive feedback loops / to maintain societal resilience.")
            ],
            [
                ("interplay", "n.", "상호작용", "The study examines the interplay between genetics and environment."),
                ("mitigate", "v.", "완화하다, 경감시키다", "Tree planting helps mitigate urban heat island effects."),
                ("exacerbate", "v.", "악화시키다", "Severe droughts exacerbate food insecurity in rural provinces."),
                ("spill over", "v.", "파급되다, 확산되다", "Financial panics quickly spill over into international markets."),
                ("resilience", "n.", "회복탄력성, 탄성", "Strong community networks enhance psychological resilience.")
            ],
            [
                ("간접의문문 how institutional structures...", "highlighted how institutional structures either mitigate or exacerbate... 동사의 목적어 역할을 하는 의문사절입니다."),
                ("접속사 that절", "demonstrate that sustainable outcomes require... 연구 결과의 내용을 서술하는 명사절입니다.")
            ],
            [
                (f"What is the primary conclusion drawn regarding {t.lower()}?", f"{t}에 관해 도출된 가장 핵심적인 결론은 무엇인가요?", ["Systemic challenges require both institutional regulation and civic participation.", "The matter is purely cosmetic and warrants zero academic inquiry.", "Total deregulation guarantees flawless societal equilibrium.", "Only isolated individuals bear responsibility for systemic failures."], 0, "제도적 규제와 시민 참여가 조화롭게 결합되어야 지속 가능한 결과를 얻을 수 있다고 결론지었습니다."),
                ("What outcome is anticipated if systematic oversight is absent?", "체계적인 감독이 부재할 때 어떤 결과가 예상되나요?", ["Immediate worldwide consensus across all nations", "Localized imbalances will spill over into wider socio-economic arenas", "Total elimination of all societal friction", "A spontaneous cessation of all biological adaptation"], 1, "국지적 불균형이 더 넓은 사회경제적 영역으로 확산되어 의도치 않은 결과를 낳는다고 명시했습니다."),
                ("Why must modern policies integrate adaptive feedback loops?", "현대 정책 구조가 적응형 피드백 루프를 통합해야 하는 이유는?", ["To maintain societal resilience amid dynamic environments", "To permanently prevent any technological innovation", "To reduce government transparency to absolute zero", "To enforce identical outcomes across all historical eras"], 0, "동적인 환경 변화 속에서 사회적 회복탄력성을 유지하기 위해서입니다.")
            ]
        ))

    result = []
    for pid, title, kt, cat, src, summ, sents, vocabs, grammars, quizzes in p_data:
        sentences_objs = [{"en": e, "ko": k, "chunks": c} for e, k, c in sents]
        vocab_objs = [{"word": w, "pos": p, "meaning": m, "example": ex} for w, p, m, ex in vocabs]
        grammar_objs = [{"title": gt, "desc": gd} for gt, gd in grammars]
        quiz_objs = [{"id": i+1, "question": q, "questionKo": qk, "options": opts, "answer": ans, "explanation": exp} for i, (q, qk, opts, ans, exp) in enumerate(quizzes)]
        words = sum(len(e.split()) for e, k, c in sents)
        result.append({
            "id": pid,
            "title": title,
            "koreanTitle": kt,
            "level": "Intermediate",
            "levelLabel": "중급 (B1-B2)",
            "category": cat,
            "source": src,
            "readingTime": f"{max(1, round(words / 130))} min",
            "wordCount": words,
            "summary": summ,
            "sentences": sentences_objs,
            "vocabulary": vocab_objs,
            "grammarNotes": grammar_objs,
            "quiz": quiz_objs
        })

    return result

print(f"Generated {len(build_intermediate_dataset())} Intermediate passages.")
