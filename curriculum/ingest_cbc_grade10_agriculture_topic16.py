"""
VLearn CBC Grade 10 Agriculture — Topic 16: Marketing Agricultural Produce
Production Ingestion Engine (Deep Senior Secondary Pedagogical Edition)

Curriculum: CBC (ID: 5)
Grade: Grade 10 (ID: 5, Level: 10)
Subject: Agriculture
Topic: Marketing Agricultural Produce (Topic Order: 16)

Decomposed into 6 Learning Units & 6 Published Lessons:
  1. Introduction to Agricultural Marketing (4 Pages, 9 Blocks)
  2. The Marketing Mix (The 4 Ps) (4 Pages, 9 Blocks)
  3. Marketing Channels & Outlets (4 Pages, 9 Blocks)
  4. Processing, Sorting, and Grading for the Market (4 Pages, 9 Blocks)
  5. Market Information & Price Fluctuations (4 Pages, 9 Blocks)
  6. Formulating a Marketing Strategy, Pitching & Topic Review (9 Pages, 18 Blocks)
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

def build_topic16_curriculum():
    """Returns the comprehensive pedagogical page and block structure for Grade 10 Topic 16: Marketing Agricultural Produce."""
    return [
        # =====================================================================
        # LESSON 1: Introduction to Agricultural Marketing
        # =====================================================================
        {
            "unit_order": 1,
            "unit_name": "Introduction to Agricultural Marketing",
            "unit_description": "Defining agricultural marketing vs raw selling; 4 Economic Utilities (Form, Place, Time, Possession); Agribusiness value chain concept.",
            "lesson_title": "Agribusiness Value Chains: Foundations of Agricultural Marketing and Economic Utility Creation",
            "pages": [
                [
                    {
                        "type": "suggested_image",
                        "title": "Vibrant Open-Air Fresh Produce Stall in Kenya",
                        "content": {
                            "title": "Vibrant Open-Air Fresh Produce Stall in Kenya",
                            "caption": "A colorful roadside agricultural stall in Kenya displaying fresh cabbages, tomatoes, and greens, illustrating agricultural marketing and retail distribution."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Introduction to Agricultural Marketing",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Define **agricultural marketing** and contrast it with simple **farm-gate selling**.",
                                "Analyze how marketing creates **Form, Place, Time, and Possession utilities**.",
                                "Trace how commodities move through the **agribusiness value chain**.",
                                "Evaluate how marketing transforms farmers from passive price-takers into strategic price-setters."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "What is Agricultural Marketing?",
                        "content": {
                            "title": "Marketing vs Simple Product Selling",
                            "text": "**Agricultural marketing** is the integrated series of business activities involved in moving agricultural products from the farm gate to the final consumer:\n\n- **Selling vs. Marketing**:\n  - *Selling*: A one-way transaction where a farmer disposes of raw harvested crops for quick cash, often accepting whatever low price a middleman dictates.\n  - *Marketing*: A customer-centric strategy involving consumer preference research, quality grading, protective packaging, competitive pricing, and targeted distribution channels to capture premium value."
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "The 4 Types of Economic Utility in Marketing",
                        "content": {
                            "title": "How Marketing Creates Economic Worth",
                            "text": "Marketing increases the monetary value of raw farm commodities by generating 4 forms of **economic utility**:\n1. **Form Utility**: Changing the physical state of the crop through processing (e.g., slicing raw potatoes into vacuum-sealed french fry strips).\n2. **Place Utility**: Transporting produce from rural surplus production zones to high-demand urban consumer centers (e.g., shipping cabbages from Nyandarua to Nairobi).\n3. **Time Utility**: Storing non-perishables safely after harvest to sell months later when market supply drops and prices soar (e.g., dry maize in hermetic bags).\n4. **Possession Utility**: Facilitating legal transfer of ownership via digital M-Pesa payments, receipts, and doorstep delivery logistics."
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "How Agricultural Marketing Creates 4 Types of Economic Utility",
                        "content": {
                            "title": "How Agricultural Marketing Creates 4 Types of Economic Utility",
                            "caption": "Utility Transformation Pipeline: Raw Harvest -> 1 Form Utility (Processing) -> 2 Place Utility (Transport) -> 3 Time Utility (Storage) -> 4 Possession Utility (Mobile Pay & Delivery) -> High-Value Consumer Good."
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "The Agribusiness Value Chain Concept",
                        "content": {
                            "title": "Connecting Farm to Consumer Plate",
                            "text": "The **agribusiness value chain** is the full sequence of coordinated activities—from input supply, farming, harvesting, bulking, processing, transporting, wholesaling, to retailing—that adds value to agricultural produce. Understanding where your farm sits in the value chain empowers you to bypass unnecessary brokers and capture higher retail margins."
                        }
                    },
                    {
                        "type": "suggested_video",
                        "title": "Understanding the Agribusiness Value Chain and Market Linkages",
                        "content": {
                            "title": "Understanding the Agribusiness Value Chain and Market Linkages",
                            "description": "Educational video exploring how agricultural commodities travel through value chain stages from farm gate to supermarket shelves, generating economic returns.",
                            "url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
                        }
                    }
                ],
                [
                    {
                        "type": "mini_activity",
                        "title": "Agribusiness Practical: Mapping Utility Creation for Sweet Potatoes",
                        "content": {
                            "title": "Economic Utility Mapping Practicum",
                            "task": "Take a 50kg bag of raw harvested sweet potatoes:\n1. Form Utility: Propose 2 processed value-added products.\n2. Place Utility: Identify an urban destination with higher prices.\n3. Time Utility: Describe a method to store them for off-season sale.\n4. Possession Utility: Describe a digital ordering and payment channel.",
                            "materials": ["Notebook", "Pen"],
                            "safety": "Ensure realistic agribusiness reasoning."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Core Summary: Introduction to Marketing",
                        "content": {
                            "title": "Key Takeaways",
                            "text": "- **Marketing is customer-centric value creation; selling is dumping produce**.\n- **Marketing creates Form, Place, Time, and Possession utility**.\n- **Place utility moves goods from surplus farms to deficit cities**.\n- **Time utility stores goods for off-season high-price windows**."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Identifying Place Utility",
                        "content": {
                            "question": "A farmer transports fresh sweet potatoes from a rural farm in Homa Bay to an urban market in Kisumu, where she sells them for double the rural farm-gate price. What type of economic utility has this farmer primarily created?",
                            "options": [
                                "Form Utility",
                                "Place Utility",
                                "Time Utility",
                                "Chemical Utility"
                            ],
                            "answer": "B",
                            "explanation": "Place Utility is created by physically moving products from geographic areas of high surplus and low demand (where farm-gate prices are depressed) to geographic areas of high demand and low supply (where market prices are substantially higher)."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 2: The Marketing Mix (The 4 Ps)
        # =====================================================================
        {
            "unit_order": 2,
            "unit_name": "The Marketing Mix (The 4 Ps)",
            "unit_description": "4 Ps framework applied to farm produce (Product, Price, Place, Promotion); penetration vs premium pricing; farm promotional channels (WhatsApp, flyers, shows); 4 Ps Agribusiness Matrix.",
            "lesson_title": "Marketing Tactics: Applying the 4 Ps Framework (Product, Price, Place, Promotion) to Agribusiness",
            "pages": [
                [
                    {
                        "type": "suggested_image",
                        "title": "Packaged Egg Cartons Demonstrating Agribusiness Product and Packaging",
                        "content": {
                            "title": "Packaged Egg Cartons Demonstrating Agribusiness Product and Packaging",
                            "caption": "Uniform, clean, weight-graded brown eggs packaged in branded cartons, illustrating the Product and Promotion elements of the agricultural marketing mix."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: The Marketing Mix (4 Ps)",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Define the **4 Ps of the Marketing Mix (Product, Price, Place, Promotion)**.",
                                "Apply the 4 Ps specifically to agricultural commodities and livestock.",
                                "Evaluate **Penetration Pricing vs. Premium Pricing** strategies.",
                                "Construct an **Agribusiness 4 Ps Matrix** for a farm enterprise."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "P1 & P2: Product and Price in Agriculture",
                        "content": {
                            "title": "Designing the Offering and Pricing Strategy",
                            "text": "1. **Product**: The physical agricultural commodity or service. In farming, quality is defined by cleanliness, size grading, varietal taste, freshness, organic certification, and food-grade packaging (e.g., selling washed, graded spinach in labeled pouches rather than dirty, un-sorted leaves).\n2. **Price**: The financial amount customers pay. Pricing strategies must exceed unit production costs while remaining competitive:\n   - *Penetration Pricing*: Setting a low initial price to capture market share from competitors.\n   - *Premium Pricing*: Charging high prices for superior organic quality, certified hygiene, or unique value addition."
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "P3 & P4: Place and Promotion in Agriculture",
                        "content": {
                            "title": "Distribution Channels and Customer Communication",
                            "text": "3. **Place (Distribution)**: The physical locations and logistical pathways where customers buy the produce (roadside farm stands, local open markets, direct supermarket supply, or doorstep estate delivery).\n4. **Promotion**: Communication activities that inform, persuade, and remind customers to buy:\n   - *Traditional*: Word-of-mouth, farm flyers, roadside signs, agricultural trade show exhibits.\n   - *Digital*: Estate WhatsApp delivery groups, Facebook Marketplace, TikTok harvest videos."
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "The Agribusiness Marketing Mix (The 4 Ps) Framework",
                        "content": {
                            "title": "The Agribusiness Marketing Mix (The 4 Ps) Framework",
                            "caption": "The 4 Ps Wheel: Product (Grading, Hygiene & Packaging) | Price (Cost-Plus, Penetration & Premium) | Place (Farm Stall, Cooperatives & Digital Delivery) | Promotion (WhatsApp Groups, Samples & Roadside Branding)."
                        }
                    }
                ],
                [
                    {
                        "type": "comparison_table",
                        "title": "Agribusiness 4 Ps Strategic Planning Matrix",
                        "content": {
                            "title": "The 4 Ps Applied to a Layer Poultry Enterprise",
                            "headers": ["Marketing Mix P", "Strategic Focus in Farming", "Layer Poultry Example", "Tomato Enterprise Example"],
                            "rows": [
                                ["Product", "Quality, grade, hygiene, packaging", "Weight-graded brown eggs in 15-egg paper cartons", "Grade 1 washed red tomatoes in 5kg net bags"],
                                ["Price", "Cost-plus, discounts, credit terms", "KES 450 / carton; 5% discount for 10+ cartons", "KES 100 / kg (Fixed retail price)"],
                                ["Place", "Retail outlets, delivery, e-commerce", "Direct doorstep delivery to local estate & farm shop", "Supply to local supermarket & fresh vegetable kiosk"],
                                ["Promotion", "Advertising, social media, free samples", "Local estate WhatsApp marketing & free sample boiled eggs", "Facebook recipe videos & branded farm signpost"]
                            ]
                        }
                    }
                ],
                [
                    {
                        "type": "mini_activity",
                        "title": "Marketing Practical: Formulating a 4 Ps Plan for School Honey",
                        "content": {
                            "title": "4 Ps Strategy Formulation Practicum",
                            "task": "Your school apiary harvested 100kg of pure honey:\n1. Define the Product (Packaging, label, volume).\n2. Set the Price (Unit cost KES 400/kg; set retail price).\n3. Choose the Place (Where will it be sold?).\n4. Design Promotion (Draft a 30-word WhatsApp marketing message).",
                            "materials": ["Notebook", "Pen", "Calculator"],
                            "safety": "Ensure ethical advertising claims."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Core Summary: The Marketing Mix (4 Ps)",
                        "content": {
                            "title": "Key Takeaways",
                            "text": "- **The 4 Ps are Product, Price, Place, and Promotion**.\n- **Product quality includes cleanliness, grading, and packaging**.\n- **Price must cover production costs and match customer willingness to pay**.\n- **Promotion connects farm produce to target buyers through social media and word-of-mouth**."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Manipulating 4 Ps Elements",
                        "content": {
                            "question": "A beekeeper decides to package pure organic honey in sterile, sealed glass jars with professional labels and sells it at KES 900/kg, compared to crude honey sold in plastic jerrycans at KES 400/kg. Which two elements of the Marketing Mix is the farmer actively manipulating?",
                            "options": [
                                "Price and Promotion only",
                                "Place and Promotion only",
                                "Product and Price",
                                "Place and Product"
                            ],
                            "answer": "C",
                            "explanation": "By putting honey into sterile, labeled glass jars, the farmer improves the physical presentation and quality of the 'Product'. By charging KES 900/kg instead of KES 400/kg, the farmer is adjusting the 'Price' strategy to capture premium value."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 3: Marketing Channels & Outlets
        # =====================================================================
        {
            "unit_order": 3,
            "unit_name": "Marketing Channels & Outlets",
            "unit_description": "Channel levels (Direct zero-level vs Indirect one-level/two-level); Traditional outlets (Farm gate, Open-air markets, Cooperatives); Digital e-commerce & social commerce (M-Pesa, digital marketplaces).",
            "lesson_title": "Distribution Logistics: Marketing Channels, Traditional Outlets, and Digital Agri-Commerce",
            "pages": [
                [
                    {
                        "type": "suggested_image",
                        "title": "Produce Section of a Commercial Supermarket",
                        "content": {
                            "title": "Produce Section of a Commercial Supermarket",
                            "caption": "A modern supermarket produce aisle displaying organized, graded vegetables, illustrating retail marketing channels and commercial outlets."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Marketing Channels & Outlets",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Classify marketing channels into **Direct (Zero-Level) and Indirect (Multi-Level)** routes.",
                                "Evaluate pros and cons of **Farm Gate, Open-Air Markets, and Cooperatives**.",
                                "Analyze how **brokers exploit smallholder farm-gate sellers**.",
                                "Deploy **digital e-commerce and social commerce (WhatsApp/M-Pesa)** to sell direct to consumers."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Marketing Channel Structure and Levels",
                        "content": {
                            "title": "The Path from Farm to Fork",
                            "text": "A **marketing channel** is the commercial path produce travels from producer to consumer:\n\n- **Direct Channel (Zero-Level)**: Producer $\\rightarrow$ Consumer.\n  - *Example*: Selling raw milk to neighbors or vegetables from a roadside farm stall. (Farmer captures 100% of consumer price!).\n- **Indirect Channels**:\n  - *One-Level*: Producer $\\rightarrow$ Retailer $\\rightarrow$ Consumer. (e.g., Farmer supplies cabbages directly to a supermarket chain).\n  - *Two-Level*: Producer $\\rightarrow$ Wholesaler $\\rightarrow$ Retailer $\\rightarrow$ Consumer. (e.g., Maize sold to grain brokers, then to commercial millers, then to retail kiosks)."
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "Traditional Agricultural Outlets in Kenya",
                        "content": {
                            "title": "Farm Gate, Open Markets, and Cooperatives",
                            "text": "1. **Farm Gate Sales**: Buyers travel directly to the farm.\n   - *Pros*: Zero transport cost; instant cash.\n   - *Cons*: **Lowest possible selling price**; middlemen exploit the farmer's lack of storage and urgent cash needs.\n2. **Open-Air Municipal Markets (e.g., Karatina, Kibuye, Wakulima)**: Farmers transport produce to weekly public trading centers.\n   - *Pros*: Higher retail prices than farm gate.\n   - *Cons*: Incurs transport fees, municipal cess, and risks unsold perishable spoilage.\n3. **Marketing Cooperatives**: Farmers pool produce for bulk institutional buyers (e.g., dairy or coffee societies).\n   - *Pros*: High volume absorption and price security.\n   - *Cons*: Delayed monthly payouts and administrative costs."
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Agricultural Marketing Channels: Direct vs Multi-Level Intermediaries",
                        "content": {
                            "title": "Agricultural Marketing Channels: Direct vs Multi-Level Intermediaries",
                            "caption": "Channel Architecture: Direct (Farmer -> Consumer, Max Profit) vs One-Level (Farmer -> Supermarket -> Consumer) vs Two-Level (Farmer -> Broker/Wholesaler -> Retailer -> Consumer, Lowest Farm-Gate Margin)."
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "Digital Agri-Commerce and Social Selling",
                        "content": {
                            "title": "The Digital Disruption of Agricultural Middlemen",
                            "text": "Kenyan agriculture is transforming through mobile technology:\n- **Social Commerce**: Farmers post harvest photos and videos in localized estate WhatsApp groups, Facebook Marketplace, and TikTok.\n- **Pre-Ordered Harvests**: Urban customers place advance orders paid via **M-Pesa**, allowing the farmer to harvest only what has already been sold.\n- **Direct Delivery**: Utilizing motorbike riders (*boda-boda*) for same-day doorstep deliveries, eliminating middleman commissions and slashing post-harvest losses!"
                        }
                    },
                    {
                        "type": "comparison_table",
                        "title": "Marketing Outlets Comparison Matrix",
                        "content": {
                            "title": "Comparison of Agricultural Marketing Outlets",
                            "headers": ["Marketing Outlet", "Price Realization", "Transport Cost for Farmer", "Payment Timing", "Bargaining Power of Farmer"],
                            "rows": [
                                ["Farm Gate Broker", "Very Low (Distress pricing)", "Zero (Broker collects)", "Instant cash", "Extremely Low"],
                                ["Open-Air Market", "Moderate to High", "High (Farmer pays truck)", "Instant cash daily", "Moderate (Fluctuates daily)"],
                                ["Dairy Cooperative", "Stable contract rate", "Low (Shared collection)", "Monthly payment", "High (Collective voting)"],
                                ["Supermarket Supply", "Premium retail rate", "Moderate (Direct delivery)", "30–60 Day credit terms", "Moderate (Strict quality)"],
                                ["Digital / WhatsApp", "Highest (Direct consumer)", "Low (Paid by customer)", "Instant M-Pesa", "Very High (Price-setter)"]
                            ]
                        }
                    }
                ],
                [
                    {
                        "type": "mini_activity",
                        "title": "Agribusiness Practical: Channel Selection Simulation for 200 Liters Milk",
                        "content": {
                            "title": "Marketing Channel Optimization Practicum",
                            "task": "A dairy farm produces 200 liters of milk daily:\n- Channel A (Farm-gate broker): KES 38/L, zero transport.\n- Channel B (Cooperative): KES 50/L, KES 3/L transport fee.\n- Channel C (Estate direct bottles): KES 80/L, KES 15/L packaging & delivery cost.\n1. Calculate daily net income for all 3 channels.\n2. Recommend the most profitable distribution mix.",
                            "materials": ["Calculator", "Notebook", "Pen"],
                            "safety": "Ensure rigorous mathematical calculations."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Core Summary: Marketing Channels",
                        "content": {
                            "title": "Key Takeaways",
                            "text": "- **Direct channels allow farmers to capture 100% of consumer price**.\n- **Farm-gate sales give brokers the power to exploit farmers**.\n- **Cooperatives provide price security and bulk transport**.\n- **Social commerce (WhatsApp + M-Pesa) eliminates middleman markups**."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Disadvantage of Farm-Gate Sales",
                        "content": {
                            "question": "What is the primary commercial disadvantage for a smallholder vegetable farmer who sells 100% of their harvest to brokers at the 'farm gate'?",
                            "options": [
                                "The farmer must pay high municipal transport taxes to the broker",
                                "The farmer receives significantly depressed prices because middlemen exploit the farmer's lack of on-farm storage and direct market access",
                                "The broker legally forces the farmer to change their soil texture",
                                "The CBC curriculum requires all farm-gate transactions to be conducted in foreign currency"
                            ],
                            "answer": "B",
                            "explanation": "Selling at the farm gate leaves the farmer with little to no bargaining power. Middlemen capitalize on the perishable nature of the crop, the farmer's lack of cold storage, and urgent need for cash to pay distress prices, capturing the majority of retail profit margins for themselves."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 4: Processing, Sorting, and Grading for the Market
        # =====================================================================
        {
            "unit_order": 4,
            "unit_name": "Processing, Sorting, and Grading for the Market",
            "unit_description": "Sorting (removing defects/rot) vs Grading (classifying by size/weight/color); Grade 1 (Premium), Grade 2 (Standard), Grade 3 (Utility); Ethylene gas and decay prevention; standardized transactions.",
            "lesson_title": "Post-Harvest Standardization: Produce Cleaning, Quality Sorting, and Market Grading Standards",
            "pages": [
                [
                    {
                        "type": "suggested_image",
                        "title": "Sorting and Packaging Fresh Tomato Fruits for Commercial Sale",
                        "content": {
                            "title": "Sorting and Packaging Fresh Tomato Fruits for Commercial Sale",
                            "caption": "Agricultural workers sorting, inspecting, and grading fresh tomatoes by size and maturity, demonstrating post-harvest quality standardization."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Sorting and Grading",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Differentiate between **Sorting (defect removal)** and **Grading (quality classification)**.",
                                "Analyze the characteristics of **Grade 1 (Premium), Grade 2 (Standard), and Grade 3 (Utility)** produce.",
                                "Explain how sorting **stops ethylene gas and fungal decay spread**.",
                                "Evaluate how grading enables **standardized telephone/digital transactions and premium pricing**."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Sorting vs Grading: Technical Distinctions",
                        "content": {
                            "title": "Preparing Produce for Premium Markets",
                            "text": "Delivering raw, un-sorted, dirty produce directly from the field signals poor quality and results in heavy price discounts:\n\n- **Sorting**: The physical separation of healthy, marketable produce from damaged, diseased, pest-eaten, or rotting items. Discarded culls are removed immediately.\n- **Grading**: Classifying sorted, clean, healthy produce into uniform categories or 'grades' based on specific commercial quality parameters (size, weight, shape, color, and maturity degree)."
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "The 3 Standard Agricultural Grades",
                        "content": {
                            "title": "Grade 1, Grade 2, and Grade 3 Standards",
                            "text": "1. **Grade 1 (Premium / Export Grade)**: Perfectly uniform size and shape, blemish-free skin, clean, and optimal maturity. Commands the highest retail price in high-end supermarkets, hotels, and export markets.\n2. **Grade 2 (Standard / Local Market Grade)**: Good quality but may have minor size variations or slight surface blemishes. Sells at standard prices in local open-air markets.\n3. **Grade 3 (Utility / Processing Grade)**: Irregular shapes, small size, or slight superficial insect damage, but completely edible. Sold at discounted prices for immediate home cooking, local kiosks, or processing into sauce/jam."
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Post-Harvest Cleaning, Sorting, and Grading Workflow",
                        "content": {
                            "title": "Post-Harvest Cleaning, Sorting, and Grading Workflow",
                            "caption": "Post-Harvest Standardization: Raw Field Harvest -> Cleaning (Wash & Dry) -> Sorting (Remove Rot & Culls) -> Grading (Classify by Size & Quality) -> Grade 1 Premium (High Price) | Grade 2 Standard | Grade 3 Utility."
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "Economic and Biological Benefits of Grading",
                        "content": {
                            "title": "Why Sorting and Grading Multiplies Farm Revenue",
                            "text": "- **Premium Pricing**: Customers gladly pay $50\\text{--}100\\%$ more for uniform, clean Grade 1 produce because it guarantees zero preparation waste.\n- **Standardized Digital Transactions**: Grading enables remote sales without physical inspection. A supermarket buyer can order *'20 crates of Grade 1 Tomatoes'* over the phone, trusting the exact size and quality they will receive.\n- **Ethylene Gas & Spoilage Prevention**: Rotting produce releases high concentrations of **ethylene gas** and fungal spores. Removing rotten culls during sorting prevents ethylene from accelerating the decay of surrounding healthy produce during transport!"
                        }
                    },
                    {
                        "type": "comparison_table",
                        "title": "Produce Grading Standards Matrix (Tomatoes)",
                        "content": {
                            "title": "Tomato Grading and Market Price Matrix",
                            "headers": ["Grade Classification", "Physical Quality Attributes", "Target Market Outlet", "Price Realization (KES/kg)"],
                            "rows": [
                                ["Grade 1 (Premium)", "Uniform large size (120-150g), blemish-free, firm red", "Supermarkets, high-end restaurants, export", "KES 100–120 / kg"],
                                ["Grade 2 (Standard)", "Medium size (80-110g), slight shape variation, firm", "Municipal open markets, neighborhood groceries", "KES 60–75 / kg"],
                                ["Grade 3 (Utility)", "Small / irregular shapes, minor skin scars, very ripe", "Local food kiosks, tomato jam / sauce processing", "KES 25–35 / kg"],
                                ["Un-Sorted Bulk Harvest", "Mixed sizes, dirty, containing 10% bruised/rotting fruits", "Distress sale to wholesale brokers at farm gate", "KES 35–45 / kg (Heavy loss)"]
                            ]
                        }
                    }
                ],
                [
                    {
                        "type": "mini_activity",
                        "title": "Field Practical: Produce Washing, Sorting, and Grading Practicum",
                        "content": {
                            "title": "Tomato / Potato Grading Lab",
                            "task": "1. Take a 10kg bucket of mixed raw produce.\n2. Wash in potable water and dry with clean towels.\n3. Sort out all damaged, bruised, or diseased items.\n4. Grade remaining produce into Grade 1 (Large/Uniform) and Grade 2 (Medium).\n5. Weigh each grade and compute total market value vs selling as un-sorted bulk.",
                            "materials": ["Produce Bucket", "Water", "Towels", "Weighing Scale", "Grading Trays"],
                            "safety": "Handle produce gently to avoid post-harvest bruising."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Core Summary: Sorting & Grading",
                        "content": {
                            "title": "Key Takeaways",
                            "text": "- **Sorting removes diseased culls; grading classifies by quality and size**.\n- **Grade 1 produce captures premium retail supermarket prices**.\n- **Sorting stops ethylene gas from rotting healthy surrounding produce**.\n- **Grading enables trust-based remote telephone and digital sales**."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Ethylene Gas and Spoilage Prevention",
                        "content": {
                            "question": "Why does sorting out and removing damaged or rotting tomatoes from a harvest crate before shipping to an urban market prevent rapid spoilage of the remaining healthy tomatoes?",
                            "options": [
                                "Rotten tomatoes consume all carbon dioxide in the delivery truck",
                                "Rotten tomatoes release high levels of ethylene gas and fungal spores that accelerate the ripening, softening, and decay of surrounding healthy tomatoes",
                                "Healthy tomatoes absorb water from rotten ones and burst",
                                "Sorting increases the soil fertility of the urban market"
                            ],
                            "answer": "B",
                            "explanation": "Decaying plant tissue produces high levels of ethylene gas (the natural ripening hormone) and sheds fungal mold spores. In an enclosed container, ethylene gas triggers rapid senescence, softening, and rotting in all adjacent healthy produce."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 5: Market Information & Price Fluctuations
        # =====================================================================
        {
            "unit_order": 5,
            "unit_name": "Market Information & Price Fluctuations",
            "unit_description": "Market intelligence sources (Digital SMS, MoA bulletins, vernacular radio); Supply and Demand principles; Seasonal harvest gluts vs off-season scarcity; Window optimization (irrigation & hermetic storage).",
            "lesson_title": "Agribusiness Market Dynamics: Information Systems, Seasonal Price Gluts, and Supply Elasticity",
            "pages": [
                [
                    {
                        "type": "suggested_image",
                        "title": "Fresh Produce Piled at a Bustling Commercial Market Stall",
                        "content": {
                            "title": "Fresh Produce Piled at a Bustling Commercial Market Stall",
                            "caption": "Bustling agricultural marketplace with produce piled high, demonstrating seasonal market supply, consumer demand elasticity, and price dynamics."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Market Information & Prices",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Identify sources of **real-time agricultural market information** in Kenya.",
                                "Analyze the economic principles of **Supply and Demand** governing farm prices.",
                                "Explain the causes of **Seasonal Market Gluts vs. Off-Season Scarcity**.",
                                "Deploy **off-season irrigation and hermetic storage** to capture high selling windows."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Sourcing Real-Time Agricultural Market Intelligence",
                        "content": {
                            "title": "Empowering Farmers with Market Data",
                            "text": "**Market information** encompasses real-time data regarding prevailing commodity prices, supply volumes in wholesale markets, consumer demand trends, and buyer quality specifications:\n\n- **Digital SMS Price Platforms (e.g., M-Farm, KALRO apps)**: Transmits daily wholesale prices across Nairobi, Mombasa, Kisumu, and Eldoret markets.\n- **Government Commodity Bulletins**: Weekly agricultural updates published by the Ministry of Agriculture.\n- **Vernacular Radio & Television**: Broadcasts daily livestock and grain market prices.\n- **Direct Market Surveys**: Visiting local traders and wholesalers to gauge buying interest."
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "The Law of Supply and Demand in Agriculture",
                        "content": {
                            "title": "Why Agricultural Prices Fluctuate Seasonally",
                            "text": "- **Supply and Demand Law**: When commodity supply is high and demand is constant $\\rightarrow$ prices crash. When supply is low and demand is high $\\rightarrow$ prices soar.\n- **Seasonal Harvest Glut**: In rain-fed farming, all farmers plant at the same time and harvest simultaneously. Local markets are flooded with massive excess supply (**glut**), causing prices to collapse (e.g., cabbages selling for KES 10/head).\n- **Off-Season Scarcity**: Months after harvest, rain-fed production ceases and farm stocks run out (**scarcity**), driving prices up by $300\\text{--}500\\%$ (e.g., cabbages selling for KES 60/head)!"
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Seasonal Agricultural Price Fluctuations: Harvest Glut vs Off-Season Scarcity",
                        "content": {
                            "title": "Seasonal Agricultural Price Fluctuations: Harvest Glut vs Off-Season Scarcity",
                            "caption": "Seasonal Price Curve: Rain-Fed Harvest Peak (Excess Supply, Market Glut, Price Crashes to KES 10) vs Dry Off-Season (Zero Rain Production, Severe Scarcity, Price Spikes to KES 60!)."
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "Strategies to Beat the Seasonal Glut",
                        "content": {
                            "title": "Capturing Premium Off-Season Selling Windows",
                            "text": "Smart agribusiness managers do not harvest when everyone else is harvesting:\n1. **Off-Season Staggered Production**: Using drip irrigation and greenhouses to plant during dry months, timing harvest for the exact off-season window when open-market supplies are dry.\n2. **Hermetic Grain Storage**: Storing dried cereals and pulses in multi-layer hermetic bags (PICS bags) during harvest price crashes, waiting to sell 4–6 months later when grain prices double.\n3. **Value Addition & Preservation**: Processing perishable surpluses into shelf-stable sauces, jams, flours, or dried fruit slices."
                        }
                    },
                    {
                        "type": "comparison_table",
                        "title": "Harvest Glut vs Off-Season Price Behavior (Nyandarua Cabbages)",
                        "content": {
                            "title": "Seasonal Price Shift Analysis Model",
                            "headers": ["Season / Month", "Market Condition", "Average Price / Bag (KES)", "Strategic Farm Action"],
                            "rows": [
                                ["January (Long Rain Harvest)", "Massive Supply Glut (Overproduction)", "KES 500 / bag", "Process into sauerkraut / feed to livestock / store"],
                                ["April (Inter-season)", "Moderate Supply", "KES 1,200 / bag", "Begin phased release from storage"],
                                ["July (Dry Off-Season)", "Severe Scarcity (Dry farms empty)", "KES 2,500 / bag (+400%!)", "Harvest irrigated crop & sell stored inventory"]
                            ]
                        }
                    }
                ],
                [
                    {
                        "type": "mini_activity",
                        "title": "Economic Practical: Seasonal Price Trend Analysis Lab",
                        "content": {
                            "title": "Price Trend Analysis Practicum",
                            "task": "1. Review a 12-month historical price chart for tomatoes in your local county.\n2. Identify the 2 months with the lowest prices (glut) and the 2 months with the highest prices (scarcity).\n3. Calculate the planting date required to harvest during the peak scarcity window (assuming a 75-day maturity crop).",
                            "materials": ["Price Trend Handout", "Calendar", "Pen"],
                            "safety": "Ensure accurate agronomic crop cycle calculations."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Core Summary: Market Dynamics & Prices",
                        "content": {
                            "title": "Key Takeaways",
                            "text": "- **Market intelligence via SMS platforms reveals current urban prices**.\n- **Harvest gluts crash farm-gate prices due to sudden oversupply**.\n- **Off-season scarcity drives prices up by 300–500%**.\n- **Drip irrigation and hermetic storage unlock peak selling windows**."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Cause of Off-Season Price Spikes",
                        "content": {
                            "question": "During the peak harvesting month of January, a bag of cabbages in Nyandarua sells for KES 500. In July, during the dry off-season, the same bag of cabbages sells for KES 2,500. What economic principle explains this dramatic price surge?",
                            "options": [
                                "Extreme government price setting regulations",
                                "The law of supply and demand, where dry off-season crop scarcity drastically reduces market supply while consumer demand remains constant, driving prices up",
                                "Cabbages grow heavier and larger during cold July nights",
                                "July temperatures alter the physical soil texture class"
                            ],
                            "answer": "B",
                            "explanation": "Agricultural prices are dictated by the laws of supply and demand. In January, rain-fed farms harvest simultaneously, flooding the market and crashing prices. In dry July, rain-fed production ceases, creating acute scarcity that drives prices up for farmers who utilize irrigation."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 6: Formulating a Marketing Strategy, Pitching & Topic Review
        # =====================================================================
        {
            "unit_order": 6,
            "unit_name": "Formulating a Marketing Strategy, Pitching & Topic Review",
            "unit_description": "Strategic marketing plan steps (Customer identification, Competitor differentiation, Budget); The 3-minute sales pitch (Hook, Solution, Economics & Quality, Call to Action); Section A & Section B Practical Scenario (500kg Onion Marketing Case); 8 Summative MCQs.",
            "lesson_title": "Agribusiness Sales Mastery: Marketing Strategy Plans, Persuasive Pitching, and Summative Review",
            "pages": [
                [
                    {
                        "type": "suggested_image",
                        "title": "Commercial Farm Shop Displaying Fresh Packaged Farm Goods",
                        "content": {
                            "title": "Commercial Farm Shop Displaying Fresh Packaged Farm Goods",
                            "caption": "A clean, branded farm retail shop displaying fresh vegetables and value-added agricultural foods, showing strategic marketing and direct-to-consumer sales."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Strategy, Pitching & Review",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Formulate a complete **Agribusiness Marketing Plan integrating the 4 Ps**.",
                                "Deliver a persuasive **3-minute sales pitch using the 4-part structure (Hook, Solution, Economics, Call to Action)**.",
                                "Synthesize the **complete 6-lesson Agricultural Marketing Framework**.",
                                "Complete the comprehensive **Summative Topic Assessment**."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "What is an Agricultural Marketing Strategy?",
                        "content": {
                            "title": "The Strategic Blueprint for Farm Profitability",
                            "text": "An **agricultural marketing strategy** is a comprehensive written roadmap outlining how an agribusiness will identify, attract, and satisfy target customers profitably:\n\n1. **Target Customer Profiling**: Define exact buyers (e.g., high-income estate households, local school boarding canteens, wholesale millers).\n2. **Competitor Analysis & Differentiation**: Determine what sets your farm apart (e.g., washed pre-cut veggies, certified organic, free doorstep delivery).\n3. **4 Ps Integration**: Harmonize Product specifications, Pricing tactics, Distribution outlets, and Promotion channels.\n4. **Marketing Budget**: Allocate funds for packaging bags, branding labels, transport fuel, and social media promotions."
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "The 3-Minute Agribusiness Sales Pitch",
                        "content": {
                            "title": "Pitching to Institutional Buyers and Supermarkets",
                            "text": "A **sales pitch** is a concise, persuasive presentation delivered to supermarket buyers, school caterers, or restaurant managers to secure forward supply contracts. It follows a 4-part logical arc:\n1. **The Hook**: Grab attention with a compelling market reality (e.g., *'Did you know that over 40% of spinach sold in this estate is wilted and unwashed, wasting 2 hours of your kitchen prep daily?'*).\n2. **The Solution (Unique Value Proposition)**: Present your farm's offering (*'We deliver washed, graded, sterile-packed spinach daily...'*).\n3. **The Economics & Reliability**: Detail your competitive bulk price, payment terms, and consistent daily delivery volume.\n4. **The Call to Action**: Propose a free 5kg trial sample or an initial 2-week supply contract!"
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Master Agricultural Produce Marketing & Sales Strategy Lifecycle",
                        "content": {
                            "title": "Master Agricultural Produce Marketing & Sales Strategy Lifecycle",
                            "caption": "Master Marketing Strategy: 1 Market Intelligence -> 2 Post-Harvest Sorting & Grading -> 3 Marketing Mix (The 4 Ps) -> 4 Channel Selection (Direct / Digital) -> 5 Sales Pitching & Contracts -> 6 Profitable Distribution."
                        }
                    }
                ],
                [
                    {
                        "type": "comparison_table",
                        "title": "Weak vs Winning Agribusiness Sales Pitch Statements",
                        "content": {
                            "title": "Sales Pitch Architecture Comparison",
                            "headers": ["Pitch Component", "Weak / Ineffective Approach", "Winning Value-Driven Approach (Agribusiness Champion)"],
                            "rows": [
                                ["The Hook", "'I am a farmer and I have some cabbages to sell if you want.'", "'Your restaurant spends KES 15,000 monthly on vegetable sorting waste and kitchen prep delays.'"],
                                ["The Solution", "'My cabbages are normal cabbages from my shamba.'", "'We deliver Grade 1, washed, core-trimmed cabbages in sterile 10kg crates, ready for instant shredding.'"],
                                ["Economics", "'I will sell at whatever price you give me.'", "'At KES 30/head with zero waste, you reduce your daily vegetable food costs by 22% guaranteed.'"],
                                ["Call to Action", "'Call me sometime if you need cabbages.'", "'Allow us to deliver a complimentary 10kg sample crate tomorrow at 7:00 AM for your chef to test.'"]
                            ]
                        }
                    }
                ],
                [
                    {
                        "type": "mini_activity",
                        "title": "Performance Task: The '500kg School Onion Marketing Challenge'",
                        "content": {
                            "title": "Onion Marketing Channel Decision Practicum",
                            "task": "A school project harvested 500kg red onions (Cost of production = KES 40/kg):\n- Option 1 (Open-market bulk broker): Sell all 500kg un-sorted at KES 50/kg instantly.\n- Option 2 (Supermarket supply): Spend KES 5,000 on net bags and transport; sort out 10% (50kg) damaged culls sold to kiosks at KES 20/kg, and sell 450kg Grade 1 onions to supermarket at KES 110/kg.\n1. Compute Net Profit for Option 1.\n2. Compute Net Profit for Option 2.\n3. Write a 2-sentence recommendation on which channel the school should select.",
                            "materials": ["Case Handout", "Calculator", "Pen"],
                            "safety": "Ensure exact mathematical cost subtraction."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Core Summary: Strategy & Pitching",
                        "content": {
                            "title": "Key Takeaways",
                            "text": "- **Never plant without a defined, verified marketing strategy**.\n- **Structure sales pitches with Hook, Solution, Economics, and Call to Action**.\n- **Emphasize how your graded produce solves buyer problems (saves labor & waste)**.\n- **Sorting and grading into premium channels drastically outperforms bulk selling**."
                        }
                    }
                ],
                # Pages 5 to 8: 8 Summative Assessment MCQs
                [
                    {
                        "type": "knowledge_check",
                        "title": "Summative MCQ 1: Types of Economic Utility in Marketing",
                        "content": {
                            "question": "A maize farmer in Trans-Nzoia dries his grain to 12% moisture, packages it in hermetic PICS bags, and stores it in a secure warehouse for six months, selling it in July when market prices double. What type of economic utility has this farmer primarily created?",
                            "options": [
                                "Form Utility",
                                "Place Utility",
                                "Time Utility",
                                "Possession Utility"
                            ],
                            "answer": "C",
                            "explanation": "Time Utility is created by safely preserving and storing agricultural commodities after harvest, delaying their sale until a future time when market supply has dropped and prices have risen."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Summative MCQ 2: The 4 Ps Marketing Mix Elements",
                        "content": {
                            "question": "Which of the following correctly pairs an element of the agricultural marketing mix with its practical agribusiness application?",
                            "options": [
                                "Place -> Deciding to spray pesticides with a boom sprayer",
                                "Product -> Sorting and packaging uniform, clean Grade 1 eggs in 15-egg paper cartons",
                                "Promotion -> Applying DAP fertilizer during crop planting",
                                "Price -> Constructing a concrete store for farm tractors"
                            ],
                            "answer": "B",
                            "explanation": "In the marketing mix, 'Product' refers to the physical commodity specifications, quality standards, hygiene, sorting, and packaging designed to appeal directly to target consumers."
                        }
                    }
                ],
                [
                    {
                        "type": "knowledge_check",
                        "title": "Summative MCQ 3: Exploitation in Farm-Gate Selling",
                        "content": {
                            "question": "Why do smallholder farmers who sell fresh horticultural produce exclusively to traveling brokers at the 'farm gate' consistently receive the lowest profit margins?",
                            "options": [
                                "Brokers are legally required to deduct 80% government taxes from farmers",
                                "Brokers take advantage of the farmer's lack of on-farm cold storage, lack of transport, and urgent need for cash, forcing distress prices",
                                "Farm-gate sales automatically reduce the nutritional quality of the vegetables",
                                "The government sets fixed minimum farm-gate prices that are lower than town prices"
                            ],
                            "answer": "B",
                            "explanation": "Farm-gate sales give brokers the upper hand. Knowing the farmer has no cold storage to keep perishable produce and lacks independent transport to urban markets, brokers negotiate aggressively, paying depressed farm-gate prices and capturing the retail profits."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Summative MCQ 4: Distinction Between Sorting and Grading",
                        "content": {
                            "question": "What is the primary technical difference between 'sorting' and 'grading' fresh agricultural produce before market delivery?",
                            "options": [
                                "Sorting is done by machines while grading is done by hand",
                                "Sorting separates healthy marketable produce from damaged, diseased, or rotten items, whereas grading classifies healthy produce into uniform quality categories based on size, weight, and color",
                                "Sorting is done before planting, while grading is done after cooking",
                                "Sorting changes the crop species, while grading changes the soil type"
                            ],
                            "answer": "B",
                            "explanation": "Sorting is the preliminary sanitation step that removes all defective, diseased, and rotting culls. Grading is the subsequent quality classification step that groups the remaining healthy produce into uniform classes (Grade 1, Grade 2, Grade 3) by size, weight, and maturity."
                        }
                    }
                ],
                [
                    {
                        "type": "knowledge_check",
                        "title": "Summative MCQ 5: Biological Hazard of Rotting Produce in Transport",
                        "content": {
                            "question": "What biological agent released by damaged and decaying fruits accelerates the softening, over-ripening, and breakdown of surrounding healthy fruits during transit?",
                            "options": [
                                "Nitrogen gas",
                                "Ethylene gas and fungal mold spores",
                                "Chlorophyll enzyme",
                                "Carbon monoxide"
                            ],
                            "answer": "B",
                            "explanation": "Decaying plant tissues produce high concentrations of ethylene gas (the gaseous ripening hormone) along with fungal spores. In transit crates, ethylene gas triggers rapid senescence and rotting in all adjacent healthy produce."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Summative MCQ 6: Seasonal Agricultural Price Behavior (Glut vs Scarcity)",
                        "content": {
                            "question": "Why do tomato prices crash to distress levels (e.g., KES 15/kg) immediately after the long rainy season, but surge to KES 100/kg during the dry season?",
                            "options": [
                                "Tomatoes become toxic during the rainy season",
                                "Rain-fed farmers harvest simultaneously, creating a seasonal market glut where supply exceeds demand, crashing prices, while dry-season production halts, creating severe scarcity",
                                "Supermarkets close down during rainy seasons",
                                "Consumers eat 10 times more tomatoes during dry seasons"
                            ],
                            "answer": "B",
                            "explanation": "Because most smallholders rely on rain-fed farming, harvests coincide, creating a sudden market oversupply (glut) that crashes prices. In the dry season, supply collapses because few farmers irrigate, driving prices up."
                        }
                    }
                ],
                [
                    {
                        "type": "knowledge_check",
                        "title": "Summative MCQ 7: Unique Value Proposition in Agribusiness Pitching",
                        "content": {
                            "question": "An agribusiness entrepreneur is pitching her farm's washed, graded, and bagged potatoes to a high-end restaurant manager. Which of the following statements represents the most effective 'unique value proposition' for her pitch?",
                            "options": [
                                "Our potatoes are grown on soil with a balanced loam texture and prepared using standard hand jembes",
                                "We deliver unwashed potatoes straight from the field with mud on them to prove they are natural",
                                "We deliver washed, graded, uniform-sized potatoes packed in sterile 10kg bags, eliminating 100% of your kitchen's sorting and washing labor costs",
                                "Our potatoes are guaranteed to cure all livestock diseases"
                            ],
                            "answer": "C",
                            "explanation": "A powerful unique value proposition clearly explains how your product solves a specific operational pain point for the buyer. Delivering washed, graded potatoes eliminates sorting time and kitchen labor for the restaurant, representing a strong commercial benefit."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Summative MCQ 8: Net Profit Calculation in Produce Marketing",
                        "content": {
                            "question": "A school farm harvested 500kg onions (Cost of Production = KES 20,000). If they sell the entire harvest to a farm-gate broker at KES 50/kg, what is their Net Profit compared to selling 450kg Grade 1 to a supermarket at KES 110/kg and 50kg culls at KES 20/kg (with KES 5,000 packaging/transport costs)?",
                            "options": [
                                "Broker Net Profit = KES 5,000; Supermarket Net Profit = KES 25,500 (+410% Higher Profit!)",
                                "Broker Net Profit = KES 25,000; Supermarket Net Profit = KES 5,000",
                                "Both options produce exactly the same profit of KES 10,000",
                                "Both options result in a net financial loss"
                            ],
                            "answer": "A",
                            "explanation": "Broker Option: Revenue = 500 x 50 = KES 25,000. Net Profit = 25,000 - 20,000 = KES 5,000. Supermarket Option: Revenue = (450 x 110) + (50 x 20) = 49,500 + 1,000 = KES 50,500. Total Costs = 20,000 (prod) + 5,000 (pack/transport) = KES 25,000. Net Profit = 50,500 - 25,000 = KES 25,500! (Over 5x higher profit!)."
                        }
                    }
                ],
                # Page 9: Capstone Summary
                [
                    {
                        "type": "summary",
                        "title": "Topic 16 Capstone Summary: Marketing Agricultural Produce Mastery",
                        "content": {
                            "title": "Mastery Overview: Grade 10 Agricultural Produce Marketing",
                            "text": "Congratulations on mastering **Topic 16: Marketing Agricultural Produce**!\n\nYou have mastered:\n- **Marketing vs Selling**: Customer-centric value creation vs disposing of crops at distress prices.\n- **The 4 Economic Utilities**: Form (processing), Place (transport from surplus to deficit), Time (hermetic storage for off-season sales), and Possession (digital M-Pesa & delivery).\n- **The Marketing Mix (The 4 Ps)**: Product quality & packaging, competitive Price strategies, Place distribution channels, and Promotion via social commerce and trade fairs.\n- **Marketing Channels & Outlets**: Direct zero-level channels vs multi-level middlemen; avoiding farm-gate exploitation; harnessing WhatsApp estate groups and digital agri-commerce.\n- **Post-Harvest Sorting & Grading**: Removing ethylene-releasing culls; Grade 1 (Premium), Grade 2 (Standard), Grade 3 (Utility); capturing premium supermarket prices.\n- **Market Information & Price Dynamics**: Utilizing SMS price platforms; analyzing supply and demand elasticity; beating seasonal harvest gluts via drip irrigation and off-season scheduling.\n- **Marketing Strategy & Pitching**: Formulating 4-part sales pitches (Hook, Solution, Economics, Call to Action) that secure profitable institutional contracts."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Topic 16 Final Takeaway",
                        "content": {
                            "title": "The Agricultural Marketing Maxim",
                            "text": "Never produce a single crop without a verified market strategy. Sort and grade your harvest, bypass predatory middlemen through direct and digital channels, time your sales to avoid harvest gluts, and communicate your unique value proposition. Marketing turns harvested commodities into sustainable agribusiness wealth."
                        }
                    }
                ]
            ]
        }
    ]

@transaction.atomic
def ingest_grade10_topic16(replace=False):
    """Executes the complete production ingestion of Grade 10 Agriculture Topic 16: Marketing Agricultural Produce."""
    print("=" * 80)
    print("STARTING INGESTION: CBC Grade 10 Agriculture — Topic 16: Marketing Agricultural Produce")
    print("=" * 80)

    curriculum = Curriculum.objects.filter(name__iexact="CBC").first()
    grade = Grade.objects.filter(curriculum=curriculum, name__icontains="10").first()
    subject = Subject.objects.filter(grade=grade, name__iexact="Agriculture").first()

    assert curriculum and grade and subject, "Curriculum/Grade/Subject not found!"

    topic_name = "Marketing Agricultural Produce"
    topic = Topic.objects.filter(subject=subject, name=topic_name).first()
    if not topic:
        topic = Topic.objects.create(
            subject=subject,
            name=topic_name,
            description="Comprehensive vocational and strategic training in marketing agricultural produce: marketing vs selling, 4 economic utilities (form, place, time, possession), the 4 Ps marketing mix (product, price, place, promotion), marketing channels and digital e-commerce, post-harvest sorting and grading standards, market intelligence and seasonal price dynamics (gluts vs scarcity), and agribusiness sales pitching.",
            order=16
        )
        print(f"Created Topic 16: {topic.name} (ID: {topic.id})")
    else:
        topic.order = 16
        topic.description = "Comprehensive vocational and strategic training in marketing agricultural produce: marketing vs selling, 4 economic utilities (form, place, time, possession), the 4 Ps marketing mix (product, price, place, promotion), marketing channels and digital e-commerce, post-harvest sorting and grading standards, market intelligence and seasonal price dynamics (gluts vs scarcity), and agribusiness sales pitching."
        topic.save()
        print(f"Resolved Topic 16: {topic.name} (ID: {topic.id})")

    if replace:
        print("Flag --replace active: Clearing existing LearningUnits and Lessons for Topic 16...")
        topic.learning_units.all().delete()
        topic.lessons.all().delete()

    curriculum_data = build_topic16_curriculum()
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
                    "topic_order": 16,
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
                    block_id=f"g10_agri_t16_u{u_order}_p{page_idx}_b{comp_idx}",
                    block_type=b_type,
                    component_type=b_type,
                    title=b_title,
                    content=b_content,
                    order=block_order_counter,
                    page_number=page_idx,
                    component_order=comp_idx,
                    page_title=b_title if comp_idx == 1 else None,
                    metadata={"topic_order": 16, "unit_order": u_order, "page": page_idx}
                )
                block_order_counter += 1
                total_blocks += 1

        print(f"  Ingested Unit {u_order}: {u_name} -> Lesson '{l_title}' ({len(pages)} Pages, {block_order_counter - 1} Blocks)")

    print("=" * 80)
    print(f"INGESTION COMPLETE: Topic 16 '{topic.name}'")
    print(f"  Total Units:   {total_units}")
    print(f"  Total Lessons: {total_lessons}")
    print(f"  Total Pages:   {total_pages}")
    print(f"  Total Blocks:  {total_blocks}")
    print("=" * 80)

if __name__ == "__main__":
    replace_flag = "--replace" in sys.argv
    ingest_grade10_topic16(replace=replace_flag)
