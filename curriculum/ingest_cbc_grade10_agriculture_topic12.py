"""
VLearn CBC Grade 10 Agriculture — Topic 12: Animal Rearing Project
Production Ingestion Engine (Deep Senior Secondary Pedagogical Edition)

Curriculum: CBC (ID: 5)
Grade: Grade 10 (ID: 5, Level: 10)
Subject: Agriculture
Topic: Animal Rearing Project (Topic Order: 12)

Decomposed into 10 Learning Units & 10 Published Lessons:
  1. Selecting an Animal Rearing Project I (Brainstorming and Feasibility Factors) (5 Pages, 10 Blocks)
  2. Selecting an Animal Rearing Project II (Selecting Mammals, Birds, or Insects) (5 Pages, 10 Blocks)
  3. Developing a Project Plan (Objectives, Activities, Resources, and Budgets) (5 Pages, 10 Blocks)
  4. Preparing a Project Budget (Detailed Agribusiness Calculations) (5 Pages, 10 Blocks)
  5. Installing Animal Rearing Structures and Housing (5 Pages, 11 Blocks)
  6. Preparing Record Templates and Routine Duty Schedules (5 Pages, 10 Blocks)
  7. Sourcing, Stocking, and Acclimatizing Livestock (5 Pages, 11 Blocks)
  8. Routine Management: Daily Feeding and Nutrition (5 Pages, 10 Blocks)
  9. Routine Management: Sanitation, Biosecurity, and Health (5 Pages, 10 Blocks)
  10. Evaluating Project Success and Financial Reporting (8 Pages, 17 Blocks)
"""

import os
import sys
import re
import django
from django.db import transaction

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from curriculum.models import (
    Curriculum, Grade, Subject, Topic, LearningUnit, Lesson, LessonBlock
)

def clean_text(text: str) -> str:
    """Removes bracket citations and normalizes unicode bullets into standard markdown list items."""
    if not text:
        return ""
    text = re.sub(r'\[(?:\d+|image_\d+|S\d+.*?|[\d,\s]{2,})\]', '', text)
    text = re.sub(r'^[ \t]*[•\u2022][ \t]*', '- ', text, flags=re.MULTILINE)
    text = re.sub(r'([^\n])[ \t]+[•\u2022][ \t]+', r'\1\n- ', text)
    text = re.sub(r'^([^\n\-\*\d\>#][^\n]*)\n(- |\* )', r'\1\n\n\2', text, flags=re.MULTILINE)
    return text.strip()

def clean_dict(data):
    """Recursively cleans all strings in dictionary/list data structures."""
    if isinstance(data, str):
        return clean_text(data)
    elif isinstance(data, dict):
        return {k: clean_dict(v) for k, v in data.items()}
    elif isinstance(data, list):
        return [clean_dict(item) for item in data]
    return data

