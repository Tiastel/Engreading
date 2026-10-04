# -*- coding: utf-8 -*-
import json
import random

# We will create 60 distinct questions for each of the 5 levels (Total: 300 questions)

questions = []

# =========================================================================
# LEVEL 1: Lv.1 기초 논리 (60문항) - 단일 빈칸 / 인과·순접·정의 / 기초 편입·수능1등급
# =========================================================================
l1_data = [
    # 1..10
    {
        "theme": "Medical Science & Public Health",
        "logicType": "인과 / 귀결 (Causality)",
        "clue": "Because childhood immunization creates community-wide herd immunity",
        "direction": "원인(집단 면역 형성) → 결과(질병 확산 억제/차단)",
        "question": "Because widespread childhood immunization establishes collective herd immunity, healthcare authorities can effectively ________ the transmission of once-fatal airborne pathogens.",
        "questionKo": "광범위한 아동 예방접종은 집단 면역을 형성하기 때문에, 보건 당국은 한때 치명적이었던 공기 매개 병원균의 전파를 효과적으로 ________할 수 있다.",
        "correct": "curtail",
        "distractors": ["exacerbate", "proliferate", "stimulate"],
        "vocab": [
            ("curtail", "축소하다, 억제하다 (v.)"),
            ("exacerbate", "악화시키다 (v.)"),
            ("proliferate", "급증하다, 확산하다 (v.)"),
            ("stimulate", "자극하다, 촉진하다 (v.)"),
            ("immunization", "예방접종, 면역 형성 (n.)"),
            ("pathogen", "병원균, 병원체 (n.)")
        ],
        "explanation": "원인을 나타내는 접속사 Because와 집단 면역(herd immunity)의 긍정적 효과가 제시되었으므로, 병원균 전파를 '줄이거나 억제한다'는 의미의 curtail이 정답입니다. 악화시키다(exacerbate)나 급증시키다(proliferate)는 반대 방향입니다."
    },
    {
        "theme": "Environmental Economics",
        "logicType": "목적 / 수단 (Purpose & Means)",
        "clue": "in order to protect endangered wetlands from irreversible degradation",
        "direction": "목적(습지 파괴 방지) → 수단(엄격한 환경 규제 도입/부과)",
        "question": "In order to protect fragile coastal wetlands from permanent industrial degradation, the municipal council voted to ________ strict zoning restrictions on commercial real estate developers.",
        "questionKo": "취약한 연안 습지를 영구적인 산업적 훼손으로부터 보호하기 위해, 시의회는 상업용 부동산 개발업자들에게 엄격한 구역 지정 규제를 ________하기로 의결했다.",
        "correct": "impose",
        "distractors": ["repeal", "rescind", "dismantle"],
        "vocab": [
            ("impose", "부과하다, 도입하다 (v.)"),
            ("repeal", "폐지하다, 철회하다 (v.)"),
            ("rescind", "무효로 하다, 폐지하다 (v.)"),
            ("dismantle", "해체하다, 분해하다 (v.)"),
            ("degradation", "퇴화, 황폐화, 훼손 (n.)"),
            ("municipal", "시의, 자치단체의 (adj.)")
        ],
        "explanation": "습지를 파괴로부터 지키기 위한 목적(In order to protect)이 주어졌으므로, 개발업자에게 규제를 '부과하거나 적용한다(impose)'가 와야 합니다. 폐지하다(repeal, rescind, dismantle)는 습지를 위험에 빠뜨리는 정반대 방향입니다."
    },
    {
        "theme": "Cognitive Psychology",
        "logicType": "순접 / 상술 (Elaboration)",
        "clue": "regular aerobic exercise increases cerebral blood flow and promotes synaptic connectivity",
        "direction": "긍정적 생리적 변화 → 인지 기능 향상(+)",
        "question": "Recent clinical evaluations reveal that consistent aerobic exercise significantly enhances neurogenesis, thereby helping to ________ memory retention among elderly cohorts.",
        "questionKo": "최근 임상 평가에 따르면 꾸준한 유산소 운동은 신경 발생을 크게 향상시키며, 그에 따라 노년층 집단의 기억력 유지를 ________하는 데 도움을 준다.",
        "correct": "bolster",
        "distractors": ["undermine", "deteriorate", "impair"],
        "vocab": [
            ("bolster", "강화하다, 지지하다 (v.)"),
            ("undermine", "약화시키다, 훼손하다 (v.)"),
            ("deteriorate", "악화되다, 저하시키다 (v.)"),
            ("impair", "손상시키다, 해치다 (v.)"),
            ("neurogenesis", "신경 발생, 신경 형성 (n.)"),
            ("retention", "보유, 유지력 (n.)")
        ],
        "explanation": "thereby(그에 따라)로 연결되는 인과/상술 구문입니다. 신경 발생을 향상시키므로(enhances neurogenesis), 기억 유지를 '강화하고 증진한다'는 뜻의 bolster가 적합합니다."
    },
    {
        "theme": "Archaeology & History",
        "logicType": "증거 / 입증 (Evidence & Verification)",
        "clue": "carbon dating and isotopic analysis provided indisputable chemical proof",
        "direction": "명백한 화학적 증거 확보 → 가설 입증(+)",
        "question": "The discovery of unglazed ceramic shards bearing distinctive Mesopotamian inscriptions helped archaeologists to ________ the hypothesis of ancient trans-continental trade routes.",
        "questionKo": "독특한 메소포타미아 비문이 새겨진 유약 바르지 않은 도자기 파편의 발견은 고고학자들이 고대 대륙 횡단 무역로 가설을 ________하는 데 기여했다.",
        "correct": "substantiate",
        "distractors": ["refute", "repudiate", "invalidate"],
        "vocab": [
            ("substantiate", "입증하다, 실증하다 (v.)"),
            ("refute", "반박하다 (v.)"),
            ("repudiate", "거부하다, 부인하다 (v.)"),
            ("invalidate", "무효화하다 (v.)"),
            ("inscription", "비문, 새겨진 글 (n.)"),
            ("hypothesis", "가설, 가정 (n.)")
        ],
        "explanation": "물리적 유물(도자기 파편)이 가설을 뒷받침하는 결정적 증거로 발견되었으므로, 가설을 '입증하다(substantiate)'가 가장 알맞습니다. refute/repudiate/invalidate는 반박하고 무효화한다는 반대 의미입니다."
    },
    {
        "theme": "Organizational Behavior",
        "logicType": "인과 / 귀결 (Causality)",
        "clue": "transparent corporate governance and merit-based promotion directly foster mutual trust",
        "direction": "투명한 경영/공정한 승진 → 직원 사기 진작(+)",
        "question": "Corporate cultures characterized by transparent decision-making and egalitarian communication invariably tend to ________ employee loyalty and reduce voluntary turnover.",
        "questionKo": "투명한 의사결정과 평등주의적 소통을 특징으로 하는 기업 문화는 예외 없이 직원의 충성도를 ________하고 자발적 이직을 줄이는 경향이 있다.",
        "correct": "foster",
        "distractors": ["jeopardize", "stifle", "diminish"],
        "vocab": [
            ("foster", "조성하다, 육성하다 (v.)"),
            ("jeopardize", "위태롭게 하다 (v.)"),
            ("stifle", "억누르다, 질식시키다 (v.)"),
            ("diminish", "감소시키다 (v.)"),
            ("egalitarian", "평등주의의 (adj.)"),
            ("turnover", "이직률, 회전율 (n.)")
        ],
        "explanation": "긍정적인 기업 문화(투명한 소통)가 이직을 줄이고 충성도를 '조성/육성한다'는 맥락이므로 foster가 논리적입니다."
    },
    {
        "theme": "Renewable Energy",
        "logicType": "인과 / 귀결 (Causality)",
        "clue": "Falling battery manufacturing costs have made solar storage commercially accessible",
        "direction": "제조 비용 급감 → 재생에너지 보급 가속화(+)",
        "question": "Drastic reductions in lithium-ion manufacturing expenditures have served to ________ the adoption of decentralized solar energy systems worldwide.",
        "questionKo": "리튬이온 제조 비용의 급격한 감소는 전 세계적으로 분산형 태양광 에너지 시스템의 도입을 ________하는 데 기여해 왔다.",
        "correct": "accelerate",
        "distractors": ["stagnate", "obstruct", "retard"],
        "vocab": [
            ("accelerate", "가속화하다, 촉진하다 (v.)"),
            ("stagnate", "정체시키다 (v.)"),
            ("obstruct", "방해하다 (v.)"),
            ("retard", "지연시키다, 늦추다 (v.)"),
            ("expenditure", "지출, 비용 (n.)"),
            ("decentralized", "분산화된 (adj.)")
        ],
        "explanation": "비용 감소(cost reduction)는 시장 보급을 촉진하는 정방향 인과 관계이므로 accelerate가 알맞습니다."
    },
    {
        "theme": "Linguistics & Education",
        "logicType": "정의 / 기능 (Definition & Function)",
        "clue": "serving as an indispensable bridge for multinational research collaboration",
        "direction": "필수적인 가교 역할 → 상호 이해 촉진(+)",
        "question": "A standardized academic lingua franca is widely considered to ________ cross-border scientific discourse by mitigating communicative ambiguities.",
        "questionKo": "표준화된 학술 링구아 프랑카(공용어)는 의사소통상의 모호성을 완화함으로써 국경을 넘나드는 과학적 담론을 ________하는 것으로 널리 여겨진다.",
        "correct": "facilitate",
        "distractors": ["hinder", "complicate", "impede"],
        "vocab": [
            ("facilitate", "용이하게 하다, 촉진하다 (v.)"),
            ("hinder", "저해하다 (v.)"),
            ("complicate", "복잡하게 만들다 (v.)"),
            ("impede", "방해하다 (v.)"),
            ("lingua franca", "공통어, 국제 공용어 (n.)"),
            ("ambiguity", "모호성 (n.)")
        ],
        "explanation": "모호성을 줄여주므로(mitigating ambiguities), 국경 간 학술 담론을 '용이하게 만든다(facilitate)'가 자연스럽습니다."
    },
    {
        "theme": "Cybersecurity & Cryptography",
        "logicType": "필연적 조건 (Necessary Condition)",
        "clue": "sophisticated encryption algorithms are required to maintain data integrity",
        "direction": "데이터 무결성 유지 목적 → 엄격한 암호화 표준 준수",
        "question": "To safeguard proprietary commercial databases against unauthorized breach, financial institutions must ________ strict cryptographic security protocols.",
        "questionKo": "무단 침해로부터 독점적인 상업 데이터베이스를 보호하기 위해, 금융 기관들은 엄격한 암호화 보안 프로토콜을 ________해야 한다.",
        "correct": "adhere to",
        "distractors": ["deviate from", "waive", "circumvent"],
        "vocab": [
            ("adhere to", "고수하다, 준수하다 (v.)"),
            ("deviate from", "~에서 벗어나다 (v.)"),
            ("waive", "포기하다, 면제하다 (v.)"),
            ("circumvent", "우회하다, 회피하다 (v.)"),
            ("proprietary", "독점적인, 소유권의 (adj.)"),
            ("cryptographic", "암호화의 (adj.)")
        ],
        "explanation": "데이터를 보호하기 위해(To safeguard) 규범을 '철저히 준수해야 한다(adhere to)'가 정답입니다. 규범을 어기거나 우회한다는 선지는 오답입니다."
    },
    {
        "theme": "Ecology & Marine Biology",
        "logicType": "인과 / 귀결 (Causality)",
        "clue": "rising ocean acidity weakens calcium carbonate shells",
        "direction": "해양 산성화 → 패류 및 산호초 생존 위협(-)",
        "question": "Sustained increases in oceanic acidity directly ________ the calcification process vital for the skeletal integrity of coral reefs and shell-forming organisms.",
        "questionKo": "해양 산성도의 지속적인 증가는 산호초와 조개껍데기 형성 생물의 골격 온전성에 필수적인 석회화 과정을 직접적으로 ________한다.",
        "correct": "disrupt",
        "distractors": ["reinforce", "facilitate", "propagate"],
        "vocab": [
            ("disrupt", "지장을 주다, 방해하다 (v.)"),
            ("reinforce", "강화하다 (v.)"),
            ("facilitate", "촉진하다 (v.)"),
            ("propagate", "증식시키다, 보급하다 (v.)"),
            ("calcification", "석회화 (n.)"),
            ("integrity", "온전성, 보전 (n.)")
        ],
        "explanation": "산성도의 증가는 석회화를 방해하고 골격을 약화시키므로 부정적 동사인 disrupt가 와야 합니다."
    },
    {
        "theme": "Sociology & Urban Planning",
        "logicType": "인과 / 귀결 (Causality)",
        "clue": "Affordable public transit and pedestrian-friendly boulevards encourage community interaction",
        "direction": "보행 친화 도시 계획 → 사회적 유대감 증진(+)",
        "question": "Urban landscapes designed with abundant green commons and accessible walkways have been demonstrated to ________ social cohesion among diverse neighborhood residents.",
        "questionKo": "풍부한 녹지 공원과 접근성 높은 보행로를 갖추도록 설계된 도시 경관은 다양한 지역 주민들 사이의 사회적 유대감을 ________하는 것으로 입증되었다.",
        "correct": "nurture",
        "distractors": ["erode", "dissolve", "alienate"],
        "vocab": [
            ("nurture", "육성하다, 키우다 (v.)"),
            ("erode", "침식하다, 약화시키다 (v.)"),
            ("dissolve", "해체하다, 녹이다 (v.)"),
            ("alienate", "소외시키다 (v.)"),
            ("cohesion", "유대, 결속력 (n.)"),
            ("commons", "공유지, 공원 (n.)")
        ],
        "explanation": "친화적 도시 경관이 주민 간의 결속력(cohesion)을 '증진하고 북돋운다'는 긍정적 결론이므로 nurture가 맞습니다."
    }
]

print("Script template ready.")
