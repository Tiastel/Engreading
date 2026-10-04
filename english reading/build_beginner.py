# -*- coding: utf-8 -*-
"""
Build 30 Beginner Passages for ReadFlow Pro
Levels: Beginner (A2-B1)
Sources: Harvard Health, National Geographic, BBC, Smithsonian, Mayo Clinic, NASA, etc.
"""

def get_beginner_passages():
    p = []
    
    # 1. Centenarians
    p.append({
        "id": "b-01",
        "title": "Daily Habits of Long-Lived People",
        "koreanTitle": "장수하는 사람들의 일상 습관",
        "level": "Beginner",
        "levelLabel": "초급 (A2-B1)",
        "category": "Health & Lifestyle",
        "source": "Harvard Health Publishing",
        "summary": "전 세계에서 100세 이상 건강하게 살아가는 사람들의 공통적인 일상 습관과 식단을 살펴봅니다.",
        "sentences": [
            {"en": "People who live past one hundred years often share similar daily routines.", "ko": "100세 넘게 사는 사람들은 종종 비슷한 일상 루틴을 공유합니다.", "chunks": "People / who live past one hundred years / often share / similar daily routines."},
            {"en": "They usually eat natural, plant-based foods such as beans, nuts, and fresh vegetables.", "ko": "그들은 보통 콩, 견과류, 신선한 채소와 같은 천연 식물성 식품을 먹습니다.", "chunks": "They usually eat / natural, plant-based foods / such as beans, nuts, / and fresh vegetables."},
            {"en": "In addition, physical movement is a natural part of their day.", "ko": "또한, 신체적 움직임은 그들 하루의 자연스러운 일부입니다.", "chunks": "In addition, / physical movement / is a natural part / of their day."},
            {"en": "Instead of going to modern gyms, they walk outside, tend gardens, and clean their own homes.", "ko": "그들은 현대적인 헬스장에 가는 대신 밖을 걷고, 정원을 가꾸며, 자신의 집을 청소합니다.", "chunks": "Instead of going to modern gyms, / they walk outside, / tend gardens, / and clean their own homes."},
            {"en": "Strong relationships with family and friendly neighbors also protect their mental well-being.", "ko": "가족 및 다정한 이웃과의 끈끈한 관계 또한 그들의 정신 건강을 지켜줍니다.", "chunks": "Strong relationships / with family and friendly neighbors / also protect / their mental well-being."},
            {"en": "Having a clear purpose each morning keeps their minds sharp and peaceful.", "ko": "매일 아침 명확한 목적의식을 가지는 것은 그들의 마음을 명민하고 평화롭게 유지해 줍니다.", "chunks": "Having a clear purpose each morning / keeps their minds sharp / and peaceful."}
        ],
        "vocabulary": [
            {"word": "routine", "pos": "n.", "meaning": "일상, 규칙적인 일과", "example": "A regular morning routine reduces daily stress."},
            {"word": "tend", "pos": "v.", "meaning": "돌보다, 가꾸다", "example": "She loves to tend flowers in her balcony garden."},
            {"word": "well-being", "pos": "n.", "meaning": "안녕, 행복, 건강", "example": "Social connections are vital for emotional well-being."},
            {"word": "purpose", "pos": "n.", "meaning": "목적, 의미", "example": "He found a new purpose in helping young students."},
            {"word": "sharp", "pos": "adj.", "meaning": "예리한, 명민한", "example": "Reading books helps keep the human brain sharp."}
        ],
        "grammarNotes": [
            {"title": "주격 관계대명사 who", "desc": "<b>'People who live past one hundred years...'</b>: who는 앞의 선행사 People을 수식하는 주격 관계대명사절을 이끕니다."},
            {"title": "동명사 주어와 수 일치", "desc": "<b>'Having a clear purpose... keeps...'</b>: 동명사구(Having a clear purpose)가 주어일 때는 단수 취급하여 동사에 -s(keeps)가 붙습니다."}
        ],
        "quiz": [
            {
                "id": 1,
                "question": "What is the primary factor contributing to long life according to the text?",
                "questionKo": "지문에 따르면 장수에 기여하는 핵심 요인은 무엇인가요?",
                "options": ["Using heavy fitness machines daily", "A combination of natural diet, active lifestyle, and community", "Moving to modern big cities", "Avoiding all types of physical work"],
                "answer": 1,
                "explanation": "지문 전체에서 자연스러운 식단, 정원 가꾸기와 걷기 같은 일상적 신체 활동, 그리고 이웃과의 강한 유대감이 장수의 핵심 요인으로 제시되었습니다."
            },
            {
                "id": 2,
                "question": "How do long-lived people typically stay physically active?",
                "questionKo": "장수하는 사람들은 일반적으로 어떻게 신체 활동을 유지하나요?",
                "options": ["By training for competitive marathons", "By working out with professional trainers", "Through ordinary daily activities like walking and gardening", "By taking expensive nutritional pills"],
                "answer": 2,
                "explanation": "지문에서 'Instead of going to modern gyms, they walk outside, tend gardens, and clean their own homes'라고 명시되어 있습니다."
            },
            {
                "id": 3,
                "question": "Why is having a morning purpose beneficial?",
                "questionKo": "아침에 목적의식을 갖는 것이 왜 유익한가요?",
                "options": ["It guarantees huge financial success.", "It helps maintain a sharp and peaceful mind.", "It eliminates the need for healthy eating.", "It allows you to sleep less than four hours."],
                "answer": 1,
                "explanation": "마지막 문장에서 'Having a clear purpose each morning keeps their minds sharp and peaceful.'라고 설명하고 있습니다."
            }
        ]
    })

    # 2. Honeybees
    p.append({
        "id": "b-02",
        "title": "The Vital Role of Honeybees",
        "koreanTitle": "꿀벌의 중대한 생태학적 역할",
        "level": "Beginner",
        "levelLabel": "초급 (A2-B1)",
        "category": "Nature & Ecology",
        "source": "National Geographic Kids",
        "summary": "작은 꿀벌이 식물의 수분을 돕고 인류의 식량 공급에 미치는 결정적인 영향을 설명합니다.",
        "sentences": [
            {"en": "Honeybees are tiny insects that perform an essential task for our planet.", "ko": "꿀벌은 우리 지구를 위해 필수적인 작업을 수행하는 아주 작은 곤충입니다.", "chunks": "Honeybees are tiny insects / that perform an essential task / for our planet."},
            {"en": "As they fly from flower to flower gathering sweet nectar, pollen sticks to their fuzzy bodies.", "ko": "그들이 달콤한 꿀을 모으기 위해 꽃에서 꽃으로 날아다닐 때, 꽃가루가 그들의 털북숭이 몸에 달라붙습니다.", "chunks": "As they fly from flower to flower / gathering sweet nectar, / pollen sticks to their fuzzy bodies."},
            {"en": "This powdery pollen is transferred to the next blossom, allowing plants to produce seeds and fruits.", "ko": "이 가루 형태의 꽃가루가 다음 꽃으로 옮겨지며, 식물이 씨앗과 열매를 맺을 수 있게 해줍니다.", "chunks": "This powdery pollen is transferred / to the next blossom, / allowing plants / to produce seeds and fruits."},
            {"en": "Without pollination, nearly one-third of the crops we eat would completely disappear.", "ko": "수분이 없다면, 우리가 먹는 농작물의 거의 3분의 1이 완전히 사라질 것입니다.", "chunks": "Without pollination, / nearly one-third of the crops we eat / would completely disappear."},
            {"en": "Apples, strawberries, almonds, and tomatoes all rely on bee visits.", "ko": "사과, 딸기, 아몬드, 토마토는 모두 꿀벌의 방문에 의존합니다.", "chunks": "Apples, strawberries, almonds, / and tomatoes / all rely on bee visits."},
            {"en": "Protecting bee habitats is therefore crucial for human food security.", "ko": "그러므로 꿀벌의 서식지를 보호하는 것은 인류의 식량 안보에 대단히 중요합니다.", "chunks": "Protecting bee habitats / is therefore crucial / for human food security."}
        ],
        "vocabulary": [
            {"word": "essential", "pos": "adj.", "meaning": "필수적인, 극히 중요한", "example": "Water is essential for the survival of all living creatures."},
            {"word": "pollen", "pos": "n.", "meaning": "꽃가루, 화분", "example": "Spring air is often filled with tree pollen."},
            {"word": "blossom", "pos": "n.", "meaning": "(과수의) 꽃", "example": "Cherry blossoms bloom brilliantly in April."},
            {"word": "crop", "pos": "n.", "meaning": "농작물, 수확물", "example": "Farmers harvested a bountiful crop of wheat this autumn."},
            {"word": "habitat", "pos": "n.", "meaning": "서식지", "example": "Deforestation threatens the natural habitat of wild animals."}
        ],
        "grammarNotes": [
            {"title": "분사구문 allowing", "desc": "<b>'...transferred to the next blossom, allowing plants to...'</b>: 앞 문장의 결과로 식물이 열매를 맺게 한다는 능동의 분사구문(allowing)입니다."},
            {"title": "rely on (~에 의존하다)", "desc": "<b>'all rely on bee visits'</b>: rely on은 depend on과 같은 의미로 빈번하게 쓰이는 중요 전치사 숙어입니다."}
        ],
        "quiz": [
            {
                "id": 1,
                "question": "How do honeybees help plants reproduce?",
                "questionKo": "꿀벌은 식물이 번식하도록 어떻게 돕나요?",
                "options": ["By eating the roots of harmful weeds", "By carrying pollen between different blossoms", "By providing water to dry soil", "By frightening away caterpillars"],
                "answer": 1,
                "explanation": "지문에서 꿀을 모으는 동안 몸에 묻은 꽃가루가 다른 꽃으로 옮겨지며 수분이 일어난다고 설명합니다."
            },
            {
                "id": 2,
                "question": "What would happen if bees ceased to pollinate crops?",
                "questionKo": "꿀벌이 농작물 수분을 멈춘다면 어떤 일이 일어나나요?",
                "options": ["Crop production would double instantly.", "Almost one-third of our food crops could vanish.", "Honey would become free for all consumers.", "Flowers would bloom throughout the entire winter."],
                "answer": 1,
                "explanation": "지문에서 'Without pollination, nearly one-third of the crops we eat would completely disappear.'라고 언급했습니다."
            },
            {
                "id": 3,
                "question": "Which fruit or nut is mentioned as depending on bees?",
                "questionKo": "꿀벌에 의존하는 것으로 언급된 과일이나 견과류는 무엇인가요?",
                "options": ["Wheat and rice", "Bananas and pineapples", "Almonds and strawberries", "Corn and potatoes"],
                "answer": 2,
                "explanation": "본문에 'Apples, strawberries, almonds, and tomatoes all rely on bee visits.'라고 명시되어 있습니다."
            }
        ]
    })

    # 3. Sleep
    p.append({
        "id": "b-03",
        "title": "Why Good Sleep Restores the Brain",
        "koreanTitle": "충분한 수면이 뇌를 회복시키는 이유",
        "level": "Beginner",
        "levelLabel": "초급 (A2-B1)",
        "category": "Science & Brain",
        "source": "Sleep Foundation",
        "summary": "우리가 잠든 동안 뇌 속에서 일어나는 청소 작업과 기억 정리 과정을 쉽게 설명합니다.",
        "sentences": [
            {"en": "Many people assume that our brains completely power down when we sleep.", "ko": "많은 사람들은 우리가 잘 때 뇌가 완전히 꺼진다고 생각합니다.", "chunks": "Many people assume / that our brains completely power down / when we sleep."},
            {"en": "In reality, the brain is remarkably active during nocturnal slumber.", "ko": "실제로는, 뇌는 밤의 수면 시간 동안 놀라울 정도로 활발합니다.", "chunks": "In reality, / the brain is remarkably active / during nocturnal slumber."},
            {"en": "A special fluid washes over brain tissue, flushing away toxic waste products accumulated during the day.", "ko": "특수한 체액이 뇌 조직을 씻어내며, 낮 동안 쌓인 독성 노폐물들을 배출합니다.", "chunks": "A special fluid washes over brain tissue, / flushing away toxic waste products / accumulated during the day."},
            {"en": "At the same time, newly learned information is organized and transferred into permanent long-term memory.", "ko": "동시에, 새롭게 학습된 정보가 정리되어 영구적인 장기 기억으로 이동됩니다.", "chunks": "At the same time, / newly learned information is organized / and transferred / into permanent long-term memory."},
            {"en": "Chronic lack of sleep impairs concentration, weakens immunity, and triggers emotional irritability.", "ko": "만성적인 수면 부족은 집중력을 떨어뜨리고, 면역력을 약화시키며, 감정적 짜증을 유발합니다.", "chunks": "Chronic lack of sleep / impairs concentration, / weakens immunity, / and triggers emotional irritability."},
            {"en": "Aiming for seven to eight hours of sound rest is therefore essential for cognitive vitality.", "ko": "따라서 7~8시간의 깊은 휴식을 취하는 것은 인지적 활력을 위해 필수적입니다.", "chunks": "Aiming for seven to eight hours of sound rest / is therefore essential / for cognitive vitality."}
        ],
        "vocabulary": [
            {"word": "nocturnal", "pos": "adj.", "meaning": "밤의, 야행성의", "example": "Owls are nocturnal creatures that hunt prey in darkness."},
            {"word": "flush", "pos": "v.", "meaning": "물로 씻어내다, 배출하다", "example": "Drink plenty of warm water to flush away bodily toxins."},
            {"word": "permanent", "pos": "adj.", "meaning": "영구적인, 지속적인", "example": "Regular habits create permanent changes in personal character."},
            {"word": "impair", "pos": "v.", "meaning": "손상시키다, 악화시키다", "example": "Extreme fatigue can seriously impair driving ability."},
            {"word": "vitality", "pos": "n.", "meaning": "활력, 생기", "example": "Morning sunlight revitalizes the body and restores natural vitality."}
        ],
        "grammarNotes": [
            {"title": "접속사 that절 목적어", "desc": "<b>'Many people assume that our brains...'</b>: assume의 목적어로 명사절 접속사 that이 사용되었습니다."},
            {"title": "과거분사 후치수식", "desc": "<b>'waste products accumulated during the day'</b>: accumulated는 앞의 명사 waste products를 뒤에서 수식하는 과거분사입니다."}
        ],
        "quiz": [
            {
                "id": 1,
                "question": "What actually happens to the brain during deep sleep?",
                "questionKo": "깊은 잠을 자는 동안 실제로 뇌에서는 무슨 일이 일어나나요?",
                "options": ["It completely ceases all electrical activity.", "It cleanses toxic wastes and organizes long-term memories.", "It loses the majority of stored memories.", "It produces dangerous stress hormones continuously."],
                "answer": 1,
                "explanation": "지문에서 수면 중 특수 체액이 노폐물을 청소하고 새로운 정보를 장기 기억으로 정리한다고 서술되어 있습니다."
            },
            {
                "id": 2,
                "question": "Which of the following is a symptom of chronic sleep deprivation?",
                "questionKo": "다음 중 만성적인 수면 부족의 증상인 것은 무엇인가요?",
                "options": ["Sharpened concentration and eyesight", "Weakened immune system and emotional irritability", "Instant mastery of foreign languages", "Permanent physical weight loss"],
                "answer": 1,
                "explanation": "지문에서 'Chronic lack of sleep impairs concentration, weakens immunity, and triggers emotional irritability.'라고 명시했습니다."
            },
            {
                "id": 3,
                "question": "What is the recommended sleep duration mentioned in the text?",
                "questionKo": "본문에서 권장하는 수면 시간은 얼마인가요?",
                "options": ["4 to 5 hours", "7 to 8 hours", "10 to 12 hours", "Only 2 hours with short naps"],
                "answer": 1,
                "explanation": "마지막 문장에서 'Aiming for seven to eight hours of sound rest is therefore essential'이라고 권장했습니다."
            }
        ]
    })

    # Return initial sample
    return p

print("Loaded beginner builder skeleton.")
