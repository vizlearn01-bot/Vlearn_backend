"""
VLearn CBC Grade 10 History — Topic 12: The First Industrial Revolution and Africa
Authoritative Pedagogical Data Definitions (Lessons 1 to 4)
"""

from curriculum.cbc_grade10_history_topic12_svgs import (
    SVG_INDUSTRIAL_INNOVATIONS,
    SVG_INDUSTRIAL_TO_COLONIAL_CHAIN,
    SVG_CYCLE_OF_UNDERDEVELOPMENT
)

TOPIC_12_LESSONS = [
    # =========================================================================
    # LESSON 1: Industrial Revolution in Britain and the USA
    # =========================================================================
    {
        "unit_order": 1,
        "unit_name": "Industrial Revolution in Britain and the USA",
        "unit_description": "Enabling factors of industrialization in Great Britain and the United States: coal, iron, James Watt's steam engine, interchangeable parts, and Eli Whitney's cotton gin.",
        "lesson_title": "Industrial Revolution in Britain and the USA",
        "pages": [
            # Card 1: Orientation & Hook
            [
                {
                    "type": "suggested_image",
                    "title": "Coal, Steam, and the Rise of Mechanical Power",
                    "content": {
                        "title": "Early British Steam Engine and Coal Mine",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/66/Newcomen_steam_engine.png/800px-Newcomen_steam_engine.png",
                        "caption": "Early industrial steam pumping engine in a British coal mine—the mechanical breakthrough that unlocked thermal energy and initiated the Industrial Revolution.",
                        "author": "Wikimedia Commons",
                        "licensing": "Public Domain"
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "The Shift from Muscle to Mechanical Power",
                    "content": {
                        "text": (
                            "How did humanity transition from a world where almost everything was crafted by hand using human and animal muscle, to a world powered by steam, steel, and roaring machines?\n\n"
                            "Between 1760 and 1840, Great Britain transformed into the **'Workshop of the World.'** A convergence of agricultural reforms, capital accumulated from global commerce, mineral abundance (coal and iron), and revolutionary inventions set off a wave of industrialization that soon spread across the Atlantic to the United States."
                        )
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 1 Learning Goals",
                    "content": {
                        "text": (
                            "By the end of this lesson, you will be able to:\n\n"
                            "- Compare the enabling factors of the Industrial Revolution in Great Britain vs the United States\n"
                            "- Explain the mechanical significance of James Watt's steam engine and Eli Whitney's cotton gin\n"
                            "- Analyze how interchangeable parts laid the foundation for modern assembly-line mass production"
                        )
                    }
                }
            ],

            # Card 2: Innovations SVG Diagram
            [
                {
                    "type": "suggested_diagram",
                    "title": "Key Innovations of the First Industrial Revolution",
                    "content": {
                        "title": "Steam Engine & Cotton Gin Mechanics",
                        "caption": "Technical diagram comparing the thermal-to-rotary mechanics of Watt's steam engine with Whitney's cotton gin and standardized interchangeable parts.",
                        "svg_content": SVG_INDUSTRIAL_INNOVATIONS
                    }
                }
            ],

            # Card 3: Britain vs USA Comparative Matrix
            [
                {
                    "type": "comparison_table",
                    "title": "Enabling Factors: Great Britain vs. United States",
                    "content": {
                        "headers": ["Enabling Dimension", "Great Britain (The Pioneer)", "United States (The Rapid Adapter)"],
                        "rows": [
                            ["Energy & Minerals", "Rich, accessible deposits of coal and iron ore located near water transport", "Abundant timber, coal, and rushing rivers for water-wheel kinetic energy"],
                            ["Labor Supply", "Agricultural enclosure acts forced dispossessed peasants into factory cities", "Mass European immigration provided a continuous workforce for industrial cities"],
                            ["Key Inventions", "James Watt's steam engine, Spinning Jenny, and Arkwright's water frame", "Eli Whitney's cotton gin (1793) and standardized interchangeable parts system"],
                            ["Infrastructure", "Dense network of navigable canals, river networks, and early national railways", "Transcontinental railroads and canals (Erie Canal) linking agricultural West to industrial East"],
                            ["Trade Policies", "Free-trade imperial dominance through global Royal Navy supremacy", "High protective tariffs defending young American domestic industries from British competition"]
                        ]
                    }
                }
            ],

            # Card 4: Video Case Study
            [
                {
                    "type": "suggested_video",
                    "title": "The First Industrial Revolution and Technological Transformation",
                    "content": {
                        "title": "How Coal, Steam, and Iron Built the Modern World",
                        "description": "Educational documentary analyzing the technological innovations and socio-economic conditions that launched the Industrial Revolution.",
                        "youtube_id": "kY31WnS8jXk"
                    }
                }
            ],

            # Card 5: Knowledge Check
            [
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check: Interchangeable Parts",
                    "content": {
                        "question": "Which technological innovation was pioneered in the United States and became crucial for modern assembly-line mass production?",
                        "options": [
                            "A. James Watt's Steam Engine, which utilized coal to generate mechanical rotary power.",
                            "B. James Hargreaves' Spinning Jenny, which automated hand spinning.",
                            "C. Eli Whitney's system of standardized interchangeable parts, allowing identical machine components to be assembled rapidly.",
                            "D. Richard Arkwright's Water Frame, which used water currents to power textile mills."
                        ],
                        "correct_answer": "C",
                        "explanation": "Standardized interchangeable parts (the American System) ensured any replacement part fit any machine of that model, making mass production and rapid repair possible."
                    }
                }
            ]
        ]
    },

    # =========================================================================
    # LESSON 2: Impacts on Africa
    # =========================================================================
    {
        "unit_order": 2,
        "unit_name": "Impacts on Africa",
        "unit_description": "The dual needs of European factories (raw materials & captive markets), forced labor, destruction of indigenous craft guilds, and extractive infrastructure.",
        "lesson_title": "Impacts on Africa",
        "pages": [
            # Card 1: Orientation & Hook
            [
                {
                    "type": "suggested_image",
                    "title": "Colonial Extraction and Forced Labor",
                    "content": {
                        "title": "Forced Rubber Extraction in the Congo Free State",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/cf/Congo_rubber_workers.jpg/800px-Congo_rubber_workers.jpg",
                        "caption": "Archival photo of African workers subjected to brutal quotas for wild rubber extraction to supply European industrial machinery and automobile tires.",
                        "author": "Wikimedia Commons",
                        "licensing": "Public Domain"
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "The Flip Side of Industrial Progress",
                    "content": {
                        "text": (
                            "While factories roared in Manchester and Birmingham, creating unprecedented wealth for European industrialists, the consequences on the African continent were devastating.\n\n"
                            "European mass production created two insatiable appetites:\n\n"
                            "1. **Raw Materials:** Massive demand for rubber (machine belts and tires), palm oil (machine lubricant), copper (electrical wiring), cotton, and minerals.\n"
                            "2. **Captive Consumer Markets:** Saturated European domestic markets required foreign territories to purchase surplus mass-produced manufactured goods."
                        )
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 2 Learning Goals",
                    "content": {
                        "text": (
                            "By the end of this lesson, you will be able to:\n\n"
                            "- Explain how European factory surpluses drove raw material extraction in Africa\n"
                            "- Analyze how cheap factory imports systematically undermined traditional African blacksmithing and weaving guilds\n"
                            "- Evaluate the extractive design of colonial railways and ports"
                        )
                    }
                }
            ],

            # Card 2: Extractive Impacts Matrix
            [
                {
                    "type": "comparison_table",
                    "title": "Multi-Dimensional Impacts of Industrialisation on African Societies",
                    "content": {
                        "headers": ["Area of Impact", "Colonial Policy & Mechanism", "Structural Impact on African Life"],
                        "rows": [
                            ["Resource Extraction", "Intensive mining and cash-crop plantations (rubber, palm oil, cotton)", "Depleted natural wealth with zero local processing; wealth shipped directly to Europe"],
                            ["Labor Systems", "Imposition of poll taxes, hut taxes, and forced labor quotas", "Disrupted food farming as adult men were forced into low-wage migrant labor"],
                            ["Indigenous Crafts", "Dumping cheap mass-produced British cotton cloth and iron hoes", "Completely destroyed traditional African iron-smelting guilds and hand-weaving arts"],
                            ["Infrastructure", "Railways constructed in straight lines from interior mines to coastal ports", "Created 'corridors of extraction' that failed to integrate domestic African regional trade"],
                            ["Political Governance", "Dismantling indigenous kingdoms and imposing direct/indirect rule", "Eroded traditional conflict-resolution barazas and installed unaccountable colonial chiefs"]
                        ]
                    }
                }
            ],

            # Card 3: Video Case Study
            [
                {
                    "type": "suggested_video",
                    "title": "Industrialisation and the Colonisation of Africa",
                    "content": {
                        "title": "How the Industrial Revolution Fueled African Colonisation",
                        "description": "Historical documentary examining the economic link between British industrial factory demand and the colonial partition of Africa.",
                        "youtube_id": "F3_6mF-yvR0"
                    }
                }
            ],

            # Card 4: Knowledge Check
            [
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check: Impact on Indigenous Crafts",
                    "content": {
                        "question": "How did the dumping of cheap, mass-produced European manufactured textiles affect traditional African economies?",
                        "options": [
                            "A. It stimulated African weavers to build their own industrial steam textile mills.",
                            "B. It had no impact because African communities completely boycotted European imports.",
                            "C. It undermined and destroyed traditional indigenous hand-weaving and iron-smelting guilds, as local artisans could not compete on price.",
                            "D. It allowed African traditional craftspeople to export handmade textiles to Europe at record profits."
                        ],
                        "correct_answer": "C",
                        "explanation": "Mass-produced factory cloth flooded African markets, undercutting local artisan guilds and forcing Africans into low-wage production of single raw cash crops."
                    }
                }
            ]
        ]
    },

    # =========================================================================
    # LESSON 3: Underdevelopment and African Responses
    # =========================================================================
    {
        "unit_order": 3,
        "unit_name": "Underdevelopment and African Responses",
        "unit_description": "Walter Rodney's thesis on structural underdevelopment, the cycle of capital outflow, and African agency through Pan-Africanism, cooperatives, and independent schools.",
        "lesson_title": "Underdevelopment and African Responses",
        "pages": [
            # Card 1: Orientation & Hook
            [
                {
                    "type": "suggested_image",
                    "title": "Pan-African Solidarity and Anti-Colonial Resistance",
                    "content": {
                        "title": "Pan-African Leaders and Intellectual Resistance",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/1945_Manchester_Pan-African_Congress.jpg/800px-1945_Manchester_Pan-African_Congress.jpg",
                        "caption": "Delegates at the 5th Pan-African Congress in Manchester (1945), organizing collective political and economic resistance against colonial exploitation.",
                        "author": "Wikimedia Commons",
                        "licensing": "Public Domain"
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "The Structural Manufacturing of Underdevelopment",
                    "content": {
                        "text": (
                            "Why did Europe become exceptionally wealthy while Africa became economically impoverished during the 19th and 20th centuries?\n\n"
                            "In his landmark 1972 historical work *How Europe Underdeveloped Africa*, historian **Walter Rodney** demonstrated that African poverty was not natural or accidental. It was a structural outcome of colonial capitalism: Africa was locked into supplying raw materials cheaply while importing expensive finished goods, draining capital continuously to Europe."
                        )
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 3 Learning Goals",
                    "content": {
                        "text": (
                            "By the end of this lesson, you will be able to:\n\n"
                            "- Explain Walter Rodney's core thesis on the manufacturing of underdevelopment\n"
                            "- Analyze the continuous feedback loop of capital extraction\n"
                            "- Identify four major forms of African agency: nationalist parties, Pan-Africanism, independent schools, and marketing cooperatives"
                        )
                    }
                }
            ],

            # Card 2: Cycle of Underdevelopment SVG Diagram
            [
                {
                    "type": "suggested_diagram",
                    "title": "The Structural Cycle of Underdevelopment",
                    "content": {
                        "title": "Walter Rodney's Underdevelopment Feedback Loop",
                        "caption": "Diagram depicting how raw material extraction, lack of domestic manufacturing, and captive export markets drained African capital to European financial centers.",
                        "svg_content": SVG_CYCLE_OF_UNDERDEVELOPMENT
                    }
                }
            ],

            # Card 3: Primary Source Analysis (Poem of Resistance)
            [
                {
                    "type": "concept_explanation",
                    "title": "Primary Source: Traditional Anti-Colonial Resistance Song",
                    "content": {
                        "text": (
                            "> *'Iron horses roared, and factories grew,*\n"
                            "> *Across the sea, a different view.*\n"
                            "> *Africa's riches, a tempting prize,*\n"
                            "> *Colonial chains, beneath harsh skies.*\n"
                            "> *But from the soil, a spirit strong,*\n"
                            "> *A fight for freedom, a righteous song.'*\n\n"
                            "**Historical Analysis:**\n"
                            "- **'Iron horses':** Refers to steam locomotives and railways used as tools of colonial extraction and military domination.\n"
                            "- **African Agency:** Proves that Africans were never passive victims; they used oral songs, strikes, independent churches/schools, and armed struggle to resist exploitation."
                        )
                    }
                },
                {
                    "type": "mini_activity",
                    "title": "Source Inquiry Task",
                    "content": {
                        "task": "How does this song contrast the European celebration of technological growth with the lived reality of African peasants forced into colonial labor?"
                    }
                }
            ],

            # Card 4: Video Case Study
            [
                {
                    "type": "suggested_video",
                    "title": "Walter Rodney and the Theory of Underdevelopment",
                    "content": {
                        "title": "How Europe Underdeveloped Africa Explained",
                        "description": "Educational lecture exploring Walter Rodney's economic history of colonial extraction, unequal exchange, and African resistance.",
                        "youtube_id": "78K3fQ94_7Y"
                    }
                }
            ],

            # Card 5: Knowledge Check
            [
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check: Underdevelopment Theory",
                    "content": {
                        "question": "Which of the following describes a key argument of Walter Rodney's 'underdevelopment' theory regarding colonial Africa?",
                        "options": [
                            "A. Africa was poor because its societies refused to trade or farm prior to European arrival.",
                            "B. Africa's resources and labor were structurally exploited to enrich European industrial economies, locking Africa into raw material dependency.",
                            "C. Underdevelopment was entirely caused by African geography and climate.",
                            "D. European colonial administrations reinvested 100% of mineral profits back into building local African factories."
                        ],
                        "correct_answer": "B",
                        "explanation": "Underdevelopment was an active historical process where colonial powers extracted wealth, suppressed local industrial skills, and drained profits to Europe."
                    }
                }
            ]
        ]
    },

    # =========================================================================
    # LESSON 4: Industrialisation and Colonisation
    # =========================================================================
    {
        "unit_order": 4,
        "unit_name": "Industrialisation and Colonisation",
        "unit_description": "The direct causal link from factory surplus to the Berlin Conference (1884–1885), industrial military technologies (Maxim gun, steamships, quinine), and the Uganda Railway case study.",
        "lesson_title": "Industrialisation and Colonisation",
        "pages": [
            # Card 1: Orientation & Hook
            [
                {
                    "type": "suggested_image",
                    "title": "The Partition of Africa (1914)",
                    "content": {
                        "title": "Colonial Partition Map of Africa in 1914",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/Scramble-for-Africa-1914.svg/800px-Scramble-for-Africa-1914.svg.png",
                        "caption": "Map showing the complete partition of Africa into European colonies following the Scramble, with only Ethiopia and Liberia retaining sovereign independence.",
                        "author": "Wikimedia Commons",
                        "licensing": "Public Domain"
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Connecting the Factory Floor to the Scramble for Africa",
                    "content": {
                        "text": (
                            "Why did European powers, who had traded informally along the African coast for four centuries, suddenly launch a massive military conquest to partition the entire continent between 1884 and 1914?\n\n"
                            "The Industrial Revolution provided both the **economic motivation** (surplus goods, raw materials, imperial rivalry) and the **technological means** (Maxim machine guns, shallow-draft river steamships, malaria-treating quinine, and electric telegraphs) to conquer the interior."
                        )
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 4 Learning Goals",
                    "content": {
                        "text": (
                            "By the end of this lesson, you will be able to:\n\n"
                            "- Trace the causal chain from domestic factory surplus to the Berlin Conference (1884–1885)\n"
                            "- Analyze how industrial technologies (Maxim gun, steamships, quinine) enabled interior military conquest\n"
                            "- Evaluate the Uganda Railway (1896–1901) as an industrial tool of colonial dominance and land alienation"
                        )
                    }
                }
            ],

            # Card 2: Industrial-to-Colonial Causal Flow SVG
            [
                {
                    "type": "suggested_diagram",
                    "title": "The Causal Chain: Industrial Expansion to Colonial Conquest",
                    "content": {
                        "title": "Factory Surplus to Military Partition",
                        "caption": "Flowchart tracing how domestic overproduction and imperial competition led to the Berlin Conference and military pacification using industrial weapons.",
                        "svg_content": SVG_INDUSTRIAL_TO_COLONIAL_CHAIN
                    }
                }
            ],

            # Card 3: Uganda Railway Case Study Table
            [
                {
                    "type": "comparison_table",
                    "title": "Case Study: The Uganda Railway (1896–1901) as an Industrial Tool",
                    "content": {
                        "headers": ["Railway Feature", "British Strategic Purpose", "Lived Impact on African Sovereignty"],
                        "rows": [
                            ["Mombasa to Kisumu Route", "Securing strategic headwaters of the Nile River to protect the Suez route to India", "Suppressed local sovereignty as British troops were transported rapidly inland to defeat Nandi resistance"],
                            ["Highland Corridor", "Transporting export cash crops (tea, coffee, sisal) cheaply from the fertile highlands", "Massive land alienation; fertile ancestral lands confiscated from Kikuyu and Maasai for white settlers"],
                            ["Inward Goods Flow", "Flooding interior markets with British mass-produced manufactured wares", "Undermined local artisan guilds and locked the Kenyan economy into single-crop export dependency"]
                        ]
                    }
                }
            ],

            # Card 4: Video Case Study
            [
                {
                    "type": "suggested_video",
                    "title": "The Scramble for Africa and Colonial Partition",
                    "content": {
                        "title": "The Berlin Conference and the Scramble for Africa",
                        "description": "Educational documentary examining how European imperial powers partitioned the African continent during the late 19th century.",
                        "youtube_id": "2r1o5Xb1pQk"
                    }
                }
            ],

            # Card 5: Knowledge Check & Synthesis Essay
            [
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check: Technologies of Interior Conquest",
                    "content": {
                        "question": "Which pair of industrial technologies was most vital in allowing Europeans to navigate tropical African rivers and survive malaria in the interior?",
                        "options": [
                            "A. The Spinning Jenny and the steam-powered textile loom.",
                            "B. Shallow-draft steamships and the medical discovery of quinine.",
                            "C. Eli Whitney's cotton gin and standardized interchangeable parts.",
                            "D. The electric telegraph and deep coastal canals."
                        ],
                        "correct_answer": "B",
                        "explanation": "Shallow-draft steamships enabled navigation against river rapids, while quinine protected European soldiers from deadly malaria in the interior."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Topic-End Synthesis Essay Challenge",
                    "content": {
                        "text": (
                            "**Essay Prompt:**\n"
                            "> *'Analyze the direct relationship between the First Industrial Revolution in Europe and the underdevelopment of Africa in the 19th and 20th centuries. Contrast the enabling factors of industrialization in Britain/USA with their extractive impacts on Africa, and explain how Africans mobilized agency to resist.'*\n\n"
                            "**Structuring Guide:** Focus on factory surplus (markets/materials), technological conquest enablers (Maxim gun/quinine), Walter Rodney's cycle of underdevelopment, and African nationalist resistance."
                        )
                    }
                }
            ]
        ]
    }
]
