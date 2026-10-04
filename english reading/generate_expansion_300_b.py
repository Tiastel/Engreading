# -*- coding: utf-8 -*-
"""
generate_expansion_300_b.py
20 Beginner passages (b-81 to b-100)
Completes Beginner tier to exactly 100 passages (b-01 to b-100).
A2-B1 level, authoritative sources, sentence chunks, vocabulary, grammar, and 3 deducible comprehension questions per passage.
"""

def get_expansion_300_b():
    return [
        (
            "b-81",
            "Why Flamingos Have Pink Feathers",
            "플라밍고의 깃털이 분홍색인 이유",
            "Ornithology",
            "Smithsonian's National Zoo & Conservation Biology Institute",
            "플라밍고는 원래 회색 깃털을 갖고 태어나지만, 카로티노이드 색소가 풍부한 조류와 갑각류를 섭취하면서 선명한 분홍빛을 띠게 됩니다.",
            [
                ("Flamingo chicks hatch / with dull grey downy feathers / rather than bright pink plumage.",
                 "플라밍고 새끼는 밝은 분홍색 깃털 대신 / 칙칙한 회색 솜털을 가지고 / 부화합니다.",
                 "Flamingo chicks hatch / with dull grey downy feathers / rather than bright pink plumage."),
                ("Their iconic pink coloration comes entirely from their diet / rich in natural red and yellow pigments called carotenoids.",
                 "그들의 상징적인 분홍빛 색채는 / 카로티노이드라 불리는 천연 붉은색 및 노란색 색소가 풍부한 / 식단에서 전적으로 비롯됩니다.",
                 "Their iconic pink coloration comes entirely from their diet / rich in natural red and yellow pigments / called carotenoids."),
                ("Flamingos filter-feed on microscopic blue-green algae / and tiny brine shrimp in saline wetlands.",
                 "플라밍고는 염호 습지에서 / 미세한 남조류와 / 작은 브라인 쉬림프(풍년새우)를 여과 섭식합니다.",
                 "Flamingos filter-feed / on microscopic blue-green algae / and tiny brine shrimp / in saline wetlands."),
                ("Their digestive enzymes break down the carotenoids in their liver, / depositing the pigments into growing feathers and skin.",
                 "그들의 소화 효소는 간에서 카로티노이드를 분해하여, / 자라나는 깃털과 피부에 색소를 침착시킵니다.",
                 "Their digestive enzymes break down the carotenoids in their liver, / depositing the pigments / into growing feathers and skin.")
            ],
            [
                ("plumage", "n.", "깃털, 깃", "Male peacocks display magnificent iridescent plumage to attract mates."),
                ("coloration", "n.", "천연색, 채색", "Protective coloration helps chameleons blend into foliage."),
                ("saline", "adj.", "염분의, 짠", "Saline lakes have high concentrations of dissolved minerals."),
                ("deposit", "v.", "침전시키다, 맡기다", "Rivers deposit fertile silt along coastal deltas.")
            ],
            [
                ("rather than + 명사", "'~라기보다는' 대조를 나타내는 표현입니다."),
                (", depositing ~", "연속적 결과를 나타내는 분사구문으로 '그 결과 색소를 침착시키면서'로 해석됩니다.")
            ],
            [
                ("What color are flamingo chicks when they hatch?",
                 "플라밍고 새끼는 부화할 때 무슨 색인가?",
                 ["Bright crimson red", "Dull grey", "Vibrant golden yellow", "Pure jet black"],
                 1,
                 "첫 문장에 플라밍고 새끼는 칙칙한 회색 솜털(dull grey downy feathers)을 갖고 태어난다고 나와 있습니다."),
                ("Where does the pink coloration of adult flamingos come from?",
                 "성체 플라밍고의 분홍빛은 어디에서 오는가?",
                 ["From their diet rich in carotenoid pigments", "From direct exposure to solar ultraviolet light", "From rolling in red desert dust", "From paint applied by wildlife rangers"],
                 0,
                 "두 번째 문장에 카로티노이드 색소가 풍부한 식단에서 전적으로 비롯된다고 명시되어 있습니다."),
                ("Where do flamingo enzymes break down carotenoids before depositing them into feathers?",
                 "플라밍고 효소는 색소를 깃털에 침착시키기 전 어디에서 카로티노이드를 분해하는가?",
                 ["In their hollow wing bones", "In their liver", "Inside their webbed feet", "Underneath their tongue"],
                 1,
                 "마지막 문장에 간(in their liver)에서 분해한다고 설명합니다.")
            ]
        ),
        (
            "b-82",
            "The Global Water Cycle",
            "지구 수문 순환의 4단계 메커니즘",
            "Hydrology",
            "U.S. Geological Survey (USGS) Water Science School",
            "지구상의 모든 물은 증발, 증산, 응결, 강수의 끊임없는 순환을 통해 육지와 대기, 대양 사이를 이동합니다.",
            [
                ("The water cycle describes how water continuously circulates / across the Earth and its atmosphere.",
                 "물 순환은 물이 지구와 대기 전역에 걸쳐 / 어떻게 끊임없이 순환하는지를 / 설명합니다.",
                 "The water cycle describes / how water continuously circulates / across the Earth and its atmosphere."),
                ("Solar thermal energy warms oceans and lakes, / causing liquid surface water to evaporate / into invisible atmospheric vapor.",
                 "태양 열에너지는 대양과 호수를 데워, / 표면의 액체 상태 물이 / 눈에 보이지 않는 대기 수증기로 증발하도록 만듭니다.",
                 "Solar thermal energy warms oceans and lakes, / causing liquid surface water to evaporate / into invisible atmospheric vapor."),
                ("As this warm vapor ascends, / it cools and condenses around tiny airborne particles / to form dense visible clouds.",
                 "이 따뜻한 수증기가 상승함에 따라, / 냉각되어 공기 중 미세 입자 주위로 응결되어 / 빽빽한 가시적인 구름을 형성합니다.",
                 "As this warm vapor ascends, / it cools and condenses / around tiny airborne particles / to form dense visible clouds."),
                ("When cloud droplets grow too heavy to remain suspended, / they fall back to the ground as rain, snow, or sleet.",
                 "구름 물방울들이 떠 있기에는 너무 무거워질 때, / 비, 눈, 또는 진눈깨비의 형태로 다시 땅으로 떨어집니다.",
                 "When cloud droplets grow too heavy / to remain suspended, / they fall back to the ground / as rain, snow, or sleet.")
            ],
            [
                ("circulate", "v.", "순환하다, 돌다", "Blood circulates throughout the body via the cardiovascular system."),
                ("evaporate", "v.", "증발하다", "Puddles evaporate quickly under the direct summer sun."),
                ("ascend", "v.", "상승하다, 올라가다", "Hot air balloons ascend slowly into the morning sky."),
                ("sleet", "n.", "진눈깨비 (비와 눈이 섞여 내림)", "Freezing rain turned into slippery sleet during the storm.")
            ],
            [
                ("causing A to B", "'A가 B하도록 야기하다' 인과 사역 구문입니다."),
                ("too + 형용사 + to부정사", "'너무 ~해서 …할 수 없는' 부정적 의미를 지닌 숙어입니다.")
            ],
            [
                ("What causes liquid water to evaporate into the atmosphere?",
                 "무엇이 액체 물을 대기 중으로 증발하도록 만드는가?",
                 ["Solar thermal energy warming oceans and lakes", "Earthquakes shaking deep tectonic plates", "Moonlight cooling surface ice", "Strong underground volcanic pressure alone"],
                 0,
                 "두 번째 문장에 태양 열에너지가 바다와 호수를 데워 증발을 일으킨다고 명시되어 있습니다."),
                ("What happens when warm water vapor ascends into cooler air?",
                 "따뜻한 수증기가 더 차가운 공기로 올라갈 때 무슨 일이 일어나는가?",
                 ["It turns into burning lightning gas.", "It cools and condenses around particles to form clouds.", "It falls instantly as molten rock.", "It permanently escapes Earth's gravity into space."],
                 1,
                 "세 번째 문장에 냉각되어 미세 입자 주위로 응결하여 구름을 형성한다고 나와 있습니다."),
                ("When does precipitation (rain, snow, sleet) fall to the ground?",
                 "언제 강수(비, 눈, 진눈깨비)가 지상으로 떨어지는가?",
                 ["When clouds turn bright green", "When cloud droplets become too heavy to remain suspended", "Only when wind stops blowing everywhere", "When ocean water runs completely dry"],
                 1,
                 "마지막 문장에 물방울이 너무 무거워져 떠 있을 수 없을 때 떨어진다고 설명합니다.")
            ]
        ),
        (
            "b-83",
            "How Bats Navigate with Echolocation",
            "박쥐의 반향 정위와 어둠 속 비행 원리",
            "Zoology",
            "National Geographic Wildlife Encyclopedia",
            "박쥐는 인간의 가청 범위를 넘어서는 고주파 초음파를 방출하고 그 반사파를 감지하여 어둠 속에서도 곤충을 정밀하게 사냥합니다.",
            [
                ("Microbats navigate through absolute darkness / using a biological sonar system / called echolocation.",
                 "소박쥐류는 반향 정위라 불리는 / 생물학적 소나 시스템을 이용하여 / 완벽한 어둠 속을 항행합니다.",
                 "Microbats navigate through absolute darkness / using a biological sonar system / called echolocation."),
                ("The bat emits rapid pulses of high-frequency sound / through its mouth or nose / that are far too shrill for human ears to hear.",
                 "박쥐는 입이나 코를 통해 / 인간의 귀로 듣기에는 너무 날카롭고 높은 / 급격한 고주파 음향 펄스를 방출합니다.",
                 "The bat emits rapid pulses of high-frequency sound / through its mouth or nose / that are far too shrill for human ears to hear."),
                ("These sound waves travel through the air, / bounce off nearby objects or flying moths, / and return as delicate echoes.",
                 "이 음파들은 공기를 통해 이동하다가, / 주변 물체나 날아다니는 나방에 부딪혀 튕겨 나가, / 미세한 메아리로 되돌아옵니다.",
                 "These sound waves travel through the air, / bounce off nearby objects or flying moths, / and return as delicate echoes."),
                ("By computing the minute time delay and frequency shift between emission and echo, / the bat determines the prey's exact distance, size, and speed.",
                 "방출과 메아리 사이의 미세한 시간 지연과 주파수 변화를 계산함으로써, / 박쥐는 먹잇감의 정확한 거리, 크기, 속도를 파악합니다.",
                 "By computing the minute time delay and frequency shift / between emission and echo, / the bat determines the prey's exact distance, size, and speed.")
            ],
            [
                ("sonar", "n.", "음파 탐지기, 소나", "Submarines use active sonar to detect underwater obstacles."),
                ("shrill", "adj.", "새된, 날카로운 고음의", "The referee blew a shrill whistle to stop the play."),
                ("minute", "adj.", "극미한, 대단히 작은 (마이뉴트)", "Microscopes reveal minute details invisible to the naked eye."),
                ("shift", "n.", "변화, 이동", "A noticeable shift in wind direction signaled an approaching cold front.")
            ],
            [
                ("far too + 형용사 + to부정사", "'~하기에는 훨씬 너무 …한' 강조 표현입니다."),
                ("By computing ~", "'~을 계산함으로써' 수단과 방법을 나타냅니다.")
            ],
            [
                ("What biological system do microbats use to navigate in the dark?",
                 "소박쥐류는 어둠 속에서 길을 찾기 위해 어떤 생물학적 시스템을 사용하는가?",
                 ["Infrared thermal cameras", "Echolocation", "Magnetic compass needles in paws", "Ultraviolet eye lanterns"],
                 1,
                 "첫 문장에 반향 정위(echolocation)를 사용한다고 명시되어 있습니다."),
                ("Why can humans not hear the echolocation pulses emitted by bats?",
                 "인간은 왜 박쥐가 방출하는 반향 정위 펄스를 들을 수 없는가?",
                 ["Because bats only emit sound when underwater", "Because the sound frequency is far too shrill (high-frequency) for human ears", "Because human ears are made of sound-absorbing foam", "Because bats whisper secretly to each other"],
                 1,
                 "두 번째 문장에 인간의 귀로 듣기에는 너무 고주파의 날카로운 음향이기 때문이라고 나와 있습니다."),
                ("What information does a bat calculate from returning echoes?",
                 "박쥐는 되돌아오는 메아리로부터 어떤 정보를 계산해 내는가?",
                 ["The prey's exact distance, size, and speed", "The scientific Latin name of the insect", "The monetary price of honey in markets", "The age of nearby ancient oak trees"],
                 0,
                 "마지막 문장에 먹잇감의 정확한 거리, 크기, 속도를 파악한다고 설명합니다.")
            ]
        ),
        (
            "b-84",
            "The Structure of the Great Barrier Reef",
            "그레이트 배리어 리프의 산호초 구조와 공생",
            "Marine Biology",
            "Australian Institute of Marine Science (AIMS) Marine Studies",
            "세계 최대의 산호초 지대인 그레이트 배리어 리프는 수십억 마리의 작은 산호 폴립이 석회석 골격을 분비하며 구축한 거대한 생명의 요람입니다.",
            [
                ("Stretching over two thousand three hundred kilometers along Australia's coast, / the Great Barrier Reef is the largest living structure on Earth.",
                 "호주 해안을 따라 2,300킬로미터 넘게 뻗어 있는 / 그레이트 배리어 리프는 지구상에서 가장 거대한 살아있는 구조물입니다.",
                 "Stretching over two thousand three hundred kilometers / along Australia's coast, / the Great Barrier Reef is the largest living structure on Earth."),
                ("It is constructed not by large animals, / but by billions of tiny marine organisms called coral polyps.",
                 "이것은 거대한 동물들이 아니라, / 산호 폴립이라 불리는 수십억 마리의 작은 해양 유기체들에 의해 건설됩니다.",
                 "It is constructed not by large animals, / but by billions of tiny marine organisms / called coral polyps."),
                ("These polyps secrete hard limestone exoskeletons / that accumulate over millennia / to form expansive undersea limestone ramparts.",
                 "이 폴립들은 단단한 석회암 외골격을 분비하는데, / 이것이 수천 년에 걸쳐 축적되어 / 광활한 해저 석회암 성벽을 형성합니다.",
                 "These polyps secrete hard limestone exoskeletons / that accumulate over millennia / to form expansive undersea limestone ramparts."),
                ("Microscopic photosynthetic algae living inside polyp tissues / provide essential sugars and vibrant pigments / in exchange for shelter.",
                 "폴립 조직 내부에 살아가는 미세 광합성 조류는 / 안식처를 얻는 대가로 / 필수적인 당분과 생생한 색소를 공급합니다.",
                 "Microscopic photosynthetic algae / living inside polyp tissues / provide essential sugars and vibrant pigments / in exchange for shelter.")
            ],
            [
                ("rampart", "n.", "성벽, 방벽", "Medieval castles were surrounded by massive stone ramparts."),
                ("secrete", "v.", "분비하다", "Glands secrete hormones directly into the bloodstream."),
                ("exoskeleton", "n.", "외골격 (체외 딱딱한 껍질)", "Crabs and beetles rely on rigid chitinous exoskeletons."),
                ("shelter", "n.", "안식처, 피난처", "During the hurricane, residents sought shelter in sturdy community buildings.")
            ],
            [
                ("not A, but B", "'A가 아니라 B' 대조를 나타내는 핵심 구문입니다."),
                ("in exchange for + 명사", "'~의 대가로, 교환으로' 보상 관계를 나타냅니다.")
            ],
            [
                ("What organisms build the Great Barrier Reef?",
                 "그레이트 배리어 리프를 건설하는 유기체는 무엇인가?",
                 ["Great white sharks", "Billions of tiny coral polyps", "Deep-sea giant squids", "Large colonies of coastal penguins"],
                 1,
                 "두 번째 문장에 산호 폴립(coral polyps)에 의해 건설된다고 명시되어 있습니다."),
                ("What material do coral polyps secrete to form the reef structure?",
                 "산호초 구조를 형성하기 위해 산호 폴립은 어떤 물질을 분비하는가?",
                 ["Hard limestone exoskeletons", "Flexible rubber fibers", "Pure liquid iron", "Transparent plastic films"],
                 0,
                 "세 번째 문장에 단단한 석회암 외골격(hard limestone exoskeletons)을 분비한다고 나와 있습니다."),
                ("What do microscopic algae provide to coral polyps in exchange for shelter?",
                 "미세 조류는 안식처의 대가로 산호 폴립에게 무엇을 제공하는가?",
                 ["Essential sugars and vibrant pigments", "Cold freezing snow crystals", "Toxic stinging poisons to kill fish", "Heavy gold nuggets"],
                 0,
                 "마지막 문장에 필수적인 당분과 생생한 색소(essential sugars and vibrant pigments)를 제공한다고 나와 있습니다.")
            ]
        ),
        (
            "b-85",
            "The Accidental Discovery of Penicillin",
            "페니실린의 우연한 발견과 의학 혁명",
            "History of Medicine",
            "Science Museum UK & Nobel Foundation Archives",
            "1928년 알렉산더 플레밍은 곰팡이에 오염된 배양 접시에서 박테리아가 사멸하는 현상을 목격하고 인류 최초의 항생제를 발견했습니다.",
            [
                ("In 1928, / Scottish bacteriologist Alexander Fleming made a historic breakthrough / quite by accident.",
                 "1928년, / 스코틀랜드의 세균학자 알렉산더 플레밍은 / 완전히 우연히 역사적인 돌파구를 마련했습니다.",
                 "In 1928, / Scottish bacteriologist Alexander Fleming / made a historic breakthrough / quite by accident."),
                ("Returning from a summer vacation, / he noticed that a petri dish of Staphylococcus bacteria / had become contaminated with blue-green mold.",
                 "여름 휴가에서 돌아왔을 때, / 그는 포도상구균 박테리아 배양 접시가 / 청록색 곰팡이에 오염되어 있음을 발견했습니다.",
                 "Returning from a summer vacation, / he noticed that a petri dish of Staphylococcus bacteria / had become contaminated / with blue-green mold."),
                ("Remarkably, / a clear ring of dissolved bacteria surrounded the fungal mold, / showing that the microbe had been completely destroyed.",
                 "놀랍게도, / 곰팡이 주위를 용해된 박테리아의 투명한 고리가 둘러싸고 있었는데, / 이는 세균이 완전히 파괴되었음을 보여주었습니다.",
                 "Remarkably, / a clear ring of dissolved bacteria / surrounded the fungal mold, / showing that the microbe had been completely destroyed."),
                ("Fleming identified the fungus as Penicillium notatum, / isolating the world's very first antibiotic / that would ultimately save millions of lives.",
                 "플레밍은 그 균류를 페니실리움 노타툼으로 식별하고, / 결국 수백만 명의 목숨을 구하게 될 / 세계 최초의 항생제를 분리해 냈습니다.",
                 "Fleming identified the fungus as Penicillium notatum, / isolating the world's very first antibiotic / that would ultimately save millions of lives.")
            ],
            [
                ("breakthrough", "n.", "돌파구, 중대한 진전", "The discovery of vaccines represented a monumental medical breakthrough."),
                ("petri dish", "n.", "페트리 접시 (세균 배양용 원형 접시)", "The lab technician smeared bacteria evenly across the sterile petri dish."),
                ("contaminated", "adj.", "오염된", "The floodwaters contaminated the municipal drinking supply."),
                ("isolate", "v.", "분리하다, 격리하다", "Chemist Marie Curie worked for years to isolate pure radium.")
            ],
            [
                ("Returning from ~", "'~에서 돌아왔을 때' 시간을 나타내는 분사구문입니다."),
                (", showing that ~", "결과적 분사구문으로 '그리하여 ~을 보여주었다'로 해석됩니다.")
            ],
            [
                ("How did Alexander Fleming discover penicillin?",
                 "알렉산더 플레밍은 페니실린을 어떻게 발견했는가?",
                 ["By purposefully mixing thousands of rare chemical powders", "Quite by accident when observing a contaminated petri dish", "By analyzing deep Antarctic ice cores", "By translating an ancient Roman medical scroll"],
                 1,
                 "첫 문장과 두 번째 문장에 오염된 배양 접시를 관찰하던 중 완전히 우연히 발견했다고 나와 있습니다."),
                ("What was unusual about the bacteria surrounding the blue-green mold?",
                 "청록색 곰팡이 주변의 박테리아에 어떤 특이한 점이 있었는가?",
                 ["The bacteria multiplied ten times faster.", "A clear ring formed where the bacteria had been completely destroyed.", "The bacteria turned bright fluorescent red.", "The bacteria turned into solid rock crystals."],
                 1,
                 "세 번째 문장에 박테리아가 완전히 파괴되어 투명한 고리가 둘러싸고 있었다고 설명합니다."),
                ("What type of medication did Fleming isolate from Penicillium notatum?",
                 "플레밍은 페니실리움 노타툼으로부터 어떤 유형의 의약품을 분리했는가?",
                 ["A synthetic sedative", "The world's first antibiotic", "A high-blood-pressure pill", "A vitamin C supplement"],
                 1,
                 "마지막 문장에 세계 최초의 항생제(the world's very first antibiotic)를 분리했다고 명시되어 있습니다.")
            ]
        ),
        (
            "b-86",
            "The Chemical Glow of Fireflies",
            "반딧불이의 생화학적 발광 메커니즘",
            "Entomology",
            "Scientific American & Harvard Museum of Comparative Zoology",
            "반딧불이는 복부의 발광 세포에서 루시페린과 산소의 효율적인 효소 반응을 통해 열 손실이 거의 없는 100% 차가운 빛을 만들어냅니다.",
            [
                ("Fireflies are winged beetles famous / for their enchanting twilight light shows.",
                 "반딧불이는 매혹적인 황혼의 빛 쇼로 / 유명한 날개 달린 딱정벌레입니다.",
                 "Fireflies are winged beetles famous / for their enchanting twilight light shows."),
                ("Their illumination is produced / inside specialized light organs located in their lower abdomen.",
                 "그들의 빛은 / 아래쪽 복부에 위치한 특수한 발광 기관 내부에서 / 생성됩니다.",
                 "Their illumination is produced / inside specialized light organs / located in their lower abdomen."),
                ("When oxygen enters the lantern organ, / it combines with a biological molecule called luciferin, / facilitated by the enzyme luciferase.",
                 "산소가 발광 기관으로 들어갈 때, / 루시페라아제 효소의 도움을 받아 / 루시페린이라 불리는 생체 분자와 결합합니다.",
                 "When oxygen enters the lantern organ, / it combines with a biological molecule called luciferin, / facilitated by the enzyme luciferase."),
                ("Unlike an incandescent lightbulb that wastes ninety percent of its energy as heat, / a firefly's light is nearly one hundred percent cold chemical illumination.",
                 "에너지의 90%를 열로 낭비하는 백열전구와 달리, / 반딧불이의 빛은 거의 100% 차가운 화학적 조명입니다.",
                 "Unlike an incandescent lightbulb / that wastes ninety percent of its energy as heat, / a firefly's light is nearly one hundred percent cold chemical illumination.")
            ],
            [
                ("enchanting", "adj.", "매혹적인, 황홀한", "The forest glade had an enchanting atmosphere under moonlight."),
                ("illumination", "n.", "빛, 조명, 발광", "Holiday illuminations lit up the pedestrian boulevard at night."),
                ("incandescent", "adj.", "백열의, 백열광을 내는", "Incandescent filament bulbs are gradually being replaced by energy-saving LEDs."),
                ("facilitate", "v.", "촉진하다, 용이하게 하다", "Modern computers facilitate rapid statistical calculations.")
            ],
            [
                ("famous for + 명사", "'~로 유명한' 형용사 수식구입니다."),
                ("Unlike + 명사", "'~와는 다르게' 대비를 나타내는 전치사구입니다.")
            ],
            [
                ("Where are a firefly's light-producing organs located?",
                 "반딧불이의 발광 기관은 어디에 위치해 있는가?",
                 ["At the tips of their antennae", "In their lower abdomen", "Inside their transparent wings", "At the back of their throat"],
                 1,
                 "두 번째 문장에 아래쪽 복부(in their lower abdomen)에 위치해 있다고 명시되어 있습니다."),
                ("What enzyme facilitates the chemical reaction creating firefly light?",
                 "반딧불이 빛을 생성하는 화학 반응을 촉진하는 효소는 무엇인가?",
                 ["Amylase", "Luciferase", "Insulin", "Pepsin"],
                 1,
                 "세 번째 문장에 루시페라아제(luciferase) 효소의 도움을 받는다고 나와 있습니다."),
                ("How does firefly light differ from an incandescent lightbulb?",
                 "반딧불이의 빛은 백열전구와 어떻게 다른가?",
                 ["It produces blinding sparks of electricity.", "It is nearly 100 percent cold illumination with virtually zero wasted heat.", "It burns nearby leaves with scorching heat.", "It only shines when exposed to kerosene oil."],
                 1,
                 "마지막 문장에 열 낭비 없이 거의 100% 차가운 화학적 조명이라고 설명합니다.")
            ]
        ),
        (
            "b-87",
            "The Engineering of the Great Pyramid of Giza",
            "기자의 대피라미드 축조 공학",
            "Ancient Engineering & Archaeology",
            "The British Museum Ancient Egypt Collections",
            "4,500년 전 건설된 기자의 대피라미드는 230만 개가 넘는 거대한 석회암 블록을 정밀하게 쌓아 올린 고대 공학의 기념비적 걸작입니다.",
            [
                ("Built over four thousand five hundred years ago, / the Great Pyramid of Giza stands / as an enduring testament to ancient Egyptian engineering.",
                 "4,500년도 더 전에 건설된 / 기자의 대피라미드는 / 고대 이집트 토목 공학의 영원한 증거로 우뚝 서 있습니다.",
                 "Built over four thousand five hundred years ago, / the Great Pyramid of Giza stands / as an enduring testament / to ancient Egyptian engineering."),
                ("The colossal monument incorporates more than two million limestone and granite blocks, / each weighing an average of two and a half tons.",
                 "이 거대한 기념비는 200만 개가 넘는 석회암 및 화강암 블록으로 이루어져 있으며, / 각 블록의 무게는 평균 2.5톤에 달합니다.",
                 "The colossal monument incorporates / more than two million limestone and granite blocks, / each weighing an average of two and a half tons."),
                ("Skilled craftsmen and laborers transported the stones along the Nile River / using wooden barges during annual flood seasons.",
                 "숙련된 석공과 노동자들은 / 연례 범람기 동안 목조 바지선을 이용하여 / 나일강을 따라 거석들을 운반했습니다.",
                 "Skilled craftsmen and laborers / transported the stones along the Nile River / using wooden barges / during annual flood seasons."),
                ("Its four base corners align almost flawlessly with true cardinal north, south, east, and west, / reflecting sophisticated astronomical knowledge.",
                 "피라미드 바닥의 네 모서리는 진북, 진남, 진동, 진서를 거의 완벽하게 가리키며, / 고도의 정교한 천문학적 지식을 반영하고 있습니다.",
                 "Its four base corners align almost flawlessly / with true cardinal north, south, east, and west, / reflecting sophisticated astronomical knowledge.")
            ],
            [
                ("enduring", "adj.", "오래 지속되는, 불멸의", "Shakespeare's plays enjoy enduring global popularity."),
                ("colossal", "adj.", "거대한, 엄청난", "A colossal marble statue guarded the palace gateway."),
                ("craftsman", "n.", "장인, 숙련공", "Master craftsmen hand-carved intricate walnut chests."),
                ("flawlessly", "adv.", "흠 없이, 완벽하게", "The concert pianist performed the complex concerto flawlessly.")
            ],
            [
                ("Built over ~ ago, the Great Pyramid stands ~", "과거분사로 시작하는 수동태 분사구문입니다."),
                (", each weighing an average of ~", "독립분사구문으로 '각각 평균 ~의 무게가 나가면서'로 해석됩니다.")
            ],
            [
                ("How many stone blocks were incorporated into the Great Pyramid?",
                 "대피라미드에는 몇 개의 석재 블록이 사용되었는가?",
                 ["Fewer than fifty blocks", "More than two million blocks", "Exactly ten thousand bricks", "Just twelve gigantic slabs"],
                 1,
                 "두 번째 문장에 200만 개가 넘는 블록(more than two million blocks)이 사용되었다고 나와 있습니다."),
                ("How did laborers transport heavy stones from distant quarries?",
                 "노동자들은 먼 채석장에서 무거운 돌을 어떻게 운반했는가?",
                 ["Using wooden barges along the Nile during annual floods", "On steam-powered railway flatcars", "By carrying them in backpacks singly", "Inside bronze submarine tunnels"],
                 0,
                 "세 번째 문장에 범람기 동안 목조 바지선으로 나일강을 따라 운반했다고 명시되어 있습니다."),
                ("What do the four base corners align with?",
                 "피라미드 바닥의 네 모서리는 무엇과 정렬되어 있는가?",
                 ["The exact height of the Pharaoh", "True cardinal directions (north, south, east, and west)", "The location of Roman roads", "The distance to the Mediterranean Sea"],
                 1,
                 "마지막 문장에 기본 방위(진북, 남, 동, 서)와 거의 완벽하게 일치한다고 설명합니다.")
            ]
        ),
        (
            "b-88",
            "Why the Sky Is Blue",
            "하늘이 푸른색으로 보이는 대기 산란 원리",
            "Atmospheric Optics",
            "NASA Science Earth's Atmosphere Education",
            "태양빛이 지구 대기를 통과할 때, 파장이 짧은 푸른색 빛이 산소와 질소 분자에 부딪혀 사방으로 강하게 산란되기 때문에 하늘이 푸르게 보입니다.",
            [
                ("Sunlight appears pure white to human observers, / but it is actually composed of all the colors of the rainbow combined.",
                 "태양빛은 인간 관찰자에게 순수한 흰색으로 보이지만, / 실제로는 무지개의 모든 색상이 결합된 것입니다.",
                 "Sunlight appears pure white to human observers, / but it is actually composed of all the colors / of the rainbow combined."),
                ("Light travels in energetic waves, / with red light possessing long wavelengths / and blue light traveling in much shorter, smaller waves.",
                 "빛은 에너지 파동으로 이동하며, / 붉은빛은 긴 파장을 지니고 / 푸른빛은 훨씬 더 짧고 작은 파동으로 이동합니다.",
                 "Light travels in energetic waves, / with red light possessing long wavelengths / and blue light traveling in much shorter, smaller waves."),
                ("When sunlight enters the Earth's atmosphere, / it collides with abundant gas molecules of nitrogen and oxygen.",
                 "태양빛이 지구 대기로 진입할 때, / 풍부한 질소와 산소 기체 분자들과 충돌합니다.",
                 "When sunlight enters the Earth's atmosphere, / it collides with abundant gas molecules / of nitrogen and oxygen."),
                ("Because shorter wavelengths scatter far more readily than longer ones in a process called Rayleigh scattering, / blue light is dispersed in every direction across the sky.",
                 "레일리 산란이라 불리는 과정에서 짧은 파장이 긴 파장보다 훨씬 더 쉽게 산란되기 때문에, / 푸른빛이 하늘 전체에 사방으로 흩어집니다.",
                 "Because shorter wavelengths scatter far more readily / than longer ones in a process called Rayleigh scattering, / blue light is dispersed in every direction across the sky.")
            ],
            [
                ("composed of", "adj. phr.", "~로 구성된", "Water is composed of hydrogen and oxygen atoms."),
                ("collide", "v.", "충돌하다", "Subatomic particles collide at near light-speed inside particle colliders."),
                ("abundant", "adj.", "풍부한, 많은", "Tropical rain forests support abundant plant biodiversity."),
                ("disperse", "v.", "흩뜨리다, 분산시키다", "Police used sirens to disperse the gathering crowd.")
            ],
            [
                ("with + 명사 + 분사", "'명사가 ~한 채로' 동시상황을 나타내는 부대상황 구문입니다."),
                ("far more readily than ~", "'~보다 훨씬 더 쉽게' 비교급 강조 부사 far가 쓰였습니다.")
            ],
            [
                ("What is white sunlight actually composed of?",
                 "백색 태양광은 실제로는 무엇으로 구성되어 있는가?",
                 ["Only invisible ultraviolet rays", "All the colors of the rainbow combined", "Pure green laser particles", "Single-tone grey heat waves"],
                 1,
                 "첫 문장에 무지개의 모든 색상이 결합된 것이라고 명시되어 있습니다."),
                ("How does the wavelength of blue light compare to red light?",
                 "푸른빛의 파장은 붉은빛과 비교하여 어떠한가?",
                 ["Blue light has much shorter wavelengths than red light.", "Blue light has ten times longer waves than red light.", "Both colors have mathematically identical wavelengths.", "Blue light has no waves at all."],
                 0,
                 "두 번째 문장에 푸른빛이 훨씬 더 짧은 파장으로 이동한다고 나와 있습니다."),
                ("What physical scattering process causes blue light to spread across the sky?",
                 "푸른빛이 하늘 전체로 퍼지게 만드는 물리적 산란 과정은 무엇인가?",
                 ["Rayleigh scattering", "Nuclear decay", "Chemical oxidation", "Thermal boiling"],
                 0,
                 "마지막 문장에 레일리 산란(Rayleigh scattering)에 의해 사방으로 흩어진다고 나와 있습니다.")
            ]
        ),
        (
            "b-89",
            "The Underground Fungal Networks of Forests",
            "숲속의 거대한 지하 균사체 네트워크",
            "Mycology & Forest Ecology",
            "Royal Botanic Gardens, Kew Research Bulletin",
            "버섯은 균류의 지상 생식 기관에 불과하며, 땅속에는 나무들에게 양분을 전달하고 소통을 매개하는 광대한 균사망이 존재합니다.",
            [
                ("When people spot mushrooms on the damp forest floor, / they are only seeing the temporary fruiting body of a vast subterranean organism.",
                 "사람들이 축축한 숲 바닥에서 버섯을 발견할 때, / 그들은 거대한 지하 유기체의 일시적인 자실체(열매)만을 보고 있는 것입니다.",
                 "When people spot mushrooms on the damp forest floor, / they are only seeing the temporary fruiting body / of a vast subterranean organism."),
                ("Beneath the soil lies the mycelium, / an intricate web of microscopic thread-like filaments called hyphae.",
                 "흙 아래에는 균사라 불리는 / 미세한 실 같은 필라멘트들의 복잡한 그물망인 / 균사체가 자리 잡고 있습니다.",
                 "Beneath the soil lies the mycelium, / an intricate web of microscopic thread-like filaments / called hyphae."),
                ("These fungal networks form a mutually beneficial partnership / with plant roots / known as mycorrhizal symbiosis.",
                 "이러한 균류 네트워크는 균근 공생으로 알려진 / 상호 유익한 동반자 관계를 / 식물 뿌리와 형성합니다.",
                 "These fungal networks form a mutually beneficial partnership / with plant roots / known as mycorrhizal symbiosis."),
                ("Fungi channel water and minerals from deep soil to trees, / while the trees share sugar produced through photosynthesis in return.",
                 "균류는 깊은 토양에서 나무로 수분과 미네랄을 공급하며, / 나무는 그 대가로 광합성을 통해 생산한 당분을 공유합니다.",
                 "Fungi channel water and minerals from deep soil to trees, / while the trees share sugar / produced through photosynthesis in return.")
            ],
            [
                ("subterranean", "adj.", "지하의, 땅속의", "Subterranean rivers flow quietly through limestone caverns."),
                ("intricate", "adj.", "복잡한, 정교한", "The pocket watch contained an intricate mechanism of brass gears."),
                ("symbiosis", "n.", "공생", "Symbiosis between clownfish and sea anemones provides mutual defense."),
                ("in return", "idiom", "그 대가로, 보답으로", "She helped me study biology, and I assisted her with calculus in return.")
            ],
            [
                ("Beneath the soil lies the mycelium", "장소 부사구 도치 구문으로 '토양 아래에 균사체가 놓여 있다'는 구조입니다."),
                ("produced through ~", "과거분사구로 sugar를 뒤에서 수식합니다.")
            ],
            [
                ("What is a mushroom in relation to the entire fungal organism?",
                 "전체 균류 유기체와 관련하여 버섯이란 무엇인가?",
                 ["The complete root system", "A temporary fruiting body of a vast subterranean organism", "A mineral stone formed by dead trees", "A type of green leaf"],
                 1,
                 "첫 문장에 거대한 지하 유기체의 일시적인 자실체(fruiting body)라고 나와 있습니다."),
                ("What is the subterranean network of threads called?",
                 "실 같은 필라멘트들의 지하 네트워크를 무엇이라 부르는가?",
                 ["The mycelium", "The tree trunk", "The stone aquifer", "The volcanic pipe"],
                 0,
                 "두 번째 문장에 균사체(the mycelium)라고 명시되어 있습니다."),
                ("What do fungi supply to trees in exchange for photosynthesis sugars?",
                 "균류는 광합성 당분의 대가로 나무에 무엇을 공급하는가?",
                 ["Water and minerals from deep soil", "Poisonous chemicals to burn leaves", "Cold winter ice crystals", "Heavy carbon coal chunks"],
                 0,
                 "마지막 문장에 깊은 흙에서 수분과 미네랄(water and minerals)을 공급한다고 설명합니다.")
            ]
        ),
        (
            "b-90",
            "The Law of Reflection and Mirrors",
            "반사의 법칙과 거울의 광학 원리",
            "Optics",
            "The Physics Classroom Educational Resource",
            "거울은 매끄러운 표면에서 입사각과 반사각이 동일하게 반사되는 정반사 법칙을 통해 선명한 가상 이미지를 만들어냅니다.",
            [
                ("A mirror is an optical device / designed to reflect light waves / to form clear, identifiable images.",
                 "거울은 선명하고 식별 가능한 상을 형성하기 위해 / 빛의 파동을 반사하도록 설계된 / 광학 장치입니다.",
                 "A mirror is an optical device / designed to reflect light waves / to form clear, identifiable images."),
                ("Most everyday mirrors consist of a flat pane of glass / coated on its rear surface with a thin reflective film of polished silver or aluminum.",
                 "대부분의 일상 거울은 광택을 낸 은이나 알루미늄의 얇은 반사 피막으로 / 뒷면이 코팅된 / 평평한 유리 판으로 이루어져 있습니다.",
                 "Most everyday mirrors consist of a flat pane of glass / coated on its rear surface / with a thin reflective film / of polished silver or aluminum."),
                ("When incoming rays of light strike this smooth metallic boundary, / they obey the fundamental Law of Reflection: / the angle of reflection equals the angle of incidence.",
                 "입사하는 광선이 이 매끄러운 금속성 경계면에 부딪힐 때, / 광선은 반사각과 입사각이 동일하다는 / 근본적인 반사의 법칙을 따릅니다.",
                 "When incoming rays of light strike this smooth metallic boundary, / they obey the fundamental Law of Reflection: / the angle of reflection equals the angle of incidence."),
                ("Because parallel incident rays bounce off uniformly without scattering, / our eyes perceive an undistorted virtual image behind the glass.",
                 "평행한 입사 광선들이 흩어짐 없이 균일하게 튕겨 나가기 때문에, / 우리의 눈은 유리 뒤편에 왜곡되지 않은 허상을 인지합니다.",
                 "Because parallel incident rays bounce off uniformly without scattering, / our eyes perceive an undistorted virtual image / behind the glass.")
            ],
            [
                ("pane", "n.", "(한 장의) 판유리", "A stray baseball shattered the bedroom window pane."),
                ("incidence", "n.", "입사 (빛 등이 닿음), 발생", "The angle of incidence is measured relative to the surface normal."),
                ("undistorted", "adj.", "왜곡되지 않은, 온전한", "High-fidelity audio systems reproduce undistorted musical sounds."),
                ("virtual image", "n.", "허상 (실제 빛이 모이지 않는 가상 상)", "Plane mirrors produce a virtual image located behind the reflective surface.")
            ],
            [
                ("consist of + 명사", "'~로 구성되다' 수동태를 쓰지 않는 자동사 구문입니다."),
                ("coated on its rear surface", "과거분사구로 glass를 뒤에서 수식합니다.")
            ],
            [
                ("What thin metallic film is coated on the rear of household mirrors?",
                 "가정용 거울 뒷면에는 어떤 얇은 금속성 피막이 코팅되어 있는가?",
                 ["Polished silver or aluminum", "Liquid green paint only", "Rusted iron flakes", "Solid lead bricks"],
                 0,
                 "두 번째 문장에 광택 낸 은이나 알루미늄(polished silver or aluminum)이 코팅되어 있다고 나와 있습니다."),
                ("What does the fundamental Law of Reflection state?",
                 "근본적인 반사의 법칙은 무엇을 명시하는가?",
                 ["The angle of reflection equals the angle of incidence.", "Light always stops moving when it hits glass.", "Reflected light turns completely into sound waves.", "All light rays bend into pure darkness."],
                 0,
                 "세 번째 문장에 반사각은 입사각과 같다(angle of reflection equals angle of incidence)고 나와 있습니다."),
                ("Why do mirrors produce clear undistorted images rather than blurry reflections?",
                 "왜 거울은 흐릿한 반사 대신 왜곡 없는 선명한 상을 만들어내는가?",
                 ["Because parallel rays bounce off uniformly without scattering", "Because glass melts light into clear water", "Because mirrors absorb all red wavelengths", "Because human eyes only focus in rooms with mirrors"],
                 0,
                 "마지막 문장에 평행 입사 광선이 흩어짐 없이 균일하게 튕겨 나가기 때문이라고 설명합니다.")
            ]
        ),
        (
            "b-91",
            "The Upstream Migration of Salmon",
            "연어의 모천 회귀와 상류 거슬러 오르기",
            "Ichthyology",
            "NOAA Fisheries Marine & Anadromous Fish Bulletin",
            "바다에서 성체로 성장한 연어는 후각적 기억을 바탕으로 자신이 태어난 모천으로 수백 킬로미터를 거슬러 올라가 산란합니다.",
            [
                ("Salmon are extraordinary anadromous fish, / meaning they are born in freshwater gravel beds, / mature in the open sea, / and return upstream to reproduce.",
                 "연어는 민물 자갈밭에서 태어나 / 탁 트인 바다에서 성숙하고 / 번식을 위해 상류로 되돌아가는 / 놀라운 소하성 어류입니다.",
                 "Salmon are extraordinary anadromous fish, / meaning they are born in freshwater gravel beds, / mature in the open sea, / and return upstream to reproduce."),
                ("After feeding on oceanic krill and small fish for several years, / adult salmon embark on a strenuous homeward pilgrimage.",
                 "수년간 바다의 크릴과 작은 물고기를 먹고 자란 후, / 성체 연어는 고향으로 향하는 험난한 순례를 시작합니다.",
                 "After feeding on oceanic krill and small fish for several years, / adult salmon embark / on a strenuous homeward pilgrimage."),
                ("Guided by an exquisite chemical olfactory memory, / they can identify the unique scent profile of their natal stream.",
                 "정교한 화학적 후각 기억에 이끌려, / 그들은 자신이 태어난 모천의 고유한 냄새 프로필을 식별해 낼 수 있습니다.",
                 "Guided by an exquisite chemical olfactory memory, / they can identify the unique scent profile / of their natal stream."),
                ("They leap courageously over rocky waterfalls and fight turbulent currents / to spawn their eggs in the very gravel where their own lives began.",
                 "그들은 바위 폭포를 용감하게 뛰어넘고 거센 물살과 싸우며 / 자신의 생명이 시작되었던 바로 그 자갈밭에 알을 낳습니다.",
                 "They leap courageously over rocky waterfalls / and fight turbulent currents / to spawn their eggs / in the very gravel where their own lives began.")
            ],
            [
                ("anadromous", "adj.", "소하성의 (강을 거슬러 오르는)", "Anadromous species bridge ecological energy between ocean and inland ecosystems."),
                ("strenuous", "adj.", "고된, 몹시 힘든", "Lifting heavy timber all afternoon is strenuous physical work."),
                ("olfactory", "adj.", "후각의", "Dogs possess an olfactory sensitivity thousands of times keener than humans."),
                ("natal", "adj.", "태어난 곳의, 출생의", "Sea turtles return to their natal beaches to dig egg nests.")
            ],
            [
                ("meaning they are born ~", "분사구문으로 앞선 명사 anadromous fish의 정의를 설명합니다."),
                ("the very gravel where ~", "명사 앞의 very는 '바로 그'를 뜻하는 강조 형용사입니다.")
            ],
            [
                ("What does 'anadromous' mean in relation to salmon?",
                 "연어와 관련하여 '소하성(anadromous)'이란 무슨 뜻인가?",
                 ["Fish that spend their entire lives in frozen desert ice", "Fish born in freshwater that mature in the sea and return upstream to spawn", "Fish that only swim backwards in salt lakes", "Fish that have no bones or scales"],
                 1,
                 "첫 문장에 민물에서 태어나 바다에서 자란 뒤 상류로 돌아와 번식한다는 뜻이라고 설명합니다."),
                ("How do adult salmon navigate back to their exact birth stream?",
                 "성체 연어는 자신이 태어난 정확한 개울로 어떻게 길을 찾는가?",
                 ["By following flashing lighthouse signals along the shore", "Using an exquisite olfactory chemical memory of the stream's scent", "By asking passing dolphins for directions", "By watching constellation patterns in the night sky"],
                 1,
                 "세 번째 문장에 정교한 화학적 후각 기억(chemical olfactory memory)으로 식별한다고 나와 있습니다."),
                ("Where do returning salmon spawn their eggs?",
                 "돌아온 연어는 알을 어디에 낳는가?",
                 ["In the deep oceanic abyss", "In the gravel bed of their natal stream where their lives began", "On dry sandy beach dunes", "Inside floating seabird nests"],
                 1,
                 "마지막 문장에 자신의 생명이 시작되었던 모천의 자갈밭에 알을 낳는다고 명시되어 있습니다.")
            ]
        ),
        (
            "b-92",
            "The Seismic Mechanics of Earthquakes",
            "지진의 발생 원인과 지진파의 전파",
            "Geology & Seismology",
            "U.S. Geological Survey (USGS) Earthquake Information Center",
            "지진은 단층면을 따라 응축되었던 지각판의 변형 에너지가 마찰 한계를 넘어설 때 한순간에 방출되면서 지진파로 지표면을 흔드는 현상입니다.",
            [
                ("An earthquake is the sudden shaking of the Earth's surface / caused by a rapid release of energy in the lithosphere.",
                 "지진은 암석권에서 에너지가 급격히 방출되면서 / 발생하는 / 지구 표면의 갑작스러운 흔들림입니다.",
                 "An earthquake is the sudden shaking of the Earth's surface / caused by a rapid release of energy in the lithosphere."),
                ("Tectonic plates constantly push against one another, / but friction along rough fault lines locks them in place.",
                 "지각판들은 끊임없이 서로를 밀어붙이지만, / 거친 단층선을 따른 마찰력이 판들을 제자리에 맞물려 고정시킵니다.",
                 "Tectonic plates constantly push against one another, / but friction along rough fault lines / locks them in place."),
                ("As continuous stress builds over decades, / the stored elastic energy eventually exceeds the rock's frictional resistance.",
                 "수십 년에 걸쳐 지속적인 응력이 쌓임에 따라, / 저장된 탄성 에너지는 결국 암석의 마찰 저항을 넘어서게 됩니다.",
                 "As continuous stress builds over decades, / the stored elastic energy / eventually exceeds the rock's frictional resistance."),
                ("The rocks abruptly fracture and slip at the hypocenter, / radiating seismic energy waves that ripple outwards to shake continental crust.",
                 "암석은 진원에서 급격히 파쇄되고 미끄러지며, / 대륙 지각을 흔들며 바깥으로 퍼져나가는 지진 에너지 파동을 방출합니다.",
                 "The rocks abruptly fracture and slip at the hypocenter, / radiating seismic energy waves / that ripple outwards to shake continental crust.")
            ],
            [
                ("lithosphere", "n.", "암석권 (지각과 상부 맨틀)", "The rigid lithosphere floats upon the ductile asthenosphere."),
                ("hypocenter", "n.", "진원 (지진 발생 지점)", "The hypocenter was located twelve kilometers beneath the city."),
                ("fracture", "v.", "파쇄되다, 금이 가다", "Excessive stress caused the concrete pillar to fracture."),
                ("seismic", "adj.", "지진의, 지진성의", "Seismic sensors detect faint sub-surface tremors miles away.")
            ],
            [
                ("caused by + 명사", "'~에 의해 유발된' 과거분사 수식구입니다."),
                (", radiating ~", "동시동작 분사구문으로 '지진 에너지 파동을 방출하면서'로 해석됩니다.")
            ],
            [
                ("What causes the sudden shaking of an earthquake?",
                 "지진의 갑작스러운 흔들림을 유발하는 것은 무엇인가?",
                 ["Heavy rain falling onto farm fields", "A rapid release of stored elastic energy in the lithosphere", "Windmills spinning too fast", "Solar eclipses heating ocean water"],
                 1,
                 "첫 문장에 암석권에서의 급격한 에너지 방출(rapid release of energy in the lithosphere) 때문이라고 명시되어 있습니다."),
                ("What locks tectonic plates together before the earthquake occurs?",
                 "지진이 발생하기 전 지각판을 맞물려 고정시키는 것은 무엇인가?",
                 ["Friction along rough fault lines", "Giant iron anchors built by humans", "Cold winter frost", "Liquid petroleum lubricant"],
                 0,
                 "두 번째 문장에 거친 단층선을 따른 마찰력(friction along fault lines)이라고 나와 있습니다."),
                ("What happens at the hypocenter when frictional resistance is exceeded?",
                 "마찰 저항이 초과될 때 진원(hypocenter)에서 무슨 일이 일어나는가?",
                 ["Rocks abruptly fracture and slip, radiating seismic waves.", "The Earth immediately stops rotating.", "All ocean water evaporates instantly.", "Bedrock turns into sweet liquid syrup."],
                 0,
                 "마지막 문장에 암석이 파쇄되고 미끄러지며 지진파를 방출한다고 설명합니다.")
            ]
        ),
        (
            "b-93",
            "Why Humans and Animals Yawn",
            "하품의 생리학과 뇌 냉각 가설",
            "Neurobiology & Physiology",
            "Harvard Health Publishing & American Physiological Society",
            "하품은 단순한 지루함의 표현이 아니라, 시원한 공기를 흡입하여 뇌의 온도를 조절하고 각성도를 높이는 생리적 적응 반응입니다.",
            [
                ("Yawning is a universal behavioral reflex / observed across nearly all vertebrate animals.",
                 "하품은 거의 모든 척추동물에게서 관찰되는 / 보편적인 행동 반사입니다.",
                 "Yawning is a universal behavioral reflex / observed across nearly all vertebrate animals."),
                ("While folk wisdom long claimed / that yawning simply supplies extra oxygen to the bloodstream, / physiological tests disproved this theory.",
                 "민간 속설은 하품이 혈류에 추가 산소를 공급할 뿐이라고 / 오랫동안 주장했으나, / 생리학적 실험들은 이 이론이 틀렸음을 증명했습니다.",
                 "While folk wisdom long claimed / that yawning simply supplies extra oxygen to the bloodstream, / physiological tests disproved this theory."),
                ("The prominent modern thermoregulatory hypothesis suggests / that yawning serves as a natural cooling mechanism for the brain.",
                 "유력한 현대 체온 조절 가설은 / 하품이 뇌를 위한 자연스러운 냉각 메커니즘 역할을 한다고 / 제안합니다.",
                 "The prominent modern thermoregulatory hypothesis suggests / that yawning serves / as a natural cooling mechanism for the brain."),
                ("A deep inhalation of cool ambient air combined with jaw stretching / increases intracranial blood flow, / dissipating excess heat to boost mental alertness.",
                 "턱 스트레칭과 결합된 서늘한 주변 공기의 깊은 흡입은 / 두개골 내 혈류를 증가시켜, / 과도한 열을 분산시키고 정신적 각성도를 높입니다.",
                 "A deep inhalation of cool ambient air combined with jaw stretching / increases intracranial blood flow, / dissipating excess heat / to boost mental alertness.")
            ],
            [
                ("reflex", "n.", "반사 작용, 반사 운동", "Blinking when dust approaches the eye is an involuntary reflex."),
                ("thermoregulatory", "adj.", "체온 조절의", "Thermoregulatory mechanisms maintain constant mammalian body temperature."),
                ("intracranial", "adj.", "두개골 내의", "Intracranial pressure must be monitored following severe head injuries."),
                ("dissipate", "v.", "소산시키다, 흩뜨려 없애다", "Breeze helps dissipate smoke from the barbecue grill.")
            ],
            [
                ("observed across ~", "과거분사구로 a universal behavioral reflex를 수식합니다."),
                ("to boost mental alertness", "목적을 나타내는 to부정사 부사적 용법입니다.")
            ],
            [
                ("What does the modern thermoregulatory hypothesis suggest about yawning?",
                 "현대 체온 조절 가설은 하품에 대해 무엇을 제안하는가?",
                 ["It serves as a natural cooling mechanism for the brain.", "It empties the stomach of digestive acid.", "It turns teeth into harder enamel.", "It permanently damages vocal chords."],
                 0,
                 "세 번째 문장에 뇌를 위한 자연 냉각 메커니즘 역할을 한다고 명시되어 있습니다."),
                ("Did physiological tests confirm the old theory that yawning supplies extra oxygen?",
                 "생리학적 실험들은 하품이 추가 산소를 공급한다는 과거 이론을 확인했는가?",
                 ["Yes, it proved blood oxygen quadruples instantly.", "No, physiological tests disproved this theory.", "It proved oxygen drops to zero during yawning.", "It proved only birds receive oxygen from yawns."],
                 1,
                 "두 번째 문장에 생리학적 실험들이 이 이론이 틀렸음을 입증했다(disproved this theory)고 나와 있습니다."),
                ("How does yawning boost mental alertness according to the passage?",
                 "본문에 따르면 하품은 어떻게 정신적 각성도를 높이는가?",
                 ["By putting the body directly into deep REM sleep", "By inhaling cool air and stretching jaws to increase blood flow and dissipate heat", "By preventing people from drinking water", "By stopping the heart for three seconds"],
                 1,
                 "마지막 문장에 서늘한 공기 흡입과 턱 스트레칭이 혈류를 늘리고 열을 분산시킨다고 설명합니다.")
            ]
        ),
        (
            "b-94",
            "The Subatomic Architecture of the Atom",
            "원자의 아원자 구조와 기본 구성 요소",
            "Atomic Physics",
            "CERN Educational Resource & Bohr Institute",
            "원자는 중심의 극히 작고 무거운 원자핵(양성자와 중성자)과 그 주변을 회전하는 전자로 이루어진 물질의 기본 단위입니다.",
            [
                ("All physical matter in the universe / is composed of microscopic building blocks / known as atoms.",
                 "우주의 모든 물리적 물질은 / 원자로 알려진 / 미세한 기본 구성 요소들로 이루어져 있습니다.",
                 "All physical matter in the universe / is composed of microscopic building blocks / known as atoms."),
                ("At the center of every atom lies a dense, compact nucleus / containing positively charged protons and uncharged neutrons.",
                 "모든 원자의 중심에는 / 양전하를 띤 양성자와 전하가 없는 중성자를 포함하는 / 조밀하고 압축된 원자핵이 자리 잡고 있습니다.",
                 "At the center of every atom / lies a dense, compact nucleus / containing positively charged protons and uncharged neutrons."),
                ("Orbiting this central nucleus at relativistic velocities / are negatively charged electrons, / which occupy specific discrete energy levels.",
                 "상대론적 속도로 이 중심 핵 주위를 궤도 회전하는 것은 / 음전하를 띤 전자들이며, / 이들은 특정한 개별 에너지 준위를 차지합니다.",
                 "Orbiting this central nucleus at relativistic velocities / are negatively charged electrons, / which occupy specific discrete energy levels."),
                ("Because electrons are situated vast distances away from the tiny nucleus, / more than ninety-nine percent of an atom's volume is empty space.",
                 "전자가 아주 작은 원자핵으로부터 광대한 거리에 떨어져 위치해 있기 때문에, / 원자 부피의 99퍼센트 이상은 텅 빈 공간입니다.",
                 "Because electrons are situated vast distances away / from the tiny nucleus, / more than ninety-nine percent of an atom's volume / is empty space.")
            ],
            [
                ("compact", "adj.", "조밀한, 빽빽한", "The city apartment featured a compact modular kitchen."),
                ("nucleus", "n.", "핵, 중심", "The atomic nucleus contains virtually all of the atom's mass."),
                ("discrete", "adj.", "별개의, 개별적인", "Sound in digital audio is sampled at discrete time intervals."),
                ("situated", "adj.", "위치한", "The historic castle is situated high upon a steep cliff.")
            ],
            [
                ("At the center lies ~", "장소 부사구 도치 구문입니다."),
                ("Orbiting this nucleus are electrons", "현재분사 보어 도치 구문으로 '핵을 공전하는 것은 전자들이다'를 의미합니다.")
            ],
            [
                ("What particles reside inside the central atomic nucleus?",
                 "중심 원자핵 내부에는 어떤 입자들이 존재하는가?",
                 ["Only negative electrons", "Positively charged protons and uncharged neutrons", "Pure light photons only", "Liquid chemical water molecules"],
                 1,
                 "두 번째 문장에 양전하를 띤 양성자와 전하 없는 중성자가 원자핵에 있다고 나와 있습니다."),
                ("What electrical charge do orbiting electrons possess?",
                 "궤도를 도는 전자는 어떤 전하를 띠고 있는가?",
                 ["Positive charge", "Negative charge", "Zero charge", "Unstable magnetic charge"],
                 1,
                 "세 번째 문장에 음전하를 띤 전자(negatively charged electrons)라고 명시되어 있습니다."),
                ("Why is more than 99 percent of an atom's volume empty space?",
                 "왜 원자 부피의 99퍼센트 이상이 빈 공간인가?",
                 ["Because electrons are situated vast distances away from the tiny nucleus", "Because protons dissolve in water immediately", "Because atoms only exist when painted by artists", "Because neutrons push all matter out into space"],
                 0,
                 "마지막 문장에 전자가 미세한 핵으로부터 광대한 거리에 위치해 있기 때문이라고 설명합니다.")
            ]
        ),
        (
            "b-95",
            "Why Migrating Birds Fly in a V-Formation",
            "철새들이 V자 대형으로 비행하는 공기역학적 이유",
            "Avian Biology & Aerodynamics",
            "Nature & Oxford Department of Zoology Field Studies",
            "기러기와 두루미 같은 대형 철새들은 앞선 새의 날갯짓이 만드는 상승 기류를 활용하여 에너지를 절약하기 위해 V자 편대 비행을 합니다.",
            [
                ("Flocks of migratory birds / such as geese, cranes, and pelicans / frequently fly in a distinct V-shaped formation.",
                 "기러기, 두루미, 펠리컨과 같은 / 철새 무리는 / 독특한 V자 형태의 편대로 자주 비행합니다.",
                 "Flocks of migratory birds / such as geese, cranes, and pelicans / frequently fly in a distinct V-shaped formation."),
                ("Aerodynamic researchers discovered / that this precise geometry / provides significant energy savings during exhausting transcontinental journeys.",
                 "공기역학 연구자들은 / 이 정밀한 기하학적 형태가 / 피로한 대륙 횡단 여정 동안 상당한 에너지 절감을 제공한다는 점을 / 발견했습니다.",
                 "Aerodynamic researchers discovered / that this precise geometry / provides significant energy savings / during exhausting transcontinental journeys."),
                ("When the lead bird flaps its wings, / it generates an upward swirl of circulating air / known as upwash behind its wingtips.",
                 "선두 새가 날개를 퍼덕일 때, / 날개 끝 뒤편으로 상승 기류(업워시)라 알려진 / 위로 소용돌이치는 순환 공기를 생성합니다.",
                 "When the lead bird flaps its wings, / it generates an upward swirl of circulating air / known as upwash behind its wingtips."),
                ("Trailing birds position themselves precisely in this wake, / riding the upward air currents to conserve heart rate and physical endurance.",
                 "뒤따르는 새들은 이 후류에 정확히 위치하여, / 심박수와 신체적 지구력을 보존하기 위해 상승 기류를 탑니다.",
                 "Trailing birds position themselves precisely in this wake, / riding the upward air currents / to conserve heart rate and physical endurance.")
            ],
            [
                ("migratory", "adj.", "이주하는, 철새의", "Migratory species require protected international resting wetlands."),
                ("flock", "n.", "무리, 떼 (새·양 등)", "A large flock of starlings swooped gracefully across the dusk sky."),
                ("upwash", "n.", "상승 기류 (날개 끝 와류)", "Formation flyers harness upwash to reduce aerodynamic drag."),
                ("wake", "n.", "지나간 자국, 후류", "Speedboats leave a frothy white wake across the calm lake surface.")
            ],
            [
                ("provides significant savings during ~", "'~ 동안 상당한 절감을 제공한다' 3형식 문장입니다."),
                (", riding ~", "동시동작 분사구문으로 '상승 기류를 타면서'로 해석됩니다.")
            ],
            [
                ("What benefit does the V-formation provide to migrating birds?",
                 "V자 대형은 이동하는 새들에게 어떤 이점을 제공하는가?",
                 ["It makes them invisible to ground hunters.", "It provides significant energy savings during exhausting flights.", "It heats their feathers up to boiling temperatures.", "It allows them to sleep without flapping wings."],
                 1,
                 "두 번째 문장에 피로한 비행 동안 상당한 에너지 절감(significant energy savings)을 제공한다고 나와 있습니다."),
                ("What does the lead bird's flapping wings create behind its wingtips?",
                 "선두 새의 날갯짓은 날개 끝 뒤편에 무엇을 만들어내는가?",
                 ["A dangerous vacuum that sucks birds down", "An upward swirl of circulating air known as upwash", "A cloud of thick grey smoke", "Heavy rain showers"],
                 1,
                 "세 번째 문장에 상승 기류(upward swirl of circulating air known as upwash)를 생성한다고 명시되어 있습니다."),
                ("Why do trailing birds position themselves in the wake of the bird ahead?",
                 "뒤따르는 새들은 왜 앞선 새의 후류에 자리를 잡는가?",
                 ["To ride upward currents and conserve endurance", "To peck at the leader's tail feathers for fun", "To block sunlight from reaching the ground", "To steal food from the leader's beak"],
                 0,
                 "마지막 문장에 상승 기류를 타고 심박수와 지구력을 보존하기 위함이라고 설명합니다.")
            ]
        ),
        (
            "b-96",
            "The History of the Ancient Silk Road",
            "고대 실크로드의 교역망과 문화 교류",
            "World History",
            "UNESCO World Heritage Silk Roads Programme",
            "실크로드는 아시아와 지중해를 잇는 고대 교역로망으로, 비단과 향신료뿐만 아니라 종교, 과학, 예술을 전달하는 문명의 가교였습니다.",
            [
                ("The Silk Road was an expansive network / of ancient caravan trade routes / connecting China with the Mediterranean basin.",
                 "실크로드는 중국과 지중해 분지를 연결하던 / 고대 캐러밴 교역로들의 / 광대한 네트워크였습니다.",
                 "The Silk Road was an expansive network / of ancient caravan trade routes / connecting China with the Mediterranean basin."),
                ("Established during the Han Dynasty over two thousand years ago, / it traversed treacherous deserts, mountain passes, and oasis kingdoms.",
                 "2,000여 년 전 한나라 시기에 개척된 / 이 길은 위험천만한 사막, 산악 고개, 오아시스 왕국들을 가로질렀습니다.",
                 "Established during the Han Dynasty over two thousand years ago, / it traversed treacherous deserts, / mountain passes, and oasis kingdoms."),
                ("Merchants traded luxurious silk, / fragrant spices, porcelain, jade, and glassware across vast continental expanses.",
                 "상인들은 광대한 대륙의 넓이에 걸쳐 / 고급스러운 비단, / 향기로운 향신료, 도자기, 옥, 유리그릇을 교역했습니다.",
                 "Merchants traded luxurious silk, / fragrant spices, porcelain, jade, / and glassware across vast continental expanses."),
                ("Even more profoundly, / the Silk Road facilitated the cross-pollination of revolutionary ideas, / transmitting papermaking, astronomy, and Buddhism between East and West.",
                 "더욱 지대하게는, / 실크로드는 혁명적 사상들의 상호 융합을 촉진하여, / 제지술, 천문학, 불교를 동서양 사이에 전파했습니다.",
                 "Even more profoundly, / the Silk Road facilitated the cross-pollination of revolutionary ideas, / transmitting papermaking, astronomy, / and Buddhism between East and West.")
            ],
            [
                ("caravan", "n.", "캐러밴, 낙타 대상 무역단", "Camel caravans traveled across the Sahara carrying blocks of salt."),
                ("treacherous", "adj.", "위험한, 배반하는", "Icy mountain roads are treacherous for heavy transport trucks."),
                ("porcelain", "n.", "도자기, 자기", "Chinese Ming Dynasty porcelain was coveted by European aristocrats."),
                ("cross-pollination", "n.", "상호 교류, 상호 수정", "Interdisciplinary seminars encourage the cross-pollination of creative ideas.")
            ],
            [
                ("connecting China with ~", "현재분사구로 ancient caravan trade routes를 수식합니다."),
                (", transmitting ~", "분사구문으로 '제지술 등을 전파하면서'로 해석됩니다.")
            ],
            [
                ("What was the Silk Road according to the passage?",
                 "본문에 따르면 실크로드란 무엇이었는가?",
                 ["A modern paved highway for automobiles", "An ancient network of caravan trade routes connecting China and the Mediterranean", "A single wooden bridge spanning the Pacific Ocean", "An underwater canal dug by ancient sailors"],
                 1,
                 "첫 문장에 중국과 지중해를 잇는 고대 캐러밴 무역로망이라고 명시되어 있습니다."),
                ("Which Chinese dynasty established the Silk Road over 2,000 years ago?",
                 "2,000여 년 전 실크로드를 개척한 중국의 왕조는 어디인가?",
                 ["The Tang Dynasty", "The Han Dynasty", "The Qing Dynasty", "The Song Dynasty"],
                 1,
                 "두 번째 문장에 한나라(the Han Dynasty) 시기 개척되었다고 나와 있습니다."),
                ("What intellectual and cultural elements were transmitted along the Silk Road besides physical goods?",
                 "물리적 상품 외에 실크로드를 따라 전파된 지적·문화적 요소는 무엇인가?",
                 ["Papermaking, astronomy, and Buddhism", "Steam engines and computers", "Printing press and factory robots", "Plastic toys and digital watches"],
                 0,
                 "마지막 문장에 제지술, 천문학, 불교(papermaking, astronomy, and Buddhism)가 전파되었다고 설명합니다.")
            ]
        ),
        (
            "b-97",
            "How Polar Bears Hunt on Arctic Sea Ice",
            "북극곰의 해빙 위 사냥 생태",
            "Arctic Ecology",
            "Polar Bears International & WWF Arctic Field Reports",
            "북극곰은 뛰어난 후각과 놀라운 인내력으로 얼음 숨구멍에서 고리무늬물범이 숨을 쉬러 올라오기를 기다리는 정지 사냥을 펼칩니다.",
            [
                ("Polar bears are apex marine predators / uniquely adapted to the frozen seascape of the high Arctic.",
                 "북극곰은 고위도 북극의 얼어붙은 바다 풍경에 / 독특하게 적응한 / 최상위 해양 포식자입니다.",
                 "Polar bears are apex marine predators / uniquely adapted / to the frozen seascape of the high Arctic."),
                ("Their primary food source is the ringed seal, / an energy-rich blubber delicacy indispensable for polar bear winter survival.",
                 "그들의 주된 먹이원은 고리무늬물범으로, / 북극곰의 겨울 생존에 없어서는 안 될 에너지가 풍부한 지방 진미입니다.",
                 "Their primary food source is the ringed seal, / an energy-rich blubber delicacy / indispensable for polar bear winter survival."),
                ("Because seals easily outswim bears in open water, / polar bears rely on a patient ambush technique called still-hunting.",
                 "물범은 탁 트인 물속에서 곰보다 훨씬 쉽게 헤엄쳐 달아나므로, / 북극곰은 정지 사냥이라 불리는 끈기 있는 매복 기술에 의존합니다.",
                 "Because seals easily outswim bears in open water, / polar bears rely on a patient ambush technique / called still-hunting."),
                ("A bear uses its keen sense of smell to locate an active breathing hole in the ice, / crouching motionless for hours until the seal surfaces for air.",
                 "곰은 예리한 후각을 이용해 얼음의 활성 숨구멍을 찾아내고, / 물범이 공기를 마시러 수면으로 올라올 때까지 몇 시간이고 미동 없이 웅크려 기다립니다.",
                 "A bear uses its keen sense of smell / to locate an active breathing hole in the ice, / crouching motionless for hours / until the seal surfaces for air.")
            ],
            [
                ("apex", "adj./n.", "최상위의, 정점", "Lions and wolves occupy the apex of their regional food chains."),
                ("outswim", "v.", "~보다 수영을 더 잘하다/빠르게 헤엄치다", "Fish outswim scuba divers with effortless tail flicks."),
                ("ambush", "n.", "매복, 기습", "Predatory leopards launch sudden ambushes from leafy tree branches."),
                ("motionless", "adj.", "움직이지 않는, 고요한", "The deer stood motionless, listening attentively for forest predators.")
            ],
            [
                ("uniquely adapted to ~", "과거분사구로 apex marine predators를 수식합니다."),
                (", crouching motionless ~", "분사구문으로 '미동도 없이 웅크리면서' 동시상황을 묘사합니다.")
            ],
            [
                ("What is the primary food source of polar bears?",
                 "북극곰의 주된 먹이원은 무엇인가?",
                 ["Fresh pine needles from Arctic trees", "The ringed seal", "Flying seagulls and arctic geese", "Berries and sweet roots in tundra soil"],
                 1,
                 "두 번째 문장에 고리무늬물범(the ringed seal)이 주된 먹이원이라고 명시되어 있습니다."),
                ("Why do polar bears avoid chasing seals in open water?",
                 "북극곰은 왜 트인 물속에서 물범을 쫓는 것을 피하는가?",
                 ["Because open water instantly turns polar bear fur black", "Because seals easily outswim bears in open water", "Because polar bears are completely unable to swim", "Because salt water burns polar bear eyes"],
                 1,
                 "세 번째 문장에 물범이 탁 트인 물에서 곰보다 훨씬 수영을 잘하기 때문이라고 나와 있습니다."),
                ("What hunting technique involves waiting motionless near an ice breathing hole?",
                 "얼음 숨구멍 근처에서 움직이지 않고 기다리는 사냥 기술은 무엇인가?",
                 ["Trolling", "Still-hunting", "Net casting", "Aerial swooping"],
                 1,
                 "세 번째 문장에 정지 사냥(still-hunting)이라 불리는 매복 기술이라고 설명합니다.")
            ]
        ),
        (
            "b-98",
            "The Aerodynamics of Returning Boomerangs",
            "돌아오는 부메랑의 공기역학 원리",
            "Applied Physics",
            "Scientific American & Australian Indigenous Aerodynamic Studies",
            "부메랑의 비대칭적인 날개 단면(양력 차이)과 회전 스핀에 의한 자이로스코프 세차 운동이 결합하여 던진 사람에게 호를 그리며 되돌아옵니다.",
            [
                ("The returning boomerang is a brilliant aerodynamic invention / pioneered by Indigenous Australians thousands of years ago.",
                 "되돌아오는 부메랑은 수천 년 전 호주 원주민들에 의해 개척된 / 탁월한 공기역학적 발명품입니다.",
                 "The returning boomerang is a brilliant aerodynamic invention / pioneered by Indigenous Australians / thousands of years ago."),
                ("Each wing of a boomerang is shaped like an aircraft airfoil, / flat on the bottom and curved on top to generate lift as it spins.",
                 "부메랑의 각 날개는 비행기 에어포일처럼 성형되어, / 회전할 때 양력을 생성하기 위해 밑면은 평평하고 윗면은 둥글게 굴곡져 있습니다.",
                 "Each wing of a boomerang is shaped like an aircraft airfoil, / flat on the bottom and curved on top / to generate lift as it spins."),
                ("Because the forward-rotating wing travels faster through the air than the retreating wing, / it experiences greater aerodynamic lift.",
                 "전방으로 회전하는 날개가 후퇴하는 날개보다 공기 중을 더 빠르게 통과하기 때문에, / 더 큰 공기역학적 양력을 받습니다.",
                 "Because the forward-rotating wing travels faster through the air / than the retreating wing, / it experiences greater aerodynamic lift."),
                ("This uneven lifting force exerts a twisting torque / that causes gyroscopic precession, / steering the spinning boomerang in a broad sweeping curve back to the thrower.",
                 "이 불균등한 양력은 비틀림 토크를 가하여 / 자이로스코프 세차 운동을 일으키며, / 회전하는 부메랑을 넓은 원호를 그리며 던진 사람에게 되돌아오도록 조종합니다.",
                 "This uneven lifting force exerts a twisting torque / that causes gyroscopic precession, / steering the spinning boomerang / in a broad sweeping curve back to the thrower.")
            ],
            [
                ("airfoil", "n.", "에어포일 (날개 단면 형상)", "Airfoils create lift through air velocity differentials."),
                ("torque", "n.", "토크, 회전력", "Wrenches apply torque to tighten stubborn plumbing bolts."),
                ("precession", "n.", "세차 운동 (회전축이 비틀려 회전함)", "A spinning toy top wobbles in gyroscopic precession as it slows down."),
                ("sweeping", "adj.", "광범위한, 둥근 호를 그리는", "The airplane banked in a sweeping turn over the bay.")
            ],
            [
                ("pioneered by ~", "과거분사구로 an aerodynamic invention을 수식합니다."),
                (", steering ~", "분사구문으로 '부메랑을 조종하면서' 결과를 나타냅니다.")
            ],
            [
                ("Who originally invented the returning boomerang thousands of years ago?",
                 "수천 년 전 돌아오는 부메랑을 처음 발명한 사람들은 누구인가?",
                 ["Ancient Viking shipbuilders", "Indigenous Australians", "Medieval German blacksmiths", "Egyptian chariot racers"],
                 1,
                 "첫 문장에 호주 원주민들(Indigenous Australians)에 의해 개척되었다고 명시되어 있습니다."),
                ("Why does the forward-rotating wing experience greater lift than the retreating wing?",
                 "왜 전방 회전 날개가 후퇴 날개보다 더 큰 양력을 받는가?",
                 ["It travels faster through the air than the retreating wing.", "It is painted with bright glowing fluorescent paint.", "It is three times heavier than the other wing.", "It absorbs hot engine steam from the air."],
                 0,
                 "세 번째 문장에 전방 회전 날개가 공기 중을 더 빠르게 이동하기 때문이라고 설명합니다."),
                ("What physical phenomenon causes the boomerang to curve back to the thrower?",
                 "부메랑이 던진 사람에게 호를 그리며 돌아오게 만드는 물리적 현상은 무엇인가?",
                 ["Gyroscopic precession caused by uneven lifting forces", "Magnetic pull from underground iron rocks", "Strong acoustic sound echoes from surrounding trees", "Electrical charges from thunderstorms"],
                 0,
                 "마지막 문장에 불균등한 양력으로 인한 자이로스코프 세차 운동(gyroscopic precession) 때문이라고 나와 있습니다.")
            ]
        ),
        (
            "b-99",
            "Why Sleep Is Essential for Memory Consolidation",
            "수면이 기억 응고화에 필수적인 이유",
            "Neuroscience",
            "National Institute of Neurological Disorders and Stroke (NINDS)",
            "잠을 자는 동안 뇌는 해마에 임시 저장된 기억을 대뇌 피질로 전송하여 영구적인 장기 기억으로 고정시키고 불필요한 시냅스를 정리합니다.",
            [
                ("Sleep is not a passive shutdown of consciousness, / but an active biological necessity / vital for cognitive health.",
                 "수면은 의식의 수동적인 정지 상태가 아니라, / 인지적 건강에 필수적인 / 능동적인 생물학적 필수 과정입니다.",
                 "Sleep is not a passive shutdown of consciousness, / but an active biological necessity / vital for cognitive health."),
                ("During waking hours, / the brain records sensory experiences as fragile temporary memory traces / in a seahorse-shaped region called the hippocampus.",
                 "깨어있는 시간 동안, / 뇌는 해마라 불리는 해마 모양의 영역에 / 감각적 경험들을 깨지기 쉬운 임시 기억 흔적으로 기록합니다.",
                 "During waking hours, / the brain records sensory experiences / as fragile temporary memory traces / in a seahorse-shaped region called the hippocampus."),
                ("During deep non-REM and REM sleep phases, / coordinated slow electrical waves replay these daytime patterns, / transferring memories to the durable neocortex for permanent storage.",
                 "깊은 비REM 및 REM 수면 단계 동안, / 조율된 느린 전기 뇌파가 이러한 낮 시간의 패턴들을 재생하여, / 영구 저장을 위해 기억을 내구성 있는 신피질로 전송합니다.",
                 "During deep non-REM and REM sleep phases, / coordinated slow electrical waves replay these daytime patterns, / transferring memories / to the durable neocortex for permanent storage."),
                ("Simultaneously, / synaptic pruning clears out redundant neural connections, / refreshing cognitive processing capacity for tomorrow's learning.",
                 "동시에, / 시냅스 가지치기가 불필요한 신경 연결들을 제거하여, / 내일의 학습을 위한 인지 처리 역량을 새롭게 갱신합니다.",
                 "Simultaneously, / synaptic pruning clears out redundant neural connections, / refreshing cognitive processing capacity / for tomorrow's learning.")
            ],
            [
                ("fragile", "adj.", "취약한, 부서지기 쉬운", "Delicate porcelain teacups are extremely fragile during moving."),
                ("neocortex", "n.", "신피질 (고차원 뇌 기능을 담당하는 대뇌 외층)", "The human neocortex governs language, spatial reasoning, and conscious thought."),
                ("redundant", "adj.", "불필요한, 과잉의", "Delete redundant adjectives to make your prose punchy and clear."),
                ("pruning", "n.", "가지치기, 전정", "Regular pruning encourages fruit trees to develop robust blossoms.")
            ],
            [
                ("not A, but B", "'A가 아니라 B' 대조 구문입니다."),
                (", transferring memories ~", "분사구문으로 '기억을 전송하면서' 연속적 작용을 나타냅니다.")
            ],
            [
                ("Where does the brain temporarily record daytime memory traces while awake?",
                 "깨어있는 동안 뇌는 낮 시간의 기억 흔적을 어디에 임시로 기록하는가?",
                 ["In bone marrow cells", "In the hippocampus", "Inside the skull teeth", "In the thyroid gland"],
                 1,
                 "두 번째 문장에 해마(the hippocampus)에 임시 기억 흔적으로 기록한다고 명시되어 있습니다."),
                ("What happens to memories during deep sleep phases according to the text?",
                 "본문에 따르면 깊은 수면 단계 동안 기억에는 무슨 일이 일어나는가?",
                 ["They are completely erased forever.", "They are replayed and transferred to the neocortex for permanent storage.", "They turn into liquid spinal fluid.", "They prevent the heart from beating."],
                 1,
                 "세 번째 문장에 주간 패턴이 재생되어 영구 저장을 위해 신피질로 전송된다고 나와 있습니다."),
                ("What is the function of synaptic pruning during sleep?",
                 "수면 중 시냅스 가지치기의 기능은 무엇인가?",
                 ["Clearing out redundant neural connections to refresh cognitive capacity", "Removing oxygen from brain cells permanently", "Doubling skull thickness every night", "Freezing nerve impulses permanently"],
                 0,
                 "마지막 문장에 불필요한 신경 연결을 제거하여 인지 처리 역량을 갱신한다고 설명합니다.")
            ]
        ),
        (
            "b-100",
            "The Frozen Realm of the Kuiper Belt",
            "카이퍼 벨트의 얼음 천체들과 태양계의 기원",
            "Planetary Astronomy",
            "NASA Solar System Exploration Science Guide",
            "해왕성 궤도 너머에 위치한 카이퍼 벨트는 명왕성을 비롯한 수십만 개의 얼음 천체들이 보존된 태양계 형성 초기의 원시 유적지입니다.",
            [
                ("Far beyond the orbit of Neptune lies a vast ring of icy debris / known as the Kuiper Belt.",
                 "해왕성의 궤도 저 멀리 너머에는 / 카이퍼 벨트라 알려진 / 얼음 잔해들의 광대한 고리가 자리 잡고 있습니다.",
                 "Far beyond the orbit of Neptune / lies a vast ring of icy debris / known as the Kuiper Belt."),
                ("This frigid celestial zone extends / from roughly thirty to fifty astronomical units / from our central sun.",
                 "이 몹시 추운 천체 구역은 / 중심 태양으로부터 / 대략 30에서 50 천문단위(AU)까지 뻗어 있습니다.",
                 "This frigid celestial zone extends / from roughly thirty to fifty astronomical units / from our central sun."),
                ("It contains hundreds of thousands of frozen remnants / composed of water, methane, and ammonia ices / left over from the solar system's birth four billion years ago.",
                 "이곳은 40억 년 전 태양계 탄생 시 남겨진 / 물, 메탄, 암모니아 얼음으로 이루어진 / 수십만 개의 얼어붙은 잔해들을 포함하고 있습니다.",
                 "It contains hundreds of thousands of frozen remnants / composed of water, methane, and ammonia ices / left over from the solar system's birth / four billion years ago."),
                ("Dwarf planets such as Pluto and Makemake reside here, / serving as primitive time capsules / that preserve clues about how planetary systems form.",
                 "명왕성과 마케마케 같은 왜소행성들이 이곳에 머물며, / 행성계가 어떻게 형성되는지에 대한 단서를 보존하는 / 원시적인 타임캡슐 역할을 합니다.",
                 "Dwarf planets such as Pluto and Makemake reside here, / serving as primitive time capsules / that preserve clues about how planetary systems form.")
            ],
            [
                ("debris", "n.", "잔해, 부스러기", "Space agencies track orbital debris to protect working satellites."),
                ("frigid", "adj.", "몹시 추운, 혹한의", "Frigid arctic blizzards blanketed the polar research station in ice."),
                ("remnants", "n. (pl.)", "잔존물, 유물", "Stone columns are the only visible remnants of the ancient Roman forum."),
                ("astronomical unit", "n.", "천문단위 (지구-태양 간 평균 거리, 약 1.5억 km)", "One astronomical unit corresponds to approximately 150 million kilometers.")
            ],
            [
                ("Far beyond the orbit lies ~", "장소 부사구 도치 구문입니다."),
                ("left over from ~", "'~에서 남겨진' 과거분사 수식구입니다.")
            ],
            [
                ("Where is the Kuiper Belt located in our solar system?",
                 "우리 태양계에서 카이퍼 벨트는 어디에 위치해 있는가?",
                 ["Between Mercury and the sun", "Far beyond the orbit of Neptune", "Inside the core of the planet Jupiter", "Between Earth and the moon"],
                 1,
                 "첫 문장에 해왕성 궤도 저 멀리 너머(far beyond the orbit of Neptune)에 위치한다고 명시되어 있습니다."),
                ("What materials primarily compose the frozen remnants in the Kuiper Belt?",
                 "카이퍼 벨트의 얼어붙은 잔존물들은 주로 어떤 물질들로 구성되어 있는가?",
                 ["Burning sulfur and volcanic molten lava", "Water, methane, and ammonia ices", "Solid gold and silver jewelry", "Pure radioactive uranium metal"],
                 1,
                 "세 번째 문장에 물, 메탄, 암모니아 얼음(water, methane, and ammonia ices)으로 구성되어 있다고 나와 있습니다."),
                ("Which dwarf planet is mentioned as residing in the Kuiper Belt?",
                 "카이퍼 벨트에 머무는 왜소행성으로 언급된 것은 무엇인가?",
                 ["Mars", "Pluto", "Saturn", "Venus"],
                 1,
                 "마지막 문장에 명왕성(Pluto)과 마케마케가 이곳에 머문다고 설명합니다.")
            ]
        )
    ]
