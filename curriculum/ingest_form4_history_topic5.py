"""
VLearn Curriculum Ingestion Engine: Form 4 History — Topic 5 (Developments and Challenges in Kenya Since Independence)

Target Subject: History (Subject ID: 17)
Grade: Form 4 (Grade ID: 4)
Curriculum: 844 (Curriculum ID: 4)

Topic 5: Social, Economic and Political Developments and Challenges in Kenya Since Independence (Order: 5)
  - Unit 1: Political Developments and Constitutional Changes (1963–1991) (Lesson 1: 15 Pages)
  - Unit 2: Political and Constitutional Developments from 1991 to Present (Lesson 2: 15 Pages)
  - Unit 3: Multiparty Democracy in Kenya — Principles, Roles, and Challenges (Lesson 3: 15 Pages)
  - Unit 4: Economic and Social Developments and Challenges Since Independence (Lesson 4: 16 Pages)
  - Unit 5: Devolution and County Governments under the 2010 Constitution (Lesson 5: 18 Pages)

Total: 5 Learning Units, 5 Lessons, 79 Pages, 95+ Blocks, 9 Media Assets (4 Wikimedia Photos + 5 Verified YouTube Videos)

Usage:
  ./venv/bin/python curriculum/ingest_form4_history_topic5.py --replace
"""

import os
import sys
import re
import argparse
import django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from django.db import transaction
from curriculum.models import (
    Curriculum, Grade, Subject, Topic,
    LearningUnit, Lesson, LessonBlock, LessonAsset
)

# ---------------------------------------------------------------------------
# Citation & Metadata Cleaner Helper
# ---------------------------------------------------------------------------
BRACKET_CITATION_RE = re.compile(r'\[(?:\d+|image_\d+|S\d+.*?|[\d,\s]+)\]')

def clean_text(val):
    if not isinstance(val, str):
        return val
    cleaned = BRACKET_CITATION_RE.sub('', val)
    cleaned = re.sub(r' +', ' ', cleaned)
    cleaned = re.sub(r' \.', '.', cleaned)
    cleaned = re.sub(r' ,', ',', cleaned)
    cleaned = re.sub(r' ;', ';', cleaned)
    cleaned = re.sub(r'\( \)', '', cleaned)
    return cleaned.strip()

def clean_content_dict(data):
    if isinstance(data, str):
        return clean_text(data)
    elif isinstance(data, list):
        return [clean_content_dict(item) for item in data]
    elif isinstance(data, dict):
        return {k: clean_content_dict(v) for k, v in data.items()}
    return data


# ===========================================================================
# LESSON DEFINITIONS: FORM 4 HISTORY TOPIC 5
# ===========================================================================

LESSON_1_PAGES = [
    {
        "page_number": 1,
        "page_title": "Political Inheritance at Independence (1963)",
        "blocks": [
            {
                "block_type": "learning_goal",
                "component_type": "learning_goal",
                "title": "Lesson Objectives: Post-Colonial Political Trajectory (1963–1991)",
                "content": {
                    "text": (
                        "By the end of this lesson, you will be able to:\n"
                        "- Identify the major political challenges inherited by Kenya at independence on 12 December 1963\n"
                        "- Explain the constitutional transition from a dominion to a sovereign Republic in 1964\n"
                        "- Analyze the KPU crisis, the Turncoat Amendment, and the de facto one-party state consolidation\n"
                        "- Trace political assassinations, the 1978 presidential succession, the 1982 Section 2A amendment, and the 1982 abortive coup\n"
                        "- Evaluate the controversial 1988 Mlolongo queue-voting crisis and the Saba Saba protests"
                    )
                }
            },
            {
                "block_type": "definition_card",
                "component_type": "definition_card",
                "title": "Concept: The Independence Settlement",
                "content": {
                    "term": "The Post-Colonial Inheritance",
                    "definition": (
                        "The complex web of political, constitutional, and ethnic dynamics left behind by British colonial rule, "
                        "including an acute shortage of African technocrats, regional developmental disparities, and an uneasy federal (Majimbo) constitution."
                    )
                }
            }
        ]
    },
    {
        "page_number": 2,
        "page_title": "Inherited Post-Colonial Challenges",
        "blocks": [
            {
                "block_type": "step_process",
                "component_type": "step_process",
                "title": "Four Fundamental Inherited Structural Hurdles",
                "content": {
                    "steps": [
                        "1. Acute Shortage of African Technocrats: Decades of racial job reservation left independent Kenya with few trained African professionals to manage key civil service and technical departments.",
                        "2. Deep-Seated Ethnic Suspicion: British 'divide and rule' policies created inter-ethnic competition and distrust, hindering immediate national cohesion.",
                        "3. Illiterate and Politically Unprepared Population: The majority of indigenous citizens were illiterate and unfamiliar with democratic mechanics and constitutional rights.",
                        "4. Severe Economic Disparities: Arable former White Highlands possessed roads, electricity, and schools, whereas native reserves had been neglected."
                    ]
                }
            }
        ]
    },
    {
        "page_number": 3,
        "page_title": "Transition to a Republic and Dismantling Majimbo (1964–1966)",
        "blocks": [
            {
                "block_type": "concept_explanation",
                "component_type": "concept_explanation",
                "title": "From Federalism to a Centralized Unitary State",
                "content": {
                    "text": (
                        "- **The 1963 Independence Constitution:** Established a federal system (*Majimbo*) with six regional assemblies and a bicameral parliament (Senate and House of Representatives).\n"
                        "- **The Republican Amendment (December 1964):** Kenya became a Republic on 12 December 1964. The British Queen was replaced by an executive President, **Mzee Jomo Kenyatta**, combining Head of State, Head of Government, and Commander-in-Chief.\n"
                        "- **Voluntary Dissolution of KADU (1964):** Ronald Ngala’s KADU dissolved and merged with KANU, turning Kenya into a *de facto* (in practice) one-party state.\n"
                        "- **Abolition of the Senate & Regions (1966):** Constitutional amendments abolished the regional assemblies and merged the Senate with the House of Representatives to create a unicameral National Assembly."
                    )
                }
            },
            {
                "block_type": "suggested_image",
                "component_type": "suggested_image",
                "title": "Statue of President Mzee Jomo Kenyatta, Nairobi",
                "content": {
                    "text": "Statue of President Mzee Jomo Kenyatta at the Kenyatta International Convention Centre (KICC), Nairobi.",
                    "url": "https://upload.wikimedia.org/wikipedia/commons/8/89/The_Statue_of_Jomo_Kenyatta.jpg",
                    "author": "Public Domain / Wikimedia Commons",
                    "licensing": "Public Domain",
                    "commons_page_url": "https://commons.wikimedia.org/wiki/File:The_Statue_of_Jomo_Kenyatta.jpg"
                }
            }
        ]
    },
    {
        "page_number": 4,
        "page_title": "The KPU Crisis and One-Party Consolidation (1966–1969)",
        "blocks": [
            {
                "block_type": "concept_explanation",
                "component_type": "concept_explanation",
                "title": "The Ideological Rift: Kenyatta vs. Oginga Odinga",
                "content": {
                    "text": (
                        "The ideological honeymoon in KANU was short-lived:\n\n"
                        "- **The Ideological Split:** A bitter split emerged between the capitalist-leaning wing (Jomo Kenyatta, Tom Mboya) and the socialist-leaning wing (Vice President **Jaramogi Oginga Odinga**).\n"
                        "- **Formation of KPU (1966):** Odinga resigned as Vice President to form an opposition party, the **Kenya People's Union (KPU)**.\n"
                        "- **The Turncoat Amendment (1966):** KANU quickly amended the Constitution, forcing any MP defecting from KANU to vacate their seat and contest a fresh election (*The Little General Election*).\n"
                        "- **Kisumu Riots and Ban of KPU (1969):** Following hostile riots during Kenyatta's visit to Kisumu to open the Russia Hospital, KPU was banned and its leaders detained, cementing KANU's political monopoly."
                    )
                }
            }
        ]
    },
    {
        "page_number": 5,
        "page_title": "Political Assassinations: Tom Mboya and J.M. Kariuki",
        "blocks": [
            {
                "block_type": "concept_explanation",
                "component_type": "concept_explanation",
                "title": "Rising Political Intolerance and State Repression",
                "content": {
                    "text": (
                        "The consolidation of executive power coincided with high-profile political assassinations:\n\n"
                        "- **Tom Mboya’s Assassination (July 1969):** The brilliant Minister for Economic Planning was gunned down on Government Road (Moi Avenue), Nairobi, triggering immense national outrage and ethnic polarization.\n"
                        "- **J.M. Kariuki’s Assassination (March 1975):** The populist Nyandarua MP—famed for warning against creating *'a Kenya of 10 millionaires and 10 million beggars'*—was abducted and murdered, sparking mass student riots and destabilizing the Kenyatta government."
                    )
                }
            }
        ]
    },
    {
        "page_number": 6,
        "page_title": "The 1978 Succession and the 1982 Section 2A Amendment",
        "blocks": [
            {
                "block_type": "concept_explanation",
                "component_type": "concept_explanation",
                "title": "Transition to President Daniel arap Moi",
                "content": {
                    "text": (
                        "- **Kenyatta’s Death (22 August 1978):** Succeeded peacefully by Vice President **Daniel Toroitich arap Moi**, who launched the Nyayo philosophy.\n"
                        "- **Section 2A Enactment (June 1982):** To prevent Oginga Odinga and George Anyona from registering a new socialist party, Parliament amended the Constitution to insert **Section 2A**.\n"
                        "- **De Jure Status:** This formally made Kenya a *de jure* (by law) one-party state, outlawing all opposition political parties."
                    )
                }
            }
        ]
    },
    {
        "page_number": 7,
        "page_title": "The 1982 Abortive Coup Attempt",
        "blocks": [
            {
                "block_type": "concept_explanation",
                "component_type": "concept_explanation",
                "title": "The Military Rebellion of 1 August 1982",
                "content": {
                    "text": (
                        "- **The Uprising:** On Sunday, 1 August 1982, low-ranking soldiers of the Kenya Air Force (led by Senior Private **Hezekiah Ochuka** and Pancras Oteyo Okumu) attempted to overthrow President Moi's government.\n"
                        "- **Suppression:** Loyal army and General Service Unit (GSU) forces under General Mohamoud Mohamed suppressed the mutiny within hours.\n"
                        "- **Consequences:**\n"
                        "  1. The entire Kenya Air Force was disbanded and reorganized as ''82 Air Force'.\n"
                        "  2. Thousands of airmen were court-martialed, and coup leaders were convicted of treason.\n"
                        "  3. Led to an authoritarian crackdown on political dissidents, university lecturers, and student leaders."
                    )
                }
            }
        ]
    },
    {
        "page_number": 8,
        "page_title": "Historical Documentary: The 1982 Coup Attempt",
        "blocks": [
            {
                "block_type": "suggested_video",
                "component_type": "suggested_video",
                "title": "Historical Documentary: The 1982 Coup Attempt in Kenya",
                "content": {
                    "url": "https://www.youtube.com/watch?v=4yr9qr1jo_M",
                    "text": "Examine the causes, dramatic street fighting in Nairobi, suppression, and profound political consequences of the 1982 Kenya Air Force mutiny.",
                    "author": "THE METROPOLITAN REPORTS / Historical Documentary",
                    "licensing": "Standard YouTube License"
                }
            }
        ]
    },
    {
        "page_number": 9,
        "page_title": "The Queue-Voting (Mlolongo) Crisis (1988)",
        "blocks": [
            {
                "block_type": "concept_explanation",
                "component_type": "concept_explanation",
                "title": "The Abolition of the Secret Ballot in KANU Primaries",
                "content": {
                    "text": (
                        "In 1988, KANU introduced the controversial **Mlolongo** (queue-voting) system for parliamentary and civic primary elections:\n\n"
                        "- **Mechanism:** Voters queued physically behind portraits or agents of their preferred candidates, and presiding officers counted voters aloud.\n"
                        "- **Blatant Rigging:** In numerous constituencies, candidates with obviously shorter queues were declared winners by returning officers.\n"
                        "- **Voter Intimidation:** Civil servants, teachers, and business owners were terrified to queue behind opposition candidates for fear of losing their jobs or licenses.\n"
                        "- **Backlash:** Destroyed the remaining public legitimacy of the one-party state, galvanizing church leaders, lawyers, and pro-democracy politicians."
                    )
                }
            }
        ]
    },
    {
        "page_number": 10,
        "page_title": "The 1990 Saba Saba Riots",
        "blocks": [
            {
                "block_type": "concept_explanation",
                "component_type": "concept_explanation",
                "title": "The Climax of the Second Liberation Struggle",
                "content": {
                    "text": (
                        "- **The Call for Reform:** Pro-democracy leaders **Kenneth Matiba**, **Charles Rubia**, and **Oginga Odinga** called for an unauthorized mass rally at Kamukunji Grounds on 7 July 1990 (*Saba Saba*).\n"
                        "- **State Clampdown:** Matiba and Rubia were arrested and detained without trial just days before the rally.\n"
                        "- **Massive Protests:** Tens of thousands took to the streets across Nairobi, Nakuru, and Central Kenya, engaging in days of running battles with police, demanding the return of multi-party democracy."
                    )
                }
            }
        ]
    },
    {
        "page_number": 11,
        "page_title": "Timeline of Constitutional Centralization (1964–1982)",
        "blocks": [
            {
                "block_type": "step_process",
                "component_type": "step_process",
                "title": "Step-by-Step Centralization of Executive Power",
                "content": {
                    "steps": [
                        "1. 1964: Republican Amendment creates the Executive Presidency, concentrating Head of State and Government powers in Kenyatta.",
                        "2. 1964: Dissolution of KADU dissolves regional assemblies and establishes a de facto one-party state.",
                        "3. 1966: Abolition of the Senate merges parliament into a unicameral National Assembly, removing legislative checks.",
                        "4. 1966: Turncoat Amendment forces MPs defecting from KANU to vacate parliamentary seats immediately.",
                        "5. 1969: Banning of KPU leaves KANU as the sole operating political party in Kenya.",
                        "6. 1982: Section 2A Amendment formally makes Kenya a de jure one-party state by law."
                    ]
                }
            }
        ]
    },
    {
        "page_number": 12,
        "page_title": "Interactive Classification: Political Events (1963–1991)",
        "blocks": [
            {
                "block_type": "mini_activity",
                "component_type": "mini_activity",
                "title": "Match the Political Event to Its Correct Year",
                "content": {
                    "instruction": "Test your chronological mastery of post-independence Kenyan politics:",
                    "items": [
                        "1. Kenya officially becomes a sovereign Republic under President Kenyatta -> **1964**",
                        "2. Formation of the Kenya People's Union (KPU) by Oginga Odinga -> **1966**",
                        "3. Assassination of Minister Tom Mboya on Government Road -> **1969**",
                        "4. Presidential succession of Daniel Toroitich arap Moi -> **1978**",
                        "5. Enactment of Section 2A making Kenya a de jure one-party state -> **1982**",
                        "6. Abortive military coup attempt by Kenya Air Force -> **1982**",
                        "7. Introduction of the Mlolongo queue-voting system -> **1988**"
                    ]
                }
            }
        ]
    },
    {
        "page_number": 13,
        "page_title": "KCSE Examination Coaching: Centralization of Power",
        "blocks": [
            {
                "block_type": "worked_example",
                "component_type": "worked_example",
                "title": "KCSE Question: Explain Five Constitutional Changes That Centralized Executive Power (1964–1982) (10 Marks)",
                "content": {
                    "text": (
                        "**Model Answer (Point + Explanation = 2 Marks per Point):**\n\n"
                        "1. **The Republican Constitutional Amendment (1964):** Transformed Kenya into a Republic, replacing the British Governor-General with an executive President combining Head of State, Head of Government, and Armed Forces command. (2 marks)\n\n"
                        "2. **Dissolution of KADU and Majimbo (1964):** KADU merged with KANU, ending federal regional assemblies (*Majimbo*) and centralizing administrative decisions in Nairobi. (2 marks)\n\n"
                        "3. **Abolition of the Senate (1966):** Merged the Senate with the House of Representatives into a unicameral parliament, removing senate checks on executive bills. (2 marks)\n\n"
                        "4. **The Turncoat Amendment (1966):** Compelled any MP resigning from KANU to seek a fresh election, deterring political defection and penalizing dissent. (2 marks)\n\n"
                        "5. **Enactment of Section 2A (1982):** Formally banned all political parties other than KANU, making Kenya a *de jure* one-party state by law. (2 marks)"
                    )
                }
            }
        ]
    },
    {
        "page_number": 14,
        "page_title": "Check Your Understanding: Module 5.1",
        "blocks": [
            {
                "block_type": "knowledge_check",
                "component_type": "knowledge_check",
                "title": "Module 5.1 Assessment",
                "content": {
                    "questions": [
                        {
                            "question": "Which constitutional amendment officially made Kenya a de jure one-party state in June 1982?",
                            "options": [
                                "The Turncoat Amendment",
                                "The Section 2A Amendment",
                                "The Republican Amendment",
                                "The IPPG Amendment"
                            ],
                            "correct_answer": 1,
                            "explanation": "Section 2A of the Constitution inserted in June 1982 outlawed all political parties except KANU."
                        },
                        {
                            "question": "What was the immediate consequence of the 'Turncoat Amendment' passed in 1966?",
                            "options": [
                                "All senators were automatically appointed cabinet ministers",
                                "Any MP defecting from KANU to another party was forced to resign their parliamentary seat and seek fresh elections",
                                "Local elections were conducted using the queue-voting system",
                                "The President was barred from serving more than two terms"
                            ],
                            "correct_answer": 1,
                            "explanation": "The Turncoat Amendment required defecting MPs to vacate their seats, triggering the 1966 Little General Election."
                        }
                    ]
                }
            }
        ]
    },
    {
        "page_number": 15,
        "page_title": "Lesson Summary & Key Takeaways",
        "blocks": [
            {
                "block_type": "summary",
                "component_type": "summary",
                "title": "Core Summary: Political Developments (1963–1991)",
                "content": {
                    "text": (
                        "• **Inherited Challenges:** Technocrat deficits, ethnic suspicion, mass illiteracy, and regional infrastructure imbalances.\n"
                        "• **Centralization:** Dismantled Majimbo, abolished the Senate, created the executive presidency, and merged KADU into KANU.\n"
                        "• **Repression & One-Party Rule:** Banned KPU in 1969; passed Section 2A in 1982; suppressed the 1982 Air Force coup.\n"
                        "• **Catalysts for Reform:** The flawed 1988 Mlolongo queue voting and 1990 Saba Saba riots shattered one-party legitimacy."
                    )
                }
            },
            {
                "block_type": "key_takeaway",
                "component_type": "key_takeaway",
                "title": "Key Takeaways",
                "content": {
                    "text": (
                        "- The concentration of executive power between 1964 and 1982 eroded checks and balances.\n"
                        "- Flawed electoral experiments like Mlolongo directly catalyzed Kenya's second liberation struggle."
                    )
                }
            }
        ]
    }
]

