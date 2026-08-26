"""
VLearn CBC Grade 10 Agriculture — Topic 15: Establishing an Agricultural Enterprise
Production Ingestion Engine (Deep Senior Secondary Pedagogical Edition)

Curriculum: CBC (ID: 5)
Grade: Grade 10 (ID: 5, Level: 10)
Subject: Agriculture
Topic: Establishing an Agricultural Enterprise (Topic Order: 15)

Decomposed into 13 Learning Units & 13 Published Lessons:
  1. Meaning and Types of Agricultural Enterprises (4 Pages, 9 Blocks)
  2. Factors to Consider when Establishing an Enterprise (4 Pages, 8 Blocks)
  3. Sourcing Agricultural Inputs (4 Pages, 9 Blocks)
  4. Capital Requirements & Types of Capital (4 Pages, 9 Blocks)
  5. Sourcing Financial Capital (4 Pages, 9 Blocks)
  6. Cost of Production (4 Pages, 8 Blocks)
  7. Formulating a Simple Farm Budget (4 Pages, 9 Blocks)
  8. Basic Farm Record Keeping (4 Pages, 9 Blocks)
  9. Preparing a Simple Profit & Loss Statement (4 Pages, 8 Blocks)
  10. Risk Management in Agricultural Enterprise (4 Pages, 8 Blocks)
  11. Labor Management and Regulations (4 Pages, 8 Blocks)
  12. Preparing a Business Proposal for an Enterprise (4 Pages, 9 Blocks)
  13. Presentation, Peer Evaluation & Topic Review (9 Pages, 18 Blocks)
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

def build_topic15_curriculum():
    """Returns the comprehensive pedagogical page and block structure for Grade 10 Topic 15: Establishing an Agricultural Enterprise."""
    return [
        # =====================================================================
        # LESSON 1: Meaning and Types of Agricultural Enterprises
        # =====================================================================
        {
            "unit_order": 1,
            "unit_name": "Meaning and Types of Agricultural Enterprises",
            "unit_description": "Agribusiness definitions; 4 ownership models (Sole proprietorship, Partnership, Cooperative, Private Limited Company); Limited vs Unlimited liability; legal continuity.",
            "lesson_title": "Agribusiness Foundations: Enterprise Types, Ownership Models, and Legal Liability",
            "pages": [
                [
                    {
                        "type": "suggested_image",
                        "title": "Commercial Agricultural Cooperative and Agribusiness Management Meeting",
                        "content": {
                            "title": "Commercial Agricultural Cooperative and Agribusiness Management Meeting",
                            "caption": "Farmers and agribusiness managers gathered at a cooperative center to discuss joint marketing, bulk input purchasing, and commercial enterprise growth."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Agribusiness Ownership",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Define an **agricultural enterprise** within a commercial agribusiness framework.",
                                "Analyze the 4 core ownership models: **Sole Proprietorship, Partnership, Agricultural Cooperative, and Private Limited Company (Ltd)**.",
                                "Contrast **Limited Liability** against **Unlimited Personal Liability**.",
                                "Evaluate legal continuity and decision-making structures across farm business models."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "What is an Agricultural Enterprise?",
                        "content": {
                            "title": "Farming as a Commercial Agribusiness",
                            "text": "An **agricultural enterprise** is any farm-based commercial venture that combines resources (**land, capital, labor, and management**) to produce agricultural commodities or services for sale at a profit:\n\n- **The Agribusiness Shift**: Moves farming away from subsistence (eating what is grown) to commercial agribusiness (tracking every cost, analyzing market demand, and optimizing returns).\n- **Profit Maximization**: Success is measured not just in harvested kilograms, but in net return on invested capital!"
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "Sole Proprietorships and Partnerships",
                        "content": {
                            "title": "Individual and Shared Ownership Structures",
                            "text": "1. **Sole Proprietorship**: Owned and managed by a single farmer.\n   - *Advantages*: Quick, autonomous decision-making; 100% of profits retained by the owner; low setup costs.\n   - *Disadvantages*: **Unlimited Liability** (personal property can be seized to pay farm debts); limited capital; lacks continuity upon owner's death.\n2. **Partnership**: Owned by 2 to 20 individuals bound by a Partnership Deed.\n   - *Advantages*: Pools diverse skills and larger capital; shared workload.\n   - *Disadvantages*: Shared profits; risk of partner disputes; joint and several **unlimited liability** unless registered as a limited liability partnership."
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "4 Primary Agribusiness Ownership Models in Kenya",
                        "content": {
                            "title": "4 Primary Agribusiness Ownership Models in Kenya",
                            "caption": "Four Ownership Models Matrix: Sole Proprietorship (1 Owner, Unlimited Liability) | Partnership (2-20 Partners, Shared Risk) | Cooperative (Member-Owned, Bulk Bargaining) | Private Limited Company (Shareholders, Limited Liability)."
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "Cooperatives and Private Limited Companies",
                        "content": {
                            "title": "Member-Owned Societies and Corporate Entities",
                            "text": "3. **Agricultural Cooperative**: A member-owned enterprise formed by farmers to pool produce, purchase bulk inputs at discount, and process commodities collectively (e.g., dairy or coffee cooperatives).\n   - *Advantages*: High market bargaining power; access to subsidized inputs; **limited liability** for members.\n   - *Disadvantages*: Slow democratic voting; risks of mismanagement.\n4. **Private Limited Company (Ltd)**: A separate legal entity owned by 1 to 50 shareholders.\n   - *Advantages*: **Limited Liability** (shareholders only risk their invested capital); perpetual succession; highly bankable.\n   - *Disadvantages*: Complex registration, strict tax compliance, high legal setup costs."
                        }
                    },
                    {
                        "type": "suggested_video",
                        "title": "Agribusiness Ownership Structures and Financing in Kenya",
                        "content": {
                            "title": "Agribusiness Ownership Structures and Financing in Kenya",
                            "description": "Educational video exploring how smallholder farmers organize into registered partnerships, cooperatives, and limited companies to secure commercial credit.",
                            "url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
                        }
                    }
                ],
                [
                    {
                        "type": "mini_activity",
                        "title": "Agribusiness Practical: Community Farm Ownership Survey",
                        "content": {
                            "title": "Farm Business Structure Survey Practicum",
                            "task": "1. Survey 3 local agricultural ventures (e.g., family dairy, school canteen supplier, local agro-dealer).\n2. Classify each venture under the 4 ownership models.\n3. Determine how each handles business debts and decision-making.",
                            "materials": ["Survey Notebook", "Pen"],
                            "safety": "Follow school guidelines when conducting community surveys."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Core Summary: Agribusiness Ownership",
                        "content": {
                            "title": "Key Takeaways",
                            "text": "- **Sole proprietorships offer quick decisions but carry unlimited liability**.\n- **Partnerships pool skills but share risks and profits**.\n- **Cooperatives provide collective bargaining power and bulk discounts**.\n- **Private limited companies provide limited liability and perpetual continuity**."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Selecting an Enterprise Structure",
                        "content": {
                            "question": "A group of young Grade 10 school leavers wants to establish a commercial poultry farm in Nakuru. They have substantial collective savings but wish to protect their personal assets from being seized if the business fails. Which ownership structure should they choose?",
                            "options": [
                                "Sole proprietorship",
                                "Unlimited partnership",
                                "Private limited company or registered limited liability partnership",
                                "Informal unregistered community self-help group"
                            ],
                            "answer": "C",
                            "explanation": "A private limited company or registered limited liability partnership provides 'limited liability'. This legally protects shareholders' personal assets from business creditors, unlike sole proprietorships or unlimited partnerships where liability is unlimited."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 2: Factors to Consider when Establishing an Enterprise
        # =====================================================================
        {
            "unit_order": 2,
            "unit_name": "Factors to Consider when Establishing an Enterprise",
            "unit_description": "Ecological & soil suitability; market demand & transport logistics; capital intensity; labor availability; technical skills.",
            "lesson_title": "Agribusiness Feasibility: Ecological Matching, Market Logistics, and Resource Allocation",
            "pages": [
                [
                    {
                        "type": "suggested_image",
                        "title": "Commercial Greenhouse Horticulture with Drip Irrigation Feasibility",
                        "content": {
                            "title": "Commercial Greenhouse Horticulture with Drip Irrigation Feasibility",
                            "caption": "A high-yielding commercial tomato greenhouse utilizing drip irrigation, showing infrastructure feasibility, water access, and market orientation."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Feasibility Factors",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Identify critical **feasibility variables before investing capital in an enterprise**.",
                                "Analyze **microclimatic, soil, and altitude parameters** governing crop and livestock fit.",
                                "Evaluate **market demand, consumer preferences, and transport logistics**.",
                                "Assess **capital intensity, labor availability, and specialized technical skills**."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Ecological and Climatic Suitability",
                        "content": {
                            "title": "Matching Enterprise to Biological Environment",
                            "text": "Before spending money on land preparation or seed, an entrepreneur must confirm biological compatibility:\n\n- **Soil Characteristics**: Soil depth, drainage, texture, and pH (e.g., tea requires acidic soils pH $4.5\\text{--}5.5$; cabbages require neutral soils pH $6.0\\text{--}6.8$).\n- **Rainfall & Temperature**: Annual rainfall volume, seasonal distribution, and ambient temperatures.\n- **Altitude**: Governs temperature and humidity regimes (e.g., pyrethrum and tea thrive in high altitudes $>2,000\\text{m}$; cotton and watermelons prefer warm, low altitudes)."
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "Market Demand and Transportation Logistics",
                        "content": {
                            "title": "Connecting the Farm to Paying Customers",
                            "text": "1. **Market Demand & Purchasing Power**: Confirm that a steady, high-volume consumer demand exists at a price that covers production costs and provides profit. Producing without a verified market results in financial disaster.\n2. **Transport Infrastructure & Perishability**:\n   - *Perishable Goods (Milk, Tomatoes, Eggs, Fresh Greens)*: Require proximity to urban markets and all-weather tarmac roads.\n   - *Non-Perishable Goods (Maize, Dry Beans, Macadamia)*: Tolerate longer transit times and rougher rural feeder roads without immediate spoilage."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Capital, Labor, and Specialized Skills",
                        "content": {
                            "title": "Assessing Farm Resources",
                            "text": "- **Capital Intensity**: Greenhouse floriculture requires millions of shillings in Capex, whereas indigenous poultry rearing can begin with modest capital.\n- **Labor Supply**: Labor-intensive crops (tea plucking, vegetable nurseries) require an abundant, reliable local labor force during peak seasons.\n- **Technical & Managerial Skills**: The farmer must possess or hire technical expertise (e.g., broiler vaccination schedules, artificial insemination, drip fertigation calibration)."
                        }
                    }
                ],
                [
                    {
                        "type": "comparison_table",
                        "title": "Agribusiness Enterprise Feasibility Assessment Matrix",
                        "content": {
                            "title": "Enterprise Feasibility Decision Matrix",
                            "headers": ["Feasibility Factor", "High-Feasibility Indicator", "High-Risk Red Flag", "Agronomic Mitigation"],
                            "rows": [
                                ["Ecological Fit", "Soil pH, rainfall & altitude match crop needs", "Saline water, shallow rocky soil, frost risk", "Soil amendment, irrigation, or switch crop"],
                                ["Market Access", "Pre-arranged buyer contracts / high local demand", "Flooded market gluts, zero local buyers", "Process into shelf-stable goods / contract farming"],
                                ["Transport Road", "All-weather tarmac within 30 min of farm", "Impassable muddy roads during rainy harvests", "Value addition (e.g., dry fruit chips / ghee)"],
                                ["Labor Availability", "Skilled seasonal workers readily available", "Severe labor scarcity during weeding/harvest", "Mechanization (tractor tillage, boom sprayers)"]
                            ]
                        }
                    }
                ],
                [
                    {
                        "type": "mini_activity",
                        "title": "Field Practical: School Land Enterprise Feasibility Scoring",
                        "content": {
                            "title": "Enterprise Feasibility Scoring Practicum",
                            "task": "1. Select a 1/4-acre plot within the school compound.\n2. Compare two competing enterprises: (a) Drip-irrigated tomato greenhouse vs. (b) Indigenous poultry unit.\n3. Score each from 1–5 on: Ecological Fit, Capital Demand, Labor Requirement, and Transport Access.\n4. Recommend the most viable enterprise based on total score.",
                            "materials": ["Scoring Rubric", "Notebook", "Measuring Tape"],
                            "safety": "Wear boots when surveying school farm plots."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Core Summary: Feasibility Factors",
                        "content": {
                            "title": "Key Takeaways",
                            "text": "- **Match crops and animals to local soil, rainfall, and altitude**.\n- **Perishable enterprises require reliable roads and nearby markets**.\n- **Ensure adequate start-up and operational capital** before launch.\n- **Secure skilled labor and management expertise** for complex systems."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Road Proximity for Perishable Crops",
                        "content": {
                            "question": "Why is it critical for a commercial cabbage farmer to evaluate the distance and road conditions to the nearest market town before planting?",
                            "options": [
                                "Cabbages are highly perishable and require fast transport to prevent post-harvest wilting, leaf rot, and market value collapse",
                                "Poor roads increase the cost of fertilizers used during top-dressing",
                                "Long distances decrease the weed population in the cabbage field",
                                "The CBC curriculum requires all vegetable farms to be situated next to national highways"
                            ],
                            "answer": "A",
                            "explanation": "Fresh vegetables like cabbages are living tissues containing over 90% water. Transport delays on rough roads cause crushing, wilting, and rotting, leading to severe post-harvest losses and price discounts at the market."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 3: Sourcing Agricultural Inputs
        # =====================================================================
        {
            "unit_order": 3,
            "unit_name": "Sourcing Agricultural Inputs",
            "unit_description": "Certified seeds, fertilizers, livestock feeds, agrochemicals; KEPHIS regulatory certification, tamper-proof scratch-off SMS codes; PCBP registration; counterfeit avoidance.",
            "lesson_title": "Agrochemicals & Inputs: Certified Sourcing, KEPHIS Quality Seals, and Anti-Counterfeit Verification",
            "pages": [
                [
                    {
                        "type": "suggested_image",
                        "title": "Display of Certified Seed Packets and Agricultural Input Supplies",
                        "content": {
                            "title": "Display of Certified Seed Packets and Agricultural Input Supplies",
                            "caption": "A certified agro-dealer store showing sealed seed packets, fertilizers, and crop protection chemicals with official regulatory labels."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Sourcing Agricultural Inputs",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Classify agricultural inputs into **seeds, fertilizers, feeds, and crop protection chemicals**.",
                                "Analyze the regulatory role of **KEPHIS and PCBP** in Kenya.",
                                "Execute **scratch-off mobile SMS seed verification protocols**.",
                                "Identify agronomic and financial hazards of counterfeit farm inputs."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Classification of Agricultural Inputs",
                        "content": {
                            "title": "The Raw Materials of Farm Production",
                            "text": "1. **Planting Materials**: Certified high-germination hybrid or open-pollinated seeds, certified potato seed tubers, and disease-free tissue culture plantlets.\n2. **Soil Nutrients**: Organic composts, basal planting fertilizers (DAP, NPK), and top-dressing nitrogen fertilizers (CAN, Urea).\n3. **Livestock Feeds & Vet Supplies**: High-protein feeds (chick mash, dairy meal, pig growers) and veterinary drugs (dewormers, vaccines, acaricides).\n4. **Crop Protection Agrochemicals**: Selective herbicides, fungicides, and systemic insecticides."
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "Regulatory Authorities: KEPHIS and PCBP",
                        "content": {
                            "title": "Protecting Farmers from Substandard Inputs",
                            "text": "- **KEPHIS (Kenya Plant Health Inspectorate Service)**: The government parastatal that inspects, certifies, and seals all commercial seeds and planting materials in Kenya. Certified seed packets feature a tamper-proof **scratch-off label with a unique PIN code**.\n- **PCBP (Pest Control Products Board)**: Regulates and registers all pesticides, ensuring they are safe for handlers, consumers, and the environment when used as directed."
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "KEPHIS Input Verification & Anti-Counterfeit Checklist",
                        "content": {
                            "title": "KEPHIS Input Verification & Anti-Counterfeit Checklist",
                            "caption": "4-Step Input Verification: 1 Licensed Agro-Dealer -> 2 Inspect KEPHIS Scratch-Off Seal -> 3 SMS Code to 1393 -> 4 Check PCBP Number & Expiry Date."
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "Hazards of Counterfeit Inputs and Verification Protocol",
                        "content": {
                            "title": "Avoiding Fake Agrochemicals and Seed",
                            "text": "Using counterfeit inputs (e.g., dyed food grain sold as certified hybrid seed, or chalk sold as fertilizer) causes total crop failure:\n- **Verification Protocol**:\n  1. Buy only from licensed, registered agro-dealers (never roadside hawkers).\n  2. Scratch the silver coating on the seed packet to reveal the hidden PIN.\n  3. Send the PIN via free SMS to **1393**; receive instant confirmation of seed variety, lot number, and germination validity.\n  4. Inspect manufacture and expiration dates on chemical bottles and feed sacks."
                        }
                    },
                    {
                        "type": "comparison_table",
                        "title": "Certified vs Counterfeit Inputs Comparison",
                        "content": {
                            "title": "Certified vs Fake Agricultural Inputs Matrix",
                            "headers": ["Input Type", "Certified Input Feature", "Counterfeit Threat / Red Flag", "Agronomic Consequence of Fake"],
                            "rows": [
                                ["Hybrid Maize Seed", "KEPHIS scratch-off seal, uniform seed size, 90%+ germination", "Loose unsealed bags, dyed grain, no scratch PIN", "Low germination (<30%), stunted plants, massive yield loss"],
                                ["DAP / CAN Fertilizer", "Uniform granules, official manufacturer seal & weight mark", "Clumping dust, sand adulteration, discolored granules", "Soil acidification, zero nutrient uptake, stunted crops"],
                                ["Crop Pesticides", "PCBP registration number, intact tamper-proof seal, clear label", "Faded photocopied label, broken cap seal, cheap discount", "Pest resistance, chemical crop scorching, toxic residue"]
                            ]
                        }
                    }
                ],
                [
                    {
                        "type": "mini_activity",
                        "title": "Classroom Practical: Seed Packet Inspection and SMS Verification Lab",
                        "content": {
                            "title": "KEPHIS Seed Authentication Practicum",
                            "task": "1. Examine sample seed packets brought to class.\n2. Inspect the KEPHIS seal, lot number, and expiration date.\n3. Demonstrate how to scratch the PIN and simulate SMS verification.\n4. Check feed sacks for KEBS certification marks.",
                            "materials": ["Sample Seed Packets", "Feed Bags", "Magnifying Glass"],
                            "safety": "Wash hands after handling pesticide containers."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Core Summary: Sourcing Inputs",
                        "content": {
                            "title": "Key Takeaways",
                            "text": "- **KEPHIS inspects and certifies all crop seeds** in Kenya.\n- **Verify seed authenticity via the scratch-off SMS code (1393)**.\n- **PCBP regulates and registers all safe pesticides**.\n- **Never buy loose, unsealed inputs from informal hawkers**."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Agronomic Risks of Uncertified Seed",
                        "content": {
                            "question": "A farmer in Eldoret buys cheap, unpackaged maize seeds from an unregistered open-market trader. What agronomic risk does this farmer primarily face?",
                            "options": [
                                "The seeds will automatically transform into weeds",
                                "High risk of poor germination, seed-borne diseases (like Maize Lethal Necrosis), and catastrophic yield loss",
                                "The soil pH will instantly drop to highly saline levels",
                                "The farmer will be banned from using organic compost forever"
                            ],
                            "answer": "B",
                            "explanation": "Uncertified, informal seeds bypassed by KEPHIS carry high disease loads (viruses, fungi), low germination rates, and poor vigor. Certified seeds undergo rigorous field inspection and laboratory germination testing to guarantee performance."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 4: Capital Requirements & Types of Capital
        # =====================================================================
        {
            "unit_order": 4,
            "unit_name": "Capital Requirements & Types of Capital",
            "unit_description": "Capital as a production factor; Fixed capital (Capex, buildings, machinery, long-term assets) vs Working capital (Opex, seeds, feed, fuel, seasonal labor).",
            "lesson_title": "Agribusiness Finance I: Capital Classification, Fixed Infrastructure, and Working Operational Assets",
            "pages": [
                [
                    {
                        "type": "suggested_image",
                        "title": "Tractor and Agricultural Machinery Operating on Farm Field",
                        "content": {
                            "title": "Tractor and Agricultural Machinery Operating on Farm Field",
                            "caption": "A heavy farm tractor towing field equipment, representing long-term fixed capital expenditure (Capex) in commercial agriculture."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Types of Capital",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Define **capital as a man-made factor of agricultural production**.",
                                "Differentiate between **Fixed Capital (Capex)** and **Working Capital (Opex)**.",
                                "Identify farm assets belonging to fixed vs. working capital categories.",
                                "Compute capital requirements for a prospective farm start-up."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "What is Agricultural Capital?",
                        "content": {
                            "title": "Man-Made Assets Fueling Farm Production",
                            "text": "In agricultural economics, **capital** includes all man-made physical and financial resources used in the production process to generate income, excluding raw land and natural resources:\n\n- **Not Just Cash**: Capital includes tractors, water dams, poultry sheds, dairy cows, seeds, and fertilizers.\n- **Function**: Capital empowers labor to work efficiently on land, multiplying farm productivity."
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "Fixed Capital (Capital Expenditure - Capex)",
                        "content": {
                            "title": "Long-Term Permanent Infrastructure",
                            "text": "**Fixed capital** consists of durable assets that last for multiple production cycles (usually more than one year) and do not change form during production:\n- *Key Traits*: High initial investment; depreciates gradually over time; provides long-term service.\n- *Examples*: Farm buildings, greenhouses, boreholes, drip irrigation piping, tractors, disc ploughs, and breeding livestock herds."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Working Capital (Operational Expenditure - Opex)",
                        "content": {
                            "title": "Short-Term Consumable Operating Assets",
                            "text": "**Working capital** (also called operational or circulating capital) consists of short-term assets and cash consumed or transformed within a single production cycle (usually less than a year):\n- *Key Traits*: Used for daily operations; directly converted into output; must be replenished each season.\n- *Examples*: Certified seeds, fertilizers, broiler feeds, diesel fuel, casual labor wages, pesticides, and packaging materials."
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Fixed Capital vs Working Capital in Agribusiness",
                        "content": {
                            "title": "Fixed Capital vs Working Capital in Agribusiness",
                            "caption": "Capital Classification: Fixed Capital (Tractor, Greenhouse, Borehole, Dairy Herd - Multi-Year Capex) vs Working Capital (Seeds, Fertilizer, Broiler Feeds, Fuel, Wages - Single-Cycle Opex)."
                        }
                    }
                ],
                [
                    {
                        "type": "comparison_table",
                        "title": "Fixed vs Working Capital Comparison Matrix",
                        "content": {
                            "title": "Capital Classification & Economic Characteristics",
                            "headers": ["Dimension", "Fixed Capital (Capex)", "Working Capital (Opex)", "Poultry Enterprise Example"],
                            "rows": [
                                ["Lifespan", "Multiple years (>1 year)", "Single cycle (<1 year)", "Poultry House (Fixed) vs Chick Feed (Working)"],
                                ["Consumption Rate", "Depreciates slowly over time", "100% Consumed in one batch", "Drinkers/Feeders (Fixed) vs Broiler Mash (Working)"],
                                ["Replenishment", "Long-term replacement cycle", "Replenished every batch/season", "Incubator (Fixed) vs Day-Old Chicks (Working)"],
                                ["Accounting Role", "Recorded on Balance Sheet", "Recorded on P&L Statement as Expense", "Concrete Store (Fixed) vs Disinfectant (Working)"]
                            ]
                        }
                    }
                ],
                [
                    {
                        "type": "mini_activity",
                        "title": "Finance Practical: Start-Up Farm Capital Classification Exercise",
                        "content": {
                            "title": "Farm Capital Audit Practicum",
                            "task": "Classify each item into Fixed Capital or Working Capital:\n1. 10 Bags of DAP fertilizer.\n2. Subsoiler plow.\n3. Solar water pumping system.\n4. Casual labor wages for weeding.\n5. Dairy milking parlor.\n6. 50kg Dairy meal concentrate.",
                            "materials": ["Notebook", "Pen"],
                            "safety": "Ensure accurate economic reasoning."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Core Summary: Types of Capital",
                        "content": {
                            "title": "Key Takeaways",
                            "text": "- **Capital includes all man-made assets used to generate farm income**.\n- **Fixed capital represents multi-year permanent assets (tractors, sheds)**.\n- **Working capital represents single-cycle consumable items (seeds, feeds)**.\n- **A viable farm requires a healthy balance of Capex and Opex**."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Classifying Broiler Feed",
                        "content": {
                            "question": "Why is animal feed for commercial broilers classified as 'Working Capital' rather than 'Fixed Capital' in farm accounting?",
                            "options": [
                                "Feed lasts for more than five years in farm storage",
                                "Feed is a permanent asset that depreciates slowly over multiple poultry cycles",
                                "Feed is completely consumed and converted into bird muscle tissue within a single short production cycle, requiring continuous seasonal replenishment",
                                "Feed is supplied for free by the county government under agricultural policies"
                            ],
                            "answer": "C",
                            "explanation": "Working capital consists of consumable inputs converted into marketable commodities within a single production cycle. Broiler feed is eaten, transformed into meat, and must be re-purchased for the next batch, making it an operational working capital expense."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 5: Sourcing Financial Capital
        # =====================================================================
        {
            "unit_order": 5,
            "unit_name": "Sourcing Financial Capital",
            "unit_description": "Internal capital (personal savings, retained profits); formal banking vs Agricultural Finance Corporation (AFC); microfinance; informal Chamas & agricultural SACCOs.",
            "lesson_title": "Agribusiness Finance II: Capital Sourcing, AFC Credit Facilities, SACCOs, and Risk Management",
            "pages": [
                [
                    {
                        "type": "suggested_image",
                        "title": "Kenyan Banknotes and Financial Currency for Farm Capitalization",
                        "content": {
                            "title": "Kenyan Banknotes and Financial Currency for Farm Capitalization",
                            "caption": "Kenyan currency banknotes, representing financial liquidity, farm credit mobilization, and agricultural capital funding."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Sourcing Financial Capital",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Differentiate between **internal capital (savings, retained earnings)** and **external capital (loans, grants)**.",
                                "Analyze the agricultural lending mandate of the **Agricultural Finance Corporation (AFC)**.",
                                "Compare commercial bank credit against **SACCOs and informal Chamas**.",
                                "Assess interest rate risks, collateral demands, and debt repayment schedules."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Internal vs External Capital Sources",
                        "content": {
                            "title": "Mobilizing Financial Resources",
                            "text": "1. **Internal Sources (Equity)**:\n   - *Personal Savings*: Safest capital source; carries zero interest and zero foreclosure risk.\n   - *Retained Farm Earnings*: Reinvesting profits from previous seasons back into expanding farm operations.\n2. **External Sources (Debt & Grants)**:\n   - *Agribusiness Grants*: Non-repayable funding from development agencies or government youth funds.\n   - *Borrowed Capital (Credit)*: Debt financing from financial institutions requiring repayment with interest."
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "Formal Lenders: Commercial Banks vs. AFC",
                        "content": {
                            "title": "Institutional Credit Channels in Kenya",
                            "text": "- **Commercial Banks**: Offer large credit lines but require substantial **hard collateral** (land title deeds), charge high commercial interest rates ($14\\text{--}18\\%+$), and enforce rigid monthly repayment schedules regardless of harvest timing.\n- **Agricultural Finance Corporation (AFC)**: A dedicated government development finance institution providing affordable, long-term credit to Kenyan farmers. AFC offers lower interest rates and tailors repayment schedules to match seasonal crop harvest cycles!"
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Agricultural Financial Capital Sources Landscape in Kenya",
                        "content": {
                            "title": "Agricultural Financial Capital Sources Landscape in Kenya",
                            "caption": "Capital Ecosystem: Internal (Personal Savings, Retained Farm Profits) vs External Formal (AFC Seasonal Loans, Commercial Banks, MFIs) vs External Cooperative (Agricultural SACCOs, Chamas)."
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "Cooperative and Community Finance: SACCOs and Chamas",
                        "content": {
                            "title": "Member-Driven Rural Financing",
                            "text": "- **Agricultural SACCOs (Savings and Credit Cooperatives)**: Member-owned societies where farmers save regularly and borrow up to $3\\times$ their savings at regulated, competitive interest rates ($1\\%\\text{ per month}$). Loan repayments are often deducted directly from cooperative crop payouts (e.g., tea or milk checks).\n- **Chamas (Merry-Go-Rounds / Table Banking)**: Informal self-help groups pooling weekly savings to provide rotating credit or low-interest emergency loans to members without formal collateral requirements."
                        }
                    },
                    {
                        "type": "comparison_table",
                        "title": "Financial Capital Sources Comparison Matrix",
                        "content": {
                            "title": "Agribusiness Credit Channels Comparison",
                            "headers": ["Funding Source", "Collateral Requirement", "Interest Rate Level", "Repayment Flexibility", "Target Farm Level"],
                            "rows": [
                                ["Personal Savings", "None (Zero debt)", "0% (Zero interest)", "Complete flexibility", "Smallholders & start-ups"],
                                ["Agricultural SACCO", "Member shares & guarantors", "Moderate (10–12% p.a.)", "Deducted from crop harvest checks", "Small to medium cooperative members"],
                                ["AFC (Agric Finance Corp)", "Land title / farm assets", "Subsidized (8–10% p.a.)", "Grace periods aligned with harvest", "Commercial crop & livestock farmers"],
                                ["Commercial Banks", "Strict title deeds / fixed assets", "High commercial rates (14–18%+)", "Rigid monthly repayment schedules", "Large-scale agribusiness corporations"],
                                ["Informal Chamas", "Social trust & peer guarantee", "Low to zero interest", "Flexible weekly/monthly meetings", "Youth & women micro-enterprises"]
                            ]
                        }
                    }
                ],
                [
                    {
                        "type": "mini_activity",
                        "title": "Agribusiness Case Study: Selecting the Optimal Loan Facility",
                        "content": {
                            "title": "Credit Channel Decision Practicum",
                            "task": "Scenario: Wanjiku has KES 50,000 savings and needs KES 150,000 to purchase a dairy cow that will produce milk in 4 months.\n1. Compare Option A (Commercial Bank @ 16% requiring monthly payments immediately) vs. Option B (Dairy SACCO @ 11% with 4-month grace period).\n2. Recommend the safer financial facility and justify your choice.",
                            "materials": ["Case Handout", "Calculator", "Pen"],
                            "safety": "Ensure sound debt management logic."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Core Summary: Sourcing Capital",
                        "content": {
                            "title": "Key Takeaways",
                            "text": "- **Personal savings carry zero interest and zero foreclosure risk**.\n- **AFC provides specialized agricultural loans tailored to harvest seasons**.\n- **SACCOs offer competitive credit linked to cooperative crop checks**.\n- **Avoid high-interest commercial bank loans with rigid monthly schedules** for seasonal crops."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Advantage of SACCO Financing",
                        "content": {
                            "question": "Why is borrowing from an agricultural SACCO often far more advantageous for a smallholder dairy farmer than taking a commercial bank loan?",
                            "options": [
                                "SACCOs do not require members to repay loans",
                                "SACCOs offer lower regulated interest rates and align repayment deductions with monthly dairy cooperative milk payouts, reducing cash flow distress",
                                "SACCOs are owned by foreign donors who pay off all member debts",
                                "Commercial banks do not allow farmers to purchase dairy animals"
                            ],
                            "answer": "B",
                            "explanation": "Agricultural SACCOs are member-owned and understand farming cash flow rhythms. They charge competitive interest rates and structure loan repayments to be deducted directly from milk or crop payout checks, preventing loan defaults during the waiting period before production."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 6: Cost of Production
        # =====================================================================
        {
            "unit_order": 6,
            "unit_name": "Cost of Production",
            "unit_description": "Total Cost = Total Fixed Costs + Total Variable Costs; Unit Cost of Production formula (Unit Cost = TC / Yield); break-even price analysis.",
            "lesson_title": "Agribusiness Economics: Cost of Production, Fixed vs Variable Expenses, and Break-Even Math",
            "pages": [
                [
                    {
                        "type": "suggested_image",
                        "title": "Bags of Harvested Grains at Market Ready for Output Cost Analysis",
                        "content": {
                            "title": "Bags of Harvested Grains at Market Ready for Output Cost Analysis",
                            "caption": "Sacks of harvested grain produce stacked for sale, illustrating total physical yield and the basis for calculating unit cost of production."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Cost of Production",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Define **cost of production** in commercial farming.",
                                "Differentiate between **Total Fixed Costs (TFC)** and **Total Variable Costs (TVC)**.",
                                "Compute **Total Cost (TC = TFC + TVC)** and **Unit Cost of Production**.",
                                "Determine the **break-even selling price** to avoid agribusiness losses."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Defining Cost of Production",
                        "content": {
                            "title": "Tracking Every Farm Shilling",
                            "text": "The **cost of production** is the total financial expenditure incurred to produce a specific volume of agricultural output:\n\n- **Why It Matters**: Tracking production costs is the single most vital step in determining farm profitability. A farmer who does not know their cost per kilogram may sell below cost, suffering silent, accumulating losses.\n- **The Golden Rule**: Selling Price must exceed Unit Cost of Production to generate net profit!"
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "Fixed Costs vs Variable Costs",
                        "content": {
                            "title": "Understanding Farm Expense Structures",
                            "text": "1. **Fixed Costs (Overhead / TFC)**: Expenses that remain constant regardless of the volume of output produced. They must be paid even if yield is zero.\n   - *Examples*: Land rent, permanent farm security salary, tool depreciation, insurance.\n2. **Variable Costs (Operating / TVC)**: Expenses that change in direct proportion to production volume.\n   - *Examples*: Seeds, fertilizers, tractor fuel, casual weeding labor, harvest packaging bags."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Unit Cost Formula and Break-Even Analysis",
                        "content": {
                            "title": "The Mathematical Formulas of Agribusiness",
                            "text": "$$\\text{Total Cost (TC)} = \\text{Total Fixed Costs (TFC)} + \\text{Total Variable Costs (TVC)}$$\n\n$$\\text{Unit Cost of Production} = \\frac{\\text{Total Cost (TC)}}{\\text{Total Output Quantity (Yield)}}$$\n\n- **Worked Example**: A farmer spends KES 20,000 on fixed costs (rent/depreciation) and KES 30,000 on variable costs (seeds/fertilizer) to harvest 50 bags of maize:\n$$\\text{Total Cost} = 20,000 + 30,000 = \\text{KES }50,000$$\n$$\\text{Unit Cost per bag} = \\frac{50,000}{50\\text{ bags}} = \\text{KES }1,000\\text{ per bag}$$\n- *Break-Even*: Selling at KES 1,000 yields zero profit/loss. Selling at KES 2,500 yields KES 1,500 profit per bag!"
                        }
                    }
                ],
                [
                    {
                        "type": "comparison_table",
                        "title": "1-Acre Maize Enterprise Cost Breakdown Table",
                        "content": {
                            "title": "1-Acre Maize Production Cost Model",
                            "headers": ["Expense Category", "Cost Component", "Amount (KES)", "Classification"],
                            "rows": [
                                ["Land Overhead", "1 Acre Land Rent (Annual)", "10,000", "Fixed Cost (TFC)"],
                                ["Equipment Overhead", "Tractor & Store Depreciation", "5,000", "Fixed Cost (TFC)"],
                                ["Planting Inputs", "Certified Hybrid Seed (10kg)", "5,000", "Variable Cost (TVC)"],
                                ["Fertilizers", "2 Bags DAP + 2 Bags CAN", "18,000", "Variable Cost (TVC)"],
                                ["Field Operations", "Ploughing, Weeding & Harvesting Labor", "12,000", "Variable Cost (TVC)"],
                                ["Packaging", "30 Gunny Bags & Twine", "3,000", "Variable Cost (TVC)"],
                                ["TOTAL COST (TC)", "TFC (15,000) + TVC (38,000)", "KES 53,000", "Total Farm Outlay"],
                                ["UNIT COST (30 Bags)", "KES 53,000 / 30 Bags Yield", "KES 1,767 / Bag", "Break-Even Price"]
                            ]
                        }
                    }
                ],
                [
                    {
                        "type": "mini_activity",
                        "title": "Math Practical: Broiler Poultry Unit Cost Calculation",
                        "content": {
                            "title": "Poultry Break-Even Math Practicum",
                            "task": "A youth group rears 100 broilers:\n- Fixed Cost (Cage depreciation): KES 4,000\n- Variable Costs (Chicks KES 10,000 + Feeds KES 18,000 + Vaccines KES 3,000): KES 31,000\n1. Calculate Total Cost (TC).\n2. Calculate Unit Cost per broiler.\n3. If birds sell at KES 450 each, calculate Total Revenue and Net Profit.",
                            "materials": ["Calculator", "Notebook", "Pen"],
                            "safety": "Ensure rigorous mathematical accuracy."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Core Summary: Cost of Production",
                        "content": {
                            "title": "Key Takeaways",
                            "text": "- **Total Cost = Total Fixed Costs + Total Variable Costs**.\n- **Unit Cost = Total Cost divided by Total Yield**.\n- **Selling above unit cost guarantees profit; selling below causes loss**.\n- **Minimizing variable costs lowers the break-even selling price**."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Break-Even Selling Price Math",
                        "content": {
                            "question": "A potato farmer incurs a total fixed cost of KES 10,000 and a total variable cost of KES 30,000. The farm harvests 200 bags of potatoes. What is the minimum price per bag the farmer must sell at to break even?",
                            "options": [
                                "KES 50",
                                "KES 150",
                                "KES 200",
                                "KES 400"
                            ],
                            "answer": "C",
                            "explanation": "Total Cost = Fixed Cost + Variable Cost = KES 10,000 + KES 30,000 = KES 40,000. Unit Cost per bag = Total Cost / Total Output = KES 40,000 / 200 bags = KES 200. To break even (zero profit/loss), the farmer must sell at exactly KES 200 per bag."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 7: Formulating a Simple Farm Budget
        # =====================================================================
        {
            "unit_order": 7,
            "unit_name": "Formulating a Simple Farm Budget",
            "unit_description": "Complete vs Partial vs Enterprise Budgets; Revenue projections; Gross Margin (Gross Margin = Revenue - TVC); Projected Net Profit.",
            "lesson_title": "Farm Financial Planning: Enterprise Budgets, Gross Margin Analysis, and Profit Projections",
            "pages": [
                [
                    {
                        "type": "suggested_image",
                        "title": "Farm Manager Formulating Financial Enterprise Budgets on Clipboard",
                        "content": {
                            "title": "Farm Manager Formulating Financial Enterprise Budgets on Clipboard",
                            "caption": "A farm entrepreneur drafting projected revenues, input costs, and gross margins on a farm planning worksheet before planting season."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Farm Budgeting",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Define a **farm budget as a forward-looking financial roadmap**.",
                                "Distinguish among **Complete, Partial, and Enterprise Budgets**.",
                                "Calculate **Gross Revenue, Total Variable Costs, and Gross Margin**.",
                                "Formulate a balanced crop enterprise budget displaying **Projected Net Profit**."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "What is a Farm Budget?",
                        "content": {
                            "title": "The Financial Blueprint Before Planting",
                            "text": "A **farm budget** is a forward-looking financial plan that estimates future revenues and expenditures for a farming enterprise over a specific future period:\n\n- **Management Role**: Helps the farmer evaluate which enterprise will be most profitable, forecast seasonal cash flow shortages, and determine loan requirements.\n- **Timing**: Always prepared *before* production begins, acting as an operational map."
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "Types of Farm Budgets",
                        "content": {
                            "title": "Complete, Partial, and Enterprise Budgets",
                            "text": "1. **Complete Budget**: Estimates revenues and expenses for the entire multi-enterprise farm business (e.g., dairy + maize + horticulture + poultry combined).\n2. **Partial Budget**: Evaluates minor adjustments to an existing farm plan (e.g., deciding whether to replace 1 acre of maize with 1 acre of French beans by comparing added costs, saved costs, lost income, and added income).\n3. **Enterprise Budget**: A detailed forecast of costs and returns for a *single* agricultural commodity (e.g., a 1-acre cabbage budget)."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Structure of an Enterprise Budget and Gross Margin",
                        "content": {
                            "title": "Revenues, Variable Costs, and Net Returns",
                            "text": "A standard enterprise budget follows a clear 3-section flow:\n1. **Gross Revenue (Gross Income)**: Estimated Yield $\\times$ Expected Market Price.\n2. **Total Variable Costs (TVC)**: All operating expenses (seeds, fertilizer, chemicals, casual labor).\n3. **Gross Margin & Net Profit**:\n$$\\text{Gross Margin} = \\text{Gross Revenue} - \\text{Total Variable Costs}$$\n$$\\text{Projected Net Profit} = \\text{Gross Margin} - \\text{Allocated Fixed Costs}$$"
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Enterprise Budget Waterfall: Revenue to Net Profit",
                        "content": {
                            "title": "Enterprise Budget Waterfall: Revenue to Net Profit",
                            "caption": "Budget Waterfall Flow: Gross Revenue (Yield x Price) -> Minus Variable Costs (Seeds, Fertilizer, Chemicals, Labor) -> Equals Gross Margin -> Minus Fixed Costs (Rent, Depreciation) -> Equals Net Profit."
                        }
                    }
                ],
                [
                    {
                        "type": "comparison_table",
                        "title": "Sample 1-Acre Cabbage Enterprise Budget",
                        "content": {
                            "title": "1-Acre Cabbage Enterprise Budget Model",
                            "headers": ["Budget Item", "Quantity / Calculation", "Unit Rate (KES)", "Total Amount (KES)"],
                            "rows": [
                                ["GROSS REVENUE", "8,000 heads harvested", "KES 25 / head", "KES 200,000"],
                                ["Seedlings", "8,500 seedlings", "KES 1 / seedling", "- 8,500"],
                                ["Basal Fertilizer", "2 Bags DAP (50kg)", "KES 6,000 / bag", "- 12,000"],
                                ["Top-Dressing Fertilizer", "2 Bags CAN (50kg)", "KES 5,000 / bag", "- 10,000"],
                                ["Agrochemicals & Spraying", "Fungicides & Insecticides", "Lump sum", "- 6,000"],
                                ["Labor (Weed & Harvest)", "20 Man-days", "KES 700 / day", "- 14,000"],
                                ["TOTAL VARIABLE COSTS", "Sum of operational costs", "-", "- 50,500"],
                                ["GROSS MARGIN", "Gross Revenue (200,000) - TVC (50,500)", "-", "+ KES 149,500"],
                                ["Allocated Fixed Costs", "Land Rent + Tool Depreciation", "-", "- 15,000"],
                                ["PROJECTED NET PROFIT", "Gross Margin (149,500) - TFC (15,000)", "-", "+ KES 134,500"]
                            ]
                        }
                    }
                ],
                [
                    {
                        "type": "mini_activity",
                        "title": "Budgeting Practical: Drafting a 1/2-Acre Tomato Enterprise Budget",
                        "content": {
                            "title": "Tomato Budget Formulation Practicum",
                            "task": "1. Estimate: 5,000 kg tomato yield sold at KES 40/kg.\n2. Estimate variable costs (Seedlings KES 10,000, Fertilizer KES 25,000, Chemicals KES 15,000, Labor KES 20,000).\n3. Estimate fixed costs (Land rent KES 10,000).\n4. Calculate Gross Revenue, Total Variable Costs, Gross Margin, and Projected Net Profit.",
                            "materials": ["Budget Worksheet", "Calculator", "Pen"],
                            "safety": "Ensure realistic farm price assumptions."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Core Summary: Farm Budgeting",
                        "content": {
                            "title": "Key Takeaways",
                            "text": "- **Budgets are forward-looking financial roadmaps**.\n- **Enterprise budgets project single-crop profitability**.\n- **Gross Margin = Gross Revenue minus Total Variable Costs**.\n- **Net Profit = Gross Margin minus Allocated Fixed Costs**."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Calculating Gross Margin",
                        "content": {
                            "question": "In farm budgeting and financial analysis, how is the 'Gross Margin' of an agricultural enterprise calculated?",
                            "options": [
                                "Total Revenue plus Total Fixed Costs",
                                "Total Revenue (Gross Income) minus Total Variable Costs",
                                "Total Variable Costs divided by Total Fixed Costs",
                                "Expected Yield multiplied by the local county tax rate"
                            ],
                            "answer": "B",
                            "explanation": "Gross Margin is a vital economic efficiency metric calculated as: Gross Revenue (Total Sales) minus Total Variable (Operating) Costs. It shows how much surplus the enterprise generates to cover fixed overhead costs and net profit."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 8: Basic Farm Record Keeping
        # =====================================================================
        {
            "unit_order": 8,
            "unit_name": "Basic Farm Record Keeping",
            "unit_description": "Rationale for records; 4 record categories (production, inventory, labor, financial); Daily Cash Book ledger design and transaction balancing.",
            "lesson_title": "Agribusiness Administration: Record Keeping Types, Daily Cash Books, and Financial Transparency",
            "pages": [
                [
                    {
                        "type": "suggested_image",
                        "title": "Daily Farm Record Keeping Ledger with Pens and Office Tools",
                        "content": {
                            "title": "Daily Farm Record Keeping Ledger with Pens and Office Tools",
                            "caption": "An open farm accounting notebook and ledger with writing utensils, showing systematic tracking of daily transactions, yields, and inputs."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Farm Record Keeping",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "State the agricultural and commercial reasons for maintaining accurate farm records.",
                                "Classify farm records into **Production, Inventory, Labor, and Financial** records.",
                                "Design a functional **Daily Farm Cash Book template**.",
                                "Balance daily cash-in (income) and cash-out (expense) transactions."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Why Keep Farm Records?",
                        "content": {
                            "title": "Eliminating Guesswork from Farm Management",
                            "text": "Many smallholder farmers fail because they manage operations solely based on memory. **Farm records** are written documents capturing all physical events, inputs, yields, and financial transactions:\n\n- **Measure Real Profit or Loss**: Proves whether the farm is genuinely generating income or draining savings.\n- **Access Bank & SACCO Credit**: Lenders require 1–3 years of verifiable farm records before approving agricultural loans.\n- **Agronomic Diagnosis**: Helps identify disease trends, yield drops, and fertilizer efficiency.\n- **Tax Compliance & Asset Protection**: Facilitates tax filing and insurance claims."
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "The 4 Core Categories of Farm Records",
                        "content": {
                            "title": "Comprehensive Farm Record Classification",
                            "text": "1. **Production Records**: Track physical yields, livestock birth dates, egg collection logs, milk volumes per cow, and crop harvest weights.\n2. **Inventory Records**: A complete itemized registry of all physical assets owned by the farm at any date (machinery, tools, stored bags of seed/fertilizer, livestock head counts).\n3. **Labor Records**: Track hours worked, tasks completed by casual or permanent staff, and wages paid.\n4. **Financial Records**: Chronologically log every shilling entering or leaving the farm cashbox or bank account."
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Daily Farm Cash Book Ledger Architecture",
                        "content": {
                            "title": "Daily Farm Cash Book Ledger Architecture",
                            "caption": "Cash Book Ledger Columns: Date | Transaction Description | Ref / Receipt # | Cash In (Income +) | Cash Out (Expense -) | Running Cash Balance."
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "Designing and Balancing a Daily Cash Book",
                        "content": {
                            "title": "The Daily Financial Ledger Template",
                            "text": "A standard **Daily Cash Book** records transactions chronologically, ensuring running cash balances are always reconciled:\n\n| Date | Transaction Description | Ref / Receipt # | Cash In (Income - KES) | Cash Out (Expense - KES) | Balance (KES) |\n| :--- | :--- | :--- | :--- | :--- | :--- |\n| 01/10 | Opening Cash Balance | - | - | - | 10,000 |\n| 03/10 | Bought 2 Bags CAN Fertilizer | Rec #104 | - | 10,000 | 0 |\n| 05/10 | Sold 20 Trays of Eggs | Inv #45 | 8,000 | - | 8,000 |\n| 08/10 | Paid Casual Weeding Wages | Vouch #12 | - | 2,400 | 5,600 |\n\n- *Balancing Rule*: Running Balance = Previous Balance + Cash In - Cash Out."
                        }
                    },
                    {
                        "type": "comparison_table",
                        "title": "Types of Farm Records Comparison Matrix",
                        "content": {
                            "title": "Farm Record Types & Strategic Applications",
                            "headers": ["Record Category", "Key Data Captured", "Primary Management Function", "Real-World Farm Example"],
                            "rows": [
                                ["Production Record", "Daily milk yields, egg counts, harvest bags", "Evaluates biological yield performance", "Cow #4 Milk Yield Sheet (15 L/day)"],
                                ["Inventory Record", "Tools, machinery, stored inputs, livestock count", "Prevents theft and tracks farm asset value", "Farm Store Register (10 Jembes, 4 Sprayers)"],
                                ["Labor Record", "Worker names, hours worked, tasks, wages paid", "Measures worker productivity & payroll", "Weeding Gang Muster Roll (5 Casuals)"],
                                ["Financial Record", "Cash in, cash out, invoices, receipts, bank state", "Determines enterprise profit and cash flow", "Daily Cash Book & Farm Bank Ledger"]
                            ]
                        }
                    }
                ],
                [
                    {
                        "type": "mini_activity",
                        "title": "Accounting Practical: Building and Balancing a Farm Cash Book",
                        "content": {
                            "title": "Cash Book Balancing Practicum",
                            "task": "Enter and balance these transactions for 'Bitega Farm':\n1. Opening Balance: KES 15,000.\n2. Oct 2: Sold 50kg kales for KES 2,500.\n3. Oct 4: Bought 1 bottle insecticide for KES 1,200.\n4. Oct 7: Paid farm guard KES 4,000.\n5. Oct 9: Sold 100 liters milk for KES 5,000.\n6. Calculate the final closing cash balance.",
                            "materials": ["Ruler", "Ledger Sheet", "Pen", "Calculator"],
                            "safety": "Ensure neat column alignment and exact mathematical balance."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Core Summary: Farm Record Keeping",
                        "content": {
                            "title": "Key Takeaways",
                            "text": "- **Never run a farm on memory; keep written records**.\n- **Maintain 4 record streams: Production, Inventory, Labor, Financial**.\n- **A Daily Cash Book reconciles income, expenses, and cash balances**.\n- **Verifiable farm records are mandatory for securing bank loans**."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Purpose of Breeding Records",
                        "content": {
                            "question": "Which specific record log should a dairy farm manager consult to determine when a pedigree heifer is due for artificial insemination (AI) services?",
                            "options": [
                                "The farm tool inventory log",
                                "The daily financial cash book",
                                "The animal breeding and reproduction record sheet",
                                "The county chemical agro-dealer register"
                            ],
                            "answer": "C",
                            "explanation": "Breeding and reproduction records log estrus (heat) cycles, past insemination dates, sire semen batch numbers, and expected calving dates, providing the essential biological data needed to schedule AI services."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 9: Preparing a Simple Profit & Loss Statement
        # =====================================================================
        {
            "unit_order": 9,
            "unit_name": "Preparing a Simple Profit & Loss Statement",
            "unit_description": "Historical financial accounting vs forward budgets; Revenues, Operating Costs, Net Profit (Revenue - Expenses), Net Loss.",
            "lesson_title": "Agribusiness Accounting: Constructing Profit and Loss Statements and Financial Viability Audits",
            "pages": [
                [
                    {
                        "type": "suggested_image",
                        "title": "Financial Calculation, Numerical Accounting, and Farm Viability Analysis",
                        "content": {
                            "title": "Financial Calculation, Numerical Accounting, and Farm Viability Analysis",
                            "caption": "A financial balance calculation on accounting paper with numerical figures, illustrating final Profit and Loss statement reconciliation."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Profit & Loss Statement",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Define a **Profit and Loss (P&L) Statement (Income Statement)**.",
                                "Contrast **forward-looking budgets against historical P&L statements**.",
                                "Calculate **Total Revenue, Operating Expenses, and Net Profit (or Net Loss)**.",
                                "Construct a standard P&L statement from raw farm transaction receipts."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "What is a Profit & Loss Statement?",
                        "content": {
                            "title": "The Ultimate Financial Scorecard",
                            "text": "A **Profit and Loss (P&L) Statement** (also known as an Income Statement) is a formal financial summary of revenues, costs, and expenses incurred by a farm enterprise during a specific accounting period (e.g., a month, quarter, or year):\n\n- **Budget vs. P&L**: While a budget is an *estimate of the future*, a P&L statement is a *record of the actual past*.\n- **The Ultimate Test**: It answers the foundational agribusiness question: *'Did this farming enterprise generate real net profit or incur a loss?'*"
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "Core Components of a P&L Statement",
                        "content": {
                            "title": "Revenues, Expenses, and Bottom-Line Net Profit",
                            "text": "1. **Gross Revenue (Total Sales)**: All cash and credit sales generated by selling farm commodities during the period.\n2. **Operating Expenses (Cost of Production)**: All variable input costs (seeds, feeds, fuel, casual wages) plus fixed overheads (rent, depreciation, maintenance).\n3. **Net Profit or Loss**:\n$$\\text{Net Profit (or Loss)} = \\text{Total Revenue} - \\text{Total Expenses}$$\n- If Revenues $>$ Expenses $\\rightarrow$ **Net Profit** (Viable, healthy business).\n- If Expenses $>$ Revenues $\\rightarrow$ **Net Loss** (Unviable; drains capital)."
                        }
                    },
                    {
                        "type": "comparison_table",
                        "title": "Constructing a Standard P&L Statement (Rabbitry Enterprise)",
                        "content": {
                            "title": "Rabbit Enterprise Annual Profit & Loss Statement",
                            "headers": ["Financial Component", "Itemized Details", "Amount (KES)", "Net Impact"],
                            "rows": [
                                ["REVENUES", "Sales of 90 Mature Meat Rabbits", "45,000", "+ KES 45,000"],
                                ["Operating Expense 1", "Purchased Breeding Stock", "8,000", "- 8,000"],
                                ["Operating Expense 2", "Rabbit Commercial Pellets & Hay", "12,000", "- 12,000"],
                                ["Operating Expense 3", "Veterinary Drugs & Dewormers", "2,500", "- 2,500"],
                                ["Operating Expense 4", "Hutch Disinfection & Repairs", "1,500", "- 1,500"],
                                ["TOTAL EXPENSES", "Sum of all operational outlays", "24,000", "- KES 24,000"],
                                ["NET PROFIT", "Total Revenue (45,000) - Total Expenses (24,000)", "KES 21,000", "PROFITABLE (+87.5% ROI!)"]
                            ]
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "Auditing Farm Financial Health from P&L",
                        "content": {
                            "title": "Diagnosing Enterprise Strengths and Weaknesses",
                            "text": "A P&L statement enables farm managers to spot financial leaks:\n- **High Feed Ratio**: If feed expenses consume $>70\\%$ of total livestock revenues, the farmer must explore on-farm feed mixing or fodder conservation.\n- **Uncontrolled Labor Costs**: If casual labor exceeds gross margins, mechanization or piece-rate pay is required.\n- **Pricing Power**: Proves whether farm-gate selling prices adequately cover escalating fertilizer and fuel costs."
                        }
                    }
                ],
                [
                    {
                        "type": "mini_activity",
                        "title": "Financial Practical: Constructing 'Moraa's Garlic Farm' P&L Statement",
                        "content": {
                            "title": "P&L Statement Construction Practicum",
                            "task": "Construct a P&L Statement from Moraa's actual season figures:\n- Garlic Sales Revenue: KES 90,000\n- Garlic Seed Cloves: KES 15,000 | Tillage: KES 8,000 | Fertilizer: KES 12,000 | Weeding Labor: KES 10,000 | Sacks: KES 3,000 | Land Rent: KES 10,000\n1. Calculate Total Expenses.\n2. Compute Net Profit/Loss and state if the enterprise is viable.",
                            "materials": ["Accounting Sheet", "Calculator", "Pen"],
                            "safety": "Ensure all expense entries are correctly subtracted."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Core Summary: Profit & Loss Statement",
                        "content": {
                            "title": "Key Takeaways",
                            "text": "- **A P&L statement records actual past financial performance**.\n- **Net Profit = Total Revenue minus Total Expenses**.\n- **Negative result indicates a Net Loss**, requiring cost-cutting or price increases.\n- **P&L audits highlight operational inefficiencies** in feeds, labor, and inputs."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Evaluating Financial Outcome",
                        "content": {
                            "question": "If a school agricultural project records total produce sales revenues of KES 12,000 but incurs total operating and fixed expenses of KES 14,500, what is the exact financial outcome of this enterprise?",
                            "options": [
                                "A Net Profit of KES 2,500",
                                "A Net Loss of KES 2,500",
                                "A balanced budget with zero net return",
                                "A government agricultural tax rebate of KES 14,500"
                            ],
                            "answer": "B",
                            "explanation": "Net Profit/Loss is calculated by subtracting total expenses from total revenues (12,000 - 14,500 = -2,500). Because the result is negative (expenses exceed revenues), the enterprise has registered a Net Loss of KES 2,500."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 10: Risk Management in Agricultural Enterprise
        # =====================================================================
        {
            "unit_order": 10,
            "unit_name": "Risk Management in Agricultural Enterprise",
            "unit_description": "Production, market, financial, and institutional risks; mitigation via crop diversification, irrigation, greenhouses, forward supply contracts, index-based satellite crop insurance.",
            "lesson_title": "Agribusiness Risk Management: Risk Typologies, Mitigation Strategies, and Index-Based Insurance",
            "pages": [
                [
                    {
                        "type": "suggested_image",
                        "title": "Agricultural Drip Irrigation System Managing Drought and Climate Risks",
                        "content": {
                            "title": "Agricultural Drip Irrigation System Managing Drought and Climate Risks",
                            "caption": "Precision drip irrigation lines delivering water directly to crop roots, demonstrating technological risk mitigation against unpredictable rainfall and drought."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Risk Management",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Define **agricultural risk and uncertainty** in farming.",
                                "Classify farm risks into **Production, Market (Price), Financial, and Institutional** risks.",
                                "Deploy risk mitigation strategies: **Crop Diversification, Irrigation, and Forward Contracts**.",
                                "Analyze how **Index-Based Satellite Agricultural Insurance** protects farm capital."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The 4 Core Sources of Agricultural Risk",
                        "content": {
                            "title": "Why Farming is Inherently Risky",
                            "text": "1. **Production Risk**: Biological threats to crop yields or livestock survival (severe droughts, hailstorms, pest outbreaks like Fall Armyworm, livestock epidemics like Foot and Mouth disease).\n2. **Market (Price) Risk**: Sharp price collapses during seasonal gluts, sudden consumer demand shifts, or cheap import dumping.\n3. **Financial Risk**: High loan interest rate spikes, cash flow shortages, or lender loan recalls.\n4. **Institutional / Policy Risk**: Sudden changes in government import tariffs, fertilizer subsidies, or land tenure laws."
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "Strategic Risk Mitigation Techniques",
                        "content": {
                            "title": "Proactive Agribusiness Defense Strategies",
                            "text": "- **Enterprise Diversification**: Growing multiple unrelated crops and livestock (e.g., 1 acre sorghum + 1 acre beans + 50 poultry). If one fails due to pests or low prices, the others sustain the business.\n- **Technological Adoption**: Installing drip irrigation eliminates drought dependence; greenhouses shield crops from extreme rainfall, hail, and pests.\n- **Forward Supply Contracts**: Signing formal pre-planting agreements with schools or supermarkets locking in a fixed purchase price, completely eliminating price drop risks!"
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Agricultural Insurance and Index-Based Systems",
                        "content": {
                            "title": "Capital Protection through Satellite Verification",
                            "text": "- **Traditional Crop Insurance**: Requires physical farm visits by claims adjusters (expensive and slow for smallholders).\n- **Index-Based Agricultural Insurance**: Uses real-time satellite imagery and weather station data to measure rainfall. If seasonal rainfall in a county drops below a pre-set millimeter threshold (indicating severe drought), automated mobile cash payouts are sent directly to insured farmers without paperwork!"
                        }
                    }
                ],
                [
                    {
                        "type": "comparison_table",
                        "title": "Agricultural Risk Types vs Mitigation Strategies",
                        "content": {
                            "title": "Agribusiness Risk Management Matrix",
                            "headers": ["Risk Category", "Specific Farm Threat", "Potential Financial Impact", "Strategic Risk Mitigation"],
                            "rows": [
                                ["Production Risk", "Severe dry spell / drought", "Total crop withering (100% loss)", "Drip irrigation & drought-tolerant crops (Sorghum)"],
                                ["Production Risk", "Pest outbreak (Armyworm)", "Severe leaf defoliation", "IPM spraying & certified resistant crop varieties"],
                                ["Market (Price) Risk", "Harvest market glut (Tomatoes KES 10/kg)", "Selling below production cost", "Value addition (Tomato Jam) & Forward contracts"],
                                ["Financial Risk", "Rising loan interest rates", "Default and asset foreclosure", "Borrow from low-interest SACCOs; maintain cash reserves"],
                                ["Climate Catastrophe", "Unprecedented regional drought", "Widespread starvation & bankruptcy", "Index-Based Satellite Agricultural Insurance"]
                            ]
                        }
                    }
                ],
                [
                    {
                        "type": "mini_activity",
                        "title": "Case Study Practical: Designing a Risk Management Plan for 'Farmer Juma'",
                        "content": {
                            "title": "Farm Risk Management Consulting Practicum",
                            "task": "Case: Farmer Juma planted 5 acres of monoculture tomatoes. Blight wiped out 80% of the crop, and tomato prices crashed to KES 10/kg.\n1. Identify Juma's production risk and market risk errors.\n2. Design a 3-point risk management plan (Diversification, Protection, Marketing) for next season.",
                            "materials": ["Case Handout", "Notebook", "Pen"],
                            "safety": "Ensure realistic risk mitigation recommendations."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Core Summary: Risk Management",
                        "content": {
                            "title": "Key Takeaways",
                            "text": "- **Farming faces Production, Market, Financial, and Policy risks**.\n- **Diversification spreads risk across multiple crops and livestock**.\n- **Drip irrigation and greenhouses buffer against climate extremes**.\n- **Forward contracts lock in prices; index insurance compensates drought**."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Example of Risk Diversification",
                        "content": {
                            "question": "Which of the following farm management practices represents a classic, effective example of agricultural risk mitigation through enterprise diversification?",
                            "options": [
                                "Planting 10 acres of the exact same variety of hybrid maize monoculture",
                                "Planting 1 acre of French beans, 1 acre of kales, and maintaining a 50-bird poultry unit",
                                "Taking three commercial bank loans simultaneously to buy an oversized tractor",
                                "Spraying the entire farm with broad-spectrum chemical pesticides every morning"
                            ],
                            "answer": "B",
                            "explanation": "Diversification involves distributing capital and labor across multiple unrelated enterprises. By combining beans, kales, and poultry, a pest outbreak or price drop in one enterprise is buffered by the survival and sales of the other two enterprises."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 11: Labor Management and Regulations
        # =====================================================================
        {
            "unit_order": 11,
            "unit_name": "Labor Management and Regulations",
            "unit_description": "Casual vs permanent farm labor; labor productivity and piece-rate incentives; Employment Act compliance, minimum wage, OSHA safety PPE, statutory deductions (NHIF, NSSF, PAYE).",
            "lesson_title": "Agribusiness Labor: Labor Types, Productivity Incentives, and Kenyan Employment Regulations",
            "pages": [
                [
                    {
                        "type": "suggested_image",
                        "title": "Agricultural Workers Harvesting Crops in Kenyan Commercial Farm",
                        "content": {
                            "title": "Agricultural Workers Harvesting Crops in Kenyan Commercial Farm",
                            "caption": "Skilled agricultural laborers harvesting tea leaves in Kenya, demonstrating labor organization, task specialization, and piece-rate productivity."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Labor Management",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Differentiate between **Casual Labor** and **Permanent Labor**.",
                                "Analyze methods to maximize **labor productivity (output per worker-hour)**.",
                                "Implement **piece-rate performance incentives**.",
                                "Ensure compliance with the **Kenyan Employment Act, Minimum Wage, OSHA PPE, and statutory deductions**."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Types of Farm Labor",
                        "content": {
                            "title": "Casual vs Permanent Agricultural Labor",
                            "text": "1. **Casual Labor**: Hired on a short-term, day-to-day basis for seasonal spikes (land clearing, transplanting, weeding, harvesting).\n   - *Terms*: Paid daily or weekly wages; no long-term contracts; high flexibility for seasonal farms.\n2. **Permanent Labor**: Hired on a long-term, continuous basis for ongoing core operations (dairy milking, machinery operators, farm manager, night security).\n   - *Terms*: Receive fixed monthly salaries; entitled to formal employment contracts, paid leave, and statutory benefits."
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "Improving Labor Productivity",
                        "content": {
                            "title": "Maximizing Output Per Worker-Hour",
                            "text": "Labor is often a farm's highest variable operational cost. To optimize **labor productivity**, managers should:\n- **Provide Ergonomic Tools**: Supply sharp wheelhoes and mechanical sprayers rather than heavy, blunt hand jembes.\n- **Implement Piece-Rate Incentives**: Pay workers per unit of output (e.g., KES 15 per kg of tea plucked, or KES 50 per crate of tomatoes sorted) rather than a flat hourly rate.\n- **Clear Training & Standard Operating Procedures (SOPs)**: Train workers on precise planting spacing and harvesting hygiene.\n- **Welfare & Safety**: Provide clean drinking water, shaded resting areas, and scheduled rest breaks."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Legal Regulations and Employer Duties in Kenya",
                        "content": {
                            "title": "Statutory Compliance under Kenyan Law",
                            "text": "Agricultural employers in Kenya must strictly comply with the **Employment Act and OSHA**:\n1. **Agricultural Minimum Wage**: Pay workers at or above the government-mandated gazetted minimum wage for agricultural labor.\n2. **Occupational Safety and Health (OSHA)**: Provide full Personal Protective Equipment (PPE: respirators, rubber gloves, overalls, gumboots) when spraying agrochemicals.\n3. **Statutory Deductions**: For permanent staff, employers must deduct and remit **SHIF/NHIF** (health insurance), **NSSF** (pension savings), and **PAYE** (income tax)."
                        }
                    }
                ],
                [
                    {
                        "type": "comparison_table",
                        "title": "Casual vs Permanent Farm Labor Comparison Matrix",
                        "content": {
                            "title": "Farm Labor Structures & Legal Requirements",
                            "headers": ["Dimension", "Casual Farm Labor", "Permanent Farm Labor", "Management Strategy"],
                            "rows": [
                                ["Employment Duration", "Day-to-day / seasonal (<3 months)", "Continuous long-term contract", "Use casuals for harvest peaks; permanent for daily chores"],
                                ["Payment Structure", "Daily wage or piece-rate (per kg/crate)", "Fixed monthly salary", "Piece-rate boosts speed; monthly salary builds loyalty"],
                                ["Statutory Benefits", "Daily pay only (no leave/pension)", "Mandatory NSSF, NHIF, 21-day paid leave", "Remit statutory deductions by 9th of every month"],
                                ["Safety / PPE Duty", "Employer MUST provide PPE for hazards", "Employer MUST provide full PPE & medical check", "OSHA applies equally to all workers on farm!"]
                            ]
                        }
                    }
                ],
                [
                    {
                        "type": "mini_activity",
                        "title": "Management Practical: Calculating Piece-Rate vs Daily Wage Labor Cost",
                        "content": {
                            "title": "Labor Productivity Calculation Practicum",
                            "task": "A coffee farm needs 1,000 kg of coffee berries picked in 1 day:\n- Option A: Hire 10 casuals at a flat rate of KES 600/day (average picking rate: 80 kg/worker).\n- Option B: Hire 8 skilled pickers paid piece-rate at KES 6 per kg picked (average picking rate: 125 kg/worker).\n1. Calculate total cost and total harvest for both options.\n2. Recommend the more productive labor structure.",
                            "materials": ["Calculator", "Notebook", "Pen"],
                            "safety": "Ensure sound agribusiness labor reasoning."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Core Summary: Labor Management",
                        "content": {
                            "title": "Key Takeaways",
                            "text": "- **Casual labor handles seasonal peaks; permanent labor manages daily operations**.\n- **Piece-rate pay directly boosts worker productivity and aligns costs with yield**.\n- **Employers must comply with agricultural minimum wage laws**.\n- **Provide mandatory OSHA PPE for all hazardous spraying and machinery tasks**."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Rationale for Piece-Rate Pay",
                        "content": {
                            "question": "A commercial horticulture farm in Naivasha pays flower harvesters based on the total number of export-grade flower stems picked and sorted each day. What is the primary agribusiness benefit of this payment system?",
                            "options": [
                                "It automatically decreases the soil pH in the greenhouse",
                                "It serves as a direct performance incentive that boosts labor productivity and aligns labor expenses with actual harvest output",
                                "It eliminates the need for the farm to purchase irrigation water",
                                "It makes the farm completely immune to national minimum wage laws"
                            ],
                            "answer": "B",
                            "explanation": "Paying workers based on piece-rate output (per stem or kg harvested) incentivizes speed and meticulous sorting, directly boosting labor productivity while ensuring that labor expenditure correlates directly with marketable yield."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 12: Preparing a Business Proposal for an Enterprise
        # =====================================================================
        {
            "unit_order": 12,
            "unit_name": "Preparing a Business Proposal for an Enterprise",
            "unit_description": "Agribusiness proposal (business plan) architecture: Executive Summary, Market Analysis, Production Plan, Financial Plan; school-based micro-enterprise pitch preparation.",
            "lesson_title": "Agribusiness Proposals: Business Plan Architecture, Production Schedules, and Financial Modeling",
            "pages": [
                [
                    {
                        "type": "suggested_image",
                        "title": "Professional Business Proposal Document on Office Desk",
                        "content": {
                            "title": "Professional Business Proposal Document on Office Desk",
                            "caption": "A formal business proposal document and financial plan, illustrating the structured blueprint required to pitch for agribusiness credit and partnerships."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Agribusiness Proposals",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Define an **agricultural business proposal (business plan)** and state its purposes.",
                                "Identify the 4 core structural sections: **Executive Summary, Market Analysis, Production Plan, and Financial Plan**.",
                                "Draft a compelling **Executive Summary highlighting the value proposition**.",
                                "Construct an **Operational Production Schedule** for an agribusiness venture."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "What is an Agribusiness Proposal?",
                        "content": {
                            "title": "The Strategic Operating Blueprint",
                            "text": "An **agricultural business proposal** (or business plan) is a comprehensive written document detailing an agribusiness's objectives, market opportunity, operational methods, and financial forecasts:\n\n- **Internal Blueprint**: Serves as the day-to-day operating manual for the farm manager.\n- **External Pitch Tool**: The primary document submitted to AFC, commercial banks, agricultural SACCOs, or investors to secure start-up and expansion capital."
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "The 4 Core Structural Sections of a Proposal",
                        "content": {
                            "title": "Architecture of a Winning Agribusiness Plan",
                            "text": "1. **Executive Summary**: A concise 1-page snapshot written last but placed first, summarizing the enterprise problem, solution, funding needs, and projected ROI.\n2. **Market Analysis**: Identifies target buyers (schools, local markets, supermarkets), competitor pricing, supply gaps, and marketing strategy.\n3. **Production (Operational) Plan**: Outlines land size, water sources, input sourcing, technical management protocols, disease biosecurity, and harvest schedules.\n4. **Financial Plan**: Contains start-up capital budget, 1-year cash flow projections, enterprise budget, break-even analysis, and projected P&L statement."
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Agribusiness Proposal (Business Plan) Structural Framework",
                        "content": {
                            "title": "Agribusiness Proposal (Business Plan) Structural Framework",
                            "caption": "Proposal Structure: 1 Executive Summary (Value Pitch & Funding) -> 2 Market Analysis (Demand & Competitors) -> 3 Production Plan (Land, Inputs & Schedule) -> 4 Financial Plan (Budgets, Cash Flow & ROI)."
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "Drafting the Executive Summary and Production Schedule",
                        "content": {
                            "title": "Engaging Investors and Agribusiness Lenders",
                            "text": "- **The Executive Summary Checklist**:\n  - *Problem*: High cost and scarcity of clean vegetables in the local urban estate.\n  - *Solution*: Establishing a 1/4-acre drip-irrigated spinach and kale unit.\n  - *Capital Request*: Seeking KES 80,000 for drip kit and certified hybrid seeds.\n  - *Return on Investment*: Projected Net Profit of KES 120,000 in Year 1 (repaying loan in 6 months).\n- **The Production Schedule**: A Gantt chart mapping nursery establishment, transplanting, weeding, fertigation, and weekly harvest windows."
                        }
                    },
                    {
                        "type": "comparison_table",
                        "title": "Agribusiness Proposal Sections & Investor Evaluation Focus",
                        "content": {
                            "title": "Agribusiness Plan Evaluation Matrix",
                            "headers": ["Proposal Section", "Core Information Required", "What Lenders / Investors Look For", "Common Pitfall to Avoid"],
                            "rows": [
                                ["Executive Summary", "Mission, value proposition, funding request", "Clarity, feasibility, confidence", "Too long, vague funding amount"],
                                ["Market Analysis", "Customer demographics, competitors, pricing", "Verified buyer demand & purchase contracts", "Assuming 'everyone will buy' without proof"],
                                ["Production Plan", "Land, water, input sourcing, agronomy timeline", "Technical competence & biosecurity protocols", "Underestimating water or labor needs"],
                                ["Financial Plan", "Start-up Capex, cash flow, P&L, break-even", "Realistic cost accounting & rapid payback period", "Omitting tool depreciation and loan interest"]
                            ]
                        }
                    }
                ],
                [
                    {
                        "type": "mini_activity",
                        "title": "Agribusiness Practical: Drafting an Executive Summary for a School Project",
                        "content": {
                            "title": "Proposal Executive Summary Practicum",
                            "task": "Form groups of 4. Select an enterprise (e.g., Raised Rabbitry, Drip Vegetable Garden, or Poultry Layer Unit):\n1. Draft a 150-word Executive Summary detailing Problem, Solution, Capital Needed, and Projected Net Profit.\n2. Create a 4-month Production Timeline table.",
                            "materials": ["Proposal Template", "Notebook", "Pen"],
                            "safety": "Ensure collaborative teamwork and realistic figures."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Core Summary: Agribusiness Proposals",
                        "content": {
                            "title": "Key Takeaways",
                            "text": "- **A business proposal is an operational manual and loan pitch document**.\n- **Contains 4 pillars: Executive Summary, Market, Production, Financial**.\n- **The Executive Summary must clearly state the capital request and ROI**.\n- **The Production Plan details physical agronomy and weekly schedules**."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Identifying Proposal Sections",
                        "content": {
                            "question": "Which specific section of an agricultural business proposal details the required land acreage, water irrigation sources, certified input suppliers, and the weekly crop management schedule?",
                            "options": [
                                "Executive Summary",
                                "Financial Plan",
                                "Market Analysis",
                                "Production (Operational) Plan"
                            ],
                            "answer": "D",
                            "explanation": "The Production (Operational) Plan outlines the physical mechanics and biological timeline of the farm, specifying land dimensions, irrigation infrastructure, input procurement, agronomic tasks, and harvest schedules."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 13: Presentation, Peer Evaluation & Topic Review
        # =====================================================================
        {
            "unit_order": 13,
            "unit_name": "Presentation, Peer Evaluation & Topic Review",
            "unit_description": "3-Minute agribusiness pitch mechanics (Why, How, Returns); 3-tier peer review rubric (Ecological feasibility, Market realism, Financial integrity); Section A & Section B Topic Assessment; 8 Summative MCQs.",
            "lesson_title": "Agribusiness Pitching: Proposal Presentations, Peer Review Rubrics, and Summative Assessment",
            "pages": [
                [
                    {
                        "type": "suggested_image",
                        "title": "Agribusiness Presentation and Technology Pitch Exhibition",
                        "content": {
                            "title": "Agribusiness Presentation and Technology Pitch Exhibition",
                            "caption": "Entrepreneurs delivering an agribusiness pitch presentation before a panel of agricultural lenders, demonstrating project viability and financial clarity."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Pitching & Topic Review",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Deliver a persuasive **3-minute agribusiness pitch** answering *Why, How, and Returns*.",
                                "Evaluate proposals using the 3-tier rubric: **Ecological Feasibility, Market Realism, and Financial Integrity**.",
                                "Synthesize the **complete 13-lesson Agribusiness Enterprise Framework**.",
                                "Complete the comprehensive **Summative Topic Assessment**."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Delivering an Agribusiness Pitch",
                        "content": {
                            "title": "The 3-Minute Investor Pitch Framework",
                            "text": "A **pitch** is a concise, persuasive presentation of an agribusiness proposal delivered to SACCO managers, bank loan officers, or grant panels. A winning 3-minute pitch must answer 3 core questions:\n1. **Why this Enterprise?** (Demonstrate the verified local market deficit and customer demand).\n2. **How will it Operate?** (Explain your biosecure, efficient production and agronomic management plan).\n3. **What are the Financial Returns?** (Present break-even price, gross margin, and net payback period!)."
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "The 3-Tier Proposal Evaluation Rubric",
                        "content": {
                            "title": "Critiquing Agribusiness Plans",
                            "text": "When acting as peer reviewers or loan officers, score proposals against 3 critical criteria:\n- **Ecological & Agronomic Feasibility**: Does the crop or animal match local soil pH, rainfall, and altitude profiles?\n- **Market Realism**: Are projected selling prices and sales volumes supported by local market surveys, or are they unrealistically inflated?\n- **Financial Integrity**: Do budgets account for all fixed and variable costs (transport, casual labor, tool depreciation, loan interest)?"
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Master Agribusiness Enterprise Establishment & Management Lifecycle",
                        "content": {
                            "title": "Master Agribusiness Enterprise Establishment & Management Lifecycle",
                            "caption": "Agribusiness Enterprise Cycle: 1 Ownership Model -> 2 Feasibility & Ecological Fit -> 3 Certified Inputs & KEPHIS -> 4 Capital & Budgeting -> 5 Production & Record Keeping -> 6 P&L Audit & Risk Mitigation -> 7 Proposal & Investment."
                        }
                    }
                ],
                [
                    {
                        "type": "mini_activity",
                        "title": "Performance Task: Classroom Agribusiness Pitch Panel & SACCO Loan Simulation",
                        "content": {
                            "title": "Agribusiness Pitch Panel Practicum",
                            "task": "1. Student groups take turns delivering a 3-minute pitch of their Lesson 12 proposals.\n2. The rest of the class acts as 'Agricultural SACCO Loan Officers', scoring on: Ecological Fit, Market Realism, and Financial Integrity.\n3. Provide constructive feedback to refine input costs and risk management before final submission.",
                            "materials": ["Pitch Rubric", "Timer", "Notebook", "Pen"],
                            "safety": "Maintain a respectful, professional peer review atmosphere."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Core Summary: Pitching & Review",
                        "content": {
                            "title": "Key Takeaways",
                            "text": "- **Pitches must answer Why, How, and Returns in 3 minutes**.\n- **Evaluate proposals on Ecological Fit, Market Realism, Financial Accuracy**.\n- **Include hidden costs like transport, depreciation, and casual labor**.\n- **Refine business plans iteratively based on expert and lender feedback**."
                        }
                    }
                ],
                # Pages 4 to 8: 8 Summative Topic Assessment MCQs
                [
                    {
                        "type": "knowledge_check",
                        "title": "Summative MCQ 1: Owner Liability in Private Limited Companies",
                        "content": {
                            "question": "What is the primary legal and financial advantage of registering an agricultural business as a Private Limited Company rather than operating as a Sole Proprietorship?",
                            "options": [
                                "The company is completely exempt from paying all national taxes",
                                "Shareholders enjoy limited liability, meaning their personal property is legally protected from being seized to settle business debts if the farm fails",
                                "The government provides free fertilizers and tractors to all limited companies",
                                "The company does not need to maintain any accounting records"
                            ],
                            "answer": "B",
                            "explanation": "In a Private Limited Company, shareholders have limited liability. They can only lose the capital they personally invested in company shares; their personal homes, land, and private assets cannot be seized by creditors to pay company debts."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Summative MCQ 2: KEPHIS Seed Verification Process",
                        "content": {
                            "question": "How does a Kenyan farmer verify that a purchased packet of hybrid maize seed is genuine and officially certified by KEPHIS?",
                            "options": [
                                "By soaking the seeds in hot tea for 24 hours",
                                "By scratching the silver tamper-proof label on the packet and sending the revealed PIN code via SMS to 1393 for instant confirmation",
                                "By checking if the packet has a colorful drawing of a tractor",
                                "By smelling the seed packet for pesticide odors"
                            ],
                            "answer": "B",
                            "explanation": "KEPHIS mandates tamper-proof scratch-off labels on all certified seed packets. Farmers scratch the panel to reveal a unique verification PIN and SMS it to 1393 to receive instant confirmation of seed variety authenticity and germination testing."
                        }
                    }
                ],
                [
                    {
                        "type": "knowledge_check",
                        "title": "Summative MCQ 3: Classifying Farm Capital Items",
                        "content": {
                            "question": "Which of the following pairs of farm assets is correctly classified as Fixed Capital and Working Capital respectively?",
                            "options": [
                                "Diesel fuel (Fixed Capital) and Farm Tractor (Working Capital)",
                                "Permanent Drip Irrigation Pipeline (Fixed Capital) and Top-Dressing CAN Fertilizer (Working Capital)",
                                "Broiler Starter Mash (Fixed Capital) and Concrete Store Building (Working Capital)",
                                "Casual Labor Wages (Fixed Capital) and Dairy Milking Parlor (Working Capital)"
                            ],
                            "answer": "B",
                            "explanation": "Fixed Capital consists of durable multi-year infrastructure like drip irrigation pipelines. Working Capital consists of operational inputs consumed within a single crop cycle like CAN fertilizer."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Summative MCQ 4: Advantage of Agricultural Finance Corporation (AFC) Credit",
                        "content": {
                            "question": "Why do commercial farmers often prefer borrowing long-term capital from the Agricultural Finance Corporation (AFC) rather than commercial retail banks?",
                            "options": [
                                "AFC loans never have to be repaid by farmers",
                                "AFC offers subsidized, lower interest rates and flexible loan repayment schedules structured around seasonal harvest cycles",
                                "Commercial banks do not allow farmers to open savings accounts",
                                "AFC only provides cash grants with zero documentation"
                            ],
                            "answer": "B",
                            "explanation": "The Agricultural Finance Corporation (AFC) is a dedicated state agricultural development bank. It offers concessionary interest rates and aligns repayment dates with crop harvesting seasons, preventing default during crop growth stages."
                        }
                    }
                ],
                [
                    {
                        "type": "knowledge_check",
                        "title": "Summative MCQ 5: Calculating Unit Cost of Production",
                        "content": {
                            "question": "A tomato farmer spends KES 15,000 on fixed overheads and KES 45,000 on variable inputs to harvest 300 crates of tomatoes. What is the unit cost of production per crate?",
                            "options": [
                                "KES 50 per crate",
                                "KES 150 per crate",
                                "KES 200 per crate",
                                "KES 600 per crate"
                            ],
                            "answer": "C",
                            "explanation": "Total Cost = Fixed Cost + Variable Cost = KES 15,000 + KES 45,000 = KES 60,000. Unit Cost = Total Cost / Output = KES 60,000 / 300 crates = KES 200 per crate."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Summative MCQ 6: Calculating Enterprise Gross Margin",
                        "content": {
                            "question": "A 1-acre watermelon enterprise generates KES 180,000 in gross sales revenue while incurring KES 60,000 in total variable costs and KES 20,000 in fixed overhead costs. What is the Gross Margin of this enterprise?",
                            "options": [
                                "KES 240,000",
                                "KES 120,000",
                                "KES 100,000",
                                "KES 40,000"
                            ],
                            "answer": "B",
                            "explanation": "Gross Margin = Gross Revenue minus Total Variable Costs = KES 180,000 - KES 60,000 = KES 120,000. (Net Profit would be Gross Margin minus Fixed Costs = 120,000 - 20,000 = KES 100,000)."
                        }
                    }
                ],
                [
                    {
                        "type": "knowledge_check",
                        "title": "Summative MCQ 7: Index-Based Satellite Crop Insurance",
                        "content": {
                            "question": "How does modern 'Index-Based Agricultural Insurance' protect smallholder farmers in drought-prone areas of Kenya?",
                            "options": [
                                "By requiring insurance agents to inspect every single crop plant by hand before paying",
                                "By automatically triggering mobile money compensation payouts when satellite sensors confirm that seasonal rainfall has dropped below a critical threshold",
                                "By providing free irrigation water during dry seasons",
                                "By forcing farmers to plant only imported grain varieties"
                            ],
                            "answer": "B",
                            "explanation": "Index-based insurance relies on satellite weather data. When regional rainfall drops below a specified millimeter index (indicating drought), compensation is automatically paid to insured farmers without lengthy manual claim adjustments."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Summative MCQ 8: Core Sections of an Agribusiness Proposal",
                        "content": {
                            "question": "Which of the following outlines the correct structural sequence of the main sections in a professional agricultural business proposal?",
                            "options": [
                                "Financial Plan -> Cover Photo -> Land Title -> Fertilizer List",
                                "Executive Summary -> Market Analysis -> Production (Operational) Plan -> Financial Plan",
                                "Market Analysis -> Worker Salaries -> Weather Forecast -> Bank Statement",
                                "Production Plan -> Farm Rules -> Land Map -> Receipt Log"
                            ],
                            "answer": "B",
                            "explanation": "A standard agribusiness proposal is structured logically: 1. Executive Summary (Project Overview), 2. Market Analysis (Demand & Competitors), 3. Production Plan (Operations & Timeline), and 4. Financial Plan (Budgets, Cash Flow & ROI)."
                        }
                    }
                ],
                # Page 9: Capstone Summary
                [
                    {
                        "type": "summary",
                        "title": "Topic 15 Capstone Summary: Establishing an Agricultural Enterprise Mastery",
                        "content": {
                            "title": "Mastery Overview: Grade 10 Agricultural Enterprise Establishment",
                            "text": "Congratulations on mastering **Topic 15: Establishing an Agricultural Enterprise**!\n\nYou have mastered:\n- **Enterprise Types & Liability**: Sole proprietorships, partnerships, cooperatives, and limited liability companies.\n- **Feasibility Analysis**: Matching soil pH, rainfall, altitude, and transport logistics to crop and livestock needs.\n- **Input Verification**: KEPHIS certified seeds, scratch-off SMS codes (1393), PCBP registered chemicals, and avoiding counterfeits.\n- **Capital Structures**: Fixed capital (Capex, multi-year infrastructure) vs Working capital (Opex, single-cycle inputs).\n- **Financial Sourcing**: Personal savings, retained profits, AFC concessionary loans, agricultural SACCOs, and Chamas.\n- **Cost of Production & Break-Even**: Total Cost = TFC + TVC; Unit Cost = TC / Output; setting profitable prices above break-even.\n- **Farm Budgeting & Records**: Enterprise budgets, Gross Margin = Revenue - TVC; Daily Cash Book reconciliation.\n- **Profit & Loss Statements**: Calculating Net Profit ($Revenue - Expenses$) vs Net Loss to audit enterprise viability.\n- **Risk & Labor Management**: Diversification, drip irrigation, forward contracts, index-based satellite insurance; Employment Act minimum wage, OSHA PPE, and piece-rate productivity.\n- **Agribusiness Proposals & Pitches**: 4-part proposal architecture (Executive Summary, Market, Production, Financial) and delivering a persuasive 3-minute agribusiness pitch."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Topic 15 Final Takeaway",
                        "content": {
                            "title": "The Agribusiness Enterprise Maxim",
                            "text": "Farming is a commercial business, not a gamble. Verify inputs with KEPHIS, track every variable cost, balance daily cash books, manage risks through diversification and irrigation, and formulate bankable business plans. Financial literacy and disciplined farm accounting transform agriculture into a powerhouse of sustainable wealth."
                        }
                    }
                ]
            ]
        }
    ]

@transaction.atomic
def ingest_grade10_topic15(replace=False):
    """Executes the complete production ingestion of Grade 10 Agriculture Topic 15: Establishing an Agricultural Enterprise."""
    print("=" * 80)
    print("STARTING INGESTION: CBC Grade 10 Agriculture — Topic 15: Establishing an Agricultural Enterprise")
    print("=" * 80)

    curriculum = Curriculum.objects.filter(name__iexact="CBC").first()
    grade = Grade.objects.filter(curriculum=curriculum, name__icontains="10").first()
    subject = Subject.objects.filter(grade=grade, name__iexact="Agriculture").first()

    assert curriculum and grade and subject, "Curriculum/Grade/Subject not found!"

    topic_name = "Establishing an Agricultural Enterprise"
    topic = Topic.objects.filter(subject=subject, name=topic_name).first()
    if not topic:
        topic = Topic.objects.create(
            subject=subject,
            name=topic_name,
            description="Comprehensive vocational and entrepreneurial training in establishing agricultural enterprises: ownership models (sole proprietorship, partnership, cooperative, limited company), feasibility analysis, input sourcing and KEPHIS verification, fixed vs working capital, AFC and SACCO financing, cost of production and break-even math, enterprise budgeting, daily cash book records, P&L statements, risk mitigation (diversification, index insurance), labor laws (minimum wage, OSHA), and agribusiness proposal pitching.",
            order=15
        )
        print(f"Created Topic 15: {topic.name} (ID: {topic.id})")
    else:
        topic.order = 15
        topic.description = "Comprehensive vocational and entrepreneurial training in establishing agricultural enterprises: ownership models (sole proprietorship, partnership, cooperative, limited company), feasibility analysis, input sourcing and KEPHIS verification, fixed vs working capital, AFC and SACCO financing, cost of production and break-even math, enterprise budgeting, daily cash book records, P&L statements, risk mitigation (diversification, index insurance), labor laws (minimum wage, OSHA), and agribusiness proposal pitching."
        topic.save()
        print(f"Resolved Topic 15: {topic.name} (ID: {topic.id})")

    if replace:
        print("Flag --replace active: Clearing existing LearningUnits and Lessons for Topic 15...")
        topic.learning_units.all().delete()
        topic.lessons.all().delete()

    curriculum_data = build_topic15_curriculum()
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
                    "topic_order": 15,
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
                    block_id=f"g10_agri_t15_u{u_order}_p{page_idx}_b{comp_idx}",
                    block_type=b_type,
                    component_type=b_type,
                    title=b_title,
                    content=b_content,
                    order=block_order_counter,
                    page_number=page_idx,
                    component_order=comp_idx,
                    page_title=b_title if comp_idx == 1 else None,
                    metadata={"topic_order": 15, "unit_order": u_order, "page": page_idx}
                )
                block_order_counter += 1
                total_blocks += 1

        print(f"  Ingested Unit {u_order}: {u_name} -> Lesson '{l_title}' ({len(pages)} Pages, {block_order_counter - 1} Blocks)")

    print("=" * 80)
    print(f"INGESTION COMPLETE: Topic 15 '{topic.name}'")
    print(f"  Total Units:   {total_units}")
    print(f"  Total Lessons: {total_lessons}")
    print(f"  Total Pages:   {total_pages}")
    print(f"  Total Blocks:  {total_blocks}")
    print("=" * 80)

if __name__ == "__main__":
    replace_flag = "--replace" in sys.argv
    ingest_grade10_topic15(replace=replace_flag)
