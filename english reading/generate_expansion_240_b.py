# -*- coding: utf-8 -*-
"""
generate_expansion_240_b.py
10 Beginner passages (b-71 to b-80)
A2-B1 level, authoritative sources, sentence chunks, vocabulary, grammar, and 3 deducible comprehension questions per passage.
"""

def get_expansion_240_b():
    return [
        (
            "b-71",
            "The Anatomy of Human Teeth",
            "인간 치아의 구조와 저작 기능",
            "Anatomy & Health",
            "American Dental Association (ADA) Educational Resource",
            "치아는 신체에서 가장 단단한 법랑질로 둘러싸여 있으며, 음식물을 분쇄하고 소화를 돕는 핵심 기관입니다.",
            [
                ("Human teeth are vital anatomical structures / designed for cutting, tearing, and grinding food.",
                 "인간의 치아는 음식물을 자르고 찢으며 으깨도록 설계된 / 매우 중요한 해부학적 구조입니다.",
                 "Human teeth are vital anatomical structures / designed for cutting, / tearing, and grinding food."),
                ("The outermost visible white layer / is called enamel, / which is the hardest substance in the human body.",
                 "눈에 보이는 가장 바깥쪽의 하얀 층은 / 법랑질이라 불리며, / 인간의 몸에서 가장 단단한 물질입니다.",
                 "The outermost visible white layer / is called enamel, / which is the hardest substance / in the human body."),
                ("Beneath this tough protective armor lies dentin, / a softer yellowish tissue surrounding the sensitive pulp.",
                 "이 단단한 보호 갑옷 아래에는 / 민감한 치수를 둘러싸고 있는 더 부드러운 노르스름한 조직인 / 상아질이 자리 잡고 있습니다.",
                 "Beneath this tough protective armor / lies dentin, / a softer yellowish tissue / surrounding the sensitive pulp."),
                ("The central pulp contains living blood vessels and nerves / that keep the tooth healthy and nourish its growth.",
                 "중앙의 치수는 살아있는 혈관과 신경을 포함하고 있어 / 치아의 건강을 유지하고 성장을 돕습니다.",
                 "The central pulp contains / living blood vessels and nerves / that keep the tooth healthy / and nourish its growth.")
            ],
            [
                ("vital", "adj.", "매우 중요한, 생명의", "Regular physical activity is vital for cardiovascular health."),
                ("enamel", "n.", "법랑질, 에나멜", "Enamel protects teeth from wear and acidic food damage."),
                ("dentin", "n.", "상아질 (치아 내부 층)", "Dentin contains microscopic tubules leading to nerve endings."),
                ("nourish", "v.", "영양분을 공급하다, 육성하다", "Nutrient-rich soil nourishes young seedling roots.")
            ],
            [
                ("designed for -ing", "'~하도록 고안된/설계된' 목적을 나타내는 과거분사 표현입니다."),
                ("Beneath ~ lies dentin", "장소 부사구 도치 구문으로 '단단한 갑옷 아래에 상아질이 놓여 있다'는 구조입니다.")
            ],
            [
                ("What is the hardest substance in the human body according to the text?",
                 "본문에 따르면 인간의 몸에서 가장 단단한 물질은 무엇인가?",
                 ["Soft yellow dentin", "Tooth enamel", "Living nerve tissue", "Skeletal finger bones"],
                 1,
                 "두 번째 문장에 'enamel, which is the hardest substance in the human body'라고 명시되어 있습니다."),
                ("Where is dentin located in relation to enamel?",
                 "상아질은 법랑질과 비교하여 어디에 위치하는가?",
                 ["Directly outside the mouth", "Beneath the protective enamel armor", "At the very tip of the fingernails", "Inside the stomach lining"],
                 1,
                 "세 번째 문장에 'Beneath this tough protective armor lies dentin'이라고 나와 있습니다."),
                ("What does the central pulp contain?",
                 "중앙의 치수는 무엇을 포함하고 있는가?",
                 ["Living blood vessels and nerves", "Solid calcium stones only", "Metallic iron filings", "Acidic digestive saliva"],
                 0,
                 "마지막 문장에 살아있는 혈관과 신경(blood vessels and nerves)을 포함한다고 설명합니다.")
            ]
        ),
        (
            "b-72",
            "How Airplanes Generate Aerodynamic Lift",
            "비행기 날개가 양력을 생성하는 원리",
            "Aviation Science",
            "NASA Glenn Research Center Aeronautics Guide",
            "비행기 날개(에어포일)의 독특한 곡면 형상은 날개 위아래의 기압 차이를 발생시켜 비행기를 공중으로 띄웁니다.",
            [
                ("Airplanes achieve flight / by creating an upward aerodynamic force / known as lift.",
                 "비행기는 양력이라 알려진 / 위로 향하는 공기역학적 힘을 생성함으로써 / 비행을 달성합니다.",
                 "Airplanes achieve flight / by creating an upward aerodynamic force / known as lift."),
                ("An airplane wing is specially curved / in a tear-drop cross section called an airfoil.",
                 "비행기 날개는 에어포일이라 불리는 / 눈물방울 모양의 단면으로 특별하게 곡면화되어 있습니다.",
                 "An airplane wing is specially curved / in a tear-drop cross section / called an airfoil."),
                ("As the aircraft speeds forward, / air flows faster over the curved upper surface / than underneath the flat wing bottom.",
                 "비행기가 전방으로 가속함에 따라, / 공기는 평평한 날개 밑면보다 / 굴곡진 상부 표면 위로 더 빠르게 흐릅니다.",
                 "As the aircraft speeds forward, / air flows faster / over the curved upper surface / than underneath the flat wing bottom."),
                ("This speed variation creates lower pressure above the wing, / causing the higher pressure below to push the plane into the sky.",
                 "이러한 속도 차이는 날개 위에 더 낮은 압력을 발생시키며, / 아래쪽의 더 높은 압력이 비행기를 하늘 위로 밀어 올리게 만듭니다.",
                 "This speed variation creates lower pressure / above the wing, / causing the higher pressure below / to push the plane into the sky.")
            ],
            [
                ("aerodynamic", "adj.", "공기역학의", "Sleek racing cars feature aerodynamic bodies to minimize drag."),
                ("airfoil", "n.", "에어포일 (날개 단면 형상)", "The curvature of an airfoil determines its lifting efficiency."),
                ("variation", "n.", "변화, 차이", "Temperature variation between day and night is extreme in deserts."),
                ("underneath", "prep./adv.", "~의 아래에", "The cat slept quietly underneath the wooden dining table.")
            ],
            [
                ("by creating ~", "'~을 생성함으로써' 수단을 나타내는 전치사구입니다."),
                ("causing A to B", "'A가 B하도록 야기하다' 인과 관계를 나타내는 구문입니다.")
            ],
            [
                ("What is the upward aerodynamic force that allows flight called?",
                 "비행을 가능하게 하는 위쪽 방향의 공기역학적 힘을 무엇이라 부르는가?",
                 ["Gravity", "Lift", "Friction", "Turbulence"],
                 1,
                 "첫 문장에 'upward aerodynamic force known as lift'라고 명시되어 있습니다."),
                ("How does air flow over the wing when the plane moves forward?",
                 "비행기가 전방으로 나아갈 때 공기는 날개 위를 어떻게 흐르는가?",
                 ["Faster over the curved upper surface than underneath", "Much slower over the top than the bottom", "It completely stops moving around the wings", "It reverses direction and flows backward through engines"],
                 0,
                 "세 번째 문장에 공기가 아래쪽보다 굴곡진 위쪽 표면에서 더 빠르게 흐른다고 설명합니다."),
                ("What causes the plane to be pushed up into the sky?",
                 "무엇이 비행기를 하늘로 밀어 올리도록 만드는가?",
                 ["Lower air pressure above the wing and higher pressure below", "Heavy lead weights attached to the airplane tail", "Strong magnetic pull from outer space", "High vacuum inside the passenger cabin"],
                 0,
                 "마지막 문장에 날개 위의 낮은 압력과 아래의 높은 압력이 비행기를 밀어 올린다고 설명합니다.")
            ]
        ),
        (
            "b-73",
            "The Metamorphosis of Frogs",
            "개구리의 변태와 생활사",
            "Herpetology",
            "Amphibian Ark Biological Resource Guide",
            "개구리는 수중에서 아가미로 숨쉬는 올챙이로 부화한 뒤, 폐와 다리가 발달하는 극적인 변태를 거쳐 육지 성체로 성장합니다.",
            [
                ("Frogs undergo a remarkable developmental transformation / known as complete metamorphosis.",
                 "개구리는 완전 변태로 알려진 / 놀라운 발생학적 변화를 거칩니다.",
                 "Frogs undergo / a remarkable developmental transformation / known as complete metamorphosis."),
                ("A female frog deposits soft gelatinous eggs in ponds, / where aquatic larvae called tadpoles hatch.",
                 "암컷 개구리는 연못에 부드러운 젤리 모양의 알을 낳으며, / 그곳에서 올챙이라 불리는 수중 유생이 부화합니다.",
                 "A female frog deposits soft gelatinous eggs / in ponds, / where aquatic larvae called tadpoles hatch."),
                ("At first, / tadpoles swim using a finned tail / and breathe dissolved underwater oxygen through delicate external gills.",
                 "처음에, / 올챙이는 지느러미가 달린 꼬리로 헤엄치며 / 섬세한 외아가미를 통해 물속에 용해된 산소로 숨을 쉽니다.",
                 "At first, / tadpoles swim using a finned tail / and breathe dissolved underwater oxygen / through delicate external gills."),
                ("Over several weeks, / the tadpole absorbs its tail, / grows strong hind legs, / and develops air-breathing lungs to live on land.",
                 "수주에 걸쳐, / 올챙이는 꼬리를 흡수하고, / 강한 뒷다리를 키우며, / 육지에서 살기 위해 공기로 숨쉬는 폐를 발달시킵니다.",
                 "Over several weeks, / the tadpole absorbs its tail, / grows strong hind legs, / and develops air-breathing lungs / to live on land.")
            ],
            [
                ("metamorphosis", "n.", "변태, 탈바꿈", "Caterpillars undergo metamorphosis inside chrysalises to become butterflies."),
                ("gelatinous", "adj.", "젤리 같은, 아교질의", "Jellyfish possess soft gelatinous bells that float in water."),
                ("delicate", "adj.", "섬세한, 연약한", "The antique glass ornament was too delicate to handle roughly."),
                ("absorb", "v.", "흡수하다", "Dry sponges absorb spilled liquids quickly.")
            ],
            [
                ("where aquatic larvae hatch", "장소를 나타내는 선행사 ponds를 부연하는 관계부사 where 절입니다."),
                ("breathe dissolved oxygen", "과거분사 dissolved가 명사 oxygen을 앞에서 수식합니다.")
            ],
            [
                ("How do young tadpoles breathe when they first hatch?",
                 "어린 올챙이는 처음 부화했을 때 어떻게 숨을 쉬는가?",
                 ["Through air-breathing lungs", "Through delicate external gills", "Using specialized skin feathers", "By popping bubbles on the surface"],
                 1,
                 "세 번째 문장에 'breathe dissolved underwater oxygen through delicate external gills'라고 명시되어 있습니다."),
                ("Where does a female frog deposit her eggs?",
                 "암컷 개구리는 알을 어디에 낳는가?",
                 ["High in dry desert trees", "Inside soft gelatinous masses in ponds", "Underneath burning volcanic rock", "Deep inside dry sand dunes"],
                 1,
                 "두 번째 문장에 연못(ponds)에 알을 낳는다고 나와 있습니다."),
                ("What bodily changes occur as a tadpole transitions to land?",
                 "올챙이가 육지로 전환되면서 어떤 신체 변화가 일어나는가?",
                 ["It loses all limbs and develops shark fins.", "It absorbs its tail, grows hind legs, and develops lungs.", "It turns into a winged insect with antennae.", "Its bones turn entirely into soft water."],
                 1,
                 "마지막 문장에 꼬리를 흡수하고, 뒷다리가 자라며, 폐를 발달시킨다고 설명합니다.")
            ]
        ),
        (
            "b-74",
            "How Thermometers Measure Temperature",
            "온도계가 온도를 측정하는 물리적 원리",
            "Physical Science",
            "National Institute of Standards and Technology (NIST) Educational Series",
            "온도계는 온도가 상승할 때 액체나 금속의 부피가 팽창하거나 전기 저항이 변화하는 물리 법칙을 이용하여 온도를 측정합니다.",
            [
                ("A thermometer is a scientific instrument / designed to measure thermal temperature precisely.",
                 "온도계는 열 온도를 정밀하게 측정하도록 설계된 / 과학 측정 도구입니다.",
                 "A thermometer is a scientific instrument / designed to measure thermal temperature precisely."),
                ("Traditional liquid thermometers rely on thermal expansion, / which is the physical tendency of matter to change volume as heat increases.",
                 "전통적인 액체 온도계는 열팽창에 의존하는데, / 이는 열이 증가함에 따라 물질의 부피가 변하는 물리적 경향입니다.",
                 "Traditional liquid thermometers / rely on thermal expansion, / which is the physical tendency of matter / to change volume as heat increases."),
                ("When heat warms the liquid inside the bulb, / molecules move faster and push outward, / forcing the fluid up a narrow calibrated tube.",
                 "열이 유리구 내부의 액체를 데우면, / 분자들이 더 빠르게 움직이며 바깥으로 밀어내어, / 유체가 눈금이 매겨진 좁은 관 위로 밀려 올라가도록 만듭니다.",
                 "When heat warms the liquid inside the bulb, / molecules move faster and push outward, / forcing the fluid up / a narrow calibrated tube."),
                ("Modern digital thermometers instead use electronic sensors / whose electrical resistance changes in predictable proportion to temperature.",
                 "현대의 디지털 온도계는 대신에 전자 센서를 사용하는데, / 이 센서의 전기 저항은 온도에 예측 가능한 비례로 변합니다.",
                 "Modern digital thermometers instead use electronic sensors / whose electrical resistance changes / in predictable proportion to temperature.")
            ],
            [
                ("expansion", "n.", "팽창, 확장", "Thermal expansion causes bridge metal to expand during summer."),
                ("calibrated", "adj.", "눈금이 매겨진, 교정된", "Scientists use calibrated pipettes to dispense exact chemical volumes."),
                ("resistance", "n.", "저항", "Insulators offer very high electrical resistance against current."),
                ("predictable", "adj.", "예측 가능한", "Tidal cycles follow predictable gravitational patterns.")
            ],
            [
                ("rely on + 명사", "'~에 의존하다'라는 기본 숙어입니다."),
                ("whose electrical resistance changes", "선행사 electronic sensors의 소유격을 나타내는 관계대명사 whose 절입니다.")
            ],
            [
                ("What physical principle do traditional liquid thermometers rely on?",
                 "전통적인 액체 온도계는 어떤 물리적 원리에 의존하는가?",
                 ["Chemical nuclear fission", "Thermal expansion", "Magnetic pole reversal", "Sound acoustic echo"],
                 1,
                 "두 번째 문장에 'rely on thermal expansion'이라고 명시되어 있습니다."),
                ("What happens to liquid molecules inside the thermometer bulb when heated?",
                 "온도계 구 안의 액체 분자들이 가열되면 무슨 일이 일어나는가?",
                 ["They freeze into solid ice cubes.", "They move faster and push outward, forcing fluid up the tube.", "They convert completely into static electricity.", "They vanish into empty vacuum."],
                 1,
                 "세 번째 문장에 분자들이 더 빠르게 움직이며 유체를 좁은 관 위로 밀어 올린다고 설명합니다."),
                ("How do modern digital thermometers detect temperature changes?",
                 "현대 디지털 온도계는 온도 변화를 어떻게 감지하는가?",
                 ["Using electronic sensors whose electrical resistance changes", "By measuring how loudly the thermometer beeps", "By catching sunlight through colored glass lenses", "By counting how many water drops fall per second"],
                 0,
                 "마지막 문장에 전기 저항이 변하는 전자 센서를 사용한다고 나와 있습니다.")
            ]
        ),
        (
            "b-75",
            "The Great Monarch Butterfly Migration",
            "제왕나비의 경이로운 대이동",
            "Ecology",
            "Smithsonian National Museum of Natural History Bulletin",
            "북미의 제왕나비는 매년 가을 혹독한 겨울을 피해 태양 나침반과 지구 자기장을 활용하여 4,000km가 넘는 대이동을 감행합니다.",
            [
                ("Every autumn, / millions of monarch butterflies undertake an epic journey / across North America.",
                 "매년 가을, / 수백만 마리의 제왕나비는 / 북미 대륙을 가로지르는 웅장한 여정을 시작합니다.",
                 "Every autumn, / millions of monarch butterflies / undertake an epic journey / across North America."),
                ("They travel over four thousand kilometers / from southern Canada and the northern United States / to forested mountains in central Mexico.",
                 "그들은 캐나다 남부와 미국 북부에서 / 멕시코 중부의 숲이 우거진 산맥까지 / 4,000킬로미터가 넘는 거리를 이동합니다.",
                 "They travel over four thousand kilometers / from southern Canada and the northern United States / to forested mountains in central Mexico."),
                ("Because individual butterflies have never visited the wintering sites before, / they rely on a genetically inherited solar compass in their eyes.",
                 "개별 나비들은 이전에 월동지를 방문해 본 적이 없기 때문에, / 눈 속에 있는 유전적으로 물려받은 태양 나침반에 의존합니다.",
                 "Because individual butterflies have never visited the wintering sites before, / they rely on a genetically inherited solar compass / in their eyes."),
                ("Tens of thousands cluster together on oyamel fir branches, / blanketed in warmth to survive until the spring thaw.",
                 "수만 마리가 오야멜 전나무 가지 위에 빽빽이 모여, / 봄 해빙기까지 생존하기 위해 따뜻하게 온기를 나눕니다.",
                 "Tens of thousands cluster together / on oyamel fir branches, / blanketed in warmth / to survive until the spring thaw.")
            ],
            [
                ("undertake", "v.", "착수하다, (여정을) 떠나다", "The explorers undertook a daring expedition across the Antarctic tundra."),
                ("inherited", "adj.", "물려받은, 유전적인", "Eye color is an inherited biological trait passed from parents."),
                ("cluster", "v.", "무리 짓다, 빽빽이 모이다", "Students clustered around the bulletin board to view exam results."),
                ("blanketed", "adj.", "뒤덮인, 감싸인", "The village was blanketed in a thick layer of fresh morning snow.")
            ],
            [
                ("from A to B", "'A에서 B까지' 출발지와 목적지를 나타냅니다."),
                ("to survive until ~", "목적을 나타내는 to부정사구로 '~까지 살아남기 위해'로 해석됩니다.")
            ],
            [
                ("How far do monarch butterflies travel during their autumn migration?",
                 "제왕나비는 가을 이동 동안 얼마나 먼 거리를 여행하는가?",
                 ["Under fifty meters", "Over four thousand kilometers", "Exactly five miles", "Around the entire globe twice"],
                 1,
                 "두 번째 문장에 4,000킬로미터가 넘는 거리를 이동한다고 명시되어 있습니다."),
                ("Where do monarch butterflies spend the winter?",
                 "제왕나비는 어디에서 겨울을 보내는가?",
                 ["In underwater ocean caves", "In forested mountains in central Mexico", "In ice tunnels in northern Alaska", "Inside hollow tree roots in London"],
                 1,
                 "두 번째 문장에 멕시코 중부의 산림 산맥(forested mountains in central Mexico)으로 간다고 나와 있습니다."),
                ("How do monarchs find their way to destinations they have never seen?",
                 "제왕나비는 한 번도 본 적 없는 목적지로 어떻게 길을 찾는가?",
                 ["By following human traffic signs along highways", "By relying on a genetically inherited solar compass in their eyes", "By calling adult birds to guide their flight", "By flying only in straight lines toward the moon"],
                 1,
                 "세 번째 문장에 눈에 유전적으로 상속된 태양 나침반(solar compass)에 의존한다고 나와 있습니다.")
            ]
        ),
        (
            "b-76",
            "Ocean Tides and Gravitational Pull",
            "조석 현상과 달의 중력 인력",
            "Oceanography",
            "NOAA National Ocean Service Education",
            "바다의 밀물과 썰물은 지구를 향한 달과 태양의 중력 인력 및 지구 자전에 의해 발생하는 주기적인 해수면 승강 현상입니다.",
            [
                ("Ocean tides are periodic rises and falls in sea level / that occur along coastlines across the globe.",
                 "해양 조석은 전 세계 해안선을 따라 발생하는 / 해수면의 주기적인 상승과 하강 현상입니다.",
                 "Ocean tides are periodic rises and falls in sea level / that occur along coastlines / across the globe."),
                ("Tides are caused primarily by the gravitational attraction / exerted on Earth's oceans by the moon.",
                 "조석은 주로 달이 지구의 대양에 가하는 / 중력 인력에 의해 발생합니다.",
                 "Tides are caused primarily / by the gravitational attraction / exerted on Earth's oceans by the moon."),
                ("Because gravity is stronger on the side of Earth closest to the moon, / ocean water bulges outward toward the lunar body.",
                 "달과 가장 가까운 지구 쪽에서 중력이 더 강하기 때문에, / 바닷물이 달 쪽을 향해 바깥으로 부풀어 오릅니다.",
                 "Because gravity is stronger / on the side of Earth closest to the moon, / ocean water bulges outward / toward the lunar body."),
                ("As the Earth rotates through these oceanic bulges each day, / coastal areas experience two high tides and two low tides roughly every twenty-four hours.",
                 "지구가 매일 이 해수 융기부를 관통하여 자전함에 따라, / 해안 지역은 대략 24시간마다 두 번의 만조와 두 번의 간조를 경험합니다.",
                 "As the Earth rotates through these oceanic bulges each day, / coastal areas experience / two high tides and two low tides / roughly every twenty-four hours.")
            ],
            [
                ("periodic", "adj.", "주기적인, 정기적인", "The comet makes a periodic return to our solar system every 76 years."),
                ("exert", "v.", "가하다, 행사하다", "Pressing the brake pedal exerts hydraulic pressure on wheels."),
                ("bulge", "v.", "부풀어 오르다, 불룩해지다", "The overpacked suitcase began to bulge along its seams."),
                ("rotate", "v.", "자전하다, 회전하다", "The earth rotates on its axis once every twenty-four hours.")
            ],
            [
                ("caused primarily by ~", "'주로 ~에 의해 유발된' 수동태 표현입니다."),
                ("exerted on ~", "과거분사구로 앞의 gravitational attraction을 수식합니다.")
            ],
            [
                ("What primarily causes ocean tides according to the passage?",
                 "본문에 따르면 대양의 조석을 주로 일으키는 것은 무엇인가?",
                 ["Underwater earthquake explosions", "The gravitational attraction exerted by the moon", "Strong seasonal hurricane winds", "Large cargo ships crossing the sea"],
                 1,
                 "두 번째 문장에 달이 지구 대양에 미치는 중력 인력(gravitational attraction) 때문이라고 설명합니다."),
                ("Why does ocean water bulge outward toward the moon?",
                 "왜 바닷물이 달 쪽으로 부풀어 오르는가?",
                 ["Because sea creatures swim toward lunar light", "Because gravity is stronger on the side of Earth closest to the moon", "Because ocean water boils under moonlight", "Because clouds push the ocean surface down"],
                 1,
                 "세 번째 문장에 달과 가장 가까운 쪽에서 중력이 더 강하기 때문이라고 명시되어 있습니다."),
                ("How many high tides and low tides do coastal areas typically experience roughly every 24 hours?",
                 "해안 지역은 대략 24시간마다 일반적으로 몇 번의 만조와 간조를 겪는가?",
                 ["Ten high tides and zero low tides", "Two high tides and two low tides", "Only one tide per entire month", "Fifty rapid tides every hour"],
                 1,
                 "마지막 문장에 'two high tides and two low tides roughly every twenty-four hours'라고 명시되어 있습니다.")
            ]
        ),
        (
            "b-77",
            "The Biology of Earthworms and Soil Health",
            "지렁이의 생물학적 구조와 토양 비옥도",
            "Soil Ecology",
            "USDA Natural Resources Conservation Service Soil Health Guide",
            "지렁이는 눈과 폐가 없지만 피부로 호흡하며, 유기물을 섭취하고 배설하여 토양을 비옥하게 가꾸는 생태계의 파수꾼입니다.",
            [
                ("Earthworms are segmented invertebrates / that play an indispensable role in maintaining healthy soil.",
                 "지렁이는 건강한 토양을 유지하는 데 있어 / 없어서는 안 될 역할을 수행하는 / 환형(분절) 무척추동물입니다.",
                 "Earthworms are segmented invertebrates / that play an indispensable role / in maintaining healthy soil."),
                ("Lacking lungs and eyes, / an earthworm absorbs oxygen directly through its moist, mucus-covered skin.",
                 "폐와 눈이 없기 때문에, / 지렁이는 축축하고 점액으로 덮인 피부를 통해 직접 산소를 흡수합니다.",
                 "Lacking lungs and eyes, / an earthworm absorbs oxygen directly / through its moist, mucus-covered skin."),
                ("As they burrow through the earth, / they consume decaying plant matter and mineral soil particles.",
                 "흙 속을 파고 들어가면서, / 그들은 부패한 식물성 물질과 광물 토양 입자들을 섭취합니다.",
                 "As they burrow through the earth, / they consume decaying plant matter / and mineral soil particles."),
                ("Their nutrient-rich digestive waste / called worm castings / enriches the ground with nitrogen, / creating ideal conditions for plant roots.",
                 "분변토라 불리는 / 그들의 영양가 높은 소화 배설물은 / 토양에 질소를 풍부하게 공급하여, / 식물 뿌리를 위한 이상적인 환경을 조성합니다.",
                 "Their nutrient-rich digestive waste / called worm castings / enriches the ground with nitrogen, / creating ideal conditions for plant roots.")
            ],
            [
                ("invertebrate", "n.", "무척추동물", "Insects, spiders, and octopuses are all invertebrates."),
                ("burrow", "v.", "굴을 파다, 파고들다", "Rabbits burrow underground warrens to evade predators."),
                ("decaying", "adj.", "부패하는, 썩어가는", "Fungi decompose decaying tree trunks on the forest floor."),
                ("castings", "n. (pl.)", "배설물 (지렁이 분변토)", "Worm castings act as a gentle organic fertilizer for flowers.")
            ],
            [
                ("Lacking lungs and eyes, ~", "이유를 나타내는 분사구문으로 '폐와 눈이 결여되어 있기 때문에'로 해석됩니다."),
                (", creating ~", "결과를 나타내는 분사구문으로 '그 결과 이상적인 조건을 만들어낸다'를 뜻합니다.")
            ],
            [
                ("How does an earthworm absorb oxygen?",
                 "지렁이는 산소를 어떻게 흡수하는가?",
                 ["Through microscopic nostrils on its tail", "Directly through its moist, mucus-covered skin", "Using feathered aquatic gills", "By drinking massive amounts of puddle water"],
                 1,
                 "두 번째 문장에 축축하고 점액질로 덮인 피부를 통해 직접 산소를 흡수한다고 나와 있습니다."),
                ("What do earthworms eat as they burrow through the ground?",
                 "지렁이는 땅속을 파고들며 무엇을 먹는가?",
                 ["Decaying plant matter and mineral soil particles", "Fresh living green leaves from treetops", "Small flying insects like mosquitoes", "Dry sand stones and quartz crystals"],
                 0,
                 "세 번째 문장에 부패한 식물 물질과 광물 토양 입자를 섭취한다고 명시되어 있습니다."),
                ("What are worm castings and how do they benefit soil?",
                 "지렁이 분변토란 무엇이며 토양에 어떤 유익을 주는가?",
                 ["Toxic acidic secretions that kill all plants", "Nutrient-rich digestive waste that enriches soil with nitrogen", "Hard plastic shells left behind after winter", "Poisonous fumes that repel farm animals"],
                 1,
                 "마지막 문장에 질소를 풍부하게 공급하는 영양가 높은 배설물(nutrient-rich digestive waste)이라고 설명합니다.")
            ]
        ),
        (
            "b-78",
            "The Invention of the Magnetic Compass",
            "자기 나침반의 발명과 항해사",
            "History of Science",
            "British Museum Scientific Inventions Archive",
            "고대 중국에서 천연 자석(자철석)으로 발명된 나침반은 지표면의 자기장을 감지하여 인류가 미지의 대양을 항해할 수 있도록 이끌었습니다.",
            [
                ("The magnetic compass is one of the greatest navigation inventions / in human maritime history.",
                 "자기 나침반은 인류 해양 역사에서 / 가장 위대한 항해 발명품 중 하나입니다.",
                 "The magnetic compass is one of the greatest navigation inventions / in human maritime history."),
                ("It was first created in ancient China / during the Han Dynasty / using naturally magnetized iron ore known as lodestone.",
                 "나침반은 한나라 시기 고대 중국에서 / 자철석으로 알려진 자연적으로 자화된 철광석을 이용하여 / 처음 제작되었습니다.",
                 "It was first created in ancient China / during the Han Dynasty / using naturally magnetized iron ore known as lodestone."),
                ("A balanced magnetic needle aligns itself / with the Earth's natural magnetic field, / always pointing toward magnetic north.",
                 "균형 잡힌 자석 바늘은 / 지구의 자연 자기장과 일치하여 스스로 정렬하며, / 언제나 자기 북극을 가리킵니다.",
                 "A balanced magnetic needle aligns itself / with the Earth's natural magnetic field, / always pointing toward magnetic north."),
                ("This indispensable navigational tool / enabled sailors to traverse open oceans safely, / even when clouds obscured the stars and sun.",
                 "이 없어서는 안 될 항해 도구는 / 구름이 별과 태양을 가렸을 때조차도, / 선원들이 탁 트인 바다를 안전하게 횡단할 수 있게 해 주었습니다.",
                 "This indispensable navigational tool / enabled sailors to traverse open oceans safely, / even when clouds obscured the stars and sun.")
            ],
            [
                ("maritime", "adj.", "해양의, 바다의", "Maritime law regulates shipping lanes and sea commerce."),
                ("lodestone", "n.", "천연 자석, 자철석", "Ancient navigators carved lodestone into floating pointer spoons."),
                ("align", "v.", "정렬하다, 나란히 맞추다", "Align the margins carefully before printing the manuscript."),
                ("obscure", "v.", "가리다, 흐리게 하다", "Heavy sea mist obscured the lighthouse beacon.")
            ],
            [
                ("one of the + 최상급 + 복수명사", "'가장 ~한 것들 중 하나'라는 전형적인 비교 최상급 구문입니다."),
                ("even when + 절", "'심지어 ~할 때조차도' 양보적 강조 표현입니다.")
            ],
            [
                ("Where and when was the magnetic compass first created?",
                 "자기 나침반은 언제 어디서 처음 제작되었는가?",
                 ["In ancient Rome during the reign of Augustus", "In ancient China during the Han Dynasty", "In 18th-century England during the Industrial Era", "In medieval Spain by royal astronomers"],
                 1,
                 "두 번째 문장에 한나라 시기 고대 중국에서 처음 제작되었다고 명시되어 있습니다."),
                ("What natural material was originally used to make the early compass?",
                 "초기 나침반을 제작하기 위해 원래 어떤 천연 물질이 사용되었는가?",
                 ["Naturally magnetized iron ore known as lodestone", "Polished yellow amber beads", "Carved white marble from Greek quarries", "Pure melted gold wires"],
                 0,
                 "두 번째 문장에 'using naturally magnetized iron ore known as lodestone'이라고 나와 있습니다."),
                ("Why was the compass indispensable when sailing at sea?",
                 "바다를 항해할 때 나침반이 왜 필수적이었는가?",
                 ["It told sailors how deep the ocean water was.", "It enabled sailors to navigate safely even when clouds obscured stars and the sun.", "It converted ocean salt water into fresh drinking water.", "It scared away dangerous sea monsters from ships."],
                 1,
                 "마지막 문장에 구름이 별과 태양을 가렸을 때조차 안전하게 바다를 횡단할 수 있게 해 주었다고 설명합니다.")
            ]
        ),
        (
            "b-79",
            "The Mechanics of Solar Eclipses",
            "일식의 발생 원리와 천체 정렬",
            "Astronomy",
            "NASA Eclipse Education Program",
            "일식은 달이 태양과 지구 사이를 완벽하게 통과하여 달의 그림자가 지구 표면에 드리워질 때 발생하는 장엄한 천문 현상입니다.",
            [
                ("A solar eclipse occurs / when the moon passes directly between the Earth and the sun, / temporarily blocking solar rays.",
                 "일식은 달이 지구와 태양 사이를 곧장 통과하여, / 태양 광선을 일시적으로 차단할 때 / 발생합니다.",
                 "A solar eclipse occurs / when the moon passes directly / between the Earth and the sun, / temporarily blocking solar rays."),
                ("During this alignment, / the moon casts a two-part celestial shadow upon the surface of the Earth.",
                 "이러한 천체 정렬 동안, / 달은 지구 표면에 두 부분으로 구성된 천체 그림자를 드리웁니다.",
                 "During this alignment, / the moon casts a two-part celestial shadow / upon the surface of the Earth."),
                ("The dark central core of the shadow / is called the umbra, / where the sun's fiery disk is completely obscured.",
                 "그림자의 어두운 중심 핵은 / 본영(umbra)이라 불리며, / 그곳에서는 태양의 불타는 원반이 완전히 가려집니다.",
                 "The dark central core of the shadow / is called the umbra, / where the sun's fiery disk is completely obscured."),
                ("Observers standing inside the narrow path of the umbra / witness a total eclipse, / revealing the sun's shimmering ghostly corona in the darkened daytime sky.",
                 "본영의 좁은 경로 안에 서 있는 관찰자들은 / 개기일식을 목격하게 되며, / 어두워진 낮 하늘에서 일렁이는 태양의 유령 같은 코로나를 보게 됩니다.",
                 "Observers standing inside the narrow path of the umbra / witness a total eclipse, / revealing the sun's shimmering ghostly corona / in the darkened daytime sky.")
            ],
            [
                ("alignment", "n.", "정렬, 일직선 배치", "The planets reached a rare celestial alignment across the night sky."),
                ("umbra", "n.", "본영 (완전 그림자)", "During a total solar eclipse, only the narrow umbra experiences complete darkness."),
                ("shimmering", "adj.", "어른거리는, 일렁이는", "A shimmering mirage appeared above the hot highway asphalt."),
                ("corona", "n.", "코로나 (태양 외곽 대기층)", "The delicate white solar corona is visible only when the moon blocks the sun."),
            ],
            [
                (", revealing ~", "분사구문으로 동시적인 결과를 나타내며 '그 결과 ~을 드러낸다'로 해석됩니다."),
                ("standing inside the path", "현재분사구가 앞의 명사 Observers를 수식합니다.")
            ],
            [
                ("What celestial body passes between the Earth and the sun during a solar eclipse?",
                 "일식 동안 어떤 천체가 지구와 태양 사이를 통과하는가?",
                 ["The planet Mars", "The moon", "A wandering comet", "The International Space Station"],
                 1,
                 "첫 문장에 달(the moon)이 지구와 태양 사이를 직접 통과한다고 나와 있습니다."),
                ("What is the dark central core of the moon's shadow called?",
                 "달 그림자의 어두운 중심부를 무엇이라 부르는가?",
                 ["The penumbra", "The umbra", "The solar flare", "The asteroid belt"],
                 1,
                 "세 번째 문장에 'dark central core of the shadow is called the umbra'라고 명시되어 있습니다."),
                ("What shimmering feature of the sun becomes visible during a total solar eclipse?",
                 "개기일식 동안 관찰 가능해지는 태양의 일렁이는 특징은 무엇인가?",
                 ["The sun's solid iron core", "The sun's shimmering corona", "Vast oceans of liquid boiling water on the sun", "Gigantic green forests on the solar surface"],
                 1,
                 "마지막 문장에 어두워진 낮 하늘에서 일렁이는 태양의 코로나(shimmering ghostly corona)가 드러난다고 설명합니다.")
            ]
        ),
        (
            "b-80",
            "Why Camels Have Humps",
            "낙타의 혹과 사막 환경 적응",
            "Zoology",
            "San Diego Zoo Wildlife Alliance Educational Archive",
            "낙타의 혹은 물이 아니라 고밀도 지방을 저장하고 있어, 물과 먹이가 부족한 사막에서 에너지를 공급하고 체온을 조절해 줍니다.",
            [
                ("A widespread myth suggests / that camel humps are filled with reserves of liquid drinking water.",
                 "널리 퍼진 한 속설은 / 낙타의 혹이 마시는 액체 상태의 물 저장소로 가득 차 있다고 / 시사합니다.",
                 "A widespread myth suggests / that camel humps are filled / with reserves of liquid drinking water."),
                ("In scientific reality, / a camel's hump stores large concentrations / of dense fatty tissue.",
                 "과학적 사실로는, / 낙타의 혹은 많은 양의 / 고밀도 지방 조직을 저장하고 있습니다.",
                 "In scientific reality, / a camel's hump stores large concentrations / of dense fatty tissue."),
                ("When food and water are scarce in the arid desert, / the camel's body metabolizes this stored fat / into caloric energy and metabolic moisture.",
                 "건조한 사막에서 먹이와 물이 부족할 때, / 낙타의 몸은 이 저장된 지방을 대사하여 / 열량 에너지와 대사성 수분으로 전환합니다.",
                 "When food and water are scarce in the arid desert, / the camel's body metabolizes this stored fat / into caloric energy and metabolic moisture."),
                ("By confining its body fat to a single hump / rather than distributing it under the skin, / the camel avoids overheating in blistering sun.",
                 "체지방을 피부 아래에 분산시키는 대신 / 하나의 혹에 국한시킴으로써, / 낙타는 타는 듯한 햇볕 속에서 체온이 과열되는 것을 방지합니다.",
                 "By confining its body fat to a single hump / rather than distributing it under the skin, / the camel avoids overheating / in blistering sun.")
            ],
            [
                ("myth", "n.", "통념, 잘못된 속설, 신화", "It is a popular myth that lightning never strikes the same place twice."),
                ("metabolize", "v.", "대사 작용을 하다, 소화 변환하다", "The liver metabolizes medicines into harmless water-soluble compounds."),
                ("confine", "v.", "제한하다, 가두다", "Please confine your questions to the topic discussed today."),
                ("blistering", "adj.", "맹렬한, 지독히 더운", "Runners struggled through the marathon under blistering summer heat.")
            ],
            [
                ("rather than -ing", "'~하기보다는 차라리' 대조 표현입니다."),
                ("By confining A to B", "'A를 B에 국한시킴으로써' 수단을 나타냅니다.")
            ],
            [
                ("What does a camel's hump actually store according to scientists?",
                 "과학자들에 따르면 낙타의 혹은 실제로 무엇을 저장하는가?",
                 ["Cold mountain rainwater", "Dense fatty tissue", "Excess volcanic minerals", "Liquid milk for calves"],
                 1,
                 "두 번째 문장에 고밀도 지방 조직(dense fatty tissue)을 저장한다고 명시되어 있습니다."),
                ("What happens to the stored fat when food and water are scarce?",
                 "먹이와 물이 부족할 때 저장된 지방은 어떻게 되는가?",
                 ["It hardens into rock-solid bone.", "The body metabolizes it into caloric energy and moisture.", "It leaks through the fur as sweet perfume.", "It dissolves completely into outer air."],
                 1,
                 "세 번째 문장에 저장된 지방을 열량 에너지와 대사성 수분으로 대사한다고 나와 있습니다."),
                ("Why does confining fat to a hump help camels in the desert?",
                 "지방을 혹에 모아두는 것이 왜 사막의 낙타에게 도움이 되는가?",
                 ["It makes the camel look much bigger to scare tigers.", "It prevents the camel from overheating in blistering sun.", "It allows camels to swim deep rivers easily.", "It attracts flying insects to feed on."],
                 1,
                 "마지막 문장에 전신 피부 아래 분산되지 않고 혹에 집중되어 타는 듯한 햇볕에서 과열되는 것을 방지한다고 설명합니다.")
            ]
        )
    ]
