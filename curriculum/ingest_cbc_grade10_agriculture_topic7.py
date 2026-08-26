"""
VLearn CBC Grade 10 Agriculture — Topic 7: General Crop Harvesting
Production Ingestion Engine (Deep Senior Secondary Pedagogical Edition)

Curriculum: CBC (ID: 5)
Grade: Grade 10 (ID: 5, Level: 10)
Subject: Agriculture
Topic: General Crop Harvesting (Topic Order: 7)

Decomposed into 10 Learning Units & 10 Published Lessons:
  1. Introduction and Harvest Factors (5 Pages, 11 Blocks)
  2. Pre-Harvest Practices (5 Pages, 11 Blocks)
  3. Harvesting Methods (5 Pages, 11 Blocks)
  4. Stage of Growth and Harvesting (5 Pages, 11 Blocks)
  5. Harvesting for Purpose (5 Pages, 11 Blocks)
  6. Harvesting Tubers (Potatoes) (5 Pages, 11 Blocks)
  7. Harvesting Cereals (Maize) (5 Pages, 11 Blocks)
  8. Post-Harvest Cereal Practice (5 Pages, 11 Blocks)
  9. Storage and Quality Protection (5 Pages, 11 Blocks)
  10. Module Review and Performance Task (8 Pages, 17 Blocks)
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

def build_topic7_curriculum():
    """Returns the comprehensive pedagogical page and block structure for Grade 10 Topic 7: General Crop Harvesting."""
    return [
        # =====================================================================
        # LESSON 1: Introduction and Harvest Factors
        # =====================================================================
        {
            "unit_order": 1,
            "unit_name": "Introduction and Harvest Factors",
            "unit_description": "Definition of crop harvesting; 4 primary determinants of harvest timing (physiological maturity, moisture percentage, weather conditions, market purpose); economic consequences of untimely harvesting on yield, quality, and market revenue.",
            "lesson_title": "Principles of Crop Harvesting and Harvest Determinants",
            "pages": [
                [
                    {
                        "type": "suggested_image",
                        "title": "Commercial Cereal Grain Harvesting Operation in Large-Scale Field",
                        "content": {
                            "title": "Commercial Cereal Grain Harvesting Operation in Large-Scale Field",
                            "caption": "Gathering mature agricultural crops at peak physiological maturity to maximize grain yield and preserve market quality."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Harvest Factors",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Define **crop harvesting** in an agricultural enterprise context.",
                                "Analyze the **4 key determinants of harvest timing** (growth stage, moisture content, weather, intended purpose).",
                                "Evaluate the severe economic losses caused by **premature vs delayed harvesting**.",
                                "Perform an on-farm diagnostic assessment of crop harvest readiness."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "What is Crop Harvesting?",
                        "content": {
                            "title": "The Culmination of the Cropping Cycle",
                            "text": "**Harvesting** is the deliberate process of gathering mature, economically valuable crop produce from the field.\n\n- **Agribusiness Significance**: Represents the final realization of all land preparation, certified seed investments, fertilizer inputs, irrigation, and labor.\n- **The Double Mandate: Yield and Quality**: Timely harvesting determines not only total tonnage recovered (quantity) but also food safety, seed viability, sugar/starch content, and shelf life (quality).\n- **The Risk of Poor Timing**: Harvesting prematurely yields shriveled, low-starch grain with high moisture; harvesting late exposes crops to grain-boring beetles, fungal rot, bird theft, and pod shattering."
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "The 4 Key Determinants of Harvest Timing",
                        "content": {
                            "title": "When is the Crop Truly Ready?",
                            "text": "1. **Stage of Growth (Physiological Maturity)**: The biological point where dry matter accumulation is 100% complete and the parent plant cuts off nutrient translocation to the seeds/tubers.\n2. **Moisture Content**: Grains must drop to safe handling moisture in the field ($18\\text{--}20\\%$) before final drying down to the $13\\text{--}14\\%$ storage threshold.\n3. **Climatic Weather Conditions**: Harvesting must be conducted during clear, dry, sunny days. Rain during harvest causes soil clumping on tubers and promotes carcinogenic fungal molds (*Aspergillus flavus*).\n4. **Market Destination / Intended Purpose**: Fresh market produce is harvested at partial maturity (e.g. breaker tomatoes for transport), whereas processing and seed crops require full maturity."
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "The 4 Key Determinants of Crop Harvest Timing",
                        "content": {
                            "title": "The 4 Key Determinants of Crop Harvest Timing",
                            "caption": "Conceptual decision matrix showcasing: 1 Physiological Maturity (Nutrient Peak), 2 Moisture Content (Storage Safety), 3 Weather Window (Dry Sunny Skies), and 4 Market Destination (Fresh vs Storage vs Seed)."
                        }
                    }
                ],
                [
                    {
                        "type": "comparison_table",
                        "title": "Premature Harvesting vs Optimal Timing vs Delayed Harvesting",
                        "content": {
                            "title": "Harvest Timing Impact Matrix",
                            "headers": ["Harvest Timing", "Physical Produce Condition", "Moisture & Mold Risk", "Economic Market Impact"],
                            "rows": [
                                ["Premature (Too Early)", "Shriveled, wrinkled grains; soft watery tubers; low starch", "Very High moisture (>25%); rapid fungal decay", "Downgraded quality; severe weight loss; low price"],
                                ["Optimal Physiological Maturity", "Plump, dense grains; fully cured tuber skin; max starch", "Safe field dry-down range; optimal storage potential", "Grade 1 premium price; maximum yield tonnage"],
                                ["Delayed (Too Late)", "Over-dry, cracked grains; rotten tubers; insect boring", "Re-wets with rain; aflatoxin mold development", "High yield loss from shattering, birds, and rotting"]
                            ]
                        }
                    },
                    {
                        "type": "mini_activity",
                        "title": "Field Practical: Crop Harvest Maturity Diagnostic Audit",
                        "content": {
                            "title": "School Farm Harvest Readiness Walk",
                            "task": "1. Walk to the school farm vegetable and cereal plots.\n2. Inspect 10 maize cobs and 5 potato plants.\n3. Record: Husk color (green vs dry brown), black layer presence on grains, and potato vine yellowing.\n4. Decide whether the crops should be harvested immediately or given another 10 days.",
                            "materials": ["Field Notebook", "Magnifier", "Pen"],
                            "safety": "Wear field boots; do not walk into muddy drainage furrows."
                        }
                    }
                ],
                [
                    {
                        "type": "key_takeaway",
                        "title": "Core Summary: Harvest Factors",
                        "content": {
                            "title": "Key Takeaways",
                            "text": "- **Harvesting is gathering mature produce** at maximum dry matter accumulation.\n- **Evaluate 4 determinants**: Physiological maturity, moisture, weather, and market purpose.\n- **Premature harvest causes shriveling**; delayed harvest causes shattering and pest rot.\n- **Harvest exclusively during dry, sunny weather** to prevent fatal mold contamination."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Rationale for Harvesting at Physiological Maturity",
                        "content": {
                            "question": "Why is harvesting an agricultural crop at the exact stage of physiological maturity considered a critical commercial agribusiness decision?",
                            "options": [
                                "It allows tractors to consume less diesel fuel during plowing",
                                "It ensures the crop has accumulated maximum dry matter and nutrients, guaranteeing maximum harvestable yield while preventing premature shriveling or post-mature field rotting",
                                "It forces the crop to produce second-generation flowers while in the storage bag",
                                "It changes the color of the soil from brown to black"
                            ],
                            "answer": "B",
                            "explanation": "Physiological maturity is the precise developmental milestone where nutrient transfer from the plant to the seed/tuber is 100% complete. Harvesting at this exact stage secures maximum dry weight, optimal nutritional density, and peak commercial grade, avoiding the shriveling of early harvest or the rot and pest attack of late harvest."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 2: Pre-Harvest Practices
        # =====================================================================
        {
            "unit_order": 2,
            "unit_name": "Pre-Harvest Practices",
            "unit_description": "Pre-harvest operations; haulm destruction (vine killing) in Irish potatoes 10–14 days prior (skin setting/curing, blight spore exclusion, size control); field drying in cereals (stooking, downward cob bending to avoid waterlogging).",
            "lesson_title": "Pre-Harvest Practices: Haulm Destruction and Cereal Field Drying",
            "pages": [
                [
                    {
                        "type": "suggested_image",
                        "title": "Potato Crop Field Prepared for Harvest After Haulm Destruction",
                        "content": {
                            "title": "Potato Crop Field Prepared for Harvest After Haulm Destruction",
                            "caption": "A potato field where vegetative vines have been cut 14 days prior, allowing subterranean tubers to cure and harden their outer skins."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Pre-Harvest Practices",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Define **pre-harvest practices** and explain their role in post-harvest longevity.",
                                "Analyze the biological mechanism of **haulm destruction (vine killing)** in potato farming.",
                                "Explain how haulm destruction triggers **skin setting (curing)** and blocks Late Blight pathogens.",
                                "Demonstrate pre-harvest cereal management: **field stooking and downward cob bending**."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "What are Pre-Harvest Practices?",
                        "content": {
                            "title": "Setting the Stage for a Successful Harvest",
                            "text": "**Pre-harvest practices** are specialized agronomic operations conducted in the field shortly before harvesting (typically 1 to 2 weeks prior).\n\n- **Core Objectives**: Uniformize crop ripening, harden produce protective skins, desiccate vegetative foliage to facilitate digging or combining, and lower moisture content while crops are still standing in the field.\n- **Major Examples**: **Haulm destruction (vine killing)** in root and tuber crops, and **field stooking / cob bending** in cereal crops."
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "Haulm Destruction (Vine Killing) in Irish Potatoes",
                        "content": {
                            "title": "The Science of Subterranean Skin Setting",
                            "text": "In commercial potato farming, the green above-ground foliage (haulms) is deliberately destroyed **10 to 14 days before harvest** using mechanical mowing or approved defoliant sprays:\n\n1. **Skin Setting (Hardening)**: Cutting the vines halts vegetative growth. The underground tubers immediately respond by thickening and hardening their outer periderm (skin), making them resistant to scraping and bruising during digging.\n2. **Pathogen Barrier**: Late Blight (*Phytophthora infestans*) lives on green foliage. Destroying haulms ensures rain does not wash fungal spores down into the soil to infect tubers, and prevents tubers from touching live spores during lifting.\n3. **Tuber Size Regulation**: Halts starch accumulation, preventing tubers from growing oversized and ensuring they meet Grade 1 supermarket standards."
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Potato Haulm Destruction & Subterranean Skin Setting",
                        "content": {
                            "title": "Potato Haulm Destruction & Subterranean Skin Setting",
                            "caption": "Diagram illustrating: 1 Green Vines Mowed at Soil Line, 2 Subterranean Tubers Developing Thick Cured Periderm Skin over 10-14 Days, and 3 Late Blight Spores Starved on Dead Foliage."
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "Field Drying and Cob Bending in Cereals",
                        "content": {
                            "title": "Natural Sun Drying While Standing",
                            "text": "For maize, sorghum, and millet in dry climates, farmers utilize the standing plant for preliminary moisture reduction:\n\n- **Field Stooking**: Cutting entire mature stalks at the soil base with a panga and stacking them upright in cone-shaped 'stooks'. Facilitates air circulation around cobs while clearing the ground for secondary cultivation.\n- **Downward Cob Bending**: Snapping the maize cob shank downward so the tip points to the ground. **Why it works**: Prevents rain from penetrating the open husk tip and pooling inside, stopping grain rotting, premature sprouting, and bird feeding."
                        }
                    },
                    {
                        "type": "suggested_video",
                        "title": "Vine Killing and Skin Set in Potatoes",
                        "content": {
                            "title": "Vine Killing and Skin Set in Potatoes",
                            "description": "Agronomic field demonstration showing mechanical haulm cutting, skin set testing via the thumb-rub method, and blight spore exclusion.",
                            "url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
                        }
                    }
                ],
                [
                    {
                        "type": "mini_activity",
                        "title": "Field Practical: Testing Potato Skin Set and Cob Bending",
                        "content": {
                            "title": "Pre-Harvest Conditioning Workshop",
                            "task": "1. In the potato plot, perform haulm cutting on 5 rows 14 days before harvest.\n2. Compare tubers from mowed rows vs uncut rows using the thumb-rub test.\n3. In the maize plot, practice bending 20 mature cobs downward at the shank without detaching them from the stalk.",
                            "materials": ["Sickle / Panga", "Hand Trowel", "Maize Plot", "Potato Plot"],
                            "safety": "Keep feet clear of swinging pangas; wear safety boots."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Core Summary: Pre-Harvest Operations",
                        "content": {
                            "title": "Key Takeaways",
                            "text": "- **Haulm destruction is performed 10–14 days before digging potatoes**.\n- **Vine killing hardens tuber skin (skin set)** and prevents Late Blight infection.\n- **Bending maize cobs downward** prevents rainwater from entering husks and rotting grain.\n- **Stooking stalks facilitates air drying** while freeing arable land."
                        }
                    }
                ],
                [
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Rationale for Haulm Destruction in Potatoes",
                        "content": {
                            "question": "What is the primary biological and phytosanitary reason for executing haulm destruction (vine killing) 10 to 14 days prior to harvesting Irish potatoes?",
                            "options": [
                                "To encourage the potato plants to produce flowers for honeybees",
                                "To trigger skin setting (hardening of the outer tuber periderm) to resist bruising and prevent foliar Late Blight fungal spores from washing down and infecting the tubers",
                                "To increase the nitrogen content in the underground roots",
                                "To make the soil compact and hard for tractors"
                            ],
                            "answer": "B",
                            "explanation": "Haulm destruction halts vegetative growth, stimulating the underground potato tubers to cure and harden their outer skins (suberization), which prevents skinning and bruising during harvest. Furthermore, killing the foliage destroys foliar Late Blight (Phytophthora infestans) pathogens, preventing spores from contacting and rotting tubers during digging."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 3: Harvesting Methods
        # =====================================================================
        {
            "unit_order": 3,
            "unit_name": "Harvesting Methods",
            "unit_description": "Manual harvesting (knives, sickles, pangas, digging forks, secateurs) vs mechanical combine harvesters/potato diggers; operational safety: sharp tool maintenance, 5 m machine clearance, dust masks for chaff/spores.",
            "lesson_title": "Manual and Mechanical Harvesting Operations and Field Safety",
            "pages": [
                [
                    {
                        "type": "suggested_image",
                        "title": "Mechanical Combine Harvester Operating in Cereal Grain Field",
                        "content": {
                            "title": "Mechanical Combine Harvester Operating in Cereal Grain Field",
                            "caption": "A high-capacity combine harvester cutting, threshing, and cleaning cereal grains simultaneously across large arable acreage."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Harvesting Methods & Safety",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Compare **manual harvesting vs mechanical harvesting** (cost, speed, selectivity, crop bruising).",
                                "Identify correct hand tools for harvesting cereals, tubers, and horticultural crops.",
                                "Execute strict **field safety standards** for manual cutting tools and moving machinery.",
                                "Explain why **respiratory dust masks** are mandatory during cereal threshing."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Manual vs Mechanical Harvesting",
                        "content": {
                            "title": "Choosing the Optimal Harvesting Technology",
                            "text": "1. **Manual Harvesting**:\n- Relies on human labor and specialized hand tools (sickles for rice/wheat, pangas for maize, digging forks for potatoes, secateurs for fruits).\n- **Advantages**: Very low capital cost; highly selective (harvests only ripe, undamaged produce); minimal bruising of tender crops.\n- **Disadvantages**: Extremely slow; labor bottlenecks during peak seasons; high physical fatigue.\n\n2. **Mechanical Harvesting**:\n- Uses tractor-mounted or self-propelled machinery (combine harvesters, potato diggers).\n- **Advantages**: Incredibly fast; harvests hundreds of acres within narrow sunny weather windows; minimizes field labor costs.\n- **Disadvantages**: High capital investment; non-selective (gathers weeds and green seeds); requires flat, rock-free topography."
                        }
                    }
                ],
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Manual vs Mechanical Harvesting Operational Comparison",
                        "content": {
                            "title": "Manual vs Mechanical Harvesting Operational Comparison",
                            "caption": "Comparative diagram: Manual Harvesting (Hand Tools, High Selectivity, Low Capital, High Labor) vs Mechanical Harvesting (Combine Harvesters, Ultra-Fast, Non-Selective, High Capital)."
                        }
                    },
                    {
                        "type": "comparison_table",
                        "title": "Manual vs Mechanical Harvesting Decision Matrix",
                        "content": {
                            "title": "Harvesting Methods Evaluation Matrix",
                            "headers": ["Evaluation Metric", "Manual Harvesting (Human Labor)", "Mechanical Harvesting (Combine / Digger)"],
                            "rows": [
                                ["Capital Equipment Cost", "Very Low (Hand tools: KES 500–2,000)", "Very High (Combine Harvester: KES 5M–15M)"],
                                ["Harvesting Speed & Capacity", "Slow (0.2–0.5 acres/day per worker)", "Ultra-Fast (20–50 acres/day)"],
                                ["Selectivity of Produce", "100% Selective; leaves unripe produce", "Non-selective; gathers weeds and green parts"],
                                ["Crop Bruising Risk", "Low; delicate hand placement", "Moderate to High if machine is poorly calibrated"],
                                ["Terrain Constraints", "Works on steep hills, small plots, rocky soil", "Restricted to flat, stone-free commercial fields"]
                            ]
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "Essential Safety Rules in Harvesting Operations",
                        "content": {
                            "title": "Zero Injury Field Protocols",
                            "text": "1. **Tool Sharpness & Maintenance**: Always keep cutting blades (pangas, sickles, secateurs) sharp. Blunt tools require excessive force, slip easily, and cause severe lacerations.\n2. **Machine Exclusion Zones**: Maintain a strict safety perimeter of at least **5 meters away from moving tractor implements and combine headers**. Never attempt to unclog moving machinery with engines running!\n3. **Respiratory PPE (Dust Masks)**: Threshing and shelling cereals release thick clouds of organic dust, grain hairs, and fungal spores. Always wear an N95 dust mask to prevent chronic respiratory allergic alveolitis."
                        }
                    },
                    {
                        "type": "mini_activity",
                        "title": "Field Practical: Tool Sharpening and PPE Inspection Workshop",
                        "content": {
                            "title": "Harvest Tool Maintenance and Safety Lab",
                            "task": "1. Inspect school farm harvest tools: sickles, pangas, digging forks, and secateurs.\n2. Sharpen cutting blades using an oiled carborundum whetstone at a 20-degree angle.\n3. Assemble a complete harvest PPE kit (leather gloves, gumboots, N95 dust mask, eye goggles).\n4. Demonstrate safe tool-carrying posture while walking in the field.",
                            "materials": ["Whetstone", "Lubricating Oil", "Pangas", "Secateurs", "PPE Kit"],
                            "safety": "Always sharpen blades moving away from your body; wear protective leather gloves."
                        }
                    }
                ],
                [
                    {
                        "type": "key_takeaway",
                        "title": "Core Summary: Harvesting Methods",
                        "content": {
                            "title": "Key Takeaways",
                            "text": "- **Manual harvesting is highly selective and low-cost** for smallholders.\n- **Mechanical harvesting is ultra-fast** for large commercial acreages.\n- **Keep hand tools sharp** to prevent dangerous slipping and injuries.\n- **Maintain a 5 m distance from machinery** and wear dust masks during threshing."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Limitation of Mechanical Combine Harvesting",
                        "content": {
                            "question": "Which of the following is a major agronomic limitation of mechanical combine harvesting compared to skilled manual labor?",
                            "options": [
                                "It requires a team of 500 manual laborers to follow the tractor",
                                "It is non-selective, gathering weed seeds and immature crop heads alongside mature grain, requiring secondary sorting and cleaning",
                                "It can only be operated during heavy nighttime rainstorms",
                                "It destroys all soil nitrogen permanently"
                            ],
                            "answer": "B",
                            "explanation": "Mechanical combine harvesters cut everything within their cutting header path without differentiation. Unlike human workers who selectively pick only ripe, clean cobs, machines collect weeds, green foliage, and immature heads, necessitating post-harvest mechanical cleaning, winnowing, and grading."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 4: Stage of Growth and Harvesting
        # =====================================================================
        {
            "unit_order": 4,
            "unit_name": "Stage of Growth and Harvesting",
            "unit_description": "Physiological maturity (maximum dry matter accumulation); cereal indicators (dry brown husks, the black layer test at kernel base, grain hardness); root/tuber indicators (potato vine drying & thumb-rub skin set, sweet potato white sap, cassava ground cracks).",
            "lesson_title": "Determining Crop Maturity: Physiological Indicators and Diagnostic Tests",
            "pages": [
                [
                    {
                        "type": "suggested_image",
                        "title": "Mature Maize Cobs on Dry Stalks Showing Brown Husks",
                        "content": {
                            "title": "Mature Maize Cobs on Dry Stalks Showing Brown Husks",
                            "caption": "A stand of mature maize displaying drooping cobs with desiccated brown husks indicating completion of physiological grain filling."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Crop Maturity Diagnostics",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Explain the biological concept of **physiological maturity**.",
                                "Execute the **Black Layer Diagnostic Test** on mature maize kernels.",
                                "Identify physical maturity signatures for **cereals (maize, sorghum)** and **tubers (potatoes, sweet potatoes, cassava)**.",
                                "Perform the **thumb-rub skin set test** on harvested Irish potatoes."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "What is Physiological Maturity?",
                        "content": {
                            "title": "The Biological Finish Line",
                            "text": "**Physiological maturity** is the exact developmental stage where a crop reaches its maximum dry matter (starch, protein, lipid) accumulation.\n\n- **Vascular Channel Closure**: At this moment, the vascular connection between the mother plant and the seed or storage organ seals permanently. No further nutrients can enter the produce.\n- **Harvest Readiness Window**: Once physiological maturity is reached, the crop simply loses water (drying down). The farmer must monitor the crop closely to harvest before insect boring and weather damage occur."
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "Maturity Indicators for Cereals (Maize Focus)",
                        "content": {
                            "title": "Reading the Cereal Plant's Signals",
                            "text": "1. **Husk Desiccation**: The green protective husks turn straw-brown, papery, and loosen around the cob.\n2. **THE BLACK LAYER TEST**: At full physiological maturity, a distinct dark brown or **black layer of dead cells forms at the base (tip) of individual kernels** where they attach to the cob. This confirms the nutrient channel has permanently sealed!\n3. **Foliage Senescence**: Lower leaves turn yellow and dry up, with stalks drying from the base upward.\n4. **Fingernail Dent Test**: Grains become hard and flinty; they cannot be dented with a fingernail."
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Maize Kernel Black Layer Physiological Maturity Marker",
                        "content": {
                            "title": "Maize Kernel Black Layer Physiological Maturity Marker",
                            "caption": "Anatomical cross-section of a mature maize kernel showing the starch endosperm, embryo, and the distinct black abscission layer sealing the kernel tip at physiological maturity."
                        }
                    }
                ],
                [
                    {
                        "type": "comparison_table",
                        "title": "Maturity Indicators for Major Kenyan Crops",
                        "content": {
                            "title": "Crop Maturity Diagnostic Chart",
                            "headers": ["Crop Enterprise", "Primary Visual Foliar Indicator", "Definitive Diagnostic Test", "Optimal Harvest Window"],
                            "rows": [
                                ["Maize", "Husks dry, turn brown, and droop", "Black layer forms at kernel tip; hard dent", "18–20% field moisture; dry sunny weather"],
                                ["Irish Potatoes", "Vines yellow, wither, and die down", "Thumb-rub test: skin does not slip or peel", "10–14 days after haulm destruction"],
                                ["Sweet Potatoes", "Leaves turn pale yellow and drop", "Cut tuber sap dries clear/white without blackening", "4–6 months after planting; dry soil"],
                                ["Cassava", "Leaves drop; prominent soil cracks above roots", "Sample root cuts show pure white, crisp starch", "8–12 months depending on variety"],
                                ["Tomatoes (Fresh)", "First pink/yellow color at blossom tip", "Breaker stage color break (<10% color)", "Morning harvest; firm fruit walls"]
                            ]
                        }
                    },
                    {
                        "type": "mini_activity",
                        "title": "Laboratory Practical: The Maize Kernel Black Layer Dissection Lab",
                        "content": {
                            "title": "Hands-On Maturity Dissection",
                            "task": "1. Collect 3 maize cobs: Cob A (green husk), Cob B (turning brown), Cob C (fully dry brown).\n2. Extract 3 kernels from the center of each cob.\n3. Use a hand magnifier to inspect the tip of the kernel where it joined the cob.\n4. Record which cob shows the complete black abscission layer.",
                            "materials": ["3 Sample Maize Cobs", "Hand Magnifier", "Tweezers", "Dissecting Tile"],
                            "safety": "Handle kernels carefully with tweezers."
                        }
                    }
                ],
                [
                    {
                        "type": "key_takeaway",
                        "title": "Core Summary: Maturity Diagnostics",
                        "content": {
                            "title": "Key Takeaways",
                            "text": "- **Physiological maturity marks peak dry matter accumulation**.\n- **The black layer at the kernel tip** confirms maize is biologically mature.\n- **Potato maturity is verified by the thumb-rub skin set test**.\n- **Sweet potatoes are mature when root sap dries white** without blackening."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: The Maize Kernel Black Layer",
                        "content": {
                            "question": "What does the distinct appearance of a 'black layer' at the tip of an extracted maize kernel scientifically confirm to an agronomist?",
                            "options": [
                                "The crop has been infected with Head Smut fungal disease",
                                "The grain has achieved complete physiological maturity, and vascular nutrient transfer from the plant has permanently ceased",
                                "The grain has absorbed excess motor oil from farm tractors",
                                "The maize cob is dead and must be burned immediately"
                            ],
                            "answer": "B",
                            "explanation": "The formation of the black layer (a layer of dense, suberized cells) at the base of the kernel is the definitive physiological marker that starch accumulation is complete. It permanently seals the kernel from the cob, indicating the crop has reached 100% physiological maturity."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 5: Harvesting for Purpose
        # =====================================================================
        {
            "unit_order": 5,
            "unit_name": "Harvesting for Purpose",
            "unit_description": "Crop destination determinants: fresh market (e.g. tomato breaker stage for transport) vs processing/canning (full ripe) vs long-term storage (cured skin, low moisture) vs seed production (maximum embryo viability and vigor).",
            "lesson_title": "Harvesting for Purpose: Fresh Market, Processing, Storage, and Seed",
            "pages": [
                [
                    {
                        "type": "suggested_image",
                        "title": "Fresh Market Vegetable Produce Displayed in Commercial Crates",
                        "content": {
                            "title": "Fresh Market Vegetable Produce Displayed in Commercial Crates",
                            "caption": "Freshly harvested horticultural vegetables harvested at optimal maturity stages to meet stringent market grade specifications."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Harvesting for Purpose",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Analyze how the **intended end-use (destination)** dictates harvesting timing and methods.",
                                "Differentiate harvesting criteria for **Fresh Market vs Processing / Canning**.",
                                "Differentiate harvesting criteria for **Long-Term Food Storage vs Certified Seed Production**.",
                                "Explain why market purpose directly drives farm gross margins and product grade."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "How Market Destination Dictates Harvest Operations",
                        "content": {
                            "title": "Tailoring Harvest to the Buyer's Needs",
                            "text": "A commercial grower never harvests in isolation; the ultimate destination of the produce dictates every harvesting decision:\n\n1. **Fresh Retail Market**: Produce must have exceptional visual appearance, intact skins, and firm texture to withstand handling and transport. *Example: Harvesting tomatoes at breaker stage so they ripen during transit without crushing*.\n2. **Industrial Processing (Canning, Drying, Juicing)**: Produce is harvested fully ripe when sugar, flavor, and color concentrations are at their absolute peak, as it will be processed within hours.\n3. **Long-Term Grain / Tuber Storage**: Crops must have minimal moisture ($<14\\%$) and fully suberized, tough skins to resist storage fungi and insect boring.\n4. **Certified Seed Production**: Crops must achieve 100% physiological maturity on the plant to ensure maximum embryo vigor, complete endosperm reserves, and high germination rates ($>95\\%$)."
                        }
                    }
                ],
                [
                    {
                        "type": "comparison_table",
                        "title": "Harvesting Requirements Based on Crop Destination",
                        "content": {
                            "title": "Purpose-Driven Harvesting Matrix",
                            "headers": ["Target Destination", "Primary Quality Goal", "Optimal Harvest Maturity Stage", "Critical Handling Rule"],
                            "rows": [
                                ["Fresh Local Market", "Crispness, cosmetic perfection, flavor", "Ripe but firm (e.g. breaker/pink tomatoes)", "Harvest in cool morning; pack in ventilated crates"],
                                ["Processing / Factory", "Maximum sugar/acid brix, color density", "Fully ripe, deep red/yellow", "Rapid bulk transit directly to processing plant"],
                                ["Long-Term Food Storage", "Resistance to mold rot and insect boring", "Fully dry grain (<14% moisture); cured skins", "Stack on pallets in hermetic PICS bags"],
                                ["Certified Seed Production", "Maximum embryo vigor and germination %", "Complete physiological maturity (dry on plant)", "Gentle threshing to prevent internal embryo cracking"]
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The Seed Production Quality Mandate",
                        "content": {
                            "title": "Protecting the Living Embryo",
                            "text": "When harvesting crops for seed (e.g. hybrid maize seed, bean seed, potato tubers):\n\n- **Maximum Embryo Development**: Seeds left to dry naturally on the mother plant accumulate protective proteins and sugars that allow the embryo to remain viable during prolonged dormancy.\n- **Mechanical Impact Damage**: High-speed motorized shellers can cause microscopic internal fractures in the seed embryo, causing zero germination next season! Seed crops must be shelled gently by hand or at low machine RPM."
                        }
                    }
                ],
                [
                    {
                        "type": "mini_activity",
                        "title": "Agribusiness Practical: Formulating a Harvest Plan for 3 Market Outlets",
                        "content": {
                            "title": "Destination-Driven Harvest Specification",
                            "task": "A school farm produces 2 tons of tomatoes and 50 bags of maize:\n1. Specify the exact harvest stage for: Outlet A (Supermarket 200 km away), Outlet B (Local tomato sauce factory), Outlet C (School grain store for next term's food).\n2. Calculate the price premium of Grade 1 fresh tomatoes vs factory grade.",
                            "materials": ["Case Handout", "Price Guide", "Calculator"],
                            "safety": "Ensure realistic agribusiness market calculations."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Core Summary: Harvesting for Purpose",
                        "content": {
                            "title": "Key Takeaways",
                            "text": "- **Fresh market produce requires firmness and cosmetic perfection**.\n- **Processing crops are harvested fully ripe** for maximum flavor and brix.\n- **Storage crops require hard cured skins and low moisture (<14%)**.\n- **Seed crops require 100% embryo maturity** and gentle threshing."
                        }
                    }
                ],
                [
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Rationale for Breaker-Stage Tomato Harvesting",
                        "content": {
                            "question": "Why do commercial horticultural farmers harvest fresh-market tomatoes intended for long-distance transport at the 'breaker stage' (pink blush) rather than waiting until they are fully red and soft?",
                            "options": [
                                "Green tomatoes contain more fertilizer than red tomatoes",
                                "Breaker-stage tomatoes have firm pericarp walls that withstand physical handling and transport vibration without crushing, completing their red ripening naturally during transit",
                                "Supermarkets only sell green tomatoes to consumers",
                                "Breaker tomatoes do not require plastic crates or boxes"
                            ],
                            "answer": "B",
                            "explanation": "Fully ripe red tomatoes have softened cell walls that easily bruise, split, and crush under transport vibration, leading to catastrophic post-harvest bacterial decay. Breaker-stage fruits maintain high physical firmness, ensuring they survive transport and ripen to uniform red quality on supermarket shelves."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 6: Harvesting Tubers (Potatoes)
        # =====================================================================
        {
            "unit_order": 6,
            "unit_name": "Harvesting Tubers (Potatoes)",
            "unit_description": "Manual digging procedure (digging fork inserted 30 cm from stem, gentle leverage); preventing slicing, skinning, and bruising; 7–10 days shaded curing (suberization wound healing, greening/solanine prevention).",
            "lesson_title": "Irish Potato Harvesting: Digging Fork Technique, Bruise Prevention, and Curing",
            "pages": [
                [
                    {
                        "type": "suggested_image",
                        "title": "Manual Digging and Gathering of Fresh Irish Potatoes in Garden",
                        "content": {
                            "title": "Manual Digging and Gathering of Fresh Irish Potatoes in Garden",
                            "caption": "Carefully lifting Irish potato tubers with a digging fork inserted away from the plant ridge to prevent mechanical slicing and skin damage."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Potato Harvesting & Curing",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Execute the step-by-step **potato digging protocol using a digging fork**.",
                                "Explain why the tool must be inserted **at least 30 cm away from the plant stem**.",
                                "Analyze the causes and prevention of **tuber slicing, skinning, and bruising**.",
                                "Execute the **7 to 10-day shaded curing protocol (suberization)**."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Step-by-Step Manual Potato Harvesting",
                        "content": {
                            "title": "Lifting Underground Tubers Safely",
                            "text": "1. **Pre-Harvest Prerequisite**: Confirm haulm destruction occurred 10–14 days prior and tubers passed the thumb-rub skin set test.\n2. **Tool Selection**: Use a **digging fork** with slender rounded tines rather than a flat jembe blade (which slices through hidden tubers).\n3. **Insertion at 30 cm Distance**: Drive the fork tines vertically into the side of the ridge at least **30 cm away from the main stem**.\n4. **Gentle Leverage**: Press the fork handle downward to lever the entire soil-and-tuber mass upward to the surface.\n5. **Hand Gathering**: Gently extract tubers from loosened soil, lightly shake off adhering dirt, and place them into padded crates."
                        }
                    }
                ],
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Step-by-Step Irish Potato Digging & 30cm Fork Clearance",
                        "content": {
                            "title": "Step-by-Step Irish Potato Digging & 30cm Fork Clearance",
                            "caption": "Technical engineering schematic showing: 1 Potato ridge with tubers, 2 Digging fork inserted 30 cm away from stem, 3 Upward leverage lifting tuber cluster unbroken, and 4 Gentle placement in padded container."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The Science of Shaded Potato Curing (Suberization)",
                        "content": {
                            "title": "Healing Wounds Before Storage",
                            "text": "Immediately after gathering, potatoes must undergo **curing** before entering long-term storage:\n\n- **Procedure**: Spread tubers in a thin layer (maximum 2 tubers deep) on a clean, dry floor in a **well-ventilated, SHADED shed** for **7 to 10 days**.\n- **Suberization Mechanism**: Under warm ($15\\text{--}20^\\circ\\text{C}$), humid, shaded conditions, potato skin cells synthesize a corky layer of **suberin** across minor abrasions, healing harvest micro-wounds and blocking Soft Rot (*Erwinia*) bacteria.\n- **THE SUNLIGHT DANGER (Greening & Solanine)**: *Never cure potatoes in direct sunlight!* Sunlight stimulates chlorophyll synthesis (green skin) accompanied by toxic **solanine glycoalkaloids**, making tubers bitter and poisonous to humans!"
                        }
                    }
                ],
                [
                    {
                        "type": "comparison_table",
                        "title": "Proper vs Faulty Potato Harvesting Practices",
                        "content": {
                            "title": "Potato Harvesting Quality Matrix",
                            "headers": ["Field Action", "Agronomically Correct Technique", "Faulty Destructive Practice"],
                            "rows": [
                                ["Tool Selection", "Digging fork with rounded tines", "Flat broad jembe (Chops tubers in half)"],
                                ["Tool Insertion Point", "30 cm away from plant stem ridge", "Directly into center of plant stem (Slices tubers)"],
                                ["Container Handling", "Smooth plastic crates or padded baskets", "Throwing tubers violently into metal buckets (Bruising)"],
                                ["Curing Environment", "Well-ventilated, dark/shaded curing shed", "Spreading in direct midday sun (Greening & toxic solanine)"],
                                ["Curing Duration", "7 to 10 days (Allows complete suberization)", "Storing wet immediately without curing (Massive rot)"]
                            ]
                        }
                    },
                    {
                        "type": "mini_activity",
                        "title": "Field Practical: Potato Digging and Shaded Curing Workshop",
                        "content": {
                            "title": "Hands-On Potato Harvest Practicum",
                            "task": "1. In the school potato plot, practice inserting digging forks at 30 cm clearance.\n2. Lift 5 potato hills, count undamaged tubers vs sliced tubers.\n3. Transfer undamaged tubers to the school store, spread on dry canvas in a shaded room for 7-day curing.\n4. Re-examine cured tubers after 7 days to verify skin firmness.",
                            "materials": ["Digging Forks", "Padded Harvest Crates", "Canvas Sheet", "Potato Plot"],
                            "safety": "Keep feet clear of fork tines; wear heavy garden boots."
                        }
                    }
                ],
                [
                    {
                        "type": "key_takeaway",
                        "title": "Core Summary: Potato Harvesting",
                        "content": {
                            "title": "Key Takeaways",
                            "text": "- **Use a digging fork inserted 30 cm away from the stem** to avoid slicing tubers.\n- **Handle tubers gently in padded containers** to prevent skinning and bruising.\n- **Cure potatoes for 7–10 days in a shaded, ventilated shed** to trigger suberization.\n- **Never expose harvested potatoes to sunlight** to prevent toxic solanine greening."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Rationale for Shaded Potato Curing",
                        "content": {
                            "question": "Why must newly harvested Irish potatoes be cured in a shaded, well-ventilated room for 7 to 10 days rather than being exposed to direct open sunlight?",
                            "options": [
                                "Sunlight makes the potatoes produce flowers underground",
                                "Curing in shade triggers suberization (corky wound healing) while preventing sunlight from inducing greening and the synthesis of toxic, bitter solanine alkaloids",
                                "Shade converts the potato starch into synthetic fertilizer",
                                "Direct sunlight causes potatoes to turn into sweet potatoes"
                            ],
                            "answer": "B",
                            "explanation": "Curing allows potatoes to heal surface abrasions through suberization (forming a protective corky periderm). Curing must take place in the shade because direct solar radiation triggers chlorophyll production (greening) along with toxic solanine glycoalkaloids, rendering the tubers bitter and unsafe for human consumption."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 7: Harvesting Cereals (Maize)
        # =====================================================================
        {
            "unit_order": 7,
            "unit_name": "Harvesting Cereals (Maize)",
            "unit_description": "Manual harvesting sequence (timing, stooking, dehusking, snapping cobs, clean transport); dry sunny weather rule; preventing Aspergillus flavus fungal mold and carcinogenic aflatoxins.",
            "lesson_title": "Maize Harvesting: Field Sequence, Weather Windows, and Aflatoxin Prevention",
            "pages": [
                [
                    {
                        "type": "suggested_image",
                        "title": "Manual Maize Harvesting and Cob Snapping in Smallholder Farm",
                        "content": {
                            "title": "Manual Maize Harvesting and Cob Snapping in Smallholder Farm",
                            "caption": "A Kenyan farmer harvesting mature maize cobs in dry weather, dehusking and snapping cobs cleanly at the shank."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Maize Harvesting",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Execute the step-by-step **manual maize harvesting sequence** (dehusking, snapping, loading).",
                                "Explain why maize must be harvested strictly during **dry, sunny weather**.",
                                "Analyze the biological formation and health hazards of **aflatoxins (*Aspergillus flavus*)**.",
                                "Prevent soil and fungal contamination during field gathering."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The Step-by-Step Manual Maize Harvesting Sequence",
                        "content": {
                            "title": "Field Gathering Standard Operating Procedure",
                            "text": "1. **Maturity Verification**: Confirm dry brown husks and black layer formation on kernels.\n2. **Stooking (Optional)**: Cut stalks at base and group in upright stooks for uniform preliminary dry-down.\n3. **Dehusking**: Peel back the dry outer husks to expose the grain cob while still attached to the stalk.\n4. **Snapping**: Firmly grasp the cob, twist, and snap it off at the shank connection.\n5. **Clean Loading**: Place dehusked cobs directly into clean woven gunny bags or baskets. *NEVER throw cobs onto bare wet soil, which introduces fungal spores and dirt!*"
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "The Dry Weather Rule and Aflatoxin Prevention",
                        "content": {
                            "title": "Protecting National Food Safety",
                            "text": "Cereal grains absorb ambient humidity like sponges. Harvesting during rainy weather creates a national food security disaster:\n\n- **The Aflatoxin Danger**: When damp maize ($>18\\%$ moisture) is harvested or stored in humid conditions, the fungus ***Aspergillus flavus*** proliferates rapidly.\n- **Toxicity**: The fungus synthesizes **aflatoxins**—potent, heat-stable, carcinogenic toxins that cause acute liver failure, child stunting, immune suppression, and death in humans and livestock.\n- **Prevention Protocol**: Harvest exclusively in dry weather, never let cobs touch damp ground, and immediately initiate rapid sun-drying on clean tarpaulins."
                        }
                    },
                    {
                        "type": "comparison_table",
                        "title": "Dry Weather vs Wet Weather Harvesting Outcomes",
                        "content": {
                            "title": "Weather Impact on Maize Quality",
                            "headers": ["Harvest Condition", "Grain Physical Status", "Microbiological Safety", "Commercial Market Value"],
                            "rows": [
                                ["Dry Sunny Weather", "Hard, shiny kernels; low field moisture (18%)", "Zero mold growth; clean, safe food supply", "Grade 1 premium; certified for commercial milling"],
                                ["Wet Rainy Weather", "Wet grains; water trapped in husks; swollen kernels", "High Aspergillus flavus mold; deadly aflatoxins", "Rejected by grain board; hazardous; severe financial loss"]
                            ]
                        }
                    }
                ],
                [
                    {
                        "type": "mini_activity",
                        "title": "Field Practical: Maize Harvesting and Cob Inspection Practicum",
                        "content": {
                            "title": "School Maize Harvesting Lab",
                            "task": "1. Put on protective gloves and boots.\n2. In the school maize plot, dehusk and snap 20 mature cobs.\n3. Inspect cobs for grain weevils, ear rots, and tip damage.\n4. Sort cobs into: Grade 1 (Clean, dry cobs) vs Grade 2 (Damaged cobs for immediate separate drying).",
                            "materials": ["Harvest Sacks", "Gloves", "Maize Plot"],
                            "safety": "Avoid eye injury from dry maize leaf edges; wear protective eye goggles."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Core Summary: Maize Harvesting",
                        "content": {
                            "title": "Key Takeaways",
                            "text": "- **Dehusk and snap mature cobs cleanly** at the shank.\n- **Harvest exclusively during dry, sunny weather**.\n- **Never drop dehusked cobs onto bare wet soil**.\n- **Wet harvesting promotes *Aspergillus flavus* and deadly aflatoxins**."
                        }
                    }
                ],
                [
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Consequences of Rainy Season Maize Harvesting",
                        "content": {
                            "question": "Why is harvesting maize during heavy rainstorms extremely dangerous to public health and grain safety?",
                            "options": [
                                "Rain causes tractors to turn into steam engines",
                                "Rainwater trapped inside the cobs promotes the rapid proliferation of Aspergillus flavus mold, which produces deadly, carcinogenic aflatoxin poisons",
                                "Rain causes maize grains to turn into wheat flour",
                                "Rain prevents birds from eating the stalks"
                            ],
                            "answer": "B",
                            "explanation": "Harvesting maize in wet weather traps moisture within the cobs. Under high humidity, the opportunistic fungus Aspergillus flavus proliferates and synthesizes aflatoxins—highly toxic and carcinogenic mycotoxins that cause acute liver damage, cancer, and death in humans and livestock."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 8: Post-Harvest Cereal Practice
        # =====================================================================
        {
            "unit_order": 8,
            "unit_name": "Post-Harvest Cereal Practice",
            "unit_description": "Post-harvest operations: cob drying, shelling/threshing, winnowing/cleaning; sun-drying on clean tarpaulins in 2–5 cm layers; the critical 13–14% moisture target (stopping fungal growth, salt test, bite test).",
            "lesson_title": "Post-Harvest Processing: Drying, Shelling, Cleaning, and the 13% Moisture Target",
            "pages": [
                [
                    {
                        "type": "suggested_image",
                        "title": "Sun-Drying Shelled Maize Grains on Clean Elevated Tarpaulin",
                        "content": {
                            "title": "Sun-Drying Shelled Maize Grains on Clean Elevated Tarpaulin",
                            "caption": "Maize grains spread in a thin layer on a clean canvas tarpaulin under direct sunlight, being stirred regularly to achieve the 13% safe storage moisture threshold."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Post-Harvest Cereal Processing",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Execute the 3 core post-harvest operations: **Drying, Shelling, and Cleaning (Winnowing)**.",
                                "Explain why grains must **never be dried directly on bare soil**.",
                                "Analyze the physiological reason why **13% to 14% moisture content** is mandatory for safe storage.",
                                "Perform the **Salt Test** and **Bite Test** to estimate grain moisture content."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The Post-Harvest Cereal Processing Pipeline",
                        "content": {
                            "title": "From Field Cob to Storage-Ready Grain",
                            "text": "1. **Cob Sun-Drying**: Spread whole cobs on raised wooden cribs or tarpaulins for 2–3 days until grains detach easily from the core.\n2. **Shelling (Threshing)**: Separating grains from the central woody cob. Performed manually (rubbing cobs, hand shellers) or with motorized shellers at controlled RPM to prevent cracked seed coats.\n3. **Cleaning & Winnowing**: Utilizing wind currents or motorized blowers to separate light chaff, dust, broken tips, and weed seeds from dense, clean grain.\n4. **Final Secondary Grain Drying**: Spreading shelled grains in a **2 to 5 cm thin layer on clean tarpaulins**, stirring every 2 hours with a wooden rake."
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "The Mandatory 13% Moisture Target",
                        "content": {
                            "title": "Why 13% Moisture is the Safe Storage Zone",
                            "text": "- **Biological Stasis**: At **13% to 14% moisture content**, the respiration rate of the seed embryo drops to near zero.\n- **Mold Inactivation**: Fungi (*Aspergillus*, *Penicillium*) **cannot germinate or grow** below 14% moisture, eliminating mold rot and aflatoxin production.\n- **Insect Suppression**: Reduces reproduction rates of grain weevils.\n\n### Practical Moisture Testing Methods\n1. **Digital Moisture Meter**: Precision electrical conductivity tool (Displays exact moisture, e.g. 13.2%).\n2. **The Salt Test**: Mix dry table salt with grain in a sealed dry glass jar. If salt clings/clumps to the glass after shaking, moisture is $>15\\%$ (too wet!). If salt stays powdery, grain is $<14\\%$ (safe!).\n3. **The Bite Test**: A dry kernel cracks with a sharp, glass-like snap between teeth; a damp kernel dents softly."
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Grain Moisture Continuum: Field Wetness to 13% Safe Storage Zone",
                        "content": {
                            "title": "Grain Moisture Continuum: Field Wetness to 13% Safe Storage Zone",
                            "caption": "Moisture scale diagram showing: >25% Physiological Maturity -> 18-20% Field Harvest -> 13-14% Safe Storage Threshold (Mold Halts) -> <10% Over-dry (Grain Cracking)."
                        }
                    }
                ],
                [
                    {
                        "type": "comparison_table",
                        "title": "Sun-Drying on Tarpaulins vs Bare Soil Drying",
                        "content": {
                            "title": "Drying Surface Hygiene Matrix",
                            "headers": ["Drying Method", "Contamination Risks", "Moisture Uniformity", "Final Grain Grade & Market Value"],
                            "rows": [
                                ["Clean Canvas Tarpaulin / Concrete", "Zero dirt, stones, or animal feces", "Uniform solar heating; easy to stir and cover", "Grade 1 Export/Milling Quality; top price"],
                                ["Bare Dusty Soil Surface", "High soil dirt, pebbles, animal dung, mold spores", "Uneven drying; moisture absorbs from ground", "Downgraded / Rejected; high health risk"]
                            ]
                        }
                    },
                    {
                        "type": "mini_activity",
                        "title": "Laboratory Practical: Executing the Salt Test for Grain Moisture",
                        "content": {
                            "title": "The Glass Jar Salt Moisture Test",
                            "task": "1. Take 2 clean, completely dry glass jars with airtight lids.\n2. Jar A: Fill 3/4 with sun-dried maize; Jar B: Fill 3/4 with freshly harvested damp maize.\n3. Add 2 tablespoons of dry table salt to each jar, seal tightly, and shake vigorously for 1 minute.\n4. Let settle for 10 minutes: observe whether salt stays powdery or clumps on the glass walls.",
                            "materials": ["2 Dry Glass Jars with Lids", "Dry Table Salt", "Maize Samples", "Tablespoon"],
                            "safety": "Ensure glass jars are completely dry inside before adding grain."
                        }
                    }
                ],
                [
                    {
                        "type": "key_takeaway",
                        "title": "Core Summary: Post-Harvest Processing",
                        "content": {
                            "title": "Key Takeaways",
                            "text": "- **Follow the post-harvest pipeline**: Cob drying $\\rightarrow$ Shelling $\\rightarrow$ Winnowing $\\rightarrow$ Secondary drying.\n- **Never dry grain directly on bare soil**; always use clean tarpaulins.\n- **Dry maize to 13%–14% moisture** to halt all fungal mold and aflatoxins.\n- **Verify moisture using moisture meters, the salt test, or bite test**."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: The 13% Moisture Target Rationale",
                        "content": {
                            "question": "What is the critical scientific reason why maize grain must be dried down to a moisture content of 13% to 14% before being placed into long-term storage bags?",
                            "options": [
                                "To make the grain heavy so it sells for more money",
                                "At 13% to 14% moisture, the seed respiration rate is minimal, and fungal molds (such as Aspergillus) cannot germinate or synthesize dangerous toxins",
                                "To turn the maize grain into liquid starch",
                                "Because digital moisture meters only have the number 13 on their screens"
                            ],
                            "answer": "B",
                            "explanation": "Fungal spores (including Aspergillus and Penicillium) require available free moisture (>15%) to germinate and grow. When grain is dried to 13%–14% moisture, cellular water is locked, seed respiration is minimal, and fungi cannot grow, guaranteeing safe, mold-free storage for months."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 9: Storage and Quality Protection
        # =====================================================================
        {
            "unit_order": 9,
            "unit_name": "Storage and Quality Protection",
            "unit_description": "Storage structures (improved granaries with downward metal rat guards, silos, bag storage on wooden pallets); Hermetic PICS bag technology (2 HDPE inner liners + woven outer bag, insect asphyxiation below 5% O₂); controlling Sitophilus zeamais weevils and rodents.",
            "lesson_title": "Grain Storage Structures, Hermetic PICS Bag Technology, and Pest Defense",
            "pages": [
                [
                    {
                        "type": "suggested_image",
                        "title": "Traditional Elevated Granary Fitted with Metal Rat Guards in Kenya",
                        "content": {
                            "title": "Traditional Elevated Granary Fitted with Metal Rat Guards in Kenya",
                            "caption": "An improved traditional grain store elevated above ground level with downward metal rat baffles on support posts to prevent rodent entry."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Storage & Pest Defense",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Compare grain storage structures (**improved granaries, metal silos, bag storage on pallets**).",
                                "Explain the mechanical design and function of **downward metal rat guards**.",
                                "Analyze the biochemical operation of **Hermetic PICS bags** (suffocating insects below 5% O₂).",
                                "Formulate pest defense protocols against the **Maize Weevil (*Sitophilus zeamais*)** and rodents."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Modern and Improved Grain Storage Structures",
                        "content": {
                            "title": "Safeguarding the Harvested Wealth",
                            "text": "1. **Improved Traditional Granary**: Elevated 1 m off the ground on sturdy hardwood posts fitted with **downward-facing metal conical rat guards (baffles)** that prevent rodents from climbing.\n2. **Airtight Metal Silos**: Galvanized steel cylinders with hermetic top loading and bottom discharge chutes; 100% insect, rodent, and thief-proof.\n3. **Warehouse Bag Stacking on Pallets**: Pack grain in clean jute or polypropylene bags. **THE PALLET RULE**: Always stack bags on elevated **wooden pallets at least 15 cm off concrete floors and 50 cm away from walls** to prevent concrete moisture seepage and facilitate air circulation."
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "Hermetic Storage Technology (PICS Bags)",
                        "content": {
                            "title": "Chemical-Free Insect Asphyxiation",
                            "text": "**Purdue Improved Crop Storage (PICS) bags** are a revolutionary, chemical-free technology for smallholder grain preservation:\n\n- **Tri-Layer Architecture**: Consists of **two inner high-density polyethylene (HDPE) liners** (80 microns thick) enclosed within an outer woven polypropylene protective sack.\n- **The Suffocation Mechanism**:\n  1. Dry grain ($<13\\%$ moisture) containing live weevil eggs or adults is loaded into the bag.\n  2. Each inner liner is twisted and tied tightly with cord, creating an **airtight hermetic seal**.\n  3. The living insects and grain embryos rapidly consume the trapped oxygen ($O_2$) and release carbon dioxide ($CO_2$).\n  4. Within days, oxygen levels plummet below **5%**; adult insects, larvae, and eggs **asphyxiate (suffocate) and die**!\n  5. Zero chemical pesticide dusts are needed, making grain 100% organic and food-safe!"
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Hermetic PICS Bag Cross-Section & Oxygen Depletion Asphyxiation Mechanism",
                        "content": {
                            "title": "Hermetic PICS Bag Cross-Section & Oxygen Depletion Asphyxiation Mechanism",
                            "caption": "Cross-sectional structural schematic: 1 Outer Woven Polypropylene Sack, 2 Middle 80-micron HDPE Liner, 3 Inner 80-micron HDPE Liner, and 4 Internal Gas Balance (O₂ Drops <5%, CO₂ Rises, Insects Asphyxiate)."
                        }
                    }
                ],
                [
                    {
                        "type": "comparison_table",
                        "title": "Storage Methods Comparison: Conventional vs Hermetic vs Silos",
                        "content": {
                            "title": "Storage Technology Evaluation Matrix",
                            "headers": ["Storage Method", "Pest Defense Mechanism", "Chemical Dust Required?", "Storage Lifespan", "Cost & Scalability"],
                            "rows": [
                                ["Standard Jute/Poly Bags", "None; relies on ambient air", "YES (Must mix with Actellic Super dust)", "3–6 Months (High weevil risk)", "Lowest initial cost; high chemical expense"],
                                ["Hermetic PICS Bags", "Oxygen depletion asphyxiation (<5% O₂)", "NO (100% Chemical-Free)", "1 to 2 Years completely insect-free", "Low cost; reusable for 3 seasons"],
                                ["Airtight Metal Silo", "Airtight oxygen depletion & physical barrier", "NO (100% Chemical-Free)", "2 to 3+ Years; rodent/thief proof", "High initial investment; lasts 20+ years"]
                            ]
                        }
                    },
                    {
                        "type": "mini_activity",
                        "title": "Field Practical: PICS Bag Inspection and Sealing Demonstration",
                        "content": {
                            "title": "Hands-On Hermetic Bag Sealing Protocol",
                            "task": "1. Inspect a PICS bag: verify 2 transparent HDPE inner liners inside the outer woven bag.\n2. Check liners for puncture holes against a light source.\n3. Fill with 50 kg dried maize, compress to remove air pockets, and twist-tie each liner separately with twine.\n4. Stack on a wooden pallet and record storage date.",
                            "materials": ["PICS Hermetic Bag", "50kg Dried Maize", "Twine", "Wooden Pallet"],
                            "safety": "Avoid sharp objects that could puncture plastic liners."
                        }
                    }
                ],
                [
                    {
                        "type": "key_takeaway",
                        "title": "Core Summary: Storage & Protection",
                        "content": {
                            "title": "Key Takeaways",
                            "text": "- **Stack grain bags on wooden pallets** away from cold, damp concrete floors.\n- **Fit granary posts with downward metal rat guards** to block rodents.\n- **PICS hermetic bags kill weevils by oxygen depletion (<5% O₂)** without chemicals.\n- **Tie each PICS inner liner separately** to ensure a 100% airtight seal."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: PICS Bag Insect Asphyxiation Mechanism",
                        "content": {
                            "question": "How do hermetic storage bags (such as PICS bags) eradicate maize weevils and preserve stored grain without using synthetic chemical pesticide dusts?",
                            "options": [
                                "The plastic bags emit high-frequency electrical pulses that shock the insects",
                                "The two airtight inner HDPE liners create an airtight seal; the insects and grain consume the trapped oxygen, dropping O₂ below 5%, which suffocates and kills all insects, larvae, and eggs",
                                "The bags are lined with sticky honey that traps weevils",
                                "The bags turn the grain into solid concrete that weevils cannot bite"
                            ],
                            "answer": "B",
                            "explanation": "Hermetic PICS bags utilize airtight physical barriers (two 80-micron HDPE liners). As insects, micro-organisms, and grain respire inside the sealed bag, they consume the limited oxygen. Once oxygen levels fall below 5%, weevil adults, larvae, and developing eggs die of asphyxiation, protecting the grain safely without chemical residues."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 10: Module Review and Performance Task
        # =====================================================================
        {
            "unit_order": 10,
            "unit_name": "Module Review and Performance Task",
            "unit_description": "Complete harvest value chain synthesis; Farm Harvest and Storage Portfolio task; 8 Summative Topic Assessment MCQs covering the complete Topic 7 module.",
            "lesson_title": "Synthesis of Crop Harvesting and Summative Assessment",
            "pages": [
                [
                    {
                        "type": "suggested_image",
                        "title": "Bumper Grain Harvest Safely Stored in Modern Warehouse Facility",
                        "content": {
                            "title": "Bumper Grain Harvest Safely Stored in Modern Warehouse Facility",
                            "caption": "A commercial grain warehouse showcasing bags stacked neatly on wooden pallets, preserving national food reserves after disciplined post-harvest management."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Synthesis & Summative Assessment",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Synthesize the **5-phase post-harvest value chain continuum**.",
                                "Draft a comprehensive **Farm Harvest and Storage Portfolio** for a local crop enterprise.",
                                "Resolve the **Farmer Kitale Wet Maize Post-Harvest Crisis Simulation**.",
                                "Complete the comprehensive **Summative Topic Assessment** covering all 10 lessons of Topic 7."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The Complete Post-Harvest Value Chain Continuum",
                        "content": {
                            "title": "From Physiological Maturity to Table",
                            "text": "1. **Maturity Diagnostics**: Verify black layer in maize or thumb-rub skin set in potatoes.\n2. **Pre-Harvest Conditioning**: Haulm destruction 10–14 days prior in tubers; stooking/cob bending in cereals.\n3. **Harvest Execution**: Dry weather window, sharp tools, 30 cm fork clearance in potatoes, 5 m machine safety.\n4. **Post-Harvest Processing**: Cob drying, gentle shelling, winnowing chaff, sun-drying to **13% moisture on tarpaulins**.\n5. **Airtight Storage**: Bagging in **Hermetic PICS bags**, stacking on **wooden pallets**, fitting **rat guards** on granaries."
                        }
                    }
                ],
                [
                    {
                        "type": "suggested_diagram",
                        "title": "The Complete Post-Harvest Value Chain Continuum",
                        "content": {
                            "title": "The Complete Post-Harvest Value Chain Continuum",
                            "caption": "Flowchart showing: Phase 1 Maturity Diagnostic -> Phase 2 Pre-Harvest Conditioning -> Phase 3 Dry Weather Harvest -> Phase 4 Drying to 13% Moisture -> Phase 5 Hermetic Palletized Storage."
                        }
                    },
                    {
                        "type": "comparison_table",
                        "title": "Master Crop Harvesting Protocol Summary",
                        "content": {
                            "title": "Synthesized Harvesting Framework",
                            "headers": ["Crop Enterprise", "Pre-Harvest Action", "Harvesting Tool & Technique", "Curing / Drying Target", "Recommended Storage Mode"],
                            "rows": [
                                ["Irish Potatoes", "Haulm destruction 10–14 days prior", "Digging fork inserted 30 cm away", "Shaded curing for 7–10 days (Suberization)", "Dark, ventilated wooden crates in cool shed"],
                                ["Maize", "Bend cobs downward; field stooking", "Snap dehusked cobs in dry weather", "Sun-dry on tarpaulins to 13% moisture", "Hermetic PICS bags on wooden pallets"],
                                ["Fresh Tomatoes", "Pruning and staking", "Hand harvest with pedicels intact", "Immediate sorting and grading", "Ventilated plastic crates in cool packing shed"],
                                ["Sweet Potatoes", "Stop irrigation 2 weeks prior", "Careful digging fork lifting", "Cure in shade for 5–7 days", "Dry sand pits or ventilated slatted boxes"]
                            ]
                        }
                    }
                ],
                [
                    {
                        "type": "mini_activity",
                        "title": "Performance Task: The Farmer Kitale Wet Maize Crisis Recovery Plan",
                        "content": {
                            "title": "Post-Harvest Emergency Turnaround Brief",
                            "task": "A smallholder in Kitale harvested 20 bags of maize during a sudden rainstorm and immediately sealed the wet, dehusked cobs inside woven plastic bags in an unventilated concrete room.\n\n**Your Deliverable**: Draft a 1-page Urgent Agronomic Advisory Note:\n1. Predict the biological disaster (Aspergillus flavus, aflatoxin toxicity, mold heating) within 14 days.\n2. Propose 3 emergency corrective actions to salvage the grain.",
                            "materials": ["Case Handout", "Advisory Template", "Pen"],
                            "safety": "Ensure evidence-based food safety recommendations."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Core Summary: Harvesting Mastery",
                        "content": {
                            "title": "Key Takeaways",
                            "text": "- **Follow the complete value chain** from maturity testing to palletized storage.\n- **Haulm destruction hardens potato skins** and excludes Late Blight.\n- **Harvest cereals in dry sunny weather** to prevent Aspergillus mold.\n- **Dry grains to 13%–14% moisture** and store in chemical-free PICS bags."
                        }
                    }
                ],
                # Pages 4 to 8: 8 Summative Assessment MCQs
                [
                    {
                        "type": "knowledge_check",
                        "title": "Summative MCQ 1: Biological Role of Haulm Destruction",
                        "content": {
                            "question": "What is the primary biological reason for carrying out haulm destruction (vine killing) in Irish potato farming 10 to 14 days before digging the tubers?",
                            "options": [
                                "To encourage the potato plants to produce flowers for seed breeding",
                                "To trigger skin curing (hardening of the outer periderm) and prevent foliar Late Blight fungal spores from washing down and infecting tubers during harvest",
                                "To increase the nitrogen concentration in the underground roots",
                                "To attract beneficial soil micro-organisms that digest the tuber skins"
                            ],
                            "answer": "B",
                            "explanation": "Haulm destruction stops vegetative growth, stimulating the underground potato tubers to cure and harden their outer skins (suberization), making them resistant to physical skinning during harvest. It also stops Late Blight pathogens on the foliage from contacting tubers."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Summative MCQ 2: Downward Cob Bending Function",
                        "content": {
                            "question": "How does the pre-harvest practice of bending mature maize cobs downward in the field preserve grain quality before harvest?",
                            "options": [
                                "It increases the rate of photosynthesis in the dying stalks",
                                "It prevents rainwater from pooling inside the husk tips, which prevents grain rotting, premature sprouting, and bird damage",
                                "It forces the roots to absorb more potassium from the soil",
                                "It makes it easier for mechanical combine harvesters to cut the stalks"
                            ],
                            "answer": "B",
                            "explanation": "Bending cobs downward shields the open tip of the cob from rainwater, allowing moisture to drain off naturally while drying continues, preventing grain rotting and bird theft."
                        }
                    }
                ],
                [
                    {
                        "type": "knowledge_check",
                        "title": "Summative MCQ 3: Black Layer Diagnostic Significance",
                        "content": {
                            "question": "In maize cultivation, what does the appearance of a distinct 'black layer' at the tip of the extracted kernel signify to an agronomist?",
                            "options": [
                                "The crop has been infected with Head Smut disease",
                                "The grain is too dry to be milled into flour",
                                "The seed has achieved complete physiological maturity, and nutrient transfer from the plant has permanently ceased",
                                "The soil is suffering from extreme phosphorus toxicity"
                            ],
                            "answer": "C",
                            "explanation": "The formation of the black layer is a physical barrier of sealed cells at the kernel base confirming that the grain has finished accumulating starch and has reached 100% physiological maturity."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Summative MCQ 4: Potato Digging Fork Insertion Clearance",
                        "content": {
                            "question": "When harvesting Irish potatoes manually, why must the digging fork be inserted at least 30 cm away from the base of the plant stem?",
                            "options": [
                                "It allows the farmer to stand on uncultivated soil",
                                "It prevents the fork tines from slicing, piercing, or bruising the subterranean tubers",
                                "It ensures the soil remains compact around root systems",
                                "It speeds up the growth of remaining potato vines"
                            ],
                            "answer": "B",
                            "explanation": "Potato tubers grow outward in the ridge around the stem. Inserting the digging fork 30 cm away allows the tool to slide underneath the tuber cluster and lever it up without slicing or impaling the potatoes."
                        }
                    }
                ],
                [
                    {
                        "type": "knowledge_check",
                        "title": "Summative MCQ 5: Shaded Potato Curing Purpose",
                        "content": {
                            "question": "What is the primary scientific purpose of curing harvested Irish potatoes in a shaded, well-ventilated area for 7 to 10 days before long-term storage?",
                            "options": [
                                "To encourage the potatoes to sprout new roots",
                                "To turn the skins green and bitter to deter rodents",
                                "To heal minor surface abrasions through suberization, harden the skin, and dry off surface moisture without producing toxic solanine",
                                "To increase the water content inside the potato starch cells"
                            ],
                            "answer": "C",
                            "explanation": "Shaded curing triggers suberization (forming a protective corky cell layer over micro-wounds), making tubers resistant to soft rot bacteria during storage. Keeping them in the shade prevents toxic solanine greening."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Summative MCQ 6: Safe Cereal Storage Moisture Target",
                        "content": {
                            "question": "What is the target moisture content percentage for maize grain to be stored safely in bags without risking fungal mold proliferation and aflatoxin contamination?",
                            "options": [
                                "5% - 8%",
                                "13% - 14%",
                                "20% - 25%",
                                "30% - 35%"
                            ],
                            "answer": "B",
                            "explanation": "Maize stored at 13% to 14% moisture content is safe from fungal spoilage, as mold fungi (Aspergillus and Penicillium) require moisture above 14% to germinate and synthesize mycotoxins."
                        }
                    }
                ],
                [
                    {
                        "type": "knowledge_check",
                        "title": "Summative MCQ 7: PICS Hermetic Bag Operating Principle",
                        "content": {
                            "question": "How do hermetic storage bags (such as PICS bags) kill weevils inside stored grain without requiring synthetic chemical pesticide dusts?",
                            "options": [
                                "They generate high electrical charges that shock the insects",
                                "They trap insects in a sticky glue layer on the inner bag surface",
                                "They create an airtight seal where respiring insects and grain consume oxygen, dropping O₂ below 5%, which suffocates and kills all insects",
                                "They emit high-frequency ultrasonic sounds that repel pests"
                            ],
                            "answer": "C",
                            "explanation": "Hermetic PICS bags exclude oxygen. As insects and grain respire, oxygen drops below 5% and carbon dioxide rises. Deprived of oxygen, weevils, larvae, and eggs die of asphyxiation naturally."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Summative MCQ 8: Wooden Pallet Stacking Rationale",
                        "content": {
                            "question": "When storing bagged maize in a warehouse, why is it mandatory to stack bags on elevated wooden pallets rather than directly on the concrete floor?",
                            "options": [
                                "To make it easier for weevils to fall out of the bags",
                                "To prevent moisture from the cold concrete floor from seeping into the bottom bags and triggering mold rot",
                                "To allow rodents to pass underneath without biting the bags",
                                "To increase the ceiling height of the storage facility"
                            ],
                            "answer": "B",
                            "explanation": "Concrete floors naturally conduct ground moisture. Placing grain bags directly on concrete causes moisture absorption, raising grain moisture above 14% and triggering lethal mold and aflatoxin contamination."
                        }
                    }
                ],
                # Page 8: Capstone Summary
                [
                    {
                        "type": "summary",
                        "title": "Topic 7 Capstone Summary: General Crop Harvesting Mastery",
                        "content": {
                            "title": "Mastery Overview: Grade 10 Crop Harvesting & Post-Harvest Value Chain",
                            "text": "Congratulations on mastering **Topic 7: General Crop Harvesting**!\n\nYou have mastered:\n- **Harvest Determinants**: Evaluating physiological maturity, moisture content, weather conditions, and market destination.\n- **Pre-Harvest Conditioning**: Haulm destruction in potatoes 10–14 days prior (skin setting, Late Blight exclusion); cereal field drying (stooking, downward cob bending).\n- **Harvesting Operations**: Manual vs mechanical harvesting; safety rules (sharp tools, 5 m machine clearance, N95 dust masks).\n- **Maturity Diagnostics**: The black layer test in maize, thumb-rub skin set in potatoes, and sap testing in sweet potatoes.\n- **Harvesting for Purpose**: Fresh market breaker tomatoes vs factory processing vs seed production.\n- **Tuber & Cereal Harvesting**: 30 cm fork clearance in potato ridges; shaded curing for 7–10 days (suberization); dry sunny weather maize harvesting.\n- **Post-Harvest Processing & Moisture**: Cob drying, shelling, winnowing, sun-drying on tarpaulins to the **13% safe moisture threshold**.\n- **Airtight Storage & Pest Defense**: Improved granaries with rat guards, bag stacking on **wooden pallets**, and **Hermetic PICS bag technology**."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Topic 7 Final Takeaway",
                        "content": {
                            "title": "The Post-Harvest Value Chain Maxim",
                            "text": "Harvest at peak physiological maturity in dry weather, cure tubers in the shade, dry grain to 13% moisture on clean tarpaulins, and store in hermetic bags on pallets to safeguard food security and maximize farm profitability."
                        }
                    }
                ]
            ]
        }
    ]

@transaction.atomic
def ingest_grade10_topic7(replace=False):
    """Executes the complete production ingestion of Grade 10 Agriculture Topic 7: General Crop Harvesting."""
    print("=" * 80)
    print("STARTING INGESTION: CBC Grade 10 Agriculture — Topic 7: General Crop Harvesting")
    print("=" * 80)

    curriculum = Curriculum.objects.filter(name__iexact="CBC").first()
    grade = Grade.objects.filter(curriculum=curriculum, name__icontains="10").first()
    subject = Subject.objects.filter(grade=grade, name__iexact="Agriculture").first()

    assert curriculum and grade and subject, "Curriculum/Grade/Subject not found!"

    topic_name = "General Crop Harvesting"
    topic = Topic.objects.filter(subject=subject, name=topic_name).first()
    if not topic:
        topic = Topic.objects.create(
            subject=subject,
            name=topic_name,
            description="Comprehensive theoretical, technical, and economic study of crop harvest determinants, pre-harvest practices, potato haulm destruction, cereal harvesting, post-harvest drying, 13% moisture standards, hermetic storage, and quality preservation.",
            order=7
        )
        print(f"Created Topic 7: {topic.name} (ID: {topic.id})")
    else:
        topic.order = 7
        topic.description = "Comprehensive theoretical, technical, and economic study of crop harvest determinants, pre-harvest practices, potato haulm destruction, cereal harvesting, post-harvest drying, 13% moisture standards, hermetic storage, and quality preservation."
        topic.save()
        print(f"Resolved Topic 7: {topic.name} (ID: {topic.id})")

    if replace:
        print("Flag --replace active: Clearing existing LearningUnits and Lessons for Topic 7...")
        topic.learning_units.all().delete()
        topic.lessons.all().delete()

    curriculum_data = build_topic7_curriculum()
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
                    "topic_order": 7,
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
                    block_id=f"g10_agri_t7_u{u_order}_p{page_idx}_b{comp_idx}",
                    block_type=b_type,
                    component_type=b_type,
                    title=b_title,
                    content=b_content,
                    order=block_order_counter,
                    page_number=page_idx,
                    component_order=comp_idx,
                    page_title=b_title if comp_idx == 1 else None,
                    metadata={"topic_order": 7, "unit_order": u_order, "page": page_idx}
                )
                block_order_counter += 1
                total_blocks += 1

        print(f"  Ingested Unit {u_order}: {u_name} -> Lesson '{l_title}' ({len(pages)} Pages, {block_order_counter - 1} Blocks)")

    print("=" * 80)
    print(f"INGESTION COMPLETE: Topic 7 '{topic.name}'")
    print(f"  Total Units:   {total_units}")
    print(f"  Total Lessons: {total_lessons}")
    print(f"  Total Pages:   {total_pages}")
    print(f"  Total Blocks:  {total_blocks}")
    print("=" * 80)

if __name__ == "__main__":
    replace_flag = "--replace" in sys.argv
    ingest_grade10_topic7(replace=replace_flag)