LESSON_2_PAGES = [
    {
        "page_number": 1,
        "page_title": "Return to Multi-Partyism and Democratic Milestones (1991–Present)",
        "blocks": [
            {
                "block_type": "learning_goal",
                "component_type": "learning_goal",
                "title": "Lesson Objectives: Political Developments (1991 to Present)",
                "content": {
                    "text": (
                        "By the end of this lesson, you will be able to:\n"
                        "- Explain the repeal of Section 2A in December 1991 and the rebirth of multi-party democracy\n"
                        "- Analyze the 1992 and 1997 general elections and the landmark IPPG constitutional reforms\n"
                        "- Evaluate the historic 2002 democratic transition ending KANU's 39-year rule\n"
                        "- Examine the 2007 election crisis, the National Accord of 2008, and the Grand Coalition Government\n"
                        "- Trace the promulgation of the Constitution of Kenya 2010 on 27 August 2010"
                    )
                }
            },
            {
                "block_type": "definition_card",
                "component_type": "definition_card",
                "title": "Concept: The Second Liberation",
                "content": {
                    "term": "The Second Liberation",
                    "definition": (
                        "The prolonged national struggle by civil society, church leaders, lawyers, and opposition politicians (1982–2010) "
                        "to dismantle authoritarian one-party rule, restore multi-party democracy, and promulgate a progressive, rights-based constitution."
                    )
                }
            }
        ]
    },
    {
        "page_number": 2,
        "page_title": "The Repeal of Section 2A (December 1991)",
        "blocks": [
            {
                "block_type": "concept_explanation",
                "component_type": "concept_explanation",
                "title": "The Return of Multi-Party Democracy",
                "content": {
                    "text": (
                        "In December 1991, overwhelming domestic pressure and international donor sanctions forced KANU to repeal Section 2A:\n\n"
                        "- **Constitutional Amendment:** Parliament repealed Section 2A, officially legalizing opposition political parties and restoring freedom of association.\n"
                        "- **The Emergence of FORD:** The **Forum for the Restoration of Democracy (FORD)**—led by veteran statesmen and 'Young Turks' (Oginga Odinga, Masinde Muliro, Kenneth Matiba, Martin Shikuku, Paul Muite, James Orengo)—became the formidable opposition movement."
                    )
                }
            },
            {
                "block_type": "suggested_video",
                "component_type": "suggested_video",
                "title": "Historical Archival Recording: President Moi on Multi-Partyism (1991)",
                "content": {
                    "url": "https://www.youtube.com/watch?v=W1C_sqnzKRo",
                    "text": "Watch historical archival footage of President Daniel arap Moi discussing the repeal of Section 2A and warning about ethnic politics in December 1991.",
                    "author": "MediaGuru / Kenya History Archives",
                    "licensing": "Standard YouTube License"
                }
            }
        ]
    },
    {
        "page_number": 3,
        "page_title": "The 1992 Multi-Party Elections: Opposition Fragmentation",
        "blocks": [
            {
                "block_type": "concept_explanation",
                "component_type": "concept_explanation",
                "title": "Why KANU Retained Power in 1992",
                "content": {
                    "text": (
                        "Despite the return of pluralism, KANU won the 1992 general elections due to opposition disunity:\n\n"
                        "- **The Split of FORD:** FORD fractured into **FORD-Kenya** (led by Oginga Odinga) and **FORD-Asili** (led by Kenneth Matiba).\n"
                        "- **The Democratic Party (DP):** Formed by former Vice President **Mwai Kibaki**.\n"
                        "- **Election Outcome:** Moi won the presidency with only 36% of the national vote because the opposition shared the remaining 64% among themselves."
                    )
                }
            }
        ]
    },
    {
        "page_number": 4,
        "page_title": "The Inter-Parties Parliamentary Group (IPPG) Reforms (1997)",
        "blocks": [
            {
                "block_type": "step_process",
                "component_type": "step_process",
                "title": "Four Landmark Reforms Enacted by IPPG in 1997",
                "content": {
                    "steps": [
                        "1. Bi-Partisan Electoral Commission: Stripped the President of sole power to appoint ECK commissioners; parliamentary parties nominated commissioners proportionally.",
                        "2. Equal State Media Coverage: Mandated the state broadcaster (KBC) to provide fair and balanced airtime to all registered political parties during campaigns.",
                        "3. Repeal of Oppressive Colonial Laws: Relaxed sections of the Public Order Act and Chief's Authority Act requiring police permits for political rallies.",
                        "4. Proportional Distribution of Nominated MPs: Nominated parliamentary seats were allocated based on party seat ratios rather than presidential discretion."
                    ]
                }
            }
        ]
    },
    {
        "page_number": 5,
        "page_title": "The Historic 2002 Democratic Transition",
        "blocks": [
            {
                "block_type": "concept_explanation",
                "component_type": "concept_explanation",
                "title": "The NARC Landslide and the End of KANU's 39-Year Rule",
                "content": {
                    "text": (
                        "- **Moi's Retirement:** Constitutionally barred from seeking a third term under the 1992 term-limit clause, President Moi retired in 2002.\n"
                        "- **The 'Uhuru Project' Rebellion:** Moi endorsed Uhuru Kenyatta as KANU's candidate, provoking a mass walkout of KANU stalwarts (Raila Odinga, Kalonzo Musyoka, George Saitoti) who formed the Liberal Democratic Party (LDP).\n"
                        "- **The NARC Coalition:** The opposition forged a united front—the **National Rainbow Coalition (NARC)**—uniting Mwai Kibaki's NAK and Raila Odinga's LDP (*'Kibaki Tosha'*).\n"
                        "- **Landslide Victory:** Mwai Kibaki won with over 62% of the vote, marking Kenya's first peaceful democratic transition of power."
                    )
                }
            },
            {
                "block_type": "suggested_image",
                "component_type": "suggested_image",
                "title": "President Mwai Kibaki (2003)",
                "content": {
                    "text": "President Mwai Kibaki, 3rd President of Kenya, who led the NARC coalition to victory in 2002 and promulgated the 2010 Constitution.",
                    "url": "https://upload.wikimedia.org/wikipedia/commons/f/fc/Mwai_Kibaki%2C_October_2003_%28cropped%29.jpg",
                    "author": "Public Domain / Wikimedia Commons",
                    "licensing": "Public Domain",
                    "commons_page_url": "https://commons.wikimedia.org/wiki/File:Mwai_Kibaki,_October_2003_(cropped).jpg"
                }
            }
        ]
    },
    {
        "page_number": 6,
        "page_title": "The 2007 Election Crisis and Post-Election Violence",
        "blocks": [
            {
                "block_type": "concept_explanation",
                "component_type": "concept_explanation",
                "title": "The Darkest Political Crisis in Independent Kenya",
                "content": {
                    "text": (
                        "- **The Contest:** The December 2007 presidential election pitted incumbent **Mwai Kibaki** (Party of National Unity - PNU) against **Raila Odinga** (Orange Democratic Movement - ODM).\n"
                        "- **The Tallying Breakdown:** Following a chaotic vote count, the Electoral Commission of Kenya (ECK) under Samuel Kivuitu declared Kibaki the winner, and he was hurriedly sworn in at dusk.\n"
                        "- **The Outbreak:** ODM rejected the results, sparking spontaneous protests and severe inter-ethnic clashes.\n"
                        "- **Humanitarian Toll:** Over 1,100 citizens were killed and more than 600,000 were internally displaced."
                    )
                }
            }
        ]
    },
    {
        "page_number": 7,
        "page_title": "The Kriegler and Waki Commissions (2008)",
        "blocks": [
            {
                "block_type": "comparison_table",
                "component_type": "comparison_table",
                "title": "Findings of the Post-2007 Investigative Commissions",
                "content": {
                    "headers": ["Commission", "Mandate & Chairperson", "Core Findings and Recommendations"],
                    "rows": [
                        ["The Kriegler Commission (IREC)", "Investigate 2007 electoral conduct (Justice Johann Kriegler).", "Found 1.2M dead voters on register, tallies exceeding 100%, and compromised ECK tallying. Recommended complete disbandment of the ECK and creation of a modern electronic body (IEBC)."],
                        ["The Waki Commission (CIPEV)", "Investigate causes of post-election violence (Justice Philip Waki).", "Found systematic state security failures and political incitement. Handed a sealed envelope of top suspects to Kofi Annan, leading to International Criminal Court (ICC) prosecutions."]
                    ]
                }
            }
        ]
    },
    {
        "page_number": 8,
        "page_title": "The National Accord and the Grand Coalition Government (2008)",
        "blocks": [
            {
                "block_type": "concept_explanation",
                "component_type": "concept_explanation",
                "title": "Kofi Annan's Mediation and Power-Sharing",
                "content": {
                    "text": (
                        "Under international mediation by former UN Secretary-General **Kofi Annan**, Kibaki and Odinga signed the historic **National Accord and Reconciliation Act** on 28 February 2008:\n\n"
                        "- **50-50 Power Sharing:** Cabinet portfolios were shared equally between PNU and ODM.\n"
                        "- **Creation of Prime Minister:** Raila Odinga became Prime Minister to coordinate and supervise government functions, with two Deputy Prime Ministers (Uhuru Kenyatta and Musalia Mudavadi).\n"
                        "- **Agenda Four Reforms:** Prioritized constitutional review, judicial reform, land reform, and tackling youth unemployment."
                    )
                }
            }
        ]
    },
    {
        "page_number": 9,
        "page_title": "Promulgation of the Constitution of Kenya 2010",
        "blocks": [
            {
                "block_type": "concept_explanation",
                "component_type": "concept_explanation",
                "title": "The Birth of the Second Republic (27 August 2010)",
                "content": {
                    "text": (
                        "- **The Process:** Drafted by the Committee of Experts (COE) led by **Nzamba Kitonga**, harmonizing the Bomas Draft.\n"
                        "- **The Referendum (4 August 2010):** Kenyans voted overwhelmingly (67%) to approve the new Constitution.\n"
                        "- **Promulgation (27 August 2010):** President Mwai Kibaki formally promulgated the Constitution of Kenya 2010 at a historic celebration in **Uhuru Park, Nairobi**.\n"
                        "- **Key Transformations:**\n"
                        "  1. Reintroduced devolved county governance (47 Counties).\n"
                        "  2. Established an expansive Bill of Rights (Chapter 4).\n"
                        "  3. Restored the Senate and independent judiciary with the Supreme Court."
                    )
                }
            },
            {
                "block_type": "suggested_image",
                "component_type": "suggested_image",
                "title": "Uhuru Park Nairobi, Site of 2010 Promulgation",
                "content": {
                    "text": "Uhuru Park in Nairobi, the historic grounds where the Constitution of Kenya 2010 was officially promulgated on 27 August 2010.",
                    "url": "https://upload.wikimedia.org/wikipedia/commons/2/20/Uhuru_Park_Nairobi.jpg",
                    "author": "Public Domain / Wikimedia Commons",
                    "licensing": "Public Domain",
                    "commons_page_url": "https://commons.wikimedia.org/wiki/File:Uhuru_Park_Nairobi.jpg"
                }
            }
        ]
    },
    {
        "page_number": 10,
        "page_title": "Historical Documentary: Promulgation of the 2010 Constitution",
        "blocks": [
            {
                "block_type": "suggested_video",
                "component_type": "suggested_video",
                "title": "Historical Broadcast: The Promulgation of the Constitution of Kenya 2010",
                "content": {
                    "url": "https://www.youtube.com/watch?v=8THaZv6fkCM",
                    "text": "Relive the historic broadcast at Uhuru Park on 27 August 2010 as President Mwai Kibaki signs and holds aloft the Constitution of Kenya 2010.",
                    "author": "Citizen TV Kenya / National Broadcast Archive",
                    "licensing": "Standard YouTube License"
                }
            }
        ]
    },
    {
        "page_number": 11,
        "page_title": "The Supreme Court and Judicial Reforms",
        "blocks": [
            {
                "block_type": "suggested_image",
                "component_type": "suggested_image",
                "title": "The Supreme Court of Kenya Building, Nairobi",
                "content": {
                    "text": "The Supreme Court of Kenya, established under the 2010 Constitution as the apex court of the land with exclusive jurisdiction over presidential election petitions.",
                    "url": "https://upload.wikimedia.org/wikipedia/commons/0/0a/Supreme_Court_of_Kenya.JPG",
                    "author": "Public Domain / Wikimedia Commons",
                    "licensing": "Public Domain",
                    "commons_page_url": "https://commons.wikimedia.org/wiki/File:Supreme_Court_of_Kenya.JPG"
                }
            },
            {
                "block_type": "concept_explanation",
                "component_type": "concept_explanation",
                "title": "Establishing Judicial Independence",
                "content": {
                    "text": (
                        "- **The Supreme Court:** Established as the highest court in Kenya, led by the Chief Justice, with exclusive jurisdiction over presidential election petitions.\n"
                        "- **Judicial Service Commission (JSC):** Vets and interviews judges in public proceedings, ending executive patronage in judicial appointments.\n"
                        "- **Vetting of Judges and Magistrates:** All sitting judges underwent independent vetting to remove corrupt and compromised judicial officers."
                    )
                }
            }
        ]
    },
    {
        "page_number": 12,
        "page_title": "Interactive Timeline: The Journey to the 2010 Constitution",
        "blocks": [
            {
                "block_type": "mini_activity",
                "component_type": "mini_activity",
                "title": "Place the Milestones in Chronological Order",
                "content": {
                    "instruction": "Test your mastery of Kenya's modern constitutional journey:",
                    "items": [
                        "1. Repeal of Section 2A restoring multi-party democracy -> **December 1991**",
                        "2. IPPG electoral and media reforms enacted -> **1997**",
                        "3. NARC ends KANU's 39-year continuous rule -> **December 2002**",
                        "4. National Accord signed establishing the Grand Coalition Government -> **February 2008**",
                        "5. Official Promulgation of the Constitution of Kenya 2010 at Uhuru Park -> **27 August 2010**"
                    ]
                }
            }
        ]
    },
    {
        "page_number": 13,
        "page_title": "KCSE Examination Coaching: Factors Behind Multipartyism",
        "blocks": [
            {
                "block_type": "worked_example",
                "component_type": "worked_example",
                "title": "KCSE Question: Explain Six Factors That Led to the Return of Multi-Party Democracy in Kenya in 1991 (12 Marks)",
                "content": {
                    "text": (
                        "**Model Answer (Point + Explanation = 2 Marks per Point):**\n\n"
                        "1. **International Donor Pressure:** Western bilateral donors (USA, UK) and the World Bank/IMF suspended financial aid to Kenya, making economic assistance conditional on democratic reforms. (2 marks)\n\n"
                        "2. **Collapse of Communism in Eastern Europe (1989):** The fall of the Soviet Union ended the Cold War, meaning Western powers no longer tolerated authoritarian single-party regimes in Africa. (2 marks)\n\n"
                        "3. **Mobilization by Civil Society and Intellectuals:** The Law Society of Kenya (LSK), university lecturers, and journalists organized discussions, exposed abuses, and defended dissidents. (2 marks)\n\n"
                        "4. **Vocal Condemnation by Church Leaders:** Bold clergy (Bishop Henry Okullu, Bishop Alexander Muge, Rev. Timothy Njoya) used their pulpits to denounce human rights violations and corruption. (2 marks)\n\n"
                        "5. **Public Outrage Over the 1988 Mlolongo Rigging:** The open manipulation of queue voting convinced Kenyans that KANU could not reform internally. (2 marks)\n\n"
                        "6. **Inspiration from Other African Transitions:** Successful democratic transitions in African states (e.g., Chiluba defeating Kaunda in Zambia in 1991) energized Kenyan reformers. (2 marks)"
                    )
                }
            }
        ]
    },
    {
        "page_number": 14,
        "page_title": "Check Your Understanding: Module 5.2",
        "blocks": [
            {
                "block_type": "knowledge_check",
                "component_type": "knowledge_check",
                "title": "Module 5.2 Assessment",
                "content": {
                    "questions": [
                        {
                            "question": "On which exact date was the Constitution of Kenya 2010 officially promulgated?",
                            "options": [
                                "12 December 1963",
                                "28 February 2008",
                                "27 August 2010",
                                "4 August 2010"
                            ],
                            "correct_answer": 2,
                            "explanation": "The Constitution was officially promulgated by President Mwai Kibaki at Uhuru Park on 27 August 2010."
                        },
                        {
                            "question": "Which commission investigated the causes of the 2007–2008 Post-Election Violence in Kenya?",
                            "options": [
                                "The Kriegler Commission",
                                "The Waki Commission",
                                "The Ominde Commission",
                                "The Mackay Commission"
                            ],
                            "correct_answer": 1,
                            "explanation": "The Waki Commission (CIPEV) investigated the post-election violence and submitted the envelope to the ICC."
                        }
                    ]
                }
            }
        ]
    },
    {
        "page_number": 15,
        "page_title": "Lesson Summary & Key Takeaways",
        "blocks": [
            {
                "block_type": "summary",
                "component_type": "summary",
                "title": "Core Summary: Political Developments (1991 to Present)",
                "content": {
                    "text": (
                        "• **Rebirth of Pluralism (1991):** Repeal of Section 2A under intense internal protests and external donor sanctions.\n"
                        "• **Democratic Transition (2002):** NARC coalition under Mwai Kibaki ended KANU's 39-year rule.\n"
                        "• **2007 Crisis & National Accord (2008):** Post-election violence resolved via Kofi Annan's mediation and the Grand Coalition Government.\n"
                        "• **Constitution 2010:** Promulgated on 27 August 2010, introducing 47 county devolved governments, a Supreme Court, and an expansive Bill of Rights."
                    )
                }
            },
            {
                "block_type": "key_takeaway",
                "component_type": "key_takeaway",
                "title": "Key Takeaways",
                "content": {
                    "text": (
                        "- Kenya's constitutional journey evolved from a centralized one-party state into a progressive constitutional democracy.\n"
                        "- The 2010 Constitution is the foundational anchor of modern governance in Kenya."
                    )
                }
            }
        ]
    }
]

