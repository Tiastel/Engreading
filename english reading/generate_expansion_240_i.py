# -*- coding: utf-8 -*-
"""
generate_expansion_240_i.py
10 Intermediate passages (i-71 to i-80)
B1-B2 level, authoritative sources, sentence chunks, vocabulary, grammar, and 3 deducible comprehension questions per passage.
"""

def get_expansion_240_i():
    return [
        (
            "i-71",
            "The Circadian Secretion of Melatonin",
            "멜라토닌의 일주기 분비와 수면 조절 기전",
            "Endocrinology & Neuroscience",
            "Harvard Medical School Sleep Medicine Guide",
            "멜라토닌은 시신경교차상핵(SCN)의 광신호 제어를 받아 송과선에서 분비되며, 어두워질 때 혈중 농도가 급상승하여 수면을 유도합니다.",
            [
                ("Melatonin is a pleiotropic hormone / synthesized primarily by the pineal gland / in strict coordination with the 24-hour solar cycle.",
                 "멜라토닌은 24시간 태양 주기에 엄격히 맞추어 / 주로 송과선에 의해 합성되는 / 다면 발현성 호르몬입니다.",
                 "Melatonin is a pleiotropic hormone / synthesized primarily by the pineal gland / in strict coordination / with the 24-hour solar cycle."),
                ("Specialized photoreceptors in the mammalian retina / detect ambient blue wavelength light / and transmit inhibitory signals to the suprachiasmatic nucleus.",
                 "포유류 망막의 특수화된 광수용체는 / 주변의 청색 파장 빛을 감지하여 / 시신경교차상핵(SCN)으로 억제성 신호를 전달합니다.",
                 "Specialized photoreceptors in the mammalian retina / detect ambient blue wavelength light / and transmit inhibitory signals / to the suprachiasmatic nucleus."),
                ("During daylight, / this neural pathway effectively suppresses melatonin synthesis, / keeping individuals alert and physiologically active.",
                 "낮 시간 동안, / 이 신경 경로는 멜라토닌 합성을 효과적으로 억제하여, / 개인이 각성되고 생리적으로 활성화된 상태를 유지하도록 합니다.",
                 "During daylight, / this neural pathway effectively suppresses melatonin synthesis, / keeping individuals alert / and physiologically active."),
                ("With the onset of darkness, / the inhibition ceases, / precipitating a surge in circulating melatonin that binds to brain receptors to induce sleepiness.",
                 "어둠이 시작되면, / 억제가 중단되고, / 순환 멜라토닌의 급증을 촉발하여 뇌 수용체와 결합함으로써 졸음을 유도합니다.",
                 "With the onset of darkness, / the inhibition ceases, / precipitating a surge in circulating melatonin / that binds to brain receptors / to induce sleepiness.")
            ],
            [
                ("pleiotropic", "adj.", "다발성의, 다기능의", "Insulin exerts pleiotropic metabolic effects across diverse tissues."),
                ("retina", "n.", "망막", "Photoreceptor rods and cones line the sensory retina at the back of the eye."),
                ("suppress", "v.", "억제하다, 진압하다", "Cold medicine helps suppress persistent coughing fits."),
                ("precipitate", "v.", "촉발하다, 침전시키다", "Sudden interest rate hikes precipitated a sharp stock market selloff.")
            ],
            [
                ("synthesized primarily by ~", "과거분사구가 명사 a pleiotropic hormone을 수식합니다."),
                ("keeping individuals alert", "'keep + 목적어 + 형용사' 구문으로 '목적어를 형용사한 상태로 유지하다'를 뜻합니다.")
            ],
            [
                ("Where is melatonin primarily synthesized in the human body?",
                 "인간의 몸에서 멜라토닌은 주로 어디에서 합성되는가?",
                 ["In the adrenal cortex", "By the pineal gland", "Inside bone marrow", "Inside thyroid cartilage"],
                 1,
                 "첫 문장에 송과선(the pineal gland)에 의해 주로 합성된다고 나와 있습니다."),
                ("What effect does daylight have on melatonin production?",
                 "낮의 햇빛은 멜라토닌 생성에 어떤 영향을 미치는가?",
                 ["It multiplies melatonin production by ten times.", "It effectively suppresses melatonin synthesis.", "It permanently damages the pineal gland.", "It converts melatonin into pure adrenaline."],
                 1,
                 "세 번째 문장에 멜라토닌 합성을 효과적으로 억제한다고 명시되어 있습니다."),
                ("What happens when darkness begins according to the passage?",
                 "본문에 따르면 어둠이 찾아올 때 무슨 일이 일어나는가?",
                 ["Inhibition ceases, causing a melatonin surge that induces sleepiness.", "The retina completely loses its ability to see forever.", "The heart stops pumping blood until sunrise.", "Body temperature rises to extreme fever levels."],
                 0,
                 "마지막 문장에 억제가 멈추고 멜라토닌이 급증하여 졸음을 유도한다고 설명합니다.")
            ]
        ),
        (
            "i-72",
            "The Keynesian Multiplier Effect",
            "케인스 승수 효과와 총수요의 경제학",
            "Macroeconomics",
            "The Brookings Institution & John Maynard Keynes Theory",
            "정부 지출이나 투자의 초기 증가는 한계소비성향을 타고 연쇄적인 소득 창출을 유발하여 최종적으로 초기 투자액 이상의 총산출 증대를 가져옵니다.",
            [
                ("The multiplier effect, / conceptualized by British economist John Maynard Keynes, / explains how autonomous expenditure generates magnified national income.",
                 "영국 경제학자 존 메이너드 케인스에 의해 개념화된 / 승수 효과는 / 독립적인 지출이 어떻게 증폭된 국민 소득을 창출하는지를 설명합니다.",
                 "The multiplier effect, / conceptualized by British economist John Maynard Keynes, / explains how autonomous expenditure / generates magnified national income."),
                ("When a government injects capital into public infrastructure, / contractors and workers receive immediate wages and profits.",
                 "정부가 공공 인프라에 자본을 투입할 때, / 도급업자와 노동자들은 즉각적인 임금과 이윤을 수령합니다.",
                 "When a government injects capital / into public infrastructure, / contractors and workers / receive immediate wages and profits."),
                ("Recipients spend a substantial fraction of this new earnings / determined by their marginal propensity to consume (MPC), / stimulating downstream businesses.",
                 "수령자들은 한계소비성향(MPC)에 의해 결정되는 / 이 새로운 소득의 상당 부분을 지출하며, / 이는 후속 연관 기업들을 자극합니다.",
                 "Recipients spend a substantial fraction / of this new earnings / determined by their marginal propensity to consume (MPC), / stimulating downstream businesses."),
                ("Through successive rounds of recirculated spending, / the ultimate expansion in national economic output / substantially exceeds the initial injection.",
                 "순환되는 지출의 연속적인 라운드를 거치면서, / 국민 경제 총산출의 최종적인 확장은 / 초기 투입액을 상당히 초과하게 됩니다.",
                 "Through successive rounds of recirculated spending, / the ultimate expansion / in national economic output / substantially exceeds the initial injection.")
            ],
            [
                ("autonomous", "adj.", "독립적인, 자율적인", "Autonomous investment is driven by long-term policy rather than current income."),
                ("propensity", "n.", "성향, 경향", "He demonstrated a natural propensity for mathematical problem-solving."),
                ("downstream", "adj./adv.", "후속의, 연관된, 하류의", "Automobile assembly plants support hundreds of downstream parts suppliers."),
                ("successive", "adj.", "연속적인, 잇따른", "The company reported record quarterly revenues for five successive years.")
            ],
            [
                ("explains how + 절", "'~가 어떻게 …하는지 설명하다' 간접의문문 목적어절입니다."),
                (", stimulating ~", "연속적 결과를 나타내는 분사구문으로 '후속 기업들을 자극하면서'로 해석됩니다.")
            ],
            [
                ("What does the Keynesian multiplier effect explain?",
                 "케인스 승수 효과는 무엇을 설명하는가?",
                 ["How to manufacture physical bank coins cheaply", "How autonomous expenditure generates magnified national income", "Why banks should never lend capital to businesses", "How tax cuts permanently eliminate government debt"],
                 1,
                 "첫 문장에 독립 지출이 어떻게 증폭된 국민 소득을 창출하는지 설명한다고 나와 있습니다."),
                ("What economic factor determines what fraction of new income is spent?",
                 "새로운 소득 중 어느 정도의 비율이 지출될지를 결정하는 경제적 요인은 무엇인가?",
                 ["The gold standard reserve ratio", "The marginal propensity to consume (MPC)", "The geographic size of the nation", "The seasonal ocean tide height"],
                 1,
                 "세 번째 문장에 한계소비성향(MPC)에 의해 결정된다고 명시되어 있습니다."),
                ("How does the final expansion in economic output compare to the initial government injection?",
                 "최종적인 경제적 총산출 확장은 초기 정부 투입액과 비교하여 어떠한가?",
                 ["It is exactly zero dollars.", "It substantially exceeds the initial injection.", "It is always cut in half due to inflation.", "It is completely transformed into foreign currency reserves."],
                 1,
                 "마지막 문장에 최종 확장이 초기 투입액을 상당히 초과한다고(substantially exceeds) 명시되어 있습니다.")
            ]
        ),
        (
            "i-73",
            "Hemostasis and the Blood Coagulation Cascade",
            "지혈 작용과 혈액 응고 연쇄 반응",
            "Hematology & Physiology",
            "Johns Hopkins Medicine Pathology & Vascular Biology",
            "혈관이 손상되면 혈소판이 즉각 부착되어 일차 지혈전을 형성하고, 응고 인자들의 효소 연쇄 반응을 통해 피브린 그물이 형성되어 출혈을 막습니다.",
            [
                ("Hemostasis is the vital physiological process / that arrests bleeding from damaged blood vessels / to maintain vascular integrity.",
                 "지혈은 혈관의 완전성을 유지하기 위해 / 손상된 혈관으로부터의 출혈을 멈추게 하는 / 필수적인 생리적 과정입니다.",
                 "Hemostasis is the vital physiological process / that arrests bleeding / from damaged blood vessels / to maintain vascular integrity."),
                ("Upon endothelial injury, / circulatory platelets adhere to exposed subendothelial collagen / and undergo rapid activation.",
                 "혈관 내피세포가 손상되면, / 순환 혈소판들이 노출된 내피하 콜라겐에 부착되어 / 신속한 활성화를 거칩니다.",
                 "Upon endothelial injury, / circulatory platelets adhere / to exposed subendothelial collagen / and undergo rapid activation."),
                ("These activated platelets recruit additional platelets / to aggregate into an initial temporary hemostatic plug.",
                 "이 활성화된 혈소판들은 추가적인 혈소판들을 모집하여 / 초기 임시 지혈전을 이루도록 응집시킵니다.",
                 "These activated platelets recruit additional platelets / to aggregate into an initial temporary hemostatic plug."),
                ("Concurrently, a biochemical coagulation cascade converts soluble fibrinogen into insoluble fibrin strands, / weaving a durable meshwork that stabilizes the clot.",
                 "동시에, 생화학적 응고 연쇄 반응이 가용성 피브리노겐을 불용성 피브린 가닥으로 전환하여, / 혈전을 안정화하는 내구성 있는 그물망을 짭니다.",
                 "Concurrently, / a biochemical coagulation cascade converts soluble fibrinogen / into insoluble fibrin strands, / weaving a durable meshwork / that stabilizes the clot.")
            ],
            [
                ("arrest", "v.", "멈추게 하다, 저지하다, 체포하다", "Prompt administration of medication arrested the spread of the infection."),
                ("endothelial", "adj.", "혈관 내피의", "Endothelial dysfunction contributes to arterial plaque formation."),
                ("aggregate", "v.", "응집하다, 모이다", "Small molecules aggregate to form protective colloidal clusters."),
                ("meshwork", "n.", "그물망, 망상 구조", "A dense meshwork of collagen fibers supports the dermis layer.")
            ],
            [
                ("Upon + 명사", "'~하자마자, ~ 시에' 시간의 즉시성을 나타내는 전치사구입니다."),
                ("converts A into B", "'A를 B로 전환하다/바꾸다' 변화의 전치사 into 구문입니다.")
            ],
            [
                ("What do platelets adhere to upon endothelial injury?",
                 "혈관 내피 손상 시 혈소판은 어디에 부착되는가?",
                 ["To floating red blood cells only", "To exposed subendothelial collagen", "To stomach acid enzymes", "To external air dust particles"],
                 1,
                 "두 번째 문장에 노출된 내피하 콜라겐(exposed subendothelial collagen)에 부착된다고 나와 있습니다."),
                ("What do activated platelets form initially at the injury site?",
                 "활성화된 혈소판들은 손상 부위에서 초기에 무엇을 형성하는가?",
                 ["A permanent scar of bone", "A temporary hemostatic plug", "An open valve that speeds blood loss", "A cluster of malignant white cells"],
                 1,
                 "세 번째 문장에 임시 지혈전(initial temporary hemostatic plug)을 형성한다고 명시되어 있습니다."),
                ("What does the coagulation cascade convert soluble fibrinogen into?",
                 "응고 연쇄 반응은 가용성 피브리노겐을 무엇으로 전환하는가?",
                 ["Insoluble fibrin strands", "Liquid cholesterol droplets", "Gaseous carbon monoxide", "Pure mineral calcium crystals"],
                 0,
                 "마지막 문장에 불용성 피브린 가닥(insoluble fibrin strands)으로 전환한다고 설명합니다.")
            ]
        ),
        (
            "i-74",
            "Asymmetric Information and the Lemons Market",
            "정보 비대칭성과 개똥차(Lemons) 시장의 실패",
            "Microeconomics",
            "Quarterly Journal of Economics & George Akerlof Nobel Lecture",
            "조지 애컬로프는 판매자가 구매자보다 상품 품질 정보를 더 많이 아는 시장에서 불량품만 남고 우량품이 퇴출되는 역선택이 발생함을 증명했습니다.",
            [
                ("In his pathbreaking 1970 paper, / George Akerlof examined markets / plagued by asymmetric information between buyers and sellers.",
                 "자신의 획기적인 1970년 논문에서, / 조지 애컬로프는 구매자와 판매자 간의 정보 비대칭성으로 / 고통받는 시장들을 조사했습니다.",
                 "In his pathbreaking 1970 paper, / George Akerlof examined markets / plagued by asymmetric information / between buyers and sellers."),
                ("Using the pre-owned automobile market as an exemplar, / he noted that sellers know whether a car is a reliable vehicle or a defective 'lemon,' / while buyers cannot discern quality beforehand.",
                 "중고차 시장을 대표적인 예로 활용하여, / 그는 구매자가 사전에 품질을 식별할 수 없는 반면, / 판매자는 차가 신뢰할 만한 차량인지 결함투성이 '개똥차(lemon)'인지를 안다는 점에 주목했습니다.",
                 "Using the pre-owned automobile market as an exemplar, / he noted that sellers know / whether a car is a reliable vehicle or a defective 'lemon,' / while buyers cannot discern quality beforehand."),
                ("Fearing they might purchase a substandard lemon, / rational buyers are only willing to pay an average market price.",
                 "기준 미달의 결함차를 살지도 모른다는 두려움 때문에, / 합리적인 구매자들은 오직 평균 시장 가격만을 지불하려 합니다.",
                 "Fearing they might purchase a substandard lemon, / rational buyers are only willing / to pay an average market price."),
                ("This discounted valuation drives sellers of high-quality cars out of the market, / resulting in adverse selection where only defective goods remain.",
                 "이러한 할인된 가치 평가는 고품질 차량 판매자들을 시장 밖으로 몰아내며, / 결국 결함 있는 상품들만 남게 되는 역선택을 초래합니다.",
                 "This discounted valuation drives sellers of high-quality cars out of the market, / resulting in adverse selection / where only defective goods remain.")
            ],
            [
                ("exemplar", "n.", "모범, 전형적 본보기", "The ancient Greek Parthenon stands as an exemplar of classical architecture."),
                ("discern", "v.", "식별하다, 알아차리다", "Trained appraisers can easily discern genuine diamonds from synthetic replicas."),
                ("substandard", "adj.", "표준 이하의, 열악한", "Substandard wiring poses severe fire hazards in old buildings."),
                ("adverse selection", "n.", "역선택 (정보 비대칭으로 인한 불리한 선택)", "Adverse selection frequently undermines unregulated private insurance markets.")
            ],
            [
                ("whether A or B", "'A인지 B인지' 의문사 명사절 접속사입니다."),
                ("resulting in + 명사", "결과를 나타내는 분사구문으로 '그 결과 ~을 초래하다'로 해석됩니다.")
            ],
            [
                ("What asymmetric information exists in the pre-owned car market according to Akerlof?",
                 "애컬로프에 따르면 중고차 시장에 어떤 정보 비대칭이 존재하는가?",
                 ["Buyers know mechanical flaws that sellers have never noticed.", "Sellers know whether a car is reliable or defective, while buyers cannot discern it beforehand.", "Governments hide the prices of all used cars from dealerships.", "Insurance companies secretly set tire pressure for all vehicles."],
                 1,
                 "두 번째 문장에 판매자는 차량 결함 유무를 아는 반면 구매자는 사전에 분별할 수 없다고 나와 있습니다."),
                ("Why are rational buyers only willing to pay an average price?",
                 "왜 합리적인 구매자들은 평균 가격만을 지불하려 하는가?",
                 ["Because they fear they might purchase a substandard lemon.", "Because luxury cars are completely illegal to own.", "Because used car sellers refuse to accept any cash.", "Because the government sets strict mandatory maximum prices."],
                 0,
                 "세 번째 문장에 결함 있는 차량(lemon)을 살지도 모른다는 두려움 때문이라고 설명합니다."),
                ("What is the consequence of adverse selection described in the text?",
                 "본문에 기술된 역선택의 결과는 무엇인가?",
                 ["High-quality sellers are driven out, leaving only defective goods in the market.", "Every single car manufacturer doubles its profits overnight.", "All cars are distributed completely free of charge.", "Buyers start purchasing airplanes instead of automobiles."],
                 0,
                 "마지막 문장에 우량차 판매자가 시장을 떠나 결함 상품들만 남게 된다고 나와 있습니다.")
            ]
        ),
        (
            "i-75",
            "Wavefunction Collapse in Quantum Physics",
            "양자역학의 파동함수 붕괴와 관측자 효과",
            "Quantum Mechanics",
            "Nature Physics & Erwin Schrödinger Foundation",
            "양자 입자는 측정되기 전까지 여러 상태가 중첩된 확률 파동으로 존재하지만, 관측이 이루어지는 순간 하나의 확정된 고유상태로 붕괴합니다.",
            [
                ("In standard quantum mechanics, / the complete physical state of an isolated subatomic system / is mathematically formulated by a wavefunction.",
                 "표준 양자역학에서, / 고립된 아원자 계의 완전한 물리적 상태는 / 파동함수에 의해 수학적으로 공식화됩니다.",
                 "In standard quantum mechanics, / the complete physical state / of an isolated subatomic system / is mathematically formulated by a wavefunction."),
                ("Governed by the Schrödinger equation, / this wavefunction evolves deterministically, / encoding a superposition of multiple potential outcomes.",
                 "슈뢰딩거 방정식에 의해 지배받는 / 이 파동함수는 결정론적으로 진화하며, / 여러 잠재적 결과들의 중첩을 부호화합니다.",
                 "Governed by the Schrödinger equation, / this wavefunction evolves deterministically, / encoding a superposition / of multiple potential outcomes."),
                ("However, / the moment an external apparatus performs a physical measurement, / this linear superposition abruptly vanishes.",
                 "그러나, / 외부 측정 장치가 물리적 측정을 수행하는 순간, / 이 선형적 중첩 상태는 갑작스럽게 사라집니다.",
                 "However, / the moment an external apparatus performs a physical measurement, / this linear superposition abruptly vanishes."),
                ("The wavefunction instantaneously collapses into a single definite eigenstate, / whose probability of observation is proportional to the square of its amplitude.",
                 "파동함수는 단 하나의 확정적인 고유상태로 즉각 붕괴하며, / 그 관측 확률은 진폭의 제곱에 비례합니다.",
                 "The wavefunction instantaneously collapses / into a single definite eigenstate, / whose probability of observation / is proportional to the square of its amplitude.")
            ],
            [
                ("superposition", "n.", "중첩 (여러 상태가 공존함)", "Quantum computers exploit superposition to evaluate algorithms in parallel."),
                ("apparatus", "n.", "장치, 기구", "The chemistry laboratory was equipped with high-vacuum distillation apparatus."),
                ("eigenstate", "n.", "고유상태 (양자 관측 시 확정되는 상태)", "Measurement projects the system onto an eigenstate of the observable operator."),
                ("amplitude", "n.", "진폭, 크기", "The seismic wave's amplitude diminished as it traveled away from the epicenter.")
            ],
            [
                ("Governed by ~", "과거분사구로 주절의 주어 this wavefunction을 수식합니다."),
                ("the moment + 절", "'~하는 순간에' 시간의 접속사 역할을 하는 표현입니다.")
            ],
            [
                ("What does the quantum wavefunction encode before measurement?",
                 "측정 전 양자 파동함수는 무엇을 부호화하고 있는가?",
                 ["The exact weight of classical steel spheres", "A superposition of multiple potential outcomes", "The temperature of the experimental room", "The financial budget of the university"],
                 1,
                 "두 번째 문장에 'encoding a superposition of multiple potential outcomes'라고 나와 있습니다."),
                ("What happens the moment a physical measurement is performed?",
                 "물리적 측정이 수행되는 순간 무슨 일이 일어나는가?",
                 ["The particle permanently turns into light.", "The linear superposition abruptly vanishes and collapses into a single eigenstate.", "The measuring apparatus melts from immense heat.", "The Schrödinger equation becomes mathematically invalid forever."],
                 1,
                 "세 번째와 네 번째 문장에 중첩이 사라지고 단 하나의 고유상태로 즉각 붕괴한다고 설명합니다."),
                ("How is the probability of observing a specific state calculated?",
                 "특정 상태를 관측할 확률은 어떻게 계산되는가?",
                 ["It is proportional to the square of its amplitude.", "It depends on the time of day shown on wall clocks.", "It is inversely related to atmospheric humidity.", "It is determined by counting how many scientists are in the room."],
                 0,
                 "마지막 문장에 진폭의 제곱에 비례한다(proportional to the square of its amplitude)고 명시되어 있습니다.")
            ]
        ),
        (
            "i-76",
            "Chemosynthesis at Hydrothermal Vents",
            "심해 열수구의 화학합성과 극한 생태계",
            "Marine Ecology",
            "Woods Hole Oceanographic Institution (WHOI) Deep-Sea Research",
            "태양빛이 닿지 않는 심해 열수구에서 화학합성 박테리아는 유독한 황화수소를 산화하여 유기물을 합성하며, 놀라운 심해 오아시스를 형성합니다.",
            [
                ("Deep on the ocean floor along midocean ridges, / hydrothermal vents spew superheated mineral fluids / into pitch-black freezing seawater.",
                 "해령을 따라 위치한 해저 깊은 곳에서, / 열수구는 칠흑같이 어둡고 차가운 바닷물 속으로 / 과열된 광물 유체를 뿜어냅니다.",
                 "Deep on the ocean floor along midocean ridges, / hydrothermal vents spew superheated mineral fluids / into pitch-black freezing seawater."),
                ("Because sunlight never reaches these abyssal depths, / the surrounding thriving ecosystem does not rely on photosynthesis.",
                 "햇빛이 이 심해의 깊이에 결코 도달하지 않기 때문에, / 주변의 번성하는 생태계는 광합성에 의존하지 않습니다.",
                 "Because sunlight never reaches these abyssal depths, / the surrounding thriving ecosystem / does not rely on photosynthesis."),
                ("Instead, primary production is driven by chemosynthetic bacteria / that oxidize toxic dissolved hydrogen sulfide / to synthesize energy-rich organic compounds.",
                 "대신에, 일차 생산은 유독한 용존 황화수소를 산화시켜 / 에너지가 풍부한 유기 화합물을 합성하는 / 화학합성 박테리아에 의해 추진됩니다.",
                 "Instead, primary production is driven / by chemosynthetic bacteria / that oxidize toxic dissolved hydrogen sulfide / to synthesize energy-rich organic compounds."),
                ("These resilient microbes form dense bacterial mats / or live symbiotically within giant tube worms and clams, / anchoring a vibrant food web independent of solar energy.",
                 "이 강인한 미생물들은 빽빽한 박테리아 매트를 형성하거나 / 거대 관벌레와 조개 내부에서 공생하며, / 태양 에너지에 독립적인 활기찬 먹이사슬의 닻을 내립니다.",
                 "These resilient microbes form dense bacterial mats / or live symbiotically within giant tube worms and clams, / anchoring a vibrant food web / independent of solar energy.")
            ],
            [
                ("spew", "v.", "뿜어내다, 분출하다", "Volcanoes spew ash and sulfurous gases high into the stratosphere."),
                ("abyssal", "adj.", "심해의, 끝없이 깊은", "Abyssal trenches harbor organisms adapted to immense hydrostatic pressures."),
                ("chemosynthetic", "adj.", "화학합성의", "Chemosynthetic communities thrive near geothermal springs."),
                ("symbiotically", "adv.", "공생하여", "Legume roots host nitrogen-fixing bacteria symbiotically.")
            ],
            [
                ("does not rely on ~", "'~에 의존하지 않는다' 부정 표현입니다."),
                (", anchoring ~", "결과/상태를 나타내는 분사구문으로 '먹이사슬을 지탱하면서'로 해석됩니다.")
            ],
            [
                ("Why does the ecosystem around hydrothermal vents not use photosynthesis?",
                 "왜 열수구 주변의 생태계는 광합성을 이용하지 않는가?",
                 ["Because the water is too cold for green plants to sprout", "Because sunlight never reaches these abyssal depths", "Because marine animals eat all chlorophyll pigments instantly", "Because hydrothermal fluids dissolve all plant roots"],
                 1,
                 "두 번째 문장에 햇빛이 이 심해의 깊이에 결코 도달하지 않기 때문이라고 명시되어 있습니다."),
                ("What do chemosynthetic bacteria oxidize to synthesize organic compounds?",
                 "화학합성 박테리아는 유기 화합물을 합성하기 위해 무엇을 산화시키는가?",
                 ["Fresh surface rainwater", "Toxic dissolved hydrogen sulfide", "Solid gold granules in bedrock", "Radioactive granite pebbles"],
                 1,
                 "세 번째 문장에 유독한 용존 황화수소(toxic dissolved hydrogen sulfide)를 산화시킨다고 나와 있습니다."),
                ("How do giant tube worms and clams interact with these microbes?",
                 "거대 관벌레와 조개는 이 미생물들과 어떻게 상호작용하는가?",
                 ["They hunt them down and eliminate them completely.", "They live symbiotically with them.", "They use them as hard building stones for houses.", "They avoid them because the bacteria are poisonous to animals."],
                 1,
                 "마지막 문장에 이 미생물들과 공생하며(live symbiotically) 살아간다고 설명합니다.")
            ]
        ),
        (
            "i-77",
            "Comparative Cognition and Animal Tool Use",
            "비교인지학과 동물의 도구 제작 능력",
            "Animal Cognition & Ethology",
            "Nature & Cambridge Comparative Cognition Research",
            "동물이 도구를 제작하고 사용하는 능력은 인간만의 고유한 특성이 아니며, 까마귀과 조류와 유인원에서 고도의 인지적 계획 능력이 확인되었습니다.",
            [
                ("For decades, / anthropologists considered sophisticated tool manufacture / the definitive hallmark separating humanity from other animals.",
                 "수십 년 동안, / 인류학자들은 정교한 도구 제작을 / 인간을 다른 동물들과 구분 짓는 결정적인 특징으로 여겼습니다.",
                 "For decades, / anthropologists considered sophisticated tool manufacture / the definitive hallmark / separating humanity from other animals."),
                ("However, / modern comparative cognition studies have fundamentally overturned this anthropocentric assumption.",
                 "그러나, / 현대의 비교인지학 연구들은 이러한 인간중심적인 가정을 근본적으로 뒤엎었습니다.",
                 "However, / modern comparative cognition studies / have fundamentally overturned / this anthropocentric assumption."),
                ("New Caledonian crows skillfully bend pliable twigs into functional hooks / to extract inaccessible beetle larvae from tree hollows.",
                 "뉴칼레도니아 까마귀는 나무 구멍에서 접근 불가능한 딱정벌레 유충을 꺼내기 위해 / 유연한 잔가지를 기능성 갈고리로 능숙하게 구부립니다.",
                 "New Caledonian crows skillfully bend pliable twigs / into functional hooks / to extract inaccessible beetle larvae / from tree hollows."),
                ("Furthermore, / chimpanzees deliberately select specific stone anvils / based on density and shape to crack open tough palm nuts, / demonstrating foresight and causal reasoning.",
                 "게다가, / 침팬지는 단단한 야자 열매를 깨기 위해 / 밀도와 형태에 기초하여 특정 돌 모루를 신중하게 선택하며, / 이는 선견지명과 인과적 추론 능력을 입증합니다.",
                 "Furthermore, / chimpanzees deliberately select specific stone anvils / based on density and shape / to crack open tough palm nuts, / demonstrating foresight and causal reasoning.")
            ],
            [
                ("hallmark", "n.", "결정적 특징, 품질 증명", "Attention to nuance and empirical rigor is the hallmark of serious scholarship."),
                ("anthropocentric", "adj.", "인간중심적인", "Environmental ethics challenges anthropocentric views of nature."),
                ("pliable", "adj.", "유연한, 잘 휘는", "Pliable copper wire is easy to bend into decorative shapes."),
                ("causal", "adj.", "인과관계의", "Epidemiologists established a causal link between smoking and lung damage.")
            ],
            [
                ("considered A B", "'A를 B로 간주했다' 5형식 구조입니다."),
                (", demonstrating ~", "분사구문으로 앞선 행동이 무엇을 시사하는지 설명하며 '선견지명과 인과적 추론을 입증하면서'로 해석됩니다.")
            ],
            [
                ("What did anthropologists historically consider the definitive hallmark separating humans from animals?",
                 "인류학자들은 역사적으로 인간과 동물을 구별하는 결정적 특징으로 무엇을 간주했는가?",
                 ["The ability to see distant stars at night", "Sophisticated tool manufacture", "The capacity to digest cooked plant sugars", "Having four fingers and one thumb"],
                 1,
                 "첫 문장에 정교한 도구 제작(sophisticated tool manufacture)을 결정적 특징으로 여겼다고 나와 있습니다."),
                ("How do New Caledonian crows extract beetle larvae from tree hollows?",
                 "뉴칼레도니아 까마귀는 나무 구멍에서 딱정벌레 유충을 어떻게 꺼내는가?",
                 ["By dropping heavy rocks on the tree until it splits", "By bending pliable twigs into functional hooks", "By breathing fire into the wood cavity", "By singing musical songs to entice them out"],
                 1,
                 "세 번째 문장에 유연한 잔가지를 기능적 갈고리로 구부려서 꺼낸다고 명시되어 있습니다."),
                ("What cognitive abilities do chimpanzees demonstrate when selecting stone anvils?",
                 "침팬지는 돌 모루를 선택할 때 어떤 인지 능력을 입증하는가?",
                 ["Supernatural psychic powers", "Foresight and causal reasoning", "Complete blind luck without thought", "Automatic mechanical instinct only"],
                 1,
                 "마지막 문장에 선견지명과 인과적 추론(foresight and causal reasoning)을 입증한다고 나와 있습니다.")
            ]
        ),
        (
            "i-78",
            "Fractional Reserve Banking and Credit Creation",
            "지급준비제도와 현대 은행의 신용 창조",
            "Money & Banking",
            "Federal Reserve Bank Educational Bulletin & Monetary Economics",
            "현대 상업은행은 예금 전액을 금고에 보관하는 것이 아니라, 법정지급준비금만 남기고 나머지를 대출함으로써 경제 내 통화량을 창출합니다.",
            [
                ("Modern financial systems operate on a mechanism / known as fractional reserve banking.",
                 "현대 금융 시스템은 부분지급준비제도라 알려진 / 메커니즘을 기반으로 작동합니다.",
                 "Modern financial systems operate / on a mechanism / known as fractional reserve banking."),
                ("Under regulatory mandates, / commercial banks are legally obligated to hold only a small fraction of customer deposits / as liquid cash reserves.",
                 "규제적 명령에 따라, / 상업은행은 고객 예금의 작은 일부만을 / 유동 현금 준비금으로 보유할 법적 의무가 있습니다.",
                 "Under regulatory mandates, / commercial banks are legally obligated / to hold only a small fraction of customer deposits / as liquid cash reserves."),
                ("The remaining excess reserves are channeled into commercial loans / for homebuyers, entrepreneurs, and industrial investments.",
                 "나머지 초과 준비금은 주택 구매자, 기업가, 산업 투자를 위한 / 상업 대출로 공급됩니다.",
                 "The remaining excess reserves / are channeled into commercial loans / for homebuyers, entrepreneurs, / and industrial investments."),
                ("Because these issued loans are redeposited into other banking institutions, / the banking system as a whole creates brand-new money / through the deposit expansion multiplier.",
                 "이렇게 발행된 대출금이 다른 은행 기관에 다시 예금되기 때문에, / 은행 시스템 전체는 예금 확대 승수를 통해 / 완전히 새로운 통화를 창출합니다.",
                 "Because these issued loans are redeposited into other banking institutions, / the banking system as a whole creates brand-new money / through the deposit expansion multiplier.")
            ],
            [
                ("mandate", "n.", "명령, 지시, 권한", "The safety regulator issued a strict mandate regarding airline maintenance."),
                ("obligated", "adj.", "의무가 있는", "Hospitals are ethically obligated to treat emergency patients."),
                ("channeled", "v. (p.p.)", "(자금 등이) 전달되다, 보내지다", "Philanthropic donations were channeled into rural school construction."),
                ("multiplier", "n.", "승수 (증폭 계수)", "The money multiplier indicates how reserves translate into broad money supply.")
            ],
            [
                ("are legally obligated to 동사원형", "'법적으로 ~할 의무가 있다'는 수동 표현입니다."),
                ("as a whole", "'전체로서, 전반적으로' 앞의 the banking system을 수식합니다.")
            ],
            [
                ("What does fractional reserve banking require commercial banks to do?",
                 "부분지급준비제도는 상업은행에 무엇을 요구하는가?",
                 ["Keep 100 percent of all gold coins permanently locked away", "Hold only a small fraction of customer deposits as liquid cash reserves", "Distribute all bank earnings to charity weekly", "Stop issuing mortgages entirely"],
                 1,
                 "두 번째 문장에 고객 예금의 작은 일부만을 유동 준비금으로 보유하도록 의무화한다고 명시되어 있습니다."),
                ("What happens to excess reserves not held in cash?",
                 "현금으로 보유되지 않는 초과 준비금은 어떻게 되는가?",
                 ["They are burned to prevent currency inflation.", "They are channeled into commercial loans for homebuyers and entrepreneurs.", "They are shipped to underground ocean vaults.", "They are used to pay off the national debt overnight."],
                 1,
                 "세 번째 문장에 주택 구매자와 기업가 등을 위한 상업 대출로 공급된다고 나와 있습니다."),
                ("How does the banking system create brand-new money according to the text?",
                 "본문에 따르면 은행 시스템은 어떻게 완전히 새로운 돈을 창출하는가?",
                 ["By printing paper banknotes at local branches secretly", "Through issued loans being redeposited via the deposit expansion multiplier", "By mining gold nuggets from national parks", "By collecting foreign stamps from tourists"],
                 1,
                 "마지막 문장에 대출금이 재예금되면서 예금 확대 승수를 통해 새로운 통화를 창출한다고 설명합니다.")
            ]
        ),
        (
            "i-79",
            "The Physics of Optical Fiber Transmission",
            "광섬유 통신의 물리학과 전반사 원리",
            "Applied Physics & Telecommunications",
            "IEEE Communications Magazine & Corning Optical Physics",
            "광섬유는 굴절률이 높은 코어와 낮은 클래딩 경계면에서 일어나는 전반사 현상을 이용하여 광신호 손실 없이 대륙 간 초고속 데이터 전송을 가능하게 합니다.",
            [
                ("Global telecommunication networks rely overwhelmingly on fiber-optic cables / to transmit digital data across planetary distances.",
                 "전 세계 통신망은 지구적 거리에 걸쳐 디지털 데이터를 전송하기 위해 / 광섬유 케이블에 압도적으로 의존합니다.",
                 "Global telecommunication networks / rely overwhelmingly on fiber-optic cables / to transmit digital data across planetary distances."),
                ("At the center of each strand lies a microscopic glass core / surrounded by an outer layer called cladding / possessing a lower refractive index.",
                 "각 가닥의 중심에는 더 낮은 굴절률을 지닌 / 클래딩이라 불리는 외부 층으로 둘러싸인 / 미세한 유리 코어가 자리 잡고 있습니다.",
                 "At the center of each strand / lies a microscopic glass core / surrounded by an outer layer called cladding / possessing a lower refractive index."),
                ("When pulses of laser light enter the core at an angle shallower than the critical angle, / they cannot escape through the boundary.",
                 "레이저 광 펄스가 임계각보다 더 얕은 각도로 코어에 입사할 때, / 빛은 경계면을 뚫고 빠져나갈 수 없습니다.",
                 "When pulses of laser light enter the core / at an angle shallower than the critical angle, / they cannot escape through the boundary."),
                ("Instead, / the light undergoes continuous total internal reflection, / zigzagging along the glass filament for hundreds of kilometers with virtually zero attenuation.",
                 "대신에, / 빛은 지속적인 전반사를 거쳐, / 사실상 감쇠 없이 수백 킬로미터 동안 유리 필라멘트를 따라 지그재그로 나아갑니다.",
                 "Instead, / the light undergoes continuous total internal reflection, / zigzagging along the glass filament / for hundreds of kilometers / with virtually zero attenuation.")
            ],
            [
                ("overwhelmingly", "adv.", "압도적으로", "Consumers overwhelmingly favored the fuel-efficient hybrid model."),
                ("cladding", "n.", "클래딩 (광섬유 외피 피복)", "Optical cladding confines light waves within the high-index silica core."),
                ("refractive", "adj.", "굴절의", "Diamond owes its brilliant sparkle to a remarkably high refractive index."),
                ("attenuation", "n.", "감쇠, 약화", "Ultra-pure silica glass reduces signal attenuation in long-haul networks.")
            ],
            [
                ("At the center lies ~", "장소 부사구 도치 구문으로 '중심에 유리 코어가 놓여 있다'는 구조입니다."),
                (", zigzagging ~", "동시동작을 나타내는 분사구문으로 '유리 필라멘트를 따라 지그재그로 나아가면서'로 해석됩니다.")
            ],
            [
                ("What property does the outer cladding of an optical fiber possess?",
                 "광섬유의 외부 클래딩은 어떤 성질을 지니고 있는가?",
                 ["It has a lower refractive index than the core.", "It is made of opaque dark iron plates.", "It boils liquid water inside the cable.", "It absorbs 100 percent of all light pulses immediately."],
                 0,
                 "두 번째 문장에 코어보다 더 낮은 굴절률(a lower refractive index)을 가지고 있다고 명시되어 있습니다."),
                ("What condition prevents laser light from escaping the glass core?",
                 "어떤 조건이 레이저 빛이 유리 코어를 탈출하지 못하도록 막아주는가?",
                 ["Entering at an angle shallower than the critical angle", "Freezing the cable below minus eighty degrees", "Coating the fiber in magnetic engine oil", "Running electric alternating current through the glass"],
                 0,
                 "세 번째 문장에 임계각보다 얕은 각도로 입사할 때 빠져나갈 수 없다고 나와 있습니다."),
                ("What optical phenomenon allows light to travel long distances with minimal loss?",
                 "빛이 최소한의 손실로 장거리를 이동하도록 해주는 광학 현상은 무엇인가?",
                 ["Total internal reflection", "Chemical combustion", "Static electrical discharge", "Acoustic resonance"],
                 0,
                 "마지막 문장에 지속적인 전반사(total internal reflection)를 거쳐 나아간다고 설명합니다.")
            ]
        ),
        (
            "i-80",
            "Cognitive Biases and the Framing Effect",
            "인지 편향과 프레이밍 효과의 심리학",
            "Cognitive Psychology & Behavioral Science",
            "Science & Amos Tversky / Daniel Kahneman Decision Studies",
            "동일한 객관적 정보라 할지라도 이익의 틀로 제시되는지 손실의 틀로 제시되는지에 따라 사람들의 위험 감수 태도와 의사결정이 급변합니다.",
            [
                ("The framing effect demonstrates / that human decisions are profoundly influenced by how identical options are semantically formulated.",
                 "프레이밍 효과는 동일한 선택지가 언어적으로 어떻게 구성되는가에 의해 / 인간의 의사결정이 심대한 영향을 받는다는 점을 / 보여줍니다.",
                 "The framing effect demonstrates / that human decisions are profoundly influenced / by how identical options are semantically formulated."),
                ("In a celebrated experiment, / participants were presented with a hypothetical disease outbreak threatening six hundred lives.",
                 "한 유명한 실험에서, / 참가자들에게 600명의 목숨을 위협하는 가상의 질병 발생 상황이 제시되었습니다.",
                 "In a celebrated experiment, / participants were presented / with a hypothetical disease outbreak / threatening six hundred lives."),
                ("When an intervention was framed positively as 'saving two hundred people,' / the vast majority chose the risk-averse certainty option.",
                 "어떤 치료 프로그램이 '200명을 살린다'는 긍정적 틀로 제시되었을 때, / 대다수는 위험을 회피하는 확실성 옵션을 선택했습니다.",
                 "When an intervention was framed positively / as 'saving two hundred people,' / the vast majority chose / the risk-averse certainty option."),
                ("Conversely, / when the mathematically identical outcome was framed negatively as 'four hundred people will die,' / people overwhelmingly favored the risky gamble, / revealing that perceived risk shifts with psychological framing.",
                 "반대로, / 수학적으로 동일한 결과가 '400명이 사망할 것이다'라는 부정적 틀로 제시되었을 때, / 사람들은 압도적으로 위험한 도박을 선호했으며, / 이는 인지된 위험이 심리적 프레이밍에 따라 달라짐을 드러냈습니다.",
                 "Conversely, / when the mathematically identical outcome / was framed negatively as 'four hundred people will die,' / people overwhelmingly favored the risky gamble, / revealing that perceived risk shifts / with psychological framing.")
            ],
            [
                ("semantically", "adv.", "의미론적으로, 언어적으로", "The two phrases are semantically equivalent despite different phrasing."),
                ("hypothetical", "adj.", "가상의, 가설의", "The economics exam tested students using hypothetical market crisis scenarios."),
                ("risk-averse", "adj.", "위험을 회피하는", "Conservative pension funds adopt risk-averse investment portfolios."),
                ("conversely", "adv.", "반대로, 역으로", "Some students excel at writing; conversely, others thrive in mathematics.")
            ],
            [
                ("were presented with ~", "'~을 제시받다, 직면하다' 수동태 구문입니다."),
                (", revealing that ~", "결과/함의를 나타내는 분사구문으로 '그 결과 ~을 드러낸다'로 해석됩니다.")
            ],
            [
                ("What does the framing effect demonstrate about human choices?",
                 "프레이밍 효과는 인간의 선택에 관해 무엇을 보여주는가?",
                 ["Decisions are always made using strict logical calculators.", "Decisions are profoundly influenced by how identical options are semantically formulated.", "Humans only care about monetary coins and ignore human lives.", "All people make identical choices regardless of wording."],
                 1,
                 "첫 문장에 동일한 선택지가 언어적으로 어떻게 구성되는가에 따라 의사결정이 큰 영향을 받는다고 나와 있습니다."),
                ("How did participants react when the program was framed as 'saving 200 people'?",
                 "프로그램이 '200명을 살린다'고 프레이밍되었을 때 참가자들은 어떻게 반응했는가?",
                 ["They chose the risk-averse certainty option.", "They refused to answer any questions.", "They flipped coins randomly.", "They unanimously favored the extreme gamble."],
                 0,
                 "세 번째 문장에 대다수가 위험 회피적인 확실성 옵션을 선택했다고 명시되어 있습니다."),
                ("What happened when the outcome was framed as '400 people will die'?",
                 "결과가 '400명이 사망할 것이다'로 프레이밍되었을 때 무슨 일이 일어났는가?",
                 ["People overwhelmingly favored the risky gamble.", "Every participant immediately left the laboratory.", "Participants demanded to pay a fine.", "They selected the certainty option with 100 percent consensus."],
                 0,
                 "마지막 문장에 사람들이 압도적으로 위험한 도박(the risky gamble)을 선호했다고 설명합니다.")
            ]
        )
    ]
