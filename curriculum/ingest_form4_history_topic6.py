"""
VLearn Curriculum Ingestion Engine: Form 4 History — Topic 6 (Developments and Challenges in Africa Since Independence)

Target Subject: History (Subject ID: 17)
Grade: Form 4 (Grade ID: 4)
Curriculum: 844 (Curriculum ID: 4)

Topic 6: Social, Economic and Political Developments and Challenges in Africa Since Independence (Order: 6)
  - Unit 1: The Post-Colonial Political and Economic Inheritance (Lesson 1: 15 Pages)
  - Unit 2: Country Case Study — The Democratic Republic of Congo (Zaire) (Lesson 2: 16 Pages)
  - Unit 3: Country Case Study — Tanzania (Lesson 3: 16 Pages)
  - Unit 4: General Political, Economic, and Social Challenges in Africa (Lesson 4: 16 Pages)
  - Unit 5: African Responses and Development Measures (Lesson 5: 18 Pages)

Total: 5 Learning Units, 5 Lessons, 81 Pages, 95+ Blocks, 9 Media Assets (4 Wikimedia Photos + 5 Verified YouTube Videos)

Usage:
  ./venv/bin/python curriculum/ingest_form4_history_topic6.py --replace
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
# LESSON DEFINITIONS: FORM 4 HISTORY TOPIC 6
# ===========================================================================

LESSON_1_PAGES = [
    {
        "page_number": 1,
        "page_title": "The Post-Colonial Political and Economic Inheritance",
        "blocks": [
            {
                "block_type": "learning_goal",
                "component_type": "learning_goal",
                "title": "Lesson Objectives: The Inherited Crises of Independent Africa",
                "content": {
                    "text": (
                        "By the end of this lesson, you will be able to:\n"
                        "- Identify the fundamental political, economic, and social inherited problems faced by African states at independence\n"
                        "- Explain the impact of the Cold War and superpower proxy conflicts on the African continent\n"
                        "- Analyze the causes and consequences of the epidemic of military coups between 1960 and the mid-1980s\n"
                        "- Apply historical evidence to explain why post-colonial African states struggled to achieve economic independence"
                    )
                }
            },
            {
                "block_type": "definition_card",
                "component_type": "definition_card",
                "title": "Concept: The Post-Colonial Predicament",
                "content": {
                    "term": "Post-Colonial Inherited Crises",
                    "definition": (
                        "The structural, economic, and institutional weaknesses inherited by newly sovereign African nations from colonial regimes, "
                        "designed for colonial resource extraction rather than sustainable democratic governance."
                    )
                }
            }
        ]
    },
    {
        "page_number": 2,
        "page_title": "Four Core Inherited Post-Independence Crises",
        "blocks": [
            {
                "block_type": "step_process",
                "component_type": "step_process",
                "title": "Structural Hurdles at Independence",
                "content": {
                    "steps": [
                        "1. Acute Shortage of African Technocrats: Colonial authorities excluded Africans from senior administrative, legal, and financial roles. In the DRC in 1960, there were fewer than twenty university graduates in the entire country.",
                        "2. The Divide-and-Rule Legacy: Colonial rulers maintained dominance by playing ethnic communities against one another, fostering deep-seated suspicions that triggered post-colonial civil wars (Nigeria, Uganda).",
                        "3. Arbitrary Colonial Borders: The 1884-1885 Berlin Conference drew boundaries that split homogeneous ethnic groups across different states (e.g., Somalis across Kenya, Somalia, Ethiopia) and forced historic rivals together.",
                        "4. Extractive Export-Oriented Economies: Transport and farming were structured solely to export raw materials (cocoa, coffee, copper, gold) to Europe, leaving states without domestic manufacturing."
                    ]
                }
            }
        ]
    },
    {
        "page_number": 3,
        "page_title": "The Impact of the Cold War on Africa",
        "blocks": [
            {
                "block_type": "concept_explanation",
                "component_type": "concept_explanation",
                "title": "Superpower Rivalry and Ideological Polarization",
                "content": {
                    "text": (
                        "African independence coincided with the height of the Cold War between the Capitalist West (USA) and Communist East (USSR):\n\n"
                        "- **Ideological Polarization:** Leaders were pressured to align with capitalism or socialism, splitting the continent into antagonistic factions (Casablanca vs. Brazzaville/Monrovia blocs).\n"
                        "- **Superpower Proxy Wars:** The US and USSR pumped weapons, funds, and mercenary troops into civil conflicts, prolonging wars in Angola, Mozambique, Ethiopia, and the Congo.\n"
                        "- **Sponsorship of Authoritarian Dictators:** Superpowers backed corrupt and brutal dictators (e.g., Mobutu Sese Seko of Zaire) simply because they were anti-communist or anti-capitalist allies."
                    )
                }
            }
        ]
    },
    {
        "page_number": 4,
        "page_title": "Historical Documentary: Cold War Conflicts in Africa",
        "blocks": [
            {
                "block_type": "suggested_video",
                "component_type": "suggested_video",
                "title": "Historical Documentary: Cold War Proxy Wars Across Africa",
                "content": {
                    "url": "https://www.youtube.com/watch?v=_COtDXgUXwg",
                    "text": "Examine how the geopolitical struggle between the United States and the Soviet Union fueled proxy wars, military coups, and dictatorships across post-colonial Africa.",
                    "author": "The Front / Historical Documentary",
                    "licensing": "Standard YouTube License"
                }
            }
        ]
    },
    {
        "page_number": 5,
        "page_title": "The Epidemic of Military Coups (1960–1985)",
        "blocks": [
            {
                "block_type": "concept_explanation",
                "component_type": "concept_explanation",
                "title": "The Collapse of Civilian Democracies",
                "content": {
                    "text": (
                        "During the first 25 years of independence, over **70 African heads of state** were overthrown in military coups:\n\n"
                        "- **Governance Failures:** Civilian politicians became associated with self-enrichment, corruption, and the suppression of democratic opposition.\n"
                        "- **Suppression of Opposition:** As leaders banned rival parties and formed one-party states, the army became the only organized body capable of forcing leadership change.\n"
                        "- **Ethnic Favoritism:** Presidents placed relatives and kinsmen in senior security posts, alienating other ethnic groups within the army ranks.\n"
                        "- **Military Grievances:** Poor salaries, substandard barracks, and unfair promotion criteria triggered army mutinies.\n"
                        "- **Foreign Intelligence Plots:** Superpowers and former colonial masters orchestrated coups against radical nationalist leaders (e.g., Patrice Lumumba in Congo, Kwame Nkrumah in Ghana)."
                    )
                }
            }
        ]
    },
    {
        "page_number": 6,
        "page_title": "General Mobutu Sese Seko and Military Dictatorship",
        "blocks": [
            {
                "block_type": "suggested_image",
                "component_type": "suggested_image",
                "title": "General Mobutu Sese Seko (1969)",
                "content": {
                    "text": "General Mobutu Sese Seko in military uniform, who seized power in a 1965 coup and ruled Zaire as an authoritarian military dictator for 32 years.",
                    "url": "https://upload.wikimedia.org/wikipedia/commons/7/7e/Mobutu_Sese_Seko%2C_1969.jpg",
                    "author": "Public Domain / Wikimedia Commons",
                    "licensing": "Public Domain",
                    "commons_page_url": "https://commons.wikimedia.org/wiki/File:Mobutu_Sese_Seko,_1969.jpg"
                }
            }
        ]
    },
    {
        "page_number": 7,
        "page_title": "Comparative Table: Inherited Crises Across Africa",
        "blocks": [
            {
                "block_type": "comparison_table",
                "component_type": "comparison_table",
                "title": "Analysis of Post-Colonial Inherited Crises",
                "content": {
                    "headers": ["Domain", "Inherited Colonial Problem", "Post-Independence Manifestation"],
                    "rows": [
                        ["Political", "Divide-and-rule governance & absence of African administrators.", "Ethnic civil wars (Nigeria/Biafra), border conflicts, and authoritarian military coups."],
                        ["Economic", "Extractive monoculture economies geared toward raw exports.", "Neo-colonial dependency, unfavorable terms of trade, lack of domestic manufacturing."],
                        ["Social", "Racial segregation in schools & neglect of African healthcare.", "Mass illiteracy, shortage of doctors, rural-urban migration, and epidemic diseases."]
                    ]
                }
            }
        ]
    },
    {
        "page_number": 8,
        "page_title": "Primary Source Analysis: The Nationalist Dilemma (1961)",
        "blocks": [
            {
                "block_type": "callout",
                "component_type": "callout",
                "title": "Historical Inquiry: Independence in Name Only",
                "content": {
                    "text": (
                        "**Excerpt from an African Nationalist Speech (1961):**\n"
                        "*> 'We are independent in name, but our schools teach European history, our factories process raw materials for European markets, and our armies are commanded by European officers.'*\n\n"
                        "**Analytical Questions:**\n"
                        "1. **Identify the Phenomenon:** What historical reality is being described (Neo-colonialism)?\n"
                        "2. **Explain the Consequence:** Why did political flag independence fail to translate automatically into economic sovereignty?"
                    )
                }
            }
        ]
    },
    {
        "page_number": 9,
        "page_title": "Five Causes of Military Takeovers (Point-Form)",
        "blocks": [
            {
                "block_type": "step_process",
                "component_type": "step_process",
                "title": "Examinable Factors Behind Military Coups",
                "content": {
                    "steps": [
                        "1. Rampant Corruption and Mismanagement: Civilian governments embezzled state funds and failed to deliver basic public services.",
                        "2. Dictatorship and Ban on Opposition: One-party regimes outlawed democratic opposition, making military force the only avenue for political change.",
                        "3. Tribalism and Nepotism in the Army: Ethnic favoritism in military promotions created intense resentment among passed-over officer corps.",
                        "4. Internal Service Grievances: Inadequate military salaries, poor living quarters, and outdated equipment prompted soldiers to mutiny.",
                        "5. External Foreign Interference: Foreign intelligence agencies (CIA, Belgian mining lobbies) plotted coups to protect Western mineral and geopolitical interests."
                    ]
                }
            }
        ]
    },
    {
        "page_number": 10,
        "page_title": "Interactive Classification: Post-Colonial Crises",
        "blocks": [
            {
                "block_type": "mini_activity",
                "component_type": "mini_activity",
                "title": "Classify the Crisis into Political, Economic, or Social",
                "content": {
                    "instruction": "Categorize each post-colonial inherited problem correctly:",
                    "items": [
                        "1. Inability to manufacture domestic machinery and heavy goods -> **Economic Challenge**",
                        "2. Overthrow of civilian governments by army generals -> **Political Challenge**",
                        "3. High rates of illiteracy and lack of universities -> **Social Challenge**",
                        "4. Border disputes caused by the Berlin Conference boundaries -> **Political Challenge**",
                        "5. Unfavorable terms of trade on raw commodity exports -> **Economic Challenge**"
                    ]
                }
            }
        ]
    },
    {
        "page_number": 11,
        "page_title": "KCSE Examination Coaching: Causes of Military Coups",
        "blocks": [
            {
                "block_type": "worked_example",
                "component_type": "worked_example",
                "title": "KCSE Question: Explain Six Factors That Contributed to Military Coups in Africa (12 Marks)",
                "content": {
                    "text": (
                        "**Model Answer (Point + Explanation = 2 Marks per Point):**\n\n"
                        "1. **Rampant Corruption and Economic Mismanagement:** Civilian politicians embezzled state funds and ruined national economies, prompting the military to intervene to 'restore order'. (2 marks)\n\n"
                        "2. **Suppression of Democratic Opposition:** Civilian leaders created oppressive one-party states and banned rival parties, leaving armed rebellion as the only route to remove them. (2 marks)\n\n"
                        "3. **Ethnic Favoritism and Nepotism:** Political leaders appointed their kinsmen to commanding security positions, breeding bitter resentment among other ethnic groups in the armed forces. (2 marks)\n\n"
                        "4. **Professional Military Grievances:** Soldiers frequently mutinied over poor pay, inadequate equipment, and unfair promotions. (2 marks)\n\n"
                        "5. **Foreign External Conspiracies:** Western and Eastern superpowers orchestrated coups against leaders whose policies threatened foreign geopolitical or mining interests. (2 marks)\n\n"
                        "6. **Ambition of Military Commanders:** Senior army generals capitalized on political instability to seize state power for personal prestige and wealth. (2 marks)"
                    )
                }
            }
        ]
    },
    {
        "page_number": 12,
        "page_title": "The Berlin Conference Legacy: Border Disputes",
        "blocks": [
            {
                "block_type": "concept_explanation",
                "component_type": "concept_explanation",
                "title": "Arbitrary Borders and Post-Colonial Conflict",
                "content": {
                    "text": (
                        "- **1884–1885 Berlin Partition:** European powers carved up Africa with straight lines without regard to ethnic, linguistic, or cultural boundaries.\n"
                        "- **Post-Colonial Flashpoints:**\n"
                        "  - **Somalia vs. Kenya & Ethiopia:** The Ogaden War and Shifta conflict over the Somali-inhabited territories.\n"
                        "  - **Ethiopia vs. Eritrea:** Decades-long border warfare over Badme.\n"
                        "  - **Libya vs. Chad:** Conflict over the mineral-rich Aouzou Strip.\n"
                        "- **OAU Principle (1964 Cairo Resolution):** The OAU declared that colonial borders must be respected (*intangibility of frontiers*) to prevent endless continental wars."
                    )
                }
            }
        ]
    },
    {
        "page_number": 13,
        "page_title": "Check Your Understanding: Module 6.1",
        "blocks": [
            {
                "block_type": "knowledge_check",
                "component_type": "knowledge_check",
                "title": "Module 6.1 Assessment",
                "content": {
                    "questions": [
                        {
                            "question": "How many university graduates did the Democratic Republic of Congo have at independence in 1960?",
                            "options": [
                                "Over 5,000 graduates",
                                "Fewer than 20 graduates",
                                "Approximately 500 graduates",
                                "Zero graduates"
                            ],
                            "correct_answer": 1,
                            "explanation": "Belgian colonial neglect left the entire DRC with fewer than 20 university graduates in 1960."
                        },
                        {
                            "question": "What principle did the OAU adopt in 1964 regarding colonial borders?",
                            "options": [
                                "All borders must be redrawn immediately along tribal boundaries",
                                "Colonial borders must be respected and preserved to prevent civil conflicts",
                                "All African borders should be dissolved into a single continental state",
                                "Border control should be managed by the United Nations"
                            ],
                            "correct_answer": 1,
                            "explanation": "The 1964 Cairo OAU resolution affirmed the respect for borders existing on achievement of independence."
                        }
                    ]
                }
            }
        ]
    },
    {
        "page_number": 14,
        "page_title": "Lesson Summary & Key Takeaways",
        "blocks": [
            {
                "block_type": "summary",
                "component_type": "summary",
                "title": "Core Summary: Post-Colonial Inheritance",
                "content": {
                    "text": (
                        "• **Inherited Crises:** Technocrat shortages, divide-and-rule animosity, arbitrary Berlin borders, and extractive primary commodity economies.\n"
                        "• **Cold War Interventions:** Ideological polarization, proxy civil wars (Angola, Congo), and foreign sponsorship of dictators.\n"
                        "• **Military Coups:** Over 70 coups between 1960 and 1985 caused by corruption, one-party authoritarianism, ethnic favoritism, and foreign plots."
                    )
                }
            },
            {
                "block_type": "key_takeaway",
                "component_type": "key_takeaway",
                "title": "Key Takeaways",
                "content": {
                    "text": (
                        "- Political independence did not automatically grant economic or institutional self-determination.\n"
                        "- Colonial structural distortions set the stage for post-independence military instability."
                    )
                }
            }
        ]
    },
    {
        "page_number": 15,
        "page_title": "Revision Checklist: Inherited Crises",
        "blocks": [
            {
                "block_type": "step_process",
                "component_type": "step_process",
                "title": "Mastery Checklist",
                "content": {
                    "steps": [
                        "1. Four inherited crises (technocrats, ethnic divisions, borders, extractive economy).",
                        "2. Three dimensions of Cold War impact in Africa.",
                        "3. Five causes of military coups.",
                        "4. OAU 1964 Cairo resolution on colonial borders."
                    ]
                }
            }
        ]
    }
]

LESSON_2_PAGES = [
    {
        "page_number": 1,
        "page_title": "Country Case Study: The Democratic Republic of Congo (Zaire)",
        "blocks": [
            {
                "block_type": "learning_goal",
                "component_type": "learning_goal",
                "title": "Lesson Objectives: The DRC Post-Independence Trajectory",
                "content": {
                    "text": (
                        "By the end of this lesson, you will be able to:\n"
                        "- Trace the causes and course of the Congo Crisis (1960–1965) and the assassination of Patrice Lumumba\n"
                        "- Analyze the rise and rule of General Mobutu Sese Seko and the 1971 Authenticity Programme\n"
                        "- Explain the economic policies of Zairianization, kleptocracy, and the collapse of infrastructure\n"
                        "- Evaluate the social crises, education collapse, healthcare breakdowns, and the 1997 overthrow of Mobutu by Laurent Kabila"
                    )
                }
            },
            {
                "block_type": "definition_card",
                "component_type": "definition_card",
                "title": "Concept: The Congo Crisis",
                "content": {
                    "term": "The Congo Crisis (1960–1965)",
                    "definition": (
                        "A turbulent period of political upheaval, army mutinies, provincial secessions (Katanga and Kasai), "
                        "and Cold War superpower proxy warfare immediately following the DRC's independence from Belgium on 30 June 1960."
                    )
                }
            }
        ]
    },
    {
        "page_number": 2,
        "page_title": "The Outbreak of the Congo Crisis (1960)",
        "blocks": [
            {
                "block_type": "concept_explanation",
                "component_type": "concept_explanation",
                "title": "Independence and Immediate Turmoil",
                "content": {
                    "text": (
                        "The DRC gained independence from Belgium on **30 June 1960** with a fragile power-sharing setup:\n\n"
                        "- **President:** Joseph Kasavubu (leader of the regional ABAKO party).\n"
                        "- **Prime Minister:** Patrice Lumumba (leader of the nationalist MNC party).\n"
                        "- **The Army Mutiny:** Days after independence, African soldiers in the *Force Publique* mutinied against Belgian officers demanding pay and promotions.\n"
                        "- **Belgian Armed Intervention:** Belgium sent paratroopers back to Congo without government consent, violating Congolese sovereignty.\n"
                        "- **Secession of Katanga & Kasai:** Moise Tshombe declared mineral-rich **Katanga** independent, while Albert Kalonji seceded **Kasai**, backed by Belgian mining companies."
                    )
                }
            },
            {
                "block_type": "suggested_image",
                "component_type": "suggested_image",
                "title": "Patrice Lumumba, First Prime Minister of Congo (1960)",
                "content": {
                    "text": "Patrice Lumumba, charismatic nationalist and first Prime Minister of the Democratic Republic of the Congo in 1960.",
                    "url": "https://upload.wikimedia.org/wikipedia/commons/7/7b/Patrice_Lumumba%2C_1960.jpg",
                    "author": "Public Domain / Wikimedia Commons",
                    "licensing": "Public Domain",
                    "commons_page_url": "https://commons.wikimedia.org/wiki/File:Patrice_Lumumba,_1960.jpg"
                }
            }
        ]
    },
    {
        "page_number": 3,
        "page_title": "Historical Documentary: The Assassination of Patrice Lumumba",
        "blocks": [
            {
                "block_type": "suggested_video",
                "component_type": "suggested_video",
                "title": "Historical Documentary: The Tragic Fate of Patrice Lumumba",
                "content": {
                    "url": "https://www.youtube.com/watch?v=17BAbZUHFb4",
                    "text": "Examine the political struggle of Patrice Lumumba, the Katanga secession, UN peacekeeping controversies, and his assassination in January 1961.",
                    "author": "Across TheAges / Historical Documentaries",
                    "licensing": "Standard YouTube License"
                }
            }
        ]
    },
    {
        "page_number": 4,
        "page_title": "The Fall and Murder of Patrice Lumumba (1961)",
        "blocks": [
            {
                "block_type": "concept_explanation",
                "component_type": "concept_explanation",
                "title": "UN Peacekeeping Hesitation and Cold War Murder",
                "content": {
                    "text": (
                        "- **The UN Dilemma:** Lumumba appealed to the UN peacekeeping force (ONUC) to crush the Katanga secession, but the UN refused to take sides in internal disputes.\n"
                        "- **Turning to the Soviets:** Frustrated, Lumumba requested Soviet military aircraft and transport trucks, alarming the US and Western allies.\n"
                        "- **The Dismissal & Capture:** Kasavubu dismissed Lumumba; army chief Mobutu placed him under house arrest.\n"
                        "- **Assassination (17 January 1961):** Lumumba was flown to Katanga and executed by firing squad in the presence of Belgian officers, turning him into a global martyr of anti-imperialism."
                    )
                }
            }
        ]
    },
    {
        "page_number": 5,
        "page_title": "The Rise of General Mobutu Sese Seko (1965)",
        "blocks": [
            {
                "block_type": "concept_explanation",
                "component_type": "concept_explanation",
                "title": "The 1965 Bloodless Coup and One-Party Dictatorship",
                "content": {
                    "text": (
                        "In November 1965, General **Joseph-Désiré Mobutu** seized power in a bloodless coup, establishing a personalist dictatorship:\n\n"
                        "- **Total Centralization:** Suspended the constitution, dissolved parliament, abolished regional federalism, and declared the **Popular Movement of the Revolution (MPR)** the sole legal party.\n"
                        "- **Cult of Personality:** Mobutu portrayed himself as the 'Father of the Nation', 'Helmsman', and 'Redeemer', controlling all appointments and state revenues.\n"
                        "- **Western Backing:** Strongly funded and armed by the USA and France as an anti-communist ally during the Cold War."
                    )
                }
            }
        ]
    },
    {
        "page_number": 6,
        "page_title": "The Authenticity Programme (1971)",
        "blocks": [
            {
                "block_type": "step_process",
                "component_type": "step_process",
                "title": "Mobutu's Cultural Campaign: Erasing the Colonial Past",
                "content": {
                    "steps": [
                        "1. Renaming the Country: Renamed Congo to Zaire in 1971; the national currency was renamed the Zaire.",
                        "2. Renaming Major Cities: Leopoldville became Kinshasa; Elisabethville became Lubumbashi; Stanleyville became Kisangani.",
                        "3. Africanisation of Names: Banned Christian/European names. The President adopted the name 'Mobutu Sese Seko Kuku Ngbendu Wa Za Banga' ('the all-powerful warrior who goes from conquest to conquest leaving fire in his wake').",
                        "4. Traditional Dress Code: Banned Western suits and ties, replacing them with the 'abacost' (a collarless tailored African tunic).",
                        "5. Nationalization of Church Institutions: Clashed with the Catholic Church, banning religious instruction in schools and taking over church-run hospitals."
                    ]
                }
            }
        ]
    },
    {
        "page_number": 7,
        "page_title": "Economic Collapse: 'Zairianization' and Kleptocracy",
        "blocks": [
            {
                "block_type": "concept_explanation",
                "component_type": "concept_explanation",
                "title": "From Mineral Riches to Economic Ruin",
                "content": {
                    "text": (
                        "Despite immense deposits of copper, cobalt, diamonds, and gold, the economy collapsed:\n\n"
                        "- **The Failure of 'Zairianization' (1973):** Mobutu nationalized all foreign-owned commercial farms, plantations, and retail businesses, handing them to political cronies (*acquéreurs*) who looted working capital and abandoned farms.\n"
                        "- **Textbook Kleptocracy (Rule by Thieves):** Mineral revenues and state budgets were siphoned directly into Mobutu's Swiss bank accounts; by the 1980s, Mobutu's personal fortune exceeded Zaire's foreign debt.\n"
                        "- **Hyperinflation:** The zaire currency became worthless; the formal cash economy collapsed into black market barter trade (*Article 15: 'Fend for yourself'*).\n"
                        "- **Infrastructure Ruin:** Roads and river ferries deteriorated, cutting off agricultural provinces from urban markets."
                    )
                }
            }
        ]
    },
    {
        "page_number": 8,
        "page_title": "Social Crises in the DRC",
        "blocks": [
            {
                "block_type": "step_process",
                "component_type": "step_process",
                "title": "Social Breakdown in Post-Colonial Congo",
                "content": {
                    "steps": [
                        "1. Education System Collapse: Teacher salaries went unpaid for years; universities suffered from a lack of books, equipment, and research funding.",
                        "2. Healthcare Decay & Epidemics: Public hospitals lacked drugs, equipment, and electricity; the country suffered severe outbreaks of Ebola, cholera, and HIV/AIDS.",
                        "3. Massive Urban Congestion: Rural poverty drove millions into Kinshasa slums lacking clean water, sewage, and electricity.",
                        "4. The Refugee & Displacement Crisis: Chronic rebellions (Shaba I & II, 1996–1997 liberation war) displaced millions of civilians, causing severe humanitarian crises."
                    ]
                }
            }
        ]
    },
    {
        "page_number": 9,
        "page_title": "The Fall of Mobutu and Rise of the Kabilas (1997–2001)",
        "blocks": [
            {
                "block_type": "concept_explanation",
                "component_type": "concept_explanation",
                "title": "The 1997 AFDL Rebellion and the Renaming to DRC",
                "content": {
                    "text": (
                        "- **End of the Cold War:** With the Soviet Union gone, Western powers withdrew military and financial support from Mobutu.\n"
                        "- **The AFDL Campaign (1996–1997):** Rebel leader **Laurent-Désiré Kabila**, backed by Rwanda and Uganda, launched a swift offensive, marching from the east to Kinshasa.\n"
                        "- **Mobutu's Flight:** Mobutu fled into exile in Morocco (dying in September 1997). Kabila declared himself President and renamed Zaire back to the **Democratic Republic of Congo (DRC)**.\n"
                        "- **Assassination & Succession (2001):** Laurent Kabila was assassinated by a bodyguard in January 2001 and succeeded by his son, **Joseph Kabila**, who signed peace accords ending the 'African World War'."
                    )
                }
            }
        ]
    },
    {
        "page_number": 10,
        "page_title": "Map of the DRC and Secessionist Provinces",
        "blocks": [
            {
                "block_type": "suggested_image",
                "component_type": "suggested_image",
                "title": "Geographical Location of the Democratic Republic of the Congo",
                "content": {
                    "text": "Map showing the vast geographical expanse of the Democratic Republic of the Congo in Central Africa.",
                    "url": "https://upload.wikimedia.org/wikipedia/commons/8/88/Democratic_Republic_of_the_Congo_in_Africa.svg",
                    "author": "Public Domain / Wikimedia Commons",
                    "licensing": "Public Domain",
                    "commons_page_url": "https://commons.wikimedia.org/wiki/File:Democratic_Republic_of_the_Congo_in_Africa.svg"
                }
            }
        ]
    },
    {
        "page_number": 11,
        "page_title": "Interactive Classification: DRC Historical Events",
        "blocks": [
            {
                "block_type": "mini_activity",
                "component_type": "mini_activity",
                "title": "Match the Event in DRC History to Its Description",
                "content": {
                    "instruction": "Test your mastery of Congolese post-independence history:",
                    "items": [
                        "1. First Prime Minister assassinated in January 1961 -> **Patrice Lumumba**",
                        "2. Mineral-rich province that seceded under Moise Tshombe in 1960 -> **Katanga**",
                        "3. Policy of nationalizing foreign businesses handed to political cronies -> **Zairianization (1973)**",
                        "4. Campaign renaming cities, banning European suits, and introducing abacost -> **Authenticity Programme (1971)**",
                        "5. Rebel leader who ousted Mobutu in May 1997 -> **Laurent-Désiré Kabila**"
                    ]
                }
            }
        ]
    },
    {
        "page_number": 12,
        "page_title": "KCSE Examination Coaching: Economic Collapse in Zaire",
        "blocks": [
            {
                "block_type": "worked_example",
                "component_type": "worked_example",
                "title": "KCSE Question: Explain Six Factors That Led to the Collapse of the Economy of Zaire Under Mobutu (12 Marks)",
                "content": {
                    "text": (
                        "**Model Answer (Point + Explanation = 2 Marks per Point):**\n\n"
                        "1. **The Failure of Zairianization (1973):** Foreign-owned commercial businesses and plantations were nationalized and allocated to inexperienced political allies who looted assets and collapsed production. (2 marks)\n\n"
                        "2. **Pervasive Kleptocracy and Corruption:** State revenues and mineral export proceeds were diverted directly into Mobutu's personal foreign bank accounts. (2 marks)\n\n"
                        "3. **Hyperinflation and Currency Collapse:** Excessive printing of unbacked zaire currency made the money worthless, destroying the formal banking economy. (2 marks)\n\n"
                        "4. **Ruin of Transport and Communication Networks:** Neglect of colonial roads, railways, and river barges isolated rural farmers and halted domestic commerce. (2 marks)\n\n"
                        "5. **Heavy Crushing Foreign Debt Burden:** Massive borrowing from Western lenders and IMF for white-elephant projects consumed national budgets in debt service. (2 marks)\n\n"
                        "6. **Shortage of Skilled Technocrats:** The sudden departure of foreign engineers and accountants after independence and Zairianization left mines and factories unmanaged. (2 marks)"
                    )
                }
            }
        ]
    },
    {
        "page_number": 13,
        "page_title": "Check Your Understanding: Module 6.2",
        "blocks": [
            {
                "block_type": "knowledge_check",
                "component_type": "knowledge_check",
                "title": "Module 6.2 Assessment",
                "content": {
                    "questions": [
                        {
                            "question": "What was the name of the traditional collarless tunic introduced by Mobutu to replace Western suits?",
                            "options": [
                                "Kanzu",
                                "Abacost",
                                "Dashiki",
                                "Agbada"
                            ],
                            "correct_answer": 1,
                            "explanation": "Mobutu introduced the abacost (from the French 'à bas le costume' — down with the suit) under Authenticity."
                        },
                        {
                            "question": "Which leader led the AFDL rebellion that overthrew Mobutu Sese Seko in 1997?",
                            "options": [
                                "Joseph Kasavubu",
                                "Laurent-Désiré Kabila",
                                "Moise Tshombe",
                                "Patrice Lumumba"
                            ],
                            "correct_answer": 1,
                            "explanation": "Laurent-Désiré Kabila led the AFDL forces to take Kinshasa in May 1997, renaming the country DRC."
                        }
                    ]
                }
            }
        ]
    },
    {
        "page_number": 14,
        "page_title": "Lesson Summary & Key Takeaways",
        "blocks": [
            {
                "block_type": "summary",
                "component_type": "summary",
                "title": "Core Summary: The DRC Case Study",
                "content": {
                    "text": (
                        "• **Congo Crisis (1960–1965):** Independence marked by army mutiny, Katanga/Kasai secessions, Cold War meddling, and Lumumba's assassination.\n"
                        "• **Mobutu Era (1965–1997):** 32-year dictatorship; MPR one-party state; 1971 Authenticity campaign (Zaire, abacost); Western-backed anti-communist ally.\n"
                        "• **Economic Ruin:** Zairianization policy failure (1973), kleptocracy, hyperinflation, transport collapse.\n"
                        "• **Post-Mobutu:** Overthrown by Laurent Kabila (1997); assassinated in 2001; succeeded by Joseph Kabila."
                    )
                }
            },
            {
                "block_type": "key_takeaway",
                "component_type": "key_takeaway",
                "title": "Key Takeaways",
                "content": {
                    "text": (
                        "- The DRC illustrates how immense mineral resources can fuel conflict and corruption rather than development.\n"
                        "- Cold War superpower meddling severely crippled democratic nation-building in Central Africa."
                    )
                }
            }
        ]
    },
    {
        "page_number": 15,
        "page_title": "Revision Checklist: DRC Trajectory",
        "blocks": [
            {
                "block_type": "step_process",
                "component_type": "step_process",
                "title": "Mastery Checklist",
                "content": {
                    "steps": [
                        "1. Key players: Kasavubu, Lumumba, Tshombe, Mobutu, Laurent Kabila.",
                        "2. Four elements of the Authenticity Programme (names, cities, country, dress).",
                        "3. Failure of Zairianization and economic kleptocracy.",
                        "4. Social crises (education, health, refugee displacement)."
                    ]
                }
            }
        ]
    },
    {
        "page_number": 16,
        "page_title": "Exam Coaching: Political Problems of Post-1960 Congo",
        "blocks": [
            {
                "block_type": "worked_example",
                "component_type": "worked_example",
                "title": "KCSE Question: State Five Political Problems That Faced the DRC Immediately After Independence in 1960 (5 Marks)",
                "content": {
                    "text": (
                        "**Examiner's Marking Scheme (1 Mark per distinct point):**\n\n"
                        "1. **Army Mutiny:** African soldiers mutinied against Belgian officers in the Force Publique days after independence. (1 mark)\n"
                        "2. **Secession of Mineral-Rich Provinces:** Moise Tshombe declared Katanga independent, while Albert Kalonji declared the secession of Kasai. (1 mark)\n"
                        "3. **Belgian Military Intervention:** Belgium sent paratroopers back to Congo without government consent, violating sovereignty. (1 mark)\n"
                        "4. **Ideological Rivalry Between Leaders:** Bitter power struggle between President Kasavubu (capitalist/federalist) and Prime Minister Lumumba (socialist/unitary). (1 mark)\n"
                        "5. **Assassination of Patrice Lumumba:** Polarized the country and intensified civil warfare. (1 mark)"
                    )
                }
            }
        ]
    }
]

LESSON_3_PAGES = [
    {
        "page_number": 1,
        "page_title": "Country Case Study: Tanzania",
        "blocks": [
            {
                "block_type": "learning_goal",
                "component_type": "learning_goal",
                "title": "Lesson Objectives: Tanzania's Post-Independence Journey",
                "content": {
                    "text": (
                        "By the end of this lesson, you will be able to:\n"
                        "- Trace political stability in Tanzania, the 1964 Union of Tanganyika and Zanzibar, and the creation of CCM (1977)\n"
                        "- Analyze the 1967 Arusha Declaration, Ujamaa (Socialism and Self-Reliance), and Villagization\n"
                        "- Explain the economic collapse of Ujamaa (villagization resistance, Kagera War, oil shocks, EAC collapse)\n"
                        "- Evaluate Tanzania's social achievements, notably Kiswahili as a national unifier and high literacy rates"
                    )
                }
            },
            {
                "block_type": "definition_card",
                "component_type": "definition_card",
                "title": "Concept: Ujamaa",
                "content": {
                    "term": "Ujamaa (African Socialism and Self-Reliance)",
                    "definition": (
                        "The socio-economic and political policy formulated by President Julius Nyerere in the 1967 Arusha Declaration, "
                        "meaning 'familyhood', based on communal villagization, nationalization of major industries, and self-reliance."
                    )
                }
            }
        ]
    },
    {
        "page_number": 2,
        "page_title": "Political Developments: The 1964 Union and One-Party State",
        "blocks": [
            {
                "block_type": "concept_explanation",
                "component_type": "concept_explanation",
                "title": "From Tanganyika to the United Republic of Tanzania",
                "content": {
                    "text": (
                        "- **Tanganyika Independence (9 December 1961):** Led by **Julius Kambarage Nyerere** and TANU.\n"
                        "- **Zanzibar Revolution (January 1964):** Abeid Amani Karume led a revolution overthrew the Arab Sultanate.\n"
                        "- **The Act of Union (22 April 1964):** Nyerere and Karume signed the historic treaty merging Tanganyika and Zanzibar to form the **United Republic of Tanzania** (Nyerere as President, Karume as First Vice President).\n"
                        "- **Chama Cha Mapinduzi (CCM) (1977):** TANU merged with Zanzibar's Afro-Shirazi Party (ASP) to form CCM, cementing one-party unity."
                    )
                }
            },
            {
                "block_type": "suggested_image",
                "component_type": "suggested_image",
                "title": "President Julius Kambarage Nyerere (1977)",
                "content": {
                    "text": "President Julius Kambarage Nyerere (Mwalimu), founding father of Tanzania, who championed Ujamaa and forged national unity through Kiswahili.",
                    "url": "https://upload.wikimedia.org/wikipedia/commons/c/ce/Julius_Nyerere_1977.jpg",
                    "author": "Public Domain / Wikimedia Commons",
                    "licensing": "Public Domain",
                    "commons_page_url": "https://commons.wikimedia.org/wiki/File:Julius_Nyerere_1977.jpg"
                }
            }
        ]
    },
    {
        "page_number": 3,
        "page_title": "Historical Documentary: Julius Nyerere and Ujamaa",
        "blocks": [
            {
                "block_type": "suggested_video",
                "component_type": "suggested_video",
                "title": "Historical Documentary: The Story of Tanzania's Ujamaa Experiment",
                "content": {
                    "url": "https://www.youtube.com/watch?v=X8UHIRzLpuo",
                    "text": "Analyze the philosophical vision of Julius Nyerere, the Arusha Declaration of 1967, communal villagization, and the economic hurdles that faced Tanzania.",
                    "author": "The Geo Africa / African History",
                    "licensing": "Standard YouTube License"
                }
            }
        ]
    },
    {
        "page_number": 4,
        "page_title": "The Kagera War and Idi Amin's Defeat (1978–1979)",
        "blocks": [
            {
                "block_type": "concept_explanation",
                "component_type": "concept_explanation",
                "title": "Defending Sovereignty Against Idi Amin",
                "content": {
                    "text": (
                        "- **The Invasion:** In October 1978, Ugandan dictator **Idi Amin Dada** invaded and annexed Tanzania's Kagera Salient.\n"
                        "- **The Counter-Offensive:** Nyerere mobilized over 100,000 soldiers in the Tanzania People's Defence Force (TPDF) alongside Ugandan exiles.\n"
                        "- **Victory & Overthrow:** TPDF forces drove the Ugandan army out, captured Kampala in April 1979, and overthrew Idi Amin.\n"
                        "- **Economic Repercussions:** The war cost Tanzania over $500 million, severely depleting foreign reserves and bankrupting the state."
                    )
                }
            }
        ]
    },
    {
        "page_number": 5,
        "page_title": "The 1967 Arusha Declaration and the Three Pillars of Ujamaa",
        "blocks": [
            {
                "block_type": "comparison_table",
                "component_type": "comparison_table",
                "title": "The Three Foundational Pillars of Ujamaa",
                "content": {
                    "headers": ["Pillar Name", "Core Policy Mechanism", "Historical Outcome & Impact"],
                    "rows": [
                        ["1. Villagization (Ujamaa Villages)", "Relocating scattered rural families into planned communal villages to farm collectively and share amenities.", "Initial social amenities expanded, but forced villagization (Operation Vijiji, 1973) disrupted farming and caused food production to plunge."],
                        ["2. Nationalization of Major Industries", "State takeover of banks, insurance firms, export-import trade, sisal estates, and factories.", "Transferred economic power to Africans, but state parastatals suffered from undercapitalization and poor management."],
                        ["3. Self-Reliance & Rejection of Foreign Aid", "Emphasizing domestic hard work and agricultural labor over reliance on foreign loans.", "Preserved national sovereignty, but left the country vulnerable during droughts and global oil price shocks."]
                    ]
                }
            }
        ]
    },
    {
        "page_number": 6,
        "page_title": "Economic Challenges of Ujamaa and Liberalization",
        "blocks": [
            {
                "block_type": "step_process",
                "component_type": "step_process",
                "title": "Factors Leading to the Abandonment of Ujamaa",
                "content": {
                    "steps": [
                        "1. Peasant Resistance to Forced Villagization: Farmers resented communal farming and lack of individual profit incentives, leading to lower crop yields.",
                        "2. Severe Droughts and Food Deficits: Recurring droughts turned Tanzania from a food exporter into a nation dependent on imported grain.",
                        "3. The 1973 & 1979 Global Oil Crises: Soaring crude oil import costs drained scarce foreign exchange reserves.",
                        "4. Collapse of the East African Community (1977): Ideological rifts with capitalist Kenya closed Tanzania's largest regional export market.",
                        "5. Crushing Cost of the Kagera War (1978-1979): Expelling Idi Amin depleted over $500M from the national treasury.",
                        "6. Economic Reforms under President Mwinyi (1985): Ali Hassan Mwinyi accepted IMF/World Bank SAPs, liberalizing trade and privatizing state parastatals."
                    ]
                }
            }
        ]
    },
    {
        "page_number": 7,
        "page_title": "Social Achievements: Kiswahili and High Literacy",
        "blocks": [
            {
                "block_type": "concept_explanation",
                "component_type": "concept_explanation",
                "title": "Nation-Building and Eradication of Tribalism",
                "content": {
                    "text": (
                        "Tanzania's post-independence social achievements are considered its greatest triumph:\n\n"
                        "- **Kiswahili as a National Unifier:** Nyerere mandated Kiswahili as the sole national and official language in government, schools, and media. This completely eradicated tribalism, making Tanzania the most cohesive nation in Africa.\n"
                        "- **Massive Literacy Campaigns:** Free primary education was introduced in 1977 and made compulsory in 1978. By 1985, adult literacy exceeded **85%**, the highest in East and Central Africa.\n"
                        "- **Rural Health Clinics:** Built thousands of rural dispensaries and mother-child health centers."
                    )
                }
            }
        ]
    },
    {
        "page_number": 8,
        "page_title": "Nyerere's Retirement and Multi-Party Return (1985–1992)",
        "blocks": [
            {
                "block_type": "concept_explanation",
                "component_type": "concept_explanation",
                "title": "Voluntary Transfer of Power and Pluralism",
                "content": {
                    "text": (
                        "- **Nyerere’s Voluntary Retirement (1985):** In a rare move for African heads of state, Julius Nyerere voluntarily stepped down in 1985, succeeded peacefully by **Ali Hassan Mwinyi**.\n"
                        "- **Return of Multi-Party Democracy (1992):** In 1992, Parliament amended the constitution to legalize opposition parties.\n"
                        "- **Subsequent Democratic Transfers:** Mwinyi was succeeded by Benjamin Mkapa (1995–2005) in multi-party polls, followed by Jakaya Kikwete (2005–2015), maintaining an unbroken record of peaceful transitions."
                    )
                }
            }
        ]
    },
    {
        "page_number": 9,
        "page_title": "Comparison: Political Stability in Tanzania vs. DRC",
        "blocks": [
            {
                "block_type": "comparison_table",
                "component_type": "comparison_table",
                "title": "Why Did Tanzania Remain Stable While the DRC Collapsed?",
                "content": {
                    "headers": ["Factor", "Tanzania", "Democratic Republic of Congo (Zaire)"],
                    "rows": [
                        ["National Language", "Universal adoption of Kiswahili created a unified national identity and eliminated tribalism.", "Lacked a single unifying national language, reinforcing regional ethnic blocs."],
                        ["Leadership Style", "Julius Nyerere lived modestly, promoted classless egalitarianism, and voluntarily retired in 1985.", "Mobutu Sese Seko operated a kleptocratic dictatorship, looting state revenues for personal luxury."],
                        ["Ethnic Demographics", "Over 120 small Bantu-speaking ethnic groups; no single tribe is large enough to dominate politics.", "Large, historically rival ethnic blocs (Bakongo, Baluba, Bangala) competed violently for state control."],
                        ["Military Discipline", "Rebuilt a disciplined, politically educated national army (TPDF) following the 1964 mutiny.", "Military mutinied immediately; soldiers were undisciplined, unpaid, and fragmented by tribal warlords."]
                    ]
                }
            }
        ]
    },
    {
        "page_number": 10,
        "page_title": "Interactive Classification: Tanzania Case Study",
        "blocks": [
            {
                "block_type": "mini_activity",
                "component_type": "mini_activity",
                "title": "Identify the Historical Policy or Event in Tanzania",
                "content": {
                    "instruction": "Match the event to its historical description:",
                    "items": [
                        "1. Policy document launching Ujamaa on 5 February 1967 -> **Arusha Declaration**",
                        "2. Revolutionary leader of Zanzibar who signed the 1964 Act of Union -> **Abeid Amani Karume**",
                        "3. Moving scattered rural farmers into collective communal villages -> **Villagization (Operation Vijiji)**",
                        "4. 1978–1979 war fought against Ugandan dictator Idi Amin -> **Kagera War**",
                        "5. President who liberalized trade and accepted IMF SAPs in 1985 -> **Ali Hassan Mwinyi**"
                    ]
                }
            }
        ]
    },
    {
        "page_number": 11,
        "page_title": "KCSE Examination Coaching: Achievements of Ujamaa",
        "blocks": [
            {
                "block_type": "worked_example",
                "component_type": "worked_example",
                "title": "KCSE Question: Explain Five Social and Economic Achievements of Ujamaa in Tanzania (10 Marks)",
                "content": {
                    "text": (
                        "**Model Answer (Point + Explanation = 2 Marks per Point):**\n\n"
                        "1. **Promotion of National Unity and Cohesion:** Grounded the nation in Kiswahili and communal familyhood (*Ujamaa*), successfully eliminating ethnic tribalism. (2 marks)\n\n"
                        "2. **Massive Increase in Literacy Rates:** Introduced free and compulsory primary education, driving adult literacy to over 85% by 1985. (2 marks)\n\n"
                        "3. **Expansion of Rural Healthcare:** Constructed thousands of dispensaries and health centers in planned Ujamaa villages, improving maternal and child health. (2 marks)\n\n"
                        "4. **Transfer of Economic Assets to Africans:** Nationalization took control of banks and sisal plantations from foreign colonial monopolies. (2 marks)\n\n"
                        "5. **Provision of Clean Water in Rural Areas:** Communal village settlements allowed the government to pipe water and sink boreholes for rural families. (2 marks)"
                    )
                }
            }
        ]
    },
    {
        "page_number": 12,
        "page_title": "KCSE Examination Coaching: Reasons for Tanzania's Stability",
        "blocks": [
            {
                "block_type": "worked_example",
                "component_type": "worked_example",
                "title": "KCSE Question: Explain Six Reasons Why Tanzania Maintained Political Stability After Independence (12 Marks)",
                "content": {
                    "text": (
                        "**Model Answer (Point + Explanation = 2 Marks per Point):**\n\n"
                        "1. **Adoption of Kiswahili as National Language:** Eliminated ethnic divisions and forged a shared national identity across all ethnic groups. (2 marks)\n\n"
                        "2. **Selfless Leadership of Julius Nyerere:** Nyerere prioritized national unity, lived modestly, and set a precedent by voluntarily retiring in 1985. (2 marks)\n\n"
                        "3. **Absence of Dominant Hostile Ethnic Groups:** Tanzania comprises over 120 small ethnic groups, none of which is large enough to monopolize power. (2 marks)\n\n"
                        "4. **Merger of TANU and ASP into CCM (1977):** Resolved mainland-Zanzibar political rivalries under a single unified ruling structure. (2 marks)\n\n"
                        "5. **Egalitarian Ujamaa Ideology:** Prevented extreme socio-economic class disparities that typically trigger civil strife. (2 marks)\n\n"
                        "6. **Professional Non-Partisan Military (TPDF):** Following the 1964 mutiny, the army was restructured and politically educated, preventing coups. (2 marks)"
                    )
                }
            }
        ]
    },
    {
        "page_number": 13,
        "page_title": "Check Your Understanding: Module 6.3",
        "blocks": [
            {
                "block_type": "knowledge_check",
                "component_type": "knowledge_check",
                "title": "Module 6.3 Assessment",
                "content": {
                    "questions": [
                        {
                            "question": "What treaty was signed on 22 April 1964 to create the United Republic of Tanzania?",
                            "options": [
                                "The Arusha Declaration",
                                "The Act of Union",
                                "The EAC Treaty",
                                "The Lancaster House Agreement"
                            ],
                            "correct_answer": 1,
                            "explanation": "The Act of Union signed by Julius Nyerere and Abeid Karume merged Tanganyika and Zanzibar."
                        },
                        {
                            "question": "Which of the following was a major factor in the collapse of Ujamaa in the 1980s?",
                            "options": [
                                "Discovery of massive oil reserves in Dodoma",
                                "Peasant resistance to forced villagization and the high cost of the Kagera War",
                                "Invasion by the Soviet Union",
                                "Rejection of the Kiswahili language"
                            ],
                            "correct_answer": 1,
                            "explanation": "Resistance to forced communal farming combined with the $500M Kagera War cost bankrupted the policy."
                        }
                    ]
                }
            }
        ]
    },
    {
        "page_number": 14,
        "page_title": "Lesson Summary & Key Takeaways",
        "blocks": [
            {
                "block_type": "summary",
                "component_type": "summary",
                "title": "Core Summary: The Tanzania Case Study",
                "content": {
                    "text": (
                        "• **Political Unification:** 1964 Act of Union merged Tanganyika and Zanzibar; TANU and ASP merged into CCM in 1977.\n"
                        "• **Ujamaa (1967 Arusha Declaration):** Villagization, nationalization, and self-reliance.\n"
                        "• **Economic Setbacks:** Collectivization failures, oil crises, Kagera War expenses, leading to 1985 SAP liberalization.\n"
                        "• **Social Triumph:** Kiswahili eradicated tribalism; adult literacy exceeded 85%; uninterrupted peaceful democratic transfers."
                    )
                }
            },
            {
                "block_type": "key_takeaway",
                "component_type": "key_takeaway",
                "title": "Key Takeaways",
                "content": {
                    "text": (
                        "- Tanzania succeeded in nation-building and ethnic cohesion through Kiswahili and ethical leadership.\n"
                        "- Economic collectivization failed due to human resistance to forced farming and external shocks."
                    )
                }
            }
        ]
    },
    {
        "page_number": 15,
        "page_title": "Revision Checklist: Tanzania Fundamentals",
        "blocks": [
            {
                "block_type": "step_process",
                "component_type": "step_process",
                "title": "Mastery Checklist",
                "content": {
                    "steps": [
                        "1. 1964 Act of Union and 1977 CCM formation.",
                        "2. Three pillars of the 1967 Arusha Declaration (Ujamaa).",
                        "3. Six causes of Ujamaa's economic collapse.",
                        "4. Six factors explaining Tanzania's exceptional political stability."
                    ]
                }
            }
        ]
    },
    {
        "page_number": 16,
        "page_title": "Quick Review: Nyerere's Legacy",
        "blocks": [
            {
                "block_type": "mini_activity",
                "component_type": "mini_activity",
                "title": "Quick Recall Quiz",
                "content": {
                    "instruction": "Answer true or false:",
                    "items": [
                        "1. Julius Nyerere voluntarily retired from the presidency in 1985 -> **True**",
                        "2. Tanzania fought the Kagera War against Kenya -> **False (fought against Uganda's Idi Amin)**",
                        "3. Multi-party democracy was reintroduced in Tanzania in 1992 -> **True**"
                    ]
                }
            }
        ]
    }
]

LESSON_4_PAGES = [
    {
        "page_number": 1,
        "page_title": "General Political, Economic, and Social Challenges in Africa",
        "blocks": [
            {
                "block_type": "learning_goal",
                "component_type": "learning_goal",
                "title": "Lesson Objectives: Continental Challenges Since Independence",
                "content": {
                    "text": (
                        "By the end of this lesson, you will be able to:\n"
                        "- Categorize the general political challenges that have plagued post-colonial Africa (coups, civil wars, border disputes, dictatorship)\n"
                        "- Analyze the core economic obstacles (neo-colonial dependency, unfavorable terms of trade, foreign debt, infrastructure gaps)\n"
                        "- Examine the pervasive social crises (population explosion, epidemics, refugee crisis, rapid urbanization and slums)\n"
                        "- Master examinable KCSE essay answering techniques for continental trends"
                    )
                }
            },
            {
                "block_type": "definition_card",
                "component_type": "definition_card",
                "title": "Concept: Continental Crisis Mapping",
                "content": {
                    "term": "Post-Colonial African Challenges",
                    "definition": (
                        "The shared set of political instabilities, economic dependencies, and social hurdles that have constrained "
                        "development across the African continent following the departure of European colonial powers."
                    )
                }
            }
        ]
    },
    {
        "page_number": 2,
        "page_title": "Educational Documentary: The Berlin Conference and African Borders",
        "blocks": [
            {
                "block_type": "suggested_video",
                "component_type": "suggested_video",
                "title": "Historical Documentary: The Berlin Conference and Modern African Border Conflicts",
                "content": {
                    "url": "https://www.youtube.com/watch?v=fy6YywL2AbQ",
                    "text": "Explore how the 1884–1885 partition of Africa created arbitrary frontiers that continue to fuel territorial disputes and civil wars across the continent.",
                    "author": "Legacy African History / Historical Analysis",
                    "licensing": "Standard YouTube License"
                }
            }
        ]
    },
    {
        "page_number": 3,
        "page_title": "General Political Challenges Across Africa",
        "blocks": [
            {
                "block_type": "step_process",
                "component_type": "step_process",
                "title": "Five Primary Political Crises",
                "content": {
                    "steps": [
                        "1. Political Instability & Military Coups: Over 70 military takeovers occurred between 1960 and 1985, replacing democratic constitutions with military juntas.",
                        "2. Devastating Civil and Ethnic Wars: Divide-and-rule colonial legacies sparked conflicts like the Biafran War in Nigeria (1967–1970), Angolan Civil War, and the 1994 Rwandan Genocide.",
                        "3. Chronic Border Disputes: Arbitrary Berlin borders split homogeneous communities, causing the Ogaden War, Ethiopia-Eritrea border war, and the Aouzou Strip conflict.",
                        "4. Rise of Authoritarian Dictatorships: Ruling elites banned opposition parties, established one-party states, and silenced critics through detention without trial.",
                        "5. Foreign Military Interference & Neo-Colonialism: Cold War superpowers and former colonizers staged coups and financed rebellions to safeguard mineral interests."
                    ]
                }
            }
        ]
    },
    {
        "page_number": 4,
        "page_title": "General Economic Challenges: Neo-Colonial Dependency",
        "blocks": [
            {
                "block_type": "concept_explanation",
                "component_type": "concept_explanation",
                "title": "The Traps of Underdevelopment",
                "content": {
                    "text": (
                        "Economic sovereignty proved far harder to achieve than political freedom:\n\n"
                        "- **Primary Commodity Dependence:** African states relied heavily on exporting unprocessed raw materials (coffee, cocoa, copper, oil) whose prices were dictated by Western markets.\n"
                        "- **Unfavorable Terms of International Trade:** Raw export prices remained low, while prices of imported machinery, fuel, and manufactured goods soared.\n"
                        "- **Crushing Foreign Debt Burden:** Massive borrowing from foreign governments and the World Bank/IMF created unsustainable debt servicing costs that drained national budgets.\n"
                        "- **Weak Industrial Bases:** Inadequate capital and skilled manpower left Africa reliant on expensive manufactured imports."
                    )
                }
            }
        ]
    },
    {
        "page_number": 5,
        "page_title": "Economic Challenges: Infrastructure and Climatic Shocks",
        "blocks": [
            {
                "block_type": "concept_explanation",
                "component_type": "concept_explanation",
                "title": "Transport Deficits, Droughts, and Corruption",
                "content": {
                    "text": (
                        "- **Extractive Transport Gaps:** Railways and roads were built solely to move minerals from the interior to coastal ports; virtually no regional transport connected neighboring states.\n"
                        "- **Recurring Droughts and Famine:** Severe droughts (Sahel crisis, Horn of Africa) crippled crop and livestock yields, forcing states to spend scarce foreign exchange on food aid.\n"
                        "- **Pervasive Corruption:** Embezzlement of public funds and capital flight to offshore tax havens deprived nations of developmental funds."
                    )
                }
            }
        ]
    },
    {
        "page_number": 6,
        "page_title": "General Social Challenges Across Africa",
        "blocks": [
            {
                "block_type": "step_process",
                "component_type": "step_process",
                "title": "Six Critical Social Hurdles",
                "content": {
                    "steps": [
                        "1. Population Explosion: Declining infant mortality caused populations to grow faster than classrooms, hospitals, and job creation.",
                        "2. Epidemics & Public Health Deficits: Heavy toll of HIV/AIDS, malaria, tuberculosis, cholera, and Ebola decimated the working-age population.",
                        "3. Refugee and Displacement Crises: Civil wars produced millions of internally displaced persons (IDPs) and refugees, straining host countries.",
                        "4. Rapid Urbanization and Slum Proliferation: Youth migrated to major cities, resulting in sprawling informal settlements lacking clean water and sanitation.",
                        "5. Persistent High Illiteracy: Inadequate educational budgets left millions of citizens without basic reading and vocational skills.",
                        "6. Gender Inequality and Cultural Barriers: Denial of equal property inheritance and secondary education to women restricted national productivity."
                    ]
                }
            }
        ]
    },
    {
        "page_number": 7,
        "page_title": "Summary Table: Continental Challenges (Political, Economic, Social)",
        "blocks": [
            {
                "block_type": "comparison_table",
                "component_type": "comparison_table",
                "title": "Master Synthesis of Post-Colonial Continental Challenges",
                "content": {
                    "headers": ["Domain", "Core Structural Problems", "Concrete Historical Examples"],
                    "rows": [
                        ["Political", "Military coups, ethnic civil wars, border disputes, authoritarian one-party regimes.", "Biafran War (Nigeria), Rwandan Genocide (1994), Mobutu dictatorship (Zaire), Ogaden War."],
                        ["Economic", "Unfavorable terms of trade, crushing debt, weak industry, extractive transport, droughts.", "Sahel famine, collapse of world cocoa/copper prices, World Bank SAP austerity programs."],
                        ["Social", "Population explosion, epidemics (HIV/AIDS), massive refugee crisis, slum growth.", "Great Lakes refugee crisis (mid-1990s), Kibera/Kinshasa slums, high youth unemployment."]
                    ]
                }
            }
        ]
    },
    {
        "page_number": 8,
        "page_title": "Interactive Classification: Political vs. Economic vs. Social",
        "blocks": [
            {
                "block_type": "mini_activity",
                "component_type": "mini_activity",
                "title": "Categorize the Continental Challenge",
                "content": {
                    "instruction": "Identify whether each challenge is Political, Economic, or Social:",
                    "items": [
                        "1. Military coups overthrowing elected governments -> **Political Challenge**",
                        "2. Low international market prices for raw agricultural exports -> **Economic Challenge**",
                        "3. Severe outbreak of the HIV/AIDS epidemic depleting the workforce -> **Social Challenge**",
                        "4. Heavy repayment of foreign debt to IMF and World Bank -> **Economic Challenge**",
                        "5. Sprawling urban slums resulting from rural-urban migration -> **Social Challenge**",
                        "6. Border warfare over arbitrary colonial partition lines -> **Political Challenge**"
                    ]
                }
            }
        ]
    },
    {
        "page_number": 9,
        "page_title": "KCSE Examination Coaching: Economic Challenges",
        "blocks": [
            {
                "block_type": "worked_example",
                "component_type": "worked_example",
                "title": "KCSE Question: Explain Six Economic Challenges That Have Faced African States Since Independence (12 Marks)",
                "content": {
                    "text": (
                        "**Model Answer (Point + Explanation = 2 Marks per Point):**\n\n"
                        "1. **Unfavorable Terms of International Trade:** African states export cheap primary raw commodities while importing expensive manufactured machinery, leading to chronic trade deficits. (2 marks)\n\n"
                        "2. **Crushing Foreign Debt Burden:** Heavy borrowing from Western nations and the IMF resulted in massive interest payments that consumed development budgets. (2 marks)\n\n"
                        "3. **Inadequate and Extractive Infrastructure:** Colonial rail and road networks only connected mines/plantations to ports, hindering inter-state African trade. (2 marks)\n\n"
                        "4. **Weak Industrial and Manufacturing Base:** Lack of domestic capital, heavy machinery, and technical expertise forced nations to depend on imported consumer goods. (2 marks)\n\n"
                        "5. **Unfavorable Climatic Conditions and Droughts:** Recurring droughts in the Sahel and Horn of Africa destroyed food crops, causing famine and forcing emergency grain imports. (2 marks)\n\n"
                        "6. **Widespread Corruption and Capital Flight:** Mismanagement and embezzlement by state officials drained treasuries and discouraged domestic investment. (2 marks)"
                    )
                }
            }
        ]
    },
    {
        "page_number": 10,
        "page_title": "KCSE Examination Coaching: Social Challenges",
        "blocks": [
            {
                "block_type": "worked_example",
                "component_type": "worked_example",
                "title": "KCSE Question: Explain Six Social Challenges That Have Hindered Development in Africa (12 Marks)",
                "content": {
                    "text": (
                        "**Model Answer (Point + Explanation = 2 Marks per Point):**\n\n"
                        "1. **Rapid Population Growth (Population Explosion):** High birth rates outpaced the expansion of schools, medical clinics, and employment opportunities. (2 marks)\n\n"
                        "2. **Prevalence of Epidemic Diseases:** HIV/AIDS, malaria, tuberculosis, and Ebola killed millions of economically productive citizens and strained healthcare systems. (2 marks)\n\n"
                        "3. **Massive Refugee and Displacement Crises:** Civil wars and ethnic clashes forced millions of people to flee into refugee camps, straining host country resources. (2 marks)\n\n"
                        "4. **Rapid Rural-Urban Migration and Slum Growth:** Lack of rural jobs drove youth into major cities, leading to overcrowded informal slums lacking sanitation and clean water. (2 marks)\n\n"
                        "5. **High Rates of Illiteracy:** Shortages of classrooms and teachers left millions of citizens illiterate and unable to participate effectively in modern industry. (2 marks)\n\n"
                        "6. **Gender Disparities and Cultural Obstacles:** Cultural practices denying girls secondary education and land inheritance rights limited the socio-economic contribution of women. (2 marks)"
                    )
                }
            }
        ]
    },
    {
        "page_number": 11,
        "page_title": "Case Study: The 1980s Structural Adjustment Programmes (SAPs)",
        "blocks": [
            {
                "block_type": "callout",
                "component_type": "callout",
                "title": "Historical Inquiry: The Impact of World Bank / IMF SAPs",
                "content": {
                    "text": (
                        "**Background:** In the 1980s, facing bankruptcy and debt defaults, dozens of African states were forced to accept **Structural Adjustment Programmes (SAPs)** from the World Bank and IMF.\n\n"
                        "**The Conditions:**\n"
                        "- Sashing government spending on education and healthcare (introducing 'cost-sharing' fees).\n"
                        "- Devaluing local currencies.\n"
                        "- Retrenching thousands of civil servants.\n"
                        "- Privatizing state-owned parastatals.\n\n"
                        "**Result:** While SAPs stabilized government deficits, they caused severe hardship for ordinary citizens, making basic medical care and school fees unaffordable for the poor."
                    )
                }
            }
        ]
    },
    {
        "page_number": 12,
        "page_title": "Check Your Understanding: Module 6.4",
        "blocks": [
            {
                "block_type": "knowledge_check",
                "component_type": "knowledge_check",
                "title": "Module 6.4 Assessment",
                "content": {
                    "questions": [
                        {
                            "question": "What is meant by 'unfavorable terms of trade' for developing African countries?",
                            "options": [
                                "African countries import only raw agricultural goods",
                                "The prices of primary raw exports remain low while the prices of imported manufactured goods and machinery continuously rise",
                                "African countries are prohibited from trading with neighboring states",
                                "All trade transactions must be conducted in gold bullion"
                            ],
                            "correct_answer": 1,
                            "explanation": "Unfavorable terms of trade occur when low-priced raw material exports buy fewer high-priced manufactured imports."
                        },
                        {
                            "question": "Which of the following was a direct consequence of the Structural Adjustment Programmes (SAPs) in the 1980s?",
                            "options": [
                                "Introduction of cost-sharing in public healthcare and schools",
                                "Immediate doubling of civil servant salaries",
                                "Abolition of all national taxes",
                                "Nationalization of all foreign commercial banks"
                            ],
                            "correct_answer": 0,
                            "explanation": "SAPs required governments to cut public subsidies, introducing cost-sharing fees for health and education."
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
                "title": "Core Summary: General Continental Challenges",
                "content": {
                    "text": (
                        "• **Political:** Over 70 coups (1960–1985), ethnic civil wars (Biafra, Rwanda Genocide), border conflicts (Ogaden, Badme), authoritarian single-party rule.\n"
                        "• **Economic:** Primary commodity dependency, unfavorable terms of trade, crushing foreign debt, weak industrial manufacturing, and extractive transport.\n"
                        "• **Social:** Population explosion, HIV/AIDS/Ebola epidemics, refugee crises, rural-urban migration, slums, and high illiteracy."
                    )
                }
            },
            {
                "block_type": "key_takeaway",
                "component_type": "key_takeaway",
                "title": "Key Takeaways",
                "content": {
                    "text": (
                        "- African states faced a shared matrix of inherited structural underdevelopment.\n"
                        "- Overcoming these challenges requires regional integration, economic diversification, and democratic governance."
                    )
                }
            }
        ]
    },
    {
        "page_number": 14,
        "page_title": "Revision Checklist: Continental Challenges",
        "blocks": [
            {
                "block_type": "step_process",
                "component_type": "step_process",
                "title": "Mastery Checklist",
                "content": {
                    "steps": [
                        "1. Five general political challenges.",
                        "2. Six general economic challenges.",
                        "3. Six general social challenges.",
                        "4. The impact of 1980s Structural Adjustment Programmes (SAPs)."
                    ]
                }
            }
        ]
    },
    {
        "page_number": 15,
        "page_title": "Discussion: Breaking the Raw Material Dependency Cycle",
        "blocks": [
            {
                "block_type": "callout",
                "component_type": "callout",
                "title": "Economic Reflection: Value Addition and Industrialization",
                "content": {
                    "text": (
                        "**Strategic Question:**\n"
                        "*> 'Why must African countries process their raw agricultural crops and minerals locally (value addition) before exporting them to international markets?'*\n\n"
                        "**Key Benefits:**\n"
                        "- Multiplies export earnings and generates foreign exchange.\n"
                        "- Creates millions of manufacturing jobs for unemployed youth.\n"
                        "- Insulates national budgets from global commodity price swings."
                    )
                }
            }
        ]
    },
    {
        "page_number": 16,
        "page_title": "Quick Knowledge Check: General Challenges",
        "blocks": [
            {
                "block_type": "mini_activity",
                "component_type": "mini_activity",
                "title": "Quick Recall Quiz",
                "content": {
                    "instruction": "Identify the challenge described:",
                    "items": [
                        "1. Devastating 1994 genocide in Central Africa resulting from ethnic division -> **Rwandan Genocide**",
                        "2. Economic condition where a country's debt servicing exceeds its development budget -> **Crushing Foreign Debt Burden**",
                        "3. Rapid growth of informal congested city settlements lacking water -> **Urban Slum Proliferation**"
                    ]
                }
            }
        ]
    }
]

LESSON_5_PAGES = [
    {
        "page_number": 1,
        "page_title": "African Responses, Development Measures, and Master Synthesis",
        "blocks": [
            {
                "block_type": "learning_goal",
                "component_type": "learning_goal",
                "title": "Lesson Objectives: Development Measures and Synthesis",
                "content": {
                    "text": (
                        "By the end of this lesson, you will be able to:\n"
                        "- Explain the key development measures and policy responses implemented by African governments to overcome post-colonial crises\n"
                        "- Analyze the role of regional economic integration (EAC, ECOWAS, COMESA, AU) in expanding trade\n"
                        "- Compare the developmental pathways of the DRC and Tanzania in a master synthesis\n"
                        "- Master comprehensive KCSE Paper 2 examination questions and marking schemes"
                    )
                }
            },
            {
                "block_type": "definition_card",
                "component_type": "definition_card",
                "title": "Concept: African Solutions to African Problems",
                "content": {
                    "term": "Developmental Responses",
                    "definition": (
                        "The strategic economic, political, and institutional initiatives—including regional trade integration, "
                        "economic diversification, democratic constitutional reforms, and universal education—enacted by African states to overcome underdevelopment."
                    )
                }
            }
        ]
    },
    {
        "page_number": 2,
        "page_title": "Educational Documentary: Regional Integration and the African Union",
        "blocks": [
            {
                "block_type": "suggested_video",
                "component_type": "suggested_video",
                "title": "Continental Analysis: The African Union and Regional Blocs in a Changing World",
                "content": {
                    "url": "https://www.youtube.com/watch?v=4vDCQzP15a0",
                    "text": "Examine how the African Union, ECOWAS, EAC, and other regional economic communities are working to tackle political instability and promote continental free trade.",
                    "author": "DW Africa / International Analysis",
                    "licensing": "Standard YouTube License"
                }
            }
        ]
    },
    {
        "page_number": 3,
        "page_title": "Five Major Development Measures Implemented by African States",
        "blocks": [
            {
                "block_type": "step_process",
                "component_type": "step_process",
                "title": "Key Strategies for Overcoming Post-Colonial Crises",
                "content": {
                    "steps": [
                        "1. Regional Economic Integration: Formed trading blocs (EAC, ECOWAS, COMESA, SADC, and AfCFTA) to dismantle colonial trade barriers, expand domestic markets, and reduce reliance on European manufactured imports.",
                        "2. Economic Diversification & Value Addition: Transitioned away from raw monoculture farming toward mineral processing, agro-processing, and tourism.",
                        "3. Democratic and Constitutional Reforms: The 1990s 'wind of change' repealed one-party laws, reintroduced multi-party democracy, and limited presidential terms.",
                        "4. National Language and Cultural Policies: Promoted indigenous national languages (such as Kiswahili in East Africa) to eliminate tribalism and foster national identity.",
                        "5. Massive Investment in Education and Healthcare: Expanded public universities, established free primary education programs, and invested in medical research."
                    ]
                }
            }
        ]
    },
    {
        "page_number": 4,
        "page_title": "Six Challenges Hindering Economic Integration in Africa",
        "blocks": [
            {
                "block_type": "step_process",
                "component_type": "step_process",
                "title": "Why Has Regional Integration Been Slow?",
                "content": {
                    "steps": [
                        "1. Poor Transport and Communication Links: Road and railway networks remain extractive toward ports rather than connecting neighboring states.",
                        "2. Commodity Similarity: Most African countries produce identical raw agricultural crops (tea, coffee) or minerals, limiting mutual trade volume.",
                        "3. Budgetary Deficits and Foreign Exchange Shortages: Inconvertible domestic currencies and lack of hard currency constrain cross-border commerce.",
                        "4. Political Instability and Civil Warfare: Armed conflicts disrupt transit corridors and divert resources to defense budgets.",
                        "5. Overlapping Memberships and Divided Loyalties: States belong to multiple competing trade blocs (e.g., EAC and SADC), creating conflicting tariff obligations.",
                        "6. Colonial Economic Ties: Many nations maintain preferential trade and monetary pacts with former colonial masters (e.g., France and CFA Franc zones)."
                    ]
                }
            }
        ]
    },
    {
        "page_number": 5,
        "page_title": "Master Comparison: Post-Colonial Trajectory of DRC vs. Tanzania",
        "blocks": [
            {
                "block_type": "comparison_table",
                "component_type": "comparison_table",
                "title": "Comprehensive Synthesis: Democratic Republic of Congo vs. Tanzania",
                "content": {
                    "headers": ["Dimension", "Democratic Republic of Congo (Zaire)", "United Republic of Tanzania"],
                    "rows": [
                        ["Colonial Power", "Belgium (Extractive, extreme neglect of African education)", "Great Britain (Indirect rule, Mandate/Trusteeship territory)"],
                        ["Founding Leaders", "Joseph Kasavubu (Pres) & Patrice Lumumba (PM)", "Julius Kambarage Nyerere (Mwalimu) & Abeid Karume"],
                        ["Political Stability", "Extreme instability, Katanga/Kasai secessions, 32-year Mobutu military dictatorship, civil wars.", "Exceptional stability, 1964 Act of Union, peaceful succession from Nyerere to Mwinyi in 1985."],
                        ["Economic Model", "Zairianization (1973), state kleptocracy, hyperinflation, collapsed infrastructure.", "Ujamaa (1967 Arusha Declaration), villagization, nationalization, SAP liberalization (1985)."],
                        ["Social Integration", "Persistent ethnic conflict, language fragmentation, education/health collapse.", "Universal Kiswahili eliminated tribalism; adult literacy exceeded 85% by 1985."]
                    ]
                }
            }
        ]
    },
    {
        "page_number": 6,
        "page_title": "Master KCSE Examination Paper 1 (Section B, 15 Marks)",
        "blocks": [
            {
                "block_type": "worked_example",
                "component_type": "worked_example",
                "title": "KCSE Question 1: Causes of Congo Crisis (3 Marks) & Tanzania's Stability (12 Marks)",
                "content": {
                    "text": (
                        "**(a) State three political causes of the Congo Crisis between 1960 and 1965 (3 marks):**\n"
                        "1. **The Army Mutiny:** African soldiers in the Force Publique mutinied against Belgian officers immediately after independence. (1 mark)\n"
                        "2. **Secession of Mineral-Rich Provinces:** Moise Tshombe seceded Katanga, while Albert Kalonji seceded Kasai. (1 mark)\n"
                        "3. **Assassination of Patrice Lumumba:** The deposition and murder of Prime Minister Lumumba in January 1961 polarized the nation. (1 mark)\n\n"
                        "**(b) Explain six reasons why Tanzania maintained political stability and national unity (12 marks):**\n"
                        "1. **Adoption of Kiswahili as National Language:** Eliminated ethnic divisions and built a strong national identity. (2 marks)\n"
                        "2. **Selfless Leadership of Julius Nyerere:** Prioritized national unity, lived modestly, and retired voluntarily in 1985. (2 marks)\n"
                        "3. **Merger of TANU and ASP into CCM (1977):** Unified mainland and Zanzibar under a single political structure. (2 marks)\n"
                        "4. **Egalitarian Ujamaa Philosophy:** Focused on classless familyhood, preventing extreme wealth disparities. (2 marks)\n"
                        "5. **Absence of Dominant Hostile Ethnic Groups:** Over 120 small Bantu groups prevented any single tribe from dominating politics. (2 marks)\n"
                        "6. **Professional Non-Partisan Military (TPDF):** Rebuilt following the 1964 mutiny, preventing military coups. (2 marks)"
                    )
                }
            }
        ]
    },
    {
        "page_number": 7,
        "page_title": "Master KCSE Examination Paper 2 (Section B, 15 Marks)",
        "blocks": [
            {
                "block_type": "worked_example",
                "component_type": "worked_example",
                "title": "KCSE Question 2: Regional Organizations (3 Marks) & Challenges to Integration (12 Marks)",
                "content": {
                    "text": (
                        "**(a) Name three regional economic organizations formed in Africa to promote cooperation (3 marks):**\n"
                        "1. The East African Community (EAC). (1 mark)\n"
                        "2. The Economic Community of West African States (ECOWAS). (1 mark)\n"
                        "3. The Common Market for Eastern and Southern Africa (COMESA). (1 mark)\n\n"
                        "**(b) Explain six challenges that have hindered economic integration in Africa (12 marks):**\n"
                        "1. **Poor Transport and Communication Networks:** Extractive colonial roads and railways connect to ports rather than neighboring states. (2 marks)\n"
                        "2. **Similarity of Export Commodities:** Member states produce identical raw crops (tea, coffee) or minerals, limiting mutual trade. (2 marks)\n"
                        "3. **Foreign Exchange and Currency Inconvertibility:** Shortages of hard currency impede interstate transactions. (2 marks)\n"
                        "4. **Political Instability and Civil Conflicts:** Wars disrupt transport corridors and destroy regional infrastructure. (2 marks)\n"
                        "5. **Overlapping Memberships and Divided Loyalties:** Belonging to multiple competing blocs (COMESA, EAC, SADC) causes conflicting tariff policies. (2 marks)\n"
                        "6. **Colonial Economic Ties:** Preferential trade and monetary agreements with former colonizers weaken inter-African economic solidarity. (2 marks)"
                    )
                }
            }
        ]
    },
    {
        "page_number": 8,
        "page_title": "Interactive Master Classification Activity",
        "blocks": [
            {
                "block_type": "mini_activity",
                "component_type": "mini_activity",
                "title": "Assign the Concept to DRC or Tanzania",
                "content": {
                    "instruction": "Test your comparative mastery across the two country case studies:",
                    "items": [
                        "1. 1967 Arusha Declaration and Villagization -> **Tanzania**",
                        "2. Zairianization (1973) and Authenticity Programme -> **DRC (Zaire)**",
                        "3. 1964 Act of Union merging Tanganyika and Zanzibar -> **Tanzania**",
                        "4. Assassination of Prime Minister Patrice Lumumba in 1961 -> **DRC**",
                        "5. Voluntary retirement of the President in 1985 -> **Tanzania (Julius Nyerere)**",
                        "6. AFDL rebellion led by Laurent-Désiré Kabila in 1997 -> **DRC**"
                    ]
                }
            }
        ]
    },
    {
        "page_number": 9,
        "page_title": "Topic 6 Comprehensive Mastery Check (Part 1)",
        "blocks": [
            {
                "block_type": "knowledge_check",
                "component_type": "knowledge_check",
                "title": "Topic 6 Mastery Assessment (Part 1)",
                "content": {
                    "questions": [
                        {
                            "question": "What was the main reason why the 'Zairianization' policy failed in the DRC in 1973?",
                            "options": [
                                "Businesses were handed to inexperienced political cronies who looted capital and mismanaged operations",
                                "The United Nations imposed economic sanctions on Zaire",
                                "Belgium refused to purchase Congolese minerals",
                                "The population refused to use the Zaire currency"
                            ],
                            "correct_answer": 0,
                            "explanation": "Zairianization failed because nationalized enterprises were allocated to political cronies lacking business expertise."
                        },
                        {
                            "question": "Which national policy in Tanzania is credited with completely eradicating tribalism and forging national unity?",
                            "options": [
                                "Forced villagization under Operation Vijiji",
                                "The adoption of Kiswahili as the sole national and official language in government and schools",
                                "The 1978–1979 Kagera War",
                                "The introduction of IMF Structural Adjustment Programmes"
                            ],
                            "correct_answer": 1,
                            "explanation": "Universal adoption of Kiswahili eliminated ethnic divisions and created a shared national identity."
                        }
                    ]
                }
            }
        ]
    },
    {
        "page_number": 10,
        "page_title": "Topic 6 Comprehensive Mastery Check (Part 2)",
        "blocks": [
            {
                "block_type": "knowledge_check",
                "component_type": "knowledge_check",
                "title": "Topic 6 Mastery Assessment (Part 2)",
                "content": {
                    "questions": [
                        {
                            "question": "Why does the similarity of primary export commodities hinder trade between African states?",
                            "options": [
                                "African states are legally prohibited from trading raw commodities",
                                "Countries producing the same agricultural crops (like coffee or tea) have little need to import them from each other",
                                "All commodities must be inspected by the African Union",
                                "African countries do not possess commercial ports"
                            ],
                            "correct_answer": 1,
                            "explanation": "When neighboring countries produce identical primary goods, there is minimal demand to trade between them."
                        },
                        {
                            "question": "Which 1978–1979 war cost Tanzania over $500 million, leading to severe economic exhaustion?",
                            "options": [
                                "The Biafran War",
                                "The Kagera War against Idi Amin's Uganda",
                                "The Shaba Rebellions",
                                "The Ogaden War"
                            ],
                            "correct_answer": 1,
                            "explanation": "The Kagera War against Idi Amin cost Tanzania over $500M, exhausting foreign exchange reserves."
                        }
                    ]
                }
            }
        ]
    },
    {
        "page_number": 11,
        "page_title": "Topic 6 Comprehensive Master Summary",
        "blocks": [
            {
                "block_type": "summary",
                "component_type": "summary",
                "title": "Topic 6 Master Summary: Developments and Challenges in Africa",
                "content": {
                    "text": (
                        "• **Inherited Colonial Crises:** Technocrat shortages, divide-and-rule animosity, arbitrary Berlin borders, and extractive export economies.\n"
                        "• **DRC Case Study:** 1960 Congo Crisis, Katanga secession, Lumumba's 1961 assassination, Mobutu's 32-year kleptocracy, Authenticity (1971), Zairianization failure (1973), AFDL overthrow by Laurent Kabila (1997).\n"
                        "• **Tanzania Case Study:** 1964 Act of Union, CCM (1977), 1967 Arusha Declaration (Ujamaa), Kagera War (1978–1979), Nyerere's 1985 voluntary retirement, Kiswahili national cohesion, 85%+ literacy.\n"
                        "• **General Challenges:** Over 70 military coups (1960–1985), civil wars (Biafra, Rwanda), unfavorable terms of trade, crushing debt, epidemics (HIV/AIDS), refugee crises.\n"
                        "• **Responses:** Regional economic integration (EAC, ECOWAS, COMESA, AfCFTA), economic diversification, 1990s democratic reforms."
                    )
                }
            }
        ]
    },
    {
        "page_number": 12,
        "page_title": "Topic 6 Final Exam Revision Checklist",
        "blocks": [
            {
                "block_type": "step_process",
                "component_type": "step_process",
                "title": "Exam Revision Checklist: Topic 6",
                "content": {
                    "steps": [
                        "1. Post-colonial inherited problems and Cold War proxy impacts.",
                        "2. DRC: Kasavubu, Lumumba, Tshombe, Mobutu, Zairianization, Authenticity, Laurent Kabila.",
                        "3. Tanzania: Nyerere, Karume, Act of Union 1964, Ujamaa pillars, Kagera War, Kiswahili unifier.",
                        "4. Continental trends: Causes of coups, economic terms of trade, foreign debt, social refugee crises.",
                        "5. Regional integration: 6 challenges hindering continental economic cooperation."
                    ]
                }
            }
        ]
    },
    {
        "page_number": 13,
        "page_title": "Exam Coaching: Command Words in Topic 6",
        "blocks": [
            {
                "block_type": "callout",
                "component_type": "callout",
                "title": "Mastering KCSE History Command Words",
                "content": {
                    "text": (
                        "**Examiner's Advice:**\n"
                        "- **'State' / 'Identify' / 'Name' (1 mark per point):** Write concise, direct points without lengthy prose (e.g., *Name three regional economic bodies in Africa: EAC, ECOWAS, COMESA*).\n"
                        "- **'Explain' / 'Discuss' (2 marks per point):** Apply the **Point + Explanation + Evidence** formula (e.g., *Explain why Ujamaa failed economically: Peasant resistance to forced villagization + disrupted agricultural seasons + food production dropped drastically*)."
                    )
                }
            }
        ]
    },
    {
        "page_number": 14,
        "page_title": "The African Continental Free Trade Area (AfCFTA)",
        "blocks": [
            {
                "block_type": "concept_explanation",
                "component_type": "concept_explanation",
                "title": "Modern Continental Economic Integration",
                "content": {
                    "text": (
                        "- **The AfCFTA Milestone (2018):** Established by the African Union, creating the largest free trade area in the world by number of participating countries.\n"
                        "- **Objective:** Eliminate tariffs on 90% of goods, harmonize customs rules, and increase intra-African trade from 15% to over 50%.\n"
                        "- **Significance:** Represents the modern culmination of Pan-African economic self-reliance envisioned by early nationalist leaders."
                    )
                }
            }
        ]
    },
    {
        "page_number": 15,
        "page_title": "Final Mastery Challenge: Key Historical Figures",
        "blocks": [
            {
                "block_type": "mini_activity",
                "component_type": "mini_activity",
                "title": "Match the Leader to Their Historical Legacy",
                "content": {
                    "instruction": "Test your mastery of post-independence African leaders:",
                    "items": [
                        "1. First Prime Minister of Congo, assassinated in 1961 -> **Patrice Lumumba**",
                        "2. Architect of Ujamaa who voluntarily retired in 1985 -> **Julius Kambarage Nyerere**",
                        "3. Military dictator who ruled Zaire for 32 years under Authenticity -> **Mobutu Sese Seko**",
                        "4. President of Zanzibar who signed the 1964 Act of Union -> **Abeid Amani Karume**",
                        "5. Rebel leader who ousted Mobutu in 1997 and renamed DRC -> **Laurent-Désiré Kabila**"
                    ]
                }
            }
        ]
    },
    {
        "page_number": 16,
        "page_title": "Check Your Knowledge: Final Exam Warmup",
        "blocks": [
            {
                "block_type": "knowledge_check",
                "component_type": "knowledge_check",
                "title": "Final Topic 6 Warmup Check",
                "content": {
                    "questions": [
                        {
                            "question": "Which country experienced the Biafran Civil War (1967–1970) as a result of post-colonial ethnic divisions?",
                            "options": [
                                "Ghana",
                                "Nigeria",
                                "Tanzania",
                                "Zambia"
                            ],
                            "correct_answer": 1,
                            "explanation": "The Biafran War was fought in Nigeria following the secession attempt by the Igbo-dominated eastern region."
                        },
                        {
                            "question": "What is the primary objective of the African Continental Free Trade Area (AfCFTA)?",
                            "options": [
                                "To eliminate tariffs on intra-African trade and create a unified single continental market",
                                "To replace all African currencies with the US Dollar",
                                "To merge all African armies into a single military force",
                                "To ban all trade with European nations"
                            ],
                            "correct_answer": 0,
                            "explanation": "AfCFTA aims to eliminate tariffs and establish a single continental market for goods and services."
                        }
                    ]
                }
            }
        ]
    },
    {
        "page_number": 17,
        "page_title": "Grand Summary: Topics 1–6 Review",
        "blocks": [
            {
                "block_type": "summary",
                "component_type": "summary",
                "title": "Comprehensive Synthesis: Form 4 History (Topics 1 to 6)",
                "content": {
                    "text": (
                        "• **Topic 1 (The World War):** WWI & WWII origins, course, Allied victory, League of Nations & UN founding.\n"
                        "• **Topic 2 (International Relations):** UN, Commonwealth, Non-Aligned Movement (NAM), Cold War superpowers & collapse.\n"
                        "• **Topic 3 (Co-operation in Africa):** Pan-Africanism, Manchester 1945, OAU founding 1963, African Union 2002, EAC, ECOWAS, COMESA.\n"
                        "• **Topic 4 (National Philosophies):** African Socialism (Sessional Paper 10), Harambee (Kenyatta 1963), Nyayoism (Moi 1978).\n"
                        "• **Topic 5 (Developments in Kenya):** Political centralization (1964–1982), return of multipartyism (1991), 2010 Constitution & Devolution.\n"
                        "• **Topic 6 (Developments in Africa):** Inherited crises, DRC Congo Crisis & Mobutu kleptocracy, Tanzania Ujamaa & Kiswahili, continental challenges."
                    )
                }
            }
        ]
    },
    {
        "page_number": 18,
        "page_title": "KCSE Examination Final Tip Sheet",
        "blocks": [
            {
                "block_type": "step_process",
                "component_type": "step_process",
                "title": "Top Examination Tips for KCSE History Paper 2",
                "content": {
                    "steps": [
                        "1. Always identify whether the question asks about a specific country (DRC or Tanzania) or general Africa.",
                        "2. Structure essays with clear Point-Explanation-Evidence format for full marks.",
                        "3. In questions asking for causes of stability in Tanzania, emphasize Kiswahili, Nyerere's leadership, and ethnic balance.",
                        "4. In questions on the DRC, cite the 1960 army mutiny, Katanga secession, Lumumba's assassination, and Mobutu's kleptocracy.",
                        "5. Distinguish between political, economic, and social categories to ensure broad point coverage."
                    ]
                }
            }
        ]
    }
]


ALL_LESSONS = [
    {
        "unit_order": 1,
        "unit_name": "The Post-Colonial Political and Economic Inheritance",
        "lesson_title": "The Post-Colonial Inheritance: Inherited Crises, Cold War, and Military Coups",
        "pages": LESSON_1_PAGES
    },
    {
        "unit_order": 2,
        "unit_name": "Country Case Study — The Democratic Republic of Congo (Zaire)",
        "lesson_title": "The Democratic Republic of Congo: The Congo Crisis, Mobutu's Dictatorship, and Turmoil",
        "pages": LESSON_2_PAGES
    },
    {
        "unit_order": 3,
        "unit_name": "Country Case Study — Tanzania",
        "lesson_title": "Tanzania: The 1964 Union, Ujamaa Socialism, National Unity, and Political Stability",
        "pages": LESSON_3_PAGES
    },
    {
        "unit_order": 4,
        "unit_name": "General Political, Economic, and Social Challenges in Africa",
        "lesson_title": "General Political, Economic, and Social Challenges in Post-Colonial Africa",
        "pages": LESSON_4_PAGES
    },
    {
        "unit_order": 5,
        "unit_name": "African Responses and Development Measures",
        "lesson_title": "African Responses, Development Measures, Regional Integration, and Master Synthesis",
        "pages": LESSON_5_PAGES
    }
]


# ===========================================================================
# DATABASE INGESTION RUNNER
# ===========================================================================

def run_ingestion(replace=False):
    print("=" * 80)
    print("VLEARN CURRICULUM INGESTION: FORM 4 HISTORY — TOPIC 6 (DEVELOPMENTS IN AFRICA)")
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
            name="Social, Economic and Political Developments and Challenges in Africa Since Independence",
            defaults={"order": 6}
        )
        if topic_created:
            print(f"[+] Created Topic: {topic.name} (Order: {topic.order})")
        else:
            topic.order = 6
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
        print(f"[SUCCESS] Form 4 History Topic 6 Ingestion Complete!")
        print(f"[*] Total Lessons Ingested: {len(ALL_LESSONS)}")
        print(f"[*] Total Pages Ingested:   {total_pages}")
        print(f"[*] Total Blocks Ingested:  {total_blocks}")
        print(f"[*] Total Media Assets:     {total_assets}")
        print("=" * 80)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Ingest Form 4 History Topic 6")
    parser.add_argument("--replace", action="store_true", help="Replace existing blocks with a fresh rebuild")
    args = parser.parse_args()

    run_ingestion(replace=args.replace)