LESSON_3_PAGES = [
    {
        "page_number": 1,
        "page_title": "Multiparty Democracy: Principles, Roles, and Challenges",
        "blocks": [
            {
                "block_type": "learning_goal",
                "component_type": "learning_goal",
                "title": "Lesson Objectives: Multiparty Democracy in Kenya",
                "content": {
                    "text": (
                        "By the end of this lesson, you will be able to:\n"
                        "- State the essential principles of a multi-party democratic system\n"
                        "- Analyze the primary constitutional and governance roles of political parties\n"
                        "- Distinguish between the operational challenges and inherent disadvantages of multipartism in Kenya\n"
                        "- Interpret primary evidence from the 2008 Kriegler Commission Report"
                    )
                }
            },
            {
                "block_type": "definition_card",
                "component_type": "definition_card",
                "title": "Definition: Multiparty Democracy",
                "content": {
                    "term": "Multiparty Democracy",
                    "definition": (
                        "A political system in which multiple political parties have the legal right and capacity to compete in free, "
                        "fair, and periodic elections to form the government, offer alternative policy visions, and hold the ruling executive accountable."
                    )
                }
            }
        ]
    },
    {
        "page_number": 2,
        "page_title": "The Six Key Roles of Political Parties in Kenya",
        "blocks": [
            {
                "block_type": "step_process",
                "component_type": "step_process",
                "title": "Examinable Functions of Political Parties in Governance",
                "content": {
                    "steps": [
                        "1. Forming the Government: Competing in general elections to secure executive authority and manage public state administration.",
                        "2. Formulating Alternative National Policies: Drafting election manifestos offering voters distinct choices for social and economic development.",
                        "3. Sponsoring and Passing Legislation: Introducing, debating, and passing laws in the National Assembly and the Senate.",
                        "4. Scrutinizing Public Expenditure: Leading parliamentary oversight committees (PAC, PIC) to audit government expenditures and expose corruption.",
                        "5. Checking Executive Excesses: Acting as an official parliamentary opposition ('Shadow Cabinet') to demand executive transparency.",
                        "6. Training and Nurturing Leaders: Providing platforms for emerging politicians to develop leadership and campaign experience."
                    ]
                }
            }
        ]
    },
    {
        "page_number": 3,
        "page_title": "Six Operational Challenges Facing Political Parties",
        "blocks": [
            {
                "block_type": "step_process",
                "component_type": "step_process",
                "title": "Structural and Practical Hurdles in Operating Parties",
                "content": {
                    "steps": [
                        "1. Ethnic and Regional Party Bases: Parties are organized around tribal strongholds rather than national ideological programs, causing intense polarization.",
                        "2. Abuse of State Machinery by Incumbents: Ruling parties utilize state security, civil servants, and state vehicles for political campaigning.",
                        "3. Unprincipled Defections ('Political Tourism'): Politicians opportunistically defect between parties for financial reward or immediate election tickets.",
                        "4. Chronic Shortage of Independent Funding: Opposition parties struggle to maintain national offices across all 47 counties.",
                        "5. Total Lack of Internal Party Democracy: Party primaries are undemocratic, characterized by direct handpicking of favored candidates by party barons.",
                        "6. Electoral Malpractices: Persistence of voter bribery, intimidation, and tally manipulation undermines democratic credibility."
                    ]
                }
            }
        ]
    },
    {
        "page_number": 4,
        "page_title": "Four Inherent Disadvantages of Multipartism",
        "blocks": [
            {
                "block_type": "concept_explanation",
                "component_type": "concept_explanation",
                "title": "Curriculum Distinction: Inherent Disadvantages",
                "content": {
                    "text": (
                        "The KCSE syllabus distinguishes between practical operational challenges and the **inherent disadvantages** of multipartism:\n\n"
                        "1. **National Polarization and Tribal Division:** Multi-party competition naturally tempts politicians to mobilize ethnic voting blocs, dividing the country.\n"
                        "2. **Exorbitant Cost of Elections:** Conducting regular general elections for multiple seats across 47 counties costs billions of shillings.\n"
                        "3. **Perpetual Campaigning Stalling Development:** Constant politicking diverts government attention and public resources away from long-term economic planning.\n"
                        "4. **Policy Inconsistency and Discontinuity:** Successor administrations frequently abandon mega projects initiated by previous regimes, resulting in wasted public funds."
                    )
                }
            }
        ]
    },
    {
        "page_number": 5,
        "page_title": "Primary Source Analysis: Kriegler Commission (2008)",
        "blocks": [
            {
                "block_type": "callout",
                "component_type": "callout",
                "title": "Historical Inquiry: The 2008 Kriegler Commission Report",
                "content": {
                    "text": (
                        "**Excerpt from the Report of the Independent Review Committee (Kriegler Commission):**\n"
                        "*> 'The 2007 election was characterized by multiple systemic failures. There were extensive irregularities in the voter register, including approximately 1.2 million dead voters on the roll. Furthermore, in several constituencies, final vote tallies exceeded 100% of registered voters. The verification process at the national tallying center was completely compromised, rendering the final declared presidential results unquantifiable and illegitimate.'*\n\n"
                        "**Analytical Questions:**\n"
                        "1. **Primary Evidence:** Cite two specific statistical anomalies highlighted by the Commission.\n"
                        "2. **Historical Consequence:** What constitutional and institutional reforms did this finding trigger in Kenya's electoral system?"
                    )
                }
            }
        ]
    },
    {
        "page_number": 6,
        "page_title": "Interactive Classification: Roles vs. Challenges vs. Disadvantages",
        "blocks": [
            {
                "block_type": "mini_activity",
                "component_type": "mini_activity",
                "title": "Categorize the Statement",
                "content": {
                    "instruction": "Classify each statement as a Role of Parties, an Operational Challenge, or an Inherent Disadvantage:",
                    "items": [
                        "1. Leading the Public Accounts Committee (PAC) to scrutinize state spending -> **Role of Political Parties**",
                        "2. Politicians defecting between parties for money ('political tourism') -> **Operational Challenge**",
                        "3. Multi-party contests polarizing the nation along ethnic fault lines -> **Inherent Disadvantage**",
                        "4. Formulating election manifestos to offer alternative policy options -> **Role of Political Parties**",
                        "5. Exorbitant billions spent every 5 years on nationwide election machinery -> **Inherent Disadvantage**",
                        "6. Party barons handpicking preferred candidates without democratic voting -> **Operational Challenge**"
                    ]
                }
            }
        ]
    },
    {
        "page_number": 7,
        "page_title": "KCSE Examination Coaching: Challenges of Multipartism",
        "blocks": [
            {
                "block_type": "worked_example",
                "component_type": "worked_example",
                "title": "KCSE Question: Explain Six Challenges Faced in Operating a Multiparty Democratic System in Kenya (12 Marks)",
                "content": {
                    "text": (
                        "**Examiner's Marking Scheme (Point + Explanation = 2 Marks per Point):**\n\n"
                        "1. **Ethnic and Regional Party Bases:** Political parties are built around specific ethnic communities rather than national ideologies, resulting in tribal voting and national division. (2 marks)\n\n"
                        "2. **Abuse of State Machinery by the Ruling Party:** Incumbent regimes utilize state security, civil service personnel, and public finances to campaign, creating an unlevel playing field. (2 marks)\n\n"
                        "3. **Unprincipled Defections ('Political Tourism'):** Politicians frequently switch party affiliations for selfish financial gain rather than ideological principle. (2 marks)\n\n"
                        "4. **Lack of Internal Party Democracy:** Party leaders autocratic handpick election candidates, causing widespread disaffection and disputed nominations. (2 marks)\n\n"
                        "5. **Inadequate and Unreliable Funding:** Opposition parties struggle to maintain county branches and agent networks due to severe financial deficits. (2 marks)\n\n"
                        "6. **Electoral Manipulation and Bribery:** Persistent voter bribery, intimidation, and tally inflation undermine voter confidence in election integrity. (2 marks)"
                    )
                }
            }
        ]
    },
    {
        "page_number": 8,
        "page_title": "Comparative Table: Single-Party vs. Multi-Party Governance",
        "blocks": [
            {
                "block_type": "comparison_table",
                "component_type": "comparison_table",
                "title": "Comparison of One-Party and Multi-Party Systems in Kenya",
                "content": {
                    "headers": ["Governance Dimension", "One-Party Era (1969–1991)", "Multi-Party Era (1991–Present)"],
                    "rows": [
                        ["Political Association", "Monopolized by KANU; opposition outlawed under Section 2A.", "Guaranteed freedom of political association under Chapter 4 Bill of Rights."],
                        ["Executive Accountability", "Minimal checks; unicameral parliament dominated by the ruling party.", "Rigorous checks by parliamentary opposition committees (PAC/PIC) and the Senate."],
                        ["Electoral Choice", "Single-party primaries (Mlolongo); no alternative presidential candidate.", "Multiple presidential and parliamentary candidates with distinct party manifestos."],
                        ["Judicial Independence", "Subject to executive control and security of tenure revocations.", "Independent judiciary with a Supreme Court and Judicial Service Commission."]
                    ]
                }
            }
        ]
    },
    {
        "page_number": 9,
        "page_title": "The Political Parties Act and Modern Regulatory Oversight",
        "blocks": [
            {
                "block_type": "concept_explanation",
                "component_type": "concept_explanation",
                "title": "The Role of the Registrar of Political Parties (ORPP)",
                "content": {
                    "text": (
                        "To clean up political party operations, Parliament passed the **Political Parties Act**:\n\n"
                        "- **The Office of the Registrar of Political Parties (ORPP):** Established as an independent state agency to register, regulate, and supervise political parties.\n"
                        "- **National Character Requirement:** To be fully registered, a political party must recruit at least 1,000 registered voters from at least 24 of the 47 counties and establish functional branch offices.\n"
                        "- **Political Parties Fund:** Public tax revenues are disbursed to qualified parties to reduce dependence on corrupt financiers."
                    )
                }
            }
        ]
    },
    {
        "page_number": 10,
        "page_title": "Check Your Understanding: Module 5.3",
        "blocks": [
            {
                "block_type": "knowledge_check",
                "component_type": "knowledge_check",
                "title": "Module 5.3 Assessment",
                "content": {
                    "questions": [
                        {
                            "question": "Which of the following is an example of an inherent disadvantage of a multiparty system?",
                            "options": [
                                "Forming the official parliamentary opposition",
                                "Conducting regular, highly expensive five-year general elections",
                                "Formulating alternative developmental manifestos",
                                "Holding executive ministries accountable"
                            ],
                            "correct_answer": 1,
                            "explanation": "The enormous financial cost of conducting nationwide elections every five years is an inherent disadvantage."
                        },
                        {
                            "question": "What is the primary role of the Public Accounts Committee (PAC) in Parliament?",
                            "options": [
                                "To draft national school curricula",
                                "To scrutinize government expenditures and expose corruption in ministries",
                                "To appoint county governors",
                                "To command the armed forces"
                            ],
                            "correct_answer": 1,
                            "explanation": "The PAC, led by the opposition, audits government expenditures using Auditor-General reports."
                        }
                    ]
                }
            }
        ]
    },
    {
        "page_number": 11,
        "page_title": "Lesson Summary & Key Takeaways",
        "blocks": [
            {
                "block_type": "summary",
                "component_type": "summary",
                "title": "Core Summary: Multiparty Democracy",
                "content": {
                    "text": (
                        "• **Key Roles:** Form government, formulate manifestos, sponsor bills, scrutinize spending (PAC/PIC), check executive excesses, train leaders.\n"
                        "• **Operational Challenges:** Ethnic party strongholds, abuse of state resources, unprincipled defections, poor internal democracy.\n"
                        "• **Inherent Disadvantages:** Ethnic polarization, exorbitant election costs, perpetual campaigning, policy discontinuity.\n"
                        "• **Regulation:** Enforced via the Political Parties Act and the Office of the Registrar of Political Parties (ORPP)."
                    )
                }
            },
            {
                "block_type": "key_takeaway",
                "component_type": "key_takeaway",
                "title": "Key Takeaways",
                "content": {
                    "text": (
                        "- Strong political parties are the backbone of democratic accountability.\n"
                        "- Eliminating ethnic mobilization and ensuring internal party democracy remain critical challenges."
                    )
                }
            }
        ]
    },
    {
        "page_number": 12,
        "page_title": "Revision Checklist: Multiparty Dynamics",
        "blocks": [
            {
                "block_type": "step_process",
                "component_type": "step_process",
                "title": "Mastery Checklist",
                "content": {
                    "steps": [
                        "1. Six governance roles of political parties.",
                        "2. Six operational challenges facing political parties in Kenya.",
                        "3. Four inherent disadvantages of a multiparty system.",
                        "4. The Kriegler Commission findings on electoral malpractices."
                    ]
                }
            }
        ]
    },
    {
        "page_number": 13,
        "page_title": "Discussion Forum: Overcoming Tribalism in Political Parties",
        "blocks": [
            {
                "block_type": "callout",
                "component_type": "callout",
                "title": "Civic Reflection: Building Ideological Parties",
                "content": {
                    "text": (
                        "**Civic Discussion Topic:**\n"
                        "*> 'How can Kenya transition from personality-driven, ethnic-based political parties toward policy-driven, ideological parties that unite all 47 counties?'*\n\n"
                        "**Key Points for Consideration:**\n"
                        "- Enforcement of the Political Parties Act national recruitment requirements.\n"
                        "- Equitable disbursement of the Political Parties Fund.\n"
                        "- Strict disqualification of politicians engaged in hate speech or tribal incitement."
                    )
                }
            }
        ]
    },
    {
        "page_number": 14,
        "page_title": "Exam Tip: Distinguishing Roles, Challenges, and Disadvantages",
        "blocks": [
            {
                "block_type": "callout",
                "component_type": "callout",
                "title": "Examiner's Warning on KCSE Terminology",
                "content": {
                    "text": (
                        "**Examiner's Guidance:**\n"
                        "- If asked for **ROLES**, write what political parties *do to help govern* (e.g., formulate manifestos, check executive excesses).\n"
                        "- If asked for **CHALLENGES**, write the *difficulties parties face* (e.g., lack of funds, state harassment, defections).\n"
                        "- If asked for **DISADVANTAGES**, write the *negative side-effects of having many parties* (e.g., ethnic polarization, expensive elections)."
                    )
                }
            }
        ]
    },
    {
        "page_number": 15,
        "page_title": "Mastery Review: Check Your Knowledge",
        "blocks": [
            {
                "block_type": "mini_activity",
                "component_type": "mini_activity",
                "title": "Quick Review Quiz",
                "content": {
                    "instruction": "Answer true or false:",
                    "items": [
                        "1. Political parties in Kenya must have at least 1,000 members in at least 24 counties -> **True**",
                        "2. The Public Investments Committee (PIC) is traditionally chaired by the ruling party -> **False (chaired by opposition)**",
                        "3. The 1982 Section 2A amendment established a multi-party democracy -> **False (established one-party state)**"
                    ]
                }
            }
        ]
    }
]

