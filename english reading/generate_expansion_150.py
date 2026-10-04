# -*- coding: utf-8 -*-
"""
generate_expansion_150.py
Produces 30 additional passages (b-41..50, i-41..50, a-41..50)
to elevate the collection to 150 passages (50 Beginner, 50 Intermediate, 50 Advanced).
"""

def get_expansion_150():
    # 10 Beginner (b-41 to b-50)
    b_extra = [
        ("b-41", "The Physics of Sailing Against the Wind", "바람을 거슬러 항해하는 범선의 물리학", "Physics & Navigation", "Scientific American",
         "돛이 비행기 날개처럼 양력을 발생시켜 맞바람을 거슬러 지그재그로 나아가는 원리를 설명합니다.",
         [
             ("Sailing directly into the teeth of the wind is aerodynamically impossible for any sailing vessel.", "바람이 불어오는 정면을 향해 곧장 항해하는 것은 어떤 범선에게도 공기역학적으로 불가능합니다.", "Sailing directly into the teeth of the wind / is aerodynamically impossible / for any sailing vessel."),
             ("However, experienced sailors can travel upwind by maneuvering their craft in a zigzag pattern called tacking.", "그러나 노련한 항해사들은 태킹이라 불리는 지그재그 패턴으로 배를 조종하여 풍상 쪽으로 이동할 수 있습니다.", "However, experienced sailors can travel upwind / by maneuvering their craft / in a zigzag pattern called tacking."),
             ("When wind flows across a curved canvas sail, it acts like an airplane wing, generating forward aerodynamic lift.", "바람이 곡면 캔버스 돛을 가로질러 흐를 때, 돛은 비행기 날개처럼 작용하여 전방 공기역학적 양력을 발생시킵니다.", "When wind flows across a curved canvas sail, / it acts like an airplane wing, / generating forward aerodynamic lift."),
             ("At the same time, the heavy underwater keel prevents the boat from slipping sideways across the water.", "동시에, 수중의 무거운 용골은 배가 물 위에서 옆으로 미끄러지는 것을 방지합니다.", "At the same time, / the heavy underwater keel prevents the boat / from slipping sideways / across the water."),
             ("By balancing sail lift against keel water resistance, the vessel converts transverse wind energy into forward motion.", "돛의 양력과 용골의 수중 저항의 균형을 맞춤으로써, 선박은 가로 방향 바람 에너지를 전진 운동으로 변환합니다.", "By balancing sail lift / against keel water resistance, / the vessel converts transverse wind energy / into forward motion."),
             ("This remarkable maritime technique enabled ancient explorers to circumnavigate vast, uncharted oceans.", "이 놀라운 해양 항해술은 고대 탐험가들이 광대하고 미지의 대양을 주해할 수 있게 해주었습니다.", "This remarkable maritime technique / enabled ancient explorers / to circumnavigate vast, uncharted oceans.")
         ],
         [("aerodynamic", "adj.", "공기역학의", "Sleek racing cars feature aerodynamic bodies to minimize air drag."), ("maneuver", "v.", "조종하다, 기동하다", "The captain skillfully maneuvered the ferry into the narrow berth."), ("keel", "n.", "용골 (배 밑바닥의 중심 뼈대)", "The lead ballast in the keel stabilizes the yacht in turbulent seas."), ("transverse", "adj.", "가로의, 횡단하는", "The engineer placed transverse steel beams across the roof structure."), ("circumnavigate", "v.", "주해하다, 세계 일주를 하다", "Magellan's expedition was the first to circumnavigate the globe.")],
         [("동명사 주어", "Sailing directly into the teeth of the wind is... 긴 동명사 주어 구문입니다."), ("prevent A from -ing", "...prevents the boat from slipping sideways... 'A가 ~하는 것을 막다' 구문입니다.")],
         [
             ("How do sailors travel in an upwind direction?", "항해사들은 어떻게 바람을 거슬러 전진하나요?", ["By towing the boat with underwater propeller submarines", "By steering in a zigzag pattern known as tacking", "By paddling backward with wooden oars", "By anchoring permanently in shallow coastal lagoons"], 1, "태킹(tacking)이라 불리는 지그재그 패턴으로 배를 조종한다고 명시했습니다."),
             ("What is the primary function of the underwater keel?", "물속 용골(keel)의 주된 기능은 무엇인가요?", ["Preventing the boat from sliding sideways through the water", "Scooping up fish for the crew to eat during voyages", "Heating the cabin using geothermal warmth", "Reflecting sunlight toward the sails"], 0, "배가 옆으로 미끄러지는 것을 방지한다고 설명했습니다."),
             ("What historic achievement was enabled by this maritime technique?", "이 해양 기술 덕분에 가능해진 역사적 성취는 무엇이었나요?", ["The invention of steam locomotives", "The circumnavigation of vast, uncharted oceans by early explorers", "The complete cessation of global trade", "The construction of underwater highways"], 1, "광대한 미지의 대양을 주해(circumnavigate)할 수 있게 해 주었다고 밝혔습니다.")
         ]),

        ("b-42", "How Glaciers Sculpt Mountain Valleys", "빙하가 산악 계곡을 깎아내는 지형학적 과정", "Earth Science & Geology", "National Geographic",
         "수천 년에 걸쳐 거대한 빙하가 흐르며 V자형 계곡을 U자형 피오르드로 침식시키는 원리를 알아봅니다.",
         [
             ("Glaciers are colossal rivers of compressed ice that move ponderously under their own immense gravitational weight.", "빙하는 자신의 거대한 중력 무게로 인해 육중하게 움직이는 거대한 압축 얼음의 강입니다.", "Glaciers are colossal rivers of compressed ice / that move ponderously / under their own immense gravitational weight."),
             ("As snow accumulates over thousands of winters, lower layers recrystallize into dense, blue glacial ice.", "수천 번의 겨울에 걸쳐 눈이 쌓임에 따라, 아래쪽 층은 조밀한 푸른 빙하 얼음으로 재결정화됩니다.", "As snow accumulates over thousands of winters, / lower layers recrystallize / into dense, blue glacial ice."),
             ("While swift mountain rivers carve sharp, narrow V-shaped gorges, glaciers widen and deepen entire valleys.", "빠른 산골 강물이 날카롭고 좁은 V자형 협곡을 깎아내는 반면, 빙하는 계곡 전체를 넓히고 깊게 만듭니다.", "While swift mountain rivers carve sharp, narrow V-shaped gorges, / glaciers widen and deepen / entire valleys."),
             ("Boulders and jagged rocks frozen into the glacier's base scour the bedrock like giant sheets of sandpaper.", "빙하 바닥에 얼어붙은 바위와 거친 암석들이 거대한 사포처럼 기반암을 문질러 깎아냅니다.", "Boulders and jagged rocks frozen into the glacier's base / scour the bedrock / like giant sheets of sandpaper."),
             ("When the ice eventually retreats during warmer climatic eras, it reveals breathtaking U-shaped valleys.", "빙하가 따뜻한 기후 시대에 마침내 후퇴할 때, 숨 막힐 듯 아름다운 U자형 계곡이 모습을 드러냅니다.", "When the ice eventually retreats / during warmer climatic eras, / it reveals / breathtaking U-shaped valleys."),
             ("These sheer-walled glacial troughs often fill with seawater to become majestic coastal fjords.", "이 깎아지른 절벽의 빙하 골짜기들은 흔히 바닷물로 채워져 웅장한 해안 피오르드가 됩니다.", "These sheer-walled glacial troughs / often fill with seawater / to become majestic coastal fjords.")
         ],
         [("colossal", "adj.", "거대한, 엄청난", "A colossal ice sheet covered much of northern North America."), ("ponderously", "adv.", "육중하게, 무겁게", "The loaded wagon moved ponderously down the steep gravel road."), ("gorge", "n.", "협곡", "A suspension bridge spans the deep river gorge."), ("scour", "v.", "문질러 닦다, 침식하다", "Sandstorms scoured the stone monuments over millennia."), ("trough", "n.", "골짜기, 저점", "A deep ocean trough marks the tectonic subduction zone.")],
         [("접속사 While 대조", "While swift rivers carve V-shaped gorges, glaciers widen... 강과 빙하의 침식 형태 대조입니다."), ("to부정사 결과 용법", "...fill with seawater to become majestic coastal fjords... 채워져서 결국 피오르드가 된다는 결과 표현입니다.")],
         [
             ("What valley shape is characteristically formed by glacial erosion?", "빙하 침식에 의해 특징적으로 형성되는 계곡의 형태는 무엇인가요?", ["Narrow V-shaped canyons", "Wide U-shaped valleys with sheer cliffs", "Perfect spherical underground chambers", "Triangular volcanic craters"], 1, "절벽을 지닌 넓은 U자형 계곡(U-shaped valleys)이라고 설명했습니다."),
             ("How does the base of a glacier grind down bedrock?", "빙하 밑바닥은 어떻게 기반암을 갈아내나요?", ["By pouring boiling hot acid onto limestone strata", "Frozen boulders and rocks scour the rock like giant sandpaper", "By sending electrical lightning into the bedrock", "By vibrating at ultrasonic acoustic frequencies"], 1, "얼어붙은 바위들이 거대한 사포처럼 기반암을 긁어낸다고 서술했습니다."),
             ("What landform is created when flooded glacial troughs meet the ocean?", "침수된 빙하 골짜기가 바다와 만날 때 어떤 지형이 형성되나요?", ["Majestic coastal fjords", "Desert sand dunes", "Subtropical coral atolls", "Artificial concrete shipping canals"], 0, "바닷물이 채워져 웅장한 해안 피오르드(fjords)가 된다고 명시했습니다.")
         ]),

        ("b-43", "The Architecture of Medieval Castles", "중세 유럽 성곽의 방어 건축술", "History & Architecture", "The British Museum",
         "외벽, 해자, 망루, 성채가 결합되어 적의 공성을 격퇴하도록 설계된 중세 요새 건축의 과학을 살펴봅니다.",
         [
             ("Medieval European castles were marvels of defensive military architecture engineered to withstand prolonged sieges.", "중세 유럽의 성은 오랜 포위 공격을 견뎌내도록 설계된 군사 방어 건축의 경이였습니다.", "Medieval European castles were marvels / of defensive military architecture / engineered to withstand prolonged sieges."),
             ("Surrounding the outer perimeter was often a deep moat filled with water or defensive sharpened wooden stakes.", "외부 둘레를 둘러싸고 있는 것은 종종 물이나 방어용 뾰족한 나무말뚝으로 채워진 깊은 해자였습니다.", "Surrounding the outer perimeter / was often a deep moat / filled with water or defensive sharpened wooden stakes."),
             ("Access was controlled by a heavy wooden drawbridge and an iron-grated sliding gate called a portcullis.", "출입은 무거운 나무 도개교와 낙하식 쇠창살 문이라 불리는 미닫이 문에 의해 통제되었습니다.", "Access was controlled / by a heavy wooden drawbridge / and an iron-grated sliding gate called a portcullis."),
             ("High stone curtain walls featured narrow vertical slits called arrow loops, protecting archers from counter-fire.", "높은 석조 커튼월 외벽에는 활 쏘는 틈새라 불리는 좁은 수직 홈이 있어, 궁수를 적의 반격으로부터 보호했습니다.", "High stone curtain walls featured / narrow vertical slits called arrow loops, / protecting archers / from counter-fire."),
             ("At the innermost core stood the keep, a massive stone tower that served as the final secure refuge.", "가장 안쪽 중심부에는 최후의 안전한 피난처 역할을 하는 거대한 석탑인 아성(keep)이 서 있었습니다.", "At the innermost core stood the keep, / a massive stone tower / that served as the final secure refuge."),
             ("Castles served both as imposing military fortresses and as political administrative centers for feudal lords.", "성은 위압적인 군사 요새이자 봉건 영주들의 정치적 행정 중심지로서 기능했습니다.", "Castles served both as imposing military fortresses / and as political administrative centers / for feudal lords.")
         ],
         [("siege", "n.", "포위 공격", "The fortress held out through a six-month winter siege."), ("perimeter", "n.", "둘레, 주변", "Guards patrolled the outer security perimeter day and night."), ("drawbridge", "n.", "도개교 (들어 올리는 다리)", "The castle guards raised the drawbridge at nightfall."), ("archer", "n.", "궁수, 활 쏘는 사람", "Medieval archers trained for years to draw heavy yew longbows."), ("feudal", "adj.", "봉건적인, 봉건 제도의", "Feudal lords commanded knights who owed them military loyalty.")],
         [("도치 구문", "Surrounding the outer perimeter was often a deep moat... 분사구가 문두에 위치해 주어(a deep moat)와 동사가 도치되었습니다."), ("both A and B", "...served both as imposing fortresses and as administrative centers... 상관접속사 구문입니다.")],
         [
             ("What protective architectural feature guarded castle archers while shooting?", "궁수들이 화살을 쏠 때 그들을 보호해 준 성곽 건축 요소는 무엇이었나요?", ["Glass mirrored bulletproof windows", "Narrow vertical slits in stone walls called arrow loops", "Canvas awnings painted with heraldic crests", "Underground drainage sewer pipes"], 1, "외벽에 난 좁은 수직 틈새인 arrow loops라고 설명했습니다."),
             ("What structure served as the ultimate secure refuge inside a castle?", "성 내부에서 최후의 안전한 피난처 역할을 한 구조물은 무엇이었나요?", ["The blacksmith workshop in the stables", "The massive stone tower known as the keep", "The wooden kitchen pantry", "The temporary tent village outside the moat"], 1, "가장 안쪽 중심부에 서 있는 거대한 석탑인 아성(the keep)이라고 명시했습니다."),
             ("What dual purpose did medieval castles fulfill?", "중세 성은 어떤 이중 목적을 수행했나요?", ["Commercial banking hubs and public elementary schools", "Imposing military fortresses and political administrative seats", "Ocean fishing docks and agricultural grain silos", "Botanical flower gardens and theatrical playhouses"], 1, "군사 요새와 봉건 영주의 정치 행정 중심지였다고 결론지었습니다.")
         ]),

        ("b-44", "How Fireflies Produce Cold Light", "반딧불이가 열 없는 빛을 발산하는 생화학", "Nature & Biochemistry", "Smithsonian",
         "에너지 손실 없이 100% 빛으로 전환되는 반딧불이의 루시페린 산화 반응과 짝짓기 신호를 설명합니다.",
         [
             ("On warm summer evenings, meadows twinkle with the enchanting yellow-green flashes of bioluminescent fireflies.", "따뜻한 여름 저녁, 풀밭은 생체발광 반딧불이의 매혹적인 황록색 섬광으로 반짝입니다.", "On warm summer evenings, / meadows twinkle / with the enchanting yellow-green flashes / of bioluminescent fireflies."),
             ("Unlike commercial lightbulbs that waste most of their energy as heat, fireflies generate completely cold light.", "에너지의 대부분을 열로 낭비하는 상업용 백열전구와 달리, 반딧불이는 완전히 열 없는 빛을 생성합니다.", "Unlike commercial lightbulbs / that waste most of their energy as heat, / fireflies generate / completely cold light."),
             ("Inside specialized abdominal lantern organs, a chemical compound called luciferin reacts with oxygen.", "특수화된 복부의 발광기 기관 내부에서, 루시페린이라 불리는 화합물이 산소와 반응합니다.", "Inside specialized abdominal lantern organs, / a chemical compound called luciferin / reacts with oxygen."),
             ("An enzyme named luciferase accelerates this reaction, converting nearly one hundred percent of the chemical energy into visible light.", "루시페라아제라는 효소가 이 반응을 가속하여, 화학 에너지의 거의 100%를 가시광선으로 변환합니다.", "An enzyme named luciferase accelerates this reaction, / converting nearly one hundred percent / of the chemical energy / into visible light."),
             ("Fireflies flash in distinctive, rhythmic sequences to signal courtship interest to prospective mates.", "반딧불이는 장래의 짝에게 구애의 관심을 신호하기 위해 독특하고 리드미컬한 순서로 빛을 깜빡입니다.", "Fireflies flash in distinctive, rhythmic sequences / to signal courtship interest / to prospective mates."),
             ("Each specific firefly species uses its own unique rhythm and duration to avoid romantic confusion.", "각각의 고유한 반딧불이 종은 짝짓기의 혼란을 피하기 위해 고유한 리듬과 지속시간을 사용합니다.", "Each specific firefly species / uses its own unique rhythm and duration / to avoid romantic confusion.")
         ],
         [("bioluminescent", "adj.", "생체발광의", "Deep-sea anglerfish carry bioluminescent lures on their foreheads."), ("abdominal", "adj.", "복부의, 배의", "Insects possess head, thorax, and abdominal body segments."), ("accelerate", "v.", "가속하다, 촉진하다", "Catalysts accelerate chemical reactions without being consumed."), ("prospective", "adj.", "장래의, 유망한", "The university welcomed prospective students at the campus open house."), ("duration", "n.", "지속 시간, 기간", "The total duration of the solar eclipse was four minutes.")],
         [("분사구문 converting", "...accelerates this reaction, converting nearly 100 percent of... 결과를 설명하는 능동 분사구문입니다."), ("부정사 부사적 용법 to avoid", "...uses its own unique rhythm to avoid... 목적을 나타내는 to부정사입니다.")],
         [
             ("What distinguishes firefly bioluminescence from traditional lightbulbs?", "반딧불이의 생체발광은 전통적인 백열전구와 어떻게 다른가요?", ["It generates completely cold light with almost no heat waste.", "It requires connection to electrical wall outlets.", "It illuminates only ultraviolet radiation invisible to eyes.", "It consumes solid timber logs inside the abdomen."], 0, "열 손실이 거의 없는 완전한 냉광(cold light)을 만든다고 설명했습니다."),
             ("What two biological components drive the light reaction inside fireflies?", "반딧불이 내부에서 발광 반응을 일으키는 두 가지 생물학적 성분은 무엇인가요?", ["Luciferin and the enzyme luciferase", "Chlorophyll and kerosene oil", "Sodium chloride and sulfur dust", "Liquid nitrogen and liquid carbon"], 0, "루시페린(luciferin) 화합물과 루시페라아제(luciferase) 효소라고 명시했습니다."),
             ("Why do different firefly species employ distinct flash rhythms?", "서로 다른 반딧불이 종들이 왜 제각기 다른 깜빡임 리듬을 사용하나요?", ["To scare away passing automobiles", "To signal courtship interest and avoid species confusion", "To warm their wings before flying in thunderstorms", "To communicate with subterranean mole crickets"], 1, "구애 관심을 전달하고 종 간의 혼란을 방지하기 위해서라고 밝혔습니다.")
         ]),

        ("b-45", "Why the Ocean Appears Blue", "바다가 푸른빛을 띠는 광학적 이유", "Oceanography & Physics", "NOAA",
         "바닷물이 하늘을 반사해서 파란 것이 아니라, 물 분자가 붉은 파장을 흡수하고 푸른 파장을 산란하기 때문임을 설명합니다.",
         [
             ("A popular misconception suggests that the ocean appears blue simply by reflecting the azure daytime sky.", "널리 퍼진 오해는 바다가 단순히 한낮의 푸른 하늘을 반사함으로써 파랗게 보인다고 여깁니다.", "A popular misconception suggests / that the ocean appears blue / simply by reflecting the azure daytime sky."),
             ("While surface reflection does contribute minor color, the true explanation lies in molecular physics.", "표면 반사가 사소한 색채에 기여하기는 하지만, 진정한 설명은 분자 물리학에 있습니다.", "While surface reflection does contribute minor color, / the true explanation lies / in molecular physics."),
             ("Pure water molecules selectively absorb long wavelengths of light—specifically red, orange, and yellow.", "순수한 물 분자는 빛의 긴 파장, 구체적으로 빨간색, 주황색, 노란색을 선택적으로 흡수합니다.", "Pure water molecules selectively absorb / long wavelengths of light / —specifically red, orange, and yellow."),
             ("As sunlight penetrates deeper into the water column, these warm colors are rapidly filtered out into darkness.", "햇빛이 수역 깊숙이 침투함에 따라, 이러한 따뜻한 색상들은 어둠 속으로 빠르게 걸러져 사라집니다.", "As sunlight penetrates deeper into the water column, / these warm colors are rapidly filtered out / into darkness."),
             ("Shorter blue wavelengths, by contrast, are much less easily absorbed and scatter off water molecules.", "대조적으로 파장이 짧은 파란빛은 훨씬 덜 흡수되며 물 분자에 부딪혀 산란됩니다.", "Shorter blue wavelengths, by contrast, / are much less easily absorbed / and scatter off water molecules."),
             ("This scattered blue light bounces back upward to human eyes, making open oceans look intensely sapphire.", "이렇게 산란된 파란빛이 인간의 눈으로 다시 튕겨 올라오면서, 망망대해가 짙은 사파이어빛으로 보이게 됩니다.", "This scattered blue light bounces back upward / to human eyes, / making open oceans look intensely sapphire.")
         ],
         [("misconception", "n.", "오해, 그릇된 생각", "That bats are completely blind is a widespread misconception."), ("azure", "adj.", "하늘빛의, 푸른", "The tropical lagoon shimmered in brilliant azure tones."), ("selectively", "adv.", "선택적으로", "The semipermeable membrane selectively filters sodium ions."), ("penetrate", "v.", "침투하다, 뚫고 들어가다", "Sunlight cannot penetrate depths beyond two hundred meters."), ("sapphire", "n./adj.", "사파이어(빛의), 짙은 청색", "The clear mountain lake possessed a deep sapphire glow.")],
         [("동사 emphasize does", "While surface reflection does contribute minor color... 일반동사 contribute를 강조하는 조동사 does입니다."), ("사역동사 make", "...making open oceans look intensely sapphire... make + 목적어 + 동사원형 구조입니다.")],
         [
             ("What is the primary scientific reason oceans appear blue?", "바다가 파랗게 보이는 가장 핵심적인 과학적 원인은 무엇인가요?", ["Water molecules absorb long red wavelengths and scatter shorter blue light.", "The ocean floor is paved with blue turquoise gemstones.", "Whales release natural blue ink dyes into the water.", "Salt crystals turn water bright blue under pressure."], 0, "물 분자가 긴 붉은 파장을 흡수하고 짧은 푸른빛을 산란시키기 때문입니다."),
             ("What misconception about ocean color is corrected in the text?", "본문에서 바로잡고 있는 바다 색깔에 대한 오해는 무엇인가요?", ["That oceans are actually dyed by sunken ship paints", "That the ocean is blue only because it reflects the sky", "That water is made of colored chemical pigments", "That cold temperatures produce blue ocean ice"], 1, "단순히 하늘빛을 반사해서 파랗다는 통념이 오해라고 밝혔습니다."),
             ("Which light wavelengths are absorbed first as sunlight penetrates water?", "햇빛이 물속으로 침투할 때 어떤 파장의 빛이 가장 먼저 흡수되나요?", ["Short blue and violet wavelengths", "Long warm wavelengths such as red and orange", "Artificial neon green rays", "Cosmic gamma radiation waves"], 1, "빨간색, 주황색과 같은 긴 파장의 빛이 먼저 걸러진다고 설명했습니다.")
         ]),

        ("b-46", "The Social Structure of Meerkat Mobs", "미어캣 무리의 사회적 협력과 보초 시스템", "Zoology & Animal Behavior", "BBC Wildlife",
         "사막의 가혹한 환경에서 보초를 서고 새끼를 공동 양육하며 생존하는 미어캣의 고도 협동 사회를 다룹니다.",
         [
             ("Meerkats are gregarious African mongooses that dwell in cooperative family groups known as mobs.", "미어캣은 몹(mob)이라 불리는 협동 가족 집단을 이루어 살아가는 사교적인 아프리카 몽구스입니다.", "Meerkats are gregarious African mongooses / that dwell in cooperative family groups / known as mobs."),
             ("Inhabiting the harsh Kalahari Desert, a mob typically contains twenty to thirty bonded individuals.", "혹독한 칼라하리사막에 서식하며, 한 무리는 전형적으로 20~30마리의 유대감 있는 개체들을 포함합니다.", "Inhabiting the harsh Kalahari Desert, / a mob typically contains / twenty to thirty bonded individuals."),
             ("While the majority of the pack forages for scorpions and beetles, one meerkat acts as sentinel.", "무리의 대다수가 전갈과 딱정벌레를 찾아 먹이 활동을 하는 동안, 한 마리의 미어캣이 보초병 역할을 합니다.", "While the majority of the pack forages for scorpions and beetles, / one meerkat acts as sentinel."),
             ("Perched high atop a termite mound, the sentinel surveys the open savanna skies for circling hawks.", "흰개미 둔덕 꼭대기 높은 곳에 자리 잡고, 보초는 선회하는 매가 있는지 탁 트인 사바나 하늘을 감시합니다.", "Perched high atop a termite mound, / the sentinel surveys the open savanna skies / for circling hawks."),
             ("If danger approaches, the lookout emits distinct sharp barking alarms, prompting the troop to dart underground.", "만약 위험이 접근하면, 망보는 미어캣은 날카로운 짖는 경보음을 내어 무리가 재빨리 지하로 피신하게 합니다.", "If danger approaches, / the lookout emits distinct sharp barking alarms, / prompting the troop / to dart underground."),
             ("Adults also take turns babysitting newborn pups, demonstrating exemplary mammalian cooperation.", "성체들은 갓 태어난 새끼들을 교대로 돌보며 모범적인 포유류의 협력을 보여줍니다.", "Adults also take turns babysitting newborn pups, / demonstrating exemplary mammalian cooperation.")
         ],
         [("gregarious", "adj.", "사교적인, 무리 지어 사는", "Gregarious dolphins hunt schools of fish in coordinated pods."), ("sentinel", "n.", "보초, 파수꾼", "The soldier stood as a watchful sentinel at the outpost gate."), ("forage", "v.", "먹이를 찾아다니다", "Wild deer forage for tender shoots in early spring."), ("prompt", "v.", "촉발하다, 유도하다", "The loud alarm prompted residents to evacuate immediately."), ("exemplary", "adj.", "모범적인, 본보기가 되는", "Her exemplary dedication earned her international recognition.")],
         [("과거분사 수동 분사구문", "Perched high atop a termite mound, the sentinel surveys... 위치를 나타내는 분사구문입니다."), ("take turns -ing", "Adults also take turns babysitting newborn pups... '교대로 ~하다' 표현입니다.")],
         [
             ("What is a cooperative group of meerkats called?", "협동 생활을 하는 미어캣 무리를 무엇이라 부르나요?", ["A herd", "A mob", "A swarm", "A flock"], 1, "몹(a mob)으로 알려져 있다고 명시했습니다."),
             ("What is the primary responsibility of the sentinel meerkat?", "보초병 미어캣의 주된 책임은 무엇인가요?", ["Digging burrows for the entire colony alone", "Watching the sky and savanna to warn against predators", "Gathering all food for the infant pups", "Hunting desert scorpions for dinner"], 1, "포식자를 감시하고 경보를 울려 무리를 지키는 것이라 설명했습니다."),
             ("How do adult meerkats care for newborn pups?", "성체 미어캣들은 신생아 새끼들을 어떻게 돌보나요?", ["By abandoning them immediately in the sand dunes", "By taking turns babysitting inside the secure underground burrows", "By carrying them into tree branches during rainstorms", "By having them hunt adult venomous snakes on day one"], 1, "성체들이 교대로 새끼를 돌보는 탁아(babysitting)를 수행한다고 밝혔습니다.")
         ]),

        ("b-47", "How Windmills Reclaimed Dutch Land", "풍차가 바다를 메워 만든 네덜란드의 간척 역사", "History & Technology", "Britannica",
         "해수면보다 낮은 저지대 네덜란드에서 풍차를 연결해 바닷물을 퍼내어 비옥한 폴더(간척지)를 일군 과정을 설명합니다.",
         [
             ("Much of the low-lying terrain in the Netherlands lies perilously below the level of the North Sea.", "네덜란드의 저지대 지형 대부분은 북해의 해수면보다 위태롭게 낮게 위치해 있습니다.", "Much of the low-lying terrain in the Netherlands / lies perilously / below the level of the North Sea."),
             ("For centuries, the Dutch fought devastating oceanic floods by constructing extensive barrier dykes.", "수세기 동안 네덜란드인들은 광범위한 방조제 제방을 건설함으로써 파괴적인 해양 홍수와 싸웠습니다.", "For centuries, / the Dutch fought devastating oceanic floods / by constructing extensive barrier dykes."),
             ("To transform muddy coastal marshes into productive agricultural soils, they pioneered drainage windmills.", "진흙투성이 해안 습지를 생산적인 농경지로 탈바꿈시키기 위해, 그들은 배수 풍차를 개척했습니다.", "To transform muddy coastal marshes into productive agricultural soils, / they pioneered drainage windmills."),
             ("Windmill blades captured North Sea breezes, turning internal wooden cogwheels that drove giant Archimedean screws.", "풍차 날개는 북해의 미풍을 포착하여 거대한 아르키메데스 나선 펌프를 구동하는 내부 나무 톱니바퀴를 돌렸습니다.", "Windmill blades captured North Sea breezes, / turning internal wooden cogwheels / that drove giant Archimedean screws."),
             ("These screw pumps lifted millions of liters of stagnant water over dykes into drainage canals.", "이 나선 펌프들은 수백만 리터의 고인 물을 제방 너머 배수 운하로 퍼 올렸습니다.", "These screw pumps lifted / millions of liters of stagnant water / over dykes into drainage canals."),
             ("The reclaimed dry lands, called polders, became some of Europe's most fertile dairy pastures.", "폴더(polder)라 불리는 간척된 건조 지대는 유럽에서 가장 비옥한 낙농 목초지가 되었습니다.", "The reclaimed dry lands, called polders, / became some of Europe's / most fertile dairy pastures.")
         ],
         [("perilously", "adv.", "위태롭게, 위험하게", "The hikers climbed perilously close to the cliff edge."), ("dyke", "n.", "제방, 둑", "Earthen dykes held back the rising river waters during the storm."), ("cogwheel", "n.", "톱니바퀴", "Intricate bronze cogwheels powered the clockwork mechanism."), ("stagnant", "adj.", "고여 있는, 정체된", "Mosquitoes breed rapidly in warm stagnant pond water."), ("reclaim", "v.", "간척하다, 되찾다", "Engineers reclaimed coastal marshes to expand port facilities.")],
         [("to부정사 목적 부사구", "To transform muddy marshes..., they pioneered... 목적을 나타내는 to부정사입니다."), ("관계대명사 주격", "...turning internal wooden cogwheels that drove giant screws... 선행사 cogwheels를 수식합니다.")],
         [
             ("What geographical challenge historically threatened the Netherlands?", "역사적으로 어떤 지리적 도전이 네덜란드를 위협했나요?", ["Living on terrain lying perilously below sea level", "Severe active volcanic eruptions every summer", "Extremely hot tropical droughts drying up all crops", "Continuous avalanche slides down granite mountains"], 0, "국토의 많은 부분이 해수면 아래에 위치해 바다 홍수의 위협을 받았다고 설명했습니다."),
             ("What mechanical device inside windmills pumped water over the dykes?", "제방 너머로 물을 퍼 올리기 위해 풍차 내부에 사용된 기계 장치는 무엇이었나요?", ["Diesel steam boilers", "Archimedean screw pumps driven by cogwheels", "Manual copper buckets carried by oxen", "Nuclear vacuum suction hoses"], 1, "톱니바퀴로 구동되는 아르키메데스 나선 펌프(Archimedean screws)라고 명시했습니다."),
             ("What are the reclaimed agricultural dry lands in the Netherlands called?", "네덜란드에서 간척된 건조 농경지를 무엇이라 부르나요?", ["Polders", "Moraines", "Atolls", "Gorges"], 0, "폴더(polders)라 불린다고 명시했습니다.")
         ]),

        ("b-48", "The Science of Musical Harmony and Chords", "음악적 화음과 배음 공명의 음향학", "Music Theory & Acoustics", "Oxford Music Online",
         "여러 음이 동시에 울릴 때 아름답게 어우러지는 화음이 정수비 주파수와 음향 공명에서 비롯됨을 설명합니다.",
         [
             ("When two musical notes are played simultaneously, human ears perceive either pleasing harmony or harsh dissonance.", "두 음악적 음이 동시에 연주될 때, 인간의 귀는 유쾌한 화음이나 거친 불협화음 중 하나를 인식합니다.", "When two musical notes are played simultaneously, / human ears perceive / either pleasing harmony / or harsh dissonance."),
             ("This acoustic phenomenon depends on mathematical ratios between the vibrations of the sound waves.", "이 음향학적 현상은 음파 진동 간의 수학적 비율에 달려 있습니다.", "This acoustic phenomenon depends / on mathematical ratios / between the vibrations of the sound waves."),
             ("Ancient Greek philosopher Pythagoras discovered that strings whose lengths form simple whole-number ratios sound harmonious.", "고대 그리스 철학자 피타고라스는 현의 길이가 단순한 정수비를 이루는 현들이 조화롭게 들린다는 것을 발견했습니다.", "Ancient Greek philosopher Pythagoras discovered / that strings whose lengths form simple whole-number ratios / sound harmonious."),
             ("For instance, an octave corresponds to a clean two-to-one frequency ratio, vibrating in perfect periodic symmetry.", "예를 들어, 옥타브는 깔끔한 2대 1 주파수 비율에 해당하여 완벽한 주기적 대칭으로 진동합니다.", "For instance, / an octave corresponds / to a clean two-to-one frequency ratio, / vibrating in perfect periodic symmetry."),
             ("When three complementary notes are combined according to mathematical intervals, they create a resonant triad chord.", "세 개의 상호 보완적인 음들이 수학적 음정에 따라 결합할 때, 그들은 공명하는 3화음 코드를 만듭니다.", "When three complementary notes are combined / according to mathematical intervals, / they create a resonant triad chord."),
             ("Harmony bridges empirical physics and human emotional expression through the universal language of acoustic vibration.", "화음은 음향 진동이라는 보편적인 언어를 통해 실증 물리학과 인간의 감정적 표현을 연결해 줍니다.", "Harmony bridges empirical physics / and human emotional expression / through the universal language of acoustic vibration.")
         ],
         [("simultaneously", "adv.", "동시에", "The two runners crossed the finish line simultaneously."), ("dissonance", "n.", "불협화음, 부조화", "Clashing musical notes created dramatic dissonance in the symphony."), ("harmonious", "adj.", "조화로운, 듣기 좋은", "The vocal ensemble produced a wonderfully harmonious blend."), ("periodic", "adj.", "주기적인", "Planetary orbits exhibit precise periodic motions."), ("resonant", "adj.", "공명하는, 깊이 울리는", "The wooden cello produced a rich, resonant tone in the hall.")],
         [("either A or B", "...human ears perceive either pleasing harmony or harsh dissonance... 양자택일 구문입니다."), ("소유격 관계대명사 whose", "...discovered that strings whose lengths form simple ratios... 선행사 strings를 수식합니다.")],
         [
             ("What determines whether two musical notes sound harmonious together?", "두 음이 함께 조화롭게 들리는지 여부를 결정하는 것은 무엇인가요?", ["The color of paint on the piano exterior", "Mathematical frequency ratios between sound wave vibrations", "The room temperature of the concert auditorium", "The thickness of the musician's clothing"], 1, "음파 진동 간의 수학적 주파수 비율이라고 설명했습니다."),
             ("What mathematical ratio defines an acoustic musical octave?", "음향학적 옥타브를 정의하는 수학적 비율은 무엇인가요?", ["A clean two-to-one ratio", "A seventeen-to-ninety ratio", "A random fractional decimal", "A zero-to-zero ratio"], 0, "깔끔한 2대 1 비율(clean two-to-one ratio)이라고 명시했습니다."),
             ("Who historically discovered the connection between integer string ratios and harmony?", "현의 정수비와 화음 간의 연관성을 역사적으로 처음 발견한 학자는 누구인가요?", ["Isaac Newton", "Pythagoras", "Galileo Galilei", "Aristotle"], 1, "고대 그리스 철학자 피타고라스(Pythagoras)라고 밝혔습니다.")
         ]),

        ("b-49", "The Anatomy of the Human Brainstem", "뇌간의 해부학과 생명 유지 자율 신경계", "Neuroanatomy & Medicine", "Harvard Health",
         "호흡, 심장 박동, 혈압 등 의식하지 않아도 생명을 유지시키는 뇌간(숨골)의 구조와 역할을 알아봅니다.",
         [
             ("Located at the base of the skull, the brainstem connects the cerebral cortex to the spinal cord.", "두개골 기저부에 위치한 뇌간은 대뇌피질을 척수와 연결해 줍니다.", "Located at the base of the skull, / the brainstem connects the cerebral cortex / to the spinal cord."),
             ("Composed of three distinct sections—the midbrain, pons, and medulla oblongata—it oversees vital autonomic functions.", "중뇌, 뇌교, 연수라는 세 개의 뚜렷한 구획으로 구성되어, 이는 필수적인 자율 신경 기능을 관장합니다.", "Composed of three distinct sections / —the midbrain, pons, and medulla oblongata— / it oversees vital autonomic functions."),
             ("While higher brain centers manage conscious thinking and voluntary movement, the brainstem operates completely involuntarily.", "상위 뇌 중추가 의식적 사고와 자발적 운동을 관리하는 반면, 뇌간은 완전히 불수의적으로 작동합니다.", "While higher brain centers manage conscious thinking / and voluntary movement, / the brainstem operates / completely involuntarily."),
             ("Specialized neural clusters constantly regulate cardiac rhythms, respiratory rate, digestion, and systemic blood pressure.", "특화된 신경 세포군이 심장 리듬, 호흡수, 소화, 전신 혈압을 끊임없이 조절합니다.", "Specialized neural clusters constantly regulate / cardiac rhythms, respiratory rate, / digestion, and systemic blood pressure."),
             ("It also routes critical reflexes including swallowing, coughing, sneezing, and pupil pupillary adjustments.", "그것은 또한 삼키기, 기침, 재채기, 동공 조절을 포함한 결정적인 반사 작용을 중계합니다.", "It also routes critical reflexes / including swallowing, coughing, / sneezing, and pupil pupillary adjustments."),
             ("Without the uninterrupted vigilance of the brainstem, survival would cease within mere minutes.", "뇌간의 중단 없는 경계 활동이 없다면, 생명은 불과 몇 분 만에 멈추게 될 것입니다.", "Without the uninterrupted vigilance of the brainstem, / survival would cease / within mere minutes.")
         ],
         [("autonomic", "adj.", "자율 신경의, 자율적인", "The autonomic nervous system regulates heart rate without conscious effort."), ("involuntary", "adj.", "불수의적인, 무의식적인", "Blinking in bright sunlight is an involuntary physical reflex."), ("cardiac", "adj.", "심장의", "Regular jogging supports long-term cardiac health."), ("respiratory", "adj.", "호흡의", "Lungs are primary organs of the mammalian respiratory system."), ("vigilance", "n.", "경계, 조심", "Air traffic controllers must maintain intense visual vigilance.")],
         [("과거분사 수동 분사구문", "Located at the base of the skull, the brainstem connects... 위치를 설명하는 분사구문입니다."), ("가정법 Without", "Without the uninterrupted vigilance..., survival would cease... '~이 없다면 ~할 것이다'라는 가정법 구문입니다.")],
         [
             ("What three primary anatomical structures comprise the brainstem?", "뇌간을 구성하는 세 가지 주요 해부학적 구조는 무엇인가요?", ["The midbrain, pons, and medulla oblongata", "The frontal lobe, occipital lobe, and cornea", "The femur, tibia, and patella bones", "The thyroid, pancreas, and adrenal glands"], 0, "중뇌(midbrain), 뇌교(pons), 연수(medulla oblongata)라고 설명했습니다."),
             ("How does brainstem function differ from the cerebral cortex?", "뇌간의 기능은 대뇌피질과 어떻게 다른가요?", ["It handles voluntary athletic sports while the cortex controls sleep.", "It regulates vital autonomic functions involuntarily without conscious effort.", "It produces digestive stomach acids rather than neural electrical pulses.", "It operates only when individuals are speaking foreign languages."], 1, "의식적 노력 없이 불수의적으로 생명 유지 자율 신경 기능을 조절한다고 밝혔습니다."),
             ("Which physiological reflex is directly mediated through the brainstem?", "어떤 생리적 반사 작용이 뇌간을 통해 직접 매개되나요?", ["Swallowing and coughing reflexes", "Synthesizing bone marrow blood platelets", "Growing fingernails during adolescence", "Changing skin pigment colors in cold water"], 0, "삼키기, 기침, 재채기 등의 반사가 중계된다고 명시했습니다.")
         ]),

        ("b-50", "The Origin of Ancient Olympic Games", "고대 올림픽 제전의 기원과 평화 휴전", "Ancient History", "Britannica",
         "기원전 776년 고대 그리스 올림피아에서 제우스 신을 기리며 전쟁을 멈추고 거행되었던 올림픽의 기원을 다룹니다.",
         [
             ("The ancient Olympic Games originated in 776 BCE in the sacred sanctuary of Olympia, Greece.", "고대 올림픽 경기는 기원전 776년 그리스 올림피아의 신성한 성역에서 시작되었습니다.", "The ancient Olympic Games originated / in 776 BCE / in the sacred sanctuary of Olympia, Greece."),
             ("Held every four years in honor of Zeus, the athletic festivals brought together fiercely rival city-states.", "제우스 신을 기려 4년마다 열린 이 체육 축제는 격렬하게 대립하던 도시 국가들을 하나로 모았습니다.", "Held every four years in honor of Zeus, / the athletic festivals brought together / fiercely rival city-states."),
             ("During the festival period, a sacred truce called the ekecheiria was proclaimed across all Greek territories.", "축제 기간 동안, '에케케이리아'라 불리는 신성한 휴전이 모든 그리스 영토 전역에 선포되었습니다.", "During the festival period, / a sacred truce called the ekecheiria / was proclaimed / across all Greek territories."),
             ("All ongoing wars and military conflicts were suspended so that athletes and spectators could travel safely.", "모든 진행 중인 전쟁과 군사적 갈등은 운동선수들과 관람객들이 안전하게 이동할 수 있도록 일시 중단되었습니다.", "All ongoing wars and military conflicts were suspended / so that athletes and spectators / could travel safely."),
             ("Athletes competed in footraces, wrestling, javelin, and chariot races, receiving olive leaf wreaths as crowning honors.", "선수들은 단거리 달리기, 레슬링, 창던지기, 전차 경주에서 경쟁하며, 최고의 영예로 올리브 잎 화관을 받았습니다.", "Athletes competed in footraces, wrestling, javelin, / and chariot races, / receiving olive leaf wreaths / as crowning honors."),
             ("The games celebrated physical excellence and cultural unity long before modern international sporting federations existed.", "이 경기들은 현대의 국제 스포츠 연맹이 존재하기 훨씬 전에 신체적 탁월성과 문화적 통합을 찬양했습니다.", "The games celebrated physical excellence / and cultural unity / long before modern international sporting federations existed.")
         ],
         [("sanctuary", "n.", "성역, 피난처", "Ancient temples provided safe sanctuary to travelers."), ("truce", "n.", "휴전, 정전", "Both armies agreed to a temporary holiday truce."), ("proclaim", "v.", "선언하다, 공포하다", "The king proclaimed a national festival across the realm."), ("suspend", "v.", "일시 중단하다, 유예하다", "School classes were suspended due to the heavy blizzard."), ("wreath", "n.", "화관, 화환", "Victorious champions were crowned with laurel wreaths.")],
         [("과거분사 수동 분사구문", "Held every four years in honor of Zeus, the festivals brought... 축제의 개최를 설명하는 분사구문입니다."), ("so that 목적 절", "...were suspended so that athletes could travel safely... 안전한 이동을 위한 목적 절입니다.")],
         [
             ("In which year did the ancient Olympic Games officially begin?", "고대 올림픽 경기는 공식적으로 몇 년도에 시작되었나요?", ["776 BCE", "1988 CE", "500 CE", "1200 BCE"], 0, "기원전 776년(776 BCE)이라고 명시했습니다."),
             ("What was the purpose of the sacred truce known as ekecheiria?", "'에케케이리아'로 알려진 신성한 휴전의 목적은 무엇이었나요?", ["Suspending military conflicts so athletes and spectators could travel safely", "Abolishing all athletic training permanently across Greece", "Enforcing mandatory taxes on foreign merchant vessels", "Drafting all competitive runners into the navy"], 0, "선수와 관람객이 안전하게 이동할 수 있도록 전쟁을 중단하는 것이라고 설명했습니다."),
             ("What prize was awarded to victorious Olympic athletes?", "승리한 올림픽 운동선수들에게 어떤 상이 수여되었나요?", ["Gold bullion bars", "Crowns made of wild olive leaves", "Horses coated in silver armor", "Free ocean voyages to Egypt"], 1, "올리브 잎 화관(olive leaf wreaths)을 최고의 영예로 받았다고 명시했습니다.")
         ])
    ]
    return b_extra

if __name__ == "__main__":
    print(f"Generated extra beginner passages for 150 target: {len(get_expansion_150())}")
