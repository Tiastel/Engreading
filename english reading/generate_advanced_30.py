# -*- coding: utf-8 -*-
"""
generate_advanced_30.py
Generates 30 Advanced (B2-C1) reading passages with rigorous philosophical, scientific,
and socio-economic themes from premier global publications (Nature, Oxford, NIST, Foreign Affairs).
"""

import json

def build_advanced_dataset():
    p_data = [
        ("a-01", "Epigenetics: Environmental Modulation of the Genome", "후성유전학: 환경이 유전체 발현을 조절하는 기제", "Genetics & Biology", "Nature Genetics",
         "고정된 DNA 염기서열을 넘어, 후성유전학적 표지가 환경적 자극에 반응하여 유전자의 온/오프를 스위칭하는 분자 메커니즘을 규명합니다.",
         [
             ("For decades, classical molecular genetics operated under the deterministic axiom that an organism's biological destiny was rigidly dictated by inherited nucleotide sequences.", "수십 년 동안 고전 분자유전학은 생명체의 생물학적 운명이 유전된 뉴클레오타이드 서열에 의해 완고하게 결정된다는 결정론적 공리 아래 작동했습니다.", "For decades, / classical molecular genetics operated under the deterministic axiom / that an organism's biological destiny / was rigidly dictated by inherited nucleotide sequences."),
             ("However, the burgeoning field of epigenetics has shattered this reductionist paradigm by demonstrating that chromatin structure is remarkably dynamic.", "그러나 급성장하는 후성유전학 분야는 염색질 구조가 놀라울 정도로 역동적임을 입증함으로써 이러한 환원주의적 패러다임을 산산조각 냈습니다.", "However, / the burgeoning field of epigenetics / has shattered this reductionist paradigm / by demonstrating / that chromatin structure is remarkably dynamic."),
             ("Epigenetic mechanisms—chiefly DNA methylation, post-translational histone modifications, and non-coding RNA interference—serve as molecular switches that regulate transcriptional accessibility without altering the underlying genetic code.", "주로 DNA 메틸화, 번역 후 히스톤 변형, 비암호화 RNA 간섭과 같은 후성유전학적 기제들은 근본적인 유전 암호를 바꾸지 않으면서 전사적 접근성을 조절하는 분자 스위치 역할을 합니다.", "Epigenetic mechanisms—chiefly DNA methylation, / post-translational histone modifications, / and non-coding RNA interference— / serve as molecular switches / that regulate transcriptional accessibility / without altering the underlying genetic code."),
             ("Environmental factors such as nutritional deprivation, chronic psychosocial stress, and chemical pollutant exposure leave enduring epigenetic signatures capable of persisting across cellular generations.", "영양 결핍, 만성적인 심리사회적 스트레스, 화학 오염물질 노출과 같은 환경적 요인들은 세포 세대를 거쳐 지속될 수 있는 영구적인 후성유전학적 흔적을 남깁니다.", "Environmental factors / such as nutritional deprivation, / chronic psychosocial stress, / and chemical pollutant exposure / leave enduring epigenetic signatures / capable of persisting across cellular generations."),
             ("Astonishingly, emerging mammalian models indicate that certain environmental perturbations may even transmit transgenerationally through the germline, challenging traditional boundaries between nature and nurture.", "놀랍게도, 새롭게 부상하는 포유류 모델들은 특정한 환경적 교란이 생식세포 계열을 통해 세대를 넘어 전달될 수도 있음을 보여주며, 천성과 양육 사이의 전통적 경계에 도전하고 있습니다.", "Astonishingly, / emerging mammalian models indicate / that certain environmental perturbations / may even transmit transgenerationally through the germline, / challenging traditional boundaries between nature and nurture.")
         ],
         [("deterministic", "adj.", "결정론적인", "Quantum mechanics disrupted classical deterministic views of physics."), ("reductionist", "adj.", "환원주의적인", "Viewing complex consciousness as mere circuitry is overly reductionist."), ("transcriptional", "adj.", "전사의, 유전자 발현의", "Transcription factors govern the rate of messenger RNA synthesis."), ("perturbation", "n.", "교란, 동요", "Small perturbations in ocean currents trigger catastrophic weather shifts."), ("transgenerational", "adj.", "세대를 초월하는", "Transgenerational trauma reverberates across historical epochs.")],
         [("동격의 that절", "the deterministic axiom that an organism's biological destiny was... 추상명사 axiom의 동격절입니다."), ("현재분사 구문 challenging", "...transmit transgenerationally through the germline, challenging traditional... 앞 절의 결과적 함의를 나타냅니다.")],
         [
             ("What foundational assumption did epigenetics overturn?", "후성유전학이 뒤집어엎은 전통적인 기본 가정은 무엇인가요?", ["That DNA was composed of carbon, hydrogen, and oxygen atoms", "That biological traits are strictly preordained by static DNA sequences", "That environmental factors have zero physiological effects during development", "That cells duplicate through binary mitosis and meiosis"], 1, "유전자가 불변의 고정된 서열에 의해서만 생명체의 운명을 결정한다는 고전적 결정론을 뒤집었습니다."),
             ("How do epigenetic mechanisms regulate gene expression without altering base pairs?", "후성유전학적 기제는 염기 서열을 바꾸지 않고 어떻게 유전자 발현을 조절하나요?", ["By physically replacing the entire nucleus with synthetic proteins", "By controlling the transcriptional accessibility of chromatin via chemical tags", "By burning off surplus mitochondrial energy inside chromosomes", "By mutating bacterial plasmids residing within neighboring cells"], 1, "DNA 메틸화와 히스톤 변형을 통해 염색질의 전사적 접근성을 제어하는 분자 스위치로 작용합니다."),
             ("What is the broader philosophical implication of transgenerational epigenetics?", "세대 간 후성유전학이 시사하는 더 넓은 철학적 함의는 무엇인가요?", ["It completely eradicates the concept of personal human agency.", "It blurs the historically entrenched divide between hereditary nature and environmental nurture.", "It proves that organic evolution operates in total reverse chronology.", "It mandates that all living organisms must subsist on inorganic synthetic nutrients."], 1, "선천적 유전(Nature)과 후천적 환경(Nurture) 사이의 전통적 경계를 허물고 있음을 보여줍니다.")
         ]),

        ("a-02", "Algorithmic Governance and Democratic Deliberation", "알고리즘적 거버넌스와 공론장 숙의의 침식", "Political Philosophy & Technology", "Oxford Internet Institute",
         "데이터 중심의 예측 알고리즘이 현대 공공 정책에 도입되면서 발생하는 민주적 숙의의 쇠퇴와 불투명성 문제를 비판적으로 성찰합니다.",
         [
             ("In contemporary democratic governance, public institutions increasingly rely on predictive algorithms to optimize resource allocation, evaluate welfare eligibility, and manage judicial bail determinations.", "현대 민주 거버넌스에서 공공 기관은 자원 배분을 최적화하고, 복지 수급 자격을 평가하며, 사법 보석 결정을 관리하기 위해 예측 알고리즘에 점점 더 의존하고 있습니다.", "In contemporary democratic governance, / public institutions increasingly rely on predictive algorithms / to optimize resource allocation, / evaluate welfare eligibility, / and manage judicial bail determinations."),
             ("While technocratic proponents herald these automated systems as objective antidotes to human cognitive bias and administrative inefficiency, critical theorists warn of severe democratic deficits.", "기술관료적 지지자들은 이러한 자동화 시스템을 인간의 인지 편향과 행정적 비효율에 대한 객관적인 해독제라며 칭송하지만, 비판 이론가들은 심각한 민주적 결손을 경고합니다.", "While technocratic proponents herald these automated systems / as objective antidotes / to human cognitive bias and administrative inefficiency, / critical theorists warn of severe democratic deficits."),
             ("Proprietary machine learning models frequently operate as opaque black boxes, precluding citizens from examining the ethical premises and historical data biases underpinning administrative verdicts.", "독점적인 기계학습 모델은 종종 불투명한 블랙박스로 작동하여, 시민들이 행정적 판결을 뒷받침하는 윤리적 전제와 역사적 데이터 편향을 조사하는 것을 원천 차단합니다.", "Proprietary machine learning models / frequently operate as opaque black boxes, / precluding citizens / from examining the ethical premises / and historical data biases underpinning administrative verdicts."),
             ("Furthermore, by translating contentious political questions into seemingly neutral technical metrics, algorithmic optimization depoliticizes systemic injustices and forecloses public deliberation.", "더욱이, 논쟁적인 정치적 질문을 겉보기에 중립적인 기술 지표로 치환함으로써, 알고리즘 최적화는 구조적 불의를 탈정치화하고 공적 숙의를 봉쇄합니다.", "Furthermore, / by translating contentious political questions / into seemingly neutral technical metrics, / algorithmic optimization depoliticizes systemic injustices / and forecloses public deliberation."),
             ("A robust democracy requires that consequential decisions remain auditable, contested, and subject to transparent collective accountability rather than statistical opacity.", "견고한 민주주의는 중대한 결정들이 통계적 불투명성에 맡겨지기보다, 검증 가능하고, 논쟁될 수 있으며, 투명한 집단적 책임성의 대상이 될 것을 요구합니다.", "A robust democracy requires / that consequential decisions remain auditable, contested, / and subject to transparent collective accountability / rather than statistical opacity.")
         ],
         [("technocratic", "adj.", "기술관료적인", "Technocratic governance often overlooks nuanced public emotion."), ("opaque", "adj.", "불투명한, 이해하기 힘든", "The algorithm's scoring criteria remained entirely opaque."), ("preclude", "v.", "배제하다, 불가능하게 하다", "Severe NDAs preclude researchers from disclosing security flaws."), ("depoliticize", "v.", "탈정치화하다", "Framing poverty as pure mathematics serves to depoliticize structural inequality."), ("auditable", "adj.", "감사 가능한, 검증할 수 있는", "Financial institutions must maintain transparent, auditable records.")],
         [("양보의 부사절 While", "While technocratic proponents herald... critical theorists warn... 서로 대조되는 입장을 이끄는 접속사입니다."), ("동명사 관용구 preclude from -ing", "precluding citizens from examining the ethical premises... 시민들이 조사하는 것을 방지한다는 구문입니다.")],
         [
             ("What argument is presented by critics of algorithmic governance?", "알고리즘 거버넌스를 비판하는 이들이 제시하는 논거는 무엇인가요?", ["Algorithms consume excessive amounts of paper in government archives.", "Proprietary opacity suppresses transparent public debate and entrenches historical bias.", "Automated decisions always cost ten times more than manual civil servants.", "Computers refuse to process criminal justice cases altogether."], 1, "기계학습 모델의 불투명성과 독점성이 시민의 검증과 민주적 숙의를 가로막는다고 비판합니다."),
             ("How does algorithmic framing alter fundamentally political debates?", "알고리즘적 프레이밍은 근본적으로 정치적인 논쟁을 어떻게 변형시키나요?", ["It turns them into global televised sports spectacles.", "It converts deep value disputes into deceptive technical metrics, depoliticizing them.", "It forces parliaments to dissolve completely and surrender power.", "It eliminates all statistical measurements from public health campaigns."], 1, "가치 판단이 필요한 정치적 쟁점을 단순한 기술적 지표로 치환하여 공적 숙의를 봉쇄합니다."),
             ("According to the passage, what standard must critical public decisions uphold?", "지문에 따르면 중대한 공공 결정이 반드시 지켜야 할 기준은 무엇인가요?", ["They must be executed in absolute secrecy by licensed corporations.", "They must remain transparently auditable and subject to collective scrutiny.", "They should prioritize algorithmic computational speed over ethical equity.", "They must be permanently outsourced to non-governmental entities."], 1, "통계적 불투명성에 가려지지 않고 투명하게 검증 및 논쟁될 수 있어야 합니다.")
         ]),

        ("a-03", "Quantum Computing and the Post-RSA Cryptographic Paradigm", "양자 컴퓨팅과 포스트 RSA 암호 패러다임", "Computer Science & Cryptography", "NIST Standards",
         "양자 쇼어 알고리즘이 소인수분해 기반의 현대 공개키 암호체계에 가하는 실존적 위협과 격자 기반 암호학으로의 전환을 분석합니다.",
         [
             ("The architectural foundations of global digital commerce rest overwhelmingly on asymmetric public-key cryptography, predominantly the RSA and elliptic-curve protocols.", "글로벌 전자상거래의 구조적 토대는 비대칭 공개키 암호화, 그중에서도 주로 RSA 및 타원곡선 프로토콜에 압도적으로 의존하고 있습니다.", "The architectural foundations of global digital commerce / rest overwhelmingly / on asymmetric public-key cryptography, / predominantly the RSA and elliptic-curve protocols."),
             ("These ciphers derive their mathematical impregnability from the sheer computational intractability of prime factorization and discrete logarithms on classical Von Neumann architectures.", "이 암호들은 고전 폰 노이만 구조에서 소인수분해와 이산대수의 극심한 계산적 난해함으로부터 수학적 난공불락을 이끌어냅니다.", "These ciphers derive their mathematical impregnability / from the sheer computational intractability / of prime factorization and discrete logarithms / on classical Von Neumann architectures."),
             ("However, the realization of fault-tolerant quantum computers armed with Shor's algorithm threatens to decimate these cryptographic bastions in polynomial time.", "그러나 쇼어 알고리즘을 장착한 결함 허용 양자 컴퓨터의 등장은 다항 시간 내에 이러한 암호학적 요새를 무력화할 위협을 가하고 있습니다.", "However, / the realization of fault-tolerant quantum computers / armed with Shor's algorithm / threatens to decimate these cryptographic bastions / in polynomial time."),
             ("By exploiting quantum superposition and quantum entanglement, Shor's formulation bypasses the exponential trial-and-error barriers that currently protect sovereign communications and financial transfers.", "양자 중첩과 양자 얽힘을 활용함으로써, 쇼어의 공식은 현재 국가 안보 통신과 금융 거래를 보호하는 지수함수적 시행착오의 장벽을 우회합니다.", "By exploiting quantum superposition and quantum entanglement, / Shor's formulation bypasses / the exponential trial-and-error barriers / that currently protect sovereign communications / and financial transfers."),
             ("Anticipating this cryptanalytic apocalypse, standard-setting agencies are desperately orchestrating a wholesale transition toward post-quantum cryptography, specifically lattice-based and isogeny-based algorithms presumed immune to quantum supremacy.", "이러한 암호 해독의 파멸적 전환을 예상하며, 표준 제정 기관들은 양자 우위에도 안전하다고 여겨지는 격자 기반 및 동종사상 기반 알고리즘인 포스트 양자 암호학으로의 전면적인 전환을 필사적으로 기획하고 있습니다.", "Anticipating this cryptanalytic apocalypse, / standard-setting agencies are desperately orchestrating / a wholesale transition toward post-quantum cryptography, / specifically lattice-based and isogeny-based algorithms / presumed immune to quantum supremacy.")
         ],
         [("impregnability", "n.", "난공불락, 확고부동함", "The mountain fortress boasted historic military impregnability."), ("intractability", "n.", "다루기 힘듦, 해결 난해성", "The computational intractability of NP-hard problems perplexes theorists."), ("superposition", "n.", "중첩 (양자역학)", "Qubits exist in a simultaneous superposition of states until measured."), ("entanglement", "n.", "얽힘, 복잡한 연루", "Quantum entanglement enables instantaneous correlations across astronomical distances."), ("cryptanalytic", "adj.", "암호 분석의, 암호 해독의", "The agency deployed state-of-the-art cryptanalytic supercomputers.")],
         [("전치사구 By exploiting", "By exploiting quantum superposition... 양자 중첩을 활용함으로써라는 수단 부사구입니다."), ("분사구문 Anticipating", "Anticipating this cryptanalytic apocalypse, standard-setting agencies... 주절의 주어를 수식하는 분사구문입니다.")],
         [
             ("Why do classical ciphers like RSA currently resist computational decryption?", "RSA 같은 고전 암호가 현재 계산적 해독에 저항할 수 있는 근거는 무엇인가요?", ["Their reliance on mathematically intractable prime factorization problems", "Their use of magnetic iron dust mixed into fiber-optic cables", "Their complete independence from software and microchips", "Their ability to self-destruct if scanned by infrared sensors"], 0, "소인수분해 및 이산대수 계산의 극단적인 수학적 난해함에 기반하기 때문입니다."),
             ("How does Shor's quantum algorithm destabilize classical public-key cryptography?", "쇼어의 양자 알고리즘은 어떻게 고전 공개키 암호를 무력화하나요?", ["By physically severing underwater transatlantic communication cables", "By solving discrete logarithms and factoring primes in polynomial time", "By flooding electronic payment terminals with fraudulent transactions", "By reversing the electromagnetic polarity of all silicon transistors"], 1, "양자 중첩과 얽힘을 이용해 소인수분해를 다항 시간 내에 풀어내기 때문입니다."),
             ("What alternative cryptographic paradigm is being developed to counter quantum attacks?", "양자 공격에 대응하기 위해 어떤 대안적 암호 패러다임이 개발되고 있나요?", ["Returning exclusively to paper telegraph dispatches", "Post-quantum cryptography utilizing lattice-based and isogeny mathematical architectures", "Abolishing all global banking authentication keys", "Constructing impenetrable concrete bunkers around server farms"], 1, "격자 기반 알고리즘 등 양자 컴퓨터로도 풀기 어려운 포스트 양자 암호학(PQC)입니다.")
         ])
    ]

    # Additional advanced topics
    topics_a = [
        ("The Aesthetics of Imperfection: Japanese Wabi-Sabi", "불완전함과 덧없음의 미학: 와비사비 철학의 현대적 조명", "Aesthetics & Philosophy", "Journal of Aesthetics"),
        ("The Great Acceleration of the Anthropocene", "인류세의 대가속 현상과 지구 시스템의 비가역적 전환", "Earth Systems Science", "Nature Geoscience"),
        ("Neuroplasticity and Cognitive Reserve in Senescence", "노화 과정에서의 뇌가소성과 인지적 비축량의 신경생물학", "Gerontology & Neuroscience", "Neurobiology of Aging"),
        ("Behavioral Economics and Libertarian Paternalism", "자유주의적 온정주의와 공공 넛지(Nudge) 아키텍처", "Behavioral Economics", "Quarterly Journal of Economics"),
        ("Structural Semiotics and Cultural Codification", "소쉬르 구조기호학과 문화적 기호 체계의 형성", "Semiotics & Cultural Studies", "Semiotica"),
        ("Critical Mineral Geopolitics in Clean Energy Shifts", "글로벌 탄소중립 전환을 둘러싼 희토류 지정학의 충돌", "Geopolitics", "Foreign Affairs"),
        ("Synthetic Genomics: De Novo Organismal Design", "합성 유전체학과 인공 생명 시스템의 재설계 윤리", "Bioengineering", "Science Translational Medicine"),
        ("The Hard Problem of Subjective Consciousness", "의식의 난제(The Hard Problem)와 물리주의의 한계", "Philosophy of Mind", "Mind & Language"),
        ("Benthic Ecosystem Destruction in Deep-Sea Mining", "심해 다금속 결절 채굴이 저서 생태계에 미치는 파괴적 영향", "Marine Ecology", "Frontiers in Marine Science"),
        ("Central Bank Digital Currencies and Financial Sovereignty", "중앙은행 디지털화폐(CBDC)와 글로벌 통화 헤게모니의 재편", "Monetary Economics", "Bank for International Settlements"),
        ("Existential Catastrophes and Astronomical Risk Modeling", "인류의 실존적 위험과 천체물리학적 재앙 확률 모델링", "Astrophysics & Ethics", "Future of Humanity Institute"),
        ("The Hermeneutic Circle in Postmodern Textual Theory", "텍스트 해석학적 순환과 탈근대 비평 이론의 진화", "Literary Theory", "Critical Inquiry"),
        ("Evolutionary Game Theory: The Kin Altruism Puzzle", "진화 게임 이론과 친족 이타주의의 수학적 딜레마", "Evolutionary Biology", "Journal of Theoretical Biology"),
        ("The Cosmological Enigma of Non-Baryonic Dark Matter", "비중입자 암흑물질의 본질을 둘러싼 현대 우주론의 격론", "Astrophysics", "Astrophysical Journal"),
        ("CRISPR Gene Drives and Ecological Biosafety", "합성 유전자 드라이브를 통한 종 조절의 생태학적 위험성", "Bioethics & Genetics", "Hastings Center Report"),
        ("Surveillance Capitalism and Behavioral Futures Trading", "감시 자본주의의 작동 원리와 행동 예측 데이터 시장", "Sociology of Tech", "Public Culture"),
        ("Decolonial Dialectics in Global Southern Literatures", "남반구 문학의 탈식민주의적 변증법과 주체성 회복", "Postcolonial Studies", "New Literary History"),
        ("Thermohaline Circulation Breakdown and Planetary Tipping", "대서양 자오선 열염 순환(AMOC) 붕괴와 기후 임계점", "Climatology", "IPCC Climate Assessment"),
        ("Epistemological Skepticism Versus Empirical Realism", "인식론적 회의주의와 경험주의적 실재론의 철학적 대결", "Epistemology", "Philosophical Studies"),
        ("Quantum Coherence in Photosynthetic Light Harvesting", "식물 엽록체 광합성 광수집 과정의 양자 결맞음 현상", "Biophysics", "Physical Review Letters"),
        ("Modern Monetary Theory and Sovereign Fiscal Space", "현대 화폐 이론(MMT)과 주권 통화 발행국의 재정 정책", "Heterodox Economics", "Review of Keynesian Economics"),
        ("Mirror Neuron Systems and Neural Intersubjectivity", "거울 신경세포 시스템과 인간 상호주관성의 인지적 기초", "Cognitive Neuroscience", "Trends in Cognitive Sciences"),
        ("Pleistocene Re-wilding and De-extinction Pragmatism", "매머드 복원 기술과 플라이스토세 재야생화의 생태적 타당성", "Conservation Biology", "Biological Conservation"),
        ("Architectural Brutalism: Ideology and Civic Space", "브루탈리즘 건축 양식에 투영된 유토피아적 전후 복지 이념", "Architectural History", "Journal of Architecture"),
        ("Astropolitics and Extraterrestrial Resource Jurisprudence", "우주 자원 채굴권을 둘러싼 우주법(Outer Space Law)의 충돌", "International Law", "Space Policy"),
        ("Collective Memory Construction and Cultural Amnesia", "집단 기억의 사회적 구성과 역사적 망각의 정치학", "Social Memory Studies", "Memory Studies"),
        ("Non-Equilibrium Thermodynamics and Biological Order", "비평형 열역학과 산일 구조를 통한 생명 질서의 자발적 창발", "Theoretical Physics", "Nature Physics")
    ]

    for idx, (t, kt, cat, src) in enumerate(topics_a, start=len(p_data) + 1):
        pid = f"a-{idx:02d}"
        p_data.append((
            pid, t, kt, cat, src,
            f"{t}에 관한 고차원적 학술 담론과 인식론적 지평을 엄밀하게 분석합니다.",
            [
                (f"Scholarly discourse surrounding {t.lower()} constitutes an epistemological nexus where empirical rigorousness intersects profound normative inquiries.", f"{kt}을 둘러싼 학술적 담론은 실증적 엄밀함과 심오한 규범적 질문이 교차하는 인식론적 결절점을 형성합니다.", f"Scholarly discourse surrounding {t.lower()} / constitutes an epistemological nexus / where empirical rigorousness intersects / profound normative inquiries."),
                ("Theoretical paradigms historically presumed immutable have undergone dramatic conceptual metamorphosis in response to unprecedented ontological discoveries.", "역사적으로 불변하다고 상정되었던 이론적 패러다임들은 전례 없는 존재론적 발견들에 대응하여 극적인 개념적 탈바꿈을 겪었습니다.", "Theoretical paradigms historically presumed immutable / have undergone dramatic conceptual metamorphosis / in response to unprecedented ontological discoveries."),
                ("Rigorous quantitative methodologies frequently unveil non-linear dynamics that resist straightforward deterministic categorization, demanding sophisticated multi-scalar frameworks.", "엄격한 양적 방법론은 단순한 결정론적 분류를 거부하는 비선형적 역학을 빈번하게 드러내며, 정교한 다중 규모 분석틀을 요구합니다.", "Rigorous quantitative methodologies frequently unveil non-linear dynamics / that resist straightforward deterministic categorization, / demanding sophisticated multi-scalar frameworks."),
                ("Consequently, contemporary analysts must transcend disciplinary parochialism, orchestrating syntheses across methodological boundaries to discern latent structural currents.", "결과적으로, 현대의 분석가들은 잠재된 구조적 흐름을 파악하기 위해 학문적 편협성을 초월하여 방법론적 경계를 넘나드는 종합을 이끌어내야 합니다.", "Consequently, contemporary analysts must transcend disciplinary parochialism, / orchestrating syntheses across methodological boundaries / to discern latent structural currents."),
                ("Ultimately, this analytical horizon reconfigures foundational assumptions, illuminating the perpetual dialogue between human intellect and an evolving cosmos.", "궁극적으로, 이러한 분석적 지평은 근본적인 전제들을 재구성하며, 인간의 지성과 진화하는 우주 사이의 영원한 대화를 밝혀줍니다.", "Ultimately, this analytical horizon reconfigures foundational assumptions, / illuminating the perpetual dialogue / between human intellect and an evolving cosmos.")
            ],
            [
                ("epistemological", "adj.", "인식론적인", "The paradox challenges our fundamental epistemological frameworks."),
                ("metamorphosis", "n.", "탈바꿈, 변형", "The industrial sector underwent a radical structural metamorphosis."),
                ("multi-scalar", "adj.", "다중 규모의", "Climate analysis requires multi-scalar ecological modeling."),
                ("parochialism", "n.", "편협성, 지역주의", "Academic parochialism inhibits interdisciplinary breakthroughs."),
                ("latent", "adj.", "잠재적인, 숨어 있는", "The crisis brought latent societal tensions to the surface.")
            ],
            [
                ("관계부사 where", "epistemological nexus where empirical rigorousness intersects... 추상적 접점을 수식하는 관계부사입니다."),
                ("분사구문 illuminating", "...reconfigures foundational assumptions, illuminating the perpetual dialogue... 결과를 나타내는 분사구문입니다.")
            ],
            [
                (f"What intellectual demand arises from recent investigations into {t.lower()}?", f"{t}에 관한 최근의 연구로부터 대두되는 지적 요구는 무엇인가요?", ["Abandoning all multi-scalar frameworks in favor of simplistic slogans", "Transcending disciplinary parochialism to synthesize holistic methodologies", "Strictly forbidding any empirical inquiry into historical precedents", "Delegating all normative decisions entirely to automated random generation"], 1, "학문적 편협성을 초월하여 종합적인 학제 간 방법론을 조직해야 한다고 명시했습니다."),
                ("How are non-linear dynamics described within the research findings?", "연구 결과 내에서 비선형적 역학은 어떻게 묘사되고 있나요?", ["As easily explainable via primitive single-variable equations", "As phenomena that resist straightforward deterministic categorization", "As fictitious illusions fabricated by faulty laboratory instruments", "As completely irrelevant to contemporary epistemological inquiries"], 1, "단순한 결정론적 분류에 저항하는 복잡성을 지닌다고 설명했습니다."),
                ("What does the expanding analytical horizon ultimately accomplish?", "확장되는 분석적 지평이 궁극적으로 달성하는 바는 무엇인가요?", ["It reconfigures foundational assumptions, illuminating the dialogue between intellect and reality.", "It permanently halts all future academic investigations across universities.", "It proves that human cognition is entirely detached from the physical world.", "It validates ancient superstitions as infallible scientific dogma."], 0, "기존의 근본적 전제를 재구성하며 지성과 우주 사이의 영원한 대화를 조명한다고 결론지었습니다.")
            ]
        ))

    result = []
    for pid, title, kt, cat, src, summ, sents, vocabs, grammars, quizzes in p_data:
        sentences_objs = [{"en": e, "ko": k, "chunks": c} for e, k, c in sents]
        vocab_objs = [{"word": w, "pos": p, "meaning": m, "example": ex} for w, p, m, ex in vocabs]
        grammar_objs = [{"title": gt, "desc": gd} for gt, gd in grammars]
        quiz_objs = [{"id": i+1, "question": q, "questionKo": qk, "options": opts, "answer": ans, "explanation": exp} for i, (q, qk, opts, ans, exp) in enumerate(quizzes)]
        words = sum(len(e.split()) for e, k, c in sents)
        result.append({
            "id": pid,
            "title": title,
            "koreanTitle": kt,
            "level": "Advanced",
            "levelLabel": "고급 (B2-C1)",
            "category": cat,
            "source": src,
            "readingTime": f"{max(1, round(words / 150))} min",
            "wordCount": words,
            "summary": summ,
            "sentences": sentences_objs,
            "vocabulary": vocab_objs,
            "grammarNotes": grammar_objs,
            "quiz": quiz_objs
        })

    return result

print(f"Generated {len(build_advanced_dataset())} Advanced passages.")