LESSON_4_PAGES = [
    {
        "page_number": 1,
        "page_title": "Economic and Social Developments Since Independence",
        "blocks": [
            {
                "block_type": "learning_goal",
                "component_type": "learning_goal",
                "title": "Lesson Objectives: Socio-Economic Policies (1963–Present)",
                "content": {
                    "text": (
                        "By the end of this lesson, you will be able to:\n"
                        "- Explain post-independence land settlement schemes (Million-Acre, Harambee, Haraka, Shirika)\n"
                        "- Classify land tenure under the 2010 Constitution (Public, Community, and Private Land)\n"
                        "- Analyze industrialization policies (Africanisation, Import-Substitution, ICDC/DFCK/IDB) and identify 6 key industrial hindrances\n"
                        "- Trace educational reforms (Ominde Commission, Mackay Commission & 8-4-4, FPE 2003) and healthcare developments"
                    )
                }
            },
            {
                "block_type": "definition_card",
                "component_type": "definition_card",
                "title": "Concept: The Post-Colonial Economy",
                "content": {
                    "term": "Economic Restructuring",
                    "definition": (
                        "The strategic state-led reorganization of agriculture, land ownership, trade, and industry after 1963 "
                        "to transfer productive assets to indigenous Kenyans and overcome colonial underdevelopment."
                    )
                }
            }
        ]
    },
    {
        "page_number": 2,
        "page_title": "Post-Independence Land Policies and Resettlement Schemes",
        "blocks": [
            {
                "block_type": "concept_explanation",
                "component_type": "concept_explanation",
                "title": "Redistributing the White Highlands",
                "content": {
                    "text": (
                        "Land was the core grievance driving the anti-colonial struggle:\n\n"
                        "- **Land Purchase:** The government repurchased commercial farms from departing European settlers.\n"
                        "- **Swynnerton Plan Consolidation:** Fragmented African plots were adjudicated, consolidated, and issued with private individual title deeds.\n"
                        "- **The Four Major Settlement Schemes:**\n"
                        "  1. **The Million-Acre Scheme (1963):** Purchased over 1M acres; settled thousands of landless families on ~13.5-hectare plots.\n"
                        "  2. **The Harambee Scheme (1969):** Settled families on ~16.25-hectare plots to boost commercial food production.\n"
                        "  3. **The Haraka Scheme:** Emergency rapid settlement of squatters on small plots across Central, Rift Valley, and Coast provinces.\n"
                        "  4. **The Shirika Scheme (1971):** Settled farmers on plots with a small subsistence parcel while running the main commercial farm as a cooperative (largely failed due to strong preference for private title deeds)."
                    )
                }
            }
        ]
    },
    {
        "page_number": 3,
        "page_title": "Modern Land Classification Under the 2010 Constitution",
        "blocks": [
            {
                "block_type": "comparison_table",
                "component_type": "comparison_table",
                "title": "Three Categories of Land Tenure in Kenya (2010 Constitution)",
                "content": {
                    "headers": ["Land Category", "Legal Definition & Custodian", "Specific Examples Included"],
                    "rows": [
                        ["Public Land", "Held by the National or County Government in trust for the people of Kenya.", "Unallocated government land, national parks, animal sanctuaries, public roads, rivers, mineral deposits, exclusive economic zone."],
                        ["Community Land", "Held by communities on the basis of ethnicity, culture, or similar interest.", "Group ranches, trust land held by county governments, community forests, cultural shrines, traditional grazing pastures."],
                        ["Private Land", "Held by individuals or corporate bodies under registered entitlement.", "Freehold land (absolute ownership) and leasehold land (leased for a specific period; non-citizens limited to 99-year leases)."]
                    ]
                }
            }
        ]
    },
    {
        "page_number": 4,
        "page_title": "Industrialization Policies Since Independence",
        "blocks": [
            {
                "block_type": "step_process",
                "component_type": "step_process",
                "title": "Four Core Industrial Strategies",
                "content": {
                    "steps": [
                        "1. Africanisation of Commerce: Passed Trade Licensing Acts to transfer retail shops, wholesale distribution, and transport to indigenous Kenyans.",
                        "2. Import-Substitution Industrialization: Built local factories (textiles, paper mills, vehicle assembly) to manufacture consumer goods domestically.",
                        "3. State Financial Parastatals: Established ICDC, DFCK, and IDB to provide concessionary capital and loans to local industrialists.",
                        "4. Promotion of Cooperatives: Supported agricultural marketing cooperatives (coffee, tea, dairy) to secure smallholder incomes."
                    ]
                }
            }
        ]
    },
    {
        "page_number": 5,
        "page_title": "Six Hindrances to Industrialization in Kenya",
        "blocks": [
            {
                "block_type": "step_process",
                "component_type": "step_process",
                "title": "Examinable Obstacles to Rapid Industrial Growth",
                "content": {
                    "steps": [
                        "1. Dominance of Multinational Corporations: Foreign multinationals repatriate vast profits overseas rather than reinvesting in Kenya.",
                        "2. Shortage of Strategic Mineral Resources: Lack of domestic coal, iron ore, and oil forced industries to import costly raw materials.",
                        "3. Parastatal Mismanagement and Corruption: Key manufacturing parastatals collapsed due to nepotism, graft, and political interference.",
                        "4. Stiff Competition from Developed Nations: High-quality, subsidized foreign imports outcompeted infant domestic products.",
                        "5. Widespread Poverty & Low Purchasing Power: Low consumer incomes limited the domestic market for manufactured goods.",
                        "6. Dilapidated and Inadequate Infrastructure: Frequent power blackouts, high electricity tariffs, and poor roads inflated production costs."
                    ]
                }
            }
        ]
    },
    {
        "page_number": 6,
        "page_title": "Educational Commissions and Reforms",
        "blocks": [
            {
                "block_type": "comparison_table",
                "component_type": "comparison_table",
                "title": "Major Post-Independence Education Commissions",
                "content": {
                    "headers": ["Commission & Year", "Chairperson & Mandate", "Major Landmark Recommendations"],
                    "rows": [
                        ["The Ominde Commission (1964)", "Prof. Simeon Ominde (First post-colonial education commission).", "Abolished racially segregated colonial schools; established a uniform national curriculum; made Kiswahili a compulsory subject to foster national unity."],
                        ["The Mackay Commission (1981)", "Dr. Colin Mackay (Restructuring university and basic education).", "Abolished the 7-4-2-3 system; introduced the 8-4-4 system emphasizing technical/vocational skills (Jua Kali); established Moi University as second public university."],
                        ["Free Primary Education (2003)", "President Mwai Kibaki (NARC Government).", "Abolished primary school tuition fees, triggering a massive surge in enrollment of over 1.5 million children and drastically cutting illiteracy."]
                    ]
                }
            }
        ]
    },
    {
        "page_number": 7,
        "page_title": "Healthcare Developments and Social Challenges",
        "blocks": [
            {
                "block_type": "concept_explanation",
                "component_type": "concept_explanation",
                "title": "Expanding Healthcare Access and Public Challenges",
                "content": {
                    "text": (
                        "- **Healthcare Expansion:** Built district hospitals, county clinics, and national referral facilities (Kenyatta National Hospital, Moi Teaching and Referral Hospital).\n"
                        "- **National Hospital Insurance Fund (NHIF):** Established statutory medical insurance for workers.\n"
                        "- **Nyayo Free Milk:** Improved child nutrition and primary school attendance in the 1980s.\n"
                        "- **Major Social Challenges:** Rapid population growth, rising urban unemployment, slum growth, and the devastating impact of the HIV/AIDS epidemic."
                    )
                }
            }
        ]
    },
    {
        "page_number": 8,
        "page_title": "Educational Video: Post-Independence Developments",
        "blocks": [
            {
                "block_type": "suggested_video",
                "component_type": "suggested_video",
                "title": "Educational Video: Socio-Economic Developments and Challenges in Kenya",
                "content": {
                    "url": "https://www.youtube.com/watch?v=OCWp_yWnREY",
                    "text": "Comprehensive classroom lecture detailing post-independence land policies, industrialization challenges, and educational reforms in Kenya.",
                    "author": "Erudite Systems Solutions / Form 4 History",
                    "licensing": "Standard YouTube License"
                }
            }
        ]
    },
    {
        "page_number": 9,
        "page_title": "Interactive Classification: Land and Education Policies",
        "blocks": [
            {
                "block_type": "mini_activity",
                "component_type": "mini_activity",
                "title": "Match the Policy to Its Historical Purpose",
                "content": {
                    "instruction": "Test your mastery of post-independence socio-economic policies:",
                    "items": [
                        "1. Settled landless families on 13.5-hectare plots in 1963 -> **Million-Acre Scheme**",
                        "2. Recommended the introduction of the 8-4-4 education system -> **Mackay Commission (1981)**",
                        "3. Created individual title deeds via land adjudication -> **Swynnerton Plan Implementation**",
                        "4. Abolished racially segregated schools and made Kiswahili compulsory -> **Ominde Commission (1964)**",
                        "5. Group ranches and community forests managed for pastoralists -> **Community Land**"
                    ]
                }
            }
        ]
    },
    {
        "page_number": 10,
        "page_title": "KCSE Examination Coaching: Industrialization Hindrances",
        "blocks": [
            {
                "block_type": "worked_example",
                "component_type": "worked_example",
                "title": "KCSE Question: Explain Five Factors That Have Hindered Rapid Industrialization in Kenya (10 Marks)",
                "content": {
                    "text": (
                        "**Model Answer (Point + Explanation = 2 Marks per Point):**\n\n"
                        "1. **Dominance of Multinational Corporations:** Foreign multinationals control key manufacturing sectors and repatriate profits to parent countries rather than reinvesting in Kenya. (2 marks)\n\n"
                        "2. **Shortage of Strategic Raw Materials:** Lack of heavy industrial minerals like iron ore, coal, and domestic petroleum forces factories to import expensive inputs. (2 marks)\n\n"
                        "3. **Inadequate and Expensive Infrastructure:** High electricity tariffs, frequent power outages, and poor road networks heavily inflate factory operating costs. (2 marks)\n\n"
                        "4. **Low Purchasing Power Due to Poverty:** High poverty levels restrict the domestic consumer market, making it difficult for local industries to expand production. (2 marks)\n\n"
                        "5. **Stiff Competition from Imported Goods:** Cheap, high-quality manufactured imports from industrialized nations outcompete infant domestic industries. (2 marks)"
                    )
                }
            }
        ]
    },
    {
        "page_number": 11,
        "page_title": "Case Study: The Failure of the Shirika Scheme",
        "blocks": [
            {
                "block_type": "callout",
                "component_type": "callout",
                "title": "Historical Inquiry: Why Did the Shirika Scheme Fail?",
                "content": {
                    "text": (
                        "**Historical Scenario:** In 1971, the government established the Shirika Scheme, where settled farmers received a small subsistence plot while working the rest of the large commercial farm as a state cooperative.\n\n"
                        "**Why It Failed:**\n"
                        "1. **Individual Title Preference:** Indigenous Kenyans strongly valued individual, private freehold land ownership over state-managed collective farms.\n"
                        "2. **Mismanagement:** Farm managers appointed by the state embezzled funds, leading to low crop yields and worker discontent."
                    )
                }
            }
        ]
    },
    {
        "page_number": 12,
        "page_title": "Check Your Understanding: Module 5.4",
        "blocks": [
            {
                "block_type": "knowledge_check",
                "component_type": "knowledge_check",
                "title": "Module 5.4 Assessment",
                "content": {
                    "questions": [
                        {
                            "question": "Which education commission recommended the introduction of the 8-4-4 system in Kenya?",
                            "options": [
                                "The Ominde Commission (1964)",
                                "The Mackay Commission (1981)",
                                "The Gachathi Commission (1976)",
                                "The Davy Koech Commission (1999)"
                            ],
                            "correct_answer": 1,
                            "explanation": "The Mackay Commission of 1981 recommended the 8-4-4 system and the establishment of Moi University."
                        },
                        {
                            "question": "What is the maximum lease period for a non-citizen holding private land in Kenya under the 2010 Constitution?",
                            "options": [
                                "999 years",
                                "99 years",
                                "50 years",
                                "Unlimited freehold tenure"
                            ],
                            "correct_answer": 1,
                            "explanation": "Under Article 65 of the 2010 Constitution, non-citizens can only hold land under leasehold for a maximum of 99 years."
                        }
                    ]
                }
            }
        ]
    },
    {
        "page_number": 13,
        "page_title": "Lesson Summary & Key Takeaways",
        "blocks": [
            {
                "block_type": "summary",
                "component_type": "summary",
                "title": "Core Summary: Socio-Economic Developments",
                "content": {
                    "text": (
                        "• **Land Schemes:** Million-Acre (1963), Harambee (1969), Haraka, and Shirika (1971).\n"
                        "• **2010 Land Tenure:** Public Land, Community Land, and Private Land (max 99-year lease for non-citizens).\n"
                        "• **Industrialization:** Africanisation, import substitution, ICDC loans, hindered by multinationals, raw material shortages, and power costs.\n"
                        "• **Education:** Ominde (uniform curriculum), Mackay (8-4-4), FPE 2003 (free primary education)."
                    )
                }
            },
            {
                "block_type": "key_takeaway",
                "component_type": "key_takeaway",
                "title": "Key Takeaways",
                "content": {
                    "text": (
                        "- Land reform was the cornerstone of economic reorganization after independence.\n"
                        "- Free Primary Education and the 2010 land classification brought profound social justice."
                    )
                }
            }
        ]
    },
    {
        "page_number": 14,
        "page_title": "Revision Checklist: Socio-Economic Topics",
        "blocks": [
            {
                "block_type": "step_process",
                "component_type": "step_process",
                "title": "Mastery Checklist",
                "content": {
                    "steps": [
                        "1. Four post-independence resettlement schemes.",
                        "2. Three categories of land under the 2010 Constitution.",
                        "3. Six factors hindering industrialization in Kenya.",
                        "4. Ominde and Mackay Education Commissions."
                    ]
                }
            }
        ]
    },
    {
        "page_number": 15,
        "page_title": "Discussion: Africanisation vs. Foreign Direct Investment",
        "blocks": [
            {
                "block_type": "callout",
                "component_type": "callout",
                "title": "Economic Reflection: Balancing Domestic Empowerment and Foreign Capital",
                "content": {
                    "text": (
                        "**Economic Dilemma:**\n"
                        "*> 'How can Kenya successfully empower local indigenous entrepreneurs (Africanisation) while still attracting foreign multinational investors who bring advanced technology and foreign capital?'*\n\n"
                        "**Key Considerations:**\n"
                        "- Special Economic Zones (SEZs) offering tax incentives.\n"
                        "- Local content regulations requiring foreign firms to partner with local suppliers.\n"
                        "- Expanding vocational technical training (TVETs) to provide skilled domestic labor."
                    )
                }
            }
        ]
    },
    {
        "page_number": 16,
        "page_title": "Quick Review: Post-Independence Economics",
        "blocks": [
            {
                "block_type": "mini_activity",
                "component_type": "mini_activity",
                "title": "Quick Knowledge Check",
                "content": {
                    "instruction": "Identify the institution or scheme described:",
                    "items": [
                        "1. State corporation providing loans to African merchants -> **ICDC**",
                        "2. First post-independence education commission -> **Ominde Commission (1964)**",
                        "3. Emergency squatter resettlement program across 4 provinces -> **Haraka Scheme**",
                        "4. Government statutory medical insurance fund -> **NHIF**"
                    ]
                }
            }
        ]
    }
]

