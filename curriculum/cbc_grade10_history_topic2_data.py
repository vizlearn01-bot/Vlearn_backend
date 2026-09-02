"""
VLearn CBC Grade 10 History — Topic 2: Establishment of Colonial Rule
Full Structured Lesson Card Definitions (Lessons 1 to 5)
"""

from curriculum.cbc_grade10_history_topic2_svgs import (
    SVG_IMPERIALISM_CAUSES_CONSEQUENCES,
    SVG_ECONOMIC_COERCION_CYCLE,
    SVG_UGANDA_RAILWAY_MAP,
    SVG_COLONIAL_CONSOLIDATION_TIMELINE,
    SVG_COLLABORATION_RESISTANCE_MATRIX,
    SVG_PRECOLONIAL_VS_COLONIAL_COMPARISON
)

TOPIC_2_LESSONS = [
    # =========================================================================
    # LESSON 1: Why Britain Established Colonial Rule
    # =========================================================================
    {
        "unit_order": 1,
        "unit_name": "Why Britain Established Colonial Rule",
        "unit_description": "Economic, strategic, and ideological motives behind British imperialism and the partition of East Africa.",
        "lesson_title": "Why Britain Established Colonial Rule",
        "pages": [
            # Page 1: Orientation & Historical Spark
            [
                {
                    "type": "learning_goal",
                    "title": "Module 1.2.1 Learning Outcomes",
                    "content": {
                        "text": (
                            "By the end of this lesson, you will be able to:\n\n"
                            "- Explain the economic, strategic, and ideological motives driving British colonization of Kenya\n"
                            "- Analyze the role of the 1884–1885 Berlin Conference and the Scramble for Africa in East African partition\n"
                            "- Evaluate the strategic importance of the Nile River Basin and Indian Ocean maritime routes\n"
                            "- Interrogate a 1895 British primary parliamentary source to detect imperial bias and justifications"
                        )
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Historical Context: The Imperial Scramble for Africa",
                    "content": {
                        "text": (
                            "In the late 19th century, Western European powers underwent an unprecedented surge of industrialization. "
                            "Factories in Britain demanded immense volumes of agricultural raw materials and minerals, while producing an excess of manufactured goods that outstripped domestic European markets.\n\n"
                            "This intense economic competition, combined with aggressive national prestige and military rivalries, catalyzed the **'Scramble for Africa'**. "
                            "At the **Berlin Conference (1884–1885)**, European nations convened without a single African representative to carve up the continent into recognized spheres of influence. "
                            "Britain laid claim to East Africa, formalizing its direct imperial takeover on **1 July 1895** by declaring the **East Africa Protectorate**."
                        )
                    }
                },
                {
                    "type": "suggested_image",
                    "title": "The Berlin Conference and Imperial Partition",
                    "content": {
                        "title": "Caricature of Imperial Partition at the Berlin Conference (1884–1885)",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/9/93/Cartoon_depicting_Leopold_2_and_other_emperial_powers_at_Berlin_conference_1884.jpg",
                        "caption": "A famous 19th-century political cartoon depicting European imperial powers carving up the African continent like a cake during the Berlin Conference, highlighting the arbitrary division of African lands.",
                        "author": "Wikimedia Commons",
                        "licensing": "Public Domain"
                    }
                }
            ],

            # Page 2: Strategic Geopolitics (The Nile & Indian Ocean)
            [
                {
                    "type": "definition_card",
                    "title": "Strategic Imperialism",
                    "content": {
                        "term": "Strategic Motive",
                        "definition": "A geopolitical or military rationale for acquiring territory to protect existing high-value empire assets, control critical waterways, and deny territorial advantages to imperial rivals."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Securing the Nile Lifeline and Indian Ocean Sea Lanes",
                    "content": {
                        "text": (
                            "Britain's geopolitical calculations in East Africa centered heavily on strategic security:\n\n"
                            "- **Control of the River Nile:** Britain had occupied Egypt in 1882 to control the Suez Canal—the maritime gateway to India. Because Egypt's agricultural economy and survival depended entirely on the annual floods of the Nile, British military planners believed that whoever controlled the headwaters of the Nile at Lake Victoria held Egypt's life in their hands. Securing Kenya and Uganda was therefore deemed vital to safeguard the Nile's source.\n"
                            "- **Indian Ocean Maritime Security:** The Kenyan coastline possessed natural deep-water ports, particularly at **Mombasa (Kilindini Harbour)**. Mombasa provided an essential naval and refueling base along the Indian Ocean shipping lanes linking Britain to India, its prized imperial possession.\n"
                            "- **Pre-empting European Competitors:** Britain acted swiftly to prevent its imperial rivals, notably **Imperial Germany** (which established German East Africa / Tanganyika) and **France**, from establishing naval bases or territorial control across the East African interior."
                        )
                    }
                },
                {
                    "type": "common_misconception",
                    "title": "Misconception: Kenya Was Colonized for Mineral Wealth",
                    "content": {
                        "misconception": "Britain colonized Kenya primarily because it discovered large gold and diamond deposits in the 1890s.",
                        "reality": "Unlike South Africa or the Congo, Kenya had no known major precious mineral deposits in the late 19th century. Britain's initial driving motives were overridingly **strategic** (protecting the Nile Basin and the route to India) and **geopolitical** (blocking German expansion in East Africa)."
                    }
                }
            ],

            # Page 3: Economic and Ideological Motives
            [
                {
                    "type": "comparison_table",
                    "title": "The Tripartite Motives of British Imperialism in Kenya",
                    "content": {
                        "headers": ["Imperial Motive Category", "Key Drivers in Kenya", "Historical Mechanism & Policy"],
                        "rows": [
                            [
                                "Strategic & Military",
                                "Control of Nile River source (Lake Victoria) & Indian Ocean trade routes to India",
                                "Declared East Africa Protectorate (1895) and built Uganda Railway to move troops rapidly"
                            ],
                            [
                                "Economic & Commercial",
                                "Demand for industrial raw materials (cotton, rubber, tea) and captive consumer markets",
                                "Encouraged White Settler agriculture, alienated fertile highlands, and imposed cash taxes"
                            ],
                            [
                                "Ideological & Religious",
                                "Paternalistic 'Civilizing Mission' and evangelical Christian expansion",
                                "Sponsored missionary societies (CMS) who built Western mission schools and clinics"
                            ]
                        ]
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Industrial Capitalism and the 'Civilizing Mission'",
                    "content": {
                        "text": (
                            "**Economic Imperatives:** Industrialization in Britain generated substantial surplus capital. British financiers sought high-yield investments in colonial infrastructure—such as railways, telegraphs, and commercial plantations—where cheap land and low African labor costs promised massive profit margins.\n\n"
                            "**The Ideological 'Civilizing Mission':** British imperialists justified their conquest through the ethnocentric philosophy of paternalism, popularized by Rudyard Kipling as the 'White Man's Burden'. They argued that it was Britain's moral duty to introduce Western education, modern medicine, British common law, and Christianity to African societies, conveniently masking the violent exploitation of land and labor."
                        )
                    }
                },
                {
                    "type": "suggested_image",
                    "title": "Pioneering Missionary Activity in East Africa",
                    "content": {
                        "title": "Johann Ludwig Krapf, CMS Missionary in East Africa",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/e/e1/Johann_Ludwig_Krapf.jpg",
                        "caption": "Johann Ludwig Krapf (Church Missionary Society), who established the first Christian mission station in Kenya at Rabai in 1844 and translated the Bible into Swahili, representing the religious dimension of European entry.",
                        "author": "Wikimedia Commons",
                        "licensing": "Public Domain"
                    }
                }
            ],

            # Page 4: Visualizing Imperial Causes & Consequences
            [
                {
                    "type": "suggested_diagram",
                    "title": "Causes and Consequences of British Imperialism in East Africa",
                    "content": {
                        "title": "Causal Flow of British Imperial Conquest in East Africa",
                        "caption": "Vector flow diagram illustrating the structural link between European industrialization, strategic Nile river geopolitics, the Berlin Conference, and the consequential loss of Kenyan sovereignty.",
                        "svg_content": SVG_IMPERIALISM_CAUSES_CONSEQUENCES
                    }
                },
                {
                    "type": "step_process",
                    "title": "The 4-Stage Imperial Escalation in Kenya",
                    "content": {
                        "intro": "The subjugation of Kenyan territories followed a systematic 4-phase progression:",
                        "steps": [
                            {
                                "step_number": 1,
                                "title": "Industrial Pressure & Commercial Scouting (1840s–1880s)",
                                "description": "European explorers, traders, and Christian missionaries mapped interior trade routes and identified agricultural potential."
                            },
                            {
                                "step_number": 2,
                                "title": "Diplomatic Partition at Berlin (1884–1885)",
                                "description": "European powers signed the Berlin Act, establishing the 'Principle of Effective Occupation' without African consultation."
                            },
                            {
                                "step_number": 3,
                                "title": "Chartered Company Administration (1888–1895)",
                                "description": "The Imperial British East Africa Company (IBEAC) operated under royal charter, signing early treaties before facing bankruptcy."
                            },
                            {
                                "step_number": 4,
                                "title": "Direct Crown Protectorate Proclamation (1895)",
                                "description": "The British Foreign Office assumed direct military and administrative sovereignty, establishing the East Africa Protectorate."
                            }
                        ]
                    }
                }
            ],

            # Page 5: Primary Source Workshop (1895 British Parliamentary Speech)
            [
                {
                    "type": "concept_explanation",
                    "title": "Source Context: The 1895 British Parliamentary Debate",
                    "content": {
                        "text": (
                            "In July 1895, the British Parliament debated the formal annexation of the territories formerly administered by the bankrupt Imperial British East Africa Company (IBEAC). "
                            "The debate pitted imperial expansionists against cautious parliamentarians concerned about administrative costs."
                        )
                    }
                },
                {
                    "type": "mini_activity",
                    "title": "Primary Source Analysis Workshop: 1895 Parliamentary Extract",
                    "content": {
                        "instructions": (
                            "Read the historical extract from the British Parliamentary debate of 1895 carefully and answer the analytical prompts below in your notes:\n\n"
                            "**Extract:**\n"
                            "> *'Our interests in East Africa are first and foremost strategic. We must secure the highway to Uganda, which is the key to the Nile Valley, and we must ensure that no rival European power establishes a foothold on the East African coast. Furthermore, our commerce demands new markets, and it is our Christian duty to bring law, order, and industry to these untamed territories.'*\n\n"
                            "**Analytical Inquiry Questions:**\n"
                            "1. **Origin & Audience:** Who is delivering this speech, and who constitutes the target audience?\n"
                            "2. **Motives Identification:** Identify three distinct motives (one strategic, one economic, and one ideological) explicitly stated in the text.\n"
                            "3. **Justification Analysis:** How does the speaker use moral rhetoric ('Christian duty', 'law and order') to rationalize imperial annexation?\n"
                            "4. **Historical Limitations:** What are the key limitations of relying solely on colonial parliamentary records to evaluate the true impact of imperial rule on indigenous societies?"
                        )
                    }
                }
            ],

            # Page 6: Knowledge Check, Educational Video & Summary
            [
                {
                    "type": "suggested_video",
                    "title": "The Scramble for Africa & European Imperialism",
                    "content": {
                        "title": "Crash Course: The Scramble for Africa",
                        "youtube_id": "alJaltUmrGo",
                        "url": "https://www.youtube.com/watch?v=alJaltUmrGo",
                        "description": "An engaging, comprehensive historical breakdown of how European industrialization, diplomatic rivalries, and the Berlin Conference triggered the partition of Africa."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Formative Assessment: British Imperial Motives",
                    "content": {
                        "question": "What was Great Britain's primary strategic motive for asserting imperial control over the territories of Kenya and Uganda in 1895?",
                        "options": [
                            "A) To establish commercial beach resorts along the Indian Ocean coastline",
                            "B) To secure control over the Nile River source at Lake Victoria and safeguard Indian Ocean sea routes to India",
                            "C) To study and adopt traditional Bantu crop rotation and cattle herding practices",
                            "D) To discover large sub-tropical gold deposits in the central Kenyan highlands"
                        ],
                        "correct_answer": "B",
                        "explanation": (
                            "Correct! Britain's primary strategic imperative in East Africa was geopolitical: controlling Lake Victoria, "
                            "the headwaters of the River Nile, was essential to protect Egypt (and the Suez Canal), while Kenya's coastal ports "
                            "like Mombasa safeguarded naval and commercial shipping routes to India."
                        )
                    }
                }
            ]
        ]
    },

    # =========================================================================
    # LESSON 2: British Methods of Establishing Rule
    # =========================================================================
    {
        "unit_order": 2,
        "unit_name": "British Methods of Establishing Rule",
        "unit_description": "Coercive and diplomatic instruments of conquest: treaties, military force, taxation, administration, and divide-and-rule.",
        "lesson_title": "British Methods of Establishing Rule",
        "pages": [
            # Page 1: Orientation & The Colonial Toolkit
            [
                {
                    "type": "learning_goal",
                    "title": "Module 1.2.2 Learning Outcomes",
                    "content": {
                        "text": (
                            "By the end of this lesson, you will be able to:\n\n"
                            "- Identify and evaluate the five primary methods used by the British to impose colonial rule in Kenya\n"
                            "- Distinguish between diplomatic deception (treaty-making) and punitive military expeditions\n"
                            "- Explain how direct taxation (Hut and Poll Tax) was engineered to create a forced wage labor supply\n"
                            "- Analyze the colonial administrative hierarchy and the strategic deployment of 'divide-and-rule' tactics\n"
                            "- Critically interrogate the 1904 Maasai Agreement as a primary document of colonial land dispossession"
                        )
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "The Paradox of Conquest: Imposing Sovereignty",
                    "content": {
                        "text": (
                            "Declaring a 'Protectorate' on paper in London in 1895 did not mean actual control on the ground. "
                            "The British faced hundreds of autonomous, militarily capable, and politically sophisticated African societies across Kenya.\n\n"
                            "With limited British personnel and financial resources, the colonial state deployed a flexible, calculated toolkit combining **diplomatic deception**, **ruthless military force**, **administrative engineering**, **economic coercion**, and **ethnic manipulation**."
                        )
                    }
                },
                {
                    "type": "suggested_image",
                    "title": "Colonial Military and Administrative Forts",
                    "content": {
                        "title": "Fort Lugard and Early British Military Bomas",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/e/eb/Fort_Lugard.jpg",
                        "caption": "Historical photograph of an early British fortified administrative post (Boma), symbolizing the military garrison architecture through which early colonial authority was physically anchored.",
                        "author": "Wikimedia Commons",
                        "licensing": "Public Domain"
                    }
                }
            ],

            # Page 2: Diplomatic Deception & Punitive Expeditions
            [
                {
                    "type": "definition_card",
                    "title": "Punitive Expedition",
                    "content": {
                        "term": "Punitive Expedition",
                        "definition": "A state-sanctioned military assault deployed by colonial armed forces (utilizing Maxim machine guns and rifle infantry) to terrorize, burn homesteads, seize livestock, and execute leaders of resisting African communities."
                    }
                },
                {
                    "type": "comparison_table",
                    "title": "Comparative Analysis: Treaty-Making vs. Military Punitive Expeditions",
                    "content": {
                        "headers": ["Method", "Colonial Rationale & Tactics", "Impact on African Communities", "Historical Case Studies"],
                        "rows": [
                            [
                                "Treaty-Making (Diplomatic Deception)",
                                "Exploited language barriers and mistranslations; presented sovereign land cessions as peaceful mutual protection pacts",
                                "African rulers unknowingly surrendered sovereign land rights and accepted British judicial authority",
                                "Maasai Agreements of 1904 & 1911 with Oloiboni Lenana; Wanga Treaty with Nabongo Mumia"
                            ],
                            [
                                "Punitive Expeditions (Military Force)",
                                "Deployed King's African Rifles (KAR) with Maxim guns; conducted scorched-earth raids, burning crops and confiscating livestock",
                                "Devastating loss of life, famine, physical destruction, and total military subjugation",
                                "Nandi Resistance Expeditions (1895–1905); Giriama Punitive Raid (1914); Gusii Expedition (1905)"
                            ]
                        ]
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Maxim Guns and Technological Asymmetry",
                    "content": {
                        "text": (
                            "The decisive military advantage held by the British was the invention of automatic weaponry, particularly the **Maxim machine gun** (firing 500 rounds per minute). "
                            "While African warriors exhibited extraordinary battlefield courage with spears, shields, and bows, they faced an industrialized weapon system designed for mass slaughter. "
                            "As the British writer Hilaire Belloc famously summarized: *'Whatever happens, we have got the Maxim Gun, and they have not.'*"
                        )
                    }
                }
            ],

            # Page 3: Administrative Architecture & 'Divide and Rule'
            [
                {
                    "type": "concept_explanation",
                    "title": "Inventing Authority: The Creation of 'Colonial Chiefs'",
                    "content": {
                        "text": (
                            "Most pre-colonial Kenyan communities (such as the Kikuyu, Kamba, Luo, and Kalenjin) were decentralized, governed democratically by councils of elders (*Kiama*) and age-set assemblies rather than absolute monarchs.\n\n"
                            "Because the British lacked the manpower to govern directly at the village level, they **invented the office of 'Colonial Chief'** (Warrant Chiefs). "
                            "They selected individuals who were willing to collaborate—often young opportunists or former caravan guides without traditional clan legitimacy—and granted them legal power to collect taxes, recruit forced labor, and maintain local order through armed tribal police."
                        )
                    }
                },
                {
                    "type": "step_process",
                    "title": "The 4-Tier Colonial Administrative Pyramid",
                    "content": {
                        "intro": "The British governed Kenya through a rigid, top-down bureaucratic hierarchy:",
                        "steps": [
                            {
                                "step_number": 1,
                                "title": "Colonial Office & Governor (Nairobi)",
                                "description": "The Governor exercised absolute executive authority, answering directly to the British Secretary of State for the Colonies in London."
                            },
                            {
                                "step_number": 2,
                                "title": "Provincial Commissioners (PCs)",
                                "description": "Senior British officers administering expansive provincial territories (e.g., Nyanza, Central, Coast Provinces)."
                            },
                            {
                                "step_number": 3,
                                "title": "District Commissioners (DCs) & District Officers (DOs)",
                                "description": "British field officers commanding local districts, managing courts, police, and tax collection."
                            },
                            {
                                "step_number": 4,
                                "title": "Appointed Colonial Chiefs & Headmen",
                                "description": "Local African collaborators enforcing tax collection, labor conscription, and suppressing dissent in the villages."
                            }
                        ]
                    }
                },
                {
                    "type": "common_misconception",
                    "title": "Misconception: Colonial Chiefs Were Traditional African Kings",
                    "content": {
                        "misconception": "British District Commissioners simply recognized pre-existing African monarchs and hereditary kings across all Kenyan societies.",
                        "reality": "Except for rare centralized kingdoms like the Wanga Kingdom, pre-colonial Kenya was characterized by decentralized, consensus-based elder councils. The British created artificial 'Colonial Chiefs' to serve as administrative tax-collecting enforcers for the imperial crown."
                    }
                }
            ],

            # Page 4: Visualizing Economic Coercion (Taxation & Labor)
            [
                {
                    "type": "suggested_diagram",
                    "title": "The Cycle of Colonial Economic Coercion",
                    "content": {
                        "title": "Flowchart: The Closed-Loop Colonial Labor Engine",
                        "caption": "Vector diagram demonstrating how direct monetary taxation (Hut and Poll Tax) forced self-sufficient African subsistence farmers into low-wage plantation labor to finance the colonial settler state.",
                        "svg_content": SVG_ECONOMIC_COERCION_CYCLE
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Monetization as Social Engineering",
                    "content": {
                        "text": (
                            "Why did the British introduce the **Hut Tax (1901)** and **Poll Tax (1910)**? "
                            "It was not merely to raise revenue for administrative costs. Its primary purpose was **social and economic engineering**.\n\n"
                            "Before colonization, African households were self-sufficient, producing food on ancestral lands. They had no need for British currency. "
                            "By strictly demanding taxes in British cash (silver rupees and shillings) and making the non-payment of tax a criminal offense punishable by imprisonment and livestock confiscation, "
                            "the colonial state forced African men to leave their homes and work on European settler farms, railways, and public works to earn the required cash wages."
                        )
                    }
                }
            ],

            # Page 5: Primary Source Workshop (1904 Maasai Agreement)
            [
                {
                    "type": "concept_explanation",
                    "title": "Source Context: The Maasai Land Agreements",
                    "content": {
                        "text": (
                            "In 1904, British Commissioner Sir Donald Stewart negotiated an agreement with Maasai leaders headed by Oloiboni Lenana. "
                            "The Maasai, severely weakened by 1890s rinderpest epidemics and civil conflict, were pressured into signing away their fertile pasturelands."
                        )
                    }
                },
                {
                    "type": "mini_activity",
                    "title": "Primary Source Analysis Workshop: The 1904 Maasai Treaty",
                    "content": {
                        "instructions": (
                            "Examine the extract from the **1904 Maasai Treaty** and answer the analytical questions below in your exercise book:\n\n"
                            "**Extract:**\n"
                            "> *'We, the chiefs of the Maasai, do hereby agree of our own free will to cede to the British Government the fertile pastures of the Rift Valley, and we agree to move our people and our cattle to the southern reserves, in order that the white settlers may farm the land in peace. In return, the government promises that these reserves shall be ours forever.'*\n\n"
                            "**Analytical Inquiry Questions:**\n"
                            "1. **Rhetoric vs. Reality:** Does the phrase *'of our own free will'* reflect genuine voluntary choice, given the threat of British Maxim guns and recent ecological devastation? Explain.\n"
                            "2. **The 'Forever' Clause:** In 1911, the British forced a second treaty that evicted the Maasai from the Northern Reserve (Laikipia) into the arid Southern Reserve. What does this breach demonstrate about the legal integrity of colonial treaties?\n"
                            "3. **Long-Term Impact:** How did the alienation of the Rift Valley pasturelands fundamentally alter Maasai pastoralist livelihood and mobility?"
                        )
                    }
                }
            ],

            # Page 6: Knowledge Check, Educational Video & Summary
            [
                {
                    "type": "suggested_video",
                    "title": "Methods of European Colonization in Africa",
                    "content": {
                        "title": "Methods of British Imperial Rule: Direct vs. Indirect Control",
                        "youtube_id": "24f__D_5qT8",
                        "url": "https://www.youtube.com/watch?v=24f__D_5qT8",
                        "description": "An educational video analyzing how European powers utilized direct rule, indirect rule, warrant chiefs, and taxation systems to administer African colonies."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Formative Assessment: Colonial Economic Coercion",
                    "content": {
                        "question": "How did the introduction of direct taxation (Hut Tax and Poll Tax) enable European settlers to solve their acute plantation labor shortages in Kenya?",
                        "options": [
                            "A) Taxes were paid directly in surplus grain, allowing settlers to sell food profitably",
                            "B) Taxes had to be paid in British cash currency, forcing subsistence African farmers to seek wage employment on European farms",
                            "C) Tax revenues were used to establish free agricultural universities for African youths",
                            "D) The tax code made it illegal for European settlers to own more than 10 acres of land"
                        ],
                        "correct_answer": "B",
                        "explanation": (
                            "Correct! Because subsistence African farmers had no need for European currency, demanding taxes strictly in cash "
                            "forced African men into wage labor on European settler plantations to earn the money required to pay their taxes and avoid arrest."
                        )
                    }
                }
            ]
        ]
    },

    # =========================================================================
    # LESSON 3: The Process of Colonial Consolidation
    # =========================================================================
    {
        "unit_order": 3,
        "unit_name": "The Process of Colonial Consolidation",
        "unit_description": "Chronological milestones from 1895 to 1920: Uganda Railway, land alienation, White Highlands, native reserves, Kipande system, and crown colony status.",
        "lesson_title": "The Process of Colonial Consolidation",
        "pages": [
            # Page 1: Orientation & The Infrastructure Spine
            [
                {
                    "type": "learning_goal",
                    "title": "Module 1.2.3 Learning Outcomes",
                    "content": {
                        "text": (
                            "By the end of this lesson, you will be able to:\n\n"
                            "- Trace the chronological consolidation of British rule in Kenya between 1895 and 1920\n"
                            "- Evaluate the strategic, economic, and demographic impact of the Uganda Railway ('The Lunatic Line')\n"
                            "- Explain the policy of land alienation and the creation of the 'White Highlands' and 'Native Reserves'\n"
                            "- Analyze the Kipande registration system (1915) as an instrument of racial and labor control\n"
                            "- Understand the legal transition from the East Africa Protectorate to the Kenya Colony in 1920"
                        )
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Consolidation: Building the Physical Spine of Empire",
                    "content": {
                        "text": (
                            "Colonization was not a single event; it was a systematic, 25-year structural consolidation process. "
                            "Between 1895 and 1920, the British transformed Kenya from a loosely claimed protectorate into a rigidly governed settler crown colony.\n\n"
                            "The centerpiece of this consolidation was the construction of the **Uganda Railway (1896–1901)**, an enormous engineering feat that served as the physical, economic, and military backbone of the new colonial state."
                        )
                    }
                },
                {
                    "type": "suggested_image",
                    "title": "Construction of the Uganda Railway",
                    "content": {
                        "title": "Early Rail Laying on the Uganda Railway (c. 1899)",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/6/69/Uganda_railway_first_work.jpg",
                        "caption": "Historical photograph of early track laying on the Uganda Railway, illustrating the massive scale of infrastructure that opened Kenya's interior to military forces and European settlers.",
                        "author": "Wikimedia Commons",
                        "licensing": "Public Domain"
                    }
                }
            ],

            # Page 2: The Uganda Railway (1896–1901)
            [
                {
                    "type": "definition_card",
                    "title": "The Lunatic Express",
                    "content": {
                        "term": "The Uganda Railway (The Lunatic Line)",
                        "definition": "A 581-mile meter-gauge railway built from Mombasa on the Indian Ocean coast to Kisumu (Port Florence) on Lake Victoria between 1896 and 1901 at a cost of £5.5 million, using over 31,000 Indian indentured laborers."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "The Triple Impact of the Uganda Railway",
                    "content": {
                        "text": (
                            "The Uganda Railway transformed East Africa in three profound ways:\n\n"
                            "1. **Military & Strategic Control:** Troops could now travel from Mombasa to Lake Victoria in under 48 hours instead of weeks on foot. This allowed the British military to rapidly deploy Maxim guns to suppress anti-colonial resistance in the interior.\n"
                            "2. **Economic Integration:** The railway linked the fertile interior highlands to world markets, enabling the export of cash crops (coffee, tea, sisal) and the import of manufactured British goods. New towns sprouted along the track, including **Nairobi** (founded in 1899 as a railway depot and workshops).\n"
                            "3. **Demographic Shift:** The British imported **31,983 Indian indentured laborers (coolies)** to construct the line through harsh terrain, disease, and lion attacks at Tsavo. About 6,700 remained in Kenya after construction, establishing commercial trading networks (*Dukas*) across East Africa."
                        )
                    }
                },
                {
                    "type": "common_misconception",
                    "title": "Misconception: The Railway Was Built to Transport African Citizens",
                    "content": {
                        "misconception": "The British constructed the Uganda Railway as a philanthropic public transport project to help African communities travel easily.",
                        "reality": "The railway was conceived entirely for imperial geopolitics (securing the Nile Basin in Uganda against French and German rivals) and commercial resource extraction for European settler agriculture."
                    }
                }
            ],

            # Page 3: Visualizing Spatial Segregation (Map 1)
            [
                {
                    "type": "suggested_diagram",
                    "title": "Geographic Map of Colonial Infrastructure and Land Alienation",
                    "content": {
                        "title": "The Uganda Railway Spine, White Highlands, and Native Reserves",
                        "caption": "Detailed geographic vector map showing the 581-mile railway route from Mombasa to Kisumu, with the fertile White Highlands reserved for European settlers and surrounding marginalized Native Reserves.",
                        "svg_content": SVG_UGANDA_RAILWAY_MAP
                    }
                },
                {
                    "type": "comparison_table",
                    "title": "Spatial Inequity: White Highlands vs. Native Reserves",
                    "content": {
                        "headers": ["Feature / Dimension", "The 'White Highlands'", "The 'Native Reserves'"],
                        "rows": [
                            [
                                "Land Quality & Climate",
                                "Prime volcanic soil, high reliable rainfall, temperate altitude (Kiambu, Nakuru, Uasin Gishu)",
                                "Arid, semi-arid, low-rainfall, rocky, and drought-prone peripheral zones"
                            ],
                            [
                                "Legal Tenure & Rights",
                                "99-year and 999-year Crown leases granting exclusive private European ownership",
                                "Crown land held in trust; Africans legally classified as 'tenants-at-will' of the Crown"
                            ],
                            [
                                "Infrastructure & Services",
                                "Paved roads, railway feeder lines, agricultural research stations, European hospitals & schools",
                                "Neglected infrastructure; severe soil erosion, overcrowding, and minimal state services"
                            ],
                            [
                                "Economic Purpose",
                                "High-yield commercial export farming (coffee, tea, wheat, dairy, sisal)",
                                "Overcrowded labor reservoirs designed to force African youth into plantation wage labor"
                            ]
                        ]
                    }
                }
            ],

            # Page 4: Interactive Chronology of Consolidation (Timeline 1)
            [
                {
                    "type": "suggested_diagram",
                    "title": "Interactive Timeline: 1895–1920 Colonial Consolidation",
                    "content": {
                        "title": "Chronological Progression of Colonial Rule in Kenya",
                        "caption": "Milestone timeline tracking the evolution from the 1895 Protectorate declaration, Uganda Railway construction, Crown Lands Ordinances, and Kipande system, to 1920 Crown Colony status.",
                        "svg_content": SVG_COLONIAL_CONSOLIDATION_TIMELINE
                    }
                },
                {
                    "type": "step_process",
                    "title": "The 5 Milestones of Colonial Territorial Consolidation",
                    "content": {
                        "intro": "British institutional control solidified across five key legislative and political steps:",
                        "steps": [
                            {
                                "step_number": 1,
                                "title": "1895: Declaration of the East Africa Protectorate",
                                "description": "The British Foreign Office assumed direct sovereignty after the bankruptcy of the IBEAC."
                            },
                            {
                                "step_number": 2,
                                "title": "1896–1901: Uganda Railway Construction",
                                "description": "Laying 581 miles of track from Mombasa to Kisumu, creating the physical economic corridor of the nation."
                            },
                            {
                                "step_number": 3,
                                "title": "1902 onwards: Crown Lands Ordinances & Settler Influx",
                                "description": "Commissioner Sir Charles Eliot declared all 'unoccupied' lands Crown property, reserving 7.5 million acres for white settlers."
                            },
                            {
                                "step_number": 4,
                                "title": "1915: The Native Registration Ordinance (Kipande System)",
                                "description": "Enacted mandatory metal cylinder fingerprint identification passes for all African males over 16 to enforce labor contracts."
                            },
                            {
                                "step_number": 5,
                                "title": "1920: Declaration of Kenya Crown Colony",
                                "description": "The protectorate was formally incorporated as the 'Kenya Colony and Protectorate', embedding British administrative supremacy."
                            }
                        ]
                    }
                }
            ],

            # Page 5: Primary Source Workshop (The Kipande Archival System)
            [
                {
                    "type": "concept_explanation",
                    "title": "The Kipande System: Pass Laws and Labor Control",
                    "content": {
                        "text": (
                            "In 1915, the colonial administration passed the **Native Registration Ordinance**, fully implemented in 1919–1920. "
                            "Under this law, every African male aged 16 and above was legally compelled to carry a metal cylinder necklace containing a registration document (**Kipande**).\n\n"
                            "The document recorded the individual's full name, tribe, fingerprint impressions, employer's name, wage rate, and employer signature upon release. "
                            "Leaving an employer without permission was a criminal offense ('desertion'), allowing police to arrest and return runaway workers."
                        )
                    }
                },
                {
                    "type": "mini_activity",
                    "title": "Archival Source Analysis: The Kipande Identity Badge",
                    "content": {
                        "instructions": (
                            "Analyze the historical context of the **Kipande registration badge** and answer the questions below in your study notebook:\n\n"
                            "**Historical Archival Description:**\n"
                            "> *A small brass cylinder worn on a string around the neck of every adult African man in colonial Kenya. Inside was a four-page card containing the bearer's photo, thumbprint, employer's monthly stamp, conduct remarks, and wage receipts. Failure to produce the Kipande on demand to any European officer resulted in immediate flogging, fines, or prison labor.*\n\n"
                            "**Analytical Inquiry Questions:**\n"
                            "1. **Functional Purpose:** How did the Kipande card function to suppress African wage bargaining and prevent workers from seeking better-paying jobs?\n"
                            "2. **Human Dignity & Citizenship:** How did forcing human beings to wear identity cylinders around their necks violate personal freedom and bodily dignity?\n"
                            "3. **Catalyst for Resistance:** Why did the Kipande become the primary grievance that united early Kenyan political associations (e.g., Harry Thuku's East African Association in 1921)?"
                        )
                    }
                }
            ],

            # Page 6: Knowledge Check, Educational Video & Summary
            [
                {
                    "type": "suggested_video",
                    "title": "Building the Uganda Railway: The Lunatic Line",
                    "content": {
                        "title": "The Engineering of the Uganda Railway",
                        "youtube_id": "rD4Lh_xV_sA",
                        "url": "https://www.youtube.com/watch?v=rD4Lh_xV_sA",
                        "description": "Historical documentary exploring the massive engineering challenges, Tsavo man-eating lions, Indian laborers, and geopolitical consequences of Kenya's Uganda Railway."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Formative Assessment: Colonial Consolidation",
                    "content": {
                        "question": "Why was the construction of the Uganda Railway (1896–1901) considered the indispensable backbone of British colonial consolidation in Kenya?",
                        "options": [
                            "A) It was financed entirely through voluntary monetary donations from African community elders",
                            "B) It allowed the rapid military deployment of British forces to suppress interior resistance and connected European settler farms to Mombasa port for export",
                            "C) It was designed exclusively as a passenger service for African children attending missionary schools",
                            "D) It legally banned European settlers from acquiring land in the Kenyan highlands"
                        ],
                        "correct_answer": "B",
                        "explanation": (
                            "Correct! The Uganda Railway provided the dual military and economic foundation of colonial rule: "
                            "it enabled rapid troop movement to crush indigenous resistance while allowing European settler cash crops to be exported efficiently."
                        )
                    }
                }
            ]
        ]
    },

    # =========================================================================
    # LESSON 4: African Agency, Collaboration, and Resistance
    # =========================================================================
    {
        "unit_order": 4,
        "unit_name": "African Agency, Collaboration, and Resistance",
        "unit_description": "Diverse African responses to British imperial conquest: collaboration (Mumia, Lenana) vs. armed and spiritual resistance (Koitalel Arap Samoei, Mekatilili wa Menza).",
        "lesson_title": "African Agency, Collaboration, and Resistance",
        "pages": [
            # Page 1: Orientation & Reclaiming African Agency
            [
                {
                    "type": "learning_goal",
                    "title": "Module 1.2.4 Learning Outcomes",
                    "content": {
                        "text": (
                            "By the end of this lesson, you will be able to:\n\n"
                            "- Define and apply the historical concept of **African Agency** during colonial conquest\n"
                            "- Compare the strategic calculations behind **collaboration** (Nabongo Mumia, Oloiboni Lenana) and **resistance** (Koitalel Arap Samoei, Mekatilili wa Menza)\n"
                            "- Evaluate the 10-year Nandi armed guerrilla resistance against the Uganda Railway\n"
                            "- Analyze Mekatilili wa Menza's spiritual mobilization and female leadership along the Kenyan Coast\n"
                            "- Corroborate contrasting primary accounts (oral tradition vs. Meinertzhagen's diary) regarding Koitalel's assassination"
                        )
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Reclaiming African Agency: Beyond the Passive Victim Myth",
                    "content": {
                        "text": (
                            "When European imperialists arrived, African societies did not passively submit or react blindly. "
                            "Every Kenyan community exercised **African Agency**—making calculated, rational decisions based on their local political, military, and ecological realities.\n\n"
                            "Depending on their internal strength, previous disease epidemics, and regional rivalries, African leaders chose either **strategic collaboration** (diplomatic alliance to preserve their people and acquire weapons) or **heroic resistance** (armed and spiritual defense of land, culture, and sovereignty)."
                        )
                    }
                },
                {
                    "type": "suggested_image",
                    "title": "African Leadership and Statecraft",
                    "content": {
                        "title": "Nabongo Mumia Shiundu of the Wanga Kingdom",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/d/db/Nabongo_Mumia_Shiundu.jpg",
                        "caption": "Archival portrait of Nabongo Mumia Shiundu, King of Wanga, who engaged in pragmatic diplomatic collaboration with British officials to protect his kingdom and expand regional influence.",
                        "author": "Wikimedia Commons",
                        "licensing": "Public Domain"
                    }
                }
            ],

            # Page 2: The Dynamics of Collaboration (Wanga & Maasai)
            [
                {
                    "type": "definition_card",
                    "title": "African Agency",
                    "content": {
                        "term": "African Agency",
                        "definition": "The capacity of African individuals and societies to act independently, make calculated political choices, formulate strategies, and shape historical outcomes in response to European colonial invasion."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Case Studies in Collaboration: Rational Statecraft",
                    "content": {
                        "text": (
                            "**1. Nabongo Mumia of the Wanga Kingdom (Western Kenya):**\n"
                            "- **Motive:** The centralized Wanga Kingdom faced hostile regional rivals, notably the Bukusu and the Luo of Ugenya. Mumia recognized the superiority of British firearms and sought a powerful military ally.\n"
                            "- **Action:** He welcomed British administrators (like C.W. Hobley), provided food supplies, and stationed British headquarters at Mumias.\n"
                            "- **Outcome:** Wanga preserved its monarchy; Mumia was appointed 'Paramount Chief' in 1909, and Wanga agents were installed as colonial chiefs across Western Kenya.\n\n"
                            "**2. Oloiboni Lenana of the Maasai (Rift Valley):**\n"
                            "- **Motive:** In the 1890s, the Maasai were decimated by catastrophic rinderpest epidemics (which wiped out 90% of cattle), smallpox, severe famine (*Enkidang'et*), and a bitter civil war between Lenana and his brother Sendeyo. The Maasai were too weakened to fight a military war.\n"
                            "- **Action:** Lenana signed the 1904 Agreement, ceding Rift Valley pastures in exchange for British protection and cattle restocking.\n"
                            "- **Outcome:** Avoided military annihilation but resulted in massive land loss to white settlers."
                        )
                    }
                },
                {
                    "type": "common_misconception",
                    "title": "Misconception: Collaborators Were Simple Traitors",
                    "content": {
                        "misconception": "African leaders who collaborated with the British were simply selfish traitors who sold out their nation.",
                        "reality": "Modern nation-states like 'Kenya' did not exist in the 1890s. Leaders like Mumia and Lenana acted as responsible sovereigns of their specific sovereign nations, seeking pragmatic alliances to protect their people from famine, regional rivals, and military devastation."
                    }
                }
            ],

            # Page 3: Armed Resistance — Koitalel Arap Samoei & The Nandi
            [
                {
                    "type": "concept_explanation",
                    "title": "The Nandi Resistance (1895–1905): 10 Years of Defiance",
                    "content": {
                        "text": (
                            "The **Nandi Resistance** was the longest, fiercest, and most organized military opposition to British colonization in East Africa, lasting a full decade.\n\n"
                            "- **Causes:** Supreme spiritual leader (**Orkoiyot Koitalel Arap Samoei**) rallied Nandi warriors to defend ancestral grazing lands and fulfill the famous prophecy of Kimnyole, which foretold that an 'Iron Snake' (the Uganda Railway) would spit fire and conquer their land.\n"
                            "- **Tactics:** The Nandi mastered **guerrilla warfare**—utilizing rugged highland topography, night ambushes, and raiding railway construction camps to steal copper telegraph wire (used for traditional ornaments) and railway spikes (smelted into spearheads).\n"
                            "- **The Assassination (19 October 1905):** Unable to defeat Koitalel on the battlefield, British Commander **Captain Richard Meinertzhagen** invited Koitalel to a peace conference under a white flag of truce at Ketparak (Nandi Hills). As Koitalel extended his hand in greeting, Meinertzhagen treacherously shot him dead."
                        )
                    }
                },
                {
                    "type": "suggested_image",
                    "title": "Indigenous Resistance Warriors",
                    "content": {
                        "title": "Nandi Warriors in Traditional War Attire",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/f/f5/Nandi_warriors_from_the_LOC.jpg",
                        "caption": "Early archival photograph of Nandi warriors with spears and painted buffalo-hide shields, representing the courageous fighters who resisted British railway encroachment for ten years.",
                        "author": "Library of Congress / Wikimedia Commons",
                        "licensing": "Public Domain"
                    }
                },
                {
                    "type": "step_process",
                    "title": "Chronology of the Nandi Anti-Colonial Struggle",
                    "content": {
                        "intro": "The decade-long confrontation progressed through four key stages:",
                        "steps": [
                            {
                                "step_number": 1,
                                "title": "1895–1897: Early Clashes & British Repulse",
                                "description": "Nandi warriors intercepted British caravans; early British punitive expeditions suffered heavy defeats in the Nandi Hills."
                            },
                            {
                                "step_number": 2,
                                "title": "1899–1900: Railway Raids & Telegraph Cutting",
                                "description": "As rail construction entered Nandi territory, warriors launched systematic raids, cutting communications."
                            },
                            {
                                "step_number": 3,
                                "title": "1902–1905: Large-Scale British Expeditions",
                                "description": "The colonial state deployed combined forces of British infantry, Indian troops, and Maasai mercenaries."
                            },
                            {
                                "step_number": 4,
                                "title": "19 October 1905: The Treacherous Parley & Martyrdom",
                                "description": "Koitalel Arap Samoei was assassinated under a peace truce; Nandi resistance collapsed, and land was alienated."
                            }
                        ]
                    }
                }
            ],

            # Page 4: Spiritual & Cultural Resistance — Mekatilili wa Menza
            [
                {
                    "type": "concept_explanation",
                    "title": "Mekatilili wa Menza and the Giriama Resistance (1913–1914)",
                    "content": {
                        "text": (
                            "In coastal Kenya, the British attempted to force Giriama youth to work on European sisal and rubber plantations, while imposing heavy poll taxes and undermining traditional sacred forests (**Kaya Shrines**).\n\n"
                            "**Mekatilili wa Menza**, an elderly charismatic widow and spiritual leader, mobilized the Giriama nation through unique socio-cultural strategies:\n"
                            "- **The Mukushekushe Dance:** She toured villages performing the prophetic *Mukushekushe* dance, attracting large crowds of women and youth.\n"
                            "- **Kifudu Oaths:** She administered the solemn *Kifudu* oath, swearing warriors never to work on European farms, pay colonial taxes, or obey appointed British headmen.\n"
                            "- **Total Labor Boycott:** The Giriama completely halted the supply of coastal laborers and attacked colonial administrative posts in 1914.\n\n"
                            "**The Outcome:** Although arrested and exiled over 1,000 km away to Kisii, Mekatilili escaped on foot back to the Coast. Her resistance forced the British to relax forced labor quotas and respect traditional Kaya customs."
                        )
                    }
                },
                {
                    "type": "comparison_table",
                    "title": "Comparative Matrix: Koitalel Arap Samoei vs. Mekatilili wa Menza",
                    "content": {
                        "headers": ["Comparison Dimension", "Koitalel Arap Samoei (Nandi)", "Mekatilili wa Menza (Giriama)"],
                        "rows": [
                            [
                                "Leadership Model",
                                "Spiritual monarch & military supreme seer (*Orkoiyot*)",
                                "Grassroots female charismatic widow & spiritual prophetess"
                            ],
                            [
                                "Primary Grievance",
                                "Alienation of ancestral land and railway encroachment",
                                "Forced plantation labor conscription of youth and taxation"
                            ],
                            [
                                "Mobilization Tactics",
                                "Armed guerrilla warfare, night raids, spear ambushes",
                                "Spiritual *Mukushekushe* dance, *Kifudu* sacred oaths, labor boycotts"
                            ],
                            [
                                "Historical Consequence",
                                "Assassinated under false peace truce (1905); land seized",
                                "Exiled twice, walked 1,000 km back; forced labor quotas reduced"
                            ]
                        ]
                    }
                }
            ],

            # Page 5: Collaboration vs. Resistance Comparative Matrix
            [
                {
                    "type": "suggested_diagram",
                    "title": "Comparative Strategic Matrix: Collaboration vs. Resistance",
                    "content": {
                        "title": "Comparative Matrix of African Responses to Colonial Invasion",
                        "caption": "Vector matrix analyzing the motives, strategies, and historical outcomes of Nabongo Mumia, Oloiboni Lenana, Koitalel Arap Samoei, and Mekatilili wa Menza.",
                        "svg_content": SVG_COLLABORATION_RESISTANCE_MATRIX
                    }
                },
                {
                    "type": "mini_activity",
                    "title": "Critical Thinking & Debate Workshop: Evaluating African Choices",
                    "content": {
                        "instructions": (
                            "In your history journal, write a balanced, evidence-based essay (100–150 words) evaluating the following historical statement:\n\n"
                            "> *'In pre-colonial Kenya, collaboration with the British was an act of betrayal, while armed resistance was the only honorable and rational choice.'*\n\n"
                            "**Guiding Evaluation Criteria:**\n"
                            "1. Use evidence from **Nabongo Mumia** (Wanga) or **Oloiboni Lenana** (Maasai) to demonstrate how collaboration was often a calculated strategy for community survival.\n"
                            "2. Use evidence from **Koitalel Arap Samoei** (Nandi) or **Mekatilili wa Menza** (Giriama) to illustrate the principles and sacrifices of armed/spiritual resistance.\n"
                            "3. Conclude by demonstrating that both pathways represented genuine expressions of **African Agency** under severe constraints."
                        )
                    }
                }
            ],

            # Page 6: Dual Source Corroboration Workshop (Koitalel's Assassination)
            [
                {
                    "type": "concept_explanation",
                    "title": "Historical Inquiry: The Assassination of Koitalel Arap Samoei",
                    "content": {
                        "text": (
                            "On the morning of 19 October 1905 at Ketparak in the Nandi Hills, a fateful parley took place between Orkoiyot Koitalel Arap Samoei and British Commander Captain Richard Meinertzhagen. "
                            "Historians evaluate conflicting accounts to reconstruct what actually happened."
                        )
                    }
                },
                {
                    "type": "mini_activity",
                    "title": "Dual Primary Source Corroboration: Oral Tradition vs. Colonial Diary",
                    "content": {
                        "instructions": (
                            "Read the two contrasting primary accounts of Koitalel Arap Samoei's death and complete the historical analysis below:\n\n"
                            "**Source A: Nandi Oral Tradition (Elder Memory):**\n"
                            "> *'Koitalel went to the meeting with only peace in his heart, carrying his ceremonial walking stick as requested. The white man had hidden soldiers in the bushes. When Koitalel extended his hand in friendship, the white man pulled his pistol and shot our leader in cold blood. They then decapitated him and took his head as a trophy.'*\n\n"
                            "**Source B: Captain Richard Meinertzhagen's Personal Diary (1905):**\n"
                            "> *'I met the Nandi Orkoiyot (Koitalel) today. As we shook hands, I sensed a trap. He tried to pull me down, and his warriors raised their spears. In self-defense, I was forced to shoot him on the spot. A melee ensued, and we cleared the ridge.'*\n\n"
                            "**Analytical Inquiry Prompts:**\n"
                            "1. **Direct Contradiction:** How do Source A and Source B directly contradict each other regarding who initiated the violence?\n"
                            "2. **Author Bias & Motive:** What motive did Meinertzhagen have to write a self-defense narrative in his official diary?\n"
                            "3. **Historical Method:** How does a professional historian corroborate oral testimony and written colonial archives to reach an objective conclusion?"
                        )
                    }
                }
            ],

            # Page 7: Knowledge Check, Educational Video & Summary
            [
                {
                    "type": "suggested_video",
                    "title": "African Resistance to European Colonization",
                    "content": {
                        "title": "African Resistance, Collaboration, and Agency",
                        "youtube_id": "u9g_X2N4l3E",
                        "url": "https://www.youtube.com/watch?v=u9g_X2N4l3E",
                        "description": "Educational video documenting the military, cultural, and political strategies utilized by African societies to confront and resist European imperialism."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Formative Assessment: African Agency & Collaboration",
                    "content": {
                        "question": "Why did Nabongo Mumia of the Wanga Kingdom choose a diplomatic policy of collaboration with the British in the 1890s?",
                        "options": [
                            "A) He sought British military alliances and modern firearms to protect and expand his kingdom against hostile regional rivals",
                            "B) He wished to dissolve his monarchy and surrender all governance to European settlers immediately",
                            "C) He mistakenly believed that British officers were spiritual deities sent from the sky",
                            "D) He signed treaties solely to facilitate the relocation of the Wanga people to the Kenyan Coast"
                        ],
                        "correct_answer": "A",
                        "explanation": (
                            "Correct! Nabongo Mumia engaged in calculated collaboration: by allying with the British, "
                            "he secured modern firearms and military support to defeat his traditional regional rivals (such as the Luo of Ugenya and Bukusu), "
                            "while preserving his throne and gaining the status of Paramount Chief."
                        )
                    }
                }
            ]
        ]
    },

    # =========================================================================
    # LESSON 5: Colonial Rule as Change Over Time
    # =========================================================================
    {
        "unit_order": 5,
        "unit_name": "Colonial Rule as Change Over Time",
        "unit_description": "Transformations in borders, political authority, land tenure, and economy; enduring legacies on modern Kenyan citizenship, politics, and land disputes.",
        "lesson_title": "Colonial Rule as Change Over Time",
        "pages": [
            # Page 1: Orientation & The Shadows of Colonialism
            [
                {
                    "type": "learning_goal",
                    "title": "Module 1.2.5 Learning Outcomes",
                    "content": {
                        "text": (
                            "By the end of this lesson, you will be able to:\n\n"
                            "- Compare pre-colonial, colonial, and post-colonial Kenyan societies across four societal dimensions\n"
                            "- Evaluate the historical transformation of territorial borders, political systems, land tenure, and economies\n"
                            "- Analyze the three major enduring legacies of colonial rule: the Land Question, Ethnic Polarization, and Imposed Legal Systems\n"
                            "- Understand how colonial border-making fragmented indigenous communities (Maasai, Somali) across modern nation-states\n"
                            "- Synthesize the entire Topic 1.2 curriculum in preparation for senior secondary assessments"
                        )
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Colonialism as Structural Rewiring",
                    "content": {
                        "text": (
                            "Colonial rule was not simply a temporary interruption in African history; it fundamentally rewired the institutional, legal, geographic, and economic architecture of Kenya.\n\n"
                            "When Kenya attained national independence on **12 December 1963**, the new independent republic inherited the borders, centralized bureaucratic structures, judicial systems, and economic patterns forged during seven decades of British colonial administration. "
                            "Understanding this 'colonial inheritance' is essential to solving modern Kenya's most pressing national challenges."
                        )
                    }
                },
                {
                    "type": "suggested_image",
                    "title": "Inherited Institutional Architecture",
                    "content": {
                        "title": "Parliament Buildings in Nairobi, Kenya",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/a/ad/Parliament_Buildings%2C_Nairobi%2C_Kenya-21April2010.jpg",
                        "caption": "The Kenyan Parliament Buildings in Nairobi, illustrating how post-colonial democratic governance inherited the centralized Westminster parliamentary architecture and institutional forms introduced during British colonial rule.",
                        "author": "Wikimedia Commons",
                        "licensing": "CC BY-SA 3.0"
                    }
                }
            ],

            # Page 2: Multi-Dimensional Change Over Time
            [
                {
                    "type": "comparison_table",
                    "title": "Four Dimensions of Transformation: Pre-Colonial vs. Colonial vs. Modern Kenya",
                    "content": {
                        "headers": ["Societal Dimension", "Pre-Colonial Era (~1880)", "British Colonial Era (1895–1963)", "Post-Colonial Modern Kenya (Present)"],
                        "rows": [
                            [
                                "Borders & Territory",
                                "Fluid, porous boundaries based on ecological zones, seasonal migration, and barter pacts",
                                "Rigid international borders and ethnic administrative 'Native Reserves' enforced by law",
                                "Inherited fixed borders; cross-border ethnic communities (e.g. Somali, Maasai, Kuria)"
                            ],
                            [
                                "Political Authority",
                                "Decentralized elder councils (*Kiama*), age-set assemblies, and consensus democracy",
                                "Authoritarian Governors, PCs, DCs, and appointed Colonial Warrant Chiefs",
                                "Centralized national executive, National Assembly, Senate, and 47 devolved county governments"
                            ],
                            [
                                "Land Tenure & Rights",
                                "Communal land ownership managed by clans for farming, grazing, and future generations",
                                "Land alienation; creation of private 'White Highlands' and overcrowded Native Reserves",
                                "Private title deeds alongside communal lands; persistent historical land injustice claims"
                            ],
                            [
                                "Economic Systems",
                                "Self-sufficient subsistence agriculture, pastoralism, and regional barter trade",
                                "Cash-crop monoculture (tea, coffee, sisal), direct cash taxation, and wage labor exploitation",
                                "Diversified market economy, mobile money (M-Pesa), global trade, and national taxation (KRA)"
                            ]
                        ]
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "The Transformation of Governance",
                    "content": {
                        "text": (
                            "In pre-colonial Kenya, political power was dispersed and held accountable by elders, women's councils, and warrior age-grades. "
                            "Decisions required consensus, preventing authoritarian tyranny.\n\n"
                            "British rule replaced this deliberative democracy with an **authoritarian, top-down provincial administration**. "
                            "The post-colonial Kenyan state retained this centralized structure (Provincial Administration) for decades, until the **2010 Constitution** introduced **devolution** to disperse power across 47 counties."
                        )
                    }
                },
                {
                    "type": "common_misconception",
                    "title": "Misconception: Kenya Was an Ancient Unified Nation-State",
                    "content": {
                        "misconception": "Kenya existed as a single unified country with national borders prior to the British arrival.",
                        "reality": "Pre-colonial Kenya comprised over 40 sovereign, culturally rich communities who interacted through dynamic trade, intermarriage, and diplomatic negotiations. 'Kenya' as a single geopolitical entity was created by British imperial cartography in 1895."
                    }
                }
            ],

            # Page 3: Visualizing Spatial Transformation
            [
                {
                    "type": "suggested_diagram",
                    "title": "Change Over Time: Pre-Colonial vs. Colonial Geography",
                    "content": {
                        "title": "Comparative Slide: Pre-Colonial Fluidity vs. Colonial Spatial Segregation",
                        "caption": "Side-by-side comparative diagram illustrating the shift from organic, overlapping indigenous zones of interaction to rigid imperial boundaries and racialized native reserves.",
                        "svg_content": SVG_PRECOLONIAL_VS_COLONIAL_COMPARISON
                    }
                },
                {
                    "type": "step_process",
                    "title": "The 5 Eras of Kenyan Statehood Evolution",
                    "content": {
                        "intro": "Kenyan governance evolved through five distinct historical transformations:",
                        "steps": [
                            {
                                "step_number": 1,
                                "title": "Pre-Colonial Sovereign Nations (Pre-1895)",
                                "description": "Independent ethnic communities governed by elder councils and consensual customary law."
                            },
                            {
                                "step_number": 2,
                                "title": "East Africa Protectorate (1895–1920)",
                                "description": "Early military pacification, railway construction, and establishment of initial settler enclaves."
                            },
                            {
                                "step_number": 3,
                                "title": "Kenya Crown Colony (1920–1963)",
                                "description": "Rigid settler domination, Kipande pass laws, White Highlands exclusivity, and anti-colonial liberation struggle."
                            },
                            {
                                "step_number": 4,
                                "title": "Independent Republic & Centralized State (1963–2010)",
                                "description": "Decolonization under Kenyatta and Moi, inheriting the centralized provincial administration."
                            },
                            {
                                "step_number": 5,
                                "title": "Devolved Constitutional Democracy (2010–Present)",
                                "description": "Modern constitutional framework restoring decentralized grassroots democracy through 47 county governments."
                            }
                        ]
                    }
                }
            ],

            # Page 4: Deep Dive into the 3 Enduring Legacies
            [
                {
                    "type": "definition_card",
                    "title": "Negative Ethnicity (Tribalism)",
                    "content": {
                        "term": "Negative Ethnicity",
                        "definition": "The political exploitation of ethnic identities, directly rooted in colonial 'divide-and-rule' administrative reserves, where ethnic groups were physically segregated and pitted against each other for state resources."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "The 3 Major Enduring Legacies of Colonial Rule",
                    "content": {
                        "text": (
                            "Modern Kenyan citizenship and society continue to grapple with three primary structural legacies:\n\n"
                            "1. **The Unresolved Land Question:** The alienation of 7.5 million acres for European settlers in the fertile Rift Valley and Central Kenya created mass displacement. At independence in 1963, fertile lands were often bought by political elites rather than restored to landless squatters, creating historical land grievances that persist in contemporary Kenyan politics.\n"
                            "2. **Ethnic Polarization & Native Reserves:** The British divided Kenya into administrative districts along strict ethnic lines (e.g., 'Central Kavirondo' for Luo, 'North Kavirondo' for Luhya, 'Fort Hall' for Kikuyu). This policy hardened ethnic boundaries and fostered 'tribalism' as a competitive political tool for national power.\n"
                            "3. **Imposed Legal and Constitutional Systems:** Kenya's formal judicial system, statutory penal code, English official language, civil service traditions, and parliamentary Westminster system were all built directly upon British colonial frameworks."
                        )
                    }
                }
            ],

            # Page 5: Scholarly & Archival Source Analysis
            [
                {
                    "type": "concept_explanation",
                    "title": "Historical Interpretation: The Architecture of Colonial Power",
                    "content": {
                        "text": (
                            "Historians analyze how colonial institutions constructed modern political identities and state structures that outlived the British Empire."
                        )
                    }
                },
                {
                    "type": "mini_activity",
                    "title": "Scholarly Source Analysis Workshop: The Centralized State Legacy",
                    "content": {
                        "instructions": (
                            "Read the scholarly extract from a leading Kenyan historian and answer the analytical prompts in your notes:\n\n"
                            "**Extract:**\n"
                            "> *'The most durable legacy of British colonialism in Kenya was not the railway tracks or the stone buildings, but the creation of a centralized state authority that concentrated power at the center. By creating administrative boundaries along ethnic lines, the colonial state constructed \"tribes\" as political units, creating the challenge of negative ethnicity that independent Kenya struggles to overcome.'*\n\n"
                            "**Analytical Inquiry Questions:**\n"
                            "1. **Core Thesis:** According to the historian, what constitutes the most enduring legacy of British colonialism in Kenya?\n"
                            "2. **Causal Mechanism:** How did colonial administrative cartography ('Native Reserves') transform fluid pre-colonial cultural groups into rigid political 'tribes'?\n"
                            "3. **Modern Solution:** How does Kenya's 2010 Constitution attempt to cure this legacy through county devolution and Bill of Rights protections?"
                        )
                    }
                },
                {
                    "type": "mini_activity",
                    "title": "Structured Examination Question & Model Answer: Border Partition",
                    "content": {
                        "instructions": (
                            "**Context & Question:**\n"
                            "> *'At independence in 1963, the founding fathers of Kenya chose to retain the international borders drawn by the British in 1895, fearing that redrawing them would trigger inter-state wars. As a result, communities like the Somali and Maasai remained divided across different modern nations.'*\n\n"
                            "**Exam Question:** Explain one major long-term consequence of colonial border-making on post-colonial citizenship and communities in East Africa.\n\n"
                            "**Model Answer:**\n"
                            "A major long-term consequence of colonial border-making was the arbitrary partition of cohesive indigenous communities across modern national boundaries. "
                            "Because borders were drawn in European boardrooms without regard for ethnic, linguistic, or pastoral grazing realities, the **Maasai** were split between Kenya and Tanzania, while the **Somali** were divided across Kenya, Somalia, and Ethiopia. "
                            "In the post-colonial era, this has generated complex challenges regarding regional cross-border security, grazing disputes during droughts, and questions of dual identity and national belonging for borderland citizens."
                        )
                    }
                }
            ],

            # Page 6: Knowledge Check, Educational Video, Topic Summary
            [
                {
                    "type": "suggested_video",
                    "title": "Colonialism's Impact on Modern Africa & Legacies",
                    "content": {
                        "title": "The Enduring Legacies of Colonial Rule in Africa",
                        "youtube_id": "T_sGTspaF4Y",
                        "url": "https://www.youtube.com/watch?v=T_sGTspaF4Y",
                        "description": "An insightful historical analysis of how colonial borders, economic extraction models, and administrative systems continue to influence governance and society across modern Africa."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Formative Assessment: Legacies of Colonial Rule",
                    "content": {
                        "question": "The colonial policy of 'divide-and-rule' and the creation of ethnically segregated 'Native Reserves' had what major long-term consequence for post-colonial Kenya?",
                        "options": [
                            "A) It completely eliminated all forms of regional trade between communities",
                            "B) It compelled all Kenyan communities to adopt a purely nomadic pastoral lifestyle",
                            "C) It hardened ethnic divisions and created the enduring political challenge of negative ethnicity",
                            "D) It ensured that all land in Kenya was distributed equally among all citizens at independence"
                        ],
                        "correct_answer": "C",
                        "explanation": (
                            "Correct! By confining ethnic groups to rigid administrative Native Reserves and pitting them against each other, "
                            "the British colonial state institutionalized ethnic divisions, leaving an enduring challenge of negative ethnicity "
                            "and ethnic politics in post-colonial Kenya."
                        )
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Topic 1.2 Comprehensive Summary: Key Learnings",
                    "content": {
                        "text": (
                            "**Topic 1.2 Summary:**\n\n"
                            "- **Motives:** Driven by strategic control over the Nile River source and Indian Ocean routes to India, alongside industrial demand for raw materials and the paternalistic 'civilizing mission'.\n"
                            "- **Methods:** Imposed through diplomatic deception (treaties), military violence (Maxim guns), direct cash taxation, invented warrant chiefs, and divide-and-rule tactics.\n"
                            "- **Consolidation:** Anchored by the Uganda Railway (1896–1901), extensive land alienation creating the White Highlands, the Kipande identity system, and Crown Colony status in 1920.\n"
                            "- **African Agency:** Expressed through calculated collaboration (Mumia, Lenana) to survive epidemics and defeat rivals, and fierce armed/spiritual resistance (Koitalel Arap Samoei, Mekatilili wa Menza).\n"
                            "- **Legacies:** Shaped modern Kenya's inherited borders, centralized governance, unresolved land questions, and ethnic political dynamics."
                        )
                    }
                }
            ]
        ]
    }
]
