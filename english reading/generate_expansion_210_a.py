# -*- coding: utf-8 -*-
"""
generate_expansion_210_a.py
10 Advanced passages (a-61 to a-70)
B2-C1 level, authoritative sources, sentence chunks, vocabulary, grammar, and 3 deducible comprehension questions per passage.
"""

def get_expansion_210_a():
    return [
        (
            "a-61",
            "Kuhnian Paradigm Shifts and Incommensurability",
            "토머스 쿤의 패러다임 전환과 공약불가능성",
            "Philosophy of Science",
            "Stanford Encyclopedia of Philosophy & The Structure of Scientific Revolutions",
            "토머스 쿤은 과학의 발전이 선형적 지식 축적이 아니라, 정상과학의 변칙사태 누적과 비선형적 패러다임 혁명을 통해 이루어진다고 논증했습니다.",
            [
                ("In his seminal 1962 treatise, / Thomas Kuhn revolutionized the philosophy of science / by contesting the positivist dogma of cumulative scientific progress.",
                 "자신의 획기적인 1962년 논문에서, / 토머스 쿤은 누적적 과학 진보라는 실증주의적 교리에 이의를 제기함으로써 / 과학철학의 일대 변혁을 일으켰습니다.",
                 "In his seminal 1962 treatise, / Thomas Kuhn revolutionized / the philosophy of science / by contesting the positivist dogma / of cumulative scientific progress."),
                ("Kuhn argued that 'normal science' operates / within an entrenched conceptual paradigm / that dictates legitimate empirical inquiries and puzzle-solving protocols.",
                 "쿤은 '정상과학'이 / 정당한 실증적 탐구와 문제 해결 규약을 규정하는 / 확고히 자리 잡은 개념적 패러다임 내부에서 작동한다고 주장했습니다.",
                 "Kuhn argued that 'normal science' operates / within an entrenched conceptual paradigm / that dictates legitimate empirical inquiries / and puzzle-solving protocols."),
                ("However, / as anomalous empirical observations steadily accumulate / that cannot be accommodated within the existing framework, / the discipline enters a severe crisis.",
                 "그러나, / 기존 체계 내에서 수용될 수 없는 / 변칙적인 실증적 관찰들이 꾸준히 누적됨에 따라, / 해당 학문 분과는 심각한 위기에 봉착하게 됩니다.",
                 "However, / as anomalous empirical observations steadily accumulate / that cannot be accommodated within the existing framework, / the discipline enters a severe crisis."),
                ("The subsequent resolution involves a revolutionary paradigm shift / characterized by incommensurability, / meaning rival theories cannot be neutrally mapped or arbitrated using identical linguistic metrics.",
                 "그 뒤를 잇는 해결은 공약불가능성을 특징으로 하는 / 혁명적인 패러다임 전환을 수반하는데, / 이는 경쟁하는 이론들이 동일한 언어적 척도를 사용하여 중립적으로 대응되거나 중재될 수 없음을 의미합니다.",
                 "The subsequent resolution involves / a revolutionary paradigm shift / characterized by incommensurability, / meaning rival theories cannot be neutrally mapped / or arbitrated using identical linguistic metrics.")
            ],
            [
                ("seminal", "adj.", "중대한, 지대한 영향을 미치는", "Einstein published four seminal papers in the extraordinary year of 1905."),
                ("entrenched", "adj.", "확고히 자리 잡은, 견고한", "Entrenched bureaucratic procedures delayed the infrastructure project."),
                ("anomalous", "adj.", "변칙적인, 통상적이지 않은", "The laboratory detected an anomalous spike in background radiation."),
                ("incommensurability", "n.", "공약불가능성 (공통 척도로 비교 불가)", "The incommensurability of competing worldviews complicates objective dialogue.")
            ],
            [
                ("by contesting ~", "'~에 이의를 제기함으로써' 수단과 방법을 나타내는 전치사구입니다."),
                ("meaning that ~", "분사구문으로 앞선 개념의 부연 설명을 이끌며 '이는 ~을 의미한다'로 해석됩니다.")
            ],
            [
                ("What positivist belief did Thomas Kuhn contest?",
                 "토머스 쿤은 어떤 실증주의적 신념에 이의를 제기했는가?",
                 ["The belief that mathematics is completely useless", "The dogma of linear, cumulative scientific progress", "The idea that light travels faster than sound", "The theory that atoms contain protons and neutrons"],
                 1,
                 "첫 문장에 선형적, 누적적 과학 진보라는 실증주의적 교리에 이의를 제기했다고 명시되어 있습니다."),
                ("When does a scientific discipline enter crisis according to Kuhn?",
                 "쿤에 따르면 과학의 한 분과는 언제 위기에 봉착하는가?",
                 ["When university professors stop giving lectures", "When anomalous observations steadily accumulate that cannot fit the paradigm", "When governments double funding for physics laboratories", "When textbooks are translated into ancient Latin"],
                 1,
                 "세 번째 문장에 기존 패러다임에 수용될 수 없는 변칙적인 관찰들이 누적될 때 위기에 진입한다고 나와 있습니다."),
                ("What does 'incommensurability' mean in the context of rival paradigms?",
                 "경쟁하는 패러다임의 맥락에서 '공약불가능성'은 무엇을 의미하는가?",
                 ["Both theories have identical grammar rules.", "Rival theories cannot be neutrally mapped using identical linguistic metrics.", "All scientists agree to retire simultaneously.", "The two theories combine into an uncontroversial synthesis."],
                 1,
                 "마지막 문장에 경쟁 이론들이 동일한 언어적 척도를 써서 중립적으로 대응되거나 중재될 수 없음을 뜻한다고 설명합니다.")
            ]
        ),
        (
            "a-62",
            "Gödel's Incompleteness and Formal Axiomatics",
            "괴델의 불완전성 정리와 형식 공리계의 한계",
            "Mathematical Logic",
            "Princeton Studies in Logic & Kurt Gödel Monograph",
            "쿠르트 괴델은 산술을 포함하는 모든 모순 없는 형식 공리계 내에 참이지만 증명할 수 없는 명제가 필연적으로 존재함을 증명했습니다.",
            [
                ("In 1931, / Austrian logician Kurt Gödel shattered David Hilbert's formalist aspiration / of constructing an all-encompassing, self-contained mathematical system.",
                 "1931년, / 오스트리아의 논리학자 쿠르트 괴델은 모든 것을 포괄하며 자족적인 수학 체계를 구축하려던 / 다비트 힐베르트의 형식주의적 열망을 무너뜨렸습니다.",
                 "In 1931, / Austrian logician Kurt Gödel / shattered David Hilbert's formalist aspiration / of constructing an all-encompassing, self-contained mathematical system."),
                ("Gödel's First Incompleteness Theorem demonstrates / that in any consistent axiomatic system rich enough to articulate basic arithmetic, / there exist statements that are fundamentally undecidable.",
                 "괴델의 제1 불완전성 정리는 / 기초 산술을 표현할 수 있을 만큼 충분히 풍부한 임의의 무모순 공리계 내에서, / 근본적으로 판정 불가능한 명제들이 존재함을 입증합니다.",
                 "Gödel's First Incompleteness Theorem demonstrates / that in any consistent axiomatic system / rich enough to articulate basic arithmetic, / there exist statements / that are fundamentally undecidable."),
                ("By ingeniously assigning unique numerical values / called Gödel numbers / to formal syntactic strings, / he devised a self-referential proposition that asserts its own unprovability.",
                 "괴델 수라 불리는 / 고유한 수치적 값들을 / 형식적 구문 문자열에 기발하게 부여함으로써, / 그는 자신의 증명 불가능성을 주장하는 자기참조적 명제를 고안해 냈습니다.",
                 "By ingeniously assigning unique numerical values called Gödel numbers / to formal syntactic strings, / he devised a self-referential proposition / that asserts its own unprovability."),
                ("Consequently, / mathematical truth irrevocably transcends the boundary of formal provability, / proving that absolute consistency cannot be demonstrated entirely from within the system itself.",
                 "결과적으로, / 수학적 진리는 형식적 증명 가능성의 경계를 돌이킬 수 없이 초월하며, / 절대적 무모순성이 체계 내부로부터 온전히 증명될 수 없음을 밝혀냈습니다.",
                 "Consequently, / mathematical truth irrevocably transcends the boundary / of formal provability, / proving that absolute consistency / cannot be demonstrated entirely / from within the system itself.")
            ],
            [
                ("all-encompassing", "adj.", "모든 것을 아우르는, 총망라한", "The encyclopedia provides an all-encompassing overview of world religions."),
                ("axiomatic", "adj.", "공리적인, 자명한", "Axiomatic set theory serves as the structural foundation of modern mathematics."),
                ("self-referential", "adj.", "자기참조적인", "A sentence that states 'this sentence is false' is inherently self-referential."),
                ("irrevocably", "adv.", "돌이킬 수 없이, 확정적으로", "The treaty irrevocably redrew the political boundaries of Central Europe.")
            ],
            [
                ("rich enough to articulate ~", "'~를 표현할 수 있을 만큼 충분히 풍부한' 형용사 + enough + to부정사 구조입니다."),
                (", proving that ~", "결과를 나타내는 분사구문으로 '그리하여 ~을 증명한다'로 해석됩니다.")
            ],
            [
                ("Whose formalist mathematical aspiration did Gödel shatter?",
                 "괴델은 누구의 형식주의 수학적 열망을 무너뜨렸는가?",
                 ["Isaac Newton's", "David Hilbert's", "René Descartes'", "Charles Darwin's"],
                 1,
                 "첫 문장에 다비트 힐베르트의 형식주의적 열망을 무너뜨렸다고 명시되어 있습니다."),
                ("What does Gödel's First Incompleteness Theorem state about consistent arithmetic systems?",
                 "괴델의 제1 불완전성 정리는 무모순의 산술 체계에 대해 무엇을 명시하는가?",
                 ["Every statement can be verified mechanically within five seconds.", "There exist statements that are fundamentally undecidable.", "Arithmetic consists entirely of optical illusions.", "Prime numbers cannot be divided into odd components."],
                 1,
                 "두 번째 문장에 근본적으로 판정 불가능한 명제들이 존재한다는 것을 증명한다고 나와 있습니다."),
                ("What did Gödel's self-referential proposition assert?",
                 "괴델의 자기참조적 명제는 무엇을 주장했는가?",
                 ["Its own unprovability", "The financial cost of German universities", "The speed of subatomic light waves", "The exact weight of mathematical textbooks"],
                 0,
                 "세 번째 문장에 'asserts its own unprovability'라고 명확히 진술되어 있습니다.")
            ]
        ),
        (
            "a-63",
            "Ostrom's Common-Pool Resources and Polycentric Governance",
            "엘리너 오스트롬의 공유자원론과 다중심 거버넌스",
            "Institutional Economics",
            "American Economic Review & Elinor Ostrom Nobel Memorial Lecture",
            "엘리너 오스트롬은 공유자원이 필연적으로 고갈된다는 통념을 깨고, 공동체의 자치적 제도와 다중심 규범을 통해 지속가능한 관리가 가능함을 입증했습니다.",
            [
                ("Garrett Hardin's influential thesis on the 'Tragedy of the Commons' / asserted that shared finite resources / are inexorably doomed to catastrophic depletion / under unrestrained individual self-interest.",
                 "개릿 하딘의 영향력 있는 '공유지의 비극' 논문은 / 공유된 유한 자원이 / 무제한적인 개인의 이기심 하에서 / 파국적인 고갈로 불가피하게 치달을 수밖에 없다고 주장했습니다.",
                 "Garrett Hardin's influential thesis on the 'Tragedy of the Commons' / asserted that shared finite resources / are inexorably doomed to catastrophic depletion / under unrestrained individual self-interest."),
                ("Conventional public policy consequently prescribed / an uncompromising dichotomy: / either stringent state coercive regulation / or complete privatization.",
                 "그에 따라 전통적인 공공 정책은 타협 없는 이분법, / 즉 엄격한 국가의 강제적 규제이거나 / 완전한 사유화 둘 중 하나만을 처방했습니다.",
                 "Conventional public policy consequently prescribed / an uncompromising dichotomy: / either stringent state coercive regulation / or complete privatization."),
                ("However, / Nobel laureate Elinor Ostrom dismantled this binary paradigm / through exhaustive empirical field investigations across global irrigation systems, fisheries, and pastoral forests.",
                 "그러나, / 노벨 경제학상 수상자 엘리너 오스트롬은 전 세계 관개 시설, 어장, 방목 삼림에 걸친 철저한 실증 현장 조사를 통해 / 이러한 이분법적 패러다임을 해체했습니다.",
                 "However, / Nobel laureate Elinor Ostrom / dismantled this binary paradigm / through exhaustive empirical field investigations / across global irrigation systems, fisheries, and pastoral forests."),
                ("Ostrom proved that local communities frequently cultivate polycentric governance— / devising nuanced customary rules, / mutual graduated sanctions, / and low-cost dispute resolution / that preserve ecological commons sustainably across generations.",
                 "오스트롬은 지역 공동체들이 미묘한 관습적 규칙, / 상호 점진적 제재, / 저비용 분쟁 해결을 고안하는 다중심 거버넌스를 자주 발전시켜 / 세대에 걸쳐 생태적 공유자원을 지속가능하게 보전함을 입증했습니다.",
                 "Ostrom proved / that local communities frequently cultivate polycentric governance— / devising nuanced customary rules, / mutual graduated sanctions, / and low-cost dispute resolution / that preserve ecological commons sustainably across generations.")
            ],
            [
                ("inexorably", "adv.", "가차 없이, 거침없이", "Technological disruption inexorably transformed legacy retail industries."),
                ("dichotomy", "n.", "이분법, 양분", "Philosophers debated the strict dichotomy between mind and physical matter."),
                ("exhaustive", "adj.", "철저한, 완전한", "The commission conducted an exhaustive audit of all corporate transactions."),
                ("polycentric", "adj.", "다중심적인, 여러 주체가 공존하는", "Polycentric governance allows overlapping authorities to collaborate effectively.")
            ],
            [
                ("are doomed to + 명사", "'~하도록 운명지어지다, 피할 수 없다'는 수동 표현입니다."),
                ("either A or B", "'A 또는 B 둘 중 하나'를 명시하는 상관접속사입니다.")
            ],
            [
                ("What did Garrett Hardin's 'Tragedy of the Commons' thesis assert?",
                 "개릿 하딘의 '공유지의 비극' 논문은 무엇을 주장했는가?",
                 ["Shared resources will be inexorably doomed to catastrophic depletion.", "All farmers will voluntarily give away their private land.", "Ocean water will expand infinitely without fish.", "Gold coins will lose their economic value in villages."],
                 0,
                 "첫 문장에 공유된 유한 자원이 파국적인 고갈로 치달을 수밖에 없다고 주장했다고 나와 있습니다."),
                ("What dichotomy did conventional public policy prescribe before Ostrom's research?",
                 "오스트롬의 연구 이전 전통 공공 정책이 처방했던 이분법은 무엇이었는가?",
                 ["Either printing money or returning to the barter system", "Either stringent state coercive regulation or complete privatization", "Either building wooden dams or draining all rivers dry", "Either banning fishing entirely or exporting all timber abroad"],
                 1,
                 "두 번째 문장에 'either stringent state coercive regulation or complete privatization'이라고 나와 있습니다."),
                ("What did Elinor Ostrom prove through her empirical investigations?",
                 "엘리너 오스트롬은 실증 조사를 통해 무엇을 입증했는가?",
                 ["That local communities can cultivate polycentric governance to manage commons sustainably.", "That all communal forests must be burned to fertilize soil.", "That private corporations always manage water systems best.", "That human beings are biologically incapable of cooperating."],
                 0,
                 "마지막 문장에 지역 공동체들이 다중심 거버넌스를 통해 공유자원을 지속가능하게 보전할 수 있음을 입증했다고 설명합니다.")
            ]
        ),
        (
            "a-64",
            "Chalmers and the Hard Problem of Consciousness",
            "데이비드 차머스와 의식의 '어려운 문제'",
            "Philosophy of Mind",
            "Mind and Language & David Chalmers 'The Conscious Mind'",
            "철학자 데이비드 차머스는 뇌의 물리적·기능적 정보 처리를 설명하는 것과 주관적 질감(퀼리아)의 발생을 설명하는 것 사이의 근본적 간극을 규명했습니다.",
            [
                ("In contemporary philosophy of mind, / David Chalmers famously bifurcated consciousness studies / into the 'easy problems' and the 'hard problem.'",
                 "현대 심리철학에서, / 데이비드 차머스는 의식 연구를 / '쉬운 문제들'과 '어려운 문제'로 양분한 것으로 유명합니다.",
                 "In contemporary philosophy of mind, / David Chalmers famously bifurcated consciousness studies / into the 'easy problems' / and the 'hard problem.'"),
                ("The easy problems concern objective neurobiological functions— / such as sensory discrimination, / cognitive focus, / and linguistic verbalization— / which are amenable to standard computational and physicalist models.",
                 "쉬운 문제들은 감각 식별, / 인지적 집중, / 언어적 언어화와 같은 객관적인 신경생물학적 기능들에 관한 것으로, / 이는 표준적인 계산주의 및 물리주의 모델로 해결될 수 있습니다.",
                 "The easy problems concern objective neurobiological functions— / such as sensory discrimination, / cognitive focus, / and linguistic verbalization— / which are amenable to standard computational and physicalist models."),
                ("In sharp contradistinction, / the hard problem asks why any physical computational processing / should be accompanied by subjective, experiential qualia at all.",
                 "이와 극명한 대조적으로, / 어려운 문제는 왜 어떠한 물리적 계산 처리가 / 주관적이고 경험적인 '퀼리아(질감)'를 애초에 동반해야만 하는지를 묻습니다.",
                 "In sharp contradistinction, / the hard problem asks / why any physical computational processing / should be accompanied / by subjective, experiential qualia at all."),
                ("Even if neuroscience meticulously maps every synaptic pathway and neural correlate, / an unbridged explanatory gap persists / between mechanistic neural firing and the inner feeling of what it is like to see crimson red.",
                 "설령 신경과학이 모든 시냅스 경로와 신경 상관관계를 꼼꼼히 규명한다 할지라도, / 기계론적인 뉴런 발화와 진홍빛을 본다는 것이 어떤 느낌인가에 대한 내적 감각 사이에는 / 메워지지 않는 설명적 간극이 지속됩니다.",
                 "Even if neuroscience meticulously maps every synaptic pathway and neural correlate, / an unbridged explanatory gap persists / between mechanistic neural firing / and the inner feeling of what it is like to see crimson red.")
            ],
            [
                ("bifurcate", "v.", "둘로 나누다, 분기하다", "The trail bifurcated into two distinct paths through the forest."),
                ("amenable", "adj.", "기꺼이 따르는, (설명·처리에) 다루기 쉬운", "Data that fits linear regressions is amenable to standard statistical software."),
                ("qualia", "n. (pl.)", "퀼리아 (주관적 경험의 고유한 감각적 질감)", "The rich subjective qualia of tasting dark chocolate defies pure objective equations."),
                ("meticulously", "adv.", "꼼꼼하게, 극히 세밀하게", "The conservator meticulously restored the damaged Renaissance portrait.")
            ],
            [
                ("which are amenable to ~", "'~로 다루어지기 쉬운, 순응하는' 관계대명사 비제한적 용법입니다."),
                ("what it is like to ~", "'~하는 것이 어떤 기분/느낌인가' 주관적 경험을 묻는 관용적 구문입니다.")
            ],
            [
                ("According to Chalmers, what do the 'easy problems' of consciousness concern?",
                 "차머스에 따르면 의식의 '쉬운 문제들'은 무엇에 관한 것인가?",
                 ["Predicting the future of human politics", "Objective neurobiological functions like sensory discrimination and cognitive focus", "The supernatural physics of ghost apparitions", "Creating artificial gold from molten iron"],
                 1,
                 "두 번째 문장에 감각 식별, 인지 집중과 같은 객관적 신경생물학적 기능들에 관한 것이라고 나와 있습니다."),
                ("What central question defines the 'hard problem' of consciousness?",
                 "어떤 핵심 질문이 의식의 '어려운 문제'를 규정하는가?",
                 ["Why humans have two eyes instead of three", "Why physical computation should be accompanied by subjective qualia at all", "How many calories the brain burns during rapid chess matches", "Why nerve signals travel at slower speeds than light in cables"],
                 1,
                 "세 번째 문장에 왜 물리적 계산 처리가 주관적 퀼리아를 동반해야 하는가를 묻는 것이라고 설명합니다."),
                ("What persists even if neuroscience maps every synaptic pathway?",
                 "신경과학이 모든 시냅스 경로를 지도로 만든다 해도 무엇이 지속되는가?",
                 ["An unbridged explanatory gap between neural firing and subjective feeling", "A total breakdown of computer operating systems worldwide", "A complete cessation of oxygen supply to the neocortex", "An immediate loss of all conscious thoughts in humans"],
                 0,
                 "마지막 문장에 뉴런 발화와 내적 감각 사이의 메워지지 않는 설명적 간극(explanatory gap)이 지속된다고 명시되어 있습니다.")
            ]
        ),
        (
            "a-65",
            "Waddington's Epigenetic Landscape and Cellular Plasticity",
            "와딩턴의 후성유전학적 지형과 세포 가소성",
            "Epigenetics & Developmental Biology",
            "Nature Reviews Genetics & Conrad Waddington Classical Model",
            "콘래드 와딩턴의 후성유전학적 지형 모형은 유전형의 변화 없이도 염색질 리모델링과 DNA 메틸화를 통해 세포의 다양한 운명과 가소성이 결정됨을 시각화합니다.",
            [
                ("In 1957, / developmental biologist Conrad Waddington proposed the 'epigenetic landscape' / as an intuitive conceptual metaphor / for embryonic cellular differentiation.",
                 "1957년, / 발생생물학자 콘래드 와딩턴은 배아 세포의 분화를 설명하는 / 직관적인 개념적 은유로서 / '후성유전학적 지형'을 제안했습니다.",
                 "In 1957, / developmental biologist Conrad Waddington / proposed the 'epigenetic landscape' / as an intuitive conceptual metaphor / for embryonic cellular differentiation."),
                ("In his topographical visualization, / an undifferentiated cell is envisioned as a marble rolling down an undulating slope / scored with bifurcating valleys.",
                 "그의 지형학적 시각화에서, / 미분화 세포는 갈라지는 골짜기들이 패여 있는 / 기복이 심한 경사면을 굴러 내려가는 구슬로 묘사됩니다.",
                 "In his topographical visualization, / an undifferentiated cell is envisioned / as a marble rolling down an undulating slope / scored with bifurcating valleys."),
                ("As the cell descends along specific crevasses, / epigenetic modifications / such as DNA methylation and histone acetylation / progressively restrict its developmental potency.",
                 "세포가 특정 협곡을 따라 내려감에 따라, / DNA 메틸화나 히스톤 아세틸화와 같은 / 후성유전학적 변형이 / 점진적으로 그 발생적 다분화능을 제한합니다.",
                 "As the cell descends along specific crevasses, / epigenetic modifications / such as DNA methylation and histone acetylation / progressively restrict its developmental potency."),
                ("While classic dogma held that lineage commitment was strictly irreversible, / modern nuclear reprogramming demonstrated / that mature somatic cells can be coaxed back up the hill / into pluripotent states.",
                 "과거의 고전적 교리는 세포 계통 결정이 엄격하게 비가역적이라고 간주했으나, / 현대의 핵 재프로그래밍 연구는 / 성숙한 체세포가 언덕 위로 다시 유도되어 / 다능성 상태로 되돌아갈 수 있음을 입증했습니다.",
                 "While classic dogma held / that lineage commitment was strictly irreversible, / modern nuclear reprogramming demonstrated / that mature somatic cells can be coaxed back up the hill / into pluripotent states.")
            ],
            [
                ("undulating", "adj.", "기복이 있는, 물결치는", "Rolling hills formed an undulating landscape stretching to the horizon."),
                ("acetylation", "n.", "아세틸화 (히스톤 등에 아세틸기를 결합)", "Histone acetylation typically loosens chromatin, promoting transcription."),
                ("irreversible", "adj.", "돌이킬 수 없는, 비가역적인", "Cellular senescence was long believed to be an irreversible biological state."),
                ("pluripotent", "adj.", "다능성의 (여러 세포로 분화 가능한)", "Induced pluripotent stem cells can differentiate into virtually any somatic lineage.")
            ],
            [
                ("is envisioned as ~", "'~로 구상되다/그려지다' 수동 표현입니다."),
                ("While + 절, 주절", "'~인 반면에' 대조적 배경을 제시하는 종속절 구문입니다.")
            ],
            [
                ("How did Waddington visualize an undifferentiated cell in his model?",
                 "와딩턴은 자신의 모델에서 미분화 세포를 어떻게 시각화했는가?",
                 ["As a rocket escaping Earth's gravitational orbit", "As a marble rolling down an undulating slope with bifurcating valleys", "As an iron anchor sinking into deep ocean mud", "As a butterfly flying against turbulent gale winds"],
                 1,
                 "두 번째 문장에 갈라지는 골짜기가 있는 경사면을 굴러 내려가는 구슬로 묘사했다고 나와 있습니다."),
                ("What biological mechanisms progressively restrict cellular developmental potency?",
                 "어떤 생물학적 메커니즘이 세포의 발생 잠재력을 점진적으로 제한하는가?",
                 ["Epigenetic modifications like DNA methylation and histone acetylation", "Rapid boiling of intracellular cytoplasm", "Exposure to high-voltage electrical current", "Loss of all cell membrane lipids during sleep"],
                 0,
                 "세 번째 문장에 DNA 메틸화와 히스톤 아세틸화 같은 후성유전적 변형이 발생 잠재력을 제한한다고 명시되어 있습니다."),
                ("What did modern nuclear reprogramming demonstrate against classic dogma?",
                 "현대 핵 재프로그래밍은 고전적 교리에 반하여 무엇을 증명했는가?",
                 ["That mature somatic cells can be coaxed back into pluripotent states.", "That cells cannot survive without eating sugar continuously.", "That all genetics is an entirely arbitrary human invention.", "That chromosomes dissolve into steam during cell division."],
                 0,
                 "마지막 문장에 성숙한 체세포가 다능성 상태로 언덕 위로 다시 유도될 수 있음을 증명했다고 나와 있습니다.")
            ]
        ),
        (
            "a-66",
            "General Relativity and Gravitational Lensing",
            "일반상대성이론과 중력 렌즈 현상",
            "Astrophysics & Cosmology",
            "The Astrophysical Journal & Albert Einstein Relativistic Mechanics",
            "아인슈타인의 일반상대성이론에 따르면 거대한 질량은 시공간을 왜곡시키며, 배경 은하의 빛을 굴절시켜 우주론적 중력 렌즈를 형성합니다.",
            [
                ("Albert Einstein's general theory of relativity fundamentally redefined gravitation / not as a conventional Newtonian force, / but as the geometrical curvature of four-dimensional spacetime.",
                 "알베르트 아인슈타인의 일반상대성이론은 중력을 / 종래의 뉴턴식 인력이 아니라, / 4차원 시공간의 기하학적 곡률로 근본적으로 재정의했습니다.",
                 "Albert Einstein's general theory of relativity / fundamentally redefined gravitation / not as a conventional Newtonian force, / but as the geometrical curvature / of four-dimensional spacetime."),
                ("Massive celestial bodies / such as galactic clusters / warp the surrounding spacetime fabric, / causing trajectories of photons to bend along curved geodesics.",
                 "은하단과 같은 거대한 천체들은 / 주변 시공간 구조를 왜곡시켜, / 광자의 궤적이 휘어진 측지선을 따라 굴절되도록 만듭니다.",
                 "Massive celestial bodies / such as galactic clusters / warp the surrounding spacetime fabric, / causing trajectories of photons / to bend along curved geodesics."),
                ("This phenomenon, / known as gravitational lensing, / acts as a cosmic magnifying glass / that splits, distorts, and magnifies the light emitted by distant background galaxies.",
                 "중력 렌즈로 알려진 이 현상은 / 먼 배경 은하들에서 방출된 빛을 쪼개고 왜곡하며 확대하는 / 우주적 돋보기 역할을 수행합니다.",
                 "This phenomenon, / known as gravitational lensing, / acts as a cosmic magnifying glass / that splits, distorts, and magnifies the light / emitted by distant background galaxies."),
                ("By analyzing the subtle shear and magnification patterns in these distorted images, / astrophysicists can map the spatial distribution / of otherwise invisible dark matter structures.",
                 "이 왜곡된 이미지들에 나타난 미세한 전단 및 확대 패턴을 분석함으로써, / 천체물리학자들은 그렇지 않으면 보이지 않는 암흑 물질 구조의 / 공간적 분포를 지도로 작성할 수 있습니다.",
                 "By analyzing the subtle shear and magnification patterns / in these distorted images, / astrophysicists can map the spatial distribution / of otherwise invisible dark matter structures.")
            ],
            [
                ("curvature", "n.", "곡률, 굽음", "The earth's curvature is clearly noticeable from high-altitude aircraft."),
                ("geodesic", "n./adj.", "측지선 (곡면 상의 최단 경로)", "Light rays in curved spacetime travel along null geodesics."),
                ("distort", "v.", "왜곡하다, 비틀다", "Atmospheric turbulence distorts telescope images of distant stars."),
                ("shear", "n.", "전단 (어긋남 변형)", "Cosmic shear analysis measures the subtle gravitational distortions in galaxy shapes.")
            ],
            [
                ("not as A, but as B", "'A로서가 아니라 B로서' 전치사구 대조 표현입니다."),
                ("causing A to B", "'A가 B하도록 야기하다' 인과 관계를 나타내는 5형식 사역류 구문입니다.")
            ],
            [
                ("How does General Relativity reframe gravitation?",
                 "일반상대성이론은 중력을 어떻게 재구성하는가?",
                 ["As an acoustic sound wave bouncing across the solar system", "As the geometrical curvature of four-dimensional spacetime", "As an invisible mechanical rope pulling planets together", "As a sudden chemical explosion of nuclear hydrogen"],
                 1,
                 "첫 문장에 4차원 시공간의 기하학적 곡률로 재정의했다고 나와 있습니다."),
                ("What does gravitational lensing act as in the cosmos?",
                 "중력 렌즈 현상은 우주에서 무엇으로 작용하는가?",
                 ["A barrier that absorbs all background light forever", "A cosmic magnifying glass that splits and magnifies distant galaxy light", "A giant black hole that swallows entire superclusters", "A mirror that reflects radio waves backwards into the Earth"],
                 1,
                 "세 번째 문장에 먼 배경 은하의 빛을 확대하고 왜곡하는 '우주적 돋보기(cosmic magnifying glass)' 역할을 한다고 나와 있습니다."),
                ("What can astrophysicists map by analyzing distorted lens images?",
                 "천체물리학자들은 왜곡된 렌즈 이미지를 분석하여 무엇을 지도로 그릴 수 있는가?",
                 ["The exact surface temperature of planetary core iron", "The spatial distribution of otherwise invisible dark matter structures", "The chemical formula of interstellar ice crystals", "The future trajectory of wandering comets in nearby orbits"],
                 1,
                 "마지막 문장에 보이지 않는 암흑 물질 구조의 공간적 분포를 매핑할 수 있다고 명시되어 있습니다.")
            ]
        ),
        (
            "a-67",
            "The Nash Equilibrium in Non-Cooperative Game Theory",
            "비협조적 게임 이론의 내시 균형과 전략적 안정성",
            "Game Theory & Applied Mathematics",
            "Econometrica & John Nash 'Non-Cooperative Games'",
            "존 내시가 정립한 내시 균형은 상대방의 전략이 주어졌을 때 어느 누구도 자신의 전략을 일방적으로 변경할 유인이 없는 안정적 균형 상태를 의미합니다.",
            [
                ("In 1950, / mathematician John Nash established a revolutionary equilibrium concept / for non-cooperative game theory.",
                 "1950년, / 수학자 존 내시는 비협조적 게임 이론에 있어 / 혁명적인 균형 개념을 확립했습니다.",
                 "In 1950, / mathematician John Nash established / a revolutionary equilibrium concept / for non-cooperative game theory."),
                ("A Nash equilibrium describes a strategic profile / wherein no individual player possesses an incentive / to unilaterally deviate from their chosen strategy.",
                 "내시 균형은 어느 개별 경기자도 자신이 선택한 전략으로부터 / 일방적으로 이탈할 유인을 갖지 않는 / 전략적 구성을 의미합니다.",
                 "A Nash equilibrium describes a strategic profile / wherein no individual player possesses an incentive / to unilaterally deviate from their chosen strategy."),
                ("Utilizing Kakutani's fixed point theorem, / Nash rigorously proved that every finite game / with any number of players and pure strategies / possesses at least one equilibrium in mixed strategies.",
                 "가쿠타니의 부동점 정리를 활용하여, / 내시는 임의의 경기자 수와 순수 전략을 갖는 / 모든 유한 게임이 / 혼합 전략 하에서 최소한 하나의 균형을 필연적으로 보유함을 엄밀하게 증명했습니다.",
                 "Utilizing Kakutani's fixed point theorem, / Nash rigorously proved / that every finite game / with any number of players and pure strategies / possesses at least one equilibrium in mixed strategies."),
                ("Crucially, / a Nash equilibrium does not imply collective social optimality, / as vividly illustrated by the classic Prisoner's Dilemma / where rational self-interested choices yield suboptimal Pareto outcomes.",
                 "결정적으로, / 내시 균형이 집단적 사회적 최적성을 의미하지는 않는데, / 이는 합리적이고 자기 이익적인 선택이 파레토 열등한 결과를 초래하는 / 고전적인 '죄수의 딜레마'에서 생생히 입증됩니다.",
                 "Crucially, / a Nash equilibrium does not imply collective social optimality, / as vividly illustrated by the classic Prisoner's Dilemma / where rational self-interested choices / yield suboptimal Pareto outcomes.")
            ],
            [
                ("equilibrium", "n.", "균형, 평형 상태", "Supply and demand intersect to determine market price equilibrium."),
                ("unilaterally", "adv.", "일방적으로, 단독으로", "The company cannot unilaterally modify the signed employment contract."),
                ("deviate", "v.", "이탈하다, 벗어나다", "Pilots must never deviate from their assigned flight corridors."),
                ("suboptimal", "adj.", "차선의, 최선에 못 미치는", "Incomplete market information often results in suboptimal investments.")
            ],
            [
                ("wherein + 완전한 절", "'그 안에서 ~하는' 관계부사 wherein 절입니다."),
                ("does not imply A, as illustrated by B", "'B에서 예시되듯 A를 함축하지는 않는다' 양보성 논평 구문입니다.")
            ],
            [
                ("What characterizes a strategic profile at a Nash equilibrium?",
                 "내시 균형에서의 전략적 구성의 특징은 무엇인가?",
                 ["Every player earns infinite financial dividends.", "No individual player has an incentive to unilaterally deviate from their strategy.", "All players resign from the game simultaneously.", "One single player dictates all rules to others."],
                 1,
                 "두 번째 문장에 어떤 개별 경기자도 자신의 전략에서 일방적으로 이탈할 유인이 없다고 설명합니다."),
                ("What mathematical theorem did Nash use to prove the existence of an equilibrium?",
                 "내시는 균형의 존재성을 증명하기 위해 어떤 수학 정리를 사용했는가?",
                 ["Pythagorean theorem", "Kakutani's fixed point theorem", "Fermat's Last Theorem", "Euclid's division lemma"],
                 1,
                 "세 번째 문장에 가쿠타니의 부동점 정리(Kakutani's fixed point theorem)를 활용했다고 나와 있습니다."),
                ("Does a Nash equilibrium guarantee collective social optimality?",
                 "내시 균형은 집단적 사회적 최적성을 보장하는가?",
                 ["Yes, it always creates the highest possible social happiness.", "No, as shown in the Prisoner's Dilemma where rational choices yield suboptimal outcomes.", "Only when playing with exactly two players.", "Only when all financial rewards are paid in physical cash."],
                 1,
                 "마지막 문장에 집단적 최적성을 뜻하지 않으며 죄수의 딜레마처럼 열등한 결과를 초래할 수 있다고 명시되어 있습니다.")
            ]
        ),
        (
            "a-68",
            "The Thermodynamic Arrow of Time and Statistical Entropy",
            "열역학적 시간의 화살과 통계적 엔트로피",
            "Statistical Mechanics & Cosmology",
            "Physical Review & Ludwig Boltzmann Statistical Physics",
            "열역학 제2법칙에 따른 엔트로피 증가는 시간의 비가역적 방향성을 규정하며, 이는 우주 초기의 극도로 낮은 엔트로피 상태라는 우주론적 경계 조건에 뿌리를 두고 있습니다.",
            [
                ("While the fundamental microscopic equations of classical mechanics and quantum theory / exhibit complete time-reversal symmetry, / macroscopic physical reality displays a relentless forward temporal arrow.",
                 "고전역학과 양자 이론의 근본적인 미시 방정식들은 / 완전한 시간 대칭성을 나타내지만, / 거시적인 물리적 실재는 가차 없는 전방향적 시간의 화살을 드러냅니다.",
                 "While the fundamental microscopic equations / of classical mechanics and quantum theory / exhibit complete time-reversal symmetry, / macroscopic physical reality displays / a relentless forward temporal arrow."),
                ("Ludwig Boltzmann reconciled this apparent paradox / by redefining entropy as a statistical measure / of the multiplicity of microscopic arrangements compatible with a given macroscopic state.",
                 "루트비히 볼츠만은 엔트로피를 주어진 거시 상태와 부합하는 / 미시적 배열들의 다양성에 대한 통계적 척도로 재정의함으로써 / 이 외견상의 역설을 조화시켰습니다.",
                 "Ludwig Boltzmann reconciled this apparent paradox / by redefining entropy as a statistical measure / of the multiplicity of microscopic arrangements / compatible with a given macroscopic state."),
                ("Because disordered macrostates correspond to overwhelmingly vastly more microstates than ordered configurations, / an isolated thermodynamic system spontaneously evolves toward maximum statistical probability.",
                 "무질서한 거시 상태는 질서 있는 배치보다 압도적으로 훨씬 더 많은 미시 상태들에 대응하기 때문에, / 고립된 열역학계는 자발적으로 최대 통계적 확률을 향해 진화합니다.",
                 "Because disordered macrostates correspond / to overwhelmingly vastly more microstates than ordered configurations, / an isolated thermodynamic system spontaneously evolves / toward maximum statistical probability."),
                ("Consequently, / the inexorable increase of entropy / stems from the special cosmological initial condition / of our universe beginning in a state of remarkably low gravitational entropy.",
                 "결과적으로, / 엔트로피의 불가피한 증가는 / 우리 우주가 현저히 낮은 중력 엔트로피 상태에서 시작되었다는 / 특별한 우주론적 초기 조건에 기인합니다.",
                 "Consequently, / the inexorable increase of entropy / stems from the special cosmological initial condition / of our universe beginning / in a state of remarkably low gravitational entropy.")
            ],
            [
                ("time-reversal", "adj.", "시간 역전의", "Time-reversal symmetry implies physical laws look identical forwards and backwards."),
                ("reconcile", "v.", "조화시키다, 화해시키다", "The theoretical physicist sought to reconcile gravity with quantum electrodynamics."),
                ("multiplicity", "n.", "다양성, 다수", "A multiplicity of pathways regulates mammalian cellular apoptosis."),
                ("inexorable", "adj.", "거침없는, 멈출 수 없는", "The inexorable march of technological progress reshapes human labor markets.")
            ],
            [
                ("While + 절, 주절", "'~인 반면에' 대조를 나타내는 부사절입니다."),
                ("stems from + 명사", "'~로부터 유래하다, 기인하다' 인과 관계를 나타내는 핵심 숙어입니다.")
            ],
            [
                ("What do fundamental microscopic equations of physics exhibit regarding time?",
                 "물리학의 근본 미시 방정식들은 시간에 관해 무엇을 나타내는가?",
                 ["Complete time-reversal symmetry", "An absolute requirement that time run backwards only", "Total destruction of time during chemical reactions", "Complete dependence on observer emotional moods"],
                 0,
                 "첫 문장에 근본 미시 방정식들이 완전한 시간 역전 대칭성을 나타낸다고 설명합니다."),
                ("How did Ludwig Boltzmann redefine entropy in statistical physics?",
                 "루트비히 볼츠만은 통계물리학에서 엔트로피를 어떻게 재정의했는가?",
                 ["As the monetary cost of burning fossil coal", "As a statistical measure of the multiplicity of microscopic arrangements", "As the literal speed of sound passing through solid copper", "As the chemical volume of pure atmospheric steam"],
                 1,
                 "두 번째 문장에 거시 상태와 부합하는 미시적 배열 다양성의 통계적 척도로 재정의했다고 나와 있습니다."),
                ("Where does the inexorable increase of entropy fundamentally stem from?",
                 "엔트로피의 불가피한 증가는 근본적으로 어디에서 기인하는가?",
                 ["From solar wind pushing planets out of orbit", "From the special cosmological initial condition of remarkably low initial entropy", "From scientists inventing complex mathematical formulas", "From ocean waves eroding rocky coastlines"],
                 1,
                 "마지막 문장에 우주가 현저히 낮은 엔트로피 상태에서 시작되었다는 특별한 우주론적 초기 조건에 기인한다고 명시되어 있습니다.")
            ]
        ),
        (
            "a-69",
            "Saussurean Structuralism and the Linguistic Sign",
            "소쉬르의 구조주의와 언어 기호의 자의성",
            "Linguistics & Semiotics",
            "Routledge Linguistics & Ferdinand de Saussure 'Course in General Linguistics'",
            "페르디낭 드 소쉬르는 언어가 기표와 기의로 이루어진 자의적 기호 체계이며, 개별 단어의 의미는 체계 내 다른 요소들과의 차이에 의해 규정된다고 보았습니다.",
            [
                ("Ferdinand de Saussure fundamentally revolutionized modern linguistics / by conceiving language not as an organic nomenclature of pre-existing objects, / but as a self-contained differential system of semiotic signs.",
                 "페르디낭 드 소쉬르는 언어를 이미 존재하는 사물들에 이름을 붙이는 유기적 명명 체계가 아니라, / 기호학적 기호들의 자족적인 차이 체계로 파악함으로써 / 현대 언어학을 근본적으로 혁신했습니다.",
                 "Ferdinand de Saussure fundamentally revolutionized modern linguistics / by conceiving language / not as an organic nomenclature of pre-existing objects, / but as a self-contained differential system / of semiotic signs."),
                ("Saussure decomposed the linguistic sign into two indivisible components: / the 'signifier' (the acoustic sound-image) / and the 'signified' (the mental concept).",
                 "소쉬르는 언어 기호를 나눌 수 없는 두 구성 요소, / 즉 '기표'(청각적 음성 영상)와 / '기의'(심상적 개념)로 분해했습니다.",
                 "Saussure decomposed the linguistic sign / into two indivisible components: / the 'signifier' (the acoustic sound-image) / and the 'signified' (the mental concept)."),
                ("Central to his structuralist paradigm / is the principle of the arbitrariness of the sign, / affirming that no natural, intrinsic link connects the phoneme sequence 'tree' to the botanical entity itself.",
                 "그의 구조주의적 패러다임의 핵심은 / 기호의 자의성 원리이며, / 이는 '나무'라는 음소 연쇄와 식물학적 실체 자체를 연결하는 어떤 자연적이고 본질적인 연결고리도 없음을 단언합니다.",
                 "Central to his structuralist paradigm / is the principle of the arbitrariness of the sign, / affirming that no natural, intrinsic link connects / the phoneme sequence 'tree' to the botanical entity itself."),
                ("Meaning emerges purely negatively through relational contrast— / a word signifies what it does / not through any inherent essence, / but precisely because it differs from every other sign in the linguistic matrix.",
                 "의미는 순수하게 관계적 대조를 통해 부정적으로 발현되는데, / 단어는 어떤 내재적 본질을 통해서가 아니라, / 언어적 모체 내의 다른 모든 기호와 구별된다는 바로 그 이유 때문에 / 자신의 의미를 지니게 됩니다.",
                 "Meaning emerges purely negatively through relational contrast— / a word signifies what it does / not through any inherent essence, / but precisely because it differs / from every other sign in the linguistic matrix.")
            ],
            [
                ("nomenclature", "n.", "명명법, 명칭 체계", "Chemical nomenclature provides standardized IUPAC names for organic compounds."),
                ("semiotic", "adj.", "기호학의, 기호의", "Semiotic analysis decodes the hidden cultural connotations of advertisements."),
                ("arbitrariness", "n.", "자의성, 임의성", "The arbitrariness of linguistic signs allows diverse languages to assign different words to identical concepts."),
                ("phoneme", "n.", "음소 (의미 구별의 최소 음성 단위)", "The difference between 'bat' and 'pat' rests upon a single initial phoneme.")
            ],
            [
                ("not as A, but as B", "'A로서가 아니라 B로서' 전치사구 대조 표현입니다."),
                ("Central to A is B", "보어 도치 구문으로 'A의 핵심에는 B가 있다'를 의미합니다.")
            ],
            [
                ("What two components did Saussure divide the linguistic sign into?",
                 "소쉬르는 언어 기호를 어떤 두 구성 요소로 분해했는가?",
                 ["The vowel and the consonant", "The signifier (sound-image) and the signified (mental concept)", "The noun and the punctuation mark", "The ink drop and the printed parchment"],
                 1,
                 "두 번째 문장에 기표(음성 영상)와 기의(정신적 개념)로 나누었다고 설명합니다."),
                ("What does the principle of the arbitrariness of the sign affirm?",
                 "기호의 자의성 원리는 무엇을 단언하는가?",
                 ["Words are physically glued to external objects in soil.", "No natural, intrinsic link connects sound sequences to objects.", "All human languages must originate from one identical mountain tribe.", "Language can only be spoken through mechanical flutes."],
                 1,
                 "세 번째 문장에 음소 연쇄와 실체 자체를 연결하는 어떤 자연적, 본질적 연결고리도 없다는 것을 뜻한다고 나와 있습니다."),
                ("How does semantic meaning emerge in Saussure's structuralist view?",
                 "소쉬르의 구조주의적 관점에서 의미는 어떻게 발현되는가?",
                 ["Through magnetic resonance in vocal chords", "Purely negatively through relational contrast with other signs", "By decree of royal grammar academies", "From the spiritual essence of ancient Egyptian hieroglyphs"],
                 1,
                 "마지막 문장에 언어 체계 내의 다른 모든 기호와의 관계적 대조를 통해 발현된다고 설명합니다.")
            ]
        ),
        (
            "a-70",
            "The Diamond-Mortensen-Pissarides Search-and-Matching Model",
            "DMP 탐색-매칭 노동 시장 이론과 마찰적 실업",
            "Macroeconomics & Labor Economics",
            "Nobel Memorial Prize Lecture & Econometrica Classical Foundations",
            "다이아몬드-모텐센-피사리디스 모델은 정보 비대칭과 탐색 비용으로 인해 구인난과 실업이 동시에 공존하는 마찰적 노동 시장 메커니즘을 규명했습니다.",
            [
                ("Standard neoclassical macroeconomic models historically treated the labor market / as an idealized Walrasian auction / where wages adjust instantaneously to clear supply and demand.",
                 "표준 신고전학파 거시경제 모델들은 역사적으로 노동 시장을 / 임금이 즉각적으로 조정되어 공급과 수요를 일치시키는 / 이상화된 왈라스적 경매 시장으로 취급했습니다.",
                 "Standard neoclassical macroeconomic models / historically treated the labor market / as an idealized Walrasian auction / where wages adjust instantaneously / to clear supply and demand."),
                ("However, / the Diamond-Mortensen-Pissarides (DMP) framework revolutionized labor economics / by formalizing search frictions and information asymmetries inherent in real-world hiring.",
                 "그러나, / 다이아몬드-모텐센-피사리디스(DMP) 프레임워크는 현실 채용에 내재된 탐색 마찰과 정보 비대칭을 공식화함으로써 / 노동경제학을 혁신했습니다.",
                 "However, / the Diamond-Mortensen-Pissarides (DMP) framework / revolutionized labor economics / by formalizing search frictions / and information asymmetries inherent in real-world hiring."),
                ("In the DMP model, / matching vacant jobs with job-seekers is not instantaneous, / but governed by an aggregate matching function / that requires costly search time and expenditure from both firms and workers.",
                 "DMP 모델에서, / 빈 일자리와 구직자의 매칭은 즉각적이지 않으며, / 기업과 노동자 양측 모두로부터 비용이 드는 탐색 시간과 지출을 요구하는 / 총체적 매칭 함수에 의해 지배됩니다.",
                 "In the DMP model, / matching vacant jobs with job-seekers is not instantaneous, / but governed by an aggregate matching function / that requires costly search time and expenditure / from both firms and workers."),
                ("Once a match is forged, / a bilateral economic rent is created, / and wages are determined through Nash wage bargaining / over this match-specific surplus.",
                 "일단 매칭이 성사되면, / 쌍방적 경제적 지대가 창출되며, / 임금은 이 매칭 특유의 잉여를 둘러싼 내시 임금 협상을 통해 결정됩니다.",
                 "Once a match is forged, / a bilateral economic rent is created, / and wages are determined / through Nash wage bargaining / over this match-specific surplus.")
            ],
            [
                ("friction", "n.", "마찰, 불일치", "Search frictions in the housing market prevent immediate transactions."),
                ("aggregate", "adj./n.", "총체적인, 집합적인", "Aggregate consumer spending rose sharply during the holiday quarter."),
                ("bilateral", "adj.", "쌍방의, 양자 간의", "The two neighboring countries signed a bilateral trade agreement."),
                ("surplus", "n.", "잉여, 흑자", "A consumer surplus occurs when buyers pay less than their maximum willingness to pay.")
            ],
            [
                ("governed by + 명사", "'~에 의해 지배되는, 통제되는' 수동 표현입니다."),
                ("Once a match is forged, ~", "'일단 매칭이 형성되면' 시간/조건의 부사절을 이끕니다.")
            ],
            [
                ("How did neoclassical models treat the labor market before the DMP framework?",
                 "DMP 프레임워크 이전 신고전학파 모델들은 노동 시장을 어떻게 취급했는가?",
                 ["As a chaotic casino with zero rules", "As an idealized Walrasian auction where wages adjust instantaneously", "As a barter exchange trading grain for labor", "As an illegal underground market operated by pirates"],
                 1,
                 "첫 문장에 임금이 즉각적으로 조정되어 수급을 맞추는 이상화된 왈라스적 경매 시장으로 취급했다고 나와 있습니다."),
                ("Why is matching vacant jobs with workers not instantaneous in the DMP model?",
                 "DMP 모델에서 왜 일자리와 구직자의 매칭이 즉각적이지 않은가?",
                 ["Because governments forbid companies from hiring workers", "Because it is governed by an aggregate matching function requiring search time and costs", "Because workers only communicate through postal letters once a year", "Because banks withhold all wage payments for twelve months"],
                 1,
                 "세 번째 문장에 시간과 비용이 드는 총체적 매칭 함수에 의해 지배되기 때문이라고 명시되어 있습니다."),
                ("How are wages determined once a match is created in the DMP model?",
                 "DMP 모델에서 매칭이 성사된 후 임금은 어떻게 결정되는가?",
                 ["By flipping a coin in court", "Through Nash wage bargaining over the match-specific surplus", "By fixed government decree without negotiation", "According to the height and physical weight of the applicant"],
                 1,
                 "마지막 문장에 매칭 잉여를 둘러싼 내시 임금 협상(Nash wage bargaining)을 통해 결정된다고 설명합니다.")
            ]
        )
    ]