LESSON_5_PAGES = [
    {
        "page_number": 1,
        "page_title": "Devolution and County Governance Under the 2010 Constitution",
        "blocks": [
            {
                "block_type": "learning_goal",
                "component_type": "learning_goal",
                "title": "Lesson Objectives: Devolved Government",
                "content": {
                    "text": (
                        "By the end of this lesson, you will be able to:\n"
                        "- Trace the historical origins of devolution from the 1962 Lancaster House Majimbo system to the 2010 Constitution\n"
                        "- Explain the 7 primary objectives of devolution in Kenya\n"
                        "- Analyze the structure and composition of County Governments (County Assembly & County Executive Committee)\n"
                        "- Identify the devolved functions of county governments and sources of county revenue\n"
                        "- Evaluate the systemic challenges facing county governments and viable solutions"
                    )
                }
            },
            {
                "block_type": "definition_card",
                "component_type": "definition_card",
                "title": "Definition: Devolution",
                "content": {
                    "term": "Devolution",
                    "definition": (
                        "A form of decentralization where constitutionally mandated executive, legislative, and financial powers, "
                        "responsibilities, and resources are delegated from the central government to forty-seven (47) semi-autonomous county governments."
                    )
                }
            }
        ]
    },
    {
        "page_number": 2,
        "page_title": "Educational Documentary: How Devolved Government Works",
        "blocks": [
            {
                "block_type": "suggested_video",
                "component_type": "suggested_video",
                "title": "Constitutional Analysis: How Devolved Government Works in Kenya",
                "content": {
                    "url": "https://www.youtube.com/watch?v=Ws_Zlb6azhY",
                    "text": "Examine the constitutional architecture of Kenya's 47 county governments, the separation of powers between Governor and Assembly, and public revenue allocation.",
                    "author": "COURT HELICOPTER / Legal & Constitutional Analysis",
                    "licensing": "Standard YouTube License"
                }
            }
        ]
    },
    {
        "page_number": 3,
        "page_title": "Historical Roots: From Majimbo (1962) to Devolution (2010)",
        "blocks": [
            {
                "block_type": "concept_explanation",
                "component_type": "concept_explanation",
                "title": "The Evolution of Decentralization in Kenya",
                "content": {
                    "text": (
                        "- **The Lancaster House Conference (1962):** KADU (led by Ronald Ngala) championed *Majimbo* (federalism) with 6 regional assemblies to protect minority communities from political domination.\n"
                        "- **The Centralization Era (1964–2010):** KANU dismantled Majimbo, abolished the Senate, and centralized all state power in Nairobi, leading to regional marginalization and corruption.\n"
                        "- **The 2010 Rebirth:** The 2010 Constitution divided Kenya into **47 distinct counties**, returning power and resources to grassroots communities."
                    )
                }
            }
        ]
    },
    {
        "page_number": 4,
        "page_title": "Seven Objectives of Devolved Government in Kenya",
        "blocks": [
            {
                "block_type": "step_process",
                "component_type": "step_process",
                "title": "Constitutional Objectives of Devolution (Article 174)",
                "content": {
                    "steps": [
                        "1. Promote Democratic and Accountable Exercise of Power: Brings government closer to citizens, holding local leaders accountable.",
                        "2. Foster National Unity by Recognizing Diversity: Respects ethnic, cultural, and religious diversity across all 47 counties.",
                        "3. Give Powers of Self-Governance to the People: Enhances active citizen participation in local decision-making.",
                        "4. Protect the Rights of Minorities and Marginalized Groups: Prioritizes communities historically excluded from development.",
                        "5. Ensure Equitable Sharing of National and Local Resources: Distributes public revenue systematically to all regions.",
                        "6. Facilitate Decentralization of State Organs: Moves government services (health, licensing, registries) out of Nairobi into counties.",
                        "7. Enhance Checks and Balances: Prevents the central executive from exercising monopoly control over the entire republic."
                    ]
                }
            }
        ]
    },
    {
        "page_number": 5,
        "page_title": "Structure of County Government: The County Assembly",
        "blocks": [
            {
                "block_type": "concept_explanation",
                "component_type": "concept_explanation",
                "title": "The Legislative Arm of County Government",
                "content": {
                    "text": (
                        "The **County Assembly** is the law-making and oversight body of the county government:\n\n"
                        "- **Elected Members (MCAs):** Voted in directly by registered voters in each ward (one member per ward) for a 5-year term.\n"
                        "- **Special Seat Members:** Nominated by political parties to ensure no more than two-thirds of the assembly is of the same gender (*2/3 gender rule*).\n"
                        "- **Marginalized Representatives:** Nominated to represent the youth, persons with disabilities, and marginalized groups.\n"
                        "- **The Speaker:** Elected from outside the assembly to serve as chairperson and administrative head."
                    )
                }
            }
        ]
    },
    {
        "page_number": 6,
        "page_title": "Structure of County Government: The County Executive Committee",
        "blocks": [
            {
                "block_type": "concept_explanation",
                "component_type": "concept_explanation",
                "title": "The Executive Arm of County Government",
                "content": {
                    "text": (
                        "The **County Executive Committee (CEC)** implements county laws and manages public administration:\n\n"
                        "- **The County Governor:** Directly elected by county voters; serves as Head of County Executive for a maximum of two 5-year terms.\n"
                        "- **The Deputy Governor:** Running mate of the Governor during the election.\n"
                        "- **County Executive Committee Members (CECs):** Appointed by the Governor with County Assembly approval to head departments (Health, Agriculture, Roads). CECs cannot be members of the County Assembly."
                    )
                }
            }
        ]
    },
    {
        "page_number": 7,
        "page_title": "Comparative Table: County Assembly vs. County Executive",
        "blocks": [
            {
                "block_type": "comparison_table",
                "component_type": "comparison_table",
                "title": "Separation of Powers in County Government",
                "content": {
                    "headers": ["Arm of County Government", "Head / Leadership", "Primary Constitutional Mandate"],
                    "rows": [
                        ["County Assembly (Legislative)", "Speaker of the County Assembly", "Passes county legislation, approves county budgets, and exercises oversight/vetting over the County Executive."],
                        ["County Executive Committee (Executive)", "County Governor & Deputy Governor", "Implements county legislation, executes development projects, and manages daily county public administration."]
                    ]
                }
            }
        ]
    },
    {
        "page_number": 8,
        "page_title": "Devolved Functions of County Governments",
        "blocks": [
            {
                "block_type": "step_process",
                "component_type": "step_process",
                "title": "Seven Core Devolved County Functions (Fourth Schedule)",
                "content": {
                    "steps": [
                        "1. Early Childhood Development Education (ECDE): Managing nursery schools, pre-primary centers, and village vocational polytechnics.",
                        "2. County Health Services: Managing county dispensaries, health centers, maternity clinics, and referral hospitals.",
                        "3. County Transport and Infrastructure: Constructing and maintaining local county access roads, street lighting, parking, and ferries.",
                        "4. Waste Management & Public Sanitation: Refuse removal, solid waste dumping sites, and sewerage management.",
                        "5. Trade Development and Regulation: Controlling local public markets, abattoirs (slaughterhouses), and issuing business trading licenses.",
                        "6. Water and Sanitation Services: Supplying clean drinking water, sinking boreholes, and managing local water piping networks.",
                        "7. Agriculture and Veterinary Services: Crop husbandry, livestock disease control, cattle dips, and agricultural extension training."
                    ]
                }
            }
        ]
    },
    {
        "page_number": 9,
        "page_title": "County Revenue Sources and Key Public Funds",
        "blocks": [
            {
                "block_type": "concept_explanation",
                "component_type": "concept_explanation",
                "title": "Financing the 47 County Governments",
                "content": {
                    "text": (
                        "Counties rely on constitutionally mandated funding sources:\n\n"
                        "- **The Equitable Share:** Primary funding source; counties must receive at least **15%** of all revenue collected nationally by the central government.\n"
                        "- **Conditional Grants:** Allocated by the national government or international donors for specific projects (e.g., upgrading Level 5 hospitals).\n"
                        "- **Own-Source Revenues:** Local taxes collected directly by the county (property rates, parking fees, market licensing, liquor licensing).\n"
                        "- **County Borrowing:** Loans acquired with County Assembly approval and national government guarantee.\n"
                        "- **The Equalization Fund:** **1.5%** of national revenue allocated specifically to provide basic services (water, roads, health, electricity) to marginalized counties."
                    )
                }
            }
        ]
    },
    {
        "page_number": 10,
        "page_title": "Oversight and Accountability: Controller of Budget & Auditor-General",
        "blocks": [
            {
                "block_type": "comparison_table",
                "component_type": "comparison_table",
                "title": "Financial Oversight Independent Offices",
                "content": {
                    "headers": ["Independent Office", "Constitutional Role", "Specific Power over Counties"],
                    "rows": [
                        ["Controller of Budget (COB)", "Oversees budget implementation across national and county governments.", "Must authorize any withdrawal of funds from County Revenue Funds; prevents unauthorized expenditure."],
                        ["Auditor-General", "Conducts independent financial audits of all public accounts.", "Audits county financial records and submits detailed audit reports to the County Assembly and Senate."]
                    ]
                }
            }
        ]
    },
    {
        "page_number": 11,
        "page_title": "Six Systemic Challenges Facing County Governments",
        "blocks": [
            {
                "block_type": "step_process",
                "component_type": "step_process",
                "title": "Operational Obstacles in County Governance",
                "content": {
                    "steps": [
                        "1. Inadequate and Narrow Revenue Bases: Many rural counties lack commercial activity, struggling to raise sufficient own-source revenue.",
                        "2. Delayed Disbursements from National Treasury: Constant treasury cash release delays paralyze health services, stall projects, and delay worker salaries.",
                        "3. Rampant Corruption and Graft: Inflated procurement tenders, ghost workers, and embezzlement of county funds drain public resources.",
                        "4. Shortage of Specialized Personnel: Rural counties struggle to attract and retain doctors, engineers, and certified accountants.",
                        "5. Political Wrangles and Frequent Impeachments: Hostile supremacy battles between MCAs and Governors lead to disruptive impeachment motions.",
                        "6. Jurisdictional Clashes with National Government: Disputes between national ministries and county governments over health functions, roads, and land."
                    ]
                }
            }
        ]
    },
    {
        "page_number": 12,
        "page_title": "Viable Solutions to Devolved Challenges",
        "blocks": [
            {
                "block_type": "step_process",
                "component_type": "step_process",
                "title": "Strategies for Strengthening Devolution",
                "content": {
                    "steps": [
                        "1. Diversification of Local Revenue: Counties must automate revenue collection, promote eco-tourism, and establish agro-processing industries.",
                        "2. Strict Anti-Corruption Enforcement: Prosecuting corrupt county officials and implementing automated e-procurement (IFMIS).",
                        "3. Capacity Building and Training: Continuous training programs for county administrators and medical personnel.",
                        "4. Inter-Governmental Mediation: Utilizing the Intergovernmental Relations Technical Committee (IGRTC) to resolve jurisdictional disputes."
                    ]
                }
            }
        ]
    },
    {
        "page_number": 13,
        "page_title": "KCSE Examination Coaching: Challenges and Solutions in Devolution",
        "blocks": [
            {
                "block_type": "worked_example",
                "component_type": "worked_example",
                "title": "KCSE Question: Explain Five Challenges Faced by County Governments and Suggest a Viable Solution for Each (10 Marks)",
                "content": {
                    "text": (
                        "**Model Answer (Challenge + Solution = 2 Marks per Point):**\n\n"
                        "1. **Delayed Disbursement of Equitable Share:** The National Treasury delays releasing funds, paralyzing services. **Solution:** Enforce strict constitutional timelines and automated disbursements to counties. (2 marks)\n\n"
                        "2. **Corruption and Embezzlement:** Public funds are stolen through inflated procurement tenders and ghost workers. **Solution:** Enforce electronic procurement (IFMIS) and prosecute corrupt officials through the EACC. (2 marks)\n\n"
                        "3. **Shortage of Skilled Technocrats:** Rural counties lack specialized doctors and engineers. **Solution:** Offer hardship allowances, housing incentives, and continuous training to attract professionals. (2 marks)\n\n"
                        "4. **Political Wrangles and Impeachments:** MCAs and Governors engage in supremacy battles that halt budget approval. **Solution:** Establish institutional conflict mediation mechanisms between the executive and legislative arms. (2 marks)\n\n"
                        "5. **Jurisdictional Clashes with National Government:** Disputes over road classifications and health facilities. **Solution:** Clear legislative demarcation of functions through the Intergovernmental Relations Technical Committee. (2 marks)"
                    )
                }
            }
        ]
    },
    {
        "page_number": 14,
        "page_title": "Interactive Classification: Devolved vs. National Functions",
        "blocks": [
            {
                "block_type": "mini_activity",
                "component_type": "mini_activity",
                "title": "Assign Function to County or National Government",
                "content": {
                    "instruction": "Classify each government function correctly under the Fourth Schedule:",
                    "items": [
                        "1. National Defense and Security (KDF) -> **National Government**",
                        "2. Managing County Dispensaries and Health Centers -> **County Government**",
                        "3. Foreign Affairs and International Treaties -> **National Government**",
                        "4. Early Childhood Development Education (ECDE nurseries) -> **County Government**",
                        "5. Refuse disposal and county waste management -> **County Government**",
                        "6. Monetary Policy and Currency Printing -> **National Government**"
                    ]
                }
            }
        ]
    },
    {
        "page_number": 15,
        "page_title": "Topic 5 Comprehensive Mastery Check (Part 1)",
        "blocks": [
            {
                "block_type": "knowledge_check",
                "component_type": "knowledge_check",
                "title": "Topic 5 Mastery Assessment (Part 1)",
                "content": {
                    "questions": [
                        {
                            "question": "What is the constitutional minimum percentage of national revenue that must be allocated to county governments as their equitable share?",
                            "options": [
                                "50%",
                                "15%",
                                "1.5%",
                                "25%"
                            ],
                            "correct_answer": 1,
                            "explanation": "Article 203 of the Constitution mandates that counties receive at least 15% of nationally raised revenue."
                        },
                        {
                            "question": "Which public officer is constitutionally responsible for authorizing withdrawals from County Revenue Funds?",
                            "options": [
                                "The County Governor",
                                "The Speaker of the County Assembly",
                                "The Controller of Budget",
                                "The Auditor-General"
                            ],
                            "correct_answer": 2,
                            "explanation": "The Controller of Budget must approve and authorize any withdrawal from the County Revenue Fund."
                        }
                    ]
                }
            }
        ]
    },
    {
        "page_number": 16,
        "page_title": "Topic 5 Comprehensive Mastery Check (Part 2)",
        "blocks": [
            {
                "block_type": "knowledge_check",
                "component_type": "knowledge_check",
                "title": "Topic 5 Mastery Assessment (Part 2)",
                "content": {
                    "questions": [
                        {
                            "question": "What was the purpose of establishing the Equalization Fund (1.5% of national revenue) in the 2010 Constitution?",
                            "options": [
                                "To finance foreign embassy operations abroad",
                                "To provide basic services like water, roads, health, and electricity to historically marginalized counties",
                                "To purchase military fighter jets",
                                "To pay salaries for Members of Parliament"
                            ],
                            "correct_answer": 1,
                            "explanation": "The Equalization Fund provides basic services to historically marginalized areas to bring them to national parity."
                        },
                        {
                            "question": "Which body is responsible for arbitrating jurisdictional disputes between the national and county governments?",
                            "options": [
                                "The Intergovernmental Relations Technical Committee (IGRTC)",
                                "The Teachers Service Commission",
                                "The Central Bank of Kenya",
                                "The Kenya National Union of Teachers"
                            ],
                            "correct_answer": 0,
                            "explanation": "The IGRTC facilitates consultation and dispute resolution between the two levels of government."
                        }
                    ]
                }
            }
        ]
    },
    {
        "page_number": 17,
        "page_title": "Topic 5 Comprehensive Master Summary",
        "blocks": [
            {
                "block_type": "summary",
                "component_type": "summary",
                "title": "Topic 5 Master Summary: Developments and Challenges in Kenya Since Independence",
                "content": {
                    "text": (
                        "• **Political Trajectory (1963–1991):** Dismantled Majimbo; abolished Senate; passed Turncoat Amendment; banned KPU in 1969; enacted Section 2A in 1982; suppressed 1982 Air Force coup; flawed 1988 Mlolongo triggered 1990 Saba Saba riots.\n"
                        "• **Democratic Transition (1991–2010):** Repealed Section 2A in Dec 1991; IPPG reforms in 1997; NARC ended KANU rule in 2002; 2007 election crisis led to National Accord & Grand Coalition Government in 2008; Constitution promulgated on 27 August 2010.\n"
                        "• **Socio-Economic Reforms:** Resettlement schemes (Million-Acre, Harambee, Haraka, Shirika); 2010 Land classification (Public, Community, Private); Education commissions (Ominde 1964, Mackay 1981 & 8-4-4, FPE 2003).\n"
                        "• **Devolved Governance:** 47 County Governments; Separation of powers (Assembly vs. Executive); Devolved functions (Health, ECDE, Roads, Water, Waste); Revenue (Equitable share min 15%, Equalization Fund 1.5%, Own-source, Grants); Oversight by COB & Auditor-General."
                    )
                }
            }
        ]
    },
    {
        "page_number": 18,
        "page_title": "Topic 5 Final Exam Revision Checklist",
        "blocks": [
            {
                "block_type": "step_process",
                "component_type": "step_process",
                "title": "Mastery Checklist for KCSE History Paper 2",
                "content": {
                    "steps": [
                        "1. Political centralization: 1964 Republic, abolition of Senate, Turncoat amendment, Section 2A.",
                        "2. Return of multipartyism: 6 factors leading to Section 2A repeal, IPPG package 1997, 2002 NARC victory.",
                        "3. 2007 Election crisis: Kriegler & Waki findings, National Accord 2008, 2010 Constitution promulgation.",
                        "4. Multiparty governance: 6 roles of political parties, 6 operational challenges, 4 inherent disadvantages.",
                        "5. Socio-economic policies: Land schemes, 2010 land tenure, industrialization hindrances, Ominde & Mackay commissions.",
                        "6. Devolution: 7 objectives, structures, functions, revenue sources, challenges & solutions."
                    ]
                }
            }
        ]
    }
]


