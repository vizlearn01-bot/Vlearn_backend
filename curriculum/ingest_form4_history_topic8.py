"""
VLearn Curriculum Ingestion Engine: Form 4 History — Topic 8 (Public Revenue and Expenditure in Kenya)

Target Subject: History (Subject ID: 17)
Grade: Form 4 (Grade ID: 4)
Curriculum: 844 (Curriculum ID: 4)

Topic 8: Public Revenue and Expenditure in Kenya (Order: 8)
  - Unit 1: Foundations of Public Finance and Principles of the Financial System (Lesson 1: 15 Pages)
  - Unit 2: The National Budget — Meaning, Importance, and Process of Preparation (Lesson 2: 16 Pages)
  - Unit 3: Sources of Public Revenue (National and County Governments) (Lesson 3: 16 Pages)
  - Unit 4: National Public Funds, Equitable Allocation, and Expenditure (Lesson 4: 16 Pages)
  - Unit 5: Financial Accountability, Oversight, and PFM Institutions (Lesson 5: 18 Pages)

Total: 5 Learning Units, 5 Lessons, 81 Pages, 92+ Blocks, 8 Media Assets (3 Wikimedia Photos + 5 Verified YouTube Videos)

Usage:
  ./venv/bin/python curriculum/ingest_form4_history_topic8.py --replace
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
# LESSON DEFINITIONS: FORM 4 HISTORY TOPIC 8
# ===========================================================================

LESSON_1_PAGES = [
    {
        "page_number": 1,
        "page_title": "Foundations of Public Finance and Principles of the Financial System",
        "blocks": [
            {
                "block_type": "learning_goal",
                "component_type": "learning_goal",
                "title": "Lesson Objectives: Constitutional Principles of Public Finance",
                "content": {
                    "text": (
                        "By the end of this lesson, you will be able to:\n"
                        "- Define public finance and its importance in sovereign nation-building\n"
                        "- Explain the historical context of public resource management in Kenya (African Socialism, Harambee, Nyayoism)\n"
                        "- Analyze the seven constitutional principles of public finance under Article 201 of the Constitution\n"
                        "- Apply principles such as intergenerational equity and progressive taxation to solve real-world fiscal scenarios"
                    )
                }
            },
            {
                "block_type": "definition_card",
                "component_type": "definition_card",
                "title": "Concept: Public Finance",
                "content": {
                    "term": "Public Finance",
                    "definition": (
                        "The constitutional system through which national and county governments raise public revenue (taxation and borrowing), "
                        "manage public funds, and plan and execute public expenditure to provide essential public goods and services."
                    )
                }
            }
        ]
    },
    {
        "page_number": 2,
        "page_title": "Historical Evolution of Public Finance in Kenya",
        "blocks": [
            {
                "block_type": "concept_explanation",
                "component_type": "concept_explanation",
                "title": "From Colonial Scarcity to Constitutional Governance",
                "content": {
                    "text": (
                        "Kenya's public finance system has evolved through distinct historical phases:\n\n"
                        "- **Post-Colonial Imbalances (1963):** Kenya inherited an extractive, unequal economy with low domestic capital and few African technocrats.\n"
                        "- **African Socialism (Sessional Paper No. 10 of 1965):** Established mutual social responsibility, state intervention in key utilities, and progressive taxation.\n"
                        "- **Harambee & Nyayoism:** Mobilized communal grassroots funding for rural schools, dispensaries, and water projects.\n"
                        "- **Chapter 12 of the 2010 Constitution:** Replaced over-centralized, opaque spending with binding, democratic principles of transparency, equity, and public participation."
                    )
                }
            }
        ]
    },
    {
        "page_number": 3,
        "page_title": "Educational Documentary: Chapter 12 Public Finance",
        "blocks": [
            {
                "block_type": "suggested_video",
                "component_type": "suggested_video",
                "title": "Constitutional Audio & Text: Chapter 12 - Public Finance (Articles 201-231)",
                "content": {
                    "url": "https://www.youtube.com/watch?v=PhuFAXpEMoc",
                    "text": "Examine the constitutional text and legal foundation of Chapter 12 of the Constitution of Kenya 2010, governing public revenue, expenditure, and devolution.",
                    "author": "Kenya Daily / Civic Education Series",
                    "licensing": "Standard YouTube License"
                }
            }
        ]
    },
    {
        "page_number": 4,
        "page_title": "The Seven Principles of Public Finance (Article 201)",
        "blocks": [
            {
                "block_type": "step_process",
                "component_type": "step_process",
                "title": "Article 201 Constitutional Principles (Point-Form)",
                "content": {
                    "steps": [
                        "1. Openness and Accountability (Public Participation): Absolute transparency in financial matters; citizens must be actively consulted before budgets and tax laws are approved.",
                        "2. Equitable Sharing of the Tax Burden: Taxation must be fair, ensuring high earners pay more (progressive taxation) while shielding low-income citizens.",
                        "3. Equitable Devolution of Nationally Raised Revenue: Revenue must be shared equitably between the national government and 47 counties, and among counties.",
                        "4. Equitable Regional Development & Affirmative Action: Public expenditure must promote balanced national development and fund marginalized areas (Equalization Fund).",
                        "5. Prudent and Responsible Use of Public Money: Public funds must be spent efficiently, avoiding waste, corruption, and unproductive debt.",
                        "6. Intergenerational Equity: Financial burdens and benefits of public debt must be shared fairly between present and future generations.",
                        "7. Responsible Financial Management and Clear Fiscal Reporting: Precise accounting records and mandatory annual audits by independent watchdogs."
                    ]
                }
            }
        ]
    },
    {
        "page_number": 5,
        "page_title": "Progressive Taxation: Fair Sharing of the Tax Burden",
        "blocks": [
            {
                "block_type": "comparison_table",
                "component_type": "comparison_table",
                "title": "Tax Systems and Social Equity",
                "content": {
                    "headers": ["Tax System Type", "Mechanism", "Impact on Wealth Redistribution"],
                    "rows": [
                        ["Progressive Tax (e.g., PAYE)", "Tax rate increases as individual income rises.", "Wealthier citizens contribute a larger percentage, reducing economic inequality and funding social services."],
                        ["Regressive Tax", "Tax rate takes a larger percentage from low-income earners.", "Places an unfair burden on poor households (e.g., flat consumption taxes on basic survival foodstuffs)."],
                        ["Proportional Tax", "Fixed flat percentage levied regardless of income.", "Maintains identical percentage, but does not actively reduce income disparities."]
                    ]
                }
            }
        ]
    },
    {
        "page_number": 6,
        "page_title": "Intergenerational Equity and Public Debt",
        "blocks": [
            {
                "block_type": "callout",
                "component_type": "callout",
                "title": "Fiscal Responsibility: Protecting Future Generations",
                "content": {
                    "text": (
                        "**What is Intergenerational Equity?**\n"
                        "The principle that the current generation must not accumulate massive foreign debts to fund daily consumption (salaries, tea, travel), "
                        "leaving future generations to pay off debts without inheriting income-generating national assets.\n\n"
                        "**Constitutional Mandate:**\n"
                        "- Borrowed money must only be invested in long-term developmental capital assets (railways, geothermal power, referral hospitals) that benefit future generations."
                    )
                }
            }
        ]
    },
    {
        "page_number": 7,
        "page_title": "Summary Table: Article 201 Principles and KCSE Key Phrases",
        "blocks": [
            {
                "block_type": "comparison_table",
                "component_type": "comparison_table",
                "title": "Article 201 Principles Summary Table",
                "content": {
                    "headers": ["Constitutional Principle", "Core Explanation", "KCSE Marking Keyword"],
                    "rows": [
                        ["Openness & Accountability", "Budget transparency and citizen consultation.", "Public Participation / Transparency"],
                        ["Equitable Tax Burden", "Fair taxation based on ability to pay.", "Progressive Taxation"],
                        ["Revenue Devolution", "Fair sharing between National and 47 Counties.", "Equitable Share"],
                        ["Affirmative Action", "Remedying historical regional development gaps.", "Equalization Fund"],
                        ["Prudent Expenditure", "Cost-effective, zero-waste public spending.", "Fiscal Responsibility"],
                        ["Intergenerational Equity", "Balancing debt burdens between present and future.", "Sustainable Debt"],
                        ["Clear Fiscal Reporting", "Accurate public accounts and independent audits.", "Auditor-General"]
                    ]
                }
            }
        ]
    },
    {
        "page_number": 8,
        "page_title": "Interactive Classification: Applying Article 201",
        "blocks": [
            {
                "block_type": "mini_activity",
                "component_type": "mini_activity",
                "title": "Identify the Violated Public Finance Principle",
                "content": {
                    "instruction": "Match each scenario to the Article 201 principle it violates:",
                    "items": [
                        "1. County passes budget without holding public hearings -> **Openness & Public Participation**",
                        "2. Government borrows $2B foreign loan solely to fund civil servant travel allowances -> **Intergenerational Equity**",
                        "3. Ministry spends KSH 10M purchasing ballpoint pens worth KSH 100K -> **Prudent and Responsible Use of Money**",
                        "4. Introducing flat food tax taking 50% of poor farmers' income -> **Equitable Sharing of Tax Burden**"
                    ]
                }
            }
        ]
    },
    {
        "page_number": 9,
        "page_title": "KCSE Examination Coaching: Principles of Public Finance",
        "blocks": [
            {
                "block_type": "worked_example",
                "component_type": "worked_example",
                "title": "KCSE Question: Explain Five Principles of Public Finance Under the 2010 Constitution (10 Marks)",
                "content": {
                    "text": (
                        "**Model Answer (Point + Explanation = 2 Marks per Point):**\n\n"
                        "1. **Openness and Accountability (Public Participation):** Financial management must be fully transparent, allowing citizens to participate in budget debates and tax policymaking. (2 marks)\n\n"
                        "2. **Equitable Sharing of the Burden of Taxation:** The tax system must be fair, ensuring individuals contribute according to their financial capacity through progressive taxation. (2 marks)\n\n"
                        "3. **Equitable Sharing of Nationally Raised Revenue:** Revenue collected nationally must be shared equitably between the national government and the 47 county governments. (2 marks)\n\n"
                        "4. **Affirmative Action for Marginalized Regions:** Public funds like the Equalization Fund must be directed to historically underdeveloped areas to bring services up to national standards. (2 marks)\n\n"
                        "5. **Prudent and Responsible Use of Public Money:** Public funds must be spent efficiently and cost-effectively, preventing wastage, corruption, and unsustainable borrowing. (2 marks)"
                    )
                }
            }
        ]
    },
    {
        "page_number": 10,
        "page_title": "Case Study: The Equalization Fund for Marginalized Counties",
        "blocks": [
            {
                "block_type": "callout",
                "component_type": "callout",
                "title": "Affirmative Action: The Equalization Fund (0.5%)",
                "content": {
                    "text": (
                        "**Constitutional Basis:** Article 204 establishes the **Equalization Fund**, allocating 0.5% of all national revenue to marginalized counties (e.g., Turkana, Mandera, Wajir, Marsabit, Samburu).\n\n"
                        "**Four Protected Basic Services:**\n"
                        "1. Clean Piped Water\n"
                        "2. Local Access Roads\n"
                        "3. Primary Health Clinics\n"
                        "4. Electricity Grid Connection\n\n"
                        "**Pedagogical Significance:** Demonstrates how public finance actively cures historical colonial and post-independence regional disparities."
                    )
                }
            }
        ]
    },
    {
        "page_number": 11,
        "page_title": "Check Your Understanding: Module 8.1",
        "blocks": [
            {
                "block_type": "knowledge_check",
                "component_type": "knowledge_check",
                "title": "Module 8.1 Assessment",
                "content": {
                    "questions": [
                        {
                            "question": "Which chapter of the 2010 Constitution of Kenya deals with Public Finance?",
                            "options": [
                                "Chapter 4",
                                "Chapter 11",
                                "Chapter 12",
                                "Chapter 15"
                            ],
                            "correct_answer": 2,
                            "explanation": "Chapter 12 of the Constitution explicitly governs all aspects of Public Finance (Articles 201–231)."
                        },
                        {
                            "question": "What is the primary objective of the principle of 'Intergenerational Equity'?",
                            "options": [
                                "To ensure all citizens pay the same flat tax amount",
                                "To ensure the burdens and benefits of public debt are shared fairly between current and future generations",
                                "To abolish all domestic borrowing",
                                "To mandate that only youth can vote on the budget"
                            ],
                            "correct_answer": 1,
                            "explanation": "Intergenerational equity prevents current generations from passing unproductive debt burdens onto future generations."
                        }
                    ]
                }
            }
        ]
    },
    {
        "page_number": 12,
        "page_title": "Lesson Summary & Key Takeaways",
        "blocks": [
            {
                "block_type": "summary",
                "component_type": "summary",
                "title": "Core Summary: Foundations of Public Finance",
                "content": {
                    "text": (
                        "• **Public Finance:** System of raising revenue, managing funds, and planning expenditure.\n"
                        "• **Constitutional Anchoring:** Chapter 12 and Article 201 set binding rules.\n"
                        "• **Seven Principles:** Openness/public participation, fair taxation, revenue devolution, affirmative action, prudent spending, intergenerational equity, clear fiscal reporting."
                    )
                }
            },
            {
                "block_type": "key_takeaway",
                "component_type": "key_takeaway",
                "title": "Key Takeaways",
                "content": {
                    "text": (
                        "- Public finance is governed by supreme constitutional principles rather than executive discretion.\n"
                        "- Transparency and citizen participation are mandatory safeguards against corruption."
                    )
                }
            }
        ]
    },
    {
        "page_number": 13,
        "page_title": "Revision Checklist: Article 201 Principles",
        "blocks": [
            {
                "block_type": "step_process",
                "component_type": "step_process",
                "title": "Mastery Checklist",
                "content": {
                    "steps": [
                        "1. Definition of public finance and Chapter 12 structure.",
                        "2. Seven principles under Article 201 with concrete examples.",
                        "3. Four services funded by the Equalization Fund (water, roads, health, electricity).",
                        "4. Meaning and application of intergenerational equity."
                    ]
                }
            }
        ]
    },
    {
        "page_number": 14,
        "page_title": "Quick Knowledge Check: Public Finance Concepts",
        "blocks": [
            {
                "block_type": "mini_activity",
                "component_type": "mini_activity",
                "title": "Quick Recall Quiz",
                "content": {
                    "instruction": "Answer true or false:",
                    "items": [
                        "1. Progressive taxation means low earners pay higher percentage rates than rich earners -> **False (wealthier earners pay higher percentage)**",
                        "2. Public participation is constitutionally required before passing tax legislation -> **True**",
                        "3. The Equalization Fund receives 0.5% of national revenue to develop marginalized areas -> **True**"
                    ]
                }
            }
        ]
    },
    {
        "page_number": 15,
        "page_title": "Discussion: Public Debt and Economic Sovereignty",
        "blocks": [
            {
                "block_type": "callout",
                "component_type": "callout",
                "title": "Critical Inquiry: Sustainable Borrowing",
                "content": {
                    "text": (
                        "**Strategic Question:**\n"
                        "*> 'Why does excessive national borrowing threaten a country's economic sovereignty?'*\n\n"
                        "**Key Impacts:**\n"
                        "- High interest repayments drain national budgets, leaving little for hospitals and schools.\n"
                        "- Forces governments to accept foreign economic austerity conditions (such as SAPs).\n"
                        "- Triggers currency depreciation and inflation."
                    )
                }
            }
        ]
    }
]

LESSON_2_PAGES = [
    {
        "page_number": 1,
        "page_title": "The National Budget: Meaning, Importance, and Preparation Process",
        "blocks": [
            {
                "block_type": "learning_goal",
                "component_type": "learning_goal",
                "title": "Lesson Objectives: The Budget Cycle in Kenya",
                "content": {
                    "text": (
                        "By the end of this lesson, you will be able to:\n"
                        "- Define a national budget and state Kenya's financial year dates (1 July to 30 June)\n"
                        "- Explain the seven major reasons why preparing a national budget is important\n"
                        "- Trace the step-by-step national budget preparation and approval cycle (Cabinet, Submission, Committee, Debate, Appropriation Bill, Gazette)\n"
                        "- Compare the national budget process with the county budget process"
                    )
                }
            },
            {
                "block_type": "definition_card",
                "component_type": "definition_card",
                "title": "Concept: The National Budget",
                "content": {
                    "term": "National Budget",
                    "definition": (
                        "A comprehensive financial statement estimating the government's anticipated revenue, planned expenditures, "
                        "and general economic policies for an upcoming financial year (1 July to 30 June)."
                    )
                }
            }
        ]
    },
    {
        "page_number": 2,
        "page_title": "Kenya Parliament: The Seat of Budgetary Power",
        "blocks": [
            {
                "block_type": "suggested_image",
                "component_type": "suggested_image",
                "title": "Parliament of Kenya",
                "content": {
                    "text": "Parliament Buildings in Nairobi, where the National Assembly reviews, debates, and approves national budget estimates and enacts the Appropriation Bill.",
                    "url": "https://upload.wikimedia.org/wikipedia/commons/8/87/Parliament_of_Kenya.jpg",
                    "author": "Public Domain / Wikimedia Commons",
                    "licensing": "Public Domain",
                    "commons_page_url": "https://commons.wikimedia.org/wiki/File:Parliament_of_Kenya.jpg"
                }
            }
        ]
    },
    {
        "page_number": 3,
        "page_title": "Educational Documentary: Budget Presentation in Parliament",
        "blocks": [
            {
                "block_type": "suggested_video",
                "component_type": "suggested_video",
                "title": "Live Parliamentary Presentation: The National Budget Statement",
                "content": {
                    "url": "https://www.youtube.com/watch?v=gghC32mFFbg",
                    "text": "Watch the presentation of the National Budget Statement in Parliament by the Cabinet Secretary for Finance, detailing revenue targets and spending priorities.",
                    "author": "iNation7 / Parliamentary Live Coverage",
                    "licensing": "Standard YouTube License"
                }
            }
        ]
    },
    {
        "page_number": 4,
        "page_title": "Seven Reasons Why the National Budget is Important",
        "blocks": [
            {
                "block_type": "step_process",
                "component_type": "step_process",
                "title": "Importance of the National Budget (Point-Form)",
                "content": {
                    "steps": [
                        "1. Sourcing Revenue: Legally sets tax rates, customs duties, and licensing fees to raise public funds.",
                        "2. Specific Expenditure Allocation: Details exact funds allocated to ministries (health, security, education), preventing unauthorized spending.",
                        "3. Prioritizing Development Needs: Directs limited state funds toward critical priority sectors (infrastructure, agriculture).",
                        "4. Providing Information to Investors: Outlines tax incentives and economic growth targets, guiding local and foreign businesses.",
                        "5. Building International Donor Confidence: Demonstrates fiscal discipline, establishing creditworthiness with the World Bank and IMF.",
                        "6. Assessing Past Performance & Rectifying Errors: Reviews the previous fiscal year to identify revenue shortfalls or overspending.",
                        "7. Maintaining Economic Balance & Inflation Control: Balances revenue against expenditure to manage deficit financing and national debt."
                    ]
                }
            }
        ]
    },
    {
        "page_number": 5,
        "page_title": "The Step-by-Step National Budget Preparation Cycle",
        "blocks": [
            {
                "block_type": "step_process",
                "component_type": "step_process",
                "title": "The Six Phases of Budget Enactment",
                "content": {
                    "steps": [
                        "1. Departmental Formulation (Cabinet Phase): Accounting officers (PSs) submit departmental estimates to the CS for Finance at least 3 months before fiscal year-end (by March).",
                        "2. Executive Submission: CS Finance submits consolidated estimates and a 3-year Medium-Term Expenditure Framework (MTEF) to the National Assembly at least 2 months before year-end (by April).",
                        "3. Legislative Committee Review: Budget and Appropriations Committee reviews estimates, holds mandatory public hearings, and tables its report.",
                        "4. National Assembly Debate & Vote: Parliament debates the report, introduces amendments, and votes to approve the estimates.",
                        "5. Enactment of the Appropriation Bill: An Appropriation Bill is introduced to formally authorize withdrawals from the Consolidated Fund.",
                        "6. Presidential Assent & Gazette: The President assents to the Appropriation Act, which is published in the Kenya Gazette to take effect on 1st July."
                    ]
                }
            }
        ]
    },
    {
        "page_number": 6,
        "page_title": "What is an Appropriation Bill?",
        "blocks": [
            {
                "block_type": "concept_explanation",
                "component_type": "concept_explanation",
                "title": "The Legal Key to Public Money",
                "content": {
                    "text": (
                        "- **Definition:** A piece of proposed legislation introduced in the National Assembly following budget approval to formally authorize the withdrawal of funds from the **Consolidated Fund**.\n"
                        "- **Consolidated Fund Services (CFS):** Certain mandatory national expenditures do NOT require annual appropriation votes. These are charged directly onto the Consolidated Fund by the Constitution:\n"
                        "  - Salaries of the President, Judges, Auditor-General, and Controller of Budget.\n"
                        "  - Public debt repayment and national debt servicing costs."
                    )
                }
            }
        ]
    },
    {
        "page_number": 7,
        "page_title": "Budget Preparation at the County Government Level",
        "blocks": [
            {
                "block_type": "comparison_table",
                "component_type": "comparison_table",
                "title": "National vs. County Budgeting Process",
                "content": {
                    "headers": ["Stage", "National Government Budget", "County Government Budget"],
                    "rows": [
                        ["Drafting Organ", "Cabinet Secretary for Finance & Ministry Departments.", "County Executive Committee (CEC) led by Governor & CEC for Finance."],
                        ["Approving Organ", "The National Assembly (Budget & Appropriations Committee).", "The local County Assembly."],
                        ["Public Consultation", "National public hearings conducted by Parliamentary committee.", "Grassroots public participation meetings held in electoral wards."],
                        ["Enactment Law", "National Appropriation Act authorizing Consolidated Fund withdrawals.", "County Appropriation Act authorizing County Revenue Fund withdrawals."],
                        ["Withdrawal Overseer", "Controller of Budget authorizes withdrawals.", "Controller of Budget provides quarterly withdrawal approvals."]
                    ]
                }
            }
        ]
    },
    {
        "page_number": 8,
        "page_title": "Interactive Flow: The National Budget Cycle",
        "blocks": [
            {
                "block_type": "mini_activity",
                "component_type": "mini_activity",
                "title": "Arrange the Budget Process in Chronological Order",
                "content": {
                    "instruction": "Order the budget steps from first to last:",
                    "items": [
                        "1. Accounting officers submit departmental estimates to CS Finance -> **Step 1 (March)**",
                        "2. CS Finance submits estimates & 3-year MTEF to National Assembly -> **Step 2 (April)**",
                        "3. Budget & Appropriations Committee holds public hearings -> **Step 3 (May)**",
                        "4. National Assembly votes and passes the Appropriation Bill -> **Step 4 (June)**",
                        "5. President assents and funds become available on 1st July -> **Step 5 (July 1st)**"
                    ]
                }
            }
        ]
    },
    {
        "page_number": 9,
        "page_title": "KCSE Examination Coaching: Importance of the Budget",
        "blocks": [
            {
                "block_type": "worked_example",
                "component_type": "worked_example",
                "title": "KCSE Question: Discuss Six Reasons Why It is Important to Prepare an Annual Budget (12 Marks)",
                "content": {
                    "text": (
                        "**Model Answer (Point + Explanation = 2 Marks per Point):**\n\n"
                        "1. **Enables the Government to Source Revenue:** Legally sets the rates of direct and indirect taxes, customs duties, and licensing fees needed to fund operations. (2 marks)\n\n"
                        "2. **Identifies and Allocates Specific Expenditures:** Specifies exact budgetary amounts for each ministry, preventing arbitrary or illegal spending. (2 marks)\n\n"
                        "3. **Prioritizes National Development Needs:** Directs scarce resources toward the most vital sectors (health, education, roads, security). (2 marks)\n\n"
                        "4. **Guides Domestic and Foreign Investors:** Provides crucial data on tax incentives, infrastructural projects, and economic targets. (2 marks)\n\n"
                        "5. **Builds Confidence Among International Donors:** Demonstrates creditworthiness and fiscal discipline to lenders like the World Bank and IMF. (2 marks)\n\n"
                        "6. **Assesses Past Performance and Corrects Mistakes:** Reviews the previous year's performance to rectify revenue deficits and curb corruption. (2 marks)"
                    )
                }
            }
        ]
    },
    {
        "page_number": 10,
        "page_title": "KCSE Examination Coaching: Budget Preparation Steps",
        "blocks": [
            {
                "block_type": "worked_example",
                "component_type": "worked_example",
                "title": "KCSE Question: Describe Five Stages in the National Budget Preparation Process (10 Marks)",
                "content": {
                    "text": (
                        "**Model Answer (Point + Explanation = 2 Marks per Point):**\n\n"
                        "1. **Departmental Formulation:** Heads of departments and ministries prepare their annual estimates and submit them to the Cabinet Secretary for Finance at least 3 months before fiscal year-end. (2 marks)\n\n"
                        "2. **Submission to National Assembly:** The CS for Finance consolidates estimates and submits them along with a 3-year Medium-Term plan to the National Assembly at least 2 months before year-end. (2 marks)\n\n"
                        "3. **Committee Review & Public Participation:** The Budget and Appropriations Committee reviews the estimates, conducts public hearings, and prepares a report for the House. (2 marks)\n\n"
                        "4. **Debate and Vote:** The National Assembly debates the report, proposes amendments, and votes to approve the budget. (2 marks)\n\n"
                        "5. **Enacting the Appropriation Bill:** Parliament passes the Appropriation Bill, and the President signs it into law (Appropriation Act), published in the Kenya Gazette. (2 marks)"
                    )
                }
            }
        ]
    },
    {
        "page_number": 11,
        "page_title": "Check Your Understanding: Module 8.2",
        "blocks": [
            {
                "block_type": "knowledge_check",
                "component_type": "knowledge_check",
                "title": "Module 8.2 Assessment",
                "content": {
                    "questions": [
                        {
                            "question": "What is the official timeframe of the financial year in Kenya?",
                            "options": [
                                "1st January to 31st December",
                                "1st July to 30th June",
                                "1st April to 31st March",
                                "1st October to 30th September"
                            ],
                            "correct_answer": 1,
                            "explanation": "In Kenya, the government financial year runs from 1st July to 30th June of the following year."
                        },
                        {
                            "question": "What is the primary function of an Appropriation Bill?",
                            "options": [
                                "To dissolve Parliament at the end of its term",
                                "To formally authorize the withdrawal and expenditure of money from the Consolidated Fund",
                                "To appoint new judges to the Supreme Court",
                                "To declare a state of emergency"
                            ],
                            "correct_answer": 1,
                            "explanation": "An Appropriation Bill authorizes lawful withdrawals from the Consolidated Fund to fund approved expenditures."
                        }
                    ]
                }
            }
        ]
    },
    {
        "page_number": 12,
        "page_title": "Lesson Summary & Key Takeaways",
        "blocks": [
            {
                "block_type": "summary",
                "component_type": "summary",
                "title": "Core Summary: The National Budget",
                "content": {
                    "text": (
                        "• **National Budget:** Annual policy document estimating revenue and expenditure (1 July–30 June).\n"
                        "• **Importance:** Sourcing revenue, specific allocations, investor confidence, donor credibility, debt management.\n"
                        "• **Preparation Cycle:** Department estimates -> CS submission -> Budget Committee hearings -> NA debate/vote -> Appropriation Act -> Presidential assent & Gazette."
                    )
                }
            },
            {
                "block_type": "key_takeaway",
                "component_type": "key_takeaway",
                "title": "Key Takeaways",
                "content": {
                    "text": (
                        "- The budget is the primary instrument of economic governance in Kenya.\n"
                        "- No public funds can be withdrawn without an Appropriation Act passed by Parliament."
                    )
                }
            }
        ]
    },
    {
        "page_number": 13,
        "page_title": "Revision Checklist: National Budgeting",
        "blocks": [
            {
                "block_type": "step_process",
                "component_type": "step_process",
                "title": "Mastery Checklist",
                "content": {
                    "steps": [
                        "1. Kenya fiscal year dates: 1 July to 30 June.",
                        "2. Seven reasons why the budget is important.",
                        "3. Six stages of the national budget cycle.",
                        "4. Role of the Appropriation Bill and Consolidated Fund Services."
                    ]
                }
            }
        ]
    },
    {
        "page_number": 14,
        "page_title": "Quick Knowledge Check: Budget Cycle",
        "blocks": [
            {
                "block_type": "mini_activity",
                "component_type": "mini_activity",
                "title": "Quick Recall Quiz",
                "content": {
                    "instruction": "Identify the office or document described:",
                    "items": [
                        "1. Parliamentary committee that conducts public hearings on the budget -> **Budget and Appropriations Committee**",
                        "2. Document authorizing withdrawals from the Consolidated Fund -> **Appropriation Act**",
                        "3. Executive official who presents the Budget Statement in Parliament -> **Cabinet Secretary for Finance**"
                    ]
                }
            }
        ]
    },
    {
        "page_number": 15,
        "page_title": "The Medium-Term Expenditure Framework (MTEF)",
        "blocks": [
            {
                "block_type": "concept_explanation",
                "component_type": "concept_explanation",
                "title": "Three-Year Rolling Budget Plan",
                "content": {
                    "text": (
                        "- **What is MTEF?** A 3-year rolling fiscal plan that links government policy objectives to multi-year spending programs.\n"
                        "- **Why is it Necessary?** Major capital projects (railways, expressways, dams) take several years to construct. MTEF guarantees funding continuity across consecutive financial years."
                    )
                }
            }
        ]
    },
    {
        "page_number": 16,
        "page_title": "Final Review: Budget Terminology",
        "blocks": [
            {
                "block_type": "step_process",
                "component_type": "step_process",
                "title": "Key Budget Terms",
                "content": {
                    "steps": [
                        "1. Fiscal Year: 1 July to 30 June.",
                        "2. Appropriation Bill: Law authorizing withdrawals from public funds.",
                        "3. Budget Deficit: When government expenditure exceeds total revenue.",
                        "4. Supplementary Budget: Mid-year mini-budget passed by Parliament to fund emergency or unexpected costs."
                    ]
                }
            }
        ]
    }
]

LESSON_3_PAGES = [
    {
        "page_number": 1,
        "page_title": "Sources of Public Revenue (National and County Governments)",
        "blocks": [
            {
                "block_type": "learning_goal",
                "component_type": "learning_goal",
                "title": "Lesson Objectives: Revenue Streams and Taxation",
                "content": {
                    "text": (
                        "By the end of this lesson, you will be able to:\n"
                        "- Classify national revenue into Domestic Sources (Tax & Non-Tax) and External Sources (Bilateral & Multilateral Aid)\n"
                        "- Distinguish between Direct Taxes (PAYE, Corporation Tax) and Indirect Taxes (VAT, Customs, Excise, Export Duties)\n"
                        "- Outline the five revenue streams of County Governments (Equitable Share, Grants, Own-Source, Borrowing, Donations)\n"
                        "- Analyze strict constitutional regulations governing taxation (Article 209/210)"
                    )
                }
            },
            {
                "block_type": "definition_card",
                "component_type": "definition_card",
                "title": "Concept: Public Revenue",
                "content": {
                    "term": "Public Revenue",
                    "definition": (
                        "The total funds collected by the state from domestic taxes, public service fees, commercial investments, "
                        "and external loans/grants to finance public administration and national development."
                    )
                }
            }
        ]
    },
    {
        "page_number": 2,
        "page_title": "Times Tower Nairobi: Headquarters of KRA",
        "blocks": [
            {
                "block_type": "suggested_image",
                "component_type": "suggested_image",
                "title": "Times Tower Nairobi",
                "content": {
                    "text": "Times Tower in Nairobi, headquarters of the Kenya Revenue Authority (KRA), the national agency responsible for tax collection and administration.",
                    "url": "https://upload.wikimedia.org/wikipedia/commons/3/30/Times_Tower%2C_Nairobi.jpg",
                    "author": "Public Domain / Wikimedia Commons",
                    "licensing": "Public Domain",
                    "commons_page_url": "https://commons.wikimedia.org/wiki/File:Times_Tower,_Nairobi.jpg"
                }
            }
        ]
    },
    {
        "page_number": 3,
        "page_title": "Educational Video: KRA and Sources of Public Revenue",
        "blocks": [
            {
                "block_type": "suggested_video",
                "component_type": "suggested_video",
                "title": "Educational Guide: How the Kenya Revenue Authority (KRA) Mobilizes Revenue",
                "content": {
                    "url": "https://www.youtube.com/watch?v=Ov2dRl-4Shg",
                    "text": "Examine the tax collection mechanisms utilized by KRA, direct and indirect taxation categories, and filing of returns.",
                    "author": "Kenya Revenue Authority / Public Education",
                    "licensing": "Standard YouTube License"
                }
            }
        ]
    },
    {
        "page_number": 4,
        "page_title": "Domestic Revenue Sources: Direct vs. Indirect Taxes",
        "blocks": [
            {
                "block_type": "comparison_table",
                "component_type": "comparison_table",
                "title": "Direct Taxes vs. Indirect Taxes",
                "content": {
                    "headers": ["Tax Category", "Definition & Shifting", "Examinable Core Examples"],
                    "rows": [
                        ["Direct Taxes", "Levied directly on the income or profits of individuals and companies; cannot be shifted.", "• Pay-As-You-Earn (PAYE) on monthly salaries\n• Corporation Tax on net business profits\n• Capital Gains Tax on property/share sales"],
                        ["Indirect Taxes", "Levied on goods and services; can be shifted from retailers to the final consumer.", "• Value-Added Tax (VAT) on consumer goods/fuel\n• Customs Duties on foreign imports\n• Excise Duty on alcohol, cigarettes, luxury goods\n• Export Duty on raw agricultural exports"]
                    ]
                }
            }
        ]
    },
    {
        "page_number": 5,
        "page_title": "Domestic Non-Tax Revenues for the National Government",
        "blocks": [
            {
                "block_type": "step_process",
                "component_type": "step_process",
                "title": "Eight Domestic Non-Tax Revenue Streams",
                "content": {
                    "steps": [
                        "1. Service Fees & Charges: Fees paid for direct government services (passports, national identity cards, birth certificates, water).",
                        "2. Court Fines: Monetary penalties imposed by courts of law on convicted offenders.",
                        "3. Parastatal Dividends & Profits: Profits earned from state-owned enterprises (Kenya Pipeline, KCB shares, KenGen).",
                        "4. Loan Interest Receipts: Interest earned from loans advanced by the national government to state parastatals.",
                        "5. Public Land & House Rent: Fees paid for public land leases and rent collected from civil servant housing.",
                        "6. Natural Resource Royalties: Mining royalties, carbon dioxide levies, and timber extraction fees.",
                        "7. Tourism & Conservation Fees: Park entry fees from local and foreign tourists visiting national game parks.",
                        "8. Domestic Borrowing: Sale of Treasury Bills (short-term) and Government Treasury Bonds (long-term) to local banks and investors."
                    ]
                }
            }
        ]
    },
    {
        "page_number": 6,
        "page_title": "External Revenue Sources: Bilateral vs. Multilateral Aid",
        "blocks": [
            {
                "block_type": "comparison_table",
                "component_type": "comparison_table",
                "title": "Bilateral Aid vs. Multilateral Aid",
                "content": {
                    "headers": ["Type of External Aid", "Definition", "Concrete Examples"],
                    "rows": [
                        ["Bilateral Aid", "Direct economic, financial, or technical assistance provided by one sovereign country directly to another.", "Direct grants and infrastructural loans from Japan (JICA), the United States (USAID), or China to Kenya."],
                        ["Multilateral Aid", "Assistance provided by international financial bodies comprised of multiple member countries.", "Developmental loans and grants from the World Bank, International Monetary Fund (IMF), African Development Bank (AfDB), and European Union."]
                    ]
                }
            }
        ]
    },
    {
        "page_number": 7,
        "page_title": "Sources of Revenue for County Governments",
        "blocks": [
            {
                "block_type": "step_process",
                "component_type": "step_process",
                "title": "Five Financial Streams for Counties",
                "content": {
                    "steps": [
                        "1. Equitable Share (Min 15%): Constitutionally guaranteed minimum 15% share of all national revenue collected, divided equitably among 47 counties.",
                        "2. County Own-Source Revenues: Local property rates, parking fees, single business permits, entertainment taxes, and market cess.",
                        "3. Conditional & Unconditional Grants: Additional funds allocated by the national government (e.g., Equalization Fund 0.5% for marginalized areas).",
                        "4. Guaranteed Loans & Borrowing: Commercial loans borrowed with County Assembly approval and National Treasury guarantee.",
                        "5. Direct Grants and NGO Donations: Direct financial or equipment donations from development partners and non-governmental organizations."
                    ]
                }
            }
        ]
    },
    {
        "page_number": 8,
        "page_title": "Constitutional Regulations Governing Taxation (Articles 209 & 210)",
        "blocks": [
            {
                "block_type": "step_process",
                "component_type": "step_process",
                "title": "Strict Constitutional Taxation Rules",
                "content": {
                    "steps": [
                        "1. Exclusive National Powers: Only the National Government can impose Income Tax, VAT, Customs duties, and Excise duties.",
                        "2. County Taxation Boundaries: Counties are restricted to property rates, entertainment taxes, and local service fees; county taxes must not disrupt inter-county trade.",
                        "3. No Arbitrary Tax Waivers: No tax or licensing fee can be waived without explicit statutory authority; all waivers must be reported to the Auditor-General.",
                        "4. Universal Taxation of State Officers: No law can exempt any public official (including the President, judges, or MPs) from paying tax."
                    ]
                }
            }
        ]
    },
    {
        "page_number": 9,
        "page_title": "Case Study: The 2004 Kenya-Egypt Cement Dispute under COMESA",
        "blocks": [
            {
                "block_type": "callout",
                "component_type": "callout",
                "title": "Trade Conflict: Customs Tariffs in Regional Blocs",
                "content": {
                    "text": (
                        "**The Dispute:** In 2004, Egyptian cement flooded the Kenyan market at heavily subsidized prices, threatening to collapse local Kenyan cement manufacturers.\n\n"
                        "**Kenya's Response:** Imposed protective customs duties and tariffs on Egyptian cement.\n\n"
                        "**The Resolution:** Egypt appealed to the **COMESA Court of Justice**, which mediated the dispute, balancing national infant industry protection against regional free-trade tariff agreements."
                    )
                }
            }
        ]
    },
    {
        "page_number": 10,
        "page_title": "Interactive Classification: Revenue Sources",
        "blocks": [
            {
                "block_type": "mini_activity",
                "component_type": "mini_activity",
                "title": "Classify the Revenue Source",
                "content": {
                    "instruction": "Identify the revenue type correctly:",
                    "items": [
                        "1. PAYE deducted from a high school teacher's salary -> **Direct Tax**",
                        "2. 16% VAT charged on purchasing a smartphone -> **Indirect Tax**",
                        "3. Parking fee paid to Nairobi City County -> **County Own-Source Revenue**",
                        "4. $50M development grant from the World Bank -> **Multilateral External Aid**",
                        "5. Direct infrastructure grant from the government of Japan -> **Bilateral External Aid**",
                        "6. Fines paid in court by traffic law offenders -> **Domestic Non-Tax Revenue**"
                    ]
                }
            }
        ]
    },
    {
        "page_number": 11,
        "page_title": "KCSE Examination Coaching: Sources of Revenue",
        "blocks": [
            {
                "block_type": "worked_example",
                "component_type": "worked_example",
                "title": "KCSE Question: Explain Five Sources of Revenue for the National Government (10 Marks)",
                "content": {
                    "text": (
                        "**Model Answer (Point + Explanation = 2 Marks per Point):**\n\n"
                        "1. **Direct Taxes (Income Tax):** Taxes levied directly on individuals' earnings (PAYE) and corporation profits of registered companies. (2 marks)\n\n"
                        "2. **Indirect Taxes (VAT, Customs, Excise):** Taxes charged on consumer goods, foreign imports, and excisable items (cigarettes, alcohol) collected through business intermediaries. (2 marks)\n\n"
                        "3. **Non-Tax Service Fees and Fines:** Charges for issuing passports, national identity cards, licensing fees, and penalties imposed by courts of law. (2 marks)\n\n"
                        "4. **Profits and Dividends from State Parastatals:** Earnings and share dividends from commercial state corporations such as KenGen and Kenya Pipeline. (2 marks)\n\n"
                        "5. **External Loans and Grants:** Bilateral aid from friendly nations and multilateral loans from the World Bank and IMF. (2 marks)"
                    )
                }
            }
        ]
    },
    {
        "page_number": 12,
        "page_title": "Check Your Understanding: Module 8.3",
        "blocks": [
            {
                "block_type": "knowledge_check",
                "component_type": "knowledge_check",
                "title": "Module 8.3 Assessment",
                "content": {
                    "questions": [
                        {
                            "question": "Which of the following is an example of an indirect tax in Kenya?",
                            "options": [
                                "Pay-As-You-Earn (PAYE)",
                                "Corporation Tax",
                                "Value-Added Tax (VAT)",
                                "Capital Gains Tax"
                            ],
                            "correct_answer": 2,
                            "explanation": "VAT is an indirect consumption tax paid by consumers through retail prices."
                        },
                        {
                            "question": "Under Article 209 of the Constitution, which level of government has exclusive authority to impose Income Tax and Customs Duties?",
                            "options": [
                                "County Governments",
                                "The National Government",
                                "Both National and County Governments concurrently",
                                "The Central Bank of Kenya"
                            ],
                            "correct_answer": 1,
                            "explanation": "Only the National Government has the power to levy Income Tax, VAT, Customs, and Excise duties."
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
                "title": "Core Summary: Sources of Public Revenue",
                "content": {
                    "text": (
                        "• **National Domestic Taxes:** Direct (PAYE, Corporation Tax) vs. Indirect (VAT, Customs, Excise, Export Duties).\n"
                        "• **National Non-Tax:** Service charges, court fines, parastatal dividends, land rates, domestic Treasury Bills/Bonds.\n"
                        "• **External Revenue:** Bilateral aid (country-to-country) vs. Multilateral aid (World Bank, IMF, AfDB).\n"
                        "• **County Finances:** Min 15% Equitable Share, Own-Source revenues, Equalization Fund, guaranteed borrowing.\n"
                        "• **Tax Regulations:** Exclusive national tax powers, county trade protections, no state officer tax exemptions."
                    )
                }
            },
            {
                "block_type": "key_takeaway",
                "component_type": "key_takeaway",
                "title": "Key Takeaways",
                "content": {
                    "text": (
                        "- Taxes fund public development and redistribute wealth to protect low-income citizens.\n"
                        "- Strict constitutional rules prevent predatory local taxation and safeguard inter-county commerce."
                    )
                }
            }
        ]
    },
    {
        "page_number": 14,
        "page_title": "Revision Checklist: Public Revenue",
        "blocks": [
            {
                "block_type": "step_process",
                "component_type": "step_process",
                "title": "Mastery Checklist",
                "content": {
                    "steps": [
                        "1. Direct taxes (PAYE, Corporation Tax) vs. Indirect taxes (VAT, Customs, Excise).",
                        "2. Eight domestic non-tax revenue sources.",
                        "3. Bilateral aid vs. Multilateral aid.",
                        "4. Five county revenue sources.",
                        "5. Constitutional taxation rules under Articles 209 and 210."
                    ]
                }
            }
        ]
    },
    {
        "page_number": 15,
        "page_title": "Quick Knowledge Check: Taxation Principles",
        "blocks": [
            {
                "block_type": "mini_activity",
                "component_type": "mini_activity",
                "title": "Quick Recall Quiz",
                "content": {
                    "instruction": "Answer true or false:",
                    "items": [
                        "1. County governments are permitted to impose income taxes -> **False (exclusive national power)**",
                        "2. Members of Parliament and judges are exempt from paying PAYE tax -> **False (no state officer is exempt)**",
                        "3. Treasury Bills are short-term domestic borrowing instruments -> **True**"
                    ]
                }
            }
        ]
    },
    {
        "page_number": 16,
        "page_title": "Customs Duties as an Economic Shield",
        "blocks": [
            {
                "block_type": "concept_explanation",
                "component_type": "concept_explanation",
                "title": "Protecting Infant Industries",
                "content": {
                    "text": (
                        "- **Tariff Protection:** Imposing high import tariffs on imported goods (sugar, textiles, footwear) makes them more expensive than locally manufactured goods.\n"
                        "- **Economic Objective:** Protects local Kenyan farmers and factories from unfair foreign dumping, safeguarding domestic jobs."
                    )
                }
            }
        ]
    }
]

LESSON_4_PAGES = [
    {
        "page_number": 1,
        "page_title": "National Public Funds, Equitable Allocation, and Expenditure",
        "blocks": [
            {
                "block_type": "learning_goal",
                "component_type": "learning_goal",
                "title": "Lesson Objectives: Public Funds and Expenditure Classification",
                "content": {
                    "text": (
                        "By the end of this lesson, you will be able to:\n"
                        "- Describe the four constitutional public funds (Consolidated Fund, Equalization Fund, Contingencies Fund, County Revenue Funds)\n"
                        "- Analyze the eleven criteria determining the equitable sharing of revenue under Article 203\n"
                        "- Classify government expenditure into Capital (Development) and Recurrent components\n"
                        "- Evaluate how public expenditure drives national development and debt sustainability"
                    )
                }
            },
            {
                "block_type": "definition_card",
                "component_type": "definition_card",
                "title": "Concept: Constitutional Public Funds",
                "content": {
                    "term": "Consolidated Fund",
                    "definition": (
                        "The primary constitutional repository into which all revenue raised or received by the national government "
                        "must be paid, and from which withdrawals can only be made under an Act of Parliament or constitutional provision."
                    )
                }
            }
        ]
    },
    {
        "page_number": 2,
        "page_title": "Educational Documentary: Government Expenditure & Deficits",
        "blocks": [
            {
                "block_type": "suggested_video",
                "component_type": "suggested_video",
                "title": "Economic Analysis: Government Expenditure and National Budget Trends",
                "content": {
                    "url": "https://www.youtube.com/watch?v=GYMbeyUXq9s",
                    "text": "Examine how government recurrent and capital expenditures are managed, and how fiscal deficits are financed in Kenya.",
                    "author": "NTV Kenya / Economic & Financial News",
                    "licensing": "Standard YouTube License"
                }
            }
        ]
    },
    {
        "page_number": 3,
        "page_title": "The Four Constitutional Public Funds",
        "blocks": [
            {
                "block_type": "comparison_table",
                "component_type": "comparison_table",
                "title": "The Four Constitutional Public Funds in Kenya",
                "content": {
                    "headers": ["Constitutional Fund", "Legal Definition & Source", "Core Purpose & Withdrawal Rules"],
                    "rows": [
                        ["The Consolidated Fund (Article 206)", "Primary national fund receiving all taxes and national revenues.", "Pays for all approved national expenditures and Consolidated Fund Services (judges' salaries, debt servicing). Withdrawals require an Appropriation Act & Controller of Budget approval."],
                        ["The Equalization Fund (Article 204)", "Receives 0.5% of all national revenue annually.", "Provides basic services (water, roads, health, electricity) to historically marginalized counties to bring them to national standards."],
                        ["The Contingencies Fund (Article 208)", "Fund established by Parliament for emergency advances.", "Provides urgent, unforeseen emergency funding (floods, famines, epidemics) when no budgetary provision exists. Requires retrospective Parliamentary approval."],
                        ["County Revenue Funds (Article 207)", "Established by each of the 47 County Governments.", "Receives all equitable share transfers, grants, and local own-source revenues. Withdrawals require County Assembly approval and Controller of Budget authorization."]
                    ]
                }
            }
        ]
    },
    {
        "page_number": 4,
        "page_title": "Eleven Criteria for Equitable Sharing (Article 203)",
        "blocks": [
            {
                "block_type": "step_process",
                "component_type": "step_process",
                "title": "Article 203 Revenue Sharing Criteria (Point-Form)",
                "content": {
                    "steps": [
                        "1. The National Interest: Protecting the security, stability, and sovereignty of the nation as a whole.",
                        "2. Public Debt Obligations: Provision must be made for public debt servicing and debt repayment before sharing.",
                        "3. Needs of the National Government: Ensuring the national executive, judiciary, parliament, and security forces operate effectively.",
                        "4. Needs of County Governments: Guaranteeing counties have sufficient funds to deliver Fourth Schedule functions.",
                        "5. Fiscal Capacity and Efficiency: Rewarding counties that manage resources prudently and collect local taxes efficiently.",
                        "6. Developmental Needs of Counties: Accounting for county land size, infrastructure backlogs, and population demands.",
                        "7. Economic Disparities: Using revenue allocation to reduce wealth and developmental inequalities between regions.",
                        "8. Affirmative Action for Marginalized Areas: Giving extra financial support to historically neglected counties.",
                        "9. Incentives for Economic Optimization: Encouraging counties to expand their own local tax bases.",
                        "10. Desirability of Stable & Predictable Allocations: Ensuring counties can plan multi-year development projects without disruption.",
                        "11. Flexibility in Emergencies: Retaining fiscal space to respond to unexpected national disasters or economic crises."
                    ]
                }
            }
        ]
    },
    {
        "page_number": 5,
        "page_title": "Classification of Government Expenditure",
        "blocks": [
            {
                "block_type": "comparison_table",
                "component_type": "comparison_table",
                "title": "Capital Expenditure vs. Recurrent Expenditure",
                "content": {
                    "headers": ["Expenditure Category", "Definition & Focus", "Concrete National & County Examples"],
                    "rows": [
                        ["Capital (Development) Expenditure", "Spending on new, long-term development projects that construct economic assets and support future growth.", "• National: Constructing Standard Gauge Railway, superhighways, geothermal dams, national referral hospitals.\n• County: Building ECDE nurseries, village polytechnics, tarmac access roads."],
                        ["Recurrent Expenditure", "Regular, ongoing spending throughout the year to maintain existing facilities and sustain daily operations.", "• National: Monthly salaries for teachers/police/civil servants, debt servicing, foreign embassy maintenance.\n• County: County staff salaries, purchasing hospital drugs, garbage collection fuel."]
                    ]
                }
            }
        ]
    },
    {
        "page_number": 6,
        "page_title": "Consolidated Fund Services (CFS)",
        "blocks": [
            {
                "block_type": "step_process",
                "component_type": "step_process",
                "title": "Expenditures Charged Directly on the Consolidated Fund",
                "content": {
                    "steps": [
                        "1. Public Debt Servicing: Principal repayments and interest on domestic Treasury Bonds and foreign Eurobonds.",
                        "2. Constitutional Office Salaries: Salaries of the President, Deputy President, Chief Justice, Supreme Court Judges, Auditor-General, and Controller of Budget.",
                        "3. Pensions and Gratuities: Retirement benefits payable to retired public servants and judges.",
                        "4. Subscription to International Bodies: Mandatory statutory contributions to the United Nations, African Union, and East African Community."
                    ]
                }
            }
        ]
    },
    {
        "page_number": 7,
        "page_title": "Interactive Classification: Capital vs. Recurrent Expenditure",
        "blocks": [
            {
                "block_type": "mini_activity",
                "component_type": "mini_activity",
                "title": "Classify the Government Expenditure",
                "content": {
                    "instruction": "Categorize each expenditure item as Capital or Recurrent:",
                    "items": [
                        "1. Construction of the Nairobi Expressway -> **Capital Expenditure**",
                        "2. Monthly payment of teachers' salaries by TSC -> **Recurrent Expenditure**",
                        "3. Servicing the national public debt -> **Recurrent Expenditure (CFS)**",
                        "4. Building a new 500-bed county referral hospital -> **Capital Expenditure**",
                        "5. Purchasing medicines and bandages for a dispensary -> **Recurrent Expenditure**",
                        "6. Constructing a geothermal power plant at Olkaria -> **Capital Expenditure**"
                    ]
                }
            }
        ]
    },
    {
        "page_number": 8,
        "page_title": "KCSE Examination Coaching: Capital vs. Recurrent Expenditure",
        "blocks": [
            {
                "block_type": "worked_example",
                "component_type": "worked_example",
                "title": "KCSE Question: Explain the Difference Between Capital and Recurrent Expenditure with Four Examples of Each (10 Marks)",
                "content": {
                    "text": (
                        "**Model Answer:**\n\n"
                        "- **Difference (2 Marks):** Capital expenditure refers to money spent on new, long-term developmental projects that build physical assets and infrastructure. Recurrent expenditure is ongoing operational spending required to maintain public facilities and deliver daily government services.\n\n"
                        "- **Capital Expenditure Examples (4 Marks):**\n"
                        "  1. Construction of national railway networks and superhighways.\n"
                        "  2. Construction of public universities and tertiary training colleges.\n"
                        "  3. Building national referral hospitals and medical research centers.\n"
                        "  4. Developing hydro-power and geothermal electricity generation stations.\n\n"
                        "- **Recurrent Expenditure Examples (4 Marks):**\n"
                        "  1. Payment of monthly salaries to civil servants, police, military, and teachers.\n"
                        "  2. Servicing and repaying domestic and foreign public debts.\n"
                        "  3. Repair and routine maintenance of existing government buildings and vehicles.\n"
                        "  4. Maintaining diplomatic missions, embassies, and high commissions abroad."
                    )
                }
            }
        ]
    },
    {
        "page_number": 9,
        "page_title": "KCSE Examination Coaching: Criteria for Revenue Sharing",
        "blocks": [
            {
                "block_type": "worked_example",
                "component_type": "worked_example",
                "title": "KCSE Question: Explain Six Criteria Used in Determining the Equitable Sharing of Revenue (12 Marks)",
                "content": {
                    "text": (
                        "**Model Answer (Point + Explanation = 2 Marks per Point):**\n\n"
                        "1. **The National Interest:** Allocations must preserve national sovereignty, security, and territorial integrity. (2 marks)\n\n"
                        "2. **Public Debt Obligations:** Funds must be set aside to service and repay national debt before revenues are shared. (2 marks)\n\n"
                        "3. **Needs of the National Government:** Allocations must ensure national executive, judicial, and legislative organs function smoothly. (2 marks)\n\n"
                        "4. **Needs of County Governments:** Ensures counties receive adequate funding to deliver devolved Fourth Schedule services. (2 marks)\n\n"
                        "5. **Fiscal Capacity and Efficiency:** Rewards counties that collect local revenues effectively and spend prudently. (2 marks)\n\n"
                        "6. **Economic Disparities and Affirmative Action:** Uses allocation formulas to reduce developmental gaps and support historically marginalized regions. (2 marks)"
                    )
                }
            }
        ]
    },
    {
        "page_number": 10,
        "page_title": "Case Study: Managing Emergency Disasters via the Contingencies Fund",
        "blocks": [
            {
                "block_type": "callout",
                "component_type": "callout",
                "title": "Disaster Response: The Contingencies Fund",
                "content": {
                    "text": (
                        "**Scenario:** Massive El Niño floods wash away bridges and displace 50,000 families in late November. The annual budget passed in June had no funds for flood relief.\n\n"
                        "**Legal Procedure:**\n"
                        "1. CS for Finance authorizes an emergency advance from the **Contingencies Fund**.\n"
                        "2. Controller of Budget confirms urgency and approves the cash withdrawal.\n"
                        "3. CS submits a **Supplementary Appropriation Bill** to Parliament within two months to regularize the expenditure."
                    )
                }
            }
        ]
    },
    {
        "page_number": 11,
        "page_title": "Check Your Understanding: Module 8.4",
        "blocks": [
            {
                "block_type": "knowledge_check",
                "component_type": "knowledge_check",
                "title": "Module 8.4 Assessment",
                "content": {
                    "questions": [
                        {
                            "question": "Which constitutional public fund receives 0.5% of national revenue to provide water, health, and roads to marginalized counties?",
                            "options": [
                                "The Consolidated Fund",
                                "The Equalization Fund",
                                "The Contingencies Fund",
                                "The County Revenue Fund"
                            ],
                            "correct_answer": 1,
                            "explanation": "The Equalization Fund is allocated 0.5% of national revenue under Article 204."
                        },
                        {
                            "question": "Which of the following is classified as Capital (Development) Expenditure?",
                            "options": [
                                "Paying monthly salaries to teachers",
                                "Constructing a new hydro-electric power dam",
                                "Maintaining foreign embassies in London and Washington",
                                "Purchasing stationery for government ministries"
                            ],
                            "correct_answer": 1,
                            "explanation": "Constructing a hydro-electric dam builds a long-term capital asset for economic growth."
                        }
                    ]
                }
            }
        ]
    },
    {
        "page_number": 12,
        "page_title": "Lesson Summary & Key Takeaways",
        "blocks": [
            {
                "block_type": "summary",
                "component_type": "summary",
                "title": "Core Summary: Public Funds and Expenditure",
                "content": {
                    "text": (
                        "• **Constitutional Funds:** Consolidated Fund (primary national vault), Equalization Fund (0.5% marginalized areas), Contingencies Fund (emergencies), County Revenue Funds.\n"
                        "• **Article 203 Sharing Criteria:** 11 factors balancing national interest, debt obligations, county needs, fiscal efficiency, and affirmative action.\n"
                        "• **Expenditure Types:** Capital (long-term infrastructure) vs. Recurrent (operational costs, salaries, debt servicing)."
                    )
                }
            },
            {
                "block_type": "key_takeaway",
                "component_type": "key_takeaway",
                "title": "Key Takeaways",
                "content": {
                    "text": (
                        "- Public funds are constitutionally segmented to guarantee fiscal transparency and emergency flexibility.\n"
                        "- Sustainable budgeting prioritizes capital development over wasteful recurrent consumption."
                    )
                }
            }
        ]
    },
    {
        "page_number": 13,
        "page_title": "Revision Checklist: Public Funds and Expenditure",
        "blocks": [
            {
                "block_type": "step_process",
                "component_type": "step_process",
                "title": "Mastery Checklist",
                "content": {
                    "steps": [
                        "1. Four constitutional funds and their functions.",
                        "2. Eleven criteria determining equitable sharing under Article 203.",
                        "3. Four examples each of capital and recurrent expenditure.",
                        "4. Purpose of the Consolidated Fund Services (CFS)."
                    ]
                }
            }
        ]
    },
    {
        "page_number": 14,
        "page_title": "Quick Knowledge Check: Public Funds",
        "blocks": [
            {
                "block_type": "mini_activity",
                "component_type": "mini_activity",
                "title": "Quick Recall Quiz",
                "content": {
                    "instruction": "Identify the fund described:",
                    "items": [
                        "1. Main national account into which all taxes must be deposited -> **Consolidated Fund**",
                        "2. Emergency fund used by CS Finance to fund unexpected natural disasters -> **Contingencies Fund**",
                        "3. Dedicated account for basic services in historically marginalized counties -> **Equalization Fund**",
                        "4. Account operated by each of the 47 county governments -> **County Revenue Fund**"
                    ]
                }
            }
        ]
    },
    {
        "page_number": 15,
        "page_title": "Fiscal Discipline: Balancing the Budget",
        "blocks": [
            {
                "block_type": "callout",
                "component_type": "callout",
                "title": "The Golden Rule of Public Finance",
                "content": {
                    "text": (
                        "**Public Finance Management (PFM) Act Rule:**\n"
                        "- At least **30%** of total national and county budgets MUST be allocated to **Capital (Development) Expenditure**.\n"
                        "- Recurrent expenditure (wages, travel, perks) must not exceed **70%** of the budget.\n\n"
                        "**Goal:** Ensures the country continues building new assets for economic expansion rather than consuming everything in salaries."
                    )
                }
            }
        ]
    },
    {
        "page_number": 16,
        "page_title": "Final Review: Revenue Allocation Formula",
        "blocks": [
            {
                "block_type": "step_process",
                "component_type": "step_process",
                "title": "CRA Revenue Sharing Parameters",
                "content": {
                    "steps": [
                        "1. Population Size: Heavily populated counties receive higher allocations for service demand.",
                        "2. Land Area: Geographically vast counties receive extra funding for transport logistics.",
                        "3. Poverty Level: Poorer counties receive affirmative action allocations.",
                        "4. Fiscal Effort: Counties with high local revenue collection efficiency receive incentive bonuses."
                    ]
                }
            }
        ]
    }
]

LESSON_5_PAGES = [
    {
        "page_number": 1,
        "page_title": "Financial Accountability, Oversight, and PFM Institutions",
        "blocks": [
            {
                "block_type": "learning_goal",
                "component_type": "learning_goal",
                "title": "Lesson Objectives: Financial Oversight and Institutions",
                "content": {
                    "text": (
                        "By the end of this lesson, you will be able to:\n"
                        "- Explain public finance management controls at national and county levels (Appropriations, CS powers, PAC/PIC, PPRA, EACC)\n"
                        "- Describe the structure and six functions of the Commission on Revenue Allocation (CRA)\n"
                        "- Detail the roles of the Controller of Budget (COB), Auditor-General, and Central Bank of Kenya (CBK)\n"
                        "- Master comprehensive KCSE Paper 1 & 2 examination questions and marking schemes"
                    )
                }
            },
            {
                "block_type": "definition_card",
                "component_type": "definition_card",
                "title": "Concept: Financial Accountability",
                "content": {
                    "term": "Public Finance Oversight",
                    "definition": (
                        "The constitutional system of independent checks, balances, and auditing bodies established to ensure public officers "
                        "spend state revenues lawfully, transparently, and prudently for the maximum benefit of citizens."
                    )
                }
            }
        ]
    },
    {
        "page_number": 2,
        "page_title": "Central Bank of Kenya: Custodian of Monetary Policy",
        "blocks": [
            {
                "block_type": "suggested_image",
                "component_type": "suggested_image",
                "title": "Central Bank of Kenya",
                "content": {
                    "text": "The Central Bank of Kenya (CBK) building in Nairobi, the premier financial institution responsible for currency issuance, monetary policy, and banking supervision.",
                    "url": "https://upload.wikimedia.org/wikipedia/commons/1/14/Central_Bank_of_Kenya.jpg",
                    "author": "Public Domain / Wikimedia Commons",
                    "licensing": "Public Domain",
                    "commons_page_url": "https://commons.wikimedia.org/wiki/File:Central_Bank_of_Kenya.jpg"
                }
            }
        ]
    },
    {
        "page_number": 3,
        "page_title": "Educational Documentary: Financial Oversight & Debt Control",
        "blocks": [
            {
                "block_type": "suggested_video",
                "component_type": "suggested_video",
                "title": "Institutional Analysis: The Controller of Budget & Auditor-General in Public Finance",
                "content": {
                    "url": "https://www.youtube.com/watch?v=nTa362ovclA",
                    "text": "Examine the vital oversight roles played by the Controller of Budget, the Auditor-General, and Parliament in monitoring public expenditure and debt.",
                    "author": "Citizen TV Kenya / National News Analysis",
                    "licensing": "Standard YouTube License"
                }
            }
        ]
    },
    {
        "page_number": 4,
        "page_title": "Public Finance Controls at the National Level",
        "blocks": [
            {
                "block_type": "step_process",
                "component_type": "step_process",
                "title": "Seven National PFM Control Mechanisms",
                "content": {
                    "steps": [
                        "1. Parliamentary Appropriation: No funds can be withdrawn without explicit approval in an Appropriation Act passed by Parliament.",
                        "2. Personal Accountability of Accounting Officers: Principal Secretaries are personally and legally liable for financial management in their ministries.",
                        "3. CS Finance Fund Stoppage Powers: The CS can temporarily freeze funding to mismanaged state organs, subject to Parliamentary approval.",
                        "4. Parliamentary Oversight Committees: Public Accounts Committee (PAC) and Public Investments Committee (PIC) summon officers to answer audit queries.",
                        "5. Regulated Open Procurement: Public Procurement Regulatory Authority (PPRA) ensures transparent, competitive bidding for public tenders.",
                        "6. Anti-Corruption Investigations: Ethics and Anti-Corruption Commission (EACC) investigates embezzlement and prosecutes corrupt officials.",
                        "7. Independent Annual Audits: Auditor-General audits all public institutions and submits reports to Parliament within 6 months."
                    ]
                }
            }
        ]
    },
    {
        "page_number": 5,
        "page_title": "The Commission on Revenue Allocation (CRA)",
        "blocks": [
            {
                "block_type": "comparison_table",
                "component_type": "comparison_table",
                "title": "CRA: Structure and Six Mandated Functions",
                "content": {
                    "headers": ["Aspect", "Constitutional Details"],
                    "rows": [
                        ["Composition (9 Members)", "Chairperson appointed by President; nominees of regional/county bodies; 2 nominees of National Assembly; Principal Secretary for Finance; Controller of Budget."],
                        ["Function 1: Revenue Division", "Recommends the basis for equitable sharing of national revenue between National and County governments."],
                        ["Function 2: County Formula", "Determines the exact formula used to distribute the county allocation among the 47 County Governments."],
                        ["Function 3: Financial Management", "Makes recommendations to counties on prudent financial management and budget execution."],
                        ["Function 4: Revenue Enhancement", "Defines and works to expand the local revenue-raising capacity of county administrations."],
                        ["Function 5: Fiscal Responsibility", "Promotes transparency, economic optimization, and fiscal discipline in counties."],
                        ["Function 6: Marginalized Areas", "Determines and regularly reviews the criteria used to identify marginalized areas for the Equalization Fund."]
                    ]
                }
            }
        ]
    },
    {
        "page_number": 6,
        "page_title": "Controller of Budget vs. Auditor-General",
        "blocks": [
            {
                "block_type": "comparison_table",
                "component_type": "comparison_table",
                "title": "Comparison: Controller of Budget vs. Auditor-General",
                "content": {
                    "headers": ["Feature", "Controller of Budget (COB)", "Auditor-General"],
                    "rows": [
                        ["Timing of Intervention", "Ex-Ante (Before expenditure occurs) — The Gatekeeper.", "Ex-Post (After expenditure has occurred) — The Auditor."],
                        ["Core Function", "Authorizes withdrawals of money from the Consolidated Fund, Equalization Fund, and County Revenue Funds only if backed by law.", "Audits all accounts of national ministries, judiciary, parliament, and county governments to verify lawful and prudent spending."],
                        ["Reporting Mandate", "Submits a budget implementation report to Parliament every four (4) months.", "Submits an annual audit report to Parliament or relevant County Assembly within six (6) months of fiscal year-end."]
                    ]
                }
            }
        ]
    },
    {
        "page_number": 7,
        "page_title": "The Central Bank of Kenya (CBK)",
        "blocks": [
            {
                "block_type": "step_process",
                "component_type": "step_process",
                "title": "Five Core Functions of the Central Bank of Kenya",
                "content": {
                    "steps": [
                        "1. Currency Stability: Promotes and maintains the internal and external value stability of the Kenyan Shilling.",
                        "2. Note and Coin Issuance: Sole constitutional authority permitted to design, print, and issue national currency notes and coins.",
                        "3. Banker to Government: Acts as the official banker, fiscal custodian, and financial advisor to the National Government.",
                        "4. Monetary Policy Formulation: Regulates money supply, interest rates, and inflation to support sustainable economic growth.",
                        "5. Commercial Bank Supervision: Licenses, regulates, and inspects commercial banks, microfinance institutions, and forex bureaus."
                    ]
                }
            }
        ]
    },
    {
        "page_number": 8,
        "page_title": "The Economic and Social Council",
        "blocks": [
            {
                "block_type": "step_process",
                "component_type": "step_process",
                "title": "Four Functions of the Economic and Social Council",
                "content": {
                    "steps": [
                        "1. Policy Advisory: Advises the national government and Parliament on strategic economic and social policies.",
                        "2. Strategic Evaluation: Evaluates the implementation and success of major national development plans (Vision 2030).",
                        "3. Legislative Review: Assesses and reports to Parliament on the socio-economic implications of all draft Bills and budget proposals.",
                        "4. Monitoring Living Standards: Tracks government programs aimed at improving the welfare of poor and marginalized citizens."
                    ]
                }
            }
        ]
    },
    {
        "page_number": 9,
        "page_title": "Interactive Classification: Institutions and Offices",
        "blocks": [
            {
                "block_type": "mini_activity",
                "component_type": "mini_activity",
                "title": "Match the Public Finance Body to Its Role",
                "content": {
                    "instruction": "Identify the office or institution described:",
                    "items": [
                        "1. Determines the formula for sharing revenue among 47 counties -> **Commission on Revenue Allocation (CRA)**",
                        "2. Financial gatekeeper authorizing all withdrawals before money is spent -> **Controller of Budget (COB)**",
                        "3. Independent office auditing public accounts after funds are spent -> **Auditor-General**",
                        "4. Premier institution that prints currency and conducts monetary policy -> **Central Bank of Kenya (CBK)**",
                        "5. Parliamentary committee reviewing audit queries on parastatals -> **Public Investments Committee (PIC)**"
                    ]
                }
            }
        ]
    },
    {
        "page_number": 10,
        "page_title": "Master KCSE Examination Paper 1 (Section C, 10 Marks)",
        "blocks": [
            {
                "block_type": "worked_example",
                "component_type": "worked_example",
                "title": "KCSE Question 1: Functions of the Commission on Revenue Allocation (10 Marks)",
                "content": {
                    "text": (
                        "**Model Answer (Point + Explanation = 2 Marks per Point):**\n\n"
                        "1. **Recommends on Equitable Sharing of Revenue:** Determines the basis for sharing revenue collected nationally between the national government and the 47 county governments. (2 marks)\n\n"
                        "2. **Recommends Sharing Formula Among Counties:** Designs and reviews the formula used to share the county revenue allocation fairly among all 47 counties. (2 marks)\n\n"
                        "3. **Recommends on County Financial Management:** Advises county assemblies and executives on prudent public financial management. (2 marks)\n\n"
                        "4. **Defines and Enhances County Revenue Sources:** Identifies mechanisms to expand local own-source revenue collection in counties. (2 marks)\n\n"
                        "5. **Identifies Marginalized Areas for Affirmative Action:** Determines and reviews criteria used to identify marginalized areas eligible for the Equalization Fund. (2 marks)"
                    )
                }
            }
        ]
    },
    {
        "page_number": 11,
        "page_title": "Master KCSE Examination Paper 2 (Section C, 12 Marks)",
        "blocks": [
            {
                "block_type": "worked_example",
                "component_type": "worked_example",
                "title": "KCSE Question 2: Measures to Control Mismanagement of Public Funds (12 Marks)",
                "content": {
                    "text": (
                        "**Model Answer (Point + Explanation = 2 Marks per Point):**\n\n"
                        "1. **Strict Parliamentary Approval:** No public money can be withdrawn from national funds without an Appropriation Act passed by Parliament. (2 marks)\n\n"
                        "2. **The Gatekeeper Role of the Controller of Budget:** The COB authorizes all withdrawals, confirming they are lawful and within budget before funds are released. (2 marks)\n\n"
                        "3. **Personal Accountability of Accounting Officers:** Principal Secretaries are personally and legally liable to Parliament for financial management in their ministries. (2 marks)\n\n"
                        "4. **Annual Audits by the Auditor-General:** The Auditor-General audits all public bodies annually, exposing financial waste and submitting reports to Parliament. (2 marks)\n\n"
                        "5. **Scrutiny by Parliamentary Oversight Committees:** The PAC and PIC review audit reports and summon negligent public officers for questioning. (2 marks)\n\n"
                        "6. **Power of CS Finance to Freeze Funds:** The CS for Finance has statutory authority to temporarily stop fund transfers to mismanaged public entities. (2 marks)"
                    )
                }
            }
        ]
    },
    {
        "page_number": 12,
        "page_title": "Topic 8 Comprehensive Mastery Check (Part 1)",
        "blocks": [
            {
                "block_type": "knowledge_check",
                "component_type": "knowledge_check",
                "title": "Topic 8 Mastery Assessment (Part 1)",
                "content": {
                    "questions": [
                        {
                            "question": "How often must the Controller of Budget submit a budget implementation report to Parliament?",
                            "options": [
                                "Every month",
                                "Every four (4) months",
                                "Every six (6) months",
                                "Once every two years"
                            ],
                            "correct_answer": 1,
                            "explanation": "Under Article 228(6), the Controller of Budget submits reports to Parliament every four months."
                        },
                        {
                            "question": "Within what deadline must the Auditor-General submit an annual audit report to Parliament after the end of the financial year?",
                            "options": [
                                "Within 3 months",
                                "Within 6 months",
                                "Within 12 months",
                                "Within 2 years"
                            ],
                            "correct_answer": 1,
                            "explanation": "Under Article 229(7), the Auditor-General must submit audit reports to Parliament within 6 months."
                        }
                    ]
                }
            }
        ]
    },
    {
        "page_number": 13,
        "page_title": "Topic 8 Comprehensive Mastery Check (Part 2)",
        "blocks": [
            {
                "block_type": "knowledge_check",
                "component_type": "knowledge_check",
                "title": "Topic 8 Mastery Assessment (Part 2)",
                "content": {
                    "questions": [
                        {
                            "question": "Which of the following is NOT a function of the Central Bank of Kenya (CBK)?",
                            "options": [
                                "Formulating and implementing monetary policy",
                                "Passing the annual Appropriation Bill",
                                "Issuing national currency notes and coins",
                                "Acting as banker and financial advisor to the National Government"
                            ],
                            "correct_answer": 1,
                            "explanation": "Passing the Appropriation Bill is the legislative function of the National Assembly, not the CBK."
                        },
                        {
                            "question": "Who serves as the accounting officer in a national government ministry, personally accountable to Parliament for finances?",
                            "options": [
                                "The Cabinet Secretary",
                                "The Principal Secretary",
                                "The Governor of Central Bank",
                                "The Speaker of the National Assembly"
                            ],
                            "correct_answer": 1,
                            "explanation": "The Principal Secretary serves as the accounting officer in each state department."
                        }
                    ]
                }
            }
        ]
    },
    {
        "page_number": 14,
        "page_title": "Topic 8 Comprehensive Master Summary",
        "blocks": [
            {
                "block_type": "summary",
                "component_type": "summary",
                "title": "Topic 8 Master Summary: Public Revenue and Expenditure",
                "content": {
                    "text": (
                        "• **Constitutional Principles (Article 201):** Openness/public participation, fair taxation, revenue devolution, affirmative action, prudent spending, intergenerational equity, fiscal reporting.\n"
                        "• **National Budget (1 July–30 June):** Sourcing revenue, allocating spending, investor confidence; enacted via the Appropriation Act.\n"
                        "• **Revenue Sources:** Direct taxes (PAYE, Corporation Tax), Indirect taxes (VAT, Customs, Excise), Non-tax fees, Bilateral/Multilateral aid, County own-sources.\n"
                        "• **Public Funds:** Consolidated Fund, Equalization Fund (0.5%), Contingencies Fund, County Revenue Funds; Article 203 sharing criteria.\n"
                        "• **PFM Oversight:** CRA (formula & equalization criteria), Controller of Budget (ex-ante gatekeeper), Auditor-General (ex-post audits), Central Bank of Kenya (monetary policy & currency)."
                    )
                }
            }
        ]
    },
    {
        "page_number": 15,
        "page_title": "Topic 8 Final Exam Revision Checklist",
        "blocks": [
            {
                "block_type": "step_process",
                "component_type": "step_process",
                "title": "Exam Revision Checklist: Topic 8",
                "content": {
                    "steps": [
                        "1. Seven constitutional principles under Article 201.",
                        "2. Seven reasons why the national budget is important.",
                        "3. Six stages of the national budget preparation cycle.",
                        "4. Direct vs. Indirect taxes and domestic vs. external revenue.",
                        "5. Four constitutional funds and eleven Article 203 sharing criteria.",
                        "6. Institutional roles: CRA, Controller of Budget, Auditor-General, Central Bank of Kenya."
                    ]
                }
            }
        ]
    },
    {
        "page_number": 16,
        "page_title": "Exam Coaching: Mastering Public Finance Questions",
        "blocks": [
            {
                "block_type": "callout",
                "component_type": "callout",
                "title": "Top Tips for KCSE History Public Finance Essays",
                "content": {
                    "text": (
                        "**Examiner's Guidelines:**\n"
                        "- **Distinguish Roles Clearly:** Do not confuse the **Controller of Budget** (approves withdrawals *before* spending) with the **Auditor-General** (audits accounts *after* spending).\n"
                        "- **Cite Exact Constitutional Funds:** Always name the *Consolidated Fund*, *Equalization Fund*, *Contingencies Fund*, and *County Revenue Fund*.\n"
                        "- **Use Full Point-Explanation Structure:** State the mechanism + explain the economic purpose + provide standard KCSE examples."
                    )
                }
            }
        ]
    },
    {
        "page_number": 17,
        "page_title": "Grand Summary: Topics 1–8 Review",
        "blocks": [
            {
                "block_type": "summary",
                "component_type": "summary",
                "title": "Comprehensive Synthesis: Form 4 History (Topics 1 to 8)",
                "content": {
                    "text": (
                        "• **Topic 1 (The World War):** WWI & WWII origins, course, Allied victory, League of Nations & UN founding.\n"
                        "• **Topic 2 (International Relations):** UN, Commonwealth, NAM, Cold War superpowers & collapse.\n"
                        "• **Topic 3 (Co-operation in Africa):** Pan-Africanism, OAU founding 1963, African Union 2002, EAC, ECOWAS, COMESA.\n"
                        "• **Topic 4 (National Philosophies):** African Socialism (Sessional Paper 10), Harambee, Nyayoism.\n"
                        "• **Topic 5 (Developments in Kenya):** Centralization (1964–1982), multipartyism (1991), 2010 Constitution.\n"
                        "• **Topic 6 (Developments in Africa):** Inherited crises, DRC Congo Crisis & Mobutu, Tanzania Ujamaa & Kiswahili.\n"
                        "• **Topic 7 (Devolved Government):** Colonial local government, Cap 265 councils, 2010 Devolution revolution, 47 Counties.\n"
                        "• **Topic 8 (Public Revenue and Expenditure):** Article 201 principles, National Budget, taxation, constitutional funds, CRA, COB, Auditor-General, CBK."
                    )
                }
            }
        ]
    },
    {
        "page_number": 18,
        "page_title": "KCSE Examination Final Tip Sheet: Public Finance",
        "blocks": [
            {
                "block_type": "step_process",
                "component_type": "step_process",
                "title": "Top Examination Tips for Topic 8",
                "content": {
                    "steps": [
                        "1. Clearly memorize the dates of the Kenyan financial year (1st July to 30th June).",
                        "2. In questions on the Equalization Fund, always mention the 0.5% allocation and the 4 basic services: water, roads, health, electricity.",
                        "3. In questions on the National Budget, explain how it guides investors, sources revenue, and prevents unauthorized expenditure.",
                        "4. Remember the difference between Direct Taxes (PAYE, Corporation Tax) and Indirect Taxes (VAT, Customs, Excise).",
                        "5. Distinguish between ex-ante oversight (Controller of Budget) and ex-post oversight (Auditor-General)."
                    ]
                }
            }
        ]
    }
]


ALL_LESSONS = [
    {
        "unit_order": 1,
        "unit_name": "Foundations of Public Finance and Principles of the Financial System",
        "lesson_title": "Foundations of Public Finance: Meaning, Historical Evolution, and Constitutional Principles (Article 201)",
        "pages": LESSON_1_PAGES
    },
    {
        "unit_order": 2,
        "unit_name": "The National Budget — Meaning, Importance, and Process of Preparation",
        "lesson_title": "The National Budget: Meaning, Strategic Importance, and Step-by-Step Preparation Cycle",
        "pages": LESSON_2_PAGES
    },
    {
        "unit_order": 3,
        "unit_name": "Sources of Public Revenue (National and County Governments)",
        "lesson_title": "Sources of Public Revenue: Direct and Indirect Taxes, Non-Tax Revenues, External Aid, and County Finances",
        "pages": LESSON_3_PAGES
    },
    {
        "unit_order": 4,
        "unit_name": "National Public Funds, Equitable Allocation, and Expenditure",
        "lesson_title": "National Public Funds, Equitable Sharing Criteria (Article 203), and Expenditure Classification",
        "pages": LESSON_4_PAGES
    },
    {
        "unit_order": 5,
        "unit_name": "Financial Accountability, Oversight, and PFM Institutions",
        "lesson_title": "Public Finance Management: Oversight Controls, Key Institutions (CRA, COB, Auditor-General, CBK), and Synthesis",
        "pages": LESSON_5_PAGES
    }
]


# ===========================================================================
# DATABASE INGESTION RUNNER
# ===========================================================================

def run_ingestion(replace=False):
    print("=" * 80)
    print("VLEARN CURRICULUM INGESTION: FORM 4 HISTORY — TOPIC 8 (PUBLIC REVENUE AND EXPENDITURE)")
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
            name="Public Revenue and Expenditure in Kenya",
            defaults={"order": 8}
        )
        if topic_created:
            print(f"[+] Created Topic: {topic.name} (Order: {topic.order})")
        else:
            topic.order = 8
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
        print(f"[SUCCESS] Form 4 History Topic 8 Ingestion Complete!")
        print(f"[*] Total Lessons Ingested: {len(ALL_LESSONS)}")
        print(f"[*] Total Pages Ingested:   {total_pages}")
        print(f"[*] Total Blocks Ingested:  {total_blocks}")
        print(f"[*] Total Media Assets:     {total_assets}")
        print("=" * 80)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Ingest Form 4 History Topic 8")
    parser.add_argument("--replace", action="store_true", help="Replace existing blocks with a fresh rebuild")
    args = parser.parse_args()

    run_ingestion(replace=args.replace)
