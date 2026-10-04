# -*- coding: utf-8 -*-
"""
Level 1 Generator: 60 Foundational Logic Questions (Lv.1 기초 논리)
Characteristics: Single blank, clear causal/additive/definitional clues, core academic vocabulary.
"""
import random

def get_level1_questions():
    items = []
    
    # 60 distinct academic problem stems
    data = [
        (
            "Medical Science", "인과 / 귀결 (Causality)",
            "Because childhood immunization establishes herd immunity", "원인(집단면역) → 결과(감염병 억제)",
            "Because widespread childhood immunization establishes collective herd immunity, healthcare authorities can effectively ________ the transmission of once-fatal airborne pathogens.",
            "광범위한 아동 예방접종은 집단 면역을 형성하기 때문에, 보건 당국은 한때 치명적이었던 공기 매개 병원균의 전파를 효과적으로 ________할 수 있다.",
            "curtail", ["exacerbate", "proliferate", "stimulate"],
            [("curtail", "축소하다, 억제하다 (v.)"), ("exacerbate", "악화시키다 (v.)"), ("proliferate", "급증하다 (v.)"), ("stimulate", "자극하다 (v.)")],
            "접속사 Because와 집단 면역(herd immunity)의 긍정적 효과를 고려할 때, 병원균 전파를 줄이거나 막는다는 의미의 curtail이 정답입니다."
        ),
        (
            "Environmental Science", "목적 / 수단 (Purpose & Means)",
            "in order to protect fragile coastal wetlands from permanent industrial degradation", "목적(습지 보호) → 수단(엄격한 규제 부과)",
            "In order to protect fragile coastal wetlands from permanent industrial degradation, the municipal council voted to ________ strict zoning restrictions on commercial developers.",
            "취약한 연안 습지를 영구적인 산업적 훼손으로부터 보호하기 위해, 시의회는 상업용 개발업자들에게 엄격한 구역 규제를 ________하기로 의결했다.",
            "impose", ["repeal", "rescind", "dismantle"],
            [("impose", "부과하다, 도입하다 (v.)"), ("repeal", "폐지하다 (v.)"), ("rescind", "철회하다 (v.)"), ("dismantle", "해체하다 (v.)")],
            "보호 목적(In order to protect)을 달성하기 위해 규제를 '부과하다(impose)'가 적합합니다."
        ),
        (
            "Cognitive Neuroscience", "순접 / 상술 (Elaboration)",
            "increases cerebral blood flow and promotes synaptic connectivity", "생리적 활성화 → 기억력 향상(+)",
            "Recent clinical evaluations reveal that consistent aerobic exercise significantly enhances neurogenesis, thereby helping to ________ memory retention among elderly cohorts.",
            "최근 임상 평가에 따르면 꾸준한 유산소 운동은 신경 발생을 크게 향상시키며, 그에 따라 노년층의 기억력 유지를 ________하는 데 도움을 준다.",
            "bolster", ["undermine", "deteriorate", "impair"],
            [("bolster", "강화하다, 북돋우다 (v.)"), ("undermine", "약화시키다 (v.)"), ("deteriorate", "악화시키다 (v.)"), ("impair", "손상시키다 (v.)")],
            "thereby(그에 따라)로 이어지며 신경 발생이 기억력을 '강화한다(bolster)'는 긍정적 흐름입니다."
        ),
        (
            "Archaeology", "증거 / 입증 (Evidence & Verification)",
            "carbon dating and isotopic analysis provided indisputable chemical proof", "결정적 증거 확보 → 가설 입증(+)",
            "The discovery of unglazed ceramic shards bearing distinctive Mesopotamian inscriptions helped archaeologists to ________ the hypothesis of ancient trans-continental trade routes.",
            "독특한 메소포타미아 비문이 새겨진 도자기 파편의 발견은 고고학자들이 고대 대륙 횡단 무역로 가설을 ________하는 데 기여했다.",
            "substantiate", ["refute", "repudiate", "invalidate"],
            [("substantiate", "입증하다, 실증하다 (v.)"), ("refute", "반박하다 (v.)"), ("repudiate", "부인하다 (v.)"), ("invalidate", "무효화하다 (v.)")],
            "유물 발견이 가설을 뒷받침하는 강력한 증거가 되므로 '입증하다(substantiate)'가 정답입니다."
        ),
        (
            "Corporate Governance", "인과 / 귀결 (Causality)",
            "transparent decision-making and egalitarian communication foster trust", "투명한 소통 → 충성도 진작(+)",
            "Corporate cultures characterized by transparent decision-making and egalitarian communication invariably tend to ________ employee loyalty and reduce voluntary turnover.",
            "투명한 의사결정과 평등주의적 소통을 특징으로 하는 기업 문화는 예외 없이 직원의 충성도를 ________하고 자발적 이직을 줄이는 경향이 있다.",
            "foster", ["jeopardize", "stifle", "diminish"],
            [("foster", "조성하다, 육성하다 (v.)"), ("jeopardize", "위태롭게 하다 (v.)"), ("stifle", "억압하다 (v.)"), ("diminish", "감소시키다 (v.)")],
            "긍정적인 조직 문화가 충성도를 '조성한다(foster)'가 자연스럽습니다."
        ),
        (
            "Renewable Energy", "인과 / 귀결 (Causality)",
            "Drastic reductions in battery manufacturing expenditures", "제조 비용 급감 → 태양광 보급 가속화(+)",
            "Drastic reductions in lithium-ion manufacturing expenditures have served to ________ the adoption of decentralized solar energy systems worldwide.",
            "리튬이온 제조 비용의 급격한 감소는 전 세계적으로 분산형 태양광 에너지 시스템의 도입을 ________하는 데 기여해 왔다.",
            "accelerate", ["stagnate", "obstruct", "retard"],
            [("accelerate", "가속화하다 (v.)"), ("stagnate", "정체시키다 (v.)"), ("obstruct", "방해하다 (v.)"), ("retard", "지연시키다 (v.)")],
            "비용 절감은 보급을 '가속화(accelerate)'하는 직접적 원인입니다."
        ),
        (
            "Linguistics", "정의 / 기능 (Definition & Function)",
            "mitigating communicative ambiguities across international teams", "모호성 해소 → 학술 담론 촉진(+)",
            "A standardized academic lingua franca is widely considered to ________ cross-border scientific discourse by mitigating communicative ambiguities.",
            "표준화된 학술 링구아 프랑카(공용어)는 의사소통상의 모호성을 완화함으로써 국경을 넘나드는 과학적 담론을 ________하는 것으로 널리 여겨진다.",
            "facilitate", ["hinder", "complicate", "impede"],
            [("facilitate", "용이하게 하다, 촉진하다 (v.)"), ("hinder", "저해하다 (v.)"), ("complicate", "복잡하게 하다 (v.)"), ("impede", "방해하다 (v.)")],
            "모호성을 줄여 의사소통을 '원활하게 한다(facilitate)'가 맞습니다."
        ),
        (
            "Cybersecurity", "필연적 조건 (Necessary Condition)",
            "To safeguard proprietary commercial databases against unauthorized breach", "보안 침해 방지 목적 → 엄격한 암호화 프로토콜 준수",
            "To safeguard proprietary commercial databases against unauthorized breach, financial institutions must strictly ________ recognized cryptographic protocols.",
            "무단 침해로부터 독점적인 상업 데이터베이스를 보호하기 위해, 금융 기관들은 공인된 암호화 프로토콜을 엄격히 ________해야 한다.",
            "adhere to", ["deviate from", "renounce", "circumvent"],
            [("adhere to", "준수하다, 고수하다 (v.)"), ("deviate from", "벗어나다 (v.)"), ("renounce", "포기하다 (v.)"), ("circumvent", "우회하다 (v.)")],
            "보안 유지를 위해 규정을 '철저히 따라야 한다(adhere to)'가 타당합니다."
        ),
        (
            "Marine Biology", "인과 / 귀결 (Causality)",
            "Sustained increases in oceanic acidity directly affect calcification", "해양 산성화 → 조개껍질/산호초 형성 방해(-)",
            "Sustained increases in oceanic acidity directly ________ the calcification process vital for the skeletal integrity of coral reefs.",
            "해양 산성도의 지속적인 증가는 산호초의 골격 온전성에 필수적인 석회화 과정을 직접적으로 ________한다.",
            "disrupt", ["reinforce", "facilitate", "propagate"],
            [("disrupt", "방해하다, 혼란에 빠뜨리다 (v.)"), ("reinforce", "강화하다 (v.)"), ("facilitate", "촉진하다 (v.)"), ("propagate", "증식시키다 (v.)")],
            "산성화라는 유해 요인이 석회화를 '방해한다(disrupt)'가 맞습니다."
        ),
        (
            "Urban Sociology", "인과 / 귀결 (Causality)",
            "abundant green commons and accessible walkways encourage bonding", "녹지 공간과 산책로 → 주민 유대감 육성(+)",
            "Urban landscapes designed with abundant green commons and accessible walkways have been demonstrated to ________ social cohesion among diverse neighborhood residents.",
            "풍부한 녹지 공원과 접근성 높은 보행로를 갖춘 도시 경관은 다양한 지역 주민들 사이의 사회적 유대감을 ________하는 것으로 입증되었다.",
            "nurture", ["erode", "dissolve", "alienate"],
            [("nurture", "육성하다, 키우다 (v.)"), ("erode", "침식하다 (v.)"), ("dissolve", "해체하다 (v.)"), ("alienate", "소외시키다 (v.)")],
            "주민 유대감(cohesion)을 '육성하고 북돋운다(nurture)'가 맞습니다."
        ),
        # 11..20
        (
            "Nutritional Science", "결핍 / 증상 (Deficiency & Consequence)",
            "lack of micronutrient intake precipitates systemic fatigue", "필수 미량영양소 결핍 → 만성 피로 유발(-)",
            "A chronic deficiency of vital micronutrients, especially magnesium and vitamin D, can severely ________ metabolic efficiency and induce persistent lethargy.",
            "필수 미량영양소, 특히 마그네슘과 비타민 D의 만성적 결핍은 대사 효율을 심각하게 ________하고 지속적인 무기력증을 유발할 수 있다.",
            "impair", ["enhance", "stimulate", "invigorate"],
            [("impair", "손상시키다, 저하시키다 (v.)"), ("enhance", "향상시키다 (v.)"), ("stimulate", "자극하다 (v.)"), ("invigorate", "활력을 주다 (v.)")],
            "만성 결핍(deficiency)은 대사 효율을 '손상시킨다(impair)'가 논리적입니다."
        ),
        (
            "Agronomy", "상보성 / 협동 (Complementarity)",
            "legume rotation enriches nitrogenous soil content naturally", "콩과 작물 윤작 → 비료 필요성 경감(+)",
            "Integrating leguminous cover crops into conventional agricultural rotations helps to replenish depleted soil nitrogen, thereby serving to ________ dependence on synthetic fertilizers.",
            "전통적인 농작물 윤작에 콩과 피복작물을 통합하는 것은 고갈된 토양 질소를 보충하는 데 도움이 되며, 그에 따라 합성 비료에 대한 의존도를 ________하는 역할을 한다.",
            "diminish", ["intensify", "perpetuate", "compound"],
            [("diminish", "줄이다, 감소시키다 (v.)"), ("intensify", "심화하다 (v.)"), ("perpetuate", "영속시키다 (v.)"), ("compound", "가중시키다 (v.)")],
            "천연 질소를 보충하므로 합성 비료 의존을 '줄인다(diminish)'가 맞습니다."
        ),
        (
            "Astrophysics", "관측 / 입증 (Observation & Confirmation)",
            "gravitational wave detectors captured ripples from binary black holes", "중력파 검출 → 일반상대성이론 예측 검증(+)",
            "The direct detection of gravitational waves emitted by colliding binary black holes served to empirically ________ Albert Einstein's century-old theoretical predictions.",
            "충돌하는 쌍성 블랙홀에서 방출된 중력파의 직접적인 검출은 알버트 아인슈타인의 100년 된 이론적 예측을 실증적으로 ________하는 역할을 했다.",
            "validate", ["falsify", "dispute", "gainsay"],
            [("validate", "검증하다, 입증하다 (v.)"), ("falsify", "위조하다, 반증하다 (v.)"), ("dispute", "이의를 제기하다 (v.)"), ("gainsay", "부인하다 (v.)")],
            "직접 관측은 이론을 '검증/확증하다(validate)'와 연결됩니다."
        ),
        (
            "Behavioral Finance", "편향 / 오류 (Cognitive Bias)",
            "investors disproportionately fear losses over equivalent gains", "손실 회피 편향 → 합리적 포트폴리오 다각화 방해(-)",
            "The psychological tendency toward loss aversion frequently causes novice investors to ________ speculative investments too early while clinging obstinately to depreciating assets.",
            "손실 회피를 향한 심리적 경향은 초보 투자자들로 하여금 가치가 하락하는 자산에 완고하게 매달리면서 수익성 있는 투자는 너무 일찍 ________하게 만든다.",
            "liquidate", ["accumulate", "amass", "hoard"],
            [("liquidate", "청산하다, 처분하다 (v.)"), ("accumulate", "축적하다 (v.)"), ("amass", "모으다 (v.)"), ("hoard", "사재기하다 (v.)")],
            "초보 투자자가 손실은 인정 못 하고 이익 자산은 성급하게 '처분한다(liquidate)'는 행동경제학의 고전 원리입니다."
        ),
        (
            "Paleontology", "화석 증거 / 진화 계통 (Fossil Records)",
            "transitional fossils exhibit mosaic morphology between reptiles and birds", "중간 화석 발견 → 조류의 수각류 기원설 뒷받침(+)",
            "The continuous discovery of feathered dinosaur fossils in Liaoning, China has provided robust morphological evidence that helps to ________ the evolutionary lineage linking theropods to modern avians.",
            "중국 랴오닝성에서 깃털 달린 공룡 화석의 지속적인 발견은 수각류와 현대 조류를 연결하는 진화 계통을 ________하는 데 도움을 주는 강력한 형태학적 증거를 제공해 왔다.",
            "illuminate", ["obscure", "confound", "shroud"],
            [("illuminate", "밝히다, 규명하다 (v.)"), ("obscure", "흐리게 하다 (v.)"), ("confound", "혼동시키다 (v.)"), ("shroud", "가리다 (v.)")],
            "풍부한 화석 증거가 진화 계통을 '명확히 밝혀준다(illuminate)'가 정답입니다."
        ),
        (
            "Materials Science", "물성 / 응용 (Material Properties)",
            "exceptional tensile strength and thermal conductivity make graphene ideal", "그래핀의 우수한 물성 → 차세대 반도체 제조 가능성 증진(+)",
            "Owing to its extraordinary tensile strength and electrical conductivity, graphene is expected to ________ revolutionary breakthroughs in flexible electronic devices.",
            "탁월한 인장 강도와 전기 전도성 덕분에, 그래핀은 유연한 전자 기기 분야에서 혁신적인 돌파구를 ________할 것으로 기대된다.",
            "instigate", ["stymie", "preclude", "hinder"],
            [("instigate", "유발하다, 촉발하다 (v.)"), ("stymie", "방해하다 (v.)"), ("preclude", "배제하다 (v.)"), ("hinder", "가로막다 (v.)")],
            "우수한 물성이 기술 혁신을 '촉발/유발할(instigate)' 것으로 기대됩니다."
        ),
        (
            "Epidemiology", "신속 대응 / 억제 (Rapid Response)",
            "early contact tracing and quarantine protocols contain viral transmission", "초기 접촉자 추적 → 지역사회 감염 억제(+)",
            "Rigorous contact tracing implemented during the incipient phase of an outbreak can effectively ________ the transmission vector before community contagion occurs.",
            "발병 초기 단계에 실행된 엄격한 접촉자 추적은 지역사회 감염이 발생하기 전에 전파 매개체를 효과적으로 ________할 수 있다.",
            "neutralize", ["propagate", "instigate", "augment"],
            [("neutralize", "무력화하다, 상쇄하다 (v.)"), ("propagate", "전파하다 (v.)"), ("instigate", "부추기다 (v.)"), ("augment", "늘리다 (v.)")],
            "감염 초기 추적으로 바이러스를 '무력화/차단한다(neutralize)'가 맞습니다."
        ),
        (
            "Developmental Economics", "인프라 투자 / 경제 성장 (Capital Investment)",
            "universal access to broadband internet and electricity unlocks rural commerce", "인프라 확충 → 지방 경제 생산성 신장(+)",
            "Public investments in rural broadband infrastructure directly stimulate local commerce by helping to ________ educational and financial resources to marginalized communities.",
            "농촌 초고속 인터넷 인프라에 대한 공공 투자는 소외된 지역사회에 교육 및 금융 자원을 ________하는 데 도움을 줌으로써 지역 상업을 직접적으로 자극한다.",
            "disseminate", ["withhold", "confiscate", "suppress"],
            [("disseminate", "보급하다, 전파하다 (v.)"), ("withhold", "보류하다 (v.)"), ("confiscate", "압수하다 (v.)"), ("suppress", "억압하다 (v.)")],
            "인프라가 자원을 '보급하고 확산한다(disseminate)'가 타당합니다."
        ),
        (
            "Classical Literature", "보편적 공감 (Universal Resonance)",
            "timeless themes of grief, hubris, and moral reconciliation transcend historical eras", "시대를 초월한 주제 → 고전 문학의 지속적 생명력(+)",
            "The tragic plays of Sophocles continue to ________ contemporary audiences because their exploration of human hubris and moral anguish remains universally relevant.",
            "소포클레스의 비극들은 인간의 오만과 도덕적 고뇌에 대한 탐구가 보편적인 타당성을 지니기 때문에 현대 관객들에게 계속해서 ________을 준다.",
            "resonate with", ["alienate", "repulse", "disenchant"],
            [("resonate with", "~에게 깊은 울림을 주다 (v.)"), ("alienate", "소외시키다 (v.)"), ("repulse", "혐오감을 주다 (v.)"), ("disenchant", "환멸을 느끼게 하다 (v.)")],
            "보편적 타당성(universally relevant) 때문에 관객에게 '깊은 울림을 준다(resonate with)'가 정답입니다."
        ),
        (
            "Meteorology", "관측 장비 발전 (Sensory Advancement)",
            "Doppler radar and satellite telemetry improve warning accuracy", "관측 장비 정밀화 → 폭풍 예측 오차 축소(+)",
            "Advances in satellite telemetry and high-resolution radar systems have enabled meteorologists to ________ prediction errors regarding severe hurricane trajectories.",
            "위성 원격 측정과 고해상도 레이더 시스템의 발전은 기상학자들이 심각한 허리케인 경로에 관한 예측 오차를 ________할 수 있게 해주었다.",
            "minimize", ["magnify", "escalate", "perpetuate"],
            [("minimize", "최소화하다 (v.)"), ("magnify", "확대하다 (v.)"), ("escalate", "증대시키다 (v.)"), ("perpetuate", "영속시키다 (v.)")],
            "기술 발전으로 예측 오차를 '최소화하다(minimize)'가 정답입니다."
        ),
        # 21..30
        (
            "Immunology", "백신 작용 원리 (Vaccine Mechanism)",
            "mRNA technology instructs ribosomes to produce target spike proteins", "항원 단백질 생성 지시 → 항체 형성 유도(+)",
            "By presenting an inert viral protein to the adaptive immune system, the vaccine trains lymphocytes to ________ neutralizing antibodies prior to actual viral exposure.",
            "적응 면역계에 비활성 바이러스 단백질을 제시함으로써, 백신은 림프구가 실제 바이러스 노출 이전에 중화 항체를 ________하도록 훈련시킨다.",
            "synthesize", ["eradicate", "degrade", "suppress"],
            [("synthesize", "합성하다, 만들어내다 (v.)"), ("eradicate", "근절하다 (v.)"), ("degrade", "분해하다 (v.)"), ("suppress", "억제하다 (v.)")],
            "면역계가 항체를 '생성/합성한다(synthesize)'가 과학적 사실에 부합합니다."
        ),
        (
            "Philosophy of Science", "반증 가능성 (Falsifiability)",
            "Karl Popper argued that scientific theories must be capable of empirical refutation", "반증 가능해야 과학적 가설 성립",
            "According to Karl Popper, a theoretical statement cannot be considered genuinely scientific unless it is inherently susceptible to empirical tests that could ________ it.",
            "칼 포퍼에 따르면, 이론적 진술은 그것을 ________할 수 있는 경험적 검증에 본질적으로 취약하지 않은 한 진정으로 과학적인 것으로 간주될 수 없다.",
            "falsify", ["validate", "canonize", "substantiate"],
            [("falsify", "반증하다, 오류를 증명하다 (v.)"), ("validate", "입증하다 (v.)"), ("canonize", "정경으로 인정하다 (v.)"), ("substantiate", "실증하다 (v.)")],
            "포퍼의 반증주의 원리: 과학적 가설은 관측에 의해 '반증(falsify)'될 가능성을 열어두어야 합니다."
        ),
        (
            "Geopolitical Strategy", "외교적 억지력 (Deterrence)",
            "mutual defense pacts increase the potential cost of unprovoked aggression", "상호방위조약 → 군사적 도발 억제(+)",
            "The establishment of a multilateral defense alliance is primarily designed to ________ prospective adversaries from initiating unilateral military adventurism.",
            "다자간 방위 동맹의 수립은 주로 잠재적 적국이 일방적인 군사적 모험주의를 감행하지 못하도록 ________하기 위해 고안되었다.",
            "deter", ["provoke", "incite", "galvanize"],
            [("deter", "단념시키다, 저지하다 (v.)"), ("provoke", "도발하다 (v.)"), ("incite", "선동하다 (v.)"), ("galvanize", "자극하다 (v.)")],
            "군사적 모험을 하지 못하도록 '저지하다(deter)'가 외교 안보의 핵심 논리입니다."
        ),
        (
            "Hydrology", "삼림 보호와 수자원 (Watershed Protection)",
            "root systems retain topsoil and filter heavy rainfall naturally", "수목 뿌리의 토양 보전 → 산사태 및 탁수 방지(+)",
            "Undisturbed montane forests play an indispensable ecological role because their dense root structures ________ soil erosion and stabilize vulnerable watersheds during torrential rains.",
            "훼손되지 않은 산악 산림은 울창한 뿌리 구조가 집중호우 동안 토양 침식을 ________하고 취약한 분수계를 안정시키기 때문에 필수적인 생태학적 역할을 수행한다.",
            "mitigate", ["exacerbate", "catalyze", "instigate"],
            [("mitigate", "완화하다, 경감하다 (v.)"), ("exacerbate", "악화시키다 (v.)"), ("catalyze", "촉진하다 (v.)"), ("instigate", "유발하다 (v.)")],
            "뿌리가 침식을 '완화한다(mitigate)'가 생태학적으로 옳습니다."
        ),
        (
            "Labor Economics", "자동화와 노동 전환 (Automation & Re-skilling)",
            "generative AI automates repetitive administrative procedures", "반복 사무 자동화 → 고숙련 직무 재교육 수요 증대",
            "As robotic process automation absorbs routine clerical duties, corporations must actively invest in worker retraining to ________ the human workforce for complex analytical roles.",
            "로봇 프로세스 자동화가 일상적인 사무 업무를 흡수함에 따라, 기업들은 복잡한 분석적 직무를 위해 인력을 ________할 수 있도록 근로자 재교육에 적극적으로 투자해야 한다.",
            "equip", ["disqualify", "handicap", "marginalize"],
            [("equip", "역량을 갖추게 하다 (v.)"), ("disqualify", "실격시키다 (v.)"), ("handicap", "불리하게 하다 (v.)"), ("marginalize", "소외시키다 (v.)")],
            "새로운 분석 직무를 수행할 수 있도록 인력을 '무장시키고 역량을 갖추게 하다(equip)'가 적합합니다."
        ),
        (
            "Evolutionary Biology", "환경 적응 (Adaptive Morphology)",
            "thick subcutaneous blubber insulates arctic mammals against subzero temperatures", "두꺼운 지방층 → 혹한 속 체온 유지(+)",
            "The substantial layer of subcutaneous blubber found in cetaceans and pinnipeds serves primarily to ________ internal body heat against freezing polar waters.",
            "고래류와 기각류에서 발견되는 상당한 두께의 피하 지방층은 주로 차가운 극지방 바닷물에 맞서 체내 열을 ________하는 역할을 한다.",
            "conserve", ["dissipate", "discharge", "vent"],
            [("conserve", "보존하다, 유지하다 (v.)"), ("dissipate", "소산시키다, 낭비하다 (v.)"), ("discharge", "방출하다 (v.)"), ("vent", "발산하다 (v.)")],
            "지방층이 체온을 잃지 않고 '보존한다(conserve)'가 정답입니다."
        ),
        (
            "Sociology of Technology", "디지털 격차 (Digital Divide)",
            "unequal access to high-speed internet widens socioeconomic stratification", "인터넷 접근 불평등 → 교육 격차 심화(-)",
            "Disparities in home broadband connectivity among school-aged children threaten to ________ existing socioeconomic achievement gaps between affluent and underserved districts.",
            "학령기 아동들 사이의 가정용 초고속 인터넷 연결 격차는 부유한 지역과 소외된 지역 사이의 기존 사회경제적 학업 격차를 ________할 위험이 있다.",
            "widen", ["narrow", "bridge", "alleviate"],
            [("widen", "넓히다, 심화시키다 (v.)"), ("narrow", "좁히다 (v.)"), ("bridge", "다리를 놓다 (v.)"), ("alleviate", "완화하다 (v.)")],
            "디지털 격차가 기존의 학업 격차를 더욱 '벌어지게 만든다(widen)'가 자연스럽습니다."
        ),
        (
            "Biochemistry", "효소 촉매 작용 (Enzymatic Catalysis)",
            "enzymes lower the activation energy required for biochemical reactions", "활성화 에너지 감소 → 생화학 반응 속도 증진(+)",
            "Biological catalysts known as enzymes operate by drastically lowering the activation energy barrier, which serves to ________ chemical reactions that would otherwise proceed imperceptibly.",
            "효소로 알려진 생물학적 촉매는 활성화 에너지 장벽을 대폭 낮춤으로써 작동하며, 이는 그렇지 않았다면 감지할 수 없을 만큼 느리게 진행되었을 화학 반응을 ________하는 역할을 한다.",
            "expedite", ["retard", "quench", "thwart"],
            [("expedite", "촉진하다, 빠르게 하다 (v.)"), ("retard", "지연시키다 (v.)"), ("quench", "소멸시키다 (v.)"), ("thwart", "좌절시키다 (v.)")],
            "촉매는 반응 속도를 '신속하게 촉진한다(expedite)'가 기본 생화학 원리입니다."
        ),
        (
            "Urban Transport", "대중교통 전용차로 (Bus Rapid Transit)",
            "dedicated bus lanes bypass congested private vehicular corridors", "전용차선 구축 → 출퇴근 소요시간 단축(+)",
            "The implementation of dedicated bus rapid transit corridors has been shown to noticeably ________ average commuting times for dense metropolitan workforces.",
            "간선급행버스(BRT) 전용 차로의 도입은 밀집된 대도시 통근자들의 평균 통근 시간을 눈에 띄게 ________하는 것으로 나타났다.",
            "curtail", ["elongate", "protract", "compound"],
            [("curtail", "단축하다, 줄이다 (v.)"), ("elongate", "늘이다 (v.)"), ("protract", "연장하다 (v.)"), ("compound", "악화시키다 (v.)")],
            "교통 정체를 우회하므로 통근 시간을 '단축한다(curtail)'가 맞습니다."
        ),
        (
            "Constitutional Law", "사법부의 독립 (Judicial Independence)",
            "lifetime judicial tenure shields judges from short-term partisan pressures", "종신 임기 보장 → 정치적 외압 차단(+)",
            "Guaranteed tenure during good behavior is considered vital to judicial independence because it ________ federal magistrates from retaliatory political interference.",
            "품행 유지 기간 동안의 종신 임기 보장은 연방 판사들을 보복성 정치적 간섭으로부터 ________하기 때문에 사법 독립에 필수적인 것으로 간주된다.",
            "insulates", ["exposes", "subjugates", "indicts"],
            [("insulates", "절연하다, 보호하다 (v.)"), ("exposes", "노출시키다 (v.)"), ("subjugates", "복종시키다 (v.)"), ("indicts", "기소하다 (v.)")],
            "정치적 외압으로부터 판사를 '보호하고 차단한다(insulates from)'가 헌법적 원리입니다."
        ),
        # 31..40
        (
            "Public Finance", "인플레이션 조세 (Inflationary Pressure)",
            "excessive unbacked monetary expansion diminishes purchasing power", "통화량 무분별한 팽창 → 화폐 구매력 하락(-)",
            "When a central bank excessively expands the money supply without corresponding growth in goods, it inevitably serves to ________ the real purchasing power of the national currency.",
            "중앙은행이 재화의 상응하는 성장 없이 통화량을 과도하게 팽창시킬 때, 이는 불가피하게 자국 통화의 실질 구매력을 ________시키는 역할을 한다.",
            "erode", ["reinforce", "elevate", "buttress"],
            [("erode", "침식하다, 갉아먹다 (v.)"), ("reinforce", "강화하다 (v.)"), ("elevate", "높이다 (v.)"), ("buttress", "지지하다 (v.)")],
            "과도한 통화 공급은 구매력을 '침식/저하시킨다(erode)'가 맞습니다."
        ),
        (
            "Agronomy & Soil Ecology", "과도한 경작과 사막화 (Soil Degradation)",
            "intensive tilling strips topsoil of organic moisture and microflora", "과도한 쟁기질 → 농지 생산성 황폐화(-)",
            "Centuries of intensive monoculture and mechanical deep tilling have severely ________ arable topsoil, turning once-fertile plains into vulnerable semi-arid scrublands.",
            "수세기에 걸친 집약적 단일 경작과 기계화된 깊은 쟁기질은 경작 가능한 표토를 심각하게 ________하여, 한때 비옥했던 평야를 취약한 반건조 관목지로 변화시켰다.",
            "depleted", ["enriched", "invigorated", "fortified"],
            [("depleted", "고갈된, 소모된 (adj.)"), ("enriched", "풍요로운 (adj.)"), ("invigorated", "활력 넘치는 (adj.)"), ("fortified", "강화된 (adj.)")],
            "비옥한 땅이 황폐해졌으므로 영양분이 '고갈되었다(depleted)'가 정답입니다."
        ),
        (
            "Cognitive Development", "유아기 언어 노출 (Linguistic Scaffolding)",
            "frequent interactive vocal exchanges stimulate synaptic networks", "언어 상호작용 빈도 증대 → 어휘 습득 가속(+)",
            "Child psychology studies show that consistent parental verbal interaction during infancy serves to drastically ________ early vocabulary acquisition and syntactic fluency.",
            "아동 심리학 연구에 따르면 영아기 동안 부모의 지속적인 언어적 상호작용은 초기 어휘 습득과 구문적 유창성을 극적으로 ________하는 역할을 한다.",
            "accelerate", ["retard", "inhibit", "dampen"],
            [("accelerate", "가속화하다 (v.)"), ("retard", "지체시키다 (v.)"), ("inhibit", "억제하다 (v.)"), ("dampen", "꺾다 (v.)")],
            "상호작용이 언어 습득을 '가속화한다(accelerate)'가 맞습니다."
        ),
        (
            "Historical Linguistics", "고립어의 보존 (Isolated Languages)",
            "geographical barriers like impassable mountain chains prevent linguistic admixture", "지리적 고립 → 고유 어휘 보존(+)",
            "The rugged topography of the Pyrenees historically served to ________ the Basque language from assimilative Romance linguistic influences for over two millennia.",
            "피레네산맥의 험준한 지형은 역사적으로 바스크어가 2천 년 이상 동화적인 로맨스어계의 언어적 영향으로부터 ________되도록 보호하는 역할을 했다.",
            "shield", ["expose", "subjugate", "amalgamate"],
            [("shield", "보호하다, 차단하다 (v.)"), ("expose", "노출시키다 (v.)"), ("subjugate", "예속시키다 (v.)"), ("amalgamate", "융합하다 (v.)")],
            "험준한 지형이 외부 영향을 막아 언어를 '보호했다(shield)'가 타당합니다."
        ),
        (
            "Behavioral Genetics", "쌍둥이 연구 (Monozygotic Twins)",
            "identical twins separated at birth share striking psychological parallels", "유전적 일치도 → 성격 형성에 유전 영향 입증(+)",
            "Rigorous twin adoption studies have provided empirical data that ________ the substantial role of hereditary factors in shaping human personality traits.",
            "엄격한 입양 쌍둥이 연구들은 인간의 성격 특성을 형성하는 데 유전적 요인이 지닌 상당한 역할을 ________하는 실증적 데이터를 제공해 왔다.",
            "corroborate", ["disprove", "debunk", "repudiate"],
            [("corroborate", "확증하다, 뒷받침하다 (v.)"), ("disprove", "반증하다 (v.)"), ("debunk", "틀렸음을 밝히다 (v.)"), ("repudiate", "부인하다 (v.)")],
            "데이터가 유전적 역할을 '확증한다(corroborate)'가 논리적입니다."
        ),
        (
            "Aviation Engineering", "공기역학적 항력 감소 (Aerodynamic Streamlining)",
            "smooth blended winglets reduce vortex wake and fuel burn", "익단 장치 장착 → 연료 소비 절감(+)",
            "Airlines routinely install curved winglets at the tips of jet wings because they reduce aerodynamic drag and noticeably ________ long-haul fuel consumption.",
            "항공사들은 제트기 날개 끝에 곡면 윙렛을 일상적으로 장착하는데, 그 이유는 공기역학적 항력을 줄이고 장거리 연료 소비를 눈에 띄게 ________하기 때문이다.",
            "curb", ["inflate", "escalate", "propagate"],
            [("curb", "억제하다, 줄이다 (v.)"), ("inflate", "부풀리다 (v.)"), ("escalate", "증가시키다 (v.)"), ("propagate", "확산하다 (v.)")],
            "항력을 줄여 연료 소비를 '줄인다(curb)'가 기술적 사실입니다."
        ),
        (
            "Ethnomusicology", "구전 전통의 보존 (Oral Traditions)",
            "indigenous story songs codify ancestral survival skills across generations", "노래를 통한 지식 전달 → 생태 지혜 보존(+)",
            "Among nomadic hunter-gatherer societies, mnemonic folk melodies functioned as vital cognitive archives designed to ________ navigational routes across featureless desert terrain.",
            "유목 수렵 채집 사회에서 기억을 돕는 민요 멜로디는 특징 없는 사막 지형을 가로지르는 항해 경로를 ________하도록 고안된 중요한 인지적 기록물로 기능했다.",
            "preserve", ["obliterate", "erase", "confound"],
            [("preserve", "보존하다 (v.)"), ("obliterate", "지우다 (v.)"), ("erase", "삭제하다 (v.)"), ("confound", "어지럽히다 (v.)")],
            "기록물로서 길을 '보존하고 후대에 전수한다(preserve)'가 맞습니다."
        ),
        (
            "Renewable Technology", "스마트 그리드 전력망 (Smart Grid Efficiency)",
            "automated load balancing prevents catastrophic voltage overloads", "자동 부하 분산 → 전력망 정전 예방(+)",
            "The incorporation of automated micro-inverters into local energy grids helps to ________ localized blackouts by redistributing surplus power instantaneously.",
            "지역 에너지 전력망에 자동화된 마이크로 인버터를 통합하는 것은 잉여 전력을 즉각적으로 재분배함으로써 국지적인 정전을 ________하는 데 도움을 준다.",
            "avert", ["precipitate", "catalyze", "instigate"],
            [("avert", "방지하다, 피하다 (v.)"), ("precipitate", "촉발하다 (v.)"), ("catalyze", "촉진하다 (v.)"), ("instigate", "일으키다 (v.)")],
            "잉여 전력을 나누어 정전을 '방지한다(avert)'가 자연스럽습니다."
        ),
        (
            "Forestry Ecology", "통제된 소각 (Controlled Burns)",
            "periodic low-intensity brush clearing prevents megafires", "주기적 잔가지 소각 → 대형 산불 예방(+)",
            "Forest rangers regularly conduct controlled prescribed burns to remove dry detritus, thereby helping to ________ catastrophic infernos that could destroy mature timber canopy.",
            "산림 관리관들은 마른 잔해를 제거하기 위해 정기적으로 계획된 통제 소각을 실시하며, 이를 통해 성숙한 수관(나뭇가지 층)을 파괴할 수 있는 대참사 산불을 ________하는 데 도움을 준다.",
            "preempt", ["ignite", "fuel", "amplify"],
            [("preempt", "미연에 방지하다 (v.)"), ("ignite", "점화하다 (v.)"), ("fuel", "부채질하다 (v.)"), ("amplify", "증폭시키다 (v.)")],
            "대형 화재를 '사전에 차단/예방한다(preempt)'가 정답입니다."
        ),
        (
            "Consumer Psychology", "희소성 마케팅 (Scarcity Principle)",
            "limited-edition countdown clocks provoke panic buying", "시간 제한 알림 → 구매 욕구 자극(+)",
            "E-commerce platforms frequently employ countdown timers and dwindling inventory alerts to ________ a sense of urgency that impels immediate purchase.",
            "전자상거래 플랫폼은 즉각적인 구매를 유도하는 긴박감을 ________하기 위해 카운트다운 타이머와 줄어드는 재고 알림을 자주 활용한다.",
            "evoke", ["quell", "stifle", "extinguish"],
            [("evoke", "불러일으키다, 자아내다 (v.)"), ("quell", "진압하다 (v.)"), ("stifle", "억누르다 (v.)"), ("extinguish", "소멸시키다 (v.)")],
            "긴박감을 소비자 마음에 '불러일으킨다(evoke)'가 가장 알맞습니다."
        ),
        # 41..50
        (
            "Macroeconomics", "중앙은행 금리 인상 (Monetary Tightening)",
            "raising overnight benchmark rates discourages speculative borrowing", "금리 인상 → 과열 경기 진정(+)",
            "In an effort to cool an overheated economy and tame stubborn inflation, the central bank made the decisive choice to ________ commercial borrowing costs.",
            "과열된 경제를 식히고 완고한 인플레이션을 길들이기 위한 노력의 일환으로, 중앙은행은 상업 대출 비용을 ________하기로 단호한 결정을 내렸다.",
            "elevate", ["slash", "subsidize", "undermine"],
            [("elevate", "인상하다, 높이다 (v.)"), ("slash", "대폭 삭감하다 (v.)"), ("subsidize", "보조금을 주다 (v.)"), ("undermine", "약화시키다 (v.)")],
            "과열을 잡기 위해 대출 비용(금리)을 '인상하다(elevate)'가 맞습니다."
        ),
        (
            "Cellular Biology", "세포 사멸 (Apoptosis)",
            "programmed cell death removes mutagenic cells before malignancy", "손상 세포 자살 → 암 발생 차단(+)",
            "Apoptosis, or programmed cellular suicide, is an indispensable biological safeguard that operates to ________ damaged cells before they can replicate mutations.",
            "아포토시스, 즉 프로그램화된 세포 자살은 돌연변이를 복제하기 전에 손상된 세포를 ________하도록 작동하는 필수적인 생물학적 안전장치이다.",
            "eliminate", ["proliferate", "propagate", "preserve"],
            [("eliminate", "제거하다, 없애다 (v.)"), ("proliferate", "증식시키다 (v.)"), ("propagate", "번식시키다 (v.)"), ("preserve", "보존하다 (v.)")],
            "손상된 세포를 '제거한다(eliminate)'가 세포 자살의 핵심 기능입니다."
        ),
        (
            "Civil Engineering", "지진 완충 장치 (Seismic Base Isolation)",
            "elastomeric bearings decouple building foundation from ground shaking", "탄성 받침대 → 지진 충격 흡수(+)",
            "Modern skyscrapers constructed on active tectonic fault lines utilize seismic base isolators to ________ kinetic shockwaves during violent earthquakes.",
            "활성 지진 단층대 위에 건설된 현대 초고층 빌딩들은 격렬한 지진이 발생하는 동안 운동 충격파를 ________하기 위해 내진 기초 절연 장치를 활용한다.",
            "absorb", ["magnify", "escalate", "propagate"],
            [("absorb", "흡수하다, 완충하다 (v.)"), ("magnify", "확대하다 (v.)"), ("escalate", "증대시키다 (v.)"), ("propagate", "전파하다 (v.)")],
            "충격파를 '흡수/완충한다(absorb)'가 맞습니다."
        ),
        (
            "Medical Epidemiology", "백신 저온 유통망 (Cold Chain Integrity)",
            "unbroken refrigeration prevents vaccine protein denaturing", "콜드체인 유지 → 백신 효능 보존(+)",
            "Maintaining an unbroken cold chain from the factory to rural clinics is essential to ________ the antigenic efficacy of temperature-sensitive viral vaccines.",
            "공장에서 농촌 진료소까지 끊김 없는 저온 유통망(콜드체인)을 유지하는 것은 온도에 민감한 바이러스 백신의 항원 효능을 ________하는 데 필수적이다.",
            "sustain", ["compromise", "sabotage", "degrade"],
            [("sustain", "유지하다, 보존하다 (v.)"), ("compromise", "손상시키다 (v.)"), ("sabotage", "파괴하다 (v.)"), ("degrade", "저하시키다 (v.)")],
            "효능이 떨어지지 않게 '유지하다(sustain)'가 자연스럽습니다."
        ),
        (
            "Cognitive Linguistics", "개념적 은유 (Conceptual Metaphor)",
            "abstract ideas are grounded in physical bodily experiences", "신체적 경험 비유 → 추상적 개념 이해 촉진(+)",
            "Linguists argue that metaphorical mapping serves to ________ abstract philosophical concepts by tethering them to concrete sensorimotor experiences.",
            "언어학자들은 은유적 사상(mapping)이 추상적인 철학적 개념을 구체적인 감각운동 경험에 결속시킴으로써 그것들을 ________하는 역할을 한다고 주장한다.",
            "elucidate", ["obfuscate", "confound", "shroud"],
            [("elucidate", "명료하게 설명하다, 밝히다 (v.)"), ("obfuscate", "애매하게 만들다 (v.)"), ("confound", "혼동시키다 (v.)"), ("shroud", "가리다 (v.)")],
            "추상적인 것을 구체적 경험과 연결하여 '명확히 밝힌다(elucidate)'가 맞습니다."
        ),
        (
            "Optics & Astronomy", "적응 광학 (Adaptive Optics)",
            "deformable mirrors correct atmospheric twinkling in real time", "거울 변형 보정 → 천체 망원경 해상도 극대화(+)",
            "Ground-based astronomical observatories install adaptive optics systems that continuously distort flexible mirrors to ________ atmospheric blur and sharpen faint star images.",
            "지상 천문대는 대기 흔들림으로 인한 흐림 현상을 ________하고 희미한 별 이미지를 선명하게 하기 위해 유연한 거울을 지속적으로 변형시키는 적응 광학 시스템을 설치한다.",
            "rectify", ["exacerbate", "induce", "compound"],
            [("rectify", "바로잡다, 교정하다 (v.)"), ("exacerbate", "악화시키다 (v.)"), ("induce", "유발하다 (v.)"), ("compound", "가중시키다 (v.)")],
            "대기 왜곡을 '바로잡다/교정하다(rectify)'가 정답입니다."
        ),
        (
            "Anthropology", "사회적 의례 (Ritual Solidarity)",
            "communal rites of passage reaffirm collective norms during crisis", "공동 의례 거행 → 사회적 연대감 재확인(+)",
            "Anthropologists have shown that seasonal collective rituals serve primarily to ________ communal bonds and reaffirm shared moral values during periods of environmental stress.",
            "인류학자들은 계절별 집단 의례가 환경적 스트레스 기간 동안 공동체적 유대를 ________하고 공유된 도덕적 가치를 재확인하는 역할을 주로 한다고 입증해 왔다.",
            "solidify", ["disintegrate", "fracture", "subvert"],
            [("solidify", "공고히 하다, 굳히다 (v.)"), ("disintegrate", "해체하다 (v.)"), ("fracture", "균열을 내다 (v.)"), ("subvert", "전복하다 (v.)")],
            "유대를 '공고히 다진다(solidify)'가 정답입니다."
        ),
        (
            "Genetics", "DNA 교정 효소 (DNA Polymerase Proofreading)",
            "exonuclease proofreading fixes base-pair mismatches during replication", "DNA 교정 효소 작동 → 유전 변이율 최소화(+)",
            "The proofreading capability inherent in DNA polymerases is remarkably effective at ________ replication errors that could otherwise trigger lethal genomic mutations.",
            "DNA 중합효소에 내재된 교정 판독 기능은 자칫 치명적인 유전체 돌연변이를 촉발할 수 있는 복제 오류를 ________하는 데 현저히 효과적이다.",
            "rectifying", ["initiating", "magnifying", "fostering"],
            [("rectifying", "바로잡는, 수정하는 (v.)"), ("initiating", "시작하는 (v.)"), ("magnifying", "확대하는 (v.)"), ("fostering", "조성하는 (v.)")],
            "복제 오류를 교정하므로 '바로잡는다(rectifying)'가 맞습니다."
        ),
        (
            "Agricultural Economics", "농작물 보험 (Crop Insurance)",
            "guaranteed payouts shield farmers from extreme climate shocks", "보험 보상 → 농가 파산 위험 방지(+)",
            "Government-subsidized agricultural insurance policies are designed to ________ smallholder farmers from catastrophic financial insolvency caused by unseasonal droughts.",
            "정부 보조 농업 보험 정책은 소규모 농가들이 때아닌 가뭄으로 인한 파국적인 재정적 파산으로부터 ________되도록 보호하기 위해 고안되었다.",
            "shield", ["expose", "imperil", "destabilize"],
            [("shield", "보호하다 (v.)"), ("expose", "노출시키다 (v.)"), ("imperil", "위태롭게 하다 (v.)"), ("destabilize", "불안정하게 하다 (v.)")],
            "파산 위협으로부터 농가를 '보호하다(shield)'가 타당합니다."
        ),
        (
            "Information Theory", "오류 정정 부호 (Error-Correcting Codes)",
            "redundant parity bits restore signal parity across noisy channels", "패리티 비트 추가 → 통신 왜곡 복구(+)",
            "In deep-space communications, engineers embed mathematical redundancy into digital signals to reliably ________ corrupted packets intercepted by cosmic radiation.",
            "심우주 통신에서 엔지니어들은 우주 방사선에 의해 손상된 데이터 패킷을 안정적으로 ________하기 위해 디지털 신호에 수학적 잉여성을 내장한다.",
            "reconstruct", ["obliterate", "jumble", "erase"],
            [("reconstruct", "재구성하다, 복원하다 (v.)"), ("obliterate", "지우다 (v.)"), ("jumble", "뒤섞다 (v.)"), ("erase", "삭제하다 (v.)")],
            "손상된 패킷을 '복원하다(reconstruct)'가 맞습니다."
        ),
        # 51..60
        (
            "Ecology", "핵심종의 역할 (Keystone Species)",
            "sea otters control sea urchin densities, allowing kelp forests to flourish", "핵심종의 초식동물 억제 → 해양 숲 번성(+)",
            "The reintroduction of apex sea otters to coastal bays served to ________ the proliferation of destructive sea urchins, thereby restoring flourishing underwater kelp canopies.",
            "연안 만에 최상위 포식자인 해달을 재도입한 것은 파괴적인 성게의 급증을 ________하는 역할을 했으며, 그에 따라 번성하는 수중 다시마 숲을 복원시켰다.",
            "quell", ["provoke", "foster", "compound"],
            [("quell", "진압하다, 억제하다 (v.)"), ("provoke", "유발하다 (v.)"), ("foster", "조성하다 (v.)"), ("compound", "악화시키다 (v.)")],
            "성게의 폭발적 증식을 '억제하다/잠재우다(quell)'가 생태학적 정답입니다."
        ),
        (
            "Neurobiology of Sleep", "수면과 글림프계 (Glymphatic Clearance)",
            "cerebrospinal fluid flushes beta-amyloid plaques during deep slow-wave sleep", "깊은 수면 → 독성 노폐물 배출(+)",
            "During deep slow-wave sleep, the glymphatic system markedly increases fluid exchange to ________ toxic metabolic byproducts that accumulate throughout waking consciousness.",
            "깊은 서파 수면 동안, 글림프계는 깨어 있는 의식 동안 축적되는 독성 대사 부산물을 ________하기 위해 체액 교환을 현저하게 증가시킨다.",
            "purge", ["amass", "synthesize", "retain"],
            [("purge", "제거하다, 깨끗이 배출하다 (v.)"), ("amass", "축적하다 (v.)"), ("synthesize", "합성하다 (v.)"), ("retain", "보유하다 (v.)")],
            "독성 노폐물을 몸 밖으로 '깨끗이 배출/제거하다(purge)'가 과학적 사실입니다."
        ),
        (
            "Legal Jurisprudence", "선례 구속의 원칙 (Stare Decisis)",
            "adhering to historical precedents ensures predictability in statutory interpretation", "선례 존중 원칙 → 법적 예측 가능성 보장(+)",
            "The judicial doctrine of stare decisis encourages appellate courts to honor established legal precedents in order to ________ stability and public trust in statutory governance.",
            "선례 구속의 사법 원칙은 성문법 통치에 대한 안정성과 대중의 신뢰를 ________하기 위해 항소법원이 확립된 법적 선례를 존중하도록 권장한다.",
            "preserve", ["subvert", "undermine", "destabilize"],
            [("preserve", "보존하다, 지키다 (v.)"), ("subvert", "전복하다 (v.)"), ("undermine", "약화시키다 (v.)"), ("destabilize", "불안정하게 하다 (v.)")],
            "법적 안정성을 '지키고 보존하다(preserve)'가 정답입니다."
        ),
        (
            "Macroeconomics", "사회간접자본 생산성 (Infrastructure Multiplier)",
            "modernized deep-water ports reduce cargo bottlenecks for exporters", "항만 현대화 → 물류비 절감 및 무역 경쟁력 강화(+)",
            "Capital expenditures directed toward deep-water port modernization have served to ________ maritime shipping bottlenecks, thereby strengthening national export competitiveness.",
            "심수항 현대화에 투입된 자본 지출은 해상 운송 병목 현상을 ________하는 역할을 했으며, 그에 따라 국가 수출 경쟁력을 강화시켰다.",
            "alleviate", ["exacerbate", "provoke", "compound"],
            [("alleviate", "완화하다, 경감하다 (v.)"), ("exacerbate", "악화시키다 (v.)"), ("provoke", "촉발하다 (v.)"), ("compound", "가중시키다 (v.)")],
            "병목 현상(bottlenecks)을 '완화하다(alleviate)'가 맞습니다."
        ),
        (
            "Epidemiology", "정기 상수도 불소화 (Water Fluoridation)",
            "trace fluoridation hardens tooth enamel across population strata", "수돗물 불소 투입 → 충치 발생률 감소(+)",
            "Decades of pediatric epidemiological surveillance confirm that municipal water fluoridation operates to significantly ________ the prevalence of dental caries among socioeconomically disadvantaged youths.",
            "수십 년에 걸친 소아 역학 감시는 도시 수돗물 불소화가 사회경제적으로 취약한 청소년들 사이에서 충치 발병률을 현저하게 ________하도록 작용함을 확인해 준다.",
            "depress", ["escalate", "propagate", "magnify"],
            [("depress", "낮추다, 떨어뜨리다 (v.)"), ("escalate", "증대시키다 (v.)"), ("propagate", "전파하다 (v.)"), ("magnify", "확대하다 (v.)")],
            "충치 발병률을 '낮추다(depress/lower)'가 맞습니다."
        ),
        (
            "Biomimicry", "연꽃잎 방수 효과 (Lotus Effect)",
            "micro-nanostructured wax crystals cause water droplets to roll off freely", "미세 돌기 구조 → 자가 세정 표면 구현(+)",
            "Inspired by the hydrophobic surface of lotus leaves, chemical engineers developed nanostructured coatings that completely ________ water and prevent surface corrosion.",
            "연꽃잎의 소수성 표면에서 영감을 받아, 화학 공학자들은 물을 완전히 ________하고 표면 부식을 방지하는 나노 구조 코팅을 개발했다.",
            "repel", ["absorb", "imbibe", "retain"],
            [("repel", "튕겨내다, 밀어내다 (v.)"), ("absorb", "흡수하다 (v.)"), ("imbibe", "빨아들이다 (v.)"), ("retain", "유지하다 (v.)")],
            "물을 튕겨내므로 '밀어내다(repel)'가 정답입니다."
        ),
        (
            "Renewable Forestry", "선별적 벌목 (Selective Logging)",
            "harvesting individual mature trunks keeps forest canopy intact", "선별 벌목 → 생물다양성 보전(+)",
            "Sustainable forestry certification programs mandate selective thinning rather than clear-cutting to ________ biodiversity and soil integrity in old-growth tropical ecosystems.",
            "지속 가능한 산림 인증 프로그램은 원시 열대 생태계에서 생물 다양성과 토양 보전을 ________하기 위해 개벌(전부 베어내기) 대신 선별적 솎아베기를 의무화한다.",
            "safeguard", ["jeopardize", "ravage", "dismantle"],
            [("safeguard", "보호하다, 지키다 (v.)"), ("jeopardize", "위태롭게 하다 (v.)"), ("ravage", "황폐화하다 (v.)"), ("dismantle", "해체하다 (v.)")],
            "생물다양성을 '보호하다(safeguard)'가 맞습니다."
        ),
        (
            "Cognitive Aging", "외국어 학습의 치매 지연 (Bilingualism & Cognitive Reserve)",
            "managing two linguistic systems builds robust executive control networks", "이중 언어 구사 → 인지 예비능 향상 및 치매 지연(+)",
            "Neurological cohort studies suggest that lifelong bilingualism helps to ________ the clinical onset of dementia symptoms by creating compensatory cognitive reserves.",
            "신경학 코호트 연구에 따르면 평생에 걸친 이중 언어 사용은 보상적 인지 예비능을 형성함으로써 치매 증상의 임상적 발현을 ________하는 데 도움을 준다.",
            "postpone", ["precipitate", "hasten", "instigate"],
            [("postpone", "연기하다, 지연시키다 (v.)"), ("precipitate", "재촉하다 (v.)"), ("hasten", "서두르다 (v.)"), ("instigate", "유발하다 (v.)")],
            "치매 발병을 늦추어 '지연시키다(postpone/delay)'가 맞습니다."
        ),
        (
            "Urban Microclimate", "도시 열섬 완화 (Urban Heat Island)",
            "reflective cool roofs and tree planting reduce ambient surface heat", "반사 지붕과 가로수 식재 → 도시 온도 저감(+)",
            "Metropolitan initiatives advocating reflective white roofs and expanded tree canopies are primarily targeted to ________ dangerous heat dome temperatures during scorching summer heatwaves.",
            "반사성 흰색 지붕과 확장된 나무 그늘을 옹호하는 대도시 계획은 타는 듯한 여름 폭염 동안 위험한 열돔 온도를 ________하는 것을 일차적 목표로 한다.",
            "temper", ["aggravate", "intensify", "compound"],
            [("temper", "완화하다, 조절하다 (v.)"), ("aggravate", "악화시키다 (v.)"), ("intensify", "심화시키다 (v.)"), ("compound", "가중시키다 (v.)")],
            "위험한 온도를 누그러뜨리고 '완화하다(temper)'가 정답입니다."
        ),
        (
            "Microbiology", "항생제 내성 관리 (Antibiotic Stewardship)",
            "restricting unnecessary broad-spectrum prescriptions curbs superbug selection", "불필요한 처방 제한 → 내성균 진화 억제(+)",
            "Hospital stewardship protocols that curtail the frivolous prescription of reserve antibiotics have proven decisive in helping to ________ the emergence of multi-drug-resistant superbugs.",
            "예비 항생제의 무분별한 처방을 억제하는 병원 관리 프로토콜은 다제내성 슈퍼박테리아의 출현을 ________하는 데 기여하는 결정적인 것으로 입증되었다.",
            "quash", ["catalyze", "induce", "accelerate"],
            [("quash", "억제하다, 가라앉히다 (v.)"), ("catalyze", "촉매작용하다 (v.)"), ("induce", "유도하다 (v.)"), ("accelerate", "가속화하다 (v.)")],
            "내성균 출현을 막아 '억제하다(quash)'가 정답입니다."
        )
    ]

    for idx, d in enumerate(data):
        theme, logicType, clue, direction, question, questionKo, correct, distractors, vocab, explanation = d
        opts = [correct] + distractors
        # Shuffle deterministically
        random.seed(1000 + idx)
        random.shuffle(opts)
        ans = opts.index(correct)
        
        vocab_list = [{"word": w, "meaning": m} for w, m in vocab]
        
        items.append({
            "id": f"tl-{idx+1:03d}",
            "level": 1,
            "levelLabel": "Lv.1 기초",
            "theme": theme,
            "category": "단일 빈칸 (Single Blank)",
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
    q = get_level1_questions()
    print(f"Generated {len(q)} Level 1 questions.")
