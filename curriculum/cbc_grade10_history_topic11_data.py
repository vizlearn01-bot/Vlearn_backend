"""
VLearn CBC Grade 10 History — Topic 11: Global Governance and the Role of the UN
Authoritative Pedagogical Data Definitions (Lessons 1 to 4)
"""

from curriculum.cbc_grade10_history_topic11_svgs import (
    SVG_WORLD_GOV_VS_GLOBAL_GOV,
    SVG_MONTREAL_PROTOCOL_TIMELINE,
    SVG_UNSC_VETO_FLOW,
    SVG_GLOBAL_CITIZENSHIP_WHEEL
)

TOPIC_11_LESSONS = [
    # =========================================================================
    # LESSON 1: Meaning and Principles of Global Governance
    # =========================================================================
    {
        "unit_order": 1,
        "unit_name": "Meaning and Principles of Global Governance",
        "unit_description": "Conceptual definitions distinguishing global governance from a world government, historical evolution post-1945, and the six foundational principles of multilateralism.",
        "lesson_title": "Meaning and Principles of Global Governance",
        "pages": [
            # Card 1: Orientation & Hook
            [
                {
                    "type": "suggested_image",
                    "title": "A Borderless, Interconnected World",
                    "content": {
                        "title": "Global Interconnection and Digital Governance",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/22/Earth_Western_Hemisphere_transparent_background.png/800px-Earth_Western_Hemisphere_transparent_background.png",
                        "caption": "Our shared planet: environmental crises, pandemics, and trade networks cross national boundaries without stopping at borders, requiring cooperative global management.",
                        "author": "Wikimedia Commons",
                        "licensing": "Public Domain"
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Solving Borderless Crises in a World of Sovereign Nations",
                    "content": {
                        "text": (
                            "How do we solve a crisis when no single country has the power to fix it alone?\n\n"
                            "If a pandemic spreads across the globe, or if carbon emissions alter global weather patterns, there is no 'World President' or 'Global Police Force' to force everyone to comply. Instead, sovereign nations must cooperate.\n\n"
                            "This cooperative, rules-based architecture is called **global governance**."
                        )
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 1 Learning Goals",
                    "content": {
                        "text": (
                            "By the end of this lesson, you will be able to:\n\n"
                            "- Differentiate between **global governance** and a **world government**\n"
                            "- Explain how the devastation of WWI and WWII catalyzed international institutional cooperation\n"
                            "- Analyze the six core principles of global governance: multilateralism, rule of law, accountability, transparency, equity, and sustainability\n"
                            "- Evaluate the tension between absolute national sovereignty and collective action"
                        )
                    }
                }
            ],

            # Card 2: World Gov vs Global Gov Diagram
            [
                {
                    "type": "suggested_diagram",
                    "title": "World Government vs Global Governance",
                    "content": {
                        "title": "Structural Comparison Matrix",
                        "caption": "Comparison of a hypothetical coercive world government hierarchy vs the actual decentralized multilateral network of sovereign equal states.",
                        "svg_content": SVG_WORLD_GOV_VS_GLOBAL_GOV
                    }
                }
            ],

            # Card 3: Six Core Principles Table
            [
                {
                    "type": "comparison_table",
                    "title": "The Six Guiding Principles of Global Governance",
                    "content": {
                        "headers": ["Guiding Principle", "Core Definition", "Real-World Application"],
                        "rows": [
                            ["Multilateralism", "Multiple nations cooperating to solve shared problems rather than acting unilaterally", "UN World Health Organization coordinating global vaccine tracking"],
                            ["Rule of Law", "Adherence to international conventions, treaties, and human rights charters", "Geneva Conventions governing humanitarian conduct during conflicts"],
                            ["Accountability", "Holding international actors and multinational corporations liable for commitments", "Paris Agreement reporting frameworks on national carbon emission reductions"],
                            ["Transparency", "Open, verifiable data-sharing to build mutual trust among sovereign states", "International Atomic Energy Agency (IAEA) nuclear inspections"],
                            ["Equity", "Fair resource distribution and decision-making power for developing nations", "UN Equalisation and climate adaptation funding for vulnerable Global South nations"],
                            ["Sustainability", "Meeting present global economic needs without destroying future generations", "UN Sustainable Development Goals (SDGs) 2030 agenda"]
                        ]
                    }
                }
            ],

            # Card 4: Critical Thinking Lab
            [
                {
                    "type": "concept_explanation",
                    "title": "Critical Thinking Lab: Sovereignty vs Environmental Transboundary Spillover",
                    "content": {
                        "text": (
                            "**Inquiry Scenario:**\n"
                            "> *Imagine Country A dumps untreated industrial toxic waste into a major transboundary river that flows directly into Country B, poisoning Country B's municipal water supply and decimating agricultural irrigation. Country A claims that as a sovereign nation, it has the absolute domestic right to manage its own factories without foreign interference.*\n\n"
                            "**Guiding Questions:**\n"
                            "1. How does this scenario prove that unchecked domestic sovereignty is insufficient to protect human rights in a borderless ecosystem?\n"
                            "2. Which principle of global governance (Rule of Law, Multilateralism, or Equity) provides the legal framework to hold Country A accountable?"
                        )
                    }
                }
            ],

            # Card 5: Media Analysis
            [
                {
                    "type": "suggested_video",
                    "title": "Introduction to Global Governance and International Cooperation",
                    "content": {
                        "title": "How Global Governance Coordinates Sovereign States",
                        "description": "Educational video exploring the structure of international treaties, multilateral diplomacy, and the preservation of national sovereignty.",
                        "youtube_id": "zJg5c1p8tW4"
                    }
                }
            ],

            # Card 6: Knowledge Check
            [
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check: World Gov vs Global Governance",
                    "content": {
                        "question": "Which of the following statements best describes the difference between a world government and global governance?",
                        "options": [
                            "A. A world government relies on voluntary treaties, whereas global governance has a global military to enforce laws.",
                            "B. A world government is a centralized sovereign authority over all states, whereas global governance is a decentralized, cooperative network of sovereign states.",
                            "C. A world government is run exclusively by private companies, while global governance is led by regional kings.",
                            "D. There is no difference; both terms mean the complete elimination of individual national constitutions."
                        ],
                        "correct_answer": "B",
                        "explanation": "Global governance preserves national sovereignty through decentralized, voluntary treaties and multilateral consensus, whereas a world government would be a centralized hierarchy."
                    }
                }
            ]
        ]
    },

    # =========================================================================
    # LESSON 2: Areas and Importance of Global Governance
    # =========================================================================
    {
        "unit_order": 2,
        "unit_name": "Areas and Importance of Global Governance",
        "unit_description": "Six critical sectors of global governance, borderless challenges, and the landmark case study of the 1987 Montreal Protocol on Ozone Layer recovery.",
        "lesson_title": "Areas and Importance of Global Governance",
        "pages": [
            # Card 1: Orientation & Hook
            [
                {
                    "type": "suggested_image",
                    "title": "The United Nations General Assembly in Session",
                    "content": {
                        "title": "UN General Assembly Hall, New York",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/05/UN_General_Assembly_hall.jpg/800px-UN_General_Assembly_hall.jpg",
                        "caption": "The UN General Assembly Hall where all 193 sovereign member states convene annually with equal voting rights to debate borderless challenges.",
                        "author": "Wikimedia Commons",
                        "licensing": "CC BY-SA 3.0"
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Six Critical Arenas of Global Action",
                    "content": {
                        "text": (
                            "From climate change and pandemic containment to international trade and cyberwarfare, global governance coordinates action across six key areas:\n\n"
                            "1. **Peace and Security:** Conflict mediation and peacekeeping missions\n"
                            "2. **Human Rights:** Setting universal standards through the UDHR\n"
                            "3. **Environmental Protection:** Treaties to protect the atmosphere, oceans, and biodiversity\n"
                            "4. **Economic Development:** Financial stability and trade regulations (IMF, World Bank, WTO)\n"
                            "5. **Global Health:** Pandemic tracking and disease eradication (WHO)\n"
                            "6. **Cybersecurity & AI:** Digital safety standards and transboundary data protection"
                        )
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 2 Learning Goals",
                    "content": {
                        "text": (
                            "By the end of this lesson, you will be able to:\n\n"
                            "- Identify the primary international mechanisms governing each of the six global sectors\n"
                            "- Analyze the landmark Montreal Protocol (1987) as a historical triumph of multilateralism\n"
                            "- Compare the ozone recovery success with the complexity of modern climate change agreements"
                        )
                    }
                }
            ],

            # Card 2: Montreal Protocol Timeline Diagram
            [
                {
                    "type": "suggested_diagram",
                    "title": "Timeline of Global Environmental Action: The Montreal Protocol",
                    "content": {
                        "title": "Montreal Protocol (1985–2060)",
                        "caption": "Timeline illustrating how scientific discovery led to 100% universal treaty ratification, a 98% drop in CFC emissions, and projected full recovery by 2060.",
                        "svg_content": SVG_MONTREAL_PROTOCOL_TIMELINE
                    }
                }
            ],

            # Card 3: Case Study Deep Dive
            [
                {
                    "type": "concept_explanation",
                    "title": "Case Study Analysis: The 1987 Montreal Protocol",
                    "content": {
                        "text": (
                            "In the 1980s, atmospheric scientists discovered that synthetic chemicals called **chlorofluorocarbons (CFCs)**—used in aerosol sprays and refrigerators—were eroding Earth's stratospheric ozone layer, exposing life to dangerous solar UV radiation.\n\n"
                            "**The Multilateral Response:**\n"
                            "- In 1987, 197 nations ratified the **Montreal Protocol**, making it the first universally signed treaty in UN history.\n"
                            "- Developing nations were provided financial and technological assistance through a dedicated Multilateral Fund to transition to ozone-safe alternatives.\n"
                            "- **Outcome:** Global CFC production dropped by over 98%, putting the ozone layer on course for complete restoration by 2060."
                        )
                    }
                }
            ],

            # Card 4: Video Case Study
            [
                {
                    "type": "suggested_video",
                    "title": "Multilateral Diplomacy and Global Environmental Treaties",
                    "content": {
                        "title": "How the World Fixed the Ozone Layer",
                        "description": "Historical documentary analyzing the political negotiations and scientific consensus behind the Montreal Protocol.",
                        "youtube_id": "2X_2IdriMTc"
                    }
                }
            ],

            # Card 5: Knowledge Check
            [
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check: Borderless Challenges",
                    "content": {
                        "question": "Why do borderless challenges like pandemics and global climate change make global governance indispensable?",
                        "options": [
                            "A. Because international agencies have the legal power to rewrite national constitutions automatically.",
                            "B. Because these threats cross borders and cannot be solved by any single nation acting unilaterally.",
                            "C. Because global treaties eliminate all financial costs of scientific research.",
                            "D. Because global governance guarantees all nations will always agree unanimously on economic policy."
                        ],
                        "correct_answer": "B",
                        "explanation": "Transnational threats do not stop at national borders; no nation can insulate itself from ecological disruption or virus spread without multilateral data-sharing and cooperation."
                    }
                }
            ]
        ]
    },

    # =========================================================================
    # LESSON 3: Emerging Issues and the UN Role
    # =========================================================================
    {
        "unit_order": 3,
        "unit_name": "Emerging Issues and the UN Role",
        "unit_description": "Organisational structure of the UN, the Security Council Veto mechanism, emerging 21st-century issues (AI, cybersecurity, climate), and institutional opportunities vs limitations.",
        "lesson_title": "Emerging Issues and the UN Role",
        "pages": [
            # Card 1: Orientation & Hook
            [
                {
                    "type": "suggested_image",
                    "title": "The United Nations Emblem and Global Peace",
                    "content": {
                        "title": "Official Emblem of the United Nations",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/Flag_of_the_United_Nations.svg/800px-Flag_of_the_United_Nations.svg.png",
                        "caption": "The UN flag featuring a polar azimuthal world map encircled by olive branches, symbolizing the worldwide quest for peace and multilateral solidarity.",
                        "author": "Wikimedia Commons",
                        "licensing": "Public Domain"
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "The UN in the 21st Century: Promise and Paralysis",
                    "content": {
                        "text": (
                            "Founded in 1945 by 51 nations after World War II, the United Nations now includes 193 member states.\n\n"
                            "While the UN has eradicated diseases, mediated ceasefires, and protected millions of refugees, it faces intense modern scrutiny: Why does the **Security Council Veto** often paralyze response during major wars? How does the UN balance **Article 2(7) non-intervention** with universal human rights protection?"
                        )
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 3 Learning Goals",
                    "content": {
                        "text": (
                            "By the end of this lesson, you will be able to:\n\n"
                            "- Explain the functions of the UN General Assembly, Security Council, and Secretariat\n"
                            "- Analyze how the **Permanent Five (P5) Veto power** operates and why it causes diplomatic bottlenecks\n"
                            "- Evaluate emerging global challenges including AI ethics, cyberwarfare, and climate migration\n"
                            "- Weigh the UN's humanitarian achievements against its structural constraints"
                        )
                    }
                }
            ],

            # Card 2: Security Council Veto Decision Flow SVG
            [
                {
                    "type": "suggested_diagram",
                    "title": "UN Security Council: Decision-Flow and the Veto Mechanism",
                    "content": {
                        "title": "Security Council Voting Architecture",
                        "caption": "Diagram depicting how a single negative vote from any of the P5 members (US, UK, France, Russia, China) defeats a resolution, versus consensus adoption under Chapter VII.",
                        "svg_content": SVG_UNSC_VETO_FLOW
                    }
                }
            ],

            # Card 3: Opportunities vs Limitations Table
            [
                {
                    "type": "comparison_table",
                    "title": "Evaluating the United Nations: Achievements vs Structural Constraints",
                    "content": {
                        "headers": ["Dimension", "Major Institutional Strengths", "Structural Limitations & Challenges"],
                        "rows": [
                            ["Peace & Security", "Over 70 peacekeeping missions deployed; decoupled warring factions", "P5 Veto power paralyzes action when permanent members have geopolitical stakes"],
                            ["Human Rights", "Codified the Universal Declaration of Human Rights (UDHR) into international law", "Article 2(7) restricts direct intervention in domestic sovereign jurisdictions"],
                            ["Humanitarian Relief", "Agencies like WFP, UNHCR, and UNICEF feed and shelter millions daily", "Relies entirely on voluntary donor funding and voluntary troop contributions"],
                            ["Global Rule of Law", "International Court of Justice (ICJ) arbitrates interstate disputes", "Lacks a standing enforcement military to compel compliance if a power refuses ruling"]
                        ]
                    }
                }
            ],

            # Card 4: Video Case Study
            [
                {
                    "type": "suggested_video",
                    "title": "The United Nations: Structure, Veto Power, and Reform",
                    "content": {
                        "title": "How the UN Works and Why Reform is Debated",
                        "description": "Educational documentary examining the historical origins of the UN Charter, the P5 veto mechanism, and African demands for Security Council reform.",
                        "youtube_id": "8YQ7Yx0bFMo"
                    }
                }
            ],

            # Card 5: Knowledge Check
            [
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check: Security Council Veto Power",
                    "content": {
                        "question": "Which of the following is a primary structural limitation that frequently paralyzes the UN Security Council during major international crises?",
                        "options": [
                            "A. The General Assembly holds absolute authority to veto all Security Council resolutions.",
                            "B. Each of the five permanent members (P5) holds absolute veto power, allowing any one of them to block resolutions that conflict with their interests.",
                            "C. The UN is funded by private corporations that dictate military decisions.",
                            "D. The UN Charter requires all 193 member states to vote with 100% unanimity."
                        ],
                        "correct_answer": "B",
                        "explanation": "Under the UN Charter, if any single permanent member (US, Russia, China, France, UK) votes 'No', the resolution is defeated, regardless of majority support."
                    }
                }
            ]
        ]
    },

    # =========================================================================
    # LESSON 4: Promoting Responsible Global Citizenship
    # =========================================================================
    {
        "unit_order": 4,
        "unit_name": "Promoting Responsible Global Citizenship",
        "unit_description": "Expanding citizenship beyond national borders, the Global Citizenship Action Wheel (environmental, human rights, digital integrity, intercultural dialogue), and evidence-based essay inquiry.",
        "lesson_title": "Promoting Responsible Global Citizenship",
        "pages": [
            # Card 1: Orientation & Hook
            [
                {
                    "type": "suggested_image",
                    "title": "Youth Environmental Action and Global Stewardship",
                    "content": {
                        "title": "Youth Community Tree Planting and Climate Action",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c5/Community_tree_planting_Kenya.jpg/800px-Community_tree_planting_Kenya.jpg",
                        "caption": "Young volunteers planting indigenous seedlings in Kenya, demonstrating how local community action directly supports global environmental sustainability.",
                        "author": "Wikimedia Commons",
                        "licensing": "CC BY-SA 4.0"
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Expanding Citizenship Beyond Borders",
                    "content": {
                        "text": (
                            "Being a **global citizen** does not mean giving up your national identity or patriotism. Instead, it is an ethical perspective recognizing that:\n\n"
                            "- Our local choices (what we buy, how we consume energy, what we share online) have direct global consequences\n"
                            "- Universal human rights belong to every person regardless of nationality\n"
                            "- Active citizens have a duty to promote peace, environmental sustainability, and digital integrity locally and globally"
                        )
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 4 Learning Goals",
                    "content": {
                        "text": (
                            "By the end of this lesson, you will be able to:\n\n"
                            "- Define responsible global citizenship and connect local actions to global goals\n"
                            "- Apply the four quadrants of the Global Citizenship Action Wheel\n"
                            "- Analyze slogans and poetry of international interdependence\n"
                            "- Construct an evidence-grounded essay on the future of multilateral global governance"
                        )
                    }
                }
            ],

            # Card 2: Global Citizenship Action Wheel SVG
            [
                {
                    "type": "suggested_diagram",
                    "title": "The Global Citizenship Action Wheel",
                    "content": {
                        "title": "Four Practical Action Quadrants",
                        "caption": "Diagram linking Environmental Stewardship, Human Rights Advocacy, Digital Integrity, and Intercultural Dialogue into daily civic life.",
                        "svg_content": SVG_GLOBAL_CITIZENSHIP_WHEEL
                    }
                }
            ],

            # Card 3: Source Analysis (Poem of Interdependence)
            [
                {
                    "type": "concept_explanation",
                    "title": "Primary Source Analysis: The Slogan of Interdependence",
                    "content": {
                        "text": (
                            "> *'Across the lands, a common thread,*\n"
                            "> *Global voices, words unsaid.*\n"
                            "> *From rising seas to borders wide,*\n"
                            "> *Together we stand, side by side.*\n"
                            "> *For governance strong, and futures bright,*\n"
                            "> *We build our world, with guiding light.'*\n\n"
                            "**Civic Interpretation:**\n"
                            "- **Core Message:** Emphasizes that shared global challenges ('rising seas') cannot be solved in isolation; they require collaborative action ('side by side') anchored in robust multilateral institutions."
                        )
                    }
                },
                {
                    "type": "mini_activity",
                    "title": "Slogan Creation Activity",
                    "content": {
                        "task": "Create a 6-word civic slogan promoting global environmental cooperation or digital integrity in your school. Explain its relevance in 2 sentences."
                    }
                }
            ],

            # Card 4: Video Case Study
            [
                {
                    "type": "suggested_video",
                    "title": "Youth Leadership, Sustainable Development, and Global Citizenship",
                    "content": {
                        "title": "Young Leaders Driving Global Change",
                        "description": "Educational documentary examining how grassroots youth movements advance the UN Sustainable Development Goals worldwide.",
                        "youtube_id": "alJaltUmrGo"
                    }
                }
            ],

            # Card 5: Knowledge Check & Cumulative Essay
            [
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check: Practical Global Citizenship",
                    "content": {
                        "question": "Which of the following actions demonstrates practical global citizenship at the local level?",
                        "options": [
                            "A. Refusing to interact with people from other cultural or linguistic backgrounds.",
                            "B. Practicing ethical consumerism, planting trees, and fact-checking online news before sharing to combat disinformation.",
                            "C. Demanding that your government unilaterally cancel all international treaties and climate pacts.",
                            "D. Ignoring environmental issues under the belief that only the UN Security Council can act."
                        ],
                        "correct_answer": "B",
                        "explanation": "Global citizenship starts with individual daily responsibility: ethical consumption, environmental care, and combating digital disinformation at home."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Topic-End Synthesis Essay Challenge",
                    "content": {
                        "text": (
                            "**Essay Prompt:**\n"
                            "> *'Evaluate the effectiveness of global governance in solving 21st-century borderless crises. Define global governance, distinguish it from a world government, and contrast the success of the Montreal Protocol with current challenges in climate change and Security Council veto deadlock.'*\n\n"
                            "**Essay Scaffolding:** Structure your argument into Introduction (definition & thesis), Body 1 (Montreal success vs Paris climate complexity), Body 2 (UNSC Veto structural bottlenecks), and Conclusion (responsible global citizenship)."
                        )
                    }
                }
            ]
        ]
    }
]
