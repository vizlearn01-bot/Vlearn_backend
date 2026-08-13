"""
VLearn Curriculum Ingestion Engine: Form 4 History — Topic 4 (National Philosophies in Kenya)

Target Subject: History (Subject ID: 17)
Grade: Form 4 (Grade ID: 4)
Curriculum: 844 (Curriculum ID: 4)

Topic 4: National Philosophies (Kenya) (Order: 4)
  - Unit 1: African Socialism — Meaning, Origin, and Features (Lesson 1: 15 Pages)
  - Unit 2: Harambee Philosophy — Meaning, Principles, and Categories (Lesson 2: 15 Pages)
  - Unit 3: Harambee's Contributions and Challenges (Lesson 3: 15 Pages)
  - Unit 4: Nyayo Philosophy — Origins, Pillars, and Sources (Lesson 4: 16 Pages)
  - Unit 5: Cumulative Impact and Synthesis of National Philosophies (Lesson 5: 18 Pages)

Total: 5 Learning Units, 5 Lessons, 79 Pages, 100+ Blocks, 10 Media Assets (5 Wikimedia Photos + 5 Verified YouTube Videos)

Usage:
  ./venv/bin/python curriculum/ingest_form4_history_topic4.py --replace
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
# LESSON DEFINITIONS: FORM 4 HISTORY TOPIC 4
# ===========================================================================

LESSON_1_PAGES = [
    {
        "page_number": 1,
        "page_title": "Introduction to National Philosophies and African Socialism",
        "blocks": [
            {
                "block_type": "learning_goal",
                "component_type": "learning_goal",
                "title": "Lesson Objectives: African Socialism",
                "content": {
                    "text": (
                        "By the end of this lesson, you will be able to:\n"
                        "- Define the concept of a national philosophy and understand why young nations require ideological blueprints\n"
                        "- Trace the historical context and origin of African Socialism in post-independence Kenya\n"
                        "- Identify the significance of Sessional Paper No. 10 of 1965\n"
                        "- Analyze the core pillars, features, and mixed economy model of African Socialism\n"
                        "- Evaluate the major achievements and challenges encountered in implementing African Socialism"
                    )
                }
            },
            {
                "block_type": "definition_card",
                "component_type": "definition_card",
                "title": "Definition: National Philosophy",
                "content": {
                    "term": "National Philosophy",
                    "definition": (
                        "A set of ideological beliefs, principles, and values championed by a country's leadership that becomes widely accepted "
                        "within a nation's geographical boundary to guide governance, foster national unity, and steer socio-economic development."
                    )
                }
            }
        ]
    },
    {
        "page_number": 2,
        "page_title": "The Post-Independence Dilemma: The 'Three Primary Evils'",
        "blocks": [
            {
                "block_type": "concept_explanation",
                "component_type": "concept_explanation",
                "title": "Poverty, Disease, and Ignorance: The Challenges of 1963",
                "content": {
                    "text": (
                        "Upon attaining independence on 12 December 1963, the young Kenyan republic inherited profound structural crises:\n\n"
                        "- **The Three Primary Evils:** The government declared war against **poverty, disease, and ignorance**.\n"
                        "- **Rejecting Western Capitalism:** Unbridled capitalism was rejected because it was perceived as individualistic, exploitative, and alien to African communal culture.\n"
                        "- **Rejecting Eastern Communism:** State communism was rejected because it severely curtailed personal liberties, private initiative, and freedom of worship.\n"
                        "- **The Third Way:** Kenya needed an authentic, home-grown socio-economic blueprint anchored in traditional African values while applying modern economic planning."
                    )
                }
            }
        ]
    },
    {
        "page_number": 3,
        "page_title": "Sessional Paper No. 10 of 1965",
        "blocks": [
            {
                "block_type": "concept_explanation",
                "component_type": "concept_explanation",
                "title": "The Foundational Economic Charter of Independent Kenya",
                "content": {
                    "text": (
                        "African Socialism was formally codified in **Sessional Paper No. 10 of 1965**, entitled *'African Socialism and its Application to Planning in Kenya'*.\n\n"
                        "- **Architects:** Drafted under the visionary leadership of Minister for Economic Planning and Development **Tom Mboya**, and championed by President **Mzee Jomo Kenyatta**.\n"
                        "- **Adoption:** Unanimously adopted by the Kenyan Parliament in 1965 as the official national planning blueprint.\n"
                        "- **Core Mandate:** Designed to build an egalitarian, democratic, and prosperous society free from racial discrimination, economic exploitation, and extreme poverty."
                    )
                }
            },
            {
                "block_type": "suggested_image",
                "component_type": "suggested_image",
                "title": "Tom Mboya, Architect of Sessional Paper No. 10",
                "content": {
                    "text": "Tom Mboya, Minister for Economic Planning and Development, who guided the drafting of Sessional Paper No. 10 of 1965.",
                    "url": "https://upload.wikimedia.org/wikipedia/commons/8/89/Tom_Mboya_1962_%28cropped%29.jpg",
                    "author": "Public Domain / Wikimedia Commons",
                    "licensing": "Public Domain",
                    "commons_page_url": "https://commons.wikimedia.org/wiki/File:Tom_Mboya_1962_(cropped).jpg"
                }
            }
        ]
    },
    {
        "page_number": 4,
        "page_title": "Historical Documentary: Tom Mboya and Early Nation Planning",
        "blocks": [
            {
                "block_type": "suggested_video",
                "component_type": "suggested_video",
                "title": "Historical Documentary: The Legacy of Tom Mboya and Early Nation Planning",
                "content": {
                    "url": "https://www.youtube.com/watch?v=WbrBNiH1D84",
                    "text": "Examine the political and intellectual career of Tom Mboya, the drafting of Sessional Paper No. 10 of 1965, and the economic vision of post-independence Kenya.",
                    "author": "254 Crime Tapes / Historical Documentary",
                    "licensing": "Standard YouTube License"
                }
            }
        ]
    },
    {
        "page_number": 5,
        "page_title": "Two Traditional African Pillars of African Socialism",
        "blocks": [
            {
                "block_type": "comparison_table",
                "component_type": "comparison_table",
                "title": "Foundational Pillars of African Socialism",
                "content": {
                    "headers": ["Pillar Name", "Traditional Cultural Meaning", "Application in Modern Statecraft"],
                    "rows": [
                        ["Political Democracy", "In pre-colonial Africa, elders deliberated openly in councils without hereditary caste oppression.", "Guarantees all citizens equal political rights, universal voting suffrage, freedom of expression, and protection under the rule of law."],
                        ["Mutual Social Responsibility", "Traditional communalism where individuals served the welfare of the extended clan, ensuring no member starved.", "Demands that personal wealth creation must contribute directly to the collective good of society through taxes, patriotism, and community service."]
                    ]
                }
            }
        ]
    },
    {
        "page_number": 6,
        "page_title": "The Six Core Features of African Socialism",
        "blocks": [
            {
                "block_type": "step_process",
                "component_type": "step_process",
                "title": "Examinable Features of African Socialism in Kenya",
                "content": {
                    "steps": [
                        "1. Political Democracy: Every citizen has equal voting rights and political representation, free from tribal, religious, or racial discrimination.",
                        "2. Mutual Social Responsibility: The state and individuals share a mutual duty of care; wealth must serve the broader public interest.",
                        "3. Various Forms of Ownership (Mixed Economy): Encourages private ownership of property alongside state-owned parastatals and joint-venture enterprises.",
                        "4. Range of Government Controls: The state retains the legal right to regulate, supervise, and control how property and land are utilized.",
                        "5. Progressive Taxation: Implementing a graduated income tax where higher earners pay higher rates, funding free primary amenities for the poor.",
                        "6. Diffusion of Ownership: Promoting broad-based business ownership via cooperative societies and public listing to prevent wealth monopolization."
                    ]
                }
            }
        ]
    },
    {
        "page_number": 7,
        "page_title": "The 'Mixed Economy' Model Explained",
        "blocks": [
            {
                "block_type": "concept_explanation",
                "component_type": "concept_explanation",
                "title": "Balancing Private Enterprise and State Ownership",
                "content": {
                    "text": (
                        "Under African Socialism, Kenya adopted a pragmatic **mixed economy**:\n\n"
                        "- **Private Enterprise:** Encouraged private capital investment, entrepreneurship, and foreign direct investment.\n"
                        "- **State Parastatals:** The government established strategic state corporations (e.g., Kenya Railways, Kenya Power, KPC, Kenya Commercial Bank) in essential sectors.\n"
                        "- **Cooperative Societies:** Allowed millions of small-scale farmers to pool agricultural harvests (coffee, tea, dairy, pyrethrum) to access collective loans and competitive overseas markets."
                    )
                }
            }
        ]
    },
    {
        "page_number": 8,
        "page_title": "Major Achievements of African Socialism",
        "blocks": [
            {
                "block_type": "step_process",
                "component_type": "step_process",
                "title": "Seven Major Accomplishments of African Socialism",
                "content": {
                    "steps": [
                        "1. Democratic Governance Foundations: Established the constitutional framework for political participation and multi-party democracy.",
                        "2. Preservation of African Culture: Grounded national planning in indigenous African traditions and values, restoring cultural dignity.",
                        "3. Fostering National Unity: Emphasized that all Kenyans belonged to one national family, bridging regional and ethnic divisions.",
                        "4. Redistribution via Progressive Tax: Generated tax revenue redistributed to build rural schools, health clinics, and roads.",
                        "5. Rapid Growth of Agricultural Cooperatives: Enabled millions of small-scale farmers to form marketing cooperatives (KTDA, KCC, KPCU).",
                        "6. Groundwork for the Harambee Movement: Inspired local communities to initiate collective self-help infrastructure projects.",
                        "7. Africanisation of the Economy: Channeled state loans through the ICDC and KCB to transfer retail trade from Europeans/Asians to indigenous Kenyans."
                    ]
                }
            }
        ]
    },
    {
        "page_number": 9,
        "page_title": "Africanisation of the Economy Case Study",
        "blocks": [
            {
                "block_type": "concept_explanation",
                "component_type": "concept_explanation",
                "title": "Transferring Economic Power to Indigenous Citizens",
                "content": {
                    "text": (
                        "Prior to 1963, retail trade, banking, and commercial farming were completely monopolized by European settlers and Asian merchants.\n\n"
                        "- **The Trade Licensing Act (1967):** Restricted retail trading licenses in non-urban centers exclusively to African citizens.\n"
                        "- **The Industrial and Commercial Development Corporation (ICDC):** Provided subsidized concessionary loans and business premises to African entrepreneurs.\n"
                        "- **Settlement Schemes:** The *Million-Acre Settlement Scheme* repurchased farms from departing European settlers and subdivided them among landless Kenyans."
                    )
                }
            }
        ]
    },
    {
        "page_number": 10,
        "page_title": "Challenges and Shortcomings of African Socialism",
        "blocks": [
            {
                "block_type": "step_process",
                "component_type": "step_process",
                "title": "Five Critical Setbacks of African Socialism",
                "content": {
                    "steps": [
                        "1. Heavy Tax Burden on Low-Income Earners: Progressive income tax and indirect sales taxes (VAT) disproportionately squeezed impoverished families.",
                        "2. Political Interference & Nepotism: State parastatals were riddled with political patronage, incompetent management, and tribal favoritism.",
                        "3. Political Leadership Wrangles: Elite rivalries between capitalists and radical socialists (e.g., Kenyatta vs. Oginga Odinga) polarized planning.",
                        "4. Misappropriation of Public Funds: Widespread corruption and embezzlement drained capital from settlement schemes and public corporations.",
                        "5. Widening Regional Inequalities: Planning disproportionately favored high-potential agricultural zones, neglecting arid and semi-arid regions."
                    ]
                }
            }
        ]
    },
    {
        "page_number": 11,
        "page_title": "Primary Source Analysis: Sessional Paper No. 10",
        "blocks": [
            {
                "block_type": "callout",
                "component_type": "callout",
                "title": "Historical Inquiry: The Philosophy Behind Sessional Paper No. 10",
                "content": {
                    "text": (
                        "**Excerpt from Sessional Paper No. 10 (1965):**\n"
                        "*> 'African Socialism must be flexible enough to borrow useful planning techniques from anywhere in the world, but it must firmly rest on our own traditional roots of mutual social responsibility and political democracy.'*\n\n"
                        "**Analytical Questions:**\n"
                        "1. **Observe:** Why did Kenya choose not to copy the Soviet communist model or the American capitalist model directly?\n"
                        "2. **Interpret:** How did the concept of 'mutual social responsibility' justify progressive taxation in post-independence Kenya?"
                    )
                }
            }
        ]
    },
    {
        "page_number": 12,
        "page_title": "Interactive Classification: Features of African Socialism",
        "blocks": [
            {
                "block_type": "mini_activity",
                "component_type": "mini_activity",
                "title": "Identify the Feature of African Socialism",
                "content": {
                    "instruction": "Match each historical policy to its core feature under African Socialism:",
                    "items": [
                        "1. Operating both private businesses and state parastatals -> **Mixed Economy**",
                        "2. Levying higher tax percentages on high-income earners -> **Progressive Taxation**",
                        "3. Empowering citizens to vote freely in national elections -> **Political Democracy**",
                        "4. Transferring European commercial businesses to African hands -> **Africanisation of the Economy**",
                        "5. Motivating citizens to serve the community rather than purely selfish gain -> **Mutual Social Responsibility**"
                    ]
                }
            }
        ]
    },
    {
        "page_number": 13,
        "page_title": "KCSE Examination Coaching: African Socialism",
        "blocks": [
            {
                "block_type": "worked_example",
                "component_type": "worked_example",
                "title": "KCSE Question: Explain Six Achievements of African Socialism in Kenya (12 Marks)",
                "content": {
                    "text": (
                        "**Examiner's Marking Scheme (Point + Explanation + Evidence = 2 Marks per Point):**\n\n"
                        "1. **Democratic Participation:** Established the constitutional basis for democratic elections and political representation, fostering political equality. (2 marks)\n\n"
                        "2. **Promotion of African Culture:** Grounded national development in traditional African values, restoring cultural identity and dignity. (2 marks)\n\n"
                        "3. **Fostering National Unity:** Emphasized that all Kenyans belonged to a single national family, helping bridge ethnic divisions post-independence. (2 marks)\n\n"
                        "4. **Fairness Through Progressive Taxation:** Successfully redistributed state revenue to construct public amenities, schools, and medical facilities. (2 marks)\n\n"
                        "5. **Agricultural Cooperative Development:** Promoted the formation of coffee, tea, and dairy cooperatives, enabling smallholders to market crops collectively. (2 marks)\n\n"
                        "6. **Africanisation of the Economy:** Provided loans through the ICDC and KCB, transferring commercial enterprises to indigenous Kenyans. (2 marks)"
                    )
                }
            }
        ]
    },
    {
        "page_number": 14,
        "page_title": "Check Your Understanding: Module 4.1",
        "blocks": [
            {
                "block_type": "knowledge_check",
                "component_type": "knowledge_check",
                "title": "Module 4.1 Assessment",
                "content": {
                    "questions": [
                        {
                            "question": "What is the official title of Sessional Paper No. 10 of 1965?",
                            "options": [
                                "National Development and Planning in Kenya",
                                "African Socialism and its Application to Planning in Kenya",
                                "The Harambee Development Strategy for Kenya",
                                "The Nyayo Blueprint for Economic Growth"
                            ],
                            "correct_answer": 1,
                            "explanation": "Sessional Paper No. 10 of 1965 is titled 'African Socialism and its Application to Planning in Kenya'."
                        },
                        {
                            "question": "Which Minister for Economic Planning and Development led the drafting of Sessional Paper No. 10 of 1965?",
                            "options": [
                                "Oginga Odinga",
                                "Tom Mboya",
                                "James Gichuru",
                                "Mwai Kibaki"
                            ],
                            "correct_answer": 1,
                            "explanation": "Tom Mboya guided the drafting and parliamentary adoption of Sessional Paper No. 10."
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
                "title": "Core Summary: African Socialism",
                "content": {
                    "text": (
                        "• **Origins:** Codified in Sessional Paper No. 10 of 1965 under Tom Mboya and Jomo Kenyatta to combat poverty, disease, and ignorance.\n"
                        "• **Two Traditional Pillars:** Political Democracy and Mutual Social Responsibility.\n"
                        "• **Core Features:** Mixed economy, progressive taxation, range of government controls, and diffusion of ownership.\n"
                        "• **Major Achievements:** Africanisation of commerce, agricultural cooperatives, progressive tax redistribution, and cultural restoration.\n"
                        "• **Major Challenges:** Political interference, corruption, widening regional disparities, and tax burden on the poor."
                    )
                }
            },
            {
                "block_type": "key_takeaway",
                "component_type": "key_takeaway",
                "title": "Key Takeaways",
                "content": {
                    "text": (
                        "- African Socialism steered Kenya between Western capitalism and Eastern communism.\n"
                        "- It provided the philosophical foundation for all subsequent national development strategies."
                    )
                }
            }
        ]
    }
]

LESSON_2_PAGES = [
    {
        "page_number": 1,
        "page_title": "The Harambee Philosophy: Meaning and Origins",
        "blocks": [
            {
                "block_type": "learning_goal",
                "component_type": "learning_goal",
                "title": "Lesson Objectives: Harambee Principles and Categories",
                "content": {
                    "text": (
                        "By the end of this lesson, you will be able to:\n"
                        "- Define Harambee and trace its origin from traditional communal mutual assistance\n"
                        "- Explain how President Jomo Kenyatta established Harambee as Kenya's official National Motto in 1963\n"
                        "- Analyze the four democratic principles guiding the authentic Harambee spirit\n"
                        "- Distinguish between the three major categories of Harambee development projects"
                    )
                }
            },
            {
                "block_type": "definition_card",
                "component_type": "definition_card",
                "title": "Definition: Harambee",
                "content": {
                    "term": "Harambee",
                    "definition": (
                        "A Kiswahili slogan meaning 'pulling together' or 'working together'. It is a grassroots development strategy "
                        "where communities voluntarily pool labor, finance, and materials to construct local public infrastructure to supplement state development programs."
                    )
                }
            }
        ]
    },
    {
        "page_number": 2,
        "page_title": "President Mzee Jomo Kenyatta and the National Motto",
        "blocks": [
            {
                "block_type": "suggested_image",
                "component_type": "suggested_image",
                "title": "President Mzee Jomo Kenyatta (1964)",
                "content": {
                    "text": "President Mzee Jomo Kenyatta, founding father of Kenya, who established Harambee as the national motto for collective development.",
                    "url": "https://upload.wikimedia.org/wikipedia/commons/9/90/Jomo_Kenyatta_1964.jpg",
                    "author": "Public Domain / Wikimedia Commons",
                    "licensing": "Public Domain",
                    "commons_page_url": "https://commons.wikimedia.org/wiki/File:Jomo_Kenyatta_1964.jpg"
                }
            },
            {
                "block_type": "concept_explanation",
                "component_type": "concept_explanation",
                "title": "Transforming Communal Tradition into National Policy",
                "content": {
                    "text": (
                        "- **Traditional Roots:** Communal mutual aid existed across all African cultures (e.g., *Ngwatio* among the Kikuyu, *Saga* among the Luo, *Mwethya* among the Kamba, *Risaga* among the Kisii).\n"
                        "- **Official Adoption (1963):** In 1963, President Mzee Jomo Kenyatta declared Harambee as Kenya's **National Motto**, inscribing it permanently on the nation's Coat of Arms.\n"
                        "- **The Rallying Call:** Kenyatta used Harambee as a powerful call to action, urging Kenyans not to wait passively for government handouts but to pull together to defeat poverty, disease, and ignorance."
                    )
                }
            }
        ]
    },
    {
        "page_number": 3,
        "page_title": "Historical Documentary: Jomo Kenyatta's Harambee Address",
        "blocks": [
            {
                "block_type": "suggested_video",
                "component_type": "suggested_video",
                "title": "Archival Footage: President Jomo Kenyatta Harambee National Address",
                "content": {
                    "url": "https://www.youtube.com/watch?v=m6B_5iIExjU",
                    "text": "Historical address by President Jomo Kenyatta rallying the Kenyan nation around the founding philosophy of Harambee (Pulling Together).",
                    "author": "Speech Archive / Kenya Historical Newsreels",
                    "licensing": "Standard YouTube License"
                }
            }
        ]
    },
    {
        "page_number": 4,
        "page_title": "Kenya's Coat of Arms and the Harambee Motto",
        "blocks": [
            {
                "block_type": "suggested_image",
                "component_type": "suggested_image",
                "title": "The Coat of Arms of Kenya with Harambee Motto",
                "content": {
                    "text": "The Coat of Arms of Kenya featuring two lions holding spears and a shield, with the national motto 'HARAMBEE' inscribed at the base.",
                    "url": "https://upload.wikimedia.org/wikipedia/commons/5/52/Coat_of_arms_of_Kenya.svg",
                    "author": "Government of Kenya / Public Domain",
                    "licensing": "Public Domain",
                    "commons_page_url": "https://commons.wikimedia.org/wiki/File:Coat_of_arms_of_Kenya.svg"
                }
            }
        ]
    },
    {
        "page_number": 5,
        "page_title": "The Four Guiding Principles of Authentic Harambee",
        "blocks": [
            {
                "block_type": "step_process",
                "component_type": "step_process",
                "title": "Core Principles of the Harambee Spirit",
                "content": {
                    "steps": [
                        "1. Collective Good as Opposed to Individual Gain: Projects must benefit the entire public community (dispensaries, school labs, water boreholes) rather than private individuals.",
                        "2. Volition (Voluntary Participation): Contributions of cash, labor, or building materials must be purely voluntary, without state coercion, force, or confiscation.",
                        "3. Felt Needs of the Majority: The choice of project must be decided democratically by the community based on their most urgent, collectively felt local priorities.",
                        "4. Maximum Utilization of Local Resources: Prioritizing local building stones, community manual labor, sand, timber, and domestic cash before seeking external aid."
                    ]
                }
            }
        ]
    },
    {
        "page_number": 6,
        "page_title": "Category 1 of Harambee: Social Projects",
        "blocks": [
            {
                "block_type": "concept_explanation",
                "component_type": "concept_explanation",
                "title": "Improving Human Capital and Community Welfare",
                "content": {
                    "text": (
                        "Social projects focus on human health, education, and community fellowship:\n\n"
                        "- **Educational Facilities:** Constructing classrooms, science laboratories, school libraries, dormitories, and founding community secondary schools (*Harambee Secondary Schools*).\n"
                        "- **Medical Facilities:** Setting up rural dispensaries, maternity wards, and local health clinics.\n"
                        "- **Religious Facilities:** Constructing churches, mosques, and community social halls."
                    )
                }
            }
        ]
    },
    {
        "page_number": 7,
        "page_title": "Category 2 of Harambee: Economic Projects",
        "blocks": [
            {
                "block_type": "concept_explanation",
                "component_type": "concept_explanation",
                "title": "Enhancing Rural Transport, Trade, and Utilities",
                "content": {
                    "text": (
                        "Economic projects build vital community connectivity and trade infrastructure:\n\n"
                        "- **Rural Transport:** Grading feeder access roads, building culverts, and constructing wooden or concrete bridges over seasonal rivers.\n"
                        "- **Water and Power Utilities:** Sinking community boreholes, constructing piped water kiosks, building earth dams, and purchasing communal electricity transformers."
                    )
                }
            }
        ]
    },
    {
        "page_number": 8,
        "page_title": "Category 3 of Harambee: Agricultural & Livestock Projects",
        "blocks": [
            {
                "block_type": "concept_explanation",
                "component_type": "concept_explanation",
                "title": "Boosting Food Security and Veterinary Health",
                "content": {
                    "text": (
                        "Agricultural projects protect community herds and improve farm yields:\n\n"
                        "- **Veterinary Infrastructure:** Constructing communal cattle dips to control tick-borne diseases (East Coast Fever) and purchasing communal milk cooling tanks.\n"
                        "- **Environmental Conservation:** Digging local irrigation canals, building soil erosion terraces on hillsides, and executing communal tree-planting drives."
                    )
                }
            }
        ]
    },
    {
        "page_number": 9,
        "page_title": "Comparative Table: Categories of Harambee Projects",
        "blocks": [
            {
                "block_type": "comparison_table",
                "component_type": "comparison_table",
                "title": "Summary of Harambee Project Categories",
                "content": {
                    "headers": ["Project Category", "Primary Objective", "Concrete Historical Examples"],
                    "rows": [
                        ["Social Projects", "Advance education, health, and spiritual welfare", "Classrooms, Harambee secondary schools, dispensaries, maternity wards, churches, mosques."],
                        ["Economic Projects", "Expand trade, market connectivity, and utilities", "Feeder access roads, culverts, river footbridges, community boreholes, piped water kiosks."],
                        ["Agricultural & Livestock Projects", "Improve food security and veterinary health", "Communal cattle dips, milk coolers, irrigation canals, soil conservation terraces, tree planting."]
                    ]
                }
            }
        ]
    },
    {
        "page_number": 10,
        "page_title": "The Principle of Volition vs. Forced Labour",
        "blocks": [
            {
                "block_type": "callout",
                "component_type": "callout",
                "title": "KCSE Conceptual Distinction: Volition",
                "content": {
                    "text": (
                        "A critical distinction examined in KCSE History:\n\n"
                        "- **Authentic Harambee:** Driven strictly by **volition** (free will). Citizens contribute because they recognize the project will improve their children's lives.\n"
                        "- **Colonial Forced Labour:** Imposed by colonial administrators under threat of imprisonment or fines.\n"
                        "- **Deviation Warning:** When overzealous chiefs confiscated chickens or goats from citizens who could not donate, they violated the core principle of volition, corrupting the spirit of Harambee."
                    )
                }
            }
        ]
    },
    {
        "page_number": 11,
        "page_title": "Interactive Classification: Harambee Categories",
        "blocks": [
            {
                "block_type": "mini_activity",
                "component_type": "mini_activity",
                "title": "Classify the Harambee Project Category",
                "content": {
                    "instruction": "Assign each project to its correct category (Social, Economic, or Agricultural/Livestock):",
                    "items": [
                        "1. Constructing a community secondary school science laboratory -> **Social Project**",
                        "2. Grading a feeder access road to link a rural village to the highway -> **Economic Project**",
                        "3. Building a communal cattle dip to eradicate tick fever -> **Agricultural / Livestock Project**",
                        "4. Sinking a deep borehole to provide clean drinking water -> **Economic / Social Project**",
                        "5. Terracing a steep hillside to prevent soil erosion -> **Agricultural / Livestock Project**",
                        "6. Constructing a maternity ward at a village dispensary -> **Social Project**"
                    ]
                }
            }
        ]
    },
    {
        "page_number": 12,
        "page_title": "KCSE Examination Coaching: Principles of Harambee",
        "blocks": [
            {
                "block_type": "worked_example",
                "component_type": "worked_example",
                "title": "KCSE Question: State Five Principles That Guide the Authentic Harambee Spirit (5 Marks)",
                "content": {
                    "text": (
                        "**Examiner's Marking Scheme (1 Mark per distinct principle):**\n\n"
                        "1. **Collective Good over Individual Gain:** Projects must serve public community welfare rather than private benefit. (1 mark)\n"
                        "2. **Volition (Voluntary Participation):** Contributions must be made freely without force, coercion, or intimidation. (1 mark)\n"
                        "3. **Felt Needs of the Majority:** The project must be decided democratically by the community based on urgent local priorities. (1 mark)\n"
                        "4. **Maximum Utilization of Local Resources:** Projects should prioritize local labor, building stones, timber, and cash. (1 mark)\n"
                        "5. **Mutual Social Responsibility:** Wealthier community members have a moral duty to assist the less fortunate. (1 mark)"
                    )
                }
            }
        ]
    },
    {
        "page_number": 13,
        "page_title": "Check Your Understanding: Module 4.2",
        "blocks": [
            {
                "block_type": "knowledge_check",
                "component_type": "knowledge_check",
                "title": "Module 4.2 Assessment",
                "content": {
                    "questions": [
                        {
                            "question": "What is the literal English translation of the Kiswahili motto 'Harambee'?",
                            "options": [
                                "Peace, Love, and Unity",
                                "Pulling together or working together",
                                "Self-Government Now",
                                "Freedom and Justice"
                            ],
                            "correct_answer": 1,
                            "explanation": "Harambee translates to 'pulling together' or 'working together' for communal development."
                        },
                        {
                            "question": "Which of the following is an example of an agricultural Harambee project?",
                            "options": [
                                "Constructing a school library",
                                "Building a communal cattle dip",
                                "Grading a rural road",
                                "Building a maternity clinic"
                            ],
                            "correct_answer": 1,
                            "explanation": "Constructing communal cattle dips directly boosts veterinary health and livestock farming."
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
                "title": "Core Summary: Harambee Meaning and Principles",
                "content": {
                    "text": (
                        "• **Origins:** Rooted in traditional African mutual aid (Ngwatio, Saga, Mwethya); declared national motto by Kenyatta in 1963.\n"
                        "• **Four Guiding Principles:** Collective good, volition (voluntary), felt needs of the majority, and maximum use of local resources.\n"
                        "• **Three Categories:** Social (schools/clinics), Economic (roads/water/bridges), and Agricultural/Livestock (cattle dips/terracing/irrigation)."
                    )
                }
            },
            {
                "block_type": "key_takeaway",
                "component_type": "key_takeaway",
                "title": "Key Takeaways",
                "content": {
                    "text": (
                        "- Harambee empowered rural Kenyans to construct schools and clinics long before central government funds arrived.\n"
                        "- True Harambee is defined by voluntary community action, not bureaucratic coercion."
                    )
                }
            }
        ]
    },
    {
        "page_number": 15,
        "page_title": "Revision Checklist for Harambee Fundamentals",
        "blocks": [
            {
                "block_type": "step_process",
                "component_type": "step_process",
                "title": "Mastery Checklist",
                "content": {
                    "steps": [
                        "1. Definition and Kiswahili meaning of Harambee ('Pulling Together').",
                        "2. Role of President Jomo Kenyatta in 1963 and the Coat of Arms.",
                        "3. Four Principles: Collective good, volition, felt needs, local resources.",
                        "4. Three Categories: Social, Economic, Agricultural/Livestock."
                    ]
                }
            }
        ]
    }
]

LESSON_3_PAGES = [
    {
        "page_number": 1,
        "page_title": "Harambee's Contributions to National Development",
        "blocks": [
            {
                "block_type": "learning_goal",
                "component_type": "learning_goal",
                "title": "Lesson Objectives: Harambee Impact and Challenges",
                "content": {
                    "text": (
                        "By the end of this lesson, you will be able to:\n"
                        "- Analyze the dedicated contribution of the Harambee movement to Kenya's education sector\n"
                        "- Explain the general social and economic impacts of Harambee on rural development\n"
                        "- Examine the systemic challenges that corrupted the Harambee movement over time\n"
                        "- Evaluate the legislative reforms introduced under the Public Officer Ethics Act"
                    )
                }
            },
            {
                "block_type": "definition_card",
                "component_type": "definition_card",
                "title": "Concept: The Engine of Rural Transformation",
                "content": {
                    "term": "Harambee in Development",
                    "definition": (
                        "The primary self-help mechanism through which rural communities mobilized hundreds of millions of shillings "
                        "to construct secondary schools, medical dispensaries, water boreholes, and cattle dips, bridging severe national budgetary deficits."
                    )
                }
            }
        ]
    },
    {
        "page_number": 2,
        "page_title": "Historical Documentary: The Harambee Spirit in Action",
        "blocks": [
            {
                "block_type": "suggested_video",
                "component_type": "suggested_video",
                "title": "Educational Documentary: Harambee — Kenya's Powerful Community Spirit",
                "content": {
                    "url": "https://www.youtube.com/watch?v=zFUZQGq1Gqw",
                    "text": "Explore how collective community fundraising transformed Kenya's rural landscape, funding schools, clinics, and clean water access.",
                    "author": "Insight Lab / Educational Documentary",
                    "licensing": "Standard YouTube License"
                }
            }
        ]
    },
    {
        "page_number": 3,
        "page_title": "Harambee's Contribution to the Education Sector",
        "blocks": [
            {
                "block_type": "concept_explanation",
                "component_type": "concept_explanation",
                "title": "A Dedicated Look at the Educational Revolution",
                "content": {
                    "text": (
                        "The single greatest beneficiary of the Harambee movement was the education sector:\n\n"
                        "- **Construction of Schools:** Thousands of primary and secondary schools (*Harambee Secondary Schools*) were built from scratch by parents.\n"
                        "- **Science Laboratories & Libraries:** Fundraisers provided specialized science equipment, chemicals, and textbooks.\n"
                        "- **School Fees for Needy Students:** Community funds paid secondary and university fees for orphans and bright children from impoverished backgrounds.\n"
                        "- **Staff Salaries:** Paid salaries for Board of Management (BOM) teachers to alleviate government teacher shortages.\n"
                        "- **School Feeding Programmes:** Financed school lunch feeding schemes in arid and semi-arid regions, boosting student retention."
                    )
                }
            }
        ]
    },
    {
        "page_number": 4,
        "page_title": "Eight Specific Educational Contributions (Point-Form)",
        "blocks": [
            {
                "block_type": "step_process",
                "component_type": "step_process",
                "title": "Examinable Educational Impacts of Harambee",
                "content": {
                    "steps": [
                        "1. Construction of Educational Facilities: Built classrooms, science laboratories, libraries, dormitories, and administration blocks.",
                        "2. Payment of School Fees: Established bursaries and community collections to keep orphans and needy students in school.",
                        "3. Upgrading Physical Infrastructure: Replaced mud-walled structures with permanent stone buildings.",
                        "4. Purchase of Learning Materials: Financed textbooks, computers, laboratory apparatus, and stationery.",
                        "5. Paying Additional Staff Salaries: Funded Board of Management (BOM) teachers and support staff to offset government shortages.",
                        "6. Supporting Co-Curricular Activities: Bought sports kits, musical instruments, and school buses.",
                        "7. Supplying School Furniture: Provided desks, chairs, lockers, and laboratory stools.",
                        "8. Funding School Feeding Programmes: Subsidized daily meals for students in drought-prone areas."
                    ]
                }
            }
        ]
    },
    {
        "page_number": 5,
        "page_title": "General Social and Economic Contributions",
        "blocks": [
            {
                "block_type": "concept_explanation",
                "component_type": "concept_explanation",
                "title": "Broader Socio-Economic Transformation",
                "content": {
                    "text": (
                        "Beyond education, Harambee served as a catalyst for overall national development:\n\n"
                        "- **Rural Infrastructure:** Financed rural electrification, borehole drilling, and feeder road grading.\n"
                        "- **National Integration:** Brought together diverse ethnic groups, religions, and classes to collaborate for a common public cause.\n"
                        "- **Culture of Self-Reliance:** Reduced over-reliance on foreign aid and government handouts, empowering citizens to solve local challenges.\n"
                        "- **Urban-to-Rural Capital Redistribution:** Urban professionals traveled to ancestral homes to donate money, transferring capital from wealthy cities to rural villages.\n"
                        "- **Safety Net for Vulnerable Groups:** Raised emergency funds for overseas medical surgeries, disability trust funds, and orphanage support."
                    )
                }
            }
        ]
    },
    {
        "page_number": 6,
        "page_title": "Case Study: The 1989 National Disability Harambee",
        "blocks": [
            {
                "block_type": "callout",
                "component_type": "callout",
                "title": "Historical Evidence: Mammoth Fundraiser at Nyayo Stadium",
                "content": {
                    "text": (
                        "**The Event:** On 8 April 1989, President Daniel arap Moi presided over a mammoth National Harambee rally at Nyayo National Stadium in Nairobi, raising a historic **KSh 70 Million** in a single afternoon to establish the National Fund for the Disabled of Kenya (NFDK).\n\n"
                        "**Impact:** The trust fund continues to support persons living with disabilities across Kenya today with wheelchairs, vocational tools, and rehabilitation grants."
                    )
                }
            }
        ]
    },
    {
        "page_number": 7,
        "page_title": "Systemic Challenges Facing the Harambee Movement",
        "blocks": [
            {
                "block_type": "step_process",
                "component_type": "step_process",
                "title": "Six Structural Abuses that Compromised Harambee",
                "content": {
                    "steps": [
                        "1. Corruption and Embezzlement: Project treasurers and committee leaders regularly stole or mismanaged public contributions, leaving projects abandoned.",
                        "2. Coercion and Extortion by Administration: Chiefs and district officers forced citizens to contribute, confiscating livestock or household goods from poor defaulters.",
                        "3. Political Hijacking & Vote-Buying: Politicians transformed fundraisers into competitive displays of wealth to purchase political influence and votes.",
                        "4. Leadership Wrangles: Local political rivalries over who should control funds paralyzed development projects.",
                        "5. Unsustainable Financial Burden on the Poor: Constant demands for donations to schools, churches, and clinics strained impoverished households.",
                        "6. Substandard Construction & Poor Planning: Facilities were often built without architectural plans or government supervision, leading to structural failures."
                    ]
                }
            }
        ]
    },
    {
        "page_number": 8,
        "page_title": "The Public Officer Ethics Act and Legislative Reform",
        "blocks": [
            {
                "block_type": "concept_explanation",
                "component_type": "concept_explanation",
                "title": "Legislative Action Against Harambee Corruption",
                "content": {
                    "text": (
                        "By the late 1990s, corrupt politicians and public officials were routinely laundering stolen public funds by making massive donations at Harambees to buy political popularity.\n\n"
                        "- **The Public Officer Ethics Act (2003):** Parliament enacted landmark legislation barring public officers and state servants from presiding over, collecting, or playing a leading role in public Harambees.\n"
                        "- **Impact:** Successfully separated public service duties from competitive political donations, curbing corruption and restoring administrative integrity."
                    )
                }
            }
        ]
    },
    {
        "page_number": 9,
        "page_title": "Comparative Analysis: Authentic vs. Compromised Harambee",
        "blocks": [
            {
                "block_type": "comparison_table",
                "component_type": "comparison_table",
                "title": "The Evolution and Degradation of the Harambee Practice",
                "content": {
                    "headers": ["Dimension", "Authentic Harambee Spirit (1960s)", "Compromised Harambee Practice (1980s–1990s)"],
                    "rows": [
                        ["Motivation", "Genuine community desire to build a school or clinic based on 'felt needs'.", "Political ambition, vote-buying, and showcasing wealth between 'the haves' and 'the have-nots'."],
                        ["Participation", "Purely voluntary (volition); contributions given gladly according to ability.", "Forced extortion by chiefs; confiscation of livestock and goods from the poor."],
                        ["Financial Integrity", "Accountable local committees trusted by the community.", "Embezzlement by project treasurers and laundering of looted state funds."],
                        ["Supervision", "Community-monitored manual labor with maximum local materials.", "Substandard contractor work without government architectural oversight."]
                    ]
                }
            }
        ]
    },
    {
        "page_number": 10,
        "page_title": "Primary Source Inquiry: Evaluating Coercion",
        "blocks": [
            {
                "block_type": "callout",
                "component_type": "callout",
                "title": "Historical Inquiry: The Chief's Harambee Tax",
                "content": {
                    "text": (
                        "**Historical Scenario:** In 1992, an assistant chief set up a roadblock, impounding milk cans from smallholder dairy farmers who could not produce a receipt proving they had contributed KSh 200 toward the construction of a local police post.\n\n"
                        "**Analytical Questions:**\n"
                        "1. **Principle Violation:** Which two foundational principles of the Harambee spirit did the assistant chief violate?\n"
                        "2. **Impact on Citizens:** How did such administrative practices transform the public perception of Harambee from voluntary mutual aid into a hated informal tax?"
                    )
                }
            }
        ]
    },
    {
        "page_number": 11,
        "page_title": "Interactive Classification: Harambee Impact vs. Abuse",
        "blocks": [
            {
                "block_type": "mini_activity",
                "component_type": "mini_activity",
                "title": "Classify the Statement as a Contribution or a Challenge",
                "content": {
                    "instruction": "Categorize each historical reality of the Harambee movement:",
                    "items": [
                        "1. Raising funds to pay school fees for orphaned and needy students -> **Educational Contribution**",
                        "2. Project treasurers diverting contributed funds into personal bank accounts -> **Systemic Challenge**",
                        "3. Wealthy urban citizens transferring capital to ancestral rural villages -> **Economic Contribution**",
                        "4. Confiscation of household chickens by local chiefs from non-contributors -> **Systemic Challenge**",
                        "5. Enacting the Public Officer Ethics Act to ban public servant collection -> **Legislative Reform**"
                    ]
                }
            }
        ]
    },
    {
        "page_number": 12,
        "page_title": "KCSE Examination Coaching: Educational Contributions",
        "blocks": [
            {
                "block_type": "worked_example",
                "component_type": "worked_example",
                "title": "KCSE Question: Explain Six Contributions of Harambee to the Development of Education in Kenya (12 Marks)",
                "content": {
                    "text": (
                        "**Examiner's Marking Scheme (Point + Explanation + Evidence = 2 Marks per Point):**\n\n"
                        "1. **Construction of Educational Facilities:** Communities pooled funds to build classrooms, science laboratories, dormitories, and libraries, significantly expanding school capacity. (2 marks)\n\n"
                        "2. **Assistance with School Fees:** Fundraisers paid secondary and college fees for needy and orphaned students, preventing dropouts. (2 marks)\n\n"
                        "3. **Upgrading School Infrastructure:** Replaced temporary mud-walled classrooms with permanent stone buildings, providing safe learning environments. (2 marks)\n\n"
                        "4. **Purchase of Learning Materials:** Financed textbooks, science equipment, charts, and computers, boosting instructional quality. (2 marks)\n\n"
                        "5. **Hiring Board of Management Teachers:** Provided funds to hire additional teachers to address severe government teacher deficits. (2 marks)\n\n"
                        "6. **Supporting Co-Curricular Activities:** Bought sports equipment, musical instruments, and school buses to nurture student talents. (2 marks)"
                    )
                }
            }
        ]
    },
    {
        "page_number": 13,
        "page_title": "Check Your Understanding: Module 4.3",
        "blocks": [
            {
                "block_type": "knowledge_check",
                "component_type": "knowledge_check",
                "title": "Module 4.3 Assessment",
                "content": {
                    "questions": [
                        {
                            "question": "Which landmark legislation was passed in 2003 to prohibit public servants from collecting or managing public Harambee funds?",
                            "options": [
                                "The Anti-Corruption and Economic Crimes Act",
                                "The Public Officer Ethics Act",
                                "The National Cohesion and Integration Act",
                                "The Leadership and Integrity Act"
                            ],
                            "correct_answer": 1,
                            "explanation": "The Public Officer Ethics Act (2003) prohibited public officers from presiding over or collecting Harambee funds."
                        },
                        {
                            "question": "How does Harambee facilitate the redistribution of resources across Kenya?",
                            "options": [
                                "By imposing compulsory income taxes on foreign tourists",
                                "By enabling high-earning urban professionals to contribute funds to underdeveloped rural home villages",
                                "By printing additional currency during national holidays",
                                "By nationalizing private banks"
                            ],
                            "correct_answer": 1,
                            "explanation": "Urban workers contribute funds during rural weekend fundraisers, channeling wealth from urban centers to rural villages."
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
                "title": "Core Summary: Harambee Impact and Challenges",
                "content": {
                    "text": (
                        "• **Educational Impact:** Built thousands of classrooms, funded needy student fees, hired BOM teachers, and purchased lab equipment.\n"
                        "• **General Impact:** Rural infrastructure expansion, urban-to-rural capital transfer, national unity, and safety nets for vulnerable groups.\n"
                        "• **Systemic Challenges:** Corruption, coercion by chiefs, political vote-buying, financial strain on the poor, and poor construction.\n"
                        "• **Reforms:** The Public Officer Ethics Act (2003) barred public officers from playing leading roles in fundraisers."
                    )
                }
            },
            {
                "block_type": "key_takeaway",
                "component_type": "key_takeaway",
                "title": "Key Takeaways",
                "content": {
                    "text": (
                        "- Harambee was the primary vehicle of grassroots school construction in post-independence Kenya.\n"
                        "- Legislative checks were essential to prevent political corruption from destroying the noble spirit of self-help."
                    )
                }
            }
        ]
    },
    {
        "page_number": 15,
        "page_title": "Revision Checklist: Harambee Performance",
        "blocks": [
            {
                "block_type": "step_process",
                "component_type": "step_process",
                "title": "Mastery Checklist for Exams",
                "content": {
                    "steps": [
                        "1. Eight educational contributions (facilities, fees, BOM teachers, learning materials).",
                        "2. General socio-economic contributions (rural roads, water, capital redistribution).",
                        "3. Six challenges (embezzlement, coercion, political hijacking, poor coordination).",
                        "4. The Public Officer Ethics Act (2003) and its purpose."
                    ]
                }
            }
        ]
    }
]

LESSON_4_PAGES = [
    {
        "page_number": 1,
        "page_title": "The Nyayo Philosophy: Origins, Pillars, and Sources",
        "blocks": [
            {
                "block_type": "learning_goal",
                "component_type": "learning_goal",
                "title": "Lesson Objectives: Nyayoism",
                "content": {
                    "text": (
                        "By the end of this lesson, you will be able to:\n"
                        "- Define Nyayoism and trace its origin from President Daniel arap Moi's 1978 political pledge\n"
                        "- Analyze the three core pillars: Peace, Love, and Unity\n"
                        "- Explain the three ideological sources of the Nyayo philosophy\n"
                        "- Evaluate the key state development programs implemented under Nyayoism (Nyayo Milk, Nyayo Wards, Jua Kali, DFRD, Nyayo Tea Zones)"
                    )
                }
            },
            {
                "block_type": "definition_card",
                "component_type": "definition_card",
                "title": "Definition: Nyayoism",
                "content": {
                    "term": "Nyayoism",
                    "definition": (
                        "A Kenyan national development philosophy formulated by President Daniel Toroitich arap Moi in 1978, "
                        "meaning 'footsteps' (nyayo), anchored on three core pillars—Peace, Love, and Unity—and the ethical requirement of being mindful of other people's welfare."
                    )
                }
            }
        ]
    },
    {
        "page_number": 2,
        "page_title": "Origins of Nyayoism: Following in the Footsteps",
        "blocks": [
            {
                "block_type": "concept_explanation",
                "component_type": "concept_explanation",
                "title": "President Daniel arap Moi's 1978 Presidential Pledge",
                "content": {
                    "text": (
                        "- **The Succession (August 1978):** Following the passing of President Mzee Jomo Kenyatta on 22 August 1978, Vice President **Daniel Toroitich arap Moi** assumed the presidency.\n"
                        "- **The 'Nyayo' Pledge:** Moi reassured a tense nation that he would follow *'in the footsteps'* (*nyayo*) of Kenyatta, ensuring policy continuity, national stability, and the preservation of the Harambee spirit.\n"
                        "- **Evolution into a Philosophy:** Over time, Nyayoism was systematically articulated into a comprehensive national philosophy centered on being mindful of other people's welfare."
                    )
                }
            },
            {
                "block_type": "suggested_image",
                "component_type": "suggested_image",
                "title": "President Daniel Toroitich arap Moi (1981)",
                "content": {
                    "text": "President Daniel Toroitich arap Moi, architect of the Nyayo philosophy, whose signature rungu and red rose became symbols of Peace, Love, and Unity.",
                    "url": "https://upload.wikimedia.org/wikipedia/commons/4/43/Daniel_arap_Moi_1981.jpg",
                    "author": "Public Domain / Wikimedia Commons",
                    "licensing": "Public Domain",
                    "commons_page_url": "https://commons.wikimedia.org/wiki/File:Daniel_arap_Moi_1981.jpg"
                }
            }
        ]
    },
    {
        "page_number": 3,
        "page_title": "Historical Documentary: President Moi and Nyayoism",
        "blocks": [
            {
                "block_type": "suggested_video",
                "component_type": "suggested_video",
                "title": "Historical Archival Recording: President Moi on Peace, Love, and Unity",
                "content": {
                    "url": "https://www.youtube.com/watch?v=ZCZRjjaRzaE",
                    "text": "Watch archival recordings of President Daniel arap Moi articulating the Nyayo philosophy and urging Kenyans to uphold Peace, Love, and Unity.",
                    "author": "MediaGuru / Kenya History Archives",
                    "licensing": "Standard YouTube License"
                }
            }
        ]
    },
    {
        "page_number": 4,
        "page_title": "The Three Core Pillars of Nyayoism",
        "blocks": [
            {
                "block_type": "comparison_table",
                "component_type": "comparison_table",
                "title": "The Pillars of Peace, Love, and Unity",
                "content": {
                    "headers": ["Pillar", "Philosophical Definition", "Role in National Development"],
                    "rows": [
                        ["Peace", "The state of being free from war, civil strife, crime, and social disorder.", "Foundation of all sustainable progress; political stability attracts investments and boosts tourism."],
                        ["Love", "Mutual respect, trust, empathy, and readiness to cooperate without selfishness.", "Encourages traditional African sharing through the extended family network, fostering mutual social responsibility."],
                        ["Unity", "State of harmony, consensus, and oneness of purpose among diverse peoples.", "Binds Kenya's 40+ ethnic groups, religions, and races into a unified, cohesive nation."]
                    ]
                }
            }
        ]
    },
    {
        "page_number": 5,
        "page_title": "The Three Ideological Sources of Nyayoism",
        "blocks": [
            {
                "block_type": "step_process",
                "component_type": "step_process",
                "title": "Where Did Nyayoism Originate?",
                "content": {
                    "steps": [
                        "1. Sessional Paper No. 10 of 1965 (African Socialism): Drew directly from its principles of mutual social responsibility, political democracy, and communal welfare.",
                        "2. Biblical Teachings: Grounded in Christian scripture and the Ten Commandments: Love for God, love for neighbor, and love for self.",
                        "3. Moi's Long Political Career: Serving as Vice President for 12 years convinced Moi that Kenya's diverse multi-ethnic society could only survive if anchored in peace, love, and unity."
                    ]
                }
            }
        ]
    },
    {
        "page_number": 6,
        "page_title": "Nyayoism in Action 1: The Nyayo Milk Programme",
        "blocks": [
            {
                "block_type": "concept_explanation",
                "component_type": "concept_explanation",
                "title": "Free Milk for Primary School Children",
                "content": {
                    "text": (
                        "- **The Policy:** Introduced in 1979, the government provided free packets of pasteurized milk to all primary school pupils nationwide every week.\n"
                        "- **Impact:** Dramatically boosted primary school enrollment and attendance, particularly in poor and marginalized arid areas.\n"
                        "- **Nutritional Benefit:** Improved childhood nutrition, reduced stunted growth, and promoted the domestic dairy farming cooperative sector (KCC)."
                    )
                }
            }
        ]
    },
    {
        "page_number": 7,
        "page_title": "Nyayoism in Action 2: Nyayo Wards in Public Hospitals",
        "blocks": [
            {
                "block_type": "concept_explanation",
                "component_type": "concept_explanation",
                "title": "Expanding Healthcare Access Across Kenya",
                "content": {
                    "text": (
                        "- **Community-State Partnerships:** The government combined state funds with community Harambee fundraisers to construct specialized multi-bed hospital wards (*Nyayo Wards*) in provincial and district hospitals nationwide.\n"
                        "- **Impact:** Vastly expanded patient bed capacity, reduced hospital overcrowding, and brought specialized inpatient healthcare closer to rural communities."
                    )
                }
            }
        ]
    },
    {
        "page_number": 8,
        "page_title": "Nyayoism in Action 3: Nyayo Tea Zones and Environmental Conservation",
        "blocks": [
            {
                "block_type": "concept_explanation",
                "component_type": "concept_explanation",
                "title": "Forest Conservation and Green Buffer Zones",
                "content": {
                    "text": (
                        "- **Environmental Buffer:** The government established a state corporation—the **Nyayo Tea Zones Development Corporation**—planting continuous belts of tea along the perimeters of public gazetted water towers (Mount Kenya, Aberdares, Mau Forest).\n"
                        "- **Dual Benefit:**\n"
                        "  1. Acted as a physical barrier preventing human encroachment, illegal logging, and deforestation.\n"
                        "  2. Generated agricultural employment and foreign exchange through tea exports."
                    )
                }
            }
        ]
    },
    {
        "page_number": 9,
        "page_title": "Nyayoism in Action 4: Promotion of the Jua Kali Sector",
        "blocks": [
            {
                "block_type": "concept_explanation",
                "component_type": "concept_explanation",
                "title": "Empowering Informal Artisans and Local Manufacturers",
                "content": {
                    "text": (
                        "- **Background:** Millions of skilled artisans (blacksmiths, mechanics, carpenters, metal fabricators) worked under the scorching sun (*Jua Kali*).\n"
                        "- **Government Support:** President Moi championed the sector, ordering the construction of permanent, state-funded metal sheds (*Nyayo Jua Kali Sheds*) in towns nationwide.\n"
                        "- **Impact:** Provided artisans with electricity, security, and workspace, fostering indigenous informal manufacturing and creating millions of self-employment opportunities."
                    )
                }
            }
        ]
    },
    {
        "page_number": 10,
        "page_title": "Nyayoism in Action 5: District Focus for Rural Development (DFRD)",
        "blocks": [
            {
                "block_type": "concept_explanation",
                "component_type": "concept_explanation",
                "title": "Decentralizing Development Planning to Grassroots Districts",
                "content": {
                    "text": (
                        "- **The Strategy (1983):** Shifted national economic planning away from the central Treasury in Nairobi to the 41 district headquarters.\n"
                        "- **District Development Committees (DDCs):** Composed of local MPs, district officers, and community elders who directly identified and prioritized local development projects.\n"
                        "- **Significance:** Early forerunner of modern devolution, ensuring rural communities actively shaped their own economic development."
                    )
                }
            }
        ]
    },
    {
        "page_number": 11,
        "page_title": "Nyayoism in Action 6: Expansion of Public Universities",
        "blocks": [
            {
                "block_type": "concept_explanation",
                "component_type": "concept_explanation",
                "title": "Democratizing Higher Education in Kenya",
                "content": {
                    "text": (
                        "Prior to 1984, Kenya possessed only one public university (University of Nairobi).\n\n"
                        "- Under President Moi's administration, university education expanded massively with the establishment of:\n"
                        "  - **Moi University (1984):** Kenya's second public university, established in Eldoret focusing on technology.\n"
                        "  - **Kenyatta University (1985):** Upgraded to a fully chartered university focusing on education.\n"
                        "  - **Egerton University (1987):** Upgraded to lead in agricultural sciences.\n"
                        "  - **JKUAT & Maseno University:** Expanded tertiary and vocational technology training."
                    )
                }
            }
        ]
    },
    {
        "page_number": 12,
        "page_title": "Summary Table: Key Nyayo Development Programs",
        "blocks": [
            {
                "block_type": "comparison_table",
                "component_type": "comparison_table",
                "title": "Developmental Programs Under the Nyayo Era",
                "content": {
                    "headers": ["Program Name", "Target Sector", "Core National Benefit"],
                    "rows": [
                        ["Nyayo Milk Programme", "Primary Education & Nutrition", "Provided free milk, boosting primary school enrollment and supporting dairy cooperatives."],
                        ["Nyayo Wards", "Public Healthcare", "Constructed multi-bed wards in district hospitals, drastically reducing hospital congestion."],
                        ["Nyayo Tea Zones", "Environment & Forestry", "Created tea buffer strips around gazetted forests to prevent illegal logging and soil erosion."],
                        ["Jua Kali Sheds", "Informal Manufacturing & Employment", "Constructed state-funded workshops, empowering blacksmiths, mechanics, and carpenters."],
                        ["District Focus (DFRD)", "Decentralized Planning", "Decentralized development planning from Nairobi to District Development Committees (DDCs)."],
                        ["University Expansion", "Higher Education", "Founded Moi, Kenyatta, Egerton, JKUAT, and Maseno Universities to expand tertiary training."]
                    ]
                }
            }
        ]
    },
    {
        "page_number": 13,
        "page_title": "Interactive Classification: Nyayo Programs",
        "blocks": [
            {
                "block_type": "mini_activity",
                "component_type": "mini_activity",
                "title": "Match the Nyayo Program to Its Primary Purpose",
                "content": {
                    "instruction": "Test your mastery of development programs implemented under Nyayoism:",
                    "items": [
                        "1. Provided free milk to boost school enrollment -> **Nyayo Milk Programme**",
                        "2. Created tea buffer strips to prevent forest encroachment -> **Nyayo Tea Zones**",
                        "3. Constructed protective metal sheds for informal artisans -> **Jua Kali Sheds**",
                        "4. Decentralized economic planning to district committees -> **District Focus for Rural Development (DFRD)**",
                        "5. Constructed multi-bed inpatient hospital wings -> **Nyayo Wards**"
                    ]
                }
            }
        ]
    },
    {
        "page_number": 14,
        "page_title": "KCSE Examination Coaching: Pillars and Sources of Nyayoism",
        "blocks": [
            {
                "block_type": "worked_example",
                "component_type": "worked_example",
                "title": "KCSE Question: State Three Core Pillars and Three Ideological Sources of Nyayoism (6 Marks)",
                "content": {
                    "text": (
                        "**Examiner's Marking Scheme (1 Mark per correct item):**\n\n"
                        "**Three Core Pillars (3 marks):**\n"
                        "1. **Peace:** Freedom from war, disorder, and civil strife, providing stability for investment. (1 mark)\n"
                        "2. **Love:** Mutual respect, empathy, and willingness to share resources with the less fortunate. (1 mark)\n"
                        "3. **Unity:** Oneness and harmony across Kenya's diverse ethnic and religious groups. (1 mark)\n\n"
                        "**Three Ideological Sources (3 marks):**\n"
                        "4. **Sessional Paper No. 10 of 1965 (African Socialism):** Drew principles of mutual social responsibility. (1 mark)\n"
                        "5. **Biblical Teachings:** Grounded in the Ten Commandments (Love for God and neighbor). (1 mark)\n"
                        "6. **Moi's Long Political Career:** Lessons learned during 12 years as Vice President. (1 mark)"
                    )
                }
            }
        ]
    },
    {
        "page_number": 15,
        "page_title": "Check Your Understanding: Module 4.4",
        "blocks": [
            {
                "block_type": "knowledge_check",
                "component_type": "knowledge_check",
                "title": "Module 4.4 Assessment",
                "content": {
                    "questions": [
                        {
                            "question": "What is the meaning of the Kiswahili word 'Nyayo'?",
                            "options": [
                                "Pulling Together",
                                "Footsteps",
                                "Peace and Unity",
                                "Self-Reliance"
                            ],
                            "correct_answer": 1,
                            "explanation": "Nyayo translates literally to 'footsteps', symbolizing President Moi following in Kenyatta's footsteps."
                        },
                        {
                            "question": "Which of the following was NOT an ideological source of the Nyayo philosophy?",
                            "options": [
                                "Sessional Paper No. 10 of 1965",
                                "Biblical Teachings",
                                "Karl Marx's Communist Manifesto",
                                "Moi's Long Political Career"
                            ],
                            "correct_answer": 2,
                            "explanation": "Nyayoism was derived from African Socialism, Biblical teachings, and Moi's political career, rejecting Marxism."
                        }
                    ]
                }
            }
        ]
    },
    {
        "page_number": 16,
        "page_title": "Lesson Summary & Key Takeaways",
        "blocks": [
            {
                "block_type": "summary",
                "component_type": "summary",
                "title": "Core Summary: The Nyayo Philosophy",
                "content": {
                    "text": (
                        "• **Origins:** Introduced in 1978 by Daniel arap Moi, pledging to follow in Kenyatta's footsteps (*nyayo*).\n"
                        "• **3 Pillars:** Peace, Love, and Unity (centered on being mindful of other people's welfare).\n"
                        "• **3 Sources:** Sessional Paper No. 10, Biblical teachings, and Moi's political experience.\n"
                        "• **Key Programs:** Nyayo Milk, Nyayo Wards, Nyayo Tea Zones, Jua Kali sheds, DFRD decentralization, and public university expansion."
                    )
                }
            },
            {
                "block_type": "key_takeaway",
                "component_type": "key_takeaway",
                "title": "Key Takeaways",
                "content": {
                    "text": (
                        "- Nyayoism provided national continuity during the delicate 1978 presidential succession.\n"
                        "- Its welfare and environmental initiatives directly touched the daily lives of millions of school children and rural farmers."
                    )
                }
            }
        ]
    }
]

LESSON_5_PAGES = [
    {
        "page_number": 1,
        "page_title": "Cumulative Impact and Synthesis of National Philosophies",
        "blocks": [
            {
                "block_type": "learning_goal",
                "component_type": "learning_goal",
                "title": "Lesson Objectives: Cumulative Impact of National Philosophies",
                "content": {
                    "text": (
                        "By the end of this lesson, you will be able to:\n"
                        "- Synthesize the collective social, economic, and political impacts of Kenya's national philosophies\n"
                        "- Compare African Socialism, Harambee, and Nyayoism in a comprehensive master table\n"
                        "- Apply the Point-Explanation-Evidence structure to KCSE examination essay questions\n"
                        "- Master the full revision checklist for Topic 4"
                    )
                }
            },
            {
                "block_type": "definition_card",
                "component_type": "definition_card",
                "title": "Concept: The Triad of National Philosophies",
                "content": {
                    "term": "Kenya's Three Philosophies",
                    "definition": (
                        "The interlocking ideological framework—African Socialism (the economic blueprint), Harambee (the community mobilization tool), "
                        "and Nyayoism (the ethical and political stabilizing guide)—that collectively guided Kenya's nation-building after 1963."
                    )
                }
            }
        ]
    },
    {
        "page_number": 2,
        "page_title": "Educational Video: National Philosophies in Kenya",
        "blocks": [
            {
                "block_type": "suggested_video",
                "component_type": "suggested_video",
                "title": "Revision Lecture: National Philosophies in Kenya (Form 4 History)",
                "content": {
                    "url": "https://www.youtube.com/watch?v=2TAtyWdo0YQ",
                    "text": "Comprehensive classroom lecture and examination walkthrough reviewing African Socialism, Harambee, and Nyayoism for Form 4 History.",
                    "author": "Dacwa Tv / Educational Video",
                    "licensing": "Standard YouTube License"
                }
            }
        ]
    },
    {
        "page_number": 3,
        "page_title": "Social Impacts of National Philosophies",
        "blocks": [
            {
                "block_type": "concept_explanation",
                "component_type": "concept_explanation",
                "title": "Transforming Education, Healthcare, and Culture",
                "content": {
                    "text": (
                        "The collective application of national philosophies generated deep social transformations:\n\n"
                        "1. **Educational Boom:** Harambee built thousands of secondary schools, African Socialism expanded free primary education, and Nyayoism expanded public universities and introduced school feeding.\n"
                        "2. **Healthcare Expansion:** Community-built dispensaries and state Nyayo Wards brought healthcare within walking distance of rural families.\n"
                        "3. **National Integration:** Emphasizing mutual social responsibility, love, and unity forged a shared national identity among 40+ ethnic groups.\n"
                        "4. **Social Welfare Safety Nets:** Fostered a culture of charity supporting orphans, the elderly, persons with disabilities, and emergency disaster victims.\n"
                        "5. **Cultural Dignity:** Preserved indigenous African traditions, communalism, and elder leadership models in modern statecraft."
                    )
                }
            }
        ]
    },
    {
        "page_number": 4,
        "page_title": "Five Social Impacts (Point-Form Revision)",
        "blocks": [
            {
                "block_type": "step_process",
                "component_type": "step_process",
                "title": "Examinable Social Impacts of National Philosophies",
                "content": {
                    "steps": [
                        "1. Massive Expansion of Educational Facilities: Thousands of primary and secondary classrooms, laboratories, and universities constructed.",
                        "2. Expansion of Rural Healthcare: Widespread construction of village dispensaries, maternity clinics, and specialized hospital Nyayo Wards.",
                        "3. Fostering National Coexistence: Bound diverse ethnic and religious groups into a unified national identity.",
                        "4. Creation of Welfare Safety Nets: Raised funds to assist disabled citizens, orphans, and famine victims.",
                        "5. Preservation of Indigenous African Culture: Integrated traditional communal values into modern economic and social planning."
                    ]
                }
            }
        ]
    },
    {
        "page_number": 5,
        "page_title": "Economic Impacts of National Philosophies",
        "blocks": [
            {
                "block_type": "concept_explanation",
                "component_type": "concept_explanation",
                "title": "Stimulating Agriculture, Industry, and Infrastructure",
                "content": {
                    "text": (
                        "The philosophies laid the structural foundation for Kenya's modern economy:\n\n"
                        "1. **Growth of the Cooperative Movement:** African Socialism organized smallholders into coffee, tea, and dairy cooperatives (KTDA, KCC), securing steady farmer incomes.\n"
                        "2. **Rural Infrastructure Expansion:** Harambees graded thousands of kilometers of feeder roads, built river bridges, and drilled community boreholes.\n"
                        "3. **Africanisation of Commerce:** Concessionary loans through ICDC transferred retail trade and small industries to indigenous Kenyan entrepreneurs.\n"
                        "4. **Agricultural Productivity:** Construction of communal cattle dips, terracing, and irrigation canals dramatically improved crop and livestock output.\n"
                        "5. **Growth of Tourism and Investment:** The Nyayo pillar of Peace ensured political stability, attracting international investors and millions of foreign tourists."
                    )
                }
            }
        ]
    },
    {
        "page_number": 6,
        "page_title": "Five Economic Impacts (Point-Form Revision)",
        "blocks": [
            {
                "block_type": "step_process",
                "component_type": "step_process",
                "title": "Examinable Economic Impacts of National Philosophies",
                "content": {
                    "steps": [
                        "1. Growth of the Cooperative Movement: Empowered small-scale farmers to collectively market produce and access credit.",
                        "2. Rural Infrastructure Development: Constructed access roads, water kiosks, and rural electrification networks.",
                        "3. Africanisation of the Economy: Transferred retail commerce from colonial monopolies to indigenous African citizens.",
                        "4. Agricultural and Livestock Enhancement: Built communal cattle dips and irrigation canals, boosting food security.",
                        "5. Promotion of Tourism and Investment: National peace and stability created a safe destination for international visitors."
                    ]
                }
            }
        ]
    },
    {
        "page_number": 7,
        "page_title": "Political Impacts of National Philosophies",
        "blocks": [
            {
                "block_type": "concept_explanation",
                "component_type": "concept_explanation",
                "title": "Shaping Patriotism, Democracy, and Diplomacy",
                "content": {
                    "text": (
                        "Politically, national philosophies shaped Kenya's sovereignty and global standing:\n\n"
                        "1. **Nationalism and Patriotism:** Inspired citizens to take pride in nation-building, reducing reliance on foreign assistance.\n"
                        "2. **Democratic Governance:** Groundwork in political democracy paved the way for multi-party politics and civil society participation.\n"
                        "3. **International Goodwill and Diplomacy:** Kenya's reputation for peace and stability enabled the nation to host major international headquarters (UNEP, UN-Habitat) and mediate regional peace accords (Sudan, Somalia)."
                    )
                }
            }
        ]
    },
    {
        "page_number": 8,
        "page_title": "Master Comparison Table: Kenya's Three National Philosophies",
        "blocks": [
            {
                "block_type": "comparison_table",
                "component_type": "comparison_table",
                "title": "Comprehensive Synthesis: African Socialism vs. Harambee vs. Nyayoism",
                "content": {
                    "headers": ["Philosophy", "Primary Architect & Year", "Core Slogan / Pillar", "Main Ideological Sources", "Primary Developmental Focus"],
                    "rows": [
                        ["African Socialism", "Tom Mboya & Jomo Kenyatta (1965)", "Sessional Paper No. 10 of 1965", "Traditional African values (Democracy & Mutual Social Responsibility)", "Mixed economy, progressive taxation, Africanisation, agricultural cooperatives."],
                        ["Harambee", "Mzee Jomo Kenyatta (1963)", "'Pulling Together'", "Traditional communal mutual assistance (Ngwatio, Saga, Mwethya)", "Grassroots bottom-up projects (schools, health dispensaries, cattle dips, rural roads)."],
                        ["Nyayoism", "Daniel Toroitich arap Moi (1978)", "'Peace, Love, and Unity'", "African Socialism, Biblical teachings, and Moi's political career", "Welfare programs (Nyayo milk, Nyayo wards, Jua Kali sheds, DFRD, Nyayo Tea Zones)."]
                    ]
                }
            }
        ]
    },
    {
        "page_number": 9,
        "page_title": "Interconnection: How the Three Philosophies Reinforce Each Other",
        "blocks": [
            {
                "block_type": "concept_explanation",
                "component_type": "concept_explanation",
                "title": "The Unified Framework of Kenyan Nation-Building",
                "content": {
                    "text": (
                        "The three national philosophies are not contradictory; they operate as complementary pillars of a single vision:\n\n"
                        "- **African Socialism** provided the overarching macro-economic and planning blueprint.\n"
                        "- **Harambee** served as the practical, grassroots mechanism to mobilize community labor and capital to implement that blueprint.\n"
                        "- **Nyayoism** provided the moral, ethical, and political stability (Peace, Love, Unity) required to sustain developmental projects over decades."
                    )
                }
            }
        ]
    },
    {
        "page_number": 10,
        "page_title": "Exam Coaching: Structuring Full-Mark Paper 2 Answers",
        "blocks": [
            {
                "block_type": "worked_example",
                "component_type": "worked_example",
                "title": "KCSE Answering Formula: Point + Explanation + Evidence",
                "content": {
                    "text": (
                        "To score maximum marks in KCSE Paper 2 essay questions, follow this exact structure:\n\n"
                        "- **1. POINT (1 mark):** State the clear historical point (e.g., *It stimulated agricultural and livestock productivity*).\n"
                        "- **2. EXPLANATION (0.5 marks):** Explain how the policy operated (e.g., *By pooling community contributions, farmers constructed communal veterinary infrastructure*).\n"
                        "- **3. EVIDENCE / EXAMPLE (0.5 marks):** Provide a concrete Kenyan historical example (e.g., *For example, building cattle dips to eradicate tick-borne diseases and establishing milk cooling centers for dairy cooperatives*)."
                    )
                }
            }
        ]
    },
    {
        "page_number": 11,
        "page_title": "Worked Example: Economic Impacts of National Philosophies",
        "blocks": [
            {
                "block_type": "worked_example",
                "component_type": "worked_example",
                "title": "KCSE Question: Explain Five Economic Impacts of National Philosophies in Kenya (10 Marks)",
                "content": {
                    "text": (
                        "**Model Answer (2 Marks per fully explained point):**\n\n"
                        "1. **Promotion of the Cooperative Movement:** Under African Socialism, the government facilitated agricultural cooperatives (coffee, tea, dairy), allowing smallholders to pool resources, access credit, and market crops collectively. (2 marks)\n\n"
                        "2. **Rural Infrastructure Development:** Harambee fundraisers enabled communities to grade access feeder roads, construct footbridges, and pipe clean water, linking rural farms to commercial urban markets. (2 marks)\n\n"
                        "3. **Africanisation of Commercial Commerce:** Through the Trade Licensing Act and ICDC loans, indigenous Kenyans acquired retail shops, transport fleets, and light industries previously dominated by foreigners. (2 marks)\n\n"
                        "4. **Boost to Informal Manufacturing (Jua Kali):** The Nyayo philosophy established permanent protective sheds, empowering informal artisans (blacksmiths, mechanics) to create self-employment. (2 marks)\n\n"
                        "5. **Growth of Tourism and Foreign Investment:** The Nyayo pillar of Peace ensured continuous political stability, making Kenya an attractive destination for international tourists and investors. (2 marks)"
                    )
                }
            }
        ]
    },
    {
        "page_number": 12,
        "page_title": "Worked Example: Social Achievements of African Socialism",
        "blocks": [
            {
                "block_type": "worked_example",
                "component_type": "worked_example",
                "title": "KCSE Question: Explain Five Social Achievements of Sessional Paper No. 10 of 1965 (10 Marks)",
                "content": {
                    "text": (
                        "**Model Answer (2 Marks per point):**\n\n"
                        "1. **Restoration of African Cultural Dignity:** Grounded development planning in traditional values, asserting that African cultural traditions were civilized and capable of guiding modern statecraft. (2 marks)\n\n"
                        "2. **Promotion of National Unity:** Emphasized that all citizens belonged to one national family, helping bridge ethnic divisions following colonial rule. (2 marks)\n\n"
                        "3. **Redistribution of Wealth Through Progressive Taxation:** Implemented graduated income taxes on higher earners to fund public healthcare, dispensaries, and primary schools for the poor. (2 marks)\n\n"
                        "4. **Foundation for Democratic Participation:** Championed political democracy and equality of all citizens, establishing the basis for multi-party democracy. (2 marks)\n\n"
                        "5. **Mobilization for Self-Help Development:** Inspired communities to adopt mutual social responsibility, laying the foundation for Harambee school construction. (2 marks)"
                    )
                }
            }
        ]
    },
    {
        "page_number": 13,
        "page_title": "Primary Source Case Study: The Bura Irrigation Scheme",
        "blocks": [
            {
                "block_type": "callout",
                "component_type": "callout",
                "title": "Historical Inquiry: The Bura Irrigation Scheme and Corruption",
                "content": {
                    "text": (
                        "**Historical Fact:** In the late 1970s and 1980s, the government launched the Bura Irrigation Scheme along the Tana River under the principles of African Socialism to settle landless families and produce cotton. However, due to political patronage, massive mismanagement, and embezzlement of millions in World Bank loans, the project collapsed.\n\n"
                        "**Analytical Inquiry:**\n"
                        "1. **Identify Challenge:** How did corruption and political interference undermine noble socialist planning goals in the Bura project?\n"
                        "2. **KCSE Connection:** Explain why state-run parastatals often failed to fulfill the promises of Sessional Paper No. 10."
                    )
                }
            }
        ]
    },
    {
        "page_number": 14,
        "page_title": "Interactive Master Classification Activity",
        "blocks": [
            {
                "block_type": "mini_activity",
                "component_type": "mini_activity",
                "title": "Assign the Concept to the Correct National Philosophy",
                "content": {
                    "instruction": "Test your mastery across the three national philosophies (African Socialism, Harambee, or Nyayoism):",
                    "items": [
                        "1. Sessional Paper No. 10 of 1965 and Progressive Taxation -> **African Socialism**",
                        "2. Grassroots self-help fundraisers for classrooms and cattle dips -> **Harambee**",
                        "3. Core pillars of Peace, Love, and Unity -> **Nyayoism**",
                        "4. Trade Licensing Act and Africanisation through ICDC loans -> **African Socialism**",
                        "5. Nyayo Milk Programme, Nyayo Wards, and Jua Kali Sheds -> **Nyayoism**",
                        "6. Public Officer Ethics Act banning public servant collections -> **Harambee**"
                    ]
                }
            }
        ]
    },
    {
        "page_number": 15,
        "page_title": "Topic 4 Comprehensive Mastery Check (Part 1)",
        "blocks": [
            {
                "block_type": "knowledge_check",
                "component_type": "knowledge_check",
                "title": "Topic 4 Mastery Assessment (Part 1)",
                "content": {
                    "questions": [
                        {
                            "question": "Which of the following describes the 'mixed economy' model adopted under African Socialism?",
                            "options": [
                                "Total state ownership of all land and factories with no private property",
                                "A combination of private enterprise, state parastatals, and cooperative societies",
                                "Complete reliance on foreign multinational companies without state regulation",
                                "A barter trade economy without national currency"
                            ],
                            "correct_answer": 1,
                            "explanation": "A mixed economy combines private enterprise with state parastatals and cooperatives."
                        },
                        {
                            "question": "Which principle of Harambee requires that projects must be undertaken voluntarily without police or administrative force?",
                            "options": [
                                "Collective Good",
                                "Volition",
                                "Felt Needs",
                                "Maximum Local Resources"
                            ],
                            "correct_answer": 1,
                            "explanation": "Volition means voluntary participation without coercion or forced seizure of property."
                        }
                    ]
                }
            }
        ]
    },
    {
        "page_number": 16,
        "page_title": "Topic 4 Comprehensive Mastery Check (Part 2)",
        "blocks": [
            {
                "block_type": "knowledge_check",
                "component_type": "knowledge_check",
                "title": "Topic 4 Mastery Assessment (Part 2)",
                "content": {
                    "questions": [
                        {
                            "question": "What was the primary environmental objective of establishing the Nyayo Tea Zones Development Corporation?",
                            "options": [
                                "To privatize all national parks in Kenya",
                                "To create continuous tea buffer strips around public gazetted forests to prevent human encroachment and deforestation",
                                "To export tea exclusively to the Soviet Union",
                                "To replace all coffee farming in Central Kenya"
                            ],
                            "correct_answer": 1,
                            "explanation": "Nyayo Tea Zones formed physical green buffer strips around major forests to prevent illegal logging and encroachment."
                        },
                        {
                            "question": "Which legislation barred public servants from playing leading roles in collecting Harambee funds to curb corruption?",
                            "options": [
                                "The Public Officer Ethics Act (2003)",
                                "The Trade Licensing Act (1967)",
                                "The Chiefs Authority Act (1975)",
                                "The Sessional Paper No. 10 Act"
                            ],
                            "correct_answer": 0,
                            "explanation": "The Public Officer Ethics Act of 2003 barred public servants from presiding over or collecting Harambee funds."
                        }
                    ]
                }
            }
        ]
    },
    {
        "page_number": 17,
        "page_title": "Topic 4 Master Summary",
        "blocks": [
            {
                "block_type": "summary",
                "component_type": "summary",
                "title": "Topic 4 Comprehensive Master Summary: National Philosophies in Kenya",
                "content": {
                    "text": (
                        "• **African Socialism (1965):** Codified in Sessional Paper No. 10 under Tom Mboya and Jomo Kenyatta; anchored on political democracy and mutual social responsibility; created a mixed economy, progressive taxation, cooperatives, and Africanisation.\n"
                        "• **Harambee (1963):** Championed by Jomo Kenyatta as the National Motto; guided by 4 principles (collective good, volition, felt needs, local resources); built thousands of classrooms, dispensaries, cattle dips, and feeder roads; reformed via the Public Officer Ethics Act (2003).\n"
                        "• **Nyayoism (1978):** Formulated by Daniel arap Moi pledging to follow Kenyatta's footsteps; guided by Peace, Love, and Unity; implemented Nyayo Milk, Nyayo Wards, Jua Kali sheds, DFRD decentralization, and public university expansion.\n"
                        "• **Cumulative Impact:** Drove educational boom, healthcare expansion, cooperative wealth, Africanisation of retail trade, national cohesion, and political stability."
                    )
                }
            }
        ]
    },
    {
        "page_number": 18,
        "page_title": "Final Exam Revision Checklist",
        "blocks": [
            {
                "block_type": "step_process",
                "component_type": "step_process",
                "title": "Exam Revision Checklist: Topics 1–4",
                "content": {
                    "steps": [
                        "1. Sessional Paper No. 10 of 1965: Background, 2 pillars, 6 features, mixed economy, achievements, challenges.",
                        "2. Harambee Movement: Origin, Kenyatta's role, Coat of Arms, 4 principles, 3 project categories.",
                        "3. Harambee Performance: 8 educational contributions, general socio-economic impacts, 6 systemic challenges, Public Officer Ethics Act.",
                        "4. Nyayo Philosophy: 1978 origin, 3 pillars (Peace, Love, Unity), 3 sources, key programs (Milk, Wards, Jua Kali, Tea Zones, DFRD).",
                        "5. Master Impacts: Social, Economic, and Political outcomes since independence."
                    ]
                }
            }
        ]
    }
]


ALL_LESSONS = [
    {
        "unit_order": 1,
        "unit_name": "African Socialism — Meaning, Origin, and Features",
        "lesson_title": "African Socialism: Origins, Principles, and Features",
        "pages": LESSON_1_PAGES
    },
    {
        "unit_order": 2,
        "unit_name": "Harambee Philosophy — Meaning, Principles, and Categories",
        "lesson_title": "The Harambee Philosophy: Origins, Principles, and Categories",
        "pages": LESSON_2_PAGES
    },
    {
        "unit_order": 3,
        "unit_name": "Harambee's Contributions and Challenges",
        "lesson_title": "Harambee in National Development: Contributions and Challenges",
        "pages": LESSON_3_PAGES
    },
    {
        "unit_order": 4,
        "unit_name": "Nyayo Philosophy — Origins, Pillars, and Sources",
        "lesson_title": "The Nyayo Philosophy: Origins, Pillars, and Development Programs",
        "pages": LESSON_4_PAGES
    },
    {
        "unit_order": 5,
        "unit_name": "Cumulative Impact and Synthesis of National Philosophies",
        "lesson_title": "Cumulative Impacts and Synthesis of Kenya's National Philosophies",
        "pages": LESSON_5_PAGES
    }
]


# ===========================================================================
# DATABASE INGESTION RUNNER
# ===========================================================================

def run_ingestion(replace=False):
    print("=" * 80)
    print("VLEARN CURRICULUM INGESTION: FORM 4 HISTORY — TOPIC 4 (NATIONAL PHILOSOPHIES)")
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
            name="National Philosophies (Kenya)",
            defaults={"order": 4}
        )
        if topic_created:
            print(f"[+] Created Topic: {topic.name} (Order: {topic.order})")
        else:
            topic.order = 4
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
        print(f"[SUCCESS] Form 4 History Topic 4 Ingestion Complete!")
        print(f"[*] Total Lessons Ingested: {len(ALL_LESSONS)}")
        print(f"[*] Total Pages Ingested:   {total_pages}")
        print(f"[*] Total Blocks Ingested:  {total_blocks}")
        print(f"[*] Total Media Assets:     {total_assets}")
        print("=" * 80)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Ingest Form 4 History Topic 4")
    parser.add_argument("--replace", action="store_true", help="Replace existing blocks with a fresh rebuild")
    args = parser.parse_args()

    run_ingestion(replace=args.replace)
