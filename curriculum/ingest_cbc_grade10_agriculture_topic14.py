"""
VLearn CBC Grade 10 Agriculture — Topic 14: Product Processing and Value Addition
Production Ingestion Engine (Deep Senior Secondary Pedagogical Edition)

Curriculum: CBC (ID: 5)
Grade: Grade 10 (ID: 5, Level: 10)
Subject: Agriculture
Topic: Product Processing and Value Addition (Topic Order: 14)

Decomposed into 12 Learning Units & 12 Published Lessons:
  1. Introduction to Product Processing and Value Addition (4 Pages, 8 Blocks)
  2. Post-Harvest Loss Mitigation (4 Pages, 8 Blocks)
  3. Nutritional and Food Security Impact of Value Addition (4 Pages, 8 Blocks)
  4. Value-Addition Methods (4 Pages, 9 Blocks)
  5. Plant Processing Practical I - Banana and Potato Crisps (4 Pages, 8 Blocks)
  6. Plant Processing Practical II - Vegetable Preservation & Sauces (4 Pages, 9 Blocks)
  7. Plant Processing Practical III - Fruit Juice Processing (4 Pages, 8 Blocks)
  8. Plant Processing Practical IV - Flour Processing (4 Pages, 9 Blocks)
  9. Animal Origin Processing I - Milk and Fermented Dairy (4 Pages, 9 Blocks)
  10. Animal Origin Processing II - Honey Refining and Bottling (4 Pages, 8 Blocks)
  11. Animal Origin Processing III - Hides and Skins Preserving (4 Pages, 8 Blocks)
  12. Packaging, Branding, Labeling, and Review (8 Pages, 17 Blocks)
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

def build_topic14_curriculum():
    """Returns the comprehensive pedagogical page and block structure for Grade 10 Topic 14: Product Processing and Value Addition."""
    return [
        # =====================================================================
        # LESSON 1: Introduction to Product Processing and Value Addition
        # =====================================================================
        {
            "unit_order": 1,
            "unit_name": "Introduction to Product Processing and Value Addition",
            "unit_description": "Definitions of product processing vs value addition; economic margins; chef/artisan real-world analogies.",
            "lesson_title": "Agribusiness Transformation: Foundations of Product Processing and Value Addition",
            "pages": [
                [
                    {
                        "type": "suggested_image",
                        "title": "Display of Value-Added Preserves, Jams, and Refined Honey Products",
                        "content": {
                            "title": "Display of Value-Added Preserves, Jams, and Refined Honey Products",
                            "caption": "A commercial display of value-added agricultural foods—jams, preserves, sauces, and bottled honey—illustrating product transformation from raw produce."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Processing & Value Addition",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Define **agricultural product processing and value addition** in precise technical terms.",
                                "Differentiate between physical **processing** and commercial **value addition**.",
                                "Analyze the **economic value-addition ladder** using the Chef and Artisan analogies.",
                                "Evaluate how value addition shifts farmers from **price-takers to price-setters**."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Defining Product Processing",
                        "content": {
                            "title": "Changing the Physical Form of Farm Produce",
                            "text": "**Product processing** refers to any mechanical, thermal, chemical, or biological operation that alters the raw physical state of harvested agricultural produce:\n\n- **Physical & Chemical Shifts**: Taking harvested maize cobs and milling dry kernels into fine flour, or peeling and slicing raw potatoes.\n- **Primary Purpose**: Processing makes raw commodities edible, digestible, transportable, and physically stable against rapid decay. It is the necessary foundation for food preservation."
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "Defining Value Addition",
                        "content": {
                            "title": "Maximizing Economic Worth and Utility",
                            "text": "**Value addition** is a strategic commercial and agronomic discipline:\n\n- **Economic Enhancement**: Any deliberate process, packaging, formulation, or branding that substantially **increases the market price, shelf-life, and consumer utility** of a farm product.\n- **Example**: Converting raw, loose farm-gate cow milk (selling at KES 40/L) into pasteurized, cultured strawberry yoghurt packaged in 250ml branded bottles selling at KES 80 each (yielding KES 320/L equivalent!).\n- **The Economic Shift**: Transforms raw, low-margin commodities into premium consumer goods, capturing retail profit margins."
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Raw Commodity vs Value-Added Product Economic Ladder",
                        "content": {
                            "title": "Raw Commodity vs Value-Added Product Economic Ladder",
                            "caption": "Economic ladder: 1 Raw Commodity (Low price, high perishability, farm-gate price taker) -> 2 Basic Processing (Milled/Cleaned, moderate shelf-life) -> 3 Value Addition (Branded, formulated, packaged, 300% profit boost)."
                        }
                    }
                ],
                [
                    {
                        "type": "comparison_table",
                        "title": "Processing vs Value Addition Comparison",
                        "content": {
                            "title": "Processing vs Value Addition Comparison Matrix",
                            "headers": ["Dimension", "Product Processing", "Value Addition", "Real-World Farm Example"],
                            "rows": [
                                ["Primary Focus", "Altering physical state & edibility", "Maximizing market price & consumer utility", "Milling maize vs Fortified baby porridge"],
                                ["Shelf-Life Impact", "Moderate extension (weeks)", "Significant extension (months to years)", "Sliced potatoes vs Sealed crisps"],
                                ["Profit Margin", "Low to moderate cost-plus margin", "High premium retail margin (+200–400%)", "Raw milk (KES 40/L) vs Yoghurt (KES 320/L)"],
                                ["Market Positioning", "Bulk raw commodity trader", "Branded consumer retail goods", "Loose farm tomatoes vs Branded tomato sauce"]
                            ]
                        }
                    }
                ],
                [
                    {
                        "type": "mini_activity",
                        "title": "Field Practical: Market Shelf Survey of Raw vs Processed Produce",
                        "content": {
                            "title": "Value Addition Price Survey Practicum",
                            "task": "1. Visit a local market or supermarket.\n2. Record the price of 1kg of raw groundnuts vs 1kg equivalent of packaged peanut butter.\n3. Record the price of 1kg raw cassava vs 1kg packaged cassava flour.\n4. Calculate the percentage price multiplier generated by value addition.",
                            "materials": ["Notebook", "Pen", "Calculator"],
                            "safety": "Follow school safety rules during market visits."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Core Summary: Processing & Value Addition",
                        "content": {
                            "title": "Key Takeaways",
                            "text": "- **Processing changes physical form**; **value addition maximizes market value**.\n- **Value addition turns price-takers into price-setters**.\n- **Raw commodities suffer rapid decay**; **value addition extends shelf-life**.\n- **Packaging and branding capture retail profits** for smallholder farmers."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Processing vs Value Addition",
                        "content": {
                            "question": "Which of the following scenarios best demonstrates the comprehensive economic concept of agricultural value addition?",
                            "options": [
                                "Leaving harvested mangoes piled under a tree in the sun until a middleman arrives",
                                "Sorting, washing, peeling, solar-drying, and packaging ripe mango slices in vacuum-sealed branded pouches for export",
                                "Selling raw unwashed potatoes straight out of the field at distress farm-gate prices",
                                "Pouring warm raw milk into an open plastic bucket for roadside sale"
                            ],
                            "answer": "B",
                            "explanation": "Value addition encompasses deliberate quality sorting, peeling, dehydrating, and branded packaging to transform perishable raw mangoes into shelf-stable, high-value consumer snacks that command premium retail market prices."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 2: Post-Harvest Loss Mitigation
        # =====================================================================
        {
            "unit_order": 2,
            "unit_name": "Post-Harvest Loss Mitigation",
            "unit_description": "Perishability dynamics (80–90% moisture, enzymatic decay); 30–40% post-harvest loss in Kenya; 4 bottlenecks (cold chain, transport, market gluts, moisture); processing as a defensive shield.",
            "lesson_title": "Post-Harvest Economics: Biological Spoilage Dynamics and Processing as a Defensive Shield",
            "pages": [
                [
                    {
                        "type": "suggested_image",
                        "title": "Freshly Harvested Tomatoes in Crates Facing Post-Harvest Spoilage Risks",
                        "content": {
                            "title": "Freshly Harvested Tomatoes in Crates Facing Post-Harvest Spoilage Risks",
                            "caption": "Fresh tomatoes stacked in field crates, highlighting high moisture content, rapid respiration, and vulnerability to market glut price crashes."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Post-Harvest Loss Mitigation",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Analyze the **biological causes of post-harvest perishability (moisture, respiration, enzymes)**.",
                                "Quantify the **economic impact of 30–40% post-harvest losses in Kenya**.",
                                "Evaluate 4 infrastructure bottlenecks: **Cold chain absence, transport damage, market gluts, and high moisture**.",
                                "Deploy **food processing as an active defensive barrier against food waste**."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The Perishability Challenge in Horticultural Crops",
                        "content": {
                            "title": "Living Tissue Breakdown After Harvest",
                            "text": "Harvested crops (tomatoes, kales, mangoes, milk) remain living biological tissues:\n\n- **High Moisture Content**: Fresh fruits and vegetables contain **80% to 92% free water**, providing an ideal medium for bacteria and fungal molds.\n- **Active Respiration & Enzymatic Decay**: Plant tissues continue respiring, consuming their own sugars and producing heat. Internal enzymes break down cell walls, causing fruit softening, browning, and rotting.\n- **Post-Harvest Loss Magnitude**: In Kenya, smallholders lose **30% to 40%** of total harvested produce before reaching consumers!"
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "4 Major Post-Harvest Loss Bottlenecks",
                        "content": {
                            "title": "Why Produce Spoils on the Farm",
                            "text": "1. **Lack of Cold Storage**: Absence of on-farm refrigeration allows ambient tropical temperatures ($25\\text{--}35^\\circ\\text{C}$) to accelerate bacterial multiplication.\n2. **Rough Transport Infrastructure**: Bumpy rural roads and overloaded wooden crates crush bottom layers of tomatoes, creating bruises where rot pathogens enter.\n3. **Seasonal Market Gluts**: Synchronized harvesting leads to flooded local markets, causing prices to crash to distress levels ($\text{KES }10/\text{kg}$), forcing farmers to abandon unsold rotting crops.\n4. **Inadequate Cereal Drying**: Harvesting maize in rainy seasons leads to damp storage ($>15\%$ moisture), triggering lethal **aflatoxin** mold contamination (*Aspergillus flavus*)."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Processing as a Defensive Shield",
                        "content": {
                            "title": "Defeating Decay Organisms",
                            "text": "Processing eliminates the environmental conditions microbes require to survive:\n- **Drying**: Lowers water activity below **12%**, halting all microbial metabolism.\n- **Thermal Pasteurization**: Kills vegetative bacteria and denatures self-digesting plant enzymes.\n- **Fermentation & Acidification**: Drops pH below **4.6**, creating an acidic barrier against pathogens.\n- *Result*: Farmers bypass market gluts, store surplus food safely for months, and sell when market supply drops and prices soar!"
                        }
                    }
                ],
                [
                    {
                        "type": "comparison_table",
                        "title": "Post-Harvest Loss Drivers vs Processing Solutions",
                        "content": {
                            "title": "Post-Harvest Mitigation Matrix",
                            "headers": ["Loss Factor", "Underlying Biological Cause", "Vulnerable Farm Commodity", "Target Processing Solution"],
                            "rows": [
                                ["Market Glut Price Crash", "Overproduction during harvest peak", "Fresh Tomatoes, Cabbages", "Processing into Tomato Sauce / Sauerkraut"],
                                ["Rapid Fungal Rot", "High internal moisture (85–90%)", "Fresh Mangoes, Bananas", "Solar dehydration into dried fruit slices"],
                                ["Aflatoxin Mold Toxin", "High grain storage moisture (>14%)", "Maize, Groundnuts, Sorghum", "Solar drying to <12% moisture & sealed silos"],
                                ["Rapid Bacterial Souring", "Lactose-consuming wild bacteria", "Fresh Raw Cow Milk", "Pasteurization & Lactic fermentation (Mala/Yoghurt)"],
                                ["Post-Harvest Root Rot", "Enzymatic decay within 48 hours", "Fresh Cassava & Sweet Potatoes", "Chipping, drying, and milling into root flour"]
                            ]
                        }
                    }
                ],
                [
                    {
                        "type": "mini_activity",
                        "title": "Simulation Practical: Fresh vs Preserved Tomato Spoilage Lab",
                        "content": {
                            "title": "Biological Decay Observation Practicum",
                            "task": "1. Place a whole ripe fresh tomato on an open shelf.\n2. Slice, boil for 5 minutes, lightly salt, and seal a second tomato in a clean glass jar.\n3. Observe and document both samples over 5 days for microbial mold, softening, and smell.",
                            "materials": ["2 Ripe Tomatoes", "Glass Jar", "Salt", "Pan & Heat Source"],
                            "safety": "Do not taste or ingest molded food samples."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Core Summary: Post-Harvest Loss Mitigation",
                        "content": {
                            "title": "Key Takeaways",
                            "text": "- **Horticultural crops contain 80–90% moisture**, fueling rapid rot.\n- **Kenya loses 30–40% of produce** to post-harvest bottlenecks.\n- **Market gluts crash prices**; processing creates shelf-stable inventory.\n- **Processing eliminates moisture, heat, and neutral pH**, stopping microbial decay."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Biological Cause of Rapid Rot",
                        "content": {
                            "question": "What is the primary biological and physiological reason fresh tomatoes rot within a few days when stored at warm room temperature?",
                            "options": [
                                "Tomatoes absorb atmospheric nitrogen and turn into gas",
                                "High internal moisture content combined with warm ambient temperatures accelerates natural plant respiration, enzymatic breakdown of cell walls, and rapid microbial proliferation",
                                "Tomato seeds explode inside the fruit",
                                "Tomatoes are converted into soil minerals by sunlight"
                            ],
                            "answer": "B",
                            "explanation": "Fresh tomatoes are living tissues containing over 90% water. Warm ambient temperatures stimulate cellular respiration and internal pectinase enzymes that soften tissue, while providing optimal growth conditions for bacteria and fungal molds."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 3: Nutritional and Food Security Impact of Value Addition
        # =====================================================================
        {
            "unit_order": 3,
            "unit_name": "Nutritional and Food Security Impact of Value Addition",
            "unit_description": "4 Pillars of food security; dry-season nutrient bridges; food fortification; composite porridge flours (*Omena*, millet, sorghum, groundnuts).",
            "lesson_title": "Food Security Engineering: 4 Pillars, Dry-Season Nutrient Bridges, and Composite Flours",
            "pages": [
                [
                    {
                        "type": "suggested_image",
                        "title": "Bowls of Diverse Cereal Grains and Legumes for Composite Flour Blending",
                        "content": {
                            "title": "Bowls of Diverse Cereal Grains and Legumes for Composite Flour Blending",
                            "caption": "A collection of sorghum, finger millet, maize, and high-protein legumes used to formulate nutrient-dense composite porridge flours."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Nutrition & Food Security",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Define the **4 pillars of food security (Availability, Access, Utilization, Stability)**.",
                                "Analyze how value addition bridges **dry-season caloric and micronutrient deficits**.",
                                "Formulate **composite porridge flours** incorporating cereals, legumes, and *Omena*.",
                                "Deploy **food fortification** to combat childhood stunting and Vitamin A deficiency."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The 4 Pillars of Food Security",
                        "content": {
                            "title": "Food Security Architecture",
                            "text": "**Food security** exists when all people, at all times, have physical, social, and economic access to sufficient, safe, and nutritious food:\n\n1. **Availability**: Sufficient quantities of food supplied through domestic production or imports.\n2. **Access**: Household purchasing power and transport access to obtain nutritious food.\n3. **Utilization**: Biological absorption of nutrients through clean water, hygiene, and balanced diet diversity.\n4. **Stability**: Continuous, reliable access to food year-round without seasonal disruptions or drought shocks.\n- *Impact*: Value addition directly fortifies **Stability and Availability** by converting perishable seasonal surpluses into year-round food stocks!"
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "Bridging Dry-Season Nutritional Gaps",
                        "content": {
                            "title": "Preserving Fragile Micronutrients",
                            "text": "During prolonged dry seasons in Kenya, diets become restricted to starchy maize, causing severe micro-nutrient deficiencies (Vitamin A, Iron, Zinc) and child stunting:\n- **Dehydrated Indigenous Vegetables**: Solar drying green leafy vegetables (amaranth, spider plant, cowpea leaves) preserves Vitamin A and iron, creating shelf-stable nutrient packs for dry seasons.\n- **Dried Fruit Chips**: Dehydrating ripe mangoes and papayas prevents seasonal waste and provides beta-carotene throughout drought months."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Composite Flours and Food Fortification",
                        "content": {
                            "title": "Combating Protein-Energy Malnutrition",
                            "text": "- **Food Fortification**: Deliberately increasing essential micronutrients in processed foods.\n- **Composite Flour Architecture**: Blending balanced proportions of complementary crops:\n  - *Finger Millet & Sorghum*: High in calcium, iron, and slow-release dietary fiber.\n  - *Maize*: Primary carbohydrate energy source.\n  - *Groundnuts / Soya*: High in essential vegetable proteins ($>25\\%$) and healthy fats.\n  - *Dried Silver Cyprinid (Omena)*: Rich in animal protein, calcium, and Omega-3 fatty acids.\n  - *Result*: A complete, highly digestible weaning porridge that prevents kwashiorkor and stunting."
                        }
                    }
                ],
                [
                    {
                        "type": "comparison_table",
                        "title": "Single Grain vs Composite Fortified Flour Comparison",
                        "content": {
                            "title": "Nutritional Profile Comparison Matrix",
                            "headers": ["Nutritional Parameter", "Pure Maize Meal (Ugali Flour)", "Fortified Composite Flour (Millet+Soya+Omena)", "Agronomic / Health Advantage"],
                            "rows": [
                                ["Crude Protein Content", "Low (7–8% incomplete protein)", "High (16–20% complete amino acids)", "Builds child muscle tissue & prevents kwashiorkor"],
                                ["Calcium & Iron Level", "Very Low (<15 mg/100g)", "High (>120 mg/100g from finger millet/omena)", "Strengthens bone density & prevents anemia"],
                                ["Dietary Fiber & GI", "Low fiber / High Glycemic Index", "High prebiotic fiber / Low Glycemic Index", "Provides sustained, long-lasting child energy"],
                                ["Market Price & Margin", "Standard commodity (KES 60/kg)", "Premium value-added (KES 180–250/kg)", "300% higher revenue for the farm processor"]
                            ]
                        }
                    }
                ],
                [
                    {
                        "type": "mini_activity",
                        "title": "Classroom Practical: Formulating a Balanced Composite Porridge Flour",
                        "content": {
                            "title": "Composite Flour Formulation Practicum",
                            "task": "1. Measure: 40% Finger Millet flour, 30% Sorghum flour, 20% Roasted Groundnut flour, and 10% Fine Omena powder.\n2. Blend thoroughly in a clean stainless bowl until uniformly mixed.\n3. Prepare a sample porridge; evaluate aroma, texture, color, and taste.\n4. Design a nutritional facts label highlighting protein and iron benefits.",
                            "materials": ["Flour Samples", "Weighing Scale", "Mixing Bowl", "Pot & Stove"],
                            "safety": "Ensure strict food hygiene when handling edible ingredients."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Core Summary: Nutrition & Food Security",
                        "content": {
                            "title": "Key Takeaways",
                            "text": "- **Value addition strengthens Availability and Stability** in food security.\n- **Solar-dried vegetables bridge dry-season Vitamin A gaps**.\n- **Composite flours blend cereals, legumes, and Omena** for balanced protein.\n- **Fortified products fight childhood stunting and anemia**."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Rationale for Composite Flour",
                        "content": {
                            "question": "Why is blending finger millet, sorghum, roasted groundnuts, and dried Omena into composite flour far superior for child nutrition than using pure maize flour alone?",
                            "options": [
                                "Maize flour is poisonous to children under five",
                                "The composite blend combines cereal energy with high-protein legumes and calcium/iron-rich Omena, providing a complete spectrum of essential amino acids and micronutrients that prevents malnutrition",
                                "Composite flour makes the porridge turn bright blue",
                                "Maize cannot be boiled in water"
                            ],
                            "answer": "B",
                            "explanation": "Pure maize meal is primarily starch with low and incomplete protein. Blending millet (calcium/iron), sorghum (fiber/minerals), groundnuts (plant protein/lipids), and Omena (animal protein/calcium) delivers complete nutrition to combat childhood stunting and kwashiorkor."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 4: Value-Addition Methods
        # =====================================================================
        {
            "unit_order": 4,
            "unit_name": "Value-Addition Methods",
            "unit_description": "6 Scientific preservation methods: Dehydration (<12% moisture), Milling, Thermal pasteurization (72°C for 15s), Chemical preservation (low pH <4.6, high sugar/salt osmosis), Fermentation (lactic acid bacteria), and Mechanical extraction.",
            "lesson_title": "Scientific Preservation: The 6 Core Pathways of Agricultural Value Addition",
            "pages": [
                [
                    {
                        "type": "suggested_image",
                        "title": "Solar Food Dryer Utilized for Agricultural Crop Dehydration",
                        "content": {
                            "title": "Solar Food Dryer Utilized for Agricultural Crop Dehydration",
                            "caption": "A clean solar box dryer with angled glazing and ventilation mesh, utilizing thermal airflow to dehydrate crops below 12% moisture."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Value-Addition Methods",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Identify the **6 primary scientific methods of agricultural value addition**.",
                                "Analyze the biological mechanism of **Dehydration, Thermal Treatment, and Milling**.",
                                "Evaluate **Chemical preservation (low pH, sugar/salt osmosis)** and **Fermentation**.",
                                "Match raw farm commodities to their optimal preservation pathway."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Methods 1 & 2: Dehydration and Milling",
                        "content": {
                            "title": "Moisture Removal and Surface Area Expansion",
                            "text": "1. **Dehydration (Drying)**: Thermally removing free cellular water until moisture activity drops below **$12\\%$**. Deprived of liquid water, bacterial and fungal enzymes cannot metabolize or multiply. Applied to grains, cassava chips, sliced mangoes, and vegetables.\n2. **Milling (Grinding)**: Mechanically crushing solid dry crops into fine powders. Multiplies surface area, enhances digestibility, facilitates mixing, and allows compact, airtight storage."
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "Methods 3 & 4: Thermal Treatment and Chemical Preservation",
                        "content": {
                            "title": "Destroying Pathogens and Altering Chemical Environments",
                            "text": "3. **Thermal Treatment (Heat)**: Heating food to destroy active vegetative pathogens and denature self-digesting enzymes. **Pasteurization** heats milk or juice to **$72^\\circ\\text{C for }15\\text{ seconds}$**; **Sterilization/Canning** boils under pressure at **$121^\\circ\\text{C}$**.\n4. **Chemical Preservation**:\n   - *Acids (Vinegar / Citric Acid)*: Lowers food pH below **$4.6$**, stopping bacterial spore germination.\n   - *High Sugar / Salt*: Creates a hypertonic environment that exerts massive **osmotic pressure**, drawing water out of microbial cells so they dehydrate and die!"
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "6 Core Scientific Methods of Agricultural Value Addition",
                        "content": {
                            "title": "6 Core Scientific Methods of Agricultural Value Addition",
                            "caption": "Preservation taxonomy: 1 Dehydration (Moisture <12%) | 2 Milling (Fine flour) | 3 Thermal (72°C Pasteurization) | 4 Chemical (pH <4.6 & Osmosis) | 5 Fermentation (Lactic acid) | 6 Extraction (Cold pressed oils)."
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "Methods 5 & 6: Fermentation and Extraction",
                        "content": {
                            "title": "Beneficial Microbes and Component Separation",
                            "text": "5. **Fermentation**: Culturing beneficial anaerobic microorganisms (lactic acid bacteria like *Lactobacillus*, yeasts) that convert sugars into organic lactic acid or alcohol. Lowers pH to **$4.5$**, enhances flavor, synthesizes B-vitamins, and creates acidic barriers against food-poisoning bacteria (Mala, Yoghurt, Pickles).\n6. **Extraction**: Applying hydraulic pressure or centrifugal force to separate high-value components from raw produce (e.g., cold-pressing sunflower seeds for oil, pressing avocado pulp for oil, extracting passion fruit nectar)."
                        }
                    },
                    {
                        "type": "comparison_table",
                        "title": "6 Core Value Addition Methods Comparison",
                        "content": {
                            "title": "Value Addition Scientific Methods Matrix",
                            "headers": ["Method", "Scientific Mechanism", "Critical Threshold / Condition", "Target Farm Commodities"],
                            "rows": [
                                ["Dehydration", "Removes free moisture; halts microbes", "Moisture content <12%", "Cereals, Cassava, Mangoes, Bananas"],
                                ["Milling", "Physical particle size reduction", "Fine mesh (<0.5 mm)", "Dried grains, Tubers, Pulses"],
                                ["Thermal Treatment", "Heat denatures enzymes & kills pathogens", "72°C for 15s (Pasteurization)", "Fresh Milk, Fruit Juices, Canned Veg"],
                                ["Chemical Preservation", "Osmotic dehydration & low pH", "pH <4.6 / High Brix sugar", "Fruit Jams, Pickles, Salted Fish/Meat"],
                                ["Fermentation", "Lactic acid production by microbes", "Anaerobic incubation at 43°C", "Cultured Milk (Mala), Yoghurt, Silage"],
                                ["Extraction", "Mechanical pressure separates liquids", "Cold-press mechanical expeller", "Sunflower Oil, Avocado Oil, Fruit Juice"]
                            ]
                        }
                    }
                ],
                [
                    {
                        "type": "mini_activity",
                        "title": "Simulation Practical: Osmotic Dehydration Lab Using Salt and Sugar",
                        "content": {
                            "title": "Osmotic Preservation Practicum",
                            "task": "1. Cut 3 identical cucumber or potato cubes (2cm x 2cm).\n2. Place Cube A in plain water, Cube B in saturated salt water, and Cube C in dry table salt.\n3. Measure the weight and firmness of all 3 cubes after 4 hours.\n4. Explain how osmosis draws cellular moisture out of tissue and microbes.",
                            "materials": ["Cucumber/Potato", "Table Salt", "Beakers", "Weighing Scale"],
                            "safety": "Handle cutting knives carefully."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Core Summary: Value-Addition Methods",
                        "content": {
                            "title": "Key Takeaways",
                            "text": "- **Drying lowers moisture below 12%**, halting microbial life.\n- **Pasteurization heats to 72°C for 15s**, killing pathogens while preserving flavor.\n- **High salt and sugar preserve food through osmotic dehydration**.\n- **Fermentation drops pH to 4.5**, creating an acidic protection shield."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Osmotic Preservation Mechanism",
                        "content": {
                            "question": "What is the precise biophysical process that occurs when raw meat, fish, or fruit jam is preserved with high concentrations of salt or sugar?",
                            "options": [
                                "The salt heats the food to boiling temperatures",
                                "A hypertonic environment is created that exerts high osmotic pressure, drawing water out of microbial cells, causing them to dehydrate, shrivel, and die",
                                "Sugar converts the food proteins into inert plastic",
                                "Salt attracts beneficial earthworms that sterilize the food"
                            ],
                            "answer": "B",
                            "explanation": "High solute concentrations (salt or sugar) create a hypertonic gradient outside microbial cells. Through osmosis, water rapidly diffuses out of the bacteria or yeasts into the surrounding medium, dehydrating the microbes and stopping all cellular reproduction."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 5: Plant Processing Practical I - Banana and Potato Crisps
        # =====================================================================
        {
            "unit_order": 5,
            "unit_name": "Plant Processing Practical I - Banana and Potato Crisps",
            "unit_description": "Raw material selection; peeling, 1mm slicing, starch rinsing, drying; frying at 170–180°C, draining, seasoning; enterprise economics (200% profit boost).",
            "lesson_title": "Tuber and Banana Processing: Crisps Manufacturing, Thermal Frying, and Enterprise Margins",
            "pages": [
                [
                    {
                        "type": "suggested_image",
                        "title": "Golden Crispy Potato Chips and Plantain Crisps in Serving Bowl",
                        "content": {
                            "title": "Golden Crispy Potato Chips and Plantain Crisps in Serving Bowl",
                            "caption": "Golden, uniformly sliced, and seasoned potato and plantain crisps, illustrating value addition from raw roots and unripe bananas."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Crisps Processing",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Select optimal **low-sugar potato varieties and green cooking bananas** for crisping.",
                                "Execute the 5-step processing pipeline: **Peel, 1mm Slice, Starch Rinse, Dry, and Fry at 170–180°C**.",
                                "Enforce **hot-oil kitchen safety and oil drainage standards**.",
                                "Compute **cost-of-production, moisture loss, and enterprise profit margins (+200%)**."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Raw Material Selection and Preparation",
                        "content": {
                            "title": "The Foundation of Quality Crisps",
                            "text": "1. **Potatoes**: Select firm, mature Irish potatoes low in reducing sugars (which turn brown/bitter when fried). Avoid green skin or sprouted tubers (**solanine toxicity**).\n2. **Bananas**: Select completely unripe, green cooking bananas (matooke or plantains) with firm starch pulp.\n3. **Peeling & Slicing**: Peel thinly with stainless knives. Slice into uniform, paper-thin discs (**$1.0\\text{ mm}$ thickness**) using a mandoline slicer.\n4. **Cold Starch Rinse**: Submerge slices in cold water to wash away surface starch, preventing them from sticking together in the frying pan."
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "Thermal Frying and Seasoning Protocol",
                        "content": {
                            "title": "Achieving Golden Crispiness",
                            "text": "1. **Cloth Drying**: Pat slices 100% dry on lint-free cloth. (Wet slices cause dangerous hot oil splattering!).\n2. **Deep Frying ($170\\text{--}180^\\circ\\text{C}$)**: Slide slices into clean vegetable oil. Maintain temperature; frying too cold ($<150^\\circ\\text{C}$) makes crisps oily and soggy; too hot ($>200^\\circ\\text{C}$) burns them.\n3. **Drainage**: Scoop golden crisps using a slotted wire skimmer and drain on food-grade absorbent paper.\n4. **Seasoning**: Dust with fine salt, chili, or paprika while still warm for optimal adhesion."
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Crisp Production Pipeline & Value Addition Economics",
                        "content": {
                            "title": "Crisp Production Pipeline & Value Addition Economics",
                            "caption": "Manufacturing flow: Raw Tuber (KES 40/kg) -> Peel & 1mm Slice -> Wash & Dry -> Deep Fry (175°C) -> Season & Pouch -> Retail Sales (KES 180 = 200% Profit Margin!)."
                        }
                    }
                ],
                [
                    {
                        "type": "comparison_table",
                        "title": "Crisp Enterprise Financial Budget (1 kg Raw Potatoes)",
                        "content": {
                            "title": "1 kg Potato Crisp Enterprise Financial Model",
                            "headers": ["Expense / Revenue Item", "Physical Quantity", "Unit Cost (KES)", "Total Value (KES)"],
                            "rows": [
                                ["Raw Irish Potatoes", "1.0 kg raw tubers", "40 / kg", "40.00"],
                                ["Vegetable Cooking Oil (Consumed)", "0.15 Liters", "200 / L", "30.00"],
                                ["Cooking Fuel (Gas / Briquettes)", "1 Batch run", "15 / batch", "15.00"],
                                ["Seasoning (Fine Salt & Spices)", "10 grams", "5 / batch", "5.00"],
                                ["Packaging Pouches (Branded)", "6 Pouches (50g each)", "3 / pouch", "18.00"],
                                ["Total Cost of Production (COP)", "6 x 50g finished packets", "-", "108.00"],
                                ["Gross Sales Revenue", "6 Packets sold @ KES 30 each", "30 / packet", "180.00"],
                                ["Net Enterprise Profit", "Gross Rev (180) - COP (108)", "-", "KES 72.00 (+180% Return!)"]
                            ]
                        }
                    }
                ],
                [
                    {
                        "type": "mini_activity",
                        "title": "Home Science Lab: Potato & Plantain Crisp Processing Practicum",
                        "content": {
                            "title": "Crisp Manufacturing Practical",
                            "task": "1. Wash, peel, and slice 500g of raw potatoes to 1mm thickness.\n2. Rinse in cold water and dry on clean towel.\n3. Deep-fry in vegetable oil at 175°C until bubbling ceases.\n4. Drain, dust with salt, weigh finished crisps, and calculate moisture loss percentage.",
                            "materials": ["Potatoes/Bananas", "Mandoline Slicer", "Cooking Oil", "Deep Pan", "Thermometer", "Scale"],
                            "safety": "Wear heat-resistant aprons; never leave hot oil unattended."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Core Summary: Crisps Processing",
                        "content": {
                            "title": "Key Takeaways",
                            "text": "- **Slice tubers to 1mm** and rinse surface starch in cold water.\n- **Pat slices dry** before frying to prevent dangerous oil splatter.\n- **Maintain frying oil at 170–180°C** for optimal crispiness.\n- **Value addition boosts profit by ~200%** over raw potato sales."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Rationale for Rinsing Slices in Cold Water",
                        "content": {
                            "question": "Why must freshly sliced potato and banana crisps be washed in cold water before frying?",
                            "options": [
                                "To add sugar to the crisps",
                                "To rinse away loose surface starch so the slices do not stick together in a soggy clump during deep frying",
                                "To make the crisps turn blue",
                                "To dissolve the potato skin completely"
                            ],
                            "answer": "B",
                            "explanation": "Slicing potatoes ruptures starch granules, leaving a sticky starch film on the surface. Rinsing in cold water washes away this free starch, ensuring individual crisp separation and uniform golden frying."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 6: Plant Processing Practical II - Vegetable Preservation & Sauces
        # =====================================================================
        {
            "unit_order": 6,
            "unit_name": "Plant Processing Practical II - Vegetable Preservation & Sauces",
            "unit_description": "Vegetable blanching (thermal enzyme deactivation); tomato sauce & jam processing; the Jam Preservation Triangle (thermal kill, pH <4.6, osmotic sugar dehydration).",
            "lesson_title": "Horticultural Processing: Vegetable Blanching, Tomato Jam, and the Preservation Triangle",
            "pages": [
                [
                    {
                        "type": "suggested_image",
                        "title": "Jars of Canned Tomato Sauce, Vegetable Preserves, and Jams",
                        "content": {
                            "title": "Jars of Canned Tomato Sauce, Vegetable Preserves, and Jams",
                            "caption": "Sterilized glass jars containing processed tomato sauce, chutney, and vegetable jam, illustrating thermal sealing and acidic preservation."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Vegetable Preservation & Sauces",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Execute **vegetable blanching and shocking to deactivate ripening enzymes**.",
                                "Manufacture shelf-stable **tomato sauce and tomato jam**.",
                                "Analyze the **Jam Preservation Triangle: Heat, Low pH (<4.6), and Osmotic Pressure**.",
                                "Sterilize glass containers and vacuum-seal jars via hot-fill inversion."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Vegetable Blanching: Halting Enzymatic Decay",
                        "content": {
                            "title": "The Science of Blanching and Shocking",
                            "text": "- **The Process**: Submerging fresh green vegetables (spinach, kales, beans) in boiling water for **1 to 2 minutes**, then instantly transferring them into ice-cold water (**shocking**).\n- **Why Blanch?**:\n  - *Deactivates Enzymes*: Destroys polyphenol oxidase and catalase enzymes that would otherwise cause browning, loss of Vitamin C, and foul off-flavors during drying or freezing.\n  - *Sanitizes*: Destroys surface bacteria and shrinks foliage volume for compact packing."
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "Tomato Sauce and Tomato Jam Manufacturing Pipeline",
                        "content": {
                            "title": "Converting Seasonal Gluts into Stable Preserves",
                            "text": "1. **Blanching & Peeling**: Dip ripe red tomatoes in boiling water for **30 seconds**; skins split and slide off effortlessly.\n2. **Pureeing & Formulation**: Blend pulp. For **Tomato Jam**, add equal weight refined sugar ($1:1$ ratio) and fresh lemon juice (citric acid).\n3. **Thermal Concentration**: Boil steadily with constant stirring until the mixture reaches the gelling point (**$104^\\circ\\text{C}$**).\n4. **Hot-Fill Bottling**: Pour boiling jam directly into sterilized, pre-warmed glass jars leaving $1\\text{ cm}$ headspace. Seal tightly and **invert jars for 5 minutes** so the boiling jam sterilizes the lid underside!"
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The Jam Preservation Triangle",
                        "content": {
                            "title": "The 3 Irreversible Defense Barriers",
                            "text": "Tomato and fruit jams last for over 12 months without refrigeration due to three synergistic barriers:\n1. **Thermal Kill**: Boiling at $104^\\circ\\text{C}$ destroys all active bacterial, yeast, and mold cells.\n2. **High Acidity (Low pH $<4.6$)**: Lemon juice citric acid creates an acidic environment that prevents *Clostridium botulinum* bacterial spore germination.\n3. **Osmotic Dehydration (High Sugar)**: Concentrated sugar binds free water molecules ($>65^\\circ\\text{ Brix}$), creating high osmotic pressure that desiccates any invading microbe!"
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "The Jam Preservation Triangle: Heat, Acidity & Osmosis",
                        "content": {
                            "title": "The Jam Preservation Triangle: Heat, Acidity & Osmosis",
                            "caption": "The 3 Pillars of Jam Preservation: 1 Thermal Kill (Boiling 104°C destroys pathogens) + 2 High Acidity (Lemon citric acid pH <4.6 halts spores) + 3 Osmotic Dehydration (Sugar binds free water)."
                        }
                    }
                ],
                [
                    {
                        "type": "comparison_table",
                        "title": "Tomato Products Processing Matrix",
                        "content": {
                            "title": "Tomato Value Addition Formulations Matrix",
                            "headers": ["Product Name", "Key Ingredients & Ratios", "Preservation Barrier", "Expected Shelf-Life"],
                            "rows": [
                                ["Tomato Jam", "Tomato pulp (50%) + Sugar (45%) + Lemon juice (5%)", "High Sugar Osmosis + Low pH + Heat", "12 to 18 Months (Room Temp)"],
                                ["Tomato Sauce / Ketchup", "Tomato puree + Vinegar + Salt + Spices + Sugar", "Acetic acid (Low pH) + Pasteurization", "6 to 12 Months (Sealed)"],
                                ["Sun-Dried Tomatoes", "Salted tomato halves dehydrated to <12% moisture", "Moisture Dehydration + Surface Salt", "12 Months (Dry storage)"],
                                ["Tomato Paste (Concentrate)", "Pure tomato pulp boiled down to 28% total solids", "Thermal sterilization + Hot vacuum seal", "12 to 24 Months (Canned/Jars)"]
                            ]
                        }
                    }
                ],
                [
                    {
                        "type": "mini_activity",
                        "title": "Food Science Lab: Tomato Jam Processing and Hot-Fill Inversion",
                        "content": {
                            "title": "Tomato Jam Manufacturing Practicum",
                            "task": "1. Blanch and peel 1kg of ripe tomatoes; puree the pulp.\n2. Add 800g sugar and 50ml fresh lemon juice in a stainless saucepan.\n3. Boil and stir until the temperature reaches 104°C and sauce thickens.\n4. Pour into sterilized hot glass jars, cap tightly, invert for 5 minutes, and label.",
                            "materials": ["Tomatoes", "Sugar", "Lemon Juice", "Saucepan", "Glass Jars + Lids", "Thermometer"],
                            "safety": "Handle boiling sugar syrup with extreme care to prevent burns."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Core Summary: Vegetable Preservation & Sauces",
                        "content": {
                            "title": "Key Takeaways",
                            "text": "- **Blanching deactivates ripening enzymes** and preserves leaf color.\n- **The Jam Triangle relies on Heat, Low pH (<4.6), and Sugar Osmosis**.\n- **Lemon juice drops pH**, stopping dangerous bacterial spores.\n- **Hot-fill jar inversion sterilizes the inner lid**, creating an airtight seal."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Role of Citric Acid in Tomato Jam",
                        "content": {
                            "question": "What is the critical scientific food safety reason for adding fresh lemon juice (citric acid) when preparing homemade tomato jam?",
                            "options": [
                                "To make the jam turn yellow",
                                "To lower the pH below 4.6, creating an acidic environment that prevents the germination of dangerous bacterial spores like Clostridium botulinum and assists pectin gelling",
                                "To make the seeds dissolve into gas",
                                "To increase the water content of the jam"
                            ],
                            "answer": "B",
                            "explanation": "Citric acid in lemon juice reduces the food pH below 4.6. This acidic threshold is essential because pathogenic spore-forming bacteria (such as Clostridium botulinum) cannot germinate in acid conditions. It also activates pectin gelling."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 7: Plant Processing Practical III - Fruit Juice Processing
        # =====================================================================
        {
            "unit_order": 7,
            "unit_name": "Plant Processing Practical III - Fruit Juice Processing",
            "unit_description": "Fruit pulp extraction and straining; pasteurization at 72–75°C for 15–20s vs boiling nutrient destruction; nectar formulation (30% pulp, 10% sugar, 60% water).",
            "lesson_title": "Horticultural Beverages: Fruit Juice Extraction, Mild Pasteurization, and Nectar Formulation",
            "pages": [
                [
                    {
                        "type": "suggested_image",
                        "title": "Fresh Fruit Juice Served in Glass Pitcher and Drinking Glass",
                        "content": {
                            "title": "Fresh Fruit Juice Served in Glass Pitcher and Drinking Glass",
                            "caption": "Freshly extracted, pasteurized fruit juice in a clear glass bottle, demonstrating clarity, natural color, and shelf-stable beverage processing."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Fruit Juice Processing",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Extract and strain fresh fruit pulp (**passion fruit, mango, citrus, pineapple**).",
                                "Execute **mild pasteurization at 72–75°C for 15–20 seconds**.",
                                "Analyze why **boiling at 100°C destroys Vitamin C and scorches fruit sugars**.",
                                "Formulate commercial fruit nectar (**30% pulp, 10% sugar, 60% water**)."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Sourcing and Pulp Extraction",
                        "content": {
                            "title": "Extracting Pure Liquid Assets",
                            "text": "1. **Washing & Sorting**: Select fully ripe, aromatic, clean fruits. Wash thoroughly in potable water.\n2. **Pulp Extraction**: Cut fruits open. For passion fruits, scoop the golden aril seeds; for mangoes/pineapples, peel and blend pulp.\n3. **Straining & Filtration**: Pass pulp through a stainless steel sieve or double cheesecloth to remove seeds and coarse fibrous debris, yielding a smooth liquid juice."
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "Thermal Pasteurization: 72°C vs. Boiling at 100°C",
                        "content": {
                            "title": "Preserving Aroma, Color, and Vitamin C",
                            "text": "Raw fruit juice contains wild yeasts and bacteria that will ferment sugars into sour alcohol within **24 hours**:\n- **The Pasteurization Protocol**: Heat strained juice in a stainless steel double-boiler to **$72^\\circ\\text{ to }75^\\circ\\text{C}$** and hold for **$15\\text{ to }20\\text{ seconds}$**, then chill rapidly below $10^\\circ\\text{C}$.\n- **Why Never Boil Juice at $100^\\circ\\text{C}$?**:\n  - *Destroys Vitamin C*: Ascorbic acid is heat-labile and degrades rapidly above $80^\\circ\\text{C}$.\n  - *Caramelization*: High heat scorches natural fructose, giving the juice a burnt, cooked taste and dull brownish color."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Nectar and Squash Formulation Ratios",
                        "content": {
                            "title": "Balancing Acidity, Sweetness, and Viscosity",
                            "text": "Pure fruit juice (like passion fruit) is too acidic to drink straight. Processors formulate **Nectars**:\n- **Standard Nectar Recipe**:\n  - **$30\\%$ Pure Fruit Pulp** (Flavor and natural nutrients)\n  - **$10\\%$ Refined Sugar Syrup** (Balances natural acidity)\n  - **$60\\%$ Boiled Purified Water** (Hydration and dilution)\n- *Preservation*: Add $0.1\\%$ food-grade sodium benzoate for room-temperature commercial shelf-life."
                        }
                    }
                ],
                [
                    {
                        "type": "comparison_table",
                        "title": "Fruit Beverage Formulations Comparison",
                        "content": {
                            "title": "Fruit Beverage Product Standards",
                            "headers": ["Beverage Category", "Minimum Fruit Content", "Sugar / Water Ratios", "Target Consumer Market"],
                            "rows": [
                                ["100% Pure Fruit Juice", "100% pure extracted fruit", "0% Added water / 0% Sugar", "High-end premium health beverage"],
                                ["Fruit Nectar", "30% to 50% fruit pulp", "10% Sugar + 40–60% Clean water", "Standard commercial bottled juice"],
                                ["Fruit Cordial / Squash", "25% fruit concentrate", "50% Sugar syrup (Diluted 1:4 by consumer)", "Economical household long-life concentrate"]
                            ]
                        }
                    }
                ],
                [
                    {
                        "type": "mini_activity",
                        "title": "Beverage Lab: Passion Fruit Pulp Extraction and 72°C Pasteurization",
                        "content": {
                            "title": "Passion Fruit Nectar Practicum",
                            "task": "1. Extract pulp from 10 ripe passion fruits; strain seeds through cheesecloth.\n2. Formulate nectar: 300ml pulp + 100g sugar + 600ml boiled water.\n3. Heat mixture in a pot to exactly 72°C (verify with thermometer) for 15s.\n4. Cool rapidly in an ice-water bath, bottle in sterilized glass bottles, and seal.",
                            "materials": ["Passion Fruits", "Cheesecloth", "Sugar", "Water", "Thermometer", "Bottles"],
                            "safety": "Monitor thermometer carefully; do not allow juice to boil."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Core Summary: Fruit Juice Processing",
                        "content": {
                            "title": "Key Takeaways",
                            "text": "- **Strain pulp through fine cheesecloth** to remove seeds and fibers.\n- **Pasteurize at 72–75°C for 15–20 seconds** to kill wild fermenting yeasts.\n- **Never boil juice at 100°C**; boiling destroys Vitamin C and scorches flavor.\n- **Formulate standard nectar using 30% pulp, 10% sugar, 60% water**."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Pasteurization Temperature for Fruit Juice",
                        "content": {
                            "question": "Why is fruit juice pasteurized at 72°C to 75°C for 15 seconds rather than being boiled at 100°C during commercial beverage processing?",
                            "options": [
                                "Boiling juice makes it freeze into solid ice",
                                "Pasteurization at 72°C kills active fermenting yeasts and pathogens while preserving natural floral aromas and heat-fragile Vitamin C, whereas boiling destroys vitamins and scorches natural sugars",
                                "Boiled juice is illegal under Kenya public health laws",
                                "Fruit juice cannot be heated above 50°C without exploding"
                            ],
                            "answer": "B",
                            "explanation": "Fruit aroma compounds and Vitamin C (ascorbic acid) are highly sensitive to heat. Pasteurization at 72–75°C achieves the required microbial kill without cooking the fruit or destroying its nutritional value, whereas boiling gives juice a burnt, unpalatable flavor."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 8: Plant Processing Practical IV - Flour Processing
        # =====================================================================
        {
            "unit_order": 8,
            "unit_name": "Plant Processing Practical IV - Flour Processing",
            "unit_description": "Root tuber drought resilience; safe cassava processing & cyanide removal (thick peel, chipping, 3-day fermentation, solar drying <12%); hammer milling, 0.5mm sieving, pallet storage.",
            "lesson_title": "Root Crop Processing: Cassava Cyanide Detoxification, Solar Dehydration, and Flour Milling",
            "pages": [
                [
                    {
                        "type": "suggested_image",
                        "title": "Cassava Flour and Traditional Food Processing Mortar",
                        "content": {
                            "title": "Cassava Flour and Traditional Food Processing Mortar",
                            "caption": "Milled cassava flour and root pieces, illustrating value-added flour processing and detoxification from perishable drought-tolerant tubers."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Root Flour Processing",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Explain why **root tubers rot within 48–72 hours after harvest**.",
                                "Analyze the biochemical hazard of **cyanogenic glycosides in raw bitter cassava**.",
                                "Execute the 4-step cassava detoxification protocol: **Thick Peel, Chip, 3-Day Ferment, and Solar Dry (<12%)**.",
                                "Perform **hammer milling, 0.5mm sieving, and moisture-proof pallet storage**."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Root Tubers and the Perishability Dilemma",
                        "content": {
                            "title": "Drought-Resilient Food Security Champions",
                            "text": "- **Agronomic Strength**: Cassava and sweet potatoes tolerate severe semi-arid droughts, producing abundant carbohydrates where maize fails.\n- **The 48-Hour Decay Crisis**: Once detached from the plant, tuber respiration skyrockets. Internal **vascular streaking and black rot** ruin the roots within **48 to 72 hours**.\n- **The Solution**: Processing tubers into dry flour extends shelf-life from 2 days to **over 12 months**!"
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "Cassava Cyanide Detoxification Protocol",
                        "content": {
                            "title": "Neutralizing Lethal Cyanogenic Glycosides",
                            "text": "**CRITICAL FOOD SAFETY HAZARD**: Raw bitter cassava contains **linamarin and lotaustralin** (cyanogenic glycosides) that release toxic **hydrogen cyanide (HCN) gas** when eaten raw, causing paralysis or fatal cyanide poisoning:\n\n1. **Thick Peeling**: Remove the outer brown woody bark AND the inner pink/white rind (which holds **$>80\\%$ of total cyanide**).\n2. **Chipping**: Slice into thin finger-sized chips ($5\\text{ mm}$) to maximize surface area.\n3. **3-Day Soaking / Fermentation**: Submerge chips in water for **72 hours**. Natural lactic fermentation activates internal linamarase enzymes that break down cyanogenic glycosides and leach out cyanide into the water.\n4. **Solar Drying**: Spread chips on raised mesh screens until bone-dry (**$<12\\%$ moisture**); chips snap cleanly with a crisp sound."
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Safe Cassava Detoxification & Flour Milling Pipeline",
                        "content": {
                            "title": "Safe Cassava Detoxification & Flour Milling Pipeline",
                            "caption": "Detoxification pipeline: 1 Raw Cassava (Contains cyanogenic glycosides) -> 2 Thick Peel & Chip -> 3 72-Hour Water Soak/Ferment (Cyanide leaches out) -> 4 Solar Dry (<12% Moisture) -> 5 Hammer Mill & 0.5mm Sieve -> 6 Safe Food Flour."
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "Milling, Sieving, and Pallet Storage",
                        "content": {
                            "title": "Professional Packaging and Storage",
                            "text": "1. **Hammer Milling**: Grind bone-dry cassava or sweet potato chips in a clean hammer mill into fine flour.\n2. **Sieving ($0.5\\text{ mm}$ Mesh)**: Sift flour through a fine vibrating sieve to remove coarse woody fibers, producing a soft, premium baking-grade flour.\n3. **Packaging**: Seal in thick, food-grade polyethylene bags.\n4. **Pallet Storage**: Store bags on **raised wooden pallets $15\\text{ cm}$ above the concrete floor** and $30\\text{ cm}$ away from walls to prevent ground dampness and mold."
                        }
                    },
                    {
                        "type": "comparison_table",
                        "title": "Raw Cassava vs Processed Cassava Flour Comparison",
                        "content": {
                            "title": "Cassava Value Addition Transformation",
                            "headers": ["Parameter", "Raw Harvested Cassava Roots", "Detoxified Cassava Flour", "Agronomic / Consumer Benefit"],
                            "rows": [
                                ["Shelf-Life", "48 to 72 Hours (Rapid rot)", "12 to 18 Months", "Year-round famine reserve storage"],
                                ["Toxicity Status", "Potentially toxic (Cyanogenic glycosides)", "100% Safe (<10 ppm HCN)", "Safe for child consumption & baking"],
                                ["Market Form", "Heavy, perishable raw bulk", "Lightweight, packaged retail powder", "80% reduction in transport weight"],
                                ["Market Price", "KES 15–20 / kg (Distress sale)", "KES 100–140 / kg (Retail flour)", "500% Increase in farmer earnings"]
                            ]
                        }
                    }
                ],
                [
                    {
                        "type": "mini_activity",
                        "title": "Field Practical: Cassava Chipping, Solar Drying, and Sieve Testing Lab",
                        "content": {
                            "title": "Root Flour Milling Practicum",
                            "task": "1. Thick-peel 2 fresh cassava roots (remove outer bark and pink cortex).\n2. Slice roots into 5mm thin chips.\n3. Observe fermentation soaking and examine bone-dry chips for snap-test crispness.\n4. Sift milled flour through 1.0mm vs 0.5mm sieves; compare smoothness.",
                            "materials": ["Cassava Roots", "Peeling Knives", "Solar Drying Rack", "Sieves (0.5mm & 1.0mm)"],
                            "safety": "Never chew or taste raw bitter cassava chips during processing."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Core Summary: Flour Processing",
                        "content": {
                            "title": "Key Takeaways",
                            "text": "- **Raw cassava contains toxic cyanogenic glycosides** (cyanide).\n- **Thick peeling, 3-day soaking, and solar drying** removes 99% of cyanide.\n- **Dry chips until they snap cleanly (<12% moisture)** before milling.\n- **Store flour on raised wooden pallets** off the cold concrete floor."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Cassava Detoxification Mechanism",
                        "content": {
                            "question": "What is the critical food safety purpose of thick peeling, 3-day water soaking, and thorough solar drying during cassava flour processing?",
                            "options": [
                                "To make the cassava flour turn bright pink",
                                "To hydrolyze, leach out, and destroy lethal cyanogenic glycosides (cyanide), ensuring the flour is non-toxic and safe for human consumption",
                                "To add artificial vitamins to the tuber",
                                "To turn the tuber into animal fertilizer"
                            ],
                            "answer": "B",
                            "explanation": "Raw bitter cassava contains cyanogenic glycosides (linamarin) that release lethal hydrogen cyanide gas if ingested. Thick peeling removes the high-cyanide cortex, soaking ferments and leaches out the water-soluble toxins, and solar drying evaporates residual cyanide, rendering the flour safe."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 9: Animal Origin Processing I - Milk and Fermented Dairy
        # =====================================================================
        {
            "unit_order": 9,
            "unit_name": "Animal Origin Processing I - Milk and Fermented Dairy",
            "unit_description": "Traditional Mala fermentation (90°C for 10 min, cool to 25–30°C, inoculate, incubate 16–18h); Scientific yoghurt making (*Streptococcus thermophilus* + *Lactobacillus bulgaricus* at 43°C for 4–6h, pH 4.5); safety of acidic dairy.",
            "lesson_title": "Dairy Biotechnology: Mala Culture, Scientific Yoghurt Making, and Acidic Protection",
            "pages": [
                [
                    {
                        "type": "suggested_image",
                        "title": "Glass Jars of Freshly Cultured Yoghurt and Fermented Milk",
                        "content": {
                            "title": "Glass Jars of Freshly Cultured Yoghurt and Fermented Milk",
                            "caption": "Thick cultured yoghurt and fermented milk (Mala) in glass jars, illustrating controlled dairy fermentation and lactic acid preservation."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Milk & Fermented Dairy",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Execute traditional **Mala fermentation (90°C heating, 25–30°C incubation)**.",
                                "Master scientific yoghurt manufacturing using **Streptococcus thermophilus and Lactobacillus bulgaricus**.",
                                "Control the critical **43°C incubation temperature and pH drop to 4.5**.",
                                "Explain how **lactic acid acidification creates a natural biological shield against pathogens**."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Fermented Milk (Mala) Production Protocol",
                        "content": {
                            "title": "Traditional Fermented Dairy Mechanics",
                            "text": "Cultured sour milk (**Mala**) is an East African value-added staple:\n1. **Thermal Treatment**: Heat fresh milk to **$90^\\circ\\text{C for }10\\text{ minutes}$** (or boil). Kills wild bacteria and denatures whey proteins for a thicker body.\n2. **Cooling**: Cool rapidly to **$25^\\circ\\text{ to }30^\\circ\\text{C}$**.\n3. **Inoculation**: Add $2\\text{--}3\\%$ active Mala starter culture (mesophilic lactic bacteria).\n4. **Incubation**: Leave undisturbed at room temperature ($25^\\circ\\text{C}$) for **16 to 18 hours** until a smooth, coagulated curd forms. Stir, chill, and bottle."
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "Scientific Yoghurt Manufacturing: Thermophilic Fermentation",
                        "content": {
                            "title": "The Dynamic Duo: Streptococcus and Lactobacillus",
                            "text": "Yoghurt requires a symbiotic blend of two **thermophilic (heat-loving)** bacteria [32]:\n- ***Streptococcus thermophilus***: Fast acid producer; drops pH rapidly.\n- ***Lactobacillus bulgaricus***: Produces acetaldehyde for rich aroma and thick texture.\n- **The Step-by-Step Pipeline**:\n  1. *Pasteurize*: Heat milk to **$85^\\circ\\text{C for }30\\text{ min}$** or **$95^\\circ\\text{C for }5\\text{ min}$**.\n  2. *Cool to $43^\\circ\\text{C}$*: **$42^\\circ\\text{--}45^\\circ\\text{C}$** is the strict biological optimum for yoghurt bacteria. (Hotter than $50^\\circ\\text{C}$ kills them; cooler than $35^\\circ\\text{C}$ stalls growth!).\n  3. *Inoculate & Incubate*: Add $2\\%$ live yoghurt culture. Incubate at **$43^\\circ\\text{C for }4\\text{ to }6\\text{ hours}$** (in thermos/water bath) until pH drops to **$4.5$** and milk proteins coagulate.\n  4. *Cool & Flavor*: Chill below $10^\\circ\\text{C}$ to arrest acidification; fold in sugar and fruit flavors."
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Scientific Yoghurt Fermentation Curve: Time, Temp & pH Drop",
                        "content": {
                            "title": "Scientific Yoghurt Fermentation Curve: Time, Temp & pH Drop",
                            "caption": "Yoghurt fermentation kinetics: Fresh Milk (pH 6.6, 43°C) -> 2 Hours (Bacteria consume lactose) -> 4 Hours (pH drops to 4.8, protein coagulation starts) -> 6 Hours (pH 4.5, firm gel formed, chilled to 4°C)."
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "The Biological Safety of Acidic Dairy",
                        "content": {
                            "title": "Why Cultured Yoghurt Does Not Spoil",
                            "text": "- **The pH Barrier**: Lactic acid drops the milk pH from neutral **$6.6$ down to $4.5$**. Dangerous food-poisoning pathogens (*Salmonella*, *E. coli*, *Listeria*) cannot survive in acid.\n- **Microbial Competition**: Billions of beneficial lactic bacteria consume available milk sugars (lactose), starving out competing spoilage microbes.\n- **Lactose Digestibility**: Fermentation digests $30\\text{--}40\\%$ of milk lactose into lactic acid, allowing lactose-intolerant individuals to enjoy dairy without stomach cramps!"
                        }
                    },
                    {
                        "type": "suggested_video",
                        "title": "Scientific Dairy Fermentation: Mala and Yoghurt Production",
                        "content": {
                            "title": "Scientific Dairy Fermentation: Mala and Yoghurt Production",
                            "description": "Agronomic dairy video demonstrating milk pasteurization, thermometer calibration at 43 degrees, culture inoculation, and thermos incubation.",
                            "url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
                        }
                    }
                ],
                [
                    {
                        "type": "mini_activity",
                        "title": "Dairy Science Lab: Thermos Flask Yoghurt Fermentation Practicum",
                        "content": {
                            "title": "Yoghurt Fermentation Practicum",
                            "task": "1. Pasteurize 1 liter of fresh cow milk to 85°C; cool down to exactly 43°C.\n2. Inoculate with 2 tablespoons of plain live yoghurt culture.\n3. Pour into a pre-warmed thermos flask and incubate undisturbed for 5 hours.\n4. Measure pH with litmus/pH paper (target: pH 4.5); sweeten, chill, and taste.",
                            "materials": ["Fresh Milk", "Live Yoghurt Culture", "Thermometer", "Thermos Flask", "pH Strips"],
                            "safety": "Sterilize all utensils in boiling water prior to milk contact."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Core Summary: Milk & Fermented Dairy",
                        "content": {
                            "title": "Key Takeaways",
                            "text": "- **Mala uses mesophilic cultures (25–30°C for 16–18h)**.\n- **Yoghurt uses thermophilic cultures at strictly 43°C for 4–6h**.\n- **Lactic acid drops milk pH to 4.5**, coagulating proteins into a gel.\n- **The acidic pH 4.5 barrier destroys food-poisoning pathogens**."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Optimum Inoculation Temperature for Yoghurt",
                        "content": {
                            "question": "Why must boiled pasteurized milk be cooled down specifically to 42°C–45°C before adding the live yoghurt starter culture?",
                            "options": [
                                "To turn the milk into cheese immediately",
                                "Because 42°C–45°C is the biological optimum temperature where thermophilic lactic acid bacteria thrive; temperatures above 50°C kill the culture, while temperatures below 35°C stall fermentation",
                                "To allow the milk to freeze into ice cream",
                                "To evaporate all water from the milk"
                            ],
                            "answer": "B",
                            "explanation": "Yoghurt starter cultures (Streptococcus thermophilus and Lactobacillus bulgaricus) are thermophiles with an optimal growth window of 42°C to 45°C. Hotter milk denatures their cellular proteins, killing the culture, while colder milk paralyzes bacterial metabolism."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 10: Animal Origin Processing II - Honey Refining and Bottling
        # =====================================================================
        {
            "unit_order": 10,
            "unit_name": "Animal Origin Processing II - Honey Refining and Bottling",
            "unit_description": "Raw comb sorting (white comb vs dark brood comb); cold crushing with wooden plunger, primary & secondary cheesecloth straining, 24–48h settling tank; moisture content threshold (<18% stable vs >20% yeast fermentation).",
            "lesson_title": "Apiary Value Addition: Comb Sorting, Cold Straining, and Moisture Thresholds",
            "pages": [
                [
                    {
                        "type": "suggested_image",
                        "title": "Jars of Pure Refined Liquid Honey and Natural Honeycomb",
                        "content": {
                            "title": "Jars of Pure Refined Liquid Honey and Natural Honeycomb",
                            "caption": "Bottles of golden, crystal-clear refined honey alongside natural honeycomb, showing value-added apiary processing and purity."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Honey Refining",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Sort **white capped honeycombs from dark brood and pollen combs**.",
                                "Execute **cold crushing and multi-stage cheesecloth straining** without heat damage.",
                                "Utilize a **24–48 hour settling tank** to clarify honey and skim wax scum.",
                                "Analyze the **$<18\\%$ moisture safety threshold to prevent wild yeast fermentation**."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Raw Comb Sorting and Sourcing",
                        "content": {
                            "title": "Preserving Honey Aroma and Purity",
                            "text": "1. **Comb Sorting**: Separate pure white combs filled with **capped honey** from dark combs containing bee brood (larvae) or pollen. Brood larvae spoil honey color and cause protein turbidity.\n2. **THE COLD STRAINING MANDATE**: Never heat honey directly over a fire! Direct heat destroys heat-sensitive diastase and invertase enzymes, scorches delicate floral volatiles, and darkens the honey to a low commercial grade."
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "Crushing, Straining, and Gravity Clarification",
                        "content": {
                            "title": "Multi-Stage Mechanical Filtration",
                            "text": "1. **Cold Crushing**: Place sorted honeycombs in a food-grade plastic bucket. Crush with a sterile wooden plunger to break wax cells.\n2. **Primary Coarse Sieve**: Pour crushed comb through a stainless steel sieve to catch large wax chunks.\n3. **Secondary Fine Strain**: Strain through double-layered cheesecloth ($100\\text{ mesh}$).\n4. **Settling Tank (Gravity Clarification)**: Let strained honey sit undisturbed in a tall food-grade settling tank for **24 to 48 hours**. Air bubbles, tiny wax particles, and bee legs float to the top as scum and are skimmed off, leaving crystal-clear honey at the bottom tap!"
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The Moisture Safety Threshold: <18% vs. >20%",
                        "content": {
                            "title": "The Science of Honey Shelf-Life",
                            "text": "- **Under $18\\%$ Moisture**: Honey is biologically stable for centuries. Intense sugar concentration ($>80\\%$) exerts massive osmotic pressure, dehydrating any invading yeast cell.\n- **Over $20\\%$ Moisture (Unripe Honey)**: Osmotolerant wild yeasts (*Zygosaccharomyces*) activate, fermenting honey sugars into sour alcohol (mead) and carbon dioxide gas, ruining the honey!"
                        }
                    }
                ],
                [
                    {
                        "type": "comparison_table",
                        "title": "Crude Honey vs Cold-Refined Bottled Honey Comparison",
                        "content": {
                            "title": "Honey Value Addition Matrix",
                            "headers": ["Quality Parameter", "Raw Unrefined Comb Honey", "Cold-Strained Bottled Honey", "Value-Added Commercial Gain"],
                            "rows": [
                                ["Visual Clarity", "Turbid (Wax, bee parts, brood debris)", "Crystal-clear, brilliant golden liquid", "High consumer appeal & trust"],
                                ["Moisture Control", "Variable (Risk of fermentation)", "Calibrated <18% moisture (Refractometer)", "Indefinite room-temperature shelf-life"],
                                ["Enzyme & Flavor State", "Intact but dirty", "100% Intact floral aroma & enzymes", "Certified premium organic grade"],
                                ["Market Price / kg", "KES 300–400 / kg (Crude comb)", "KES 900–1,200 / kg (Glass jar)", "300% Increase in apiary revenue"]
                            ]
                        }
                    }
                ],
                [
                    {
                        "type": "mini_activity",
                        "title": "Apiary Lab: Cold Crushing, Cheesecloth Straining, and Density Water Test",
                        "content": {
                            "title": "Honey Refining Practicum",
                            "task": "1. Crush 500g of ripe capped honeycomb using a wooden plunger in a clean bowl.\n2. Pass mixture through a primary sieve and a secondary double cheesecloth.\n3. Perform the 'Water Drop Test': Drop 1 teaspoon into cold water; observe if it sinks intact as a solid bead (pure <18% moisture) or disperses rapidly (watery >20%).",
                            "materials": ["Honeycomb", "Wooden Plunger", "Cheesecloth", "Beakers", "Glass Jars"],
                            "safety": "Keep processing room bee-tight to prevent scout bee invasion."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Core Summary: Honey Refining",
                        "content": {
                            "title": "Key Takeaways",
                            "text": "- **Never heat honey over a fire**; cold straining preserves enzymes and aroma.\n- **Use a 24–48 hour settling tank** to let wax scum float to the surface.\n- **Moisture must remain strictly under 18%** to prevent wild yeast fermentation.\n- **Package in dry, airtight glass jars** for premium market pricing."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Moisture Threshold in Honey Preservation",
                        "content": {
                            "question": "What is the critical scientific reason honey must have a moisture content strictly under 18% before being bottled for commercial sale?",
                            "options": [
                                "Honey with over 20% moisture will turn into solid rock",
                                "Moisture levels above 20% allow wild osmotolerant yeasts to ferment honey sugars into sour alcohol and carbon dioxide, causing spoilage and souring",
                                "Moisture below 18% is poisonous to humans",
                                "Bees will sting any honey with under 18% moisture"
                            ],
                            "answer": "B",
                            "explanation": "At moisture levels below 18%, osmotic pressure is too high for wild yeasts to grow. If honey is harvested unripe with moisture exceeding 20%, wild yeasts proliferate, fermenting fructose and glucose into alcohol and acetic acid, ruining the honey."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 11: Animal Origin Processing III - Hides and Skins Preserving
        # =====================================================================
        {
            "unit_order": 11,
            "unit_name": "Animal Origin Processing III - Hides and Skins Preserving",
            "unit_description": "Hides (cattle) vs skins (goats/sheep); 2-hour post-slaughter window; washing & fleshing over curved beam; wet salting (30% weight) vs shaded dry salting.",
            "lesson_title": "Leather By-Product Engineering: Hides & Skins Fleshing, Salting Curing, and Defect Prevention",
            "pages": [
                [
                    {
                        "type": "suggested_image",
                        "title": "Historical Curing and Salting of Animal Hides for Leather Tanning",
                        "content": {
                            "title": "Historical Curing and Salting of Animal Hides for Leather Tanning",
                            "caption": "An animal hide being prepared and salt-cured on a sloped beam, illustrating fleshing to remove subcutaneous fat and prevent bacterial decay."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Hides & Skins Preserving",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Distinguish between **Hides (large cattle/camel)** and **Skins (goats/sheep/rabbits)**.",
                                "Execute **washing and fleshing over a curved beam within 2 hours of slaughter**.",
                                "Master **Wet Salting (30% weight in sloped stacks) and Shaded Dry Salting**.",
                                "Eliminate common leather defects: **gouge marks, putrefaction spots, and direct sun damage**."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Hides and Skins as Value-Added Farm Assets",
                        "content": {
                            "title": "Turning Slaughter By-Products into Commercial Leather",
                            "text": "- **Classification**: **Hide** refers to the pelt of large livestock (cattle, camels, horses); **Skin** refers to small livestock (goats, sheep, rabbits).\n- **The 2-Hour Window**: Freshly flayed pelts are warm ($38^\\circ\\text{C}$), wet, and protein-rich. Bacteria begin decomposing the dermal collagen fiber network within **2 hours** of slaughter, causing permanent hair slip and rot if not cured immediately!"
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "Washing and the Critical Fleshing Step",
                        "content": {
                            "title": "Scraping Away Fat to Permit Salt Penetration",
                            "text": "1. **Washing**: Rinse off dung, blood, and dirt in cold running water.\n2. **The Fleshing Protocol**: Drape the hide, flesh-side up, over a smooth, curved wooden beam. Use a dull, curved fleshing knife to scrape away all remaining subcutaneous fat, muscle tissue, and blood vessels.\n3. **Why Fleshing is Non-Negotiable**: Subcutaneous fat is impermeable to salt brine. Leaving fat patches traps moisture underneath, blocking salt penetration and creating localized **greasy putrefaction rot holes**!"
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Salting and Curing Methods: Wet vs. Dry Salting",
                        "content": {
                            "title": "Halting Bacterial Decomposition Through Dehydration",
                            "text": "- **Wet Salting**: Apply coarse salt ($30\\%$ of hide weight) evenly across the flesh side. Stack hides flesh-to-flesh on a sloped concrete floor for **14 to 21 days** to allow brine liquid to drain away freely.\n- **Dry Salting (Shaded Suspension)**: Rub salt onto the skin, then lace it to a wooden frame inside a dry, **shaded, well-ventilated barn**.\n- **NEVER DRY IN DIRECT HOT SUN**: Direct tropical sunlight heats the surface, gelatinizing and cooking the collagen fibers, causing the leather to become hard, brittle, and crack irreparably!"
                        }
                    }
                ],
                [
                    {
                        "type": "comparison_table",
                        "title": "Hides and Skins Preservation Methods Matrix",
                        "content": {
                            "title": "Hide & Skin Curing Protocols Comparison",
                            "headers": ["Curing Method", "Salt Application Ratio", "Drying Environment", "Primary Technical Advantage", "Critical Flaw to Avoid"],
                            "rows": [
                                ["Wet Salting", "30% hide weight (coarse salt)", "Stacked on sloped floor (14–21 days)", "Excellent flexibility & tannery yield", "Poor drainage causes salt-burn & rot"],
                                ["Dry Salting", "20% skin weight (fine salt)", "Framed in shaded, ventilated shed", "Lightweight for long transport", "Direct sunlight cooks collagen fibers"],
                                ["Air Suspension Drying", "0% Salt (Pure air drying)", "Laced to wooden frame in shade", "Zero chemical cost for remote areas", "High risk of hide beetle infestation"]
                            ]
                        }
                    }
                ],
                [
                    {
                        "type": "mini_activity",
                        "title": "Workshop Practical: Hide Fleshing and Frame Lacing Simulation",
                        "content": {
                            "title": "Hide Curing Practicum",
                            "task": "1. Inspect a freshly flayed skin or model piece.\n2. Place over a curved beam and practice using a curved scraper to remove fat.\n3. Apply coarse salt evenly across the flesh side at 30% weight.\n4. Demonstrate frame lacing in a shaded barn model.",
                            "materials": ["Skin Piece", "Curved Scraper", "Coarse Salt", "Lacing Frame"],
                            "safety": "Wear rubber gloves and sanitize hands after handling raw animal pelts."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Core Summary: Hides & Skins Preserving",
                        "content": {
                            "title": "Key Takeaways",
                            "text": "- **Preserve pelts within 2 hours of slaughter** to stop bacterial rot.\n- **Fleshing removes subcutaneous fat**, allowing complete salt penetration.\n- **Apply 30% coarse salt by weight** on a sloped draining floor.\n- **Never dry hides in direct sunlight**; sun cooks collagen fibers."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Rationale for Fleshing Hides",
                        "content": {
                            "question": "Why is the mechanical 'fleshing' step strictly mandatory before applying curing salt to an animal hide?",
                            "options": [
                                "To change the color of the fur from brown to black",
                                "To scrape off remaining fat and muscle tissue that would otherwise form a waterproof barrier, blocking salt penetration and causing localized bacterial rotting",
                                "To soften the hide so dogs can eat it",
                                "To make the hide stretch to double its size"
                            ],
                            "answer": "B",
                            "explanation": "Subcutaneous fat is water-resistant. If fat and muscle chunks are left on the skin, curing salt cannot dissolve into the underlying dermal fibers. Moisture remains trapped under the fat, allowing putrefying bacteria to destroy the leather grain."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 12: Packaging, Branding, Labeling, and Review
        # =====================================================================
        {
            "unit_order": 12,
            "unit_name": "Packaging, Branding, Labeling, and Review",
            "unit_description": "Food-grade packaging materials; mandatory legal label anatomy (product name, net weight, ingredients, manufacturer contacts, dates, batch, KEBS mark); 'Tomato Glut Value Addition' consulting case study; 8 Summative Topic Assessment MCQs.",
            "lesson_title": "Agribusiness Packaging: Food-Grade Materials, Legal Label Anatomy, and Summative Assessment",
            "pages": [
                [
                    {
                        "type": "suggested_image",
                        "title": "Commercial Retail Display of Packaged Agricultural Foods with Legal Labels",
                        "content": {
                            "title": "Commercial Retail Display of Packaged Agricultural Foods with Legal Labels",
                            "caption": "A retail shelf showing professionally packaged, sealed, and labeled agricultural foods, illustrating consumer branding and regulatory compliance."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Packaging, Labeling & Review",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Select appropriate **food-grade packaging materials (Glass, Food-Grade Plastic, Aluminum Foil, Kraft Paper)**.",
                                "Design a legally compliant label with **all 8 mandatory Kenyan regulatory components (KEBS)**.",
                                "Synthesize the **complete 12-lesson Value Addition & Processing Framework**.",
                                "Complete the comprehensive **Summative Topic Assessment**."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Food-Grade Packaging Material Engineering",
                        "content": {
                            "title": "Protecting Product Integrity and Market Appeal",
                            "text": "Packaging must protect value-added food from **oxygen, moisture, UV light, and physical crushing**:\n1. **Glass Jars / Bottles**: 100% impermeable to oxygen and moisture; inert (does not react with acidic jams or tomato sauce); allows hot-filling at $100^\\circ\\text{C}$.\n2. **Food-Grade Polyethylene / Foil Pouches**: Impermeable to water vapor; heat-sealable; lightweight for packaging crisps and dried fruit slices.\n3. **Multi-Wall Kraft Paper Bags**: Breathable; protects root and cereal flours from humidity when stored on pallets."
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "Anatomy of a Mandatory Legal Food Label",
                        "content": {
                            "title": "The 8 Mandatory Label Requirements (KEBS Standards)",
                            "text": "Under Kenya Bureau of Standards (**KEBS**) regulations, every commercial food package must display:\n1. **Brand & Product Name**: Clear, prominent statement of identity (e.g., *'Nandi Pure Mountain Honey'*).\n2. **Net Weight / Volume**: In metric units (e.g., *'Net Weight: 500g'*).\n3. **Complete Ingredients List**: Listed in **descending order of proportion by weight**.\n4. **Manufacturer Name & Physical Address**: City, street, and registered company name.\n5. **Date of Manufacture & Expiry / Best-Before Date**: Explicit DD/MM/YYYY.\n6. **Batch / Lot Number**: For product traceability during food safety recalls.\n7. **Storage Instructions**: E.g., *'Store in a cool, dry place away from direct sunlight'*.\n8. **Standardization / Certification Mark**: Valid KEBS quality permit logo."
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Food-Safe Product Packaging & Mandatory Legal Label Anatomy",
                        "content": {
                            "title": "Food-Safe Product Packaging & Mandatory Legal Label Anatomy",
                            "caption": "Label anatomy: 1 Product Name -> 2 Net Weight (500g) -> 3 Ingredients in Descending Order -> 4 Manufacturer Address -> 5 Mfg & Expiry Dates -> 6 Batch Lot Number -> 7 Storage Conditions -> 8 KEBS Standardization Mark."
                        }
                    }
                ],
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Master Agricultural Product Processing & Value Addition Lifecycle Matrix",
                        "content": {
                            "title": "Master Agricultural Product Processing & Value Addition Lifecycle Matrix",
                            "caption": "Master value addition pipeline: 1 Harvest & Post-Harvest Mitigation -> 2 Preservation Method (Thermal, Osmosis, Fermentation, Drying) -> 3 Processing Practicals (Plant & Animal) -> 4 Food-Grade Packaging -> 5 Mandatory Legal Labeling -> 6 Market Distribution & High Profit."
                        }
                    }
                ],
                [
                    {
                        "type": "mini_activity",
                        "title": "Performance Task: The 'Tomato Glut Value Addition' Agribusiness Plan",
                        "content": {
                            "title": "Tomato Glut Agribusiness Consulting Case",
                            "task": "A youth group harvests 500kg of fresh tomatoes weekly. During peak glut, prices crash to KES 10/kg, and half the crop rots unsold.\n\n**Your Deliverable**: Design a Tomato Value Addition Protocol:\n1. Select a processed product (Tomato Jam, Sauce, or Sun-Dried Tomatoes).\n2. Detail the 5-step processing pipeline (Blanching, Formulating, Boiling, Bottling).\n3. Design a complete 8-point legal label for the jar.\n4. Calculate the financial profit margin over raw tomato sales.",
                            "materials": ["Case Handout", "Response Template", "Pen"],
                            "safety": "Ensure rigorous, evidence-based agribusiness calculations."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Core Summary: Packaging & Labeling",
                        "content": {
                            "title": "Key Takeaways",
                            "text": "- **Use food-grade glass, foil, and Kraft paper** to block moisture and oxygen.\n- **List ingredients in descending order of weight** on all food labels.\n- **Display manufacturing dates, expiry dates, batch codes, and KEBS marks**.\n- **Value addition transforms distress crops into profitable consumer brands**."
                        }
                    }
                ],
                # Pages 5 to 8: 8 Summative Assessment MCQs
                [
                    {
                        "type": "knowledge_check",
                        "title": "Summative MCQ 1: Biological Role of Vegetable Blanching",
                        "content": {
                            "question": "What is the primary biological and nutritional function of blanching green vegetables in boiling water before freezing or solar drying?",
                            "options": [
                                "To add artificial food coloring to the leaves",
                                "To thermally deactivate internal ripening enzymes that would otherwise cause browning, off-flavors, and rapid Vitamin C degradation",
                                "To turn the vegetables into liquid juice",
                                "To make the vegetables double in weight"
                            ],
                            "answer": "B",
                            "explanation": "Blanching exposes vegetables to brief boiling heat (1–2 minutes), which denatures native enzymes (catalase, peroxidase, polyphenol oxidase). This arrests enzymatic browning, preserves green chlorophyll color, and locks in essential vitamins."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Summative MCQ 2: The Jam Preservation Triangle",
                        "content": {
                            "question": "Which combination of three scientific principles forms the 'Jam Preservation Triangle' that allows fruit and tomato jams to store safely for over a year at room temperature?",
                            "options": [
                                "Freezing temperatures, vacuum pumping, and electrical radiation",
                                "Thermal kill (boiling at 104°C), High Acidity (lemon juice citric acid pH <4.6), and Osmotic Dehydration (high sugar concentration binding free water)",
                                "Adding synthetic chemical insecticides, direct sunlight, and raw water",
                                "Fermenting with wild yeasts in open buckets"
                            ],
                            "answer": "B",
                            "explanation": "Jam preservation relies on three interlocking barriers: boiling destroys active vegetative microbes, high acidity (pH <4.6) prevents bacterial spore germination, and high sugar content creates hypertonic osmotic pressure that dehydrates any invading microbe."
                        }
                    }
                ],
                [
                    {
                        "type": "knowledge_check",
                        "title": "Summative MCQ 3: Pasteurization vs Boiling of Fruit Juices",
                        "content": {
                            "question": "Why is mild thermal pasteurization at 72°C–75°C for 15 seconds preferred over boiling at 100°C for fruit juice preservation?",
                            "options": [
                                "Boiling juice makes it turn into plastic",
                                "Pasteurization destroys active fermenting yeasts and pathogens while preserving fresh aroma volatiles and heat-fragile Vitamin C, whereas boiling scorches sugars and destroys vitamins",
                                "Boiled juice is illegal to sell in East Africa",
                                "Pasteurization turns the juice into cow milk"
                            ],
                            "answer": "B",
                            "explanation": "Ascorbic acid (Vitamin C) and delicate fruit aroma esters are heat-sensitive. Pasteurization at 72–75°C delivers the necessary microbial kill without cooking the juice, whereas 100°C boiling caramelizes fructose and destroys the nutritional profile."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Summative MCQ 4: Safe Cassava Detoxification Pipeline",
                        "content": {
                            "question": "What is the critical food safety reason why raw bitter cassava roots must be thickly peeled, chipped, soaked for 3 days, and solar-dried before milling into flour?",
                            "options": [
                                "To allow weevils to eat the root starch",
                                "To leach out, hydrolyze, and destroy lethal cyanogenic glycosides that release deadly hydrogen cyanide gas if consumed raw",
                                "To make the flour turn bright yellow",
                                "To make the flour dissolve into water instantly"
                            ],
                            "answer": "B",
                            "explanation": "Raw bitter cassava contains high concentrations of toxic cyanogenic glycosides. Thick peeling removes the high-cyanide outer cortex, 72-hour water soaking ferments and leaches out the soluble toxins, and solar drying evaporates residual cyanide to safe levels (<10 ppm)."
                        }
                    }
                ],
                [
                    {
                        "type": "knowledge_check",
                        "title": "Summative MCQ 5: Biological Mechanism of Dairy Yoghurt Fermentation",
                        "content": {
                            "question": "How do Streptococcus thermophilus and Lactobacillus bulgaricus bacteria preserve milk and convert it into thick yoghurt during 43°C incubation?",
                            "options": [
                                "They freeze the milk into solid ice",
                                "They consume milk sugar (lactose) and produce lactic acid, dropping the pH to 4.5, which coagulates milk proteins into a gel and creates an acidic barrier that halts pathogen growth",
                                "They filter out water through mechanical osmosis",
                                "They add synthetic chemical preservatives to the milk"
                            ],
                            "answer": "B",
                            "explanation": "Yoghurt bacteria ferment lactose into lactic acid. As lactic acid accumulates, the milk pH drops to 4.5, which causes casein proteins to precipitate into a smooth gel. The acidic environment destroys harmful food poisoning bacteria like Salmonella and E. coli."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Summative MCQ 6: Moisture Safety Limit in Pure Honey",
                        "content": {
                            "question": "What is the mandatory moisture safety threshold required to prevent wild yeast fermentation in commercial bottled honey?",
                            "options": [
                                "Above 50% moisture",
                                "Strictly under 18% moisture (preventing osmotolerant wild yeasts from fermenting sugars into sour alcohol)",
                                "Exactly 90% water content",
                                "Moisture content does not affect honey preservation"
                            ],
                            "answer": "B",
                            "explanation": "Honey with moisture below 18% exerts massive osmotic pressure that inhibits yeast growth. If harvested with moisture above 20%, wild yeasts proliferate, fermenting glucose and fructose into sour alcohol and carbon dioxide, ruining the honey."
                        }
                    }
                ],
                [
                    {
                        "type": "knowledge_check",
                        "title": "Summative MCQ 7: Purpose of Fleshing Hides and Skins",
                        "content": {
                            "question": "Why is the mechanical fleshing of animal hides and skins on a curved beam mandatory before applying curing salt?",
                            "options": [
                                "To dye the leather fur green",
                                "To scrape off subcutaneous fat and muscle tissues that would block salt penetration and trap moisture, preventing localized putrefaction and rot holes",
                                "To sew the hide into shoes immediately",
                                "To make the hide heavier for selling by weight"
                            ],
                            "answer": "B",
                            "explanation": "Subcutaneous fat is impermeable to salt brine. If left on the hide, fat chunks block salt penetration into the collagen fibers beneath, trapping moisture and allowing putrefying bacteria to destroy the leather."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Summative MCQ 8: Regulatory Order of Ingredients on Food Labels",
                        "content": {
                            "question": "Under KEBS and international food labeling standards, in what specific order must ingredients be listed on a commercial food package?",
                            "options": [
                                "In alphabetical order from A to Z",
                                "In descending order of proportion by weight (the ingredient present in the largest quantity is listed first)",
                                "In order of cost from cheapest to most expensive",
                                "In random order chosen by the printer"
                            ],
                            "answer": "B",
                            "explanation": "Food labeling laws require ingredients to be listed in descending order of predominance by weight at the time of manufacture. The ingredient that makes up the largest proportion must appear first on the list."
                        }
                    }
                ],
                # Page 8: Capstone Summary
                [
                    {
                        "type": "summary",
                        "title": "Topic 14 Capstone Summary: Product Processing and Value Addition Mastery",
                        "content": {
                            "title": "Mastery Overview: Grade 10 Agricultural Value Addition",
                            "text": "Congratulations on mastering **Topic 14: Product Processing and Value Addition**!\n\nYou have mastered:\n- **Foundations of Value Addition**: Transforming raw commodities into high-margin consumer products; capturing retail profits.\n- **Post-Harvest Loss Mitigation**: Eliminating the 30–40% loss bottleneck through moisture removal, thermal processing, and acidification.\n- **Food Security & Nutrition**: Strengthening Availability and Stability; formulating composite flours with millet, sorghum, groundnuts, and *Omena*.\n- **The 6 Preservation Methods**: Dehydration (<12%), Milling, Thermal (72°C pasteurization), Chemical (low pH & sugar/salt osmosis), Fermentation, and Extraction.\n- **Horticultural Processing**: Potato/banana crisps (1mm slice, 175°C fry, +200% margin); Tomato jam and the Preservation Triangle; Fruit nectar formulation (30% pulp, 10% sugar, 60% water); Cassava cyanide detoxification (peel, soak 3 days, solar dry).\n- **Animal Product Processing**: Mala mesophilic fermentation; Scientific yoghurt thermophilic culture (*43°C for 4–6h, pH 4.5*); Honey cold straining and <18% moisture threshold; Hides/skins fleshing and 30% salt curing.\n- **Packaging & Legal Labeling**: Food-grade materials (glass, foil, Kraft paper) and the 8 mandatory KEBS label components (ingredients in descending order of weight, batch, dates, KEBS mark)."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Topic 14 Final Takeaway",
                        "content": {
                            "title": "The Value Addition Agribusiness Maxim",
                            "text": "Never sell raw commodities at distress farm-gate prices. Process surplus crops, preserve nutrients, package in food-grade materials with compliant labels, and capture high retail value. Value addition builds wealth, stabilizes household food security, and eliminates post-harvest waste."
                        }
                    }
                ]
            ]
        }
    ]

@transaction.atomic
def ingest_grade10_topic14(replace=False):
    """Executes the complete production ingestion of Grade 10 Agriculture Topic 14: Product Processing and Value Addition."""
    print("=" * 80)
    print("STARTING INGESTION: CBC Grade 10 Agriculture — Topic 14: Product Processing and Value Addition")
    print("=" * 80)

    curriculum = Curriculum.objects.filter(name__iexact="CBC").first()
    grade = Grade.objects.filter(curriculum=curriculum, name__icontains="10").first()
    subject = Subject.objects.filter(grade=grade, name__iexact="Agriculture").first()

    assert curriculum and grade and subject, "Curriculum/Grade/Subject not found!"

    topic_name = "Product Processing and Value Addition"
    topic = Topic.objects.filter(subject=subject, name=topic_name).first()
    if not topic:
        topic = Topic.objects.create(
            subject=subject,
            name=topic_name,
            description="Comprehensive vocational and scientific training in agricultural product processing and value addition: post-harvest loss mitigation, food security fortification, composite flours, potato/banana crisps, tomato jams, fruit juices, cassava detoxification, fermented dairy (Mala/Yoghurt), honey refining, hides & skins curing, food-grade packaging, and KEBS regulatory labeling.",
            order=14
        )
        print(f"Created Topic 14: {topic.name} (ID: {topic.id})")
    else:
        topic.order = 14
        topic.description = "Comprehensive vocational and scientific training in agricultural product processing and value addition: post-harvest loss mitigation, food security fortification, composite flours, potato/banana crisps, tomato jams, fruit juices, cassava detoxification, fermented dairy (Mala/Yoghurt), honey refining, hides & skins curing, food-grade packaging, and KEBS regulatory labeling."
        topic.save()
        print(f"Resolved Topic 14: {topic.name} (ID: {topic.id})")

    if replace:
        print("Flag --replace active: Clearing existing LearningUnits and Lessons for Topic 14...")
        topic.learning_units.all().delete()
        topic.lessons.all().delete()

    curriculum_data = build_topic14_curriculum()
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
                    "topic_order": 14,
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
                    block_id=f"g10_agri_t14_u{u_order}_p{page_idx}_b{comp_idx}",
                    block_type=b_type,
                    component_type=b_type,
                    title=b_title,
                    content=b_content,
                    order=block_order_counter,
                    page_number=page_idx,
                    component_order=comp_idx,
                    page_title=b_title if comp_idx == 1 else None,
                    metadata={"topic_order": 14, "unit_order": u_order, "page": page_idx}
                )
                block_order_counter += 1
                total_blocks += 1

        print(f"  Ingested Unit {u_order}: {u_name} -> Lesson '{l_title}' ({len(pages)} Pages, {block_order_counter - 1} Blocks)")

    print("=" * 80)
    print(f"INGESTION COMPLETE: Topic 14 '{topic.name}'")
    print(f"  Total Units:   {total_units}")
    print(f"  Total Lessons: {total_lessons}")
    print(f"  Total Pages:   {total_pages}")
    print(f"  Total Blocks:  {total_blocks}")
    print("=" * 80)

if __name__ == "__main__":
    replace_flag = "--replace" in sys.argv
    ingest_grade10_topic14(replace=replace_flag)
