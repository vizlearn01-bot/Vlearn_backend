"""
VLearn Curriculum Ingestion Engine: Form 4 History — Topic 2 (International Relations)

Target Subject: History (Subject ID: 17)
Grade: Form 4 (Grade ID: 4)
Curriculum: 844 (Curriculum ID: 4)

Topic 2: International Relations (Order: 2)
  - Unit 1: International Relations — Meaning, Benefits, and Forms (Lesson 1: 14 Pages)
  - Unit 2: International Organizations — IGOs and NGOs (Lesson 2: 14 Pages)
  - Unit 3: The League of Nations — Origins, Organs, Achievements, and Collapse (Lesson 3: 16 Pages)
  - Unit 4: The United Nations Organization (UN) — Structure, Impact, and Challenges (Lesson 4: 18 Pages)
  - Unit 5: The Commonwealth of Nations — Evolution, Organs, and Impact (Lesson 5: 15 Pages)
  - Unit 6: The Non-Aligned Movement (NAM) — Active Neutrality and Global Role (Lesson 6: 16 Pages)
  - Unit 7: The Cold War — Superpower Rivalry, Proxy Theatres, and Impact on Africa (Lesson 7: 18 Pages)

Total: 7 Learning Units, 7 Lessons, 111 Pages, 165+ Blocks, 17 Media Assets (13 Wikimedia Photos + 4 Documentary Videos)

Usage:
  ./venv/bin/python curriculum/ingest_form4_history_topic2.py --replace
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
# LESSON DEFINITIONS: FORM 4 HISTORY TOPIC 2
# ===========================================================================

LESSON_1_PAGES = [
    {
        "page_number": 1,
        "page_title": "Introduction to International Relations",
        "blocks": [
            {
                "block_type": "learning_goal",
                "component_type": "learning_goal",
                "title": "Lesson Objectives: Understanding International Relations",
                "content": {
                    "text": (
                        "By the end of this lesson, you will be able to:\n"
                        "- Define international relations and analyze the formal framework of interstate engagement\n"
                        "- Distinguish between the four major examinable forms of international relations\n"
                        "- Explain the five vital benefits nations derive from global cooperation\n"
                        "- Apply the Point-Explanation-Evidence structure to KCSE evaluation questions on Kenya's foreign relations"
                    )
                }
            },
            {
                "block_type": "suggested_image",
                "component_type": "suggested_image",
                "title": "Bilateral Diplomatic Credentials Ceremony",
                "content": {
                    "text": "A newly appointed High Commissioner presents diplomatic credentials, illustrating the formal, sovereign framework of bilateral international relations.",
                    "url": "https://upload.wikimedia.org/wikipedia/commons/3/34/Commonwealth_Heads_of_Government_Meeting_-_2018_%2826690677697%29.jpg",
                    "author": "Commonwealth Secretariat / CC BY 2.0",
                    "licensing": "CC BY 2.0",
                    "commons_page_url": "https://commons.wikimedia.org/wiki/File:Commonwealth_Heads_of_Government_Meeting_-_2018_(26690677697).jpg"
                }
            },
            {
                "block_type": "definition_card",
                "component_type": "definition_card",
                "title": "Definition: International Relations",
                "content": {
                    "term": "International Relations",
                    "definition": (
                        "The cooperation, communication, and multifaceted interactions between individual citizens, special interest groups, "
                        "and sovereign nations across the globe. It provides a formal diplomatic and legal framework through which states manage shared resources, "
                        "resolve political disputes, and pursue mutual economic and social development."
                    )
                }
            }
        ]
    },
    {
        "page_number": 2,
        "page_title": "The Four Examinable Forms of International Relations",
        "blocks": [
            {
                "block_type": "concept_explanation",
                "component_type": "concept_explanation",
                "title": "How Nations Interact: Categorizing Interstate Cooperation",
                "content": {
                    "text": (
                        "In modern history and under the KCSE syllabus, international cooperation is classified into four distinct, examinable forms:\n\n"
                        "1. **Economic Relations:** Involves trade, commercial exchanges, international banking, currency regulations, and developmental assistance.\n"
                        "2. **Diplomatic Relations:** The peaceful, formal political communication channels established between sovereign states through permanent foreign embassies and high commissions.\n"
                        "3. **Political Relations:** Strategic alliances, treaties, and ideological cooperation between countries sharing similar governance systems or collective defense priorities.\n"
                        "4. **Socio-Cultural Relations:** Cross-border interactions based on shared human experiences, academic research, educational exchanges, artistic performances, and international sporting tournaments."
                    )
                }
            },
            {
                "block_type": "comparison_table",
                "component_type": "comparison_table",
                "title": "Classification of International Relations Forms",
                "content": {
                    "headers": ["Form of Relation", "Primary Mechanism", "Key Historical Example", "Strategic Purpose"],
                    "rows": [
                        ["Economic Relations", "Bilateral & multilateral trade treaties, development loans, tariff agreements", "World Bank & IMF infrastructure loans to developing states", "Accelerate national economic growth and access overseas consumer markets."],
                        ["Diplomatic Relations", "Permanent embassies, consulates, exchange of Ambassadors and High Commissioners", "Kenya maintaining a High Commission in London and an Embassy in Washington", "Protect national citizens abroad and maintain continuous lines of peaceful dialogue."],
                        ["Political Relations", "Bilateral treaties, joint governance pacts, regional political blocs", "The 1964 political union of Tanganyika and Zanzibar forming Tanzania", "Advance shared ideological interests and coordinate foreign policy positions."],
                        ["Socio-Cultural Relations", "Sporting events, academic scholarships, cultural dance troupes, scientific research", "Global participation in the Olympic Games and Commonwealth Games", "Foster mutual tolerance, break down ethnic prejudices, and build global solidarity."]
                    ]
                }
            }
        ]
    },
    {
        "page_number": 3,
        "page_title": "Diplomatic Terminology: Ambassadors vs. High Commissioners",
        "blocks": [
            {
                "block_type": "callout",
                "component_type": "callout",
                "title": "KCSE Examination Distinction: Ambassadors vs. High Commissioners",
                "content": {
                    "text": (
                        "A critical distinction frequently tested in KCSE exams:\n\n"
                        "- **Ambassador:** The principal diplomatic representative sent by a republic or non-Commonwealth sovereign nation to reside in a foreign capital (e.g., US Ambassador to Kenya).\n"
                        "- **High Commissioner:** The principal diplomatic representative exchanged between two member states of the Commonwealth of Nations (e.g., Kenya's High Commissioner to the United Kingdom).\n\n"
                        "**Status:** High Commissioners and Ambassadors hold identical diplomatic rank, immunities, and executive responsibilities."
                    )
                }
            }
        ]
    },
    {
        "page_number": 4,
        "page_title": "Benefit 1: Enhancement of Global Peace and Security",
        "blocks": [
            {
                "block_type": "concept_explanation",
                "component_type": "concept_explanation",
                "title": "Preventing War Through Structured Diplomacy",
                "content": {
                    "text": (
                        "The primary objective of international relations is the preservation of world peace and stability.\n\n"
                        "- Regular diplomatic communication enables sovereign nations to arbitrate territorial and political disputes through peaceful mediation rather than catastrophic military conflict.\n"
                        "- International tribunals, such as the International Court of Justice (ICJ), provide legal arbitration for contested borders.\n\n"
                        "**Historical Evidence:** The peaceful resolution of the volatile Bakassi Peninsula border dispute between Nigeria and Cameroon in 2004 following an ICJ ruling, averting a major regional war in West Africa."
                    )
                }
            }
        ]
    },
    {
        "page_number": 5,
        "page_title": "Benefit 2: Collective Solutions to Global Challenges",
        "blocks": [
            {
                "block_type": "concept_explanation",
                "component_type": "concept_explanation",
                "title": "Addressing Transnational Environmental and Scientific Crises",
                "content": {
                    "text": (
                        "Many modern existential threats transcend national sovereign borders and cannot be solved by any single country acting in isolation.\n\n"
                        "- **Global Environmental Crises:** Climate change, desertification, global warming, ocean acidification, and air pollution require binding global emissions treaties.\n"
                        "- **Global Epidemics & Pandemics:** Combating transnational diseases (e.g., COVID-19, Ebola, Polio) requires coordinated vaccine distribution and surveillance led by the World Health Organization (WHO).\n\n"
                        "**Historical Evidence:** The Montreal Protocol of 1987, which successfully united 197 nations to phase out ozone-depleting chlorofluorocarbons (CFCs)."
                    )
                }
            }
        ]
    },
    {
        "page_number": 6,
        "page_title": "Benefit 3: Promotion of Economic Growth through Trade",
        "blocks": [
            {
                "block_type": "concept_explanation",
                "component_type": "concept_explanation",
                "title": "Market Expansion and Resource Exchange",
                "content": {
                    "text": (
                        "No single nation on earth possesses all natural resources or industrial capacities required for self-sufficiency.\n\n"
                        "- International economic relations allow nations to specialize in goods where they hold a comparative advantage and trade for items they lack.\n"
                        "- Developing countries gain access to vast consumer markets in Europe, Asia, and North America, earning vital foreign exchange reserves.\n\n"
                        "**Historical Evidence:** Kenya exporting high-value horticultural flowers, tea, and coffee to the European Union while importing refined petroleum, heavy industrial machinery, and electronics."
                    )
                }
            }
        ]
    },
    {
        "page_number": 7,
        "page_title": "Benefit 4: Financial and Technical Assistance",
        "blocks": [
            {
                "block_type": "concept_explanation",
                "component_type": "concept_explanation",
                "title": "Financing Infrastructure and Human Capital Development",
                "content": {
                    "text": (
                        "Developing nations leverage international partnerships to bridge domestic capital and technical knowledge gaps:\n\n"
                        "- **Development Loans & Grants:** Wealthier nations and international financial institutions (World Bank, African Development Bank) provide concessionary loans for mega-infrastructure projects (highways, railways, hydroelectric dams, ports).\n"
                        "- **Transfer of Technical Expertise:** Developing states receive foreign agronomists, civil engineers, medical specialists, and advanced technologies to modernize domestic sectors.\n\n"
                        "**Historical Evidence:** Bilateral technical assistance funding the construction of major infrastructure across East Africa, such as modern bypass networks and geothermal energy plants."
                    )
                }
            }
        ]
    },
    {
        "page_number": 8,
        "page_title": "Benefit 5: Socio-Cultural Integration and Understanding",
        "blocks": [
            {
                "block_type": "concept_explanation",
                "component_type": "concept_explanation",
                "title": "Fostering International Solidarity and Tolerance",
                "content": {
                    "text": (
                        "Interstate cooperation extends deeply into cultural and human interactions:\n\n"
                        "- **Cultural Exchange:** Touring art exhibitions, traditional music groups, and academic exchange programs promote mutual respect and dismantle xenophobic stereotypes.\n"
                        "- **Sporting Tournaments:** Major competitions like the Olympic Games, FIFA World Cup, and Commonwealth Games unite athletes and spectators from diverse ethnic and racial backgrounds in friendly competition.\n\n"
                        "**Historical Evidence:** Kenyan middle- and long-distance runners competing globally, creating national pride and serving as goodwill ambassadors."
                    )
                }
            }
        ]
    },
    {
        "page_number": 9,
        "page_title": "Summary of Examinable Benefits (Point-Form Revision)",
        "blocks": [
            {
                "block_type": "step_process",
                "component_type": "step_process",
                "title": "The 5 Core Pillars of International Cooperation",
                "content": {
                    "steps": [
                        "1. Enhancement of Peace & Security: Resolving border and political disputes through diplomatic arbitration to prevent armed conflict.",
                        "2. Collective Problem Solving: Tackling global crises (climate change, pandemics, desertification) requiring unified international action.",
                        "3. Economic Growth Through Trade: Expanding export markets for agricultural products and importing essential industrial capital goods.",
                        "4. Financial & Technical Assistance: Securing bilateral loans, grants, and technical experts to fund major domestic infrastructure.",
                        "5. Socio-Cultural Integration: Promoting international understanding, tolerance, and friendship through global sports and cultural exchanges."
                    ]
                }
            }
        ]
    },
    {
        "page_number": 10,
        "page_title": "Case Study: Kenya's Strategic International Relations",
        "blocks": [
            {
                "block_type": "concept_explanation",
                "component_type": "concept_explanation",
                "title": "How Kenya Leverages Multilateral Diplomacy",
                "content": {
                    "text": (
                        "Since gaining independence on 12 December 1963, Kenya has pursued an active foreign policy anchored on non-alignment, peaceful coexistence, and good neighborliness:\n\n"
                        "- **Host to Global Agencies:** Kenya hosts the global headquarters of the United Nations Environment Programme (UNEP) and UN-Habitat in Gigiri, Nairobi—the only UN headquarters in the Global South.\n"
                        "- **Regional Peacekeeping:** Kenya has deployed defense forces under UN and AU peacekeeping mandates to Namibia, Sierra Leone, Liberia, South Sudan, and Somalia.\n"
                        "- **Regional Economic Integration:** Active leadership in the East African Community (EAC) and COMESA to expand duty-free trade for Kenyan manufacturers."
                    )
                }
            }
        ]
    },
    {
        "page_number": 11,
        "page_title": "Interactive Classification Activity",
        "blocks": [
            {
                "block_type": "mini_activity",
                "component_type": "mini_activity",
                "title": "Classify the Form of International Relation",
                "content": {
                    "instruction": "Test your historical classification skills. Assign each scenario to its correct category (Economic, Diplomatic, Political, or Socio-Cultural):",
                    "items": [
                        "1. Kenya exchanging High Commissioners with Canada -> **Diplomatic Relations**",
                        "2. The World Bank granting a loan for geothermal drilling in Olkaria -> **Economic Relations**",
                        "3. Kenyan athletes participating in the Olympic Games -> **Socio-Cultural Relations**",
                        "4. Tanzania and Kenya coordinating border security anti-smuggling patrols -> **Political / Security Relations**",
                        "5. The European Union lowering tariffs on Kenyan tea and cut flowers -> **Economic Relations**",
                        "6. A cultural dance troupe performing at an international arts festival in Japan -> **Socio-Cultural Relations**"
                    ]
                }
            }
        ]
    },
    {
        "page_number": 12,
        "page_title": "KCSE Examination Coaching: Structuring Full-Mark Responses",
        "blocks": [
            {
                "block_type": "worked_example",
                "component_type": "worked_example",
                "title": "KCSE Question: Explain Five Benefits that Kenya Derives from Participating in International Relations (10 Marks)",
                "content": {
                    "text": (
                        "**Examiner's Marking Scheme (Point + Explanation + Evidence = 2 Marks per Point):**\n\n"
                        "1. **Promotion of Trade and Economic Growth:** Enables Kenya to access overseas markets in Europe, Asia, and America for agricultural exports like tea, coffee, and horticulture, earning vital foreign exchange. (2 marks)\n\n"
                        "2. **Acquisition of Financial and Technical Aid:** Allows Kenya to secure developmental loans, budgetary grants, and technical experts from international bodies like the World Bank and IMF to finance infrastructure like roads and dams. (2 marks)\n\n"
                        "3. **Enhancement of National and Regional Security:** Provides access to collective defense arrangements, joint intelligence sharing, and UN/AU security frameworks to combat regional terrorism and piracy. (2 marks)\n\n"
                        "4. **Transfer of Science and Technology:** Facilitates the exchange of advanced agricultural techniques, medical research, and renewable energy technologies to modernize local industries. (2 marks)\n\n"
                        "5. **Promotion of Cultural and Sporting Ties:** Fosters national prestige and international goodwill through participation in the Commonwealth Games and global cultural festivals. (2 marks)"
                    )
                }
            }
        ]
    },
    {
        "page_number": 13,
        "page_title": "Check Your Understanding: Module 2.1",
        "blocks": [
            {
                "block_type": "knowledge_check",
                "component_type": "knowledge_check",
                "title": "Module 2.1 Mastery Assessment",
                "content": {
                    "questions": [
                        {
                            "question": "What is the official title given to a senior diplomatic envoy exchanged between two Commonwealth member nations?",
                            "options": [
                                "Ambassador Extraordinary",
                                "High Commissioner",
                                "Consul General",
                                "Chargé d'Affaires"
                            ],
                            "correct_answer": 1,
                            "explanation": "High Commissioner is the unique diplomatic title used exclusively between sovereign Commonwealth nations, reflecting their shared historical partnership."
                        },
                        {
                            "question": "Which of the following is an example of a socio-cultural form of international relations?",
                            "options": [
                                "Signing a double taxation avoidance treaty",
                                "Exporting horticultural flowers to the Netherlands",
                                "Participating in the quadrennial Commonwealth Games",
                                "Deploying naval warships on anti-piracy patrols"
                            ],
                            "correct_answer": 2,
                            "explanation": "Participation in international sporting competitions like the Commonwealth Games or Olympic Games is a direct form of socio-cultural interaction."
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
                "title": "Core Summary: International Relations Fundamentals",
                "content": {
                    "text": (
                        "• **Definition:** International relations provide the formal framework for peaceful diplomatic, economic, political, and socio-cultural interactions between sovereign states.\n"
                        "• **Four Forms:** Economic (trade/aid), Diplomatic (embassies/high commissions), Political (alliances/unions), and Socio-Cultural (sports/culture/education).\n"
                        "• **Five Core Benefits:** Peaceful dispute settlement, collective response to global crises, expanded trade markets, financial/technical aid, and cross-cultural tolerance.\n"
                        "• **KCSE Exam Rule:** Always structure essay answers with explicit Point + Explanation + Kenyan/Historical Example to achieve full 10/10 marks."
                    )
                }
            },
            {
                "block_type": "key_takeaway",
                "component_type": "key_takeaway",
                "title": "Key Takeaways",
                "content": {
                    "text": (
                        "- In the modern globalized world, no nation can survive in isolation.\n"
                        "- International relations balance national sovereignty with collective global problem-solving."
                    )
                }
            }
        ]
    }
]

LESSON_2_PAGES = [
    {
        "page_number": 1,
        "page_title": "Introduction to International Organizations",
        "blocks": [
            {
                "block_type": "learning_goal",
                "component_type": "learning_goal",
                "title": "Lesson Objectives: IGOs and NGOs",
                "content": {
                    "text": (
                        "By the end of this lesson, you will be able to:\n"
                        "- Define international organizations and understand why sovereign nations establish multilateral bodies\n"
                        "- Distinguish between International Governmental Organizations (IGOs) and Non-Governmental Organizations (NGOs)\n"
                        "- Analyze the five core roles performed by IGOs in regulating global affairs\n"
                        "- Evaluate the humanitarian and advocacy functions of international NGOs"
                    )
                }
            },
            {
                "block_type": "definition_card",
                "component_type": "definition_card",
                "title": "Definition: International Organization",
                "content": {
                    "term": "International Organization",
                    "definition": (
                        "An institutional body with global or regional scope, established either by sovereign states (IGOs) through formal treaties "
                        "or by private individuals and associations (NGOs) to coordinate collective action, resolve cross-border problems, and manage international affairs."
                    )
                }
            }
        ]
    },
    {
        "page_number": 2,
        "page_title": "Classification: IGOs vs. NGOs",
        "blocks": [
            {
                "block_type": "concept_explanation",
                "component_type": "concept_explanation",
                "title": "Two Distinct Categories of Global Bodies",
                "content": {
                    "text": (
                        "To manage complex transnational challenges, international bodies are classified into two major categories depending on their legal basis and founding membership:\n\n"
                        "1. **International Governmental Organizations (IGOs):** Formed strictly by two or more sovereign national governments through binding international treaties or charters (e.g., United Nations, African Union, Commonwealth, Non-Aligned Movement).\n\n"
                        "2. **International Non-Governmental Organizations (NGOs):** Founded by private individuals, philanthropic trusts, or civil society associations operating independently of government control (e.g., International Committee of the Red Cross, Amnesty International, Transparency International, Greenpeace)."
                    )
                }
            }
        ]
    },
    {
        "page_number": 3,
        "page_title": "Comparative Analysis: IGOs vs. NGOs",
        "blocks": [
            {
                "block_type": "comparison_table",
                "component_type": "comparison_table",
                "title": "Detailed Comparison: IGOs vs. NGOs",
                "content": {
                    "headers": ["Feature", "International Governmental Organizations (IGOs)", "International Non-Governmental Organizations (NGOs)"],
                    "rows": [
                        ["Founders", "Two or more sovereign state governments.", "Private citizens, philanthropists, or civil society groups."],
                        ["Legal Foundation", "Formal multilateral treaties or charters signed and ratified by sovereign parliaments.", "Registered under civil laws and non-profit statutes of individual host countries."],
                        ["Primary Examples", "United Nations (UN), African Union (AU), Commonwealth, Non-Aligned Movement (NAM).", "International Red Cross, Amnesty International, Transparency International, Oxfam."],
                        ["Funding Sources", "Mandatory or assessed annual financial contributions from member state national treasuries.", "Private donations, public fundraising, philanthropic grants, and charitable bequests."],
                        ["Political Authority", "Hold sovereign and legal authority; can issue binding resolutions and deploy armed peacekeepers.", "Possess no state authority; rely on public advocacy, independent reporting, and moral pressure."]
                    ]
                }
            }
        ]
    },
    {
        "page_number": 4,
        "page_title": "Funding and Operational Autonomy",
        "blocks": [
            {
                "block_type": "concept_explanation",
                "component_type": "concept_explanation",
                "title": "How Governance and Funding Dictate Global Action",
                "content": {
                    "text": (
                        "The operational effectiveness of international bodies depends directly on their funding and independence:\n\n"
                        "- **IGOs:** Vulnerable to political pressure from major contributing nations (e.g., superpowers withholding dues to influence policy). However, they carry legal legitimacy under international law.\n"
                        "- **NGOs:** Enjoy independence from government foreign policy agendas, allowing them to neutrally report on human rights abuses, governmental corruption, and environmental violations without fear of political retaliation."
                    )
                }
            }
        ]
    },
    {
        "page_number": 5,
        "page_title": "Role 1 of IGOs: Provision of Neutral Forums for Consultation",
        "blocks": [
            {
                "block_type": "concept_explanation",
                "component_type": "concept_explanation",
                "title": "Facilitating Global Dialogue and Consensus",
                "content": {
                    "text": (
                        "IGOs provide a structured, neutral platform where political leaders from conflicting or aligned nations meet regularly to debate pressing global challenges.\n\n"
                        "- Prevents diplomatic isolation and creates opportunities for informal bilateral meetings on the sidelines of major summits.\n"
                        "- Facilitates multilateral negotiations on trade tariffs, arms control, and environmental preservation.\n\n"
                        "**Historical Evidence:** The annual UN General Assembly sessions in New York, where heads of state gather every September to articulate national priorities."
                    )
                }
            }
        ]
    },
    {
        "page_number": 6,
        "page_title": "Role 2 of IGOs: Regulation of Specialized Technical Fields",
        "blocks": [
            {
                "block_type": "concept_explanation",
                "component_type": "concept_explanation",
                "title": "Setting Uniform International Technical Standards",
                "content": {
                    "text": (
                        "Modern global commerce, transport, and public health require strict cross-border synchronization governed by specialized IGO agencies:\n\n"
                        "- **Civil Aviation:** The International Civil Aviation Organization (ICAO) standardizes global air traffic control, runway safety, and pilot licensing protocols.\n"
                        "- **Telecommunications:** The International Telecommunication Union (ITU) allocates global satellite orbital slots and radio frequencies.\n"
                        "- **Global Health:** The World Health Organization (WHO) coordinates epidemiological surveillance, sets pharmaceutical purity guidelines, and directs disease eradication campaigns."
                    )
                }
            }
        ]
    },
    {
        "page_number": 7,
        "page_title": "Role 3 of IGOs: Enhancement of Global Peace and Security",
        "blocks": [
            {
                "block_type": "concept_explanation",
                "component_type": "concept_explanation",
                "title": "Peacekeeping, Mediation, and Collective Sanctions",
                "content": {
                    "text": (
                        "IGOs possess executive mandates to intervene in armed conflicts to protect civilian lives and restore constitutional order:\n\n"
                        "- Deploying multinational peacekeeping forces (wearing the iconic 'Blue Helmets') to buffer warring factions and monitor ceasefires.\n"
                        "- Imposing binding economic sanctions, arms embargoes, and travel bans against rogue regimes that violate international law.\n\n"
                        "**Historical Evidence:** UN peacekeeping missions deployed in the Democratic Republic of Congo (MONUSCO) and South Sudan (UNMISS) to protect vulnerable civilian populations."
                    )
                }
            }
        ]
    },
    {
        "page_number": 8,
        "page_title": "Role 4 of IGOs: Humanitarian Assistance and Disaster Relief",
        "blocks": [
            {
                "block_type": "concept_explanation",
                "component_type": "concept_explanation",
                "title": "Coordinating Emergency Food, Water, and Medical Aid",
                "content": {
                    "text": (
                        "When natural disasters (earthquakes, tsunamis, prolonged droughts) or civil wars cause massive displacement, IGOs organize global emergency relief pipelines:\n\n"
                        "- **World Food Programme (WFP):** Distributes emergency food rations to millions facing famine in conflict zones.\n"
                        "- **UN High Commissioner for Refugees (UNHCR):** Establishes and manages refugee camps, providing shelter, clean water, and legal documentation (e.g., Kakuma and Dadaab refugee complexes in Kenya)."
                    )
                }
            }
        ]
    },
    {
        "page_number": 9,
        "page_title": "Role 5 of IGOs: Economic Stabilization and Development Finance",
        "blocks": [
            {
                "block_type": "concept_explanation",
                "component_type": "concept_explanation",
                "title": "Providing Concessionary Capital and Monetary Advice",
                "content": {
                    "text": (
                        "IGOs maintain international macroeconomic stability and fund long-term poverty alleviation:\n\n"
                        "- **International Monetary Fund (IMF):** Provides short-term emergency balance-of-payments loans to stabilize collapsing national currencies and prevent debt defaults.\n"
                        "- **World Bank (IBRD / IDA):** Finances large-scale capital infrastructure projects—including national electrical grids, trunk highways, and modern port terminals—in developing nations."
                    )
                }
            }
        ]
    },
    {
        "page_number": 10,
        "page_title": "The Vital Role of International NGOs",
        "blocks": [
            {
                "block_type": "concept_explanation",
                "component_type": "concept_explanation",
                "title": "Independent Civil Society: Watchdogs for Human Dignity",
                "content": {
                    "text": (
                        "Operating without governmental constraints, international NGOs perform indispensable advocacy and frontline humanitarian duties:\n\n"
                        "- **International Committee of the Red Cross (ICRC):** Founded under the Geneva Conventions to provide neutral medical care on battlefields and inspect the humane treatment of prisoners of war.\n"
                        "- **Amnesty International:** Campaigns against torture, unlawful political detentions, and capital punishment worldwide.\n"
                        "- **Transparency International:** Publishes the annual Corruption Perceptions Index (CPI), exposing public sector bribery and advocating for institutional accountability."
                    )
                }
            }
        ]
    },
    {
        "page_number": 11,
        "page_title": "Interactive Categorization Activity",
        "blocks": [
            {
                "block_type": "mini_activity",
                "component_type": "mini_activity",
                "title": "Classify the International Body (IGO vs. NGO)",
                "content": {
                    "instruction": "Categorize each of the following international organizations into either an IGO or an NGO:",
                    "items": [
                        "1. World Health Organization (WHO) -> **IGO (Inter-Governmental Organization)**",
                        "2. Amnesty International -> **NGO (Non-Governmental Organization)**",
                        "3. African Union (AU) -> **IGO (Inter-Governmental Organization)**",
                        "4. International Committee of the Red Cross (ICRC) -> **NGO (Non-Governmental Organization)**",
                        "5. International Monetary Fund (IMF) -> **IGO (Inter-Governmental Organization)**",
                        "6. Transparency International -> **NGO (Non-Governmental Organization)**"
                    ]
                }
            }
        ]
    },
    {
        "page_number": 12,
        "page_title": "KCSE Examination Coaching: Roles of IGOs",
        "blocks": [
            {
                "block_type": "worked_example",
                "component_type": "worked_example",
                "title": "KCSE Question: Explain Five Roles Played by International Governmental Organizations in the Modern World (10 Marks)",
                "content": {
                    "text": (
                        "**Model Full-Mark Answer (Point + Explanation + Evidence):**\n\n"
                        "1. **Provision of Forums for Dialogue:** They provide neutral diplomatic platforms where sovereign leaders regularly meet to debate international crises and build consensus on global treaties. (2 marks)\n\n"
                        "2. **Enhancement of Peace and Security:** They deploy multinational peacekeeping forces to conflict zones and enforce economic sanctions to deter aggressive nations. (2 marks)\n\n"
                        "3. **Regulation of Technical and Health Standards:** Specialized agencies like the WHO and ICAO set uniform international safety guidelines for aviation, maritime transport, and epidemic control. (2 marks)\n\n"
                        "4. **Humanitarian Relief and Crisis Response:** Bodies like the World Food Programme (WFP) and UNHCR deliver emergency food, medical supplies, and shelter to victims of war and natural disasters. (2 marks)\n\n"
                        "5. **Economic Stabilization and Development Finance:** Institutions such as the World Bank and IMF provide development loans and structural advice to stabilize struggling national economies. (2 marks)"
                    )
                }
            }
        ]
    },
    {
        "page_number": 13,
        "page_title": "Check Your Understanding: Module 2.2",
        "blocks": [
            {
                "block_type": "knowledge_check",
                "component_type": "knowledge_check",
                "title": "Module 2.2 Assessment",
                "content": {
                    "questions": [
                        {
                            "question": "Which feature fundamentally differentiates an IGO from an NGO?",
                            "options": [
                                "IGOs are established through formal treaties signed by sovereign governments, whereas NGOs are founded by private citizens or trusts.",
                                "IGOs only operate in Africa, while NGOs operate globally.",
                                "NGOs possess state police powers, whereas IGOs have no authority.",
                                "IGOs are funded entirely by private public donations."
                            ],
                            "correct_answer": 0,
                            "explanation": "IGOs are formed by sovereign states through legal treaties, while NGOs are private, non-profit civil society entities."
                        },
                        {
                            "question": "Which international NGO is primarily dedicated to monitoring global corruption and promoting transparency?",
                            "options": [
                                "Greenpeace",
                                "Amnesty International",
                                "Transparency International",
                                "Médecins Sans Frontières"
                            ],
                            "correct_answer": 2,
                            "explanation": "Transparency International publishes the annual Corruption Perceptions Index and advocates for open, ethical governance."
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
                "title": "Core Summary: IGOs and NGOs in Global Governance",
                "content": {
                    "text": (
                        "• **Classification:** IGOs are created by sovereign states via treaties (UN, AU, Commonwealth), while NGOs are created by private civil society (Red Cross, Amnesty, Transparency International).\n"
                        "• **Five Core IGO Roles:** Consultation forums, technical standard-setting, peacekeeping and security, humanitarian disaster relief, and development finance.\n"
                        "• **NGO Strength:** Freedom from government control enables NGOs to act as independent moral watchdogs for human rights and governance."
                    )
                }
            },
            {
                "block_type": "key_takeaway",
                "component_type": "key_takeaway",
                "title": "Key Takeaways",
                "content": {
                    "text": (
                        "- Both IGOs and NGOs are essential pillars of global order, complementing each other to address security, humanitarian, and developmental needs."
                    )
                }
            }
        ]
    }
]

LESSON_3_PAGES = [
    {
        "page_number": 1,
        "page_title": "The League of Nations: The First Experiment in Global Security",
        "blocks": [
            {
                "block_type": "learning_goal",
                "component_type": "learning_goal",
                "title": "Lesson Objectives: The League of Nations",
                "content": {
                    "text": (
                        "By the end of this lesson, you will be able to:\n"
                        "- Analyze the origins, founding principles, and 6 core aims of the League of Nations\n"
                        "- Describe the composition and specific functions of the League's 5 structural organs\n"
                        "- Evaluate the major successes achieved by the League during the 1920s\n"
                        "- Explain the fatal crises of the 1930s and the 6 fundamental reasons for the League's collapse"
                    )
                }
            },
            {
                "block_type": "definition_card",
                "component_type": "definition_card",
                "title": "Definition: The League of Nations",
                "content": {
                    "term": "The League of Nations",
                    "definition": (
                        "The world's first permanent intergovernmental collective security organization, established in 1920 under the Treaty of Versailles "
                        "following World War I, tasked with preserving global peace, promoting disarmament, and settling international disputes through arbitration."
                    )
                }
            }
        ]
    },
    {
        "page_number": 2,
        "page_title": "Origins and Headquarters in Geneva",
        "blocks": [
            {
                "block_type": "concept_explanation",
                "component_type": "concept_explanation",
                "title": "Woodrow Wilson's Vision and the Paris Peace Conference",
                "content": {
                    "text": (
                        "The catastrophic carnage of World War I convinced world leaders that secret diplomacy and mutual defense pacts had failed humanity.\n\n"
                        "- **Champion of the Idea:** US President **Woodrow Wilson** proposed the creation of a 'general association of nations' in Point 14 of his famous Fourteen Points address (January 1918).\n"
                        "- **Founding Covenant:** The Covenant of the League of Nations was incorporated into Part I of the Treaty of Versailles in 1919.\n"
                        "- **Commencement & Headquarters:** The League officially commenced operations on **10 January 1920**, establishing its permanent headquarters at the **Palais des Nations in Geneva, Switzerland** (chosen for Swiss historic neutrality).\n\n"
                        "*(Critical Irony: The US Senate refused to ratify the Treaty of Versailles, meaning the United States never joined the very organization its own President had created!)*"
                    )
                }
            }
        ]
    },
    {
        "page_number": 3,
        "page_title": "The Palais des Nations in Geneva",
        "blocks": [
            {
                "block_type": "suggested_image",
                "component_type": "suggested_image",
                "title": "The Palace of Nations (Palais des Nations) in Geneva",
                "content": {
                    "text": "The Palais des Nations in Geneva, Switzerland, built as the grand headquarters of the League of Nations to serve as the global capital of collective diplomacy.",
                    "url": "https://upload.wikimedia.org/wikipedia/commons/7/72/Palace_of_Nations_Geneva_20102014_02.jpg",
                    "author": "Gerd Eichmann / CC BY-SA 4.0",
                    "licensing": "CC BY-SA 4.0",
                    "commons_page_url": "https://commons.wikimedia.org/wiki/File:Palace_of_Nations_Geneva_20102014_02.jpg"
                }
            }
        ]
    },
    {
        "page_number": 4,
        "page_title": "The Six Core Aims of the League of Nations",
        "blocks": [
            {
                "block_type": "concept_explanation",
                "component_type": "concept_explanation",
                "title": "The Covenant's Mandate for World Order",
                "content": {
                    "text": (
                        "The Covenant set out six fundamental objectives for member states:\n\n"
                        "1. **Maintenance of World Peace:** Preventing the outbreak of another catastrophic world war through transparent collective diplomacy.\n"
                        "2. **Enforcement of Collective Security:** Members pledged joint, immediate action (diplomatic boycotts, economic sanctions, or military force) against any agreed aggressor state.\n"
                        "3. **Promotion of International Cooperation:** Fostering cross-border solutions for global socio-economic, health, and transit problems.\n"
                        "4. **Global Disarmament:** Encouraging all nations to reduce national armaments to the lowest point consistent with domestic safety.\n"
                        "5. **Administration of Mandated Territories:** Supervising the welfare and gradual development of former German and Ottoman colonies.\n"
                        "6. **Securing Humane Labour Conditions:** Establishing international labor standards, fair wages, reasonable work hours, and social security."
                    )
                }
            }
        ]
    },
    {
        "page_number": 5,
        "page_title": "Structural Organ 1: The Assembly",
        "blocks": [
            {
                "block_type": "concept_explanation",
                "component_type": "concept_explanation",
                "title": "The General Parliament of the League",
                "content": {
                    "text": (
                        "- **Composition:** Comprised official delegates from all member states. Each member country was permitted up to three representatives but held **exactly one vote**.\n"
                        "- **Meetings:** Met annually in Geneva every September, with special emergency sessions convened when necessary.\n"
                        "- **Key Functions:**\n"
                        "  - Controlled and approved the League's annual operational budget.\n"
                        "  - Admitted new member states (required a two-thirds majority vote).\n"
                        "  - Elected the non-permanent rotational members of the Council.\n"
                        "  - Jointly appointed the 15 judges of the Permanent Court of International Justice alongside the Council."
                    )
                }
            }
        ]
    },
    {
        "page_number": 6,
        "page_title": "Structural Organ 2: The Council",
        "blocks": [
            {
                "block_type": "concept_explanation",
                "component_type": "concept_explanation",
                "title": "The Executive Organ for Dispute Settlement",
                "content": {
                    "text": (
                        "- **Composition:** Consisted of **Permanent Members** (Great Britain, France, Italy, and Japan; Germany joined in 1926, USSR in 1934) and four (later nine) **Non-Permanent Members** elected by the Assembly for rotational three-year terms.\n"
                        "- **Meetings:** Met four to five times a year and in immediate emergency sessions during border crises.\n"
                        "- **Key Functions:**\n"
                        "  - Primary executive body charged with settling international disputes threatening peace.\n"
                        "  - Had the constitutional power to formulate disarmament plans and recommend economic or military sanctions against aggressor states.\n"
                        "- **The Unanimity Flaw:** Substantive decisions required the **unanimous vote** of all members present, allowing any single state on the Council to paralyze action."
                    )
                }
            }
        ]
    },
    {
        "page_number": 7,
        "page_title": "Structural Organ 3: The Secretariat",
        "blocks": [
            {
                "block_type": "concept_explanation",
                "component_type": "concept_explanation",
                "title": "The International Administrative Civil Service",
                "content": {
                    "text": (
                        "- **Composition:** Headed by the **Secretary-General**, supported by an international civil service staff based in Geneva.\n"
                        "- **First Secretary-General:** British diplomat **Sir Eric Drummond** (served 1920–1933), followed by Joseph Avenol of France (1933–1940).\n"
                        "- **Key Functions:**\n"
                        "  - Managed daily administrative correspondence, prepared agendas, and drafted official reports for the Assembly and Council.\n"
                        "  - Registered and published international treaties to eliminate secret military pacts.\n"
                        "  - Coordinated the documentation and logistical operations of all specialized commissions."
                    )
                }
            }
        ]
    },
    {
        "page_number": 8,
        "page_title": "Structural Organs 4 & 5: PCIJ, ILO, and Mandates Commission",
        "blocks": [
            {
                "block_type": "comparison_table",
                "component_type": "comparison_table",
                "title": "Specialized Judicial and Functional Bodies of the League",
                "content": {
                    "headers": ["Body Name", "Headquarters", "Composition", "Primary Mandate"],
                    "rows": [
                        ["Permanent Court of International Justice (PCIJ)", "The Hague, Netherlands", "11 permanent judges & 4 deputy judges elected for 9-year terms", "Arbitrated legal border and maritime disputes between states and delivered formal advisory opinions."],
                        ["International Labour Organization (ILO)", "Geneva, Switzerland", "Representatives from national governments, employers, and trade unions", "Standardized the 8-hour workday, abolished child labor, set minimum wage baselines, and regulated workplace safety."],
                        ["The Mandates Commission", "Geneva, Switzerland", "Ten independent colonial specialists appointed by the Council", "Supervised the administration of former German and Turkish colonies (e.g., Tanganyika, Togo, Cameroon, Rwanda-Urundi) to protect indigenous rights."]
                    ]
                }
            }
        ]
    },
    {
        "page_number": 9,
        "page_title": "Major Achievements of the League in the 1920s",
        "blocks": [
            {
                "block_type": "concept_explanation",
                "component_type": "concept_explanation",
                "title": "Successful Diplomatic Arbitrations and Humanitarian Feats",
                "content": {
                    "text": (
                        "During its first decade (1920–1929), the League recorded significant successes:\n\n"
                        "1. **Aaland Islands Dispute (1920–1921):** Successfully arbitrated a tense territorial dispute between Sweden and Finland, awarding the islands to Finland with safeguards for Swedish culture.\n"
                        "2. **Upper Silesia Settlement (1921):** Mediated a peaceful partition of the industrial border province of Upper Silesia between Poland and Germany following a contested plebiscite.\n"
                        "3. **Mosul Frontier Dispute (1924–1926):** Settled the volatile oil-rich border dispute between Turkey and Iraq, resolving the conflict in Iraq's favor.\n"
                        "4. **Greek-Bulgarian Crisis (1925):** When Greek forces invaded Bulgaria after a border shooting, the League ordered a swift ceasefire and forced Greece to pay reparations.\n"
                        "5. **Refugee Resettlement:** The League's High Commission for Refugees (led by Fridtjof Nansen) created the 'Nansen Passport,' resettling over 400,000 displaced prisoners of war and refugees from the Russian Revolution."
                    )
                }
            }
        ]
    },
    {
        "page_number": 10,
        "page_title": "The Manchurian Crisis (1931–1933)",
        "blocks": [
            {
                "block_type": "concept_explanation",
                "component_type": "concept_explanation",
                "title": "The First Fatal Blow to Collective Security",
                "content": {
                    "text": (
                        "In September 1931, the Imperial Japanese Army staged a false-flag bombing on the South Manchurian Railway (the Mukden Incident) and launched a full-scale military invasion of the Chinese province of Manchuria, renaming it the puppet state of *Manchukuo*.\n\n"
                        "- **China's Appeal:** China appealed to the League of Nations for collective defense under Article 16.\n"
                        "- **League's Ineffective Response:** The League dispatched the **Lytton Commission**, which took over a year to publish a report condemning Japanese aggression.\n"
                        "- **Japan's Defiance:** Japan rejected the report, walked out of the League Assembly in March 1933, and officially withdrew from the organization, continuing its brutal occupation of China completely unpunished."
                    )
                }
            }
        ]
    },
    {
        "page_number": 11,
        "page_title": "The Abyssinian Crisis (1935–1936)",
        "blocks": [
            {
                "block_type": "concept_explanation",
                "component_type": "concept_explanation",
                "title": "Mussolini's Unprovoked Invasion of Ethiopia",
                "content": {
                    "text": (
                        "In October 1935, Italian Fascist dictator **Benito Mussolini** launched a massive military invasion of Ethiopia (Abyssinia) using poison mustard gas, heavy bombers, and mechanized armor to avenge Italy's humiliating 1896 defeat at Adwa.\n\n"
                        "- **Haile Selassie's Appeal:** Ethiopian Emperor **Haile Selassie** traveled to Geneva in June 1936 to address the League Assembly in person, uttering the prophetic warning:\n"
                        "  > *'It is collective security; it is the very existence of the League of Nations... God and history will remember your judgment.'*\n"
                        "- **League's Weak Sanctions:** The League imposed partial economic sanctions on Italy but fatally excluded oil and coal, while Britain and France kept the Suez Canal open to Italian troopships to avoid provoking Mussolini.\n"
                        "- **Result:** Italy conquered Addis Ababa in May 1936, annexed Ethiopia, and withdrew from the League in 1937."
                    )
                }
            },
            {
                "block_type": "suggested_image",
                "component_type": "suggested_image",
                "title": "Emperor Haile Selassie Addressing the League in Geneva, 1936",
                "content": {
                    "text": "Emperor Haile Selassie of Ethiopia delivering his historic address to the League of Nations Assembly in Geneva in June 1936, pleading for collective security against Italian aggression.",
                    "url": "https://upload.wikimedia.org/wikipedia/commons/1/16/Emperor_Haile_Selassie_League_of_Nations_speech.png",
                    "author": "Public Domain / League of Nations Archives",
                    "licensing": "Public Domain",
                    "commons_page_url": "https://commons.wikimedia.org/wiki/File:Emperor_Haile_Selassie_League_of_Nations_speech.png"
                }
            }
        ]
    },
    {
        "page_number": 12,
        "page_title": "Historical Documentary: Haile Selassie's 1936 Warning",
        "blocks": [
            {
                "block_type": "suggested_video",
                "component_type": "suggested_video",
                "title": "Archival Footage: Emperor Haile Selassie at the League of Nations (1936)",
                "content": {
                    "url": "https://www.youtube.com/watch?v=KEzjieGNV0I",
                    "text": "Quick History documentary tracing the origins, structural organs, successes, and ultimate collapse of the League of Nations.",
                    "author": "History Core",
                    "licensing": "Standard YouTube License"
                }
            }
        ]
    },
    {
        "page_number": 13,
        "page_title": "Hitler's Defiance and the Soviet Invasion of Finland (1939)",
        "blocks": [
            {
                "block_type": "concept_explanation",
                "component_type": "concept_explanation",
                "title": "The Total Collapse of International Law",
                "content": {
                    "text": (
                        "During the late 1930s, the League was completely ignored as aggressive dictators dismantled the Versailles order:\n\n"
                        "- **German Rearmament & Expansion (1935–1939):** Adolf Hitler reintroduced military conscription, remilitarized the Rhineland (1936), annexed Austria (*Anschluss*, 1938), and swallowed Czechoslovakia (1939) without a single League sanction.\n"
                        "- **Soviet Invasion of Finland (November 1939):** The USSR invaded Finland during the Winter War. While the League formally expelled the Soviet Union in December 1939 (its final official act), it had zero physical power to halt the invasion.\n\n"
                        "When World War II erupted in September 1939, the League ceased all political operations, formally dissolving itself on **18 April 1946** to transfer its assets to the newly formed United Nations."
                    )
                }
            }
        ]
    },
    {
        "page_number": 14,
        "page_title": "Why Did the League of Nations Fail? (Six Core Factors)",
        "blocks": [
            {
                "block_type": "step_process",
                "component_type": "step_process",
                "title": "The Six Fundamental Causes of the League's Collapse",
                "content": {
                    "steps": [
                        "1. Absence of Major Superpowers: The world's wealthiest and most powerful nation, the United States, never joined. Germany and the USSR were initially excluded and only remained temporary members.",
                        "2. Lack of an Independent Standing Army: The League had no military force of its own. It depended on member states to contribute soldiers, but nations refused to risk troops in conflicts that did not serve national interests.",
                        "3. The Appeasement Policy of Britain and France: The two dominant leading members prioritized national self-preservation and appeased expansionist dictators (Hitler and Mussolini) rather than taking decisive collective action.",
                        "4. Structural Unanimity / Veto Flaw: The Assembly and Council required unanimous votes on substantive issues, allowing any single rogue state to veto and block emergency interventions.",
                        "5. Association with the Punitive Versailles Treaty: The League was viewed by defeated nations (Germany, Austria, Hungary) as an instrument of Allied oppression, making voluntary compliance impossible.",
                        "6. Severe Financial Constraints & Great Depression: The 1929 Wall Street Crash caused global economic collapse; nations turned inward toward economic protectionism and defaulted on League dues."
                    ]
                }
            }
        ]
    },
    {
        "page_number": 15,
        "page_title": "KCSE Examination Coaching: Factors for League Failure",
        "blocks": [
            {
                "block_type": "worked_example",
                "component_type": "worked_example",
                "title": "KCSE Question: Explain Five Factors that Undermined the Effectiveness of the League of Nations in Maintaining World Peace (10 Marks)",
                "content": {
                    "text": (
                        "**Examiner's Marking Scheme (Point + Explanation + Evidence = 2 Marks per Point):**\n\n"
                        "1. **Absence of the United States:** The US Senate refused to ratify the Treaty of Versailles, denying the League the massive diplomatic influence and financial leverage of the world's richest power. (2 marks)\n\n"
                        "2. **Lack of an Independent Army:** The League lacked a standing military force to physically enforce its resolutions against determined aggressors like Japan in Manchuria and Italy in Abyssinia. (2 marks)\n\n"
                        "3. **Appeasement Policy of Major Powers:** Leading members like Britain and France feared another world war and chose to appease aggressive dictators instead of standing up for collective security. (2 marks)\n\n"
                        "4. **Defective Decision-Making Process:** The constitutional requirement for unanimous voting in the Assembly and Council made it impossible to pass decisive peace resolutions during rapid military crises. (2 marks)\n\n"
                        "5. **Severe Financial Constraints:** The global Great Depression of 1929 led member nations to default on annual dues, leaving the Secretariat perpetually underfunded. (2 marks)"
                    )
                }
            }
        ]
    },
    {
        "page_number": 16,
        "page_title": "Check Your Understanding & Summary",
        "blocks": [
            {
                "block_type": "knowledge_check",
                "component_type": "knowledge_check",
                "title": "Module 2.3 Assessment",
                "content": {
                    "questions": [
                        {
                            "question": "Which British diplomat served as the first Secretary-General of the League of Nations from 1920 to 1933?",
                            "options": [
                                "Sir Eric Drummond",
                                "Woodrow Wilson",
                                "David Lloyd George",
                                "Fridtjof Nansen"
                            ],
                            "correct_answer": 0,
                            "explanation": "Sir Eric Drummond organized the League's international civil service and served as its first Secretary-General."
                        },
                        {
                            "question": "In which crisis did the League of Nations fail to impose oil sanctions, allowing Italian forces to conquer Ethiopia?",
                            "options": [
                                "The Manchurian Crisis (1931)",
                                "The Abyssinian Crisis (1935)",
                                "The Spanish Civil War (1936)",
                                "The Corfu Incident (1923)"
                            ],
                            "correct_answer": 1,
                            "explanation": "The Abyssinian Crisis of 1935 exposed the League's toothlessness when it failed to sanction Italian oil or close the Suez Canal."
                        }
                    ]
                }
            },
            {
                "block_type": "summary",
                "component_type": "summary",
                "title": "Core Summary: The League of Nations",
                "content": {
                    "text": (
                        "• **Origins:** Founded in Geneva in 1920 under the Treaty of Versailles, championed by Woodrow Wilson.\n"
                        "• **Organs:** Assembly (universal), Council (executive), Secretariat (admin), PCIJ (court at The Hague), ILO (labor), Mandates Commission.\n"
                        "• **1920s Successes:** Aaland Islands, Upper Silesia, Mosul frontier, Nansen refugee passports.\n"
                        "• **1930s Collapse:** Manchuria (1931), Abyssinia (1935), German rearmament, and Finnish invasion.\n"
                        "• **Core Weaknesses:** No US membership, no standing army, British/French appeasement, and unanimity voting flaw."
                    )
                }
            }
        ]
    }
]

LESSON_4_PAGES = [
    {
        "page_number": 1,
        "page_title": "The United Nations Organization (UN): Founding and Vision",
        "blocks": [
            {
                "block_type": "learning_goal",
                "component_type": "learning_goal",
                "title": "Lesson Objectives: The United Nations Organization",
                "content": {
                    "text": (
                        "By the end of this lesson, you will be able to:\n"
                        "- Trace the step-by-step chronological evolution of the UN from the London Declaration (1941) to the San Francisco Charter (1945)\n"
                        "- Explain the 6 core principles of Article 2 of the UN Charter\n"
                        "- Analyze the composition, powers, and functions of the 6 principal organs of the UN\n"
                        "- Evaluate the global impact of the UN's 8 specialized agencies and its major achievements and challenges"
                    )
                }
            },
            {
                "block_type": "definition_card",
                "component_type": "definition_card",
                "title": "Definition: The United Nations Organization",
                "content": {
                    "term": "United Nations Organization (UN)",
                    "definition": (
                        "An association of independent sovereign states founded on 24 October 1945 following World War II, dedicated to preserving international peace, "
                        "fostering friendly relations among nations based on sovereign equality, promoting human rights, and coordinating global socio-economic cooperation."
                    )
                }
            }
        ]
    },
    {
        "page_number": 2,
        "page_title": "The Chronological Evolution of the UN (1941–1945)",
        "blocks": [
            {
                "block_type": "step_process",
                "component_type": "step_process",
                "title": "The Seven Diplomatic Steps to Founding the UN",
                "content": {
                    "steps": [
                        "1. London Declaration (12 June 1941): Allied representatives meeting in London signed the first joint pledge to build a post-war world free from aggression.",
                        "2. Atlantic Charter (14 August 1941): US President Franklin D. Roosevelt and British PM Winston Churchill drafted core principles: human freedoms, self-determination, and no territorial expansion.",
                        "3. Declaration by United Nations (1 January 1942): 26 Allied nations meeting in Washington DC signed the declaration, officially coining the name 'United Nations' suggested by Roosevelt.",
                        "4. Dumbarton Oaks Conference (Sept–Oct 1944): Representatives of USA, USSR, UK, and China met in Washington DC to draft the first concrete blueprint and organizational structure of the UN.",
                        "5. Yalta Conference (February 1945): Roosevelt, Churchill, and Stalin finalized the Security Council voting procedure and agreed on the permanent P5 veto mechanism.",
                        "6. San Francisco Conference (April–June 1945): Delegates from 50 nations debated and adopted the final 111-Article UN Charter on 25 June 1945.",
                        "7. Official Commencement (24 October 1945): The UN officially began operations after ratification by the P5 and majority of signatories (celebrated globally as United Nations Day). Kenya joined on 16 December 1963."
                    ]
                }
            }
        ]
    },
    {
        "page_number": 3,
        "page_title": "Core Principles of the United Nations Charter",
        "blocks": [
            {
                "block_type": "concept_explanation",
                "component_type": "concept_explanation",
                "title": "Article 2: The Binding Code of International Conduct",
                "content": {
                    "text": (
                        "All member states are legally bound by the six foundational principles established in Article 2 of the UN Charter:\n\n"
                        "1. **Sovereign Equality:** The UN is based on the principle of the sovereign equality of all its members, regardless of size, population, or military wealth.\n"
                        "2. **Good Faith Obligations:** Member states must fulfill in good faith all obligations assumed under the Charter.\n"
                        "3. **Peaceful Settlement of Disputes:** Members must settle international disputes by peaceful diplomatic means without endangering peace, security, or justice.\n"
                        "4. **Prohibition of Threat or Use of Force:** States must refrain in international relations from the threat or use of military force against the territorial integrity or political independence of any state.\n"
                        "5. **Assisting the UN:** Members must give the UN full assistance in any enforcement action it takes and refrain from assisting target states.\n"
                        "6. **Non-Interference in Domestic Affairs:** The UN cannot intervene in matters essentially within the domestic jurisdiction of any sovereign state (except when applying Chapter VII security enforcement)."
                    )
                }
            }
        ]
    },
    {
        "page_number": 4,
        "page_title": "Principal Organ 1: The General Assembly",
        "blocks": [
            {
                "block_type": "concept_explanation",
                "component_type": "concept_explanation",
                "title": "The Global Deliberative Town Hall",
                "content": {
                    "text": (
                        "- **Composition:** Comprises all 193 member states of the UN. Each nation can send up to five delegates but possesses **exactly one vote**.\n"
                        "- **Sessions:** Convenes its regular annual session every September at the UN Headquarters in New York.\n"
                        "- **Core Functions:**\n"
                        "  - Deliberates and makes recommendations on any matters within the scope of the UN Charter.\n"
                        "  - Approves the UN annual budget and apportions financial expenses among member states.\n"
                        "  - Elects the 10 non-permanent members of the Security Council, the 54 members of ECOSOC, and judges of the ICJ.\n"
                        "  - Appoints the Secretary-General upon recommendation of the Security Council.\n"
                        "  - Admits new member states by a two-thirds majority vote upon Security Council recommendation."
                    )
                }
            }
        ]
    },
    {
        "page_number": 5,
        "page_title": "The UN General Assembly Hall",
        "blocks": [
            {
                "block_type": "suggested_image",
                "component_type": "suggested_image",
                "title": "United Nations General Assembly Hall in New York",
                "content": {
                    "text": "The United Nations General Assembly hall in New York City, where representatives of all 193 sovereign nations assemble annually to debate global peace and development.",
                    "url": "https://upload.wikimedia.org/wikipedia/commons/b/bf/United_Nations_General_Assembly_2024.jpg",
                    "author": "United Nations Photo / CC BY-NC-ND 2.0",
                    "licensing": "CC BY-NC-ND 2.0",
                    "commons_page_url": "https://commons.wikimedia.org/wiki/File:United_Nations_General_Assembly_2024.jpg"
                }
            }
        ]
    },
    {
        "page_number": 6,
        "page_title": "Principal Organ 2: The Security Council and the Veto Power",
        "blocks": [
            {
                "block_type": "concept_explanation",
                "component_type": "concept_explanation",
                "title": "The Executive Enforcer of Global Peace",
                "content": {
                    "text": (
                        "- **Composition:** Consists of **15 member states**:\n"
                        "  - **Five Permanent Members (P5):** United States, Russia (successor to USSR), Great Britain, France, and China.\n"
                        "  - **Ten Non-Permanent Members:** Elected by the General Assembly for rotational two-year terms based on geographic distribution.\n"
                        "- **Primary Mandate:** Holds primary responsibility under the Charter for maintaining international peace and security.\n"
                        "- **Enforcement Powers:** Can dispatch ceasefire observers, deploy armed peacekeeping missions, impose binding economic sanctions, or authorize collective military action under Chapter VII.\n"
                        "- **The Veto Power:** Substantive resolutions require 9 affirmative votes, including the concurring votes of all five permanent members. If any single P5 member casts a 'No' vote (Veto), the resolution is instantly defeated."
                    )
                }
            }
        ]
    },
    {
        "page_number": 7,
        "page_title": "The UN Security Council in Session",
        "blocks": [
            {
                "block_type": "suggested_image",
                "component_type": "suggested_image",
                "title": "The UN Security Council Chamber in Session",
                "content": {
                    "text": "The United Nations Security Council in session in New York, showing the iconic circular diplomatic table where binding global security resolutions are debated.",
                    "url": "https://upload.wikimedia.org/wikipedia/commons/9/9a/Rados%C5%82aw_Sikorski_at_the_UN_Security_Council%2C_during_the_opening_of_79th_UNGA_%281%29.jpg",
                    "author": "Ministry of Foreign Affairs of Poland / CC BY 3.0 PL",
                    "licensing": "CC BY 3.0 PL",
                    "commons_page_url": "https://commons.wikimedia.org/wiki/File:Rados%C5%82aw_Sikorski_at_the_UN_Security_Council,_during_the_opening_of_79th_UNGA_(1).jpg"
                }
            }
        ]
    },
    {
        "page_number": 8,
        "page_title": "Principal Organs 3 & 4: ECOSOC and the Trusteeship Council",
        "blocks": [
            {
                "block_type": "comparison_table",
                "component_type": "comparison_table",
                "title": "Socio-Economic and Decolonization Organs of the UN",
                "content": {
                    "headers": ["Organ Name", "Composition", "Meeting Schedule", "Primary Mandate"],
                    "rows": [
                        ["Economic and Social Council (ECOSOC)", "54 member states elected by General Assembly for 3-year rotational terms", "Convenes major annual month-long sessions alternating between NY and Geneva", "Coordinates international economic, social, cultural, educational, and health work of specialized agencies and functional commissions."],
                        ["The Trusteeship Council", "The five permanent Security Council members + administering powers", "Suspended active annual operations in November 1994", "Supervised the administration of 11 trust territories (former colonies) to guide them toward self-governance; successfully dissolved operations after Palau gained independence in 1994."]
                    ]
                }
            }
        ]
    },
    {
        "page_number": 9,
        "page_title": "Principal Organ 5: The Secretariat and Secretary-Generals",
        "blocks": [
            {
                "block_type": "comparison_table",
                "component_type": "comparison_table",
                "title": "Historical Leaders of the United Nations Secretariat",
                "content": {
                    "headers": ["Secretary-General", "Country of Origin", "Tenure of Office", "Major Global Milestone"],
                    "rows": [
                        ["Trygve Lie", "Norway", "1946–1953", "Oversaw the establishment of UN headquarters and the Korean War intervention."],
                        ["Dag Hammarskjöld", "Sweden", "1953–1961", "Pioneered modern UN peacekeeping during the Suez Crisis; died in a plane crash during the Congo Crisis."],
                        ["U Thant", "Burma (Myanmar)", "1961–1971", "Mediated during the Cuban Missile Crisis and oversaw the admission of newly independent African nations."],
                        ["Kurt Waldheim", "Austria", "1972–1981", "Managed global relief during the Middle East Arab-Israeli wars and international energy crises."],
                        ["Javier Pérez de Cuéllar", "Peru", "1982–1991", "Mediated the end of the Iran-Iraq War and oversaw the independence of Namibia."],
                        ["Boutros Boutros-Ghali", "Egypt", "1992–1996", "First African Secretary-General; authored 'An Agenda for Peace' for post-Cold War diplomacy."],
                        ["Kofi Annan", "Ghana", "1997–2006", "Launched the Millennium Development Goals (MDGs) and Global Compact; awarded Nobel Peace Prize (2001)."],
                        ["Ban Ki-moon", "South Korea", "2007–2016", "Championed the landmark 2015 Paris Climate Agreement and Sustainable Development Goals (SDGs)."]
                    ]
                }
            }
        ]
    },
    {
        "page_number": 10,
        "page_title": "Principal Organ 6: International Court of Justice (ICJ)",
        "blocks": [
            {
                "block_type": "concept_explanation",
                "component_type": "concept_explanation",
                "title": "The World Court at The Hague",
                "content": {
                    "text": (
                        "- **Composition:** Comprises **15 independent judges** of different nationalities, elected by the General Assembly and Security Council for **nine-year renewable terms**.\n"
                        "- **Seat:** Located at the **Peace Palace in The Hague, Netherlands** (the only principal UN organ not located in New York).\n"
                        "- **Dual Jurisdiction:**\n"
                        "  1. **Contentious Cases:** Settles binding legal disputes submitted by sovereign states (e.g., land border demarcations, maritime sovereignty, diplomatic immunity violations).\n"
                        "  2. **Advisory Opinions:** Delivers non-binding legal guidance on complex questions submitted by the General Assembly, Security Council, or specialized agencies."
                    )
                }
            }
        ]
    },
    {
        "page_number": 11,
        "page_title": "The Eight Major Specialized Agencies of the UN",
        "blocks": [
            {
                "block_type": "comparison_table",
                "component_type": "comparison_table",
                "title": "Specialized UN Agencies and Their Mandates",
                "content": {
                    "headers": ["Specialized Agency", "Headquarters", "Year Founded", "Core Global Function"],
                    "rows": [
                        ["World Health Organization (WHO)", "Geneva, Switzerland", "1948", "Directs international public health, coordinates disease eradication (smallpox, polio, malaria), and sets pharmaceutical safety standards."],
                        ["Food and Agriculture Organization (FAO)", "Rome, Italy", "1945", "Leads global efforts to defeat hunger, improve agricultural productivity, forestry, and rural nutrition."],
                        ["UNESCO", "Paris, France", "1945", "Promotes global literacy, scientific collaboration, freedom of expression, and designates World Heritage Sites."],
                        ["The World Bank (IBRD)", "Washington DC, USA", "1944", "Provides long-term concessionary development loans and grants to fund infrastructure in developing nations."],
                        ["International Monetary Fund (IMF)", "Washington DC, USA", "1944", "Stabilizes global exchange rates, monitors international financial systems, and provides emergency balance-of-payments loans."],
                        ["UNICEF", "New York, USA", "1946", "Delivers humanitarian and developmental aid to children, focusing on immunization, nutrition, primary education, and child protection."],
                        ["UN Environment Programme (UNEP)", "Nairobi, Kenya", "1972", "Coordinates global environmental governance, monitors climate change, biodiversity, and anti-desertification programs."],
                        ["UNHCR", "Geneva, Switzerland", "1950", "Protects the legal rights, safety, and physical welfare of refugees fleeing war, persecution, or disasters worldwide."]
                    ]
                }
            }
        ]
    },
    {
        "page_number": 12,
        "page_title": "Documentary Video: The Founding of the UN (1945)",
        "blocks": [
            {
                "block_type": "suggested_video",
                "component_type": "suggested_video",
                "title": "Historical Documentary: The Birth of the United Nations (1945)",
                "content": {
                    "url": "https://www.youtube.com/watch?v=Z7cZlyIJV3M",
                    "text": "Educational overview explaining the structure, principal organs, and global mission of the United Nations Organization.",
                    "author": "GlobalBriefs",
                    "licensing": "Standard YouTube License"
                }
            }
        ]
    },
    {
        "page_number": 13,
        "page_title": "Major Achievements of the United Nations",
        "blocks": [
            {
                "block_type": "concept_explanation",
                "component_type": "concept_explanation",
                "title": "How the UN Has Shaped the Post-War World",
                "content": {
                    "text": (
                        "Over its eight decades of global operations, the UN has achieved monumental milestones:\n\n"
                        "1. **Prevention of World War III:** Prevented localized Cold War confrontations from escalating into direct nuclear war between superpowers.\n"
                        "2. **Peacekeeping Deployments:** Conducted over 70 peacekeeping and military observer operations across Africa, the Middle East, Asia, and the Balkans.\n"
                        "3. **Decolonization of Empires:** Championed self-determination, accelerating the political independence of over **80 former colonial nations**.\n"
                        "4. **Codification of Universal Human Rights:** Adopted the landmark **Universal Declaration of Human Rights (UDHR)** on 10 December 1948, creating a global standard for human dignity.\n"
                        "5. **Massive Refugee Relief:** The UNHCR has provided life-saving shelter, legal protection, and food assistance to over **50 million refugees** globally.\n"
                        "6. **Environmental Governance:** Organized landmark global summits (1972 Stockholm, 1992 Rio Earth Summit, 2015 Paris Accord) to coordinate climate action."
                    )
                }
            }
        ]
    },
    {
        "page_number": 14,
        "page_title": "Critical Challenges Facing the United Nations",
        "blocks": [
            {
                "block_type": "step_process",
                "component_type": "step_process",
                "title": "Six Structural Obstacles Undermining UN Authority",
                "content": {
                    "steps": [
                        "1. National Sovereignty Constraints: The Charter respects state sovereignty, allowing member nations to ignore non-binding resolutions when they conflict with domestic interests.",
                        "2. Superpower Hegemony & Unilateralism: The UN cannot prevent aggression when a permanent P5 member acts unilaterally (e.g., the 2003 US-led invasion of Iraq without Security Council approval).",
                        "3. Abuse of the Veto Power: Permanent P5 members frequently abuse their veto to shield themselves or political allies from sanctions, paralyzing the Security Council.",
                        "4. Chronic Financial Deficits: Many member states default on annual dues, while major contributors delay payments to exert political influence over UN policies.",
                        "5. Absence of an Independent Army: The UN has no standing military force; it must plead for troop contributions from member states, leading to slow emergency deployments.",
                        "6. Ideological and Geopolitical Polarization: Cold War divisions and modern superpower rivalries (USA, Russia, China) obstruct collective consensus on humanitarian crises."
                    ]
                }
            }
        ]
    },
    {
        "page_number": 15,
        "page_title": "Primary Source Inquiry: Evaluating UN Enforcement Authority",
        "blocks": [
            {
                "block_type": "callout",
                "component_type": "callout",
                "title": "Historical Inquiry: The 2003 Iraq Crisis and UN Authority",
                "content": {
                    "text": (
                        "**Historical Scenario:** In March 2003, the United States and Great Britain launched a full-scale military invasion of Iraq despite failing to obtain a authorizing resolution from the UN Security Council.\n\n"
                        "**Historical Analysis Questions:**\n"
                        "1. **Observe:** Why was the UN Security Council unable to prevent the unilateral military invasion of Iraq in 2003?\n"
                        "2. **Interpret:** What does this crisis reveal about the relationship between permanent P5 superpower status and international law?\n"
                        "3. **KCSE Analytical Point:** Explain why the lack of an independent standing army limits the UN's ability to restrain unilateral superpower actions."
                    )
                }
            }
        ]
    },
    {
        "page_number": 16,
        "page_title": "Interactive Classification Activity: UN Agencies",
        "blocks": [
            {
                "block_type": "mini_activity",
                "component_type": "mini_activity",
                "title": "Match the UN Agency to Its Mandate and Headquarters",
                "content": {
                    "instruction": "Test your mastery of the UN system. Match each specialized agency to its correct headquarters and global function:",
                    "items": [
                        "1. WHO (Geneva, Switzerland) -> **Directs international public health and disease control**",
                        "2. UNEP (Nairobi, Kenya) -> **Coordinates global environmental protection and climate monitoring**",
                        "3. FAO (Rome, Italy) -> **Works to defeat global hunger and modernize agriculture**",
                        "4. UNESCO (Paris, France) -> **Promotes global literacy, science, and cultural heritage preservation**",
                        "5. UNHCR (Geneva, Switzerland) -> **Provides legal protection and humanitarian aid to refugees**",
                        "6. World Bank (Washington DC, USA) -> **Provides long-term infrastructure loans to developing nations**"
                    ]
                }
            }
        ]
    },
    {
        "page_number": 17,
        "page_title": "KCSE Examination Coaching: Challenges Facing the UN",
        "blocks": [
            {
                "block_type": "worked_example",
                "component_type": "worked_example",
                "title": "KCSE Question: Explain Five Factors that Limit the Effectiveness of the United Nations Organization (10 Marks)",
                "content": {
                    "text": (
                        "**Examiner's Marking Scheme (Point + Explanation + Evidence = 2 Marks per Point):**\n\n"
                        "1. **National Sovereignty of Member States:** Member states frequently prioritize domestic self-interests over international peace, defying UN resolutions without facing direct enforcement. (2 marks)\n\n"
                        "2. **Abuse of the Veto Power:** Permanent members (P5) abuse their veto to protect their own geopolitical interests or shield allies from international sanctions, paralyzing the Security Council during crises. (2 marks)\n\n"
                        "3. **Lack of a Standing Military Force:** The UN possesses no independent army of its own and must rely on voluntary troop contributions from member states, causing fatal delays during rapid humanitarian emergencies. (2 marks)\n\n"
                        "4. **Persistent Financial Shortages:** Many member states default on or delay their assessed contributions, leaving the UN Secretariat with inadequate funds to finance peacekeeping operations. (2 marks)\n\n"
                        "5. **Superpower Unilateralism and Hegemony:** The UN is powerless to discipline permanent superpowers when they act outside international law (e.g., the 2003 US invasion of Iraq without Security Council authorization). (2 marks)"
                    )
                }
            }
        ]
    },
    {
        "page_number": 18,
        "page_title": "Check Your Understanding & Summary",
        "blocks": [
            {
                "block_type": "knowledge_check",
                "component_type": "knowledge_check",
                "title": "Module 2.4 Assessment",
                "content": {
                    "questions": [
                        {
                            "question": "Which of the following is the only principal organ of the United Nations located outside New York City?",
                            "options": [
                                "The Economic and Social Council (ECOSOC)",
                                "The International Court of Justice (ICJ)",
                                "The Trusteeship Council",
                                "The Secretariat"
                            ],
                            "correct_answer": 1,
                            "explanation": "The ICJ sits at the Peace Palace in The Hague, Netherlands, while all other five principal organs are headquartered in New York."
                        },
                        {
                            "question": "On what date did Kenya officially become a member state of the United Nations?",
                            "options": [
                                "24 October 1945",
                                "12 December 1963",
                                "16 December 1963",
                                "1 June 1964"
                            ],
                            "correct_answer": 2,
                            "explanation": "Kenya was admitted to the United Nations on 16 December 1963, four days after attaining independence."
                        }
                    ]
                }
            },
            {
                "block_type": "summary",
                "component_type": "summary",
                "title": "Core Summary: The United Nations Organization",
                "content": {
                    "text": (
                        "• **Founding:** Formed on 24 October 1945 following the San Francisco Conference (50 nations).\n"
                        "• **6 Principal Organs:** General Assembly (all members), Security Council (P5 with Veto + 10 non-permanent), ECOSOC (54 members), Trusteeship Council (suspended 1994), Secretariat (led by Secretary-General), ICJ (The Hague).\n"
                        "• **8 Key Agencies:** WHO, FAO, UNESCO, World Bank, IMF, UNICEF, UNEP (Nairobi), UNHCR.\n"
                        "• **Major Strengths:** Averted World War III, accelerated decolonization (80+ nations), established UDHR (1948), and delivered refugee aid.\n"
                        "• **Core Limitations:** Veto abuse, lack of standing army, funding deficits, and superpower unilateralism."
                    )
                }
            }
        ]
    }
]

LESSON_5_PAGES = [
    {
        "page_number": 1,
        "page_title": "The Commonwealth of Nations: Origins and Evolution",
        "blocks": [
            {
                "block_type": "learning_goal",
                "component_type": "learning_goal",
                "title": "Lesson Objectives: The Commonwealth of Nations",
                "content": {
                    "text": (
                        "By the end of this lesson, you will be able to:\n"
                        "- Trace the historical roots of the Commonwealth from the Durham Report (1839) to the modern voluntary association (1947)\n"
                        "- Describe the 6 unique characteristics shared by Commonwealth member nations\n"
                        "- Analyze the principal organs, decision-making procedures, and specialized agencies of the Commonwealth\n"
                        "- Evaluate the benefits member states enjoy and the 6 major challenges confronting the organization"
                    )
                }
            },
            {
                "block_type": "definition_card",
                "component_type": "definition_card",
                "title": "Definition: The Commonwealth of Nations",
                "content": {
                    "term": "The Commonwealth of Nations",
                    "definition": (
                        "A voluntary association of 56 independent sovereign states, most of which were formerly territories, colonies, protectorates, "
                        "or dominions of the British Empire, working collaboratively to advance democracy, human rights, economic development, and cultural cooperation."
                    )
                }
            }
        ]
    },
    {
        "page_number": 2,
        "page_title": "Historical Evolution: From Empire to Equal Partnership",
        "blocks": [
            {
                "block_type": "step_process",
                "component_type": "step_process",
                "title": "The Four Historic Milestones of the Commonwealth",
                "content": {
                    "steps": [
                        "1. The Durham Report (1839): Lord Durham recommended that self-governing British colonies (Canada) be granted internal responsible government while retaining loyalty to the British Crown.",
                        "2. Statute of Westminster (1931): Formally recognized Britain and self-governing Dominions (Canada, Australia, New Zealand, South Africa) as equal, autonomous communities within the British Empire.",
                        "3. The London Declaration (1949): Created the modern Commonwealth when India and Pakistan gained independence and chose to remain members as republics, recognizing the British Monarch strictly as the 'symbolic Head of the Commonwealth'.",
                        "4. Expansion to Non-British Colonies (1995–Present): The modern Commonwealth admitted nations with no historic British colonial ties (Mozambique in 1995, Rwanda in 2009, Gabon and Togo in 2022)."
                    ]
                }
            }
        ]
    },
    {
        "page_number": 3,
        "page_title": "Symbolic Leadership and Headquarters",
        "blocks": [
            {
                "block_type": "concept_explanation",
                "component_type": "concept_explanation",
                "title": "Head of the Commonwealth and the London Secretariat",
                "content": {
                    "text": (
                        "- **Head of the Commonwealth:** The reigning British Monarch (King Charles III) serves as the symbolic, non-executive head of the association, symbolizing the historical unity of the member states.\n"
                        "- **Equal Sovereign Status:** The British Monarch holds no political or constitutional authority over member states; all 56 member nations interact as absolute sovereign equals.\n"
                        "- **Headquarters:** Located at **Marlborough House in London, United Kingdom**, where the permanent Commonwealth Secretariat manages daily operations."
                    )
                }
            }
        ]
    },
    {
        "page_number": 4,
        "page_title": "The Six Distinctive Characteristics of Member States",
        "blocks": [
            {
                "block_type": "step_process",
                "component_type": "step_process",
                "title": "Shared Heritage of Commonwealth Member Nations",
                "content": {
                    "steps": [
                        "1. Shared Official Language: English is used as the common official language of government, education, legal proceedings, and commerce across member states.",
                        "2. Parliamentary Democratic Traditions: Member constitutions and parliamentary structures are largely modeled on the British Westminster democratic system.",
                        "3. Educational and Legal Ties: Members maintain common legal systems based on English Common Law and participate in mutual university scholarship programs.",
                        "4. The Commonwealth Games: Every four years, athletes from member states compete in the 'Friendly Games' to promote international goodwill and cultural solidarity.",
                        "5. Shared Military and Administrative Traditions: Armed forces and civil service structures share similar ranks, uniforms, drills, and administrative procedures.",
                        "6. Unique Diplomatic Exchange: Member states represent their governments in each other's capitals by exchanging High Commissioners rather than ambassadors."
                    ]
                }
            }
        ]
    },
    {
        "page_number": 5,
        "page_title": "Principal Organs of the Commonwealth",
        "blocks": [
            {
                "block_type": "comparison_table",
                "component_type": "comparison_table",
                "title": "Key Decision-Making Bodies of the Commonwealth",
                "content": {
                    "headers": ["Principal Organ", "Composition", "Meeting Frequency", "Primary Function"],
                    "rows": [
                        ["Commonwealth Heads of Government Meeting (CHOGM)", "Heads of State and Prime Ministers of all member countries", "Meets once every two years (biennially) hosted by rotational member states", "Highest policymaking summit; debates global politics, trade, and climate change; reaches decisions strictly by consensus rather than voting."],
                        ["Ministerial Meetings", "Sectoral government ministers (Finance, Foreign Affairs, Health, Education, Law)", "Finance/Foreign Ministers meet annually; Health/Education meet triennially", "Coordinates regional policy implementation, harmonizes legal standards, and oversees development projects."],
                        ["The Commonwealth Secretariat", "Headed by the Secretary-General with international staff based in London", "Continuous daily administrative service (established in 1965 at Ghana's proposal)", "Manages day-to-day operations, executes CHOGM directives, organizes conferences, and coordinates technical assistance programs."]
                    ]
                }
            }
        ]
    },
    {
        "page_number": 6,
        "page_title": "Specialized Agencies of the Commonwealth",
        "blocks": [
            {
                "block_type": "comparison_table",
                "component_type": "comparison_table",
                "title": "Specialized Operational Bodies",
                "content": {
                    "headers": ["Specialized Body", "Established Role & Function"],
                    "rows": [
                        ["Commonwealth Fund for Technical Co-operation (CFTC)", "Provides developmental funds, finance, and technical experts to poorer member states to build public infrastructure and manage government departments."],
                        ["Commonwealth Agricultural Bureau", "Conducts agricultural research, pest control studies, and shares modern farming technologies to boost food security across member states."],
                        ["Commonwealth Parliamentary Association (CPA)", "Brings together parliamentarians across the Commonwealth to exchange legislative best practices and strengthen democratic governance."],
                        ["Commonwealth Scholarship and Fellowship Plan", "Enables students and scholars from developing member nations to pursue advanced postgraduate degrees in universities across the UK, Canada, Australia, and New Zealand."]
                    ]
                }
            }
        ]
    },
    {
        "page_number": 7,
        "page_title": "Commonwealth Heads of Government Meeting (CHOGM)",
        "blocks": [
            {
                "block_type": "suggested_image",
                "component_type": "suggested_image",
                "title": "Commonwealth Heads of Government Meeting (CHOGM) Portrait",
                "content": {
                    "text": "Commonwealth Heads of Government gathered for their biennial summit, reflecting the voluntary, multicultural, and egalitarian partnership of the 56 member nations.",
                    "url": "https://upload.wikimedia.org/wikipedia/commons/3/34/Commonwealth_Heads_of_Government_Meeting_-_2018_%2826690677697%29.jpg",
                    "author": "Commonwealth Secretariat / CC BY 2.0",
                    "licensing": "CC BY 2.0",
                    "commons_page_url": "https://commons.wikimedia.org/wiki/File:Commonwealth_Heads_of_Government_Meeting_-_2018_(26690677697).jpg"
                }
            }
        ]
    },
    {
        "page_number": 8,
        "page_title": "Major Benefits of Commonwealth Membership",
        "blocks": [
            {
                "block_type": "concept_explanation",
                "component_type": "concept_explanation",
                "title": "Tangible Gains for Member States",
                "content": {
                    "text": (
                        "Member nations derive extensive benefits across six key sectors:\n\n"
                        "1. **Educational Growth and Scholarships:** Thousands of scholars from developing states access advanced university training in Britain, Canada, and Australia through Commonwealth scholarships.\n"
                        "2. **Financial and Technical Assistance:** The CFTC supplies technical advisors, agronomists, engineers, and financial grants to implement public development projects.\n"
                        "3. **Favourable Trade Opportunities:** Members enjoy reduced trade barriers, tariff preferences, and commercial networking through Commonwealth business forums.\n"
                        "4. **Democratic Governance & Election Monitoring:** Dispatches neutral election observer missions to monitor elections and ensure transparent, free, and fair voting.\n"
                        "5. **Socio-Cultural Integration:** The quadrennial Commonwealth Games foster global solidarity and friendly athletic competition without political rancor.\n"
                        "6. **Human Rights Watchdog:** Actively censures human rights violations and suspends rogue military regimes that subvert democracy."
                    )
                }
            }
        ]
    },
    {
        "page_number": 9,
        "page_title": "Historical Case Studies: Standing for Human Rights",
        "blocks": [
            {
                "block_type": "concept_explanation",
                "component_type": "concept_explanation",
                "title": "Enforcing Democratic Standards: South Africa and Zimbabwe",
                "content": {
                    "text": (
                        "The Commonwealth has demonstrated its commitment to human rights through decisive political sanctions:\n\n"
                        "- **Apartheid South Africa (1961):** Facing overwhelming condemnation from newly independent Afro-Asian members over its racist apartheid policies, South Africa was forced to withdraw from the Commonwealth in 1961. (It rejoined in 1994 following the democratic election of Nelson Mandela).\n"
                        "- **Nigeria (1995):** Suspended following the execution of human rights activist Ken Saro-Wiwa and environmental campaigners by the military regime of General Sani Abacha (reinstated in 1999 upon return to civilian democracy).\n"
                        "- **Zimbabwe (2002):** Suspended following state-sponsored election violence and human rights abuses under Robert Mugabe; Zimbabwe subsequently withdrew from the organization in 2003."
                    )
                }
            }
        ]
    },
    {
        "page_number": 10,
        "page_title": "Six Major Challenges Facing the Commonwealth",
        "blocks": [
            {
                "block_type": "step_process",
                "component_type": "step_process",
                "title": "Structural and Political Limitations of the Commonwealth",
                "content": {
                    "steps": [
                        "1. Economic Disparities Among Members: The vast wealth gap between industrialized members (UK, Canada, Australia) and developing members (Lesotho, Tuvalu) makes it difficult to align on trade policies.",
                        "2. Chronic Financial Constraints: Many developing nations, suffering domestic economic distress, default on their annual contributions, leaving the Secretariat underfunded.",
                        "3. Lack of Enforcement Machinery: The Commonwealth has no standing army or binding judicial court to enforce its decisions; it relies entirely on moral persuasion, suspension, and diplomatic goodwill.",
                        "4. Conflicting Regional Loyalties: Member states belong to competing regional bodies (AU, EU, EAC, ECOWAS, COMESA) whose policies often take priority over Commonwealth commitments.",
                        "5. Internal Political Instability and Coups: Frequent military coups, civil wars, and governance crises in developing members disrupt the execution of joint programs.",
                        "6. Bilateral Conflicts Between Member States: Longstanding military disputes between prominent members (e.g., recurring border tensions between India and Pakistan over Kashmir) weaken unity."
                    ]
                }
            }
        ]
    },
    {
        "page_number": 11,
        "page_title": "Primary Evidence Analysis: The Consensus Model",
        "blocks": [
            {
                "block_type": "callout",
                "component_type": "callout",
                "title": "Evaluating the Commonwealth Decision-Making Architecture",
                "content": {
                    "text": (
                        "**The Consensus Principle:** Unlike the UN Security Council with its veto power or the General Assembly with its majority votes, CHOGM reaches all decisions strictly through **consensus** (broad general agreement without formal voting).\n\n"
                        "**Analytical Inquiry:**\n"
                        "1. **Advantage:** How does decision-making by consensus protect smaller, less powerful member states like Kenya, Lesotho, or Fiji from being steamrolled by larger powers?\n"
                        "2. **Disadvantage:** Why does consensus make it difficult for the Commonwealth to take rapid, aggressive action during sudden military coups or regional human rights emergencies?"
                    )
                }
            }
        ]
    },
    {
        "page_number": 12,
        "page_title": "Interactive Classification Activity: Commonwealth Organs",
        "blocks": [
            {
                "block_type": "mini_activity",
                "component_type": "mini_activity",
                "title": "Match the Commonwealth Feature to Its Correct Category",
                "content": {
                    "instruction": "Test your knowledge of the Commonwealth system. Match each function to its correct organ or agency:",
                    "items": [
                        "1. Highest policymaking biennial summit of heads of state -> **CHOGM (Head of State Summit)**",
                        "2. Daily administrative management based at Marlborough House, London -> **Commonwealth Secretariat**",
                        "3. Supplying developmental funds and technical experts -> **CFTC (Fund for Technical Co-operation)**",
                        "4. Forum for parliamentarians to share legislative best practices -> **Commonwealth Parliamentary Association**",
                        "5. Quadrennial multi-sport competition promoting cultural ties -> **The Commonwealth Games**"
                    ]
                }
            }
        ]
    },
    {
        "page_number": 13,
        "page_title": "KCSE Examination Coaching: Benefits of Commonwealth",
        "blocks": [
            {
                "block_type": "worked_example",
                "component_type": "worked_example",
                "title": "KCSE Question: Explain Five Benefits that Member States Derive from the Commonwealth of Nations (10 Marks)",
                "content": {
                    "text": (
                        "**Examiner's Marking Scheme (Point + Explanation + Evidence = 2 Marks per Point):**\n\n"
                        "1. **Technical and Financial Assistance:** Poorer nations receive development finance, engineering expertise, and agricultural specialists through the Commonwealth Fund for Technical Co-operation (CFTC). (2 marks)\n\n"
                        "2. **Educational Growth and Scholarships:** Thousands of students access higher education and research opportunities in Britain, Canada, and Australia through Commonwealth scholarship programs. (2 marks)\n\n"
                        "3. **Democratic Governance and Election Monitoring:** The organization deploys neutral observer missions during national elections to ensure transparent and credible voting. (2 marks)\n\n"
                        "4. **Favourable Trade and Commercial Ties:** Member nations enjoy preferential trade access, reduced tariff barriers, and networking through Commonwealth business forums. (2 marks)\n\n"
                        "5. **Socio-Cultural Integration and Sporting Harmony:** The quadrennial Commonwealth Games build international friendship, national prestige, and cultural solidarity among diverse peoples. (2 marks)"
                    )
                }
            }
        ]
    },
    {
        "page_number": 14,
        "page_title": "Check Your Understanding: Module 2.5",
        "blocks": [
            {
                "block_type": "knowledge_check",
                "component_type": "knowledge_check",
                "title": "Module 2.5 Assessment",
                "content": {
                    "questions": [
                        {
                            "question": "In which city is the permanent headquarters of the Commonwealth Secretariat located?",
                            "options": [
                                "Geneva, Switzerland",
                                "London, United Kingdom",
                                "Ottawa, Canada",
                                "Nairobi, Kenya"
                            ],
                            "correct_answer": 1,
                            "explanation": "The Commonwealth Secretariat is based at Marlborough House in London, United Kingdom."
                        },
                        {
                            "question": "Why did South Africa withdraw from the Commonwealth of Nations in 1961?",
                            "options": [
                                "Disputes over Commonwealth membership fees",
                                "Severe international condemnation of its apartheid racial policies",
                                "A border war with neighbouring Namibia",
                                "Refusal to participate in the Commonwealth Games"
                            ],
                            "correct_answer": 1,
                            "explanation": "South Africa withdrew in 1961 following intense criticism from Afro-Asian members over its white-minority apartheid regime."
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
                "title": "Core Summary: The Commonwealth of Nations",
                "content": {
                    "text": (
                        "• **Evolution:** Grew from the 1839 Durham Report, 1931 Statute of Westminster, and 1949 London Declaration.\n"
                        "• **Structure:** Headed symbolically by the British Monarch; managed by the London Secretariat; highest summit is CHOGM (biennial, consensus-based).\n"
                        "• **6 Characteristics:** English language, Westminster democracy, Common Law legal traditions, Commonwealth Games, military traditions, High Commissioners.\n"
                        "• **Key Benefits:** Scholarships, CFTC technical aid, preferential trade, election observation, and human rights watchdog.\n"
                        "• **Key Challenges:** Economic disparities, lack of enforcement army, default on financial dues, and conflicting regional loyalties."
                    )
                }
            },
            {
                "block_type": "key_takeaway",
                "component_type": "key_takeaway",
                "title": "Key Takeaways",
                "content": {
                    "text": (
                        "- The Commonwealth transformed from an imperial dominion into an egalitarian association of sovereign equals.\n"
                        "- Its consensus model balances the voices of small island nations with global economic powers."
                    )
                }
            }
        ]
    }
]

LESSON_6_PAGES = [
    {
        "page_number": 1,
        "page_title": "The Non-Aligned Movement (NAM): The Third Way",
        "blocks": [
            {
                "block_type": "learning_goal",
                "component_type": "learning_goal",
                "title": "Lesson Objectives: The Non-Aligned Movement",
                "content": {
                    "text": (
                        "By the end of this lesson, you will be able to:\n"
                        "- Define non-alignment and understand active neutrality during the Cold War\n"
                        "- Trace the origins from the 1955 Bandung Conference to the 1961 Belgrade Summit\n"
                        "- Identify the Big Four founding leaders and analyze the 6 core objectives of NAM\n"
                        "- Explain the unique administrative architecture (no permanent HQ, rotational chair, consensus)\n"
                        "- Evaluate the major achievements and challenges confronting NAM in the modern era"
                    )
                }
            },
            {
                "block_type": "definition_card",
                "component_type": "definition_card",
                "title": "Definition: The Non-Aligned Movement (NAM)",
                "content": {
                    "term": "The Non-Aligned Movement (NAM)",
                    "definition": (
                        "A voluntary international association of 120 developing nations across Africa, Asia, and Latin America, founded during the Cold War, "
                        "which resolved not to align themselves formally with either superpower military bloc (the capitalist West or communist East), "
                        "pursuing a foreign policy of active neutrality, anti-colonialism, and national sovereignty."
                    )
                }
            }
        ]
    },
    {
        "page_number": 2,
        "page_title": "Cold War Context: Active Neutrality vs. Passive Isolation",
        "blocks": [
            {
                "block_type": "concept_explanation",
                "component_type": "concept_explanation",
                "title": "Why Developing Nations Chose Non-Alignment",
                "content": {
                    "text": (
                        "Following World War II, newly independent countries in Asia and Africa found the world dangerously partitioned between two heavily armed superpower military blocs:\n\n"
                        "- **The Western Bloc:** Led by the United States and NATO, championing democratic capitalism.\n"
                        "- **The Eastern Bloc:** Led by the Soviet Union (USSR) and the Warsaw Pact, championing state communism.\n\n"
                        "**The Meaning of Active Neutrality:**\n"
                        "Non-alignment did **not** mean passive disinterest or total isolation from world affairs. Instead, it meant:\n"
                        "- Judging every international crisis independently on its own moral and legal merits rather than following superpower dictates.\n"
                        "- Refusing to join multi-lateral military alliances (NATO or Warsaw Pact) or host foreign military bases on national soil.\n"
                        "- Championing the total eradication of European colonialism, racial apartheid, and economic exploitation."
                    )
                }
            }
        ]
    },
    {
        "page_number": 3,
        "page_title": "Historic Milestones: Bandung (1955) and Belgrade (1961)",
        "blocks": [
            {
                "block_type": "step_process",
                "component_type": "step_process",
                "title": "From Bandung Principles to the Belgrade Summit",
                "content": {
                    "steps": [
                        "1. The Bandung Conference (April 1955): Leaders of 29 newly independent Afro-Asian states met in Bandung, Indonesia. They formulated the 'Ten Principles of Bandung' (Panchsheel), emphasizing peaceful coexistence, mutual non-aggression, and anti-imperialism.",
                        "2. Preparatory Cairo Meeting (June 1961): Foreign ministers established formal criteria for NAM membership: independent foreign policy, support for national liberation, and refusal of bilateral military pacts with superpowers.",
                        "3. The Belgrade Summit (September 1961): The First Official Summit of Non-Aligned Heads of State convened in Belgrade, Yugoslavia, formally launching the movement with 25 founding member nations."
                    ]
                }
            }
        ]
    },
    {
        "page_number": 4,
        "page_title": "The Historic 1955 Bandung Conference",
        "blocks": [
            {
                "block_type": "suggested_image",
                "component_type": "suggested_image",
                "title": "Delegates at the Asian-African Bandung Conference, 1955",
                "content": {
                    "text": "Delegates attending the historic 1955 Asian-African Conference in Bandung, Indonesia, where the founding principles of the Non-Aligned Movement were established.",
                    "url": "https://upload.wikimedia.org/wikipedia/commons/3/3c/Asian%E2%80%93African_Conference_at_Bandung_April_1955.jpg",
                    "author": "Indonesian Ministry of Information / Public Domain",
                    "licensing": "Public Domain",
                    "commons_page_url": "https://commons.wikimedia.org/wiki/File:Asian%E2%80%93African_Conference_at_Bandung_April_1955.jpg"
                }
            }
        ]
    },
    {
        "page_number": 5,
        "page_title": "The Big Four Founding Fathers of NAM",
        "blocks": [
            {
                "block_type": "comparison_table",
                "component_type": "comparison_table",
                "title": "The Visionary Leaders Behind Non-Alignment",
                "content": {
                    "headers": ["Founding Leader", "Country", "Political Role", "Core Contribution to NAM"],
                    "rows": [
                        ["Jawaharlal Nehru", "India", "Prime Minister", "Formulated the concept of positive non-alignment and the Five Principles of Peaceful Coexistence (Panchsheel)."],
                        ["Marshal Josip Broz Tito", "Yugoslavia", "President", "Broke away from Soviet domination in 1948, proving that a socialist state could remain fiercely independent outside the Warsaw Pact; hosted the 1961 Belgrade Summit."],
                        ["Gamal Abdel Nasser", "Egypt", "President", "Championed Arab and African anti-imperialism; nationalized the Suez Canal (1956), demonstrating the courage of developing states against colonial aggression."],
                        ["Kwame Nkrumah", "Ghana", "President", "Champion of Pan-African liberation; asserted that Ghana's independence was meaningless unless linked with the total liberation of the African continent."]
                    ]
                }
            }
        ]
    },
    {
        "page_number": 6,
        "page_title": "Tito, Nasser, and Nehru in Belgrade (1961)",
        "blocks": [
            {
                "block_type": "suggested_image",
                "component_type": "suggested_image",
                "title": "Tito, Nasser, and Nehru at the 1961 Belgrade Conference",
                "content": {
                    "text": "The founding leaders of the Non-Aligned Movement—Josip Broz Tito, Gamal Abdel Nasser, and Jawaharlal Nehru—photographed during the landmark 1961 Belgrade Summit.",
                    "url": "https://upload.wikimedia.org/wikipedia/commons/4/4d/Belgrade_Conference%2C_1961.jpg",
                    "author": "Museum of Yugoslav History / CC BY-SA 3.0 RS",
                    "licensing": "CC BY-SA 3.0 RS",
                    "commons_page_url": "https://commons.wikimedia.org/wiki/File:Belgrade_Conference,_1961.jpg"
                }
            }
        ]
    },
    {
        "page_number": 7,
        "page_title": "The Six Core Objectives of NAM",
        "blocks": [
            {
                "block_type": "step_process",
                "component_type": "step_process",
                "title": "The Foundational Goals of the Non-Aligned Movement",
                "content": {
                    "steps": [
                        "1. Safeguarding National Sovereignty: Protecting the fragile political independence and territorial integrity of newly liberated developing states.",
                        "2. Anti-Colonialism & Anti-Apartheid: Providing diplomatic, material, and moral backing to African and Asian liberation movements fighting colonial rule and white-minority regimes.",
                        "3. Rejecting Superpower Military Alliances: Refusing to join multi-lateral military pacts (NATO, Warsaw Pact, SEATO, CENTO) or permit foreign military bases on national soil.",
                        "4. Promoting Global Disarmament: Demanding that superpowers dismantle and eliminate their massive nuclear arsenals to prevent atomic warfare.",
                        "5. Dismantling Neo-Colonialism: Resisting economic exploitation and foreign economic interference in the domestic resources of developing nations.",
                        "6. Establishing a New International Economic Order (NIEO): Advocating for fairer terms of world trade, debt relief, and technology transfers from the Global North to the Global South."
                    ]
                }
            }
        ]
    },
    {
        "page_number": 8,
        "page_title": "The Unique Administrative Architecture of NAM",
        "blocks": [
            {
                "block_type": "concept_explanation",
                "component_type": "concept_explanation",
                "title": "Administration Without Bureaucracy: Why NAM Has No Headquarters",
                "content": {
                    "text": (
                        "Unlike the UN or Commonwealth, NAM was deliberately designed without rigid institutional bureaucracy:\n\n"
                        "- **No Permanent Headquarters or Secretariat:** Deliberately avoids a fixed physical headquarters to prevent any single superpower or wealthy member from dominating the movement.\n"
                        "- **No Formal Written Constitution:** Operates flexibly through declarations and resolutions adopted at triennial summits.\n"
                        "- **Rotational Chairmanship:** The Head of State of the nation hosting the triennial summit automatically assumes the **Chairmanship of NAM for three years**, using their own national Foreign Ministry to run administrative affairs.\n"
                        "- **The Coordinating Bureau (New York):** Composed of NAM permanent ambassadors to the UN in New York, coordinating daily voting positions inside the UN General Assembly.\n"
                        "- **Decision-Making by Consensus:** Reaches decisions through exhaustive consultation and mutual accommodation rather than divisive formal voting.\n"
                        "- **The Troika:** A consultative trio comprising the past, current, and incoming future Chairpersons to ensure administrative continuity."
                    )
                }
            }
        ]
    },
    {
        "page_number": 9,
        "page_title": "Historical Documentary: The Birth of Non-Alignment",
        "blocks": [
            {
                "block_type": "suggested_video",
                "component_type": "suggested_video",
                "title": "Documentary Footage: The 1955 Bandung Conference & Birth of NAM",
                "content": {
                    "url": "https://www.youtube.com/watch?v=S8uNOerjtSQ",
                    "text": "Historical documentary explaining the 1955 Bandung Conference, active neutrality, and the formation of the Non-Aligned Movement during the Cold War.",
                    "author": "PostalPast",
                    "licensing": "Standard YouTube License"
                }
            }
        ]
    },
    {
        "page_number": 10,
        "page_title": "Major Achievements of the Non-Aligned Movement",
        "blocks": [
            {
                "block_type": "concept_explanation",
                "component_type": "concept_explanation",
                "title": "Transforming the Global Geopolitical Landscape",
                "content": {
                    "text": (
                        "NAM has achieved monumental successes since 1961:\n\n"
                        "1. **Accelerated Global Decolonization:** Channeled diplomatic and financial aid to armed liberation movements, speeding the independence of Angola, Mozambique, Namibia, and Zimbabwe.\n"
                        "2. **Dismantling Apartheid in South Africa:** Used its massive voting power as an Afro-Asian bloc in the UN General Assembly to impose global arms embargoes and economic sanctions on the Pretoria regime.\n"
                        "3. **Cold War Superpower Conflict Mediation:** Because of their neutrality, NAM leaders served as trusted mediators during dangerous crises (e.g., Nehru and Nkrumah defusing the 1961 Berlin Crisis).\n"
                        "4. **Championing Nuclear Disarmament:** Successfully pushed for the creation of nuclear-weapon-free zones in Latin America (Treaty of Tlatelolco, 1967) and Africa (Pelindaba Treaty, 1996).\n"
                        "5. **Fostering South-South Cooperation:** Founded the **Group of 77 (G77)** in 1964 to coordinate collective economic bargaining for developing countries."
                    )
                }
            }
        ]
    },
    {
        "page_number": 11,
        "page_title": "Six Major Challenges Confronting NAM",
        "blocks": [
            {
                "block_type": "step_process",
                "component_type": "step_process",
                "title": "Structural and Political Obstacles to Non-Alignment",
                "content": {
                    "steps": [
                        "1. Severe Poverty and Economic Dependency: Many member states rely heavily on foreign loans, food aid, and military grants from the USA or Russia, making true foreign policy neutrality difficult.",
                        "2. Internal Political Instability and Civil Wars: Frequent military coups, ethnic clashes, and civil wars (e.g., DRC, Sudan, Rwanda) divert national resources away from collective NAM initiatives.",
                        "3. Bilateral Wars Between Member States: Destructive military conflicts between member nations (e.g., the 8-year Iran-Iraq War, border wars between Somalia-Ethiopia and Uganda-Tanzania) shattered solidarity.",
                        "4. Lack of Permanent Enforcement Machinery: Without a permanent secretariat, budget, or military force, NAM cannot enforce its resolutions or halt wars among members.",
                        "5. Hidden Ideological Alignments: Despite formal non-alignment, several members leaned heavily toward capitalism (e.g., Philippines, Kenya) or communism (e.g., Cuba, Vietnam), causing deep internal friction.",
                        "6. Post-Cold War Identity Crisis: Following the collapse of the Soviet Union in 1991, critics argued NAM lost its purpose in a unipolar world (though NAM remains vital for economic justice and resisting unilateral hegemony)."
                    ]
                }
            }
        ]
    },
    {
        "page_number": 12,
        "page_title": "Debating Modern Relevance: Does NAM Still Matter Today?",
        "blocks": [
            {
                "block_type": "concept_explanation",
                "component_type": "concept_explanation",
                "title": "The Vital Role of NAM in the 21st Century",
                "content": {
                    "text": (
                        "Despite the end of the Cold War, NAM remains profoundly relevant today across four critical dimensions:\n\n"
                        "- **Shield Against Unilateral Superpower Hegemony:** Provides a collective diplomatic counterweight against unilateral military interventions by global superpowers.\n"
                        "- **Champion for Global Economic Justice:** Leads negotiations inside the World Trade Organization (WTO) for fairer agricultural subsidies and intellectual property waivers for life-saving medicines.\n"
                        "- **Advocacy on Climate Justice:** Pushes developed nations (the historical polluters) to finance loss-and-damage funds for climate-vulnerable nations in Africa and small island states.\n"
                        "- **Reform of the UN Security Council:** Demands the democratization of the UN, insisting that Africa and Latin America receive permanent seats with veto rights."
                    )
                }
            }
        ]
    },
    {
        "page_number": 13,
        "page_title": "Interactive Classification Activity: NAM Architecture",
        "blocks": [
            {
                "block_type": "mini_activity",
                "component_type": "mini_activity",
                "title": "Identify Key Features of the Non-Aligned Movement",
                "content": {
                    "instruction": "Test your understanding of NAM history and administration. Match each item to its historical significance:",
                    "items": [
                        "1. 1955 Bandung Conference -> **Formulated the Ten Principles of Peaceful Coexistence**",
                        "2. 1961 Belgrade Summit -> **First official summit formally launching the Non-Aligned Movement**",
                        "3. Coordinating Bureau in New York -> **Coordinates daily voting alignments of NAM members inside the UN**",
                        "4. Rotational Chairmanship -> **Head of State hosting the triennial summit serves as executive chair for 3 years**",
                        "5. Group of 77 (G77) -> **Collective economic bargaining coalition of developing nations established in 1964**"
                    ]
                }
            }
        ]
    },
    {
        "page_number": 14,
        "page_title": "KCSE Examination Coaching: Challenges of NAM",
        "blocks": [
            {
                "block_type": "worked_example",
                "component_type": "worked_example",
                "title": "KCSE Question: Explain Five Challenges that Have Undermined the Performance of the Non-Aligned Movement (10 Marks)",
                "content": {
                    "text": (
                        "**Examiner's Marking Scheme (Point + Explanation + Evidence = 2 Marks per Point):**\n\n"
                        "1. **Severe Economic Dependency:** Widespread poverty forces member nations to depend on development aid and debt loans from superpowers, compromising their political independence. (2 marks)\n\n"
                        "2. **Internal Political Instability:** Recurring military coups and civil wars across member states disrupt governance and weaken commitment to collective foreign policy. (2 marks)\n\n"
                        "3. **Destructive Bilateral Conflicts:** Border disputes and military wars between member states (e.g., the Iran-Iraq War or Somalia-Ethiopia conflict) severely shattered organizational unity. (2 marks)\n\n"
                        "4. **Lack of Permanent Enforcement Machinery:** The movement lacks a permanent secretariat, written constitution, or military force to enforce resolutions or discipline aggressive members. (2 marks)\n\n"
                        "5. **Hidden Ideological Leanings:** Many members covertly aligned with either the Western capitalist or Eastern communist bloc, creating deep internal ideological distrust. (2 marks)"
                    )
                }
            }
        ]
    },
    {
        "page_number": 15,
        "page_title": "Check Your Understanding: Module 2.6",
        "blocks": [
            {
                "block_type": "knowledge_check",
                "component_type": "knowledge_check",
                "title": "Module 2.6 Assessment",
                "content": {
                    "questions": [
                        {
                            "question": "In which Indonesian city was the landmark 1955 Asian-African Conference held that laid the foundations of NAM?",
                            "options": [
                                "Jakarta",
                                "Bandung",
                                "Surabaya",
                                "Bali"
                            ],
                            "correct_answer": 1,
                            "explanation": "The 1955 Bandung Conference united 29 Afro-Asian nations and established the core principles of non-alignment."
                        },
                        {
                            "question": "Why did the founders of NAM deliberately decide NOT to establish a permanent headquarters or secretariat?",
                            "options": [
                                "To avoid high construction costs in developing nations",
                                "To prevent any single wealthy member or superpower from dominating the movement",
                                "Because the United Nations forbade them from having an office",
                                "Due to a lack of trained diplomats in Asia and Africa"
                            ],
                            "correct_answer": 1,
                            "explanation": "Operating without a permanent headquarters prevented institutional hegemony and preserved sovereign equality through rotational chairmanship."
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
                "title": "Core Summary: The Non-Aligned Movement",
                "content": {
                    "text": (
                        "• **Origins:** Conceived at Bandung (1955), formally launched at Belgrade (1961) under Nehru, Tito, Nasser, and Nkrumah.\n"
                        "• **6 Objectives:** Sovereignty protection, anti-colonialism/apartheid, rejecting military pacts, nuclear disarmament, combating neo-colonialism, and establishing NIEO.\n"
                        "• **Unique Architecture:** No permanent HQ, rotational triennial chair, New York Coordinating Bureau, consensus decision-making.\n"
                        "• **Key Achievements:** Accelerated decolonization, dismantled apartheid through UN embargoes, mediated Cold War crises, and formed G77.\n"
                        "• **Core Challenges:** Aid dependency on superpowers, civil wars, bilateral wars (Iran-Iraq), lack of enforcement army, and post-Cold War identity challenges."
                    )
                }
            },
            {
                "block_type": "key_takeaway",
                "component_type": "key_takeaway",
                "title": "Key Takeaways",
                "content": {
                    "text": (
                        "- Non-alignment was an active strategy of foreign policy independence, not passive isolationism.\n"
                        "- Today, NAM remains a critical collective voice for developing nations fighting for economic equity and climate justice."
                    )
                }
            }
        ]
    }
]

LESSON_7_PAGES = [
    {
        "page_number": 1,
        "page_title": "The Cold War: Superpower Rivalry (1945–1991)",
        "blocks": [
            {
                "block_type": "learning_goal",
                "component_type": "learning_goal",
                "title": "Lesson Objectives: The Cold War",
                "content": {
                    "text": (
                        "By the end of this lesson, you will be able to:\n"
                        "- Define the Cold War and understand the non-military mechanisms of superpower conflict\n"
                        "- Analyze the 7 major root causes of the geopolitical confrontation between the USA and USSR\n"
                        "- Trace the major proxy theatres of war across Europe, Asia, Latin America, and Africa\n"
                        "- Explain the factors that led to détente and the eventual collapse of the Soviet Union in 1991\n"
                        "- Evaluate the 6 profound, long-lasting political and economic consequences of the Cold War on Africa"
                    )
                }
            },
            {
                "block_type": "definition_card",
                "component_type": "definition_card",
                "title": "Definition: The Cold War",
                "content": {
                    "term": "The Cold War",
                    "definition": (
                        "The intense state of ideological, political, economic, and military rivalry that existed between the Western capitalist bloc "
                        "(led by the United States and NATO) and the Eastern communist bloc (led by the Soviet Union and the Warsaw Pact) between 1945 and 1991, "
                        "waged through proxy wars, espionage, arms races, economic blockades, and propaganda without direct military combat between the superpowers."
                    )
                }
            }
        ]
    },
    {
        "page_number": 2,
        "page_title": "Why Was It Called a 'Cold' War? (Non-Military Weapons)",
        "blocks": [
            {
                "block_type": "concept_explanation",
                "component_type": "concept_explanation",
                "title": "The Arsenal of Cold Warfare: Fighting Without Direct Combat",
                "content": {
                    "text": (
                        "Because both superpowers possessed massive nuclear arsenals capable of **Mutually Assured Destruction (MAD)**, direct armed combat was avoided. Instead, the war was fought through five indirect instruments:\n\n"
                        "1. **Ideological Propaganda:** Worldwide media campaigns promoting democracy and capitalism while demonizing communism, and vice versa.\n"
                        "2. **Proxy Wars:** Superpowers financing, arming, and training opposing sides in localized civil wars across the Third World (Korea, Vietnam, Angola, Ethiopia).\n"
                        "3. **Nuclear & Conventional Arms Race:** Massive competitive stockpiling of intercontinental ballistic missiles (ICBMs), nuclear submarines, and supersonic bombers.\n"
                        "4. **Espionage and Secret Intelligence:** Covert operations, assassinations, and intelligence gathering led by the **CIA** (USA) and the **KGB** (USSR).\n"
                        "5. **Economic Warfare and Space Race:** Financial blockades, trade embargoes, and competition in satellite technology and lunar landings (e.g., Apollo vs. Sputnik)."
                    )
                }
            }
        ]
    },
    {
        "page_number": 3,
        "page_title": "The Seven Major Causes of the Cold War",
        "blocks": [
            {
                "block_type": "step_process",
                "component_type": "step_process",
                "title": "The Root Causes of Superpower Hostility",
                "content": {
                    "steps": [
                        "1. Deep Ideological Clash: Democratic Capitalism (private property, free markets, individual liberties) vs. Soviet Communism (state command economy, elimination of private ownership, one-party rule).",
                        "2. Disarmament Breakdown: Following the 1945 US atomic bombings of Japan, superpowers failed to agree on a joint nuclear control plan, triggering a nuclear arms race.",
                        "3. Disagreement over Post-War Germany: The West wanted a reconstructed, prosperous Germany to anchor European recovery; Stalin demanded a permanently crippled Germany to prevent future Russian invasions.",
                        "4. The Soviet 'Iron Curtain' in Eastern Europe: The Red Army occupied Eastern Europe (Poland, East Germany, Romania, Hungary, Bulgaria, Czechoslovakia), installing puppet communist satellite regimes.",
                        "5. Truman Doctrine and Marshall Plan (1947): President Truman pledged US military aid to resist communism (Truman Doctrine) and poured $13 billion to rebuild Western Europe (Marshall Plan). The USSR countered with COMECON.",
                        "6. Antagonistic Military Alliances: Formation of NATO in April 1949 by the West, countered by the Soviet Warsaw Pact in May 1955, dividing Europe into armed camps.",
                        "7. Soviet Veto Abuse in the UN: The USSR repeatedly vetoed Western-backed peace resolutions in the Security Council, turning the UN into a Cold War propaganda battleground."
                    ]
                }
            }
        ]
    },
    {
        "page_number": 4,
        "page_title": "Superpower Diplomacy: Kennedy and Khrushchev in Vienna",
        "blocks": [
            {
                "block_type": "suggested_image",
                "component_type": "suggested_image",
                "title": "US President John F. Kennedy and Soviet Premier Nikita Khrushchev (1961)",
                "content": {
                    "text": "US President John F. Kennedy and Soviet Premier Nikita Khrushchev meet during the tense Vienna Summit in June 1961, illustrating the personal diplomacy of the Cold War.",
                    "url": "https://upload.wikimedia.org/wikipedia/commons/7/7e/John_Kennedy%2C_Nikita_Khrushchev_1961.jpg",
                    "author": "US National Archives / Public Domain",
                    "licensing": "Public Domain",
                    "commons_page_url": "https://commons.wikimedia.org/wiki/File:John_Kennedy,_Nikita_Khrushchev_1961.jpg"
                }
            }
        ]
    },
    {
        "page_number": 5,
        "page_title": "Proxy Theatre 1: Europe (Berlin Blockade and the Berlin Wall)",
        "blocks": [
            {
                "block_type": "concept_explanation",
                "component_type": "concept_explanation",
                "title": "Divided Germany: The Epicenter of European Tension",
                "content": {
                    "text": (
                        "Germany and its capital Berlin were partitioned into four allied zones, creating two hostile states in 1949: capitalist **West Germany (FRG)** and communist **East Germany (GDR)**.\n\n"
                        "- **The Berlin Blockade & Airlift (1948–1949):** Stalin cut off all road, rail, and canal routes into West Berlin to starve the city into surrender. The Western Allies launched the historic **Berlin Airlift**, flying in over 2.3 million tons of food, fuel, and medicine for 11 months until Stalin lifted the blockade in May 1949.\n"
                        "- **The Berlin Wall (1961):** To stop millions of skilled East Germans from fleeing to the prosperous capitalist West, the communist regime erected a concrete wall dividing Berlin overnight in August 1961. The Berlin Wall stood as the physical symbol of the Iron Curtain until its historic fall on **9 November 1989**."
                    )
                }
            }
        ]
    },
    {
        "page_number": 6,
        "page_title": "Proxy Theatre 2: Asia (Korea and Vietnam)",
        "blocks": [
            {
                "block_type": "comparison_table",
                "component_type": "comparison_table",
                "title": "Superpower Proxy Wars in Asia",
                "content": {
                    "headers": ["Conflict", "Years", "Opposing Blocs & Leaders", "Superpower Role & Outcome"],
                    "rows": [
                        ["The Korean War", "1950–1953", "Communist North Korea (Kim Il-sung) vs. Capitalist South Korea (Syngman Rhee)", "USSR and China backed North Korea; USA and a UN-authorized coalition led by General Douglas MacArthur defended South Korea. Ended in a stalemate at the 38th parallel, leaving Korea divided to this day."],
                        ["The Vietnam War", "1955–1975", "Communist North Vietnam & Viet Cong (Ho Chi Minh) vs. Capitalist South Vietnam (Ngo Dinh Diem)", "USSR and China provided heavy weapons and funds; USA deployed over 500,000 troops and launched massive bombing campaigns. The US suffered defeat, withdrawing in 1973; Vietnam unified under a communist government in 1975."]
                    ]
                }
            }
        ]
    },
    {
        "page_number": 7,
        "page_title": "Proxy Theatre 3: Latin America (The Cuban Missile Crisis)",
        "blocks": [
            {
                "block_type": "concept_explanation",
                "component_type": "concept_explanation",
                "title": "October 1962: 13 Days on the Brink of Nuclear Holocaust",
                "content": {
                    "text": (
                        "The most dangerous confrontation in human history unfolded 90 miles off the coast of Florida:\n\n"
                        "- **Background:** In 1959, socialist revolutionary **Fidel Castro** overthrew the US-backed Batista regime in Cuba. Following the failed US-backed Bay of Pigs invasion (1961), Castro allied with the Soviet Union.\n"
                        "- **The Discovery:** In October 1962, US U-2 spy planes photographed Soviet nuclear missile launch pads under construction in Cuba, capable of striking major American cities in minutes.\n"
                        "- **The Crisis:** President **John F. Kennedy** ordered a strict naval 'quarantine' (blockade) of Cuba, warning that any missile launch would trigger full nuclear retaliation against the USSR.\n"
                        "- **The Resolution:** After 13 tense days, Soviet Premier **Nikita Khrushchev** agreed to dismantle and withdraw the missiles in exchange for a US public pledge not to invade Cuba and a secret agreement to remove US missiles from Turkey."
                    )
                }
            }
        ]
    },
    {
        "page_number": 8,
        "page_title": "Documentary Video: The Cuban Missile Crisis",
        "blocks": [
            {
                "block_type": "suggested_video",
                "component_type": "suggested_video",
                "title": "Historical Documentary: The Cuban Missile Crisis (1962)",
                "content": {
                    "url": "https://www.youtube.com/watch?v=bwWW3sbk4EU",
                    "text": "Examine authentic declassified archival recordings and military footage documenting the 13 days of the Cuban Missile Crisis when the world stood on the edge of global thermonuclear war.",
                    "author": "Historical Archives / Cold War Documentary",
                    "licensing": "Standard YouTube License"
                }
            }
        ]
    },
    {
        "page_number": 9,
        "page_title": "Proxy Theatre 4: Africa (Angola and Ethiopia)",
        "blocks": [
            {
                "block_type": "concept_explanation",
                "component_type": "concept_explanation",
                "title": "Cold War Battlegrounds in the Horn and Southern Africa",
                "content": {
                    "text": (
                        "Superpowers actively turned African post-independence transitions into brutal proxy conflicts:\n\n"
                        "- **The Angolan Civil War (1975–2002):** Following independence from Portugal, a brutal war erupted. The Soviet Union and Cuba poured thousands of troops and heavy weapons to back the Marxist **MPLA** government in Luanda. The United States and apartheid South Africa financed and armed **Jonas Savimbi's UNITA** rebels, devastating Angola for nearly three decades.\n"
                        "- **The Horn of Africa (Ethiopia & Somalia):** In 1974, socialist military officer **Mengistu Haile Mariam** overthrew Emperor Haile Selassie in Ethiopia, establishing the communist *Derg* regime backed by Soviet arms. When Somalia invaded the Ogaden in 1977, the USSR switched sides to heavily arm Ethiopia, sparking decades of regional instability."
                    )
                }
            }
        ]
    },
    {
        "page_number": 10,
        "page_title": "The Road to Détente: Disarmament Treaties",
        "blocks": [
            {
                "block_type": "comparison_table",
                "component_type": "comparison_table",
                "title": "Key Treaties Limiting the Nuclear Arms Race",
                "content": {
                    "headers": ["Treaty Name", "Year Signed", "Signatory Powers", "Strategic Agreement"],
                    "rows": [
                        ["Partial Nuclear Test Ban Treaty (PTBT)", "1963", "USA, USSR, UK", "Banned all nuclear weapons test detonations in the atmosphere, outer space, and underwater (permitting only underground tests)."],
                        ["Nuclear Non-Proliferation Treaty (NPT)", "1968", "Global multilateral treaty", "Prohibited nuclear-armed states from transferring weapons technology to non-nuclear states and promoted peaceful atomic energy."],
                        ["Strategic Arms Limitation Talks (SALT I)", "1972", "USA (Nixon) & USSR (Brezhnev)", "Froze the number of strategic ballistic missile launchers and restricted Anti-Ballistic Missile (ABM) defense systems."],
                        ["Helsinki Accords", "1975", "35 nations (USA, USSR, Europe)", "Recognized post-WWII European borders and committed Eastern bloc states to respect fundamental human rights."]
                    ]
                }
            }
        ]
    },
    {
        "page_number": 11,
        "page_title": "Five Factors Leading to the Collapse of the Cold War",
        "blocks": [
            {
                "block_type": "step_process",
                "component_type": "step_process",
                "title": "The Fall of the Soviet Empire (1985–1991)",
                "content": {
                    "steps": [
                        "1. Mikhail Gorbachev's Reforms (1985): Introduced Glasnost (freedom of speech and political transparency) and Perestroika (economic restructuring away from strict state control).",
                        "2. Severe Economic Bankruptcy of the USSR: Massive military spending (competing with US President Reagan's 'Star Wars' missile defense) and economic stagnation crippled the Soviet economy.",
                        "3. Disastrous Soviet Invasion of Afghanistan (1979–1989): Known as the 'Soviet Vietnam', costing thousands of lives and billions of dollars against US-backed Mujahideen fighters.",
                        "4. Fall of the Berlin Wall and Revolutions of 1989: Peaceful democratic uprisings swept across Poland, Hungary, East Germany, Romania, and Bulgaria, dismantling communist satellite regimes.",
                        "5. Disintegration of the Soviet Union (December 1991): Secession of 15 constituent republics (Ukraine, Belarus, Kazakhstan, Baltic states) formally dissolved the USSR, ending the Cold War."
                    ]
                }
            }
        ]
    },
    {
        "page_number": 12,
        "page_title": "Impact on Africa 1: Proliferation of Small Arms and Civil Wars",
        "blocks": [
            {
                "block_type": "concept_explanation",
                "component_type": "concept_explanation",
                "title": "Militarizing African Conflicts with Superpower Hardware",
                "content": {
                    "text": (
                        "- The USA and USSR flooded Africa with millions of automatic rifles (AK-47s, M16s), landmines, and artillery to arm competing political factions.\n"
                        "- These weapons outlasted the Cold War, fueling banditry, cattle rustling, and devastating multi-decade civil wars in **Angola, Mozambique, Somalia, Chad, and Sudan**.\n"
                        "- Millions of unexploded landmines in Angola and Mozambique continue to maim rural farmers decades after hostilities ended."
                    )
                }
            }
        ]
    },
    {
        "page_number": 13,
        "page_title": "Impact on Africa 2: Propping Up Brutal Dictatorships",
        "blocks": [
            {
                "block_type": "concept_explanation",
                "component_type": "concept_explanation",
                "title": "Shielding Tyrants in Exchange for Ideological Loyalty",
                "content": {
                    "text": (
                        "- Both superpowers actively protected and financed corrupt, oppressive, and undemocratic African dictators simply because they pledged allegiance to Washington or Moscow:\n"
                        "  - **Mobutu Sese Seko of Zaire (DRC):** Embezzled billions from national coffers but received uncritical US financial and military backing as an anti-communist bulwark.\n"
                        "  - **Mengistu Haile Mariam of Ethiopia:** Carried out the brutal 'Red Terror' killing thousands of political opponents, shielded by Soviet military aid and Cuban advisors."
                    )
                }
            }
        ]
    },
    {
        "page_number": 14,
        "page_title": "Impact on Africa 3: Severe Economic Devastation and Famine",
        "blocks": [
            {
                "block_type": "concept_explanation",
                "component_type": "concept_explanation",
                "title": "Destruction of Infrastructure and Displaced Populations",
                "content": {
                    "text": (
                        "- Proxy warfare obliterated critical bridges, trunk railways, electricity grids, and agricultural plantations across war-torn nations.\n"
                        "- Disrupted agricultural planting cycles, triggering catastrophic famines (e.g., the devastating 1984–1985 Ethiopian famine).\n"
                        "- Created over **10 million displaced refugees** across the Horn of Africa, Great Lakes, and Southern Africa."
                    )
                }
            }
        ]
    },
    {
        "page_number": 15,
        "page_title": "Impact on Africa 4: Marginalization and Aid Conditionality",
        "blocks": [
            {
                "block_type": "concept_explanation",
                "component_type": "concept_explanation",
                "title": "The Post-1991 Vacuum and Western Political Demands",
                "content": {
                    "text": (
                        "- **Loss of Strategic Leverage:** Following the Soviet collapse in 1991, African states could no longer play superpowers against each other to secure easy loans.\n"
                        "- **Sudden Aid Withdrawals & State Collapse:** Sudden cuts in foreign subsidies led to total governmental breakdown in fragile nations (e.g., the complete collapse of the central state in Somalia in 1991).\n"
                        "- **Introduction of Political Conditionality:** Western nations and financial institutions (World Bank, IMF) began making aid strictly conditional on multi-party democracy, human rights, and anti-corruption reforms."
                    )
                }
            }
        ]
    },
    {
        "page_number": 16,
        "page_title": "Impact on Africa 5: Acceleration of Liberation Struggles",
        "blocks": [
            {
                "block_type": "concept_explanation",
                "component_type": "concept_explanation",
                "title": "Eastern Bloc Assistance to Freedom Fighters",
                "content": {
                    "text": (
                        "- On the positive side, African liberation movements capitalized on Cold War rivalry to secure vital military hardware, guerrilla training, and academic scholarships from the USSR, China, and Cuba.\n"
                        "- Freedom fighters in **Mozambique (FRELIMO), Angola (MPLA), Zimbabwe (ZANU/ZAPU), Namibia (SWAPO), and South Africa (ANC)** utilized Soviet weapons and training to defeat entrenched European colonial rule and apartheid."
                    )
                }
            }
        ]
    },
    {
        "page_number": 17,
        "page_title": "KCSE Examination Coaching: Cold War Effects on Africa",
        "blocks": [
            {
                "block_type": "worked_example",
                "component_type": "worked_example",
                "title": "KCSE Question: Explain Five Political and Economic Effects of the Cold War on the African Continent (10 Marks)",
                "content": {
                    "text": (
                        "**Examiner's Marking Scheme (Point + Explanation + Evidence = 2 Marks per Point):**\n\n"
                        "1. **Proliferation of Small Arms and Civil Wars:** Superpowers flooded Africa with automatic weapons to back opposing factions, causing multi-decade civil wars in Angola, Mozambique, and Somalia. (2 marks)\n\n"
                        "2. **Entrenchment of Oppressive Dictatorships:** Corrupt tyrants like Mobutu in Zaire and Mengistu in Ethiopia were kept in power through foreign military aid in exchange for ideological loyalty. (2 marks)\n\n"
                        "3. **Severe Economic Ruin and Famine:** Destruction of agricultural lands, roads, and railways caused catastrophic economic collapse and triggered massive refugee crises. (2 marks)\n\n"
                        "4. **Introduction of Political Aid Conditionality:** Following the Soviet collapse, Western donors began tying development aid to multi-party democracy and human rights reforms. (2 marks)\n\n"
                        "5. **Acceleration of Anti-Colonial Liberation Struggles:** Nationalist movements in Southern Africa secured weapons, training, and scholarships from the USSR and China to dismantle colonial rule. (2 marks)"
                    )
                }
            }
        ]
    },
    {
        "page_number": 18,
        "page_title": "Topic 2 Mastery Checklist & Comprehensive Summary",
        "blocks": [
            {
                "block_type": "knowledge_check",
                "component_type": "knowledge_check",
                "title": "Topic 2 Comprehensive Mastery Check",
                "content": {
                    "questions": [
                        {
                            "question": "Which reform policy introduced by Mikhail Gorbachev in 1985 promoted political openness and freedom of speech in the USSR?",
                            "options": [
                                "Perestroika",
                                "Glasnost",
                                "COMECON",
                                "Détente"
                            ],
                            "correct_answer": 1,
                            "explanation": "Glasnost (Openness) permitted public debate, freedom of expression, and political criticism in the Soviet Union."
                        },
                        {
                            "question": "Which Cold War confrontation in October 1962 brought the USA and USSR closest to direct nuclear warfare?",
                            "options": [
                                "The Berlin Blockade",
                                "The Cuban Missile Crisis",
                                "The Korean War",
                                "The Suez Canal Crisis"
                            ],
                            "correct_answer": 1,
                            "explanation": "The 13-day Cuban Missile Crisis over Soviet nuclear installations in Cuba was the most dangerous moment of the Cold War."
                        }
                    ]
                }
            },
            {
                "block_type": "summary",
                "component_type": "summary",
                "title": "Topic 2 Master Summary: International Relations",
                "content": {
                    "text": (
                        "• **Module 1 (Basics):** 4 Forms (Economic, Diplomatic, Political, Cultural); 5 Benefits (Peace, Collective Action, Trade, Aid, Integration).\n"
                        "• **Module 2 (IGOs vs NGOs):** IGOs created by states via treaties (UN, AU); NGOs created by private civil society (Red Cross, Amnesty).\n"
                        "• **Module 3 (League of Nations):** Founded 1920 in Geneva; failed due to lack of army, no US membership, appeasement, and unanimity flaw.\n"
                        "• **Module 4 (United Nations):** Founded 24 Oct 1945; 6 Principal Organs (GA, SC, ECOSOC, Trusteeship, Secretariat, ICJ); 8 Specialized Agencies; P5 Veto Power.\n"
                        "• **Module 5 (Commonwealth):** Voluntary association of 56 nations; symbolic head is British Monarch; consensus-based CHOGM; scholarships & CFTC.\n"
                        "• **Module 6 (NAM):** Bandung (1955) to Belgrade (1961); Nehru, Tito, Nasser, Nkrumah; no permanent HQ, rotational chair, active neutrality.\n"
                        "• **Module 7 (Cold War):** USA vs USSR (1945–1991); proxy wars in Berlin, Korea, Vietnam, Cuba, Angola; collapsed via Gorbachev's reforms; profound impact on African security and governance."
                    )
                }
            }
        ]
    }
]


ALL_LESSONS = [
    {
        "unit_order": 1,
        "unit_name": "International Relations — Meaning, Benefits, and Forms",
        "lesson_title": "Meaning, Forms, and Benefits of International Relations",
        "pages": LESSON_1_PAGES
    },
    {
        "unit_order": 2,
        "unit_name": "International Organizations — IGOs and NGOs",
        "lesson_title": "International Organizations: IGOs and NGOs",
        "pages": LESSON_2_PAGES
    },
    {
        "unit_order": 3,
        "unit_name": "The League of Nations — Origins, Organs, Achievements, and Collapse",
        "lesson_title": "The League of Nations: Origins, Achievements, and Collapse",
        "pages": LESSON_3_PAGES
    },
    {
        "unit_order": 4,
        "unit_name": "The United Nations Organization (UN) — Structure, Impact, and Challenges",
        "lesson_title": "The United Nations Organization: Structure, Impact, and Challenges",
        "pages": LESSON_4_PAGES
    },
    {
        "unit_order": 5,
        "unit_name": "The Commonwealth of Nations — Evolution, Organs, and Impact",
        "lesson_title": "The Commonwealth of Nations: Evolution, Impact, and Dynamics",
        "pages": LESSON_5_PAGES
    },
    {
        "unit_order": 6,
        "unit_name": "The Non-Aligned Movement (NAM) — Active Neutrality and Global Role",
        "lesson_title": "The Non-Aligned Movement: Active Neutrality and Global Role",
        "pages": LESSON_6_PAGES
    },
    {
        "unit_order": 7,
        "unit_name": "The Cold War — Superpower Rivalry, Proxy Theatres, and Impact on Africa",
        "lesson_title": "The Cold War: Superpower Rivalry, Proxy Theatres, and African Impact",
        "pages": LESSON_7_PAGES
    }
]


# ===========================================================================
# DATABASE INGESTION RUNNER
# ===========================================================================

def run_ingestion(replace=False):
    print("=" * 80)
    print("VLEARN CURRICULUM INGESTION: FORM 4 HISTORY — TOPIC 2 (INTERNATIONAL RELATIONS)")
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
            name="International Relations",
            defaults={"order": 2}
        )
        if topic_created:
            print(f"[+] Created Topic: {topic.name} (Order: {topic.order})")
        else:
            topic.order = 2
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
        print(f"[SUCCESS] Form 4 History Topic 2 Ingestion Complete!")
        print(f"[*] Total Lessons Ingested: {len(ALL_LESSONS)}")
        print(f"[*] Total Pages Ingested:   {total_pages}")
        print(f"[*] Total Blocks Ingested:  {total_blocks}")
        print(f"[*] Total Media Assets:     {total_assets}")
        print("=" * 80)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Ingest Form 4 History Topic 2")
    parser.add_argument("--replace", action="store_true", help="Replace existing blocks with a fresh rebuild")
    args = parser.parse_args()

    run_ingestion(replace=args.replace)
