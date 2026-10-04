# -*- coding: utf-8 -*-
"""
generate_expansion_210_b.py
10 Beginner passages (b-61 to b-70)
A2-B1 level, authoritative sources, sentence chunks, vocabulary, grammar, and 3 deducible comprehension questions per passage.
"""

def get_expansion_210_b():
    return [
        (
            "b-61",
            "The Science of Rainbows",
            "무지개가 생성되는 광학 원리",
            "Earth Science",
            "NOAA (National Oceanic and Atmospheric Administration) Educational Resource",
            "무지개는 공기 중 물방울에 의해 태양광이 굴절, 반사, 분산되면서 나타나는 아름다운 광학 현상입니다.",
            [
                ("A rainbow is an optical phenomenon / caused by both reflection and refraction of light.",
                 "무지개는 빛의 반사와 굴절 모두에 의해 발생하는 / 광학 현상입니다.",
                 "A rainbow is an optical phenomenon / caused by both reflection / and refraction of light."),
                ("When sunlight enters a raindrop, / it slows down and bends / as it moves from air to water.",
                 "태양빛이 빗방울로 들어갈 때, / 빛은 공기에서 물로 이동하면서 / 속도가 느려지고 굴절합니다.",
                 "When sunlight enters a raindrop, / it slows down and bends / as it moves from air to water."),
                ("Inside the droplet, / light reflects off the back surface / before emerging into the open air again.",
                 "물방울 내부에서, / 빛은 다시 바깥 공기로 나오기 전에 / 뒷면에서 반사됩니다.",
                 "Inside the droplet, / light reflects off the back surface / before emerging into the open air again."),
                ("Because different colors of light bend at slightly different angles, / white sunlight is separated into a vivid spectrum.",
                 "빛의 색상마다 약간 다른 각도로 굴절하기 때문에, / 흰색의 태양광은 생생한 스펙트럼으로 분리됩니다.",
                 "Because different colors of light / bend at slightly different angles, / white sunlight is separated / into a vivid spectrum.")
            ],
            [
                ("phenomenon", "n.", "현상, 사건", "A solar eclipse is a rare celestial phenomenon."),
                ("refraction", "n.", "굴절", "Refraction makes a straw in water look bent."),
                ("droplet", "n.", "작은 물방울", "Tiny water droplets form dense fog in the valley."),
                ("spectrum", "n.", "스펙트럼, 범위", "A glass prism separates white light into a rainbow spectrum.")
            ],
            [
                ("caused by + 명사", "과거분사구 수식으로 '~에 의해 발생된'을 뜻하며 명사를 뒤에서 수식합니다."),
                ("Because + 절", "원인이나 이유를 나타내는 접속사절로 '주어가 ~하기 때문에'로 해석됩니다.")
            ],
            [
                ("What happens when sunlight enters a raindrop according to the text?",
                 "본문에 따르면 햇빛이 빗방울 안으로 들어갈 때 무슨 일이 일어나는가?",
                 ["It speeds up and evaporates instantly.", "It slows down and bends as it moves from air to water.", "It completely turns into dark infrared heat.", "It bounces back without ever entering the droplet."],
                 1,
                 "두 번째 문장에서 'When sunlight enters a raindrop, it slows down and bends as it moves from air to water'라고 명시되어 있습니다."),
                ("Where does reflection happen inside the raindrop?",
                 "빗방울 내부의 어디에서 반사가 일어나는가?",
                 ["On the outer surface of the clouds", "Off the back surface inside the droplet", "Underneath the damp ground", "Only when passing through tree leaves"],
                 1,
                 "세 번째 문장에 'Inside the droplet, light reflects off the back surface'라고 설명되어 있습니다."),
                ("Why does white sunlight separate into different colors?",
                 "왜 백색 태양광이 서로 다른 색상들로 분리되는가?",
                 ["Because different colors of light bend at slightly different angles.", "Because the air pressure drops suddenly during thunder.", "Because raindrops absorb every color except blue.", "Because eyes only detect colors when looking upwards."],
                 0,
                 "마지막 문장에서 서로 다른 색의 빛이 약간씩 다른 각도로 꺾이기 때문이라고 설명합니다.")
            ]
        ),
        (
            "b-62",
            "How Penguins Survive Antarctic Cold",
            "남극 펭귄의 극한 추위 적응 생리학",
            "Zoology",
            "National Geographic Wildlife Encyclopedia",
            "남극의 극한 환경에서 펭귄은 두꺼운 지방층, 방수 깃털, 그리고 집단 허들링 행동을 통해 체온을 유지합니다.",
            [
                ("Emperor penguins endure winter temperatures / falling far below minus forty degrees Celsius.",
                 "황제펭귄은 영하 40도 아래로 떨어지는 / 겨울 기온을 견뎌냅니다.",
                 "Emperor penguins endure winter temperatures / falling far below / minus forty degrees Celsius."),
                ("They possess a dense layer of subcutaneous fat / called blubber / that prevents critical body heat loss.",
                 "그들은 치명적인 체온 손실을 방지하는 / 블러버(피하지방)라고 불리는 / 두꺼운 피하지방층을 가지고 있습니다.",
                 "They possess a dense layer / of subcutaneous fat called blubber / that prevents critical body heat loss."),
                ("On the outside, / tightly overlapping feathers form an impenetrable waterproof barrier.",
                 "바깥쪽에는, / 촘촘하게 겹쳐진 깃털들이 물이 스며들지 않는 방수 장벽을 형성합니다.",
                 "On the outside, / tightly overlapping feathers form / an impenetrable waterproof barrier."),
                ("During brutal blizzards, / penguins gather closely in large huddles / to share warmth and protect one another.",
                 "혹독한 눈보라가 칠 때, / 펭귄들은 온기를 나누고 서로를 보호하기 위해 / 거대한 무리로 밀착해 모입니다.",
                 "During brutal blizzards, / penguins gather closely in large huddles / to share warmth / and protect one another.")
            ],
            [
                ("endure", "v.", "견디다, 인내하다", "Camels can endure extreme heat and lack of water."),
                ("subcutaneous", "adj.", "피하의, 피부 밑의", "Subcutaneous injections reach beneath the dermis."),
                ("impenetrable", "adj.", "침투할 수 없는, 뚫을 수 없는", "The fortress walls were impenetrable to enemy cannons."),
                ("huddle", "n.", "옹기종기 모임, 밀착 군집", "The players formed a tight huddle before starting the match.")
            ],
            [
                ("possess + 목적어", "'~을 보유하다, 가지고 있다'라는 의미의 격식체 타동사입니다."),
                ("overlapping", "현재분사 형용사로 '서로 겹쳐지는'을 뜻하며 뒤의 명사를 수식합니다.")
            ],
            [
                ("What is the primary function of penguin blubber?",
                 "펭귄 지방층(blubber)의 주된 기능은 무엇인가?",
                 ["To enable long-distance flight", "To prevent critical body heat loss", "To help them camouflage in the green grass", "To produce electric shocks for self-defense"],
                 1,
                 "두 번째 문장에서 블러버가 치명적인 체온 손실을 막는다고 설명합니다."),
                ("What forms an impenetrable waterproof barrier on penguins?",
                 "펭귄의 몸에서 물이 침투하지 않는 방수 장벽을 이루는 것은 무엇인가?",
                 ["A coat of frozen ice", "Tightly overlapping feathers", "Thick sea salt crystals", "Synthetic wax secreted by seals"],
                 1,
                 "세 번째 문장에 'tightly overlapping feathers form an impenetrable waterproof barrier'라고 나와 있습니다."),
                ("Why do penguins gather in large huddles during blizzards?",
                 "눈보라가 칠 때 펭귄들이 커다란 무리를 이루어 모이는 이유는 무엇인가?",
                 ["To locate buried fish eggs", "To share warmth and protect one another", "To signal overhead rescue planes", "To sharpen their beaks on stones"],
                 1,
                 "마지막 문장에 온기를 나누고 서로를 지키기 위해서라고 명시되어 있습니다.")
            ]
        ),
        (
            "b-63",
            "The Gutenberg Printing Revolution",
            "구텐베르크 활판 인쇄 혁명",
            "World History",
            "Encyclopaedia Britannica & British Library Records",
            "15세기 구텐베르크의 금속 활판 인쇄술 발명은 지식의 대량 보급과 르네상스 확산의 기폭제가 되었습니다.",
            [
                ("In the mid-fifteenth century, / Johannes Gutenberg invented movable metal type in Germany.",
                 "15세기 중반, / 요하네스 구텐베르크는 독일에서 금속 활자를 발명했습니다.",
                 "In the mid-fifteenth century, / Johannes Gutenberg invented / movable metal type in Germany."),
                ("Before this milestone, / every single book had to be laboriously copied by hand.",
                 "이 기념비적인 사건 전에는, / 모든 단 한 권의 책도 손으로 힘들게 필사되어야만 했습니다.",
                 "Before this milestone, / every single book had to be / laboriously copied by hand."),
                ("Gutenberg's durable mechanical press / allowed thousands of uniform pages / to be printed rapidly.",
                 "구텐베르크의 내구성 있는 기계식 인쇄기는 / 수천 장의 균일한 페이지가 / 신속하게 인쇄되도록 만들었습니다.",
                 "Gutenberg's durable mechanical press / allowed thousands of uniform pages / to be printed rapidly."),
                ("This dramatic technological leap / made books affordable / and ignited widespread literacy across Europe.",
                 "이 획기적인 기술적 도약은 / 책의 가격을 저렴하게 만들었고 / 유럽 전역에 광범위한 문해력을 촉발했습니다.",
                 "This dramatic technological leap / made books affordable / and ignited widespread literacy / across Europe.")
            ],
            [
                ("movable", "adj.", "이동식의, 움직일 수 있는", "Movable furniture provides great flexibility in small rooms."),
                ("laboriously", "adv.", "고되게, 공들여", "Scholars laboriously deciphered ancient stone inscriptions."),
                ("uniform", "adj.", "균일한, 일관된", "The factory produced bricks of uniform size and strength."),
                ("literacy", "n.", "문해력, 읽고 쓰는 능력", "Universal education led to higher adult literacy rates.")
            ],
            [
                ("had to be + p.p.", "'~되어야만 했다'라는 수동태 의무 표현입니다."),
                ("allow A to B", "'A가 B하도록 허용하다/가능하게 만들다'라는 전형적인 5형식 구문입니다.")
            ],
            [
                ("How were books produced before Gutenberg's invention?",
                 "구텐베르크 발명 이전에 책들은 어떻게 제작되었는가?",
                 ["They were carved into marble slabs.", "Every single book had to be laboriously copied by hand.", "They were photocopied on digital parchment.", "They were spoken into wax recording tubes."],
                 1,
                 "두 번째 문장에 책들이 손으로 힘들게 필사되어야 했다고 명시되어 있습니다."),
                ("What was an immediate benefit of Gutenberg's mechanical press?",
                 "구텐베르크의 기계식 인쇄기가 가져온 즉각적인 이점은 무엇인가?",
                 ["It replaced paper with heavy metal plates.", "It allowed thousands of uniform pages to be printed rapidly.", "It banned all foreign books in Germany.", "It prevented people from reading religious texts."],
                 1,
                 "세 번째 문장에 수천 장의 균일한 페이지를 신속히 인쇄할 수 있게 되었다고 나와 있습니다."),
                ("What impact did Gutenberg's press have across Europe?",
                 "구텐베르크의 인쇄기는 유럽 전역에 어떤 영향을 미쳤는가?",
                 ["It made books affordable and ignited widespread literacy.", "It made education completely illegal for citizens.", "It forced all libraries to close down permanently.", "It reduced paper production to near zero."],
                 0,
                 "마지막 문장에 책의 가격이 저렴해지고 광범위한 문해력이 촉발되었다고 설명합니다.")
            ]
        ),
        (
            "b-64",
            "Why Autumn Leaves Turn Red and Gold",
            "가을철 나뭇잎의 색소 변화 원리",
            "Botany",
            "U.S. Forest Service Research Publication",
            "가을이 되면 일조량 감소로 녹색 엽록소가 파괴되면서 숨어 있던 카로티노이드와 안토시아닌의 붉고 노란 색이 드러납니다.",
            [
                ("During spring and summer, / green chlorophyll absorbs sunlight / to generate plant food via photosynthesis.",
                 "봄과 여름 동안, / 녹색 엽록소는 햇빛을 흡수하여 / 광합성을 통해 식물의 양분을 생성합니다.",
                 "During spring and summer, / green chlorophyll absorbs sunlight / to generate plant food / via photosynthesis."),
                ("As daylight hours shorten in autumn, / trees gradually reduce chlorophyll production.",
                 "가을에 낮의 길이가 짧아짐에 따라, / 나무는 점진적으로 엽록소 생성을 줄여나갑니다.",
                 "As daylight hours shorten in autumn, / trees gradually reduce / chlorophyll production."),
                ("When the overpowering green pigment fades, / yellow and orange carotenoids already inside the leaf / become visible.",
                 "강렬했던 녹색 색소가 사라지면, / 이미 잎 안에 존재하던 노란색과 주황색 카로티노이드가 / 눈에 보이게 됩니다.",
                 "When the overpowering green pigment fades, / yellow and orange carotenoids / already inside the leaf / become visible."),
                ("Additionally, / cool autumn nights stimulate the production of bright red anthocyanin pigments.",
                 "또한, / 서늘한 가을밤은 선명한 붉은색 안토시아닌 색소의 생성을 촉진합니다.",
                 "Additionally, / cool autumn nights / stimulate the production / of bright red anthocyanin pigments.")
            ],
            [
                ("chlorophyll", "n.", "엽록소", "Chlorophyll gives plant leaves their vibrant green color."),
                ("photosynthesis", "n.", "광합성", "Plants convert light energy into glucose through photosynthesis."),
                ("pigment", "n.", "색소, 염료", "Natural pigments in berries yield deep purple dyes."),
                ("stimulate", "v.", "자극하다, 촉진하다", "Gentle aerobic exercise stimulates heart rate and circulation.")
            ],
            [
                ("As + 주어 + 동사", "'~함에 따라, ~할 때' 시간의 경과나 비례적 변화를 나타냅니다."),
                ("become + 형용사", "상태의 변화를 나타내는 2형식 동사로 '~한 상태가 되다'를 의미합니다.")
            ],
            [
                ("What role does green chlorophyll play during spring and summer?",
                 "봄과 여름 동안 녹색 엽록소는 어떤 역할을 하는가?",
                 ["It repels insects with strong odors.", "It absorbs sunlight to generate plant food via photosynthesis.", "It causes leaves to drop off branches immediately.", "It freezes moisture in the plant roots."],
                 1,
                 "첫 문장에 광합성을 통해 식물의 양분을 생성하기 위해 햇빛을 흡수한다고 명시되어 있습니다."),
                ("Why do yellow and orange colors appear in autumn leaves?",
                 "가을철 나뭇잎에서 왜 노란색과 주황색이 나타나는가?",
                 ["Because the green pigment fades, revealing existing carotenoids.", "Because the soil turns bright orange from rust.", "Because winter frost paints the leaf tips.", "Because bird droppings alter the tree's chemical structure."],
                 0,
                 "세 번째 문장에 녹색 색소가 희미해지며 이미 존재하던 카로티노이드가 드러난다고 설명합니다."),
                ("What promotes the formation of red anthocyanin pigments?",
                 "붉은색 안토시아닌 색소의 형성을 촉진하는 요인은 무엇인가?",
                 ["Dry desert winds", "Cool autumn nights", "Continuous twenty-four-hour direct sunlight", "Excessive ocean rainfall"],
                 1,
                 "마지막 문장에 'cool autumn nights stimulate the production of bright red anthocyanin pigments'라고 나와 있습니다.")
            ]
        ),
        (
            "b-65",
            "Bioluminescence in the Deep Ocean",
            "심해 생물의 생물발광 메커니즘",
            "Marine Biology",
            "Monterey Bay Aquarium Research Institute (MBARI)",
            "빛이 도달하지 않는 칠흑 같은 심해에서 생물들은 화학 반응을 통해 빛을 내며 포식자를 피하거나 먹이를 유인합니다.",
            [
                ("In the bathypelagic zone of the ocean, / sunlight cannot penetrate the immense depth of water.",
                 "해양의 심해저대에서는, / 햇빛이 엄청난 수심의 물을 뚫고 들어갈 수 없습니다.",
                 "In the bathypelagic zone / of the ocean, / sunlight cannot penetrate / the immense depth of water."),
                ("Over seventy percent of deep-sea creatures / produce their own light / through a process called bioluminescence.",
                 "70퍼센트가 넘는 심해 생물들이 / 생물발광이라 불리는 과정을 통해 / 스스로의 빛을 만들어냅니다.",
                 "Over seventy percent / of deep-sea creatures / produce their own light / through a process called bioluminescence."),
                ("This cold light is created / when a molecule called luciferin / reacts with oxygen and an enzyme.",
                 "이 차가운 빛은 / 루시페린이라는 분자가 / 산소 및 효소와 반응할 때 생성됩니다.",
                 "This cold light is created / when a molecule called luciferin / reacts with oxygen and an enzyme."),
                ("Animals use these luminous flashes / to lure unsuspecting prey, / confuse predators, / or communicate in the dark.",
                 "동물들은 이러한 발광 섬광을 이용하여 / 경계하지 않는 먹잇감을 유인하거나, / 포식자를 교란하거나, / 어둠 속에서 소통합니다.",
                 "Animals use these luminous flashes / to lure unsuspecting prey, / confuse predators, / or communicate in the dark.")
            ],
            [
                ("penetrate", "v.", "관통하다, 침투하다", "Radar signals cannot easily penetrate dense concrete walls."),
                ("bioluminescence", "n.", "생물발광", "Fireflies and deep-sea anglerfish exhibit bioluminescence."),
                ("enzyme", "n.", "효소", "Digestive enzymes break down complex carbohydrates in the stomach."),
                ("luminous", "adj.", "빛을 발하는, 야광의", "Luminous hands on the watch allow time reading in the dark.")
            ],
            [
                ("Over + 수사 + percent", "'~퍼센트 이상의'를 나타내는 수량 표현입니다."),
                ("use A to B", "'B하기 위해 A를 사용하다' 목적을 나타내는 to부정사 구문입니다.")
            ],
            [
                ("Why can sunlight not reach the bathypelagic zone?",
                 "왜 햇빛이 심해저대에 도달할 수 없는가?",
                 ["Because sea ice blocks the sky permanently.", "Because of the immense depth of water.", "Because deep-sea water is made of black oil.", "Because clouds permanently cover the entire ocean."],
                 1,
                 "첫 문장에 'sunlight cannot penetrate the immense depth of water'라고 설명되어 있습니다."),
                ("What chemical reaction produces bioluminescent light?",
                 "어떤 화학 반응이 생물발광의 빛을 생성하는가?",
                 ["The collision of dry volcanic sulfur and nitrogen", "A molecule called luciferin reacting with oxygen and an enzyme", "The rapid decay of radioactive uranium in sand", "Electric sparks generated by copper scales"],
                 1,
                 "세 번째 문장에 루시페린 분자가 산소 및 효소와 반응하여 만들어진다고 나와 있습니다."),
                ("What is ONE purpose of luminous flashes mentioned in the passage?",
                 "본문에서 언급된 발광 섬광의 목적 중 하나는 무엇인가?",
                 ["To boil surrounding cold seawater", "To lure unsuspecting prey", "To build underground stone nests", "To measure water salinity"],
                 1,
                 "마지막 문장에 'to lure unsuspecting prey, confuse predators, or communicate'라고 명시되어 있습니다.")
            ]
        ),
        (
            "b-66",
            "The Stages of Seed Germination",
            "씨앗 발아와 식물 성장의 초기 단계",
            "Agricultural Science",
            "Royal Horticultural Society Education Guide",
            "휴면 상태의 씨앗은 수분, 적절한 온도, 산소를 흡수하면서 대사 작용을 시작하여 뿌리와 싹을 틔웁니다.",
            [
                ("A dry seed contains an inactive plant embryo / protected by a tough exterior seed coat.",
                 "건조한 씨앗은 질긴 외부 씨껍질에 의해 보호받는 / 휴면 상태의 식물 배아를 포함하고 있습니다.",
                 "A dry seed contains / an inactive plant embryo / protected by a tough exterior seed coat."),
                ("When exposed to favorable moisture and temperature, / the seed absorbs water rapidly / through a process called imbibition.",
                 "유리한 수분과 온도에 노출되었을 때, / 씨앗은 임비비션(수분 흡수)이라 불리는 과정을 통해 / 물을 빠르게 흡수합니다.",
                 "When exposed to favorable moisture / and temperature, / the seed absorbs water rapidly / through a process called imbibition."),
                ("This hydration activates dormant enzymes, / which break down stored starches into nourishing sugars.",
                 "이러한 수분 공급은 휴면 중이던 효소들을 활성화하며, / 이 효소들은 저장된 전분을 영양가 있는 당분으로 분해합니다.",
                 "This hydration activates dormant enzymes, / which break down stored starches / into nourishing sugars."),
                ("Soon, the embryonic root / called the radicle / breaks through the softened coat / to anchor in the soil.",
                 "곧, 유근이라 불리는 / 배아 뿌리가 / 부드러워진 껍질을 뚫고 나와 / 토양에 단단히 고정됩니다.",
                 "Soon, the embryonic root called the radicle / breaks through the softened coat / to anchor in the soil.")
            ],
            [
                ("embryo", "n.", "배아, 싹", "The fertile egg contained an early bird embryo."),
                ("imbibition", "n.", "흡수, 침윤", "Imbibition causes dried seeds to swell before sprouting."),
                ("dormant", "adj.", "휴면 상태의, 잠자는", "Volcanoes can remain dormant for centuries before erupting."),
                ("anchor", "v.", "닻을 내리다, 단단히 고정하다", "Deep tree roots anchor firmly into bedrock to withstand storms.")
            ],
            [
                ("When exposed to ~", "'When it is exposed to ~'에서 주어와 be동사가 생략된 분사구문입니다."),
                ("which break down ~", "계속적 용법의 관계대명사로 '그리고 그것들이 ~을 분해한다'로 해석됩니다.")
            ],
            [
                ("What protects the inactive plant embryo inside a seed?",
                 "씨앗 내부의 휴면 상태 식물 배아를 보호하는 것은 무엇인가?",
                 ["A cluster of sharp green thorns", "A tough exterior seed coat", "A thick layer of frozen winter snow", "A waterproof wax secreted by adult leaves"],
                 1,
                 "첫 문장에 'protected by a tough exterior seed coat'라고 명시되어 있습니다."),
                ("What triggers the activation of dormant enzymes inside the seed?",
                 "씨앗 내부에서 휴면 중이던 효소들을 활성화하는 계기는 무엇인가?",
                 ["Extreme heat above boiling point", "Hydration through water absorption (imbibition)", "Complete isolation from surrounding moisture", "Exposure to heavy industrial metals"],
                 1,
                 "세 번째 문장에 'This hydration activates dormant enzymes'라고 나와 있습니다."),
                ("What does the radicle do once it breaks through the seed coat?",
                 "유근(radicle)이 씨껍질을 뚫고 나온 후 무엇을 하는가?",
                 ["It anchors in the soil.", "It turns directly into mature flower petals.", "It flies into the air using downy hairs.", "It dissolves all nearby stones into liquid."],
                 0,
                 "마지막 문장에 부드러워진 껍질을 뚫고 나와 토양에 고정된다고 설명합니다.")
            ]
        ),
        (
            "b-67",
            "The Engineering of Roman Aqueducts",
            "고대 로마 수도교의 공학적 경이",
            "Archaeology & Engineering",
            "Smithsonian Magazine & Historic Civil Engineering Records",
            "고대 로마인들은 펌프 없이 중력의 경사각만을 활용하여 수십 킬로미터 밖의 깨끗한 샘물을 도시로 운반했습니다.",
            [
                ("Ancient Roman aqueducts were marvels of civil engineering / designed to supply fresh water to distant cities.",
                 "고대 로마 수도교는 먼 도시들에 깨끗한 물을 공급하도록 설계된 / 토목 공학의 경이로운 걸작이었습니다.",
                 "Ancient Roman aqueducts were marvels / of civil engineering / designed to supply fresh water / to distant cities."),
                ("Rather than using pumps, / Roman engineers relied entirely on the natural force of gravity.",
                 "펌프를 사용하는 대신, / 로마 공학자들은 전적으로 중력의 자연스러운 힘에 의존했습니다.",
                 "Rather than using pumps, / Roman engineers relied entirely / on the natural force of gravity."),
                ("They constructed stone channels with a continuous, slight downward slope / to keep water flowing steadily.",
                 "그들은 물이 꾸준히 흐르도록 유지하기 위해 / 끊이지 않고 완만한 하향 경사를 가진 석조 수로를 건설했습니다.",
                 "They constructed stone channels / with a continuous, slight downward slope / to keep water flowing steadily."),
                ("These majestic conduits / crossed wide valleys using arched bridges / and provided clean drinking water to millions.",
                 "이 웅장한 수로들은 / 아치형 다리를 이용해 넓은 계곡을 건넜으며 / 수백만 명에게 깨끗한 식수를 제공했습니다.",
                 "These majestic conduits / crossed wide valleys / using arched bridges / and provided clean drinking water / to millions.")
            ],
            [
                ("aqueduct", "n.", "수도교, 수로", "The Pont du Gard is a remarkably preserved Roman aqueduct."),
                ("marvel", "n.", "경이로운 것, 놀라운 업적", "Modern suspension bridges are engineering marvels."),
                ("conduit", "n.", "도관, 수로", "Underground conduits carry electrical cables through the city."),
                ("downward", "adj./adv.", "아래로 향하는, 하향의", "The gentle downward slope allowed runoff water to drain.")
            ],
            [
                ("Rather than -ing", "'~하기보다는, ~하는 대신에' 대비를 나타내는 전치사적 표현입니다."),
                ("rely on + 명사", "'~에 의존하다, 기대다'라는 필수 빈출 숙어입니다.")
            ],
            [
                ("What force did Roman engineers rely on to move water through aqueducts?",
                 "로마 공학자들은 수도교로 물을 이동시키기 위해 어떤 힘에 의존했는가?",
                 ["Steam-powered water pumps", "The natural force of gravity", "Windmill rotation mechanisms", "Manual bucket wheels powered by horses"],
                 1,
                 "두 번째 문장에 'Roman engineers relied entirely on the natural force of gravity'라고 적혀 있습니다."),
                ("Why were the stone channels built with a downward slope?",
                 "왜 석조 수로는 하향 경사를 지니도록 건설되었는가?",
                 ["To prevent soldiers from walking inside", "To keep water flowing steadily", "To store excess grain during famines", "To make room for defensive archers"],
                 1,
                 "세 번째 문장에 'to keep water flowing steadily'라고 명시되어 있습니다."),
                ("How did aqueducts cross wide valleys according to the text?",
                 "본문에 따르면 수도교는 넓은 계곡을 어떻게 건넜는가?",
                 ["Through wooden canoes", "Using arched bridges", "By evaporating into clouds first", "Inside hollowed oak tree trunks"],
                 1,
                 "마지막 문장에 'crossed wide valleys using arched bridges'라고 명시되어 있습니다.")
            ]
        ),
        (
            "b-68",
            "The Waggle Dance of Honeybees",
            "꿀벌의 8자 춤과 정보 전달 체계",
            "Entomology",
            "Scientific American & Karl von Frisch Nobel Studies",
            "꿀벌은 벌통 안에서 특유의 8자 춤(Waggle Dance)을 춤으로써 동료 벌들에게 꽃의 방향과 거리를 정확히 전달합니다.",
            [
                ("Honeybees communicate the exact location of rich food sources / through a unique ritual called the waggle dance.",
                 "꿀벌은 8자 춤이라 불리는 독특한 의식을 통해 / 풍부한 먹이원의 정확한 위치를 전달합니다.",
                 "Honeybees communicate the exact location / of rich food sources / through a unique ritual / called the waggle dance."),
                ("A returning forager bee performs a figure-eight pattern / on the vertical comb inside the hive.",
                 "돌아온 정찰벌은 벌통 내부의 수직 벌집 위에서 / 숫자 8 모양의 패턴을 수행합니다.",
                 "A returning forager bee / performs a figure-eight pattern / on the vertical comb inside the hive."),
                ("The angle of her central waggle run / indicates the flower's direction / relative to the position of the sun.",
                 "벌이 중앙에서 몸을 흔들며 나아가는 각도는 / 태양의 위치를 기준으로 한 / 꽃의 방향을 나타냅니다.",
                 "The angle of her central waggle run / indicates the flower's direction / relative to the position of the sun."),
                ("Furthermore, / the duration of the waggle vibration tells nestmates / precisely how far away the blossoms are.",
                 "게다가, / 몸을 흔드는 진동의 지속 시간은 동료 벌들에게 / 그 꽃들이 얼마나 멀리 떨어져 있는지를 정확히 알려줍니다.",
                 "Furthermore, / the duration of the waggle vibration / tells nestmates / precisely how far away the blossoms are.")
            ],
            [
                ("forager", "n.", "먹이를 찾는 자, 채집벌", "Forager ants travel meters away from the nest to collect seeds."),
                ("comb", "n.", "벌집", "Bees construct hexagonal wax combs to store golden honey."),
                ("relative to", "prep.", "~에 비례하여, ~와 관련하여", "The boat moved at ten knots relative to the shoreline."),
                ("duration", "n.", "지속 시간, 기간", "The total duration of the flight was four hours.")
            ],
            [
                ("relative to + 명사", "'~을 기준으로, ~와 비교하여' 기준점을 명시하는 표현입니다."),
                ("tells + 간접목적어 + 직접목적어(의문사절)", "4형식 문장으로 '동료들에게 얼마나 먼지를 말해준다'는 구조입니다.")
            ],
            [
                ("What does the returning forager bee perform inside the hive?",
                 "돌아온 채집벌은 벌통 내부에서 무엇을 수행하는가?",
                 ["A figure-eight dance pattern", "A complete hibernation sleep", "A loud buzzing alert to defend the queen", "A circular burrow in the wooden floor"],
                 0,
                 "두 번째 문장에 'performs a figure-eight pattern on the vertical comb'라고 나와 있습니다."),
                ("What does the angle of the waggle run indicate?",
                 "벌이 흔들며 나아가는 각도는 무엇을 나타내는가?",
                 ["The age of the queen bee", "The flower's direction relative to the sun", "The temperature inside the beehive", "The arrival of autumn rain"],
                 1,
                 "세 번째 문장에 'indicates the flower's direction relative to the position of the sun'이라고 명시되어 있습니다."),
                ("How do nestmates learn how far away the blossoms are?",
                 "동료 벌들은 꽃이 얼마나 멀리 있는지 어떻게 알게 되는가?",
                 ["By smelling the forager's wings", "From the duration of the waggle vibration", "By counting how many leaves the bee brought", "By observing the color of the pollen"],
                 1,
                 "마지막 문장에 진동의 지속 시간(duration of the waggle vibration)이 거리를 알려준다고 설명합니다.")
            ]
        ),
        (
            "b-69",
            "The Formation of Atmospheric Clouds",
            "대기 중 구름의 응결과 생성 메커니즘",
            "Meteorology",
            "World Meteorological Organization (WMO) Educational Resource",
            "지표면의 따뜻한 공기가 상승하며 냉각될 때, 수증기가 미세한 응결핵에 응결되면서 무수한 물방울로 이루어진 구름이 형성됩니다.",
            [
                ("Clouds are visible collections / of billions of microscopic water droplets or ice crystals / suspended in the air.",
                 "구름은 공기 중에 떠 있는 / 수십억 개의 미세한 물방울이나 얼음 결정들의 / 눈에 보이는 집합체입니다.",
                 "Clouds are visible collections / of billions of microscopic water droplets / or ice crystals / suspended in the air."),
                ("They begin to form / when warm, moist air rises from the Earth's surface / and cools as it ascends.",
                 "구름은 따뜻하고 습한 공기가 지표면에서 상승하여 / 위로 올라가면서 냉각될 때 / 형성되기 시작합니다.",
                 "They begin to form / when warm, moist air rises / from the Earth's surface / and cools as it ascends."),
                ("Because cool air holds less moisture than warm air, / the invisible water vapor condenses into liquid drops.",
                 "차가운 공기는 따뜻한 공기보다 수분을 덜 머금기 때문에, / 눈에 보이지 않던 수증기가 액체 방울로 응결됩니다.",
                 "Because cool air holds less moisture / than warm air, / the invisible water vapor / condenses into liquid drops."),
                ("This condensation requires tiny airborne particles / such as dust or salt, / known as cloud condensation nuclei.",
                 "이 응결 과정은 구름 응결핵으로 알려진 / 먼지나 소금과 같은 / 공기 중의 미세한 입자들을 필요로 합니다.",
                 "This condensation requires tiny airborne particles / such as dust or salt, / known as cloud condensation nuclei.")
            ],
            [
                ("microscopic", "adj.", "미세한, 현미경으로만 보이는", "Microscopic bacteria thrive in warm soil environments."),
                ("suspended", "adj.", "떠 있는, 매달린", "Tiny dust specks remained suspended in the beam of light."),
                ("condense", "v.", "응결되다, 농축되다", "Steam condenses into droplets on a cold glass window."),
                ("nuclei", "n. (pl.)", "핵 (nucleus의 복수형)", "Condensation nuclei provide a surface for vapor to collect.")
            ],
            [
                ("suspended in the air", "과거분사구로 앞의 물방울과 얼음 결정들을 수식합니다."),
                ("holds less A than B", "'B보다 더 적은 A를 수용하다/머금다' 비교급 표현입니다.")
            ],
            [
                ("What are clouds composed of according to the text?",
                 "본문에 따르면 구름은 무엇으로 구성되어 있는가?",
                 ["Burning sulfur gas and soot", "Microscopic water droplets or ice crystals suspended in the air", "Solid plates of frozen titanium", "Pure static electrical energy"],
                 1,
                 "첫 문장에 'microscopic water droplets or ice crystals suspended in the air'라고 나와 있습니다."),
                ("Why does water vapor condense as warm air rises?",
                 "따뜻한 공기가 상승할 때 왜 수증기가 응결되는가?",
                 ["Because the air cools, and cool air holds less moisture than warm air.", "Because the sun's gravity pulls water molecules together.", "Because birds flap their wings to press the air.", "Because ozone gas turns moisture into ice immediately."],
                 0,
                 "세 번째 문장에 찬 공기가 따뜻한 공기보다 수분을 덜 머금기 때문이라고 설명합니다."),
                ("What is needed for water vapor to condense into droplets?",
                 "수증기가 물방울로 응결되기 위해 무엇이 필요한가?",
                 ["A lightning strike", "Tiny airborne particles like dust or salt (condensation nuclei)", "Complete absence of any air pressure", "Large magnetic rocks on mountains"],
                 1,
                 "마지막 문장에 먼지나 소금 같은 미세 입자(cloud condensation nuclei)가 필요하다고 나와 있습니다.")
            ]
        ),
        (
            "b-70",
            "The Chemistry of Baking Bread",
            "빵 굽기 속에 숨겨진 화학 반응",
            "Food Chemistry",
            "American Chemical Society (ACS) Food Science Bulletin",
            "밀가루 속 단백질이 물과 만나 글루텐 망을 형성하고, 효모가 생성한 이산화탄소 기포가 부풀어 오르며 부드러운 빵이 완성됩니다.",
            [
                ("Baking a loaf of bread / is a precise culinary application / of fundamental chemical principles.",
                 "빵 한 덩이를 굽는 것은 / 기초적인 화학적 원리들을 / 정밀하게 조리에 응용한 것입니다.",
                 "Baking a loaf of bread / is a precise culinary application / of fundamental chemical principles."),
                ("When flour is combined with water and kneaded, / two proteins called glutenin and gliadin / bind together to form gluten.",
                 "밀가루를 물과 섞어 반죽할 때, / 글루테닌과 글리아딘이라는 두 단백질이 / 서로 결합하여 글루텐을 형성합니다.",
                 "When flour is combined with water and kneaded, / two proteins called glutenin and gliadin / bind together to form gluten."),
                ("Living yeast cells feed on flour sugars / and produce bubbles of carbon dioxide gas / that inflate the stretchy dough.",
                 "살아있는 효모 세포들은 밀가루 당분을 섭취하고 / 탄력 있는 반죽을 부풀리는 / 이산화탄소 기체 방울들을 생성합니다.",
                 "Living yeast cells / feed on flour sugars / and produce bubbles of carbon dioxide gas / that inflate the stretchy dough."),
                ("Finally, high oven heat causes the Maillard reaction, / creating a flavorful brown crust / and alluring aroma.",
                 "마지막으로, 오븐의 높은 열은 마이야르 반응을 일으켜, / 풍미 가득한 갈색 껍질과 / 매혹적인 향기를 만들어냅니다.",
                 "Finally, high oven heat / causes the Maillard reaction, / creating a flavorful brown crust / and alluring aroma.")
            ],
            [
                ("knead", "v.", "반죽하다, 주무르다", "The baker kneaded the dough for ten minutes until smooth."),
                ("inflate", "v.", "부풀리다, 팽창시키다", "Bicycle pumps are used to inflate rubber tires."),
                ("culinary", "adj.", "요리의, 조리의", "She developed exceptional culinary skills at French cooking school."),
                ("alluring", "adj.", "매혹적인, 유혹적인", "The fresh bakery gave off an alluring fragrance of warm pastry.")
            ],
            [
                ("When + 주어 + be p.p. and p.p.", "수동태 접속사절로 '주어가 ~되고 ~될 때'로 해석됩니다."),
                (", creating ~", "결과를 나타내는 연속 분사구문으로 '그 결과 ~을 창출한다'를 의미합니다.")
            ],
            [
                ("What two proteins combine to form gluten when flour is kneaded?",
                 "밀가루를 반죽할 때 어떤 두 단백질이 결합하여 글루텐을 형성하는가?",
                 ["Keratin and collagen", "Glutenin and gliadin", "Hemoglobin and insulin", "Casein and whey"],
                 1,
                 "두 번째 문장에 'two proteins called glutenin and gliadin bind together to form gluten'이라고 명시되어 있습니다."),
                ("What gas do yeast cells produce to inflate the dough?",
                 "효모 세포가 반죽을 부풀리기 위해 생성하는 기체는 무엇인가?",
                 ["Pure oxygen", "Carbon dioxide gas", "Nitrous oxide", "Methane gas"],
                 1,
                 "세 번째 문장에 효모가 이산화탄소 기체(carbon dioxide gas) 방울을 만든다고 나와 있습니다."),
                ("What causes the flavorful brown crust on bread during baking?",
                 "빵을 구울 때 풍미 있는 갈색 껍질을 만드는 것은 무엇인가?",
                 ["High oven heat causing the Maillard reaction", "Adding cold water after taking it out of the oven", "Freezing the dough below minus ten degrees", "Exposing the crust to ultraviolet light"],
                 0,
                 "마지막 문장에 오븐의 고열이 마이야르 반응을 일으켜 풍미 있는 갈색 껍질을 만든다고 나와 있습니다.")
            ]
        )
    ]
