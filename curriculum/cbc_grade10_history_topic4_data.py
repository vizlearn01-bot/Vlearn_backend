"""
VLearn CBC Grade 10 History — Topic 4: Political Developments in Kenya Since Independence
Comprehensive Pedagogical Data Definitions (Lessons 1 to 4)
"""

from curriculum.cbc_grade10_history_topic4_svgs import (
    SVG_TIMELINE_POLITICAL_CHRONOLOGY,
    SVG_CHALLENGES_SOLUTIONS_MATRIX,
    SVG_BOUNDARY_FREE_SPEECH,
    SVG_CONSTITUTIONAL_EVOLUTION
)

TOPIC_4_LESSONS = [
    # =========================================================================
    # LESSON 1: Post-Independence Political Chronology
    # =========================================================================
    {
        "unit_order": 1,
        "unit_name": "Post-Independence Political Chronology",
        "unit_description": "Milestones in Kenya's governance from the 1963 constitutional monarchy to the 1964 Republic, one-party consolidation, the return to multi-party democracy, and the 2010 Constitution.",
        "lesson_title": "Post-Independence Political Chronology",
        "pages": [
            # Card 1: Orientation & Hook
            [
                {
                    "type": "suggested_image",
                    "title": "The Dawn of Independence in Kenya (1963)",
                    "content": {
                        "title": "Sovereignty and the Raising of the Kenyan Flag",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/4/49/Flag_of_Kenya.svg",
                        "caption": "The national flag of Kenya, first hoisted on December 12, 1963, marking the end of colonial rule and the birth of a sovereign African nation.",
                        "author": "Wikimedia Commons",
                        "licensing": "Public Domain / CC BY-SA"
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "The Journey of an Independent Nation",
                    "content": {
                        "text": (
                            "On **December 12, 1963**, the British Union Jack flag was lowered in Nairobi, "
                            "and the new black, red, and green flag of Kenya was raised. For the first time in nearly "
                            "seventy years, the destiny of Kenya lay in the hands of its own people.\n\n"
                            "However, winning independence was not the end of the journey; it was the beginning of a "
                            "complex, ongoing process of nation-building. How do you govern a diverse country with dozens of "
                            "distinct language groups? How do you build a strong economy and stable political institutions "
                            "after decades of colonial exploitation? In this lesson, we will explore the key chronological "
                            "milestones and transitions that have shaped Kenya's political landscape from independence in 1963 "
                            "to the present day."
                        )
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 1 Learning Outcomes",
                    "content": {
                        "text": (
                            "By the end of this lesson, you will be able to:\n\n"
                            "- Trace the constitutional transition from a **constitutional monarchy** (1963) to a **Republic** (1964)\n"
                            "- Analyze the causes and effects of the **KANU-KADU merger** (1964) and **Sessional Paper No. 10 of 1965**\n"
                            "- Differentiate between a **de facto** and a **de jure** one-party state under **Section 2A** (1982)\n"
                            "- Describe the restoration of multi-party democracy (1991) and the historic 2002 peaceful transfer of power\n"
                            "- Evaluate the impact of the **2007/2008 post-election crisis** and the transformative **2010 Constitution**"
                        )
                    }
                }
            ],

            # Card 2: Historical Context (Dominion to Republic 1963-64)
            [
                {
                    "type": "concept_explanation",
                    "title": "From Constitutional Monarchy to Republic (1963–1964)",
                    "content": {
                        "text": (
                            "When Kenya first achieved independence on **December 12, 1963**, it was not immediately a Republic. "
                            "Instead, it was a **constitutional monarchy** (Dominion) with Queen Elizabeth II of Britain remaining as the "
                            "nominal Head of State, represented locally in Nairobi by a Governor-General (Malcolm MacDonald).\n\n"
                            "The nation was governed under the **Independence Constitution**, which featured a decentralized regional "
                            "system of governance commonly called **Majimboism**. This regional structure had been strongly championed by "
                            "the **Kenya African Democratic Union (KADU)** to safeguard the interests and land rights of smaller ethnic communities.\n\n"
                            "This structure changed rapidly. On **December 12, 1964**, exactly one year after independence, Kenya officially "
                            "transitioned to **Republic Status**. The office of the Governor-General was abolished, Queen Elizabeth II ceased to "
                            "be Head of State, and **Jomo Kenyatta** was sworn in as Kenya's first President, combining the roles of Head of State, "
                            "Head of Government, and Commander-in-Chief of the Armed Forces."
                        )
                    }
                },
                {
                    "type": "comparison_table",
                    "title": "Constitutional Monarchy (1963) vs. Republic (1964)",
                    "content": {
                        "headers": ["Constitutional Feature", "1963 Independence Structure", "1964 Republic Structure"],
                        "rows": [
                            ["Head of State", "British Monarch (Queen Elizabeth II)", "Executive President (Jomo Kenyatta)"],
                            ["Local Representation", "Governor-General (Malcolm MacDonald)", "Office of the Governor-General abolished"],
                            ["System of Government", "Regional Federalism (Majimbo System)", "Centralized Unitary Republic"],
                            ["Legislature", "Bicameral (Senate & House of Representatives)", "National Assembly (Senate merged in 1966)"],
                            ["Executive Authority", "Divided between Prime Minister and Governor-General", "Fused in the President as Head of State & Government"]
                        ]
                    }
                }
            ],

            # Card 3: Core Knowledge (One-Party State 1964-91)
            [
                {
                    "type": "concept_explanation",
                    "title": "The Road to a One-Party State (1964–1991)",
                    "content": {
                        "text": (
                            "In the early days of independence, Kenya had two major political parties:\n"
                            "- **KANU (Kenya African National Union)**: Led by Jomo Kenyatta and Tom Mboya, advocating for a strong, centralized national government.\n"
                            "- **KADU (Kenya African Democratic Union)**: Led by Ronald Ngala and Daniel arap Moi, advocating for regional autonomy (Majimbo).\n\n"
                            "In late 1964, **KANU and KADU merged** when KADU voluntarily dissolved and its members crossed the floor to join KANU. "
                            "This merger effectively turned Kenya into a **de facto one-party state** (a nation where multiple parties are legally allowed, but only one exists in practice).\n\n"
                            "In **1965**, the government published **Sessional Paper No. 10 of 1965**, titled *African Socialism and its Application to Planning in Kenya*. "
                            "Written primarily under the guidance of Tom Mboya, this blueprint rejected pure capitalism and Soviet communism, proposing an economic model "
                            "based on mutual social responsibility and state guidance of private enterprise.\n\n"
                            "In **1966**, ideological differences led Jaramogi Oginga Odinga to resign as Vice President and form the opposition **Kenya People's Union (KPU)**. "
                            "Following the 1969 Kisumu hospital unrest, KPU was proscribed (banned), restoring the de facto one-party state. "
                            "Following the death of Jomo Kenyatta in 1978, **Daniel arap Moi** assumed the presidency. In **1982**, Parliament passed a constitutional amendment "
                            "inserting **Section 2A**, which legally prohibited all political parties other than KANU, turning Kenya into a **de jure one-party state**."
                        )
                    }
                },
                {
                    "type": "definition_card",
                    "title": "De Facto vs. De Jure One-Party State",
                    "content": {
                        "term": "De Facto vs. De Jure One-Party Rule",
                        "definition": "A **De Facto One-Party State** exists in political practice because opposition parties have voluntarily dissolved or failed to form, though the law does not explicitly forbid them (Kenya 1964–1966, 1969–1982). A **De Jure One-Party State** exists by constitutional law, where the constitution strictly makes all opposition parties illegal (Kenya 1982–1991 under Section 2A)."
                    }
                }
            ],

            # Card 4: Multi-Party Transition (1991-2002)
            [
                {
                    "type": "concept_explanation",
                    "title": "The Rebirth of Democracy (1991–2002)",
                    "content": {
                        "text": (
                            "During the late 1980s and early 1990s, pressure mounted on the government from citizens, civil society groups, "
                            "churches (such as the National Council of Churches of Kenya and vocal clerics like Rev. Timothy Njoya and Bishop Alexander Muge), "
                            "lawyers (LSK), and international development partners demanding political pluralism.\n\n"
                            "This civic agitation culminated in the **repeal of Section 2A on December 10, 1991**. The constitutional ban on opposition "
                            "parties was lifted, formally restoring **multi-party democracy** to Kenya.\n\n"
                            "New political parties formed rapidly, including the **Forum for the Restoration of Democracy (FORD)** and the **Democratic Party (DP)**. "
                            "The **1992 and 1997 general elections** were historic as the first multi-party elections in over two decades. However, the opposition remained "
                            "fractured along ethnic and personality lines, allowing KANU to retain power, while parts of the country experienced politically instigated ethnic clashes.\n\n"
                            "The monumental turning point arrived in the **2002 General Election**. The opposition formed a broad, unified alliance—the "
                            "**National Rainbow Coalition (NARC)**—under **Mwai Kibaki**. NARC decisively defeated the KANU candidate, marking the first peaceful, "
                            "democratic transfer of power from the ruling party to the opposition since 1963."
                        )
                    }
                },
                {
                    "type": "step_process",
                    "title": "Four Stages of the Democratic Transition (1991–2002)",
                    "content": {
                        "intro": "The restoration of competitive democracy in Kenya unfolded through four crucial phases:",
                        "steps": [
                            "**1. Pro-Democracy Agitation (1990–1991)**: Protests, Saba Saba rallies, and international pressure force the repeal of Section 2A.",
                            "**2. Divided Opposition Contests (1992 & 1997)**: Reintroduction of multi-party ballots, but fragmented opposition enables KANU victories.",
                            "**3. Inter-Parties Parliamentary Group (IPPG) Reforms (1997)**: Legislative agreements expand media access and electoral fairness.",
                            "**4. The 2002 Watershed Transfer**: Broad opposition unity under NARC leads to Mwai Kibaki's landslide victory and peaceful transition."
                        ]
                    }
                }
            ],

            # Card 5: Chronology / Timeline Visual
            [
                {
                    "type": "suggested_diagram",
                    "title": "Visual Chronology: Political History of Kenya (1963–Present)",
                    "content": {
                        "title": "Timeline of Kenya's Major Political Transitions",
                        "caption": "Milestones illustrating the transition from 1963 independence, the 1964 Republic, Section 2A de jure one-party rule, multi-party restoration in 1991, to the 2010 Constitution.",
                        "svg_content": SVG_TIMELINE_POLITICAL_CHRONOLOGY
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Summary of Key Chronological Shifts",
                    "content": {
                        "text": (
                            "- **1963**: Kenya achieves independence as a constitutional monarchy under Queen Elizabeth II.\n"
                            "- **1964**: Transition to Republic Status; KANU-KADU merger creates de facto one-party state.\n"
                            "- **1965**: Sessional Paper No. 10 outlines the economic vision of African Socialism.\n"
                            "- **1969**: KPU is banned following Kisumu unrest; de facto one-party state restored.\n"
                            "- **1982**: Section 2A amendment establishes de jure one-party state; August 1 attempted coup suppressed.\n"
                            "- **1991**: Repeal of Section 2A reintroduces multi-party democracy.\n"
                            "- **1992 & 1997**: First multi-party general elections held under the restored multi-party framework.\n"
                            "- **2002**: NARC wins general election, achieving Kenya's first peaceful democratic transition of power.\n"
                            "- **2007–2008**: Disputed election results trigger Post-Election Violence; National Accord signed under Kofi Annan.\n"
                            "- **August 27, 2010**: Promulgation of the Constitution of Kenya (2010), introducing Devolution and an expansive Bill of Rights."
                        )
                    }
                }
            ],

            # Card 6: New Constitutional Era (2007 Crisis & 2010 Constitution)
            [
                {
                    "type": "concept_explanation",
                    "title": "The 2007 Crisis and the Promulgation of the 2010 Constitution",
                    "content": {
                        "text": (
                            "The democratic trajectory of Kenya encountered its most severe challenge during the **2007/2008 Post-Election Violence (PEV)**. "
                            "Following deeply contested results in the December 2007 presidential election, widespread ethnic and political violence erupted, "
                            "resulting in over 1,000 deaths and the displacement of more than 600,000 citizens.\n\n"
                            "The crisis revealed catastrophic institutional weaknesses: total public distrust in the electoral commission and judiciary, "
                            "deep-seated ethnic grievances over historical land injustices, and excessive concentration of power in the national presidency.\n\n"
                            "To halt the destruction, the African Union appointed the **Panel of Eminent African Personalities**, chaired by former UN Secretary-General "
                            "**Kofi Annan**. Mediation resulted in the signing of the **National Accord and Reconciliation Agreement** on February 28, 2008, "
                            "forming a power-sharing Grand Coalition Government and mandating far-reaching constitutional reform under **Agenda Item 4**.\n\n"
                            "This historic journey concluded on **August 27, 2010**, with the official **promulgation of the Constitution of Kenya (2010)**. "
                            "The new constitution completely reshaped the governance landscape by:\n"
                            "- Establishing **Devolution** (distributing governance and minimum 15% revenue to 47 county governments)\n"
                            "- Enacting an enforceable, progressive **Bill of Rights** (Chapter Four)\n"
                            "- Creating an independent **Judiciary** with an apex **Supreme Court** to handle presidential election petitions\n"
                            "- Instituting independent constitutional oversight commissions (IEBC, NLC, NCIC, EACC)"
                        )
                    }
                },
                {
                    "type": "suggested_video",
                    "title": "Constitutional Development and Democratic Systems",
                    "content": {
                        "title": "Constitutional Systems and Checks and Balances",
                        "description": "Educational documentary examining the historical evolution of constitutions, separation of powers, and civic rights in democratic states.",
                        "youtube_id": "bO7FQsCcbD8"
                    }
                }
            ],

            # Card 7: Assessment & Review Questions
            [
                {
                    "type": "interactive_quiz",
                    "title": "Assessment Question 1: Section 2A Constitutional Amendment",
                    "content": {
                        "question": "Which constitutional amendment, passed in 1982 and repealed in 1991, made Kenya a legal (de jure) one-party state under KANU?",
                        "options": [
                            "A. Section 75",
                            "B. Section 2A",
                            "C. Article 201",
                            "D. Chapter Six"
                        ],
                        "correct_answer": "B",
                        "explanation": "Section 2A of the constitution was inserted in 1982 to legally ban all opposition parties and establish a de jure one-party state. It was repealed in December 1991 to restore multi-party democracy. Article 201 governs public finance, and Chapter Six addresses leadership and integrity."
                    }
                },
                {
                    "type": "interactive_quiz",
                    "title": "Assessment Question 2: The 1964 KANU-KADU Merger",
                    "content": {
                        "question": "What was the primary political outcome of the voluntary dissolution of KADU and its merger with KANU in late 1964?",
                        "options": [
                            "A. It led to the immediate division of Kenya into 47 county governments",
                            "B. It established a de facto one-party state under KANU",
                            "C. It resulted in the immediate outbreak of post-election violence",
                            "D. It restored Queen Elizabeth II as the permanent Head of State"
                        ],
                        "correct_answer": "B",
                        "explanation": "When KADU voluntarily dissolved and its members joined KANU in late 1964, Kenya was left with only one functioning political party, establishing a de facto one-party state. Devolution was created much later in 2010."
                    }
                },
                {
                    "type": "interactive_quiz",
                    "title": "Assessment Question 3: Significance of the 2002 Election",
                    "content": {
                        "question": "What is the historical significance of Mwai Kibaki's election under the NARC coalition in the 2002 General Election?",
                        "options": [
                            "A. It marked the first time Kenya became a Republic",
                            "B. It was the first peaceful, democratic transfer of power from the ruling party (KANU) to an opposition coalition since independence",
                            "C. It led to the immediate repeal of Section 2A",
                            "D. It abolished the Parliament of Kenya"
                        ],
                        "correct_answer": "B",
                        "explanation": "The 2002 election was historic because it marked the first peaceful and democratic transfer of executive power from the ruling KANU party to an opposition coalition (NARC). Kenya became a Republic in 1964, and Section 2A was repealed in 1991."
                    }
                },
                {
                    "type": "misconception_card",
                    "title": "Misconception: Republic Status at Independence",
                    "content": {
                        "misconception": "Kenya became a Republic on the exact day it gained independence on December 12, 1963.",
                        "correction": "On December 12, 1963, Kenya gained independence as a constitutional monarchy (Dominion) with Queen Elizabeth II as Head of State represented by a Governor-General. It was not until one year later, on December 12, 1964, that Kenya officially became a Republic with Jomo Kenyatta as its first President."
                    }
                }
            ]
        ]
    },

    # =========================================================================
    # LESSON 2: Political Challenges and Possible Solutions
    # =========================================================================
    {
        "unit_order": 2,
        "unit_name": "Political Challenges and Possible Solutions",
        "unit_description": "Investigation into major post-independence challenges—political assassinations, the 1982 attempted coup, ethnic divisions, and corruption—paired with institutional solutions from the 2010 Constitution.",
        "lesson_title": "Political Challenges and Possible Solutions",
        "pages": [
            # Card 1: Orientation & Hook
            [
                {
                    "type": "suggested_image",
                    "title": "The Parliament of Kenya, Nairobi",
                    "content": {
                        "title": "The National Assembly and Legislative Power",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/a/ad/Parliament_Buildings%2C_Nairobi%2C_Kenya-21April2010.jpg",
                        "caption": "The Parliament Buildings in Nairobi, where national laws, constitutional amendments, and investigative inquiries have shaped Kenyan political history since 1963.",
                        "author": "Wikimedia Commons",
                        "licensing": "CC BY-SA 3.0"
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Navigating the Storms of Nation-Building",
                    "content": {
                        "text": (
                            "Building a peaceful and prosperous nation is like sailing a large ship across an open ocean. "
                            "The destination is clear—a stable, united, and democratic society. But the sea is not always calm. "
                            "Strong winds, rough waves, and hidden reefs can threaten to push the ship off course or damage its hull.\n\n"
                            "In our first lesson, we mapped the chronological journey of Kenya since 1963. In this lesson, we will focus on the "
                            "**storms** that have tested the Kenyan political ship: major political challenges since independence, and the constructive "
                            "solutions and institutional measures designed to address them."
                        )
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 2 Learning Outcomes",
                    "content": {
                        "text": (
                            "By the end of this lesson, you will be able to:\n\n"
                            "- Analyze the causes and national impacts of **political assassinations** in post-colonial Kenya (Tom Mboya, JM Kariuki, Robert Ouko)\n"
                            "- Describe the events and governance consequences of the **August 1, 1982 attempted military coup**\n"
                            "- Evaluate how **ethnic division**, historical land injustices, and corruption undermined stability\n"
                            "- Map specific constitutional and institutional mechanisms (**Devolution, NCIC, NLC, IEBC, EACC**) to each political challenge\n"
                            "- Conduct a structured four-step **historical source analysis** on JM Kariuki's parliamentary speech"
                        )
                    }
                }
            ],

            # Card 2: Historical Context (Assassinations & Coup Attempts)
            [
                {
                    "type": "concept_explanation",
                    "title": "Political Instability and the Struggles of Governance",
                    "content": {
                        "text": (
                            "From the earliest years of the post-colonial era, Kenya faced fierce internal struggles for power and resource control. "
                            "Political differences were not always resolved through constitutional dialogue or democratic debate. In the 1960s, 1970s, "
                            "and 1980s, intense political rivalry occasionally turned fatal, resulting in the **political assassinations** of popular leaders:\n\n"
                            "- **Pio Gama Pinto (February 1965)**: Freedom fighter, socialist ideologue, and MP; independent Kenya's first political assassination.\n"
                            "- **Tom Mboya (July 5, 1969)**: Brilliant Minister for Economic Planning and KANU Secretary-General; his murder triggered widespread riots and deep ethnic alienation.\n"
                            "- **Josiah Mwangi (JM) Kariuki (March 1975)**: Vocal populist MP who criticized extreme wealth concentration; his murder sparked nationwide student protests.\n"
                            "- **Dr. Robert Ouko (February 1990)**: Minister for Foreign Affairs; his unexplained murder intensified domestic and international pressure for democratic reforms.\n\n"
                            "Furthermore, on **August 1, 1982**, low-ranking soldiers from the Kenya Air Force (led by Senior Private Hezekiah Ochuka) launched an **attempted military coup d'état** "
                            "to overthrow the government of President Daniel arap Moi. Although loyal army and police forces suppressed the coup within hours, it caused hundreds of civilian "
                            "and military deaths, widespread property destruction in Nairobi, and prompted a severe consolidation of executive control, including the enactment of Section 2A."
                        )
                    }
                }
            ],

            # Card 3: Core Knowledge (Four Major Political Challenges)
            [
                {
                    "type": "concept_explanation",
                    "title": "Four Major Political Challenges Since Independence",
                    "content": {
                        "text": (
                            "Historians identify four central challenges that have recurringly tested Kenya's political stability:\n\n"
                            "**1. Executive Centralization & Political Assassinations**:\n"
                            "The consolidation of immense power in the presidency weakened parliamentary oversight and compromised judicial independence. "
                            "The unresolved assassinations of prominent reformists created a culture of political fear and persistent public cynicism.\n\n"
                            "**2. Attempted Military Coups & State Repression**:\n"
                            "The 1982 coup attempt highlighted deep institutional disaffection. In its aftermath, the state clamped down on civil liberties, "
                            "curbed university academic freedom, and detained political dissidents without trial.\n\n"
                            "**3. Deep-Seated Ethnic and Political Divisions**:\n"
                            "Political parties were frequently organized along ethnic alliances rather than clear ideological principles. "
                            "This ethnic mobilization converted electoral contests into high-stakes ethnic competitions, occasionally sparking violence (such as in 1992, 1997, and 2007).\n\n"
                            "**4. Corruption and Historical Injustices**:\n"
                            "Abuse of public office, illegal alienation of public land (documented in the 2004 Ndung'u Land Report), and economic marginalization "
                            "of arid regions entrenched historical grievances that undermined national cohesion."
                        )
                    }
                },
                {
                    "type": "comparison_table",
                    "title": "Overview of Historical Political Crises in Kenya",
                    "content": {
                        "headers": ["Crisis Event", "Year", "Underlying Drivers", "Governance Impact"],
                        "rows": [
                            ["Tom Mboya Assassination", "1969", "Intra-party succession and ethnic power rivalries", "National unrest; proscription of KPU opposition party"],
                            ["JM Kariuki Assassination", "1975", "Outspoken critique of elite wealth concentration", "Parliamentary inquiry; deep public distrust of state security"],
                            ["Attempted Military Coup", "1982", "Economic stagnation, corruption, military disaffection", "Section 2A enacted; Air Force disbanded; executive tightening"],
                            ["Post-Election Violence", "2007–08", "Disputed presidential results, institutional distrust, land grievances", "Over 1,000 deaths; Kofi Annan mediation; 2010 Constitution"]
                        ]
                    }
                }
            ],

            # Card 4: Systemic Solutions Matrix
            [
                {
                    "type": "suggested_diagram",
                    "title": "Political Challenges & Constitutional Solutions Matrix",
                    "content": {
                        "title": "Institutional Remedies in the 2010 Constitution",
                        "caption": "Infographic mapping historical governance challenges in post-independence Kenya to the constitutional remedies established under the 2010 Constitution.",
                        "svg_content": SVG_CHALLENGES_SOLUTIONS_MATRIX
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Systemic Institutional Solutions",
                    "content": {
                        "text": (
                            "To systematically resolve these historical challenges, the **Constitution of Kenya (2010)** instituted structural reforms:\n\n"
                            "- **Executive Centralization &#8594; Devolution & Separation of Powers**: Articles 174–200 decentralized governance to 47 county governments, ensuring regional resource sharing and checks on the presidency.\n"
                            "- **Historical Injustices & Land Grabbing &#8594; National Land Commission (NLC) & TJRC**: Article 67 established the NLC to manage public land and investigate historical land injustices.\n"
                            "- **Ethnic Discrimination & Tribalism &#8594; NCIC & Equalization Fund**: The National Cohesion and Integration Commission combats hate speech, while Article 204 dedicates funds to previously marginalized areas.\n"
                            "- **Electoral Malpractice & Disputed Polls &#8594; Independent IEBC & Supreme Court**: Article 88 mandates transparent elections, while Article 140 empowers the Supreme Court to adjudicate presidential dispute petitions peacefully.\n"
                            "- **Corruption & Impunity &#8594; Chapter Six & EACC**: Chapter Six establishes mandatory ethical standards for state officers, enforced by the Ethics and Anti-Corruption Commission."
                        )
                    }
                }
            ],

            # Card 5: Source Analysis Activity (JM Kariuki Testimony)
            [
                {
                    "type": "concept_explanation",
                    "title": "Primary Source: JM Kariuki's Outspoken Testimony",
                    "content": {
                        "text": (
                            "Read the following primary source excerpt from a speech delivered by Josiah Mwangi (JM) Kariuki in Parliament in the early 1970s:\n\n"
                            "> *\"Kenya has become a nation of ten millionaires and ten million beggars... We do not want a nation where a few people "
                            "live in luxury and the majority live in absolute poverty. We must build a country where every Kenyan can afford three meals "
                            "a day, has access to clean water, and can send their children to school without fear of discrimination.\"*\n\n"
                            "— **Josiah Mwangi (JM) Kariuki**, MP for Nyandarua North"
                        )
                    }
                },
                {
                    "type": "step_process",
                    "title": "Four-Step Historical Source Analysis",
                    "content": {
                        "intro": "Apply the historical inquiry method to evaluate JM Kariuki's speech:",
                        "steps": [
                            "**1. Origin & Creator**: Josiah Mwangi Kariuki, a veteran of the Mau Mau liberation struggle, Assistant Minister, and outspoken Member of Parliament.",
                            "**2. Context & Purpose**: Delivered in the early 1970s to criticize the Jomo Kenyatta administration's economic policies, which Kariuki argued were concentrating land and wealth in the hands of a small political elite.",
                            "**3. Historical Insight**: It proves that severe economic inequality, land grievances, and internal dissent existed within the ruling establishment during early post-colonial Kenya.",
                            "**4. Limitations**: As a populist parliamentary speech, it reflects Kariuki's political perspective and rhetorical emphasis rather than comprehensive economic statistics or official government planning justifications."
                        ]
                    }
                }
            ],

            # Card 6: Institutional Architecture & Video
            [
                {
                    "type": "concept_explanation",
                    "title": "Building Resilient Democratic Institutions",
                    "content": {
                        "text": (
                            "Constitutional provisions are only as effective as the institutions designed to enforce them. "
                            "In modern Kenya, the establishment of independent oversight commissions, an impartial judiciary, "
                            "and an active civil society ensures that political disputes are resolved within courtrooms and legislative chambers "
                            "rather than through civil unrest.\n\n"
                            "The Supreme Court's constitutional role under Article 140—adjudicating presidential election petitions within 14 days—provides "
                            "a structured, peaceful mechanism to address disputed election results, reinforcing public trust in democratic governance."
                        )
                    }
                },
                {
                    "type": "suggested_video",
                    "title": "Institutional Governance and Democratic Accountability",
                    "content": {
                        "title": "How Democratic Institutions Prevent State Failure",
                        "description": "Educational analysis of how checks and balances, independent commissions, and economic oversight safeguard national stability.",
                        "youtube_id": "fTTGALaRZoc"
                    }
                }
            ],

            # Card 7: Assessment & Review Questions
            [
                {
                    "type": "interactive_quiz",
                    "title": "Assessment Question 1: National Cohesion Commission",
                    "content": {
                        "question": "Which independent commission was established following the 2010 constitutional reform specifically to combat ethnic discrimination, investigate hate speech, and promote national unity in Kenya?",
                        "options": [
                            "A. The Kenya Revenue Authority (KRA)",
                            "B. The National Cohesion and Integration Commission (NCIC)",
                            "C. The National Land Commission (NLC)",
                            "D. The Teachers Service Commission (TSC)"
                        ],
                        "correct_answer": "B",
                        "explanation": "The NCIC is legally mandated to eliminate ethnic discrimination, combat hate speech, and foster national cohesion. KRA collects revenue, and NLC manages public land disputes."
                    }
                },
                {
                    "type": "interactive_quiz",
                    "title": "Assessment Question 2: Governance Impact of the 1982 Coup Attempt",
                    "content": {
                        "question": "How did the aftermath of the August 1, 1982 attempted military coup directly affect Kenyan governance during the rest of the 1980s?",
                        "options": [
                            "A. It led to the immediate establishment of multi-party democracy",
                            "B. It caused the voluntary merger of KANU and KADU",
                            "C. It resulted in the constitutional enactment of Section 2A and tighter political control by the state",
                            "D. It dissolved the office of the President and established a Prime Minister"
                        ],
                        "correct_answer": "C",
                        "explanation": "Following the 1982 coup attempt, the government intensified executive control and enacted Section 2A of the constitution, legally transforming Kenya into a de jure one-party state."
                    }
                },
                {
                    "type": "misconception_card",
                    "title": "Misconception: Post-Independence Assassinations",
                    "content": {
                        "misconception": "Political assassinations in post-independence Kenya were isolated criminal incidents with no broader political causes or consequences.",
                        "correction": "Historical evidence demonstrates that assassinations (such as those of Tom Mboya in 1969 and JM Kariuki in 1975) were deeply connected to struggles over political succession, ideological differences, and national wealth distribution, triggering major political crises and protests."
                    }
                }
            ]
        ]
    },

    # =========================================================================
    # LESSON 3: Promoting Peaceful Political Environments
    # =========================================================================
    {
        "unit_order": 3,
        "unit_name": "Promoting Peaceful Political Environments",
        "unit_description": "Strategies for peacebuilding in Kenya: dialogue, mediation, community policing, youth engagement, responsible media, Article 33 free speech boundaries, and digital information literacy.",
        "lesson_title": "Promoting Peaceful Political Environments",
        "pages": [
            # Card 1: Orientation & Hook
            [
                {
                    "type": "suggested_image",
                    "title": "Mediation and National Reconciliation",
                    "content": {
                        "title": "International Mediation and the National Accord",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/7/72/Kofi_Annan_2012_%28cropped%29.jpg",
                        "caption": "Former UN Secretary-General Kofi Annan, who led the African Union mediation team during the 2008 Kenyan National Dialogue and Reconciliation process.",
                        "author": "Wikimedia Commons",
                        "licensing": "CC BY-SA 3.0"
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "The Foundation of Progress — Why Peace is Not Silent",
                    "content": {
                        "text": (
                            "Some people believe that a 'peaceful political environment' simply means an environment where there is no shouting, "
                            "no protests, and no disagreements. But that is not true peace; that is the **silence of fear**.\n\n"
                            "In a vibrant democratic society, citizens will naturally hold different political opinions, support different candidates, "
                            "and debate how public funds should be spent. Disagreement is healthy and essential for democratic accountability.\n\n"
                            "A truly **peaceful political environment** is one where disagreements are resolved through **democratic institutions, "
                            "structured dialogue, and the rule of law**, rather than violence, intimidation, or hate speech. In this lesson, we will "
                            "explore the multi-stakeholder strategies used to cultivate and defend political peace in Kenya."
                        )
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 3 Learning Outcomes",
                    "content": {
                        "text": (
                            "By the end of this lesson, you will be able to:\n\n"
                            "- Distinguish between **negative peace** (absence of violence) and **positive peace** (justice, equality, and rule of law)\n"
                            "- Analyze the role of mediation and the **2008 National Accord** in resolving electoral conflict\n"
                            "- Detail the **five national strategies** for cultivating a peaceful political environment in Kenya\n"
                            "- Differentiate between protected **freedom of expression** (Article 33(1)) and unlawful **hate speech** (Article 33(2))\n"
                            "- Apply the **'Stop, Think, Verify'** digital literacy model to counter political disinformation"
                        )
                    }
                }
            ],

            # Card 2: Historical Context (Mediation & National Accord)
            [
                {
                    "type": "concept_explanation",
                    "title": "From Electoral Conflict to Mediation: The 2008 Serena Talks",
                    "content": {
                        "text": (
                            "Following the disputed December 2007 presidential elections and the outbreak of Post-Election Violence, Kenya stood at the brink of civil war. "
                            "The crisis proved that military force alone could not resolve deep-rooted political disputes.\n\n"
                            "In January 2008, the African Union established the **Panel of Eminent African Personalities**, led by **Kofi Annan**, alongside former Tanzanian President "
                            "**Benjamin Mkapa** and former First Lady of Mozambique and South Africa **Graça Machel**. The mediation talks—known as the **Serena Talks**—brought together "
                            "representatives of the Party of National Unity (PNU) and the Orange Democratic Movement (ODM).\n\n"
                            "On **February 28, 2008**, President Mwai Kibaki and ODM leader Raila Odinga signed the historic **National Accord and Reconciliation Agreement**. "
                            "The agreement structured peace around four essential agenda items:\n"
                            "- **Agenda 1**: Immediate cessation of violence and restoration of fundamental rights.\n"
                            "- **Agenda 2**: Immediate humanitarian measures to assist internally displaced persons (IDPs).\n"
                            "- **Agenda 3**: Resolving the political impasse through a power-sharing Grand Coalition Government.\n"
                            "- **Agenda 4**: Addressing long-term structural issues: constitutional reform, land reform, institutional strengthening, and youth unemployment.\n\n"
                            "This historic mediation proved that sustainable peace is built through compromise, dialogue, and comprehensive constitutional reform."
                        )
                    }
                }
            ],

            # Card 3: Core Knowledge (Five National Peacebuilding Strategies)
            [
                {
                    "type": "concept_explanation",
                    "title": "Five National Strategies for Peacebuilding",
                    "content": {
                        "text": (
                            "Kenya employs five core institutional and societal strategies to foster a peaceful political environment:\n\n"
                            "**1. Dialogue and Reconciliation**:\n"
                            "Facilitating structured discussions among opposing political parties, local councils of elders, and the Inter-Religious Council of Kenya (IRCK) "
                            "to de-escalate tensions before they turn violent.\n\n"
                            "**2. Community Policing (Nyumba Kumi)**:\n"
                            "Fostering active partnerships where local residents collaborate with national police officers to share information, identify security risks, "
                            "and maintain neighborhood safety as trusted partners.\n\n"
                            "**3. Youth Engagement and Economic Empowerment**:\n"
                            "Equipping young people through vocational skills, technical training, and civic mentorship so they participate positively in governance "
                            "rather than being manipulated by unscrupulous politicians as agents of political violence.\n\n"
                            "**4. Media Responsibility and Fact-Checking**:\n"
                            "Upholding ethical journalism through the Media Council of Kenya (MCK) to ensure fair reporting, fact-checking political claims, "
                            "and prohibiting broadcasts that incite ethnic hatred.\n\n"
                            "**5. Cultural Diversity and National Festivals**:\n"
                            "Celebrating multi-ethnic cultural festivals, national school drama/music festivals, and national holidays (Madaraka Day, Mashujaa Day, Jamhuri Day) "
                            "to celebrate cultural diversity while reinforcing a unified national identity."
                        )
                    }
                },
                {
                    "type": "comparison_table",
                    "title": "Negative Peace vs. Positive Peace",
                    "content": {
                        "headers": ["Characteristic", "Negative Peace", "Positive Peace"],
                        "rows": [
                            ["Definition", "Mere absence of active physical fighting or riots", "Presence of justice, equity, human rights, and institutional fairness"],
                            ["Enforcement Mechanism", "Heavy military/police patrols, curfews, silencing dissent", "Dialogue, fair democratic elections, rule of law, devolved development"],
                            ["Sustainability", "Fragile and unstable; underlying grievances remain unaddressed", "Resilient and long-lasting; conflicts resolved constructively through institutions"],
                            ["Citizen Role", "Fearful obedience and political passivity", "Active, media-literate civic participation and peaceful advocacy"]
                        ]
                    }
                }
            ],

            # Card 4: Critical Thinking (Free Speech vs Hate Speech & SVG)
            [
                {
                    "type": "suggested_diagram",
                    "title": "The Boundary of Free Speech: Article 33",
                    "content": {
                        "title": "Balancing Free Expression and Constitutional Limits",
                        "caption": "A balance scale diagram contrasting constitutionally protected expression under Article 33(1) with strictly prohibited hate speech and incitement under Article 33(2).",
                        "svg_content": SVG_BOUNDARY_FREE_SPEECH
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Understanding Article 33: Expression vs. Incitement",
                    "content": {
                        "text": (
                            "Under **Article 33** of the Constitution of Kenya (2010), every citizen has the fundamental right to **freedom of expression**.\n\n"
                            "**Protected Under Article 33(1)**:\n"
                            "- Freedom to seek, receive, or impart information and ideas.\n"
                            "- Freedom of artistic creativity and scientific research.\n"
                            "- Freedom to critique public policies, scrutinize government expenditures, and engage in vigorous political debate.\n\n"
                            "**Strictly Prohibited Under Article 33(2)**:\n"
                            "- **Propaganda for war**.\n"
                            "- **Incitement to violence**.\n"
                            "- **Hate Speech**: Speech that vilifies, degrades, or incites hatred against an individual or community based on ethnicity, race, religion, gender, or disability.\n\n"
                            "Under the **National Cohesion and Integration Commission (NCIC) Act of 2008**, publishing or uttering hate speech carries criminal penalties, "
                            "including heavy fines up to KES 1 million or imprisonment for up to 3 years."
                        )
                    }
                }
            ],

            # Card 5: Real-World Application (Digital Information Literacy)
            [
                {
                    "type": "step_process",
                    "title": "The 'Stop, Think, Verify' Framework for Digital Literacy",
                    "content": {
                        "intro": "In the digital age, political misinformation on social media can spark panic in minutes. Practice this verification framework:",
                        "steps": [
                            "**1. Stop**: When you encounter an inflammatory political post, viral audio clip, or breaking headline, pause immediately before sharing or forwarding.",
                            "**2. Think**: Ask critical questions: Is this post designed to evoke anger or fear? Who created it, and what political agenda do they serve?",
                            "**3. Verify**: Cross-check the information against accredited news outlets, official government statements, and independent fact-checkers (e.g., Africa Check, PesaCheck).",
                            "**4. Report**: Flag unverified rumors, fabricated videos (deepfakes), and ethnic slurs to platform moderators and the NCIC."
                        ]
                    }
                }
            ],

            # Card 6: Practice & Video (Community Dispute Mediation)
            [
                {
                    "type": "concept_explanation",
                    "title": "Role-Play Scenario: Mediating a Cross-County Water Dispute",
                    "content": {
                        "text": (
                            "**Scenario**: During a severe drought, tensions rise between Community A (upstream) and Community B (downstream) along a river border. "
                            "Community B accuses Community A of diverting river water for irrigation, leaving livestock downstream without drinking water. "
                            "Youth on both sides threaten violent confrontation.\n\n"
                            "**Structured Mediation Steps**:\n"
                            "1. **Identify Stakeholders**: Bring together local elders, youth leaders, water resource authority officers, and county administration.\n"
                            "2. **Gather Evidence**: Inspect water intake meters and review the regional water management schedule.\n"
                            "3. **Facilitate Dialogue**: Provide a neutral forum where both parties state their community's needs without interruption.\n"
                            "4. **Draft Shared Agreement**: Establish a rotational water-rationing timetable and form a joint inter-community monitoring committee.\n\n"
                            "*Why is institutional mediation far more sustainable than deploying armed police to suppress the dispute?*"
                        )
                    }
                },
                {
                    "type": "suggested_video",
                    "title": "Constitutional Rights, Free Speech, and Rule of Law",
                    "content": {
                        "title": "The Boundaries of Free Expression and Conflict Resolution",
                        "description": "Educational overview of democratic rights, the rule of law, and institutional mechanisms for maintaining peace in society.",
                        "youtube_id": "rNu8XDBSn10"
                    }
                }
            ],

            # Card 7: Assessment & Review Questions
            [
                {
                    "type": "interactive_quiz",
                    "title": "Assessment Question 1: Community Policing",
                    "content": {
                        "question": "Which of the following best describes 'community policing' as a peacebuilding strategy in Kenya?",
                        "options": [
                            "A. Deploying the national military to patrol civilian neighborhoods during elections",
                            "B. Establishing a collaborative partnership where local citizens and police officers work together to maintain security",
                            "C. Allowing private citizens to form armed vigilante groups to enforce their own laws",
                            "D. Banning all public participation forums to prevent political arguments"
                        ],
                        "correct_answer": "B",
                        "explanation": "Community policing relies on trust and cooperation between residents and law enforcement officers. Vigilantism (Option C) and military enforcement (Option A) violate the rule of law."
                    }
                },
                {
                    "type": "interactive_quiz",
                    "title": "Assessment Question 2: Protected Free Speech under Article 33",
                    "content": {
                        "question": "Under Article 33 of the Constitution of Kenya (2010), which of the following is protected under the fundamental right to freedom of expression?",
                        "options": [
                            "A. Inciting a crowd to burn down a public market",
                            "B. Publishing a critical analytical article evaluating county government budget expenditures",
                            "C. Broadcasting ethnic slurs against a minority community during a political rally",
                            "D. Urging youth to mobilize weapons for post-election clashes"
                        ],
                        "correct_answer": "B",
                        "explanation": "Scrutinizing public expenditure and critiquing government policies is a constitutionally protected right and civic duty under Article 33(1). Incitement to violence and ethnic slurs (Options A, C, D) are strictly excluded under Article 33(2)."
                    }
                },
                {
                    "type": "misconception_card",
                    "title": "Misconception: The Meaning of Political Peace",
                    "content": {
                        "misconception": "A peaceful political environment means that citizens never disagree with leaders, question government decisions, or hold peaceful protests.",
                        "correction": "In a democracy, robust disagreement, critical scrutiny, and lawful peaceful assembly are signs of a healthy political environment. Peace is broken only when disagreements turn into violence, intimidation, or hate speech."
                    }
                }
            ]
        ]
    },

    # =========================================================================
    # LESSON 4: Political History Inquiry
    # =========================================================================
    {
        "unit_order": 4,
        "unit_name": "Political History Inquiry",
        "unit_description": "Historical dossier analysis comparing Section 2A (1982) with the 2010 Constitution (Articles 1 & 4), voter registration trends, and a comparative inquiry into the 1992 vs. 2002 democratic transitions.",
        "lesson_title": "Political History Inquiry",
        "pages": [
            # Card 1: Orientation & Hook
            [
                {
                    "type": "suggested_image",
                    "title": "The Supreme Court of Kenya",
                    "content": {
                        "title": "Apex Judicial Custodian of Constitutional Democracy",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/f/fa/Supreme_Court_of_Kenya_05.jpg",
                        "caption": "The Supreme Court of Kenya in Nairobi, established by the 2010 Constitution to protect the rule of law and impartially resolve constitutional and electoral disputes.",
                        "author": "Wikimedia Commons",
                        "licensing": "CC BY-SA 4.0"
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Deconstructing Our Political Past: The Historical Detective",
                    "content": {
                        "text": (
                            "How do we evaluate the overall progress of Kenya's political system since independence in 1963?\n\n"
                            "Some historians argue that Kenya has made extraordinary democratic strides: transitioning from a rigid, centralized "
                            "one-party state into a vibrant, decentralized multi-party democracy with a progressive Bill of Rights and an independent judiciary.\n\n"
                            "Other scholars contend that deep-seated ethnic voting blocs, corruption, and socio-economic inequality continue to hinder the realization "
                            "of true democratic ideals, arguing that institutional reforms have not completely eliminated historical patterns of political patronage.\n\n"
                            "As historical detectives, we recognize that **both perspectives contain vital truths**. In this culminating inquiry lesson, you will "
                            "examine primary legal texts, statistical voter datasets, and comparative case studies to formulate your own evidence-based assessment of "
                            "change and continuity in Kenya's political history."
                        )
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 4 Learning Outcomes",
                    "content": {
                        "text": (
                            "By the end of this lesson, you will be able to:\n\n"
                            "- Compare primary constitutional texts (**1982 Section 2A** vs. **2010 Articles 1 & 4**)\n"
                            "- Analyze historical voter registration trends from 1963 (1.2M) to 2022 (22.1M)\n"
                            "- Conduct a comparative inquiry between the **1992 and 2002 democratic transitions**\n"
                            "- Formulate evidence-based arguments evaluating **political continuity and change** in Kenya\n"
                            "- Synthesize all four lessons into an integrated understanding of Kenya's post-independence journey"
                        )
                    }
                }
            ],

            # Card 2: The Historical Dossier (Three Archival Sources)
            [
                {
                    "type": "concept_explanation",
                    "title": "The Historical Dossier: Three Archival Sources",
                    "content": {
                        "text": (
                            "Examine the following primary and statistical evidence:\n\n"
                            "###### Source A: Section 2A of the Constitution of Kenya (Enacted in 1982)\n"
                            "> *\"There shall be in Kenya only one political party, the Kenya African National Union.\"*\n\n"
                            "###### Source B: Chapter One of the Constitution of Kenya (Promulgated in 2010)\n"
                            "> **Article 1: Sovereignty of the people**\n"
                            "> 1. All sovereign power belongs to the people of Kenya and shall be exercised only in accordance with this Constitution.\n"
                            "> 2. The people may exercise their sovereign power either directly or indirectly through their democratically elected representatives.\n\n"
                            "> **Article 4: Declaration of the Republic**\n"
                            "> 1. Kenya is a sovereign Democratic Republic.\n"
                            "> 2. The Republic of Kenya shall be a multi-party democratic State founded on the national values and principles of governance referred to in Article 10.\n\n"
                            "###### Source C: National Voter Registration Growth Trends (1963–2022)\n"
                            "- **1963 Independence Election**: ~1.2 million registered voters (limited franchise, first post-independence assembly).\n"
                            "- **1992 Multi-Party Election**: ~7.9 million registered voters (first multi-party poll following repeal of Section 2A).\n"
                            "- **2002 Democratic Transition**: ~10.5 million registered voters (historic opposition coalition victory under NARC).\n"
                            "- **2013 First Devolved Election**: ~14.4 million registered voters (implementation of county governments and Supreme Court oversight).\n"
                            "- **2022 General Election**: ~22.1 million registered voters (biometric voter verification and public digital results transmission)."
                        )
                    }
                }
            ],

            # Card 3: Critical Thinking (Analyzing the Dossier)
            [
                {
                    "type": "step_process",
                    "title": "Guided Historical Inquiry Tasks",
                    "content": {
                        "intro": "Use historical reasoning skills to evaluate the evidence dossier:",
                        "steps": [
                            "**1. Analyze Legal Change**: Contrast the legal monopoly of political power in Source A with the principle of popular sovereignty and multiparty democracy in Source B. How did the locus of sovereignty fundamentally shift?",
                            "**2. Evaluate Political Continuity**: Despite the comprehensive constitutional transformation from 1982 to 2010, why have ethnic coalitions and regional voting blocs remained influential in contemporary Kenyan elections?",
                            "**3. Interpret Demographic Expansion**: How does the eighteen-fold increase in voter registration from 1.2 million in 1963 to 22.1 million in 2022 (Source C) reflect expanding civic participation, universal franchise, and youth empowerment?"
                        ]
                    }
                }
            ],

            # Card 4: Comparative Inquiry Dossier (1992 vs 2002 Transitions)
            [
                {
                    "type": "comparison_table",
                    "title": "Comparative Inquiry: The 1992 vs. 2002 Democratic Transitions",
                    "content": {
                        "headers": ["Inquiry Dimension", "1992 Multi-Party Election", "2002 Democratic Transition"],
                        "rows": [
                            ["Opposition Unity", "Fragmented into competing parties (FORD-Asili, FORD-Kenya, DP)", "United under a single national coalition (NARC)"],
                            ["Electoral Environment", "Partisan state machinery; state-dominated broadcast media", "IPPG reforms in place; pluralistic media; active election observation"],
                            ["Security & Clashes", "Severe politically instigated ethnic clashes in Rift Valley & Western", "Peaceful nationwide voting; heightened civic vigilance"],
                            ["Electoral Outcome", "President Daniel arap Moi & KANU won with ~36% plurality of votes", "Mwai Kibaki & NARC won decisively with over 62% majority"],
                            ["Historical Significance", "Restored multi-party competition after 26 years; exposed ethnic fragility", "First peaceful, democratic transfer of power from ruling party to opposition"]
                        ]
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Historical Deductions from the 1992 & 2002 Comparative Inquiry",
                    "content": {
                        "text": (
                            "Comparing the 1992 and 2002 general elections yields critical historical insights:\n\n"
                            "1. **Institutional Reform is Crucial**: Multi-party laws alone were insufficient in 1992 because electoral administrative structures remained biased. The 1997 IPPG reforms helped level the playing field for the 2002 contest.\n"
                            "2. **Coalition Politics as a Transformative Tool**: In 1992, a divided opposition split the pro-reform vote. In 2002, broad-based coalition building enabled the opposition to cross ethnic divides and secure a decisive majority.\n"
                            "3. **The Precedent of Peaceful Power Transfer**: The 2002 election proved that an African ruling party in power for nearly four decades could be peacefully voted out, cementing Kenya's democratic credentials."
                        )
                    }
                }
            ],

            # Card 5: Constitutional Evolution Framework & Video
            [
                {
                    "type": "suggested_diagram",
                    "title": "Constitutional Evolution Framework: 1982 vs. 2010",
                    "content": {
                        "title": "The Locus of Sovereignty Transformation",
                        "caption": "Visual diagram detailing the historical transfer of sovereignty from executive party monopoly (Section 2A) to popular citizen sovereignty and devolved governance (Articles 1 & 4).",
                        "svg_content": SVG_CONSTITUTIONAL_EVOLUTION
                    }
                },
                {
                    "type": "suggested_video",
                    "title": "Democratic Evolution and Historical Inquiry",
                    "content": {
                        "title": "Analyzing Democratic Transitions and Constitutional Law",
                        "description": "Documentary exploring historical methodology, democratic transitions, and constitutional evolution in post-colonial governance.",
                        "youtube_id": "T_sGTspaF4Y"
                    }
                }
            ],

            # Card 6: Topic Synthesis & Essay Formulation Guide
            [
                {
                    "type": "concept_explanation",
                    "title": "Topic 1.4 Synthesis: Change, Continuity, and the Democratic Path",
                    "content": {
                        "text": (
                            "Let us synthesize the core thematic threads of Topic 1.4:\n\n"
                            "- **Chronological Evolution (Lesson 1)**: Kenya evolved from a 1963 constitutional monarchy to a 1964 Republic, traversed de facto and de jure one-party rule, restored multi-party democracy in 1991, and established a devolved constitutional order in 2010.\n"
                            "- **Navigating Political Challenges (Lesson 2)**: The nation endured severe shocks—assassinations, the 1982 coup attempt, and ethnic polarization—countered by modern institutional remedies like Devolution, NCIC, NLC, and IEBC.\n"
                            "- **Promoting Peace Architecture (Lesson 3)**: Sustainable peace is built on positive peace, mediation (the 2008 National Accord), community policing, Article 33 free speech limits, and digital media literacy.\n"
                            "- **Historical Inquiry (Lesson 4)**: Primary evidence demonstrates that while legal frameworks have undergone profound transformation, citizen vigilance and ethical leadership remain essential to overcome persistent ethnic division and corruption."
                        )
                    }
                },
                {
                    "type": "step_process",
                    "title": "Historical Inquiry Essay Writing Scaffold",
                    "content": {
                        "intro": "When writing an evidence-based historical essay on Kenya's political developments:",
                        "steps": [
                            "**1. Formulate a Clear Thesis**: State an arguable claim (e.g., 'While Kenya achieved major institutional reforms through the 2010 Constitution, ethnic mobilization remains a persistent continuity in election cycles').",
                            "**2. Present Primary Evidence**: Support arguments using specific textual references (Section 2A, Article 1, voter registration figures, or JM Kariuki's testimony).",
                            "**3. Evaluate Counter-Arguments**: Weigh conflicting historical interpretations with balanced nuance.",
                            "**4. Synthesize Historical Significance**: Explain how historical milestones continue to shape contemporary Kenyan governance and citizenship."
                        ]
                    }
                }
            ],

            # Card 7: Assessment & Review Questions
            [
                {
                    "type": "interactive_quiz",
                    "title": "Assessment Question 1: Political Continuity vs. Change",
                    "content": {
                        "question": "Which of the following pairs accurately represents an example of political continuity and political change in Kenya between the 1980s and the post-2010 era?",
                        "options": [
                            "A. Continuity: Section 2A remained in force; Change: Jomo Kenyatta remained President",
                            "B. Continuity: KANU remained the sole legal political party; Change: Queen Elizabeth II remained Head of State",
                            "C. Continuity: Ethnic voting alliances persisted in general elections; Change: Devolution decentralized executive power and budgets to 47 counties",
                            "D. Continuity: The central government in Nairobi managed all county functions; Change: Multi-party elections were legally banned"
                        ],
                        "correct_answer": "C",
                        "explanation": "This pair correctly identifies continuity (ethnic mobilization has persisted across election cycles) and transformative constitutional change (Devolution established 47 county governments and shared public finances). Options A, B, and D contain historical inaccuracies."
                    }
                },
                {
                    "type": "interactive_quiz",
                    "title": "Assessment Question 2: Comparing Constitutional Sovereignty",
                    "content": {
                        "question": "When comparing Section 2A of the 1982 Constitution with Article 1 of the 2010 Constitution, what is the fundamental historical shift regarding sovereignty?",
                        "options": [
                            "A. Sovereignty was transferred from the people to a single ruling political party",
                            "B. Sovereignty shifted from state monopoly under a single political party to popular sovereignty belonging to all the people of Kenya",
                            "C. Sovereignty was transferred to the Governor-General of the British Crown",
                            "D. Sovereignty was eliminated entirely in favor of regional assembly rule"
                        ],
                        "correct_answer": "B",
                        "explanation": "Section 2A established a single-party monopoly over the state, whereas Article 1 of the 2010 Constitution explicitly declares that all sovereign power belongs to the people of Kenya and is exercised in accordance with the Constitution."
                    }
                },
                {
                    "type": "misconception_card",
                    "title": "Misconception: Constitutional Reform and Instant Solutions",
                    "content": {
                        "misconception": "Promulgating the 2010 Constitution automatically eliminated all political corruption, tribalism, and governance challenges overnight without needing ongoing civic participation.",
                        "correction": "A progressive constitution provides the legal architecture, rights, and institutions for good governance. However, realizing its ideals requires continuous citizen vigilance, public participation, ethical leadership (Chapter Six), and active defense of constitutional principles."
                    }
                }
            ]
        ]
    }
]
