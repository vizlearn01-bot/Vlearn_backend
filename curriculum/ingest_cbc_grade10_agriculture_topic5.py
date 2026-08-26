"""
VLearn CBC Grade 10 Agriculture — Topic 5: Growing Selected Crops
Production Ingestion Engine (Deep Senior Secondary Pedagogical Edition)

Curriculum: CBC (ID: 5)
Grade: Grade 10 (ID: 5, Level: 10)
Subject: Agriculture
Topic: Growing Selected Crops (Topic Order: 5)

Decomposed into 10 Learning Units & 10 Published Lessons:
  1. Selecting a Crop and Planning Production (5 Pages, 11 Blocks)
  2. Establishing a Nursery Bed (5 Pages, 11 Blocks)
  3. Sowing and Early Nursery Management (5 Pages, 11 Blocks)
  4. Nursery Management (5 Pages, 11 Blocks)
  5. Crop Establishment (Transplanting) (5 Pages, 11 Blocks)
  6. Field Management of Selected Crop (5 Pages, 12 Blocks)
  7. Monitoring Crop Growth (5 Pages, 11 Blocks)
  8. Harvesting the Selected Crop (5 Pages, 11 Blocks)
  9. Justifying Management Practices (5 Pages, 11 Blocks)
  10. Synthesis and Practical Assessment (8 Pages, 16 Blocks)
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

def build_topic5_curriculum():
    """Returns the comprehensive pedagogical page and block structure for Grade 10 Topic 5: Growing Selected Crops."""
    return [
        # =====================================================================
        # LESSON 1: Selecting a Crop and Planning Production
        # =====================================================================
        {
            "unit_order": 1,
            "unit_name": "Selecting a Crop and Planning Production",
            "unit_description": "Nursery crops (tomatoes, capsicums, cabbages, onions) vs direct-seeded crops; enterprise selection matrix (market demand, ecological fit, input access, maturity period); formulating a production calendar.",
            "lesson_title": "Agribusiness Crop Selection and Production Planning",
            "pages": [
                [
                    {
                        "type": "suggested_image",
                        "title": "Commercial Vegetable Seedling Production and Crop Planning",
                        "content": {
                            "title": "Commercial Vegetable Seedling Production and Crop Planning",
                            "caption": "High-quality vegetable seedlings raised in specialized nursery facilities being prepared for farm enterprise establishment."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Crop Selection & Planning",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Identify crops that require establishment via a **nursery bed** (**tomatoes, cabbages, capsicums, onions**).",
                                "Evaluate the 4 key factors for enterprise selection (**market demand, ecological fit, input access, maturity duration**).",
                                "Explain the biological and economic justifications for nursery propagation over direct field seeding.",
                                "Formulate a comprehensive **crop production calendar and input checklist**."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Why Use a Nursery Bed?",
                        "content": {
                            "title": "Protecting Small, Delicate Seeds",
                            "text": "In commercial crop production, seeds vary enormously in size and physiological vulnerability. While large, vigorous seeds (maize, beans) are sown directly into the open field, small-seeded horticultural crops require intensive initial care.\n\n- A **nursery bed** is a specially prepared, sheltered plot of fertile, fine-tilth soil dedicated to nurturing delicate young seedlings before they are transplanted into the main field.\n- **Crops Requiring Nursery Propagation**: Tomatoes, capsicums (peppers), cabbages, kales (Sukuma wiki), onions, and eggplants."
                        }
                    }
                ],
                [
                    {
                        "type": "comparison_table",
                        "title": "Direct Field Seeding vs Nursery Bed Propagation",
                        "content": {
                            "title": "Propagation Strategy Comparison",
                            "headers": ["Parameter", "Direct Field Seeding", "Nursery Bed Propagation"],
                            "rows": [
                                ["Target Crop Types", "Large seeds (Maize, Beans, Peas, Groundnuts)", "Small, delicate seeds (Tomatoes, Cabbages, Capsicums)"],
                                ["Seed Cost Efficiency", "Higher seed loss due to heavy rain, birds, and insects", "Maximizes germination of expensive certified hybrid seeds"],
                                ["Resource Concentration", "Water, weeding, and shading dispersed across whole farm", "Intensive watering, pest control, and care in 3 m² space"],
                                ["Field Stand Uniformity", "Irregular emergence; gaps requiring heavy thinning/gapping", "Only vigorous, uniform, disease-free seedlings transplanted"],
                                ["Weed Competition Risk", "Young seedlings easily choked by emerging field weeds", "Seedlings reach 15 cm before facing field weed pressure"]
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The 4 Agribusiness Crop Selection Factors",
                        "content": {
                            "title": "Minimizing Financial Risk",
                            "text": "1. **Market Demand & Price Trends**: Conduct a local market survey. Select high-demand crops with ready buyers (e.g. local retail markets, school kitchens, hotels).\n2. **Ecological Compatibility**: Match crop climatic requirements (altitude, temperature, rainfall, soil pH) to your specific agro-ecological zone.\n3. **Water and Input Access**: Ensure access to clean irrigation water (critical for dry-season high-profit vegetable production), certified seeds, fertilizer, and tools.\n4. **Maturity Duration**: For school projects and fast-turnaround cash flow, prioritize short-duration crops (maturing in 2 to 3 months)."
                        }
                    }
                ],
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Agribusiness Crop Selection Decision Matrix",
                        "content": {
                            "title": "Agribusiness Crop Selection Decision Matrix",
                            "caption": "Decision flowchart illustrating the 4 critical filters (Market Demand, Ecological Fit, Water/Input Access, and Maturity Window) leading to Enterprise Selection."
                        }
                    },
                    {
                        "type": "step_process",
                        "title": "Protocol: Developing a Crop Production Calendar",
                        "content": {
                            "title": "Chronological Production Master Schedule",
                            "steps": [
                                "1. **Week 1 (Enterprise Planning & Sourcing)**: Conduct market survey, select crop variety, source certified hybrid seeds and fertilizers.",
                                "2. **Week 2 (Nursery Bed Preparation & Sowing)**: Clear, dig 30 cm deep, pulverize to fine tilth, incorporate compost, drill seeds, mulch, and erect shade.",
                                "3. **Weeks 3–5 (Nursery Husbandry)**: Water twice daily, pull weeds by hand, thin crowded seedlings, prick out into containers.",
                                "4. **Week 6 (Hardening Off & Main Field Preparation)**: Reduce nursery watering and remove shade; plow and manure main field.",
                                "5. **Week 7 (Transplanting)**: Transplant late afternoon with intact root balls; water and mulch.",
                                "6. **Weeks 8–14 (Field Management)**: Weed, top-dress at knee-high/flowering, stake with figure-of-8 ties, and scout pests weekly.",
                                "7. **Weeks 15–18 (Harvesting & Agribusiness Accounting)**: Harvest at optimal maturity, pack in crates, market produce, and balance financial ledger."
                            ]
                        }
                    }
                ],
                [
                    {
                        "type": "mini_activity",
                        "title": "Market Survey Practical: Selecting a School Farm Vegetable Enterprise",
                        "content": {
                            "title": "Conducting an Agribusiness Market Feasibility Survey",
                            "task": "In groups of three:\n\n1. Interview two local vegetable vendors or the school caterer.\n2. Record wholesale and retail prices for tomatoes, cabbages, and capsicums over the past 3 months.\n3. Identify which vegetable experienced high price spikes and evaluate your school farm's water availability.\n4. Present a 1-page business justification for your chosen crop enterprise.",
                            "materials": ["Survey Questionnaire", "Clipboard", "Pen"],
                            "safety": "Follow school guidelines during community vendor interviews."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Core Summary: Crop Selection and Planning",
                        "content": {
                            "title": "Key Takeaways",
                            "text": "- **Small-seeded vegetables** (tomatoes, capsicums, cabbages) require initial nursery bedding.\n- **Nurseries concentrate resources**, protect delicate seedlings, and ensure 100% field uniformity.\n- **Evaluate 4 selection pillars**: Market demand, ecological fit, input access, and maturity duration.\n- **A production calendar** ensures timely synchronization of nursery, transplanting, and harvesting."
                        }
                    }
                ],
                [
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Nursery Crop Classification",
                        "content": {
                            "question": "Which of the following agricultural crop groupings consists entirely of crops that are conventionally raised in a specialized nursery bed before being transplanted into the main field?",
                            "options": [
                                "Maize, Dry Beans, and Groundnuts",
                                "Tomatoes, Cabbages, Capsicums, and Onions",
                                "Sorghum, Finger Millet, and Cassava",
                                "Sugarcane, Irish Potatoes, and Napier Grass"
                            ],
                            "answer": "B",
                            "explanation": "Tomatoes, cabbages, capsicums, and onions have tiny, delicate seeds with minimal endosperm reserves that require fine seedbed tilth, constant moisture, and protection from harsh weather in a nursery. In contrast, maize and beans are direct-seeded, while cassava, sugarcane, and napier grass are propagated vegetatively."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 2: Establishing a Nursery Bed
        # =====================================================================
        {
            "unit_order": 2,
            "unit_name": "Establishing a Nursery Bed",
            "unit_description": "Nursery siting rules (water source proximity, gentle slope, shelter from strong winds, crop rotation history); standard 1.0 m width; 5-step preparation (clearing, 30 cm deep digging, pulverization to fine tilth, compost mixing, leveling).",
            "lesson_title": "Nursery Siting and Seedbed Preparation",
            "pages": [
                [
                    {
                        "type": "suggested_image",
                        "title": "Standard Garden Nursery Bed Preparation and Soil Leveling",
                        "content": {
                            "title": "Standard Garden Nursery Bed Preparation and Soil Leveling",
                            "caption": "A well-sited, raised garden seedbed with refined granular tilth and organic compost incorporation ready for precision drilling."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Nursery Siting & Preparation",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Identify critical **nursery siting criteria** (**water proximity, gentle slope, wind shelter, crop rotation history**).",
                                "Explain why standard nursery beds are constructed to a fixed width of **1.0 meter**.",
                                "Execute the 5-step sequence for preparing a fine-tilth nursery bed.",
                                "Incorporate well-decomposed organic compost into the topsoil safely."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Criteria for Siting a Successful Nursery Bed",
                        "content": {
                            "title": "Strategic Site Selection",
                            "text": "The location of a nursery bed directly determines seedling emergence and vigor:\n\n1. **Reliable Water Source**: Must be located within a short walking distance of a clean water point, as seedlings require daily watering.\n2. **Gentle Topography (Slope)**: Sited on flat or gently sloping land. Steep slopes cause severe erosion and wash seeds away; low-lying hollows cause waterlogging and root rot.\n3. **Shelter & Sunlight**: Positioned in a sheltered spot protected from strong prevailing winds, but exposed to morning sunlight. *Avoid dense tree shade, which starves seedlings of light, causing weak, elongated stems (etiolation)*.\n4. **Disease-Free Soil History**: Avoid sites where solanaceous (tomatoes, potatoes, peppers) or brassica crops were grown in the past 2 seasons to prevent soil-borne bacterial wilt (*Ralstonia*) and fungal damping-off (*Pythium*)."
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "Why the Standard Width is Exactly 1.0 Meter",
                        "content": {
                            "title": "Ergonomics and Soil Conservation",
                            "text": "A standard nursery bed is designed to be **1.0 meter wide** (and any convenient length, typically 3.0 meters):\n\n- **Arm Reach Ergonomics**: A 1.0 m width allows a learner or farmer to comfortably reach the center of the bed (50 cm from either side) with their hands during delicate weeding, pricking out, and watering.\n- **Zero Soil Compaction**: Eliminates the need to ever step onto the bed. Stepping on seedbeds crushes delicate roots and severely compacts fine tilth, destroying soil porosity."
                        }
                    },
                    {
                        "type": "step_process",
                        "title": "Protocol: 5 Steps to Prepare a Standard Nursery Bed",
                        "content": {
                            "title": "Nursery Bed Construction Workflow",
                            "steps": [
                                "1. **Clearing & Demarcation**: Remove tall brush, stones, and trash. Measure a 1.0 m x 3.0 m rectangle using pegs and string.",
                                "2. **Deep Primary Digging (30 cm)**: Dig the soil deeply with a hand jembe to break hardpans, loosen subsoil, and expose soil pests to the sun.",
                                "3. **Secondary Pulverization**: Shatter large soil clods using a fork jembe and rake until a fine, crumbly granular tilth (<5 mm) is achieved.",
                                "4. **Compost Incorporation**: Spread 1 to 2 buckets (10–15 kg) of well-decomposed, sieved compost or farmyard manure across the top 10 cm and mix thoroughly.",
                                "5. **Leveling and Edge Furrows**: Smooth and level the surface with a hand rake to prevent water pooling in hollows, and dig shallow 10 cm perimeter drainage furrows."
                            ]
                        }
                    }
                ],
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Standard 1.0m Wide Nursery Bed Architecture & Siting",
                        "content": {
                            "title": "Standard 1.0m Wide Nursery Bed Architecture & Siting",
                            "caption": "Cross-sectional engineering diagram showing 1.0m bed width, 15cm raised height, refined topsoil with compost, 50cm reach from both sides, and perimeter drainage channels."
                        }
                    },
                    {
                        "type": "comparison_table",
                        "title": "Nursery Bed vs Main Field Seedbed Characteristics",
                        "content": {
                            "title": "Seedbed Architecture Comparison",
                            "headers": ["Feature", "Nursery Bed", "Main Field Permanent Seedbed"],
                            "rows": [
                                ["Soil Tilth Size", "Ultra-fine crumb (<5 mm) to maximize delicate seed contact", "Medium to coarse clods (20–50 mm) to resist rainfall crusting"],
                                ["Organic Matter Input", "Heavy incorporation of sieved, well-decomposed compost", "Basal planting fertilizer (DAP) or broadcast farmyard manure"],
                                ["Bed Width & Structure", "Strictly 1.0 m width; raised 15 cm above ground level", "Full field rows spaced 60–75 cm or flat contour strips"],
                                ["Protection Features", "Low shade frame (1.0 m high) and temporary grass mulch", "Unshaded open field with crop residue or mulch"]
                            ]
                        }
                    }
                ],
                [
                    {
                        "type": "mini_activity",
                        "title": "Field Practical: Siting and Constructing a 1.0m x 3.0m School Nursery Bed",
                        "content": {
                            "title": "Hands-On Nursery Construction Lab",
                            "task": "In teams of four:\n\n1. Select a sheltered, gently sloping site 10 meters from the school water tap.\n2. Demarcate a 1.0 m x 3.0 m bed using measuring tape, 4 corner wooden pegs, and string.\n3. Dig the bed to 30 cm depth, pulverize clods with a rake to a fine tilth.\n4. Mix in 10 kg of cured compost and level the surface flat.\n5. Confirm that you can reach the exact center of the bed from both sides without stepping on the soil.",
                            "materials": ["4 Pegs", "String", "Measuring Tape", "Hand Jembe", "Fork Jembe", "Rake", "Cured Compost"],
                            "safety": "Keep feet clear of swinging jembes; wear protective garden boots."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Core Summary: Nursery Siting & Preparation",
                        "content": {
                            "title": "Key Takeaways",
                            "text": "- **Site nurseries near clean water**, on gentle slopes, in sheltered spots with fresh rotation history.\n- **The standard 1.0 m width** ensures farmers can reach the center without stepping on and compacting soil.\n- **Deep digging (30 cm) and pulverization** create an ultra-fine tilth essential for tiny seeds.\n- **Incorporate cured compost** into the top 10 cm to provide biological nutrients and retain moisture."
                        }
                    }
                ],
                [
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Rationale for 1.0m Nursery Width",
                        "content": {
                            "question": "Why is it an established standard agronomic rule to construct vegetable nursery beds with a maximum width of exactly 1.0 meter?",
                            "options": [
                                "To match the standard width of tractor tires in commercial wheat farming",
                                "To allow learners and farmers to comfortably reach the center of the bed from either side for weeding, thinning, and watering without stepping on the soil and compacting the delicate root zone",
                                "Because nursery seeds refuse to germinate in beds wider than one meter",
                                "To ensure that rain falls only on the edges of the bed"
                            ],
                            "answer": "B",
                            "explanation": "A 1.0-meter bed width provides an ergonomic reach of 50 cm from either side. This allows the grower to carry out all delicate manual tasks (weeding, pricking out, fine-rose watering) without ever having to step onto the bed, which would crush fragile seedlings and cause severe soil compaction."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 3: Sowing and Early Nursery Management
        # =====================================================================
        {
            "unit_order": 3,
            "unit_name": "Sowing and Early Nursery Management",
            "unit_description": "Drilling procedure across the bed (10–15 cm furrow spacing, 1.0–1.5 cm depth, light soil covering); dry grass mulching; 1.0 m sloped shade frame; prompt mulch removal upon germination to avoid etiolation.",
            "lesson_title": "Drilling Seeds, Mulching, and Shade Construction",
            "pages": [
                [
                    {
                        "type": "suggested_image",
                        "title": "Vegetable Seedlings Emerging under Protected Nursery Shading",
                        "content": {
                            "title": "Vegetable Seedlings Emerging under Protected Nursery Shading",
                            "caption": "Young vegetable seedlings growing in a sheltered nursery environment with regulated light penetration and soil moisture management."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Sowing & Early Management",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Demonstrate the **drilling method** for sowing small vegetable seeds in a nursery bed.",
                                "Calculate and apply correct **furrow spacing (10–15 cm)** and **sowing depth (1.0–1.5 cm)**.",
                                "Apply a protective **dry grass mulch layer** and erect a **1.0-meter sloped shade structure**.",
                                "Explain why mulch must be **removed immediately upon seedling emergence** to prevent fatal **etiolation**."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Drilling Seeds vs Random Broadcasting",
                        "content": {
                            "title": "Why Professional Growers Drill Seeds",
                            "text": "In a vegetable nursery, never scatter seeds randomly (broadcasting). Always practice **drilling**:\n\n- **Drilling** involves drawing shallow, parallel miniature furrows across the width of the bed using a straight stick.\n- **Furrow Spacing**: Make furrows **10 to 15 cm apart** across the 1.0 m bed.\n- **Sowing Depth**: Sow small seeds at a depth of **1.0 to 1.5 cm** (approximately $2\\times$ to $3\\times$ the diameter of the seed).\n- **Why Drilling is Superior**: Distributes seeds evenly, prevents severe crowding, ensures uniform germination depth, and leaves clear 10 cm walkways for easy hand-weeding between rows."
                        }
                    }
                ],
                [
                    {
                        "type": "step_process",
                        "title": "Protocol: Step-by-Step Sowing in a Nursery Bed",
                        "content": {
                            "title": "Precision Nursery Sowing Protocol",
                            "steps": [
                                "1. **Draw Furrows (Drills)**: Using a straight stick and a 10 cm measuring spacer, press shallow 1.0–1.5 cm grooves across the bed.",
                                "2. **Sow Seeds Thinly**: Drop seeds along the furrow at a rate of 1 seed every 1–2 cm. Avoid pouring seed clumps in one spot.",
                                "3. **Cover Lightly with Fine Soil**: Gently pinch fine topsoil over the furrow to cover seeds, and press down lightly with your palm to establish capillary seed-to-soil contact.",
                                "4. **Water with Fine-Rose Nozzle**: Irrigate gently using a watering can with a fine rose to avoid displacing the seeds.",
                                "5. **Apply Surface Mulch**: Spread a thin layer of clean, seed-free dry grass directly on the soil surface.",
                                "6. **Erect Shade Canopy**: Build a 1.0 m high sloped wooden frame covered with grass or palm fronds over the bed."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The Science of Mulching and Shading",
                        "content": {
                            "title": "Regulating Microclimate for Rapid Germination",
                            "text": "### 1. The Dry Grass Mulch Layer\n- **Functions**: Retains soil moisture, prevents surface crusting from drying winds, and buffers seeds against dislodgement during watering.\n- **THE CRITICAL RULE**: As soon as green shoots emerge (typically 5–8 days after sowing), **the surface mulch MUST be removed immediately**! If left in place, seedlings stretch in search of light, growing pale, thin, weak, and spindly—a fatal condition known as **etiolation**.\n\n### 2. The Overhead Shade Structure\n- A 1.0 m high temporary wooden frame covered with grass or palm fronds.\n- **Functions**: Protects tender seedlings from intense scorching noon solar radiation and shatters heavy raindrops into fine mist, preventing soil erosion."
                        }
                    }
                ],
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Sowing, Mulching & Sloped Shade Frame Cross-Section",
                        "content": {
                            "title": "Sowing, Mulching & Sloped Shade Frame Cross-Section",
                            "caption": "Stratigraphic cross-section of a sown nursery bed showing: Refined topsoil, 1.5 cm drilled seeds, surface grass mulch, 10 cm perimeter trenches, and 1.0 m high sloped overhead shade roof."
                        }
                    },
                    {
                        "type": "suggested_video",
                        "title": "How to Sow and Manage a Vegetable Nursery Bed",
                        "content": {
                            "title": "How to Sow and Manage a Vegetable Nursery Bed",
                            "description": "Practical horticultural demonstration showing furrow drilling, seed spacing, fine-rose watering, surface mulching, and shade construction.",
                            "url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
                        }
                    }
                ],
                [
                    {
                        "type": "mini_activity",
                        "title": "Field Practical: Drilling Cabbage / Tomato Seeds and Erecting Shade",
                        "content": {
                            "title": "Hands-On Sowing and Shade Building Practical",
                            "task": "On your prepared 1.0 m x 3.0 m nursery bed:\n\n1. Use a straight stick to make parallel drills 15 cm apart and 1.0 cm deep.\n2. Sow tomato or cabbage seeds thinly along each drill and cover with fine soil.\n3. Water using a fine-rose can.\n4. Spread clean dry grass mulch across the bed.\n5. Construct a 1.0 m high sloped wooden frame using 4 corner forked sticks and cover with palm fronds.",
                            "materials": ["Tomato / Cabbage Seeds", "Measuring Stick", "Watering Can with Rose", "Dry Grass", "Forked Wooden Posts", "Palm Fronds"],
                            "safety": "Ensure wooden frame posts are firmly driven into the ground."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Core Summary: Sowing and Early Management",
                        "content": {
                            "title": "Key Takeaways",
                            "text": "- **Drill seeds 10–15 cm apart at 1.0–1.5 cm depth** across the 1.0 m bed.\n- **Mulch conserves moisture** and protects seeds during early germination.\n- **Remove mulch immediately upon seedling emergence** to prevent weak, yellow etiolation.\n- **Erect a 1.0 m sloped shade frame** to shield delicate seedlings from scorching noon sun and heavy rain."
                        }
                    }
                ],
                [
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Consequences of Delayed Mulch Removal",
                        "content": {
                            "question": "A student sowed tomato seeds in a nursery bed and covered the soil with dry grass mulch. Two weeks after germination began, the mulch was still left in place. What physiological damage will the seedlings exhibit?",
                            "options": [
                                "The seedlings will develop deep purple leaves and thick wooden trunks",
                                "The seedlings will stretch upward in the dark, becoming excessively tall, thin, pale yellow, and mechanically weak (etiolation), making them collapse and die",
                                "The seedlings will begin producing ripe tomatoes underground",
                                "The mulch will transform into synthetic NPK fertilizer"
                            ],
                            "answer": "B",
                            "explanation": "Seedlings require solar radiation immediately after emergence to initiate chlorophyll synthesis and photosynthesis. If the surface mulch is not removed promptly upon emergence, the dark environment triggers etiolation—the seedlings produce excess gibberellins, stretching into long, spindly, pale yellow stems that lack mechanical strength and collapse from disease."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 4: Nursery Management
        # =====================================================================
        {
            "unit_order": 4,
            "unit_name": "Nursery Management",
            "unit_description": "Routine maintenance: fine-rose watering twice daily (preventing fungal damping-off), hand weeding, thinning, pricking out into 5x5 cm spacing, and hardening off 1–2 weeks prior (gradually reducing water and removing shade).",
            "lesson_title": "Routine Nursery Husbandry and Hardening Off",
            "pages": [
                [
                    {
                        "type": "suggested_image",
                        "title": "Disciplined Watering and Daily Nursery Husbandry Care",
                        "content": {
                            "title": "Disciplined Watering and Daily Nursery Husbandry Care",
                            "caption": "A garden watering can equipped with a fine-rose nozzle used for gentle seedling irrigation without soil displacement or stem damage."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Nursery Husbandry & Hardening Off",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Execute routine nursery practices: **watering, hand weeding, thinning, and pest scouting**.",
                                "Explain the biological cause and prevention of **damping-off fungal disease**.",
                                "Demonstrate **pricking out** crowded seedlings into secondary trays/beds at **5 cm $\\times$ 5 cm** spacing.",
                                "Execute the **hardening off protocol (1–2 weeks prior to transplanting)** by reducing water and removing shade."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Routine Daily Nursery Husbandry",
                        "content": {
                            "title": "The Golden Rules of Daily Seedling Care",
                            "text": "1. **Watering**: Water twice daily (early morning before 8:00 AM and late afternoon after 4:30 PM when evaporation is low) using a **fine-rose nozzle**. *Never flood the bed with an open pipe or splash large buckets, which dislodges roots and causes soil compaction*.\n2. **Hand Weeding**: Pull weeds gently by hand as soon as they appear. Weeds grow twice as fast as vegetable seedlings and quickly steal nitrogen and light.\n3. **Pest & Disease Scouting**: Check daily for cutworms, aphids, and flea beetles. Apply organic neem extracts or mild copper fungicides if fungal spots appear."
                        }
                    }
                ],
                [
                    {
                        "type": "definition_card",
                        "title": "Disease Alert: Damping-Off Fungal Disease",
                        "content": {
                            "term": "Damping-Off Disease",
                            "definition": "A destructive soil-borne fungal complex (primarily Pythium and Rhizoctonia spp.) that attacks the base of young seedlings in cold, waterlogged, poorly ventilated, or overcrowded nurseries.",
                            "example": "Seedling stems develop water-soaked brown lesions at the soil line, turn thread-thin, collapse, and rot en masse in circular patches."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Thinning vs Pricking Out vs Hardening Off",
                        "content": {
                            "title": "Producing Sturdy, High-Survival Seedlings",
                            "text": "### 1. Thinning\n- Selectively plucking out crowded, weak, or deformed seedlings within the rows to give healthy seedlings sufficient room ($2\\text{--}3\\text{ cm}$) to develop thick stems.\n\n### 2. Pricking Out\n- Transferring overcrowded seedlings from the primary nursery bed into individual potting tubes or a secondary 'pricking-out bed' spaced at **5 cm $\\times$ 5 cm**.\n- **When Done**: When seedlings develop their **first 2 to 3 true leaves** (usually 2 weeks after emergence).\n\n### 3. Hardening Off\n- The gradual physiological conditioning of seedlings to prepare them for the harsh conditions of the open field.\n- **When Done**: **1 to 2 weeks before transplanting**."
                        }
                    }
                ],
                [
                    {
                        "type": "step_process",
                        "title": "Protocol: The 2-Week Hardening Off Procedure",
                        "content": {
                            "title": "Hardening Off Operational Steps",
                            "steps": [
                                "1. **Day 1–3 (Initial Shade Thinning)**: Remove 30% of the palm fronds on the shade frame to introduce partial direct sunlight.",
                                "2. **Day 4–7 (Water Reduction)**: Reduce watering from twice daily to once daily, allowing the surface soil to dry slightly between waterings.",
                                "3. **Day 8–10 (Total Shade Removal)**: Completely remove the overhead shade frame, exposing seedlings to full all-day solar radiation.",
                                "4. **Day 11–13 (Water Withholding)**: Water only when seedlings show slight temporary wilting. This stimulates the accumulation of protective sugars and thickens cuticle layers.",
                                "5. **Day 14 (Transplanting Day)**: Water the bed heavily 30 minutes before lifting to ensure roots slide out with intact soil balls."
                            ]
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Nursery Management: Thinning, Pricking Out & Hardening Off",
                        "content": {
                            "title": "Nursery Management: Thinning, Pricking Out & Hardening Off",
                            "caption": "Comparative biological process diagram illustrating: Step 1 Thinning crowded rows, Step 2 Pricking out into 5x5 cm secondary spacing, and Step 3 Hardening off via progressive shade and water reduction."
                        }
                    }
                ],
                [
                    {
                        "type": "mini_activity",
                        "title": "Field Practical: Pricking Out Seedlings into Potting Tubes",
                        "content": {
                            "title": "Hands-On Pricking Out and Nursery Audit",
                            "task": "In the school nursery:\n\n1. Identify seedlings with 2 fully formed true leaves.\n2. Use a blunt dibber or wooden stick to loosen soil beneath seedling roots.\n3. Lift seedling by holding its leaf (NEVER pinch the stem).\n4. Transplant into a soil-filled potting tube, firm soil around root collar, and water gently.\n5. Place pricked-out tubes under 50% shade for 3 days to recover.",
                            "materials": ["2-Week Old Seedlings", "Potting Tubes / Secondary Bed", "Wooden Dibber", "Fine-Rose Watering Can"],
                            "safety": "Handle tender seedling roots with extreme care."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Core Summary: Nursery Husbandry & Hardening",
                        "content": {
                            "title": "Key Takeaways",
                            "text": "- **Water twice daily using a fine rose**; avoid overwatering to prevent damping-off disease.\n- **Hand weed and thin crowded rows** to build thick, stocky stems.\n- **Prick out crowded seedlings at 2 true leaves** into 5 cm x 5 cm spacing.\n- **Harden off 1–2 weeks before transplanting** by gradually reducing water and removing shade."
                        }
                    }
                ],
                [
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Hardening Off Mechanism",
                        "content": {
                            "question": "How does a commercial vegetable grower practically carry out the hardening off process for tomato seedlings, and what physiological benefit does it provide?",
                            "options": [
                                "By boiling the roots in warm water to kill insects",
                                "By gradually reducing watering frequency and removing the overhead shade canopy 1 to 2 weeks prior to transplanting, which builds sturdy fibrous stems and thick leaf cuticles to withstand field transplant shock",
                                "By keeping the seedlings in an airtight dark box for 10 days",
                                "By applying high doses of urea fertilizer to force rapid height growth"
                            ],
                            "answer": "B",
                            "explanation": "Hardening off prepares seedlings for the harsh realities of the open field (intense sun, strong wind, moisture fluctuations). Gradually withholding water and exposing plants to direct sunlight stimulates the deposition of thicker epidermal cuticles, accumulates protective cell solutes, and builds a robust, fibrous root system, dramatically reducing transplanting shock and mortality."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 5: Crop Establishment (Transplanting)
        # =====================================================================
        {
            "unit_order": 5,
            "unit_name": "Crop Establishment (Transplanting)",
            "unit_description": "Determining transplanting readiness (4–6 weeks, 10–15 cm tall, 4–6 true leaves, pencil-thick stem); late afternoon timing; nursery pre-watering; lifting with intact root ball using a garden trowel; planting at collar depth; immediate watering and temporary shade protection.",
            "lesson_title": "Field Establishment and Seedling Transplanting",
            "pages": [
                [
                    {
                        "type": "suggested_image",
                        "title": "Transplanting Vegetable Seedlings into Main Field Soil",
                        "content": {
                            "title": "Transplanting Vegetable Seedlings into Main Field Soil",
                            "caption": "A farmer using a garden trowel to transplant healthy vegetable seedlings with intact root soil balls into well-manured main field planting holes."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Seedling Transplanting",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Identify the physiological indicators of **transplanting readiness** (height, leaf count, stem thickness).",
                                "Explain why transplanting must be done in the **late afternoon (after 4:00 PM)** or on cloudy days.",
                                "Execute the step-by-step transplanting protocol using a garden trowel to maintain an **intact root ball**.",
                                "Plant seedlings at the correct **root collar depth** and apply immediate post-planting water and light mulch."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Determining Transplanting Readiness",
                        "content": {
                            "title": "The Optimal Physiological Window",
                            "text": "Moving seedlings to the main field must be timed precisely. Transplanting too early leaves fragile plants vulnerable to insect pests; transplanting too late results in root-bound, woody seedlings that establish poorly.\n\n- **Optimal Age**: **4 to 6 weeks after sowing** in tomatoes, cabbages, capsicums, and kales.\n- **Physical Readiness Indicators**:\n  1. **Height**: 10 to 15 cm tall (approx. the length of a standard pen).\n  2. **Leaf Count**: 4 to 6 fully expanded, dark-green true leaves.\n  3. **Stem Caliper**: Pencil-thick, sturdy, fibrous stem.\n  4. **Root System**: Dense, white, fibrous root network holding soil particles."
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "The 2 Critical Rules of Successful Transplanting",
                        "content": {
                            "title": "Minimizing Transplant Shock and Root Mortality",
                            "text": "### Rule 1: Transplant Exclusively in the Late Afternoon (from 4:00 PM)\n- Transplanting during the cool evening gives seedlings 12 to 14 hours of dark, cool nighttime humidity to recover root water uptake before facing hot midday sunlight the next day.\n\n### Rule 2: Water Nursery 30 Minutes Prior to Lifting\n- Thoroughly soaking the nursery bed saturates the root zone. When lifted with a hand trowel, the damp soil clings tightly around the roots, forming an **intact root ball** that protects delicate root hairs from tearing or desiccation."
                        }
                    },
                    {
                        "type": "step_process",
                        "title": "Protocol: The Step-by-Step Transplanting Operation",
                        "content": {
                            "title": "Field Transplanting Standard Operating Procedure",
                            "steps": [
                                "1. **Prepare Main Field Holes**: Dig planting holes spaced 60 cm x 60 cm (for tomatoes) or 45 cm x 45 cm (for cabbages). Mix a handful (200g) of well-rotted compost into each hole.",
                                "2. **Pre-Water Nursery Bed**: Soak the nursery bed thoroughly 30 minutes before lifting.",
                                "3. **Lift with Garden Trowel**: Slide the trowel blade 10 cm deep beneath the seedling root system and lift gently. *NEVER pull seedlings forcefully by the stem!*",
                                "4. **Place at Collar Depth**: Lower the seedling into the hole so the soil level matches its original nursery collar depth. *Never bury leaves or leave exposed roots*.",
                                "5. **Firm Soil Around Base**: Press the soil gently with fingertips to eliminate air pockets around roots.",
                                "6. **Water and Mulch Immediately**: Pour 1 liter of water per seedling and place a ring of dry mulch 5 cm away from the stem."
                            ]
                        }
                    }
                ],
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Step-by-Step Seedling Transplanting Protocol with Root Ball",
                        "content": {
                            "title": "Step-by-Step Seedling Transplanting Protocol with Root Ball",
                            "caption": "Sequential technical illustration showing: 1 Trowel lifting intact root ball, 2 Collar depth placement in manured hole, 3 Soil firming to eliminate air pockets, and 4 Immediate watering and light ring mulching."
                        }
                    },
                    {
                        "type": "comparison_table",
                        "title": "Correct vs Incorrect Transplanting Practices",
                        "content": {
                            "title": "Transplanting Execution Matrix",
                            "headers": ["Field Action", "Agronomically Correct Method", "Dangerous Flawed Method"],
                            "rows": [
                                ["Timing of Operation", "Late afternoon (after 4:00 PM) or cloudy overcast days", "Midday under hot scorching noon sun (Severe wilting)"],
                                ["Lifting Technique", "Careful trowel under-cutting with intact soil root ball", "Pulling stem roughly by hand (Strips feeder root hairs)"],
                                ["Planting Depth", "Exact root collar level (Same depth as nursery)", "Burying lower leaves (Triggers stem rot) or exposed roots"],
                                ["Post-Planting Care", "Immediate watering (1L/plant) and light surface ring mulch", "Leaving dry for 24 hours without water (High seedling death)"]
                            ]
                        }
                    }
                ],
                [
                    {
                        "type": "mini_activity",
                        "title": "Field Practical: Transplanting 20 Tomato Seedlings into Main Plot",
                        "content": {
                            "title": "Hands-On Field Crop Establishment Lab",
                            "task": "Working in pairs at 4:30 PM:\n\n1. Water the school nursery bed.\n2. In the main plot, dig holes at 60 cm x 60 cm spacing and add 1 handful of compost per hole.\n3. Use hand trowels to lift 20 tomato seedlings with intact root balls.\n4. Plant at collar depth, firm soil, water immediately with a watering can, and place protective twigs for temporary shading.",
                            "materials": ["20 Hardened Seedlings", "Garden Trowels", "Compost", "Watering Can", "Measuring Stick (60 cm)"],
                            "safety": "Wear garden gloves; wash hands after soil handling."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Core Summary: Crop Establishment",
                        "content": {
                            "title": "Key Takeaways",
                            "text": "- **Transplant at 4–6 weeks** when seedlings are 10–15 cm tall with 4–6 true leaves.\n- **Always transplant in the late afternoon** to give roots cool nighttime recovery.\n- **Pre-water nursery and lift with a trowel** to keep the root ball 100% intact.\n- **Plant at root collar depth**, firm soil to remove air pockets, water, and mulch immediately."
                        }
                    }
                ],
                [
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Transplanting Time and Root Ball Integrity",
                        "content": {
                            "question": "Why is it mandatory for farmers to pre-water the nursery bed and carry out transplanting operations strictly in the late afternoon?",
                            "options": [
                                "Because tractors are legally prohibited from driving during the morning",
                                "Pre-watering allows seedlings to be lifted with an intact soil root ball without stripping root hairs, while late afternoon timing minimizes transpiration water loss during the initial 12 hours of root establishment",
                                "Because insects sleep during the afternoon and cannot see seedlings",
                                "It forces seedlings to grow double the number of roots overnight"
                            ],
                            "answer": "B",
                            "explanation": "Pre-watering softens the soil, allowing the root system to be lifted with a protective ball of soil (root ball) that preserves delicate root hairs. Transplanting in the late afternoon avoids the intense heat and high vapor pressure deficit of midday sun, giving the newly placed seedling 12+ hours of cool night humidity to recover root hydraulic contact before facing morning transpiration stress."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 6: Field Management of Selected Crop
        # =====================================================================
        {
            "unit_order": 6,
            "unit_name": "Field Management of Selected Crop",
            "unit_description": "Irrigation management and blossom end rot prevention; shallow hand weeding; dry organic mulching; vertical staking with 1.5 m wooden stick; tying with loose figure-of-8 sisal loops to prevent stem girdling.",
            "lesson_title": "Field Crop Care: Staking, Weeding, and Moisture Control",
            "pages": [
                [
                    {
                        "type": "suggested_image",
                        "title": "Tomato Plants Staked and Mulched in Commercial Field",
                        "content": {
                            "title": "Tomato Plants Staked and Mulched in Commercial Field",
                            "caption": "Indeterminate tomato vines supported vertically by strong wooden stakes using loose figure-of-8 ties, with organic mulch conserving root moisture."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Field Management & Staking",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Execute field practices: **consistent irrigation, mulching, and shallow weeding**.",
                                "Analyze the physiological cause of **blossom end rot in tomatoes** (calcium deficiency due to erratic watering).",
                                "Demonstrate **staking and trellising** of indeterminate tomatoes using 1.5 m wooden poles.",
                                "Execute the **figure-of-8 knot tying technique** to support stems without causing mechanical stem girdling."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Irrigation and Blossom End Rot Prevention",
                        "content": {
                            "title": "The Physiology of Calcium Transport",
                            "text": "Vegetables require approximately 25 to 35 mm of water per week, especially during flowering and fruit filling:\n\n- **The Blossom End Rot Disaster**: Inconsistent watering (alternating between drought stress and flooding) prevents continuous calcium ($Ca^{2+}$) uptake through the transpiration stream.\n- **Symptoms**: The blossom end (bottom tip) of developing tomato fruits develops a water-soaked spot that turns into a large, sunken, black, leathery scar, rendering the fruit completely unmarketable!\n- **Prevention**: Maintain uniform, consistent soil moisture through regular drip irrigation and thick organic mulching."
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "Why Tomatoes and Capsicums Require Staking",
                        "content": {
                            "title": "Lifting Fruits to the Light",
                            "text": "Indeterminate tomatoes and heavy-fruiting capsicums cannot support their own weight:\n\n1. **Disease Suppression**: Elevates foliage and fruits off damp, spore-laden soil, suppressing fungal early/late blight and ground rot.\n2. **Enhanced Photosynthesis**: Spreads leaves to intercept maximum solar radiation, increasing fruit size and sugar brix levels.\n3. **Ease of Management**: Makes weed control, side-dress fertilization, pesticide spraying, and harvesting effortless.\n4. **Clean Produce**: Ensures fruits remain clean, dry, and free of soil blemishes, qualifying for Grade 1 market premiums."
                        }
                    },
                    {
                        "type": "step_process",
                        "title": "Protocol: The Figure-of-8 Staking Technique",
                        "content": {
                            "title": "Proper Staking and Tying Mechanics",
                            "steps": [
                                "1. **Drive Stake 5–10 cm Away from Stem**: Drive a 1.5 m wooden stake 20 cm deep into the soil 5–10 cm away from the seedling base to avoid severing main roots.",
                                "2. **Wrap String Around Stake First**: Tie soft sisal twine firmly around the wooden stake first.",
                                "3. **Cross Twine in Figure-of-8 Loop**: Cross the twine between the stake and the plant stem to form an '8' shape.",
                                "4. **Loop Loosely Around Stem**: Tie the loop loosely around the tomato stem, leaving a 2 cm buffer space.",
                                "5. **CRITICAL REASON: Prevent Stem Girdling**: As the tomato vine grows, its stem diameter expands from 5 mm to over 25 mm. A tight knot would strangle the stem (girdling), blocking vascular sap flow and killing the vine; the loose figure-of-8 allows natural stem expansion!"
                            ]
                        }
                    }
                ],
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Tomato Staking & Loose Figure-of-8 Tie Mechanics",
                        "content": {
                            "title": "Tomato Staking & Loose Figure-of-8 Tie Mechanics",
                            "caption": "Biomechanical diagram of a tomato plant tied to a 1.5 m wooden stake: Detailed zoom of the loose sisal twine figure-of-8 loop showing stem expansion buffer and mulch layer."
                        }
                    },
                    {
                        "type": "suggested_video",
                        "title": "Tomato Staking and Pruning Guide",
                        "content": {
                            "title": "Tomato Staking and Pruning Guide",
                            "description": "Step-by-step practical video showing stake placement, figure-of-8 loop tying, and pruning lateral suckers on indeterminate tomatoes.",
                            "url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
                        }
                    }
                ],
                [
                    {
                        "type": "mini_activity",
                        "title": "Field Practical: Staking 10 Tomato Plants with Figure-of-8 Ties",
                        "content": {
                            "title": "Hands-On Staking and Figure-of-8 Tying Practical",
                            "task": "In the school tomato plot:\n\n1. Drive 10 wooden stakes (1.5 m tall) 5 cm away from growing tomato plants.\n2. Cut 30 cm lengths of soft sisal twine.\n3. Practice tying loose figure-of-8 loops around the main stems beneath fruit clusters.\n4. Inspect ties to verify a 2 cm finger space between string and stem.",
                            "materials": ["10 Wooden Stakes (1.5m)", "Mallet / Jembe handle", "Sisal Twine", "Scissors"],
                            "safety": "Drive stakes steadily without striking hands."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Core Summary: Staking and Field Care",
                        "content": {
                            "title": "Key Takeaways",
                            "text": "- **Consistent watering prevents blossom end rot** by maintaining calcium transport.\n- **Staking lifts fruits off wet soil**, stopping disease and cosmetic rot.\n- **Always tie with a loose figure-of-8 loop** to avoid lethal stem girdling as stems expand.\n- **Drive stakes 5–10 cm from the plant** to avoid damaging the taproot."
                        }
                    }
                ],
                [
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Staking Figure-of-8 Rationale",
                        "content": {
                            "question": "Why is it an essential horticultural rule to tie a tomato stem to a wooden stake using a loose figure-of-8 loop rather than tying a tight, direct knot?",
                            "options": [
                                "It allows strong wind to rip the tomato vine off the stake easily",
                                "As the tomato stem grows, its diameter increases significantly; a tight knot would pinch the stem and cause lethal mechanical girdling (strangulation of vascular xylem and phloem), whereas a loose figure-of-8 allows safe stem expansion",
                                "Tight knots attract underground termites that eat the fruit",
                                "The figure-of-8 loop forces tomato fruits to turn square"
                            ],
                            "answer": "B",
                            "explanation": "Tomato stems expand rapidly in diameter during vegetative and fruit-filling stages. A tight direct knot creates a physical choke point that cuts into the tender bark, severing the vascular cambium (xylem and phloem). This girdling effect halts water and nutrient flow, killing the plant above the knot. A loose figure-of-8 loop cushions the stem while allowing unrestricted radial expansion."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 7: Monitoring Crop Growth
        # =====================================================================
        {
            "unit_order": 7,
            "unit_name": "Monitoring Crop Growth",
            "unit_description": "Field diagnostics: healthy crop signals vs mobile nitrogen chlorosis (yellowing of older lower leaves) vs phosphorus purpling; maintaining a 4-column Field Management Logbook.",
            "lesson_title": "Field Diagnostics, Nutrient Scouting, and Logbooks",
            "pages": [
                [
                    {
                        "type": "suggested_image",
                        "title": "Agronomist Conducting Routine Field Scouting and Health Audit",
                        "content": {
                            "title": "Agronomist Conducting Routine Field Scouting and Health Audit",
                            "caption": "An agricultural scout systematically inspecting crop foliage, monitoring vegetative development, and diagnosing nutrient deficiency symptoms in a farm field."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Scouting & Diagnostics",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Conduct a weekly **crop growth and diagnostic health audit** across field rows.",
                                "Diagnose symptoms of **Nitrogen ($N$) chlorosis** on older lower leaves vs **Phosphorus ($P$) purpling**.",
                                "Identify common insect pest feeding signatures (leaf holes, sap sucking, webbing).",
                                "Maintain a structured **4-Column Field Management Logbook** for agribusiness record keeping."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The Diagnostic Scouting Protocol",
                        "content": {
                            "title": "Reading the Plant's Signals",
                            "text": "Commercial agribusiness managers walk their fields weekly to detect anomalies before they cause yield loss:\n\n- **Healthy Growth**: Turgid stems, vibrant dark-green leaves, robust flower set, and clean developing fruits.\n- **Nitrogen ($N$) Deficiency**: Progressive **chlorosis** (uniform pale yellowing) starting on older lower leaves, caused by the mobile translocation of nitrogen to young shoots. Leads to stunted, thin, woody stems.\n- **Phosphorus ($P$) Deficiency**: Purplish or dark reddish-bronze coloration along veins of older leaves, accompanied by poor root development and delayed flowering.\n- **Pest Damage**: Rolled leaves (leaf rollers), chewed margins (caterpillars), sticky honeydew/sooty mold (aphids, whiteflies), and fine webbing (spider mites)."
                        }
                    }
                ],
                [
                    {
                        "type": "comparison_table",
                        "title": "Visual Nutrient Deficiency Diagnostic Chart",
                        "content": {
                            "title": "Foliar Deficiency Comparison",
                            "headers": ["Mineral Element", "Mobility in Plant", "First Location of Symptoms", "Visual Foliar Signature"],
                            "rows": [
                                ["Nitrogen (N)", "Highly Mobile", "Older Lower Leaves First", "Uniform pale yellow chlorosis; V-shaped midrib yellowing in cereals"],
                                ["Phosphorus (P)", "Mobile", "Older Lower Leaves First", "Distinct purple/reddish discoloration; stunted root growth"],
                                ["Potassium (K)", "Mobile", "Older Lower Leaves First", "Marginal scorching, leaf tip curling, and necrotic edges"],
                                ["Calcium (Ca)", "Immobile", "Young Growing Tips & Fruits", "Blossom end rot in tomato fruits; distorted, cupped young leaves"],
                                ["Iron (Fe)", "Immobile", "Youngest Top Leaves First", "Interveinal chlorosis (yellow leaf blade with sharp dark-green veins)"]
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Maintaining the 4-Column Field Logbook",
                        "content": {
                            "title": "Tracking Farm Operations and Inputs",
                            "text": "Every enterprise requires disciplined data logging to evaluate cost efficiency and schedule future operations:\n\n| Date | Growth Stage / Observation | Farm Activity Performed | Inputs & Quantity Used |\n| :--- | :--- | :--- | :--- |\n| **12/09/2026** | Seedlings 12cm tall; 5 leaves | Transplanted into main plot | 50 tomato seedlings; 5kg compost |\n| **19/09/2026** | Established; minor weeds | Hand weeded and applied mulch | Sisal string; dry grass mulch |\n| **03/10/2026** | Early flowering started | Staked all plants; top-dressed | 50 wooden stakes; 2.5kg CAN |"
                        }
                    }
                ],
                [
                    {
                        "type": "step_process",
                        "title": "Protocol: Responding to Diagnostic Scouting Findings",
                        "content": {
                            "title": "Action Steps for Identified Crop Stresses",
                            "steps": [
                                "1. **If Lower Leaf Chlorosis (N Deficiency)**: Top-dress immediately with 10g CAN per plant in a covered ring at the drip line, or apply high-N foliar spray.",
                                "2. **If Purple Leaf Veins (P Deficiency)**: Verify soil pH; apply rock phosphate or soluble foliar feed.",
                                "3. **If Black Fruit Bottoms (Blossom End Rot)**: Regulate irrigation to steady daily intervals; spray foliar calcium nitrate.",
                                "4. **If Aphid / Whitefly Swarms**: Spray organic neem oil solution or insecticidal soap on leaf undersides.",
                                "5. **Log All Actions in Field Book**: Record input quantities, labor costs, and response timelines."
                            ]
                        }
                    },
                    {
                        "type": "mini_activity",
                        "title": "Field Practical: Diagnostic Scouting Walk and Logbook Entry",
                        "content": {
                            "title": "School Farm Diagnostic Health Walk",
                            "task": "1. In pairs, walk through the school vegetable beds.\n2. Inspect 10 plants across different rows.\n3. Identify any symptoms of chlorosis, purpling, blossom end rot, or insect feeding.\n4. Fill in a complete 4-column logbook entry with observations and recommended corrective actions.",
                            "materials": ["Field Logbook", "Magnifying Hand Lens", "Ruler", "Pen"],
                            "safety": "Do not touch unidentified stinging caterpillars."
                        }
                    }
                ],
                [
                    {
                        "type": "key_takeaway",
                        "title": "Core Summary: Crop Monitoring & Records",
                        "content": {
                            "title": "Key Takeaways",
                            "text": "- **Scout fields weekly** to detect nutrient deficiencies, pests, and water stress early.\n- **Nitrogen chlorosis** appears on older lower leaves first due to vascular nutrient mobility.\n- **Blossom end rot** is caused by erratic watering disrupting calcium uptake.\n- **A 4-column Field Logbook** is mandatory for professional agribusiness tracking."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Diagnosing Mobile Nitrogen Chlorosis",
                        "content": {
                            "question": "While scouting a school vegetable plot, a student notices that the older, lower leaves of the tomato crop are turning a uniform pale yellow, while the youngest top leaves remain green. What is the diagnosis and remedy?",
                            "options": [
                                "Iron deficiency; spray sulfuric acid immediately",
                                "Nitrogen deficiency; apply fast-acting CAN top-dressing in a covered ring at the drip line or spray high-nitrogen foliar feed",
                                "The tomatoes are ready for harvesting",
                                "Soil is too rich in gold and silver"
                            ],
                            "answer": "B",
                            "explanation": "Nitrogen is a mobile nutrient. When soil nitrogen is deficient, the plant translocates nitrogen from its older, lower leaves upward to sustain the young growing shoot tips. This causes generalized chlorosis (yellowing) on older leaves first. The remedy is an emergency top-dressing of fast-acting Calcium Ammonium Nitrate (CAN) or a high-nitrogen foliar spray."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 8: Harvesting the Selected Crop
        # =====================================================================
        {
            "unit_order": 8,
            "unit_name": "Harvesting the Selected Crop",
            "unit_description": "Maturity indices for vegetables: tomatoes (green mature, breaker, fully ripe), cabbages (firm solid head, wrapper leaf curling), capsicums (firm skin, color break); cool morning harvesting; clean pedicel cutting; gentle crate handling.",
            "lesson_title": "Harvest Maturity Indices and Post-Harvest Handling",
            "pages": [
                [
                    {
                        "type": "suggested_image",
                        "title": "Harvesting Fresh Red Ripe Tomatoes into Farm Crates",
                        "content": {
                            "title": "Harvesting Fresh Red Ripe Tomatoes into Farm Crates",
                            "caption": "Freshly harvested, premium-grade red ripe tomatoes handled gently with intact pedicels and packed into ventilated harvest crates."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Harvest Maturity & Handling",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Identify physical maturity stages for **tomatoes (green mature, breaker, ripe)**, **cabbages**, and **capsicums**.",
                                "Match tomato harvest maturity stages to specific marketing channels (long-distance transit vs local retail).",
                                "Execute safe harvesting techniques using clean shears/knives to leave **pedicels intact**.",
                                "Apply post-harvest handling rules: **cool morning harvest, gentle handling, and ventilated crate storage**."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Identifying Harvest Maturity in Vegetables",
                        "content": {
                            "title": "Precision Harvesting Secures Market Value",
                            "text": "Harvesting at the correct maturity stage is critical to maximizing shelf-life and preventing post-harvest losses:\n\n### 1. Tomatoes (*Solanum lycopersicum*)\n- **Green Mature Stage**: Fruit is fully sized, shiny, with internal jelly formed, but skin is green. *Optimal for long-distance transport (ripen slowly in transit without bruising)*.\n- **Breaker Stage**: First blush of pink/yellow appears at the blossom end tip (less than 10% color). *Ideal for wholesale markets and retail supermarkets*.\n- **Fully Ripe Stage**: Fruit is 100% red or yellow, firm, and fully developed. *Best for immediate local sale, hotels, and home consumption*.\n\n### 2. Cabbages (*Brassica oleracea*)\n- The head feels hard and solid when pressed firmly with the hand; outer wrapper leaves curl outward and turn slightly yellow.\n\n### 3. Capsicums (Sweet Peppers)\n- Fruits reach full size, walls are thick and firm, and skin shows shiny gloss (or color break to red/yellow for colored varieties)."
                        }
                    }
                ],
                [
                    {
                        "type": "comparison_table",
                        "title": "Tomato Maturity Stages and Market Suitability",
                        "content": {
                            "title": "Tomato Harvesting Stages Matrix",
                            "headers": ["Maturity Stage", "Physical Appearance & Firmness", "Target Market / Destination", "Post-Harvest Advantage"],
                            "rows": [
                                ["Green Mature", "100% green skin; fully sized; very hard", "Long-distance transport (>100 km) and export", "Highest firmness; zero transit squashing; ripens in 7–10 days"],
                                ["Breaker / Turning", "First pink/yellow star at blossom end (<10% color)", "Local supermarkets and retail grocery stores", "Perfect balance of shelf-life (4–6 days) and flavor development"],
                                ["Fully Ripe (Red)", "100% red/crimson; firm but softening", "Immediate farm-gate sale, schools, and restaurants", "Maximum sugar brix and flavor; immediate culinary use"]
                            ]
                        }
                    },
                    {
                        "type": "step_process",
                        "title": "Protocol: 4 Rules of Post-Harvest Handling",
                        "content": {
                            "title": "Preserving Produce Shelf-Life",
                            "steps": [
                                "1. **Harvest in Cool Morning Hours**: Pick produce before 9:00 AM when field heat is low, preserving crispness and shelf-life.",
                                "2. **Clean Pedicel Cut**: Cut tomato and capsicum stems cleanly with shears, leaving a small stem piece attached. *NEVER yank or pull fruits roughly, which tears the skin and creates wounds for fungal rot!*",
                                "3. **Cabbage Base Cut with Wrapper Leaves**: Cut cabbage heads at the soil base, leaving 2–3 outer wrapper leaves to shield the head from transport bruising.",
                                "4. **Pack in Ventilated Crates**: Place produce gently into smooth, ventilated plastic crates; store immediately in a shaded, cool packing shed."
                            ]
                        }
                    }
                ],
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Tomato Harvest Maturity Stages: Green Mature vs Breaker vs Ripe",
                        "content": {
                            "title": "Tomato Harvest Maturity Stages: Green Mature vs Breaker vs Ripe",
                            "caption": "Maturity continuum diagram illustrating: Stage 1 Mature Green (Hard, transit ready), Stage 2 Breaker (Pink blossom star, retail ready), and Stage 3 Full Ripe Red (Local market ready) with pedicel cut detail."
                        }
                    },
                    {
                        "type": "mini_activity",
                        "title": "Field Practical: Maturity Indexing and Harvesting Practical",
                        "content": {
                            "title": "Grading and Harvesting Tomato Fruits",
                            "task": "In the school garden:\n\n1. Inspect 10 tomato plants and categorize fruits into Green Mature, Breaker, Pink, and Red Ripe.\n2. Use sharp secateurs to harvest 5 breaker-stage fruits with pedicels intact.\n3. Pack gently into a ventilated crate and inspect for skin damage.\n4. Cut cabbages with 2 protective wrapper leaves.",
                            "materials": ["Harvesting Shears", "Plastic Crates", "Tomato / Cabbage Plot"],
                            "safety": "Keep fingers clear of cutting blades."
                        }
                    }
                ],
                [
                    {
                        "type": "key_takeaway",
                        "title": "Core Summary: Harvesting & Quality",
                        "content": {
                            "title": "Key Takeaways",
                            "text": "- **Harvest tomatoes at Green Mature / Breaker stage** for long-distance transport.\n- **Harvest fully ripe tomatoes** for immediate local market consumption.\n- **Always harvest during cool morning hours** to minimize field heat.\n- **Cut pedicels cleanly** with shears and use ventilated crates to prevent bruising and rot."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Matching Harvest Maturity to Transit Distance",
                        "content": {
                            "question": "A school agribusiness club in Kitale plans to transport a 1-ton harvest of tomatoes 350 kilometers to Nairobi over bumpy roads. At which maturity stage must they harvest the fruits to minimize transit losses?",
                            "options": [
                                "Fully red, deep crimson, and soft stage",
                                "Green mature or breaker stage (where fruits are firm and just showing the first blush of color)",
                                "Early flowering vegetative stage",
                                "Over-ripe stage when skin is splitting"
                            ],
                            "answer": "B",
                            "explanation": "At the green mature or breaker stage, tomato fruits have reached full size but remain physically firm and resistant to compression damage during long transit over rough roads. They will naturally synthesize ethylene and complete their uniform red ripening by the time they reach retail markets in Nairobi."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 9: Justifying Management Practices
        # =====================================================================
        {
            "unit_order": 9,
            "unit_name": "Justifying Management Practices",
            "unit_description": "Scientific, economic, and ecological justifications for crop management practices (nursery bedding, pruning, staking, mulching); soil humus accumulation; water stewardship; Integrated Pest Management (IPM).",
            "lesson_title": "Scientific, Economic, and Ecological Justifications",
            "pages": [
                [
                    {
                        "type": "suggested_image",
                        "title": "Sustainable Smallholder Horticulture and Ecological Stewardship",
                        "content": {
                            "title": "Sustainable Smallholder Horticulture and Ecological Stewardship",
                            "caption": "Smallholder farmers practicing sustainable vegetable production using organic mulching, integrated pest management, and water conservation in Kenya."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Justifying Management Practices",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Articulate the **scientific principles** behind nursery bedding, pruning, staking, and mulching.",
                                "Analyze the **agribusiness and economic justifications** (seed savings, Grade 1 premiums, labor efficiency).",
                                "Explain the **ecological benefits** of humus accumulation, water conservation, and Integrated Pest Management (IPM).",
                                "Formulate evidence-based arguments for sustainable horticultural production."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The Science and Economics of Crop Management",
                        "content": {
                            "title": "Why Professional Agronomists Perform Farm Chores",
                            "text": "Every farm operation is grounded in physiological and economic logic that directly impacts crop yields and farm revenue.\n\n- **Nursery Bedding**: Protects fragile root systems during early cell division, maximizing the germination of expensive hybrid seeds and cutting seed waste.\n- **Pruning**: Redirects plant sugars from non-productive leaves to fruit clusters, producing large, premium Grade 1 fruits.\n- **Staking**: Elevates fruits away from damp soil pathogens, eliminating rot and cosmetic defects to secure premium market prices.\n- **Mulching**: Blocks light to weed seeds and cuts soil water evaporation by 70%, slashing weeding labor and irrigation costs."
                        }
                    }
                ],
                [
                    {
                        "type": "comparison_table",
                        "title": "Master Justification Matrix for Crop Management",
                        "content": {
                            "title": "Agronomic Justification Matrix",
                            "headers": ["Field Practice", "Scientific / Physiological Reason", "Economic / Agribusiness Justification", "Ecological Impact"],
                            "rows": [
                                ["Nursery Bedding", "Concentrates water/nutrients; protects delicate root systems", "Cuts seed wastage; ensures 100% uniform field population", "Reduces pesticide application area by 90% during early growth"],
                                ["Pruning (Suckering)", "Redirects photosynthetic sugars into fruit expansion", "Increases fruit size and Grade 1 supermarket price premiums", "Opens canopy to airflow; lowers fungal chemical spray frequency"],
                                ["Staking & Trellising", "Prevents fruit contact with soil-borne fungal spores", "Eliminates ground rot losses; maximizes harvestable tonnage", "Allows vertical high-density production, saving land space"],
                                ["Organic Mulching", "Smothers weed seeds; breaks soil evaporation boundary layer", "Saves 70% irrigation costs and cuts weeding labor", "Decomposes into permanent soil organic humus, improving fertility"],
                                ["Precision Top-Dressing", "Supplies nitrogen at exponential growth demand windows", "Generates 300%+ Return on Investment (ROI) in leaf/fruit weight", "Covering prevents ammonia gas loss and water eutrophication"]
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Integrated Pest Management (IPM) and Water Stewardship",
                        "content": {
                            "title": "Long-Term Farm Sustainability",
                            "text": "Senior secondary agriculture champions environmental and ecological longevity:\n\n- **Integrated Pest Management (IPM)**: Combines physical weeding, crop rotation, and biological predators to keep pests below economic injury levels, minimizing synthetic chemical pesticide residues on food and protecting honeybee pollinators.\n- **Water Stewardship**: Efficient drip irrigation and mulching prevent the over-extraction of community aquifers and rivers in Kenya's arid and semi-arid lands (ASALs)."
                        }
                    }
                ],
                [
                    {
                        "type": "mini_activity",
                        "title": "Class Debate: Chemical-Only vs Integrated Sustainable Horticulture",
                        "content": {
                            "title": "Debating Agronomic Sustainability",
                            "task": "Divide into two teams:\n- Team A: Advocates for chemical-intensive quick-fix farming (heavy broadcast fertilizers, non-stop synthetic spraying).\n- Team B: Advocates for Integrated Sustainable Horticulture (mulching, compost, IPM, precision top-dressing).\n\nPresent 3 structured arguments evaluating: 1. Input costs, 2. Long-term soil health, 3. Community water safety.",
                            "materials": ["Debate Guidelines", "Notebook"],
                            "safety": "Maintain respectful, evidence-based academic discourse."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Core Summary: Justifying Practices",
                        "content": {
                            "title": "Key Takeaways",
                            "text": "- **Every management practice is grounded in scientific and economic principles**.\n- **Pruning and staking** transform unmarketable crops into premium Grade 1 produce.\n- **Mulching and composting** build long-term soil humus and slash water expenses.\n- **IPM and water stewardship** ensure ecological and economic sustainability."
                        }
                    }
                ],
                [
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Economic and Scientific Rationale of Mulching",
                        "content": {
                            "question": "Which of the following statements provides the strongest combined scientific, economic, and ecological justification for applying organic mulch in a vegetable field?",
                            "options": [
                                "Mulching converts the soil into white lime and repels birds permanently",
                                "Scientifically, it reduces soil water evaporation and smothers weed seeds; economically, it slashes irrigation water and weeding labor costs; ecologically, it breaks down into organic humus that enhances long-term soil structure",
                                "Mulching forces crops to produce fruits without flowers",
                                "Mulching attracts termites that eat the weeds"
                            ],
                            "answer": "B",
                            "explanation": "Organic mulching is an exemplary sustainable practice: it physically blocks light to suppress weed seed germination and halts capillary water evaporation (scientific), directly reduces farm expenditure on irrigation and weeding labor (economic), and gradually decomposes into stable organic humus that improves soil water-holding capacity and fertility for future seasons (ecological)."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 10: Synthesis and Practical Assessment
        # =====================================================================
        {
            "unit_order": 10,
            "unit_name": "Synthesis and Practical Assessment",
            "unit_description": "Full crop lifecycle synthesis (Planning -> Nursery -> Nursery Mgmt -> Establishment -> Field Mgmt -> Harvesting); Agribusiness project portfolio & ROI calculation; 8 Summative Topic Assessment MCQs.",
            "lesson_title": "Synthesis of Crop Production and Summative Assessment",
            "pages": [
                [
                    {
                        "type": "suggested_image",
                        "title": "Successful School Agriculture Garden Project Harvest",
                        "content": {
                            "title": "Successful School Agriculture Garden Project Harvest",
                            "caption": "A thriving school vegetable garden project demonstrating the complete crop production cycle from nursery establishment to harvest."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Synthesis & Summative Assessment",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Synthesize the **6-phase crop production lifecycle** (Planning $\\rightarrow$ Nursery $\\rightarrow$ Husbandry $\\rightarrow$ Establishment $\\rightarrow$ Field Care $\\rightarrow$ Harvest).",
                                "Perform a comprehensive **Agribusiness Project Financial Audit** (Revenue, Total Cost, Net Profit, ROI).",
                                "Draft an advisory plan to rehabilitate mismanaged crop plots.",
                                "Complete the comprehensive **Summative Topic Assessment** covering all 10 lessons of Topic 5."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The Complete 6-Phase Crop Production Lifecycle",
                        "content": {
                            "title": "From Seed Selection to Market Ledger",
                            "text": "1. **Planning & Enterprise Selection**: Evaluate market demand, agro-ecological fit, water access, and maturity duration.\n2. **Nursery Construction & Sowing**: Prepare 1.0 m wide fine-tilth bed, drill seeds 10–15 cm apart at 1.5 cm depth, mulch, and erect 1.0 m sloped shade.\n3. **Nursery Husbandry & Hardening**: Water twice daily with fine rose, thin, prick out at 2 true leaves, and harden off 2 weeks prior.\n4. **Field Establishment (Transplanting)**: Water nursery, lift with intact root ball using trowel, plant at collar depth in late afternoon, water and mulch.\n5. **Field Management**: Stake with loose figure-of-8 ties, prune lateral suckers, top-dress CAN at drip line, and weed regularly.\n6. **Harvesting & Agribusiness Accounting**: Harvest at breaker/ripe stage in cool morning, pack in crates, market produce, and audit net profit."
                        }
                    }
                ],
                [
                    {
                        "type": "suggested_diagram",
                        "title": "The Complete 6-Phase Crop Production Lifecycle",
                        "content": {
                            "title": "The Complete 6-Phase Crop Production Lifecycle",
                            "caption": "Circular continuous lifecycle diagram showcasing: Phase 1 Planning, Phase 2 Nursery Sowing, Phase 3 Nursery Husbandry, Phase 4 Field Establishment, Phase 5 Field Management, and Phase 6 Harvesting & Accounting."
                        }
                    },
                    {
                        "type": "comparison_table",
                        "title": "Agribusiness Project Financial Performance Statement",
                        "content": {
                            "title": "Crop Enterprise Ledger Example (500 Tomato Plants)",
                            "headers": ["Cost / Revenue Item", "Quantity / Unit", "Unit Cost (KES)", "Total Amount (KES)"],
                            "rows": [
                                ["Certified Hybrid Seeds", "1 Packet (50g)", "2,500", "2,500"],
                                ["Cured Organic Compost", "4 Bags", "500", "2,000"],
                                ["CAN Top-Dressing Fertilizer", "1 Bag (50kg)", "3,500", "3,500"],
                                ["Wooden Stakes & Sisal Twine", "500 Stakes + Twine", "4,000", "4,000"],
                                ["Total Production Cost", "—", "—", "KES 12,000"],
                                ["Gross Harvest Revenue", "1,200 kg @ KES 60/kg", "60 / kg", "KES 72,000"],
                                ["Net Financial Profit", "KES 72,000 - KES 12,000", "—", "+ KES 60,000 (500% ROI!)"]
                            ]
                        }
                    }
                ],
                [
                    {
                        "type": "mini_activity",
                        "title": "Performance Task: Drafting a Crop Project Portfolio & Advisory Brief",
                        "content": {
                            "title": "Agribusiness Turnaround Brief",
                            "task": "A farmer in Kakamega broadcast hybrid cabbage seeds directly onto dry unweeded field soil, resulting in sparse, spindly seedlings that died in heavy rain.\n\n**Your Deliverable**: Draft a 1-page Corrective Advisory Note explaining:\n1. Her 3 major agronomic errors.\n2. A step-by-step nursery establishment and transplanting plan for her next crop cycle.\n3. A 4-column Field Management Logbook template.",
                            "materials": ["Case Handout", "Advisory Template", "Pen"],
                            "safety": "Ensure professional, supportive agribusiness recommendations."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Core Summary: Crop Production Mastery",
                        "content": {
                            "title": "Key Takeaways",
                            "text": "- **Follow the 6-phase production lifecycle** from planning to harvest accounting.\n- **Small seeds must be raised in fine-tilth nursery beds** to maximize germination.\n- **Harden off seedlings and transplant in the late afternoon** with intact root balls.\n- **Stake with loose figure-of-8 ties** and scout weekly for pests and nutrient deficiencies.\n- **Audit project finances** to ensure positive agribusiness profit margins."
                        }
                    }
                ],
                # Pages 4 to 8: 8 Summative Assessment MCQs
                [
                    {
                        "type": "knowledge_check",
                        "title": "Summative MCQ 1: Nursery Bed Width Rationale",
                        "content": {
                            "question": "Why is it an established standard agricultural design rule to construct vegetable nursery beds with a width of exactly 1.0 meter?",
                            "options": [
                                "It allows tractor-mounted disc harrows to cultivate the nursery automatically",
                                "It allows the farmer to comfortably reach the center of the bed from either side for weeding, watering, and thinning without stepping on the soil and compacting the fine tilth",
                                "It prevents wind currents from reaching the seeds",
                                "It forces the seedlings to grow 1 meter tall"
                            ],
                            "answer": "B",
                            "explanation": "A 1.0-meter width allows a comfortable reaching distance of 50 cm from either side. This allows the grower to carry out all manual maintenance tasks without ever stepping on the seedbed, preventing soil compaction and root damage."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Summative MCQ 2: Prompt Mulch Removal upon Germination",
                        "content": {
                            "question": "What is the primary agronomic danger of failing to remove the dry grass mulch layer immediately after seedlings begin to emerge in a nursery bed?",
                            "options": [
                                "The seeds will undergo secondary dormancy",
                                "Seedlings will be deprived of sunlight and stretch upward rapidly, becoming excessively tall, thin, pale yellow, and mechanically weak (etiolation)",
                                "The soil pH will drop to zero immediately",
                                "The grass mulch will turn into destructive caterpillars"
                            ],
                            "answer": "B",
                            "explanation": "Emerging seedlings require sunlight immediately for photosynthesis. Leaving mulch over emerging shoots blocks light, causing etiolation—where seedlings stretch into spindly, pale, weak stems that collapse and die."
                        }
                    }
                ],
                [
                    {
                        "type": "knowledge_check",
                        "title": "Summative MCQ 3: Hardening Off Protocol",
                        "content": {
                            "question": "How does a farmer practically carry out the hardening off process for vegetable seedlings 1 to 2 weeks before transplanting?",
                            "options": [
                                "By applying heavy doses of urea fertilizer to double seedling height",
                                "By gradually reducing the frequency of watering and progressively removing the overhead shade frame to expose seedlings to full sun",
                                "By placing seedlings under airtight plastic sheets",
                                "By submerging the nursery bed under 30 cm of water"
                            ],
                            "answer": "B",
                            "explanation": "Hardening off involves gradually reducing watering frequency and removing the shade cover 1–2 weeks before transplanting. This builds thicker leaf cuticles, accumulates protective sugars, and develops a sturdy root system that minimizes transplant shock in the open field."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Summative MCQ 4: Seedling Lifting and Root Ball Preservation",
                        "content": {
                            "question": "Why should a farmer heavily water the nursery bed 30 minutes before lifting seedlings with a garden trowel?",
                            "options": [
                                "To wash all the soil off the roots so seedlings are light to carry",
                                "To soften the soil so the roots can be lifted intact with a protective ball of soil around them, preventing damage and desiccation to fine feeder root hairs",
                                "To drown all earthworms living in the nursery",
                                "To turn the nursery soil into liquid mud"
                            ],
                            "answer": "B",
                            "explanation": "Pre-watering softens the soil, allowing the trowel to slide underneath and lift the seedling with an intact root ball. This preserves delicate root hairs and prevents root desiccation, ensuring rapid establishment after transplanting."
                        }
                    }
                ],
                [
                    {
                        "type": "knowledge_check",
                        "title": "Summative MCQ 5: Timing of Field Transplanting",
                        "content": {
                            "question": "Why is it strongly recommended to transplant seedlings into the main field in the late afternoon (from 4:00 PM) rather than during midday?",
                            "options": [
                                "Because farm workers are only available in the evening",
                                "Late afternoon transplanting minimizes transpiration water loss and gives the young plant 12 hours of cool nighttime humidity to recover before facing hot sun",
                                "Because soil nutrients only become active at night",
                                "Because seeds only germinate after sunset"
                            ],
                            "answer": "B",
                            "explanation": "Transplanting in the late afternoon avoids the intense heat and high transpiration stress of midday sun, giving newly placed seedlings a cool, humid overnight period to re-establish root hydraulic contact with the soil."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Summative MCQ 6: Figure-of-8 Staking Knot Mechanics",
                        "content": {
                            "question": "Why must a tomato stem be tied to a wooden stake using a loose figure-of-8 loop rather than a tight, direct knot?",
                            "options": [
                                "To allow the wind to slide the plant completely off the stake",
                                "To provide firm mechanical support while allowing the stem to expand in diameter as it matures without suffering lethal constriction and vascular girdling",
                                "To force tomato vines to produce flowers on the stake",
                                "To prevent bees from visiting the plant"
                            ],
                            "answer": "B",
                            "explanation": "A tight knot around a growing tomato stem pinches and strangles the stem as its diameter expands (girdling), cutting off the flow of water and sugars through the xylem and phloem. A loose figure-of-8 loop provides support while allowing unrestricted radial expansion."
                        }
                    }
                ],
                [
                    {
                        "type": "knowledge_check",
                        "title": "Summative MCQ 7: Mobile Nitrogen Deficiency Diagnosis",
                        "content": {
                            "question": "During a field walk, you observe that the bottom older leaves of your tomato crop are turning pale yellow (chlorotic), while the top young leaves remain light green. What is the physiological cause?",
                            "options": [
                                "Iron toxicity in the top leaves",
                                "Nitrogen deficiency; because nitrogen is mobile, the plant scavenges nitrogen from old lower leaves and moves it to the growing tip",
                                "The tomato crop has completed its lifecycle",
                                "Excessive potassium in the soil"
                            ],
                            "answer": "B",
                            "explanation": "Nitrogen is highly mobile within plant tissues. Under nitrogen deficiency, the plant breaks down chlorophyll in older lower leaves and translocates the mobile nitrogen ions upward to sustain new growing shoots, causing lower-leaf chlorosis first."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Summative MCQ 8: Agribusiness Net Profit Calculation",
                        "content": {
                            "question": "A student club harvested 250 kg of tomatoes and sold them at KES 60 per kg. Their total production costs were KES 5,000. What was their total revenue and net financial profit?",
                            "options": [
                                "Revenue: KES 10,000; Profit: KES 5,000",
                                "Revenue: KES 15,000; Net Profit: KES 10,000",
                                "Revenue: KES 15,000; Net Profit: KES 5,000",
                                "Revenue: KES 5,000; Net Profit: KES 0"
                            ],
                            "answer": "B",
                            "explanation": "Total Revenue = $250\\text{ kg} \\times \\text{KES } 60 = \\text{KES } 15,000$. Net Profit = $\\text{Total Revenue} - \\text{Total Cost} = \\text{KES } 15,000 - \\text{KES } 5,000 = \\text{KES } 10,000$."
                        }
                    }
                ],
                # Page 8: Capstone Summary
                [
                    {
                        "type": "summary",
                        "title": "Topic 5 Capstone Summary: Growing Selected Crops Mastery",
                        "content": {
                            "title": "Mastery Overview: Grade 10 Crop Production Lifecycle",
                            "text": "Congratulations on mastering **Topic 5: Growing Selected Crops**!\n\nYou have mastered:\n- **Enterprise Selection**: Evaluating market demand, agro-ecological fit, water access, and maturity duration.\n- **Nursery Siting & Preparation**: 1.0 m standard width, deep digging, fine tilth refining, and organic compost mixing.\n- **Drilling, Mulching & Shading**: 10–15 cm furrow spacing, 1.5 cm depth, sloped shade frames, and prompt mulch removal.\n- **Nursery Husbandry**: Fine-rose watering, thinning, pricking out at 2 true leaves, and 2-week hardening off.\n- **Field Establishment**: Pre-watering nursery, lifting intact root balls, late afternoon transplanting at collar depth, and initial shading.\n- **Field Management**: Staking with loose figure-of-8 ties, pruning suckers, precision CAN top-dressing, and weeding.\n- **Monitoring & Harvesting**: Diagnosing mobile nitrogen chlorosis, harvesting at green mature/breaker/ripe stages, and project financial accounting."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Topic 5 Final Takeaway",
                        "content": {
                            "title": "The Commercial Crop Husbandry Maxim",
                            "text": "Raise seedlings with tender care in the nursery, harden them for the field, establish them with intact root balls, manage them with scientific precision, and harvest at peak market grade for commercial agribusiness success."
                        }
                    }
                ]
            ]
        }
    ]

@transaction.atomic
def ingest_grade10_topic5(replace=False):
    """Executes the complete production ingestion of Grade 10 Agriculture Topic 5: Growing Selected Crops."""
    print("=" * 80)
    print("STARTING INGESTION: CBC Grade 10 Agriculture — Topic 5: Growing Selected Crops")
    print("=" * 80)

    curriculum = Curriculum.objects.filter(name__iexact="CBC").first()
    grade = Grade.objects.filter(curriculum=curriculum, name__icontains="10").first()
    subject = Subject.objects.filter(grade=grade, name__iexact="Agriculture").first()

    assert curriculum and grade and subject, "Curriculum/Grade/Subject not found!"

    topic_name = "Growing Selected Crops"
    topic = Topic.objects.filter(subject=subject, name=topic_name).first()
    if not topic:
        topic = Topic.objects.create(
            subject=subject,
            name=topic_name,
            description="Comprehensive theoretical, practical, and scientific study of vegetable nursery establishment, crop management, field establishment, harvesting, and agribusiness project evaluation.",
            order=5
        )
        print(f"Created Topic 5: {topic.name} (ID: {topic.id})")
    else:
        topic.order = 5
        topic.description = "Comprehensive theoretical, practical, and scientific study of vegetable nursery establishment, crop management, field establishment, harvesting, and agribusiness project evaluation."
        topic.save()
        print(f"Resolved Topic 5: {topic.name} (ID: {topic.id})")

    if replace:
        print("Flag --replace active: Clearing existing LearningUnits and Lessons for Topic 5...")
        topic.learning_units.all().delete()
        topic.lessons.all().delete()

    curriculum_data = build_topic5_curriculum()
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
                    "topic_order": 5,
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
                    block_id=f"g10_agri_t5_u{u_order}_p{page_idx}_b{comp_idx}",
                    block_type=b_type,
                    component_type=b_type,
                    title=b_title,
                    content=b_content,
                    order=block_order_counter,
                    page_number=page_idx,
                    component_order=comp_idx,
                    page_title=b_title if comp_idx == 1 else None,
                    metadata={"topic_order": 5, "unit_order": u_order, "page": page_idx}
                )
                block_order_counter += 1
                total_blocks += 1

        print(f"  Ingested Unit {u_order}: {u_name} -> Lesson '{l_title}' ({len(pages)} Pages, {block_order_counter - 1} Blocks)")

    print("=" * 80)
    print(f"INGESTION COMPLETE: Topic 5 '{topic.name}'")
    print(f"  Total Units:   {total_units}")
    print(f"  Total Lessons: {total_lessons}")
    print(f"  Total Pages:   {total_pages}")
    print(f"  Total Blocks:  {total_blocks}")
    print("=" * 80)

if __name__ == "__main__":
    replace_flag = "--replace" in sys.argv
    ingest_grade10_topic5(replace=replace_flag)
