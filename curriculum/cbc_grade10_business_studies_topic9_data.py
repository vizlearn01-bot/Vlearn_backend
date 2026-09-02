"""
VLearn CBC Grade 10 Business Studies — Topic 9: Production
Full Structured Lesson Card Definitions (Lessons 1 to 9)
Decomposed into 8 atomic pedagogical cards per lesson with zero bracket citations,
complete responsive SVGs, verified Wikimedia visual hooks, and KaTeX math formulas.
"""

from curriculum.cbc_grade10_business_studies_topic9_svgs import (
    SVG_MEANING_AND_UTILITIES,
    SVG_FACTORS_OF_PRODUCTION,
    SVG_PRODUCTION_COST_CURVES,
    SVG_COST_DECISION_TREE,
    SVG_DIVISION_OF_LABOUR_PIPELINE,
    SVG_TYPES_OF_SPECIALISATION,
    SVG_PRODUCER_RESPONSIBILITIES,
    SVG_PRODUCT_LABEL_ANATOMY,
    SVG_MACRO_PRODUCTION_CIRCULAR_FLOW
)

TOPIC_9_LESSONS = [
    # =========================================================================
    # LESSON 1: Meaning and Importance of Production
    # =========================================================================
    {
        "unit_order": 1,
        "unit_name": "Meaning and Importance of Production",
        "unit_description": "Definition of production, creation of economic utility (form, place, time, possession), and its core contributions to economic wealth.",
        "lesson_title": "Meaning and Importance of Production",
        "pages": [
            # Card 1: Photographic Hook & Learning Goals
            [
                {
                    "type": "suggested_image",
                    "title": "Kisii Soapstone Artisan Workshop",
                    "content": {
                        "title": "Manual Transformation of Natural Resources in Kenya",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/d/db/Person_hand-carving_carving_soapstone_trinket_box%2C_Tabaka_Hills%2C_Kenya.jpg",
                        "caption": "An artisan in Tabaka Hills, Kisii County, meticulously hand-carving raw soapstone rock into polished sculptures, illustrating the transformation of raw materials into finished goods.",
                        "author": "Wikimedia Commons",
                        "licensing": "CC BY-SA 4.0"
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 1 Learning Outcomes",
                    "content": {
                        "text": "By the end of this lesson, you will be able to:\n\n- Define production in economic terms\n- Distinguish between tangible goods and intangible services\n- Explain the 4 types of utility created by production (Form, Place, Time, Possession)\n- Analyze the importance of production in employment, income generation, and national GDP"
                    }
                }
            ],
            # Card 2: Formal Definitions & Core Concepts
            [
                {
                    "type": "definition_card",
                    "title": "Production and Economic Utility",
                    "content": {
                        "term": "Production",
                        "definition": "The systematic economic process of converting raw natural resources and factor inputs into finished goods and services that satisfy human needs and wants."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Goods, Services, and Utility Creation",
                    "content": {
                        "text": "Production is not merely manufacturing physical items; it encompasses all activities that create **utility** (the want-satisfying power of a commodity).\n\n- **Tangible Goods**: Physical items that can be seen, touched, and stored (e.g., carved soapstone sculptures, classroom desks, maize flour).\n- **Intangible Services**: Beneficial human actions or expertise that satisfy needs without transferring physical ownership (e.g., teaching, freight transport, healthcare, commercial banking).\n- **Economic Utility**: Raw rocks in a quarry have low utility. By carving, transporting, storing, and selling them, businesses add value at every stage."
                    }
                }
            ],
            # Card 3: Deep-Dive Breakdown & Vector Diagram
            [
                {
                    "type": "suggested_diagram",
                    "title": "The 4 Types of Utility Created by Production",
                    "content": {
                        "title": "Production Transformation Engine & Utility Architecture",
                        "caption": "Vector diagram illustrating how the production engine converts raw inputs into Form, Place, Time, and Possession utility.",
                        "svg_content": SVG_MEANING_AND_UTILITIES
                    }
                }
            ],
            # Card 4: Comparative Matrix of Utility Types
            [
                {
                    "type": "comparison_table",
                    "title": "The 4 Types of Economic Utility",
                    "content": {
                        "headers": ["Type of Utility", "Core Mechanism", "Primary Business Activity", "Kenyan Enterprise Example"],
                        "rows": [
                            ["Form Utility", "Altering physical structure and appearance", "Manufacturing & Processing", "Carving Tabaka soapstone into animal figurines; Sawing timber into chairs"],
                            ["Place Utility", "Moving goods from production site to consumers", "Transportation & Logistics", "Transporting Kericho tea to Mombasa port; Hauling Naivasha flowers to JKIA"],
                            ["Time Utility", "Storing surplus commodities until scarcity", "Warehousing & Preservation", "Preserving maize harvests in NCPB grain silos; Cold storage for dairy milk"],
                            ["Possession Utility", "Transferring legal ownership from seller to buyer", "Trade & Commercial Retailing", "Purchasing groceries at a supermarket; Transferring vehicle logbooks"]
                        ]
                    }
                }
            ],
            # Card 5: Step-by-Step Worked Example
            [
                {
                    "type": "worked_example",
                    "title": "Worked Example: Value Addition & Utility Analysis in Agribusiness",
                    "content": {
                        "intro": "A farmers' cooperative in Murang'a harvests 10,000 kg of raw mangoes valued at KES 20 per kg at the farm gate. They process 6,000 kg into bottled mango juice selling at KES 120 per liter (requiring 1.5 kg of fruit per liter), and transport the remaining 4,000 kg of fresh fruit to retail markets in Nairobi selling at KES 50 per kg.",
                        "steps": [
                            "**Step 1 — Understand what we are finding:** Calculate the initial raw harvest value, the processed juice value (Form Utility), the transported fresh fruit value (Place Utility), and the total economic value added by production.",
                            "**Step 2 — Identify given information:**\n- Total harvest = $10,000\\text{ kg}$\n- Farm gate price = $\\text{KES } 20\\text{ per kg}$\n- Processing allocation = $6,000\\text{ kg}$ fruit $\\rightarrow 6,000 / 1.5 = 4,000\\text{ liters juice}$\n- Juice retail price = $\\text{KES } 120\\text{ per liter}$\n- Fresh fruit transported = $4,000\\text{ kg}$ at $\\text{KES } 50\\text{ per kg}$",
                            "**Step 3 — Choose the formulas:**\n$$\\text{Initial Value} = \\text{Total kg} \\times \\text{Farm Gate Price}$$\n$$\\text{Form Utility Value} = \\text{Liters} \\times \\text{Juice Price}$$\n$$\\text{Place Utility Value} = \\text{Kg Transported} \\times \\text{Nairobi Price}$$\n$$\\text{Total Value Added} = (\\text{Juice Value} + \\text{Transported Fruit Value}) - \\text{Initial Value}$$",
                            "**Step 4 — Perform the calculations step by step:**\n- Initial raw harvest value: $10,000 \\times 20 = \\text{KES } 200,000$\n- Processed juice revenue: $4,000\\text{ liters} \\times 120 = \\text{KES } 480,000$\n- Transported fresh fruit revenue: $4,000\\text{ kg} \\times 50 = \\text{KES } 200,000$\n- Total final revenue: $480,000 + 200,000 = \\text{KES } 680,000$\n- Value added: $680,000 - 200,000 = \\text{KES } 480,000$",
                            "**Step 5 — State the final answer:** Production generated an extra $\\mathbf{\\text{KES } 480,000}$ in economic wealth (a $240\\%$ increase over the raw farm gate value).",
                            "**Step 6 — Economic Interpretation & Pitfall:** Selling unprocessed raw commodities locks farmers into low earnings. By adding Form Utility (processing) and Place Utility (transporting), enterprises dramatically increase revenue and create stable local jobs."
                        ]
                    }
                }
            ],
            # Card 6: Kenyan Case Study & Video
            [
                {
                    "type": "real_world_example",
                    "title": "Kenyan Enterprise Case: Tabaka Soapstone Artisans Cooperative",
                    "content": {
                        "title": "From Dusty Rocks to Global Export Art in Kisii",
                        "text": "In Tabaka, Kisii County, over 5,000 artisans belong to cooperative societies. Raw soapstone mined from local quarries is transformed through skilled carving, water sanding, and natural dyeing into sculptures exported to Europe and the United States. This local production creates all 4 utilities: changing raw rock shape (Form), shipping worldwide (Place), storing seasonal carvings (Time), and selling to tourists (Possession), sustaining the regional economy."
                    }
                },
                {
                    "type": "suggested_video",
                    "title": "Understanding Production and Economic Utility",
                    "content": {
                        "title": "Production Process and the Creation of Utility",
                        "youtube_id": "v83s92y5Tq4",
                        "url": "https://www.youtube.com/watch?v=v83s92y5Tq4",
                        "description": "Educational lesson examining how production converts raw natural factors into economic goods and services by creating form, place, time, and possession utility."
                    }
                }
            ],
            # Card 7: Formative Scenario-Based MCQs
            [
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 1: Identifying Form Utility",
                    "content": {
                        "question": "A dairy cooperative in Nyandarua collects 20,000 liters of raw milk daily and converts it into pasteurized butter, yogurt, and packaged cheese. What specific type of economic utility has been created by this process?",
                        "options": [
                            "Place Utility",
                            "Form Utility",
                            "Possession Utility",
                            "Time Utility"
                        ],
                        "correct": "B",
                        "explanation": "Form utility is created by altering the physical structure, composition, or state of raw materials to make them more useful and valuable. Converting raw milk into butter, cheese, and yogurt changes its physical form."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 2: Time Utility in National Reserves",
                    "content": {
                        "question": "The National Cereals and Produce Board (NCPB) purchases surplus maize from Kitale farmers during the December harvest and preserves it in hermetic silos for distribution during the dry planting season in July. Which economic utility is being demonstrated?",
                        "options": [
                            "Time Utility",
                            "Place Utility",
                            "Form Utility",
                            "Direct Utility"
                        ],
                        "correct": "A",
                        "explanation": "Time utility is created by storing surplus goods during harvest abundance and making them available during periods of scarcity or high consumer demand."
                    }
                }
            ],
            # Card 8: Synthesis & Key Takeaways
            [
                {
                    "type": "key_takeaway",
                    "title": "Lesson 1 Summary & Key Takeaways",
                    "content": {
                        "text": "1. **Definition**: Production is the economic process of combining factor inputs to produce want-satisfying goods and services.\n2. **The 4 Utilities**: Production creates Form (shape), Place (location), Time (storage), and Possession (ownership) utility.\n3. **Economic Engine**: Production generates employment, distributes factor income, increases national output (GDP), and improves living standards."
                    }
                }
            ]
        ]
    },

    # =========================================================================
    # LESSON 2: Factors of Production
    # =========================================================================
    {
        "unit_order": 2,
        "unit_name": "Factors of Production",
        "unit_description": "The four foundational pillars of enterprise output: Land (Rent), Labour (Wages), Capital (Interest), and Entrepreneurship (Profit).",
        "lesson_title": "Factors of Production",
        "pages": [
            # Card 1: Photographic Hook & Learning Goals
            [
                {
                    "type": "suggested_image",
                    "title": "Tea Plucking at Kericho Tea Estate",
                    "content": {
                        "title": "Combining Natural Resources and Human Labour in Kericho",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/1/1f/KER_-_Tea_pickers_working_near_Kericho%2C_Kenya%2C_2012.jpg",
                        "caption": "Tea pluckers harvesting fresh tea leaves in Kericho County, demonstrating the combination of fertile natural land, human labour, and processing capital.",
                        "author": "Wikimedia Commons",
                        "licensing": "CC BY-SA 4.0"
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 2 Learning Outcomes",
                    "content": {
                        "text": "By the end of this lesson, you will be able to:\n\n- Identify the four factors of production: Land, Labour, Capital, and Entrepreneurship\n- Describe the key characteristics and limitations of each factor\n- State the specific financial reward for each factor (Rent, Wages, Interest, Profit)\n- Explain factor interdependence in commercial enterprise operations"
                    }
                }
            ],
            # Card 2: Formal Definitions & Factor Descriptions
            [
                {
                    "type": "definition_card",
                    "title": "Factors of Production",
                    "content": {
                        "term": "Factors of Production",
                        "definition": "The essential economic resources and inputs required to produce goods and services, classified into Land, Labour, Capital, and Entrepreneurship."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "The Four Essential Pillars and Their Rewards",
                    "content": {
                        "text": "Production cannot occur in isolation; it requires combining four interdependent factors:\n\n- **Land (Natural Resources)**: All free gifts of nature on, above, or below the earth (soil, rivers, minerals, climate). Earns **Rent**.\n- **Labour (Human Effort)**: The physical and mental effort exerted by human workers. Earns **Wages** or **Salaries**.\n- **Capital (Man-Made Assets)**: Physical tools, machinery, buildings, and transport equipment used to produce other goods. Earns **Interest**.\n- **Entrepreneurship (Enterprise & Risk)**: The human drive that organizes the other three factors, makes decisions, and bears commercial risks. Earns **Profit**."
                    }
                }
            ],
            # Card 3: Deep-Dive Breakdown & Vector Diagram
            [
                {
                    "type": "suggested_diagram",
                    "title": "The 4 Factors of Production & Factor Rewards",
                    "content": {
                        "title": "Factors of Production Architecture & Factor Rewards",
                        "caption": "Vector diagram breaking down the 4 pillars of production, their distinct characteristics, and their economic rewards.",
                        "svg_content": SVG_FACTORS_OF_PRODUCTION
                    }
                }
            ],
            # Card 4: Detailed Factor Comparison Table
            [
                {
                    "type": "comparison_table",
                    "title": "Characteristics, Roles, and Rewards of Factors of Production",
                    "content": {
                        "headers": ["Factor", "Primary Definition", "Key Characteristics", "Economic Reward", "Kenyan Examples"],
                        "rows": [
                            ["Land", "Natural resources provided freely by nature", "Fixed in supply, geographically immobile, passive, subject to diminishing returns", "Rent / Royalties", "Kericho fertile soils, Lake Victoria fishing waters, Olkaria geothermal steam"],
                            ["Labour", "Physical and mental human effort", "Human and living, perishable (lost if unused), heterogeneous skills, mobile", "Wages / Salaries", "Tea pluckers, factory technicians, software engineers, accountants"],
                            ["Capital", "Man-made physical assets used in production", "Man-made, depreciates over time, multiplies labour productivity, requires maintenance", "Interest", "Commercial tractors, tea processing machinery, SGR cargo wagons, computers"],
                            ["Entrepreneurship", "Organization, management, and risk-bearing", "Initiates enterprise, combines inputs, bears financial risks, drives innovation", "Profit (or Loss)", "Wanjiku (Tailor), James Mwangi (Banking), local agri-business founders"]
                        ]
                    }
                }
            ],
            # Card 5: Step-by-Step Worked Example
            [
                {
                    "type": "worked_example",
                    "title": "Worked Example: Calculating Total Factor Payment Budget",
                    "content": {
                        "intro": "Baraka Furniture Workshop in Nakuru manufactures school desks. In a month, the workshop pays factory plot rent of KES 25,000, employs 4 carpenters earning KES 30,000 each, pays interest on an equipment loan of KES 15,000, and spends KES 60,000 on raw timber and hardware. The owner sells 100 desks at KES 2,800 each.",
                        "steps": [
                            "**Step 1 — Understand what we are finding:** Calculate total revenue, factor payments (Rent, Labour Wages, Capital Interest, Raw Materials), and the entrepreneur's residual profit.",
                            "**Step 2 — Identify given information:**\n- Revenue = $100\\text{ desks} \\times \\text{KES } 2,800 = \\text{KES } 280,000$\n- Land reward (Plot Rent) = $\\text{KES } 25,000$\n- Labour reward (4 carpenters) = $4 \\times 30,000 = \\text{KES } 120,000$\n- Capital reward (Loan Interest) = $\\text{KES } 15,000$\n- Intermediate raw material inputs = $\\text{KES } 60,000$",
                            "**Step 3 — Choose the formulas:**\n$$\\text{Total Expenses} = \\text{Rent} + \\text{Labour} + \\text{Interest} + \\text{Materials}$$\n$$\\text{Entrepreneur's Profit} = \\text{Total Revenue} - \\text{Total Expenses}$$",
                            "**Step 4 — Perform the calculations step by step:**\n- Total operational expenses: $25,000 + 120,000 + 15,000 + 60,000 = \\text{KES } 220,000$\n- Residual profit for entrepreneur: $280,000 - 220,000 = \\text{KES } 60,000$",
                            "**Step 5 — State the final answer:** The entrepreneur receives a monthly profit reward of $\\mathbf{\\text{KES } 60,000}$ after paying all other factor rewards (Rent KES 25,000, Wages KES 120,000, Interest KES 15,000).",
                            "**Step 6 — Economic Interpretation & Pitfall:** Notice that Rent, Wages, and Interest are fixed contractual obligations that must be paid regardless of performance. Profit is the residual reward—it can be positive or negative (loss) if sales drop."
                        ]
                    }
                }
            ],
            # Card 6: Kenyan Case Study & Video
            [
                {
                    "type": "real_world_example",
                    "title": "Kenyan Enterprise Case: Kapset Tea Estate, Kericho",
                    "content": {
                        "title": "Factor Harmony on the Rolling Hills of the Great Rift Valley",
                        "text": "Kapset Tea Estate in Kericho illustrates factor synergy in large-scale agribusiness. The fertile volcanic soil and rainfall represent Land. Thousands of trained pluckers represent Labour. The multi-million shilling processing factory with CTC (Cut, Tear, Curl) drying machines and transport lorries represents Capital. The estate managers and directors who coordinate these resources and market Kenyan tea on the Mombasa Tea Auction represent Entrepreneurship."
                    }
                },
                {
                    "type": "suggested_video",
                    "title": "The Four Factors of Production Explained",
                    "content": {
                        "title": "Land, Labour, Capital, and Entrepreneurship in Business",
                        "youtube_id": "qgVFkRn8f10",
                        "url": "https://www.youtube.com/watch?v=qgVFkRn8f10",
                        "description": "Comprehensive video breaking down the four factors of production, their unique economic characteristics, and their factor rewards."
                    }
                }
            ],
            # Card 7: Formative Scenario-Based MCQs
            [
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 1: Characteristics of Land",
                    "content": {
                        "question": "Which of the following is a fundamental characteristic of land as a factor of production?",
                        "options": [
                            "It can be easily manufactured and increased in total quantity",
                            "It is geographically immobile and fixed in total supply",
                            "It earns wages as its primary economic reward",
                            "It produces finished output without requiring any human effort"
                        ],
                        "correct": "B",
                        "explanation": "Land is a gift of nature that is fixed in total physical supply and cannot be physically moved from one geographical location to another. It is also a passive factor requiring labour to produce output."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 2: The Perishable Nature of Labour",
                    "content": {
                        "question": "A construction company in Mombasa suffers a 3-day site strike where workers stay away from the job site. Why is labour described as 'perishable' in this economic scenario?",
                        "options": [
                            "The cement and concrete bags on site will rot immediately",
                            "The lost working hours and productive capacity during the strike cannot be stored or recovered in the future",
                            "The workers will permanently forget how to operate construction machinery",
                            "The financial interest paid to the bank will become zero"
                        ],
                        "correct": "B",
                        "explanation": "Labour is perishable because if a worker's capacity is not used on a given day, that time and effort are lost forever. Unlike physical goods, human labour capacity cannot be saved or warehoused for future use."
                    }
                }
            ],
            # Card 8: Synthesis & Key Takeaways
            [
                {
                    "type": "key_takeaway",
                    "title": "Lesson 2 Summary & Key Takeaways",
                    "content": {
                        "text": "1. **The 4 Factors**: Production requires Land (Natural), Labour (Human effort), Capital (Tools/Machinery), and Entrepreneurship (Management/Risk).\n2. **Factor Rewards**: Land earns Rent; Labour earns Wages; Capital earns Interest; Entrepreneurship earns Profit.\n3. **Interdependence**: Production is impossible if any single factor is missing; sustainable growth requires balanced investment in all four pillars."
                    }
                }
            ]
        ]
    },

    # =========================================================================
    # LESSON 3: Costs in a Production Unit
    # =========================================================================
    {
        "unit_order": 3,
        "unit_name": "Costs in a Production Unit",
        "unit_description": "Accounting and economic cost structures: Fixed Costs (TFC), Variable Costs (TVC), Total Cost (TC), and Unit Costs (AFC, AVC, ATC).",
        "lesson_title": "Costs in a Production Unit",
        "pages": [
            # Card 1: Photographic Hook & Learning Goals
            [
                {
                    "type": "suggested_image",
                    "title": "Tailoring Workshop in Kenya",
                    "content": {
                        "title": "Operational Costs in a Small Manufacturing Enterprise",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/d/d5/A_tailor_at_her_workshop.jpg",
                        "caption": "A tailor operating sewing machines and fabric stock in a production workshop, illustrating fixed workshop rent and variable material costs.",
                        "author": "Wikimedia Commons",
                        "licensing": "CC BY-SA 4.0"
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 3 Learning Outcomes",
                    "content": {
                        "text": "By the end of this lesson, you will be able to:\n\n- Distinguish between Fixed Costs (TFC) and Variable Costs (TVC)\n- Calculate Total Cost ($TC = TFC + TVC$)\n- Calculate Average Fixed Cost (AFC), Average Variable Cost (AVC), and Average Total Cost (ATC)\n- Explain how expanding output generates Economies of Scale by lowering unit costs"
                    }
                }
            ],
            # Card 2: Formal Definitions & Cost Classifications
            [
                {
                    "type": "definition_card",
                    "title": "Production Costs & Short-Run Cost Structures",
                    "content": {
                        "term": "Production Costs",
                        "definition": "The total monetary expenses incurred by an enterprise to acquire factor inputs and produce a specific quantity of goods or services."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Fixed Costs vs. Variable Costs",
                    "content": {
                        "text": "In the short run, enterprise costs are classified into two major categories:\n\n- **Total Fixed Costs (TFC / Overheads)**: Expenses that do not vary with output volume. They must be paid in full even if production is zero (e.g., shop rent, business license, security guard salary, equipment loan interest).\n- **Total Variable Costs (TVC / Direct Costs)**: Expenses that increase or decrease directly with the volume of goods produced (e.g., fabric, thread, buttons, raw milk, packaging bags, piece-rate wages).\n- **Total Cost (TC)**: The complete expenditure incurred: $TC = TFC + TVC$."
                    }
                }
            ],
            # Card 3: Deep-Dive Breakdown & Vector Diagram
            [
                {
                    "type": "suggested_diagram",
                    "title": "Short-Run Cost Curves & Mathematical Formulas",
                    "content": {
                        "title": "Cost Curves Behavior & Formulas",
                        "caption": "Vector diagram illustrating the horizontal TFC line, upward sloping TVC and TC curves, and the unit cost formulas (AFC, AVC, ATC).",
                        "svg_content": SVG_PRODUCTION_COST_CURVES
                    }
                }
            ],
            # Card 4: Cost Classification & Formula Reference Table
            [
                {
                    "type": "comparison_table",
                    "title": "Cost Metric Formulas and Short-Run Behavior",
                    "content": {
                        "headers": ["Cost Metric", "Mathematical Formula", "Behavior as Output (Q) Increases", "Managerial Purpose"],
                        "rows": [
                            ["Total Fixed Cost (TFC)", "TFC = Constant", "Remains unchanged regardless of output", "Establishes base overhead burden"],
                            ["Total Variable Cost (TVC)", "TVC = Q × AVC", "Increases steadily with output", "Calculates direct operational expenses"],
                            ["Total Cost (TC)", "TC = TFC + TVC", "Increases as TVC increases", "Determines complete enterprise spending"],
                            ["Average Fixed Cost (AFC)", "AFC = TFC / Q", "Continuously decreases (approaches zero)", "Spreads fixed overheads over more units"],
                            ["Average Variable Cost (AVC)", "AVC = TVC / Q", "Usually constant in normal capacity", "Sets minimum price floor in short run"],
                            ["Average Total Cost (ATC)", "ATC = TC / Q = AFC + AVC", "Decreases initially (Economies of Scale)", "Determines profit margin per unit ($P - ATC$)"]
                        ]
                    }
                }
            ],
            # Card 5: Step-by-Step Worked Cost Calculation
            [
                {
                    "type": "worked_example",
                    "title": "Worked Example: Comprehensive Cost Table for Wanjiku's Tailoring Shop",
                    "content": {
                        "intro": "Wanjiku operates a school uniform tailoring shop in Eldoret. Her shop rent and equipment depreciation (TFC) total KES 10,000 per month. The fabric, buttons, and tailor wages (AVC) cost KES 500 per uniform. Complete the cost schedule for output levels of Q = 0, Q = 20, and Q = 50 uniforms.",
                        "steps": [
                            "**Step 1 — Understand what we are finding:** Calculate Total Fixed Cost (TFC), Total Variable Cost (TVC), Total Cost (TC), Average Fixed Cost (AFC), Average Variable Cost (AVC), and Average Total Cost (ATC) for $Q = 0, 20, 50$.",
                            "**Step 2 — Identify given information:**\n- $\\text{TFC} = \\text{KES } 10,000$ (constant)\n- $\\text{Variable cost per unit (AVC)} = \\text{KES } 500$",
                            "**Step 3 — Choose the formulas:**\n$$\\text{TVC} = Q \\times 500$$\n$$\\text{TC} = \\text{TFC} + \\text{TVC} = 10,000 + \\text{TVC}$$\n$$\\text{AFC} = \\frac{\\text{TFC}}{Q} = \\frac{10,000}{Q}$$\n$$\\text{ATC} = \\frac{\\text{TC}}{Q} = \\text{AFC} + \\text{AVC}$$",
                            "**Step 4 — Perform the calculations step by step:**\n- **For Q = 0 uniforms:**\n  - $\\text{TVC} = 0 \\times 500 = \\text{KES } 0$\n  - $\\text{TC} = 10,000 + 0 = \\text{KES } 10,000$\n  - $\\text{AFC, AVC, ATC} = \\text{Undefined (cannot divide by zero)}$\n\n- **For Q = 20 uniforms:**\n  - $\\text{TVC} = 20 \\times 500 = \\text{KES } 10,000$\n  - $\\text{TC} = 10,000 + 10,000 = \\text{KES } 20,000$\n  - $\\text{AFC} = \\frac{10,000}{20} = \\text{KES } 500$\n  - $\\text{ATC} = \\frac{20,000}{20} = \\text{KES } 1,000\\text{ per uniform}$\n\n- **For Q = 50 uniforms:**\n  - $\\text{TVC} = 50 \\times 500 = \\text{KES } 25,000$\n  - $\\text{TC} = 10,000 + 25,000 = \\text{KES } 35,000$\n  - $\\text{AFC} = \\frac{10,000}{50} = \\text{KES } 200$\n  - $\\text{ATC} = \\frac{35,000}{50} = \\text{KES } 700\\text{ per uniform}$",
                            "**Step 5 — State the final answer:**\n| Quantity (Q) | TFC (KES) | TVC (KES) | TC (KES) | AFC (KES) | AVC (KES) | ATC (KES) |\n| :---: | :---: | :---: | :---: | :---: | :---: | :---: |\n| **0** | 10,000 | 0 | 10,000 | - | - | - |\n| **20** | 10,000 | 10,000 | 20,000 | 500 | 500 | **1,000** |\n| **50** | 10,000 | 25,000 | 35,000 | 200 | 500 | **700** |",
                            "**Step 6 — Economic Interpretation & Pitfall:** Expanding production from 20 to 50 uniforms cuts unit cost from **KES 1,000 to KES 700**! This is **Economies of Scale** in action. Avoid the common pitfall of assuming fixed costs increase with output; fixed costs stay constant at KES 10,000."
                        ]
                    }
                }
            ],
            # Card 6: Kenyan Case Study & Video
            [
                {
                    "type": "real_world_example",
                    "title": "Kenyan Enterprise Case: Eldoret School Uniform Factory",
                    "content": {
                        "title": "Overhead Dilution & Competitive Bulk Pricing",
                        "text": "Small tailoring kiosks that make only 10 uniforms a month have high unit costs because workshop rent is spread over very few pieces. In contrast, large industrial uniform producers in Eldoret produce 5,000 uniforms monthly. By spreading factory rent and power bills over thousands of units, their average fixed cost drops to under KES 30 per shirt, allowing them to supply schools across the North Rift at highly competitive prices."
                    }
                },
                {
                    "type": "suggested_video",
                    "title": "Fixed vs Variable Costs and Total Cost Calculations",
                    "content": {
                        "title": "Understanding Short-Run Cost Structures in Business",
                        "youtube_id": "WqlX5z6k4eQ",
                        "url": "https://www.youtube.com/watch?v=WqlX5z6k4eQ",
                        "description": "Step-by-step video tutorial demonstrating how to calculate Fixed Costs, Variable Costs, Total Costs, and Unit Average Costs in business."
                    }
                }
            ],
            # Card 7: Formative Scenario-Based MCQs
            [
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 1: Behavior of Average Fixed Cost",
                    "content": {
                        "question": "A commercial bakery in Nakuru increases its daily bread output from 500 loaves to 2,000 loaves. What happens to its Average Fixed Cost (AFC)?",
                        "options": [
                            "It quadruples because production has multiplied by 4",
                            "It remains unchanged because total fixed costs are constant",
                            "It decreases because the same total fixed cost is divided across 2,000 loaves",
                            "It immediately drops to zero"
                        ],
                        "correct": "C",
                        "explanation": "Average Fixed Cost ($AFC = TFC / Q$) always declines as output increases because the fixed rent and loan costs are spread over a larger quantity of products."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 2: Calculating Total Cost at Zero Output",
                    "content": {
                        "question": "A small shoe workshop in Nairobi has a monthly shop rent of KES 18,000 and machine lease of KES 7,000. If the workshop produces 0 pairs of shoes in April during renovation, what is its Total Cost for April?",
                        "options": [
                            "KES 0",
                            "KES 7,000",
                            "KES 18,000",
                            "KES 25,000"
                        ],
                        "correct": "D",
                        "explanation": "At zero output ($Q = 0$), Variable Costs are KES 0, but Total Fixed Costs ($18,000 + 7,000 = \\text{KES } 25,000$) must still be paid in full. Therefore, $TC = TFC + 0 = \\text{KES } 25,000$."
                    }
                }
            ],
            # Card 8: Synthesis & Key Takeaways
            [
                {
                    "type": "key_takeaway",
                    "title": "Lesson 3 Summary & Key Takeaways",
                    "content": {
                        "text": "1. **Fixed vs Variable**: TFC stays constant regardless of output; TVC changes directly with the number of units produced.\n2. **Total Cost Formula**: $TC = TFC + TVC$; at zero production, $TC = TFC$.\n3. **Unit Cost Spreading**: As output expands, AFC falls, pulling down Average Total Cost (ATC) and creating Economies of Scale."
                    }
                }
            ]
        ]
    },

    # =========================================================================
    # LESSON 4: Cost Interpretation and Decisions
    # =========================================================================
    {
        "unit_order": 4,
        "unit_name": "Cost Interpretation and Decisions",
        "unit_description": "Managerial decision making: Evaluating special bulk orders, capacity utilization, and contribution margin pricing.",
        "lesson_title": "Cost Interpretation and Decisions",
        "pages": [
            # Card 1: Photographic Hook & Learning Goals
            [
                {
                    "type": "suggested_image",
                    "title": "Jua Kali Manufacturing Workshop",
                    "content": {
                        "title": "Operational Capacity and Commercial Pricing Decisions",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/3/36/Jua_Kali_fabricator.jpg",
                        "caption": "Artisans in an informal Kenyan workshop assessing material costs and orders, demonstrating capacity utilization and cost-based decision making.",
                        "author": "Harold Odhiambo Otieno",
                        "licensing": "CC BY-SA 4.0"
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 4 Learning Outcomes",
                    "content": {
                        "text": "By the end of this lesson, you will be able to:\n\n- Define capacity utilization and identify spare production capacity\n- Distinguish between Average Total Cost (ATC) and Average Variable Cost (AVC) in decision making\n- Apply the Contribution Margin Rule to evaluate special discounted bulk orders\n- Make economically sound business decisions that protect cash flow and enhance profit"
                    }
                }
            ],
            # Card 2: Formal Definitions & Core Decision Principles
            [
                {
                    "type": "definition_card",
                    "title": "Capacity Utilization and Contribution Margin",
                    "content": {
                        "term": "Capacity Utilization",
                        "definition": "The extent to which an enterprise operates its productive assets (machinery, factory space, labor hours) compared to its maximum potential output."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "The Special Order Pricing Dilemma",
                    "content": {
                        "text": "When an enterprise has **spare (idle) capacity**, standard Average Total Cost (ATC) can lead to flawed business decisions:\n\n- **The Pitfall**: Comparing a special discounted bulk offer against ATC (which includes already-paid rent) makes profitable deals look like losses.\n- **The Economic Principle**: Fixed costs (TFC) are already paid by standard sales. To make extra units using idle machines, the business only incurs **Variable Costs (AVC)**.\n- **Contribution Margin**: Any offer price ($P$) higher than Average Variable Cost ($P > AVC$) generates positive cash contribution toward fixed overheads and increases net enterprise profit."
                    }
                }
            ],
            # Card 3: Deep-Dive Breakdown & Vector Diagram
            [
                {
                    "type": "suggested_diagram",
                    "title": "Special Bulk Order & Capacity Decision Framework",
                    "content": {
                        "title": "Managerial Special Order Decision Tree",
                        "caption": "Vector diagram illustrating the logical decision path for evaluating discounted bulk orders based on spare capacity and variable cost comparison.",
                        "svg_content": SVG_COST_DECISION_TREE
                    }
                }
            ],
            # Card 4: Comparative Matrix of Decision Scenarios
            [
                {
                    "type": "comparison_table",
                    "title": "Managerial Decision Matrix for Special Orders",
                    "content": {
                        "headers": ["Scenario Condition", "Comparison Test", "Recommended Action", "Financial Rationale"],
                        "rows": [
                            ["Spare Capacity + High Offer", "Offer Price > Average Variable Cost ($P > AVC$)", "ACCEPT ORDER", "Generates positive contribution margin, adds direct net profit, utilizes idle workers"],
                            ["Spare Capacity + Low Offer", "Offer Price < Average Variable Cost ($P < AVC$)", "REJECT ORDER", "Fails to cover raw materials; business loses cash on every unit manufactured"],
                            ["Zero Spare Capacity (100% Full)", "Requires hiring new shop or overtime machinery", "REJECT OR REQUOTE", "Fixed costs would rise; accepting discounted orders displaces regular high-paying clients"],
                            ["Market Cannibalization Risk", "Discounted buyers could resell to regular customers", "REJECT OR BRAND SEPARATELY", "Protects brand equity and preserves standard pricing power in primary market"]
                        ]
                    }
                }
            ],
            # Card 5: Step-by-Step Worked Example
            [
                {
                    "type": "worked_example",
                    "title": "Worked Example: Wanjiku's School Uniform Bulk Order Decision",
                    "content": {
                        "intro": "Wanjiku's Tailoring Shop in Eldoret has fixed rent of KES 10,000 per month and variable cost of KES 500 per uniform. Her standard price is KES 1,200. She is currently producing 20 uniforms (ATC = KES 1,000). A local school headteacher offers to buy 30 uniforms in a single bulk batch at KES 600 each. Wanjiku has idle sewing machines.",
                        "steps": [
                            "**Step 1 — Understand what we are finding:** Evaluate whether Wanjiku should accept or reject the special order of 30 uniforms at KES 600 per unit.",
                            "**Step 2 — Identify given information:**\n- Available capacity = Idle sewing machines exist (no extra rent)\n- Special offer price ($P$) = $\\text{KES } 600$\n- Variable cost per unit ($AVC$) = $\\text{KES } 500$\n- Batch size ($Q$) = $30\\text{ uniforms}$",
                            "**Step 3 — Choose the formulas:**\n$$\\text{Unit Contribution} = P - AVC$$\n$$\\text{Total Extra Profit} = Q \\times \\text{Unit Contribution}$$",
                            "**Step 4 — Perform the calculations step by step:**\n- Unit contribution: $600 - 500 = \\text{KES } 100\\text{ per uniform}$\n- Total additional profit generated: $30 \\times 100 = \\text{KES } 3,000$\n- Verification with Total Cost approach:\n  - Initial profit without order: $(20 \\times 1,200) - [10,000 + (20 \\times 500)] = 24,000 - 20,000 = \\text{KES } 4,000$\n  - New total revenue: $(20 \\times 1,200) + (30 \\times 600) = 24,000 + 18,000 = \\text{KES } 42,000$\n  - New total cost: $10,000 + (50 \\times 500) = 10,000 + 25,000 = \\text{KES } 35,000$\n  - New total profit: $42,000 - 35,000 = \\text{KES } 7,000$ (Increase of KES 3,000!)",
                            "**Step 5 — State the final answer:** Wanjiku should **ACCEPT** the order because it increases monthly profit by $\\mathbf{\\text{KES } 3,000}$ (from KES 4,000 to KES 7,000).",
                            "**Step 6 — Economic Interpretation & Pitfall:** If Wanjiku erroneously compared the KES 600 offer against her historical unit cost of KES 1,000, she would have rejected the deal and forgone KES 3,000 in clean profit! Fixed rent was already covered by her standard sales."
                        ]
                    }
                }
            ],
            # Card 6: Kenyan Case Study & Video
            [
                {
                    "type": "real_world_example",
                    "title": "Kenyan Enterprise Case: Baraka Brick Makers, Kakamega",
                    "content": {
                        "title": "Off-Peak Bulk Contracting in Construction",
                        "text": "Baraka Brick Makers in Kakamega pays monthly yard rent of KES 30,000. Variable cost per molded brick (clay and water) is KES 10, selling regularly at KES 25. During the heavy rainy season when local building slows, a road contractor offered to buy 10,000 bricks at KES 14. Because yard rent was already incurred, Baraka accepted the deal, generating a net contribution of KES 4 per brick (KES 40,000 total cash injection) that kept the business solvent during the off-season."
                    }
                },
                {
                    "type": "suggested_video",
                    "title": "Marginal Cost and Decision Making in Business",
                    "content": {
                        "title": "How to Evaluate Special Orders Using Incremental Costs",
                        "youtube_id": "Zk2y_mX-6-k",
                        "url": "https://www.youtube.com/watch?v=Zk2y_mX-6-k",
                        "description": "Educational video explaining how business managers analyze capacity utilization, variable cost contribution, and special discounted orders."
                    }
                }
            ],
            # Card 7: Formative Scenario-Based MCQs
            [
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 1: Evaluating a Bulk Offer with Spare Capacity",
                    "content": {
                        "question": "A commercial bakery in Nakuru has spare oven capacity. Its fixed rent is KES 40,000, variable cost per loaf is KES 35, and standard price is KES 60. A boarding school requests 1,000 loaves at KES 45 per loaf. What should the bakery do?",
                        "options": [
                            "Reject the offer because KES 45 is below the standard price of KES 60",
                            "Accept the offer because KES 45 exceeds the variable cost of KES 35, adding KES 10,000 to profit",
                            "Reject the offer because fixed costs will immediately double",
                            "Accept only if the school agrees to pay KES 70 per loaf"
                        ],
                        "correct": "B",
                        "explanation": "Since the bakery has spare capacity and fixed rent is already paid, the offer price of KES 45 exceeds the variable cost of KES 35, generating a positive contribution of KES 10 per loaf ($1,000 \\times 10 = \\text{KES } 10,000$ extra profit)."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 2: Risk of Accepting Below-Variable-Cost Orders",
                    "content": {
                        "question": "If an event organizer offers to buy 500 chairs from a carpentry shop at KES 300 per chair, but the shop's variable cost for timber and varnish is KES 380 per chair, what will happen if the shop accepts?",
                        "options": [
                            "The shop will make an extra profit of KES 40,000",
                            "The shop will suffer an operating cash loss of KES 80 per chair (KES 40,000 total loss)",
                            "The shop's fixed rent will be completely eliminated",
                            "Average total cost will fall to zero"
                        ],
                        "correct": "B",
                        "explanation": "If the selling price is lower than the variable cost ($P < AVC$), the business loses money on every single unit made ($300 - 380 = -\\text{KES } 80$). Producing 500 chairs would cause a direct cash loss of KES 40,000."
                    }
                }
            ],
            # Card 8: Synthesis & Key Takeaways
            [
                {
                    "type": "key_takeaway",
                    "title": "Lesson 4 Summary & Key Takeaways",
                    "content": {
                        "text": "1. **Decision Benchmark**: When evaluating special orders with spare capacity, compare offer price against Variable Cost (AVC), not Average Total Cost (ATC).\n2. **Contribution Rule**: If $P > AVC$, accept the order to generate positive cash contribution toward fixed overheads.\n3. **Capacity Boundaries**: Do not accept discounted orders if the factory is already running at 100% capacity or if it harms regular pricing."
                    }
                }
            ]
        ]
    },

    # =========================================================================
    # LESSON 5: Division of Labour
    # =========================================================================
    {
        "unit_order": 5,
        "unit_name": "Division of Labour",
        "unit_description": "Breaking complex production processes into sequential specialized tasks to maximize speed, dexterity, and factory output.",
        "lesson_title": "Division of Labour",
        "pages": [
            # Card 1: Photographic Hook & Learning Goals
            [
                {
                    "type": "suggested_image",
                    "title": "Shoe Factory Assembly Line",
                    "content": {
                        "title": "Industrial Division of Labour and Sequential Tasks",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/a/ae/Rex_Shoe_Factory%2C_New_Orleans_1917_-_Workers_in_Cutting_Dept.jpg",
                        "caption": "Factory workers stationed at dedicated cutting and assembly stations, illustrating how division of labour dramatically increases manufacturing output.",
                        "author": "Wikimedia Commons",
                        "licensing": "Public Domain"
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 5 Learning Outcomes",
                    "content": {
                        "text": "By the end of this lesson, you will be able to:\n\n- Define division of labour and specialisation of tasks\n- Trace the flow of an industrial assembly line pipeline\n- Explain the major economic advantages (dexterity, time savings, mechanization)\n- Analyze the operational risks (monotony, interdependence bottlenecks, narrow skills)"
                    }
                }
            ],
            # Card 2: Formal Definitions & Assembly Line Dynamics
            [
                {
                    "type": "definition_card",
                    "title": "Division of Labour and Specialisation",
                    "content": {
                        "term": "Division of Labour",
                        "definition": "The organizational practice of breaking down a complex manufacturing process into smaller, sequential, and specialized tasks, with each worker assigned to a specific task."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "From Solo Craftsman to High-Speed Assembly Line",
                    "content": {
                        "text": "Division of labour transforms enterprise productivity:\n\n- **Traditional Solo Craftsman**: A single worker cuts leather, stitches uppers, molds soles, glues parts, and polishes shoes alone. Frequent tool changes and station swaps result in low output (e.g., 1 pair every 2 days).\n- **Assembly Line Team**: A team of 5 specialized workers each masters one specific station along a conveyor line. Eliminating tool-swap downtime and repeating simple motions raises output to 200 pairs per day.\n- **Economic Basis**: First documented by Adam Smith in his famous *Pin Factory* study, proving that specialization multiplies output by hundreds of times."
                    }
                }
            ],
            # Card 3: Deep-Dive Breakdown & Vector Diagram
            [
                {
                    "type": "suggested_diagram",
                    "title": "Sequential Assembly Line & Division of Labour Pipeline",
                    "content": {
                        "title": "Shoe Manufacturing Assembly Line & Pros/Cons",
                        "caption": "Vector diagram illustrating the 5 sequential stages of footwear manufacturing, productivity comparison, and operational pros/cons.",
                        "svg_content": SVG_DIVISION_OF_LABOUR_PIPELINE
                    }
                }
            ],
            # Card 4: Advantages vs. Disadvantages Comparative Table
            [
                {
                    "type": "comparison_table",
                    "title": "Pros and Cons of Division of Labour in Manufacturing",
                    "content": {
                        "headers": ["Dimension", "Key Advantages (The Pros)", "Key Disadvantages (The Cons)", "Mitigation Strategy"],
                        "rows": [
                            ["Worker Productivity", "High speed & dexterity through repetition ('learning by doing')", "Monotony, boredom, and severe mental fatigue", "Job rotation and ergonomic rest breaks"],
                            ["Time & Tool Usage", "Zero time wasted putting down tools and moving stations", "Loss of individual pride in complete craftsmanship", "Performance bonuses & quality circles"],
                            ["Mechanization & Tools", "Facilitates specialized single-purpose machines and automation", "Interdependence risk: 1 broken machine halts the entire line", "Preventative maintenance & buffer inventory"],
                            ["Workforce Training", "Fast and cheap training (hours/days instead of years)", "Narrow skill trap; workers vulnerable to technological displacement", "Multi-skill cross-training programs"]
                        ]
                    }
                }
            ],
            # Card 5: Step-by-Step Worked Example
            [
                {
                    "type": "worked_example",
                    "title": "Worked Example: Productivity Gain from Division of Labour",
                    "content": {
                        "intro": "In a leather workshop in Athi River, 10 artisans work independently as solo craftsmen, each producing 3 pairs of shoes per 5-day week. The factory manager reorganizes them into a 10-person sequential assembly line with division of labour. The reorganized line produces 120 pairs of shoes per day.",
                        "steps": [
                            "**Step 1 — Understand what we are finding:** Calculate weekly output under solo craftsmanship, weekly output under division of labour (5-day week), total percentage productivity gain, and the output multiplier.",
                            "**Step 2 — Identify given information:**\n- 10 solo artisans = $10 \\times 3 = 30\\text{ pairs per week}$\n- Assembly line daily output = $120\\text{ pairs per day}$\n- Working days per week = $5\\text{ days}$",
                            "**Step 3 — Choose the formulas:**\n$$\\text{Assembly Line Weekly Output} = \\text{Daily Output} \\times 5$$\n$$\\text{Productivity Multiplier} = \\frac{\\text{Assembly Line Output}}{\\text{Solo Output}}$$\n$$\\text{Percentage Increase} = \\frac{\\text{Assembly Output} - \\text{Solo Output}}{\\text{Solo Output}} \\times 100\\%$$",
                            "**Step 4 — Perform the calculations step by step:**\n- Assembly line weekly output: $120 \\times 5 = 600\\text{ pairs per week}$\n- Solo craftsmen weekly output: $10 \\times 3 = 30\\text{ pairs per week}$\n- Productivity multiplier: $\\frac{600}{30} = 20\\text{ times}$\n- Percentage increase: $\\frac{600 - 30}{30} \\times 100\\% = \\frac{570}{30} \\times 100\\% = 1,900\\%$",
                            "**Step 5 — State the final answer:** Reorganizing workers into a division of labour increased weekly output from **30 pairs to 600 pairs** (a **20-fold / 1,900% productivity surge**).",
                            "**Step 6 — Economic Interpretation & Pitfall:** The dramatic increase in output occurs without adding extra workers or overtime hours—it is purely achieved by eliminating tool-swap transitions, increasing manual dexterity, and streamlining workflow."
                        ]
                    }
                }
            ],
            # Card 6: Kenyan Case Study & Video
            [
                {
                    "type": "real_world_example",
                    "title": "Kenyan Enterprise Case: Bata Shoe Company, Limuru",
                    "content": {
                        "title": "Mass Footwear Manufacturing via Assembly Lines in Limuru",
                        "text": "Bata Shoe Company in Limuru is East Africa's largest footwear manufacturer, producing tens of thousands of school shoes, canvas gumboots, and safari boots daily. Instead of a single shoemaker crafting one pair, Bata operates specialized production conveyors where workers focus exclusively on cutting leather, vulcanizing rubber soles, stitching seams, or boxing finished shoes. This extreme division of labour makes quality footwear affordable for millions of Kenyan families."
                    }
                },
                {
                    "type": "suggested_video",
                    "title": "Division of Labour & Adam Smith's Assembly Line",
                    "content": {
                        "title": "How Division of Labour Revolutionized Modern Manufacturing",
                        "youtube_id": "3jwAGWky98c",
                        "url": "https://www.youtube.com/watch?v=3jwAGWky98c",
                        "description": "Educational economics documentary illustrating Adam Smith's pin factory model and modern industrial assembly line operations."
                    }
                }
            ],
            # Card 7: Formative Scenario-Based MCQs
            [
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 1: Main Operational Vulnerability",
                    "content": {
                        "question": "In a tea packaging factory operating an automated conveyor line, the electronic tea weighing scale breaks down. All subsequent workers stationed at packaging and sealing are forced to stop working. What specific risk of division of labour does this illustrate?",
                        "options": [
                            "Specialisation by Craft",
                            "High training costs",
                            "Interdependence bottleneck",
                            "Lack of capital depreciation"
                        ],
                        "correct": "C",
                        "explanation": "Interdependence is a major operational vulnerability of division of labour. Because tasks are linked sequentially in a chain, any breakdown, delay, or slow worker in an early stage immediately halts all subsequent stages."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 2: Efficiency Gain from Division of Labour",
                    "content": {
                        "question": "Why does a worker stationed exclusively on a fabric die-cutting machine produce more cut pieces per hour than a worker who cuts, stitches, and packages garments?",
                        "options": [
                            "The worker does not waste time switching tools, changing tables, and adjusting machine settings",
                            "The worker earns double the commission of other tailors",
                            "The worker is exempt from all factory safety regulations",
                            "The worker operates without any fixed costs"
                        ],
                        "correct": "A",
                        "explanation": "Division of labour saves time by eliminating transition downtime between tasks and allows workers to develop high speed and precision through continuous task repetition."
                    }
                }
            ],
            # Card 8: Synthesis & Key Takeaways
            [
                {
                    "type": "key_takeaway",
                    "title": "Lesson 5 Summary & Key Takeaways",
                    "content": {
                        "text": "1. **Definition**: Division of labour splits complex production into simple, specialized, sequential micro-tasks.\n2. **Key Benefits**: Massive output gains, zero tool-switching downtime, fast worker training, and automation feasibility.\n3. **Key Drawbacks**: Job monotony/boredom, loss of craft satisfaction, and high vulnerability to sequential bottlenecks."
                    }
                }
            ]
        ]
    },

    # =========================================================================
    # LESSON 6: Specialisation
    # =========================================================================
    {
        "unit_order": 6,
        "unit_name": "Specialisation",
        "unit_description": "Macro-economic concentration on specific goods and services across four levels: Craft, Firm, Region, and International Country trade.",
        "lesson_title": "Specialisation",
        "pages": [
            # Card 1: Photographic Hook & Learning Goals
            [
                {
                    "type": "suggested_image",
                    "title": "Mombasa Port Container Cargo Export",
                    "content": {
                        "title": "Regional and National Specialisation in Commercial Trade",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/9/94/Container_ship_exiting_Mombasa_port%2C_Kenya_01.jpg",
                        "caption": "A cargo container ship departing Mombasa Port loaded with Kenyan tea, coffee, and horticultural exports, illustrating national and regional specialisation.",
                        "author": "Ian Kiptoo",
                        "licensing": "CC BY 4.0"
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 6 Learning Outcomes",
                    "content": {
                        "text": "By the end of this lesson, you will be able to:\n\n- Define specialisation and distinguish it from division of labour\n- Explain the 4 types of specialisation: Craft, Firm, Region, and Country\n- Analyze how comparative advantage drives regional and international trade in Kenya\n- Calculate economic output gains achieved through specialized trade"
                    }
                }
            ],
            # Card 2: Formal Definitions & Economic Principles
            [
                {
                    "type": "definition_card",
                    "title": "Specialisation and Comparative Advantage",
                    "content": {
                        "term": "Specialisation",
                        "definition": "The concentration of productive effort by an individual, business enterprise, geographical region, or nation on a limited range of goods or services in which they possess superior skill or comparative advantage."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Division of Labour vs. Specialisation",
                    "content": {
                        "text": "While related, these two economic terms operate at different scales:\n\n- **Division of Labour (Micro-level)**: Internal separation of tasks among workers inside a single factory or workshop (e.g., cutting vs. stitching in a tailoring shop).\n- **Specialisation (Macro-level)**: Complete enterprise or regional focus on producing specific goods/services and trading the surplus for other needs (e.g., Naivasha specializing in export flowers, Safaricom specializing in telecommunications).\n- **Necessity of Trade**: When an entity specializes, it cannot be self-sufficient; it must trade surplus goods to acquire commodities it does not produce."
                    }
                }
            ],
            # Card 3: Deep-Dive Breakdown & Vector Diagram
            [
                {
                    "type": "suggested_diagram",
                    "title": "The 4 Levels of Economic Specialisation",
                    "content": {
                        "title": "Specialisation Levels Architecture",
                        "caption": "Vector diagram illustrating Specialisation by Craft (Individual), Firm (Enterprise), Region (Geographical), and Country (International Trade).",
                        "svg_content": SVG_TYPES_OF_SPECIALISATION
                    }
                }
            ],
            # Card 4: Detailed Level Comparison Table
            [
                {
                    "type": "comparison_table",
                    "title": "The 4 Levels of Economic Specialisation in Kenya",
                    "content": {
                        "headers": ["Level of Specialisation", "Scope & Description", "Key Driving Factors", "Kenyan Real-World Example"],
                        "rows": [
                            ["1. By Craft (Trade)", "An individual concentrates on a specific profession", "Personal talent, education, and vocational training", "Certified public accountants (CPA), software developers, medical surgeons"],
                            ["2. By Firm (Process)", "A business focuses exclusively on a distinct product line", "Capital investment, brand identity, and technical expertise", "Safaricom (Telecom/Fintech), Brookside Dairy (Milk processing), Kipekee Bakers"],
                            ["3. By Region (Geographical)", "An entire town/county focuses on goods favored by location", "Climate, soil fertility, mineral deposits, and natural harbors", "Naivasha (Export roses/geothermal), Mombasa (Maritime logistics), Kericho (Tea)"],
                            ["4. By Country (International)", "A nation exports products with comparative advantage", "Resource endowments, technological lead, and global trade agreements", "Kenya exports black tea, coffee, cut flowers; imports heavy machinery, oil, vehicles"]
                        ]
                    }
                }
            ],
            # Card 5: Step-by-Step Worked Example
            [
                {
                    "type": "worked_example",
                    "title": "Worked Example: Output Gains from Regional Specialisation and Trade",
                    "content": {
                        "intro": "Consider two Kenyan counties: Nakuru (temperate climate) and Kisumu (lake basin). Each county has 100 hectares of land. Without specialisation, each county splits its land 50-50 between Potatoes and Fish farming. Nakuru yields 20 tons of potatoes or 2 tons of farmed fish per hectare. Kisumu yields 5 tons of potatoes or 8 tons of farmed fish per hectare.",
                        "steps": [
                            "**Step 1 — Understand what we are finding:** Compare total combined output before specialisation (50 ha each) against total combined output after full regional specialisation (100 ha dedicated to the higher-yield crop).",
                            "**Step 2 — Identify given information:**\n- **Nakuru Yields per ha:** Potatoes = $20\\text{ tons}$, Fish = $2\\text{ tons}$\n- **Kisumu Yields per ha:** Potatoes = $5\\text{ tons}$, Fish = $8\\text{ tons}$\n- Total land per county = $100\\text{ hectares}$",
                            "**Step 3 — Choose the formulas:**\n$$\\text{Combined Output} = \\text{Nakuru Output} + \\text{Kisumu Output}$$\n$$\\text{Output Gain} = \\text{Specialized Output} - \\text{Unspecialized Output}$$",
                            "**Step 4 — Perform the calculations step by step:**\n- **Case A: Without Specialisation (50 ha Potatoes, 50 ha Fish each):**\n  - Nakuru: $50 \\times 20 = 1,000\\text{ tons potatoes}$; $50 \\times 2 = 100\\text{ tons fish}$\n  - Kisumu: $50 \\times 5 = 250\\text{ tons potatoes}$; $50 \\times 8 = 400\\text{ tons fish}$\n  - **Combined Total:** Potatoes = $1,000 + 250 = \\mathbf{1,250\\text{ tons}}$; Fish = $100 + 400 = \\mathbf{500\\text{ tons}}$\n\n- **Case B: With Full Specialisation (Nakuru 100 ha Potatoes, Kisumu 100 ha Fish):**\n  - Nakuru (100 ha Potatoes): $100 \\times 20 = \\mathbf{2,000\\text{ tons potatoes}}$\n  - Kisumu (100 ha Fish): $100 \\times 8 = \\mathbf{800\\text{ tons fish}}$\n  - **Combined Total:** Potatoes = $\\mathbf{2,000\\text{ tons}}$; Fish = $\\mathbf{800\\text{ tons}}$\n\n- **Net Output Gain from Specialisation:**\n  - Extra Potatoes: $2,000 - 1,250 = \\mathbf{+750\\text{ tons (+60%)}}$\n  - Extra Fish: $800 - 500 = \\mathbf{+300\\text{ tons (+60%)}}$",
                            "**Step 5 — State the final answer:** Full regional specialisation increases total food output by **750 extra tons of potatoes and 300 extra tons of fish** from the exact same 200 hectares of land!",
                            "**Step 6 — Economic Interpretation & Pitfall:** Specialisation creates massive wealth gains without needing extra land or capital. However, Nakuru and Kisumu must have reliable transport infrastructure (SGR/highways) to trade their surpluses smoothly."
                        ]
                    }
                }
            ],
            # Card 6: Kenyan Case Study & Video
            [
                {
                    "type": "real_world_example",
                    "title": "Kenyan Enterprise Case: The Naivasha Floriculture & Energy Cluster",
                    "content": {
                        "title": "Regional Specialisation Around Lake Naivasha",
                        "text": "Naivasha in Nakuru County has become a global floriculture capital, producing over 70% of Kenya's export cut flowers. Favorable fresh lake water, high altitude, and abundant sunlight make rose farming highly efficient. Furthermore, the Olkaria geothermal fields in Naivasha specialize in clean electricity generation, supplying over 800 MW to the national grid. By concentrating on flowers and geothermal power, Naivasha drives national export earnings."
                    }
                },
                {
                    "type": "suggested_video",
                    "title": "Specialisation, Trade, and Comparative Advantage",
                    "content": {
                        "title": "How Specialisation and Trade Drive Economic Prosperity",
                        "youtube_id": "W7q_y6Zk9g4",
                        "url": "https://www.youtube.com/watch?v=W7q_y6Zk9g4",
                        "description": "Educational economics lesson breaking down absolute and comparative advantage, regional specialisation, and international trade exchange."
                    }
                }
            ],
            # Card 7: Formative Scenario-Based MCQs
            [
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 1: Identifying Regional Specialisation",
                    "content": {
                        "question": "Bamburi in Mombasa is renowned for large-scale limestone cement manufacturing, while Kericho is globally famous for tea plantations. What form of specialisation does this represent?",
                        "options": [
                            "Specialisation by Craft",
                            "Specialisation by Region (Geographical)",
                            "Specialisation by Division of Labour",
                            "Specialisation by Consumer Demand"
                        ],
                        "correct": "B",
                        "explanation": "Regional or geographical specialisation occurs when an entire geographical area concentrates on producing specific commodities favored by its local climate, mineral endowment, or geography (limestone in Bamburi, volcanic soil in Kericho)."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 2: The Critical Prerequisite for Specialisation",
                    "content": {
                        "question": "If a farmer in Nyandarua specializes exclusively in growing potatoes and produces zero maize or vegetables, what economic mechanism is absolutely required for the farmer's household to survive?",
                        "options": [
                            "A system of commercial trade and market exchange to buy other foodstuffs",
                            "A complete shutdown of all local transport routes",
                            "Elimination of all commercial banks in the county",
                            "Higher fixed rental payments"
                        ],
                        "correct": "A",
                        "explanation": "Specialisation eliminates self-sufficiency. An entity that produces only one commodity must engage in trade and market exchange to buy goods and services they do not produce."
                    }
                }
            ],
            # Card 8: Synthesis & Key Takeaways
            [
                {
                    "type": "key_takeaway",
                    "title": "Lesson 6 Summary & Key Takeaways",
                    "content": {
                        "text": "1. **Definition**: Specialisation is focusing productive effort on a limited range of goods where one holds comparative advantage.\n2. **4 Levels**: Craft (Individual), Firm (Company), Region (Geographical town/county), and Country (International trade).\n3. **Trade Synergy**: Specialisation multiplies total economic output, but requires efficient transport and market exchange systems."
                    }
                }
            ]
        ]
    },

    # =========================================================================
    # LESSON 7: Producer Roles and Responsibilities to Consumers
    # =========================================================================
    {
        "unit_order": 7,
        "unit_name": "Producer Roles and Responsibilities to Consumers",
        "unit_description": "Legal, ethical, and moral consumer protection obligations: Product safety, KEBS standards, fair pricing, honest marketing, and redress.",
        "lesson_title": "Producer Roles and Responsibilities to Consumers",
        "pages": [
            # Card 1: Photographic Hook & Learning Goals
            [
                {
                    "type": "suggested_image",
                    "title": "Retail Marketplace and Consumer Safety in Kenya",
                    "content": {
                        "title": "Consumer Trust and Producer Stewardship in Kenyan Markets",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/9/97/A_vegetable_stall_in_the_outskirts_of_Nairobi%2C_Kenya.jpg",
                        "caption": "Traders presenting fresh agricultural goods for consumer purchase, emphasizing the producer's duty to provide clean, safe, and honest products.",
                        "author": "Terryngari",
                        "licensing": "CC BY-SA 4.0"
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 7 Learning Outcomes",
                    "content": {
                        "text": "By the end of this lesson, you will be able to:\n\n- Identify the core moral and legal responsibilities of producers to consumers\n- Explain the role of the Kenya Bureau of Standards (KEBS) and Competition Authority of Kenya (CAK)\n- Describe consumer rights: Safety, Information, Choice, Redress, and Fair Pricing\n- Evaluate business actions in product recall, warranty fulfillment, and environmental stewardship"
                    }
                }
            ],
            # Card 2: Formal Definitions & Legal Principles
            [
                {
                    "type": "definition_card",
                    "title": "Producer Responsibilities and Duty of Care",
                    "content": {
                        "term": "Duty of Care",
                        "definition": "The legal and ethical obligation of a producer to ensure that products and manufacturing processes do not cause harm, deception, or financial loss to consumers."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "The Six Pillars of Consumer Protection in Kenya",
                    "content": {
                        "text": "Responsible enterprises must uphold 6 fundamental pillars:\n\n- **1. Product Safety & Quality**: Complying with KEBS standards to eliminate harmful toxins, electric hazards, and food adulteration.\n- **2. Truth in Advertising**: Prohibiting deceptive claims, fake discounts, and misleading health promises.\n- **3. Fair Pricing & Anti-Gouging**: Prohibiting artificial price spikes during droughts or crises and eliminating cartel collusion.\n- **4. Transparent Sales Terms**: Providing clear warranty documents, return guidelines, and no hidden charges.\n- **5. Grievance Redress & Refunds**: Resolving customer complaints promptly with free repairs, replacements, or full refunds.\n- **6. Environmental & Data Care**: Complying with NEMA waste management laws and protecting digital payment data under the Data Protection Act."
                    }
                }
            ],
            # Card 3: Deep-Dive Breakdown & Vector Diagram
            [
                {
                    "type": "suggested_diagram",
                    "title": "Producer Responsibilities & Consumer Stewardship",
                    "content": {
                        "title": "Producer Responsibilities Architecture",
                        "caption": "Vector diagram detailing the 6 core pillars of producer responsibility, regulatory enforcement bodies (KEBS, CAK, NEMA), and breach penalties.",
                        "svg_content": SVG_PRODUCER_RESPONSIBILITIES
                    }
                }
            ],
            # Card 4: Consumer Rights vs. Producer Duties Matrix
            [
                {
                    "type": "comparison_table",
                    "title": "Consumer Rights and Corresponding Producer Obligations",
                    "content": {
                        "headers": ["Consumer Right", "Producer Obligation", "Enforcing Kenyan Body", "Practical Business Practice"],
                        "rows": [
                            ["Right to Safety", "Manufacture non-toxic, hygienic, and tested goods", "KEBS (Kenya Bureau of Standards)", "Displaying genuine KEBS standardization marks; Testing aflatoxin levels in maize flour"],
                            ["Right to Information", "Provide truthful packaging, ingredients, and dates", "Competition Authority of Kenya (CAK)", "Clear ingredient lists, allergen warnings, and accurate manufacturing/expiry dates"],
                            ["Right to Fair Price", "Avoid price gouging, hoarding, and cartel fixing", "CAK & Consumer Protection Act 2012", "Transparent price tags on shelf displays with no hidden checkout fees"],
                            ["Right to Redress", "Provide prompt refund, repair, or product exchange", "Commercial Courts & Small Claims Courts", "Honoring 12-month electronic warranties; Dedicated customer care desks"],
                            ["Right to Clean Environment", "Eliminate toxic smoke, river effluent, and plastic waste", "NEMA (National Environment Management Authority)", "Installing industrial water treatment filters; Biodegradable packaging"],
                            ["Right to Data Privacy", "Secure customer mobile money numbers and records", "Office of the Data Protection Commissioner (ODPC)", "Never selling customer M-Pesa contact databases to third-party telemarketers"]
                        ]
                    }
                }
            ],
            # Card 5: Step-by-Step Worked Example
            [
                {
                    "type": "worked_example",
                    "title": "Worked Example: Auditing Product Safety Recall Costs vs. Brand Liability",
                    "content": {
                        "intro": "Baraka Bottlers in Kisumu discovers that a batch of 5,000 fruit juice bottles contains a faulty cap seal causing premature spoilage. Each bottle sells for KES 100 (manufacturing cost KES 60). A full public recall and replacement will cost KES 500,000. If they ignore the defect, medical compensation and KEBS regulatory fines would average KES 2,500,000.",
                        "steps": [
                            "**Step 1 — Understand what we are finding:** Compare the immediate financial cost of a proactive product recall against the legal, regulatory, and compensation liabilities of ignoring the defect.",
                            "**Step 2 — Identify given information:**\n- Defective batch = $5,000\\text{ bottles}$\n- Proactive product recall cost = $\\text{KES } 500,000$\n- Expected legal fines, medical claims & sanctions = $\\text{KES } 2,500,000$\n- Initial batch sales revenue = $5,000 \\times 100 = \\text{KES } 500,000$",
                            "**Step 3 — Choose the formulas:**\n$$\\text{Net Savings from Responsible Recall} = \\text{Potential Liability} - \\text{Recall Cost}$$",
                            "**Step 4 — Perform the calculations step by step:**\n- Liability of ignoring defect: $\\text{KES } 2,500,000$\n- Cost of proactive recall: $\\text{KES } 500,000$\n- Financial savings: $2,500,000 - 500,000 = \\text{KES } 2,000,000$\n- Brand reputation preservation = Invaluable long-term commercial asset",
                            "**Step 5 — State the final answer:** Proactive product recall saves the enterprise $\\mathbf{\\text{KES } 2,000,000}$ in direct legal costs while upholding consumer safety and preserving long-term brand goodwill.",
                            "**Step 6 — Economic Interpretation & Pitfall:** Responsible producers do not treat consumer protection as an optional cost—it is a legal duty that prevents catastrophic lawsuits, factory shutdowns by KEBS, and brand destruction."
                        ]
                    }
                }
            ],
            # Card 6: Kenyan Case Study & Video
            [
                {
                    "type": "real_world_example",
                    "title": "Kenyan Regulatory Case: KEBS Aflatoxin Surveillance & Product Recalls",
                    "content": {
                        "title": "Protecting Millions of Consumers from Contaminated Flour",
                        "text": "The Kenya Bureau of Standards (KEBS) routinely conducts market surveillance across supermarkets and retail kiosks. In multiple nationwide actions, KEBS has suspended commercial milling permits and ordered the immediate public recall of maize flour brands exceeding the safe aflatoxin limit of 10 parts per billion (ppb). This enforcement reinforces the legal duty of food millers to test raw maize thoroughly before processing."
                    }
                },
                {
                    "type": "suggested_video",
                    "title": "Consumer Protection and Producer Responsibilities",
                    "content": {
                        "title": "Consumer Rights and Ethical Standards in Business",
                        "youtube_id": "fTTGALaRZoc",
                        "url": "https://www.youtube.com/watch?v=fTTGALaRZoc",
                        "description": "Educational overview of consumer protection legislation, product safety standards, honest advertising, and producer ethical duties."
                    }
                }
            ],
            # Card 7: Formative Scenario-Based MCQs
            [
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 1: Ethical Action on Safety Defect",
                    "content": {
                        "question": "A manufacturer of electric water kettles in Nairobi discovers that an internal thermostat defect causes the plastic handle to overheat. What is the most legally and ethically responsible action the producer should take?",
                        "options": [
                            "Increase kettle prices to cover potential future hospital bills",
                            "Quietly fix new factory units but leave already-sold kettles with consumers",
                            "Issue a public safety recall, warn customers, and offer free repairs or replacements",
                            "Launch a new advertising campaign claiming the kettle heats water twice as fast"
                        ],
                        "correct": "C",
                        "explanation": "Under the Consumer Protection Act and product liability laws, producers have a duty of care to issue an immediate public recall, notify consumers of the hazard, and provide free repairs or refunds."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 2: Deceptive Marketing Practice",
                    "content": {
                        "question": "A beverage company advertises its packaged drink as '100% Pure Organic Passion Juice' with 'Zero Added Sugar'. Chemical laboratory tests reveal it contains 60% tap water, artificial sweeteners, and synthetic food coloring. Which consumer right has been violated?",
                        "options": [
                            "Right to Information and Truthful Marketing",
                            "Right to Fast Transport Logistics",
                            "Right to Pay Loan Interest",
                            "Right to Division of Labour"
                        ],
                        "correct": "A",
                        "explanation": "Consumers have a fundamental right to truthful, accurate information. Making false claims about ingredients, organic status, or nutritional value violates consumer protection laws and constitutes deceptive marketing."
                    }
                }
            ],
            # Card 8: Synthesis & Key Takeaways
            [
                {
                    "type": "key_takeaway",
                    "title": "Lesson 7 Summary & Key Takeaways",
                    "content": {
                        "text": "1. **Duty of Care**: Producers must guarantee safety, hygiene, honest advertising, and fair pricing on all goods.\n2. **Regulatory Standards**: Regulatory bodies like KEBS, CAK, and NEMA enforce compliance to protect public health and economic welfare.\n3. **Consumer Rights**: Consumers are entitled to Safety, Information, Choice, Redress, and Environmental Protection."
                    }
                }
            ]
        ]
    },

    # =========================================================================
    # LESSON 8: Product Labels
    # =========================================================================
    {
        "unit_order": 8,
        "unit_name": "Product Labels",
        "unit_description": "Designing effective, compliant product labels: Brand identity, net contents, ingredients, expiry dates, allergen alerts, and KEBS standardization marks.",
        "lesson_title": "Product Labels",
        "pages": [
            # Card 1: Photographic Hook & Learning Goals
            [
                {
                    "type": "suggested_image",
                    "title": "Standardized Consumer Product Label",
                    "content": {
                        "title": "Mandatory Packaging Information on Consumer Goods",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/2/2b/FDA_Nutrition_Facts_Label_2006.jpg",
                        "caption": "A standardized product label displaying ingredients, net quantity, nutritional data, and manufacturer details required for regulatory consumer protection.",
                        "author": "US Food and Drug Administration",
                        "licensing": "Public Domain"
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 8 Learning Outcomes",
                    "content": {
                        "text": "By the end of this lesson, you will be able to:\n\n- Define a product label and explain its role as a product's 'Identity Card'\n- Identify all mandatory label components required by KEBS and public health regulations\n- Distinguish between Manufacturing Date and Expiry Date\n- Design a professional, compliant, and attractive consumer product label"
                    }
                }
            ],
            # Card 2: Formal Definitions & Labeling Functions
            [
                {
                    "type": "definition_card",
                    "title": "Product Label",
                    "content": {
                        "term": "Product Label",
                        "definition": "The written, printed, or graphic visual display affixed to a product package that provides critical identification, ingredients, usage instructions, safety warnings, and regulatory certification."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "The Dual Role of Product Labels: Marketing & Legal Compliance",
                    "content": {
                        "text": "A product label serves two vital functions:\n\n- **1. Marketing & Brand Communication**: Attracts consumers on supermarket shelves through distinctive brand logos, typography, product descriptions, and vibrant color schemes.\n- **2. Legal & Health Protection**: Conveys mandatory technical data required by law, including exact net weight/volume, ingredient lists in descending order of proportion, allergen warnings, storage directions, manufacturer's physical location, and official regulatory quality seals (KEBS)."
                    }
                }
            ],
            # Card 3: Deep-Dive Breakdown & Vector Diagram
            [
                {
                    "type": "suggested_diagram",
                    "title": "Anatomy of a Compliant & Effective Product Label",
                    "content": {
                        "title": "Product Label Anatomy & Standards Architecture",
                        "caption": "Vector diagram detailing all 10 mandatory components of a commercial product label, including barcode, KEBS quality mark, and nutrition panel.",
                        "svg_content": SVG_PRODUCT_LABEL_ANATOMY
                    }
                }
            ],
            # Card 4: Mandatory Label Elements Reference Table
            [
                {
                    "type": "comparison_table",
                    "title": "10 Mandatory Product Label Elements and Functions",
                    "content": {
                        "headers": ["Label Component", "Required Content", "Regulatory Purpose", "Sample Product Display"],
                        "rows": [
                            ["1. Brand & Product Name", "Clear brand logo and specific item description", "Identifies manufacturer and product identity", "Baraka Fresh Foods: 100% Pure Passion Fruit Juice"],
                            ["2. Net Content / Quantity", "Exact metric weight or liquid volume", "Prevents cheating on package fill levels", "Net Volume: 500 ml (or Net Weight: 1 Kg)"],
                            ["3. Ingredient List", "Complete list in descending order of weight", "Informs consumers with dietary restrictions", "Water, Passion Fruit Pulp (40%), Cane Sugar, Citric Acid"],
                            ["4. Allergen Warning", "Prominent warning of common allergen risks", "Prevents life-threatening allergic reactions", "WARNING: Manufactured in a facility that processes peanuts"],
                            ["5. Mfg & Expiry Dates", "Day/Month/Year of production and expiration", "Guarantees freshness and prevents food poisoning", "Mfg: 15/08/2026 | Exp: 15/02/2027 (Batch BF-2026)"],
                            ["6. Storage Instructions", "Temperature and preservation guidelines", "Prevents spoilage before the expiry date", "Store in a cool, dry place. Keep refrigerated below 4°C"],
                            ["7. Nutritional Information", "Energy (kJ/kcal), Protein, Carbs, Fats, Vitamins", "Supports healthy diet management", "Per 100ml: Energy 180 kJ, Carbs 10.2g, Vit C 35mg"],
                            ["8. Manufacturer Details", "Registered company name and physical address", "Enables regulatory traceability and customer queries", "Baraka Foods Ltd, Plot 45 Kibos Rd, Kisumu, Kenya"],
                            ["9. Regulatory Quality Mark", "Official certification seal and standard number", "Proves compliance with national quality tests", "KEBS Standardization Mark (KS EAS 35:2024)"],
                            ["10. Barcode & Disposal", "EAN Barcode and recycling/litter symbols", "Facilitates POS scanning and green disposal", "EAN-13 Barcode + 'Keep Kenya Clean' Trash Icon"]
                        ]
                    }
                }
            ],
            # Card 5: Step-by-Step Worked Example
            [
                {
                    "type": "worked_example",
                    "title": "Worked Example: Auditing a Startup Product Label for Regulatory Compliance",
                    "content": {
                        "intro": "A youth startup in Kisumu plans to launch 'Yummy Peanut Butter' in 400g glass jars. Their draft label features: Brand Name ('Yummy'), a picture of peanuts, price tag ('KES 250'), and phone number. Conduct a professional compliance audit identifying defects and corrective actions before printing 10,000 labels.",
                        "steps": [
                            "**Step 1 — Understand what we are finding:** Review the draft label against KEBS standards, list all missing mandatory elements, and specify the required corrections.",
                            "**Step 2 — Identify given information in draft label:**\n- Present: Brand Name ('Yummy'), Graphic picture, Price (KES 250), Phone number.\n- Missing elements: Net Weight, Expiry Date, Manufacturing Date, Batch Number, Ingredient List, Allergen Warning, Physical Address, Storage Directions, KEBS Standardization Mark, Barcode.",
                            "**Step 3 — Choose the compliance audit criteria:** Compare against Kenya Standard KS EAS 38 (Labeling of Pre-packaged Foods).",
                            "**Step 4 — Perform the audit step by step:**\n- **Critical Omission 1 (Safety)**: Peanuts are a major allergen. Must include prominent bold text: **'ALLERGEN WARNING: Contains Peanuts'**.\n- **Critical Omission 2 (Shelf Life)**: Must add **'Mfg Date: DD/MM/YY'** and **'Best Before / Exp Date: DD/MM/YY'** alongside Batch Number.\n- **Critical Omission 3 (Measurement)**: Must state metric net quantity: **'Net Weight: 400g'**.\n- **Critical Omission 4 (Traceability)**: Add full physical location: **'Manufactured by Yummy Nut Butters Ltd, Industrial Area, Kisumu, Kenya'**.\n- **Critical Omission 5 (Certification)**: Leave a dedicated box for the **KEBS Standardization Mark** after lab clearance.",
                            "**Step 5 — State the final answer:** The draft label is **NON-COMPLIANT and DANGEROUS**. The startup must redesign the label to incorporate all 10 mandatory technical items before commercial distribution.",
                            "**Step 6 — Economic Interpretation & Pitfall:** Printing non-compliant labels is a costly error. Non-compliant stock will be impounded by public health inspectors, leading to total loss of printing expenditure and heavy regulatory fines."
                        ]
                    }
                }
            ],
            # Card 6: Kenyan Case Study & Video
            [
                {
                    "type": "real_world_example",
                    "title": "Kenyan Enterprise Case: Baraka Fresh Foods Labeling Overhaul",
                    "content": {
                        "title": "Securing National Supermarket Shelves Through Compliant Packaging",
                        "text": "When Baraka Fresh Foods in Kisumu first attempted to sell fruit juices to major supermarket chains like Naivas and Quickmart, their stock was rejected because their bottles had handwritten expiry dates and no EAN barcodes. After redesigning their labels to include full nutrition panels, batch codes, scannable EAN-13 barcodes, and the KEBS mark, their juices were accepted into over 60 branches across Kenya, multiplying sales tenfold."
                    }
                },
                {
                    "type": "suggested_video",
                    "title": "Designing Compliant Product Labels: Packaging & Standards",
                    "content": {
                        "title": "Essential Elements of Effective and Legal Product Labels",
                        "youtube_id": "r7pdUswl8qM",
                        "url": "https://www.youtube.com/watch?v=r7pdUswl8qM",
                        "description": "Comprehensive tutorial explaining how to design food and consumer product labels with correct nutrition facts, barcodes, and regulatory marks."
                    }
                }
            ],
            # Card 7: Formative Scenario-Based MCQs
            [
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 1: Mandatory Ingredient Ordering",
                    "content": {
                        "question": "Under standard food labeling regulations (KEBS / ISO), in what specific order must ingredients be listed on a packaged food label?",
                        "options": [
                            "In alphabetical order from A to Z",
                            "In descending order of weight (highest quantity ingredient first)",
                            "In random order based on label color aesthetics",
                            "In order of retail ingredient cost"
                        ],
                        "correct": "B",
                        "explanation": "Food labeling regulations mandate that all ingredients must be listed in descending order of weight or proportion, ensuring the primary ingredient used is displayed first."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 2: Expiry Date vs. Manufacturing Date",
                    "content": {
                        "question": "A consumer purchases a container of fresh yogurt showing 'Mfg: 01/08/2026' and 'Exp: 15/08/2026'. If the consumer attempts to consume the product on 25th August 2026, what risk exists?",
                        "options": [
                            "The retail price of the yogurt will increase",
                            "The product has passed its safe shelf life and may cause food poisoning or bacterial illness",
                            "The volume of yogurt will double in size",
                            "The manufacturer's business license will automatically expire"
                        ],
                        "correct": "B",
                        "explanation": "The Expiry Date (Exp Date) indicates the final date after which the product is no longer safe for human consumption due to bacterial degradation or nutrient spoilage."
                    }
                }
            ],
            # Card 8: Synthesis & Key Takeaways
            [
                {
                    "type": "key_takeaway",
                    "title": "Lesson 8 Summary & Key Takeaways",
                    "content": {
                        "text": "1. **Identity Card**: A product label is a package's identity card that attracts buyers and communicates essential safety data.\n2. **10 Mandatory Elements**: Brand name, net weight, ingredient order, allergen warnings, dates, storage, nutrition, address, KEBS mark, and barcode.\n3. **Compliance Value**: Proper label design is not just marketing; it is a legal requirement that enables supermarket distribution and builds customer trust."
                    }
                }
            ]
        ]
    },

    # =========================================================================
    # LESSON 9: Production and the National Economy
    # =========================================================================
    {
        "unit_order": 9,
        "unit_name": "Production and the National Economy",
        "unit_description": "Macroeconomic linkages: Connecting Primary, Secondary, and Tertiary sectors to National Output (GDP), employment, and living standards.",
        "lesson_title": "Production and the National Economy",
        "pages": [
            # Card 1: Photographic Hook & Learning Goals
            [
                {
                    "type": "suggested_image",
                    "title": "Standard Gauge Railway (SGR) Freight Transport",
                    "content": {
                        "title": "National Production and Transport Infrastructure in Kenya",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/6/61/Express_passenger_train_on_the_Mombasa_-_Nairobi_Standard_Gauge_Railway.jpg",
                        "caption": "The Standard Gauge Railway connecting Mombasa Port to Nairobi and inland economic zones, driving the distribution of manufactured and agricultural output.",
                        "author": "TTC dude",
                        "licensing": "CC BY-SA 4.0"
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 9 Learning Outcomes",
                    "content": {
                        "text": "By the end of this lesson, you will be able to:\n\n- Trace the flow of production across Primary, Secondary, and Tertiary sectors\n- Explain how domestic production contributes to Gross Domestic Product (GDP)\n- Analyze the multiplier effect of manufacturing on national employment and tax revenues\n- Calculate value addition across economic sectors in Kenya"
                    }
                }
            ],
            # Card 2: Formal Definitions & Macroeconomic Roles
            [
                {
                    "type": "definition_card",
                    "title": "Gross Domestic Product (GDP) and Economic Sectors",
                    "content": {
                        "term": "Gross Domestic Product (GDP)",
                        "definition": "The total monetary value of all finished goods and services produced within the geographical boundaries of a country during a specific period (typically one year)."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "The Three Interconnected Economic Sectors",
                    "content": {
                        "text": "Production forms the engine that powers the entire macroeconomy:\n\n- **1. Primary Sector (Extraction)**: Direct extraction of natural raw materials (e.g., Kericho tea plucking, Tabaka soapstone quarrying, fishing in Lake Victoria, maize farming).\n- **2. Secondary Sector (Manufacturing & Processing)**: Industrial transformation of raw materials into finished physical goods (e.g., tea processing factories, Athi River cement manufacturing, textile mills).\n- **3. Tertiary Sector (Services & Distribution)**: Distribution, logistics, financial, and retail services that connect finished goods to consumers (e.g., SGR freight cargo trains, commercial banking, wholesale/retail supermarkets)."
                    }
                }
            ],
            # Card 3: Deep-Dive Breakdown & Vector Diagram
            [
                {
                    "type": "suggested_diagram",
                    "title": "Production in the National Macroeconomy",
                    "content": {
                        "title": "Three Economic Sectors Flow & Macro Impact",
                        "caption": "Vector diagram illustrating the sequential linkages between Primary, Secondary, and Tertiary production, and their macro impact on GDP and standard of living.",
                        "svg_content": SVG_MACRO_PRODUCTION_CIRCULAR_FLOW
                    }
                }
            ],
            # Card 4: Macroeconomic Contributions Matrix
            [
                {
                    "type": "comparison_table",
                    "title": "Macroeconomic Impact of a Strong Production Sector",
                    "content": {
                        "headers": ["Macroeconomic Area", "Primary Mechanism", "Benefit to Kenyan Citizens", "Key Kenyan Milestone"],
                        "rows": [
                            ["1. Employment Creation", "Farms, processing plants, and transport networks hire workers", "Provides stable salaries, reduces poverty, and develops vocational skills", "Over 3 million Kenyans engaged in agricultural and manufacturing value chains"],
                            ["2. GDP Growth & Output", "Higher physical output expands total national wealth", "Increases national income per capita and raises standard of living", "Kenya's GDP surpassing KES 15 trillion driven by services and agriculture"],
                            ["3. Foreign Exchange (Forex)", "Exporting tea, coffee, cut flowers, and processed foods", "Earns USD/EUR to import essential machinery, fuels, and medicines", "Tea and horticultural exports earning over KES 300 billion annually"],
                            ["4. Government Tax Revenues", "Corporation tax on factory profits, PAYE on salaries, and VAT on sales", "Funds public schools, hospitals, tarmac highways, and the SGR railway", "KRA collecting over KES 2 trillion to finance national development budgets"],
                            ["5. Resource Utilization", "Prevents fertile land, mineral deposits, and human talent from idling", "Transforms raw natural endowment into tangible national capital", "Harnessing Olkaria geothermal steam to power clean industrial parks"]
                        ]
                    }
                }
            ],
            # Card 5: Step-by-Step Worked Example
            [
                {
                    "type": "worked_example",
                    "title": "Worked Example: Calculating Value-Added Contribution to National GDP",
                    "content": {
                        "intro": "Trace the value-added contribution to national GDP across three stages of a tea production value chain in Kenya: Stage 1 (Farmer harvests green leaf sold to factory for KES 30 per kg); Stage 2 (Factory dries, cuts, and packs black tea sold to distributor for KES 90 per kg); Stage 3 (Distributor transports and retails packaged tea in supermarkets for KES 150 per kg). Calculate the total GDP contribution for 1,000 kg.",
                        "steps": [
                            "**Step 1 — Understand what we are finding:** Calculate the value added at each production stage (Primary, Secondary, Tertiary) and confirm that the sum of value added equals the final retail GDP contribution.",
                            "**Step 2 — Identify given information (per kg of tea):**\n- Stage 1 (Primary - Farmer sale) = $\\text{KES } 30$\n- Stage 2 (Secondary - Factory sale) = $\\text{KES } 90$\n- Stage 3 (Tertiary - Retail supermarket sale) = $\\text{KES } 150$\n- Volume = $1,000\\text{ kg}$",
                            "**Step 3 — Choose the formulas:**\n$$\\text{Value Added} = \\text{Stage Output Value} - \\text{Intermediate Input Cost}$$\n$$\\text{Total GDP Contribution} = \\sum \\text{Value Added across all 3 stages}$$",
                            "**Step 4 — Perform the calculations step by step:**\n- **Stage 1 (Primary Sector - Farming):**\n  - Output value = $1,000 \\times 30 = \\text{KES } 30,000$\n  - Input cost = $\\text{KES } 0$ (direct natural extraction)\n  - **Value Added (Primary) = KES 30,000**\n\n- **Stage 2 (Secondary Sector - Manufacturing):**\n  - Output value = $1,000 \\times 90 = \\text{KES } 90,000$\n  - Input cost = $\\text{KES } 30,000$ (green leaves bought from farmer)\n  - **Value Added (Secondary) = 90,000 - 30,000 = KES 60,000**\n\n- **Stage 3 (Tertiary Sector - Distribution & Retail):**\n  - Output value = $1,000 \\times 150 = \\text{KES } 150,000$\n  - Input cost = $\\text{KES } 90,000$ (packaged tea bought from factory)\n  - **Value Added (Tertiary) = 150,000 - 90,000 = KES 60,000**\n\n- **Total GDP Contribution (Sum of Value Added):**\n  $$\\text{Total GDP} = 30,000 + 60,000 + 60,000 = \\mathbf{\\text{KES } 150,000}$$",
                            "**Step 5 — State the final answer:** The value chain contributes $\\mathbf{\\text{KES } 150,000}$ to national GDP (Primary: KES 30,000; Secondary: KES 60,000; Tertiary: KES 60,000).",
                            "**Step 6 — Economic Interpretation & Pitfall:** Notice that secondary processing and tertiary logistics together add $\\text{KES } 120,000$ ($80\\%$ of total GDP value). If Kenya only exported raw green leaves, the nation would lose $80\\%$ of potential economic wealth! Avoid double counting by measuring Value Added rather than summing gross sales."
                        ]
                    }
                }
            ],
            # Card 6: Kenyan Case Study & Video
            [
                {
                    "type": "real_world_example",
                    "title": "Kenyan Enterprise Case: SGR Logistics & The Agricultural Export Value Chain",
                    "content": {
                        "title": "Powering the National Economy from Kericho to Global Markets",
                        "text": "The Mombasa–Nairobi–Naivasha Standard Gauge Railway (SGR) illustrates the vital role of tertiary logistics in the national economy. Freight trains transport over 6 million tons of cargo annually, hauling processed tea, coffee, and manufactured cement to Mombasa Port while returning with imported industrial equipment. This infrastructure cuts cargo transit times from 3 days to under 8 hours, lowering consumer prices and boosting Kenya's international trade competitiveness."
                    }
                },
                {
                    "type": "suggested_video",
                    "title": "Macroeconomic Production, Economic Sectors & GDP Growth",
                    "content": {
                        "title": "How National Production Drives Gross Domestic Product (GDP)",
                        "youtube_id": "yoY_uH8-l6Y",
                        "url": "https://www.youtube.com/watch?v=yoY_uH8-l6Y",
                        "description": "Educational economics lecture examining the circular flow of production, Primary/Secondary/Tertiary sector value addition, and GDP calculation."
                    }
                }
            ],
            # Card 7: Formative Scenario-Based MCQs
            [
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 1: Secondary Production Classification",
                    "content": {
                        "question": "Which of the following business operations represents Secondary Production in the Kenyan economy?",
                        "options": [
                            "A farmer harvesting maize in Kitale",
                            "A commercial bank processing loan applications in Nairobi",
                            "A textile mill in Eldoret spinning raw cotton into school uniform fabric",
                            "A fisherman casting nets into Lake Victoria"
                        ],
                        "correct": "C",
                        "explanation": "Secondary production involves the manufacturing, processing, or industrial transformation of raw materials into finished or semi-finished goods (such as spinning raw cotton into textile fabric)."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 2: Impact of Domestic Manufacturing on Balance of Trade",
                    "content": {
                        "question": "How does establishing domestic fertilizer and electronic assembly factories directly improve Kenya's national balance of trade?",
                        "options": [
                            "It increases the country's dependence on expensive imported foreign goods",
                            "It substitutes expensive imports with locally made goods and enables export of surplus goods to EAC neighbors",
                            "It prevents commercial banks from issuing M-Pesa loans",
                            "It eliminates the need for any primary agricultural farming"
                        ],
                        "correct": "B",
                        "explanation": "Domestic manufacturing reduces import expenditure (import substitution) and creates surplus high-value goods for export to regional trading partners, thereby creating a favorable balance of trade and conserving foreign currency."
                    }
                }
            ],
            # Card 8: Synthesis & Key Takeaways
            [
                {
                    "type": "key_takeaway",
                    "title": "Lesson 9 Summary & Key Takeaways",
                    "content": {
                        "text": "1. **Sector Linkages**: Production connects Primary extraction, Secondary industrial processing, and Tertiary distribution services.\n2. **GDP Driver**: Gross Domestic Product measures the sum of value added across all three production sectors.\n3. **National Prosperity**: High domestic production creates stable jobs, expands tax revenues for public infrastructure, earns foreign exchange, and elevates national living standards."
                    }
                }
            ]
        ]
    }
]
