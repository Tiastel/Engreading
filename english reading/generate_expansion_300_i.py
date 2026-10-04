# -*- coding: utf-8 -*-
"""
generate_expansion_300_i.py
20 Intermediate passages (i-81 to i-100)
Completes Intermediate tier to exactly 100 passages (i-01 to i-100).
B1-B2 level, authoritative sources, sentence chunks, vocabulary, grammar, and 3 deducible comprehension questions per passage.
"""

def get_expansion_300_i():
    return [
        (
            "i-81",
            "Climate Risk and Systemic Financial Stability",
            "기후 리스크와 금융 시스템의 구조적 안정성",
            "Financial Economics",
            "Bank of England Quarterly Bulletin & Mark Carney 'Breaking the Tragedy of the Horizon'",
            "기후 변화는 물리적 재해 손실뿐 아니라 저탄소 경제 전환 과정의 좌초 자산 위험을 유발하여 글로벌 금융 시스템에 구조적 충격을 가할 수 있습니다.",
            [
                ("Central banks and financial regulators increasingly classify climate change / not merely as an environmental challenge, / but as a profound systemic risk to financial stability.",
                 "중앙은행과 금융 규제 당국은 기후 변화를 / 단순한 환경적 도전 과제가 아니라, / 금융 안정성에 대한 심대한 구조적 위험으로 점점 더 분류하고 있습니다.",
                 "Central banks and financial regulators / increasingly classify climate change / not merely as an environmental challenge, / but as a profound systemic risk to financial stability."),
                ("Regulators divide climate risk into two core categories: / physical risks arising from catastrophic weather events, / and transition risks stemming from structural decarbonization.",
                 "규제 기관은 기후 위험을 두 가지 핵심 범주로 나누는데, / 파국적인 기상 이변에서 발생하는 물리적 위험과 / 구조적 탈탄소화에서 기인하는 전환 위험입니다.",
                 "Regulators divide climate risk into two core categories: / physical risks arising from catastrophic weather events, / and transition risks stemming from structural decarbonization."),
                ("If carbon pricing policies or clean energy breakthroughs render fossil fuel reserves unextractable, / trillions of dollars in corporate balance sheets / will abruptly become stranded assets.",
                 "탄소 가격제 정책이나 청정 에너지 혁신으로 인해 화석 연료 매장량의 채굴이 불가능해진다면, / 기업 대차대조표 상의 수조 달러 규모 자산이 / 갑작스럽게 좌초 자산으로 전락할 것입니다.",
                 "If carbon pricing policies or clean energy breakthroughs / render fossil fuel reserves unextractable, / trillions of dollars in corporate balance sheets / will abruptly become stranded assets."),
                ("Consequently, / financial institutions are implementing rigorous stress tests / to gauge whether commercial banks hold adequate capital buffers / to weather sudden macroeconomic asset devaluations.",
                 "결과적으로, / 금융 기관들은 상업은행이 갑작스러운 거시경제적 자산 평가절하를 견딜 수 있는 / 충분한 자본 완충 장치를 보유하고 있는지를 측정하기 위해 / 엄격한 스트레스 테스트를 시행하고 있습니다.",
                 "Consequently, / financial institutions are implementing rigorous stress tests / to gauge whether commercial banks hold adequate capital buffers / to weather sudden macroeconomic asset devaluations.")
            ],
            [
                ("systemic", "adj.", "전체 시스템의, 구조적인", "A banking panic poses severe systemic risks to the broader real economy."),
                ("transition", "n.", "전환, 이행", "The global economy is undergoing a historic energy transition toward renewables."),
                ("stranded assets", "n. phr.", "좌초 자산 (조기 상각되는 화석연료 자산)", "Coal-fired power plants risk becoming stranded assets as solar costs plunge."),
                ("weather", "v.", "(폭풍·위기를) 견뎌내다", "The resilient firm weathered the economic recession without declaring bankruptcy.")
            ],
            [
                ("not merely A, but B", "'단지 A뿐만 아니라 B도' 강조 구문입니다."),
                ("to gauge whether + 절", "'~인지 측정/평가하기 위해' 목적을 나타내는 to부정사 명사절입니다.")
            ],
            [
                ("Into what two core categories do financial regulators divide climate risk?",
                 "금융 규제 기관은 기후 위험을 어떤 두 가지 핵심 범주로 나누는가?",
                 ["Chemical risks and acoustic risks", "Physical risks and transition risks", "Oceanic risks and lunar risks", "Software risks and hardware risks"],
                 1,
                 "두 번째 문장에 물리적 위험(physical risks)과 전환 위험(transition risks)으로 구분한다고 명시되어 있습니다."),
                ("What are 'stranded assets' in the context of climate transition?",
                 "기후 전환의 맥락에서 '좌초 자산(stranded assets)'이란 무엇인가?",
                 ["Assets left on desert islands by ships", "Assets that abruptly lose value when carbon reserves become unextractable", "Gold coins buried underground during wars", "Office furniture that cannot be sold"],
                 1,
                 "세 번째 문장에 탄소 규제 등으로 화석 연료 채굴이 불가능해지며 가치가 상실되는 자산이라고 나와 있습니다."),
                ("Why are financial institutions implementing climate stress tests on banks?",
                 "금융 기관들은 왜 은행에 기후 스트레스 테스트를 시행하고 있는가?",
                 ["To measure if banks hold adequate capital buffers to weather devaluations", "To force banks to stop using paper currency immediately", "To close down all commercial banks permanently", "To lower the salaries of junior bank clerks"],
                 0,
                 "마지막 문장에 급작스러운 자산 가치 하락을 견딜 충분한 자본 완충력을 보유했는지 측정하기 위함이라고 설명합니다.")
            ]
        ),
        (
            "i-82",
            "Epigenetic Clocks and the Biology of Aging",
            "후성유전학적 시계와 생체 나이 측정",
            "Biogerontology",
            "Nature Aging & Steve Horvath Epigenetic Clock Research",
            "DNA 메틸화 패턴을 분석하는 후성유전학적 시계는 단순한 주민등록상 연대기적 나이를 넘어 세포와 조직의 실제 생물학적 노화 속도를 정밀하게 측정합니다.",
            [
                ("For decades, / biological age was considered synonymous / with chronological age—the simple passage of calendar years.",
                 "수십 년 동안, / 생물학적 나이는 단순한 달력 연도의 경과를 뜻하는 / 연대학적 나이와 동의어로 여겨졌습니다.",
                 "For decades, / biological age was considered synonymous / with chronological age— / the simple passage of calendar years."),
                ("However, / molecular geneticist Steve Horvath pioneered a biological metric / known as the epigenetic clock.",
                 "그러나, / 분자유전학자 스티브 호바스는 후성유전학적 시계라 알려진 / 생물학적 측정 기준을 개척했습니다.",
                 "However, / molecular geneticist Steve Horvath / pioneered a biological metric / known as the epigenetic clock."),
                ("By assessing the methylation status across hundreds of specific cytosine-phosphate-guanine (CpG) sites in the genome, / the algorithm measures cumulative molecular wear and tear.",
                 "게놈 내 수백 개의 특정 CpG 부위에 걸친 메틸화 상태를 평가함으로써, / 이 알고리즘은 누적된 분자적 마모를 측정합니다.",
                 "By assessing the methylation status / across hundreds of specific cytosine-phosphate-guanine (CpG) sites in the genome, / the algorithm measures cumulative molecular wear and tear."),
                ("Individuals whose epigenetic age outpaces their chronological age / display significantly higher risks / of cardiovascular mortality and age-related neurodegenerative diseases.",
                 "후성유전학적 나이가 실제 연대학적 나이를 앞지르는 개인들은 / 심혈관 질환 사망률과 노인성 신경퇴행성 질환의 위험이 / 현저하게 더 높게 나타납니다.",
                 "Individuals whose epigenetic age outpaces their chronological age / display significantly higher risks / of cardiovascular mortality / and age-related neurodegenerative diseases.")
            ],
            [
                ("synonymous", "adj.", "동의어의, 아주 밀접한", "Her name became synonymous with fearless investigative journalism."),
                ("methylation", "n.", "메틸화 (DNA에 메틸기를 결합해 유전자 발현 억제)", "Aberrant DNA methylation is a hallmark of many human tumors."),
                ("wear and tear", "idiom", "마모, 손상", "Bicycle chains suffer natural wear and tear after hundreds of kilometers."),
                ("outpace", "v.", "앞지르다, 능가하다", "Consumer inflation outpaced wage growth over the past fiscal quarter.")
            ],
            [
                ("was considered synonymous with ~", "'~와 동의어로 간주되었다' 수동태 구문입니다."),
                ("whose epigenetic age outpaces ~", "선행사 Individuals의 소유격을 나타내는 관계대명사 whose 절입니다.")
            ],
            [
                ("What was biological age historically equated with before epigenetic clocks?",
                 "후성유전학적 시계 이전 생물학적 나이는 역사적으로 무엇과 동일시되었는가?",
                 ["The geographic location of birth", "Chronological age (the passage of calendar years)", "The physical height of an individual", "The number of hours spent sleeping per day"],
                 1,
                 "첫 문장에 달력 연도의 경과를 뜻하는 연대학적 나이(chronological age)와 동의어로 여겨졌다고 나와 있습니다."),
                ("How does the epigenetic clock calculate molecular wear and tear?",
                 "후성유전학적 시계는 분자적 마모를 어떻게 계산하는가?",
                 ["By counting how many white hairs a person has", "By assessing DNA methylation across hundreds of specific CpG sites in the genome", "By measuring how fast a patient runs a mile", "By testing fingernail flexibility in cold water"],
                 1,
                 "세 번째 문장에 게놈 내 수백 개 CpG 부위의 DNA 메틸화 상태를 평가하여 측정한다고 설명합니다."),
                ("What health risks face individuals whose epigenetic age outpaces their chronological age?",
                 "후성유전학적 나이가 연대학적 나이를 앞지른 개인들은 어떤 건강 위험에 직면하는가?",
                 ["Higher risks of cardiovascular mortality and neurodegenerative diseases", "Guaranteed immunity to all infectious viral diseases", "Inability to dream during REM sleep", "Complete loss of skin pigmentation within five days"],
                 0,
                 "마지막 문장에 심혈관 사망률과 신경퇴행성 질환의 현저히 높은 위험을 나타낸다고 명시되어 있습니다.")
            ]
        ),
        (
            "i-83",
            "The Challenge of CRISPR Off-Target Mutations",
            "CRISPR 유전자 가위의 오프타깃 돌연변이 과제",
            "Genomics & Bioengineering",
            "Cell Research & Nature Biotechnology Clinical Reviews",
            "CRISPR-Cas9 기술은 혁명적이지만, 표적 서열과 유사한 비표적 유전체 부위를 오인하여 절단하는 오프타깃 돌연변이 위험을 최소화해야 합니다.",
            [
                ("CRISPR-Cas9 has ushered in an unprecedented era / of precise targeted genome editing.",
                 "CRISPR-Cas9은 정밀한 표적 게놈 편집의 / 전례 없는 시대를 열었습니다.",
                 "CRISPR-Cas9 has ushered in / an unprecedented era / of precise targeted genome editing."),
                ("However, / the clinical translation of this technology faces a critical hurdle / known as off-target mutagenesis.",
                 "그러나, / 이 기술의 임상적 적용은 오프타깃 돌연변이라 알려진 / 중대한 난관에 직면해 있습니다.",
                 "However, / the clinical translation of this technology / faces a critical hurdle / known as off-target mutagenesis."),
                ("Although the guide RNA is designed to bind to a unique 20-base-pair target, / the Cas9 enzyme occasionally tolerates minor mismatches, / cleaving unintended genomic loci.",
                 "가이드 RNA가 고유한 20염기쌍 표적에 결합하도록 설계되었음에도 불구하고, / Cas9 효소는 때때로 미세한 불일치를 용인하여 / 의도치 않은 게놈 위치를 절단합니다.",
                 "Although the guide RNA is designed / to bind to a unique 20-base-pair target, / the Cas9 enzyme occasionally tolerates minor mismatches, / cleaving unintended genomic loci."),
                ("These spurious cuts can induce deleterious chromosomal translocations / or disrupt vital tumor suppressor genes, / necessitating high-fidelity engineered Cas9 variants for human therapies.",
                 "이러한 부적절한 절단은 유해한 염색체 전좌를 유발하거나 / 중요한 종양 억제 유전자를 파괴할 수 있어, / 인간 치료를 위한 고충실도 조작 Cas9 변이체의 개발을 필요로 합니다.",
                 "These spurious cuts can induce deleterious chromosomal translocations / or disrupt vital tumor suppressor genes, / necessitating high-fidelity engineered Cas9 variants / for human therapies.")
            ],
            [
                ("usher in", "v. phr.", "~을 도입하다, 시작하다", "The invention of transistors ushered in the digital computing era."),
                ("mutagenesis", "n.", "돌연변이 유발", "Chemical pollutants act as potent agents of environmental mutagenesis."),
                ("spurious", "adj.", "거짓된, 잘못된, 비의도적인", "Researchers filtered out spurious signals generated by electrical noise."),
                ("deleterious", "adj.", "해로운, 유해한", "Lead exposure has deleterious effects on developing nervous systems.")
            ],
            [
                ("Although + 절", "'비록 ~일지라도' 양보의 부사절을 이끕니다."),
                (", cleaving ~", "분사구문으로 '의도치 않은 게놈 위치를 절단하면서' 결과를 나타냅니다.")
            ],
            [
                ("What critical hurdle faces the clinical translation of CRISPR-Cas9?",
                 "CRISPR-Cas9의 임상적 적용이 직면한 중대한 난관은 무엇인가?",
                 ["The total absence of RNA in human cells", "Off-target mutagenesis where unintended genomic loci are cleaved", "The inability of Cas9 to dissolve in water", "A complete shortage of laboratory test tubes globally"],
                 1,
                 "두 번째 문장과 세 번째 문장에 의도치 않은 위치가 절단되는 오프타깃 돌연변이 유발이라고 설명합니다."),
                ("Why does the Cas9 enzyme cleave off-target genomic sites?",
                 "왜 Cas9 효소가 오프타깃 게놈 부위를 절단하는가?",
                 ["Because it mistakes plastic for DNA", "Because it occasionally tolerates minor base mismatches with the guide RNA", "Because it operates only when exposed to strong radioactive waves", "Because scientists command it to destroy chromosomes"],
                 1,
                 "세 번째 문장에 가이드 RNA와의 미세한 염기 불일치를 때때로 용인하기 때문이라고 나와 있습니다."),
                ("What potential danger can spurious chromosomal cuts cause in patients?",
                 "잘못된 염색체 절단이 환자에게 어떤 잠재적 위험을 초래할 수 있는가?",
                 ["Inducing deleterious chromosomal translocations or disrupting tumor suppressor genes", "Causing immediate loss of finger bones", "Turning skin bright blue permanently", "Forcing the heart to beat backwards"],
                 0,
                 "마지막 문장에 유해한 염색체 전좌를 유발하거나 종양 억제 유전자를 파괴할 수 있다고 명시되어 있습니다.")
            ]
        ),
        (
            "i-84",
            "Monetary Policy and the Liquidity Trap",
            "통화정책과 유동성 함정의 딜레마",
            "Macroeconomics",
            "Federal Reserve Bank Economic Review & Keynesian Monetary Theory",
            "기준금리가 0% 근처로 떨어지는 유동성 함정 상태에서는 중앙은행이 통화 공급을 늘려도 경제 주체들이 현금만 사재기하여 경기 부양 효과가 무력화됩니다.",
            [
                ("Under conventional monetary policy, / central banks stimulate sluggish economies / by slashing benchmark interest rates to encourage commercial borrowing.",
                 "전통적인 통화 정책 하에서, / 중앙은행은 상업적 차입을 장려하기 위해 / 기준금리를 인하함으로써 / 침체된 경제를 부양합니다.",
                 "Under conventional monetary policy, / central banks stimulate sluggish economies / by slashing benchmark interest rates / to encourage commercial borrowing."),
                ("However, / when nominal interest rates decline to near zero, / the economy can become ensnared in a liquidity trap.",
                 "그러나, / 명목 이자율이 거의 0에 가깝게 하락할 때, / 경제는 유동성 함정에 갇힐 수 있습니다.",
                 "However, / when nominal interest rates decline to near zero, / the economy can become ensnared / in a liquidity trap."),
                ("At this zero lower bound, / investors and households anticipate that interest rates cannot drop further, / preferring to hoard risk-free cash rather than buying bonds or investing.",
                 "이 제로 금리 하한선에서, / 투자자와 가계는 금리가 더 떨어질 수 없다고 예상하여, / 채권을 매수하거나 투자하기보다는 위험 없는 현금을 사재기하는 것을 선호합니다.",
                 "At this zero lower bound, / investors and households anticipate that interest rates cannot drop further, / preferring to hoard risk-free cash / rather than buying bonds or investing."),
                ("Consequently, / incremental injections of central bank liquidity fail to depress yields or boost consumption, / rendering traditional interest rate cuts impotent.",
                 "결과적으로, / 중앙은행의 추가적인 유동성 주입은 수익률을 낮추거나 소비를 진작시키는 데 실패하며, / 전통적인 금리 인하를 무력하게 만듭니다.",
                 "Consequently, / incremental injections of central bank liquidity / fail to depress yields or boost consumption, / rendering traditional interest rate cuts impotent.")
            ],
            [
                ("ensnare", "v.", "함정에 빠뜨리다, 덫에 걸리게 하다", "Poachers ensnared wild animals using concealed wire traps."),
                ("bound", "n.", "한계선, 경계", "Zero represents the practical lower bound for nominal currency rates."),
                ("hoard", "v.", "비축하다, 사재기하다", "Consumers hoarded canned goods in anticipation of the hurricane."),
                ("impotent", "adj.", "무력한, 효력이 없는", "The outdated antibiotics proved completely impotent against the resistant bacterial strain.")
            ],
            [
                ("prefer A rather than B", "'B하기보다는 A를 선호하다' 선호 표현입니다."),
                (", rendering ~ impotent", "'render + 목적어 + 형용사' 5형식 분사구문으로 '~을 무력한 상태로 만들면서'로 해석됩니다.")
            ],
            [
                ("How do central banks stimulate sluggish economies under conventional policy?",
                 "전통적 정책 하에서 중앙은행은 침체된 경제를 어떻게 부양하는가?",
                 ["By doubling corporate income tax rates", "By slashing benchmark interest rates to encourage borrowing", "By closing down all stock market exchanges", "By banning the use of checking accounts"],
                 1,
                 "첫 문장에 대출을 장려하기 위해 기준금리를 대폭 인하함으로써 부양한다고 나와 있습니다."),
                ("What do households and investors prefer to do in a liquidity trap?",
                 "유동성 함정 상태에서 가계와 투자자들은 무엇을 선호하는가?",
                 ["Borrow immense sums to buy factory machinery", "Hoard risk-free cash rather than investing or buying bonds", "Donate all liquid savings to the central treasury", "Spend all disposable income immediately on retail luxury goods"],
                 1,
                 "세 번째 문장에 투자하거나 채권을 사기보다 무위험 현금을 사재기하는 것을 선호한다고 명시되어 있습니다."),
                ("What is the consequence of the liquidity trap on traditional interest rate policy?",
                 "유동성 함정이 전통적인 금리 정책에 미치는 결과는 무엇인가?",
                 ["It makes traditional interest rate cuts impotent.", "It instantly causes triple-digit hyperinflation.", "It forces central bankers to resign immediately.", "It replaces paper banknotes with physical gold bullion."],
                 0,
                 "마지막 문장에 전통적 금리 인하를 무력하게 만든다(rendering interest rate cuts impotent)고 설명합니다.")
            ]
        ),
        (
            "i-85",
            "Oxytocin and the Neurobiology of Social Bonding",
            "옥시토신과 사회적 유대감의 신경생물학",
            "Behavioral Endocrinology",
            "Trends in Neurosciences & National Institute of Mental Health",
            "뇌하수체 후엽에서 분비되는 옥시토신 펩타이드는 모성 애착, 짝 결합, 타인에 대한 신뢰를 형성하는 핵심 신경 펩타이드입니다.",
            [
                ("Oxytocin is an evolutionary conserved neuropeptide / synthesized in the hypothalamus / and released by the posterior pituitary gland.",
                 "옥시토신은 시상하부에서 합성되어 / 뇌하수체 후엽에 의해 방출되는 / 진화적으로 보존된 신경 펩타이드입니다.",
                 "Oxytocin is an evolutionary conserved neuropeptide / synthesized in the hypothalamus / and released by the posterior pituitary gland."),
                ("While initially recognized for its hormonal role in stimulating uterine contractions and lactation, / neuroscientists discovered it modulates social cognition.",
                 "처음에는 자궁 수축과 수유를 자극하는 호르몬 역할로 알려졌으나, / 신경과학자들은 옥시토신이 사회적 인지를 조절한다는 점을 발견했습니다.",
                 "While initially recognized / for its hormonal role in stimulating uterine contractions and lactation, / neuroscientists discovered it modulates social cognition."),
                ("Oxytocin binding to receptors in the amygdala dampens vigilance and fear responses, / fostering interpersonal trust and maternal attachment.",
                 "편도체의 수용체에 결합하는 옥시토신은 경계심과 공포 반응을 완화하여, / 대인 간의 신뢰와 모성 애착을 촉진합니다.",
                 "Oxytocin binding to receptors in the amygdala / dampens vigilance and fear responses, / fostering interpersonal trust and maternal attachment."),
                ("In monogamous prairie voles, / density of oxytocin receptors in the reward system / directly determines lifelong partner bonding / compared to promiscuous montane cousins.",
                 "일편단심 일부일처제를 따르는 프레리 들쥐에서, / 보상 체계 내 옥시토신 수용체의 밀도는 / 난혼을 하는 산악 들쥐 사촌과 비교하여 / 평생의 파트너 유대 형성을 직접적으로 결정합니다.",
                 "In monogamous prairie voles, / density of oxytocin receptors in the reward system / directly determines lifelong partner bonding / compared to promiscuous montane cousins.")
            ],
            [
                ("conserved", "adj.", "보존된 (진화 과정에서 유지된)", "Hox genes are highly conserved across all bilateral animal phyla."),
                ("lactation", "n.", "수유, 젖 분비", "Prolactin and oxytocin cooperatively regulate postpartum mammalian lactation."),
                ("vigilance", "n.", "경계, 각성 경계 태세", "Guards maintained constant vigilance along the perimeter fence."),
                ("monogamous", "adj.", "일부일처의, 한 파트너만 유지하는", "Many swan species form monogamous lifelong reproductive pairs.")
            ],
            [
                ("While initially recognized for ~, neuroscientists discovered ~", "양보 부사절 접속사 While 구문입니다."),
                (", fostering ~", "결과/수반을 나타내는 분사구문으로 '신뢰를 촉진하면서'로 해석됩니다.")
            ],
            [
                ("Where is oxytocin synthesized in the mammalian brain?",
                 "포유류 뇌에서 옥시토신은 어디에서 합성되는가?",
                 ["In the hypothalamus", "In the optic retina", "Inside tooth pulp", "In the middle ear bones"],
                 0,
                 "첫 문장에 시상하부(in the hypothalamus)에서 합성된다고 명시되어 있습니다."),
                ("How does oxytocin affect fear and vigilance in the amygdala?",
                 "옥시토신은 편도체에서 공포와 경계심에 어떤 영향을 미치는가?",
                 ["It increases fear to panic levels.", "It dampens vigilance and fear responses, fostering trust.", "It permanently disables the ability to see colors.", "It stops blood circulation to the ears."],
                 1,
                 "세 번째 문장에 경계심과 공포 반응을 완화하여 신뢰를 촉진한다고 나와 있습니다."),
                ("What animal research demonstrates oxytocin's role in lifelong partner bonding?",
                 "평생 파트너 유대 형성에서 옥시토신의 역할을 보여주는 동물 연구는 무엇인가?",
                 ["Desert scorpions", "Monogamous prairie voles", "Deep sea jellyfish", "Migrating monarch butterflies"],
                 1,
                 "마지막 문장에 일부일처제 프레리 들쥐(monogamous prairie voles) 연구에서 입증되었다고 설명합니다.")
            ]
        ),
        (
            "i-86",
            "The P versus NP Problem in Computer Science",
            "컴퓨터 과학의 P-NP 문제와 계산 복잡도",
            "Theoretical Computer Science",
            "Clay Mathematics Institute Millennium Prize Problems",
            "P-NP 문제는 다항 시간 내에 빠르게 해결할 수 있는 문제의 집합과 정답이 주어졌을 때 다항 시간 내에 검증할 수 있는 문제의 집합이 동일한가를 묻는 수학적 난제입니다.",
            [
                ("The P versus NP problem stands / as the most profound open question / in theoretical computer science and mathematical logic.",
                 "P 대 NP 문제는 / 이론 컴퓨터 과학과 수리논리학에서 / 가장 심오한 미해결 난제로 우뚝 서 있습니다.",
                 "The P versus NP problem stands / as the most profound open question / in theoretical computer science and mathematical logic."),
                ("The complexity class P consists of decision problems / that can be solved efficiently by a deterministic computer / within polynomial time.",
                 "복잡도 클래스 P는 / 다항 시간 내에 결정론적 컴퓨터에 의해 / 효율적으로 해결될 수 있는 결정 문제들로 구성됩니다.",
                 "The complexity class P consists of decision problems / that can be solved efficiently / by a deterministic computer / within polynomial time."),
                ("In contrast, the class NP comprises problems / whose proposed candidate solutions can be verified in polynomial time, / even if discovering the solution requires brute-force search.",
                 "대조적으로, 클래스 NP는 비록 해를 찾는 데 무차별 대입 탐색이 필요할지라도, / 제시된 후보 해를 다항 시간 내에 검증할 수 있는 / 문제들을 포함합니다.",
                 "In contrast, the class NP comprises problems / whose proposed candidate solutions can be verified in polynomial time, / even if discovering the solution requires brute-force search."),
                ("Whether every easily verifiable problem can also be solved easily (P equals NP) remains unproven, / with monumental implications for cryptography, optimization, and artificial intelligence.",
                 "쉽게 검증 가능한 모든 문제가 쉽게 해결될 수도 있는가(P = NP인가)는 여전히 미증명 상태로 남아 있으며, / 암호학, 최적화, 인공지능에 지대한 영향을 미칩니다.",
                 "Whether every easily verifiable problem can also be solved easily (P equals NP) / remains unproven, / with monumental implications / for cryptography, optimization, and artificial intelligence.")
            ],
            [
                ("deterministic", "adj.", "결정론적인", "Deterministic algorithms yield identical outputs given identical initial inputs."),
                ("polynomial", "adj.", "다항식의, 다항 시간의 (컴퓨터에서 다룰 수 있는 계산 규모)", "Sorting algorithms like mergesort run in polynomial time."),
                ("brute-force", "adj./n.", "무차별 대입의 (모든 경우를 일일이 계산함)", "Cracking complex passwords via brute-force enumeration takes centuries."),
                ("monumental", "adj.", "기념비적인, 엄청난", "Decoding the complete human genome was a monumental scientific feat.")
            ],
            [
                ("consists of + 명사", "'~로 구성되다' 수동태를 쓰지 않는 표현입니다."),
                ("Whether + 절 + remains unproven", "Whether 명사절이 전체 문장의 주어로 쓰였습니다.")
            ],
            [
                ("What characterizes the complexity class P?",
                 "복잡도 클래스 P의 특징은 무엇인가?",
                 ["Problems that can never be solved by any machine", "Problems that can be solved efficiently within polynomial time", "Problems that take billions of years to verify", "Algorithms that operate without any electricity"],
                 1,
                 "두 번째 문장에 다항 시간 내에 효율적으로 해결될 수 있는 문제들이라고 명시되어 있습니다."),
                ("How does class NP differ from class P in the text?",
                 "본문에서 클래스 NP는 클래스 P와 어떻게 다른가?",
                 ["NP problems cannot be represented using numbers.", "NP problems have proposed solutions that can be verified in polynomial time.", "NP problems only run on ancient mechanical clocks.", "NP problems are completely illegal to compute."],
                 1,
                 "세 번째 문장에 후보 해가 주어졌을 때 다항 시간 내에 검증될 수 있는 문제들이라고 설명합니다."),
                ("What fields are mentioned as having monumental implications if P equals NP?",
                 "P=NP가 증명될 경우 지대한 영향을 받을 것으로 언급된 분야들은 무엇인가?",
                 ["Cryptography, optimization, and artificial intelligence", "Classical oil painting and pottery making", "Desert sand dune erosion", "Deep ocean tidal heights"],
                 0,
                 "마지막 문장에 암호학, 최적화, 인공지능(cryptography, optimization, and AI)에 지대한 영향을 미친다고 나와 있습니다.")
            ]
        ),
        (
            "i-87",
            "The Economics of Urban Congestion Pricing",
            "도시 교통 혼잡 통행료의 경제학",
            "Urban Economics & Public Policy",
            "Journal of Transport Economics and Policy & London Transport Studies",
            "도로 이용자가 다른 운전자들에게 유발하는 지체 지연 비용(부정적 외부효과)을 피구세 형태의 혼잡 통행료로 부과하여 교통 흐름과 대기질을 개선합니다.",
            [
                ("Urban roadways during peak rush hours / exhibit a classic tragedy of unpriced scarce public goods.",
                 "출퇴근 피크 시간대의 도시 도로는 / 가격이 책정되지 않은 희소한 공공재의 / 전형적인 비극을 보여줍니다.",
                 "Urban roadways during peak rush hours / exhibit a classic tragedy / of unpriced scarce public goods."),
                ("When a motorist enters an already gridlocked thoroughfare, / they consider only their private travel delay, / ignoring the marginal delay their vehicle imposes upon every other driver.",
                 "운전자가 이미 꽉 막힌 간선 도로로 진입할 때, / 그들은 자신의 사적 주행 지연만을 고려하고, / 자신의 차량이 다른 모든 운전자들에게 부과하는 한계 지연 비용은 무시합니다.",
                 "When a motorist enters an already gridlocked thoroughfare, / they consider only their private travel delay, / ignoring the marginal delay their vehicle imposes upon every other driver."),
                ("Congestion pricing rectifies this market distortion / by levying a dynamic electronic toll / calibrated to real-time traffic volume.",
                 "혼잡 통행료는 실시간 교통량에 맞추어 조정되는 / 동적 전자 통행료를 부과함으로써 / 이러한 시장 왜곡을 바로잡습니다.",
                 "Congestion pricing rectifies this market distortion / by levying a dynamic electronic toll / calibrated to real-time traffic volume."),
                ("Empirical evidence from London, Stockholm, and Singapore demonstrates / that congestion pricing dampens vehicular volume, / accelerates bus transit, / and slashes urban greenhouse emissions.",
                 "런던, 스톡홀름, 싱가포르의 실증적 증거는 / 혼잡 통행료가 차량 통행량을 줄이고, / 버스 대중교통 속도를 높이며, / 도시 온실가스 배출을 대폭 감축한다는 점을 입증합니다.",
                 "Empirical evidence from London, Stockholm, and Singapore demonstrates / that congestion pricing dampens vehicular volume, / accelerates bus transit, / and slashes urban greenhouse emissions.")
            ],
            [
                ("thoroughfare", "n.", "주요 도로, 간선도로", "Emergency ambulances sped down the designated central thoroughfare."),
                ("rectify", "v.", "바로잡다, 교정하다", "Engineers installed a filter to rectify the water pressure irregularity."),
                ("calibrated", "adj.", "조정된, 눈금이 맞춰진", "The sensor is carefully calibrated to detect minute temperature shifts."),
                ("transit", "n.", "대중교통, 수송", "Public transit investments reduce suburban commuter highway gridlock.")
            ],
            [
                ("ignoring the delay ~", "동시동작 분사구문으로 '지연을 무시하면서'로 해석됩니다."),
                ("by levying ~", "'~를 부과함으로써' 수단과 방법을 나타냅니다.")
            ],
            [
                ("What cost does a driver ignore when entering an already crowded road?",
                 "운전자가 이미 혼잡한 도로로 진입할 때 무시하는 비용은 무엇인가?",
                 ["The price of car insurance next year", "The marginal delay their vehicle imposes upon all other drivers", "The cost of building the road fifty years ago", "The price of steel in manufacturing plants"],
                 1,
                 "두 번째 문장에 자신의 차량이 다른 모든 운전자에게 부과하는 한계 지연 비용을 무시한다고 나와 있습니다."),
                ("How does congestion pricing rectify market distortion?",
                 "혼잡 통행료는 어떻게 시장 왜곡을 바로잡는가?",
                 ["By banning all automobiles permanently", "By levying a dynamic electronic toll calibrated to traffic volume", "By demolishing existing highways", "By giving away free gasoline to every citizen"],
                 1,
                 "세 번째 문장에 실시간 교통량에 맞춘 동적 전자 통행료를 부과함으로써 교정한다고 명시되어 있습니다."),
                ("What benefits were observed in cities like London, Stockholm, and Singapore?",
                 "런던, 스톡홀름, 싱가포르 같은 도시에서 관찰된 이점은 무엇인가?",
                 ["Reduced vehicular volume, faster bus transit, and lower urban emissions", "Complete elimination of bicycles", "Quadrupling of traffic accidents", "Free taxi rides for everyone"],
                 0,
                 "마지막 문장에 차량 통행량 감소, 버스 환승 가속화, 도시 온실가스 감축이 입증되었다고 설명합니다.")
            ]
        ),
        (
            "i-88",
            "Solar Wind and the Earth's Magnetosphere",
            "태양풍과 지구 자기권의 방어 차폐막",
            "Space Physics",
            "NASA Heliophysics Science Division Bulletin",
            "태양이 뿜어내는 고에너지 하전 입자들의 흐름인 태양풍은 지구 외핵이 형성한 자기장 차폐막에 가로막혀 우주로 튕겨 나가며 오로라를 만들어냅니다.",
            [
                ("The sun continuously emits a torrential stream / of high-energy charged protons and electrons / known as the solar wind.",
                 "태양은 태양풍이라 알려진 / 고에너지 하전 양성자와 전자들의 / 거센 흐름을 끊임없이 방출합니다.",
                 "The sun continuously emits a torrential stream / of high-energy charged protons and electrons / known as the solar wind."),
                ("Traveling at supersonic speeds exceeding four hundred kilometers per second, / this ionizing radiation would strip away our atmosphere / were Earth unprotected.",
                 "초당 400킬로미터가 넘는 초음속으로 이동하는 / 이 전리 방사선은 지구가 보호받지 못한다면 / 우리의 대기를 벗겨내 날려버릴 것입니다.",
                 "Traveling at supersonic speeds exceeding four hundred kilometers per second, / this ionizing radiation would strip away our atmosphere / were Earth unprotected."),
                ("Fortunately, / churning molten iron currents inside Earth's outer core / generate a massive geomagnetic dipole field / that encloses the planet in a protective magnetosphere.",
                 "다행스럽게도, / 지구 외핵 내부에서 소용돌이치는 용융 철 전류가 / 거대한 지구 자기 쌍극자 장을 생성하여 / 행성을 보호 자기권으로 둘러쌉니다.",
                 "Fortunately, / churning molten iron currents inside Earth's outer core / generate a massive geomagnetic dipole field / that encloses the planet in a protective magnetosphere."),
                ("When violent solar flares strike this magnetic shield, / particles are funneled toward polar regions, / ionizing upper atmospheric gases to illuminate brilliant auroral displays.",
                 "격렬한 태양 플레어가 이 자기 차폐막을 타격할 때, / 입자들은 극지방으로 유도되어, / 상층 대기 기체를 이온화시킴으로써 찬란한 오로라를 밝힙니다.",
                 "When violent solar flares strike this magnetic shield, / particles are funneled toward polar regions, / ionizing upper atmospheric gases / to illuminate brilliant auroral displays.")
            ],
            [
                ("torrential", "adj.", "거센, 격렬한", "Torrential monsoon rains triggered widespread mountain mudslides."),
                ("ionizing", "adj.", "전리(이온화)의, 방사성의", "Ionizing radiation damages molecular DNA strands inside living cells."),
                ("churning", "adj.", "소용돌이치는, 요동치는", "Churning ocean breakers battered the coastal lighthouse."),
                ("funnel", "v.", "깔때기처럼 유도하다, 모으다", "Stadium corridors funneled thousands of fans toward exits safely.")
            ],
            [
                ("were Earth unprotected", "'if Earth were unprotected'에서 접속사 if가 생략되어 도치된 가정법 과거 구문입니다."),
                (", ionizing ~", "분사구문으로 '기체를 이온화시키면서' 연속적 작용을 나타냅니다.")
            ],
            [
                ("What is the solar wind composed of according to the text?",
                 "본문에 따르면 태양풍은 무엇으로 구성되어 있는가?",
                 ["Frozen water ice cubes", "High-energy charged protons and electrons", "Heavy volcanic dust clouds", "Liquid helium fuel droplets"],
                 1,
                 "첫 문장에 고에너지 하전 양성자와 전자(charged protons and electrons)의 흐름이라고 나와 있습니다."),
                ("What generates Earth's protective geomagnetic field?",
                 "무엇이 지구의 보호 지구 자기장을 생성하는가?",
                 ["Churning molten iron currents inside Earth's outer core", "Ocean waves splashing against sandy beaches", "Trees absorbing carbon dioxide through leaves", "Wind turbines rotating in polar regions"],
                 0,
                 "세 번째 문장에 외핵 내부의 용융 철 전류(churning molten iron currents)라고 명시되어 있습니다."),
                ("How are brilliant auroral displays illuminated in polar skies?",
                 "극지 하늘에서 찬란한 오로라는 어떻게 불을 밝히는가?",
                 ["By giant artificial searchlights built on icebergs", "By solar particles funneled to polar regions ionizing upper atmospheric gases", "By burning forest fires in northern Canada", "By moonlight reflecting off solid sea ice mirrors"],
                 1,
                 "마지막 문장에 극지로 유도된 태양 입자들이 상층 대기 기체를 이온화시켜 빛을 낸다고 설명합니다.")
            ]
        ),
        (
            "i-89",
            "Autophagy and Cellular Quality Control",
            "세포 자가포식(오토파지)과 세포 정화 기전",
            "Cell Biology",
            "Nature Reviews Molecular Cell Biology & Yoshinori Ohsumi Nobel Discovery",
            "오토파지는 세포 내 손상된 단백질 응집체와 노후 소기관을 이중막으로 감싸 리소좀에서 분해하여 재활용하는 생체 정화 시스템입니다.",
            [
                ("Autophagy, / derived from the Greek roots for 'self-eating,' / is a fundamental catabolic mechanism / essential for cellular homeostasis.",
                 "'스스로 먹기'를 뜻하는 그리스어 어원에서 유래한 / 오토파지(자가포식)는 / 세포 항상성에 필수적인 / 기초적인 이화작용 메커니즘입니다.",
                 "Autophagy, / derived from the Greek roots for 'self-eating,' / is a fundamental catabolic mechanism / essential for cellular homeostasis."),
                ("During periods of nutrient deprivation or metabolic stress, / cells sequester dysfunctional organelles and toxic protein aggregates / within a specialized double-membrane vesicle called an autophagosome.",
                 "영양 결핍이나 대사적 스트레스 기간 동안, / 세포는 오토파고사이라 불리는 특수화된 이중막 소낭 내에 / 기능 장애 소기관과 독성 단백질 응집체를 격리합니다.",
                 "During periods of nutrient deprivation or metabolic stress, / cells sequester dysfunctional organelles and toxic protein aggregates / within a specialized double-membrane vesicle / called an autophagosome."),
                ("This vesicle fuses with an acidic lysosome, / whose potent hydrolytic enzymes degrade the sequestered contents / into basic amino acids and fatty acids.",
                 "이 소낭은 산성 리소좀과 융합하며, / 리소좀의 강력한 가수분해 효소가 격리된 내용물을 / 기본 아미노산과 지방산으로 분해합니다.",
                 "This vesicle fuses with an acidic lysosome, / whose potent hydrolytic enzymes / degrade the sequestered contents / into basic amino acids and fatty acids."),
                ("These recycled molecular building blocks are then channeled into energetic synthesis, / clearing toxic cellular debris to defend against neurodegeneration and cancer.",
                 "이 재활용된 분자 기본 블록들은 그 후 에너지 합성에 투입되어, / 신경퇴행과 암을 방어하기 위해 독성 세포 잔해를 청소합니다.",
                 "These recycled molecular building blocks / are then channeled into energetic synthesis, / clearing toxic cellular debris / to defend against neurodegeneration and cancer.")
            ],
            [
                ("catabolic", "adj.", "이화작용의, 분해 대사의", "Catabolic reactions break down complex molecules to yield metabolic energy."),
                ("sequester", "v.", "격리하다, 따로 떼어놓다", "Juries in sensitive trials may be sequestered in hotels without media access."),
                ("hydrolytic", "adj.", "가수분해의", "Hydrolytic enzymes in the gut cleave complex starches into simple glucose."),
                ("debris", "n.", "잔해, 부스러기", "White blood cells engulf cellular debris following localized tissue trauma.")
            ],
            [
                ("derived from ~", "과거분사구로 주어 Autophagy를 보충 설명합니다."),
                (", clearing toxic cellular debris ~", "분사구문으로 '독성 세포 잔해를 청소하면서' 목적/결과를 나타냅니다.")
            ],
            [
                ("What does the word 'autophagy' literally mean from Greek roots?",
                 "그리스어 어원에서 '오토파지(autophagy)'는 글자 그대로 무슨 뜻인가?",
                 ["Fast running", "Self-eating", "Deep sleeping", "Sunlight drinking"],
                 1,
                 "첫 문장에 'derived from the Greek roots for self-eating'이라고 명시되어 있습니다."),
                ("What double-membrane vesicle sequesters damaged cellular components?",
                 "어떤 이중막 소낭이 손상된 세포 구성 성분을 격리하는가?",
                 ["An autophagosome", "A red blood cell", "A bone cartilage cap", "A hair follicle"],
                 0,
                 "두 번째 문장에 오토파고솜(an autophagosome)이라 불리는 이중막 소낭이라고 나와 있습니다."),
                ("What organelle degrades the sequestered contents using hydrolytic enzymes?",
                 "가수분해 효소를 사용하여 격리된 내용물을 분해하는 세포 소기관은 무엇인가?",
                 ["The cell nucleus", "The acidic lysosome", "The external cell wall", "The optic nerve"],
                 1,
                 "세 번째 문장에 산성 리소좀(acidic lysosome)의 가수분해 효소가 분해한다고 설명합니다.")
            ]
        ),
        (
            "i-90",
            "High-Frequency Trading and Latency Arbitrage",
            "초단타 매매(HFT)와 지연시간 차익거래",
            "Financial Engineering",
            "Journal of Finance & Michael Lewis 'Flash Boys' Studies",
            "컴퓨터 알고리즘과 마이크로초 단위 초고속 네트워크를 이용하는 초단타 매매업자들은 거래소 간 미세한 시차를 활용하여 차익거래를 수행합니다.",
            [
                ("In contemporary capital markets, / algorithmic high-frequency trading (HFT) accounts / for more than half of all equity transaction volume.",
                 "현대 자본 시장에서, / 알고리즘 초단타 매매(HFT)는 / 전체 주식 거래량의 절반 이상을 차지합니다.",
                 "In contemporary capital markets, / algorithmic high-frequency trading (HFT) accounts / for more than half of all equity transaction volume."),
                ("Rather than relying on human analytical intuition, / sophisticated mathematical algorithms execute thousands of trades / within microsecond timescales.",
                 "인간의 분석적 직관에 의존하는 대신, / 정교한 수학적 알고리즘이 마이크로초 단위의 시간 척도 안에서 / 수천 건의 거래를 체결합니다.",
                 "Rather than relying on human analytical intuition, / sophisticated mathematical algorithms execute thousands of trades / within microsecond timescales."),
                ("Firms pay immense premiums to co-locate their proprietary computing servers / inside exchange data centers, / minimizing physical cable distances to eliminate nanoseconds of transmission latency.",
                 "HFT 기업들은 자체 전산 서버를 거래소 데이터 센터 내부에 나란히 입주(코로케이션)시키기 위해 막대한 프리미엄을 지불하며, / 나노초 단위의 전송 지연시간을 없애기 위해 물리적 케이블 거리를 최소화합니다.",
                 "Firms pay immense premiums to co-locate their proprietary computing servers / inside exchange data centers, / minimizing physical cable distances / to eliminate nanoseconds of transmission latency."),
                ("By exploiting minuscule price discrepancies between fragmented exchanges before other market participants can react, / latency arbitrageurs harvest steady low-risk trading profits.",
                 "다른 시장 참여자들이 반응하기 전에 분산된 거래소들 간의 극미한 가격 차이를 활용함으로써, / 지연시간 차익거래자들은 지속적인 저위험 거래 이익을 수확합니다.",
                 "By exploiting minuscule price discrepancies between fragmented exchanges / before other market participants can react, / latency arbitrageurs harvest steady low-risk trading profits.")
            ],
            [
                ("equity", "n.", "주식, 지분, 공정성", "Private equity firms invest directly in unlisted growth companies."),
                ("co-locate", "v.", "동일 장소에 배치하다, 코로케이션하다", "Telecom providers co-locate servers in carrier-neutral data facilities."),
                ("latency", "n.", "지연 시간, 대기 시간", "Fiber-optic routes reduce latency between global financial exchanges."),
                ("minuscule", "adj.", "극미한, 대단히 작은", "A minuscule software error caused the automated system to crash."),
            ],
            [
                ("accounts for + 수량", "'~의 비중을 차지하다' 통계 표현입니다."),
                ("By exploiting ~", "'~를 활용/착취함으로써' 수단을 나타내는 전치사구입니다.")
            ],
            [
                ("How much equity transaction volume does high-frequency trading account for in modern markets?",
                 "현대 시장에서 초단타 매매는 주식 거래량의 얼마를 차지하는가?",
                 ["Less than one percent", "More than half of all equity transaction volume", "Exactly five trades per day", "Only night transactions on weekends"],
                 1,
                 "첫 문장에 전체 주식 거래량의 절반 이상(more than half)을 차지한다고 명시되어 있습니다."),
                ("Why do HFT firms co-locate their servers inside exchange data centers?",
                 "HFT 기업들은 왜 거래소 데이터 센터 내부에 서버를 코로케이션하는가?",
                 ["To save heating costs during cold winters", "To minimize cable distances and eliminate transmission latency", "To hire exchange security guards cheaply", "To paint their computers the same color as the exchange floor"],
                 1,
                 "세 번째 문장에 전송 지연시간(latency)을 없애기 위해 물리적 케이블 거리를 최소화하기 위함이라고 나와 있습니다."),
                ("How do latency arbitrageurs earn profits according to the text?",
                 "본문에 따르면 지연시간 차익거래자들은 어떻게 이익을 얻는가?",
                 ["By holding stocks for twenty years until dividends grow", "By exploiting minuscule price discrepancies across exchanges before others react", "By printing paper stock certificates secretly", "By waiting for corporate annual shareholder meetings"],
                 1,
                 "마지막 문장에 다른 참여자가 반응하기 전 거래소 간의 극미한 가격 불일치를 활용한다고 설명합니다.")
            ]
        ),
        (
            "i-91",
            "Mitochondrial DNA and the Search for Human Ancestry",
            "미토콘드리아 DNA와 인류 기원의 추적",
            "Human Evolutionary Genetics",
            "Nature & Allan Wilson Molecular Evolution Studies",
            "모계를 통해서만 변형 없이 유전되는 미토콘드리아 DNA의 돌연변이 축적률을 추적하여 인류의 공통 모계 조상인 '미토콘드리아 이브'가 아프리카에 살았음을 밝혔습니다.",
            [
                ("Unlike nuclear DNA which is recombined from both parents during sexual reproduction, / mitochondrial DNA (mtDNA) is inherited strictly along the maternal lineage.",
                 "유성 생식 동안 양부모 모두로부터 재조합되는 핵 DNA와 달리, / 미토콘드리아 DNA(mtDNA)는 전적으로 모계 혈통을 따라 유전됩니다.",
                 "Unlike nuclear DNA which is recombined from both parents during sexual reproduction, / mitochondrial DNA (mtDNA) is inherited strictly along the maternal lineage."),
                ("During fertilization, / the sperm's mitochondria are selectively destroyed, / leaving only the egg's mitochondrial genome intact within the developing zygote.",
                 "수정 과정에서, / 정자의 미토콘드리아는 선택적으로 파괴되고, / 오직 난자의 미토콘드리아 게놈만이 발생 중인 수정란 내에 온전하게 남겨집니다.",
                 "During fertilization, / the sperm's mitochondria are selectively destroyed, / leaving only the egg's mitochondrial genome intact / within the developing zygote."),
                ("Because mtDNA mutations accumulate at a remarkably constant statistical rate, / geneticists use it as a molecular clock to track human evolutionary chronology.",
                 "mtDNA 돌연변이는 현저하게 일정한 통계적 속도로 축적되기 때문에, / 유전학자들은 인류의 진화 연대기를 추적하기 위한 분자 시계로 이를 활용합니다.",
                 "Because mtDNA mutations accumulate at a remarkably constant statistical rate, / geneticists use it as a molecular clock / to track human evolutionary chronology."),
                ("This phylogenetic tracing famously identified 'Mitochondrial Eve,' / an ancient African woman / from whom all living humans trace an unbroken maternal ancestry.",
                 "이 계통발생학적 추적은 오늘날 살아있는 모든 인간이 끊이지 않는 모계 혈통을 거슬러 올라가는 / 고대 아프리카 여성인 / '미토콘드리아 이브'를 규명한 것으로 유명합니다.",
                 "This phylogenetic tracing famously identified 'Mitochondrial Eve,' / an ancient African woman / from whom all living humans trace an unbroken maternal ancestry.")
            ],
            [
                ("maternal", "adj.", "어머니의, 모계의", "Maternal antibodies provide passive immunity to newborn infants."),
                ("zygote", "n.", "수정란, 접합체", "The fertilized zygote undergoes repeated mitotic divisions."),
                ("intact", "adj.", "온전한, 손상되지 않은", "The ancient pottery remained miraculously intact inside the buried tomb."),
                ("phylogenetic", "adj.", "계통발생의", "Phylogenetic trees map evolutionary divergence among related species.")
            ],
            [
                ("Unlike A, B is inherited ~", "대비를 나타내는 전치사구입니다."),
                ("from whom all living humans trace ~", "전치사 + 관계대명사 구문으로 선행사 an ancient African woman을 수식합니다.")
            ],
            [
                ("How is mitochondrial DNA (mtDNA) inherited in humans?",
                 "인간에게서 미토콘드리아 DNA(mtDNA)는 어떻게 유전되는가?",
                 ["Exclusively from the paternal father", "Strictly along the maternal mother's lineage", "Through airborne viral infection only", "Equally recombined from fifty distant ancestors"],
                 1,
                 "첫 문장에 엄격하게 모계 혈통을 따라 유전된다(strictly along the maternal lineage)고 명시되어 있습니다."),
                ("Why can scientists use mtDNA as a molecular clock?",
                 "과학자들은 왜 mtDNA를 분자 시계로 활용할 수 있는가?",
                 ["Because mutations accumulate at a remarkably constant statistical rate", "Because mtDNA ticks with an audible acoustic sound", "Because it resets to zero every hundred years", "Because it glows under blacklight lamps"],
                 0,
                 "세 번째 문장에 돌연변이가 일정한 통계적 속도로 축적되기 때문이라고 나와 있습니다."),
                ("What geographic origin did phylogenetic tracing identify for 'Mitochondrial Eve'?",
                 "계통 추적 연구는 '미토콘드리아 이브'의 지리적 기원을 어디로 규명했는가?",
                 ["Ancient Africa", "Northern Europe", "Central Antarctica", "Eastern Australia"],
                 0,
                 "마지막 문장에 고대 아프리카 여성(an ancient African woman)으로 규명했다고 명시되어 있습니다.")
            ]
        ),
        (
            "i-92",
            "Carbon Border Adjustments and Carbon Leakage",
            "탄소 국경 조정제(CBAM)와 탄소 누출 방지",
            "International Trade & Climate Policy",
            "OECD Trade and Environment Directorate Reports",
            "엄격한 탄소 배출 규제를 시행하는 국가는 환경 규제가 느슨한 국가로 산업이 유출되는 탄소 누출을 방지하기 위해 탄소 국경세를 도입하고 있습니다.",
            [
                ("As industrialized nations implement stringent domestic carbon pricing to meet Paris Climate goals, / they confront the severe economic threat of carbon leakage.",
                 "산업화된 국가들이 파리 기후 협약 목표를 달성하기 위해 엄격한 국내 탄소 가격제를 시행함에 따라, / 그들은 탄소 누출이라는 심각한 경제적 위협에 직면합니다.",
                 "As industrialized nations implement stringent domestic carbon pricing / to meet Paris Climate goals, / they confront the severe economic threat of carbon leakage."),
                ("Carbon leakage occurs / when energy-intensive manufacturers relocate production factories to countries with lax environmental regulations / to evade regulatory compliance costs.",
                 "탄소 누출은 에너지 집약적 제조업체들이 규제 준수 비용을 피하기 위해 / 환경 규제가 느슨한 국가로 생산 공장을 이전할 때 / 발생합니다.",
                 "Carbon leakage occurs / when energy-intensive manufacturers relocate production factories / to countries with lax environmental regulations / to evade regulatory compliance costs."),
                ("To neutralize this competitive disadvantage and deter relocation, / jurisdictions like the European Union are deploying Carbon Border Adjustment Mechanisms (CBAM).",
                 "이러한 경쟁적 불이익을 상쇄하고 공장 이전을 억제하기 위해, / 유럽연합과 같은 관할권들은 탄소 국경 조정제(CBAM)를 도입하고 있습니다.",
                 "To neutralize this competitive disadvantage and deter relocation, / jurisdictions like the European Union / are deploying Carbon Border Adjustment Mechanisms (CBAM)."),
                ("By imposing an import tariff equivalent to the embedded carbon emissions of foreign goods, / CBAM levels the economic playing field and incentivizes trade partners to decarbonize.",
                 "외국 상품에 내재된 탄소 배출량에 상응하는 수입 관세를 부과함으로써, / CBAM은 경제적 경쟁의 장을 평탄하게 만들고 무역 상대국들이 탈탄소화하도록 유도합니다.",
                 "By imposing an import tariff equivalent to the embedded carbon emissions of foreign goods, / CBAM levels the economic playing field / and incentivizes trade partners to decarbonize.")
            ],
            [
                ("stringent", "adj.", "엄격한, 엄중한", "Pharmaceutical companies undergo stringent quality control audits."),
                ("leakage", "n.", "누출, 유출", "Carbon leakage undermines global emission reduction efforts."),
                ("lax", "adj.", "느슨한, 해이한", "Lax enforcement of safety protocols led to workplace accidents."),
                ("neutralize", "v.", "상쇄하다, 무력화하다", "Baking soda was used to neutralize the spilled hydrochloric acid.")
            ],
            [
                ("equivalent to + 명사", "'~에 상응하는, 동등한' 형용사 수식구입니다."),
                ("By imposing ~", "'~를 부과함으로써' 수단과 방법을 나타냅니다.")
            ],
            [
                ("When does economic 'carbon leakage' occur according to the text?",
                 "본문에 따르면 경제적 '탄소 누출'은 언제 발생하는가?",
                 ["When underground carbon storage pipes break open", "When manufacturers relocate to nations with lax environmental rules to evade costs", "When trees release carbon monoxide during nighttime", "When cars burn gasoline in city centers"],
                 1,
                 "두 번째 문장에 비용을 회피하기 위해 환경 규제가 느슨한 국가로 공장을 이전할 때 발생한다고 설명합니다."),
                ("What policy tool has the European Union deployed to counter carbon leakage?",
                 "탄소 누출에 대응하기 위해 유럽연합이 도입한 정책 도구는 무엇인가?",
                 ["A total ban on all ocean merchant ships", "The Carbon Border Adjustment Mechanism (CBAM)", "Printing subsidies for coal power stations", "Abolishing domestic environmental laws completely"],
                 1,
                 "세 번째 문장에 탄소 국경 조정제(CBAM)를 도입하고 있다고 명시되어 있습니다."),
                ("How does CBAM level the economic playing field for imported goods?",
                 "CBAM은 수입품에 대해 어떻게 경제적 경쟁 환경을 평탄하게 만드는가?",
                 ["By giving foreign factories free European citizenship", "By imposing an import tariff equivalent to foreign goods' embedded carbon emissions", "By forcing foreign companies to pay in physical gold", "By burning imported steel at border ports"],
                 1,
                 "마지막 문장에 외국 상품에 내재된 탄소 배출량에 상응하는 수입 관세를 부과함으로써 경쟁 환경을 평탄하게 만든다고 설명합니다.")
            ]
        ),
        (
            "i-93",
            "The Gut-Brain Axis and Microbial Endocrinology",
            "장-뇌 축과 마이크로바이옴의 신경 조절",
            "Neurogastroenterology",
            "Gastroenterology & Nature Microbiology Reviews",
            "장내 미생물군은 미주신경과 단쇄지방산 같은 신경 활성 대사물질을 통해 중추신경계와 양방향으로 소통하며 기분과 인지 기능에 지대한 영향을 미칩니다.",
            [
                ("The human gastrointestinal tract harbors trillions of symbiotic microorganisms / collectively known as the gut microbiome.",
                 "인간의 위장관은 집합적으로 장내 마이크로바이옴(미생물군)으로 알려진 / 수조 마리의 공생 미생물들을 수용하고 있습니다.",
                 "The human gastrointestinal tract harbors trillions of symbiotic microorganisms / collectively known as the gut microbiome."),
                ("Far from being passive bystanders in digestion, / these commensal bacteria engage in continuous bidirectional communication / with the central nervous system.",
                 "소화 과정의 수동적인 방관자에 머무르기는커녕, / 이 공생 박테리아들은 중추신경계와 / 끊임없는 양방향 소통에 관여합니다.",
                 "Far from being passive bystanders in digestion, / these commensal bacteria engage in continuous bidirectional communication / with the central nervous system."),
                ("Through the tenth cranial nerve / known as the vagus nerve, / microbial metabolites like short-chain fatty acids stimulate neural signals that modulate emotion and stress resilience.",
                 "미주신경이라 알려진 / 제10 뇌신경을 통해, / 단쇄지방산과 같은 미생물 대사산물들은 감정과 스트레스 회복력을 조절하는 신경 신호를 자극합니다.",
                 "Through the tenth cranial nerve known as the vagus nerve, / microbial metabolites like short-chain fatty acids / stimulate neural signals that modulate emotion and stress resilience."),
                ("Remarkably, / gut bacteria synthesize more than ninety percent of the body's peripheral serotonin, / demonstrating that digestive microbiology intimately shapes emotional neuropsychiatry.",
                 "놀랍게도, / 장내 박테리아는 신체 말초 세로토닌의 90퍼센트 이상을 합성하며, / 소화 미생물학이 감정 신경정신의학을 밀접하게 형성한다는 점을 입증합니다.",
                 "Remarkably, / gut bacteria synthesize more than ninety percent / of the body's peripheral serotonin, / demonstrating that digestive microbiology / intimately shapes emotional neuropsychiatry.")
            ],
            [
                ("commensal", "adj.", "공생의, 편리공생의", "Commensal bacteria protect epithelial surfaces from pathogenic colonization."),
                ("bidirectional", "adj.", "양방향의", "Effective communication between teachers and students is inherently bidirectional."),
                ("vagus nerve", "n.", "미주신경 (뇌와 내장을 잇는 주요 부교감 신경)", "Vagus nerve stimulation can reduce intractable epileptic seizures."),
                ("intimately", "adv.", "밀접하게, 깊이", "Economics is intimately entwined with political decision-making.")
            ],
            [
                ("Far from being ~", "'결코 ~이기는커녕' 강한 부정을 나타내는 관용 표현입니다."),
                (", demonstrating that ~", "분사구문으로 '그리하여 ~을 입증하면서' 결과를 나타냅니다.")
            ],
            [
                ("What is the collection of trillions of microorganisms in the gut called?",
                 "장내 수조 마리의 미생물 집합체를 무엇이라 부르는가?",
                 ["The cranial skeleton", "The gut microbiome", "The cardiac valve", "The thyroid cluster"],
                 1,
                 "첫 문장에 장내 마이크로바이옴(the gut microbiome)이라고 명시되어 있습니다."),
                ("Which cranial nerve serves as a primary bidirectional communication highway between gut and brain?",
                 "어떤 뇌신경이 장과 뇌 사이의 주요 양방향 소통 고속도로 역할을 하는가?",
                 ["The optic nerve", "The vagus nerve", "The olfactory nerve", "The acoustic nerve"],
                 1,
                 "세 번째 문장에 미주신경(the vagus nerve)이라고 나와 있습니다."),
                ("What major neurotransmitter is synthesized overwhelmingly (over 90%) in the gut?",
                 "장내에서 압도적으로(90% 이상) 합성되는 주요 신경전달물질은 무엇인가?",
                 ["Adrenaline", "Peripheral serotonin", "Thyroxine", "Insulin"],
                 1,
                 "마지막 문장에 말초 세로토닌(peripheral serotonin)의 90% 이상을 합성한다고 명시되어 있습니다.")
            ]
        ),
        (
            "i-94",
            "The BB84 Protocol and Quantum Cryptography",
            "BB84 프로토콜과 양자 암호화의 물리학",
            "Quantum Information & Cybersecurity",
            "Physical Review Letters & Charles Bennett / Gilles Brassard Quantum Protocols",
            "BB84 양자 키 분배 프로토콜은 단일 광자의 편광 상태를 측정하려 시도하는 도청자의 존재가 물리 법칙에 의해 즉각 감지되는 완벽한 보안성을 제공합니다.",
            [
                ("Classical mathematical encryption schemes / such as RSA / rely on the conjectured difficulty of factoring gigantic composite numbers.",
                 "RSA와 같은 / 고전적인 수학적 암호화 방식은 / 거대한 합성수를 소인수분해하는 것의 추정된 난이도에 의존합니다.",
                 "Classical mathematical encryption schemes such as RSA / rely on the conjectured difficulty / of factoring gigantic composite numbers."),
                ("However, / the advent of quantum computing threatens to render these algorithms vulnerable to rapid decryption.",
                 "그러나, / 양자 컴퓨팅의 등장은 이러한 알고리즘들을 신속한 복호화에 취약하게 만들 위협을 가하고 있습니다.",
                 "However, / the advent of quantum computing / threatens to render these algorithms vulnerable / to rapid decryption."),
                ("In response, / physicists Charles Bennett and Gilles Brassard formulated the BB84 protocol / for unconditional quantum key distribution.",
                 "이에 대응하여, / 물리학자 찰스 베넷과 질 브라사르는 무조건적인 양자 키 분배를 위한 / BB84 프로토콜을 정립했습니다.",
                 "In response, / physicists Charles Bennett and Gilles Brassard formulated the BB84 protocol / for unconditional quantum key distribution."),
                ("Because the quantum no-cloning theorem dictates / that measuring an unknown photon collapses its polarization state, / any eavesdropping attempt introduces unavoidable error rates / that alert legitimate communicators immediately.",
                 "알 수 없는 광자를 측정하는 행위가 그 편광 상태를 붕괴시킨다는 양자 복제 불가능성 정리에 의해, / 어떠한 도청 시도도 피할 수 없는 오류율을 발생시켜 / 정당한 통신자들에게 즉시 경고를 보냅니다.",
                 "Because the quantum no-cloning theorem dictates / that measuring an unknown photon collapses its polarization state, / any eavesdropping attempt introduces unavoidable error rates / that alert legitimate communicators immediately.")
            ],
            [
                ("decryption", "n.", "복호화, 암호 해독", "Decryption of wartime cipher cables shortened the global conflict."),
                ("unconditional", "adj.", "무조건적인, 절대적인", "Quantum mechanics provides unconditional security based on laws of physics."),
                ("eavesdropping", "n.", "도청, 엿듣기", "End-to-end encryption shields private messaging against unauthorized eavesdropping."),
                ("unavoidable", "adj.", "불가피한, 피할 수 없는", "Supply delays were unavoidable following the catastrophic port hurricane.")
            ],
            [
                ("threatens to render A B", "'A를 B한 상태로 만들겠다고 위협하다' 5형식 구문입니다."),
                ("Because + 절", "이유의 접속사절로 주절에 앞서 원인을 제시합니다.")
            ],
            [
                ("What mathematical vulnerability threatens classical RSA encryption?",
                 "어떤 수학적 취약점이 고전적 RSA 암호화를 위협하는가?",
                 ["The total absence of prime numbers", "Rapid factoring of gigantic composite numbers by quantum computers", "The physical weight of computer cables", "The freezing of digital screens in cold weather"],
                 1,
                 "첫 문장과 두 번째 문장에 양자 컴퓨터가 거대한 합성수 소인수분해를 신속하게 해독할 위협이 있다고 설명합니다."),
                ("Who formulated the celebrated BB84 quantum protocol?",
                 "유명한 BB84 양자 프로토콜을 정립한 사람들은 누구인가?",
                 ["Isaac Newton and Gottfried Leibniz", "Charles Bennett and Gilles Brassard", "Albert Einstein and Niels Bohr", "Adam Smith and David Ricardo"],
                 1,
                 "세 번째 문장에 찰스 베넷과 질 브라사르(Charles Bennett and Gilles Brassard)라고 나와 있습니다."),
                ("Why does eavesdropping fail on a quantum channel?",
                 "양자 채널에서 도청은 왜 실패하는가?",
                 ["Because the wire burns the hands of the spy", "Because measuring unknown photons collapses their quantum state, creating detectable errors", "Because quantum cables are buried thousands of miles underground", "Because spies cannot understand the language of light"],
                 1,
                 "마지막 문장에 광자를 측정하는 행위가 상태를 붕괴시켜 감지 가능한 오류율을 발생시키기 때문이라고 명시되어 있습니다.")
            ]
        ),
        (
            "i-95",
            "The Global Crisis of Antibiotic Resistance",
            "항생제 내성의 진화와 글로벌 보건 위기",
            "Microbiology & Epidemiology",
            "World Health Organization (WHO) Antimicrobial Resistance Fact Sheets",
            "항생제의 광범위한 남용은 자연선택을 가속화하여 플라스미드를 통해 내성 유전자를 수평 전달하는 슈퍼버그의 출현을 초래하고 있습니다.",
            [
                ("The discovery of antimicrobial drugs in the twentieth century / transformed fatal bacterial infections / into routinely curable medical conditions.",
                 "20세기 항균 의약품의 발견은 / 치명적인 세균 감염을 / 일상적으로 치료 가능한 의학적 질환으로 탈바꿈시켰습니다.",
                 "The discovery of antimicrobial drugs in the twentieth century / transformed fatal bacterial infections / into routinely curable medical conditions."),
                ("However, / the widespread overprescription of antibiotics in human healthcare and industrial livestock agriculture / has accelerated an evolutionary crisis.",
                 "그러나, / 인간 의료 및 산업적 가축 농업에서 항생제의 광범위한 과다 처방은 / 진화론적 위기를 가속화했습니다.",
                 "However, / the widespread overprescription of antibiotics / in human healthcare and industrial livestock agriculture / has accelerated an evolutionary crisis."),
                ("Under relentless selective drug pressure, / rare bacterial mutants possessing resistance mechanisms survive / and disseminate resistance genes across species / through horizontal gene transfer via mobile plasmids.",
                 "가차 없는 선택적 약물 압력 하에서, / 내성 기전을 보유한 희귀한 박테리아 돌연변이가 생존하여 / 이동성 플라스미드를 통한 수평적 유전자 전달로 / 종을 넘어 내성 유전자를 전파합니다.",
                 "Under relentless selective drug pressure, / rare bacterial mutants possessing resistance mechanisms survive / and disseminate resistance genes across species / through horizontal gene transfer via mobile plasmids."),
                ("Consequently, / multi-drug resistant 'superbugs' increasingly evade last-line reserve antibiotics, / threatening a post-antibiotic era where simple surgical procedures become perilous.",
                 "결과적으로, / 다제내성 '슈퍼버그'는 점점 더 최후의 보루 항생제마저 회피하여, / 단순한 수술 절차조차 위험해지는 포스트 항생제 시대를 위협하고 있습니다.",
                 "Consequently, / multi-drug resistant 'superbugs' increasingly evade last-line reserve antibiotics, / threatening a post-antibiotic era / where simple surgical procedures become perilous.")
            ],
            [
                ("disseminate", "v.", "보급하다, 널리 퍼뜨리다", "Public health agencies disseminate vaccination guidelines to clinics."),
                ("plasmid", "n.", "플라스미드 (세균 내 독립 증식 원형 DNA)", "Plasmids frequently carry antibiotic resistance cassettes between bacteria."),
                ("perilous", "adj.", "매우 위험한", "Navigating narrow mountain ridges during blizzards is exceptionally perilous."),
                ("overprescription", "n.", "과다 처방", "Regulatory reforms seek to curb the overprescription of narcotic painkillers.")
            ],
            [
                ("transformed A into B", "'A를 B로 탈바꿈시키다' 변화 구문입니다."),
                (", threatening ~", "분사구문으로 '포스트 항생제 시대를 위협하면서' 결과를 나타냅니다.")
            ],
            [
                ("What human activities have accelerated the antibiotic resistance crisis?",
                 "어떤 인간 활동들이 항생제 내성 위기를 가속화했는가?",
                 ["Drinking excessive pure spring water", "Overprescription in healthcare and industrial livestock agriculture", "Exercising too frequently in morning hours", "Brushing teeth with fluoride toothpaste"],
                 1,
                 "두 번째 문장에 의료 및 가축 농업에서의 항생제 과다 처방 때문이라고 명시되어 있습니다."),
                ("How do bacteria share resistance genes across different species?",
                 "박테리아는 서로 다른 종 사이에서 내성 유전자를 어떻게 공유하는가?",
                 ["Through horizontal gene transfer via mobile plasmids", "By sending radio telegraph signals", "By dissolving into pure mineral water", "By flying through bird feathers"],
                 0,
                 "세 번째 문장에 이동성 플라스미드를 통한 수평적 유전자 전달(horizontal gene transfer via mobile plasmids)이라고 나와 있습니다."),
                ("Why are 'superbugs' dangerous to modern medicine?",
                 "왜 '슈퍼버그'가 현대 의학에 위험한가?",
                 ["They make all hospital lights flicker.", "They evade last-line reserve antibiotics, making simple procedures perilous.", "They turn medicines into solid stone blocks.", "They only attack expensive computer hardware."],
                 1,
                 "마지막 문장에 최후의 항생제를 회피하여 단순 수술 절차조차 위험하게 만들기 때문이라고 설명합니다.")
            ]
        ),
        (
            "i-96",
            "Network Externalities and Digital Platform Lock-in",
            "네트워크 외부성과 디지털 플랫폼의 고착 효과",
            "Platform Economics",
            "Harvard Business Review & MIT Sloan Management Review",
            "플랫폼의 가치가 사용자 수의 제곱에 비례하여 증가한다는 메트칼프의 법칙에 따라, 거대 테크 플랫폼은 강력한 네트워크 효과와 고착(Lock-in)을 형성합니다.",
            [
                ("In digital platform markets, / the utility derived by any individual participant / escalates as the total number of connected users expands.",
                 "디지털 플랫폼 시장에서, / 개별 참가자가 얻는 효용은 / 연결된 총 사용자 수가 확대됨에 따라 / 급격히 증가합니다.",
                 "In digital platform markets, / the utility derived by any individual participant / escalates as the total number of connected users expands."),
                ("This phenomenon, / formalised as a direct network externality or Metcalfe's Law, / creates exponential compounding value / that tips markets in favor of early dominant platforms.",
                 "직접 네트워크 외부성 또는 메트칼프의 법칙으로 공식화된 이 현상은 / 초기 지배적 플랫폼에 유리하게 시장을 기울어지게 만드는 / 기하급수적인 복리 가치를 창출합니다.",
                 "This phenomenon, / formalised as a direct network externality or Metcalfe's Law, / creates exponential compounding value / that tips markets in favor of early dominant platforms."),
                ("Additionally, / high switching costs—including accumulated social contacts, / proprietary file architectures, / and algorithmic personalization— / generate formidable user lock-in.",
                 "게다가, / 축적된 소셜 연락망, / 독점적 파일 구조, / 알고리즘 기반 개인화를 포함하는 높은 전환 비용은 / 강력한 사용자 고착(Lock-in)을 만들어냅니다.",
                 "Additionally, / high switching costs— / including accumulated social contacts, proprietary file architectures, and algorithmic personalization— / generate formidable user lock-in."),
                ("Consequently, / digital platform ecosystems frequently solidify into winner-take-all monopolies / where technologically superior competitors struggle to unseat entrenched incumbents.",
                 "결과적으로, / 디지털 플랫폼 생태계는 기술적으로 더 우수한 경쟁자조차 확고히 자리 잡은 기득권 기업을 축출하기 어려운 / 승자독식 독점으로 자주 굳어집니다.",
                 "Consequently, / digital platform ecosystems frequently solidify into winner-take-all monopolies / where technologically superior competitors struggle / to unseat entrenched incumbents.")
            ],
            [
                ("escalate", "v.", "확대되다, 급증하다", "Border skirmishes threaten to escalate into full-scale war."),
                ("compounding", "adj.", "복리의, 가속하는", "Compound interest accelerates the compounding growth of retirement savings."),
                ("formidable", "adj.", "어마어마한, 가공할 만한", "The champion faced a formidable challenger in the finals."),
                ("unseat", "v.", "축출하다, 자리에서 몰아내다", "The grassroots reform candidate sought to unseat the incumbent senator.")
            ],
            [
                ("as the number expands", "비례적 변화를 나타내는 접속사 as 절입니다."),
                ("where technologically superior competitors struggle", "장소/상황을 나타내는 관계부사 where 절입니다.")
            ],
            [
                ("What does Metcalfe's Law describe regarding digital platforms?",
                 "메트칼프의 법칙은 디지털 플랫폼에 관해 무엇을 설명하는가?",
                 ["That computers double their memory every single week", "That platform value escalates exponentially as the number of connected users expands", "That all internet platforms lose money on weekends", "That consumers only use software built before the year 2000"],
                 1,
                 "첫 문장과 두 번째 문장에 연결된 사용자 수가 늘어남에 따라 가치가 기하급수적으로 증가한다고 나와 있습니다."),
                ("Which factor contributes to high switching costs that lock in users?",
                 "사용자를 고착시키는 높은 전환 비용에 기여하는 요인은 무엇인가?",
                 ["Accumulated social contacts, proprietary files, and personalization", "The physical weight of desktop computers", "The price of paper textbooks", "The color of the computer monitor"],
                 0,
                 "세 번째 문장에 축적된 연락망, 독점 파일 구조, 개인화 등이 높은 전환 비용을 만든다고 명시되어 있습니다."),
                ("What market outcome frequently emerges due to network effects and lock-in?",
                 "네트워크 효과와 고착으로 인해 시장에 어떤 결과가 자주 나타나는가?",
                 ["Tens of thousands of equal microscopic businesses with zero customers", "Winner-take-all monopolies where entrenched incumbents are hard to unseat", "Complete elimination of all digital technology", "All software becoming 100 percent free globally"],
                 1,
                 "마지막 문장에 승자독식 독점(winner-take-all monopolies)으로 굳어지는 경우가 많다고 설명합니다.")
            ]
        ),
        (
            "i-97",
            "Glacial Isostatic Adjustment and Post-Glacial Rebound",
            "빙하 지각 평형 조정과 후빙기 반동",
            "Geophysics & Geodesy",
            "Geophysical Research Letters & NASA Jet Propulsion Laboratory",
            "빙하기에 거대한 빙하의 무게로 짓눌렸던 지각이 빙하가 녹아내리면서 수만 년에 걸쳐 서서히 융기하는 현상이 지구 해수면 측정에 영향을 미칩니다.",
            [
                ("During the Last Glacial Maximum twenty thousand years ago, / colossal continental ice sheets kilometers thick / burdened North America and Northern Europe.",
                 "2만 년 전 마지막 최대 빙하기 동안, / 수 킬로미터 두께의 거대한 대륙 빙상이 / 북미와 북유럽을 짓눌렀습니다.",
                 "During the Last Glacial Maximum twenty thousand years ago, / colossal continental ice sheets kilometers thick / burdened North America and Northern Europe."),
                ("The immense gravitational weight of this ice / depressed the underlying elastic lithosphere, / displacing viscous mantle magma outward into peripheral peripheral bulges.",
                 "이 빙하의 엄청난 중력 무게는 / 밑에 깔린 탄성 암석권을 눌러 가라앉혔고, / 점성의 맨틀 마그마를 주변부 융기부로 바깥쪽으로 밀어냈습니다.",
                 "The immense gravitational weight of this ice / depressed the underlying elastic lithosphere, / displacing viscous mantle magma outward / into peripheral bulges."),
                ("Following the post-glacial warming thaw, / the removal of this surface load initiated glacial isostatic adjustment (GIA)— / an ongoing rebound of the landmass / that continues today.",
                 "후빙기의 온난화 해빙에 이어, / 이 표면 하중의 제거는 지각 평형 조정(GIA), / 즉 오늘날까지도 지속되고 있는 / 육지의 지속적인 반동 융기를 시작시켰습니다.",
                 "Following the post-glacial warming thaw, / the removal of this surface load / initiated glacial isostatic adjustment (GIA)— / an ongoing rebound of the landmass that continues today."),
                ("Because mantle rock possesses high viscosity, / the crust rebounds at rates of merely millimeters to centimeters per year, / distorting local coastal sea-level measurements.",
                 "맨틀 암석이 높은 점성을 지니고 있기 때문에, / 지각은 1년에 불과 몇 밀리미터에서 센티미터 속도로 반동하며, / 국지적 해안 해수면 측정을 왜곡시킵니다.",
                 "Because mantle rock possesses high viscosity, / the crust rebounds at rates of merely millimeters to centimeters per year, / distorting local coastal sea-level measurements.")
            ],
            [
                ("burden", "v.", "부담을 주다, 짓누르다", "Developing countries are heavily burdened by foreign sovereign debt."),
                ("viscous", "adj.", "점성의, 끈적거리는", "Cold maple syrup is much more viscous than water."),
                ("rebound", "n./v.", "반동, 융기, 되튀다", "The economic output staged a vigorous rebound after supply shocks eased."),
                ("isostatic", "adj.", "지각 평형의 (부력 균형을 이루는)", "Isostatic equilibrium explains why lighter continental crust sits higher than ocean basins.")
            ],
            [
                ("Following + 명사", "'~에 뒤이어' 시간을 나타내는 전치사구입니다."),
                (", distorting ~", "분사구문으로 '국지적 해수면 측정을 왜곡하면서' 결과를 나타냅니다.")
            ],
            [
                ("What caused the Earth's crust in Northern Europe and North America to depress 20,000 years ago?",
                 "2만 년 전 북유럽과 북미의 지각을 눌러 침하시킨 원인은 무엇인가?",
                 ["The immense gravitational weight of continental ice sheets kilometers thick", "An explosion of a massive underground oil well", "The gravitational pull of wandering comets", "Intensive agricultural farming by ancient tribes"],
                 0,
                 "첫 문장과 두 번째 문장에 수 킬로미터 두께 대륙 빙상의 엄청난 무게 때문이라고 나와 있습니다."),
                ("What is Glacial Isostatic Adjustment (GIA)?",
                 "빙하 지각 평형 조정(GIA)이란 무엇인가?",
                 ["The immediate melting of all Antarctic ice in one day", "The slow ongoing rebound of the landmass after the removal of ice loads", "The construction of concrete sea walls by geologists", "The evaporation of deep oceans into outer space"],
                 1,
                 "세 번째 문장에 빙하 하중이 제거된 후 육지가 서서히 반동 융기하는 현상이라고 명시되어 있습니다."),
                ("Why does the crust rebound so slowly at only millimeters to centimeters per year?",
                 "지각은 왜 연간 불과 몇 밀리미터에서 센티미터라는 극히 느린 속도로 융기하는가?",
                 ["Because the mantle rock beneath possesses high viscosity", "Because the sun freezes the crust at night", "Because satellites push the continents down from orbit", "Because ocean waves push the land backwards"],
                 0,
                 "마지막 문장에 밑에 있는 맨틀 암석이 높은 점성(high viscosity)을 지니고 있기 때문이라고 설명합니다.")
            ]
        ),
        (
            "i-98",
            "The Availability Heuristic and Risk Distortion",
            "가용성 휴리스틱과 위험 인지의 왜곡",
            "Cognitive Psychology & Behavioral Science",
            "Cognitive Psychology & Amos Tversky / Daniel Kahneman Judgment Under Uncertainty",
            "인간은 어떤 사건의 실제 통계적 발생 확률보다 기억 속에서 얼마나 쉽게 생생하게 떠올릴 수 있는가에 의존하여 위험을 과대평가하는 인지 편향을 보입니다.",
            [
                ("In everyday decision-making, / human beings frequently rely on cognitive shortcuts / known as heuristics / to evaluate uncertainty under time pressure.",
                 "일상의 의사결정에서, / 인간은 시간 압박 속에서 불확실성을 평가하기 위해 / 휴리스틱이라 알려진 / 인지적 지름길에 자주 의존합니다.",
                 "In everyday decision-making, / human beings frequently rely on cognitive shortcuts / known as heuristics / to evaluate uncertainty under time pressure."),
                ("Psychologists Daniel Kahneman and Amos Tversky formulated the 'availability heuristic,' / which posits that people judge the frequency of an event / by the ease with which instances come to mind.",
                 "심리학자 대니얼 카너먼과 아모스 트버스키는 '가용성 휴리스틱'을 정립했는데, / 이는 사람들이 어떤 사건의 발생 빈도를 / 사례가 머릿속에 얼마나 쉽게 떠오르는가에 따라 판단한다고 상정합니다.",
                 "Psychologists Daniel Kahneman and Amos Tversky formulated the 'availability heuristic,' / which posits that people judge the frequency of an event / by the ease with which instances come to mind."),
                ("Because sensational events / such as plane crashes or shark attacks / receive vivid sensationalized media coverage, / they leave indelible emotional impressions in memory.",
                 "비행기 추락이나 상어 습격과 같은 / 자극적인 사건들은 / 생생하고 선정적인 언론 보도를 받기 때문에, / 기억 속에 지워지지 않는 감정적 인상을 남깁니다.",
                 "Because sensational events such as plane crashes or shark attacks / receive vivid sensationalized media coverage, / they leave indelible emotional impressions in memory."),
                ("Consequently, / people grossly overestimate the statistical probability of dramatic rare catastrophes / while underestimating mundane but statistically far deadlier risks like diabetes or car accidents.",
                 "결과적으로, / 사람들은 극적이고 드문 대참사의 통계적 확률을 턱없이 과대평가하는 반면, / 당뇨병이나 자동차 사고처럼 평범하지만 통계적으로 훨씬 더 치명적인 위험은 과소평가합니다.",
                 "Consequently, / people grossly overestimate the statistical probability of dramatic rare catastrophes / while underestimating mundane but statistically far deadlier risks / like diabetes or car accidents.")
            ],
            [
                ("heuristic", "n.", "휴리스틱 (경험적 발견법, 간편한 직관)", "Heuristics allow rapid choices but can introduce systematic cognitive biases."),
                ("indelible", "adj.", "지워지지 않는, 잊을 수 없는", "The historic speech left an indelible mark on democratic philosophy."),
                ("grossly", "adv.", "극도로, 심하게", "Auditors noted that the asset value was grossly inflated on official filings."),
                ("mundane", "adj.", "일상적인, 평범한", "Automated software eliminates mundane clerical bookkeeping tasks.")
            ],
            [
                ("by the ease with which ~", "'~가 얼마나 쉽게 일어나는가에 의해' 관계대명사 전치사 수식구입니다."),
                ("while underestimating ~", "대조를 나타내는 분사구문으로 '평범한 위험을 과소평가하는 반면에'로 해석됩니다.")
            ],
            [
                ("What does the availability heuristic state about human judgment?",
                 "가용성 휴리스틱은 인간의 판단에 대해 무엇을 말하는가?",
                 ["People use quantum calculators to make every choice.", "People judge the frequency of an event by how easily instances come to mind.", "People only believe facts written in ancient Latin scrolls.", "Human memory stores zero information about past events."],
                 1,
                 "두 번째 문장에 사례가 머릿속에 얼마나 쉽게 떠오르는가에 의해 빈도를 판단한다고 나와 있습니다."),
                ("Why do plane crashes or shark attacks leave vivid impressions in memory?",
                 "비행기 추락이나 상어 공격이 왜 기억에 생생한 인상을 남기는가?",
                 ["Because they happen billions of times every single second", "Because they receive sensationalized media coverage that leaves emotional impressions", "Because government laws require citizens to memorize them weekly", "Because schools teach shark hunting classes daily"],
                 1,
                 "세 번째 문장에 생생하고 선정적인 미디어 보도로 감정적 인상을 남기기 때문이라고 설명합니다."),
                ("What is a consequence of the availability heuristic described in the text?",
                 "본문에 기술된 가용성 휴리스틱의 결과는 무엇인가?",
                 ["People overestimate rare dramatic events while underestimating common deadlier risks.", "People completely stop driving cars and exclusively ride horses.", "People become immune to all medical diseases.", "All statistical mathematics is deleted from universities."],
                 0,
                 "마지막 문장에 드문 극적 참사는 과대평가하고 당뇨 등 평범하지만 치명적인 위험은 과소평가한다고 명시되어 있습니다.")
            ]
        ),
        (
            "i-99",
            "High-Temperature Cuprate Superconductivity",
            "고온 구리산화물 초전도체의 수수께끼",
            "Condensed Matter Physics",
            "Science & J. Georg Bednorz / K. Alex Müller Nobel Discovery",
            "액체 질소 비등점 이상에서 전기 저항이 0이 되는 고온 구리산화물 초전도체는 고전적 BCS 이론을 넘어서는 응집물질물리학의 최대 수수께끼입니다.",
            [
                ("Superconductivity is a quantum physical state / wherein electrical resistance vanishes entirely / and magnetic flux is expelled via the Meissner effect.",
                 "초전도 현상은 전기 저항이 완전히 소멸하고 / 마이스너 효과를 통해 자속이 외부로 밀려나는 / 양자 물리적 상태입니다.",
                 "Superconductivity is a quantum physical state / wherein electrical resistance vanishes entirely / and magnetic flux is expelled via the Meissner effect."),
                ("For decades, / physicists believed superconductivity could only occur / at temperatures hovering near absolute zero, / requiring prohibitively expensive liquid helium cooling.",
                 "수십 년 동안, / 물리학자들은 초전도성이 절대 영도 부근의 온도에서만 발생할 수 있다고 믿었으며, / 엄청나게 값비싼 액체 헬륨 냉각을 필요로 했습니다.",
                 "For decades, / physicists believed superconductivity could only occur / at temperatures hovering near absolute zero, / requiring prohibitively expensive liquid helium cooling."),
                ("In 1986, / researchers Georg Bednorz and Alex Müller stunned the scientific world / by discovering high-temperature superconductivity in ceramic cuprate materials / above the boiling point of liquid nitrogen.",
                 "1986년, / 연구자 게오르크 베드노르츠와 알렉스 뮐러는 / 액체 질소의 비등점보다 높은 온도에서 / 세라믹 구리산화물 물질의 고온 초전도성을 발견함으로써 과학계를 경악시켰습니다.",
                 "In 1986, / researchers Georg Bednorz and Alex Müller stunned the scientific world / by discovering high-temperature superconductivity in ceramic cuprate materials / above the boiling point of liquid nitrogen."),
                ("Because standard BCS electron-phonon pairing theory fails to explain / how electron pairs form within these complex layered copper-oxide planes, / solving this mechanism remains a holy grail of modern physics.",
                 "표준적인 BCS 전자-음향자 결합 이론은 / 이러한 복잡한 층상 구리 산화물 평면 내에서 전자쌍이 어떻게 형성되는지 설명하지 못하기 때문에, / 이 기전을 규명하는 것은 현대 물리학의 성배로 남아 있습니다.",
                 "Because standard BCS electron-phonon pairing theory fails to explain / how electron pairs form within these complex layered copper-oxide planes, / solving this mechanism remains a holy grail of modern physics.")
            ],
            [
                ("prohibitively", "adv.", "엄두도 못 낼 정도로, 과도하게", "Replacing entire aircraft engines is prohibitively expensive."),
                ("cuprate", "n./adj.", "구리산화물, 구리산염의", "High-temperature cuprate superconductors feature two-dimensional copper-oxygen sheets."),
                ("holy grail", "n. idiom", "성배 (모두가 갈망하는 궁극적 목표)", "Finding a unified field theory is considered the holy grail of theoretical physics."),
                ("expel", "v.", "퇴출시키다, 내쫓다, 밀어내다", "The human lung expels carbon dioxide during exhalation.")
            ],
            [
                ("wherein + 절", "'그 안에서 ~하는' 관계부사 wherein 절입니다."),
                ("above the boiling point of ~", "'~의 비등점 이상의 온도에서' 전치사구입니다.")
            ],
            [
                ("What two physical properties define a superconducting state?",
                 "어떤 두 물리적 특성이 초전도 상태를 규정하는가?",
                 ["Zero electrical resistance and magnetic expulsion (Meissner effect)", "Infinite heat generation and acoustic singing", "Turning solid metal into transparent liquid water", "Converting electrons into neutrons instantly"],
                 0,
                 "첫 문장에 전기 저항 완전 소멸과 자속 배출(마이스너 효과)이라고 명시되어 있습니다."),
                ("What was groundbreaking about Bednorz and Müller's 1986 discovery?",
                 "1986년 베드노르츠와 뮐러의 발견에서 획기적이었던 점은 무엇인가?",
                 ["They proved copper cannot conduct electricity.", "They discovered superconductivity in ceramic cuprates above the liquid nitrogen boiling point.", "They built a working time machine out of ice.", "They created artificial gravity on mountain peaks."],
                 1,
                 "세 번째 문장에 액체 질소 비등점 위에서 세라믹 구리산화물의 초전도성을 발견했다고 나와 있습니다."),
                ("Why is cuprate superconductivity still considered an open puzzle?",
                 "구리산화물 초전도성은 왜 여전히 미해결 난제로 여겨지는가?",
                 ["Because scientists lost all the laboratory samples", "Because standard BCS theory fails to explain pairing within layered copper-oxide planes", "Because copper-oxide materials turn into gold spontaneously", "Because nobody has ever been able to replicate the experiment"],
                 1,
                 "마지막 문장에 표준 BCS 이론이 층상 평면 내 전자쌍 형성을 설명하지 못하기 때문이라고 설명합니다.")
            ]
        ),
        (
            "i-100",
            "Choice Architecture and Behavioral Nudges",
            "선택 설계학과 행동경제학적 넛지",
            "Public Policy & Behavioral Economics",
            "Journal of Public Economics & Richard Thaler / Cass Sunstein 'Nudge'",
            "선택의 자유를 제한하거나 경제적 인센티브를 바꾸지 않고도 선택지의 기본값(디폴트) 설정을 변경하는 것만으로 사람들의 바람직한 결정을 유도할 수 있습니다.",
            [
                ("Traditional public policy historically assumed / that citizens behave as rational economic agents / who meticulously analyze all available options before deciding.",
                 "전통적인 공공 정책은 역사적으로 / 시민들이 결정하기 전 모든 가용한 선택지를 꼼꼼히 분석하는 / 합리적 경제 행위자로 행동한다고 가정했습니다.",
                 "Traditional public policy historically assumed / that citizens behave as rational economic agents / who meticulously analyze all available options before deciding."),
                ("However, / behavioral economists Richard Thaler and Cass Sunstein demonstrated / that subtle alterations in choice architecture / can dramatically influence outcomes without restricting freedom.",
                 "그러나, / 행동경제학자 리처드 탈러와 캐스 선스타인은 / 선택 설계의 미묘한 변경이 / 자유를 제한하지 않고도 결과를 극적으로 변화시킬 수 있음을 입증했습니다.",
                 "However, / behavioral economists Richard Thaler and Cass Sunstein demonstrated / that subtle alterations in choice architecture / can dramatically influence outcomes without restricting freedom."),
                ("Known as 'nudges,' / these interventions preserve libertarian choice / while leveraging cognitive biases like the default effect.",
                 "'넛지'라 알려진 / 이러한 개입들은 자유주의적 선택권을 보존하면서 / 디폴트(기본값) 효과와 같은 인지 편향을 활용합니다.",
                 "Known as 'nudges,' / these interventions preserve libertarian choice / while leveraging cognitive biases like the default effect."),
                ("For instance, / switching retirement pension enrollment from an 'opt-in' to an automatic 'opt-out' default / skyrocketed employee savings rates from under forty to over ninety percent.",
                 "예를 들어, / 퇴직 연금 가입 방식을 '선택 가입(opt-in)'에서 자동 가입 후 '선택 탈퇴(opt-out)' 기본값으로 전환하자, / 직원의 저축률이 40% 미만에서 90% 이상으로 급등했습니다.",
                 "For instance, / switching retirement pension enrollment from an 'opt-in' to an automatic 'opt-out' default / skyrocketed employee savings rates / from under forty to over ninety percent.")
            ],
            [
                ("alteration", "n.", "변경, 수정", "Minor architectural alterations improved natural daylight inside the office."),
                ("libertarian", "adj.", "자유주의적인", "Libertarian paternalism seeks to guide behavior while preserving personal choice."),
                ("leverage", "v.", "활용하다, 지렛대로 쓰다", "Startups leverage open-source tools to build software cost-effectively."),
                ("skyrocket", "v.", "급등하다, 치솟다", "Rental housing prices skyrocketed following the tech boom.")
            ],
            [
                ("without restricting freedom", "전치사 without + 동명사 구문으로 '자유를 제한함이 없이'를 뜻합니다."),
                ("switching A from B to C", "'A를 B에서 C로 전환하면서' 동명사 주어 구문입니다.")
            ],
            [
                ("What do 'nudges' do according to Richard Thaler and Cass Sunstein?",
                 "리처드 탈러와 캐스 선스타인에 따르면 '넛지'는 무엇을 하는가?",
                 ["Imprison anyone who fails to save money", "Influence choices through subtle design changes without restricting individual freedom", "Ban all forms of private pension funds", "Double income tax on luxury grocery items"],
                 1,
                 "두 번째 문장에 개인의 자유를 제한하지 않고 선택 설계의 변경을 통해 결과를 극적으로 유도한다고 나와 있습니다."),
                ("What cognitive bias do many nudges leverage?",
                 "많은 넛지는 어떤 인지 편향을 활용하는가?",
                 ["The default effect", "The photographic memory illusion", "The fear of blue light waves", "The instinct to run backwards"],
                 0,
                 "세 번째 문장에 디폴트(기본값) 효과와 같은 인지 편향을 활용한다고 명시되어 있습니다."),
                ("What happened when pension enrollment switched from opt-in to automatic opt-out?",
                 "연금 등록 방식이 opt-in에서 자동 opt-out으로 전환되었을 때 무슨 일이 일어났는가?",
                 ["All employees resigned simultaneously.", "Employee savings rates skyrocketed from under 40% to over 90%.", "The company went immediately bankrupt.", "Pensions were abolished across the country."],
                 1,
                 "마지막 문장에 직원 저축률이 40% 미만에서 90% 이상으로 치솟았다고 설명합니다.")
            ]
        )
    ]
