# -*- coding: utf-8 -*-
"""
generate_expansion_210_i.py
10 Intermediate passages (i-61 to i-70)
B1-B2 level, authoritative sources, sentence chunks, vocabulary, grammar, and 3 deducible comprehension questions per passage.
"""

def get_expansion_210_i():
    return [
        (
            "i-61",
            "Cognitive Load Theory and Instructional Design",
            "인지 부하 이론과 효과적인 학습 설계",
            "Cognitive Psychology",
            "Educational Psychology Review & John Sweller Research",
            "인지 부하 이론은 인간의 작업 기억 용량이 극히 제한적이므로, 불필요한 외재적 부하를 줄이고 도식 형성을 촉진해야 한다고 강조합니다.",
            [
                ("Cognitive Load Theory posits / that human working memory possesses an extremely limited capacity / for processing novel information.",
                 "인지 부하 이론은 인간의 작업 기억이 / 새로운 정보를 처리하는 데 있어 / 극히 제한된 용량을 지니고 있다고 상정합니다.",
                 "Cognitive Load Theory posits / that human working memory possesses / an extremely limited capacity / for processing novel information."),
                ("Working memory can hold only a handful of discrete chunks / for a few fleeting seconds / without active rehearsal.",
                 "작업 기억은 능동적인 되뇌임 없이는 / 불과 몇 초 동안 / 몇 개 안 되는 개별 정보 덩어리만을 유지할 수 있습니다.",
                 "Working memory can hold / only a handful of discrete chunks / for a few fleeting seconds / without active rehearsal."),
                ("In contrast, long-term memory acts as a vast reservoir / where automated cognitive schemas store complex knowledge indefinitely.",
                 "대조적으로, 장기 기억은 / 자동화된 인지 도식이 복잡한 지식을 무기한 저장하는 / 방대한 저장소 역할을 합니다.",
                 "In contrast, / long-term memory acts as a vast reservoir / where automated cognitive schemas / store complex knowledge indefinitely."),
                ("Effective instructional design must minimize extraneous load / caused by poor formatting / so that learners can allocate attention to meaningful schema construction.",
                 "효과적인 교수 설계는 서툰 형식으로 인한 / 불필요한 외재적 부하를 최소화해야만 하며, / 이를 통해 학습자가 의미 있는 도식 구축에 주의를 할당할 수 있도록 해야 합니다.",
                 "Effective instructional design / must minimize extraneous load / caused by poor formatting / so that learners can allocate attention / to meaningful schema construction.")
            ],
            [
                ("posit", "v.", "상정하다, 사실로 가정하다", "The hypothesis posits a link between stress and sleep disorders."),
                ("discrete", "adj.", "별개의, 분리된", "The curriculum is divided into twelve discrete thematic modules."),
                ("reservoir", "n.", "저장소, 저수지", "Libraries serve as immense cultural reservoirs of human thought."),
                ("extraneous", "adj.", "이질적인, 불필요한 외적인", "Eliminate extraneous background noise during audio recording.")
            ],
            [
                ("so that + 주어 + can 동사원형", "'~가 …할 수 있도록' 목적을 나타내는 접속사절입니다."),
                ("where automated schemas store ~", "장소를 나타내는 선행사 reservoir를 수식하는 관계부사 where 절입니다.")
            ],
            [
                ("According to Cognitive Load Theory, what limitation does working memory have?",
                 "인지 부하 이론에 따르면 작업 기억은 어떤 한계를 가지고 있는가?",
                 ["It cannot retain images of faces.", "It possesses an extremely limited capacity for processing novel information.", "It can only function during deep sleep.", "It completely resets every twenty-four hours."],
                 1,
                 "첫 문장에 'working memory possesses an extremely limited capacity for processing novel information'라고 명시되어 있습니다."),
                ("How does long-term memory differ from working memory in the passage?",
                 "본문에서 장기 기억은 작업 기억과 어떻게 다른가?",
                 ["It only stores sensory sound waves.", "It acts as a vast reservoir where automated schemas store complex knowledge indefinitely.", "It can hold only two numbers at a time.", "It decays within five seconds without repetition."],
                 1,
                 "세 번째 문장에 'acts as a vast reservoir where automated cognitive schemas store complex knowledge indefinitely'라고 나와 있습니다."),
                ("Why must instructional design minimize extraneous load?",
                 "교수 설계에서 외재적 부하를 최소화해야 하는 이유는 무엇인가?",
                 ["To allow learners to allocate attention to meaningful schema construction.", "To eliminate the need for long-term memory altogether.", "To prevent textbooks from becoming too expensive.", "To accelerate the physical printing process of tests."],
                 0,
                 "마지막 문장에 학습자가 유의미한 도식 형성에 주의를 기울일 수 있도록 하기 위함이라고 설명합니다.")
            ]
        ),
        (
            "i-62",
            "The Molecular Machinery of CRISPR-Cas9",
            "CRISPR-Cas9 유전자 편집의 분자 기전",
            "Molecular Biology",
            "Broad Institute & Nature Biotechnology Reviews",
            "CRISPR-Cas9은 박테리아의 바이러스 방어 체계에서 유래한 기술로, 합성 가이드 RNA를 이용해 특정 DNA 서열을 정밀하게 절단합니다.",
            [
                ("CRISPR-Cas9 originated as an adaptive immune mechanism / in bacteria defending against bacteriophage viral infections.",
                 "CRISPR-Cas9은 박테리오파지 바이러스 감염에 맞서 방어하던 / 박테리아의 후천성 면역 기전에서 유래했습니다.",
                 "CRISPR-Cas9 originated / as an adaptive immune mechanism / in bacteria / defending against bacteriophage viral infections."),
                ("The system utilizes a synthetic single guide RNA (sgRNA) / engineered to match a specific target sequence in the genome.",
                 "이 시스템은 게놈 내 특정 표적 서열과 일치하도록 공학적으로 설계된 / 합성 단일 가이드 RNA(sgRNA)를 활용합니다.",
                 "The system utilizes / a synthetic single guide RNA (sgRNA) / engineered to match / a specific target sequence in the genome."),
                ("Once bound to the designated DNA locus, / the Cas9 endonuclease enzyme acts like molecular scissors, / generating a double-strand break.",
                 "지정된 DNA 위치에 결합하면, / Cas9 엔도뉴클레아제 효소가 분자 가위처럼 작용하여 / 이중 가닥 절단을 일으킵니다.",
                 "Once bound to the designated DNA locus, / the Cas9 endonuclease enzyme / acts like molecular scissors, / generating a double-strand break."),
                ("The cell's innate repair pathways then mend the break, / allowing scientists to either disrupt dysfunctional genes / or insert precise corrective sequences.",
                 "그 후 세포 본래의 복구 경로가 절단면을 치유하며, / 이를 통해 과학자들은 기능 장애 유전자를 불활성화하거나 / 정밀한 교정 서열을 삽입할 수 있습니다.",
                 "The cell's innate repair pathways / then mend the break, / allowing scientists to either disrupt dysfunctional genes / or insert precise corrective sequences.")
            ],
            [
                ("adaptive", "adj.", "적응성의, 후천적인", "Adaptive immune systems remember past pathogen exposures."),
                ("endonuclease", "n.", "내포 뉴클레아제 (핵산 분해 효소)", "Endonucleases cleave internal phosphodiester bonds in DNA."),
                ("locus", "n.", "유전자 좌, 특정 위치", "The genetic mutation was mapped to a specific chromosomal locus."),
                ("dysfunctional", "adj.", "기능 장애의, 고장 난", "Dysfunctional valves caused backflow of blood into the atrium.")
            ],
            [
                ("Once bound to ~", "'일단 ~에 결합하고 나면' 조건을 나타내는 분사구문입니다."),
                ("either A or B", "'A 또는 B 둘 중 하나' 상관접속사 구문입니다.")
            ],
            [
                ("What was the original natural function of CRISPR in bacteria?",
                 "박테리아에서 CRISPR의 원래 자연적 기능은 무엇이었는가?",
                 ["Synthesizing starch for winter hibernation", "Defending against bacteriophage viral infections", "Producing sweet nectar to attract bees", "Absorbing sunlight for bacterial photosynthesis"],
                 1,
                 "첫 문장에 박테리오파지 바이러스 감염에 대항하는 방어 면역 기전으로 유래했다고 나와 있습니다."),
                ("How does the Cas9 enzyme behave when bound to the target DNA?",
                 "Cas9 효소는 표적 DNA에 결합했을 때 어떻게 작동하는가?",
                 ["It acts like molecular scissors, generating a double-strand break.", "It freezes the entire chromosome into a glass cube.", "It translates DNA directly into heavy metals.", "It dissolves all water molecules inside the cell."],
                 0,
                 "세 번째 문장에 분자 가위처럼 작용해 이중 가닥 절단을 발생시킨다고 명시되어 있습니다."),
                ("What happens during the cell's repair pathway following the break?",
                 "절단 후 세포 복구 경로 동안 무엇이 가능해지는가?",
                 ["Scientists can disrupt dysfunctional genes or insert corrective sequences.", "The entire organism is instantly cloned without errors.", "All cellular proteins are permanently deleted.", "The cell converts into an inanimate mineral crystal."],
                 0,
                 "마지막 문장에 과학자들이 고장 난 유전자를 불활성화하거나 정밀한 교정 서열을 삽입할 수 있게 된다고 설명합니다.")
            ]
        ),
        (
            "i-63",
            "Comparative Advantage and Global Trade",
            "비교우위론과 국제 무역의 경제학",
            "Economics",
            "International Monetary Fund (IMF) Economic Issues & David Ricardo",
            "데이비드 리카도의 비교우위론은 기회비용이 더 낮은 상품에 특화하여 무역할 때 모든 참여국이 경제적 후생을 누릴 수 있음을 증명합니다.",
            [
                ("The theory of comparative advantage, / formulated by economist David Ricardo in 1817, / remains the bedrock of international trade theory.",
                 "1817년 경제학자 데이비드 리카도에 의해 정립된 / 비교우위론은 / 여전히 국제 무역 이론의 확고한 기반입니다.",
                 "The theory of comparative advantage, / formulated by economist David Ricardo in 1817, / remains the bedrock / of international trade theory."),
                ("It demonstrates / that nations can achieve mutual economic gains / even if one country produces every single good more efficiently.",
                 "이 이론은 비록 한 국가가 모든 재화를 더 효율적으로 생산할지라도 / 국가들이 상호 경제적 이익을 달성할 수 있음을 / 보여줍니다.",
                 "It demonstrates / that nations can achieve mutual economic gains / even if one country produces every single good / more efficiently."),
                ("The crucial metric is not absolute productivity, / but opportunity cost—the value of the alternative goods sacrificed.",
                 "결정적인 척도는 절대적인 생산성이 아니라, / 희생된 대체 재화의 가치를 뜻하는 기회비용입니다.",
                 "The crucial metric is not absolute productivity, / but opportunity cost— / the value of the alternative goods sacrificed."),
                ("By specializing in sectors / where their relative opportunity cost is lowest / and exchanging output, / all participating economies expand their total consumption possibilities.",
                 "상대적 기회비용이 가장 낮은 부문에 특화하고 / 생산물을 교환함으로써, / 모든 참여 경제는 총 소비 가능성을 확장합니다.",
                 "By specializing in sectors / where their relative opportunity cost is lowest / and exchanging output, / all participating economies / expand their total consumption possibilities.")
            ],
            [
                ("bedrock", "n.", "기반, 근본 원리", "Trust and transparency form the bedrock of financial markets."),
                ("metric", "n.", "측정 기준, 지표", "Gross domestic product is a standard metric of economic activity."),
                ("opportunity cost", "n.", "기회비용", "Choosing college entails the opportunity cost of foregone wage earnings."),
                ("consumption", "n.", "소비", "Household consumption represents a major component of national spending.")
            ],
            [
                ("even if + 절", "'비록 ~일지라도' 양보의 부사절을 이끕니다."),
                ("not A, but B", "'A가 아니라 B' 대조를 나타내는 구문입니다.")
            ],
            [
                ("According to Ricardo's theory, can two nations benefit from trade if one is superior in producing everything?",
                 "리카도의 이론에 따르면, 한 국가가 모든 재화 생산에서 우월하더라도 두 국가가 무역을 통해 이익을 얻을 수 있는가?",
                 ["No, the weaker nation will inevitably collapse.", "Yes, nations can achieve mutual economic gains.", "Only if they share the exact same currency.", "Only during times of international warfare."],
                 1,
                 "두 번째 문장에서 한 국가가 모든 재화를 더 효율적으로 생산하더라도 상호 경제적 이익을 얻을 수 있다고 증명합니다."),
                ("What is the crucial economic metric according to the text?",
                 "본문에 따르면 결정적인 경제적 척도는 무엇인가?",
                 ["Absolute factory size", "Opportunity cost", "Geographical land mass", "Gold reserve volume"],
                 1,
                 "세 번째 문장에 'The crucial metric is not absolute productivity, but opportunity cost'라고 나와 있습니다."),
                ("How do participating economies expand their total consumption possibilities?",
                 "참여 경제들은 어떻게 그들의 총 소비 가능성을 확장하는가?",
                 ["By imposing total import embargoes on neighbors", "By specializing where relative opportunity cost is lowest and trading", "By eliminating all forms of private enterprise", "By printing unlimited fiat currency notes"],
                 1,
                 "마지막 문장에 상대적 기회비용이 가장 낮은 부문에 특화하고 교환함으로써 소비 가능성을 확장한다고 설명합니다.")
            ]
        ),
        (
            "i-64",
            "Ocean Acidification and Marine Calcifiers",
            "해양 산성화와 석회화 해양 생물의 위기",
            "Oceanography & Climate Science",
            "NOAA Pacific Marine Environmental Laboratory & IPCC Working Group",
            "인류가 배출한 이산화탄소를 바다가 과도하게 흡수하면서 해수 pH가 떨어져 산호와 조개류의 껍데기 형성이 심각하게 저해되고 있습니다.",
            [
                ("The world's oceans have absorbed approximately thirty percent / of anthropogenic carbon dioxide emissions / produced since the industrial era.",
                 "전 세계 대양은 산업화 시대 이후 배출된 / 인위적 이산화탄소 배출량의 / 약 30퍼센트를 흡수해 왔습니다.",
                 "The world's oceans have absorbed / approximately thirty percent / of anthropogenic carbon dioxide emissions / produced since the industrial era."),
                ("When carbon dioxide dissolves in seawater, / it reacts with water molecules / to form carbonic acid, / thereby lowering ocean pH.",
                 "이산화탄소가 바닷물에 용해될 때, / 물 분자와 반응하여 탄산을 형성하며, / 그 결과 해양의 pH를 낮춥니다.",
                 "When carbon dioxide dissolves in seawater, / it reacts with water molecules / to form carbonic acid, / thereby lowering ocean pH."),
                ("This progressive acidification / reduces the concentration of ambient carbonate ions, / which marine calcifiers rely upon to build shells.",
                 "이 점진적인 산성화는 / 주변 탄산염 이온의 농도를 감소시키며, / 이는 석회화 해양 생물들이 껍데기를 만들기 위해 의존하는 물질입니다.",
                 "This progressive acidification / reduces the concentration of ambient carbonate ions, / which marine calcifiers rely upon / to build shells."),
                ("Corals, pteropods, and shellfish face thinning shells and stunted growth, / threatening the foundation of marine food webs.",
                 "산호, 익족류, 조개류는 껍데기 박형화와 성장 저해에 직면하여, / 해양 먹이사슬의 기반을 위협받고 있습니다.",
                 "Corals, pteropods, and shellfish / face thinning shells and stunted growth, / threatening the foundation / of marine food webs.")
            ],
            [
                ("anthropogenic", "adj.", "인위적인, 인류 활동에서 기인한", "Anthropogenic greenhouse gas emissions drive global warming."),
                ("dissolve", "v.", "용해되다, 녹다", "Granulated sugar dissolves quickly in hot coffee."),
                ("calcifiers", "n.", "석회화 생물 (탄산칼슘 골격을 만드는 유기체)", "Marine calcifiers struggle to precipitate aragonite in acidic waters."),
                ("stunted", "adj.", "발달이 저해된, 성장을 멈춘", "Severe drought resulted in stunted crop growth across the region.")
            ],
            [
                ("thereby lowering ~", "'그로 인해 ~을 낮추면서' 결과를 나타내는 분사구문입니다."),
                ("which marine calcifiers rely upon", "전치사 upon의 목적어 역할을 하는 관계대명사 which 절입니다.")
            ],
            [
                ("What chemical is formed when carbon dioxide dissolves in seawater?",
                 "이산화탄소가 바닷물에 녹을 때 어떤 화학 물질이 형성되는가?",
                 ["Hydrochloric acid", "Carbonic acid", "Liquid nitrogen", "Solid calcium carbonate"],
                 1,
                 "두 번째 문장에 'it reacts with water molecules to form carbonic acid'라고 명시되어 있습니다."),
                ("Why is the reduction of carbonate ions dangerous for marine calcifiers?",
                 "탄산염 이온의 감소가 왜 석회화 해양 생물들에게 위험한가?",
                 ["Because they rely upon carbonate ions to build shells.", "Because it stops fish from breathing dissolved oxygen.", "Because it prevents sunlight from reaching shallow waters.", "Because it makes oceanic water too warm to survive."],
                 0,
                 "세 번째 문장에 탄산염 이온은 석회화 생물들이 껍데기를 만들기 위해 의존하는 물질이라고 나와 있습니다."),
                ("Which marine organisms are highlighted as facing thinning shells?",
                 "껍데기 박형화에 직면한 것으로 강조된 해양 생물들은 무엇인가?",
                 ["Sharks and killer whales", "Corals, pteropods, and shellfish", "Deep-sea squids and octopuses", "Pelicans and coastal seagulls"],
                 1,
                 "마지막 문장에 산호, 익족류, 조개류가 껍데기 박형화와 성장 저해에 직면해 있다고 명시되어 있습니다.")
            ]
        ),
        (
            "i-65",
            "Backpropagation and Neural Network Learning",
            "역전파 알고리즘과 인공신경망의 학습 원리",
            "Computer Science & AI",
            "MIT CSAIL & Nature Review on Deep Learning",
            "역전파 알고리즘은 출력 오차를 연쇄 법칙을 통해 역방향으로 전파하여 각 가중치의 기여도를 계산하고 손실을 최소화합니다.",
            [
                ("Artificial neural networks learn complex patterns / by continuously tuning internal parameters / known as weights and biases.",
                 "인공신경망은 가중치와 편향으로 알려진 / 내부 매개변수들을 지속적으로 미세 조정함으로써 / 복잡한 패턴을 학습합니다.",
                 "Artificial neural networks learn complex patterns / by continuously tuning internal parameters / known as weights and biases."),
                ("During a forward pass, / input signals traverse layered nodes / to yield a predicted output.",
                 "순전파 과정 동안, / 입력 신호들은 계층화된 노드들을 통과하여 / 예측된 출력값을 산출합니다.",
                 "During a forward pass, / input signals traverse layered nodes / to yield a predicted output."),
                ("The loss function computes the discrepancy / between the network's prediction and the ground truth.",
                 "손실 함수는 네트워크의 예측값과 / 실제 정답 사이의 불일치를 계산합니다.",
                 "The loss function computes the discrepancy / between the network's prediction / and the ground truth."),
                ("Backpropagation then applies the mathematical chain rule of calculus / to propagate errors backward, / updating weights via gradient descent to minimize overall loss.",
                 "그런 다음 역전파는 미적분학의 연쇄 법칙을 적용하여 / 오차를 역방향으로 전파하고, / 경사 하강법을 통해 가중치를 갱신하여 전체 손실을 최소화합니다.",
                 "Backpropagation then applies / the mathematical chain rule of calculus / to propagate errors backward, / updating weights via gradient descent / to minimize overall loss.")
            ],
            [
                ("traverse", "v.", "가로지르다, 통과하다", "Hikers traversed the rugged mountain range over four days."),
                ("discrepancy", "n.", "불일치, 차이", "Auditors uncovered a discrepancy between receipts and ledger entries."),
                ("calculus", "n.", "미적분학", "Differential calculus allows scientists to model rates of instantaneous change."),
                ("gradient", "n.", "기울기, 경사도", "The train slowed down as it approached a steep railway gradient.")
            ],
            [
                ("by continuously tuning ~", "'~을 지속적으로 조정함으로써' 수단과 방법을 나타내는 전치사구입니다."),
                ("updating weights via ~", "동시동작을 나타내는 분사구문으로 '경사 하강법을 통해 가중치를 갱신하면서'로 해석됩니다.")
            ],
            [
                ("What happens during the forward pass of a neural network?",
                 "인공신경망의 순전파 과정 동안 무슨 일이 일어나는가?",
                 ["The network deletes its training database.", "Input signals traverse layered nodes to yield a predicted output.", "The computer hardware completely shuts down.", "Weights are randomly erased to save electricity."],
                 1,
                 "두 번째 문장에 'input signals traverse layered nodes to yield a predicted output'라고 나와 있습니다."),
                ("What does the loss function compute?",
                 "손실 함수는 무엇을 계산하는가?",
                 ["The internet connection speed", "The discrepancy between the prediction and the ground truth", "The physical weight of the server racks", "The price of graphic cards in international markets"],
                 1,
                 "세 번째 문장에 예측값과 실제 정답 사이의 불일치를 계산한다고 명시되어 있습니다."),
                ("What mathematical principle does backpropagation utilize to send errors backward?",
                 "역전파는 오차를 역방향으로 전달하기 위해 어떤 수학적 원리를 활용하는가?",
                 ["Euclidean geometry", "The chain rule of calculus", "Prime number factorization", "Bayesian coin tossing"],
                 1,
                 "마지막 문장에 'mathematical chain rule of calculus to propagate errors backward'라고 명시되어 있습니다.")
            ]
        ),
        (
            "i-66",
            "The Neurobiology of REM Sleep",
            "렘(REM) 수면의 신경생물학과 기억 통합",
            "Neuroscience",
            "Harvard Medical School Division of Sleep Medicine",
            "렘수면 동안 뇌간의 신경전달물질 조절로 전신 근육 마비가 유도되며, 활발한 뇌파 활동 속에 정서적 기억이 재구성됩니다.",
            [
                ("Rapid Eye Movement (REM) sleep represents a paradoxical state / characterized by high brain metabolic activity / accompanied by somatic muscle paralysis.",
                 "빠른 안구 운동(REM) 수면은 전신 근육 마비를 동반한 / 높은 뇌 대사 활동을 특징으로 하는 / 역설적인 수면 상태를 나타냅니다.",
                 "Rapid Eye Movement (REM) sleep / represents a paradoxical state / characterized by high brain metabolic activity / accompanied by somatic muscle paralysis."),
                ("While the sleeper's eyes dart rapidly beneath closed eyelids, / brain waves closely resemble the wakeful waking state.",
                 "수면자의 안구가 감긴 눈꺼풀 아래에서 빠르게 움직이는 동안, / 뇌파는 각성 상태인 깨어있는 상태와 매우 유사합니다.",
                 "While the sleeper's eyes dart rapidly / beneath closed eyelids, / brain waves closely resemble / the wakeful waking state."),
                ("Specialized neurons in the brainstem release inhibitory neurotransmitters / that block motor signals, / preventing individuals from physically acting out their vivid dreams.",
                 "뇌간의 특수화된 뉴런들은 운동 신호를 차단하는 / 억제성 신경전달물질을 방출하여, / 개인이 생생한 꿈을 물리적으로 행동으로 옮기는 것을 방지합니다.",
                 "Specialized neurons in the brainstem / release inhibitory neurotransmitters / that block motor signals, / preventing individuals from physically acting out / their vivid dreams."),
                ("Neuroscientists believe this neurological phase / is indispensable for consolidating procedural memories / and regulating emotional homeostasis.",
                 "신경과학자들은 이 신경학적 단계가 / 절차적 기억을 공고히 다지고 / 감정적 항상성을 조절하는 데 필수적이라고 믿습니다.",
                 "Neuroscientists believe / this neurological phase / is indispensable for consolidating procedural memories / and regulating emotional homeostasis.")
            ],
            [
                ("paradoxical", "adj.", "역설적인, 모순처럼 보이는", "It is paradoxical that standing still can cause more fatigue than walking."),
                ("somatic", "adj.", "신체의, 육체의", "Somatic nerves control voluntary skeletal muscle movements."),
                ("inhibitory", "adj.", "억제성의, 제어하는", "GABA is the chief inhibitory neurotransmitter in the mammalian central nervous system."),
                ("homeostasis", "n.", "항상성 (생체 균형 유지)", "Sweating helps maintain thermal homeostasis in scorching weather.")
            ],
            [
                ("prevent A from -ing", "'A가 ~하는 것을 방지하다/막다'라는 핵심 빈출 금지 구문입니다."),
                ("indispensable for ~", "'~에 필수불가결한, 없어서는 안 될'을 뜻하는 형용사구입니다.")
            ],
            [
                ("Why is REM sleep described as a 'paradoxical' state?",
                 "왜 렘수면은 '역설적인' 상태로 기술되는가?",
                 ["Because the heart completely stops beating for hours.", "Because high brain metabolic activity is accompanied by muscle paralysis.", "Because body temperature drops below freezing.", "Because people never breathe during this phase."],
                 1,
                 "첫 문장에 높은 뇌 대사 활동과 신체 근육 마비가 함께 동반되기 때문이라고 설명합니다."),
                ("What prevents people from acting out their dreams during REM sleep?",
                 "렘수면 동안 사람들이 꿈을 행동으로 옮기지 못하게 막아주는 것은 무엇인가?",
                 ["Inhibitory neurotransmitters from the brainstem blocking motor signals", "Heavy iron blankets placed on sleeping limbs", "The absolute absence of sensory neurons in ears", "A conscious decision made before falling asleep"],
                 0,
                 "세 번째 문장에 뇌간의 억제성 신경전달물질이 운동 신호를 차단하기 때문이라고 나와 있습니다."),
                ("According to neuroscientists, what is REM sleep indispensable for?",
                 "신경과학자들에 따르면 렘수면은 무엇에 필수적인가?",
                 ["Digesting raw fibrous vegetables", "Consolidating procedural memories and regulating emotional homeostasis", "Cooling down blood temperature below twenty degrees", "Generating permanent muscle mass without food"],
                 1,
                 "마지막 문장에 절차적 기억을 통합하고 감정적 항상성을 조절하는 데 필수적이라고 명시되어 있습니다.")
            ]
        ),
        (
            "i-67",
            "Economic Externalities and Pigouvian Taxes",
            "외부효과의 경제학과 피구세",
            "Economics & Public Policy",
            "Journal of Economic Perspectives & Arthur Pigou Classical Theory",
            "시장 거래가 제3자에게 의도치 않은 비용을 발생시키는 부정적 외부효과는 세금을 통해 사회적 한계 비용을 가격에 내부화함으로써 교정할 수 있습니다.",
            [
                ("In free-market economics, / an externality occurs / when the production or consumption of a good / imposes uncompensated costs on third parties.",
                 "자유 시장 경제학에서, / 외부효과는 재화의 생산이나 소비가 / 제3자에게 보상되지 않는 비용을 부과할 때 / 발생합니다.",
                 "In free-market economics, / an externality occurs / when the production or consumption of a good / imposes uncompensated costs on third parties."),
                ("For instance, / a factory emitting toxic fumes creates a negative externality / because surrounding residents suffer pollution damages.",
                 "예를 들어, / 유독성 연기를 배출하는 공장은 주변 주민들이 오염 피해를 입기 때문에 / 부정적 외부효과를 발생시킵니다.",
                 "For instance, / a factory emitting toxic fumes / creates a negative externality / because surrounding residents suffer pollution damages."),
                ("Because these environmental damages are omitted from private balance sheets, / the market produces more pollutants than is socially optimal.",
                 "이러한 환경 피해가 사적 대차대조표에서 누락되기 때문에, / 시장은 사회적으로 최적인 수준보다 더 많은 오염물질을 배출합니다.",
                 "Because these environmental damages / are omitted from private balance sheets, / the market produces more pollutants / than is socially optimal."),
                ("To remedy this market failure, / economist Arthur Pigou proposed levying a targeted tax / equal to the marginal external damage, / effectively internalizing the social cost into market prices.",
                 "이러한 시장 실패를 바로잡기 위해, / 경제학자 아서 피구는 한계 외부 피해액과 동일한 표적 세금을 부과하여 / 사회적 비용을 시장 가격 안으로 효과적으로 내부화할 것을 제안했습니다.",
                 "To remedy this market failure, / economist Arthur Pigou proposed / levying a targeted tax / equal to the marginal external damage, / effectively internalizing the social cost / into market prices.")
            ],
            [
                ("externality", "n.", "외부효과 (제3자에게 미치는 영향)", "Industrial runoff polluting rivers is a classic negative externality."),
                ("uncompensated", "adj.", "보상받지 못한", "The volunteers provided hundreds of hours of uncompensated community service."),
                ("optimal", "adj.", "최적의, 가장 바람직한", "Aerodynamic cars achieve optimal fuel efficiency on highways."),
                ("internalize", "v.", "내부화하다", "Firms internalize waste disposal costs by recycling manufacturing byproducts.")
            ],
            [
                ("To remedy ~", "문두에 위치한 to부정사 부사적 용법으로 '~을 바로잡기 위해' 목적을 나타냅니다."),
                ("equal to + 명사", "'~와 동등한, 같은' 형용사구 수식입니다.")
            ],
            [
                ("When does an economic externality occur?",
                 "경제적 외부효과는 언제 발생하는가?",
                 ["When governments abolish all currency notes", "When production or consumption imposes uncompensated costs on third parties", "When companies earn zero profit on holidays", "When workers demand lower wages willingly"],
                 1,
                 "첫 문장에 재화의 생산이나 소비가 제3자에게 보상되지 않는 비용을 부과할 때 발생한다고 설명합니다."),
                ("Why does the free market produce more pollutants than socially optimal?",
                 "왜 자유 시장은 사회적 최적치보다 더 많은 오염물질을 생산하는가?",
                 ["Because buyers refuse to purchase goods", "Because environmental damages are omitted from private balance sheets", "Because factories are strictly legally required to pollute", "Because pollution cleans urban air faster"],
                 1,
                 "세 번째 문장에 환경 피해가 기업의 사적 대차대조표에서 빠져 있기 때문이라고 명시되어 있습니다."),
                ("What was Arthur Pigou's proposed remedy for negative externalities?",
                 "부정적 외부효과에 대해 아서 피구가 제안한 해결책은 무엇이었는가?",
                 ["Completely closing down all manufacturing sectors", "Levying a targeted tax equal to the marginal external damage", "Providing free cash handouts to factory owners", "Banning international oceanic trade"],
                 1,
                 "마지막 문장에 한계 외부 피해액에 상응하는 세금을 부과하여 비용을 내부화하는 것이라고 나와 있습니다.")
            ]
        ),
        (
            "i-68",
            "The Mystery of Quantum Entanglement",
            "양자 얽힘의 신비와 국소성 원리의 붕괴",
            "Theoretical Physics",
            "Stanford Encyclopedia of Philosophy & Alain Aspect Nobel Studies",
            "양자 얽힘 상태의 입자들은 공간적으로 무한히 떨어져 있어도 하나의 입자 상태가 측정되는 즉시 다른 입자의 상태가 결정됩니다.",
            [
                ("Quantum entanglement is a phenomenon / wherein two or more subatomic particles become deeply interconnected / such that one particle's quantum state cannot be described independently.",
                 "양자 얽힘은 둘 이상의 아원자 입자가 매우 깊게 상호 연결되어 / 한 입자의 양자 상태를 독립적으로 기술할 수 없게 되는 / 현상입니다.",
                 "Quantum entanglement is a phenomenon / wherein two or more subatomic particles / become deeply interconnected / such that one particle's quantum state / cannot be described independently."),
                ("When a physical property / such as spin or polarization / is measured on one entangled particle, / the corresponding state of its entangled partner collapses instantaneously.",
                 "스핀이나 편광과 같은 물리적 성질이 / 얽힌 한 입자에서 측정될 때, / 얽힌 상대 입자의 해당 상태는 즉각적으로 붕괴되어 결정됩니다.",
                 "When a physical property / such as spin or polarization / is measured on one entangled particle, / the corresponding state of its entangled partner / collapses instantaneously."),
                ("Albert Einstein famously expressed profound skepticism, / derisively referring to this instantaneous non-local correlation / as 'spooky action at a distance.'",
                 "알베르트 아인슈타인은 이러한 순간적인 비국소적 상관관계를 / 조롱하듯 '유령 같은 원격 작용'이라 부르며 / 깊은 회의감을 표명했습니다.",
                 "Albert Einstein famously expressed profound skepticism, / derisively referring to this instantaneous non-local correlation / as 'spooky action at a distance.'"),
                ("However, / rigorous Bell test experiments conducted across vast distances / have consistently confirmed that the quantum world defies classical notions of local realism.",
                 "그러나, / 광대한 거리에 걸쳐 수행된 엄격한 벨 부등식 검증 실험들은 / 양자 세계가 국소 실재론이라는 고전적 개념을 거부한다는 점을 일관되게 확인해 주었습니다.",
                 "However, / rigorous Bell test experiments / conducted across vast distances / have consistently confirmed / that the quantum world defies classical notions of local realism.")
            ],
            [
                ("interconnected", "adj.", "상호 연결된, 밀접한 관계의", "Modern power grids and computer systems are deeply interconnected."),
                ("instantaneously", "adv.", "순간적으로, 즉각", "The laser beam hit the target sensor instantaneously."),
                ("skepticism", "n.", "회의론, 의심", "Scientists greeted the cold fusion claims with healthy skepticism."),
                ("defy", "v.", "거부하다, 무시하다, 반항하다", "The acrobat's balance seemed to defy physical gravity.")
            ],
            [
                ("such that + 절", "'그 결과 ~할 정도로, ~하도록' 결과를 나타내는 구문입니다."),
                (", referring to A as B", "'A를 B라고 부르면서' 동시동작을 나타내는 분사구문입니다.")
            ],
            [
                ("What happens when a property is measured on one entangled particle?",
                 "얽힌 한 입자에서 물리적 특성이 측정되면 무슨 일이 일어나는가?",
                 ["The particle permanently disappears from existence.", "The corresponding state of its partner collapses instantaneously.", "The partner turns into an anti-matter proton.", "Both particles heat up to millions of degrees."],
                 1,
                 "두 번째 문장에 얽힌 상대 입자의 상태가 즉각적으로 결정(붕괴)된다고 나와 있습니다."),
                ("What phrase did Albert Einstein use to describe this non-local correlation?",
                 "알베르트 아인슈타인은 이 비국소적 상관관계를 묘사하기 위해 어떤 어구를 사용했는가?",
                 ["'Harmonious planetary dance'", "'Spooky action at a distance'", "'Invisible mechanical gravity'", "'Subatomic clockwork motion'"],
                 1,
                 "세 번째 문장에 'spooky action at a distance'라고 불렀다고 명시되어 있습니다."),
                ("What have Bell test experiments confirmed about the quantum world?",
                 "벨 부등식 실험들은 양자 세계에 대해 무엇을 확인해 주었는가?",
                 ["It strictly adheres to 19th-century mechanical clocks.", "It defies classical notions of local realism.", "It proves that particles do not exist at all.", "It invalidates all laws of electromagnetic optics."],
                 1,
                 "마지막 문장에 양자 세계가 국소 실재론의 고전적 개념을 거부함을 일관되게 확인했다고 나와 있습니다.")
            ]
        ),
        (
            "i-69",
            "Plate Tectonics and Megathrust Earthquakes",
            "판 구조론과 거대 역단층 지진의 역학",
            "Geophysics",
            "U.S. Geological Survey (USGS) Earthquake Hazards Program",
            "해양판이 대륙판 아래로 섭입하는 경계에서 축적된 엄청난 마찰 응력이 한순간에 방출되면서 규모 9 이상의 거대 지진과 쓰나미가 발생합니다.",
            [
                ("The outermost shell of the Earth / is fragmented into rigid lithospheric plates / that glide slowly over the ductile asthenosphere.",
                 "지구의 가장 바깥쪽 껍질은 / 연약한 연약권 위를 천천히 미끄러지는 / 단단한 암석권 판들로 조각나 있습니다.",
                 "The outermost shell of the Earth / is fragmented into rigid lithospheric plates / that glide slowly over the ductile asthenosphere."),
                ("At convergent boundaries, / a denser oceanic plate plunges underneath a lighter continental plate / in a geological process known as subduction.",
                 "수렴 경계에서는, / 더 조밀한 해양판이 섭입이라 알려진 지질학적 과정을 통해 / 더 가벼운 대륙판 아래로 밀려 들어갑니다.",
                 "At convergent boundaries, / a denser oceanic plate plunges / underneath a lighter continental plate / in a geological process known as subduction."),
                ("Along the contact interface, / tectonic friction locks the plates together, / accumulating enormous elastic strain over centuries.",
                 "접촉면을 따라, / 판의 마찰력이 판들을 서로 맞물려 고정시키며, / 수세기에 걸쳐 거대한 탄성 변형 에너지를 축적합니다.",
                 "Along the contact interface, / tectonic friction locks the plates together, / accumulating enormous elastic strain / over centuries."),
                ("When frictional resistance is finally overwhelmed, / the fault slips catastrophically in a megathrust earthquake, / displacing ocean water to generate destructive tsunamis.",
                 "마찰 저항이 마침내 한계를 넘어서면, / 단층이 거대 역단층 지진으로 파국적인 미끄러짐을 일으키며, / 바닷물을 밀어내어 파괴적인 쓰나미를 발생시킵니다.",
                 "When frictional resistance is finally overwhelmed, / the fault slips catastrophically / in a megathrust earthquake, / displacing ocean water / to generate destructive tsunamis.")
            ],
            [
                ("lithospheric", "adj.", "암석권의", "Lithospheric plates drift at speeds of several centimeters per year."),
                ("ductile", "adj.", "연성의, 변형하기 쉬운", "Ductile metals like copper can be drawn into thin electrical wires."),
                ("subduction", "n.", "섭입 (한 판이 다른 판 밑으로 들어감)", "The Pacific Ring of Fire is shaped by widespread subduction zones."),
                ("catastrophically", "adv.", "파국적으로, 대참사로", "The poorly designed earthen dam failed catastrophically during torrential rains.")
            ],
            [
                ("is fragmented into ~", "'~로 조각나다, 분할되다' 수동태 표현입니다."),
                (", displacing ~", "연속적인 결과를 나타내는 분사구문으로 '바닷물을 밀어내면서'로 해석됩니다.")
            ],
            [
                ("What happens at convergent plate boundaries according to the text?",
                 "본문에 따르면 수렴 판 경계에서 무슨 일이 일어나는가?",
                 ["Plates melt into steam instantly.", "A denser oceanic plate plunges underneath a lighter continental plate.", "Plates move away leaving a deep empty hole to the core.", "The ground freezes permanently into pure granite."],
                 1,
                 "두 번째 문장에 조밀한 해양판이 가벼운 대륙판 아래로 섭입한다고 설명합니다."),
                ("What locks the plates together and accumulates strain over centuries?",
                 "무엇이 판을 맞물려 고정시키고 수세기에 걸쳐 변형 에너지를 축적시키는가?",
                 ["Underground magma rivers flowing backwards", "Tectonic friction along the contact interface", "Artificial concrete walls built by civil engineers", "Strong magnetic charges on mountain peaks"],
                 1,
                 "세 번째 문장에 'tectonic friction locks the plates together, accumulating enormous elastic strain'이라고 명시되어 있습니다."),
                ("How are destructive tsunamis generated during a megathrust earthquake?",
                 "거대 역단층 지진 동안 파괴적인 쓰나미는 어떻게 발생하는가?",
                 ["By lightning striking open ocean waters", "By the catastrophic fault slip displacing immense volumes of ocean water", "By hurricane winds blowing water onto shorelines", "By marine creatures swimming in rapid unison"],
                 1,
                 "마지막 문장에 단층의 파국적 미끄러짐이 바닷물을 밀어내어 쓰나미를 만든다고 설명합니다.")
            ]
        ),
        (
            "i-70",
            "Loss Aversion in Behavioral Economics",
            "행동경제학의 손실 회피성과 인간 심리",
            "Behavioral Science & Economics",
            "Econometrica & Daniel Kahneman / Amos Tversky Prospect Theory",
            "인간은 동등한 금액의 이익에서 느끼는 기쁨보다 손실에서 느끼는 심리적 고통을 대략 2배 이상 더 강렬하게 인지한다는 것이 밝혀졌습니다.",
            [
                ("Classical economic models assumed / that human decision-makers evaluate prospective gains and losses / with strict mathematical symmetry.",
                 "고전 경제학 모델들은 / 인간 의사결정자가 예상되는 이익과 손실을 / 엄격한 수학적 대칭성 속에서 평가한다고 가정했습니다.",
                 "Classical economic models assumed / that human decision-makers / evaluate prospective gains and losses / with strict mathematical symmetry."),
                ("However, / groundbreaking research in Prospect Theory by psychologists Daniel Kahneman and Amos Tversky / debunked this rational premise.",
                 "그러나, / 심리학자 대니얼 카너먼과 아모스 트버스키의 전망 이론에 관한 획기적인 연구는 / 이러한 합리적 전제를 무너뜨렸습니다.",
                 "However, / groundbreaking research in Prospect Theory / by psychologists Daniel Kahneman and Amos Tversky / debunked this rational premise."),
                ("They uncovered the phenomenon of loss aversion, / demonstrating that the psychological pain of losing one hundred dollars / is roughly twice as intense as the pleasure of gaining that same amount.",
                 "그들은 손실 회피 현상을 규명하여, / 백 달러를 잃었을 때의 심리적 고통이 / 동일한 금액을 얻었을 때의 기쁨보다 대략 두 배 더 강렬하다는 점을 증명했습니다.",
                 "They uncovered the phenomenon of loss aversion, / demonstrating that the psychological pain / of losing one hundred dollars / is roughly twice as intense / as the pleasure of gaining that same amount."),
                ("This asymmetric valuation explains / why investors irrationally cling to declining stocks / rather than realizing losses to reallocate capital effectively.",
                 "이러한 비대칭적인 가치 평가는 / 왜 투자자들이 자본을 효과적으로 재배분하기 위해 손실을 확정짓기보다 / 가치가 하락하는 주식을 비합리적으로 붙들고 있는지를 설명해 줍니다.",
                 "This asymmetric valuation explains / why investors irrationally cling to declining stocks / rather than realizing losses / to reallocate capital effectively.")
            ],
            [
                ("symmetry", "n.", "대칭성, 균형", "The classical facade displayed perfect architectural symmetry."),
                ("debunk", "v.", "틀렸음을 밝히다, 허구성을 폭로하다", "Modern medical trials debunked the myth of miracle herbal cures."),
                ("asymmetric", "adj.", "비대칭의, 불균형한", "Asymmetric information between buyers and sellers distorts markets."),
                ("reallocate", "v.", "재배분하다, 재할당하다", "The corporate board voted to reallocate budget toward research and development.")
            ],
            [
                ("twice as + 원급 + as", "'~보다 두 배 더 …한' 배수사 비교 표현입니다."),
                ("rather than -ing", "'~하기보다는 차라리' 선택적 대비를 나타냅니다.")
            ],
            [
                ("What did classical economics assume about gains and losses?",
                 "고전 경제학은 이익과 손실에 대해 무엇을 가정했는가?",
                 ["That humans always prefer losing money", "That humans evaluate them with strict mathematical symmetry", "That only coins matter and banknotes are ignored", "That emotions dictate every single financial calculation"],
                 1,
                 "첫 문장에 고전 경제학 모델은 이익과 손실을 엄격한 수학적 대칭성으로 평가한다고 가정했다고 나와 있습니다."),
                ("According to loss aversion research, how does losing $100 compare to gaining $100?",
                 "손실 회피 연구에 따르면, 100달러를 잃는 것은 100달러를 얻는 것과 비교하여 어떠한가?",
                 ["The pain of losing is roughly twice as intense as the pleasure of gaining.", "The pleasure of gaining is ten times stronger than losing.", "Both evoke zero psychological reaction.", "Losing money makes people feel immediately happy."],
                 0,
                 "세 번째 문장에 100달러를 잃을 때의 심리적 고통이 같은 금액을 얻을 때의 기쁨보다 대략 두 배 더 강렬하다고 명시되어 있습니다."),
                ("What irrational investor behavior does asymmetric valuation explain?",
                 "비대칭적 가치 평가는 투자자들의 어떤 비합리적인 행동을 설명해 주는가?",
                 ["Buying companies without knowing their corporate names", "Clinging to declining stocks rather than realizing losses", "Donating all portfolio gains to stranger charities", "Trading only during midnight hours"],
                 1,
                 "마지막 문장에 투자자들이 손실을 확정짓기보다 하락하는 주식을 비합리적으로 붙들고 있는 이유를 설명한다고 나와 있습니다.")
            ]
        )
    ]