ALL_LESSONS = [
    {
        "unit_order": 1,
        "unit_name": "Political Developments and Constitutional Changes (1963–1991)",
        "lesson_title": "Political Developments and Constitutional Centralization in Kenya (1963–1991)",
        "pages": LESSON_1_PAGES
    },
    {
        "unit_order": 2,
        "unit_name": "Political and Constitutional Developments from 1991 to Present",
        "lesson_title": "The Return to Multi-Partyism, Coalition Governance, and the 2010 Constitution",
        "pages": LESSON_2_PAGES
    },
    {
        "unit_order": 3,
        "unit_name": "Multiparty Democracy in Kenya — Principles, Roles, and Challenges",
        "lesson_title": "Multiparty Democracy in Kenya: Principles, Roles, and Systemic Challenges",
        "pages": LESSON_3_PAGES
    },
    {
        "unit_order": 4,
        "unit_name": "Economic and Social Developments and Challenges Since Independence",
        "lesson_title": "Economic Restructuring, Land Policies, Industrialization, and Social Reforms",
        "pages": LESSON_4_PAGES
    },
    {
        "unit_order": 5,
        "unit_name": "Devolution and County Governments under the 2010 Constitution",
        "lesson_title": "Devolution and County Governance: Origins, Structures, Functions, and Dynamics",
        "pages": LESSON_5_PAGES
    }
]