def build_topic12_curriculum():
    """Returns the comprehensive pedagogical page and block structure for Grade 10 Topic 12: Animal Rearing Project."""
    return [
        # =====================================================================
        # LESSON 1: Selecting an Animal Rearing Project I (Feasibility Factors)
        # =====================================================================
        {
            "unit_order": 1,
            "unit_name": "Selecting an Animal Rearing Project I (Brainstorming and Feasibility Factors)",
            "unit_description": "Feasibility studies for micro-livestock; evaluating land/spatial footprints, capital assets (Capex vs Opex), water reliability, labor duty commitments, technical skills, and market demand.",
            "lesson_title": "Agribusiness Feasibility Studies: Resource Auditing, Capital Modeling, and Enterprise Selection",
            "pages": [
                [
                    {
                        "type": "suggested_image",
                        "title": "Smallholder Farmer Planning a Farm Livestock Project",
                        "content": {
                            "title": "Smallholder Farmer Planning a Farm Livestock Project",
                            "caption": "A Kenyan agricultural producer surveying farm land and water infrastructure before establishing a micro-livestock enterprise."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Feasibility Factors",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Define an **agricultural enterprise feasibility study**.",
                                "Evaluate 5 critical resource parameters: **Land/Space, Capital Assets, Water Security, Labor Rosters, and Technical Skills**.",
                                "Distinguish **Capital Expenditure (Capex)** from **Operational Expenditure (Opex)**.",
                                "Conduct a **market demand and price elasticity assessment** before animal stocking."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The Agribusiness Feasibility Framework",
                        "content": {
                            "title": "Planning for Agribusiness Success",
                            "text": "An agricultural project is a planned allocation of resources to generate specific animal commodities within a defined timeframe:\n\n- **The Risk of Unplanned Farming**: Rearing animals without a preliminary feasibility study frequently results in premature project collapse due to feed shortages, space constraints, or missing markets.\n- **The Micro-Livestock Advantage**: For Senior School agricultural clubs and urban homesteads, micro-livestock (rabbits, poultry, guinea pigs, black soldier fly larvae) offer compact spatial footprints ($<10\\text{ m}^2$), rapid capital turnover (4–16 weeks), and low startup costs compared to large ruminants."
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "Resource Auditing: Space, Capital, Water, Labor, and Markets",
                        "content": {
                            "title": "The 5 Pillars of Enterprise Viability",
                            "text": "1. **Land and Spatial Footprint**: Can animals be housed vertically (multi-tier rabbit hutches, battery cages) or horizontally (deep litter coops)?\n2. **Capital Assets**:\n  - *Capex (Startup)*: Permanent durable assets (housing timber, wire mesh, feeders, drinkers, initial parent stock).\n  - *Opex (Recurring)*: Consumable daily inputs (commercial feed, veterinary drugs, disinfectants, transport, water bills).\n3. **Water Security**: Micro-livestock require daily access to clean, pathogen-free water. Hauling water manually adds unsustainable labor costs.\n4. **Labor and Routine Duty**: Animals require daily care (morning and afternoon feeding/cleaning). Student duty rosters ensure zero animal neglect.\n5. **Target Market Demand**: Always identify consumers and selling prices *before* purchasing day-old stock!"
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Livestock Enterprise Feasibility Matrix",
                        "content": {
                            "title": "Livestock Enterprise Feasibility Matrix",
                            "caption": "Agribusiness decision engine: 1 Land & Space Audit -> 2 Capex & Opex Capital -> 3 Water & Labor Commitments -> 4 Market Demand -> 5 Enterprise Selection."
                        }
                    }
                ],
                [
                    {
                        "type": "comparison_table",
                        "title": "Resource Feasibility Matrix for School Livestock Projects",
                        "content": {
                            "title": "Micro-Livestock Enterprise Resource Matrix",
                            "headers": ["Livestock Enterprise", "Spatial Requirement", "Startup Capital (Capex)", "Production Cycle Duration", "Market Liquidity"],
                            "rows": [
                                ["Broiler Poultry", "Very Low (Deep litter / cages)", "Moderate (KES 15,000–30,000)", "4 – 6 Weeks (Fastest)", "Very High (Immediate local demand)"],
                                ["Cuniculture (Rabbits)", "Very Low (Vertical hutches)", "Low to Moderate (KES 10,000–20,000)", "12 – 16 Weeks", "Moderate (Requires targeted buyers)"],
                                ["Layer Poultry", "Low (Deep litter / cages)", "High (KES 40,000–80,000)", "18 – 20 Weeks pre-lay; 18 months laying", "Very High (Daily cash-flow from eggs)"],
                                ["Dairy Goats", "Moderate (Elevated pens)", "High (KES 30,000–50,000)", "5 Months gestation; long lactation", "High (Premium goat milk prices)"],
                                ["Black Soldier Fly Larvae", "Micro (<2 m² plastic bins)", "Very Low (KES 3,000–8,000)", "2 – 3 Weeks", "High (Used on-farm as protein feed)"]
                            ]
                        }
                    }
                ],
                [
                    {
                        "type": "mini_activity",
                        "title": "Field Practical: School Farm Feasibility and Spatial Audit",
                        "content": {
                            "title": "Feasibility Audit Practicum",
                            "task": "1. Survey available space on your school farm.\n2. Measure square footage and assess distance to clean water and classrooms.\n3. Interview 10 students and staff to assess local demand for broiler meat vs rabbit meat vs fresh eggs.\n4. Score three project options using a 20-point rubric and present your top recommendation.",
                            "materials": ["Measuring Tape", "Survey Form", "Clipboard"],
                            "safety": "Avoid walking near uncontained machinery or construction hazards."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Core Summary: Feasibility Factors",
                        "content": {
                            "title": "Key Takeaways",
                            "text": "- **Feasibility studies prevent enterprise failure** before spending capital.\n- **Capex covers durable housing/tools**; **Opex covers recurring feeds/drugs**.\n- **Micro-livestock maximize space efficiency** for schools and urban plots.\n- **Identify your market and price margins** before buying parent stock."
                        }
                    }
                ],
                [
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Matching Enterprise to Water and Capital Constraints",
                        "content": {
                            "question": "A school agricultural club has a very small startup budget, limited water supply, small land area, and wants a project that produces marketable protein within 6 weeks. Which enterprise is most feasible?",
                            "options": [
                                "Establishing a high-yield dairy cow unit",
                                "Rearing a flock of 50 broiler chickens on a deep litter floor",
                                "Setting up a commercial rainbow trout fish pond",
                                "Rearing a herd of 20 dairy goats"
                            ],
                            "answer": "B",
                            "explanation": "Broiler chickens require minimal spatial footprint, have a rapid 4–6 week production turnaround, consume manageable amounts of water compared to cattle or trout ponds, and generate rapid revenue to recover operational costs."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 2: Selecting an Animal Rearing Project II (Mammals, Birds, Insects)
        # =====================================================================
        {
            "unit_order": 2,
            "unit_name": "Selecting an Animal Rearing Project II (Selecting Mammals, Birds, or Insects)",
            "unit_description": "Comparative animal selection: Cuniculture (rabbits) and dairy goats vs Avian (Broilers and Layers) vs Insects (Black Soldier Fly Larvae); matching biological traits to school constraints.",
            "lesson_title": "Comparative Livestock Biology: Mammalian, Avian, and Insect Micro-Livestock Pathways",
            "pages": [
                [
                    {
                        "type": "suggested_image",
                        "title": "New Zealand White Meat Rabbit in Clean Breeding Hutch",
                        "content": {
                            "title": "New Zealand White Meat Rabbit in Clean Breeding Hutch",
                            "caption": "A purebred New Zealand White rabbit, a premier commercial meat breed known for rapid growth, high fecundity, and efficient forage utilization."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Species Comparison",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Compare biological traits of **Mammals (Rabbits, Goats)**, **Birds (Broilers, Layers)**, and **Insects (BSFL)**.",
                                "Analyze **growth cycles, feed conversion, and reproductive rates** across livestock categories.",
                                "Evaluate the **forage supplementation advantage of cuniculture**.",
                                "Select the optimal species based on school resource constraints."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Cuniculture: The Rabbit Enterprise",
                        "content": {
                            "title": "High-Fecundity Mammalian Micro-Livestock",
                            "text": "- **Biological Advantages**: Rabbits have a short gestation period ($30\\text{--}32\\text{ days}$) and high fecundity (a single doe produces 4–5 litters per year, yielding 30+ kits). They reach $2.0\\text{--}2.5\\text{ kg}$ market weight in **12 to 16 weeks**.\n- **Dietary Flexibility**: Rabbits are hindgut herbivores that can thrive on cheap, locally harvested wild forages (blackjack, sweet potato vines, lucerne) supplemented with pellets, reducing feed costs by up to $50\\%$.\n- **Challenges**: Sensitive to high heat, coccidiosis, and digestive bloat if fed unwilted green forage."
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "Avian and Insect Pathways: Broilers, Layers, and BSFL",
                        "content": {
                            "title": "Rapid Turnaround vs Daily Cash Flow vs Bio-Recycling",
                            "text": "1. **Broiler Poultry**: Market-ready in **4 to 6 weeks** with high Feed Conversion Efficiency. Capital-intensive; requires $100\\%$ commercial crumbles and brooder heating.\n2. **Layer Poultry**: Point of lay at **18 to 20 weeks**; produces daily cash-flow from eggs for 12–18 months. High initial pre-lay feeding investment.\n3. **Black Soldier Fly Larvae (BSFL)**: Reared on organic kitchen waste, bioconverting waste into high-protein ($>40\\%$ crude protein) livestock feed in **2 to 3 weeks** with near-zero land requirements!"
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Micro-Livestock Selection Comparison: Rabbits vs Broilers vs BSFL",
                        "content": {
                            "title": "Micro-Livestock Selection Comparison: Rabbits vs Broilers vs BSFL",
                            "caption": "Comparative biological dynamics: Left: Cuniculture (Forage-fed, 16-week cycle) | Center: Broiler Poultry (Commercial crumbles, 6-week cycle) | Right: BSFL Insect Bio-conversion (Organic waste, 3-week cycle)."
                        }
                    }
                ],
                [
                    {
                        "type": "comparison_table",
                        "title": "Biological and Operational Comparison of Project Species",
                        "content": {
                            "title": "Project Species Operational Matrix",
                            "headers": ["Biological Parameter", "Meat Rabbits (Cuniculture)", "Broiler Chickens", "Black Soldier Fly Larvae (BSFL)"],
                            "rows": [
                                ["Primary Feed Source", "Wilted forages + Pellets", "100% Commercial Crumbles", "Organic kitchen & market waste"],
                                ["Turnaround to Market", "12 – 16 Weeks", "4 – 6 Weeks", "2 – 3 Weeks"],
                                ["Feed Cost Exposure", "Low (50% local greens)", "High (100% purchased feed)", "Near Zero (Free organic waste)"],
                                ["Vulnerability to Cold", "Low (Tolerate cool climate)", "High (Require artificial heat brooding)", "Moderate (Require warm bins)"],
                                ["Primary Commercial Product", "Lean white meat & pelts", "Tender dressed chicken meat", "High-protein animal feed supplement"]
                            ]
                        }
                    }
                ],
                [
                    {
                        "type": "mini_activity",
                        "title": "Classroom Practical: Comparative Enterprise Pitch Debate",
                        "content": {
                            "title": "Livestock Selection Pitching Practicum",
                            "task": "1. Divide into 3 groups: Team Rabbit, Team Broiler, Team BSFL.\n2. Each team has 3 minutes to present why their species is the best choice for Grade 10 Term 2.\n3. Defend questions regarding feed costs, mortality risks, and local market sales.\n4. Vote on the winning school enterprise.",
                            "materials": ["Pitch Worksheet", "Timer"],
                            "safety": "Engage in respectful, evidence-based academic debate."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Core Summary: Species Comparison",
                        "content": {
                            "title": "Key Takeaways",
                            "text": "- **Rabbits have high fecundity and utilize local forages**.\n- **Broilers offer the fastest turnaround (4–6 weeks)** but require high feed capital.\n- **Layers provide daily revenue** but require a 5-month pre-lay investment.\n- **BSFL recycle food waste** into high-protein animal feed."
                        }
                    }
                ],
                [
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Forage Feeding Economics in Rabbits",
                        "content": {
                            "question": "Why is a rabbit meat rearing project considered to have lower financial operating risk for a school club compared to a commercial broiler poultry project?",
                            "options": [
                                "Rabbits do not drink any water during their lifetime",
                                "Rabbits can utilize free, locally harvested farm forages (sweet potato vines, blackjack) to meet up to 50% of their diet, whereas broilers require 100% expensive commercial feed",
                                "Rabbits are immune to all diseases and parasites",
                                "Rabbit cages can be built without wire mesh"
                            ],
                            "answer": "B",
                            "explanation": "Feed accounts for 60–70% of livestock operational costs. Broilers must consume 100% balanced commercial starter and finisher feeds. Rabbits are herbivores that can thrive on wilted farm weeds and forages supplemented with small amounts of pellets, drastically lowering cash operational expenditures."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 3: Developing a Project Plan (Objectives, Activities, Budgets)
        # =====================================================================
        {
            "unit_order": 3,
            "unit_name": "Developing a Project Plan (Objectives, Activities, Resources, and Budgets)",
            "unit_description": "SMART project objectives; 4-phase chronological activity mapping (pre-stocking, stocking, management, marketing); budget architecture (Capex, Opex, depreciation, net profit formula).",
            "lesson_title": "Agribusiness Project Planning: SMART Objectives, Chronological Phasing, and Budget Architecture",
            "pages": [
                [
                    {
                        "type": "suggested_image",
                        "title": "Agricultural Student Formulating Farm Project Plans on Clipboard",
                        "content": {
                            "title": "Agricultural Student Formulating Farm Project Plans on Clipboard",
                            "caption": "An agricultural student documenting SMART goals, activity timelines, resource schedules, and financial budgets on a project clipboard."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Project Planning",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Formulate **SMART project objectives** (Specific, Measurable, Achievable, Relevant, Time-bound).",
                                "Map activities across **4 chronological phases: Pre-stocking, Stocking, Management, Marketing**.",
                                "Categorize all project inputs into **Capex vs Opex**.",
                                "Construct the **Net Profit and Depreciation mathematical model**."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Formulating SMART Agribusiness Objectives",
                        "content": {
                            "title": "Setting Clear Performance Targets",
                            "text": "A project plan without clear objectives is bound to lose direction. Objectives must follow the **SMART** standard:\n\n- **Weak Objective**: *'We will rear some chickens and try to make a profit.'*\n- **SMART Objective**: *'To rear **50 Cobb-500 broiler chickens** on the school farm to an average live weight of **2.2 kg within 6 weeks**, achieving a Feed Conversion Ratio of **$\\le 1.8$** and generating a net profit of **KES 12,000** by August 2026.'*"
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "The 4 Chronological Activity Phases",
                        "content": {
                            "title": "Chronological Project Execution",
                            "text": "1. **Phase 1: Pre-Stocking (Weeks -3 to 0)**: Siting structures, purchasing timber and wire mesh, constructing housing, installing feeders/drinkers, cleaning, and disinfecting.\n2. **Phase 2: Stocking & Acclimatization (Day 0 to Week 1)**: Sourcing certified day-old chicks/weaners, stress-free transport, setting up anti-stress glucose water, and brooder heating.\n3. **Phase 3: Routine Management (Weeks 1 to 6/16)**: Daily feeding, watering, litter turning, vaccination schedules, biosecurity enforcement, and growth weighing.\n4. **Phase 4: Harvesting, Marketing & Financial Audit (Final Week)**: Humane slaughtering, dressing, packaging, selling, and compiling final Profit & Loss reports."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Financial Budget Architecture: Capex, Opex & Net Profit",
                        "content": {
                            "title": "The Accounting Model of Agribusiness",
                            "text": "- **Capital Expenditure (Capex)**: Durable assets used across multiple cycles (Coop timber, wire mesh, feeders, brooder stove).\n- **Operational Expenditure (Opex)**: Consumables used in a single cycle (Chicks, feed, vaccines, charcoal, disinfectant).\n- **Depreciation**: The wear-and-tear cost of Capex allocated per cycle (typically $10\\%$ of Capex).\n\n$$\\text{Total Production Cost} = \\text{Opex} + \\text{Depreciation on Capex}$$\n$$\\text{Net Profit} = \\text{Gross Revenue} - \\text{Total Production Cost}$$"
                        }
                    }
                ],
                [
                    {
                        "type": "comparison_table",
                        "title": "Input Expenditure Classification Matrix",
                        "content": {
                            "title": "Capex vs Opex Expenditure Classification",
                            "headers": ["Project Item / Resource", "Accounting Category", "Durable Life Span", "Financial Treatment"],
                            "rows": [
                                ["Galvanized Wire Mesh & Timber", "Capex (Startup)", "3 – 5 Years", "Depreciated 10% per production cycle"],
                                ["Plastic Hanging Feeders & Drinkers", "Capex (Startup)", "3 – 5 Years", "Depreciated 10% per production cycle"],
                                ["50 Day-Old Broiler Chicks", "Opex (Running)", "1 Production Cycle (6 wks)", "100% expensed in current cycle"],
                                ["Commercial Starter & Finisher Feed", "Opex (Running)", "1 Production Cycle", "100% expensed in current cycle"],
                                ["Gumboro & Newcastle Vaccines", "Opex (Running)", "1 Production Cycle", "100% expensed in current cycle"]
                            ]
                        }
                    }
                ],
                [
                    {
                        "type": "mini_activity",
                        "title": "Classroom Practical: Drafting a 6-Week Broiler Project Gantt Chart",
                        "content": {
                            "title": "Project Activity Timeline Practicum",
                            "task": "1. Using a large sheet of paper, draw a 6-week project timeline grid.\n2. Map out all essential tasks: Brooder pre-heating (Day -1), Newcastle vaccination (Day 7), Gumboro vaccination (Day 14), Feed transition to Finisher (Day 21), Final market weighing (Day 42).\n3. Assign student group leaders to each activity block.",
                            "materials": ["Manila Paper", "Ruler", "Colored Markers"],
                            "safety": "Ensure realistic timeline pacing."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Core Summary: Project Planning",
                        "content": {
                            "title": "Key Takeaways",
                            "text": "- **SMART objectives define clear weight, time, and profit targets**.\n- **Execute across 4 chronological phases** to prevent operational delays.\n- **Include 10% Capex depreciation** in total production cost calculations.\n- **Net Profit equals Gross Revenue minus (Opex + Depreciation)**."
                        }
                    }
                ],
                [
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Capex vs Opex Classification",
                        "content": {
                            "question": "Which of the following items in a 50-bird poultry project is correctly classified as a Capital Expenditure (Capex)?",
                            "options": [
                                "Three 50kg bags of Broiler Starter feed",
                                "A bottle of Newcastle eye-drop vaccine",
                                "Purchasing 4 durable plastic hanging tube feeders and galvanized wire mesh for coop construction",
                                "Charcoal used to heat the brooder jiko during week 1"
                            ],
                            "answer": "C",
                            "explanation": "Capex refers to durable physical assets that last across multiple years and production cycles (feeders, wire mesh, timber). Feeds, vaccines, and charcoal are consumable inputs used up in a single cycle, making them Operational Expenditures (Opex)."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 4: Preparing a Project Budget (Agribusiness Calculations)
        # =====================================================================
        {
            "unit_order": 4,
            "unit_name": "Preparing a Project Budget (Detailed Agribusiness Calculations)",
            "unit_description": "Feed requirement formulas (4.5 kg feed/broiler $\times$ 50 birds = 225 kg / 5 bags); production cost modeling; mortality buffer; break-even price formula; Net Profit & ROI.",
            "lesson_title": "Agribusiness Mathematical Modeling: Feed Consumption, Break-Even Thresholds, and ROI",
            "pages": [
                [
                    {
                        "type": "suggested_image",
                        "title": "Commercial Poultry Flock Consuming Balanced Feed from Hoppers",
                        "content": {
                            "title": "Commercial Poultry Flock Consuming Balanced Feed from Hoppers",
                            "caption": "Broiler chickens consuming commercial feed from hanging hoppers, illustrating the mathematical feed budget required for commercial livestock growth."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Budget Calculations",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Calculate **total feed requirements and bag quantities** for a livestock flock.",
                                "Model total operational costs including **mortality risk buffers ($4\\%$)**.",
                                "Calculate the exact **Break-Even Price per marketable bird**.",
                                "Project **Gross Revenue, Net Profit, and Return on Investment (ROI)**."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Step 1: Calculating Feed Requirements",
                        "content": {
                            "title": "The Mathematical Feed Formula",
                            "text": "Feed is the single largest operational cost ($60\\text{--}70\\%$ of total Opex):\n\n- **Standard Broiler Feed Intake**: $1\\text{ broiler}$ consumes **$4.5\\text{ kg}$ of feed** over $6\\text{ weeks}$ ($1.2\\text{ kg}$ Starter + $3.3\\text{ kg}$ Finisher).\n- **Total Feed for 50 Broilers**: $50 \\times 4.5\\text{ kg} = 225\\text{ kg}$.\n- **Bag Calculation ($50\\text{ kg bags}$)**: $225\\text{ kg} / 50\\text{ kg/bag} = 4.5\\text{ bags} \\rightarrow \\mathbf{5\\text{ bags}}$ (round up to prevent shortages).\n- **Feed Cost (at KES 4,000/bag)**: $5 \\times \\text{KES }4,000 = \\mathbf{\\text{KES }20,000}$."
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "Step 2: Total Cost and Break-Even Calculations",
                        "content": {
                            "title": "Finding the Minimum Survival Price",
                            "text": "- **Total Capex**: $\\text{KES }15,000$ (Depreciation at $10\\% = \\mathbf{\\text{KES }1,500}$).\n- **Total Opex**:\n  - 50 Day-old chicks (at KES 100): $\\text{KES }5,000$\n  - 5 Bags of feed: $\\text{KES }20,000$\n  - Vaccines, charcoal, vitamins: $\\text{KES }3,000$\n  - Total Opex = $\\text{KES }28,000$.\n- **Total Production Cost**: $\\text{KES }28,000 + \\text{KES }1,500 = \\mathbf{\\text{KES }29,500}$.\n- **Mortality Factor ($4\\%$)**: $2\\text{ birds die} \\rightarrow \\mathbf{48\\text{ surviving birds}}$.\n\n$$\\text{Break-Even Price} = \\frac{\\text{Total Production Cost}}{\\text{Surviving Marketable Birds}} = \\frac{\\text{KES }29,500}{48} = \\mathbf{\\text{KES }614.58 \\approx \\text{KES }615}$$"
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Agribusiness Financial Pipeline: Capex, Opex, Break-Even & ROI",
                        "content": {
                            "title": "Agribusiness Financial Pipeline: Capex, Opex, Break-Even & ROI",
                            "caption": "Financial computation engine: 1 Capex & Opex Summation -> 2 Total Cost (KES 29,500) -> 3 Surviving Birds (48) -> 4 Break-Even Threshold (KES 615) -> 5 Market Sale (KES 850) -> 6 Net Profit (KES 11,300, ROI 38.3%)."
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "Step 3: Revenue, Net Profit, and ROI",
                        "content": {
                            "title": "Profitability and Return on Investment",
                            "text": "If mature broilers are sold at the prevailing market price of **KES 850 per bird**:\n\n- **Gross Revenue**: $48\\text{ birds} \\times \\text{KES }850 = \\mathbf{\\text{KES }40,800}$.\n- **Net Profit**: $\\text{Gross Revenue} - \\text{Total Production Cost} = \\text{KES }40,800 - \\text{KES }29,500 = \\mathbf{\\text{KES }11,300}$.\n- **Return on Investment (ROI)**:\n\n$$\\text{ROI} = \\left( \\frac{\\text{Net Profit}}{\\text{Total Production Cost}} \\right) \\times 100 = \\left( \\frac{\\text{KES }11,300}{\\text{KES }29,500} \\right) \\times 100 = \\mathbf{38.3\\%}$$"
                        }
                    },
                    {
                        "type": "comparison_table",
                        "title": "Financial Sensitivity Analysis (Selling Price vs Net Profit)",
                        "content": {
                            "title": "Market Price Sensitivity Matrix (48 Surviving Birds)",
                            "headers": ["Market Price per Bird", "Gross Revenue (KES)", "Total Production Cost (KES)", "Net Profit / Loss (KES)", "Return on Investment (%)"],
                            "rows": [
                                ["KES 550 (Distress Sale)", "26,400", "29,500", "-3,100 (LOSS)", "-10.5% (Negative ROI)"],
                                ["KES 615 (Break-Even Price)", "29,520", "29,500", "+20 (Zero Profit)", "0.0% (Cost Recovery)"],
                                ["KES 750 (Wholesale Price)", "36,000", "29,500", "+6,500 (Profit)", "+22.0% (Moderate ROI)"],
                                ["KES 850 (Target Retail Price)", "40,800", "29,500", "+11,300 (Profit)", "+38.3% (High ROI)"],
                                ["KES 950 (Premium Dressed Price)", "45,600", "29,500", "+16,100 (Profit)", "+54.6% (Exceptional ROI)"]
                            ]
                        }
                    }
                ],
                [
                    {
                        "type": "mini_activity",
                        "title": "Classroom Practical: Enterprise Budget Calculator Workshop",
                        "content": {
                            "title": "Budget Calculation Practicum",
                            "task": "1. Calculate the feed budget for a 100-broiler project assuming 4.5kg feed per bird at KES 3,800 per 50kg bag.\n2. Add KES 10,000 for chicks, KES 5,000 for vet drugs, and KES 2,500 for depreciation.\n3. Compute the break-even price per bird assuming a 5% mortality rate (95 surviving birds).\n4. Calculate net profit if sold at KES 800 per bird.",
                            "materials": ["Calculator", "Worksheet", "Pen"],
                            "safety": "Verify all mathematical rounding up of feed bags."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Core Summary: Budget Calculations",
                        "content": {
                            "title": "Key Takeaways",
                            "text": "- **Broilers consume 4.5 kg of feed** over 6 weeks.\n- **Round feed bags up** to prevent mid-cycle feed shortages.\n- **Break-even price is Total Cost divided by surviving birds**.\n- **Selling above break-even generates positive ROI** ($>35\\%$)."
                        }
                    }
                ],
                [
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Break-Even Price Calculation",
                        "content": {
                            "question": "A poultry club spends a total of KES 30,000 to raise 100 broilers. If 5 birds die during the rearing cycle, what is the exact minimum break-even price per bird the club must charge for the remaining 95 birds to avoid a financial loss?",
                            "options": [
                                "KES 300.00",
                                "KES 315.79",
                                "KES 285.00",
                                "KES 350.00"
                            ],
                            "answer": "B",
                            "explanation": "Break-even price is Total Production Cost divided by surviving marketable units: KES 30,000 / 95 surviving birds = KES 315.79 per bird. Selling below KES 315.79 results in a financial loss; selling above it generates a profit."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 5: Installing Animal Rearing Structures and Housing
        # =====================================================================
        {
            "unit_order": 5,
            "unit_name": "Installing Animal Rearing Structures and Housing",
            "unit_description": "Housing siting and environmental orientation; elevated rabbit hutch design (0.9–1.2m legs, slotted 1.2cm floor, dark nest box, $1.0 \times 0.8 \times 0.6\text{ m}$); deep litter poultry coop design (10–15cm wood shavings, adjustable feeders, wire ventilation).",
            "lesson_title": "Livestock Housing Architecture: Siting Engineering, Elevated Hutches, and Deep Litter Coops",
            "pages": [
                [
                    {
                        "type": "suggested_image",
                        "title": "Elevated Wooden Rabbit Hutch with Slotted Flooring",
                        "content": {
                            "title": "Elevated Wooden Rabbit Hutch with Slotted Flooring",
                            "caption": "A professionally constructed outdoor rabbit hutch elevated on 1-meter legs, featuring slotted floors, wire ventilation mesh, and an external forage feeder rack."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Housing Architecture",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Analyze **siting criteria for livestock housing** (slope, wind orientation, drainage).",
                                "Construct an **elevated rabbit hutch ($0.9\\text{--}1.2\\text{ m}$ legs, $1.2\\text{ cm}$ slotted floor, nest box)**.",
                                "Design a **deep litter poultry coop ($10\\text{--}15\\text{ cm}$ wood shavings, wire ventilation)**.",
                                "Install **feeders and drinkers at animal back-level** to prevent feed contamination."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Siting Engineering for Livestock Housing",
                        "content": {
                            "title": "Positioning Housing for Health and Comfort",
                            "text": "- **Elevation and Drainage**: Site structures on gently sloping, well-drained ground to prevent water pooling around foundations, which rots timber and breeds pathogens.\n- **Wind Orientation**: Position solid walls against prevailing strong winds to prevent chilling drafts from blowing directly onto young animals, while orienting open mesh sides toward gentle breezes for continuous air exchange.\n- **Sunlight Alignment**: Orient long axes East-West so morning sun warms the pen while midday heat is blocked by roof overhangs."
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "Cuniculture Housing: The Elevated Rabbit Hutch",
                        "content": {
                            "title": "Engineering the Standard Rabbit Hutch",
                            "text": "1. **Leg Elevation ($0.9\\text{ to }1.2\\text{ m}$)**: Elevating the hutch on sturdy timber legs prevents ground predators (dogs, rats, safari ants) from entering and places cages at a comfortable working height for keepers.\n2. **Slotted Floor ($1.2\\text{ cm}$ Spacing)**: Use heavy galvanized wire mesh or wooden slats spaced **precisely $1.2\\text{ cm}$ apart**. This allows droppings and urine to fall through to the ground below, keeping paws dry and preventing **sore hocks and coccidiosis**.\n3. **Dimensions**: Standard single doe unit: **$1.0\\text{ m (length)} \\times 0.8\\text{ m (width)} \\times 0.6\\text{ m (height)}$** with an attached dark, warm **nesting box**."
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Standard Elevated Rabbit Hutch Architectural Blueprint",
                        "content": {
                            "title": "Standard Elevated Rabbit Hutch Architectural Blueprint",
                            "caption": "Blueprint: 1 1.0m Elevated Legs with Metal Ant Deflectors, 2 1.2cm Slotted Wire Floor, 3 Dark Enclosed Nesting Compartment (Kindling Box), 4 Exterior Wire Hay Feeder Rack, 5 Sloping Corrugated Iron Roof."
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "Poultry Housing: The Deep Litter System",
                        "content": {
                            "title": "Ventilation and Floor Litter Standards",
                            "text": "- **Continuous Wire Ventilation**: Open-sided structure with chicken wire covering the top half of walls to vent out hot air and toxic **ammonia gas ($<10\\text{ ppm}$)**.\n- **Deep Litter ($10\\text{ to }15\\text{ cm}$)**: Cover concrete or rammed-earth floors with clean wood shavings or chopped straw. The litter absorbs moisture from droppings and insulates birds from the cold ground.\n- **Suspended Feeders and Drinkers**: Hang hoppers and bell drinkers at **the level of the birds' backs**. This prevents birds from scratching feed onto the floor or defecating in drinking water."
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Deep Litter Poultry Coop Ventilation & Feeder Elevation",
                        "content": {
                            "title": "Deep Litter Poultry Coop Ventilation & Feeder Elevation",
                            "caption": "Poultry coop engineering: 1 10–15cm Clean Wood Shaving Deep Litter -> 2 Feeders & Bell Drinkers Suspended at Birds' Back-Level -> 3 Upper Wire Mesh Open-Air Ventilation Ridge -> 4 0.5m Roof Overhang."
                        }
                    }
                ],
                [
                    {
                        "type": "comparison_table",
                        "title": "Rabbit Hutch vs Deep Litter Coop Structural Comparison",
                        "content": {
                            "title": "Livestock Structure Comparison Matrix",
                            "headers": ["Structural Feature", "Elevated Rabbit Hutch", "Deep Litter Poultry Coop"],
                            "rows": [
                                ["Floor Type", "Elevated slotted timber / wire ($1.2\\text{ cm}$ gap)", "Ground floor with $10\\text{--}15\\text{ cm}$ wood shavings litter"],
                                ["Waste Management", "Waste falls through to collection ground", "Litter turned weekly; cleaned between cycles"],
                                ["Ventilation Mechanism", "Full wire-mesh front and sides", "Upper-wall wire mesh; solid lower wall ($0.6\\text{ m}$)"],
                                ["Predator Defense", "$1\\text{ m}$ legs with grease/metal ant baffles", "Perimeter wire netting buried $30\\text{ cm}$ into soil"],
                                ["Special Compartment", "Dark, warm nesting box for kindling doe", "Darkened laying nest boxes (for layer hens)"]
                            ]
                        }
                    }
                ],
                [
                    {
                        "type": "mini_activity",
                        "title": "Field Practical: Building a Model Rabbit Hutch / Poultry Tractor",
                        "content": {
                            "title": "Housing Construction Practicum",
                            "task": "1. Using timber offcuts, wire mesh, and roofing nails, construct a model elevated rabbit hutch.\n2. Measure floor slats using a 1.2cm spacer block to ensure perfect dung clearance without foot trapping.\n3. Attach an external wire forage rack on the side door.\n4. Apply used engine oil / wood preservative on external posts.",
                            "materials": ["Timber", "Wire Mesh", "Nails", "Hammer", "Spacer Block"],
                            "safety": "Wear safety goggles and gloves when sawing and nailing."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Core Summary: Housing Architecture",
                        "content": {
                            "title": "Key Takeaways",
                            "text": "- **Elevate rabbit hutches 1 meter off the ground** with 1.2 cm floor gaps.\n- **Maintain 10–15 cm clean deep litter** in poultry coops.\n- **Hang feeders at the birds' back-level** to prevent feed fouling.\n- **Provide continuous upper-wall ventilation** to eliminate ammonia."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Rationale for 1.2cm Slotted Floor Spacing",
                        "content": {
                            "question": "Why must the floor slats or wire mesh of an elevated rabbit hutch be spaced precisely 1.2 cm apart?",
                            "options": [
                                "To let the rabbits climb down to the ground when hungry",
                                "To allow manure pellets and urine to drop through freely while keeping the rabbits' paws dry and preventing their feet from slipping through or getting trapped",
                                "To allow sunlight to heat the bottom of the rabbit",
                                "To prevent air from entering the hutch"
                            ],
                            "answer": "B",
                            "explanation": "A 1.2cm gap is the ideal engineering dimension for rabbits. It allows round manure droppings and urine to fall through cleanly into collection trays, keeping the rabbit dry and preventing coccidiosis, while being narrow enough to safely support the rabbit's paws without trapping legs."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 6: Preparing Record Templates and Routine Duty Schedules
        # =====================================================================
        {
            "unit_order": 6,
            "unit_name": "Preparing Record Templates and Routine Duty Schedules",
            "unit_description": "4 Core livestock logs: Animal Inventory, Feeding/Watering, Production/Growth, and Health/Medication (with drug withdrawal tracking); structured morning (7:00 AM) and afternoon (4:30 PM) duty rosters.",
            "lesson_title": "Agribusiness Data Systems: 4-Core Farm Records, Drug Withdrawal Logs, and Duty Rosters",
            "pages": [
                [
                    {
                        "type": "suggested_image",
                        "title": "Livestock Manager Inspecting Farm Records and Inventory Sheet",
                        "content": {
                            "title": "Livestock Manager Inspecting Farm Records and Inventory Sheet",
                            "caption": "A farm manager auditing a physical livestock record ledger, tracking daily feed intake, mortalities, vaccinations, and drug withdrawal dates."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Farm Records & Duty Rosters",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Structure the **4 core farm record books: Inventory, Feeding, Growth/Production, and Health**.",
                                "Track **drug withdrawal periods** in health logs to ensure food safety.",
                                "Design an **equitable morning and afternoon student duty roster**.",
                                "Audit live farm data to detect **subclinical diseases and feed wastage early**."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The 4 Core Farm Record Templates",
                        "content": {
                            "title": "The Written Memory of the Agribusiness",
                            "text": "Without structured records, a farmer cannot calculate profitability or diagnose operational issues:\n\n1. **Animal Inventory Log**: Tracks stock movements.\n   $$\\text{Closing Stock} = \\text{Opening Stock} + \\text{Births/Purchases} - \\text{Deaths/Sales}$$\n2. **Feeding & Expense Log**: Records daily kilograms consumed, brand name, batch number, and cost.\n3. **Production & Growth Log**: Records weekly bird/rabbit weight measurements, egg production counts, and cullings.\n4. **Health & Medication Log**: Documents disease symptoms, drug administered, dosage, veterinary cost, and **mandatory drug withdrawal dates**."
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "Health Records and the Drug Withdrawal Period",
                        "content": {
                            "title": "Ensuring Food Safety and Regulatory Compliance",
                            "text": "- **What is the Drug Withdrawal Period?**: The mandatory minimum time that must elapse between the last administration of a veterinary drug (antibiotic, dewormer, coccidiostat) and the slaughter of the animal (or sale of its eggs/milk).\n- **Why It Matters**: Selling meat or eggs before the withdrawal period expires exposes human consumers to dangerous chemical residues and drives **Antimicrobial Resistance (AMR)**.\n- **Health Record Requirement**: Health logs must prominently highlight the **'Safe for Market Date'** for every treated animal!"
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "4-Core Farm Record-Keeping Ledger Architecture",
                        "content": {
                            "title": "4-Core Farm Record-Keeping Ledger Architecture",
                            "caption": "Data ledger system: 1 Animal Inventory (Stock balance) | 2 Feed Intake & Expenses (Cost control) | 3 Growth & Production (ADG/FCR) | 4 Health & Treatment (Drug withdrawal tracking)."
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "The Routine Student Duty Roster",
                        "content": {
                            "title": "Ensuring Continuous 365-Day Animal Care",
                            "text": "- **Equitable Role Sharing**: Divide students into paired teams on a rotating weekly schedule.\n- **Morning Shift (7:00 AM)**:\n  - Inspect all animals for alertness and signs of sickness.\n  - Empty, scrub, and refill water drinkers with fresh water.\n  - Top up feed hoppers to **1/3 full**; sweep droppings.\n  - Record any mortalities in the inventory log.\n- **Afternoon Shift (4:30 PM)**:\n  - Check water levels; cut and wilt fresh forage (for rabbits).\n  - Collect eggs; secure all latches and locks to prevent night predators.\n  - Finalize daily entries in the record binder."
                        }
                    },
                    {
                        "type": "comparison_table",
                        "title": "Standard Health & Medication Record Template",
                        "content": {
                            "title": "Health & Treatment Log Sample",
                            "headers": ["Date", "Animal / Flock ID", "Clinical Symptom", "Treatment / Drug", "Withdrawal Days", "Safe Market Date"],
                            "rows": [
                                ["10/08", "Broiler Batch A", "Ruffled feathers, coccidiosis", "Amprolium 20% in water", "7 Days", "17/08"],
                                ["15/08", "Doe Rabbit #3", "Ear crusts / Mange mites", "Ivermectin 1% injection", "14 Days", "29/08"],
                                ["20/08", "Pullet Flock B", "Sneezing / Respiratory noise", "Tylosin Tartrate powder", "5 Days", "25/08"]
                            ]
                        }
                    }
                ],
                [
                    {
                        "type": "mini_activity",
                        "title": "Classroom Practical: Designing a 4-Template Project Record Binder",
                        "content": {
                            "title": "Farm Record Binder Practicum",
                            "task": "1. In your project notebooks, draw out the four blank record tables: Inventory, Feeding, Growth, and Health.\n2. Mock-fill the first 3 rows of each table using hypothetical broiler data.\n3. Calculate closing stock after a 2-bird mortality event.\n4. Calculate the drug withdrawal date for an antibiotic administered today.",
                            "materials": ["Project Notebook", "Ruler", "Pen"],
                            "safety": "Ensure neat, legible handwriting for legal audit compliance."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Core Summary: Farm Records & Rosters",
                        "content": {
                            "title": "Key Takeaways",
                            "text": "- **Keep 4 core records: Inventory, Feeding, Growth, and Health**.\n- **Track drug withdrawal periods** to prevent chemical meat contamination.\n- **Divide daily care into Morning (7:00 AM) and Afternoon (4:30 PM) shifts**.\n- **Audit records weekly** to catch feed waste and mortality spikes."
                        }
                    }
                ],
                [
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Rationale for Drug Withdrawal Tracking",
                        "content": {
                            "question": "Why is it strictly mandatory under agricultural and food safety laws to document the exact date of drug administration and the withdrawal period in a farm Health Log?",
                            "options": [
                                "To calculate how much water the animal drank",
                                "To ensure meat or eggs are not sold to consumers while containing harmful drug residues, protecting public health and preventing antimicrobial resistance",
                                "To prove that the medicine made the animal grow feathers",
                                "To increase the weight of the animal before weighing"
                            ],
                            "answer": "B",
                            "explanation": "Veterinary drugs require a specific metabolic clearance time (withdrawal period). Selling meat or eggs before this window clears exposes consumers to active antibiotics and chemicals, which violates food safety standards and promotes drug-resistant bacterial strains."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 7: Sourcing, Stocking, and Acclimatizing Livestock
        # =====================================================================
        {
            "unit_order": 7,
            "unit_name": "Sourcing, Stocking, and Acclimatizing Livestock",
            "unit_description": "Sourcing from certified commercial hatcheries/breeders; physical health inspection checklist for day-old chicks and weaner rabbits; stress-free transport; acclimatization with glucose + multivitamin anti-stress water.",
            "lesson_title": "Stocking Operations: Certified Breeder Sourcing, Quality Screening, and Anti-Stress Acclimatization",
            "pages": [
                [
                    {
                        "type": "suggested_image",
                        "title": "Day-Old Broiler Chicks in Commercial Brooder Under Heat Lamp",
                        "content": {
                            "title": "Day-Old Broiler Chicks in Commercial Brooder Under Heat Lamp",
                            "caption": "Healthy day-old broiler chicks clustered actively under an infrared brooder heat lamp, demonstrating proper temperature, clean litter, and anti-stress drinker setup."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Stocking & Acclimatization",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Identify **certified, reputable sources** for purchasing parent livestock.",
                                "Execute a **physical health screening checklist** on day-old chicks and weaners.",
                                "Implement **stress-free livestock transport protocols**.",
                                "Formulate **anti-stress drinking water (glucose + multivitamins)** for incoming stock."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Sourcing Certified Stock vs Open-Market Hazards",
                        "content": {
                            "title": "The Foundation of Herd Quality",
                            "text": "- **Certified Commercial Sources**: Always purchase day-old chicks from certified hatcheries (e.g., Kenchic, Muguku) or weaner rabbits from registered breeding stations. Certified stock guarantees uniform genetics, high parent immunity, and freedom from seed-borne pathogens.\n- **The Open-Market Hazard**: Never buy loose stock from roadside open-air markets. Animals in open markets are exposed to mixed disease carriers, subclinical Newcastle/coccidiosis infections, and transport stress, resulting in $>40\\%$ farm mortalities!"
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "Visual Health Screening Checklist",
                        "content": {
                            "title": "Physical Inspection Before Purchase",
                            "text": "1. **Day-Old Chicks**:\n  - *Alertness*: Highly active, responsive to tapping sounds.\n  - *Down Feathers*: Clean, dry, fluffy down (no pasted vents or white diarrhea staining).\n  - *Eyes & Beak*: Bright round eyes, straight clean beak.\n  - *Navel & Legs*: Fully healed, closed dry navel (no black scabs/infection); straight, strong legs (no spraddle legs).\n2. **Weaner Rabbits**:\n  - *Ears*: Clean and pink (zero brown crusts or ear mites).\n  - *Nose & Paws*: Clean dry nose; paws free of matted fur (matted front paws indicate chronic wiping of nasal discharge/snuffles).\n  - *Eyes & Coat*: Bright clear eyes, smooth glossy fur."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Transport and Anti-Stress Acclimatization Protocol",
                        "content": {
                            "title": "Minimizing Transport Stress",
                            "text": "- **Transport Timing**: Move stock during the **cool morning hours ($6:00\\text{--}8:00\\text{ AM}$)** or late evening in well-ventilated, wood-shaving-lined crates.\n- **The Anti-Stress Water Solution**: Upon arrival, provide immediate access to clean water fortified with **glucose ($20\\text{ g/L}$) and multivitamins**.\n  - *Glucose*: Rapidly absorbed simple sugar that replenishes depleted glycogen stores after transport exhaustion.\n  - *Multivitamins (A, D3, E, B-complex)*: Strengthen the immune system against opportunistic bacteria.\n- **Quiet Rest**: Allow newly arrived stock to rest in a warm, dimly lit environment for the first 2–4 hours before introducing heavy feed."
                        }
                    }
                ],
                [
                    {
                        "type": "suggested_video",
                        "title": "Day-Old Chick Brooding and Acclimatization Setup",
                        "content": {
                            "title": "Day-Old Chick Brooding and Acclimatization Setup",
                            "description": "Agronomic video guide demonstrating brooder ring construction, temperature regulation, drinker placement, and anti-stress water administration.",
                            "url": "https://www.youtube.com/watch?v=chick-brooding-guide"
                        }
                    },
                    {
                        "type": "comparison_table",
                        "title": "Healthy Stock vs Defective Stock Screening Matrix",
                        "content": {
                            "title": "Stocking Health Screening Matrix",
                            "headers": ["Diagnostic Checkpoint", "Prime High-Quality Stock", "Defective Rejected Stock", "Associated Pathological Risk"],
                            "rows": [
                                ["Chicks: Navel Region", "Dry, clean, fully healed navel", "Unhealed wet navel with black scab", "Omphalitis (Yolk sac infection); early death"],
                                ["Chicks: Vent Area", "Dry, fluffy down feathers", "Pasted vent with white chalky feces", "Salmonellosis / Pullorum disease"],
                                ["Rabbits: Front Paws", "Dry, clean, uniform hair", "Matted, crusty inner paws", "Pasteurellosis (Snuffles / Runny nose wiping)"],
                                ["Rabbits: Inner Ears", "Smooth, pink, clean skin", "Brown crusty scabs and foul odor", "Psoroptic ear canker mites"]
                            ]
                        }
                    }
                ],
                [
                    {
                        "type": "mini_activity",
                        "title": "Field Practical: Formulating Anti-Stress Water and Brooder Setup",
                        "content": {
                            "title": "Stocking Acclimatization Practicum",
                            "task": "1. Set up a brooder ring with wood shavings and an infrared heat lamp (Target: 32–35°C).\n2. Dissolve 20g glucose powder and 5g soluble poultry multivitamin in 1 liter of clean water.\n3. Dip the beaks of 5 incoming chicks gently into the water to teach them where to drink.\n4. Observe their dispersal pattern under the heat lamp.",
                            "materials": ["Brooder Guard", "Heat Lamp", "Glucose Powder", "Multivitamins", "Drinker"],
                            "safety": "Handle young chicks with extreme gentleness."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Core Summary: Stocking & Acclimatization",
                        "content": {
                            "title": "Key Takeaways",
                            "text": "- **Source only from certified commercial breeders**.\n- **Reject chicks with unhealed navels or pasted vents**.\n- **Transport stock during cool morning hours**.\n- **Provide glucose + multivitamin water immediately** to overcome stress."
                        }
                    }
                ],
                [
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Function of Anti-Stress Glucose Water",
                        "content": {
                            "question": "Why is it standard poultry practice to offer newly arrived day-old chicks drinking water fortified with glucose and multivitamins before offering them commercial starter crumbles?",
                            "options": [
                                "The glucose turns their down feathers white",
                                "Transport causes severe glycogen depletion and physical exhaustion; glucose provides immediate metabolic energy to recover, while vitamins boost immunity against opportunistic transport stress pathogens",
                                "Chicks cannot eat dry feed until they are two months old",
                                "The sugar water sterilizes the chicken coop floor"
                            ],
                            "answer": "B",
                            "explanation": "Newly hatched chicks experience severe metabolic exhaustion and dehydration during transport. Glucose is a simple monosaccharide absorbed directly into the bloodstream without digestion, providing instant cellular energy, while multivitamins stimulate immune response."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 8: Routine Management: Daily Feeding and Nutrition
        # =====================================================================
        {
            "unit_order": 8,
            "unit_name": "Routine Management: Daily Feeding and Nutrition",
            "unit_description": "Phase feeding (Broiler Starter 20–22% CP vs Finisher); feed waste reduction (hoppers 1/3 full at back-level); safe local rabbit forages and the mandatory 12–24h wilting rule to prevent fatal bloat/tympany.",
            "lesson_title": "Nutritional Management: Phase Feeding Protocols, Feed Wastage Mitigation, and Forage Wilting",
            "pages": [
                [
                    {
                        "type": "suggested_image",
                        "title": "Domestic Rabbit Consuming Fresh Wilted Green Grass and Forage",
                        "content": {
                            "title": "Domestic Rabbit Consuming Fresh Wilted Green Grass and Forage",
                            "caption": "A domestic rabbit feeding on clean, properly wilted forage from an elevated hay rack, illustrating safe fiber nutrition without bloat risk."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Feeding & Nutrition",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Implement **phase feeding (Broiler Starter 20–22% CP vs Broiler Finisher)**.",
                                "Apply the **1/3 feeder fill and back-level height rule** to prevent feed wastage.",
                                "Identify **safe local green forages** for cuniculture.",
                                "Explain the biological necessity of **wilting fresh forages for 12–24 hours to prevent fatal bloat/tympany**."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Phase Feeding in Commercial Broilers",
                        "content": {
                            "title": "Matching Nutrients to Growth Biology",
                            "text": "Broilers have distinct nutritional requirements as their bodies develop:\n\n1. **Weeks 1 to 3 (Broiler Starter Crumbles)**: Contains **$20\\text{--}22\\%$ Crude Protein (CP)** and high amino acids (lysine, methionine) to accelerate rapid skeletal framework development, organ growth, and immune priming.\n2. **Weeks 4 to 6 (Broiler Finisher Pellets)**: Contains **$18\\text{--}19\\%$ Crude Protein** with higher metabolizable energy (carbohydrates and fats) to promote rapid muscle bulk deposition and weight gain before market sale."
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "Feed Wastage Reduction: The 1/3 Fill Rule",
                        "content": {
                            "title": "Stopping the Direct Drain on Farm Profits",
                            "text": "Feed spilled on the floor is trampled, soiled with manure, promotes fungal mold, and attracts wild rodents:\n- **The 1/3 Fill Rule**: Never fill feed hoppers to the brim! Fill hoppers only **one-third (1/3) full**. Filling to the top leads to $>30\\%$ feed wastage as birds 'beak-scratch' feed onto the floor.\n- **Adjustable Height**: Keep the lip of the feeder aligned with the **level of the bird's back**. If too low, birds stand in the feeder; if too high, feeding is restricted.\n- **Daily Cleaning**: Sieve powdered dust out of feeders daily; chickens refuse to eat dusty residue."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Forage Nutrition in Rabbits: The 12–24h Wilting Rule",
                        "content": {
                            "title": "Safe Herbivorous Feeding Dynamics",
                            "text": "- **Safe Forages**: Blackjack (*Bidens pilosa*), Sweet potato vines, Wandering Jew (*Commelina diffusa*), Lucerne, and Sow thistle.\n- **THE MANDATORY WILTING RULE**: Never feed freshly cut, wet, or dew-covered green forage directly to rabbits!\n  - Fresh green forage must be spread in shade and **wilted for 12 to 24 hours** before feeding.\n  - *The Fatal Bloat Pathology*: High-moisture fresh greens undergo rapid microbial fermentation in the rabbit's cecum, producing massive gas buildup (**Bloat / Tympany**). The distended cecum presses on the diaphragm, suffocating the rabbit to death within hours!"
                        }
                    }
                ],
                [
                    {
                        "type": "comparison_table",
                        "title": "Fresh Green Forage vs Properly Wilted Forage Comparison",
                        "content": {
                            "title": "Forage Management Comparison Matrix",
                            "headers": ["Forage State", "Moisture Content", "Cecal Fermentation Rate", "Digestive Health Outcome"],
                            "rows": [
                                ["Freshly Cut Dewy Forage", ">85% Moisture", "Excessively rapid fermentation", "Fatal acute bloat (tympany), severe watery scours"],
                                ["12–24h Wilted Forage", "60 – 70% Moisture", "Normal, controlled fermentation", "Healthy gut motility, high nutrient absorption, safe growth"],
                                ["Dry Hay (Rhodes / Lucerne)", "<15% Moisture", "Slow structural fermentation", "Optimal crude fiber source, prevents trichobezoars (hairballs)"]
                            ]
                        }
                    }
                ],
                [
                    {
                        "type": "mini_activity",
                        "title": "Field Practical: Forage Harvesting, Identification, and Wilting Lab",
                        "content": {
                            "title": "Forage Wilting Practicum",
                            "task": "1. Harvest 2 kg of sweet potato vines and blackjack from the school garden.\n2. Spread 1 kg on a clean mesh screen in the shade to wilt for 12 hours.\n3. Weigh both batches to measure moisture loss.\n4. Observe how wilted forage becomes limp and pliable, eliminating excess surface water.",
                            "materials": ["Harvesting Shears", "Weighing Scale", "Drying Screen"],
                            "safety": "Do not harvest plants from areas sprayed with chemical pesticides."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Core Summary: Feeding & Nutrition",
                        "content": {
                            "title": "Key Takeaways",
                            "text": "- **Feed Broiler Starter (20–22% CP) for weeks 1–3**, then Finisher for weeks 4–6.\n- **Fill feeders only 1/3 full at back-level** to stop feed wastage.\n- **Rabbits thrive on safe wild forages** supplemented with pellets.\n- **Always wilt fresh green forage for 12–24 hours** to prevent fatal bloat."
                        }
                    }
                ],
                [
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Rationale for Forage Wilting in Rabbits",
                        "content": {
                            "question": "A student harvests fresh, dew-covered sweet potato vines and feeds them directly to weaner rabbits. Within 12 hours, several rabbits have swollen abdomens, breathe with difficulty, and die. What is the scientific cause of this mortality?",
                            "options": [
                                "The student accidentally fed the rabbits poisonous timber",
                                "Feeding fresh, high-moisture green forage triggered rapid microbial fermentation in the rabbit's cecum, producing massive gas buildup (bloat/tympany) that compressed the lungs and caused fatal suffocation",
                                "The rabbits choked on the dry leaves",
                                "The dew on the leaves contained rabies virus"
                            ],
                            "answer": "B",
                            "explanation": "Rabbits are hindgut cecal fermenters. Fresh, wet, or dew-covered greens contain high moisture and soluble sugars that ferment uncontrollably in the cecum, creating severe gas distension (bloat/tympany). Wilting forages for 12–24h in the shade reduces water content and ensures safe digestion."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 9: Routine Management: Sanitation, Biosecurity, and Health
        # =====================================================================
        {
            "unit_order": 9,
            "unit_name": "Routine Management: Sanitation, Biosecurity, and Health",
            "unit_description": "3 Pillars of farm biosecurity: Isolation, Sanitation, and Traffic Control; daily drinker washing; weekly deep litter raking; entry disinfectant footbaths; Disease Action Plan (The Three Is: Isolate, Investigate, Immunize/Treat).",
            "lesson_title": "Apiary & Farm Biosecurity: 3 Pillars, Disinfectant Footbaths, and Disease Protocols",
            "pages": [
                [
                    {
                        "type": "suggested_image",
                        "title": "Modern Commercial Poultry Unit with Biosecurity Layout",
                        "content": {
                            "title": "Modern Commercial Poultry Unit with Biosecurity Layout",
                            "caption": "An engineered poultry house showing clean perimeter wire netting, raised foundations, closed visitor entrances, and a bio-sanitary footbath at the doorway."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Sanitation & Biosecurity",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Define **farm biosecurity** and explain its **3 pillars: Isolation, Sanitation, Traffic Control**.",
                                "Execute **daily drinker washing and weekly deep litter raking**.",
                                "Construct and maintain a **disinfectant entry footbath**.",
                                "Apply the **'Three Is' Disease Action Plan (Isolate, Investigate, Immunize/Treat)**."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The 3 Pillars of Farm Biosecurity",
                        "content": {
                            "title": "Creating a Biological Defense Shield",
                            "text": "**Biosecurity** encompasses all management practices designed to prevent pathogens from entering or spreading across a farm:\n\n1. **Isolation**: Keeping the livestock unit fully fenced and screened against wild birds, rodents, stray dogs, and unauthorized visitors.\n2. **Sanitation**: Routine cleaning, scrubbing, and chemical disinfection of water drinkers, feeders, cages, and boots.\n3. **Traffic Control**: Restricting entry to authorized students/keepers wearing dedicated clean boots and stepping through disinfectant footbaths."
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "Sanitation Protocols and the Entry Footbath",
                        "content": {
                            "title": "Mechanical Barrier Against Pathogens",
                            "text": "- **Daily Sanitation**: Scrub water drinkers daily with clean water and mild disinfectant *before* refilling. Remove wet, clumped litter immediately.\n- **Weekly Maintenance**: Rake and turn poultry deep litter to aerate it and prevent ammonia gas buildup. Disinfect wall perimeters.\n- **The Disinfectant Footbath**: A shallow tray containing a broad-spectrum disinfectant solution (e.g., Virkon-S, copper sulfate, bleaching solution) placed at the **sole entrance** of the livestock shed. Every person must step into the footbath to sterilize footwear before entering!"
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Farm Biosecurity Perimeter & Disinfected Entry Footbath",
                        "content": {
                            "title": "Farm Biosecurity Perimeter & Disinfected Entry Footbath",
                            "caption": "Biosecurity architecture: 1 Perimeter Fence with 'No Unauthorized Visitors' Sign -> 2 Disinfectant Entry Footbath Tray (Virkon-S/Chlorine) -> 3 Dedicated Clean Gumboots -> 4 Isolated Quarantine Pen."
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "The 'Three Is' Disease Emergency Action Plan",
                        "content": {
                            "title": "Immediate Response to Sickness",
                            "text": "When an animal shows clinical symptoms (lethargy, coughing, bloody diarrhea, abnormal posture):\n\n1. **ISOLATE**: Immediately remove the sick animal and place it in an **isolated quarantine pen** far from the healthy flock to stop pathogen transmission.\n2. **INVESTIGATE**: Examine symptoms, review health records, check environmental triggers (wet litter, cold drafts), and consult a veterinary officer.\n3. **IMMUNIZE / TREAT**: Administer prescribed veterinary medication to the sick animal and prophylactic treatment (vitamins/vaccines) to the healthy herd."
                        }
                    },
                    {
                        "type": "comparison_table",
                        "title": "Biosecurity Routine Protocols Schedule",
                        "content": {
                            "title": "Biosecurity Protocol Matrix",
                            "headers": ["Frequency", "Sanitation & Biosecurity Task", "Target Pathogens / Risks", "Operational Outcome"],
                            "rows": [
                                ["Daily (Every Shift)", "Scrub drinkers and replenish clean water", "E. coli, Salmonella, Coliform bacteria", "Zero water-borne gastrointestinal infections"],
                                ["Daily (Every Shift)", "Step in disinfected footbath at entrance", "Viruses and spores carried on shoe soles", "Mechanical disinfection; blocks external diseases"],
                                ["Weekly", "Rake and turn deep litter; add fresh shavings", "Coccidial oocysts, damp ammonia buildup", "Dry bedding; zero foot rot or ciliary paralysis"],
                                ["Between Cycles", "Total cleanout, blowtorch/lime disinfection, 2-wk rest", "Residual viral and bacterial bio-films", "Complete sanitary break; disease-free next batch"]
                            ]
                        }
                    }
                ],
                [
                    {
                        "type": "mini_activity",
                        "title": "Field Practical: Constructing and Testing an Entry Footbath",
                        "content": {
                            "title": "Footbath Construction Practicum",
                            "task": "1. Place a shallow plastic tray at the entrance of the school poultry/rabbit unit.\n2. Line the base with a clean gunny sack or sponge.\n3. Mix 50g disinfectant powder (or 50ml bleach) into 5 liters of clean water and pour into the tray.\n4. Demonstrate proper 10-second foot immersion before entering the shed.",
                            "materials": ["Shallow Tray", "Gunny Sack", "Disinfectant Solution", "Water"],
                            "safety": "Wear rubber gloves when handling concentrated disinfectant chemicals."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Core Summary: Sanitation & Biosecurity",
                        "content": {
                            "title": "Key Takeaways",
                            "text": "- **Biosecurity rests on 3 pillars: Isolation, Sanitation, Traffic Control**.\n- **Scrub drinkers daily**; rake deep litter weekly.\n- **Step in a disinfected footbath** at every entrance.\n- **Follow the 'Three Is': Isolate, Investigate, Immunize/Treat**."
                        }
                    }
                ],
                [
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Rationale for Disinfectant Footbaths",
                        "content": {
                            "question": "What is the primary agricultural purpose of maintaining a disinfected footbath at the entrance of a school poultry coop?",
                            "options": [
                                "To wash mud off chickens' feet when they walk into the coop",
                                "To mechanically destroy disease-causing viruses, bacteria, and fungal spores carried on visitors' shoe soles, preventing the introduction of pathogens into the flock",
                                "To provide drinking water for chickens",
                                "To keep the entrance floor wet and cool"
                            ],
                            "answer": "B",
                            "explanation": "Human footwear carries millions of fungal spores, bacterial cells, and viral particles picked up from across the farm. Stepping into a disinfected footbath kills these pathogens mechanically on contact, breaking the chain of infection before entering the poultry house."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 10: Evaluating Project Success and Financial Reporting
        # =====================================================================
        {
            "unit_order": 10,
            "unit_name": "Evaluating Project Success and Financial Reporting",
            "unit_description": "Production data synthesis: Average Daily Gain (ADG), Feed Conversion Ratio (FCR = Feed / Gain); constructing a Profit & Loss Statement; compiling final agribusiness presentation; Kisumu Unplanned Agribusiness diagnostic audit; 8 Summative Topic Assessment MCQs.",
            "lesson_title": "Project Evaluation: Production KPIs, Profit & Loss Statements, and Summative Assessment",
            "pages": [
                [
                    {
                        "type": "suggested_image",
                        "title": "Commercial Broiler Chickens Reaching Market Weight in Barn",
                        "content": {
                            "title": "Commercial Broiler Chickens Reaching Market Weight in Barn",
                            "caption": "Uniform, healthy broiler chickens reaching market harvest weight at 6 weeks, ready for final weighing, dressing, and financial accounting."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Project Evaluation & Summative Assessment",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Synthesize the **complete Animal Rearing Project agribusiness framework**.",
                                "Compute **Key Performance Indicators: Average Daily Gain (ADG), Feed Conversion Ratio (FCR), Mortality Rate, and Net Profit Margin**.",
                                "Construct a formal **Profit and Loss (P&L) Financial Statement**.",
                                "Complete the comprehensive **Summative Topic Assessment** covering all 10 lessons of Topic 12."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Evaluating Biological Production KPIs: ADG and FCR",
                        "content": {
                            "title": "The Mathematics of Biological Efficiency",
                            "text": "1. **Average Daily Gain (ADG)**: Measures the daily rate of live body weight growth.\n\n$$\\text{ADG} = \\frac{\\text{Final Weight (g)} - \\text{Initial Weight (g)}}{\\text{Project Duration in Days}}$$\n\n2. **Feed Conversion Ratio (FCR)**: Measures how efficiently animals convert feed into meat. A **lower FCR is superior** (indicates higher efficiency and lower production cost!):\n\n$$\\text{FCR} = \\frac{\\text{Total Commercial Feed Consumed (kg)}}{\\text{Total Live Weight Gained by Flock (kg)}}$$\n\n- *Target Broiler FCR*: **$1.6\\text{ to }1.8$** ($1.8\\text{ kg feed}$ produces $1.0\\text{ kg meat}$). If FCR exceeds $2.2$, feed is being wasted or animals are diseased!"
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "Master Animal Rearing Project Agribusiness Lifecycle Matrix",
                        "content": {
                            "title": "The Unified Project Execution Lifecycle",
                            "text": "1. **Feasibility**: Space, Capex/Opex capital, water security, labor rosters, local market demand.\n2. **Species Selection**: Broilers (fast 6-wk turnaround) vs Rabbits (forage-efficient 16-wk cycle) vs BSFL.\n3. **Planning & Budgeting**: SMART objectives, 4 activity phases, feed calculations, break-even thresholds.\n4. **Housing Architecture**: Elevated rabbit hutches ($1.2\\text{ cm}$ slotted floor, nest box) vs Deep litter poultry coops ($10\\text{--}15\\text{ cm}$ shavings, upper wire ventilation).\n5. **Data & Duty**: 4 core logs (Inventory, Feed, Growth, Health with drug withdrawal); morning/afternoon shifts.\n6. **Stocking & Nutrition**: Certified breeders, anti-stress water (glucose + vitamins), phase feeding, 12–24h forage wilting.\n7. **Biosecurity & Sanitation**: 3 pillars, disinfected footbaths, 'Three Is' disease plan.\n8. **Financial Audit**: ADG, FCR, P&L Statement, ROI, and class presentation."
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Master Animal Rearing Project Agribusiness Lifecycle Matrix",
                        "content": {
                            "title": "Master Animal Rearing Project Agribusiness Lifecycle Matrix",
                            "caption": "Master project execution engine: 1 Feasibility & Species Selection -> 2 SMART Plan & Budget -> 3 Housing Construction -> 4 Stocking & Acclimatization -> 5 Daily Feeding & Biosecurity -> 6 Harvesting, P&L Audit & Presentation."
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "Constructing the Final Profit & Loss (P&L) Statement",
                        "content": {
                            "title": "The Accounting Capstone",
                            "text": "The student enterprise must construct a formal Profit and Loss Statement reconciling all revenues and expenditures:\n\n- **Total Revenue**: Product sales (meat birds, dressed rabbit carcasses, eggs) + secondary by-products (manure bags, pelts).\n- **Total Expenses**: Day-old stock purchase + Commercial feed + Veterinary drugs/vaccines + Heating fuel + Housing depreciation ($10\\%$ of Capex).\n- **Net Profit**: $\\text{Total Revenue} - \\text{Total Expenses}$.\n- **Net Profit Margin**: $(\\text{Net Profit} / \\text{Total Revenue}) \\times 100$."
                        }
                    },
                    {
                        "type": "comparison_table",
                        "title": "Completed 50-Broiler Project Profit & Loss Statement",
                        "content": {
                            "title": "Grade 10 Model Broiler Enterprise P&L Statement",
                            "headers": ["Revenue Category (Inflows)", "Amount (KES)", "Expense Category (Outflows)", "Amount (KES)"],
                            "rows": [
                                ["Sale of 48 Dressed Broilers (at KES 850)", "40,800", "50 Day-Old Chicks (at KES 100)", "5,000"],
                                ["Sale of 2 Bags Poultry Manure (at KES 500)", "1,000", "5 Bags Commercial Feed (Starter & Finisher)", "20,000"],
                                ["", "", "Vaccines, Vitamins & Antibiotics", "2,000"],
                                ["", "", "Charcoal for Brooder Jiko", "1,000"],
                                ["", "", "Housing Depreciation (10% of KES 15,000 Capex)", "1,500"],
                                ["TOTAL GROSS REVENUE", "41,800", "TOTAL PRODUCTION COST", "29,500"],
                                ["NET ENTERPRISE PROFIT", "+12,300", "NET PROFIT MARGIN", "29.4%"]
                            ]
                        }
                    }
                ],
                [
                    {
                        "type": "mini_activity",
                        "title": "Performance Task: The 'Kisumu Unplanned Agribusiness' Diagnostic Audit",
                        "content": {
                            "title": "Commercial Livestock Consulting Case",
                            "task": "A student club skipped planning, built a pen on wet ground, bought 100 open-market chicks, and fed kitchen scraps. By week 4, 30 chicks died from cold drafts and dampness. The remaining 70 birds required 9 weeks to reach 1.5kg, consuming 400kg of feed.\n\n**Your Deliverable**: Write an Expert Diagnostic Report:\n1. Identify 3 critical sourcing, housing, and nutrition errors committed.\n2. Calculate mortality rate and Feed Conversion Ratio (FCR = 400kg / [70 birds * 1.5kg]).\n3. Provide corrective architectural, nutritional, and biosecurity recommendations.",
                            "materials": ["Case Handout", "Response Template", "Pen"],
                            "safety": "Ensure rigorous, evidence-based recommendations."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Core Summary: Project Evaluation",
                        "content": {
                            "title": "Key Takeaways",
                            "text": "- **Compute FCR to measure feed efficiency** (Target: 1.6–1.8 for broilers).\n- **Include 10% housing depreciation** in total production costs.\n- **P&L statements reconcile revenue against total costs**.\n- **Present findings, challenges, and ROI** to the class."
                        }
                    }
                ],
                # Pages 5 to 8: 8 Summative Assessment MCQs
                [
                    {
                        "type": "knowledge_check",
                        "title": "Summative MCQ 1: Biological Rationale of Feed Conversion Ratio",
                        "content": {
                            "question": "A school agriculture club raises broilers. The flock gains a total of 100 kg of live body weight and consumed 180 kg of commercial feed. What is the Feed Conversion Ratio (FCR), and what does this number indicate?",
                            "options": [
                                "FCR = 0.55; indicates that the birds lost weight",
                                "FCR = 1.80; indicates that the birds required 1.8 kg of feed to produce 1.0 kg of live body weight",
                                "FCR = 1.00; indicates perfect zero waste",
                                "FCR = 2.80; indicates that 2.8 birds died"
                            ],
                            "answer": "B",
                            "explanation": "Feed Conversion Ratio (FCR) is calculated as Total Feed Consumed / Total Weight Gained = 180 kg / 100 kg = 1.80. A lower FCR indicates superior feed efficiency and profitability."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Summative MCQ 2: Elevated Rabbit Hutch Engineering",
                        "content": {
                            "question": "Why is it mandatory in cuniculture housing engineering to elevate rabbit hutches 1 meter off the ground with wire-mesh or slotted floors spaced 1.2 cm apart?",
                            "options": [
                                "To let the rabbits climb up trees to escape heat",
                                "To protect vulnerable rabbits from ground predators (dogs, rats, safari ants) and allow manure droppings and urine to fall through cleanly, keeping paws dry and preventing coccidiosis and sore hocks",
                                "To make it impossible for students to reach the rabbits",
                                "To let the rabbits catch flying insects for protein"
                            ],
                            "answer": "B",
                            "explanation": "Elevating hutches 1m off the ground deters climbing predators and safari ants. The 1.2cm slotted floor allows urine and manure pellets to fall through immediately, keeping bedding dry and preventing parasitic coccidiosis and bacterial pododermatitis (sore hocks)."
                        }
                    }
                ],
                [
                    {
                        "type": "knowledge_check",
                        "title": "Summative MCQ 3: Mandatory Forage Wilting Rule in Rabbits",
                        "content": {
                            "question": "Why must fresh green forages (sweet potato vines, blackjack) harvested from the farm always be wilted in the shade for 12 to 24 hours before feeding them to rabbits?",
                            "options": [
                                "Wilting turns green leaves into yellow corn kernels",
                                "Fresh, high-moisture greens cause rapid, uncontrolled microbial fermentation in the rabbit's cecum, producing massive gas distension (bloat/tympany) that compresses the lungs and causes fatal suffocation",
                                "Rabbits refuse to touch any plant that is green",
                                "Wilting kills all the rabbit fleas"
                            ],
                            "answer": "B",
                            "explanation": "Rabbits are hindgut cecal fermenters. Feeding fresh, wet, or dew-covered greens introduces excess moisture and soluble sugars, triggering explosive bacterial fermentation and acute bloat (tympany). Wilting reduces moisture content, ensuring safe, controlled cecal fermentation."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Summative MCQ 4: Feeder Height and Waste Prevention",
                        "content": {
                            "question": "How should commercial poultry feed hoppers be managed inside a deep litter coop to minimize expensive feed wastage?",
                            "options": [
                                "Fill hoppers to overflowing and place them flat on the floor",
                                "Fill hoppers only one-third (1/3) full and suspend them so the feeding lip is level with the birds' backs",
                                "Scatter the dry feed by hand across the wood shaving litter",
                                "Mix the dry feed with mud before serving"
                            ],
                            "answer": "B",
                            "explanation": "Filling feeders to the brim leads to birds 'beak-scratching' and spilling over 30% of feed onto the floor. Filling hoppers 1/3 full and adjusting height to back-level prevents birds from scratching feed out or standing and defecating inside the trough."
                        }
                    }
                ],
                [
                    {
                        "type": "knowledge_check",
                        "title": "Summative MCQ 5: Function of Disinfectant Footbaths",
                        "content": {
                            "question": "What is the biological mechanism and primary purpose of maintaining a disinfected footbath at the entrance of a livestock rearing house?",
                            "options": [
                                "To provide drinking water for chickens that escape the coop",
                                "To mechanically destroy pathogenic viruses, bacteria, and fungal spores clinging to keepers' footwear before entering, preventing the introduction of infectious diseases into the flock",
                                "To keep the entrance floor muddy and cool",
                                "To wash off feathers from students' shoes"
                            ],
                            "answer": "B",
                            "explanation": "Footwear is the primary mechanical vector for introducing external farm pathogens into clean livestock housing. Stepping into a disinfected footbath kills viral, bacterial, and fungal particles on contact, preserving flock biosecurity."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Summative MCQ 6: Sourcing Hazards of Open-Air Markets",
                        "content": {
                            "question": "Why is it considered a critical management mistake to purchase day-old chicks or weaner rabbits from uncertified open-air livestock markets rather than registered commercial hatcheries?",
                            "options": [
                                "Open-air markets charge higher prices than certified hatcheries",
                                "Open-air market stock is mixed from diverse unknown sources, exposed to severe transport stress, and frequently carries subclinical viral and bacterial infections, resulting in high farm mortality",
                                "Open-air market chicks are born without wings",
                                "Open-market animals cannot eat commercial feed"
                            ],
                            "answer": "B",
                            "explanation": "Unregulated open-air markets mix stock from multiple unverified farms. Animals are stressed and frequently harbor incubating pathogens (Newcastle, Salmonella, Coccidiosis). Purchasing certified stock guarantees genetic uniformity, maternal antibody protection, and disease freedom."
                        }
                    }
                ],
                [
                    {
                        "type": "knowledge_check",
                        "title": "Summative MCQ 7: Importance of Drug Withdrawal Periods",
                        "content": {
                            "question": "Why is tracking the drug withdrawal period in a farm Health Log essential for public health and agribusiness ethics?",
                            "options": [
                                "It tells the farmer how many eggs the hen laid during treatment",
                                "It ensures animals are not slaughtered and sold for human consumption while their tissues still contain active veterinary drug residues, protecting consumers from chemical toxicity and preventing antimicrobial resistance",
                                "It makes the meat taste like medicine",
                                "It reduces the weight of the animal"
                            ],
                            "answer": "B",
                            "explanation": "All veterinary pharmaceuticals have a mandatory withdrawal period during which residues are metabolized and cleared from meat, milk, and eggs. Harvesting before clearance violates food safety standards and promotes dangerous antimicrobial resistance."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Summative MCQ 8: Break-Even Price Calculation",
                        "content": {
                            "question": "A school agriculture club spends KES 28,000 on Opex and KES 1,500 on depreciation to rear 50 broilers. If 2 birds die during the cycle (48 surviving birds), what is the minimum break-even price per bird?",
                            "options": [
                                "KES 590.00",
                                "KES 614.58 (approx. KES 615)",
                                "KES 560.00",
                                "KES 650.00"
                            ],
                            "answer": "B",
                            "explanation": "Total Production Cost = Opex (KES 28,000) + Depreciation (KES 1,500) = KES 29,500. Break-Even Price = Total Production Cost / Surviving Birds = KES 29,500 / 48 = KES 614.58 (approx. KES 615). Selling above KES 615 generates net profit."
                        }
                    }
                ],
                # Page 8: Capstone Summary
                [
                    {
                        "type": "summary",
                        "title": "Topic 12 Capstone Summary: Animal Rearing Project Mastery",
                        "content": {
                            "title": "Mastery Overview: Grade 10 Animal Rearing Agribusiness",
                            "text": "Congratulations on mastering **Topic 12: Animal Rearing Project**!\n\nYou have mastered:\n- **Feasibility & Resource Auditing**: Evaluating space footprints, Capex vs Opex capital, water security, labor rosters, and local market demand.\n- **Species Selection**: Broiler poultry (4–6 wk rapid cycle) vs Cuniculture (high fecundity, 50% forage feeding) vs BSFL bio-conversion.\n- **SMART Planning & Budgeting**: SMART objectives, 4 activity phases, feed consumption math (4.5kg/broiler), 10% depreciation, and break-even pricing.\n- **Housing Engineering**: Elevated rabbit hutches (1.0m legs, 1.2cm slotted floor, nest box) and deep litter poultry coops (10–15cm shavings, upper wire ventilation, back-level feeders).\n- **Data Systems & Rosters**: 4 core record logs (Inventory, Feeding, Growth, Health with drug withdrawal tracking); morning and afternoon duty rosters.\n- **Stocking & Acclimatization**: Certified breeder sourcing, quality screening checklist, cool-hour transport, and anti-stress glucose + multivitamin water.\n- **Nutrition & Wastage**: Phase feeding (Starter 20–22% CP vs Finisher), 1/3 feeder fill rule, and the mandatory 12–24h forage wilting rule against fatal bloat.\n- **Biosecurity & Health**: 3 pillars, entry disinfectant footbaths, and the 'Three Is' disease emergency protocol (Isolate, Investigate, Immunize/Treat).\n- **Project Evaluation**: ADG, FCR, P&L Financial Statements, Net Profit Margins, and class presentation delivery."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Topic 12 Final Takeaway",
                        "content": {
                            "title": "The Agribusiness Project Maxim",
                            "text": "Successful animal rearing is built on rigorous planning, precision feeding, biosecure housing, and meticulous record-keeping. Calculate your break-even thresholds, protect your stock with daily biosecurity, and operate every livestock unit as a profitable, sustainable commercial enterprise."
                        }
                    }
                ]
            ]
        }
    ]

@transaction.atomic
def ingest_grade10_topic12(replace=False):
    """Executes the complete production ingestion of Grade 10 Agriculture Topic 12: Animal Rearing Project."""
    print("=" * 80)
    print("STARTING INGESTION: CBC Grade 10 Agriculture — Topic 12: Animal Rearing Project")
    print("=" * 80)

    curriculum = Curriculum.objects.filter(name__iexact="CBC").first()
    grade = Grade.objects.filter(curriculum=curriculum, name__icontains="10").first()
    subject = Subject.objects.filter(grade=grade, name__iexact="Agriculture").first()

    assert curriculum and grade and subject, "Curriculum/Grade/Subject not found!"

    topic_name = "Animal Rearing Project"
    topic = Topic.objects.filter(subject=subject, name=topic_name).first()
    if not topic:
        topic = Topic.objects.create(
            subject=subject,
            name=topic_name,
            description="Intensive project-based training in micro-livestock enterprise management: feasibility studies, SMART budgeting, elevated rabbit hutches, deep litter coops, 4-core record keeping, anti-stress stocking, forage wilting, farm biosecurity, and Profit & Loss financial evaluation.",
            order=12
        )
        print(f"Created Topic 12: {topic.name} (ID: {topic.id})")
    else:
        topic.order = 12
        topic.description = "Intensive project-based training in micro-livestock enterprise management: feasibility studies, SMART budgeting, elevated rabbit hutches, deep litter coops, 4-core record keeping, anti-stress stocking, forage wilting, farm biosecurity, and Profit & Loss financial evaluation."
        topic.save()
        print(f"Resolved Topic 12: {topic.name} (ID: {topic.id})")

    if replace:
        print("Flag --replace active: Clearing existing LearningUnits and Lessons for Topic 12...")
        topic.learning_units.all().delete()
        topic.lessons.all().delete()

    curriculum_data = build_topic12_curriculum()
    total_units = 0
    total_lessons = 0
    total_pages = 0
    total_blocks = 0

    for item in curriculum_data:
        u_order = item["unit_order"]
        u_name = item["unit_name"]
        u_desc = item["unit_description"]
        l_title = item["lesson_title"]
        pages = item["pages"]

        unit, u_created = LearningUnit.objects.get_or_create(
            topic=topic,
            order=u_order,
            defaults={"name": u_name, "description": u_desc}
        )
        if not u_created:
            unit.name = u_name
            unit.description = u_desc
            unit.save()
        total_units += 1

        lesson, l_created = Lesson.objects.get_or_create(
            topic=topic,
            learning_unit=unit,
            defaults={
                "title": l_title,
                "status": "published",
                "version": 1,
                "immutable_metadata": {
                    "author": "VLearn Senior Curriculum Agent",
                    "grade": "Grade 10",
                    "subject": "Agriculture",
                    "topic_order": 12,
                    "unit_order": u_order
                }
            }
        )
        if not l_created:
            lesson.title = l_title
            lesson.status = "published"
            lesson.version = 1
            lesson.save()

        lesson.blocks.all().delete()
        total_lessons += 1

        block_order_counter = 1
        for page_idx, page_blocks in enumerate(pages, start=1):
            total_pages += 1
            for comp_idx, block_def in enumerate(page_blocks, start=1):
                b_type = block_def["type"]
                b_title = clean_text(block_def.get("title", ""))
                b_content = clean_dict(block_def.get("content", {}))

                LessonBlock.objects.create(
                    lesson=lesson,
                    block_id=f"g10_agri_t12_u{u_order}_p{page_idx}_b{comp_idx}",
                    block_type=b_type,
                    component_type=b_type,
                    title=b_title,
                    content=b_content,
                    order=block_order_counter,
                    page_number=page_idx,
                    component_order=comp_idx,
                    page_title=b_title if comp_idx == 1 else None,
                    metadata={"topic_order": 12, "unit_order": u_order, "page": page_idx}
                )
                block_order_counter += 1
                total_blocks += 1

        print(f"  Ingested Unit {u_order}: {u_name} -> Lesson '{l_title}' ({len(pages)} Pages, {block_order_counter - 1} Blocks)")

    print("=" * 80)
    print(f"INGESTION COMPLETE: Topic 12 '{topic.name}'")
    print(f"  Total Units:   {total_units}")
    print(f"  Total Lessons: {total_lessons}")
    print(f"  Total Pages:   {total_pages}")
    print(f"  Total Blocks:  {total_blocks}")
    print("=" * 80)

if __name__ == "__main__":
    replace_flag = "--replace" in sys.argv
    ingest_grade10_topic12(replace=replace_flag)
