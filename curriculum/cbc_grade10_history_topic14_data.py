"""
VLearn CBC Grade 10 History — Topic 14: Modern Slavery and Servitude
Authoritative Pedagogical Data Definitions (Lessons 1 to 4)
"""

from curriculum.cbc_grade10_history_topic14_svgs import (
    SVG_TAXONOMY_MODERN_SLAVERY,
    SVG_FOUR_PS_FRAMEWORK
)

TOPIC_14_LESSONS = [
    # =========================================================================
    # LESSON 1: Defining Modern Slavery and Its Forms
    # =========================================================================
    {
        "unit_order": 1,
        "unit_name": "Defining Modern Slavery and Its Forms",
        "unit_description": "Distinguishing historical chattel slavery from modern slavery and servitude, the taxonomy of exploitation (forced labor, debt bondage, trafficking, child/forced marriage).",
        "lesson_title": "Defining Modern Slavery and Its Forms",
        "pages": [
            # Card 1: Orientation & Hook
            [
                {
                    "type": "suggested_image",
                    "title": "Human Dignity and the Global Fight Against Modern Slavery",
                    "content": {
                        "title": "United Nations Human Rights Demonstration",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e7/Human_rights_protest.jpg/800px-Human_rights_protest.jpg",
                        "caption": "Human rights advocates demonstrating against forced labor and human trafficking, demanding strict enforcement of universal anti-slavery laws.",
                        "author": "Wikimedia Commons",
                        "licensing": "CC BY-SA 2.0"
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "The Persistence of Exploitation in the Modern World",
                    "content": {
                        "text": (
                            "In previous history topics, we explored how **chattel slavery**—a codified legal system where human beings were owned as property—was legally abolished worldwide during the 19th century.\n\n"
                            "However, legal abolition did not automatically eliminate the underlying dynamics of exploitation.\n\n"
                            "Today, in the 21st century, **modern slavery** refers to illegal situations where a person is coerced, deceived, or forced into labor or marriage that they cannot refuse or leave due to violence, debt manipulation, or abuse of power."
                        )
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 1 Learning Goals",
                    "content": {
                        "text": (
                            "By the end of this lesson, you will be able to:\n\n"
                            "- Differentiate between historical chattel slavery and modern illegal slavery\n"
                            "- Define the core forms: forced labor, debt bondage, human trafficking, child slavery, and servitude\n"
                            "- Identify how exploiters use informal debt and document confiscation to trap victims"
                        )
                    }
                }
            ],

            # Card 2: Taxonomy Diagram SVG
            [
                {
                    "type": "suggested_diagram",
                    "title": "Taxonomy of Modern Slavery and Servitude",
                    "content": {
                        "title": "Dimensions of Modern Exploitation",
                        "caption": "Classification model categorizing Modern Slavery into Forced Labor, Debt Bondage, Human Trafficking, Child/Forced Marriage, and Servitude.",
                        "svg_content": SVG_TAXONOMY_MODERN_SLAVERY
                    }
                }
            ],

            # Card 3: Historical vs Modern Comparison
            [
                {
                    "type": "comparison_table",
                    "title": "Comparative Analysis: Historical Chattel Slavery vs Modern Slavery",
                    "content": {
                        "headers": ["Dimension", "Historical Chattel Slavery (16th–19th Century)", "Modern Slavery (21st Century)"],
                        "rows": [
                            ["Legal Status", "Formally legal and protected by national and imperial property laws", "Strictly illegal under national constitutions and international conventions"],
                            ["Method of Control", "Legal deeds of ownership, public auctions, and state-backed physical chains", "Clandestine coercion, psychological threats, confiscated passports, and debt traps"],
                            ["Economic Structure", "Mainstream, open pillar of trans-Atlantic and colonial economies", "Hidden in shadow economies, informal subcontracting, and unregulated labor sectors"],
                            ["Global Abolition Focus", "Passing abolition laws to eliminate the legal status of human property", "Enforcing existing laws, eradicating corruption, auditing supply chains, and poverty alleviation"]
                        ]
                    }
                }
            ],

            # Card 4: Video Case Study
            [
                {
                    "type": "suggested_video",
                    "title": "Understanding Modern Slavery and Human Trafficking",
                    "content": {
                        "title": "The Reality of Modern Slavery Today",
                        "description": "Educational documentary examining the global scale of modern forced labor, human trafficking, and international abolitionist efforts.",
                        "youtube_id": "kY31WnS8jXk"
                    }
                }
            ],

            # Card 5: Knowledge Check & Misconceptions
            [
                {
                    "type": "common_misconception",
                    "title": "Misconception vs Reality: Modern Existence",
                    "content": {
                        "misconception": "Because slavery was outlawed in the 1800s, it no longer exists anywhere in the world today.",
                        "reality": "While legal ownership was abolished, illegal modern slavery persists in shadow sectors, affecting an estimated 50 million people through debt traps, human trafficking, and forced labor."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check: Chattel vs Modern Slavery",
                    "content": {
                        "question": "What is the fundamental distinction between historical chattel slavery and modern slavery?",
                        "options": [
                            "A. Historical slavery was completely non-violent, while modern slavery is strictly military.",
                            "B. Historical chattel slavery was a legally codified institution of human ownership, whereas modern slavery is illegal but enforced through coercion, debt traps, and deception.",
                            "C. Historical slavery occurred only in factories, while modern slavery is confined to agriculture.",
                            "D. Historical slavery was voluntary, whereas modern slavery is fully funded by the state."
                        ],
                        "correct_answer": "B",
                        "explanation": "Chattel slavery was legally recognized human ownership. Modern slavery is a clandestine, illegal crime driven by debt manipulation and coercion."
                    }
                }
            ]
        ]
    },

    # =========================================================================
    # LESSON 2: Causes and Consequences
    # =========================================================================
    {
        "unit_order": 2,
        "unit_name": "Causes and Consequences",
        "unit_description": "Multi-causal architecture: poverty, corruption, conflict, global supply chains, survivor testimonies of debt bondage, and intergenerational poverty.",
        "lesson_title": "Causes and Consequences",
        "pages": [
            # Card 1: Orientation & Hook
            [
                {
                    "type": "suggested_image",
                    "title": "Informal Labor and Supply Chain Vulnerabilities",
                    "content": {
                        "title": "Informal Brick Kiln and Manual Labor",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/53/Brick_kiln_workers.jpg/800px-Brick_kiln_workers.jpg",
                        "caption": "Manual brick kiln operations in unregulated sectors where vulnerable families often fall victim to debt bondage and document confiscation.",
                        "author": "Wikimedia Commons",
                        "licensing": "CC BY-SA 3.0"
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "The Multi-Causal Architecture of Modern Exploitation",
                    "content": {
                        "text": (
                            "Modern slavery does not happen in isolation. It is driven by intersecting vulnerabilities:\n\n"
                            "- **Poverty & Shocks:** Families without savings take informal loans during droughts or medical crises, falling into debt traps.\n"
                            "- **Corruption & Weak Enforcement:** Corrupt officials or lack of labor inspectors allow traffickers to operate.\n"
                            "- **Global Supply Chain Pressures:** Consumer demand for cheap clothes and tech pressures factories to cut labor costs through forced labor."
                        )
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 2 Learning Goals",
                    "content": {
                        "text": (
                            "By the end of this lesson, you will be able to:\n\n"
                            "- Analyze the root causes that leave individuals vulnerable to exploitation\n"
                            "- Evaluate primary survivor testimonies documenting debt bondage tactics\n"
                            "- Trace the systemic economic and social consequences of modern servitude"
                        )
                    }
                }
            ],

            # Card 2: Causes and Effects Matrix
            [
                {
                    "type": "comparison_table",
                    "title": "Structural Causes vs. Systemic Consequences of Modern Slavery",
                    "content": {
                        "headers": ["Structural Driver (Cause)", "Mechanism of Exploitation", "Systemic Impact (Consequence)"],
                        "rows": [
                            ["Extreme Household Poverty", "Unregulated loan advances for emergencies (medical bills, crop failure)", "Intergenerational debt bondage where children inherit manufactured debts"],
                            ["Systemic Corruption", "Bribing border police, labor inspectors, and forging travel papers", "Impunity for criminal trafficking cartels and breakdown of the rule of law"],
                            ["Global Consumer Demand", "Relentless corporate cost-cutting in garments, agriculture, and mining", "Suppression of legitimate local wages and economic underdevelopment"],
                            ["War & Climate Displacement", "Refugees and IDPs lacking legal citizenship or formal work permits", "Severe psychological trauma, loss of human dignity, and civic alienation"]
                        ]
                    }
                }
            ],

            # Card 3: Survivor Source Analysis
            [
                {
                    "type": "concept_explanation",
                    "title": "Primary Source Analysis: Survivor Testimony on Debt Bondage",
                    "content": {
                        "text": (
                            "> *'The recruiter came to our village when our crops failed. He offered us an advance of 15,000 shillings to pay for my daughter's urgent medical treatment in exchange for working at his brick kiln. Once we arrived, he took our national ID cards 'for safekeeping.' He charged us daily fees for our mud hut, water, and tools. At the end of three months, he showed us a ledger claiming we now owed 30,000 shillings due to living costs and interest. We were trapped by armed guards and police threats.'*\n\n"
                            "**Historical Source Analysis:**\n"
                            "- **Coercion Tactics:** Confiscation of identity cards eliminates physical and legal mobility.\n"
                            "- **Debt Manipulation:** Arbitrary charges for basic necessities guarantee the manufactured debt can never be repaid with labor."
                        )
                    }
                }
            ],

            # Card 4: Video Case Study
            [
                {
                    "type": "suggested_video",
                    "title": "Debt Bondage and Human Rights in the Global Economy",
                    "content": {
                        "title": "How Debt Bondage Traps Workers in the Modern Era",
                        "description": "Investigative documentary analyzing how illegal debt manipulation and unregulated advance payments operate in global industries.",
                        "youtube_id": "F3_6mF-yvR0"
                    }
                }
            ],

            # Card 5: Knowledge Check
            [
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check: Debt Bondage Manipulation",
                    "content": {
                        "question": "Based on the survivor testimony, how did the exploiter manipulate the debt to ensure the family could not leave?",
                        "options": [
                            "A. By obtaining a certified order from a national high court.",
                            "B. By confiscating identity documents and charging arbitrary fees for basic living necessities, inflating the debt.",
                            "C. By offering the family corporate ownership shares in the brick factory.",
                            "D. By paying high wages and deducting official government income taxes."
                        ],
                        "correct_answer": "B",
                        "explanation": "Confiscating ID documents removes legal mobility while charging arbitrary fees for housing and tools ensures the debt grows faster than labor can pay off."
                    }
                }
            ]
        ]
    },

    # =========================================================================
    # LESSON 3: Government, Civil Society, and Abolitionist Action
    # =========================================================================
    {
        "unit_order": 3,
        "unit_name": "Government, Civil Society, and Abolitionist Action",
        "unit_description": "The '4Ps' Anti-Slavery Framework (Prevention, Protection, Prosecution, Partnership), ethical consumerism, and safe citizen reporting guidelines.",
        "lesson_title": "Government, Civil Society, and Abolitionist Action",
        "pages": [
            # Card 1: Orientation & Hook
            [
                {
                    "type": "suggested_image",
                    "title": "Abolitionist Action from the 19th Century to Today",
                    "content": {
                        "title": "Abolitionist Movement Legacy",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Official_medallion_of_the_British_Anti-Slavery_Society_%281795%29.jpg/800px-Official_medallion_of_the_British_Anti-Slavery_Society_%281795%29.jpg",
                        "caption": "Historical medallion of the British Anti-Slavery Society (1795) with the motto 'Am I Not a Man and a Brother?'—a legacy continuing in modern civil society alliances.",
                        "author": "Wikimedia Commons",
                        "licensing": "Public Domain"
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "The Modern Abolitionist Coalition",
                    "content": {
                        "text": (
                            "In the 18th and 19th centuries, abolitionist movements mobilized petitions, legal challenges, and public awareness to outlaw chattel slavery.\n\n"
                            "Today, modern abolitionists—governments, international bodies, and civil society organizations (CSOs)—work together under the **'4Ps' Framework**: **Prevention**, **Protection**, **Prosecution**, and **Partnership** to eradicate human exploitation."
                        )
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 3 Learning Goals",
                    "content": {
                        "text": (
                            "By the end of this lesson, you will be able to:\n\n"
                            "- Explain the four pillars of the international '4Ps' Anti-Slavery Framework\n"
                            "- Practice ethical consumerism by researching supply chain certifications\n"
                            "- Apply safe reporting protocols when encountering suspected community exploitation"
                        )
                    }
                }
            ],

            # Card 2: 4Ps Framework SVG Diagram
            [
                {
                    "type": "suggested_diagram",
                    "title": "The '4Ps' Anti-Slavery Framework",
                    "content": {
                        "title": "International Anti-Trafficking Framework",
                        "caption": "Comprehensive architecture showing how Prevention, Protection, Prosecution, and Partnership combine to dismantle modern slavery networks.",
                        "svg_content": SVG_FOUR_PS_FRAMEWORK
                    }
                }
            ],

            # Card 3: Safe Civic Advocacy & Consumer Ethics
            [
                {
                    "type": "concept_explanation",
                    "title": "Ethical Consumerism and Student Safety Rules",
                    "content": {
                        "text": (
                            "**How Citizens Drive Change:**\n"
                            "1. **Ethical Consumerism:** Support brands that certify fair wages and audit their global supply chains (e.g. Fair Trade certification for cocoa and tea).\n"
                            "2. **Public Awareness:** Educate peers on digital recruitment scams offering fraudulent jobs abroad.\n\n"
                            "⚠️ **Critical Student Safety Protocol:**\n"
                            "Learners must **NEVER** attempt to investigate or confront suspected traffickers directly. Doing so is highly dangerous. Always report concerns anonymously to official law enforcement or designated national child protection hotlines."
                        )
                    }
                }
            ],

            # Card 4: Video Case Study
            [
                {
                    "type": "suggested_video",
                    "title": "Civil Society and Modern Abolitionist Movements",
                    "content": {
                        "title": "Fighting Human Trafficking Through the 4Ps",
                        "description": "Documentary exploring how international police, NGOs, and citizen reporting coordinate to rescue survivors and prosecute human traffickers.",
                        "youtube_id": "78K3fQ94_7Y"
                    }
                }
            ],

            # Card 5: Knowledge Check
            [
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check: Safe Citizen Reporting",
                    "content": {
                        "question": "What is the safest and most effective way for a student to address a suspected case of modern exploitation in their community?",
                        "options": [
                            "A. Conducting an undercover investigation to confront the suspects personally.",
                            "B. Blockading the premises with a group of student activists.",
                            "C. Recording details privately and reporting directly and anonymously to official law enforcement or an authorized child helpline.",
                            "D. Ignoring the situation because modern slavery is only a global issue."
                        ],
                        "correct_answer": "C",
                        "explanation": "Student safety is paramount; reporting through official child protection hotlines or police ensures trained investigators handle criminal syndicates safely."
                    }
                }
            ]
        ]
    },

    # =========================================================================
    # LESSON 4: Evidence and Ethical Citizenship
    # =========================================================================
    {
        "unit_order": 4,
        "unit_name": "Evidence and Ethical Citizenship",
        "unit_description": "Historical evidence literacy: evaluating statistical reports, legal statutes (UN Palermo Protocol), survivor testimonies, literary sources, and unit-end synthesis assessment.",
        "lesson_title": "Evidence and Ethical Citizenship",
        "pages": [
            # Card 1: Orientation & Hook
            [
                {
                    "type": "suggested_image",
                    "title": "Evaluating Human Rights Evidence and Legal Charters",
                    "content": {
                        "title": "International Labour Organization (ILO) Headquarters, Geneva",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/90/ILO_Geneva.jpg/800px-ILO_Geneva.jpg",
                        "caption": "The International Labour Organization (ILO) in Geneva, which collects global statistical data and establishes binding conventions against forced labor.",
                        "author": "Wikimedia Commons",
                        "licensing": "CC BY-SA 3.0"
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Evidence-Based Historical Inquiry into Human Rights",
                    "content": {
                        "text": (
                            "When investigating sensitive issues like modern servitude, ethical historians must avoid sensationalism or unverified claims.\n\n"
                            "We use **evidence-based inquiry**: cross-referencing statistical reports (ILO), legal statutes (Palermo Protocol), survivor testimonies, and creative literature to construct balanced, accurate historical arguments."
                        )
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 4 Learning Goals",
                    "content": {
                        "text": (
                            "By the end of this lesson, you will be able to:\n\n"
                            "- Evaluate the strengths and limitations of different source categories (statistical, legal, survivor, literary)\n"
                            "- Analyze the Palermo Protocol's 3-part definition of human trafficking (Act, Means, Purpose)\n"
                            "- Complete the Unit Assessment on Modern Slavery and Servitude"
                        )
                    }
                }
            ],

            # Card 2: Source Evaluation Table
            [
                {
                    "type": "comparison_table",
                    "title": "Evaluating Source Categories in Human Rights Research",
                    "content": {
                        "headers": ["Source Category", "Typical Examples", "Primary Strengths", "Major Limitations"],
                        "rows": [
                            ["Statistical Reports", "UN, ILO, and Global Slavery Index databases", "Provides objective global/regional scale, trends, and measurable data", "May undercount clandestine, underground criminal operations"],
                            ["Legal Statutes", "National penal codes, UN Palermo Protocol (2000)", "Defines precise enforceable boundaries and statutory duties", "Reflects the law as written, not how effectively it is enforced"],
                            ["Survivor Testimonies", "First-hand court depositions and NGO interviews", "Offers authentic human insight into lived experiences and coercion", "Represents specific individual cases; cannot prove total industry trends"],
                            ["Creative Literature", "Poetry ('Chains Unseen'), protest songs, documentaries", "Builds empathy, moral reflection, and public awareness", "Subjective and emotional; lacks empirical data and dates"]
                        ]
                    }
                }
            ],

            # Card 3: Source Workshop (UN Palermo Protocol 2000)
            [
                {
                    "type": "concept_explanation",
                    "title": "Primary Source Analysis: UN Palermo Protocol (Article 3)",
                    "content": {
                        "text": (
                            "> *'Trafficking in persons shall mean the recruitment, transportation, transfer, harboring or receipt of persons, by means of the threat or use of force or other forms of coercion, of abduction, of fraud, of deception, of the abuse of power or of a position of vulnerability... for the purpose of exploitation.'*\n\n"
                            "**The 3-Part Legal Triad of Human Trafficking:**\n"
                            "1. **The Act:** What is done (recruitment, transportation, harboring)\n"
                            "2. **The Means:** How it is done (force, fraud, deception, abuse of vulnerability)\n"
                            "3. **The Purpose:** Why it is done (forced labor, servitude, commercial exploitation)"
                        )
                    }
                }
            ],

            # Card 4: Video Case Study
            [
                {
                    "type": "suggested_video",
                    "title": "Historical Source Criticism and Modern Human Rights Inquiry",
                    "content": {
                        "title": "Analyzing Human Rights Evidence and Testimonies",
                        "description": "Educational video guiding students on evaluating historical sources, corroborating testimonies with statistical data, and practicing ethical citizenship.",
                        "youtube_id": "2r1o5Xb1pQk"
                    }
                }
            ],

            # Card 5: Knowledge Check & Unit Assessment
            [
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 1: Source Corroboration",
                    "content": {
                        "question": "Why must a history researcher corroborate creative literary sources with statistical reports from the ILO when investigating modern slavery?",
                        "options": [
                            "A. Because poems are completely invalid for historical research.",
                            "B. To balance emotional empathy with empirical, objective data on the actual scale and economic sectors of exploitation.",
                            "C. Because international courts only accept numerical data.",
                            "D. To prove that modern slavery only exists in poetry."
                        ],
                        "correct_answer": "B",
                        "explanation": "Corroborating creative literature with ILO statistical reports ensures the historical narrative combines human empathy with verified empirical data."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 2: 4Ps Protection Pillar",
                    "content": {
                        "question": "In the '4Ps' Anti-Slavery Framework, which pillar focuses on providing survivors with emergency shelters, counseling, and legal assistance?",
                        "options": [
                            "A. Prevention",
                            "B. Protection",
                            "C. Prosecution",
                            "D. Partnership"
                        ],
                        "correct_answer": "B",
                        "explanation": "The Protection pillar centers on survivor welfare: safe shelter, medical and mental health care, and legal aid to empower rehabilitation."
                    }
                }
            ]
        ]
    }
]
