# -*- coding: utf-8 -*-
"""
Level 3 Generator: 60 Advanced Double-Blank Logic Questions (Lv.3 상급 논리)
Characteristics: Double blank (2빈칸), reciprocal/balanced logical structure, paired choices.
"""
import random

def get_level3_questions():
    items = []
    
    # 60 distinct academic double blank stems
    data = [
        # 1..10
        (
            "Ecology & Agriculture", "인과 / 대구 (Causality & Parallelism)",
            "Because pollinators provide an irreplaceable ecological service... collapse would severely [A]... and trigger [B] disruptions",
            "원인(핵심 수분 매개자 붕괴) → 결과([A] 농작물 타격[-] + [B] 파국적 결과[-])",
            "Because pollinators provide an irreplaceable ecological service to terrestrial flora, their sudden population collapse would severely ________ agricultural yields and trigger ________ disruptions across international commodity markets.",
            "수분 매개자들은 육상 식물군에 대체 불가능한 생태학적 서비스를 제공하기 때문에, 그들의 갑작스러운 개체수 붕괴는 농업 수확량을 심각하게 ________시키고 국제 원자재 시장 전반에 ________ 혼란을 촉발할 것이다.",
            "jeopardize — catastrophic",
            ["bolster — negligible", "proliferate — transient", "stabilize — unprecedented"],
            [("jeopardize", "위태롭게 하다 (v.)"), ("catastrophic", "파국적인, 대참사의 (adj.)"), ("bolster", "강화하다 (v.)"), ("negligible", "하찮은 (adj.)"), ("proliferate", "급증하다 (v.)"), ("transient", "일시적인 (adj.)")],
            "Because와 개체수 붕괴라는 마이너스 원인이 주어졌으므로, [A]와 [B] 모두 심각한 부정적 피해를 의미하는 jeopardize(위태롭게 하다)와 catastrophic(파국적인)이 완벽한 대구를 이룹니다."
        ),
        (
            "Quantum Computing", "양보 / 대조 (Concession & Contrast)",
            "While theoretical quantum algorithms promise exponential advantages, decoherence remains a [A] obstacle that continues to [B] realization",
            "이론적 약속(+) vs 현실적 장애([A] 엄청난 난관[-] + [B] 상용화 방해[-])",
            "While theoretical quantum algorithms promise exponential processing advantages, quantum decoherence remains a ________ obstacle that continues to ________ large-scale commercial realization.",
            "이론적 양자 알고리즘이 기하급수적인 연산상 이점을 약속하지만, 양자 결맞음 상실은 대규모 상용화를 지속적으로 ________하는 ________ 장애물로 남아 있다.",
            "formidable — thwart",
            ["trivial — expedite", "negligible — accelerate", "ephemeral — facilitate"],
            [("formidable", "만만찮은, 가공할 (adj.)"), ("thwart", "좌절시키다, 방해하다 (v.)"), ("trivial", "사소한 (adj.)"), ("expedite", "촉진하다 (v.)"), ("negligible", "무시할 수 있는 (adj.)")],
            "While(양보)을 통해 이론적 이점과 대비되는 현실적 어려움이 와야 하므로, 만만찮은 장애물(formidable obstacle)과 상용화를 가로막는다(thwart)가 정답입니다."
        ),
        (
            "Macroeconomic Monetary Policy", "역접 / 대조 (Contrast)",
            "Far from [A] speculative bubbles, reckless interest rate cuts [B] inflationary pressures",
            "기대 효과([A] 버블 진정) ↔ 실제 역효과([B] 인플레이션 악화)",
            "Far from ________ speculative market volatility, the central bank's abrupt benchmark rate reduction merely served to ________ runaway inflationary expectations across the real estate sector.",
            "투기적 시장 변동성을 ________하기는커녕, 중앙은행의 급작스러운 기준금리 인하는 부동산 부문 전반에 걸쳐 걷잡을 수 없는 인플레이션 기대를 ________하는 역할만을 했다.",
            "dampening — exacerbate",
            ["escalating — mitigate", "fueling — appease", "magnifying — assuage"],
            [("dampening", "가라앉히는, 꺾는 (v./adj.)"), ("exacerbate", "악화시키다 (v.)"), ("escalating", "증대시키는 (adj.)"), ("mitigate", "완화하다 (v.)"), ("appease", "달래다 (v.)")],
            "Far from [A](~하기는커녕)와 merely served to [B](오히려 악화시켰다)의 구조이므로, 진정시키기는커녕(dampening) 악화시켰다(exacerbate)가 맞습니다."
        ),
        (
            "Developmental Psychology & Literacy", "상보 / 인과 (Complementarity & Causality)",
            "Parents who [A] interactive dialogue can [B] language development",
            "긍정적 양육([A] 대화 장려) → 결과([B] 언어 지연 예방)",
            "Caregivers who actively ________ verbal discourse during early childhood can substantially ________ the risk of developmental communicative delays in later schooling.",
            "유아기 동안 언어적 대화를 적극적으로 ________하는 양육자들은 이후 학령기에 발달상의 의사소통 지연 위험을 실질적으로 ________할 수 있다.",
            "encourage — mitigate",
            ["suppress — eliminate", "inhibit — aggravate", "disregard — compound"],
            [("encourage", "장려하다 (v.)"), ("mitigate", "완화하다 (v.)"), ("suppress", "억압하다 (v.)"), ("inhibit", "저해하다 (v.)"), ("disregard", "무시하다 (v.)")],
            "대화를 적극 권장하고(encourage) 위험을 줄인다(mitigate)가 논리적 짝을 이룹니다."
        ),
        (
            "Evolutionary Anthropology", "통념 반박 (Counter-intuition)",
            "Rather than being [A] beasts, hominids showed [B] cooperation",
            "통념([A] 야만적인) ↔ 실제([B] 이타적인)",
            "Rather than being the ________ brutes envisioned by Victorian sociologists, early hominids exhibited complex patterns of food sharing and ________ medical care for disabled elders.",
            "빅토리아 시대 사회학자들이 상상했던 ________ 야수들이기보다는, 초기 인류는 장애가 있는 노인들에 대한 복잡한 음식 공유와 ________ 의료 돌봄 패턴을 보여주었다.",
            "ferocious — compassionate",
            ["benevolent — callous", "docile — predatory", "amiable — brutal"],
            [("ferocious", "사나운, 잔혹한 (adj.)"), ("compassionate", "연민 어린, 자비로운 (adj.)"), ("benevolent", "자애로운 (adj.)"), ("callous", "냉담한 (adj.)"), ("docile", "온순한 (adj.)")],
            "사나운 야수(ferocious brutes)가 아니라 연민 어린 돌봄(compassionate care)을 베풀었다는 대조입니다."
        ),
        (
            "Environmental Ecology", "인과 / 상보 (Reciprocal Degradation)",
            "Deforestation not only [A] soil stability but also [B] carbon emissions",
            "이중 피해([A] 토양 침식 초래 + [B] 온실가스 배출 증폭)",
            "Widespread deforestation in the Amazon basin not only ________ regional hydrologic equilibrium, but also ________ atmospheric carbon dioxide concentrations on an unprecedented scale.",
            "아마존 유역의 광범위한 삼림 벌채는 지역의 수문학적 평형을 ________할 뿐만 아니라, 대기 중 이산화탄소 농도를 전례 없는 규모로 ________한다.",
            "destabilizes — elevates",
            ["fortifies — depresses", "reconstitutes — diminishes", "preserves — curtails"],
            [("destabilizes", "불안정하게 하다 (v.)"), ("elevates", "높이다 (v.)"), ("fortifies", "강화하다 (v.)"), ("depresses", "낮추다 (v.)"), ("reconstitutes", "재구성하다 (v.)")],
            "not only [A] but also [B]의 순접 심화 구조로, 평형을 흔들고(destabilizes) 탄소 농도를 높인다(elevates)가 일치합니다."
        ),
        (
            "Philosophy of Science", "이론과 관측의 불일치 (Theoretical Anomaly)",
            "When observed phenomena [A] mathematical predictions, scientists must [B] their premises",
            "조건([A] 예측 위배/모순) → 귀결([B] 전제 수정/재평가)",
            "When experimental observations consistently ________ established theoretical models, empirical researchers are compelled to ________ their foundational cosmological axioms.",
            "실험 관측이 기존의 확립된 이론 모델과 지속적으로 ________할 때, 실증 연구자들은 그들의 근본적인 우주론적 공리들을 ________하지 않을 수 없게 된다.",
            "contradict — revise",
            ["corroborate — abandon", "affirm — repudiate", "substantiate — discard"],
            [("contradict", "모순되다, 반박하다 (v.)"), ("revise", "수정하다 (v.)"), ("corroborate", "확증하다 (v.)"), ("affirm", "단언하다 (v.)"), ("substantiate", "실증하다 (v.)")],
            "관측이 모델과 모순될 때(contradict), 공리를 수정해야 한다(revise)가 과학 방법론의 표준입니다."
        ),
        (
            "Corporate Ethics", "외견과 실질의 모순 (Greenwashing)",
            "The corporation attempted to [A] its environmental transgressions with [B] philanthropy",
            "의도([A] 죄책 은폐) + 수단([B] 피상적인/위선적인 자선)",
            "The conglomerate attempted to ________ its extensive toxic emissions by launching a series of ________ public relations campaigns boasting of modest solar donations.",
            "그 대기업은 겸손한 태양광 기부를 자랑하는 일련의 ________ 홍보 캠페인을 시작함으로써 자신들의 광범위한 유독 물질 배출을 ________하려고 시도했다.",
            "disguise — superficial",
            ["expose — profound", "acknowledge — lavish", "publicize — authentic"],
            [("disguise", "위장하다, 숨기다 (v.)"), ("superficial", "피상적인, 겉치레의 (adj.)"), ("expose", "폭로하다 (v.)"), ("profound", "심오한 (adj.)"), ("lavish", "호화로운 (adj.)")],
            "오염을 위장하고(disguise) 피상적인(superficial) 홍보를 벌였다는 그린워싱 비판 맥락입니다."
        ),
        (
            "Biochemistry & Genetics", "CRISPR의 장단점 (Precision vs. Off-target)",
            "While CRISPR allows scientists to [A] mutated genes, off-target cuts can induce [B] pathologies",
            "장점([A] 돌연변이 교정) vs 위험([B] 예상치 못한 병리)",
            "While CRISPR-Cas9 endonuclease empowers geneticists to ________ deleterious mutations with remarkable pinpoint accuracy, unguided off-target cleavages risk precipitating ________ cellular malignancies.",
            "CRISPR-Cas9 엔도뉴클레아제는 유전학자들이 현저한 핀포인트 정확도로 해로운 돌연변이를 ________할 수 있게 해주는 반면, 유도되지 않은 표적 외 절단은 ________ 세포 악성종양을 촉발할 위험이 있다.",
            "excise — unforeseen",
            ["replicate — predictable", "preserve — benign", "amplify — harmless"],
            [("excise", "잘라내다, 절제하다 (v.)"), ("unforeseen", "예측하지 못한 (adj.)"), ("replicate", "복제하다 (v.)"), ("benign", "양성의 (adj.)"), ("amplify", "증폭하다 (v.)")],
            "돌연변이를 잘라내어 제거하고(excise), 예상치 못한(unforeseen) 부작용을 낳을 수 있다는 대조입니다."
        ),
        (
            "Sociology of Urban Housing", "임대료 상한제의 역설 (Rent Control Consequences)",
            "Rent ceilings intend to make apartments [A], but landlord disinvestment makes housing [B]",
            "의도([A] 주거비 부담 경감) vs 현실([B] 주택 공급 부족/희소)",
            "Although statutory rent ceilings are enacted to render metropolitan housing ________ for impoverished families, empirical economists argue that subsequent developer disinvestment makes quality rentals increasingly ________.",
            "비록 법정 임대료 상한제는 빈곤 가구를 위해 대도시 주거를 ________하게 만들기 위해 제정되지만, 실증 경제학자들은 후속적인 개발업자들의 투자 철회가 양질의 임대주택을 점차 ________하게 만든다고 주장한다.",
            "affordable — scarce",
            ["exorbitant — abundant", "untenable — ubiquitous", "prohibitive — accessible"],
            [("affordable", "감당할 수 있는, 저렴한 (adj.)"), ("scarce", "부족한, 희소한 (adj.)"), ("exorbitant", "터무니없이 비싼 (adj.)"), ("untenable", "지탱할 수 없는 (adj.)"), ("prohibitive", "엄두를 못 낼 (adj.)")],
            "저렴하게 만들려는(affordable) 의도와 달리 공급이 희소해진다(scarce)가 전형적인 경제학적 역설입니다."
        ),
        # 11..20
        (
            "Constitutional Governance", "견제와 균형 (Checks and Balances)",
            "A system of checks and balances is designed to [A] tyrannical impulses and [B] civil liberties",
            "권력 남용 억제([A] 전횡 저지) → 목적([B] 자유 수호)",
            "The structural division of governmental prerogatives is explicitly crafted to ________ tyrannical power grabs and ________ the foundational civil rights of individual citizens.",
            "정부 특권의 구조적 분할은 전제주의적인 권력 찬탈을 ________하고 개별 시민의 근본적인 시민권을 ________하도록 명시적으로 고안되었다.",
            "curb — safeguard",
            ["foster — dismantle", "incite — obliterate", "instigate — compromise"],
            [("curb", "억제하다 (v.)"), ("safeguard", "보호하다 (v.)"), ("foster", "조성하다 (v.)"), ("dismantle", "해체하다 (v.)"), ("obliterate", "말살하다 (v.)")],
            "독재를 억제하고(curb) 시민권을 보호한다(safeguard)가 헌법적 대구입니다."
        ),
        (
            "Cognitive Neuroscience", "시냅스 가지치기 (Synaptic Pruning)",
            "Pruning eliminates [A] connections to [B] neural efficiency",
            "수단([A] 불필요한 시냅스 제거) → 결과([B] 뇌 회로 최적화)",
            "During adolescent brain maturation, extensive synaptic pruning acts to systematically ________ redundant neural pathways in order to ________ the computational speed of core cognitive circuits.",
            "청소년기 뇌 성숙 동안, 광범위한 시냅스 가지치기는 핵심 인지 회로의 연산 속도를 ________하기 위해 불필요한 신경 경로를 체계적으로 ________하는 역할을 한다.",
            "eliminate — optimize",
            ["proliferate — impair", "preserve — retard", "amplify — compromise"],
            [("eliminate", "제거하다 (v.)"), ("optimize", "최적화하다 (v.)"), ("proliferate", "급증하다 (v.)"), ("retard", "지체시키다 (v.)"), ("compromise", "손상하다 (v.)")],
            "잉여 경로를 제거하여(eliminate) 효율을 최적화한다(optimize)가 맞습니다."
        ),
        (
            "Economic History", "자유무역과 보호무역 (Protectionism vs Free Trade)",
            "Tariffs may temporarily [A] domestic producers, but they invariably [B] retaliatory levies",
            "단기 보호([A] 국내 기업 차폐) vs 장기 부작용([B] 보복 관세 촉발)",
            "While high protectionist tariffs may momentarily ________ domestic manufacturers from foreign competition, they invariably ________ retaliatory embargoes that depress aggregate exports.",
            "높은 보호주의 관세가 외국과의 경쟁으로부터 국내 제조업체를 일시적으로 ________할 수는 있지만, 그것들은 총수출을 침체시키는 보복성 금수 조치를 예외 없이 ________한다.",
            "insulate — provoke",
            ["expose — quell", "handicap — avert", "subjugate — prevent"],
            [("insulate", "보호하다, 격리하다 (v.)"), ("provoke", "유발하다 (v.)"), ("expose", "노출하다 (v.)"), ("quell", "진압하다 (v.)"), ("handicap", "불리하게 하다 (v.)")],
            "국내 제조업을 잠시 보호하지만(insulate) 보복을 초래한다(provoke)가 맞습니다."
        ),
        (
            "Paleoclimatology", "빙하기 주기와 밀란코비치 주기 (Milankovitch Cycles)",
            "Orbital wobbles [A] solar irradiance, which in turn [B] massive glaciation",
            "천문학적 원인([A] 일사량 변조) → 기후학적 결과([B] 대빙하 촉발)",
            "Subtle periodic oscillations in Earth's axial tilt significantly ________ the seasonal intensity of high-latitude solar radiation, which in turn ________ prolonged continental glaciation epochs.",
            "지구 자전축 경사의 미묘한 주기적 요동은 고위도 태양 복사의 계절적 강도를 크게 ________시키며, 이는 결국 장기간의 대륙 빙하 시대를 ________한다.",
            "modulate — precipitates",
            ["stabilize — precludes", "standardize — averts", "harmonize — prevents"],
            [("modulate", "조절하다, 변조하다 (v.)"), ("precipitates", "촉발하다, 재촉하다 (v.)"), ("stabilize", "안정시키다 (v.)"), ("precludes", "배제하다 (v.)"), ("averts", "피하다 (v.)")],
            "일사량을 변조하여(modulate) 빙하기를 촉발한다(precipitates)가 과학적 사실입니다."
        ),
        (
            "Behavioral Finance", "과잉 확신과 손실 (Overconfidence & Market Crash)",
            "Investors who [A] their own predictive acumen are prone to [B] catastrophic downside risks",
            "심리적 오류([A] 예측력 과대평가) → 비극적 결과([B] 하방 위험 과소평가/무시)",
            "Market speculators who excessively ________ their own analytical prescience invariably tend to ________ the catastrophic systemic risks inherent in high-leverage portfolios.",
            "자신의 분석적 예지력을 지나치게 ________하는 시장 투기꾼들은 고레버리지 포트폴리오에 내재된 파국적인 시스템적 위험을 ________하는 경향이 언제나 있다.",
            "overestimate — discount",
            ["undervalue — magnify", "downplay — dread", "disparage — anticipate"],
            [("overestimate", "과대평가하다 (v.)"), ("discount", "무시하다, 가볍게 보다 (v.)"), ("undervalue", "과소평가하다 (v.)"), ("downplay", "경시하다 (v.)"), ("disparage", "비하하다 (v.)")],
            "자신의 능력을 과대평가하고(overestimate) 위험은 가볍게 무시한다(discount)가 전형적인 금융 심리입니다."
        ),
        (
            "Literary Modernism", "의식의 흐름 기법 (Stream of Consciousness)",
            "By rejecting [A] chronology, modernist authors sought to capture the [B] flux of thoughts",
            "거부 대상([A] 엄격한 선형적 시간) ↔ 추구 대상([B] 분절되고 유동적인 내면)",
            "By deliberately abandoning ________ chronological progression, modernist novelists like Virginia Woolf sought to authentically reflect the ________ and associative nature of human consciousness.",
            "엄격하게 ________ 연대기적 진행을 의도적으로 버림으로써, 버지니아 울프와 같은 모더니스트 소설가들은 인간 의식의 ________하고 연상적인 본질을 진정성 있게 반영하고자 했다.",
            "linear — fluid",
            ["chaotic — static", "erratic — rigid", "sporadic — immutable"],
            [("linear", "선형적인 (adj.)"), ("fluid", "유동적인, 흐르는 (adj.)"), ("chaotic", "혼돈의 (adj.)"), ("static", "정적인 (adj.)"), ("erratic", "불규칙한 (adj.)")],
            "선형적 시간(linear chronology)을 버리고 유동적인 내면(fluid nature)을 포착했습니다."
        ),
        (
            "Cybernetics & AI Alignment", "목표 명시와 정렬 실패 (The Alignment Problem)",
            "An autonomous agent programmed with [A] objectives may execute them with [B] ruthlessness",
            "원인([A] 조잡하게 명시된 단일 목표) → 부작용([B] 맹목적이고 파괴적인 잔혹성)",
            "In artificial intelligence safety theory, an algorithmic system endowed with poorly ________ utility functions might pursue its assigned targets with ________ indifference to human welfare.",
            "인공지능 안전 이론에서 조잡하게 ________ 효용 함수를 부여받은 알고리즘 시스템은 인간의 복지에 대한 ________ 무관심으로 지정된 목표를 추구할 수 있다.",
            "circumscribed — chilling",
            ["articulated — empathetic", "delineated — benevolent", "formulated — compassionate"],
            [("circumscribed", "협소하게 규정된 (adj.)"), ("chilling", "오싹한, 냉혹한 (adj.)"), ("articulated", "분명히 표현된 (adj.)"), ("empathetic", "공감하는 (adj.)"), ("benevolent", "자애로운 (adj.)")],
            "좁게 규정된(circumscribed) 목표를 오싹하고 냉혹하게(chilling indifference) 밀어붙입니다."
        ),
        (
            "Evolutionary Parasitology", "기생충과 숙주 조종 (Host Manipulation)",
            "The parasite does not merely [A] host nutrients, but actively [B] host behavior",
            "단순 수탈 초과([A] 자원 흡수) ↔ 능동적 조종([B] 자살적 행동 유도)",
            "The parasitic fungus Cordyceps does not merely ________ nutritional sustenance from its ant host; it actively ________ the insect's motor nervous system to ensure transmission.",
            "기생 곰팡이 동충하초는 개미 숙주로부터 영양분을 단순히 ________하는 것에 그치지 않고, 자신의 포자 전파를 보장하기 위해 곤충의 운동 신경계를 능동적으로 ________한다.",
            "drain — hijacks",
            ["replenish — liberates", "synthesize — pacifies", "produce — soothes"],
            [("drain", "빼내다, 고갈시키다 (v.)"), ("hijacks", "납치하다, 장악하다 (v.)"), ("replenish", "보충하다 (v.)"), ("liberates", "해방하다 (v.)"), ("pacifies", "진정시키다 (v.)")],
            "영양분을 빨아먹을 뿐 아니라(drain) 신경계를 완전히 장악한다(hijacks)가 맞습니다."
        ),
        (
            "Aesthetic Architecture", "형태와 기능의 조화 (Form Follows Function)",
            "True architectural excellence does not [A] utility for beauty, but [B] both seamlessly",
            "대립 거부([A] 실용성을 희생시킴) ↔ 유기적 융합([B] 미와 기능을 융합함)",
            "Master architects argue that transcendent structural design does not ________ functional utility on the altar of visual spectacle, but rather ________ pragmatic efficacy with aesthetic grace.",
            "거장 건축가들은 초월적인 구조 설계가 시각적 화려함의 제단 위에 기능적 실용성을 ________하는 것이 아니라, 오히려 실용적 효능을 미적 우아함과 ________하는 것이라고 주장한다.",
            "sacrifice — synthesizes",
            ["venerate — divides", "celebrate — polarizes", "glorify — divorces"],
            [("sacrifice", "희생시키다 (v.)"), ("synthesizes", "종합하다, 합성하다 (v.)"), ("venerate", "숭배하다 (v.)"), ("divides", "나누다 (v.)"), ("divorces", "분리하다 (v.)")],
            "기능을 희생시키지 않고(sacrifice) 실용과 미를 종합한다(synthesizes)가 건축 철학입니다."
        ),
        (
            "Bioethics & Clinical Trials", "위약 대조군의 윤리 (Placebo Ethics)",
            "Withholding active treatment from sick patients may be scientifically [A], yet ethically [B]",
            "과학적 관점([A] 엄밀한 입증) vs 윤리적 관점([B] 용납될 수 없는 방치)",
            "In clinical trials for terminal oncological therapies, administering a pure inert placebo rather than the existing standard of care is methodologically ________, yet morally ________.",
            "말기 종양학 치료를 위한 임상 시험에서 기존의 표준 치료제 대신 순수한 비활성 위약을 투여하는 것은 방법론적으로는 ________하지만, 도덕적으로는 ________하다.",
            "rigorous — indefensible",
            ["sloppy — laudable", "flawed — commendable", "haphazard — praiseworthy"],
            [("rigorous", "엄격한, 정밀한 (adj.)"), ("indefensible", "변명할 수 없는, 정당화되지 않는 (adj.)"), ("sloppy", "엉성한 (adj.)"), ("laudable", "칭찬할 만한 (adj.)"), ("flawed", "결함 있는 (adj.)")],
            "과학적 엄밀함(rigorous)은 있을지언정 환자를 방치하므로 도덕적으로는 용납되지 않는다(indefensible)가 정답입니다."
        ),
        # 21..30
        (
            "Epidemiological Policy", "격리와 경제 충격 (Lockdowns vs Economy)",
            "Strict quarantine measures can successfully [A] infection rates, but severely [B] service commerce",
            "방역 성공([A] 감염률 억제) ↔ 경제 타격([B] 서비스 산업 질식/위축)",
            "Prolonged mandatory lockdowns can swiftly ________ viral transmission waves, but prolonged commercial isolation risks ________ fragile retail and hospitality businesses.",
            "장기간의 의무적 봉쇄 조치는 바이러스 전파 파동을 신속하게 ________할 수 있지만, 장기화된 상업적 고립은 취약한 소매 및 숙박업체를 ________할 위험이 있다.",
            "abate — suffocating",
            ["propagate — stimulating", "compound — bolstering", "escalate — invigorating"],
            [("abate", "가라앉히다, 줄이다 (v.)"), ("suffocating", "질식시키는 (adj./v.)"), ("propagate", "전파하다 (v.)"), ("compound", "악화시키다 (v.)"), ("escalate", "증대시키다 (v.)")],
            "전파를 줄이지만(abate) 상권을 질식시킨다(suffocating)가 대조를 이룹니다."
        ),
        (
            "Urban Sociology", "사회적 혼합 주거 (Mixed-Income Housing)",
            "Integrating varied income strata helps [A] class prejudices and [B] community cohesion",
            "부정적 편견 타파([A] 계층 갈등 해체) → 긍정적 효과([B] 유대감 강화)",
            "Urban renewal programs that deliberately construct mixed-income neighborhoods seek to ________ entrenched class stereotypes and ________ lasting community solidarity.",
            "소득 혼합 동네를 의도적으로 건설하는 도시 재생 프로그램은 깊게 뿌리박힌 계급 고정관념을 ________하고 지속적인 공동체 연대감을 ________하고자 한다.",
            "dismantle — foster",
            ["reinforce — undermine", "perpetuate — disrupt", "solidify — erode"],
            [("dismantle", "해체하다 (v.)"), ("foster", "조성하다, 기르다 (v.)"), ("reinforce", "강화하다 (v.)"), ("undermine", "약화시키다 (v.)"), ("perpetuate", "영속하다 (v.)")],
            "고정관념을 깨부수고(dismantle) 연대감을 키운다(foster)가 맞습니다."
        ),
        (
            "Astrophysics & Relativity", "블랙홀과 정보 역설 (Hawking Radiation Paradox)",
            "Hawking radiation implies black holes [A], which appears to [B] unitarity",
            "물리적 사건([A] 입자 방출로 증발) ↔ 양자역학 법칙([B] 정보 보존 법칙 위배)",
            "Stephen Hawking's discovery that black holes eventually ________ via quantum thermal emission created a theoretical paradox that appears to ________ the fundamental quantum law of information conservation.",
            "블랙홀이 양자 열 방출을 통해 결국 ________한다는 스티븐 호킹의 발견은 정보 보존이라는 근본적인 양자 법칙을 ________하는 것으로 보이는 이론적 역설을 낳았다.",
            "evaporate — violate",
            ["coagulate — affirm", "solidify — confirm", "crystallize — uphold"],
            [("evaporate", "증발하다 (v.)"), ("violate", "위반하다 (v.)"), ("coagulate", "응고하다 (v.)"), ("affirm", "단언하다 (v.)"), ("crystallize", "결정화하다 (v.)")],
            "블랙홀이 증발하면서(evaporate) 정보 보존 법칙을 위반한다(violate)가 유명한 정보 역설입니다."
        ),
        (
            "Linguistic Typology", "어순과 인지적 효율 (Word Order & Parsing)",
            "Flexible word order languages utilize [A] suffixes to [B] syntactic ambiguity",
            "문법적 도구([A] 격 어미 부착) → 인지적 효용([B] 구문 모호성 해소)",
            "Natural languages featuring highly unconstrained word order frequently rely on rich morphological ________ to ________ grammatical relationships and eliminate syntactic confusion.",
            "매우 제약 없는 어순을 특징으로 하는 자연어들은 문법적 관계를 ________하고 구문론적 혼란을 없애기 위해 풍부한 형태론적 ________에 자주 의존한다.",
            "inflections — clarify",
            ["omissions — confound", "abbreviations — obscure", "deletions — complicate"],
            [("inflections", "굴절, 어미 변화 (n.)"), ("clarify", "명확히 하다 (v.)"), ("omissions", "생략 (n.)"), ("confound", "혼동하다 (v.)"), ("obscure", "모호하게 하다 (v.)")],
            "풍부한 굴절 어미(inflections)를 통해 주어/목적어를 명확히 밝힌다(clarify)가 언어학적 사실입니다."
        ),
        (
            "Economics of Monopoly", "자연독점의 규제 딜레마 (Natural Monopoly)",
            "Unchecked monopolists will [A] prices, compelling regulators to [B] tariffs",
            "독점 폐해([A] 가격 착취/인상) → 정부 개입([B] 요금 규제/상한 설정)",
            "Without government oversight, private utility monopolies inevitably tend to ________ consumer rates to maximize rents, forcing public regulatory commissions to ________ legal rate caps.",
            "정부의 감독이 없다면, 민간 공공 유틸리티 독점 기업들은 지대를 극대화하기 위해 소비자 요금을 ________하는 경향이 예외 없이 나타나며, 이는 공공 규제 위원회가 법적 요금 상한선을 ________하도록 강제한다.",
            "gouge — impose",
            ["subsidize — repeal", "discount — abolish", "slash — rescind"],
            [("gouge", "바가지 씌우다, 과도하게 매기다 (v.)"), ("impose", "부과하다, 도입하다 (v.)"), ("subsidize", "보조금을 주다 (v.)"), ("repeal", "폐지하다 (v.)"), ("rescind", "철회하다 (v.)")],
            "가격을 바가지 씌우므로(gouge) 규제 당국이 상한선을 부과한다(impose)가 맞습니다."
        ),
        (
            "Environmental Toxicology", "생물농축 현상 (Bioaccumulation)",
            "Plankton absorb [A] concentrations of mercury, but apex predators end up with [B] levels",
            "하위 먹이사슬([A] 극미량 흡수) ↔ 상위 포식자([B] 치명적 고농도 축적)",
            "While microscopic phytoplankton ingest only ________ trace amounts of industrial methylmercury, apex marine raptors at the trophic summit accumulate ________ concentrations capable of causing reproductive collapse.",
            "비록 미세한 식물성 플랑크톤은 산업 메틸수은의 ________ 극미량만을 섭취하지만, 영양 단계 정점에 있는 최상위 해양 맹금류는 번식 붕괴를 일으킬 수 있는 ________ 농도를 축적한다.",
            "negligible — lethal",
            ["toxic — minuscule", "deadly — harmless", "fatal — benign"],
            [("negligible", "미미한, 하찮은 (adj.)"), ("lethal", "치명적인 (adj.)"), ("toxic", "유독한 (adj.)"), ("minuscule", "극소의 (adj.)"), ("benign", "무해한 (adj.)")],
            "플랑크톤은 미미하게(negligible) 섭취하지만 상위 포식자에게는 치명적인(lethal) 양이 쌓입니다."
        ),
        (
            "Epistemology & Conspiracy Theories", "음모론의 자기완결성 (Unfalsifiable Conspiracies)",
            "Absence of evidence is interpreted not as [A], but as proof of a [B] cover-up",
            "합리적 해석([A] 가설 기각의 증거) ↔ 망상적 해석([B] 완벽하고 사악한 은폐)",
            "In paranoid conspiracy narratives, the absolute absence of corroborating evidence is paradoxically viewed not as an objective ________ of the theory, but as definitive proof of a ________ cover-up.",
            "편집증적인 음모 서사에서 뒷받침하는 증거의 절대적인 부재는 역설적이게도 그 이론에 대한 객관적인 ________으로 간주되는 것이 아니라, ________ 은폐 공작에 대한 결정적인 증거로 간주된다.",
            "refutation — sinister",
            ["validation — clumsy", "endorsement — transparent", "confirmation — trivial"],
            [("refutation", "반박, 논박 (n.)"), ("sinister", "사악한, 불길한 (adj.)"), ("validation", "입증 (n.)"), ("clumsy", "서투른 (adj.)"), ("endorsement", "지지 (n.)")],
            "증거가 없음을 반박(refutation)으로 보지 않고 사악한 은폐(sinister cover-up)의 증거로 봅니다."
        ),
        (
            "Neurobiology of Addiction", "도파민 보상 예측 오차 (Reward Prediction Error)",
            "Anticipation of reward triggers a dopamine [A], whereas unfulfilled craving causes an agonizing [B]",
            "기대감([A] 도파민 분출/급증) ↔ 좌절([B] 도파민 급락/우울)",
            "Neurochemical investigations into behavioral compulsion reveal that the mere anticipation of a jackpot stimulates an intense dopamine ________, while subsequent omission of the payout triggers a visceral neurochemical ________.",
            "행동 강박에 대한 신경화학적 연구는 잭팟에 대한 단순한 기대만으로도 강렬한 도파민 ________을 자극하는 반면, 뒤이은 배당금의 누락은 본능적인 신경화학적 ________을 촉발함을 보여준다.",
            "surge — plunge",
            ["drop — ascent", "dearth — boom", "deficiency — spike"],
            [("surge", "급증, 솟구침 (n.)"), ("plunge", "급락, 추락 (n.)"), ("drop", "하락 (n.)"), ("ascent", "상승 (n.)"), ("dearth", "부족 (n.)")],
            "기대할 땐 급증하고(surge) 빗나갈 땐 급락한다(plunge)가 보상 오차의 메커니즘입니다."
        ),
        (
            "Labor Sociology", "원격 근무의 고립감 (Remote Work Alienation)",
            "Telecommuting grants scheduling [A], yet deprives employees of spontaneous social [B]",
            "편익([A] 시간적 유연성) vs 대가([B] 유기적 친교의 결핍)",
            "While ubiquitous telecommuting endows knowledge workers with unprecedented temporal ________, it frequently deprives them of the casual workplace camaraderie essential for psychological ________.",
            "어디서나 가능한 원격 근무가 지식 노동자들에게 전례 없는 시간적 ________을 부여하지만, 그것은 심리적 ________에 필수적인 직장 내 격의 없는 동료애를 자주 박탈한다.",
            "flexibility — well-being",
            ["rigidity — isolation", "paralysis — alienation", "confinement — distress"],
            [("flexibility", "유연성 (n.)"), ("well-being", "안녕, 행복 (n.)"), ("rigidity", "경직성 (n.)"), ("isolation", "고립 (n.)"), ("alienation", "소외 (n.)")],
            "시간적 유연성(flexibility)을 얻지만 행복/안녕(well-being)에 필요한 유대를 잃습니다."
        ),
        (
            "Macroprudential Regulation", "금융 시스템의 시스템적 리스크 (Contagion)",
            "Interconnected banks can efficiently [A] liquidity, but shockwaves can [B] the entire network",
            "평시 장점([A] 유동성 분산) ↔ 위기 파급([B] 전신 마비/붕괴 초래)",
            "A hyper-interconnected interbank lending network allows institutions to smoothly ________ seasonal liquidity deficits, yet a sudden default by a flagship conglomerate risks ________ the entire financial apparatus.",
            "고도로 상호 연결된 은행 간 대출 네트워크는 금융기관들이 계절적 유동성 적자를 순조롭게 ________할 수 있게 해주지만, 대표 대기업의 갑작스러운 채무불이행은 전체 금융 기구를 ________할 위험이 있다.",
            "absorb — paralyzing",
            ["magnify — stabilizing", "escalate — fortifying", "compound — invigorating"],
            [("absorb", "흡수하다, 완충하다 (v.)"), ("paralyzing", "마비시키는 (adj./v.)"), ("magnify", "확대하다 (v.)"), ("stabilizing", "안정시키는 (adj.)"), ("compound", "악화시키다 (v.)")],
            "평소엔 유동성 충격을 흡수하지만(absorb) 연쇄 도산 시 전체를 마비시킨다(paralyzing)가 맞습니다."
        ),
        # 31..40
        (
            "Bioethics of Human Enhancement", "생체 증강의 불평등 (Transhumanist Inequality)",
            "Cognitive implants will not be [A] distributed, creating an entrenched [B] elite",
            "비판([A] 평등한 분배 실패) → 결과([B] 유전적/인지적 귀족 계급 형성)",
            "Sociologists warn that expensive cybernetic neuro-enhancements will never be ________ allocated, thereby threatening to birth a biologically distinct and socioeconomically ________ caste.",
            "사회학자들은 값비싼 인공두뇌 신경 증강 기술이 결코 ________ 배분되지 않을 것이며, 그에 따라 생물학적으로 뚜렷하고 사회경제적으로 ________ 계급을 낳을 위험이 있다고 경고한다.",
            "equitably — entrenched",
            ["sporadically — transient", "scarcely — vulnerable", "randomly — powerless"],
            [("equitably", "공평하게 (adv.)"), ("entrenched", "견고하게 자리 잡은 (adj.)"), ("sporadically", "산발적으로 (adv.)"), ("transient", "일시적인 (adj.)"), ("vulnerable", "취약한 (adj.)")],
            "공평하게(equitably) 나뉘지 않아 견고한(entrenched) 특권층을 낳을 것입니다."
        ),
        (
            "Aero-acoustics", "초음속 비행의 충격파 (Sonic Boom Mitigation)",
            "Commercial supersonic transit was banned because of [A] booms, prompting engineers to design [B] fuselages",
            "문제([A] 귀청 찢는 폭음) → 해결책([B] 충격파 분산 유선형 동체)",
            "Commercial supersonic overland travel was historically banned due to ________ sonic detonations, driving modern aeronautical engineers to shape razor-thin fuselages that ________ shockwave convergence.",
            "상업용 초음속 내륙 비행은 역사적으로 ________ 소닉붐 폭음 때문에 금지되었으며, 이는 현대 항공 엔지니어들로 하여금 충격파의 집중을 ________하는 극도로 얇은 동체를 설계하도록 이끌었다.",
            "deafening — disperse",
            ["imperceptible — concentrate", "inaudible — focus", "subtle — magnify"],
            [("deafening", "귀청이 터질 듯한 (adj.)"), ("disperse", "분산시키다 (v.)"), ("imperceptible", "감지할 수 없는 (adj.)"), ("concentrate", "집중시키다 (v.)"), ("inaudible", "들리지 않는 (adj.)")],
            "귀청이 찢어지는 폭음(deafening booms) 때문에 파동을 분산시키는(disperse) 동체를 만듭니다."
        ),
        (
            "Evolutionary Game Theory", "죄수의 딜레마 (Tit-for-Tat Strategy)",
            "The Tit-for-Tat strategy succeeds because it is immediately [A] to cooperation and decisively [B] toward betrayal",
            "성공 비결([A] 협력에 대한 보답) + [B] 배신에 대한 즉각 보복",
            "Axelrod's classic computational tournament demonstrated that the 'Tit-for-Tat' strategy triumphs because it is inherently ________ to initial peaceful overtures, yet consistently ________ against unprovoked exploitation.",
            "액설로드의 고전적인 컴퓨터 토너먼트는 '팃포탯(눈에는 눈)' 전략이 초기의 평화적 제안에는 본질적으로 ________하지만, 도발 없는 착취에 대해서는 일관되게 ________하기 때문에 승리함을 입증했다.",
            "receptive — retaliatory",
            ["hostile — forgiving", "impervious — lenient", "aggressive — tolerant"],
            [("receptive", "수용적인, 잘 받아들이는 (adj.)"), ("retaliatory", "보복적인 (adj.)"), ("hostile", "적대적인 (adj.)"), ("forgiving", "관대한 (adj.)"), ("lenient", "자비로운 (adj.)")],
            "협력은 기꺼이 받아들이고(receptive) 배신에는 단호히 보복한다(retaliatory)가 맞습니다."
        ),
        (
            "Geological Volcanology", "초화산과 화산 겨울 (Volcanic Winter)",
            "Super-eruptions inject sulfate aerosols that [A] sunlight and trigger [B] global cooling",
            "기작([A] 태양광 차단/반사) → 귀결([B] 가혹한 기온 급락)",
            "Cataclysmic volcanic super-eruptions eject vast quantities of sulfurous aerosols into the stratosphere that ________ incoming solar radiation and precipitate ________ planetary cooling epochs.",
            "격변적인 화산 초분화는 성층권으로 막대한 양의 황산염 에어로졸을 분출하여 유입되는 태양 복사를 ________하고 ________ 전 지구적 냉각 시대를 촉발한다.",
            "deflect — severe",
            ["absorb — temperate", "transmit — balmy", "harness — mild"],
            [("deflect", "굴절시키다, 반사하다 (v.)"), ("severe", "가혹한, 극심한 (adj.)"), ("absorb", "흡수하다 (v.)"), ("temperate", "온화한 (adj.)"), ("balmy", "아늑한 (adj.)")],
            "햇빛을 튕겨내어 차단하고(deflect) 가혹한(severe) 냉각을 부릅니다."
        ),
        (
            "Philosophy of Aesthetics", "숭고미의 본질 (The Sublime)",
            "Beauty evokes harmony, whereas the Sublime evokes a blend of [A] terror and [B] awe",
            "미(아늑함) ↔ 숭고([A] 압도적인 공포와 위협 + [B] 황홀한 경외감)",
            "Edmund Burke distinguished the Beautiful from the Sublime by noting that while beauty elicits calm pleasure, the Sublime inspires a paradoxically thrilling combination of ________ fear and transcendent ________.",
            "에드먼드 버크는 아름다움이 고요한 즐거움을 이끌어내는 반면, 숭고는 ________ 공포와 초월적인 ________의 역설적으로 스릴 넘치는 결합을 고무한다는 점을 지적함으로써 미와 숭고를 구별했다.",
            "paralyzing — veneration",
            ["trivial — contempt", "trifling — disdain", "negligible — scorn"],
            [("paralyzing", "마비시키는 (adj.)"), ("veneration", "경외, 숭배 (n.)"), ("trivial", "사소한 (adj.)"), ("contempt", "경멸 (n.)"), ("disdain", "멸시 (n.)")],
            "압도적 공포(paralyzing fear)와 초월적 경외(transcendent veneration)가 숭고의 양대 축입니다."
        ),
        (
            "Cognitive Linguistics", "프레임 이론 (Framing Effects)",
            "Semantic framing does not merely [A] information, but actively [B] perception",
            "단순 전달 초과([A] 팩트 서술) ↔ 능동적 조작([B] 유권자의 해석 틀 구성)",
            "Cognitive linguist George Lakoff proved that political metaphors do not merely ________ objective facts, but actively ________ the conceptual parameters within which voters evaluate policy proposals.",
            "인지언어학자 조지 레이코프는 정치적 은유가 객관적 사실을 단순히 ________하는 것에 그치지 않고, 유권자들이 정책 제안을 평가하는 개념적 매개변수를 능동적으로 ________함을 증명했다.",
            "convey — delimit",
            ["withhold — liberate", "conceal — emancipate", "distort — unfetter"],
            [("convey", "전달하다 (v.)"), ("delimit", "한계/경계를 정하다 (v.)"), ("withhold", "보류하다 (v.)"), ("liberate", "해방하다 (v.)"), ("conceal", "숨기다 (v.)")],
            "사실을 전달할(convey) 뿐 아니라 사고의 경계를 구획한다(delimit)가 프레이밍 이론입니다."
        ),
        (
            "Macroeconomics", "스태그플레이션의 딜레마 (Stagflationary Bind)",
            "Stagflation couples [A] inflation with [B] output growth",
            "동시 고통([A] 치솟는 물가 + [B] 정체된 실물 경제)",
            "Stagflation represents the ultimate nightmare for monetary economists because it combines ________ price increases with ________ economic expansion, confounding conventional policy remedies.",
            "스태그플레이션은 기존의 정책 처방을 혼란에 빠뜨리면서 ________ 물가 상승과 ________ 경제 팽창을 결합하기 때문에 통화 경제학자들에게 궁극적인 악몽을 나타낸다.",
            "runaway — stagnant",
            ["moderate — booming", "benign — vigorous", "subdued — buoyant"],
            [("runaway", "걷잡을 수 없는 (adj.)"), ("stagnant", "정체된 (adj.)"), ("moderate", "온건한 (adj.)"), ("booming", "번성하는 (adj.)"), ("buoyant", "활황의 (adj.)")],
            "걷잡을 수 없는 물가(runaway prices)와 침체된 성장(stagnant growth)의 결합입니다."
        ),
        (
            "Immunotherapy & Cancer", "면역관문억제제 (Checkpoint Inhibitors)",
            "Tumors evade detection by [A] T-cells, but inhibitors [B] antitumor immunity",
            "종양의 면역 회피([A] T세포 억제) ↔ 항암제 작용([B] 면역계 족쇄 해방)",
            "Malignant neoplasms frequently evade immune surveillance by deploying ligands that ________ killer T-cells, but monoclonal checkpoint inhibitors effectively ________ the body's natural cytotoxic arsenal.",
            "악성 신생물(종양)은 살상 T세포를 ________하는 리간드를 배치함으로써 면역 감시를 자주 회피하지만, 단일클론 면역관문억제제는 신체의 자연적인 세포독성 무기고를 효과적으로 ________한다.",
            "deactivate — unleash",
            ["energize — shackle", "stimulate — tether", "invigorate — constrain"],
            [("deactivate", "비활성화하다 (v.)"), ("unleash", "촉발하다, 풀어놓다 (v.)"), ("energize", "활력을 주다 (v.)"), ("shackle", "차꼬를 채우다 (v.)"), ("tether", "묶다 (v.)")],
            "T세포를 마비시키는(deactivate) 암에 맞서 면역 공격력을 완전히 풀어놓는다(unleash)가 정답입니다."
        ),
        (
            "Urban Transport", "유도 수요 현상 (Induced Demand)",
            "Widening highways to [A] gridlock paradoxically [B] private car usage",
            "의도([A] 정체 해소) ↔ 실제 역효과([B] 통행량 폭증 유발)",
            "Urban traffic engineering exhibits the paradox of induced demand: expanding metropolitan freeways in an attempt to ________ congestion invariably ________ new vehicular trips that quickly refill the lanes.",
            "도시 교통 공학은 유도 수요의 역설을 보여준다. 즉, 정체를 ________하려는 시도로 대도시 고속도로를 확장하는 것은 차선을 빠르게 다시 채우는 새로운 차량 통행을 예외 없이 ________한다.",
            "alleviate — attracts",
            ["aggravate — repels", "compound — discourages", "escalate — deters"],
            [("alleviate", "완화하다 (v.)"), ("attracts", "끌어들이다 (v.)"), ("aggravate", "악화시키다 (v.)"), ("repels", "쫓아내다 (v.)"), ("compound", "가중시키다 (v.)")],
            "정체를 풀려고(alleviate) 길을 넓히면 더 많은 차를 유인한다(attracts)가 교통학의 상식입니다."
        ),
        (
            "Philosophy of Technology", "기술의 자율성과 소외 (Technological Alienation)",
            "Machines promise to [A] human drudgery, but workers feel increasingly [B] by pacing algorithms",
            "약속([A] 고된 노동 경감) ↔ 현실([B] 기계의 속도에 종속되어 소외됨)",
            "Industrial automation was heralded as a liberating development that would ________ workers from backbreaking physical toil, yet many modern logistics employees find themselves ________ by ruthless tracking software.",
            "산업 자동화는 고된 육체 노동으로부터 노동자들을 ________할 해방적 발전으로 선포되었지만, 많은 현대 물류 노동자들은 무자비한 추적 소프트웨어에 의해 자신들이 ________되고 있음을 발견한다.",
            "emancipate — enslaved",
            ["shackle — empowered", "imprison — liberated", "subjugate — unconstrained"],
            [("emancipate", "해방하다 (v.)"), ("enslaved", "노예가 된 (adj.)"), ("shackle", "차꼬를 채우다 (v.)"), ("empowered", "권한을 얻은 (adj.)"), ("subjugate", "굴복시키다 (v.)")],
            "노동에서 해방시켜줄(emancipate) 줄 알았으나 오히려 소프트웨어의 노예가 되었다(enslaved)는 비판입니다."
        ),
        # 41..50
        (
            "Environmental Climatology", "피드백 루프 (Methane Feedback Loops)",
            "Melting permafrost [A] trapped methane, which accelerates atmospheric warming and [B] further thawing",
            "원인([A] 온실가스 방출) → 증폭([B] 추가 해빙 촉진)",
            "Thawing arctic tundra risks triggering an irreversible feedback loop wherein decomposing organic soil layers ________ immense volumes of trapped methane, which further ________ atmospheric temperature anomalies.",
            "녹아내리는 북극 툰드라는 갇혀 있던 막대한 양의 메탄을 유기 토양층의 분해가 ________하고, 이것이 대기 온도 기형을 더욱 ________하는 돌이킬 수 없는 되먹임 고리를 촉발할 위험이 있다.",
            "release — compounds",
            ["absorb — mitigates", "trap — alleviates", "sequester — quenches"],
            [("release", "방출하다 (v.)"), ("compounds", "가중시키다, 악화시키다 (v.)"), ("absorb", "흡수하다 (v.)"), ("mitigates", "완화하다 (v.)"), ("sequester", "격리하다 (v.)")],
            "메탄을 대기 중으로 방출하고(release) 온난화를 더욱 가중시킨다(compounds)가 맞습니다."
        ),
        (
            "Corporate Monopsony", "단일 구매자 독점과 임금 압박 (Wage Stagnation)",
            "Isolated local employers can [A] wages because workers lack [B] alternatives",
            "원인([A] 임금 억제/착취) ← 배경([B] 대체 일자리 결핍)",
            "When a solitary corporation dominates a regional employment market, it possesses monopsony leverage that enables it to ________ labor compensation because desperate residents have few ________ opportunities.",
            "단독 기업이 지역 고용 시장을 지배할 때, 그것은 절박한 주민들이 ________ 기회를 거의 갖지 못하기 때문에 노동 보수를 ________할 수 있게 해주는 구매자독점 지배력을 소유한다.",
            "suppress — viable",
            ["inflate — scarce", "elevate — remote", "augment — barren"],
            [("suppress", "억압하다, 낮추다 (v.)"), ("viable", "실행 가능한, 유효한 (adj.)"), ("inflate", "부풀리다 (v.)"), ("scarce", "부족한 (adj.)"), ("augment", "늘리다 (v.)")],
            "마땅한 대안(viable opportunities)이 없어 임금을 억누른다(suppress)가 노동경제학 모델입니다."
        ),
        (
            "Evolutionary Parasitology", "적혈구 변이와 말라리아 (Sickle Cell Heterozygote Advantage)",
            "Carrying a single sickle-cell gene [A] malaria vulnerability without causing [B] anemia",
            "이점([A] 말라리아 저항성 획득) ↔ 무해([B] 치명적 빈혈 회피)",
            "The evolutionary persistence of the sickle-cell allele in equatorial Africa is explained by heterozygote advantage: carrying a single mutated gene ________ resistance against lethal malaria while avoiding the ________ complications of full-blown sickle cell disease.",
            "적도 아프리카에서 겸상 적혈구 대립유전자의 진화적 지속성은 이형접합체 이점에 의해 설명된다. 즉, 단일 돌연변이 유전자를 지니는 것은 완전한 겸상 적혈구 질환의 ________ 합병증을 피하면서 치명적인 말라리아에 대한 저항성을 ________한다.",
            "confers — debilitating",
            ["strips — benign", "diminishes — harmless", "erodes — trivial"],
            [("confers", "부여하다 (v.)"), ("debilitating", "쇠약하게 하는 (adj.)"), ("strips", "박탈하다 (v.)"), ("benign", "양성의 (adj.)"), ("erodes", "침식하다 (v.)")],
            "저항성을 부여하고(confers) 쇠약하게 하는(debilitating) 빈혈은 겪지 않습니다."
        ),
        (
            "Epistemology of Testimony", "소셜 증언의 신뢰성 (Testimonial Injustice)",
            "Prejudice leads listeners to [A] marginalized witnesses and [B] credibility",
            "편견의 작용([A] 증언 불신) → 결과([B] 신뢰성 강탈)",
            "Miranda Fricker introduced 'testimonial injustice' to describe epistemic bigotry wherein hearers, tainted by identity prejudice, unfairly ________ the testimony of minority speakers and systematically ________ their epistemic credibility.",
            "미란다 프릭커는 정체성 편견에 물든 청자들이 소수자 화자의 증언을 부당하게 ________하고 그들의 인식적 신뢰성을 체계적으로 ________하는 인식론적 편협함을 설명하기 위해 '증언 불의'를 도입했다.",
            "discredit — deflate",
            ["venerate — inflate", "celebrate — augment", "canonize — bolster"],
            [("discredit", "불신하다, 신뢰를 떨어뜨리다 (v.)"), ("deflate", "끌어내리다, 축소하다 (v.)"), ("venerate", "숭배하다 (v.)"), ("inflate", "부풀리다 (v.)"), ("canonize", "성문화하다 (v.)")],
            "증언을 불신하고(discredit) 신뢰성을 깎아내린다(deflate)가 철학적 개념입니다."
        ),
        (
            "Archaeogenetics", "인류 고대 이동과 DNA (Ancient DNA Sequencing)",
            "Old archaeological digs inferred slow [A], but ancient DNA revealed rapid [B]",
            "과거 통념([A] 점진적 문화 전파) ↔ 유전체 분석([B] 대규모 인구 대체 및 이주)",
            "Earlier generations of archaeologists assumed pottery styles spread through peaceful cultural ________, but revolutionary ancient genome sequencing has proven that historical shifts were driven by sweeping population ________.",
            "이전 세대의 고고학자들은 도자기 양식이 평화로운 문화적 ________을 통해 퍼졌다고 가정했지만, 혁명적인 고대 게놈 염기서열 분석은 역사적 변화가 전면적인 인구 ________에 의해 주도되었음을 증명했다.",
            "diffusion — replacements",
            ["extinction — preservation", "eradication — stagnation", "stoppage — isolation"],
            [("diffusion", "확산, 전파 (n.)"), ("replacements", "대체, 교체 (n.)"), ("extinction", "멸종 (n.)"), ("preservation", "보존 (n.)"), ("stagnation", "정체 (n.)")],
            "단순한 문화 전파(diffusion)가 아니라 실제 인구의 물리적 대체(replacements)였습니다."
        ),
        (
            "Constitutional Jurisprudence", "비례의 원칙 (Principle of Proportionality)",
            "State restrictions must not be [A], but strictly [B] to legitimate goals",
            "금지 요건([A] 과도하고 자의적임) ↔ 필수 요건([B] 목표에 비례하고 부합함)",
            "In constitutional human rights jurisprudence, statutory limitations on free speech must never be ________, but must remain strictly ________ to the compelling public interest at stake.",
            "헌법적 인권 판례에서 표현의 자유에 대한 법정 제한은 결코 ________해서는 안 되며, 문제가 된 절박한 공공 이익에 엄격하게 ________ 상태를 유지해야 한다.",
            "disproportionate — tailored",
            ["commensurate — hostile", "harmonious — adverse", "consonant — detrimental"],
            [("disproportionate", "불균형적인, 과도한 (adj.)"), ("tailored", "맞춤형의, 비례하는 (adj.)"), ("commensurate", "비례하는 (adj.)"), ("hostile", "적대적인 (adj.)"), ("harmonious", "조화로운 (adj.)")],
            "불균형적이어서는(disproportionate) 안 되며 목표에 딱 맞춰져야(tailored) 합니다."
        ),
        (
            "Behavioral Architecture", "넛지 이론 (Choice Architecture)",
            "Nudges do not [A] choices, but subtly [B] decisions toward health",
            "금지 거부([A] 선택지 박탈) ↔ 부드러운 유도([B] 건강한 선택 방향 안내)",
            "Behavioral choice architects emphasize that a benign nudge does not forcibly ________ unhealthy dietary options, but rather subtly ________ consumer attention toward wholesome produce.",
            "행동 선택 설계자들은 온건한 넛지가 건강에 해로운 식단 선택지를 강제로 ________하는 것이 아니라, 오히려 유익한 농산물 쪽으로 소비자의 주의를 미묘하게 ________한다고 강조한다.",
            "outlaw — steers",
            ["mandate — diverts", "enforce — distracts", "impose — alienates"],
            [("outlaw", "불법화하다, 금지하다 (v.)"), ("steers", "유도하다, 이끌다 (v.)"), ("mandate", "의무화하다 (v.)"), ("diverts", "돌리다 (v.)"), ("enforce", "강제하다 (v.)")],
            "선택을 금지하지(outlaw) 않고 부드럽게 이끈다(steers)가 넛지의 본령입니다."
        ),
        (
            "Economic Geography", "클러스터 경제학 (Agglomeration Economies)",
            "Proximity of firms creates [A] talent pools that [B] collaborative innovation",
            "지리적 인접성([A] 풍부한 인재 풀 형성) → 귀결([B] 협력적 혁신 가속)",
            "The geographical concentration of biotechnology firms in Silicon Valley creates a deep ________ of specialized laboratory talent that dramatically ________ collaborative innovation cycles.",
            "실리콘밸리에 바이오테크 기업들이 지리적으로 집중된 것은 협력적 혁신 주기를 극적으로 ________하는 전문화된 실험실 인재의 두터운 ________을 형성한다.",
            "reservoir — accelerates",
            ["scarcity — impedes", "dearth — retards", "vacuum — obstructs"],
            [("reservoir", "저수지, 보고 (n.)"), ("accelerates", "가속화하다 (v.)"), ("scarcity", "부족 (n.)"), ("impedes", "방해하다 (v.)"), ("dearth", "결핍 (n.)")],
            "두터운 인재의 보고(reservoir)가 혁신을 가속한다(accelerates)가 집적 경제학입니다."
        ),
        (
            "Cellular Senescence", "노화세포 제거 약물 (Senolytics)",
            "Senescent zombie cells [A] toxic cytokines, but senolytics [B] tissue regeneration",
            "노화세포 악영향([A] 염증 물질 분비) ↔ 신약 효과([B] 청춘 조직 재생 촉진)",
            "Aging tissues accumulate dormant senescent cells that chronically ________ pro-inflammatory cytokines, but novel senolytic drugs clear these cellular zombies to ________ juvenile tissue regeneration.",
            "노화하는 조직은 전염증성 사이토카인을 만성적으로 ________하는 휴면 노화세포를 축적하지만, 새로운 세놀리틱스 약물은 젊은 조직 재생을 ________하기 위해 이러한 좀비 세포들을 제거한다.",
            "secrete — reinvigorate",
            ["absorb — stifle", "ingest — extinguish", "quench — suppress"],
            [("secrete", "분비하다 (v.)"), ("reinvigorate", "새로운 활력을 불어넣다 (v.)"), ("absorb", "흡수하다 (v.)"), ("stifle", "억누르다 (v.)"), ("ingest", "섭취하다 (v.)")],
            "독성 물질을 분비하지만(secrete) 약물이 조직을 다시 활성화한다(reinvigorate)가 맞습니다."
        ),
        (
            "Sociolinguistics", "코드 스위칭 (Code-Switching)",
            "Bilinguals do not randomly [A] grammars, but purposefully [B] identities",
            "오해 해소([A] 혼란스러운 문법 뒤섞기) ↔ 사회적 기능([B] 상황별 정체성 조율)",
            "Sociolinguistic research demonstrates that multilingual code-switching is not an ungrammatical ________ of idioms, but a sophisticated communicative tactic used to skillfully ________ social solidarity.",
            "사회언어학 연구는 다국어 코드 전환이 관용구의 비문법적인 ________가 아니라, 사회적 연대감을 능숙하게 ________하는 데 사용되는 정교한 의사소통 전술임을 보여준다.",
            "jumble — negotiate",
            ["clarification — destroy", "synthesis — subvert", "cohesion — shatter"],
            [("jumble", "뒤범벅, 혼합 (n.)"), ("negotiate", "조율하다, 성사시키다 (v.)"), ("clarification", "명료화 (n.)"), ("synthesis", "종합 (n.)"), ("subvert", "전복하다 (v.)")],
            "어설픈 뒤범벅(jumble)이 아니라 사회적 관계를 조율하는(negotiate) 전술입니다."
        ),
        # 51..60
        (
            "Philosophy of Mind", "기능주의 (Functionalism)",
            "Mind is not defined by its biological [A], but by its computational [B]",
            "물질 환원 거부([A] 뇌의 유기적 기질) ↔ 기능 중시([B] 정보 처리적 조직화)",
            "Philosophical functionalists argue that cognitive states are not defined by their specific physical ________, but rather by their abstract functional and computational ________ within a cognitive network.",
            "철학적 기능주의자들은 인지 상태가 특정한 물리적 ________에 의해 정의되는 것이 아니라, 인지 네트워크 내에서의 추상적인 기능적 및 계산적 ________에 의해 정의된다고 주장한다.",
            "substrate — architecture",
            ["outcome — destruction", "consequence — dissolution", "destiny — annihilation"],
            [("substrate", "기질, 바탕 물질 (n.)"), ("architecture", "구조, 구조적 설계 (n.)"), ("outcome", "결과 (n.)"), ("dissolution", "해체 (n.)"), ("annihilation", "전멸 (n.)")],
            "물리적 기질(substrate)이 아니라 계산적 구조(architecture)가 핵심입니다."
        ),
        (
            "Macroeconomic Labor Markets", "필립스 곡선의 붕괴 (The Breakdown of Phillips Curve)",
            "Policymakers assumed inflation would [A] employment, yet stagflation [B] this trade-off",
            "과거 믿음([A] 고용 촉진) ↔ 70년대 현실([B] 전통 이론 반박/박살)",
            "Mid-century central bankers operated under the assumption that modest inflation would reliably ________ job creation, yet the stagflation shocks of the 1970s thoroughly ________ this cherished trade-off.",
            "20세기 중반 중앙은행 총재들은 완만한 인플레이션이 일자리 창출을 안정적으로 ________할 것이라는 가정하에 운영되었지만, 1970년대의 스태그플레이션 충격은 이 소중한 상충관계를 완전히 ________했다.",
            "stimulate — demolished",
            ["stifle — corroborated", "suppress — validated", "curb — substantiated"],
            [("stimulate", "자극하다, 촉진하다 (v.)"), ("demolished", "무너뜨렸다, 박살 냈다 (v.)"), ("stifle", "억누르다 (v.)"), ("corroborated", "확증했다 (v.)"), ("substantiated", "실증했다 (v.)")],
            "고용을 자극할 줄 알았으나(stimulate) 가설이 완전히 무너졌다(demolished)가 맞습니다."
        ),
        (
            "Ecological Invasions", "외래종과 토착종 경쟁 (Invasive Species)",
            "Invasive kudzu possesses [A] adaptability that allows it to rapidly [B] native flora",
            "외래종 강점([A] 가공할 활력) → 토착종 피해([B] 햇빛과 영양분 독점으로 질식)",
            "The invasive kudzu vine possesses an aggressive physiological ________ that allows its dense foliage to completely ________ native saplings by blocking essential sunlight.",
            "침입성 칡덩굴은 빽빽한 잎으로 필수적인 햇빛을 차단함으로써 토착 묘목들을 완전히 ________할 수 있게 해주는 공격적인 생리적 ________을 가지고 있다.",
            "vitality — smother",
            ["fragility — nourish", "debility — foster", "feebleness — cultivate"],
            [("vitality", "활력, 생명력 (n.)"), ("smother", "질식시키다, 뒤덮다 (v.)"), ("fragility", "취약성 (n.)"), ("nourish", "영양을 주다 (v.)"), ("feebleness", "연약함 (n.)")],
            "강한 생명력(vitality)으로 토착 식물을 질식시킨다(smother)가 생태학적 정답입니다."
        ),
        (
            "Literary Translation", "직역과 의역의 갈등 (Formal vs Dynamic Equivalence)",
            "A rigid literal translation yields [A] syntax, whereas excessive poetic license [B] original meaning",
            "직역의 결함([A] 어색한 문장) vs 과도한 의역의 결함([B] 원작 왜곡)",
            "Translators must tread a delicate path: slavish word-for-word adherence yields ________, wooden phrasing, while excessive interpretive freedom risks ________ the author's nuanced nuances.",
            "번역가들은 섬세한 길을 걸어야 한다. 즉, 맹목적인 단어 대 단어의 고수는 ________하고 딱딱한 어구를 낳는 반면, 과도한 해석적 자유는 저자의 미묘한 뉘앙스를 ________할 위험이 있다.",
            "stilted — distorting",
            ["fluent — preserving", "graceful — honoring", "natural — capturing"],
            [("stilted", "부자연스러운, 어색한 (adj.)"), ("distorting", "왜곡하는 (adj./v.)"), ("fluent", "유창한 (adj.)"), ("preserving", "보존하는 (adj.)"), ("graceful", "우아한 (adj.)")],
            "너무 직역하면 어색하고(stilted), 너무 의역하면 왜곡한다(distorting)가 번역의 딜레마입니다."
        ),
        (
            "Epistemology of Science", "귀납의 문제 (Hume's Problem of Induction)",
            "Observing ten thousand white swans does not [A] the rule, but a single black swan [B] it",
            "확증의 한계([A] 절대적 입증 불가) ↔ 반례의 힘([B] 가설의 즉각적 붕괴)",
            "David Hume observed that no finite number of white swan sightings can ever logically ________ the universal hypothesis that all swans are white, whereas the appearance of a single black specimen decisively ________ it.",
            "데이비드 흄은 아무리 유한한 수의 흰 백조 목격도 모든 백조가 희다는 보편적 가설을 논리적으로 ________할 수는 없는 반면, 단 한 마리의 검은 백조의 출현은 그것을 결정적으로 ________한다고 관찰했다.",
            "prove — falsifies",
            ["refute — corroborates", "disprove — validates", "subvert — confirms"],
            [("prove", "증명하다 (v.)"), ("falsifies", "반증하다 (v.)"), ("refute", "반박하다 (v.)"), ("corroborates", "확증하다 (v.)"), ("validates", "검증하다 (v.)")],
            "경험으로 증명할(prove) 수는 없지만 반례 하나가 반증한다(falsifies)가 흄의 귀납 문제입니다."
        ),
        (
            "Evolutionary Psychology", "집단 내 이타성과 집단 간 적대 (Parochial Altruism)",
            "Human evolution bonded clans through [A] internal loyalty alongside [B] outgroup hostility",
            "내집단([A] 헌신적 결속) ↔ 외집단([B] 적대적 배타성)",
            "Anthropologists theorize that ancient tribal warfare forged human nature into an engine of 'parochial altruism,' combining fierce ________ solidarity toward kin with deep-seated ________ toward competing clans.",
            "인류학자들은 고대 부족 전쟁이 인간 본성을 '편협한 이타주의'의 엔진으로 벼려내어, 친족에 대한 맹렬한 ________ 연대감과 경쟁 부족에 대한 뿌리 깊은 ________을 결합시켰다고 이론화한다.",
            "unselfish — enmity",
            ["treacherous — affinity", "perfidious — harmony", "hostile — amity"],
            [("unselfish", "이타적인 (adj.)"), ("enmity", "적대감, 원한 (n.)"), ("treacherous", "배반하는 (adj.)"), ("affinity", "친밀감 (n.)"), ("amity", "우호 (n.)")],
            "자기 부족에게는 이타적(unselfish)이지만 타 부족에는 적대감(enmity)을 품었습니다."
        ),
        (
            "Economic History", "산업혁명과 생활수준 논쟁 (Standard of Living Debate)",
            "Early mechanization multiplied [A] productivity, but imposed [B] squalor on factory slums",
            "산업적 성공([A] 기하급수적 생산량) vs 인도적 비극([B] 끔찍한 도시 빈민촌)",
            "During the early Industrial Revolution, steam mechanization yielded ________ national manufacturing outputs, but simultaneous urban crowding subjected factory proletariats to ________ living conditions.",
            "초기 산업혁명 동안 증기 기계화는 ________ 국가 제조업 산출량을 낳았지만, 동시적인 도시 과밀화는 공장 프롤레타리아트를 ________ 주거 환경에 처하게 했다.",
            "colossal — squalid",
            ["meager — luxurious", "scanty — opulent", "negligible — palatial"],
            [("colossal", "거대한, 엄청난 (adj.)"), ("squalid", "비참한, 지저분한 (adj.)"), ("meager", "빈약한 (adj.)"), ("luxurious", "호화로운 (adj.)"), ("opulent", "부유한 (adj.)")],
            "생산량은 거대했지만(colossal) 생활 환경은 비참했다(squalid)가 대조됩니다."
        ),
        (
            "Bioethics & Xenotransplantation", "이종 이식의 기회와 위협 (Porcine Organ Transplants)",
            "Genetically edited pig kidneys could [A] donor shortages, but risk transferring [B] zoonoses",
            "희망([A] 장기 부족 해소) vs 위험([B] 잠복된 동물성 바이러스 전파)",
            "Xenotransplantation utilizing cloned porcine organs promises to completely ________ persistent shortages on human donor waiting lists, yet researchers must stringently ensure that such surgeries do not transmit ________ retroviruses to recipients.",
            "복제된 돼지 장기를 활용하는 이종 이식은 인간 기증자 대기자 명단의 지속적인 부족을 완전히 ________할 것으로 기대되지만, 연구자들은 그러한 수술이 수혜자에게 ________ 레트로바이러스를 전파하지 않도록 엄격하게 보장해야 한다.",
            "remedy — dormant",
            ["exacerbate — harmless", "aggravate — benign", "compound — inert"],
            [("remedy", "해결하다, 치료하다 (v.)"), ("dormant", "휴면 상태의, 잠복된 (adj.)"), ("exacerbate", "악화시키다 (v.)"), ("benign", "무해한 (adj.)"), ("inert", "비활성의 (adj.)")],
            "부족 문제를 해결하지만(remedy) 잠복된(dormant) 바이러스 위험이 있습니다."
        ),
        (
            "Sociology of Bureaucracy", "베버의 합리성과 쇠창살 (The Iron Cage)",
            "Bureaucratic rationality eliminated [A] nepotism, but trapped citizens in a soulless [B]",
            "긍정적 기여([A] 자의적 정고주의 근절) ↔ 비극적 귀결([B] 메마른 관료제의 쇠창살)",
            "Max Weber observed that modern bureaucratic legalism successfully eradicated capricious ________ in public administration, but warned it simultaneously imprisoned the human spirit in a rationalized 'iron ________.'",
            "막스 베버는 현대 관료적 법치주의가 공공 행정에서 변덕스러운 ________을 성공적으로 근절했지만, 그것이 동시에 인간 정신을 합리화된 '쇠________' 속에 가두었다고 경고했다.",
            "nepotism — cage",
            ["fairness — prison", "equity — dungeon", "impartiality — tomb"],
            [("nepotism", "친족 등용, 족벌주의 (n.)"), ("cage", "새장, 감옥 (n.)"), ("fairness", "공정성 (n.)"), ("equity", "형평성 (n.)"), ("impartiality", "공평무사 (n.)")],
            "연줄과 족벌주의(nepotism)를 없앴으나 영혼 없는 쇠창살(iron cage)에 갇혔습니다."
        ),
        (
            "Macroeconomics & Modern Monetary Theory", "재정 적자와 인플레이션 제약 (Fiscal Limits)",
            "A sovereign government can never involuntarily [A] in its own currency, but unlimited spending triggers [B] hyperinflation",
            "이론적 무제한([A] 채무불이행 불가능) ↔ 물리적 제약([B] 파괴적 초인플레이션)",
            "Modern Monetary Theory posits that a currency-issuing sovereign state can never technically ________ on debts denominated in its own fiat money, but cautions that unconstrained deficit monetization will unleash ________ hyperinflation once productive capacity is maxed.",
            "현대 통화 이론(MMT)은 자국 법정 화폐로 표시된 부채에 대해 통화 발행 주권국이 기술적으로 결코 ________할 수 없다고 상정하지만, 생산 능력이 한계에 도달하면 통제되지 않는 적자 화폐화가 ________ 초인플레이션을 촉발할 것이라고 경고한다.",
            "default — ruinous",
            ["prosper — benign", "flourish — harmless", "survive — negligible"],
            [("default", "채무불이행하다 (v.)"), ("ruinous", "파멸적인 (adj.)"), ("prosper", "번영하다 (v.)"), ("benign", "양성의 (adj.)"), ("flourish", "번성하다 (v.)")],
            "파산(default)하지는 않지만 파멸적인(ruinous) 초인플레이션을 낳을 수 있습니다."
        )
    ]

    for idx, d in enumerate(data):
        theme, logicType, clue, direction, question, questionKo, correct, distractors, vocab, explanation = d
        opts = [correct] + distractors
        random.seed(3000 + idx)
        random.shuffle(opts)
        ans = opts.index(correct)
        
        vocab_list = [{"word": w, "meaning": m} for w, m in vocab]
        
        items.append({
            "id": f"tl-{idx+121:03d}",
            "level": 3,
            "levelLabel": "Lv.3 상급",
            "theme": theme,
            "category": "더블 빈칸 (Double Blank)",
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
    q = get_level3_questions()
    print(f"Generated {len(q)} Level 3 questions.")