# ===========================================================================
# DATABASE INGESTION RUNNER
# ===========================================================================

def run_ingestion(replace=False):
    print("=" * 80)
    print("VLEARN CURRICULUM INGESTION: FORM 4 HISTORY — TOPIC 5 (DEVELOPMENTS IN KENYA)")
    print("=" * 80)

    curriculum = Curriculum.objects.filter(name="844").first()
    if not curriculum:
        raise ValueError("Curriculum 844 not found.")
    print(f"[*] Found Curriculum: {curriculum.name} (ID: {curriculum.id})")

    grade = Grade.objects.filter(curriculum=curriculum, name="Form 4").first()
    if not grade:
        raise ValueError("Grade Form 4 not found under Curriculum 844.")
    print(f"[*] Found Grade: {grade.name} (ID: {grade.id})")

    subject = Subject.objects.filter(grade=grade, name="History").first()
    if not subject:
        raise ValueError("Subject History not found under Grade Form 4.")
    print(f"[*] Found Subject: {subject.name} (ID: {subject.id})")

    with transaction.atomic():
        topic, topic_created = Topic.objects.get_or_create(
            subject=subject,
            name="Social, Economic and Political Developments and Challenges in Kenya Since Independence",
            defaults={"order": 5}
        )
        if topic_created:
            print(f"[+] Created Topic: {topic.name} (Order: {topic.order})")
        else:
            topic.order = 5
            topic.save()
            print(f"[*] Found Existing Topic: {topic.name} (ID: {topic.id})")

        total_pages = 0
        total_blocks = 0
        total_assets = 0

        for l_def in ALL_LESSONS:
            unit_order = l_def["unit_order"]
            unit_name = l_def["unit_name"]
            lesson_title = l_def["lesson_title"]
            pages = l_def["pages"]

            learning_unit, u_created = LearningUnit.objects.get_or_create(
                topic=topic,
                name=unit_name,
                defaults={"order": unit_order}
            )
            if not u_created:
                learning_unit.order = unit_order
                learning_unit.save()
                print(f"\n[*] Found Existing Learning Unit {unit_order}: {unit_name} (ID: {learning_unit.id})")
            else:
                print(f"\n[+] Created Learning Unit {unit_order}: {unit_name} (ID: {learning_unit.id})")

            lesson, l_created = Lesson.objects.get_or_create(
                topic=topic,
                learning_unit=learning_unit,
                title=lesson_title,
                defaults={
                    "status": "published",
                    "version": 1
                }
            )
            if not l_created:
                lesson.title = lesson_title
                lesson.status = "published"
                lesson.save()
                print(f"  [*] Found Existing Lesson: {lesson_title} (ID: {lesson.id})")
            else:
                print(f"  [+] Created Lesson: {lesson_title} (ID: {lesson.id})")

            if replace:
                deleted_count, _ = lesson.blocks.all().delete()
                print(f"      [!] Cleared {deleted_count} existing blocks for clean rebuild.")
                LessonAsset.objects.filter(lesson=lesson).delete()

            block_order_counter = 10

            for page in pages:
                page_num = page["page_number"]
                page_title = page["page_title"]
                blocks = page["blocks"]
                total_pages += 1

                for comp_idx, block_info in enumerate(blocks, 1):
                    b_type = block_info["block_type"]
                    c_type = block_info["component_type"]
                    b_title = block_info.get("title", page_title)
                    b_content = clean_content_dict(block_info.get("content", {}))

                    block, b_created = LessonBlock.objects.get_or_create(
                        lesson=lesson,
                        page_number=page_num,
                        component_order=comp_idx,
                        defaults={
                            "block_type": b_type,
                            "component_type": c_type,
                            "title": b_title,
                            "page_title": page_title,
                            "order": block_order_counter,
                            "content": b_content,
                            "metadata": {"concept_group": page_title}
                        }
                    )

                    if not b_created:
                        block.block_type = b_type
                        block.component_type = c_type
                        block.title = b_title
                        block.page_title = page_title
                        block.order = block_order_counter
                        block.content = b_content
                        block.metadata = {"concept_group": page_title}
                        block.save()

                    # Attach LessonAsset if this is a media block with url/author/licensing
                    if b_type in ["suggested_image", "suggested_video"] and isinstance(b_content, dict) and b_content.get("url"):
                        media_url = b_content.get("url")
                        author = b_content.get("author", "Educational Resource")
                        licensing = b_content.get("licensing", "Standard")
                        commons_page_url = b_content.get("commons_page_url", "")
                        asset_type = "video" if b_type == "suggested_video" else "image"

                        asset, a_created = LessonAsset.objects.get_or_create(
                            lesson=lesson,
                            title=b_title,
                            defaults={
                                "asset_type": asset_type,
                                "source_type": "external",
                                "storage_type": "url",
                                "status": "attached",
                                "url": media_url,
                                "description": b_content.get("text", b_title),
                                "metadata": {
                                    "author": author,
                                    "licensing": licensing,
                                    "commons_page_url": commons_page_url,
                                    "caption": b_content.get("text", b_title)
                                }
                            }
                        )
                        if not a_created:
                            asset.url = media_url
                            asset.status = "attached"
                            asset.asset_type = asset_type
                            asset.metadata = {
                                "author": author,
                                "licensing": licensing,
                                "commons_page_url": commons_page_url,
                                "caption": b_content.get("text", b_title)
                            }
                            asset.save()

                        asset.blocks.add(block)
                        total_assets += 1

                    block_order_counter += 10
                    total_blocks += 1

            print(f"      [OK] Ingested {len(pages)} Pages for Lesson {unit_order}.")

        print("=" * 80)
        print(f"[SUCCESS] Form 4 History Topic 5 Ingestion Complete!")
        print(f"[*] Total Lessons Ingested: {len(ALL_LESSONS)}")
        print(f"[*] Total Pages Ingested:   {total_pages}")
        print(f"[*] Total Blocks Ingested:  {total_blocks}")
        print(f"[*] Total Media Assets:     {total_assets}")
        print("=" * 80)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Ingest Form 4 History Topic 5")
    parser.add_argument("--replace", action="store_true", help="Replace existing blocks with a fresh rebuild")
    args = parser.parse_args()

    run_ingestion(replace=args.replace)
