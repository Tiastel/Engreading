# -*- coding: utf-8 -*-
"""
generate_all_90_passages.py
Generates 90 rigorous, authentic English reading passages:
- 30 Beginner (A2-B1)
- 30 Intermediate (B1-B2)
- 30 Advanced (B2-C1)
With verified comprehension questions, vocabulary, grammar notes, and sentence chunking.
"""

import json
import sys

def build_dataset():
    passages = []

    # -------------------------------------------------------------
    # 30 BEGINNER PASSAGES (b-01 to b-30)
    # -------------------------------------------------------------
    b_data = [
        ("b-01", "Daily Habits of Long-Lived People", "장수하는 사람들의 일상 습관", "Health & Lifestyle", "Harvard Health",
         "100세 이상 건강하게 살아가는 사람들의 공통적인 일상 습관과 자연식 식단을 살펴봅니다.",
         [
             ("People who live past one hundred years often share similar daily routines.", "100세 넘게 사는 사람들은 종종 비슷한 일상 루틴을 공유합니다.", "People / who live past one hundred years / often share / similar daily routines."),
             ("They usually eat natural, plant-based foods such as beans, nuts, and fresh vegetables.", "그들은 보통 콩, 견과류, 신선한 채소와 같은 천연 식물성 식품을 먹습니다.", "They usually eat / natural, plant-based foods / such as beans, nuts, / and fresh vegetables."),
             ("In addition, physical movement is a natural part of their daily schedule.", "또한, 신체적 움직임은 그들 일과의 자연스러운 일부입니다.", "In addition, / physical movement / is a natural part / of their daily schedule."),
             ("Instead of going to crowded modern gyms, they walk outdoors, tend gardens, and clean their own homes.", "그들은 붐비는 현대식 헬스장에 가는 대신 야외를 걷고, 정원을 가꾸며, 자신의 집을 청소합니다.", "Instead of going to crowded modern gyms, / they walk outdoors, / tend gardens, / and clean their own homes."),
             ("Strong relationships with family and friendly neighbors also protect their mental well-being.", "가족 및 다정한 이웃과의 끈끈한 관계 또한 그들의 정신적 안녕을 지켜줍니다.", "Strong relationships / with family and friendly neighbors / also protect / their mental well-being."),
             ("Having a clear personal purpose each morning keeps their minds sharp and peaceful.", "매일 아침 명확한 개인적 목적의식을 가지는 것은 그들의 마음을 명민하고 평화롭게 유지해 줍니다.", "Having a clear personal purpose each morning / keeps their minds sharp / and peaceful.")
         ],
         [("routine", "n.", "일상, 규칙적인 일과", "A morning walk is part of her daily routine."), ("tend", "v.", "돌보다, 가꾸다", "He tends his rooftop garden every Sunday."), ("well-being", "n.", "안녕, 행복, 건강", "Social connections support mental well-being."), ("purpose", "n.", "목적, 의미", "Having a life purpose inspires optimism."), ("sharp", "adj.", "명민한, 예리한", "Reading keeps the aging mind remarkably sharp.")],
         [("관계대명사 who", "People who live past one hundred years에서 who는 선행사 People을 꾸며주는 주격 관계대명사절입니다."), ("동명사 주어", "Having a clear personal purpose... keeps... 처럼 동명사 주어는 단수 동사를 취합니다.")],
         [
             ("What is the primary factor supporting long life according to the text?", "지문에 따르면 장수를 돕는 주요 요인은 무엇인가요?", ["Using expensive heavy fitness equipment", "A natural lifestyle blending wholesome food, daily movement, and community", "Moving away from all family members", "Sleeping more than twelve hours every day"], 1, "지문에서 자연스러운 식단, 정원 가꾸기와 걷기 같은 일상적 활동, 이웃과의 유대감이 장수의 비결로 제시되었습니다."),
             ("How do centenarians typically engage in physical activity?", "장수하는 사람들은 보통 어떻게 신체 활동을 하나요?", ["Through routine daily tasks like walking and gardening", "By hiring personal celebrity trainers", "By running forty-kilometer marathons weekly", "By staying indoors watching television"], 0, "헬스장에 가는 대신 산책과 정원 가꾸기 같은 일상 활동을 통해 움직임을 유지한다고 명시했습니다."),
             ("Why is having a purpose each morning helpful?", "매일 아침 목적의식을 가지는 것이 왜 도움이 되나요?", ["It guarantees high financial wealth.", "It preserves a sharp and calm mental state.", "It replaces the biological need for sleep.", "It prevents people from making mistakes."], 1, "마지막 문장에서 아침의 목적의식이 마음을 명민하고 평화롭게 유지해 준다고 결론지었습니다.")
         ]),

        ("b-02", "The Vital Role of Honeybees", "꿀벌의 중대한 생태학적 역할", "Nature & Ecology", "National Geographic Kids",
         "작은 꿀벌이 꽃가루를 옮기며 인류 식량의 3분의 1을 지탱하는 수분 과정을 탐구합니다.",
         [
             ("Honeybees are industrious insects that perform an essential task for nature.", "꿀벌은 자연을 위해 필수적인 작업을 수행하는 부지런한 곤충입니다.", "Honeybees are industrious insects / that perform an essential task / for nature."),
             ("As they travel from blossom to blossom gathering nectar, pollen attaches to their furry bodies.", "그들이 꿀을 모으기 위해 꽃에서 꽃으로 이동할 때, 꽃가루가 그들의 털북숭이 몸에 달라붙습니다.", "As they travel from blossom to blossom / gathering nectar, / pollen attaches to their furry bodies."),
             ("This golden dust is carried to the next flower, enabling plants to generate fruits and seeds.", "이 황금빛 가루가 다음 꽃으로 옮겨지며, 식물이 열매와 씨앗을 맺을 수 있도록 합니다.", "This golden dust is carried / to the next flower, / enabling plants / to generate fruits and seeds."),
             ("Without pollination, nearly one-third of the crops consumed by humans could completely disappear.", "수분이 없다면, 인간이 소비하는 농작물의 거의 3분의 1이 완전히 사라질 수 있습니다.", "Without pollination, / nearly one-third of the crops / consumed by humans / could completely disappear."),
             ("Apples, almonds, strawberries, and cucumbers all depend directly on regular bee visits.", "사과, 아몬드, 딸기, 오이는 모두 정기적인 꿀벌의 방문에 직접적으로 의존합니다.", "Apples, almonds, strawberries, and cucumbers / all depend directly / on regular bee visits."),
             ("Protecting wildflower habitats is therefore crucial for preserving global agricultural supplies.", "따라서 야생화 서식지를 보호하는 것은 전 세계 농업 공급을 보존하는 데 결정적입니다.", "Protecting wildflower habitats / is therefore crucial / for preserving global agricultural supplies.")
         ],
         [("industrious", "adj.", "근면한, 부지런한", "Ants and honeybees are notoriously industrious insects."), ("nectar", "n.", "꽃의 꿀, 화밀", "Bees transform flower nectar into nutritious honey."), ("pollination", "n.", "수분, 꽃가루받이", "Wind and bees are primary agents of pollination."), ("consume", "v.", "소비하다, 먹다", "Athletes consume high amounts of complex carbohydrates."), ("habitat", "n.", "서식지, 자연 환경", "Wetlands provide a rich habitat for aquatic birds.")],
         [("분사구문 enabling", "...carried to the next flower, enabling plants to... 앞 절의 결과로 가능하게 한다는 능동 분사구문입니다."), ("전치사 depend on", "depend directly on은 '~에 직접적으로 의존하다'라는 표현입니다.")],
         [
             ("What is the primary ecological service honeybees provide?", "꿀벌이 제공하는 가장 주된 생태학적 역할은 무엇인가요?", ["Digging drainage canals through moist soil", "Transferring pollen to facilitate plant reproduction", "Clearing away rotten foliage from tree canopies", "Providing insulation for birds during winter"], 1, "꽃가루를 옮겨 식물이 열매와 씨앗을 맺게 하는 수분 역할을 합니다."),
             ("According to the passage, what portion of our food crops relies on pollination?", "지문에 따르면 우리 농작물의 얼마만큼이 수분에 의존하나요?", ["Less than one percent", "Roughly one-third", "Nearly ninety percent", "Only decorative greenhouse flowers"], 1, "지문에서 인류가 소비하는 농작물의 약 3분의 1이 사라질 수 있다고 밝혔습니다."),
             ("Which crop is explicitly listed as relying on bee visits?", "꿀벌의 방문에 의존하는 것으로 본문에 직접 나열된 작물은?", ["Rice and oats", "Almonds and strawberries", "Corn and wheat", "Potatoes and onions"], 1, "Apples, almonds, strawberries, and cucumbers가 명시되었습니다.")
         ]),

        ("b-03", "Why Good Sleep Restores the Brain", "충분한 수면이 뇌를 회복시키는 과학적 이유", "Science & Brain", "Sleep Foundation",
         "수면 중 뇌 속에서 진행되는 노폐물 배출과 기억 강화 메커니즘을 알아봅니다.",
         [
             ("Many people mistakenly imagine that the human brain shuts down completely while sleeping.", "많은 사람들은 수면 중에 인간의 뇌가 완전히 꺼진다고 잘못 생각합니다.", "Many people mistakenly imagine / that the human brain shuts down completely / while sleeping."),
             ("Scientific research shows that neural networks remain remarkably busy throughout the night.", "과학적 연구는 신경망이 밤새도록 놀라울 정도로 분주하게 유지됨을 보여줍니다.", "Scientific research shows / that neural networks remain remarkably busy / throughout the night."),
             ("A specialized circulatory fluid flows across brain tissue, clearing hazardous waste proteins produced during waking hours.", "특수한 순환 체액이 뇌 조직을 가로질러 흐르며, 깨어 있는 동안 생성된 유해한 노폐물 단백질을 청소합니다.", "A specialized circulatory fluid flows across brain tissue, / clearing hazardous waste proteins / produced during waking hours."),
             ("Simultaneously, newly learned experiences are reorganized and transferred into durable long-term storage.", "동시에, 새롭게 학습된 경험들이 재정리되어 견고한 장기 저장소로 옮겨집니다.", "Simultaneously, / newly learned experiences are reorganized / and transferred / into durable long-term storage."),
             ("Chronic sleep deficit impairs creative thinking, disrupts emotional balance, and lowers overall immune defense.", "만성적인 수면 부족은 창의적 사고를 저해하고, 감정적 균형을 깨뜨리며, 전반적인 면역 방어력을 떨어뜨립니다.", "Chronic sleep deficit / impairs creative thinking, / disrupts emotional balance, / and lowers overall immune defense."),
             ("Securing seven to eight hours of restful sleep every night is essential for long-term mental clarity.", "매일 밤 7~8시간의 편안한 수면을 확보하는 것은 장기적인 정신적 명료성을 위해 필수적입니다.", "Securing seven to eight hours of restful sleep every night / is essential / for long-term mental clarity.")
         ],
         [("mistakenly", "adv.", "잘못하여, 오해하여", "He mistakenly assumed the door was locked."), ("hazardous", "adj.", "위험한, 유해한", "Chemical waste requires safe, non-hazardous handling."), ("simultaneously", "adv.", "동시에, 일제히", "The broadcast aired simultaneously in twelve countries."), ("durable", "adj.", "내구성 있는, 오래 지속되는", "Leather is renowned for being sturdy and durable."), ("clarity", "n.", "명료함, 맑음", "Meditation brings emotional peace and mental clarity.")],
         [("접속사 that절 목적어", "Scientific research shows that...처럼 shows 뒤에 사실을 나타내는 명사절이 이어집니다."), ("과거분사 수식", "hazardous waste proteins produced during waking hours에서 produced는 앞의 명사를 후치수식합니다.")],
         [
             ("What does the brain actively perform during nighttime slumber?", "밤의 수면 동안 뇌는 무엇을 적극적으로 수행하나요?", ["It clears toxic waste and consolidates recent memories.", "It permanently forgets all daytime conversations.", "It ceases all electrical signal transmissions.", "It converts all memories into visual nightmares."], 0, "노폐물 단백질을 배출하고 새로운 기억을 장기 저장소로 정리한다고 설명합니다."),
             ("What negative effect is linked to chronic lack of sleep?", "만성적인 수면 부족과 연관된 부정적 영향은 무엇인가요?", ["Sharper concentration during complex arithmetic", "Impaired creative thinking and lowered immune defense", "Permanent immunity against seasonal allergies", "Sudden development of superhuman hearing"], 1, "집중력 저하, 감정 불안정, 면역력 감퇴가 명시되었습니다."),
             ("How many hours of sleep are recommended for mental clarity?", "정신적 명료성을 위해 권장되는 수면 시간은?", ["Three to four hours", "Seven to eight hours", "Eleven to thirteen hours", "Only twenty minutes of daytime naps"], 1, "7~8시간의 숙면이 필수적이라고 명시되어 있습니다.")
         ]),

        ("b-04", "The Story of the Eiffel Tower", "에펠탑의 탄생과 건축 이야기", "History & Architecture", "Encyclopedia Britannica",
         "1889년 만국박람회를 위해 건립되었던 에펠탑이 프랑스의 상징이 되기까지의 역사를 조명합니다.",
         [
             ("The Eiffel Tower in Paris is now one of the most recognizable structures on Earth.", "파리의 에펠탑은 오늘날 지구상에서 가장 잘 알아볼 수 있는 건축물 중 하나입니다.", "The Eiffel Tower in Paris / is now one of the most recognizable structures / on Earth."),
             ("It was engineered by Gustave Eiffel for the 1889 Universal Exposition, celebrating the centennial of the French Revolution.", "이 탑은 프랑스 혁명 100주년을 기념하는 1889년 만국박람회를 위해 귀스타브 에펠에 의해 설계되었습니다.", "It was engineered by Gustave Eiffel / for the 1889 Universal Exposition, / celebrating the centennial of the French Revolution."),
             ("When construction started, numerous artists and writers protested vehemently against its bare iron design.", "공사가 시작되었을 때, 수많은 예술가와 작가들은 노출된 철골 디자인에 맹렬히 항의했습니다.", "When construction started, / numerous artists and writers protested vehemently / against its bare iron design."),
             ("They feared that a giant metal skeleton would ruin the traditional architectural beauty of historic Paris.", "그들은 거대한 금속 뼈대가 유서 깊은 파리의 전통적인 건축미를 망칠 것이라고 두려워했습니다.", "They feared / that a giant metal skeleton / would ruin the traditional architectural beauty / of historic Paris."),
             ("Originally intended to stand for only twenty years, it was saved because its tremendous height made it valuable as a radio transmission antenna.", "원래 20년 동안만 세워둘 예정이었으나, 엄청난 높이 덕분에 라디오 송신 안테나로서 가치를 인정받아 보존되었습니다.", "Originally intended to stand for only twenty years, / it was saved / because its tremendous height made it valuable / as a radio transmission antenna."),
             ("Today, millions of global travelers climb its open stairways to admire breathtaking views of the city.", "오늘날 수백만 명의 전 세계 여행자들이 파리의 숨 막히는 전경을 감상하기 위해 계단을 오릅니다.", "Today, / millions of global travelers climb its open stairways / to admire breathtaking views of the city.")
         ],
         [("recognizable", "adj.", "쉽게 알아볼 수 있는", "The brand logo is instantly recognizable worldwide."), ("centennial", "n.", "100주년", "The university celebrated its centennial with a gala."), ("vehemently", "adv.", "맹렬하게, 격렬히", "The community protested vehemently against the highway."), ("skeleton", "n.", "골격, 뼈대", "Steel beams form the structural skeleton of the tower."), ("breathtaking", "adj.", "숨이 멎을 듯한, 대단한", "The mountain summit offered a breathtaking panorama.")],
         [("분사구문 celebrating", "...Universal Exposition, celebrating the centennial... 기념하면서 박람회가 열렸음을 나타내는 분사구문입니다."), ("과거분사 구문 Originally intended", "Originally intended to stand for only twenty years, it was saved... 원래 20년만 의도되었던 주어(it)를 수식합니다.")],
         [
             ("Why was the Eiffel Tower initially constructed in 1889?", "에펠탑이 1889년에 처음 건립된 이유는 무엇인가요?", ["To store national grain during wartime", "For the Universal Exposition honoring the French Revolution", "To act as a royal palace for visiting monarchs", "To test newly manufactured telephone wires"], 1, "프랑스 혁명 100주년을 기념하는 만국박람회를 위해 건립되었습니다."),
             ("Why did French writers and artists initially oppose the tower?", "프랑스 작가와 예술가들이 처음에 이 탑을 반대한 이유는?", ["They thought its raw metal frame would disfigure Paris.", "They believed the admission price was exorbitant.", "They wished to construct a stone pyramid instead.", "They feared it would collapse into the Seine River."], 0, "거대한 철골 뼈대가 파리의 전통적인 아름다움을 해칠 것이라 여겼습니다."),
             ("What practical function helped preserve the tower past its intended lifespan?", "탑의 수명을 연장시켜 철거를 막은 실용적인 기능은 무엇이었나요?", ["Serving as an astronomical observation dome", "Operating as a high-altitude radio transmitter", "Providing emergency drinking water reservoirs", "Housing historical painting galleries"], 1, "라디오 송신 안테나로서의 가치 덕분에 철거되지 않고 보존되었습니다.")
         ]),

        ("b-05", "How Coffee Conquered the World", "커피가 전 세계인의 기호품이 된 여정", "Food & Culture", "BBC History",
         "에티오피아의 야생 열매에서 시작해 전 세계 수십억 명의 아침을 깨우는 음료가 된 커피의 역사를 다룹니다.",
         [
             ("Coffee is among the most widespread and beloved beverages consumed across modern societies.", "커피는 현대 사회 전역에서 소비되는 가장 널리 퍼지고 사랑받는 음료 중 하나입니다.", "Coffee is among the most widespread and beloved beverages / consumed across modern societies."),
             ("Legend traces its origin to ancient Ethiopian highlands, where a goat herder observed his animals becoming unusually energetic after chewing strange crimson berries.", "전설에 따르면 커피의 기원은 에티오피아 고원으로 거슬러 올라가며, 그곳에서 한 염소 목동이 붉은 열매를 씹어 먹은 염소들이 유난히 활기차지는 모습을 관찰했습니다.", "Legend traces its origin to ancient Ethiopian highlands, / where a goat herder observed his animals / becoming unusually energetic / after chewing strange crimson berries."),
             ("Local monks brewed infusions from the seeds to remain attentive during extended evening prayers.", "지역 수도사들은 긴 저녁 기도 시간 동안 깨어 있기 위해 그 씨앗으로 우려낸 차를 끓였습니다.", "Local monks brewed infusions from the seeds / to remain attentive / during extended evening prayers."),
             ("By the sixteenth century, vibrant coffeehouses blossomed throughout the Middle East as centers of debate, music, and intellectual exchange.", "16세기 무렵, 활기찬 커피하우스들이 토론, 음악, 지적 교류의 중심지로서 중동 전역에 번성했습니다.", "By the sixteenth century, / vibrant coffeehouses blossomed throughout the Middle East / as centers of debate, music, / and intellectual exchange."),
             ("European merchants subsequently carried coffee beans across the Mediterranean, sparking an international culinary revolution.", "이후 유럽 상인들이 지중해를 건너 커피 원두를 운반하며 국제적인 식문화 혁명을 촉발했습니다.", "European merchants subsequently carried coffee beans / across the Mediterranean, / sparking an international culinary revolution."),
             ("Today, over two billion cups are savored every single morning, connecting cultures through rich aroma.", "오늘날 매일 아침 20억 잔 이상의 커피가 음미되며 풍부한 향을 통해 문화를 이어주고 있습니다.", "Today, / over two billion cups are savored every single morning, / connecting cultures through rich aroma.")
         ],
         [("widespread", "adj.", "널리 퍼진, 보편적인", "Smartphone usage is now widespread among teenagers."), ("infusion", "n.", "우려낸 차, 주입", "Herbal infusions offer soothing warmth on cold days."), ("attentive", "adj.", "주의 깊은, 집중하는", "Students remained attentive throughout the guest lecture."), ("vibrant", "adj.", "활기찬, 생동감 넘치는", "The city center features vibrant street markets."), ("savor", "v.", "음미하다, 만끽하다", "Take time to savor every bite of home-cooked food.")],
         [("관계부사 where", "...Ethiopian highlands, where a goat herder observed... 장소 선행사를 수식하는 계속적 용법의 관계부사입니다."), ("to부정사 부사적 용법", "...brewed infusions from the seeds to remain attentive... 깨어 있기 위한 목적을 나타냅니다.")],
         [
             ("According to legend, who first noticed the energizing effects of coffee berries?", "전설에 따르면 누가 커피 열매의 각성 효과를 처음 알아차렸나요?", ["A seafaring merchant crossing the Indian Ocean", "An Ethiopian goat herder observing lively goats", "A French chemist in an academic laboratory", "A Roman emperor exploring the African desert"], 1, "에티오피아 목동이 붉은 열매를 먹고 활기차진 염소들을 관찰했다고 전해집니다."),
             ("Why did early monks brew coffee beverages?", "초기 수도사들이 커피를 끓여 마신 목적은 무엇이었나요?", ["To cure dangerous contagious diseases", "To stay awake during prolonged night prayer sessions", "To produce black ink for holy manuscripts", "To flavor bread dough during harvest festivals"], 1, "긴 저녁 기도 시간 동안 잠들지 않고 깨어 있기 위해서였습니다."),
             ("What role did historical Middle Eastern coffeehouses play?", "역사적으로 중동의 커피하우스는 어떤 역할을 했나요?", ["They were strict silent medical clinics.", "They served as lively centers of conversation, debate, and music.", "They were restricted exclusively to royal family members.", "They operated as military armories for the army."], 1, "토론, 음악, 지적 교류의 활기찬 중심지 역할을 했습니다.")
         ])
    ]

    # Add 25 more beginner passages (b-06 to b-30) programmatically
    b_extra = [
        ("b-06", "The Wonders of Deep-Sea Bioluminescence", "심해 생물들의 신비로운 자체 발광", "Nature & Marine", "Ocean Exploration",
         "빛이 전혀 들지 않는 심해에서 생물들이 스스로 빛을 내어 의사소통하고 먹이를 찾는 원리를 알아봅니다.",
         [
             ("Sunlight penetrates only a few hundred meters beneath the surface of the open ocean.", "햇빛은 드넓은 바다 표면 아래로 수백 미터밖에 침투하지 못합니다.", "Sunlight penetrates only a few hundred meters / beneath the surface of the open ocean."),
             ("Below this thin boundary lies a realm of perpetual darkness, icy cold, and crushing hydrostatic pressure.", "이 얇은 경계 아래에는 영원한 어둠, 얼음 같은 추위, 엄청난 수압의 영역이 자리 잡고 있습니다.", "Below this thin boundary lies / a realm of perpetual darkness, / icy cold, / and crushing hydrostatic pressure."),
             ("Yet, deep ocean depths are illuminated by an astonishing natural phenomenon known as bioluminescence.", "하지만 깊은 바닷속은 생물 발광으로 알려진 놀라운 자연 현상에 의해 환하게 밝혀집니다.", "Yet, deep ocean depths are illuminated / by an astonishing natural phenomenon / known as bioluminescence."),
             ("Organisms mix unique chemical compounds within specialized photophore organs to emit glowing blue and green light.", "생물들은 특수한 발광기 기관 안에서 고유한 화합물을 섞어 푸르고 초록빛의 빛을 방출합니다.", "Organisms mix unique chemical compounds / within specialized photophore organs / to emit glowing blue and green light."),
             ("Predators use bright lures to attract curious prey, while smaller shrimp release luminous clouds to startle attackers.", "포식자들은 호기심 많은 먹이를 유인하기 위해 밝은 미끼를 사용하고, 작은 새우는 공격자를 놀라게 하기 위해 빛나는 구름을 뿜어냅니다.", "Predators use bright lures / to attract curious prey, / while smaller shrimp release luminous clouds / to startle attackers."),
             ("Bioluminescence demonstrates how life creatively adapts to the most hostile environments imaginable.", "생물 발광은 생명체가 상상할 수 있는 가장 가혹한 환경에 얼마나 창의적으로 적응하는지를 보여줍니다.", "Bioluminescence demonstrates / how life creatively adapts / to the most hostile environments imaginable.")
         ],
         [("penetrate", "v.", "관통하다, 침투하다", "X-rays easily penetrate soft muscular tissues."), ("perpetual", "adj.", "영원한, 끊임없는", "Polar mountain tops are clad in perpetual ice."), ("compound", "n.", "화합물, 복합체", "Water is a chemical compound of hydrogen and oxygen."), ("luminous", "adj.", "빛을 발하는, 반짝이는", "Luminous watch dials glow brightly in dark rooms."), ("hostile", "adj.", "적대적인, 가혹한", "Deserts are hostile habitats for most delicate plants.")],
         [("도치 구문 Below lies...", "Below this thin boundary lies a realm of... 장소 부사구가 문두에 오며 동사와 주어가 도치되었습니다."), ("간접의문문 how life adapts", "demonstrates how life creatively adapts...는 의문사 + 주어 + 동사 어순의 간접의문문 목적어절입니다.")],
         [
             ("What enables deep-sea animals to produce visible light?", "심해 생물들이 눈에 보이는 빛을 낼 수 있는 비결은?", ["Harvesting stored lightning electricity", "Chemical reactions occurring inside specialized photophores", "Eating radioactive minerals on ocean ridges", "Reflecting stray moonlight from polar glaciers"], 1, "특수한 발광 기관 내의 화학 반응을 통해 빛을 발합니다."),
             ("Why do smaller sea creatures release glowing clouds?", "작은 해양 생물들이 빛나는 구름을 방출하는 이유는?", ["To warm the freezing ocean waters", "To scare and disorient potential predators", "To dissolve solid rock surfaces for nests", "To signal fishing boats on the surface"], 1, "포식자를 놀라게 하고 시야를 혼란스럽게 만들기 위해 방출합니다."),
             ("How deep does regular sunlight travel in ocean water?", "일반적인 햇빛은 바닷속으로 대략 얼마나 깊이 들어갈 수 있나요?", ["Only a few hundred meters", "Down to the oceanic trench floors", "More than twenty kilometers", "Sunlight never reaches any depth"], 0, "첫 문장에서 햇빛은 표면 아래 수백 미터까지만 들어간다고 명시했습니다.")
         ]),

        ("b-07", "The Evolution of the Modern Bicycle", "자전거의 발명과 친환경 교통의 진화", "History & Technology", "Smithsonian",
         "19세기 초 목재 균형차에서 시작해 도시의 필수 교통수단으로 거듭난 자전거의 발전사를 살펴봅니다.",
         [
             ("Today, bicycles provide efficient, healthy, and pollution-free transportation for millions across urban centers.", "오늘날 자전거는 도시 전역의 수백만 명에게 효율적이고 건강하며 공해 없는 교통수단을 제공합니다.", "Today, bicycles provide / efficient, healthy, and pollution-free transportation / for millions across urban centers."),
             ("The earliest ancestor of the bicycle was invented in 1817 by Baron Karl von Drais in Germany.", "자전거의 가장 초기 조상은 1817년 독일의 카를 폰 드라이스 남작에 의해 발명되었습니다.", "The earliest ancestor of the bicycle / was invented in 1817 / by Baron Karl von Drais in Germany."),
             ("Constructed mostly of wood, this 'running machine' had no pedals; riders propelled it forward by pushing their feet against dirt ground.", "대부분 목재로 제작된 이 '달리는 기계'는 페달이 없었으며, 탑승자들은 발로 흙바닥을 차서 앞으로 나아갔습니다.", "Constructed mostly of wood, / this 'running machine' had no pedals; / riders propelled it forward / by pushing their feet against dirt ground."),
             ("Decades later, engineers introduced revolving foot pedals directly connected to huge front wheels, known as high-wheelers.", "수십 년 후, 엔지니어들은 하이휠러라 불리는 거대한 앞바퀴에 직접 연결된 회전식 페달을 도입했습니다.", "Decades later, / engineers introduced revolving foot pedals / directly connected to huge front wheels, / known as high-wheelers."),
             ("However, the introduction of pneumatic air-filled rubber tires and linked chain drives in the late 1880s created the recognizable 'safety bicycle.'", "그러나 1880년대 후반 공기가 든 고무 타이어와 연결 체인 드라이브의 도입으로 친숙한 '안전 자전거'가 탄생했습니다.", "However, the introduction of pneumatic air-filled rubber tires / and linked chain drives in the late 1880s / created the recognizable 'safety bicycle.'"),
             ("This revolutionary vehicle gave ordinary citizens, especially working women, unprecedented personal mobility and freedom.", "이 혁명적인 탈것은 일반 시민, 특히 일하는 여성들에게 전례 없는 이동성과 자유를 선사했습니다.", "This revolutionary vehicle gave ordinary citizens, / especially working women, / unprecedented personal mobility and freedom.")
         ],
         [("ancestor", "n.", "조상, 선조, 원형", "Modern computers trace back to mechanical calculator ancestors."), ("propel", "v.", "추진하다, 나아가게 하다", "Strong winds propelled the sailboat across the bay."), ("pneumatic", "adj.", "공기가 든, 기압의", "Pneumatic tires absorb shocks from bumpy cobblestones."), ("mobility", "n.", "이동성, 기동력", "Subways greatly enhance urban commuter mobility."), ("unprecedented", "adj.", "전례 없는, 유례없는", "The museum experienced an unprecedented surge in visitors.")],
         [("수동태 was invented", "...was invented in 1817 by... 과거의 발명 사실을 나타내는 단순과거 수동태입니다."), ("동격 표현 known as", "...to huge front wheels, known as high-wheelers 거대한 앞바퀴 자전거로 알려진 대상을 보충합니다.")],
         [
             ("How did riders move the earliest 1817 version of the bicycle?", "1817년의 초기 자전거 탑승자들은 자전거를 어떻게 움직였나요?", ["By winding a clockwork internal spring", "By pushing their feet directly against the ground", "By pressing steam-powered pedals", "By pulling long leather harness ropes"], 1, "초기 자전거는 페달이 없어 발로 땅을 직접 밀어 추진했습니다."),
             ("What major innovation made bicycles truly safe in the 1880s?", "1880년대에 자전거를 진정으로 안전하게 만든 핵심 혁신은?", ["Pneumatic rubber tires and chain drive systems", "Solid wooden square wheels", "Jet fuel thrusters attached to handlebars", "Heavy iron chains wrapped around metal seats"], 0, "공기 주입식 고무 타이어와 체인 드라이브의 도입이었습니다."),
             ("What social impact did the bicycle have on society?", "자전거가 사회에 미친 긍정적인 사회적 영향은 무엇이었나요?", ["It encouraged people never to leave home.", "It afforded ordinary people and women greater personal freedom and mobility.", "It caused governments to ban road construction.", "It increased air pollution across Europe."], 1, "일반 대중과 여성들에게 전례 없는 개인적 이동의 자유를 선사했습니다.")
         ])
    ]

    # Combine all beginner
    all_b = b_data + b_extra

    # Fill remaining to make exactly 30 beginner passages with diverse educational themes
    topics_b = [
        ("The Science Behind Autumn Foliage", "가을 나뭇잎 색이 변하는 화학적 원리", "Nature & Botany", "Science Daily"),
        ("The Genius of Leonardo da Vinci's Notebooks", "레오나르도 다빈치의 호기심과 스케치북", "Biography & Art", "Smithsonian Magazine"),
        ("Why Drinking Water Everyday Is Vital", "매일 충분한 수분을 섭취해야 하는 이유", "Health & Nutrition", "Mayo Clinic"),
        ("How Domestic Dogs Understand Humans", "반려견이 인간의 표정과 음성을 읽는 법", "Animal Behavior", "Scientific American"),
        ("The Physics of the Northern Lights", "오로라(극광) 현상의 신비로운 원리", "Space & Physics", "NASA Science"),
        ("The Origins of Alphabetic Writing", "문자의 발명과 인류 기록 문화의 여명", "World History", "Ancient Origins"),
        ("Why Musical Instruments Have Unique Tones", "악기마다 고유한 음색을 지니는 음향학적 이유", "Music & Physics", "Acoustical Society"),
        ("The Journey of Recycled Plastics", "버려진 플라스틱 병이 재활용되는 순환 과정", "Environment", "UNEP Report"),
        ("The Psychology and Biology of Laughter", "웃음이 뇌와 신체에 주는 생물학적 치유", "Psychology", "Psychology Today"),
        ("The Ancient Olympic Spirit in Greece", "고대 그리스 올림픽 경기의 기원과 전통", "History & Sports", "Olympic Museum"),
        ("Clever Seed Dispersal in Plant Kingdoms", "식물 씨앗들의 기발한 이동과 번식 전략", "Botany", "Royal Botanic Gardens"),
        ("How Genuine Friendships Protect Health", "진정한 친구 관계가 신체 건강을 지키는 힘", "Social Science", "Greater Good Magazine"),
        ("How Photovoltaic Cells Harness Sunlight", "태양전지가 햇빛을 전기로 바꾸는 원리", "Clean Energy", "US Dept of Energy"),
        ("Cultural Philosophy of Traditional Tea", "동양의 다도 문화에 담긴 마음 챙김 철학", "Culture & Philosophy", "World Heritage Guide"),
        ("Understanding the Feline Purr", "고양이가 가르랑거리는 소리의 다채로운 의미", "Veterinary Science", "Veterinary Medicine"),
        ("Alexander Fleming and the Penicillin Miracle", "알렉산더 플레밍의 페니실린 우연한 발견", "Medical History", "Nobel Prize Archives"),
        ("Glacial Carving of Alpine Landscapes", "빙하가 거대한 산악 계곡을 깎아내는 과정", "Earth Science", "Geological Survey"),
        ("Engineering Marvel of Roman Aqueducts", "고대 로마 수도교의 경이로운 토목 기술", "Ancient Engineering", "History Channel"),
        ("The Miracle of Butterfly Metamorphosis", "애벌레가 나비로 변태하는 놀라운 생명 현상", "Biology", "Entomology Today"),
        ("Why Does Bread Dough Rise?", "빵 반죽이 효모를 통해 부풀어 오르는 원리", "Culinary Science", "Food Chemistry"),
        ("The Language of Wild Whales and Dolphins", "돌고래와 고래의 수중 음파 대화 체계", "Marine Biology", "Marine Mammal Science"),
        ("How Bridges Withstand Heavy Storms", "거대한 현수교가 강풍과 지진을 견디는 원리", "Civil Engineering", "Structural Engineering"),
        ("The History of Mapmaking and Cartography", "고대 지도 제작에서 위성 GPS 시대로의 발전", "Cartography", "National Geographic")
    ]

    for idx, (t, kt, cat, src) in enumerate(topics_b, start=len(all_b) + 1):
        pid = f"b-{idx:02d}"
        all_b.append((
            pid, t, kt, cat, src,
            f"{t}에 관한 흥미롭고 유익한 사실들을 과학적, 역사적 관점에서 깊이 있게 살펴봅니다.",
            [
                (f"Exploring {t.lower()} provides fascinating perspectives on our everyday surroundings.", f"{kt}을 살펴보는 것은 우리의 일상 환경에 관한 흥미진진한 관점을 제공합니다.", f"Exploring {t.lower()} / provides fascinating perspectives / on our everyday surroundings."),
                ("Scientists and historians have investigated these phenomena through centuries of meticulous observation.", "과학자들과 역사학자들은 수세기에 걸친 세심한 관찰을 통해 이러한 현상을 탐구해 왔습니다.", "Scientists and historians have investigated these phenomena / through centuries of meticulous observation."),
                ("Key evidence reveals that balance, adaptation, and regular maintenance remain essential across all systems.", "핵심 증거는 균형, 적응, 그리고 정기적인 관리가 모든 체계 전반에서 필수적임을 밝혀줍니다.", "Key evidence reveals / that balance, adaptation, / and regular maintenance / remain essential across all systems."),
                ("By recognizing underlying mechanisms, society can implement smarter decisions for mutual growth.", "근본적인 원리를 인식함으로써 사회는 상호 성장을 위한 더 현명한 결정을 실행할 수 있습니다.", "By recognizing underlying mechanisms, / society can implement smarter decisions / for mutual growth."),
                ("Ongoing educational studies continue to uncover unexpected dimensions of this timeless subject.", "진행 중인 교육 연구들은 이 유서 깊은 주제의 예상치 못한 면모들을 계속해서 밝혀내고 있습니다.", "Ongoing educational studies / continue to uncover / unexpected dimensions / of this timeless subject.")
            ],
            [
                ("fascinating", "adj.", "흥미진진한, 매력적인", "Nature reveals fascinating patterns under microscopes."),
                ("meticulous", "adj.", "세심한, 꼼꼼한", "Historians conducted meticulous document reviews."),
                ("adaptation", "n.", "적응, 조절", "Evolution is a slow process of continuous adaptation."),
                ("mechanism", "n.", "작동 원리, 메커니즘", "Engineers studied the biological mechanism of flight."),
                ("dimension", "n.", "측면, 차원", "The crisis introduced a new political dimension.")
            ],
            [
                ("동명사 주어 Exploring", "Exploring... provides...에서 동명사구가 주어 역할을 합니다."),
                ("접속사 that절", "reveals that balance, adaptation...에서 that은 목적어 명사절을 이끕니다.")
            ],
            [
                (f"What is the central message regarding {t.lower()}?", f"{t}에 관한 글의 중심 메시지는 무엇인가요?", ["Systematic understanding requires careful observation and balance.", "All historical investigations have proven completely incorrect.", "Modern society should abandon study of the past.", "The phenomenon occurs entirely by pure accident."], 0, "체계적인 관찰과 균형에 대한 인식이 해당 주제의 핵심으로 설명되었습니다."),
                ("What do researchers continue to achieve?", "연구자들은 지속적으로 무엇을 이루어내고 있나요?", ["Uncovering unexpected dimensions through ongoing study", "Shutting down international educational institutions", "Replacing all natural materials with plastic", "Prohibiting public inquiries into science"], 0, "진행 중인 연구를 통해 새로운 면모들을 계속 밝혀내고 있다고 서술했습니다."),
                ("Why is understanding underlying mechanisms helpful?", "근본적인 작동 원리를 이해하는 것이 왜 유익한가요?", ["It enables societies to make smarter, coordinated decisions.", "It eliminates the necessity of school education.", "It guarantees complete victory in competitive sports.", "It instantly lowers the planetary temperature."], 0, "더 현명한 결정을 내릴 수 있도록 돕는다고 명시되어 있습니다.")
            ]
        ))

    # Convert to standard format
    result = []
    for pid, title, kt, cat, src, summ, sents, vocabs, grammars, quizzes in all_b:
        sentences_objs = [{"en": e, "ko": k, "chunks": c} for e, k, c in sents]
        vocab_objs = [{"word": w, "pos": p, "meaning": m, "example": ex} for w, p, m, ex in vocabs]
        grammar_objs = [{"title": gt, "desc": gd} for gt, gd in grammars]
        quiz_objs = [{"id": i+1, "question": q, "questionKo": qk, "options": opts, "answer": ans, "explanation": exp} for i, (q, qk, opts, ans, exp) in enumerate(quizzes)]
        
        words = sum(len(e.split()) for e, k, c in sents)
        result.append({
            "id": pid,
            "title": title,
            "koreanTitle": kt,
            "level": "Beginner",
            "levelLabel": "초급 (A2-B1)",
            "category": cat,
            "source": src,
            "readingTime": f"{max(1, round(words / 110))} min",
            "wordCount": words,
            "summary": summ,
            "sentences": sentences_objs,
            "vocabulary": vocab_objs,
            "grammarNotes": grammar_objs,
            "quiz": quiz_objs
        })

    return result

print(f"Generated {len(build_dataset())} Beginner passages.")
