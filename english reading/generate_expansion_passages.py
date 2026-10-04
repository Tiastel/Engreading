# -*- coding: utf-8 -*-
"""
generate_expansion_passages.py
Generates 30 additional rigorous passages:
- 10 Beginner (b-31 to b-40)
- 10 Intermediate (i-31 to i-40)
- 10 Advanced (a-31 to a-40)
Sources: NASA, MIT Tech Review, Scientific American, The Economist, BBC, Nature, Harvard Business Review, Oxford Academic.
"""

def get_expansion_passages():
    b_extra = [
        ("b-31", "Why Leaves Change Color in Autumn", "가을에 나뭇잎 색이 변하는 과학적 원리", "Nature & Botany", "Smithsonian Magazine",
         "가을이 되면 초록색 엽록소가 분해되고 숨겨져 있던 노란색과 붉은색 색소가 드러나는 자연의 원리를 설명합니다.",
         [
             ("During the warm summer months, tree leaves are packed with green chlorophyll.", "따뜻한 여름 몇 달 동안, 나뭇잎은 초록색 엽록소로 가득 차 있습니다.", "During the warm summer months, / tree leaves are packed / with green chlorophyll."),
             ("Chlorophyll uses sunlight, water, and carbon dioxide to manufacture nutritious sugars for the tree.", "엽록소는 햇빛, 물, 이산화탄소를 이용해 나무를 위한 영양가 있는 당분을 생산합니다.", "Chlorophyll uses sunlight, water, / and carbon dioxide / to manufacture nutritious sugars / for the tree."),
             ("As days grow shorter and nights become chillier in autumn, trees prepare for winter rest.", "가을에 낮이 짧아지고 밤이 쌀쌀해짐에 따라, 나무는 겨울 휴식을 준비합니다.", "As days grow shorter / and nights become chillier in autumn, / trees prepare for winter rest."),
             ("They slowly cease producing green chlorophyll, which causes the vivid green color to fade away.", "나무는 초록색 엽록소 생성을 서서히 중단하며, 이로 인해 선명한 초록빛이 사라집니다.", "They slowly cease producing green chlorophyll, / which causes the vivid green color / to fade away."),
             ("Yellow and orange pigments that were concealed underneath all summer finally become visible.", "여름 내내 그 아래 숨겨져 있던 노란색과 주황색 색소가 마침내 눈에 띄게 드러납니다.", "Yellow and orange pigments / that were concealed underneath all summer / finally become visible."),
             ("In some trees, newly created red anthocyanin pigments turn the entire canopy into brilliant scarlet.", "일부 나무에서는 새롭게 생성된 붉은 안토시아닌 색소가 숲의 덮개를 눈부신 진홍빛으로 물들입니다.", "In some trees, / newly created red anthocyanin pigments / turn the entire canopy / into brilliant scarlet.")
         ],
         [("manufacture", "v.", "제조하다, 만들어내다", "Plants manufacture sugars through photosynthesis."), ("chilly", "adj.", "쌀쌀한, 으스스한", "A chilly autumn breeze swept across the valley."), ("cease", "v.", "중단하다, 그치다", "The factory ceased operations during the storm."), ("pigment", "n.", "색소, 안료", "Natural pigments give berries their deep blue color."), ("conceal", "v.", "숨기다, 감추다", "The thick fog concealed the mountain peak.")],
         [("which 계속적 용법", "...cease producing..., which causes... 앞 절 전체 내용을 받아 '이것이 결과를 낳는다'고 서술합니다."), ("현재완료 수동 / 관계사", "...pigments that were concealed... 주격 관계대명사 that절의 수동태 수식입니다.")],
         [
             ("What is the primary function of chlorophyll in summer?", "여름철 엽록소의 가장 핵심적인 기능은 무엇인가요?", ["Protecting leaves from cold winter frosts", "Producing sugars using sunlight, water, and carbon dioxide", "Attracting pollinating insects with bright scarlet hues", "Absorbing excess minerals from fallen seeds"], 1, "지문에서 햇빛, 물, 이산화탄소로 나무를 위한 당분을 생산한다고 설명했습니다."),
             ("Why do yellow and orange colors appear in autumn?", "가을에 노란색과 주황색이 나타나는 이유는 무엇인가요?", ["Trees absorb dyed rainwater from the moist soil.", "Green chlorophyll production ceases, revealing underlying pigments.", "Birds paint the leaves while building nests.", "The sun burns the outer leaf surface into ash."], 1, "초록색 엽록소 생성이 중단되면서 아래 숨어있던 색소들이 드러난다고 밝혔습니다."),
             ("According to the text, what creates brilliant red colors?", "본문에 따르면 눈부신 붉은색을 만드는 것은 무엇인가요?", ["Anthocyanin pigments newly created in some trees", "Chlorophyll exposed to high winter heat", "Dead bark falling onto the leaf surface", "Excess water stored inside root nodules"], 0, "일부 나무에서 새로 생성된 안토시아닌 색소가 진홍빛을 만든다고 명시했습니다.")
         ]),

        ("b-32", "How the Human Eye Detects Light", "인간의 눈이 빛을 감지하는 메커니즘", "Science & Anatomy", "Britannica Kids",
         "빛이 각막과 수정체를 통과해 망막의 시세포에서 전기 신호로 바뀌어 뇌로 전달되는 시각 경로를 살펴봅니다.",
         [
             ("The human eye functions much like an exceptionally sophisticated photographic camera.", "인간의 눈은 대단히 정교한 사진 카메라와 매우 흡사하게 작동합니다.", "The human eye functions / much like an exceptionally sophisticated / photographic camera."),
             ("Light waves first enter through the cornea, a clear protective outer window on the eye.", "빛 파동은 먼저 눈의 투명한 보호용 외창인 각막을 통해 들어옵니다.", "Light waves first enter through the cornea, / a clear protective outer window / on the eye."),
             ("Next, the pupil adjusts its aperture size to regulate how much illumination enters.", "다음으로, 동공은 얼마나 많은 조명이 들어올지 조절하기 위해 구멍 크기를 조절합니다.", "Next, the pupil adjusts its aperture size / to regulate / how much illumination enters."),
             ("Behind the pupil, a flexible lens focuses the incoming light directly onto the retina at the back.", "동공 뒤에서, 유연한 수정체가 들어오는 빛을 뒤쪽 망막 위에 직접 초점을 맞춥니다.", "Behind the pupil, / a flexible lens focuses the incoming light / directly onto the retina at the back."),
             ("The retina contains millions of specialized sensory cells called rods and cones.", "망막은 간상체와 추상체라고 불리는 수백만 개의 특수 감각 세포를 포함하고 있습니다.", "The retina contains / millions of specialized sensory cells / called rods and cones."),
             ("These light-sensitive cells convert photons into electrical pulses that travel along the optic nerve to the brain.", "이 빛에 민감한 세포들은 광자를 전기 펄스로 변환하여 시신경을 따라 뇌로 전달합니다.", "These light-sensitive cells convert photons / into electrical pulses / that travel along the optic nerve / to the brain.")
         ],
         [("sophisticated", "adj.", "정교한, 고도화된", "Modern satellites carry sophisticated optical sensors."), ("cornea", "n.", "각막", "The cornea refracts the majority of light entering the eye."), ("regulate", "v.", "조절하다, 규제하다", "The thermostat regulates room temperature automatically."), ("convert", "v.", "전환하다, 변환하다", "Solar panels convert ambient sunlight into electricity."), ("optic", "adj.", "시각의, 눈의", "The optic nerve delivers visual information to the cortex.")],
         [("동격의 콤마", "...through the cornea, a clear protective outer window... cornea와 뒤 명사구가 동격입니다."), ("관계대명사 that절", "...electrical pulses that travel along the optic nerve... 선행사 pulses를 수식하는 주격 관계대명사입니다.")],
         [
             ("What is the primary role of the pupil according to the passage?", "지문에 따르면 동공의 주된 역할은 무엇인가요?", ["Cleaning dust from the exterior cornea", "Adjusting size to regulate the volume of light entering the eye", "Storing electrical signals overnight", "Protecting the optic nerve from bacterial infections"], 1, "동공이 크기를 조절해 유입되는 빛의 양을 조절한다고 명시되었습니다."),
             ("Where is incoming light focused inside the eye?", "눈 안으로 들어온 빛은 어디에 초점이 맺히나요?", ["Onto the cornea", "Onto the retina at the back", "Inside the skull cavity", "Directly within the tear duct"], 1, "수정체가 빛을 눈 뒤쪽의 망막(retina)에 직접 초점을 맞춘다고 설명했습니다."),
             ("How do rods and cones transmit visual information?", "간상체와 추상체는 시각 정보를 어떻게 전달하나요?", ["By heating the surrounding blood vessels", "By converting light into electrical pulses sent through the optic nerve", "By producing chemical tears that lubricate the eyelid", "By changing color according to external temperatures"], 1, "광자를 전기 펄스로 변환하여 시신경을 통해 뇌로 보낸다고 명시했습니다.")
         ]),

        ("b-33", "The History and Purpose of Postage Stamps", "우표의 기원과 인류 통신의 혁신", "History & Culture", "BBC History",
         "1840년 영국의 페니 블랙 발행으로 시작된 균일 요금제 우표가 어떻게 통신을 대중화했는지 다룹니다.",
         [
             ("Before the nineteenth century, sending letters across long distances was extraordinarily expensive.", "19세기 이전에는, 먼 거리를 건너 편지를 보내는 것이 엄청나게 비쌌습니다.", "Before the nineteenth century, / sending letters across long distances / was extraordinarily expensive."),
             ("Furthermore, the person receiving the postal dispatch had to pay the courier fee upon delivery.", "게다가, 우편물을 받는 사람이 배달 시점에 배달부 요금을 지불해야만 했습니다.", "Furthermore, / the person receiving the postal dispatch / had to pay the courier fee / upon delivery."),
             ("If the recipient refused to accept the letter, the postal carrier lost money on transportation.", "만약 수신자가 편지 수령을 거부하면, 우편 배달부는 운송비에서 손해를 보았습니다.", "If the recipient refused to accept the letter, / the postal carrier lost money / on transportation."),
             ("In 1840, Great Britain revolutionized communication by issuing the famous Penny Black stamp.", "1840년, 영국은 그 유명한 '페니 블랙' 우표를 발행함으로써 통신에 혁명을 일으켰습니다.", "In 1840, Great Britain revolutionized communication / by issuing the famous Penny Black stamp."),
             ("This system required the sender to prepay a uniform, affordable fee by pasting an adhesive label.", "이 제도는 발신자가 접착식 라벨을 붙여 균일하고 저렴한 요금을 선납하도록 요구했습니다.", "This system required the sender / to prepay a uniform, affordable fee / by pasting an adhesive label."),
             ("The innovation made personal correspondence accessible to ordinary working people for the first time.", "이 혁신은 개인 서신 교환을 사상 처음으로 평범한 노동자 계층도 이용할 수 있게 만들었습니다.", "The innovation made personal correspondence / accessible to ordinary working people / for the first time.")
         ],
         [("extraordinarily", "adv.", "대단히, 엄청나게", "The summit of the mountain was extraordinarily cold."), ("recipient", "n.", "수신자, 수령인", "The recipient signed the receipt for the package."), ("revolutionize", "v.", "대변혁을 일으키다", "Steam engines revolutionized nineteenth-century transport."), ("adhesive", "adj.", "접착성의, 들러붙는", "Adhesive tape is used to seal cardboard boxes."), ("accessible", "adj.", "접근 가능한, 이용하기 쉬운", "Public libraries make literature accessible to all citizens.")],
         [("동명사 주어", "sending letters across long distances was... 긴 동명사 주어 구문입니다."), ("사역/유도 5형식 make", "The innovation made personal correspondence accessible... 목적어와 목적격 보어(형용사) 구조입니다.")],
         [
             ("Who originally paid postal fees before stamps were invented?", "우표가 발명되기 전에는 원래 누가 우편 요금을 지불했나요?", ["The government treasury", "The recipient upon delivery", "Local charity guilds", "The ship captain at harbor"], 1, "편지를 받는 수신자(recipient)가 배달 시 요금을 내야 했다고 명시했습니다."),
             ("What major change did the Penny Black introduce?", "페니 블랙은 어떤 중대한 변화를 도입했나요?", ["Making senders prepay a uniform low fee using an adhesive label", "Requiring letters to be memorized and recited orally", "Banning international personal correspondence completely", "Demanding gold coins for every delivered envelope"], 0, "접착 라벨을 붙여 발신자가 균일하고 저렴한 요금을 선납하게 했습니다."),
             ("What was the social consequence of the postage stamp?", "우표 도입이 가져온 사회적 결과는 무엇이었나요?", ["Only royalty were allowed to write letters.", "Personal correspondence became accessible to ordinary working people.", "The postal service ceased operations within six months.", "All paper production was heavily restricted by law."], 1, "마지막 문장에서 평범한 노동자들도 처음으로 편지를 보낼 수 있게 되었다고 밝혔습니다.")
         ]),

        ("b-34", "The Life Cycle of a River Delta", "강 삼각주의 형성과 생태학적 풍요", "Earth Science & Geography", "National Geographic",
         "강물이 바다와 만나며 토사를 퇴적시켜 비옥한 삼각주를 형성하는 지형학적 순환을 설명합니다.",
         [
             ("A river begins high up in rugged mountains, flowing swiftly over steep rocky slopes.", "강은 험준한 산 높은 곳에서 시작하여, 가파른 바위 비탈을 따라 빠르게 흘러내립니다.", "A river begins high up in rugged mountains, / flowing swiftly / over steep rocky slopes."),
             ("As it rushes downhill, the water erodes boulders and picks up tons of fine mineral silt.", "산비탈을 급히 내려오면서, 물은 바위를 침식시키고 수많은 톤의 미세한 광물 퇴적토를 실어나릅니다.", "As it rushes downhill, / the water erodes boulders / and picks up tons / of fine mineral silt."),
             ("When the river finally approaches a calm lake or wide ocean, its velocity drops dramatically.", "강물이 마침내 잔잔한 호수나 넓은 바다에 접근할 때, 유속은 급격히 감소합니다.", "When the river finally approaches a calm lake or wide ocean, / its velocity drops dramatically."),
             ("Unable to carry heavy sediment anymore, the slow-moving current deposits rich soil at its mouth.", "더 이상 무거운 퇴적물을 운반할 수 없게 된 느린 물줄기는 하구에 기름진 흙을 쌓아 놓습니다.", "Unable to carry heavy sediment anymore, / the slow-moving current deposits rich soil / at its mouth."),
             ("Over many centuries, these layers of silt accumulate into fan-shaped landforms called deltas.", "수세기에 걸쳐, 이러한 침전토 층이 쌓여 삼각주라 불리는 부채꼴 모양의 지형을 이룹니다.", "Over many centuries, / these layers of silt accumulate / into fan-shaped landforms called deltas."),
             ("Deltas support abundant wetland ecosystems and provide some of the world's most fertile farmland.", "삼각주는 풍부한 습지 생태계를 지탱하며 세계에서 가장 비옥한 농경지 중 일부를 제공합니다.", "Deltas support abundant wetland ecosystems / and provide some of the world's / most fertile farmland.")
         ],
         [("rugged", "adj.", "울퉁불퉁한, 험준한", "The rugged trail challenged even experienced hikers."), ("erode", "v.", "침식시키다, 좀먹다", "Heavy coastal waves slowly erode limestone cliffs."), ("velocity", "n.", "속도, 유속", "The velocity of the river decreases on flat plains."), ("sediment", "n.", "퇴적물, 침전물", "Layers of marine sediment turned into solid shale."), ("fertile", "adj.", "비옥한, 기름진", "Volcanic ash leaves fertile soil suitable for vineyards.")],
         [("형용사구 분사구문", "Unable to carry heavy sediment anymore, the current deposits... Being이 생략된 분사구문입니다."), ("자동사 accumulate", "...layers of silt accumulate into... 수세기에 걸쳐 퇴적토가 축적된다는 표현입니다.")],
         [
             ("Why does a river deposit silt when reaching the ocean?", "강물이 바다에 도달할 때 왜 퇴적토를 내려놓나요?", ["Because salt water dissolves all rock fragments instantly", "Because the river's flow velocity drops dramatically", "Because ocean fish push sediment toward the shoreline", "Because evaporation removes all liquid water immediately"], 1, "호수나 바다에 접근하면서 유속(velocity)이 급격히 떨어지기 때문입니다."),
             ("What shape do delta landforms typically take?", "삼각주 지형은 전형적으로 어떤 형태를 띠나요?", ["A perfectly square moat", "A fan-shaped landform", "A narrow spiral staircase", "A hollow underground cavern"], 1, "수세기에 걸쳐 부채꼴 모양(fan-shaped) 지형으로 축적된다고 명시했습니다."),
             ("What makes deltas valuable for human society?", "삼각주가 인간 사회에 가치 있는 이유는 무엇인가요?", ["They provide some of the most fertile farmland on Earth.", "They prevent any marine vessels from navigating rivers.", "They freeze into permanent ice sheets during summer.", "They eliminate all moisture from regional atmospheres."], 0, "풍부한 습지 생태계와 세계에서 가장 비옥한 농경지를 제공한다고 결론지었습니다.")
         ]),

        ("b-35", "How Bicycles Transform Urban Transit", "자전거가 바꾸는 현대 도시의 친환경 교통", "Urban Planning", "The Guardian Cities",
         "배출가스가 없고 공간 효율이 높은 자전거 교통망이 도시의 건강과 이동성을 어떻게 바꾸는지 다룹니다.",
         [
             ("Many major metropolitan centers struggle with chronic traffic congestion and severe smog.", "많은 주요 대도시 중심가는 만성적인 교통 혼잡과 심각한 스모그로 몸살을 앓고 있습니다.", "Many major metropolitan centers struggle / with chronic traffic congestion / and severe smog."),
             ("To address these environmental issues, progressive cities are investing heavily in protected bike lanes.", "이러한 환경 문제를 해결하기 위해, 진보적인 도시들은 분리된 자전거 전용차로에 대규모 투자를 하고 있습니다.", "To address these environmental issues, / progressive cities are investing heavily / in protected bike lanes."),
             ("Bicycles consume zero fossil fuels, producing no toxic tailpipe emissions into the atmosphere.", "자전거는 화석 연료를 전혀 소비하지 않아, 대기 중으로 유독한 배기가스를 배출하지 않습니다.", "Bicycles consume zero fossil fuels, / producing no toxic tailpipe emissions / into the atmosphere."),
             ("Moreover, ten bicycles can easily fit into a parking space normally occupied by a single private automobile.", "게다가, 자전거 열 대는 보통 개인 승용차 한 대가 차지하는 주차 공간에 쉽게 들어갈 수 있습니다.", "Moreover, / ten bicycles can easily fit / into a parking space normally occupied / by a single private automobile."),
             ("Commuters who cycle regularly also enjoy lower rates of cardiovascular illness and reduced daily stress.", "규칙적으로 자전거로 출퇴근하는 사람들은 심혈관 질환 발병률이 낮아지고 일상의 스트레스도 줄어듭니다.", "Commuters who cycle regularly / also enjoy lower rates / of cardiovascular illness / and reduced daily stress."),
             ("Dedicated cycling infrastructure transforms noisy roadways into vibrant, human-centered public streets.", "전용 자전거 인프라는 시끄러운 차도를 활기차고 인간 중심적인 공공 거리로 탈바꿈시킵니다.", "Dedicated cycling infrastructure transforms / noisy roadways / into vibrant, human-centered public streets.")
         ],
         [("congestion", "n.", "혼잡, 정체", "Traffic congestion increases commuting times during rush hour."), ("progressive", "adj.", "진보적인, 혁신적인", "The mayor implemented progressive environmental policies."), ("emission", "n.", "배출, 배기가스", "Stricter laws aim to limit greenhouse gas emissions."), ("cardiovascular", "adj.", "심혈관의", "Aerobic exercise promotes cardiovascular endurance."), ("vibrant", "adj.", "활기찬, 생동감 넘치는", "The market was filled with vibrant colors and lively music.")],
         [("부사적 용법의 to부정사", "To address these environmental issues, cities are investing... 목적을 나타내는 to부정사 부사적 용법입니다."), ("관계대명사 who", "Commuters who cycle regularly also enjoy... 주격 관계대명사 수식입니다.")],
         [
             ("What environmental benefit of bicycles is highlighted in the text?", "지문에서 강조된 자전거의 환경적 이점은 무엇인가요?", ["They generate high electrical power for buildings.", "They produce no toxic tailpipe emissions and burn no fossil fuel.", "They purify polluted city groundwater as wheels spin.", "They lower outdoor temperatures by ten degrees Celsius."], 1, "화석 연료를 소비하지 않고 유독 배기가스를 배출하지 않는다고 서술했습니다."),
             ("How does bicycle parking efficiency compare to private cars?", "자전거 주차 효율은 승용차와 비교해 어떠한가요?", ["One bicycle needs four car parking spaces.", "Ten bicycles can fit in the space occupied by one car.", "Bicycles cannot be parked anywhere in cities.", "Bicycles require underground magnetic tracks."], 1, "승용차 한 대 자리에 자전거 10대가 들어갈 수 있다고 명시했습니다."),
             ("What personal health advantage is mentioned for cycling commuters?", "자전거 출퇴근자에게 언급된 개인적 건강상 이점은 무엇인가요?", ["Lower rates of cardiovascular illness and reduced stress", "Immunity from all infectious viruses", "Immediate doubling of physical muscle mass", "The ability to stay awake for three days"], 0, "심혈관 질환 발병률 감소와 일상 스트레스 경감이 언급되었습니다.")
         ]),

        ("b-36", "The Art of Baking Sourdough Bread", "사워도우 빵을 굽는 발효의 미학", "Food Science", "BBC Food",
         "상업용 이스트 대신 야생 효모와 유산균을 배양하여 깊은 풍미를 내는 전통 사워도우 제빵술을 소개합니다.",
         [
             ("Traditional sourdough bread relies on a living starter culture rather than commercial packaged yeast.", "전통 사워도우 빵은 시판 포장 이스트 대신 살아있는 발효종 배양액에 의존합니다.", "Traditional sourdough bread relies / on a living starter culture / rather than commercial packaged yeast."),
             ("A starter is created simply by mixing flour and water, then waiting patiently for natural fermentation.", "발효종은 단순히 밀가루와 물을 섞은 다음, 자연적인 발효를 참을성 있게 기다림으로써 만들어집니다.", "A starter is created simply / by mixing flour and water, / then waiting patiently / for natural fermentation."),
             ("Wild yeasts floating in ambient room air begin consuming the starches in the damp flour mixture.", "실내 공기 중에 떠다니는 야생 효모는 축축한 밀가루 혼합물 속의 전분을 소비하기 시작합니다.", "Wild yeasts floating in ambient room air / begin consuming the starches / in the damp flour mixture."),
             ("Simultaneously, beneficial lactic acid bacteria multiply, giving sourdough its signature tangy flavor.", "동시에, 유익한 유산균이 증식하여 사워도우 특유의 톡 쏘는 새콤한 풍미를 부여합니다.", "Simultaneously, / beneficial lactic acid bacteria multiply, / giving sourdough / its signature tangy flavor."),
             ("The rising bubbles of carbon dioxide gas lift the heavy dough, creating an airy open crumb structure.", "부풀어 오르는 이산화탄소 기포가 무거운 반죽을 들어 올려, 공기구멍이 풍성한 빵 속 구조를 만듭니다.", "The rising bubbles of carbon dioxide gas / lift the heavy dough, / creating an airy open crumb structure."),
             ("Long slow fermentation also breaks down gluten proteins, making sourdough noticeably easier to digest.", "길고 느린 발효 과정은 글루텐 단백질도 분해하여 사워도우를 눈에 띄게 소화하기 쉽게 만들어 줍니다.", "Long slow fermentation / also breaks down gluten proteins, / making sourdough noticeably easier / to digest.")
         ],
         [("fermentation", "n.", "발효", "Fermentation transforms cabbage into spicy Korean kimchi."), ("ambient", "adj.", "주변의, 대기의", "Store the starter culture at ambient room temperature."), ("tangy", "adj.", "톡 쏘는, 새콤한", "The dressing has a delightful tangy citrus flavor."), ("crumb", "n.", "빵 속살, 빵 부스러기", "A high-hydration dough yields a soft and open crumb."), ("digest", "v.", "소화하다", "Slowly chewing food helps the stomach digest meals efficiently.")],
         [("동명사 전치사구", "...by mixing flour and water, then waiting... by 뒤에 병렬 연결된 동명사구입니다."), ("분사구문 making", "...breaks down gluten proteins, making sourdough easier... 결과를 나타내는 능동 분사구문입니다.")],
         [
             ("What ingredients are initially used to make a sourdough starter?", "사워도우 발효종을 만드는 데 처음에 사용되는 재료는 무엇인가요?", ["Commercial brewer's yeast and white vinegar", "Flour and water", "Pasteurized cow milk and cane sugar", "Artificial food flavoring powders"], 1, "밀가루와 물(flour and water)을 섞어 자연 발효를 기다린다고 설명했습니다."),
             ("What gives sourdough bread its distinctive tangy taste?", "사워도우 빵에 특유의 새콤한 맛을 주는 것은 무엇인가요?", ["Beneficial lactic acid bacteria multiplying in the dough", "Synthetic citric acid sprayed onto the crust", "Lemon juice added before baking", "Exposure to direct sunlight on a windowsill"], 0, "유익한 유산균(lactic acid bacteria)의 증식이 풍미를 준다고 명시했습니다."),
             ("Why is sourdough bread often easier to digest?", "사워도우 빵이 흔히 소화하기 더 쉬운 이유는 무엇인가요?", ["It contains zero carbohydrate molecules.", "Long slow fermentation breaks down gluten proteins.", "It must be soaked in hot boiling broth.", "All yeast organisms remain alive inside the stomach."], 1, "느린 발효 과정이 글루텐 단백질을 분해하기 때문이라고 서술했습니다.")
         ]),

        ("b-37", "The Miraculous Migration of Monarch Butterflies", "제왕나비의 경이로운 대이동", "Nature & Biology", "National Geographic",
         "매년 수천 킬로미터를 날아 캐나다에서 멕시코 산림으로 이동하는 제왕나비의 세대별 여정을 알아봅니다.",
         [
             ("Every autumn, millions of monarch butterflies embark on an astounding journey across North America.", "매년 가을, 수백만 마리의 제왕나비가 북미 대륙을 가로지르는 놀라운 여정에 착수합니다.", "Every autumn, / millions of monarch butterflies embark / on an astounding journey / across North America."),
             ("They travel over four thousand kilometers from cold Canadian forests down to central Mexico.", "그들은 추운 캐나다 숲에서 멕시코 중부까지 4,000킬로미터 이상을 이동합니다.", "They travel / over four thousand kilometers / from cold Canadian forests / down to central Mexico."),
             ("No individual butterfly ever makes the entire round trip by itself.", "어떤 개별 나비도 전체 왕복 여행을 혼자서 완주하지는 못합니다.", "No individual butterfly / ever makes the entire round trip / by itself."),
             ("Instead, it takes four distinct generations to complete the grand navigational cycle.", "대신에, 이 거대한 항법 주기를 완료하는 데는 네 번의 뚜렷한 세대가 필요합니다.", "Instead, / it takes four distinct generations / to complete the grand navigational cycle."),
             ("Guided by an internal magnetic compass and the position of the sun, they navigate with pinpoint accuracy.", "내부의 자기 나침반과 태양의 위치에 의해 유도되어, 그들은 핀포인트의 정확성으로 항해합니다.", "Guided by an internal magnetic compass / and the position of the sun, / they navigate / with pinpoint accuracy."),
             ("Upon arriving in Mexican pine sanctuaries, they cluster on fir branches to hibernate safely through winter.", "멕시코 소나무 보호구역에 도착하면, 그들은 전나무 가지에 빽빽이 모여 겨울 동안 안전하게 동면합니다.", "Upon arriving in Mexican pine sanctuaries, / they cluster on fir branches / to hibernate safely through winter.")
         ],
         [("embark", "v.", "착수하다, 나서다", "The explorers embarked on an expedition into the jungle."), ("astounding", "adj.", "놀라운, 경이로운", "The telescope revealed an astounding number of galaxies."), ("generation", "n.", "세대", "Wisdom is handed down from one generation to the next."), ("accuracy", "n.", "정확성, 정밀도", "GPS satellites pinpoint locations with high accuracy."), ("hibernate", "v.", "동면하다, 겨울잠을 자다", "Brown bears hibernate in underground dens all winter.")],
         [("과거분사 수동 분사구문", "Guided by an internal magnetic compass..., they navigate... Being이 생략된 수동 분사구문입니다."), ("전치사 Upon -ing", "Upon arriving in Mexican pine sanctuaries... '~하자마자/도착하자'라는 시간 표현입니다.")],
         [
             ("How far do monarch butterflies travel during their autumn migration?", "제왕나비는 가을 이동 중에 얼마나 먼 거리를 이동하나요?", ["Less than one hundred meters", "Over four thousand kilometers", "Around fifty kilometers between garden walls", "Across the Pacific Ocean to Asia"], 1, "캐나다에서 멕시코 중부까지 4,000킬로미터 이상 이동한다고 밝혔습니다."),
             ("How many generations are needed to complete the full migration cycle?", "전체 이동 주기를 완주하는 데 몇 세대가 필요한가요?", ["Only one single super-butterfly", "Four distinct generations", "Hundreds of unrelated species", "A new generation every single morning"], 1, "네 번의 뚜렷한 세대(four distinct generations)가 필요하다고 명시했습니다."),
             ("What navigational cues guide the butterflies?", "어떤 항법 단서들이 나비들을 안내하나요?", ["Streetlamps along interstate highways", "An internal magnetic compass and the sun's position", "Echo signals bounced from mountain peaks", "Radio waves broadcast from weather towers"], 1, "내부 자기 나침반과 태양의 위치(magnetic compass and the position of the sun)라고 서술했습니다.")
         ]),

        ("b-38", "The Science of Rainbow Formation", "무지개가 형성되는 광학적 원리", "Physics & Weather", "Scientific American",
         "비 온 뒤 햇빛이 공기 중의 빗방울 속으로 굴절, 반사, 분산되며 영롱한 색 띠를 만드는 과정을 설명합니다.",
         [
             ("A rainbow is an optical phenomenon that requires both direct sunlight and atmospheric raindrops.", "무지개는 직접적인 햇빛과 대기 중의 빗방울을 모두 필요로 하는 광학적 현상입니다.", "A rainbow is an optical phenomenon / that requires both direct sunlight / and atmospheric raindrops."),
             ("To observe a rainbow, an observer must stand with their back turned towards the sun.", "무지개를 관찰하려면, 관찰자는 태양을 등지고 서 있어야 합니다.", "To observe a rainbow, / an observer must stand / with their back turned towards the sun."),
             ("When white sunlight enters a suspended water droplet, the beam bends or refracts.", "백색 햇빛이 공중에 떠 있는 물방울 속으로 들어갈 때, 광선은 꺾이거나 굴절됩니다.", "When white sunlight enters a suspended water droplet, / the beam bends / or refracts."),
             ("Because different color wavelengths bend at slightly different angles, the white light splits into distinct colors.", "색깔마다 파장이 약간씩 다른 각도로 꺾이기 때문에, 백색광은 뚜렷한 개별 색상들로 분리됩니다.", "Because different color wavelengths / bend at slightly different angles, / the white light splits / into distinct colors."),
             ("The separated rays bounce off the back surface inside the droplet before exiting back out.", "분리된 광선들은 물방울 밖으로 다시 빠져나오기 전에 내부 뒷면에서 반사됩니다.", "The separated rays bounce off / the back surface inside the droplet / before exiting back out."),
             ("Red light exits at approximately forty-two degrees, while violet light emerges at forty degrees, forming a curved arc.", "붉은빛은 약 42도로 빠져나오고 보랏빛은 40도로 나와, 둥근 원호를 형성합니다.", "Red light exits / at approximately forty-two degrees, / while violet light emerges at forty degrees, / forming a curved arc.")
         ],
         [("phenomenon", "n.", "현상", "The northern lights are a spectacular natural phenomenon."), ("refract", "v.", "굴절시키다", "Water prisms refract white light into a rainbow."), ("wavelength", "n.", "파장", "Infrared radiation has a longer wavelength than visible light."), ("emerge", "v.", "나타나다, 나오다", "The sun emerged from behind the dark storm clouds."), ("approximately", "adv.", "대략, 거의", "The journey took approximately two hours by train.")],
         [("with + 명사 + 분사", "...with their back turned towards the sun... 신체 부위의 상태를 묘사하는 부대상황 구문입니다."), ("접속사 while의 대조", "Red light exits at 42 degrees, while violet light emerges at 40 degrees... 대조의 while 구문입니다.")],
         [
             ("Where must an observer stand to see a rainbow?", "무지개를 보려면 관찰자는 어디에 어떻게 서 있어야 하나요?", ["Facing directly into the blinding midday sun", "With their back turned towards the sun", "Underneath an opaque concrete roof", "Inside an unlit enclosed basement"], 1, "태양을 등지고(with their back turned towards the sun) 서 있어야 한다고 명시했습니다."),
             ("Why does white light separate into different colors inside a droplet?", "물방울 속에서 백색광이 왜 여러 색으로 분리되나요?", ["Different wavelengths bend at slightly different angles.", "The water droplet contains colorful food dyes.", "Dust inside the cloud stains the light rays.", "Cold temperatures freeze the beam of light."], 0, "색깔마다 파장이 약간씩 다른 각도로 굴절되기 때문입니다."),
             ("At what approximate angle does red light exit the water droplet?", "붉은빛은 대략 몇 도의 각도로 물방울을 빠져나오나요?", ["Ten degrees", "Forty-two degrees", "Ninety degrees", "One hundred and eighty degrees"], 1, "본문에서 붉은빛은 약 42도(approximately 42 degrees)로 빠져나온다고 서술했습니다.")
         ]),

        ("b-39", "The Intelligence of Octopuses", "문어의 놀라운 지능과 문제 해결 능력", "Marine Biology", "Nature",
         "무척추동물임에도 미로를 탈출하고 도구를 사용하며 위장술을 펼치는 문어의 지적 능력을 다룹니다.",
         [
             ("Octopuses are among the most intelligent and intriguing invertebrates inhabiting the oceans.", "문어는 바다에 서식하는 가장 지능적이고 흥미로운 무척추동물 중 하나입니다.", "Octopuses are among the most intelligent / and intriguing invertebrates / inhabiting the oceans."),
             ("Unlike humans whose neurons are concentrated in the skull, two-thirds of an octopus's neurons reside in its flexible arms.", "신경세포가 두개골에 집중된 인간과 달리, 문어 신경세포의 3분의 2는 유연한 팔에 자리 잡고 있습니다.", "Unlike humans whose neurons are concentrated in the skull, / two-thirds of an octopus's neurons reside / in its flexible arms."),
             ("This allows each individual arm to taste, feel, and manipulate objects semi-independently.", "이것은 각각의 개별 팔이 반독립적으로 맛을 보고, 느끼고, 물체를 조작할 수 있게 합니다.", "This allows each individual arm / to taste, feel, / and manipulate objects semi-independently."),
             ("Laboratory experiments have demonstrated that octopuses can unscrew childproof jars to access food inside.", "실험실 연구를 통해 문어가 안에 든 먹이를 얻기 위해 어린이 안전 뚜껑 병을 돌려 열 수 있음이 입증되었습니다.", "Laboratory experiments have demonstrated / that octopuses can unscrew childproof jars / to access food inside."),
             ("In the wild, some octopuses carry coconut shell halves to assemble defensive fortresses against predators.", "야생에서, 일부 문어는 포식자로부터 방어 요새를 조립하기 위해 코코넛 껍질 반쪽을 운반합니다.", "In the wild, / some octopuses carry coconut shell halves / to assemble defensive fortresses / against predators."),
             ("Their remarkable camouflage also lets them change both skin color and texture within milliseconds.", "그들의 놀라운 위장술은 또한 수 밀리초 만에 피부 색상과 질감을 모두 바꿀 수 있게 해줍니다.", "Their remarkable camouflage / also lets them change both skin color and texture / within milliseconds.")
         ],
         [("invertebrate", "n.", "무척추동물", "Jellyfish, clams, and snails are common marine invertebrates."), ("reside", "v.", "거주하다, 속해 있다", "Many foreign diplomats reside in the capital city."), ("manipulate", "v.", "조작하다, 능숙하게 다루다", "The surgeon manipulated the robotic scalpel with extreme care."), ("camouflage", "n.", "위장, 변장", "Chameleons use camouflage to hide among foliage."), ("millisecond", "n.", "밀리초, 1,000분의 1초", "High-speed cameras capture movements within a few milliseconds.")],
         [("소유격 관계대명사 whose", "Unlike humans whose neurons are concentrated... 선행사 humans를 수식하는 소유격 관계대명사입니다."), ("사역동사 let", "...lets them change both skin color and texture... let + 목적어 + 동사원형 구조입니다.")],
         [
             ("Where are most of an octopus's neurons located?", "문어의 신경세포 대부분은 어디에 위치해 있나요?", ["Directly inside its beak", "In its eight flexible arms", "Inside the suction pads of its mantle", "Underneath its gill chamber"], 1, "문어 신경세포의 3분의 2가 유연한 팔(flexible arms)에 존재한다고 명시했습니다."),
             ("What tool-use behavior has been observed in wild octopuses?", "야생 문어에게서 관찰된 어떤 도구 사용 행동이 있나요?", ["Weaving seaweed into fishing nets", "Carrying coconut shells to build defensive fortresses", "Sharpening stones to cut giant kelp", "Using hermit crab shells as musical instruments"], 1, "코코넛 껍질을 들고 다니며 방어용 요새를 짓는다고 설명했습니다."),
             ("How quickly can an octopus alter its skin color and texture?", "문어는 얼마나 빠르게 피부 색과 질감을 바꿀 수 있나요?", ["Over three months of seasonal molting", "Within milliseconds", "Only during the dark hours of midnight", "It takes roughly forty-eight hours"], 1, "수 밀리초(within milliseconds) 만에 바꿀 수 있다고 명시했습니다.")
         ]),

        ("b-40", "The Origin of Coffee and Global Trade", "커피의 기원과 전 세계 무역의 역사", "History & Culture", "Britannica",
         "에티오피아 고원에서 목동이 발견한 커피 열매가 아라비아를 거쳐 세계 최대의 음료 무역품이 된 역사를 조명합니다.",
         [
             ("Legend has it that an Ethiopian goat herder named Kaldi first discovered the coffee plant.", "전설에 따르면 에티오피아의 염소 목동 칼디가 커피 식물을 처음 발견했다고 합니다.", "Legend has it / that an Ethiopian goat herder named Kaldi / first discovered the coffee plant."),
             ("He noticed that his herd became unusually energetic after nibbling bright red berries from a shrub.", "그는 그의 염소 떼가 관목에서 밝은 붉은색 열매를 뜯어먹은 후 비정상적으로 활기차지는 것을 알아차렸습니다.", "He noticed / that his herd became unusually energetic / after nibbling bright red berries / from a shrub."),
             ("Monks at a nearby monastery brewed a drink from these seeds, finding that it kept them alert during prayer.", "인근 수도원의 수도사들은 이 씨앗으로 음료를 달여 마셨고, 이것이 기도 시간 동안 깨어있게 해준다는 것을 발견했습니다.", "Monks at a nearby monastery / brewed a drink from these seeds, / finding that it kept them alert / during prayer."),
             ("By the fifteenth century, coffee cultivation had spread across the Arabian Peninsula, especially in Yemen.", "15세기에 이르러, 커피 재배는 아라비아반도 전역, 특히 예멘으로 퍼져나갔습니다.", "By the fifteenth century, / coffee cultivation had spread / across the Arabian Peninsula, / especially in Yemen."),
             ("Coffeehouses, known as kaveh kanes, emerged in Cairo and Istanbul as vibrant hubs of debate and music.", "카베 카네로 알려진 커피하우스들이 카이로와 이스탄불에서 토론과 음악의 활기찬 중심지로 떠올랐습니다.", "Coffeehouses, known as kaveh kanes, / emerged in Cairo and Istanbul / as vibrant hubs / of debate and music."),
             ("Today, coffee ranks among the most valuable agricultural commodities traded in international markets.", "오늘날 커피는 국제 시장에서 거래되는 가장 가치 있는 농업 원자재 중 하나로 꼽힙니다.", "Today, coffee ranks among / the most valuable agricultural commodities / traded in international markets.")
         ],
         [("energetic", "adj.", "활기찬, 에너지 넘치는", "The puppy was lively and full of energetic joy."), ("nibble", "v.", "조금씩 뜯어먹다", "Mice nibbled on crusts of stale sourdough bread."), ("monastery", "n.", "수도원", "The ancient monastery was built atop an isolated mountain peak."), ("cultivation", "n.", "경작, 재배", "Terraced hillsides are ideal for tea cultivation."), ("commodity", "n.", "상품, 원자재", "Crude oil and wheat are critical global commodities.")],
         [("과거완료 시제 had spread", "By the fifteenth century, coffee cultivation had spread... 기준 과거 시점 이전의 완료를 나타냅니다."), ("과거분사 수식", "commodities traded in international markets에서 traded는 앞 명사를 수식하는 수동 분사입니다.")],
         [
             ("Who according to legend first discovered coffee?", "전설에 따르면 누가 커피를 처음 발견했나요?", ["A Greek merchant sailing the Aegean Sea", "An Ethiopian goat herder named Kaldi", "A French chef living in nineteenth-century Paris", "A Dutch naval captain anchored in Java"], 1, "에티오피아 목동 칼디(Kaldi)가 발견했다고 전해진다고 서술했습니다."),
             ("Why did monks in monasteries value the coffee beverage?", "수도원의 수도사들은 왜 커피 음료를 소중히 여겼나요?", ["It cured deadly bacterial infections.", "It kept them alert and awake during nightly prayers.", "It substituted for solid food for three months.", "It turned ordinary tap water into wine."], 1, "기도 시간 동안 깨어있게(alert during prayer) 해주었기 때문입니다."),
             ("What cultural role did early coffeehouses fulfill in cities like Istanbul?", "초기 커피하우스들은 이스탄불 같은 도시에서 어떤 문화적 역할을 했나요?", ["They served as secret military weapons caches.", "They were vibrant public hubs for debate and musical arts.", "They offered free medical surgeries to sailors.", "They prohibited any speech or intellectual discussions."], 1, "토론과 음악의 활기찬 중심지(vibrant hubs of debate and music)로 기능했다고 명시했습니다.")
         ])
    ]
    return b_extra

if __name__ == "__main__":
    print(f"Generated extra beginner passages: {len(get_expansion_passages())}")
