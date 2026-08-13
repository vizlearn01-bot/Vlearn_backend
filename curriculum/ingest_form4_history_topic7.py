"""
VLearn Curriculum Ingestion Engine: Form 4 History — Topic 7 (Devolved Government / Local Authorities in Kenya)

Target Subject: History (Subject ID: 17)
Grade: Form 4 (Grade ID: 4)
Curriculum: 844 (Curriculum ID: 4)

Topic 7: Devolved Government (Order: 7)
  - Unit 1: Historical Development of Local Government (Colonial Era to 1963) (Lesson 1: 15 Pages)
  - Unit 2: Local Authorities under the Local Government Act (Cap 265) (Lesson 2: 15 Pages)
  - Unit 3: Transition to Devolution and County Governments (Lesson 3: 15 Pages)
  - Unit 4: Structures, Functions, and Finances of County Governments (Lesson 4: 16 Pages)
  - Unit 5: Relationship and Intergovernmental Relations in Devolution (Lesson 5: 18 Pages)

Total: 5 Learning Units, 5 Lessons, 79 Pages, 90+ Blocks, 8 Media Assets (3 Wikimedia Photos + 5 Verified YouTube Videos)

Usage:
  ./venv/bin/python curriculum/ingest_form4_history_topic7.py --replace
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
# LESSON DEFINITIONS: FORM 4 HISTORY TOPIC 7
# ===========================================================================

LESSON_1_PAGES = [
    {
        "page_number": 1,
        "page_title": "Historical Development of Local Government (Colonial Era to 1963)",
        "blocks": [
            {
                "block_type": "learning_goal",
                "component_type": "learning_goal",
                "title": "Lesson Objectives: Colonial Local Government Origins",
                "content": {
                    "text": (
                        "By the end of this lesson, you will be able to:\n"
                        "- Explain why the British colonial administration established local government structures in Kenya\n"
                        "- Trace the historical transition from District Advisory Councils to Local Native Councils (1924) and African District Councils (1948)\n"
                        "- Analyze the objectives, achievements, and structural limitations of Local Native Councils (LNCs)\n"
                        "- Evaluate the factors that undermined colonial local authorities"
                    )
                }
            },
            {
                "block_type": "definition_card",
                "component_type": "definition_card",
                "title": "Concept: Colonial Local Administration",
                "content": {
                    "term": "Local Native Councils (LNCs)",
                    "definition": (
                        "Grassroots administrative bodies established by the British colonial government under the Native Authority Ordinance in 1924 "
                        "to manage local social services, collect local levies, and contain African political grievances within designated native reserves."
                    )
                }
            }
        ]
    },
    {
        "page_number": 2,
        "page_title": "Evolutionary Timeline of Colonial Local Government",
        "blocks": [
            {
                "block_type": "step_process",
                "component_type": "step_process",
                "title": "Historical Progression (1902–1963)",
                "content": {
                    "steps": [
                        "1. Village Headman Ordinance (1902): Empowered Provincial Commissioners to appoint native headmen to collect hut tax and enforce labor orders.",
                        "2. Native Authority Ordinance (1922): Established District Advisory Councils (DACs) presided over by European District Commissioners.",
                        "3. Local Native Councils (LNCs) (1924): Replaced DACs, giving educated African leaders a controlled legal forum to debate local welfare issues and levy local rates.",
                        "4. African District Councils (ADCs) (1948): Replaced LNCs, introducing elected African majorities and culminating in 1958 with Pascal Nabwane becoming the first African Chairman.",
                        "5. Independence Transition (1963): ADCs formed the foundation for post-independence County and Municipal Councils under Cap 265."
                    ]
                }
            }
        ]
    },
    {
        "page_number": 3,
        "page_title": "Why the British Introduced Local Government in Kenya",
        "blocks": [
            {
                "block_type": "concept_explanation",
                "component_type": "concept_explanation",
                "title": "Six Core Motives for Colonial Local Governance",
                "content": {
                    "text": (
                        "The British administration established local government structures due to administrative and strategic necessities:\n\n"
                        "- **Shortage of European Personnel:** Britain lacked sufficient administrative officers to govern all territories directly, necessitating local African chiefs and councils.\n"
                        "- **Reducing Administrative Costs:** Shifting the financial burden of local services onto Africans through local taxes and communal labor.\n"
                        "- **Mobilization of Local Resources:** Harnessing local labor, cattle dips, and agricultural markets to support the colonial economy.\n"
                        "- **Legal Forum for Grievances:** Providing mission-educated elites with a controlled platform to articulate grievances without forming radical political movements.\n"
                        "- **Containment within Reserves:** Restricting African political organization strictly within designated ethnic reserves.\n"
                        "- **Protection of Settler Interests:** Creating separate settler-run county councils in the White Highlands to preserve European privileges."
                    )
                }
            }
        ]
    },
    {
        "page_number": 4,
        "page_title": "Historical Documentary: Colonial Governance in Kenya",
        "blocks": [
            {
                "block_type": "suggested_video",
                "component_type": "suggested_video",
                "title": "Historical Documentary: British Rule and Grassroots Administration in Kenya",
                "content": {
                    "url": "https://www.youtube.com/watch?v=KuWacZkACnw",
                    "text": "Examine the methods used by the British colonial government to enforce indirect rule, levy taxes, and establish grassroots administrative councils in Kenya.",
                    "author": "The Untold Africa / Historical Documentaries",
                    "licensing": "Standard YouTube License"
                }
            }
        ]
    },
    {
        "page_number": 5,
        "page_title": "Objectives of Local Native Councils (LNCs)",
        "blocks": [
            {
                "block_type": "step_process",
                "component_type": "step_process",
                "title": "Colonial Mandate of LNCs (1924)",
                "content": {
                    "steps": [
                        "1. Encouraging Responsibility: Developing basic administrative and fiscal responsibility among local African leaders.",
                        "2. Articulating Grievances: Providing an orderly mechanism for educated Africans to express complaints under District Commissioner supervision.",
                        "3. Ensuring Containment: Confining African political energy strictly to district and ethnic reserve boundaries.",
                        "4. Enhancing Colonial Surveillance: Allowing the colonial government to study African customs and social dynamics to maintain effective control."
                    ]
                }
            }
        ]
    },
    {
        "page_number": 6,
        "page_title": "Achievements of LNCs and ADCs",
        "blocks": [
            {
                "block_type": "concept_explanation",
                "component_type": "concept_explanation",
                "title": "Grassroots Development Milestones",
                "content": {
                    "text": (
                        "Despite tight colonial supervision, LNCs and ADCs achieved significant milestones:\n\n"
                        "- **Social Infrastructure:** Constructed and maintained primary schools, dispensaries, maternity centers, and cattle dips.\n"
                        "- **Feeder Roads and Bridges:** Built local access roads linking farming reserves to colonial trading centers and railway stations.\n"
                        "- **Local Revenue Collection:** Levied local cesses, trade licenses, and rates to self-finance council projects.\n"
                        "- **District African Courts:** Arbitrated customary civil matters, land disputes, and domestic conflicts.\n"
                        "- **Nurturing African Leadership:** Provided training grounds for pioneer nationalist leaders (such as James Gichuru and Oginga Odinga)."
                    )
                }
            }
        ]
    },
    {
        "page_number": 7,
        "page_title": "Factors That Undermined Colonial Local Government",
        "blocks": [
            {
                "block_type": "step_process",
                "component_type": "step_process",
                "title": "Systemic Constraints on LNCs and ADCs",
                "content": {
                    "steps": [
                        "1. Acute Shortage of Skilled Personnel: Severe lack of Africans with accounting, engineering, and administrative training.",
                        "2. Weak Financial Tax Base: African reserves had low incomes and were initially banned from growing profitable cash crops like coffee.",
                        "3. Racial Funding Disparity: The colonial state heavily subsidized European county councils in the White Highlands while African councils relied on meager self-help.",
                        "4. Strict District Commissioner Veto: European DCs chaired council meetings, controlled agendas, and held absolute power to veto African proposals.",
                        "5. Nationalist Disruption: From the late 1940s, Mau Mau and nationalist agitation disrupted the authority of colonial-appointed chiefs and councillors."
                    ]
                }
            }
        ]
    },
    {
        "page_number": 8,
        "page_title": "Comparative Table: LNCs (1924) vs. ADCs (1948)",
        "blocks": [
            {
                "block_type": "comparison_table",
                "component_type": "comparison_table",
                "title": "Comparison: Local Native Councils vs. African District Councils",
                "content": {
                    "headers": ["Feature", "Local Native Councils (LNCs, 1924)", "African District Councils (ADCs, 1948)"],
                    "rows": [
                        ["Leadership", "Chaired strictly ex-officio by European District Commissioners.", "Transitioned to elected African Chairmen (e.g., Pascal Nabwane in 1958)."],
                        ["Membership", "Dominated by colonial-appointed chiefs and headmen.", "Included an increasing majority of democratically elected African councillors."],
                        ["Revenue Powers", "Limited local cesses on grain and cattle.", "Broader tax base, including commercial licensing and agricultural cooperatives."],
                        ["Political Voice", "Strictly confined to localized ethnic reserve welfare.", "Gradually integrated with broader national political discourse leading to 1963 independence."]
                    ]
                }
            }
        ]
    },
    {
        "page_number": 9,
        "page_title": "Interactive Classification: Colonial Local Government",
        "blocks": [
            {
                "block_type": "mini_activity",
                "component_type": "mini_activity",
                "title": "Match the Colonial Legislation to Its Impact",
                "content": {
                    "instruction": "Test your mastery of colonial administrative laws in Kenya:",
                    "items": [
                        "1. 1902 law empowering PCs to appoint native headmen -> **Village Headman Ordinance**",
                        "2. 1924 body created to provide a legal forum for educated Africans in reserves -> **Local Native Councils (LNCs)**",
                        "3. 1948 councils that succeeded LNCs with increased elected African members -> **African District Councils (ADCs)**",
                        "4. First African Chairman of an ADC elected in 1958 -> **Pascal Nabwane**"
                    ]
                }
            }
        ]
    },
    {
        "page_number": 10,
        "page_title": "KCSE Examination Coaching: Reasons for Colonial Local Government",
        "blocks": [
            {
                "block_type": "worked_example",
                "component_type": "worked_example",
                "title": "KCSE Question: Explain Five Reasons Why the British Established Local Government in Kenya (10 Marks)",
                "content": {
                    "text": (
                        "**Model Answer (Point + Explanation = 2 Marks per Point):**\n\n"
                        "1. **Shortage of European Administrative Staff:** The British colonial administration lacked sufficient white officers to manage all rural districts directly, making local chiefs and councils essential. (2 marks)\n\n"
                        "2. **Reduction of Administrative Expenses:** Establishing local councils shifted the financial cost of schools, dispensaries, and roads directly onto Africans through local tax levies. (2 marks)\n\n"
                        "3. **Mobilization of Local Resources and Labor:** Local councils provided a structured mechanism to organize communal labor for road construction and agricultural projects. (2 marks)\n\n"
                        "4. **Containment of African Political Agitation:** Councils were deliberately designed to confine African political ambitions strictly within ethnic reserves, preventing national unity movements. (2 marks)\n\n"
                        "5. **Provision of a Controlled Forum for Grievances:** LNCs offered educated Africans a legal outlet to express complaints under the watchful eye of the District Commissioner. (2 marks)"
                    )
                }
            }
        ]
    },
    {
        "page_number": 11,
        "page_title": "KCSE Examination Coaching: Challenges of Colonial Local Authorities",
        "blocks": [
            {
                "block_type": "worked_example",
                "component_type": "worked_example",
                "title": "KCSE Question: Explain Five Factors That Undermined Local Authorities During Colonial Rule (10 Marks)",
                "content": {
                    "text": (
                        "**Model Answer (Point + Explanation = 2 Marks per Point):**\n\n"
                        "1. **Acute Shortage of Skilled Personnel:** Lack of Africans with formal training in accounting, civil engineering, and public administration crippled council operations. (2 marks)\n\n"
                        "2. **Weak Local Revenue Base:** African reserves had low incomes and were long prohibited from growing profitable cash crops, resulting in insufficient revenue. (2 marks)\n\n"
                        "3. **Racial Discrimination in Resource Allocation:** The colonial government allocated generous grants to European councils in the White Highlands while starving African councils. (2 marks)\n\n"
                        "4. **Overbearing District Commissioner Veto:** European DCs exercised total control over meetings and could nullify any resolution passed by African members. (2 marks)\n\n"
                        "5. **Poor Transport and Communication Infrastructure:** Impassable feeder roads and lack of telecommunications isolated reserves and delayed development projects. (2 marks)"
                    )
                }
            }
        ]
    },
    {
        "page_number": 12,
        "page_title": "Check Your Understanding: Module 7.1",
        "blocks": [
            {
                "block_type": "knowledge_check",
                "component_type": "knowledge_check",
                "title": "Module 7.1 Assessment",
                "content": {
                    "questions": [
                        {
                            "question": "In what year were Local Native Councils (LNCs) established in colonial Kenya?",
                            "options": [
                                "1902",
                                "1924",
                                "1948",
                                "1958"
                            ],
                            "correct_answer": 1,
                            "explanation": "Local Native Councils were established in 1924 to replace District Advisory Councils."
                        },
                        {
                            "question": "Who was the first African Chairman of an African District Council (ADC) in Kenya in 1958?",
                            "options": [
                                "James Gichuru",
                                "Pascal Nabwane",
                                "Oginga Odinga",
                                "Tom Mboya"
                            ],
                            "correct_answer": 1,
                            "explanation": "Pascal Nabwane made history in 1958 as the first African Chairman of an ADC (Elgon Nyanza ADC)."
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
                "title": "Core Summary: Colonial Local Governance",
                "content": {
                    "text": (
                        "• **Origins:** Started with the 1902 Village Headman Ordinance, evolving into LNCs (1924) and ADCs (1948).\n"
                        "• **British Motives:** Cut costs, overcome European manpower shortages, mobilize resources, and contain African politics within ethnic reserves.\n"
                        "• **Achievements:** Built schools, dispensaries, cattle dips, feeder roads, collected local rates, and arbitrated civil disputes.\n"
                        "• **Limitations:** Racial funding disparities, DC vetoes, lack of skilled manpower, and poor infrastructure."
                    )
                }
            },
            {
                "block_type": "key_takeaway",
                "component_type": "key_takeaway",
                "title": "Key Takeaways",
                "content": {
                    "text": (
                        "- Colonial local authorities were designed for control and cost-cutting rather than democratic empowerment.\n"
                        "- Despite restrictions, they laid the foundation for grassroots African administrative leadership."
                    )
                }
            }
        ]
    },
    {
        "page_number": 14,
        "page_title": "Revision Checklist: Colonial Local Government",
        "blocks": [
            {
                "block_type": "step_process",
                "component_type": "step_process",
                "title": "Mastery Checklist",
                "content": {
                    "steps": [
                        "1. Evolution: 1902 Headman Ordinance -> 1924 LNCs -> 1948 ADCs -> 1958 Pascal Nabwane.",
                        "2. Six reasons why the British established local authorities.",
                        "3. Four objectives of Local Native Councils.",
                        "4. Five achievements and five challenges of colonial local councils."
                    ]
                }
            }
        ]
    },
    {
        "page_number": 15,
        "page_title": "Quick Knowledge Check: Colonial Local Authorities",
        "blocks": [
            {
                "block_type": "mini_activity",
                "component_type": "mini_activity",
                "title": "Quick Recall Quiz",
                "content": {
                    "instruction": "Answer true or false:",
                    "items": [
                        "1. The British introduced LNCs to encourage national political parties -> **False (to contain politics to ethnic reserves)**",
                        "2. African councils built cattle dips, markets, and feeder roads -> **True**",
                        "3. European District Commissioners originally presided over LNC meetings as chairmen -> **True**"
                    ]
                }
            }
        ]
    }
]

LESSON_2_PAGES = [
    {
        "page_number": 1,
        "page_title": "Local Authorities under the Local Government Act (Cap 265)",
        "blocks": [
            {
                "block_type": "learning_goal",
                "component_type": "learning_goal",
                "title": "Lesson Objectives: The Pre-2010 Local Government System",
                "content": {
                    "text": (
                        "By the end of this lesson, you will be able to:\n"
                        "- Describe the structure of local authorities under the Local Government Act (Cap 265)\n"
                        "- Distinguish between the four categories of councils (Municipal, Town, County, and Urban Councils)\n"
                        "- Explain the roles of elected councillors, nominated councillors, Mayors, and Town Clerks\n"
                        "- Analyze the core functions and systemic failures that plagued the Cap 265 system"
                    )
                }
            },
            {
                "block_type": "definition_card",
                "component_type": "definition_card",
                "title": "Concept: Local Authorities Under Cap 265",
                "content": {
                    "term": "Local Government Act (Cap 265)",
                    "definition": (
                        "The statutory framework governing local administration in Kenya from independence in 1963 until 2010, "
                        "which placed over 175 local councils under the direct supervisory control of the Minister for Local Government."
                    )
                }
            }
        ]
    },
    {
        "page_number": 2,
        "page_title": "Nairobi City Hall and Urban Governance",
        "blocks": [
            {
                "block_type": "suggested_image",
                "component_type": "suggested_image",
                "title": "Nairobi City Hall",
                "content": {
                    "text": "Nairobi City Hall, historic seat of the pre-2010 Nairobi City Council and current headquarters of Nairobi City County Government.",
                    "url": "https://upload.wikimedia.org/wikipedia/commons/d/dc/Nairobi_City_Hall.jpg",
                    "author": "Public Domain / Wikimedia Commons",
                    "licensing": "Public Domain",
                    "commons_page_url": "https://commons.wikimedia.org/wiki/File:Nairobi_City_Hall.jpg"
                }
            }
        ]
    },
    {
        "page_number": 3,
        "page_title": "Four Types of Local Authorities Under Cap 265",
        "blocks": [
            {
                "block_type": "step_process",
                "component_type": "step_process",
                "title": "Categories of Councils",
                "content": {
                    "steps": [
                        "1. Municipal Councils: Established in major commercial cities and large urban centers (e.g., Nairobi City Council, Mombasa, Kisumu, Nakuru, Eldoret). Headed by a Mayor elected by councillors.",
                        "2. Town Councils: Created in medium-sized growing urban centers. Headed by a Council Chairman elected by councillors.",
                        "3. County Councils: Established in rural districts to manage rural development, land adjudication, and feeder roads. Headed by a Chairman.",
                        "4. Urban Councils: Formed in smaller commercial centers within county council boundaries, operating under the oversight of parent County Councils."
                    ]
                }
            }
        ]
    },
    {
        "page_number": 4,
        "page_title": "Council Leadership and Administration",
        "blocks": [
            {
                "block_type": "comparison_table",
                "component_type": "comparison_table",
                "title": "Political vs. Administrative Arms Under Cap 265",
                "content": {
                    "headers": ["Role", "Method of Appointment", "Core Responsibilities & Powers"],
                    "rows": [
                        ["Elected Councillors", "Elected by registered voters in electoral wards during general elections.", "Represent ward interests, debate local by-laws, sit on council committees."],
                        ["Nominated Councillors", "Appointed by the Minister for Local Government.", "Intended to represent special community interests, but often used for political patronage."],
                        ["Mayor / Council Chairman", "Elected bi-annually by fellow councillors.", "Political head of the council; chairs council meetings and ceremonial functions."],
                        ["Town / County Clerk", "Appointed by the Public Service Commission (Central Govt).", "Chief Executive and Accounting Officer; manages civil service staff and finances."]
                    ]
                }
            }
        ]
    },
    {
        "page_number": 5,
        "page_title": "Educational Video: Pre-2010 Local Government Concepts",
        "blocks": [
            {
                "block_type": "suggested_video",
                "component_type": "suggested_video",
                "title": "Educational Video: Structures and Concepts of Local Government",
                "content": {
                    "url": "https://www.youtube.com/watch?v=48EYath0xxg",
                    "text": "Review the fundamental principles of local government, municipal councils, by-laws, and grassroots service delivery.",
                    "author": "Civics Academy / Public Governance",
                    "licensing": "Standard YouTube License"
                }
            }
        ]
    },
    {
        "page_number": 6,
        "page_title": "Key Functions of Pre-2010 Local Authorities",
        "blocks": [
            {
                "block_type": "step_process",
                "component_type": "step_process",
                "title": "Statutory Functions Under Cap 265",
                "content": {
                    "steps": [
                        "1. Regulatory Services: Enacting and enforcing local council by-laws to regulate business hours, hawking, construction, and public sanitation.",
                        "2. Trade and Markets: Constructing, maintaining, and licensing municipal markets, slaughterhouses, and open-air trading centers.",
                        "3. Public Health: Providing garbage collection, refuse disposal, pest control, and running municipal health dispensaries.",
                        "4. Transport & Infrastructure: Building local access roads, maintaining street lighting, bus parks, and managing parking meters.",
                        "5. Social & Educational Amenities: Operating nursery schools (pre-primary), village polytechnics, public libraries, sports stadiums, and public cemeteries."
                    ]
                }
            }
        ]
    },
    {
        "page_number": 7,
        "page_title": "Systemic Failures of the Cap 265 Local Authority System",
        "blocks": [
            {
                "block_type": "concept_explanation",
                "component_type": "concept_explanation",
                "title": "Why Did the Pre-2010 System Collapse?",
                "content": {
                    "text": (
                        "The pre-2010 system suffered from crippling structural and governance defects:\n\n"
                        "- **Excessive Centralization:** The Minister for Local Government held absolute powers to dissolve councils, nominate councillors, and veto local resolutions, destroying local autonomy.\n"
                        "- **Financial Starvation:** Councils relied on weak local rates and delayed central government grants (LATF), leaving them perpetually broke.\n"
                        "- **Rampant Corruption & Land Grabbing:** Massive embezzlement, payrolls packed with 'ghost workers', and illegal grabbing of public utility plots (playgrounds, markets).\n"
                        "- **Mayor vs. Clerk Rivalry:** Persistent power struggles between elected Mayors (political heads) and appointed Clerks (accounting officers).\n"
                        "- **Uncontrolled Slum Expansion:** Rapid urbanization overwhelmed municipal capacities, resulting in uncollected garbage and sprawling informal settlements."
                    )
                }
            }
        ]
    },
    {
        "page_number": 8,
        "page_title": "Mayor vs. Town Clerk: The Institutional Clash",
        "blocks": [
            {
                "block_type": "callout",
                "component_type": "callout",
                "title": "Historical Inquiry: The Duality of Executive Power",
                "content": {
                    "text": (
                        "**The Problem:**\n"
                        "Under Cap 265, the **Mayor** was elected by councillors and was the political face of the city, but held **no financial or executive authority**. The **Town Clerk** was appointed by the Central Government and controlled all tenders, finances, and staff.\n\n"
                        "**Consequences:**\n"
                        "- Friction and paralysis whenever Mayors attempted to implement policies without Clerk approval.\n"
                        "- Central government used Town Clerks to undermine opposition-led municipal councils in urban centers like Nairobi, Kisumu, and Mombasa."
                    )
                }
            }
        ]
    },
    {
        "page_number": 9,
        "page_title": "Interactive Classification: Pre-2010 Local Authorities",
        "blocks": [
            {
                "block_type": "mini_activity",
                "component_type": "mini_activity",
                "title": "Classify the Council Category",
                "content": {
                    "instruction": "Match each Kenyan local authority to its correct Cap 265 category:",
                    "items": [
                        "1. Nairobi, Mombasa, Kisumu, Nakuru -> **Municipal Council**",
                        "2. Council managing a rural administrative district -> **County Council**",
                        "3. Small trading center operating under a parent county council -> **Urban Council**",
                        "4. Medium-sized expanding urban trading center -> **Town Council**"
                    ]
                }
            }
        ]
    },
    {
        "page_number": 10,
        "page_title": "KCSE Examination Coaching: Challenges of Pre-2010 Councils",
        "blocks": [
            {
                "block_type": "worked_example",
                "component_type": "worked_example",
                "title": "KCSE Question: Explain Five Challenges Faced by Local Authorities Under Cap 265 (10 Marks)",
                "content": {
                    "text": (
                        "**Model Answer (Point + Explanation = 2 Marks per Point):**\n\n"
                        "1. **Over-Centralization and Ministerial Interference:** The Minister for Local Government possessed absolute veto powers to dissolve councils and overturn decisions, eliminating local independence. (2 marks)\n\n"
                        "2. **Inadequate Financial Resources:** Councils suffered from a narrow tax base, massive default on property rates, and delayed remittances of central funds (LATF). (2 marks)\n\n"
                        "3. **Pervasive Corruption and Mismanagement:** Embezzlement of funds, fraudulent procurement tenders, and illegal grabbing of council land crippled service delivery. (2 marks)\n\n"
                        "4. **Shortage of Qualified Technical Personnel:** Many councils lacked qualified engineers, town planners, and accountants, leading to unplanned urban growth. (2 marks)\n\n"
                        "5. **Rapid Urbanization and Slum Growth:** Massive influx of rural migrants overwhelmed sanitation, water supply, and garbage collection capacities in major towns. (2 marks)"
                    )
                }
            }
        ]
    },
    {
        "page_number": 11,
        "page_title": "KCSE Examination Coaching: Functions of Local Councils",
        "blocks": [
            {
                "block_type": "worked_example",
                "component_type": "worked_example",
                "title": "KCSE Question: State Five Functions of Municipal Councils Under Cap 265 (5 Marks)",
                "content": {
                    "text": (
                        "**Model Answer (1 Mark per distinct point):**\n\n"
                        "1. Passing local by-laws to regulate public order, health, and trade within the municipality. (1 mark)\n"
                        "2. Providing and maintaining public markets, slaughterhouses, and trading centers. (1 mark)\n"
                        "3. Managing public health services, including garbage collection and sewage disposal. (1 mark)\n"
                        "4. Constructing and maintaining local access feeder roads, streetlights, and bus parks. (1 mark)\n"
                        "5. Establishing and running nursery schools, day-care centers, and village polytechnics. (1 mark)"
                    )
                }
            }
        ]
    },
    {
        "page_number": 12,
        "page_title": "Check Your Understanding: Module 7.2",
        "blocks": [
            {
                "block_type": "knowledge_check",
                "component_type": "knowledge_check",
                "title": "Module 7.2 Assessment",
                "content": {
                    "questions": [
                        {
                            "question": "Who was the chief executive and accounting officer of a pre-2010 Municipal Council?",
                            "options": [
                                "The Mayor",
                                "The Town Clerk",
                                "The Provincial Commissioner",
                                "The Minister for Local Government"
                            ],
                            "correct_answer": 1,
                            "explanation": "The Town Clerk was appointed by the Public Service Commission as the council's accounting officer."
                        },
                        {
                            "question": "Which of the following was a major weakness of the Cap 265 Local Authorities system?",
                            "options": [
                                "Complete absence of local taxes",
                                "The Minister for Local Government held absolute powers to dissolve councils and veto decisions",
                                "Lack of registered voters",
                                "Councils were prohibited from building markets"
                            ],
                            "correct_answer": 1,
                            "explanation": "Ministerial interference and lack of constitutional autonomy were primary causes of council failure."
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
                "title": "Core Summary: The Pre-2010 Local Government System",
                "content": {
                    "text": (
                        "• **Structure:** 4 Council categories (Municipal, Town, County, Urban) under Cap 265.\n"
                        "• **Leadership Duality:** Elected Mayors (ceremonial/political) clashed with Central Government-appointed Town Clerks (executive/accounting).\n"
                        "• **Functions:** Regulatory by-laws, markets, sanitation, access roads, nursery schools, polytechnics.\n"
                        "• **Systemic Collapse:** Ministerial vetoes, financial starvation, rampant graft, ghost workers, and slum expansion prompted the 2010 devolution reform."
                    )
                }
            },
            {
                "block_type": "key_takeaway",
                "component_type": "key_takeaway",
                "title": "Key Takeaways",
                "content": {
                    "text": (
                        "- Cap 265 local councils lacked constitutional protection and were wholly subservient to central ministerial whims.\n"
                        "- These failures created widespread national consensus for constitutional devolution in 2010."
                    )
                }
            }
        ]
    },
    {
        "page_number": 14,
        "page_title": "Revision Checklist: Cap 265 System",
        "blocks": [
            {
                "block_type": "step_process",
                "component_type": "step_process",
                "title": "Mastery Checklist",
                "content": {
                    "steps": [
                        "1. Four types of local authorities under Cap 265.",
                        "2. Roles: Councillor, Mayor, Town Clerk, Minister for Local Government.",
                        "3. Five statutory functions of pre-2010 councils.",
                        "4. Five systemic causes of the collapse of Cap 265 councils."
                    ]
                }
            }
        ]
    },
    {
        "page_number": 15,
        "page_title": "Quick Knowledge Check: Cap 265",
        "blocks": [
            {
                "block_type": "mini_activity",
                "component_type": "mini_activity",
                "title": "Quick Recall Quiz",
                "content": {
                    "instruction": "Identify the office described:",
                    "items": [
                        "1. Political head of a Municipal Council elected by fellow councillors -> **Mayor**",
                        "2. Chief Executive Officer appointed by the Public Service Commission -> **Town Clerk**",
                        "3. Central government cabinet official with powers to dissolve local councils -> **Minister for Local Government**"
                    ]
                }
            }
        ]
    }
]

LESSON_3_PAGES = [
    {
        "page_number": 1,
        "page_title": "Transition to Devolution and County Governments",
        "blocks": [
            {
                "block_type": "learning_goal",
                "component_type": "learning_goal",
                "title": "Lesson Objectives: The Devolution Revolution",
                "content": {
                    "text": (
                        "By the end of this lesson, you will be able to:\n"
                        "- Explain the historical rationale and objectives of establishing devolved government under the 2010 Constitution\n"
                        "- Analyze the nine constitutional objectives of devolution under Article 174\n"
                        "- Compare the pre-2010 Local Authorities system with the devolved County Government system across key features\n"
                        "- Understand how devolution decentralizes power, fosters national unity, and protects marginalized minorities"
                    )
                }
            },
            {
                "block_type": "definition_card",
                "component_type": "definition_card",
                "title": "Concept: Devolution Under Chapter 11",
                "content": {
                    "term": "Devolution",
                    "definition": (
                        "The constitutional transfer of political authority, legislative powers, executive functions, "
                        "and financial resources from the national central government to 47 semi-autonomous, coordinate County Governments."
                    )
                }
            }
        ]
    },
    {
        "page_number": 2,
        "page_title": "Educational Documentary: Devolution in the 2010 Constitution",
        "blocks": [
            {
                "block_type": "suggested_video",
                "component_type": "suggested_video",
                "title": "Legal Analysis: How Devolved Government Works in Kenya (Articles 174–185 Explained)",
                "content": {
                    "url": "https://www.youtube.com/watch?v=Ws_Zlb6azhY",
                    "text": "Examine the constitutional foundation of devolution, the powers of County Assemblies, and the separation of powers between National and County levels.",
                    "author": "COURT HELICOPTER / Legal Education Series",
                    "licensing": "Standard YouTube License"
                }
            }
        ]
    },
    {
        "page_number": 3,
        "page_title": "The Nine Constitutional Objectives of Devolution (Article 174)",
        "blocks": [
            {
                "block_type": "step_process",
                "component_type": "step_process",
                "title": "Article 174 Constitutional Objectives (Point-Form)",
                "content": {
                    "steps": [
                        "1. Promoting Democratic and Accountable Exercise of Power: Giving citizens direct oversight over local government.",
                        "2. Fostering National Unity: Recognizing and celebrating ethnic and cultural diversity without exclusion.",
                        "3. Giving Powers of Self-Governance: Empowering local communities to make developmental decisions through public participation.",
                        "4. Recognizing Community Rights: Allowing local populations to manage and benefit from their local resources and development priorities.",
                        "5. Protecting Minorities and Marginalized Groups: Guaranteeing representation and specialized funding for historically neglected communities.",
                        "6. Promoting Equitable Sharing of Resources: Ensuring national revenues are shared equitably across all 47 counties.",
                        "7. Decentralizing State Organs & Services: Moving ministries, licensing, and medical services from Nairobi closer to the people.",
                        "8. Enhancing Checks and Balances: Establishing constitutional separation of powers between national and county governments.",
                        "9. Facilitating Rapid Social & Economic Development: Accelerating local infrastructure, clinics, and clean water delivery across Kenya."
                    ]
                }
            }
        ]
    },
    {
        "page_number": 4,
        "page_title": "Map of the 47 Counties of Kenya",
        "blocks": [
            {
                "block_type": "suggested_image",
                "component_type": "suggested_image",
                "title": "Map of the 47 Counties of Kenya",
                "content": {
                    "text": "Map showing the 47 devolved County Governments established under the First Schedule of the Constitution of Kenya 2010.",
                    "url": "https://upload.wikimedia.org/wikipedia/commons/8/86/Kenya_counties_map_Labelled.jpg",
                    "author": "Public Domain / Wikimedia Commons",
                    "licensing": "Public Domain",
                    "commons_page_url": "https://commons.wikimedia.org/wiki/File:Kenya_counties_map_Labelled.jpg"
                }
            }
        ]
    },
    {
        "page_number": 5,
        "page_title": "Master Comparison: Pre-2010 Local Authorities vs. 2010 Devolution",
        "blocks": [
            {
                "block_type": "comparison_table",
                "component_type": "comparison_table",
                "title": "Structural Comparison: Cap 265 vs. 2010 Devolution",
                "content": {
                    "headers": ["Feature", "Pre-2010 Local Authorities (Cap 265)", "Devolved County Governments (2010 Constitution)"],
                    "rows": [
                        ["Foundational Legal Basis", "Ordinary Act of Parliament (Local Government Act Cap 265), easily amended or repealed.", "Supreme Law of Kenya (Chapter 11 of the 2010 Constitution), protected from political tampering."],
                        ["Number of Administrative Units", "Over 175 fluctuating municipal, county, town, and urban councils.", "Fixed at exactly 47 Counties listed in the First Schedule."],
                        ["Degree of Autonomy", "Completely subordinate to the Minister for Local Government who could dissolve councils.", "Distinct, self-governing, and coordinate levels of government with constitutional autonomy."],
                        ["Executive Leadership", "Mayor or Council Chairman (elected indirectly by fellow councillors bi-annually).", "County Governor directly elected by registered county voters for a 5-year term."],
                        ["Legislative Power", "Council committees that passed local subordinate by-laws.", "County Assembly with full legislative powers to pass binding County Acts."],
                        ["Financial Guarantees", "Discretionary central grants (LATF) and local market charges.", "Constitutionally guaranteed minimum 15% equitable share of national revenue."]
                    ]
                }
            }
        ]
    },
    {
        "page_number": 6,
        "page_title": "Key Principles of Devolution (Article 175)",
        "blocks": [
            {
                "block_type": "concept_explanation",
                "component_type": "concept_explanation",
                "title": "Constitutional Pillars of County Governance",
                "content": {
                    "text": (
                        "Under Article 175, County Governments must conduct their affairs based on three non-negotiable principles:\n\n"
                        "- **Democratic Principles and Separation of Powers:** Clear institutional separation between the County Assembly (legislature) and the County Executive Committee (executive).\n"
                        "- **Guaranteed Reliable Revenue Streams:** The national government must ensure counties have reliable sources of revenue to perform devolved functions.\n"
                        "- **Gender Equity and Inclusion:** No more than two-thirds of the members of representative bodies shall be of the same gender (*two-thirds gender rule*)."
                    )
                }
            }
        ]
    },
    {
        "page_number": 7,
        "page_title": "Public Participation: The Heart of Devolution",
        "blocks": [
            {
                "block_type": "callout",
                "component_type": "callout",
                "title": "Civic Power: Citizen-Led Development",
                "content": {
                    "text": (
                        "**What is Public Participation?**\n"
                        "The mandatory constitutional requirement that county governments must consult citizens before passing county legislation, approving county budgets, or initiating development projects.\n\n"
                        "**Impact on Governance:**\n"
                        "- Citizens directly decide whether their county needs a dispensary, water borehole, or access road.\n"
                        "- High Court can nullify any county budget or bill passed without meaningful public participation."
                    )
                }
            }
        ]
    },
    {
        "page_number": 8,
        "page_title": "Protection of Minorities and Marginalized Communities",
        "blocks": [
            {
                "block_type": "step_process",
                "component_type": "step_process",
                "title": "How Devolution Protects Vulnerable Groups",
                "content": {
                    "steps": [
                        "1. Special Seat Nominations: Mandating nominated MCAs in County Assemblies to represent youth, persons with disabilities, and ethnic minorities.",
                        "2. Two-Thirds Gender Rule: Ensuring gender balance in county assemblies and executive committees.",
                        "3. The Equalization Fund (0.5%): Earmarked national funding targeted specifically at marginalized counties (Turkana, Mandera, Wajir, Samburu) to elevate water, health, and road standards.",
                        "4. Grassroots Resource Control: Preventing dominant national ethnic groups from monopolizing local natural resources."
                    ]
                }
            }
        ]
    },
    {
        "page_number": 9,
        "page_title": "Interactive Classification: Pre-2010 vs. 2010 Devolution",
        "blocks": [
            {
                "block_type": "mini_activity",
                "component_type": "mini_activity",
                "title": "Assign Feature to Pre-2010 Local Authorities or 2010 Devolution",
                "content": {
                    "instruction": "Test your mastery of the historical shift to devolution:",
                    "items": [
                        "1. Minister for Local Government had absolute power to dissolve councils -> **Pre-2010 (Cap 265)**",
                        "2. Guaranteed minimum 15% equitable share of national revenue -> **2010 Devolution**",
                        "3. Directly elected County Governor heading the executive -> **2010 Devolution**",
                        "4. Over 175 councils regulated by an Act of Parliament -> **Pre-2010 (Cap 265)**",
                        "5. Fixed number of 47 County Governments protected by Constitution -> **2010 Devolution**"
                    ]
                }
            }
        ]
    },
    {
        "page_number": 10,
        "page_title": "KCSE Examination Coaching: Objectives of Devolution",
        "blocks": [
            {
                "block_type": "worked_example",
                "component_type": "worked_example",
                "title": "KCSE Question: Explain Six Objectives of Devolving Government in Kenya (12 Marks)",
                "content": {
                    "text": (
                        "**Model Answer (Point + Explanation = 2 Marks per Point):**\n\n"
                        "1. **To Promote Democratic and Accountable Exercise of Power:** Giving citizens direct authority to elect county leaders and scrutinize local budgets. (2 marks)\n\n"
                        "2. **To Foster National Unity by Recognizing Diversity:** Celebrating cultural and regional diversity while preventing ethnic marginalization. (2 marks)\n\n"
                        "3. **To Give Powers of Self-Governance to the People:** Empowering grassroots communities to participate actively in decisions affecting their daily lives. (2 marks)\n\n"
                        "4. **To Protect the Rights of Minorities and Marginalized Groups:** Guaranteeing special representation and the Equalization Fund for historically neglected areas. (2 marks)\n\n"
                        "5. **To Ensure Equitable Sharing of National Resources:** Allocating a constitutionally protected minimum of 15% of national revenue to all 47 counties. (2 marks)\n\n"
                        "6. **To Decentralize State Organs and Services:** Moving critical administrative departments, health services, and registries away from Nairobi closer to the citizens. (2 marks)"
                    )
                }
            }
        ]
    },
    {
        "page_number": 11,
        "page_title": "KCSE Examination Coaching: Structural Comparison",
        "blocks": [
            {
                "block_type": "worked_example",
                "component_type": "worked_example",
                "title": "KCSE Question: Compare the Structure of Pre-2010 Local Authorities with 2010 County Governments (10 Marks)",
                "content": {
                    "text": (
                        "**Model Answer (Point-by-Point Contrast = 2 Marks per Pair):**\n\n"
                        "1. **Legal Foundation:** Pre-2010 councils were anchored in an ordinary Act of Parliament (Cap 265), whereas County Governments are established under Chapter 11 of the supreme 2010 Constitution. (2 marks)\n\n"
                        "2. **Autonomy:** Pre-2010 councils were wholly subordinate to the Minister for Local Government, while modern counties are distinct, self-governing, and coordinate. (2 marks)\n\n"
                        "3. **Executive Head:** Pre-2010 councils were headed by Mayors/Chairmen elected indirectly by councillors, whereas modern counties are led by directly elected Governors. (2 marks)\n\n"
                        "4. **Legislative Authority:** Pre-2010 councils could only pass subordinate by-laws, while modern County Assemblies pass binding County Acts. (2 marks)\n\n"
                        "5. **Revenue Allocation:** Pre-2010 councils received discretionary central grants (LATF), whereas modern counties receive a constitutionally guaranteed minimum 15% equitable share. (2 marks)"
                    )
                }
            }
        ]
    },
    {
        "page_number": 12,
        "page_title": "Check Your Understanding: Module 7.3",
        "blocks": [
            {
                "block_type": "knowledge_check",
                "component_type": "knowledge_check",
                "title": "Module 7.3 Assessment",
                "content": {
                    "questions": [
                        {
                            "question": "What is the minimum percentage of national revenue guaranteed to County Governments under Article 203 of the Constitution?",
                            "options": [
                                "5%",
                                "15%",
                                "30%",
                                "50%"
                            ],
                            "correct_answer": 1,
                            "explanation": "Article 203 guarantees that County Governments receive at least 15% of all national revenue raised."
                        },
                        {
                            "question": "How many County Governments are established in Kenya under the First Schedule of the 2010 Constitution?",
                            "options": [
                                "8 Counties",
                                "47 Counties",
                                "175 Counties",
                                "290 Counties"
                            ],
                            "correct_answer": 1,
                            "explanation": "The First Schedule of the 2010 Constitution fixes the number of counties at exactly 47."
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
                "title": "Core Summary: Transition to Devolution",
                "content": {
                    "text": (
                        "• **Constitutional Anchoring:** Chapter 11 replaced Cap 265 with 47 coordinate, self-governing County Governments.\n"
                        "• **Article 174 Objectives:** Democratic accountability, self-governance, equitable revenue sharing, minority protection, and service decentralization.\n"
                        "• **Structural Upgrades:** Directly elected Governors, legislative County Assemblies, guaranteed 15% equitable share, and mandatory public participation."
                    )
                }
            },
            {
                "block_type": "key_takeaway",
                "component_type": "key_takeaway",
                "title": "Key Takeaways",
                "content": {
                    "text": (
                        "- Devolution is the most transformative constitutional reform in Kenya since independence in 1963.\n"
                        "- It transformed local governance from central subordination to constitutional partnership."
                    )
                }
            }
        ]
    },
    {
        "page_number": 14,
        "page_title": "Revision Checklist: Devolution Objectives",
        "blocks": [
            {
                "block_type": "step_process",
                "component_type": "step_process",
                "title": "Mastery Checklist",
                "content": {
                    "steps": [
                        "1. Nine constitutional objectives of devolution (Article 174).",
                        "2. Three principles of devolution (Article 175).",
                        "3. Five structural differences between Cap 265 councils and 2010 Counties.",
                        "4. Role of public participation and minority protection in devolution."
                    ]
                }
            }
        ]
    },
    {
        "page_number": 15,
        "page_title": "Quick Knowledge Check: Devolution Principles",
        "blocks": [
            {
                "block_type": "mini_activity",
                "component_type": "mini_activity",
                "title": "Quick Recall Quiz",
                "content": {
                    "instruction": "Answer true or false:",
                    "items": [
                        "1. County Assemblies have the power to make binding county legislation -> **True**",
                        "2. The Minister for Local Government still appoints nominated MCAs -> **False (voters elect, political parties nominate under IEBC formula)**",
                        "3. Public participation is a mandatory constitutional requirement in county budget making -> **True**"
                    ]
                }
            }
        ]
    }
]

LESSON_4_PAGES = [
    {
        "page_number": 1,
        "page_title": "Structures, Functions, and Finances of County Governments",
        "blocks": [
            {
                "block_type": "learning_goal",
                "component_type": "learning_goal",
                "title": "Lesson Objectives: County Governance and Operations",
                "content": {
                    "text": (
                        "By the end of this lesson, you will be able to:\n"
                        "- Outline the composition and functions of the County Assembly and County Executive Committee\n"
                        "- Identify the devolved functions assigned to counties under the Fourth Schedule of the Constitution\n"
                        "- Detail the revenue streams that finance County Governments (Equitable Share, Own-Source, Equalization Fund, Grants)\n"
                        "- Analyze systemic challenges facing modern County Governments and formulate viable solutions"
                    )
                }
            },
            {
                "block_type": "definition_card",
                "component_type": "definition_card",
                "title": "Concept: County Separation of Powers",
                "content": {
                    "term": "County Government Arms",
                    "definition": (
                        "The distinct separation between the legislative arm (County Assembly) which makes laws and conducts oversight, "
                        "and the executive arm (County Executive Committee headed by the Governor) which implements county policies."
                    )
                }
            }
        ]
    },
    {
        "page_number": 2,
        "page_title": "Educational Documentary: Structure of the Kenyan Government",
        "blocks": [
            {
                "block_type": "suggested_video",
                "component_type": "suggested_video",
                "title": "Constitutional Analysis: Structure of The Kenyan Government & Devolution Made Easy",
                "content": {
                    "url": "https://www.youtube.com/watch?v=8H_MEx8F5QM",
                    "text": "Explore the three arms of national government, the structure of County Assemblies and County Executives, and the division of devolved functions.",
                    "author": "Learn and Learn Channel / Civic Education",
                    "licensing": "Standard YouTube License"
                }
            }
        ]
    },
    {
        "page_number": 3,
        "page_title": "Structure of a County Government",
        "blocks": [
            {
                "block_type": "comparison_table",
                "component_type": "comparison_table",
                "title": "County Assembly vs. County Executive Committee",
                "content": {
                    "headers": ["Organ", "Composition", "Primary Functions & Mandate"],
                    "rows": [
                        ["County Assembly (Legislature)", "Elected Ward MCAs, nominated special seat members (2/3 gender rule), marginalized youth/PWD reps, and an ex-officio Speaker.", "Enacting county legislation, approving county budgets, vetting executive nominees, and oversight of the executive."],
                        ["County Executive Committee (Executive)", "County Governor (Chief Executive), Deputy Governor, and up to 10 CEC Members appointed with Assembly approval.", "Implementing county legislation, managing county departments, preparing budgets, and delivering devolved services."],
                        ["County Public Service Board", "Independent board appointed by the Governor with Assembly approval.", "Recruiting, managing, promoting, and disciplining county civil servants and medical personnel."]
                    ]
                }
            }
        ]
    },
    {
        "page_number": 4,
        "page_title": "Devolved Functions Under the Fourth Schedule",
        "blocks": [
            {
                "block_type": "step_process",
                "component_type": "step_process",
                "title": "Six Core Devolved Functions",
                "content": {
                    "steps": [
                        "1. Agriculture: Crop farming, animal husbandry, livestock sale yards, county abattoirs, and local fisheries.",
                        "2. County Health Services: County hospitals, health centers, dispensaries, pharmacies, ambulance services, and sanitation.",
                        "3. Environmental Control: Managing noise pollution, air pollution, refuse disposal, and outdoor advertising.",
                        "4. County Transport & Infrastructure: Constructing access roads, street lighting, public parking, traffic management, and ferries.",
                        "5. Pre-Primary Education: Early Childhood Development Education (ECDE) nurseries, village polytechnics, and home craft centers.",
                        "6. Trade Development & Regulation: Markets, trade licenses, fair trading practices, cooperative societies, and local tourism."
                    ]
                }
            }
        ]
    },
    {
        "page_number": 5,
        "page_title": "Sources of County Government Finances",
        "blocks": [
            {
                "block_type": "step_process",
                "component_type": "step_process",
                "title": "Five Revenue Streams for Counties",
                "content": {
                    "steps": [
                        "1. The Equitable Share (Min 15%): Constitutionally guaranteed share of national revenue raised by the national government, divided among counties using the CRA formula.",
                        "2. Own-Source Revenues: Locally collected revenues, including land/property rates, single business permits, parking fees, market cess, and hospital service fees.",
                        "3. Equalization Fund (0.5%): Dedicated national fund targeted at marginalized counties to provide basic water, roads, health facilities, and electricity.",
                        "4. Conditional and Unconditional Grants: Additional funds allocated by the national government or international development partners for specific projects (e.g., donor-funded hospital equipment).",
                        "5. Guaranteed Borrowing: Loans taken by counties, subject to strict National Treasury guarantees and County Assembly approval."
                    ]
                }
            }
        ]
    },
    {
        "page_number": 6,
        "page_title": "Six Challenges Facing Modern County Governments",
        "blocks": [
            {
                "block_type": "step_process",
                "component_type": "step_process",
                "title": "Systemic Roadblocks in County Governance",
                "content": {
                    "steps": [
                        "1. Delayed Treasury Remittances: Chronic delays by the National Treasury in disbursing equitable share funds, causing salary arrears and paralyzed health services.",
                        "2. Narrow Own-Source Revenue Base: Many semi-arid counties have low commercial activity and weak tax bases, making them over 90% reliant on national transfers.",
                        "3. Rampant Corruption & Embezzlement: Inflated procurement contracts, nepotism, and looting of public funds by county officials.",
                        "4. Executive-Assembly Wrangles: Frequent political conflicts and impeachment threats between Governors and MCAs over budget approvals and ward development funds.",
                        "5. Shortage of Skilled Technical Personnel: Acute deficits of medical specialists, civil engineers, and chartered financial controllers in remote counties.",
                        "6. Duplication and Boundary Disputes: Jurisdictional clashes with national agencies over functions like national trunk roads (KeNHA) vs. county roads (KeRRA)."
                    ]
                }
            }
        ]
    },
    {
        "page_number": 7,
        "page_title": "Viable Solutions to County Governance Challenges",
        "blocks": [
            {
                "block_type": "comparison_table",
                "component_type": "comparison_table",
                "title": "Challenge vs. Proposed Reform Solution",
                "content": {
                    "headers": ["Governance Challenge", "Viable Reform Solution", "Expected Outcome"],
                    "rows": [
                        ["Delayed Treasury Remittances", "Strict adherence to the legal Cash Disbursement Schedule and automation of Treasury transfers.", "Predictable monthly cash flows to pay medical staff and contractors on time."],
                        ["Narrow Own-Source Revenue", "Digitizing revenue collection systems (cashless mobile payments) and automating land valuation rolls.", "Plugs revenue leakages and triples local county revenues."],
                        ["Corruption and Graft", "Strengthening oversight by the Auditor-General, Ethics and Anti-Corruption Commission (EACC), and County Assembly PACs.", "Ensures deterrence and recovery of embezzled public funds."],
                        ["Executive-Assembly Wrangles", "Institutionalizing alternative dispute resolution (ADR) through the Council of Governors and County Assemblies Forum.", "Prevents frivolous impeachment motions and fosters budget consensus."],
                        ["Shortage of Technocrats", "Offering hardship allowances, in-service specialized training, and inter-county staff exchanges.", "Attracts and retains doctors, surgeons, and engineers in remote counties."]
                    ]
                }
            }
        ]
    },
    {
        "page_number": 8,
        "page_title": "Interactive Classification: Devolved vs. National Functions",
        "blocks": [
            {
                "block_type": "mini_activity",
                "component_type": "mini_activity",
                "title": "Classify the Function Under the Fourth Schedule",
                "content": {
                    "instruction": "Identify whether each function belongs to the National Government or County Government:",
                    "items": [
                        "1. National Defense and National Police Service -> **National Government**",
                        "2. County health facilities, dispensaries, and pharmacies -> **County Government**",
                        "3. Foreign affairs and international trade treaties -> **National Government**",
                        "4. Pre-primary Early Childhood Development Education (ECDE) -> **County Government**",
                        "5. Local access feeder roads and street lighting -> **County Government**",
                        "6. Monetary policy, currency issuance, and central banking -> **National Government**"
                    ]
                }
            }
        ]
    },
    {
        "page_number": 9,
        "page_title": "KCSE Examination Coaching: Functions of County Governments",
        "blocks": [
            {
                "block_type": "worked_example",
                "component_type": "worked_example",
                "title": "KCSE Question: Explain Six Functions Devolved to County Governments (12 Marks)",
                "content": {
                    "text": (
                        "**Model Answer (Point + Explanation = 2 Marks per Point):**\n\n"
                        "1. **County Health Services:** Constructing, equipping, and managing dispensaries, health centers, and county hospitals, and providing ambulance services. (2 marks)\n\n"
                        "2. **Agriculture and Animal Husbandry:** Promoting crop production, running livestock saleyards, abattoirs, and controlling plant and animal diseases. (2 marks)\n\n"
                        "3. **County Transport and Infrastructure:** Building and maintaining local feeder access roads, managing public bus parks, parking facilities, and street lighting. (2 marks)\n\n"
                        "4. **Trade Development and Regulation:** Regulating local trading markets, issuing single business permits, and overseeing cooperative societies. (2 marks)\n\n"
                        "5. **Pre-Primary and Vocational Education:** Managing Early Childhood Development Education (ECDE) nurseries, village polytechnics, and vocational craft centers. (2 marks)\n\n"
                        "6. **Environmental and Pollution Control:** Managing public refuse disposal, waste collection, noise pollution, and regulating outdoor advertising. (2 marks)"
                    )
                }
            }
        ]
    },
    {
        "page_number": 10,
        "page_title": "KCSE Examination Coaching: County Finances and Challenges",
        "blocks": [
            {
                "block_type": "worked_example",
                "component_type": "worked_example",
                "title": "KCSE Question: Explain Five Sources of Revenue for County Governments in Kenya (10 Marks)",
                "content": {
                    "text": (
                        "**Model Answer (Point + Explanation = 2 Marks per Point):**\n\n"
                        "1. **The Equitable Share:** The constitutionally guaranteed minimum 15% share of all revenue raised nationally, distributed among counties by Parliament. (2 marks)\n\n"
                        "2. **Own-Source Revenues:** Local taxes levied by counties, including land rates, business licensing permits, parking charges, and market fees. (2 marks)\n\n"
                        "3. **The Equalization Fund:** Dedicated national fund (0.5% of national revenue) allocated to marginalized counties to bring basic services to national standards. (2 marks)\n\n"
                        "4. **Conditional and Unconditional Grants:** Additional funding allocations from the national government or foreign development partners for specific programs. (2 marks)\n\n"
                        "5. **Domestic and External Borrowing:** Loans acquired by counties with County Assembly approval and guaranteed by the National Treasury. (2 marks)"
                    )
                }
            }
        ]
    },
    {
        "page_number": 11,
        "page_title": "Financial Oversight: The Controller of Budget & Auditor-General",
        "blocks": [
            {
                "block_type": "concept_explanation",
                "component_type": "concept_explanation",
                "title": "Independent Constitutional Oversight Bodies",
                "content": {
                    "text": (
                        "To prevent financial looting and unauthorized spending, the Constitution establishes two vital watchdogs:\n\n"
                        "- **Controller of Budget (COB):** Authorizes all withdrawals from County Revenue Funds only after confirming that the expenditure is lawful and budgeted for.\n"
                        "- **Auditor-General:** Conducts annual audits of all 47 County Executive and Assembly accounts, submitting investigative reports to the Senate and County Assemblies for action."
                    )
                }
            }
        ]
    },
    {
        "page_number": 12,
        "page_title": "Check Your Understanding: Module 7.4",
        "blocks": [
            {
                "block_type": "knowledge_check",
                "component_type": "knowledge_check",
                "title": "Module 7.4 Assessment",
                "content": {
                    "questions": [
                        {
                            "question": "Which independent office is responsible for authorizing all withdrawals of funds from County Revenue Funds?",
                            "options": [
                                "The County Governor",
                                "The Controller of Budget (COB)",
                                "The Speaker of the County Assembly",
                                "The Minister for Finance"
                            ],
                            "correct_answer": 1,
                            "explanation": "The Controller of Budget oversees the implementation of budgets and authorizes all withdrawals."
                        },
                        {
                            "question": "Which educational level is devolved to County Governments under the Fourth Schedule?",
                            "options": [
                                "Secondary Education",
                                "Pre-Primary (ECDE) and Village Polytechnics",
                                "University Education",
                                "Primary Teacher Training Colleges"
                            ],
                            "correct_answer": 1,
                            "explanation": "Pre-primary education (ECDE) and village polytechnics are fully devolved functions."
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
                "title": "Core Summary: County Structures, Functions, and Finances",
                "content": {
                    "text": (
                        "• **Structure:** County Assembly (legislature/oversight) vs. County Executive Committee (executive/service delivery).\n"
                        "• **Devolved Functions:** Agriculture, county healthcare/clinics, county access roads, pre-primary ECDE, trade licensing, refuse disposal.\n"
                        "• **Finances:** Min 15% Equitable Share, Own-Source revenues (rates/parking), Equalization Fund (0.5%), Grants, and Borrowing.\n"
                        "• **Challenges & Solutions:** Delayed Treasury releases, corruption, and wrangles addressed through digital revenue systems, COB/Auditor-General oversight, and capacity building."
                    )
                }
            },
            {
                "block_type": "key_takeaway",
                "component_type": "key_takeaway",
                "title": "Key Takeaways",
                "content": {
                    "text": (
                        "- County Governments combine democratic local lawmaking with executive service delivery.\n"
                        "- Strong financial controls by independent watchdogs are essential to safeguard devolved public funds."
                    )
                }
            }
        ]
    },
    {
        "page_number": 14,
        "page_title": "Revision Checklist: County Governance",
        "blocks": [
            {
                "block_type": "step_process",
                "component_type": "step_process",
                "title": "Mastery Checklist",
                "content": {
                    "steps": [
                        "1. County Assembly composition and functions.",
                        "2. County Executive Committee composition and functions.",
                        "3. Six devolved functions under the Fourth Schedule.",
                        "4. Five sources of county revenue.",
                        "5. Six challenges and five reform solutions."
                    ]
                }
            }
        ]
    },
    {
        "page_number": 15,
        "page_title": "Interactive Match: Revenue Streams",
        "blocks": [
            {
                "block_type": "mini_activity",
                "component_type": "mini_activity",
                "title": "Match the Revenue Stream",
                "content": {
                    "instruction": "Identify the county revenue stream described:",
                    "items": [
                        "1. Minimum 15% constitutionally protected national revenue share -> **Equitable Share**",
                        "2. 0.5% national fund for water and roads in marginalized regions -> **Equalization Fund**",
                        "3. Local parking fees, single business permits, and land rates -> **Own-Source Revenues**",
                        "4. External loans requiring National Treasury guarantees -> **Guaranteed Borrowing**"
                    ]
                }
            }
        ]
    },
    {
        "page_number": 16,
        "page_title": "Quick Knowledge Check: County Operations",
        "blocks": [
            {
                "block_type": "mini_activity",
                "component_type": "mini_activity",
                "title": "Quick Recall Quiz",
                "content": {
                    "instruction": "Answer true or false:",
                    "items": [
                        "1. County Executives can withdraw funds without Controller of Budget approval -> **False**",
                        "2. Primary schools and national universities are managed by County Governments -> **False (managed by National Government)**",
                        "3. County Assemblies must approve CEC members before they take office -> **True**"
                    ]
                }
            }
        ]
    }
]

LESSON_5_PAGES = [
    {
        "page_number": 1,
        "page_title": "Intergovernmental Relations, Dispute Resolution, and Master Synthesis",
        "blocks": [
            {
                "block_type": "learning_goal",
                "component_type": "learning_goal",
                "title": "Lesson Objectives: Intergovernmental Relations and Synthesis",
                "content": {
                    "text": (
                        "By the end of this lesson, you will be able to:\n"
                        "- Explain the constitutional principles governing relations between National and County governments (Article 189)\n"
                        "- Analyze the institutional bodies coordinating intergovernmental relations (Summit, COG, IGRTC)\n"
                        "- Describe the mechanisms for dispute resolution and the procedure for suspending a County Government under Article 192\n"
                        "- Master comprehensive KCSE Paper 2 examination questions and marking schemes"
                    )
                }
            },
            {
                "block_type": "definition_card",
                "component_type": "definition_card",
                "title": "Concept: Distinct but Interdependent",
                "content": {
                    "term": "Intergovernmental Relations",
                    "definition": (
                        "The constitutional framework under Article 189 governing the interactions, consultation, and cooperative governance "
                        "between the National Government and the 47 County Governments based on mutual respect and distinct institutional integrity."
                    )
                }
            }
        ]
    },
    {
        "page_number": 2,
        "page_title": "News Analysis: Intergovernmental Relations in Devolution",
        "blocks": [
            {
                "block_type": "suggested_video",
                "component_type": "suggested_video",
                "title": "News Analysis: Good Intergovernmental Relations Key in Realising the Benefits of Devolution",
                "content": {
                    "url": "https://www.youtube.com/watch?v=VapIpgS0PoY",
                    "text": "Examine how consultation, dialogue, and collaborative frameworks between National Ministries and County Governors resolve policy conflicts and enhance development.",
                    "author": "NTV Kenya / National News Analysis",
                    "licensing": "Standard YouTube License"
                }
            }
        ]
    },
    {
        "page_number": 3,
        "page_title": "Principles of Intergovernmental Relations (Article 189)",
        "blocks": [
            {
                "block_type": "step_process",
                "component_type": "step_process",
                "title": "Six Core Principles Governing National-County Relations",
                "content": {
                    "steps": [
                        "1. Mutual Respect & Functional Integrity: Each level of government must respect the constitutional status, functions, and institutions of the other.",
                        "2. Consultation and Coordination: Both levels must assist, support, consult, and coordinate policies to enhance governance capacity.",
                        "3. Information Sharing: Regularly exchange administrative and technical information and establish joint coordination committees.",
                        "4. Alternative Dispute Resolution (ADR): Must make every reasonable effort to resolve conflicts through negotiation, conciliation, and mediation before going to court.",
                        "5. National Legislative Supremacy: In cases of direct conflict between national and county legislation on concurrent matters, national legislation prevails.",
                        "6. Extraordinary Intervention: The national government may intervene or suspend a county government under strictly defined constitutional conditions."
                    ]
                }
            }
        ]
    },
    {
        "page_number": 4,
        "page_title": "Key Intergovernmental Coordination Bodies",
        "blocks": [
            {
                "block_type": "comparison_table",
                "component_type": "comparison_table",
                "title": "Coordinating Organs in Kenyan Devolution",
                "content": {
                    "headers": ["Coordinating Body", "Composition & Leadership", "Mandate & Core Responsibilities"],
                    "rows": [
                        ["The Summit (National & County Coordinating Summit)", "President of Kenya (Chair) and all 47 County Governors.", "Apex consultative organ; evaluates devolution progress, resolves policy deadlocks, coordinates national-county priorities."],
                        ["Council of Governors (COG)", "All 47 County Governors, headed by an elected Governor as Chairperson.", "Collective voice of counties; shares best practices, negotiates with National Treasury, coordinates dispute settlement."],
                        ["Intergovernmental Relations Technical Committee (IGRTC)", "Technical body of administrative, legal, and public finance experts.", "Implements Summit decisions, manages the transfer of devolved assets, facilitates ADR mediation between governments."]
                    ]
                }
            }
        ]
    },
    {
        "page_number": 5,
        "page_title": "Suspension of a County Government (Article 192)",
        "blocks": [
            {
                "block_type": "step_process",
                "component_type": "step_process",
                "title": "Constitutional Procedure for County Suspension",
                "content": {
                    "steps": [
                        "1. Grounds for Suspension: Can only occur under exceptional circumstances: (a) In case of an emergency arising out of internal conflict or war, or (b) in case of exceptional circumstances warranting state intervention.",
                        "2. Independent Commission of Inquiry: The President must appoint an independent commission of inquiry to investigate the allegations and recommend suspension.",
                        "3. Presidential Approval: The President receives the commission's report and must be satisfied that the grounds are justified.",
                        "4. Senate Authorisation: The Senate must debate and formally approve the suspension resolution.",
                        "5. Maximum Duration of 90 Days: A suspension lasts for a maximum of 90 days, after which fresh county elections must be conducted unless the suspension is lifted earlier."
                    ]
                }
            }
        ]
    },
    {
        "page_number": 6,
        "page_title": "Role of the Senate in Devolution",
        "blocks": [
            {
                "block_type": "concept_explanation",
                "component_type": "concept_explanation",
                "title": "The Senate: The Guardian of Devolution",
                "content": {
                    "text": (
                        "Under Article 96 of the Constitution, the **Senate** serves as the ultimate protector of County Governments:\n\n"
                        "- **Representing Counties:** Defends the interests of the 47 counties and their governments at the national level.\n"
                        "- **Legislative Role:** Considers, debates, and passes bills concerning counties (e.g., County Allocation of Revenue Act — CARA).\n"
                        "- **Revenue Determination:** Determines the basis for allocating the equitable share of national revenue among counties (*CRA Formula*).\n"
                        "- **Oversight:** Exercises financial oversight over devolved revenue and investigates impeachment motions against County Governors passed by County Assemblies."
                    )
                }
            }
        ]
    },
    {
        "page_number": 7,
        "page_title": "Nairobi Skyline and National-County Seat",
        "blocks": [
            {
                "block_type": "suggested_image",
                "component_type": "suggested_image",
                "title": "Nairobi Skyline Showing KICC, Times Tower, and City Hall",
                "content": {
                    "text": "Nairobi skyline capturing the administrative heart of Kenya, featuring Parliament, National Ministries, and Nairobi City Hall.",
                    "url": "https://upload.wikimedia.org/wikipedia/commons/7/77/Nairobi_showing_KICC_Times_Tower_and_City_Hall.jpg",
                    "author": "Public Domain / Wikimedia Commons",
                    "licensing": "Public Domain",
                    "commons_page_url": "https://commons.wikimedia.org/wiki/File:Nairobi_showing_KICC_Times_Tower_and_City_Hall.jpg"
                }
            }
        ]
    },
    {
        "page_number": 8,
        "page_title": "Master KCSE Examination Paper 1 (Section B, 15 Marks)",
        "blocks": [
            {
                "block_type": "worked_example",
                "component_type": "worked_example",
                "title": "KCSE Question 1: Colonial Local Government Motives (3 Marks) & County Challenges (12 Marks)",
                "content": {
                    "text": (
                        "**(a) State three reasons why the British colonial administration introduced Local Native Councils in Kenya (3 marks):**\n"
                        "1. To overcome the shortage of European administrative staff by using African chiefs and councils. (1 mark)\n"
                        "2. To cut administrative costs by shifting local development expenses onto Africans through local taxes. (1 mark)\n"
                        "3. To contain African political agitation within designated native reserves. (1 mark)\n\n"
                        "**(b) Explain six challenges facing County Governments in Kenya today (12 marks):**\n"
                        "1. **Delayed Treasury Remittances:** Delays by the National Treasury in disbursing equitable shares cripple public services and delay salaries. (2 marks)\n"
                        "2. **Pervasive Corruption and Embezzlement:** Misappropriation of devolved funds and inflated procurement tenders drain local budgets. (2 marks)\n\n"
                        "3. **Inadequate Own-Source Revenue:** Low local commercial activity leaves many rural counties over 90% dependent on national transfers. (2 marks)\n\n"
                        "4. **Executive-Assembly Wrangles:** Political rivalry between Governors and MCAs leads to budget deadlocks and frequent impeachment motions. (2 marks)\n\n"
                        "5. **Shortage of Skilled Technical Staff:** Deficits of specialized doctors, engineers, and planners undermine service delivery in remote counties. (2 marks)\n\n"
                        "6. **Duplication and Role Conflicts:** Overlapping jurisdictional boundaries between national agencies and county departments. (2 marks)"
                    )
                }
            }
        ]
    },
    {
        "page_number": 9,
        "page_title": "Master KCSE Examination Paper 2 (Section B, 15 Marks)",
        "blocks": [
            {
                "block_type": "worked_example",
                "component_type": "worked_example",
                "title": "KCSE Question 2: Objectives of Devolution (3 Marks) & Intergovernmental Relations (12 Marks)",
                "content": {
                    "text": (
                        "**(a) State three constitutional objectives of devolution in Kenya under Article 174 (3 marks):**\n"
                        "1. To promote democratic and accountable exercise of state power. (1 mark)\n"
                        "2. To foster national unity by recognizing diversity. (1 mark)\n"
                        "3. To ensure equitable sharing of national and local resources throughout Kenya. (1 mark)\n\n"
                        "**(b) Explain six principles governing relations between National and County governments (12 marks):**\n"
                        "1. **Mutual Respect for Functional Integrity:** Each level must respect the constitutional status and powers of the other level. (2 marks)\n\n"
                        "2. **Consultation and Coordination:** Governments must assist, consult, and coordinate policies to enhance capacity. (2 marks)\n\n"
                        "3. **Information Sharing and Joint Committees:** Both levels must regularly exchange administrative information and set up joint coordination committees. (2 marks)\n\n"
                        "4. **Peaceful Dispute Resolution (ADR):** Governments must make every reasonable effort to settle conflicts through negotiation and mediation before going to court. (2 marks)\n\n"
                        "5. **National Supremacy in Concurrent Legislation:** Where there is a direct conflict on concurrent matters, national legislation prevails. (2 marks)\n\n"
                        "6. **Strict Conditions for County Suspension:** Suspension can only occur on grounds of war/emergency or exceptional circumstances with Senate approval. (2 marks)"
                    )
                }
            }
        ]
    },
    {
        "page_number": 10,
        "page_title": "Topic 7 Comprehensive Mastery Check (Part 1)",
        "blocks": [
            {
                "block_type": "knowledge_check",
                "component_type": "knowledge_check",
                "title": "Topic 7 Mastery Assessment (Part 1)",
                "content": {
                    "questions": [
                        {
                            "question": "What is the apex consultative body between the President of Kenya and all 47 County Governors?",
                            "options": [
                                "The Council of Governors (COG)",
                                "The National and County Government Coordinating Summit",
                                "The Intergovernmental Relations Technical Committee (IGRTC)",
                                "The Senate Committee on Devolution"
                            ],
                            "correct_answer": 1,
                            "explanation": "The Summit, chaired by the President and comprising all 47 Governors, is the apex consultative body."
                        },
                        {
                            "question": "For how many days maximum can a County Government be suspended under Article 192 before fresh elections are held?",
                            "options": [
                                "30 days",
                                "60 days",
                                "90 days",
                                "180 days"
                            ],
                            "correct_answer": 2,
                            "explanation": "Under Article 192(4), a county suspension cannot extend beyond 90 days."
                        }
                    ]
                }
            }
        ]
    },
    {
        "page_number": 11,
        "page_title": "Topic 7 Comprehensive Mastery Check (Part 2)",
        "blocks": [
            {
                "block_type": "knowledge_check",
                "component_type": "knowledge_check",
                "title": "Topic 7 Mastery Assessment (Part 2)",
                "content": {
                    "questions": [
                        {
                            "question": "Which house of Parliament is constitutionally designated as the guardian of County Governments and determines revenue allocation?",
                            "options": [
                                "The National Assembly",
                                "The Senate",
                                "The East African Legislative Assembly",
                                "The County Assembly"
                            ],
                            "correct_answer": 1,
                            "explanation": "Under Article 96, the Senate represents the counties and protects their financial interests."
                        },
                        {
                            "question": "What happens when there is a direct conflict between National legislation and County legislation on concurrent functions?",
                            "options": [
                                "The County legislation automatically prevails",
                                "The National legislation prevails",
                                "Both laws are nullified by the Supreme Court",
                                "The Council of Governors decides"
                            ],
                            "correct_answer": 1,
                            "explanation": "Under Article 191 of the Constitution, national legislation prevails in concurrent matters."
                        }
                    ]
                }
            }
        ]
    },
    {
        "page_number": 12,
        "page_title": "Topic 7 Comprehensive Master Summary",
        "blocks": [
            {
                "block_type": "summary",
                "component_type": "summary",
                "title": "Topic 7 Master Summary: Devolved Government in Kenya",
                "content": {
                    "text": (
                        "• **Colonial Era (1902–1963):** Headman Ordinance (1902), LNCs (1924), ADCs (1948); designed to cut costs, overcome manpower deficits, and contain African politics.\n"
                        "• **Pre-2010 Cap 265 System:** Municipal, Town, County, Urban councils; Mayor vs. Town Clerk rivalry; crippled by ministerial vetoes and graft.\n"
                        "• **2010 Devolution Revolution:** 47 County Governments; Article 174 objectives (self-governance, equity, minority rights); guaranteed min 15% revenue.\n"
                        "• **Structures & Functions:** County Assembly (legislative/oversight) vs. County Executive Committee (executive/services); Fourth Schedule devolved functions.\n"
                        "• **Intergovernmental Relations:** Distinct & interdependent (Article 189); Summit, COG, IGRTC; Senate oversight; Article 192 suspension rules."
                    )
                }
            }
        ]
    },
    {
        "page_number": 13,
        "page_title": "Topic 7 Final Exam Revision Checklist",
        "blocks": [
            {
                "block_type": "step_process",
                "component_type": "step_process",
                "title": "Exam Revision Checklist: Topic 7",
                "content": {
                    "steps": [
                        "1. Colonial local authorities: 6 reasons for introduction, 4 objectives of LNCs, 5 challenges.",
                        "2. Cap 265 system: 4 council categories, Mayor vs. Clerk rivalry, 5 systemic failures.",
                        "3. 2010 Devolution: 9 objectives under Article 174, 5 structural differences from Cap 265.",
                        "4. County operations: Assembly vs. Executive, 6 devolved functions, 5 revenue sources.",
                        "5. Intergovernmental relations: Article 189 principles, Summit, COG, IGRTC, Article 192 suspension."
                    ]
                }
            }
        ]
    },
    {
        "page_number": 14,
        "page_title": "Exam Coaching: Structuring Devolution Essay Answers",
        "blocks": [
            {
                "block_type": "callout",
                "component_type": "callout",
                "title": "Top Examination Tips for Devolution Questions",
                "content": {
                    "text": (
                        "**Key Tips:**\n"
                        "- **Distinguish the Era:** Check whether the question asks about **Colonial local government (LNCs/ADCs)**, **Pre-2010 Local Authorities (Cap 265)**, or **2010 County Devolution**.\n"
                        "- **Use Precise Legal Terminology:** Cite *Article 174 (Objectives of Devolution)*, *Article 189 (Intergovernmental Relations)*, *Fourth Schedule (Devolved Functions)*, and *Equitable Share*.\n"
                        "- **Always give complete explanations:** State the point + Explain the operational impact + Cite practical examples."
                    )
                }
            }
        ]
    },
    {
        "page_number": 15,
        "page_title": "Final Mastery Challenge: Key Institutions and Offices",
        "blocks": [
            {
                "block_type": "mini_activity",
                "component_type": "mini_activity",
                "title": "Match the Institution to Its Role",
                "content": {
                    "instruction": "Test your mastery of Kenyan devolution institutions:",
                    "items": [
                        "1. Apex consultative organ chaired by the President and all Governors -> **The Summit**",
                        "2. Collective forum representing all 47 County Governors -> **Council of Governors (COG)**",
                        "3. Parliamentary house that protects county interests and allocates revenue -> **The Senate**",
                        "4. Independent office authorizing all withdrawals from County Revenue Funds -> **Controller of Budget (COB)**",
                        "5. First African Chairman of an ADC in 1958 -> **Pascal Nabwane**"
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
                "title": "Final Topic 7 Warmup Check",
                "content": {
                    "questions": [
                        {
                            "question": "Which of the following is an example of an own-source revenue collected directly by County Governments?",
                            "options": [
                                "Customs and import duties",
                                "Income tax (PAYE)",
                                "Single business licensing permits and property land rates",
                                "Value Added Tax (VAT)"
                            ],
                            "correct_answer": 2,
                            "explanation": "Single business permits, property rates, and parking fees are own-source revenues collected by counties."
                        },
                        {
                            "question": "What is the primary role of the County Public Service Board?",
                            "options": [
                                "Passing county legislation",
                                "Recruiting, managing, and disciplining county government personnel",
                                "Auditing county accounts",
                                "Approving the county budget"
                            ],
                            "correct_answer": 1,
                            "explanation": "The County Public Service Board handles hiring, promotion, and human resource management."
                        }
                    ]
                }
            }
        ]
    },
    {
        "page_number": 17,
        "page_title": "Grand Summary: Topics 1–7 Review",
        "blocks": [
            {
                "block_type": "summary",
                "component_type": "summary",
                "title": "Comprehensive Synthesis: Form 4 History (Topics 1 to 7)",
                "content": {
                    "text": (
                        "• **Topic 1 (The World War):** WWI & WWII origins, course, Allied victory, League of Nations & UN founding.\n"
                        "• **Topic 2 (International Relations):** UN, Commonwealth, NAM, Cold War superpowers & collapse.\n"
                        "• **Topic 3 (Co-operation in Africa):** Pan-Africanism, OAU founding 1963, African Union 2002, EAC, ECOWAS, COMESA.\n"
                        "• **Topic 4 (National Philosophies):** African Socialism (Sessional Paper 10), Harambee, Nyayoism.\n"
                        "• **Topic 5 (Developments in Kenya):** Centralization (1964–1982), multipartyism (1991), 2010 Constitution.\n"
                        "• **Topic 6 (Developments in Africa):** Inherited crises, DRC Congo Crisis & Mobutu, Tanzania Ujamaa & Kiswahili.\n"
                        "• **Topic 7 (Devolved Government):** Colonial local government, Cap 265 councils, 2010 Devolution revolution, 47 County Governments."
                    )
                }
            }
        ]
    },
    {
        "page_number": 18,
        "page_title": "KCSE Examination Final Tip Sheet: Devolved Government",
        "blocks": [
            {
                "block_type": "step_process",
                "component_type": "step_process",
                "title": "Top Examination Tips for Topic 7",
                "content": {
                    "steps": [
                        "1. Clearly understand the chronological progression: LNCs (1924) -> ADCs (1948) -> Cap 265 Councils (1963–2010) -> County Governments (2010).",
                        "2. In questions on devolution objectives, cite Article 174 points (accountability, self-governance, minority protection, equitable resource sharing).",
                        "3. In questions on county functions, reference Fourth Schedule areas (health clinics, ECDE, feeder roads, trade licensing).",
                        "4. In questions on intergovernmental relations, emphasize 'distinct and interdependent' status and Alternative Dispute Resolution (ADR).",
                        "5. Distinguish between own-source revenues and national revenue transfers."
                    ]
                }
            }
        ]
    }
]


ALL_LESSONS = [
    {
        "unit_order": 1,
        "unit_name": "Historical Development of Local Government (Colonial Era to 1963)",
        "lesson_title": "Historical Development of Local Government: From Colonial Control to African District Councils",
        "pages": LESSON_1_PAGES
    },
    {
        "unit_order": 2,
        "unit_name": "Local Authorities under the Local Government Act (Cap 265)",
        "lesson_title": "Local Authorities under Cap 265: Structures, Functions, Leadership Duality, and Systemic Failures",
        "pages": LESSON_2_PAGES
    },
    {
        "unit_order": 3,
        "unit_name": "Transition to Devolution and County Governments",
        "lesson_title": "Transition to Devolution: Constitutional Objectives, Principles, and Structural Comparison",
        "pages": LESSON_3_PAGES
    },
    {
        "unit_order": 4,
        "unit_name": "Structures, Functions, and Finances of County Governments",
        "lesson_title": "County Governments: Structures, Devolved Functions, Revenue Sources, and Governance Challenges",
        "pages": LESSON_4_PAGES
    },
    {
        "unit_order": 5,
        "unit_name": "Relationship and Intergovernmental Relations in Devolution",
        "lesson_title": "Intergovernmental Relations, Coordination Organs, Dispute Resolution, and Master Synthesis",
        "pages": LESSON_5_PAGES
    }
]


# ===========================================================================
# DATABASE INGESTION RUNNER
# ===========================================================================

def run_ingestion(replace=False):
    print("=" * 80)
    print("VLEARN CURRICULUM INGESTION: FORM 4 HISTORY — TOPIC 7 (DEVOLVED GOVERNMENT)")
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
            name="Devolved Government",
            defaults={"order": 7}
        )
        if topic_created:
            print(f"[+] Created Topic: {topic.name} (Order: {topic.order})")
        else:
            topic.order = 7
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
        print(f"[SUCCESS] Form 4 History Topic 7 Ingestion Complete!")
        print(f"[*] Total Lessons Ingested: {len(ALL_LESSONS)}")
        print(f"[*] Total Pages Ingested:   {total_pages}")
        print(f"[*] Total Blocks Ingested:  {total_blocks}")
        print(f"[*] Total Media Assets:     {total_assets}")
        print("=" * 80)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Ingest Form 4 History Topic 7")
    parser.add_argument("--replace", action="store_true", help="Replace existing blocks with a fresh rebuild")
    args = parser.parse_args()

    run_ingestion(replace=args.replace)
