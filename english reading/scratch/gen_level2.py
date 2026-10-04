# -*- coding: utf-8 -*-
"""
Level 2 Generator: 60 Intermediate Logic Questions (Lv.2 중급 논리)
Characteristics: Single blank, contrast/concession/paradox pivots, nuanced transfer academic vocabulary.
"""
import random

def get_level2_questions():
    items = []
    
    # 60 distinct academic problem stems for Level 2
    data = [
        # 1..10
        (
            "Medical Science & Longevity", "역접 / 대조 (Contrast)",
            "rather than resorting to aggressive, artificial regimens", "인위적·격렬함(-) ↔ 자연스러운 습관화(+)",
            "Although modern urban culture often glorifies intense, sporadic physical exhaustion, centenarians in long-lived communities demonstrate that enduring vitality is achieved through ________ integration of movement into daily chores rather than resorting to aggressive, artificial regimens.",
            "현대 도시 문화는 종종 강렬하고 산발적인 육체적 탈진을 미화하지만, 장수촌의 100세인들은 지속적인 활력이 공격적이고 인위적인 운동 요법에 의존하기보다는 일상 가사 속에 움직임을 ________ 통합함으로써 달성된다는 것을 보여준다.",
            "seamless", ["precarious", "sporadic", "superficial"],
            [("seamless", "아주 매끄러운, 단절이 없는 (adj.)"), ("precarious", "불안정한, 위태로운 (adj.)"), ("sporadic", "산발적인 (adj.)"), ("superficial", "피상적인 (adj.)")],
            "역접 접속사 Although와 대조 표현 'rather than resorting to aggressive regimens'를 통해, 빈칸에는 일상 속에 자연스럽게 녹아든 긍정적 수식어인 seamless(매끄러운, 단절 없는)가 와야 합니다."
        ),
        (
            "Neuroscience & Brain Plasticity", "역접 / 대조 (Contrast)",
            "Contrary to the long-held neurological dogma that the adult central nervous system is structurally immutable", "과거 통념(불변/경직) ↔ 현대 뇌과학(가소성/적응성)",
            "Contrary to the long-held neurological dogma that the adult central nervous system is structurally immutable, contemporary neuroplasticity research demonstrates that synaptic architecture remains remarkably ________ even in late senescence.",
            "성인의 중추신경계가 구조적으로 불변한다는 오랜 신경학적 도그마와는 반대로, 현대의 신경가소성 연구는 시냅스 구조가 노년기 후반에조차 현저하게 ________ 상태를 유지함을 보여준다.",
            "malleable", ["ossified", "immutable", "stagnant"],
            [("malleable", "가소성이 있는, 유연한 (adj.)"), ("ossified", "경직된, 뼈처럼 굳은 (adj.)"), ("immutable", "불변의 (adj.)"), ("stagnant", "침체된 (adj.)")],
            "Contrary to structurally immutable(불변이라는 통념과 반대로)가 역접 기준선이므로, '형태를 바꿀 수 있는, 유연한' 뜻의 malleable이 정답입니다."
        ),
        (
            "Philosophical Epistemology", "양보 / 전환 (Concession)",
            "Despite presenting arguments that were ostensibly lucid and rigorously structured", "표면적 타당성(+) vs 본질적 논리 결함(-)",
            "Despite presenting arguments that were ostensibly lucid and rigorously structured, the philosopher's treatise was ultimately dismissed by his peers as ________ due to unverified empirical premises.",
            "비록 표면상으로는 명료하고 엄격하게 구조화된 논증을 제시했음에도 불구하고, 그 철학자의 논문은 검증되지 않은 경험적 전제 때문에 동료 학자들에 의해 궁극적으로 ________한 것으로 일축되었다.",
            "spurious", ["impeccable", "cogent", "unassailable"],
            [("spurious", "겉만 번드르르한, 거짓된 (adj.)"), ("impeccable", "결점 없는 (adj.)"), ("cogent", "설득력 있는 (adj.)"), ("unassailable", "공격할 수 없는 (adj.)")],
            "Despite(양보)와 ostensibly(표면상)를 통해, 실제로는 결함이 있다는 부정적 단어 spurious(겉만 그럴듯한, 위조의)가 와야 합니다."
        ),
        (
            "Behavioral Economics", "역접 / 대조 (Contrast)",
            "far from acting as dispassionate calculating utility-maximizers", "이론적 합리성 가정(-) ↔ 실제 비합리적 감정 동요(+)",
            "In real-world financial panics, individual market participants, far from acting as dispassionate calculating utility-maximizers, frequently prove to be remarkably ________, swaying impulsively between euphoria and panic.",
            "실제 금융 공황 상황에서 개별 시장 참여자들은 냉철하게 계산하는 효용 극대화자로 행동하기는커녕, 도취감과 공포 사이를 충동적으로 오가며 현저하게 ________함을 자주 드러낸다.",
            "mercurial", ["resolute", "equanimous", "steadfast"],
            [("mercurial", "변덕스러운, 변하기 쉬운 (adj.)"), ("resolute", "단호한 (adj.)"), ("equanimous", "침착한 (adj.)"), ("steadfast", "확고한 (adj.)")],
            "far from acting dispassionately(냉철하기는커녕)와 swaying impulsively(충동적으로 흔들린다)를 통해 '변덕스러운' 뜻의 mercurial이 정답입니다."
        ),
        (
            "Aesthetic Theory & Art History", "역설 / 대조 (Paradox)",
            "Paradoxically, the minimalist sculptor achieved profound emotional resonance through austere restraint", "금욕적 절제(수단) → 역설적 풍요로움(결과)",
            "Paradoxically, the minimalist sculptor achieved profound emotional resonance not through flamboyant ornamentation, but through a rigorous, ________ economy of form that stripped away all extraneous detail.",
            "역설적이게도, 그 미니멀리즘 조각가는 화려한 장식을 통해서가 아니라, 모든 불필요한 세부사항을 제거한 엄격하고 ________ 형태의 경제성을 통해 심오한 정서적 울림을 달성했다.",
            "austere", ["ostentatious", "sumptuous", "baroque"],
            [("austere", "절제된, 소박한, 엄숙한 (adj.)"), ("ostentatious", "과시하는 (adj.)"), ("sumptuous", "호화로운 (adj.)"), ("baroque", "지나치게 장식적인 (adj.)")],
            "not through flamboyant ornamentation(화려한 장식이 아닌)과 stripped away(제거했다)를 통해 검소하고 절제된 austere가 알맞습니다."
        ),
        (
            "Political Philosophy", "외견과 실질의 괴리 (Apparent vs. Real)",
            "While professing an unwavering commitment to democratic egalitarianism, his regime was in reality", "명분(민주적 평등) vs 실재(독재적 권위주의)",
            "While the prime minister publicly professed an unwavering devotion to participatory democracy, his administration's secretive maneuvers revealed a distinctly ________ style of governance.",
            "총리는 대외적으로 참여 민주주의에 대한 확고한 헌신을 공언했지만, 그의 행정부의 은밀한 공작은 명백히 ________ 통치 스타일을 드러냈다.",
            "autocratic", ["collaborative", "libertarian", "pluralistic"],
            [("autocratic", "독재적인, 전제적인 (adj.)"), ("collaborative", "협력적인 (adj.)"), ("libertarian", "자유의지론의 (adj.)"), ("pluralistic", "다원주의적인 (adj.)")],
            "공언한 민주주의와 대비되는 비밀 공작을 벌였으므로 독재적이라는 뜻의 autocratic이 정답입니다."
        ),
        (
            "Evolutionary Anthropology", "통념 반박 (Counter-intuitive Finding)",
            "Although early hominids are conventionally depicted as solitary brutes, fossil sites show", "통념(고립된 야만인) ↔ 실제(이타적 상호 돌봄)",
            "Although popular culture routinely portrays Neanderthals as brutal, unthinking savages, paleolithic burials exhibiting cared-for crippled skeletons suggest they practiced surprisingly ________ social compassion.",
            "대중문화는 네안데르탈인을 일상적으로 잔혹하고 생각 없는 야만인으로 묘사하지만, 부상당한 유골을 돌본 흔적을 보여주는 구석기 매장지는 그들이 놀라울 정도로 ________ 사회적 연민을 실천했음을 시사한다.",
            "altruistic", ["callous", "ruthless", "truculent"],
            [("altruistic", "이타적인 (adj.)"), ("callous", "냉담한 (adj.)"), ("ruthless", "무자비한 (adj.)"), ("truculent", "호전적인 (adj.)")],
            "야만인 묘사와 대조되며 부상자를 돌본 흔적이 있으므로 '이타적인(altruistic)'이 정답입니다."
        ),
        (
            "Sociology of Science", "관료제적 경직성 (Institutional Inertia)",
            "Rather than fostering revolutionary interdisciplinary inquiry, bureaucratic grant committees favor", "혁신적 모험(-) ↔ 안전하고 진부한 연구 선호(+)",
            "Rather than actively encouraging revolutionary paradigms, peer-review committees dominated by senior academics often demonstrate a regrettable bias toward safe, ________ research proposals.",
            "선임 학자들이 지배하는 동료 평가 위원회는 혁신적인 패러다임을 적극적으로 장려하기보다는 안전하고 ________ 연구 제안서에 대해 유감스러운 편향을 자주 드러낸다.",
            "pedestrian", ["groundbreaking", "unprecedented", "trailblazing"],
            [("pedestrian", "진부한, 평범한, 보행자의 (adj.)"), ("groundbreaking", "획기적인 (adj.)"), ("unprecedented", "전례 없는 (adj.)"), ("trailblazing", "선구적인 (adj.)")],
            "혁신을 피하고 안전한 것만 선호하므로 평범하고 진부하다는 뜻의 pedestrian이 와야 합니다."
        ),
        (
            "Literary Criticism", "외유내강의 문체 (Stylistic Paradox)",
            "Beneath the seemingly effortless, casual simplicity of her prose lies an extraordinarily", "겉모습(소박하고 무심함) ↔ 내면(치밀하고 정교한 계산)",
            "Beneath the deceptively casual simplicity of the author's narrative prose lies an extraordinarily ________ architectonic design that balances every thematic leitmotif with mathematical precision.",
            "그 작가의 서사 산문이 지닌 겉보기의 무심한 소박함 이면에는 모든 주제적 유도동기를 수학적 정밀성으로 균형 맞추는 대단히 ________ 구조적 설계가 숨겨져 있다.",
            "meticulous", ["haphazard", "cursory", "slipshod"],
            [("meticulous", "세심한, 꼼꼼한 (adj.)"), ("haphazard", "우연한, 두서없는 (adj.)"), ("cursory", "대충 하는 (adj.)"), ("slipshod", "엉성한 (adj.)")],
            "수학적 정밀성을 갖춘 치밀한 설계를 나타내므로 meticulous가 정답입니다."
        ),
        (
            "Historical Historiography", "수정주의 역사학 (Revisionist History)",
            "Far from being an uninterrupted era of peaceful cultural flourishing, the reign was in reality marred by", "통념(평화와 번영) vs 실재(지속적 반란과 탄압)",
            "Far from being an idyllic golden age of artistic serenity, the emperor's celebrated reign was, in historical reality, ________ by chronic peasant revolts and relentless palace purges.",
            "예술적 평온함의 목가적인 황금기와는 거리가 멀게도, 그 황제의 찬양받는 통치기는 역사적 실재에 있어서 만성적인 농민 반란과 가혹한 궁정 숙청으로 ________ 상태였다.",
            "marred", ["ennobled", "sanctified", "embellished"],
            [("marred", "손상된, 얼룩진 (adj.)"), ("ennobled", "고결해진 (adj.)"), ("sanctified", "신성화된 (adj.)"), ("embellished", "미화된 (adj.)")],
            "황금기라는 통념과 달리 반란과 숙청으로 '얼룩지고 훼손되었다(marred)'가 맞습니다."
        ),
        # 11..20
        (
            "Clinical Psychology", "감정 억압의 역설 (Emotional Repression)",
            "While suppressing painful trauma may provide temporary emotional anesthesia, it ultimately leads to", "단기적 회피(+) vs 장기적 증상 악화(-)",
            "While psychic denial may offer fleeting solace to an overwhelmed mind, the prolonged repression of acute trauma invariably leads to ________ neurotic symptoms that resurface uncontrollably.",
            "심리적 부인이 압도된 마음에 덧없는 위안을 제공할 수는 있지만, 극심한 트라우마의 장기적인 억압은 통제할 수 없이 다시 수면 위로 떠오르는 ________ 신경증적 증상으로 불가피하게 이어진다.",
            "debilitating", ["therapeutic", "benign", "curative"],
            [("debilitating", "쇠약하게 만드는 (adj.)"), ("therapeutic", "치료의 (adj.)"), ("benign", "무해한, 양성의 (adj.)"), ("curative", "치유적인 (adj.)")],
            "억압이 결국 통제 불능의 해로운 증상으로 이어지므로 debilitating(쇠약하게 만드는)이 맞습니다."
        ),
        (
            "Microeconomic Theory", "베블런 효과 (Conspicuous Consumption)",
            "Contrary to the standard law of demand where higher prices discourage consumption, luxury goods exhibit", "표준 수요 법칙(가격 상승 시 수요 감소) ↔ 과시적 소비(가격 상승 시 수요 증가)",
            "Defying the classical economic axiom that escalating prices suppress market demand, premier luxury fashion labels enjoy a ________ surge in sales as their exorbitant price tags heighten social prestige.",
            "가격 상승이 시장 수요를 억제한다는 고전 경제학적 공리를 무시한 채, 최고급 명품 패션 브랜드들은 터무니없는 가격표가 사회적 명성을 높여줌에 따라 판매량의 ________ 급증을 누린다.",
            "paradoxical", ["predictable", "customary", "prosaic"],
            [("paradoxical", "역설적인 (adj.)"), ("predictable", "예측 가능한 (adj.)"), ("customary", "관례적인 (adj.)"), ("prosaic", "평범한 (adj.)")],
            "고전 공리를 거스르는 반직관적 현상이므로 '역설적인(paradoxical)'이 정답입니다."
        ),
        (
            "Environmental Ethics", "단기 편익과 장기 파멸 (Tragedy of the Commons)",
            "Although strip mining yields immense immediate financial windfalls, it leaves behind an ecologically", "단기 이익(+) vs 영구적 생태 파괴(-)",
            "Although mountaintop removal mining yields immense immediate revenues for extraction syndicates, it leaves behind an ecologically ________ wasteland stripped of all biodiversity.",
            "비록 산꼭대기 제거 채굴이 채굴 신디케이트에 막대한 즉각적 수익을 가져다주지만, 그것은 모든 생물 다양성이 박탈된 생태학적으로 ________ 황무지를 남겨놓는다.",
            "desolate", ["fertile", "resilient", "pristine"],
            [("desolate", "황량한, 적막한 (adj.)"), ("fertile", "비옥한 (adj.)"), ("resilient", "회복력 있는 (adj.)"), ("pristine", "자연 그대로의 (adj.)")],
            "수익은 크지만 남겨진 땅은 생물다양성이 사라진 '황량한(desolate)' 땅입니다."
        ),
        (
            "Linguistic Relativity", "언어와 사고의 관계 (Sapir-Whorf Hypothesis)",
            "While extreme linguistic determinism has been discredited, weak linguistic relativity remains an intriguing and", "극단적 결정론 기각(-) ↔ 온건한 가설의 유효성(+)",
            "Although linguists have largely repudiated the rigid claim that language strictly imprisons cognitive thought, milder formulations of linguistic relativity remain an intellectually ________ hypothesis.",
            "언어학자들이 언어가 인지적 사고를 엄격하게 감금한다는 경직된 주장은 대체로 거부해 왔지만, 언어 상대성의 더 온건한 명제들은 지적으로 여전히 ________ 가설로 남아 있다.",
            "defensible", ["untenable", "preposterous", "ludicrous"],
            [("defensible", "옹호 가능한, 타당한 (adj.)"), ("untenable", "방어할 수 없는 (adj.)"), ("preposterous", "터무니없는 (adj.)"), ("ludicrous", "익살맞은, 가소로운 (adj.)")],
            "극단적 주장은 거부되었지만 온건한 버전은 '여전히 타당하고 옹호 가능하다(defensible)'가 자연스럽습니다."
        ),
        (
            "Architecture & Urbanism", "모더니즘 도시계획의 비판 (Jane Jacobs' Critique)",
            "Ostensibly designed to impose geometric order and hygienic efficiency, brutalist superblocks in fact created", "표면적 목적(기하학적 질서) vs 실제 결과(황량하고 적대적인 공간)",
            "Ostensibly constructed to promote sanitation and geometric order, mid-century residential superblocks in fact generated deeply ________ public spaces that discouraged casual neighborhood interaction.",
            "표면상으로는 위생과 기하학적 질서를 증진하기 위해 건설되었지만, 20세기 중반의 주거용 수퍼블록은 사실 일상적인 이웃 간 상호작용을 저해하는 지극히 ________ 공공 공간을 만들어냈다.",
            "inhospitable", ["welcoming", "genial", "gregarious"],
            [("inhospitable", "불친절한, 황량한 (adj.)"), ("welcoming", "반기는 (adj.)"), ("genial", "친절한 (adj.)"), ("gregarious", "사교적인 (adj.)")],
            "이웃 간 교류를 저해했으므로 황량하고 삭막하다는 뜻의 inhospitable이 정답입니다."
        ),
        (
            "Ethics of Artificial Intelligence", "알고리즘 공정성의 환상 (Algorithmic Bias)",
            "While automated algorithms are celebrated for eliminating subjective human prejudice, they often covertly", "표면적 명분(인간 편견 제거) vs 실제 결과(기존 편견 강화 및 재생산)",
            "While automated predictive models are frequently marketed as objective mathematical arbiters, they often covertly ________ historical societal inequalities encoded within training data.",
            "자동화된 예측 모델은 객관적인 수학적 중재자로 자주 마케팅되지만, 훈련 데이터 내에 인코딩된 역사적인 사회적 불평등을 은밀하게 ________하는 경우가 많다.",
            "perpetuate", ["eradicate", "extinguish", "rectify"],
            [("perpetuate", "영속시키다, 지속시키다 (v.)"), ("eradicate", "근절하다 (v.)"), ("extinguish", "소멸시키다 (v.)"), ("rectify", "바로잡다 (v.)")],
            "객관적이라는 홍보와 달리 불평등을 '영속시킨다(perpetuate)'가 기술비평의 핵심 논지입니다."
        ),
        (
            "Immunology & Autoimmunity", "자가면역 질환의 역설 (Autoimmune Paradox)",
            "Instead of defending host tissues against lethal pathogens, a malfunctioning immune system will attack", "정상 기능(외인성 병원체 방어) ↔ 질환 상태(자기 조직 파괴)",
            "In patients suffering from lupus, the adaptive immune apparatus, instead of directing its firepower exclusively against external microbes, begins to produce antibodies that ________ the body's own vital organs.",
            "루푸스 환자에게서 적응 면역 기구는 자신의 화력을 외부 미생물에만 독점적으로 겨냥하는 대신, 신체 자체의 중요한 장기를 ________하는 항체를 생산하기 시작한다.",
            "assail", ["bolster", "nurture", "succor"],
            [("assail", "공격하다 (v.)"), ("bolster", "강화하다 (v.)"), ("nurture", "육성하다 (v.)"), ("succor", "구호하다 (v.)")],
            "외부 균이 아닌 신체 자체 장기를 '공격한다(assail)'가 자가면역 질환의 본질입니다."
        ),
        (
            "International Diplomacy", "외교적 벼랑끝 전술 (Brinkmanship Risks)",
            "Although aggressive brinkmanship can force immediate concessions, it inherently heightens the danger of", "단기 양보 획득(+) vs 파국적 오판 위험 증가(-)",
            "Although diplomatic brinkmanship can occasionally coerce a reluctant rival into immediate concessions, it inherently escalates the catastrophic hazard of ________ warfare triggered by strategic miscalculation.",
            "비록 외교적 벼랑끝 전술이 내키지 않아 하는 라이벌을 강압하여 즉각적인 양보를 이끌어낼 수 있지만, 그것은 전략적 오판으로 촉발되는 ________ 전쟁이라는 파국적 위험을 본질적으로 고조시킨다.",
            "inadvertent", ["premeditated", "intentional", "calculated"],
            [("inadvertent", "의도치 않은, 우발적인 (adj.)"), ("premeditated", "계획된 (adj.)"), ("intentional", "의도적인 (adj.)"), ("calculated", "계산된 (adj.)")],
            "오판(miscalculation)에 의해 발생하는 전쟁이므로 '의도치 않은, 우발적인(inadvertent)'이 맞습니다."
        ),
        (
            "Intellectual History", "학문적 분과화 비판 (Academic Siloing)",
            "While hyper-specialization produces meticulous domain-specific insights, it often breeds an intellectual", "지나친 세분화(+) vs 시야 협소화(-)",
            "While extreme academic specialization yields extraordinarily detailed domain expertise, it all too frequently fosters a narrow, ________ intellectual parochialism that ignores broad interdisciplinary synthesis.",
            "극단적인 학문적 전문화는 유난히 상세한 영역별 전문지식을 낳지만, 광범위한 학제간 융합을 무시하는 좁고 ________ 지적 편협성을 너무나 자주 조장한다.",
            "myopic", ["far-sighted", "comprehensive", "ecumenical"],
            [("myopic", "근시안적인 (adj.)"), ("far-sighted", "원시안적인 (adj.)"), ("comprehensive", "포괄적인 (adj.)"), ("ecumenical", "보편적인 (adj.)")],
            "넓은 융합을 무시하는 좁은 편협성이므로 근시안적인 myopic이 정답입니다."
        ),
        (
            "Economic History", "네덜란드 병 (The Dutch Disease)",
            "A sudden bonanza in natural gas extraction, rather than enriching all sectors, paradoxically", "자원 발견 횡재(+) ↔ 제조업 공동화 및 경제 왜곡(-)",
            "The unexpected discovery of vast offshore petroleum reserves, far from enriching the entire national economy, frequently triggers the 'Dutch Disease' by severely ________ the nation's domestic manufacturing exports.",
            "거대한 해양 석유 매장량의 예상치 못한 발견은 전체 국가 경제를 부유하게 만들기는커녕, 자국의 국내 제조업 수출을 심각하게 ________함으로써 종종 '네덜란드 병'을 촉발한다.",
            "crippling", ["invigorating", "subsidizing", "propping"],
            [("crippling", "무력화하는, 마비시키는 (adj.)"), ("invigorating", "활력을 불어넣는 (adj.)"), ("subsidizing", "보조금을 주는 (adj.)"), ("propping", "받쳐주는 (adj.)")],
            "통화 강세로 인해 국내 제조업을 '무력화/마비시킨다(crippling)'가 네덜란드병의 정형화된 모델입니다."
        ),
        # 21..30
        (
            "Philosophy of Mind", "의식의 환원주의 비판 (Hard Problem of Consciousness)",
            "Neuroscience can map physical synapses, but subjective qualia remain profoundly", "물리적 신경 지도 완성(+) vs 주관적 체험의 수수께끼(-)",
            "Although contemporary neuroimaging can comprehensively chart neural firing across the cerebral cortex, the qualitative essence of subjective experience remains stubbornly ________ to purely physicalist reduction.",
            "비록 현대의 뇌영상 기술이 대뇌 피질 전반에 걸친 신경 발화를 종합적으로 지도화할 수 있지만, 주관적 경험의 질적 본질은 순수한 물리주의적 환원에 완강하게 ________ 상태로 남아 있다.",
            "impervious", ["yielding", "amenable", "susceptible"],
            [("impervious", "통하지 않는, 굴하지 않는 (adj.)"), ("yielding", "순응하는 (adj.)"), ("amenable", "순종하는 (adj.)"), ("susceptible", "영향을 받기 쉬운 (adj.)")],
            "아무리 물리적 지도를 그려도 주관적 의식은 물리주의적 환원에 '굴하지 않고 통하지 않는다(impervious to)'가 맞습니다."
        ),
        (
            "Evolutionary Ecology", "성선택과 공작의 꼬리 (Handicap Principle)",
            "The peacock's extravagant plumage, while impairing aerodynamic escape, serves as a reliable signal because", "생존상 불리함(-) ↔ 짝짓기상 우수 유전자 입증(+)",
            "A peacock's massive train of decorative feathers, while undeniably a physical ________ when fleeing terrestrial predators, paradoxically signals genetic fitness precisely because surviving with such a burden is difficult.",
            "공작새의 거대한 장식용 깃털은 육상 포식자로부터 도망칠 때 명백히 신체적 ________임에도 불구하고, 그러한 부담을 안고 생존하는 것 자체가 어렵기 때문에 역설적으로 유전적 적합성을 알린다.",
            "handicap", ["boon", "asset", "catalyst"],
            [("handicap", "핸디캡, 불리한 조건 (n.)"), ("boon", "은혜, 혜택 (n.)"), ("asset", "자산 (n.)"), ("catalyst", "촉매 (n.)")],
            "도망칠 때는 '핸디캡/불리함(handicap)'이지만 역설적으로 유전적 강인함을 증명합니다."
        ),
        (
            "Corporate Culture", "단기 실적주의 비판 (Quarterly Capitalism)",
            "Fixating on quarterly profits incentivizes myopic cost-cutting that undermines", "단기 실적 집착(+) vs 장기 연구개발 역량 훼손(-)",
            "Executive compensation schemes tethered exclusively to short-term earnings encourage managers to make decisions that, while boosting immediate shareholder dividends, irrevocably ________ long-term research innovation.",
            "단기 수익에만 배타적으로 연계된 임원 보수 제도는 즉각적인 주주 배당금을 늘려주는 반면, 장기적인 연구 혁신을 돌이킬 수 없이 ________하는 결정을 내리도록 관리자들을 부추긴다.",
            "sabotage", ["foster", "propagate", "nurture"],
            [("sabotage", "파괴하다, 망치다 (v.)"), ("foster", "조성하다 (v.)"), ("propagate", "증식하다 (v.)"), ("nurture", "양육하다 (v.)")],
            "단기 배당을 올리는 대신 장기 혁신을 '망쳐놓는다(sabotage)'가 대조를 이룹니다."
        ),
        (
            "Biomedical Ethics", "유전자 편집의 윤리적 딜레마 (CRISPR Eugenics)",
            "While somatic editing eliminates hereditary agony, germline modifications raise fears of", "치료적 편익(+) vs 우생학적 변형에 대한 공포(-)",
            "While gene therapy for debilitating sickle cell anemia offers immense humanitarian relief, unregulated germline alterations evoke widespread dread of a dystopian future marred by genetic ________.",
            "쇠약하게 만드는 겸상 적혈구 빈혈에 대한 유전자 치료가 엄청난 인도주의적 안도를 제공하는 반면, 규제되지 않은 생식세포 변형은 유전적 ________으로 얼룩진 디스토피아적 미래에 대한 광범위한 공포를 불러일으킨다.",
            "stratification", ["egalitarianism", "solidarity", "harmony"],
            [("stratification", "계층화, 계급 분화 (n.)"), ("egalitarianism", "평등주의 (n.)"), ("solidarity", "연대 (n.)"), ("harmony", "조화 (n.)")],
            "유전자 조작을 누릴 수 있는 부유층과 그렇지 못한 계층 사이의 '유전적 계층화(stratification)'가 윤리학의 주된 우려입니다."
        ),
        (
            "Astrophysics & Cosmology", "암흑 물질의 수수께끼 (Dark Matter Invisibility)",
            "Dark matter exerts undeniable gravitational pull across galaxies, yet it remains completely", "중력적 실재성(+) vs 전자기적 불가시성(-)",
            "Although dark matter constitutes roughly eighty-five percent of all cosmic matter and gravitationally anchors galaxies, it remains completely ________ to direct electromagnetic observation.",
            "비록 암흑 물질이 전체 우주 물질의 약 85%를 구성하며 은하들을 중력적으로 붙들어 매고 있지만, 그것은 직접적인 전자기적 관측에는 완전히 ________ 상태로 남아 있다.",
            "elusive", ["manifest", "patent", "conspicuous"],
            [("elusive", "파악하기 힘든, 피하는 (adj.)"), ("manifest", "명백한 (adj.)"), ("patent", "명백한 (adj.)"), ("conspicuous", "눈에 띄는 (adj.)")],
            "우주의 대다수를 차지함에도 직접 관측으로는 '포착되지 않고 파악하기 힘들다(elusive)'가 정답입니다."
        ),
        (
            "Psychology of Intuition", "직관과 과신 (Overconfidence Bias)",
            "Experienced practitioners pride themselves on gut instincts, yet empirical audits reveal", "직관에 대한 자부심(+) ↔ 실제 빈번한 오류(-)",
            "Seasoned diagnosticians often take pride in their intuitive hunches, yet blinded clinical trials demonstrate that such unreflective gut feelings are shockingly ________ when confronted with atypical pathologies.",
            "노련한 진단가들은 종종 자신의 직관적 예감에 자부심을 가지지만, 맹검 임상 시험은 그러한 성찰 없는 육감이 이례적인 병리 상황에 직면했을 때 충격적으로 ________함을 입증한다.",
            "fallible", ["infallible", "unerring", "impeccable"],
            [("fallible", "오류를 범하기 쉬운 (adj.)"), ("infallible", "틀림이 없는 (adj.)"), ("unerring", "어김없는 (adj.)"), ("impeccable", "완벽한 (adj.)")],
            "자부심과 달리 이례적 상황에서는 '오류를 범하기 쉽다(fallible)'가 맞습니다."
        ),
        (
            "Art Conservation", "고전 유물의 과도한 복원 (Over-restoration)",
            "Aiming to restore original brilliance, aggressive chemical cleanings often accidentally", "빛나는 복원 의도(+) vs 원작의 역사적 고색 박탈(-)",
            "Intending to restore a Renaissance fresco to its pristine luminosity, overzealous conservators used harsh alkaline solvents that accidentally ________ delicate surface glazes applied by the master's own hand.",
            "르네상스 프레스코화를 원초적인 광채로 복원하고자 의도했던 지나치게 열성적인 보존가들은 거친 알칼리 용제를 사용하여 거장의 손으로 직접 칠해진 섬세한 표면 유약을 뜻하지 않게 ________해 버렸다.",
            "effaced", ["burnished", "fortified", "embellished"],
            [("effaced", "지워버린, 삭제한 (adj./v.)"), ("burnished", "광택을 낸 (adj.)"), ("fortified", "강화한 (adj.)"), ("embellished", "꾸민 (adj.)")],
            "독한 용제로 유약을 뜻하지 않게 '지워버렸다(effaced)'가 맞습니다."
        ),
        (
            "Political Rhetoric", "선동 정치의 어휘 (Demagogic Simplification)",
            "Complex socioeconomic dilemmas cannot be addressed by soundbites, yet demagogues offer", "복잡다단한 현실 문제(-) ↔ 선동가의 단순한 만병통치약 제안(+)",
            "Confronted by multi-layered economic stagnation that defies facile remedies, populist demagogues invariably exploit public frustration by peddling deceptively ________ slogans that apportion blame to scapegoats.",
            "손쉬운 처방을 거부하는 다층적인 경제 침체에 직면하여, 포퓰리스트 선동가들은 희생양에게 비난을 돌리는 기만적으로 ________ 슬로건을 퍼뜨림으로써 대중의 좌절감을 언제나 악용한다.",
            "simplistic", ["nuanced", "sophisticated", "erudite"],
            [("simplistic", "지나치게 단순화한 (adj.)"), ("nuanced", "미묘한 차이가 있는 (adj.)"), ("sophisticated", "정교한 (adj.)"), ("erudite", "학식 있는 (adj.)")],
            "복잡한 문제를 희생양 하나로 퉁치는 '단순화된(simplistic)' 슬로건입니다."
        ),
        (
            "Ecological Resilience", "단일 품종 재배의 취약성 (Monoculture Vulnerability)",
            "Vast uniform monocultures appear remarkably productive, yet they are biologically", "외형적 높은 생산성(+) vs 전염병에 대한 전멸 위험(-)",
            "Vast contiguous agricultural fields planted with genetically identical Cavendish banana clones, while optimizing harvesting mechanization, remain acutely ________ to virulent fungal blight.",
            "유전적으로 동일한 캐번디시 바나나 복제본으로 심어진 광대한 인접 농경지는 수확 기계화를 최적화하는 반면, 치명적인 곰팡이 마름병에 극도로 ________ 상태로 남아 있다.",
            "vulnerable", ["impervious", "resilient", "resistant"],
            [("vulnerable", "취약한 (adj.)"), ("impervious", "통하지 않는 (adj.)"), ("resilient", "탄력 있는 (adj.)"), ("resistant", "저항력 있는 (adj.)")],
            "유전적 다양성이 없어 질병에 '취약하다(vulnerable)'가 정답입니다."
        ),
        (
            "Sociology of Law", "법률의 의도치 않은 역효과 (Perverse Incentives)",
            "Stiff statutory penalties intended to deter minor theft ended up creating", "범죄 억제 목적(+) vs 더 큰 중범죄 유발이라는 역효과(-)",
            "Mandatory minimum sentencing statutes, while enacted to deter organized criminality, paradoxically produced a perverse incentive that ________ convicts from confessing or collaborating with prosecutors.",
            "의무적 최저 형량 법률은 조직 범죄를 저지하기 위해 제정되었지만, 역설적으로 죄수들이 자백하거나 검찰과 협력하는 것을 ________하는 왜곡된 인센티브를 낳았다.",
            "dissuaded", ["impelled", "incentivized", "galvanized"],
            [("dissuaded", "단념시킨 (adj./v.)"), ("impelled", "촉구한 (adj.)"), ("incentivized", "동기를 부여한 (adj.)"), ("galvanized", "자극한 (adj.)")],
            "협력을 이끌어내기는커녕 단념시켰으므로 dissuaded가 맞습니다."
        ),
        # 31..40
        (
            "Philosophy of Language", "의사소통의 관용어 (Idiomatic Opacity)",
            "Literal semantic translation yields gibberish because colloquial idioms are culturally", "글자 그대로의 번역 실패(-) ↔ 문화적으로 특정화된 표현(+)",
            "Machine translation software frequently falters when interpreting colloquial vernacular because metaphorical idioms are culturally ________, defying word-for-word algorithmic substitution.",
            "기계 번역 소프트웨어는 구어체 방언을 해석할 때 자주 비틀거리는데, 그 이유는 은유적 관용구가 문화적으로 ________하여 단어 대 단어의 알고리즘적 대체를 거부하기 때문이다.",
            "idiosyncratic", ["universal", "standardized", "ubiquitous"],
            [("idiosyncratic", "특이한, 고유한 (adj.)"), ("universal", "보편적인 (adj.)"), ("standardized", "표준화된 (adj.)"), ("ubiquitous", "도처에 존재하는 (adj.)")],
            "일대일 번역이 안 되는 이유는 문화적으로 '고유하고 특이하기(idiosyncratic)' 때문입니다."
        ),
        (
            "Economic History", "금본위제의 경직성 (Gold Standard Rigidity)",
            "While gold backing prevented arbitrary inflation, it severely constrained policy during", "물가 안정(+) vs 대공황 시기 경기부양 불능(-)",
            "While an orthodox gold standard successfully anchored long-term monetary expectations, it proved disastrously ________ during liquidity panics by preventing central banks from expanding credit.",
            "정통 금본위제가 장기적인 화폐 기대를 성공적으로 고정시켰던 반면, 중앙은행이 신용을 팽창시키는 것을 막음으로써 유동성 공황 동안에는 재앙적으로 ________함이 입증되었다.",
            "inflexible", ["adaptable", "elastic", "versatile"],
            [("inflexible", "융통성 없는, 경직된 (adj.)"), ("adaptable", "적응할 수 있는 (adj.)"), ("elastic", "탄력적인 (adj.)"), ("versatile", "다재다능한 (adj.)")],
            "위기 시 통화를 풀지 못해 '융통성 없고 경직되었다(inflexible)'가 맞습니다."
        ),
        (
            "Developmental Psychology", "지나친 과보호의 부작용 (Helicopter Parenting)",
            "Parents who shield children from every hardship inadvertently cultivate fragility rather than", "모든 역경 차단(+) ↔ 회복탄력성 대신 나약함 육성(-)",
            "Parents who compulsively insulate their offspring from the slightest disappointment or adversity inadvertently cultivate emotional fragility rather than fostering psychological ________.",
            "자녀를 사소한 실망이나 역경으로부터 강박적으로 차단하는 부모들은 심리적 ________을 함양하기보다는 뜻하지 않게 정서적 취약성을 키우게 된다.",
            "resilience", ["debility", "impotence", "frailty"],
            [("resilience", "회복탄력성, 회복력 (n.)"), ("debility", "쇠약 (n.)"), ("impotence", "무력함 (n.)"), ("frailty", "취약성 (n.)")],
            "취약성(fragility)과 대비되는 '회복탄력성(resilience)'이 와야 합니다."
        ),
        (
            "Urban Architecture", "젠트리피케이션의 양면성 (Gentrification Discontent)",
            "Real estate investment revitalizes dilapidated facades, yet it inexorably displaces", "도시 미관 개선(+) vs 저소득층 원주민 축출(-)",
            "While urban renewal capital investments renovate crumbling tenement facades, they all too often unleash gentrification pressures that forcibly ________ marginalized, long-term working-class residents.",
            "도시 재생 자본 투자가 무너져가는 연립주택의 외관을 개보수하는 반면, 그것은 소외된 오랜 노동계층 주민들을 강제로 ________하는 젠트리피케이션 압력을 너무나 자주 촉발한다.",
            "displace", ["accommodate", "harbor", "domicile"],
            [("displace", "쫓아내다, 이전시키다 (v.)"), ("accommodate", "수용하다 (v.)"), ("harbor", "숨겨주다 (v.)"), ("domicile", "거주하게 하다 (v.)")],
            "임대료 상승으로 원주민을 밖으로 '쫓아낸다(displace)'가 사회학적 현실입니다."
        ),
        (
            "Neuroethics", "기억 소거 약물의 윤리성 (Memory Dampening Drugs)",
            "Erasing traumatic memories alleviates severe PTSD, but critics argue it impairs", "고통 완화 편익(+) vs 정체성과 도덕적 성장 훼손(-)",
            "Although pharmacological memory dampening agents offer therapeutic relief for debilitating grief, bioethicists caution that selectively extinguishing painful recollections may compromise personal ________.",
            "쇠약하게 만드는 비통함에 대해 약리학적 기억 완화제가 치료적 안도를 제공하지만, 생명윤리학자들은 고통스러운 회상을 선별적으로 지우는 것이 개인의 ________을 손상시킬 수 있다고 경고한다.",
            "authenticity", ["falsity", "duplicity", "spuriousness"],
            [("authenticity", "진정성 (n.)"), ("falsity", "허위 (n.)"), ("duplicity", "이중성 (n.)"), ("spuriousness", "가짜임 (n.)")],
            "인간의 삶의 진정한 의미와 기억을 지키는 '진정성(authenticity)'을 훼손할 수 있습니다."
        ),
        (
            "Evolutionary Paleontology", "단속평형설 (Punctuated Equilibrium)",
            "Fossil lineages exhibit long stretches of morphological stasis interrupted by rapid bursts of", "수백만 년 정체(stasis) ↔ 급격한 분화 폭발",
            "Stephen Jay Gould argued that evolution does not proceed through sluggish, continuous gradations, but rather through protracted equilibrium punctuated by brief geologically rapid episodes of ________ speciation.",
            "스티븐 제이 굴드는 진화가 느리고 연속적인 점진성을 통해 진행되는 것이 아니라, 지질학적으로 신속한 짧은 ________ 종 분화 사건들에 의해 중단되는 장기간의 평형 상태를 통해 진행된다고 주장했다.",
            "explosive", ["lethargic", "stagnant", "dormant"],
            [("explosive", "폭발적인, 급격한 (adj.)"), ("lethargic", "무기력한 (adj.)"), ("stagnant", "정체된 (adj.)"), ("dormant", "휴면 상태의 (adj.)")],
            "평형을 깨뜨리는 급격하고 '폭발적인(explosive)' 종 분화입니다."
        ),
        (
            "Media Studies", "반향실 효과 (Echo Chambers)",
            "Social media feeds promise diverse connections, yet algorithmic curation creates", "연결성 증대 명분(+) vs 편향된 확증편향의 방호벽(-)",
            "Despite marketing claims that digital platforms foster cosmopolitan understanding, recommendation algorithms overwhelmingly create insular silos that insulate users from ________ perspectives.",
            "디지털 플랫폼이 보편적인 이해를 증진한다는 마케팅 주장에도 불구하고, 추천 알고리즘은 사용자를 ________ 관점으로부터 고립시키는 편협한 고립 공간을 압도적으로 만들어낸다.",
            "divergent", ["homogenous", "consonant", "uniform"],
            [("divergent", "다른, 갈라지는 (adj.)"), ("homogenous", "동질적인 (adj.)"), ("consonant", "일치하는 (adj.)"), ("uniform", "균일한 (adj.)")],
            "자신과 생각이 '다른, 이질적인(divergent)' 관점으로부터 차단합니다."
        ),
        (
            "Historiography of War", "승자의 역사 (Victor's Bias)",
            "Official state archives celebrate triumphal conquests, while systematically expunging", "승리의 찬양(+) vs 패자의 수난 및 학살 기록 말살(-)",
            "Imperial chronicle records invariably celebrate monarchical conquests in glowing epic prose, while deliberately rendering ________ the brutal atrocities inflicted upon subjugated populations.",
            "제국의 연대기 기록들은 군주의 정복 활동을 찬란한 서사 산문으로 예외 없이 찬양하는 반면, 정복당한 민중들에게 가해진 잔혹한 만행은 의도적으로 ________ 상태로 만든다.",
            "invisible", ["conspicuous", "manifest", "salient"],
            [("invisible", "보이지 않는 (adj.)"), ("conspicuous", "눈에 띄는 (adj.)"), ("manifest", "명백한 (adj.)"), ("salient", "두드러진 (adj.)")],
            "패자의 비극은 역사 속에서 의도적으로 '보이지 않게(invisible)' 지워버립니다."
        ),
        (
            "Biochemistry & Pharmacology", "호메시스 효과 (Hormesis)",
            "High doses of radiation prove universally lethal, whereas micro-doses paradoxically", "대량 노출의 치명성(-) ↔ 미량 노출의 방어 기제 자극(+)",
            "In toxicological science, the concept of hormesis posits that while massive exposure to a chemical agent is lethal, minuscule dosages can paradoxically exert a ________ physiological effect by stimulating cellular repair.",
            "독성학에서 호메시스 개념은 화학 물질에 대한 대량 노출이 치명적인 반면, 극미량의 투여량은 세포 복구를 자극함으로써 역설적으로 ________ 생리적 효과를 발휘할 수 있다고 상정한다.",
            "beneficial", ["deleterious", "pernicious", "toxic"],
            [("beneficial", "유익한 (adj.)"), ("deleterious", "해로운 (adj.)"), ("pernicious", "유해한 (adj.)"), ("toxic", "유독한 (adj.)")],
            "대량 투여는 치명적이지만 극미량은 역설적으로 '유익한(beneficial)' 효과를 냅니다."
        ),
        (
            "Philosophy of Technology", "도구주의의 함정 (Technological Determinism)",
            "We imagine we remain sovereign masters of our tools, yet our devices quietly", "인간의 주도권 환상(+) ↔ 도구가 인간의 행동과 사고를 재구성(-)",
            "We flatter ourselves with the comforting illusion that we wield digital gadgets with absolute autonomy, yet the structural affordances of our software quietly ________ our cognitive habits and attention spans.",
            "우리는 절대적인 자율성을 가지고 디지털 기기를 휘두른다는 위안이 되는 착각으로 스스로를 치켜세우지만, 우리 소프트웨어의 구조적 행동 유도성은 우리의 인지적 습관과 주의 지속 시간을 은밀하게 ________한다.",
            "dictate", ["liberate", "emancipate", "unfetter"],
            [("dictate", "명령하다, 좌우하다 (v.)"), ("liberate", "해방하다 (v.)"), ("emancipate", "해방시키다 (v.)"), ("unfetter", "족쇄를 풀다 (v.)")],
            "인간이 주인이 아니라 도구가 인간의 주의력을 '좌우하고 명령한다(dictate)'가 비판 철학의 시각입니다."
        ),
        # 41..50
        (
            "Ecological Succession", "산림 교란의 중요성 (Intermediate Disturbance)",
            "Complete fire suppression produces decadent stagnation, whereas occasional blazes foster", "인위적 완전 차단(정체) ↔ 적절한 교란(다양성 유지)",
            "Conservationists once believed that ecosystems thrive best in perpetual stillness, but field evidence shows that periodic natural disturbances are essential to maintain dynamic biodiversity and prevent ecological ________.",
            "환경보호론자들은 한때 생태계가 영구적인 고요함 속에서 가장 잘 번성한다고 믿었지만, 현장 증거는 주기적인 자연 교란이 역동적인 생물 다양성을 유지하고 생태학적 ________을 방지하는 데 필수적임을 보여준다.",
            "stagnation", ["vitality", "vigor", "proliferation"],
            [("stagnation", "정체, 침체 (n.)"), ("vitality", "활력 (n.)"), ("vigor", "생기 (n.)"), ("proliferation", "급증 (n.)")],
            "주기적 교란이 생태계의 굳어버림과 '정체(stagnation)'를 막아줍니다."
        ),
        (
            "Literary Aesthetics", "열린 결말의 힘 (Ambiguity in Fiction)",
            "Rather than tidily resolving all narrative conflicts, master novelists often embrace", "깔끔한 결말 지양(-) ↔ 여운을 남기는 모호성 수용(+)",
            "Rather than wrapping up the protagonist's moral dilemmas with an artificial, tidy denouement, the novelist concluded the story with a poignant ________ that leaves the ultimate ethical judgment to the reader.",
            "주인공의 도덕적 딜레마를 인위적이고 깔끔한 대단원으로 마무리하기보다는, 그 소설가는 궁극적인 윤리적 판단을 독자에게 맡기는 가슴 저린 ________으로 이야기를 끝맺었다.",
            "ambiguity", ["certainty", "dogmatism", "finality"],
            [("ambiguity", "모호성 (n.)"), ("certainty", "확실성 (n.)"), ("dogmatism", "독단주의 (n.)"), ("finality", "최종성 (n.)")],
            "독자에게 판단을 맡기는 열린 결말이므로 '모호성(ambiguity)'이 맞습니다."
        ),
        (
            "Cultural Anthropology", "선물의 호혜성 (Mauss's Gift Economy)",
            "A gift is ostensibly presented without expectation, yet unwritten social norms make return", "표면적 무상 증여(+) ↔ 보이지 않는 답례의 강제성(-)",
            "In archaic gift economies, while an exchange is formally celebrated as voluntary generosity, unwritten cultural codes render a reciprocal counter-gift practically ________.",
            "고대 선물 경제에서 교환은 형식적으로는 자발적인 관대함으로 칭송받지만, 불문의 문화적 규약은 상호적인 답례 선물을 실질적으로 ________하게 만든다.",
            "mandatory", ["optional", "discretionary", "superfluous"],
            [("mandatory", "의무적인, 강제적인 (adj.)"), ("optional", "선택적인 (adj.)"), ("discretionary", "자유재량의 (adj.)"), ("superfluous", "불필요한 (adj.)")],
            "자발적이라는 외양과 달리 답례는 반드시 해야 하는 '의무적인(mandatory)' 행위입니다."
        ),
        (
            "Philosophy of Law", "자연법 대 실증법 (Natural Law vs. Legal Positivism)",
            "An authoritarian statute may be procedurally valid, yet morally it remains completely", "형식적 적법성(+) vs 도덕적 정당성의 결여(-)",
            "Natural law jurists insist that a legislative edict enacted by a tyrannical despot, even if procedurally certified by a puppet parliament, remains morally ________ if it violates fundamental human dignity.",
            "자연법 법학자들은 폭군 독재자에 의해 제정된 입법 칙령이 꼭두각시 의회에 의해 절차적으로 공인되었을지라도, 근본적인 인간의 존엄성을 침해한다면 도덕적으로 ________ 상태로 남는다고 주장한다.",
            "illegitimate", ["impeccable", "sanctified", "unassailable"],
            [("illegitimate", "정당하지 못한, 불법의 (adj.)"), ("impeccable", "결점 없는 (adj.)"), ("sanctified", "신성화된 (adj.)"), ("unassailable", "공격할 수 없는 (adj.)")],
            "인간 존엄을 해친다면 절차와 무관하게 도덕적으로 '정당하지 못하다(illegitimate)'가 자연법 사상입니다."
        ),
        (
            "Cognitive Neuroscience", "시각의 구성성 (Constructed Perception)",
            "We assume sight passively mirrors reality, but brain scans prove visual perception is actively", "수동적 거울 반영 환상(-) ↔ 능동적 뇌의 구성 및 예측(+)",
            "Contrary to the intuitive naive-realist assumption that our eyes function like impartial cameras, visual cognition is an actively ________ process where prior expectations shape what we see.",
            "우리의 눈이 공평한 카메라처럼 작동한다는 직관적인 소박 실재론적 가정과는 반대로, 시각 인지는 이전의 기대치가 우리가 보는 것을 형성하는 능동적으로 ________ 과정이다.",
            "constructed", ["passive", "inert", "receptive"],
            [("constructed", "구성된 (adj.)"), ("passive", "수동적인 (adj.)"), ("inert", "비활성의 (adj.)"), ("receptive", "수용적인 (adj.)")],
            "수동적 반영이 아니라 뇌에 의해 능동적으로 '구성된다(constructed)'가 정답입니다."
        ),
        (
            "Macroeconomic Policy", "긴축의 역설 (Paradox of Thrift)",
            "When every family cuts spending during recessions, aggregate demand collapses and economic ruin is", "개인의 절약 미덕(+) ↔ 사회 전체의 총수요 붕괴 및 파멸 가속(-)",
            "During severe economic downturns, individual frugality, while virtuous on a household scale, leads to the macroeconomic paradox where widespread spending cuts ________ systemic unemployment.",
            "심각한 경기 침체 동안 개별적인 검소함은 가계 규모에서는 미덕이지만, 광범위한 지출 삭감이 구조적인 실업을 ________하는 거시경제적 역설로 이어진다.",
            "aggravate", ["mitigate", "alleviate", "quench"],
            [("aggravate", "악화시키다 (v.)"), ("mitigate", "완화하다 (v.)"), ("alleviate", "경감하다 (v.)"), ("quench", "해소하다 (v.)")],
            "지출 감소가 총수요를 위축시켜 실업을 '악화시킨다(aggravate)'가 케인스의 절약의 역설입니다."
        ),
        (
            "Political Sociology", "투표의 역설 (Voter Apathy)",
            "A single vote almost never alters election outcomes, yet democratic institutions collapse without", "개별 표의 미미한 영향력(-) vs 전체 참여의 필수성(+)",
            "Because an individual vote possesses near-zero mathematical probability of swinging a national election, rational-choice theorists find mass electoral turnout ________ without appealing to civic duty.",
            "개별 유권자의 투표가 국가 선거 결과를 뒤바꿀 수학적 확률이 0에 가깝기 때문에, 합리적 선택 이론가들은 시민적 의무감에 호소하지 않고서는 대규모 선거 투표율을 설명하기가 ________함을 발견한다.",
            "inexplicable", ["lucid", "transparent", "coherent"],
            [("inexplicable", "설명할 수 없는 (adj.)"), ("lucid", "명료한 (adj.)"), ("transparent", "투명한 (adj.)"), ("coherent", "일관성 있는 (adj.)")],
            "합리성만으로는 대중의 투표 행위를 '설명할 수 없다(inexplicable)'가 투표의 역설입니다."
        ),
        (
            "Evolutionary Medicine", "알레르기 증가와 위생 가설 (Hygiene Hypothesis)",
            "Hyper-sterile modern homes, far from protecting infants, leave immune systems untrained and", "극도의 무균 환경(-) ↔ 알레르기 과잉 반응 유발(-)",
            "The hygiene hypothesis suggests that hyper-sanitized domestic environments, far from universally protecting infants, leave developing immune systems untrained and prone to ________ inflammatory allergies.",
            "위생 가설은 극도로 소독된 가정 환경이 유아를 보편적으로 보호하기는커녕, 발달 중인 면역 체계를 훈련되지 않은 채로 남겨두어 ________ 염증성 알레르기에 걸리기 쉽게 만든다고 시사한다.",
            "hyperactive", ["dormant", "quiescent", "torpid"],
            [("hyperactive", "과잉 반응하는 (adj.)"), ("dormant", "휴면의 (adj.)"), ("quiescent", "잠잠한 (adj.)"), ("torpid", "무기력한 (adj.)")],
            "무해한 물질에도 면역계가 '과잉 반응하는(hyperactive)' 알레르기입니다."
        ),
        (
            "Historiography", "우연성과 결정론 (Historical Contingency)",
            "Marxist determinists view history as inevitable class struggles, while contingency historians highlight the role of", "역사적 필연론(-) ↔ 돌발적 우연과 개인의 결단(+)",
            "Rejecting sweeping teleological narratives that treat the rise of empires as inevitable, modern historians emphasize the pivotal role of ________ accidents and unpredictable human eccentricities.",
            "제국의 부흥을 불가피한 것으로 취급하는 광범위한 목적론적 서사를 거부하면서, 현대 역사가들은 ________ 우연과 예측 불가능한 인간의 기이한 행동이 지닌 중추적인 역할을 강조한다.",
            "serendipitous", ["preordained", "immutable", "inexorable"],
            [("serendipitous", "우연한, 뜻밖의 (adj.)"), ("preordained", "예정된 (adj.)"), ("immutable", "불변의 (adj.)"), ("inexorable", "거스를 수 없는 (adj.)")],
            "필연론을 거부하므로 '우연한(serendipitous)' 사건의 역할이 강조됩니다."
        ),
        (
            "Art Criticism", "사진술의 등장과 회화의 변화 (Birth of Modern Painting)",
            "Mechanical cameras captured photographic realism, liberating painters to explore", "카메라의 사실적 재현 독점(-) ↔ 회화의 주관적 추상성 해방(+)",
            "When chemical photography rendered literal pictorial reproduction obsolete, it unexpectedly ________ painters from representational duties, enabling the rise of radical expressionism and abstraction.",
            "화학 사진술이 글자 그대로의 시각적 재현을 구식으로 만들었을 때, 그것은 뜻밖에도 화가들을 재현적 의무로부터 ________하여 급진적인 표현주의와 추상화의 발흥을 가능하게 했다.",
            "liberated", ["shackled", "constrained", "subjugated"],
            [("liberated", "해방시킨 (adj./v.)"), ("shackled", "차꼬를 채운 (adj.)"), ("constrained", "제약한 (adj.)"), ("subjugated", "예속시킨 (adj.)")],
            "모사 의무에서 화가를 '해방시켰다(liberated)'가 현대 미술사의 핵심입니다."
        ),
        # 51..60
        (
            "Corporate Strategy", "혁신가의 딜레마 (The Innovator's Dilemma)",
            "Listening loyally to existing high-end customers causes companies to miss disruptive", "기존 고객 만족(+) ↔ 파괴적 저가 혁신 간과(-)",
            "In Christensen's model, market-leading corporations frequently fail not because of managerial incompetence, but because faithful devotion to their most profitable customers blinds them to ________ low-end technological disruptions.",
            "크리스텐슨의 모델에서 시장 선도 기업들은 경영상의 무능 때문이 아니라, 가장 수익성 높은 고객들에 대한 충실한 헌신이 그들로 하여금 ________ 저가 기술 혁신을 보지 못하게 만들기 때문에 실패한다.",
            "nascent", ["mature", "obsolete", "antiquated"],
            [("nascent", "초기의, 태동하는 (adj.)"), ("mature", "성숙한 (adj.)"), ("obsolete", "구식의 (adj.)"), ("antiquated", "시대에 뒤떨어진 (adj.)")],
            "처음에는 조잡해 보이는 '초기의, 태동하는(nascent)' 혁신을 간과합니다."
        ),
        (
            "Ecological Economics", "성장의 한계 (Planetary Boundaries)",
            "Infinite physical expansion on a finite sphere is a mathematical", "유한한 지구 자원(-) ↔ 무한 성장 추구의 모순",
            "Ecological economists argue that industrial capitalism's assumption of perpetual material throughput across a finite biosphere represents an ecological ________.",
            "생태경제학자들은 유한한 생물권 전반에 걸친 영구적인 물질적 산출에 대한 산업 자본주의의 가정이 생태학적 ________을 나타낸다고 주장한다.",
            "impossibility", ["inevitability", "panacea", "truism"],
            [("impossibility", "불가능성 (n.)"), ("inevitability", "불가피성 (n.)"), ("panacea", "만병통치약 (n.)"), ("truism", "자명한 이치 (n.)")],
            "유한한 지구에서 무한 성장은 물리적으로 '불가능함(impossibility)'입니다."
        ),
        (
            "Philosophy of Science", "패러다임 전환과 공약불가능성 (Incommensurability)",
            "Newtonian and Einsteinian physics do not merely differ in equations, their terms are conceptually", "단순 수치 차이(-) ↔ 근본적 세계관 공약불가능성(+)",
            "Thomas Kuhn asserted that competing scientific paradigms cannot be neutrally adjudicated against a shared standard because their foundational conceptual languages are fundamentally ________.",
            "토마스 쿤은 경쟁하는 과학적 패러다임들이 공유된 기준에 비추어 중립적으로 판정될 수 없다고 단언했는데, 그 이유는 그들의 기초적인 개념 언어들이 근본적으로 ________하기 때문이다.",
            "incommensurable", ["interchangeable", "identical", "harmonious"],
            [("incommensurable", "공약 불가능한, 같은 척도로 잴 수 없는 (adj.)"), ("interchangeable", "교환 가능한 (adj.)"), ("identical", "동일한 (adj.)"), ("harmonious", "조화로운 (adj.)")],
            "패러다임 간의 척도가 달라 비교 불가능하다는 뜻의 incommensurable이 정답입니다."
        ),
        (
            "Biosecurity", "이중 용도 연구의 딜레마 (Gain-of-Function Research)",
            "Enhancing viral transmissibility helps develop future vaccines, yet it poses", "미래 예방 편익(+) vs 실험실 유출 시 파국적 참사(-)",
            "Gain-of-function virological research that enhances pathogen lethality presents a terrifying dual-use conundrum: while offering insights into pandemic emergence, it poses an ________ risk of accidental laboratory escape.",
            "병원균의 치사율을 높이는 기능 획득 바이러스 연구는 무서운 이중 용도 딜레마를 제시한다. 즉 팬데믹 출현에 대한 통찰을 제공하는 반면, 우발적인 실험실 유출이라는 ________ 위험을 제기한다.",
            "existential", ["negligible", "trifling", "inconsequential"],
            [("existential", "실존적인, 인류 존망에 관한 (adj.)"), ("negligible", "하찮은 (adj.)"), ("trifling", "사소한 (adj.)"), ("inconsequential", "중요치 않은 (adj.)")],
            "치명적 유출 위험은 인류의 존망이 걸린 '실존적(existential)' 위험입니다."
        ),
        (
            "Social Media Psychology", "디지털 행복감의 기만 (Social Comparison)",
            "Curated feeds showcase glamorous triumphs, fostering feelings of personal", "타인의 하이라이트 과시(+) ↔ 내면의 열등감과 불충분함(-)",
            "Constant immersion in curated lifestyle feeds creates a distorted cognitive benchmark that leads adolescents to feel deeply ________ regarding their own mundane lives.",
            "잘 편집된 라이프스타일 피드에 대한 지속적인 몰입은 청소년들로 하여금 자신의 평범한 삶에 대해 깊이 ________ 느끼도록 이끄는 왜곡된 인지적 기준점을 만들어낸다.",
            "inadequate", ["exalted", "superior", "triumphant"],
            [("inadequate", "불충분한, 부적절한 (adj.)"), ("exalted", "의기양양한 (adj.)"), ("superior", "우월한 (adj.)"), ("triumphant", "승리감에 찬 (adj.)")],
            "타인의 화려한 모습과 비교하여 자신이 '불충분하고 모자라다(inadequate)'고 느낍니다."
        ),
        (
            "Linguistic Anthropology", "사멸 위기 언어와 전통 지식 (Language Extinction)",
            "When an unwritten indigenous tongue dies, irreplaceable botanical and ecological wisdom is", "언어 소멸(-) ↔ 수천 년간 축적된 민간 생태 지식 영구 소실(-)",
            "When an unwritten Amazonian dialect goes extinct, linguists lose more than phonetic patterns; thousands of years of indigenous pharmacopeia and botanical taxonomy are permanently ________.",
            "문자가 없는 아마존 방언이 사멸할 때, 언어학자들은 음성 패턴 이상의 것을 잃게 된다. 즉, 수천 년에 걸친 원주민 약전과 식물 분류학이 영구적으로 ________된다.",
            "lost", ["replicated", "canonized", "archived"],
            [("lost", "상실된, 사라진 (adj.)"), ("replicated", "복제된 (adj.)"), ("canonized", "정전에 오른 (adj.)"), ("archived", "보관된 (adj.)")],
            "문서화되지 않은 구전 지식이 영원히 '상실된다(lost)'가 맞습니다."
        ),
        (
            "Macroeconomic Sanctions", "경제 제재의 인도주의적 역설 (Sanctions Efficacy)",
            "Sanctions intend to punish autocratic rulers, but they often impoverish innocent civilians while leaving dictators", "독재자 처벌 의도(+) vs 서민 피폐 및 독재자 건재(-)",
            "Comprehensive international trade embargos, while designed to weaken despotic regimes, all too often devastate vulnerable civilian populations while leaving the ruling elite relatively ________.",
            "포괄적인 국제 무역 금수 조치는 전제주의 정권을 약화시키기 위해 고안되었지만, 너무나 자주 취약한 민간인들에게 피해를 주는 반면 지배 엘리트들은 상대적으로 ________ 상태로 남겨둔다.",
            "unscathed", ["devastated", "destitute", "ruined"],
            [("unscathed", "상처 없는, 무사한 (adj.)"), ("devastated", "황폐해진 (adj.)"), ("destitute", "빈곤한 (adj.)"), ("ruined", "파멸한 (adj.)")],
            "서민은 고통받지만 지배층은 '다치지 않고 무사하다(unscathed)'가 제재의 역설입니다."
        ),
        (
            "Cognitive Psychology", "선택의 역설 (Paradox of Choice)",
            "Infinite options promise ultimate consumer freedom, yet an overabundance of choices leads to", "선택지 무한 증가(+) ↔ 결정 마비와 만족도 저하(-)",
            "Barry Schwartz demonstrated that offering consumers an overwhelming proliferation of choices, rather than conferring liberating autonomy, frequently induces acute decision ________ and buyer's remorse.",
            "배리 슈워츠는 소비자에게 압도적으로 급증하는 선택지를 제공하는 것이 해방감을 주는 자율성을 부여하기보다는 급성 결정 ________과 구매자의 후회를 자주 유발함을 입증했다.",
            "paralysis", ["alacrity", "agility", "promptness"],
            [("paralysis", "마비 (n.)"), ("alacrity", "민첩함 (n.)"), ("agility", "기민함 (n.)"), ("promptness", "신속함 (n.)")],
            "너무 많은 선택지는 결정을 내리지 못하게 만드는 '결정 마비(paralysis)'를 부릅니다."
        ),
        (
            "Space Exploration", "우주 쓰레기 증후군 (Kessler Syndrome)",
            "Each satellite collision creates shrapnel that increases the likelihood of future", "파편 발생(+) ↔ 연쇄 충돌로 궤도 불능화(-)",
            "The Kessler Syndrome warns that low-Earth orbit may eventually become impassable because dense debris clouds create a catastrophic cascade where each collision ________ future impacts exponentially.",
            "케슬러 증후군은 궤도 내 빽빽한 잔해 구름이 각 충돌이 미래의 충돌을 기하급수적으로 ________하는 파국적인 연쇄 반응을 만들어내어 저궤도가 결국 통과 불가능해질 수 있다고 경고한다.",
            "multiplies", ["dampens", "quells", "extinguishes"],
            [("multiplies", "배가하다, 증식시키다 (v.)"), ("dampens", "꺾다 (v.)"), ("quells", "진압하다 (v.)"), ("extinguishes", "소멸시키다 (v.)")],
            "충돌이 파편을 만들어 다음 충돌 위험을 '증대시킨다(multiplies)'가 맞습니다."
        ),
        (
            "Behavioral Economics", "매몰비용 오류 (Sunk Cost Fallacy)",
            "Pouring resources into a failing project simply because of past investments is a hallmark of", "과거 투자 미련(-) ↔ 합리적 손절 실패 및 추가 낭비(-)",
            "Continuing to channel capital into an unprofitable venture merely to justify prior expenditure is a quintessential manifestation of the sunk cost fallacy, illustrating how past losses can ________ future judgment.",
            "이전의 지출을 정당화하기 위해 수익성 없는 벤처에 자본을 계속 쏟아붓는 것은 매몰비용 오류의 전형적인 발현이며, 과거의 손실이 어떻게 미래의 판단을 ________할 수 있는지를 보여준다.",
            "corrupt", ["clarify", "refine", "purify"],
            [("corrupt", "타락시키다, 왜곡하다 (v.)"), ("clarify", "명확히 하다 (v.)"), ("refine", "정제하다 (v.)"), ("purify", "순화하다 (v.)")],
            "합리적 판단을 흐리고 '왜곡/타락시킨다(corrupt)'가 정답입니다."
        )
    ]

    for idx, d in enumerate(data):
        theme, logicType, clue, direction, question, questionKo, correct, distractors, vocab, explanation = d
        opts = [correct] + distractors
        random.seed(2000 + idx)
        random.shuffle(opts)
        ans = opts.index(correct)
        
        vocab_list = [{"word": w, "meaning": m} for w, m in vocab]
        
        items.append({
            "id": f"tl-{idx+61:03d}",
            "level": 2,
            "levelLabel": "Lv.2 중급",
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
    q = get_level2_questions()
    print(f"Generated {len(q)} Level 2 questions.")
