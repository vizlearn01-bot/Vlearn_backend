"""
VLearn CBC Grade 10 Agriculture — Topic 4: Field Management Practices
Production Ingestion Engine (Deep Senior Secondary Pedagogical Edition)

Curriculum: CBC (ID: 5)
Grade: Grade 10 (ID: 5, Level: 10)
Subject: Agriculture
Topic: Field Management Practices (Topic Order: 4)

Decomposed into 10 Learning Units & 10 Published Lessons:
  1. Introduction to Field Management Practices (6 Pages, 12 Blocks)
  2. Pruning Capsicum (6 Pages, 13 Blocks)
  3. Single-Stem Pruning of Tomatoes (6 Pages, 12 Blocks)
  4. Multiple-Stem Pruning of Tomatoes (6 Pages, 13 Blocks)
  5. Pruning Perennial Crops (6 Pages, 12 Blocks)
  6. Top-Dressing Materials and Timing (6 Pages, 12 Blocks)
  7. Top-Dressing Application Methods (6 Pages, 13 Blocks)
  8. Field Observation and Records (6 Pages, 12 Blocks)
  9. Importance and Resource Stewardship (6 Pages, 12 Blocks)
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

def build_topic4_curriculum():
    """Returns the comprehensive pedagogical page and block structure for Grade 10 Topic 4: Field Management Practices."""
    return [
        # =====================================================================
        # LESSON 1: Introduction to Field Management Practices
        # =====================================================================
        {
            "unit_order": 1,
            "unit_name": "Introduction to Field Management Practices",
            "unit_description": "Definition of post-planting field management, 6 key post-planting operations (gapping/thinning, weeding, pruning, top-dressing, staking/trellising, mulching), and agronomic yield potential.",
            "lesson_title": "Introduction to Post-Planting Field Management",
            "pages": [
                [
                    {
                        "type": "suggested_image",
                        "title": "Post-Planting Crop Field Management and Monitoring",
                        "content": {
                            "title": "Post-Planting Crop Field Management and Monitoring",
                            "caption": "Agricultural field managers conducting routine post-planting crop care, weeding, and vegetative growth audits in a commercial vegetable field."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Field Management Overview",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Define **field management practices** in commercial crop production.",
                                "Identify the six primary **post-planting agronomic operations** (**gapping, thinning, weeding, pruning, top-dressing, staking, mulching**).",
                                "Explain how post-planting management bridges the critical developmental gap between planting and harvesting.",
                                "Analyze the economic and yield penalties of neglecting field management."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "What is Field Management?",
                        "content": {
                            "title": "Nurturing the Growing Crop",
                            "text": "**Field management practices** encompass all the agronomic, biological, physical, and chemical operations carried out in a crop field from the moment seeds emerge or seedlings are transplanted until the final harvest is gathered.\n\n- While land preparation establishes the initial seedbed, field management protects and fuels the crop through its active vegetative, flowering, and fruit-filling stages.\n- Neglecting post-planting care is the leading cause of crop failure; unmanaged weeds, nutrient starvation, dense tangled foliage, and soil-borne diseases rapidly reduce genetic yield potential by 50% to 90%."
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "Six Primary Post-Planting Operations",
                        "content": {
                            "title": "The Core Agronomic Toolkit",
                            "text": "1. **Gapping & Thinning**: Sowing replacement seeds in failed spots (gapping) to maintain optimal plant population, and removing weak, overcrowded seedlings (thinning) to eliminate intra-crop competition.\n2. **Weeding**: Eradicating competitive wild vegetation mechanically, manually, or chemically to conserve moisture, fertilizer, and sunlight for the crop.\n3. **Pruning**: Systematically cutting away excess lateral shoots, old diseased foliage, or non-productive branches to maximize fruit size and improve air circulation.\n4. **Top-Dressing**: Applying fast-acting nitrogenous fertilizers (CAN, Urea, Liquid Manure) to the soil surface to power rapid leaf canopy expansion.\n5. **Staking & Trellising**: Installing wooden poles or suspended twine to support heavy, climbing, or fruit-laden plants off wet soil.\n6. **Mulching**: Spreading organic straw across soil to stop evaporation, suppress weed emergence, and regulate soil temperature."
                        }
                    },
                    {
                        "type": "definition_card",
                        "title": "Key Term: Yield Potential",
                        "content": {
                            "term": "Crop Yield Potential",
                            "definition": "The maximum theoretical genetic harvest a crop variety can produce when grown under ideal environmental conditions with zero biotic stress (weeds, pests) and non-limiting nutrient/water supplies.",
                            "example": "A hybrid maize variety with a genetic yield potential of 45 bags/acre that yields only 12 bags/acre due to severe weed competition and lack of top-dressing."
                        }
                    }
                ],
                [
                    {
                        "type": "suggested_diagram",
                        "title": "The 6 Pillars of Post-Planting Field Management",
                        "content": {
                            "title": "The 6 Pillars of Post-Planting Field Management",
                            "caption": "Integrated wheel diagram illustrating the 6 core field practices: Gapping/Thinning, Weeding, Pruning, Top-Dressing, Staking/Trellising, and Mulching encircling maximum harvest yield and market grade."
                        }
                    },
                    {
                        "type": "comparison_table",
                        "title": "Impact of Timely vs Neglected Field Management",
                        "content": {
                            "title": "Field Management Outcomes Matrix",
                            "headers": ["Field Operation", "Timely Professional Execution", "Neglected / Delayed Management"],
                            "rows": [
                                ["Weeding", "Crop receives 100% moisture and fertilizer; zero pest shelters", "Weeds choke crops; 40–70% yield loss; high pest infestation"],
                                ["Top-Dressing", "Vibrant dark green canopy; massive photosynthesis; rapid growth", "Yellowing chlorosis; stunted stems; small pale fruits"],
                                ["Pruning", "Large, Grade-1 uniform fruits; excellent airflow; low blight", "Dense tangled 'jungle'; tiny rotten fruits; high fungal rot"],
                                ["Staking", "Clean fruits elevated off wet soil; effortless spraying", "Fruits touch damp ground; soil splashing; high fruit rot"],
                                ["Gapping", "Uniform plant population across 100% of field area", "Empty field gaps; wasted land area; lower total tonnage"]
                            ]
                        }
                    }
                ],
                [
                    {
                        "type": "step_process",
                        "title": "Protocol: Planning a Post-Planting Field Schedule",
                        "content": {
                            "title": "Chronological Management Flowchart",
                            "steps": [
                                "1. **Days 7–14 (Gapping & Thinning)**: Inspect emergence; replant empty holes and thin crowded clusters.",
                                "2. **Weeks 2–3 (First Weeding & Top-Dressing)**: Remove early weed flushes; apply first top-dressing around established roots.",
                                "3. **Weeks 3–4 (Staking & Trellising)**: Install wooden stakes or string trellises before plants begin to lodge.",
                                "4. **Weeks 4–8 (Routine Pruning & Suckering)**: Pinch out weekly lateral suckers on tomatoes and clear lower capsicum stems.",
                                "5. **Weeks 6–10 (Second Top-Dressing & Disease Scouting)**: Apply booster fertilizer at flowering; conduct weekly diagnostic health audits."
                            ]
                        }
                    },
                    {
                        "type": "callout",
                        "title": "Agribusiness Principle: The Critical Period",
                        "content": {
                            "title": "The First 30 Days Dictate 80% of Yield",
                            "text": "Agronomic research proves that the **first 30 days after planting** represent the 'critical weed-free window'. If a crop is kept 100% weed-free and properly top-dressed during this formative window, its canopy closes and naturally shades out subsequent weed flushes!"
                        }
                    }
                ],
                [
                    {
                        "type": "mini_activity",
                        "title": "Diagnostic Field Audit: School Farm Health Survey",
                        "content": {
                            "title": "Conducting a Field Management Audit",
                            "task": "Take a diagnostic walk around the school farm or an adjacent community farm:\n\n1. Select two different crop plots (e.g. a well-managed vegetable plot vs an unweeded plot).\n2. Record observations in a 3-column table: *Crop Name*, *Observed Practices (Pruning, Weeding, Staking)*, and *Plant Health Condition (Green/Yellow, Upright/Lodged)*.\n3. Present a 3-minute oral diagnostic summary comparing crop vigor between the two plots.",
                            "materials": ["Audit Notebook", "Clip Board", "Pen"],
                            "safety": "Wear field boots and watch for prickly weeds or uneven ground."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Core Summary: Field Management Overview",
                        "content": {
                            "title": "Key Takeaways",
                            "text": "- **Field management** covers all crop care activities from emergence to harvest.\n- **The 6 core practices**: Gapping/Thinning, Weeding, Pruning, Top-Dressing, Staking, Mulching.\n- **Timely execution** allows crops to achieve their genetic yield potential.\n- **The first 30 days** represent the most critical window for weed and nutrient management."
                        }
                    }
                ],
                [
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Consequences of Neglected Field Care",
                        "content": {
                            "question": "A youth group invests in certified hybrid tomato seeds and drip irrigation on 1 acre of land. However, after planting, they do not weed, prune, or top-dress the crop for 6 weeks. What will be the primary biological and economic outcome?",
                            "options": [
                                "The tomato plants will automatically cross-pollinate into sweet potatoes",
                                "Aggressive weeds will outcompete the tomatoes for soil moisture and fertilizer, unpruned suckers will create a humid tangled bush that triggers fungal blight, and the resulting tiny, rotten fruits will cause massive financial loss",
                                "The tomato fruits will grow twice as large because of weed shade",
                                "The drip irrigation pipes will turn into solid fertilizer"
                            ],
                            "answer": "B",
                            "explanation": "High-quality hybrid seeds require disciplined post-planting management to express their yield potential. Without weeding, nutrients and water are stolen by wild plants. Without pruning and staking, lateral suckers form a dense, humid canopy on the damp ground that rapidly rots from fungal blights, leaving the farmer with tiny, diseased, unmarketable fruits and heavy financial losses."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 2: Pruning Capsicum
        # =====================================================================
        {
            "unit_order": 2,
            "unit_name": "Pruning Capsicum",
            "unit_description": "Definition of pruning, reasons for pruning capsicum (sweet pepper) in tropical conditions (humidity control, fungal suppression, fruit size), and the step-by-step Y-fork clearance procedure using sanitized secateurs.",
            "lesson_title": "Capsicum Pruning and Canopy Architecture",
            "pages": [
                [
                    {
                        "type": "suggested_image",
                        "title": "Capsicum (Sweet Pepper) Cultivation in Greenhouse",
                        "content": {
                            "title": "Capsicum (Sweet Pepper) Cultivation in Greenhouse",
                            "caption": "A healthy, well-pruned capsicum (sweet pepper) crop in a greenhouse showing clean upright stems below the primary Y-fork and vigorous fruit development."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Pruning Capsicum",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Define **pruning** in horticultural vegetable management.",
                                "Analyze the agronomic reasons for pruning **capsicum (sweet pepper)** under tropical conditions.",
                                "Identify the anatomical **Y-fork** on the main stem of a capsicum plant.",
                                "Execute the step-by-step procedure for **clearing side shoots below the Y-fork** using sanitized secateurs."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "What is Pruning?",
                        "content": {
                            "title": "The Art and Science of Plant Architecture",
                            "text": "**Pruning** is the selective, disciplined removal of specific plant parts—including lateral side shoots (suckers), non-productive branches, old yellowing leaves, diseased foliage, and excess flowers or fruits.\n\n- Pruning is never done randomly. It is a precise physiological intervention designed to redirect photosynthetic sugars into harvestable fruits, open the canopy to sunlight, improve air circulation, and suppress fungal diseases."
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "Why We Prune Capsicum (Sweet Pepper)",
                        "content": {
                            "title": "Managing Tropical Vegetative Growth",
                            "text": "Capsicum plants naturally develop a dense, bushy growth habit. In warm tropical climates, unmanaged bushes create three severe problems:\n\n1. **High Microclimate Humidity & Blight**: Dense foliage traps moisture around the base of the plant, creating an ideal breeding ground for **bacterial leaf spot, powdery mildew, and anthracnose fruit rot**.\n2. **Small, Low-Grade Fruits**: The plant divides its carbohydrates among dozens of tiny branches, producing numerous small, thin-walled peppers that fail commercial export standards.\n3. **Soil Pathogen Splashing**: Leaves touching the wet ground are easily infected by soil-borne fungal spores splashed during rain or irrigation.\n\n- *Pruning resolves these issues by opening the center of the plant to sunlight, elevating foliage off the ground, and directing energy into 2 to 4 robust main fruiting stems.*"
                        }
                    },
                    {
                        "type": "step_process",
                        "title": "Protocol: The Step-by-Step Capsicum Pruning Procedure",
                        "content": {
                            "title": "Horticultural Capsicum Pruning Workflow",
                            "steps": [
                                "1. **Sanitize Cutting Tools**: Dip secateur blades into a 10% bleach solution or methylated spirit to prevent transferring viral pathogens between plants.",
                                "2. **Locate the Primary 'Y-Fork'**: Trace the central main stem upwards from the ground to find the first major split where the stem divides into two branches (the 'Y-fork').",
                                "3. **Remove All Base Shoots and Leaves**: Cut away all lateral suckers and leaves growing on the main stem **below the primary Y-fork**, creating a clean 15–20 cm air clearance zone.",
                                "4. **Structure the Upper Canopy**: Above the Y-fork, select 2 to 4 vigorous, outward-growing structural branches; pinch off weak, inward-crossing shoots.",
                                "5. **Remove Crown Flower (Optional)**: Pinch off the single first 'crown flower' that forms inside the center of the Y-fork to allow the plant to build stronger vegetative frames before fruit set.",
                                "6. **Dispose of Prunings**: Collect pruned leaves in a bucket and compost them; never leave clippings lying on the soil around plant stems."
                            ]
                        }
                    }
                ],
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Capsicum Plant Pruning Architecture: Base Y-Fork Clearance",
                        "content": {
                            "title": "Capsicum Plant Pruning Architecture: Base Y-Fork Clearance",
                            "caption": "Botanical diagram highlighting the 15–20 cm clean base below the primary Y-fork (all lower suckers removed) and the 2–4 strong outward structural branches above the fork."
                        }
                    },
                    {
                        "type": "comparison_table",
                        "title": "Pruned vs Unpruned Capsicum Comparison",
                        "content": {
                            "title": "Capsicum Performance Comparison",
                            "headers": ["Agronomic Metric", "Pruned Capsicum Plant (Y-Fork Cleared)", "Unpruned Bushy Capsicum Plant"],
                            "rows": [
                                ["Canopy Microclimate", "Open, airy, fast-drying, high sunlight penetration", "Dense, shaded, humid; traps moisture and spores"],
                                ["Fungal Disease Rate", "Very Low (Leaves elevated off damp soil)", "High (Bacterial spot, anthracnose, powdery mildew)"],
                                ["Individual Fruit Size", "Large, thick-walled, blocky (Grade 1 Premium)", "Small, thin-walled, misshapen (Low market grade)"],
                                ["Spray & Harvest Ease", "Effortless pesticide coverage; easy picking", "Dense tangled leaves block sprays and hide fruits"],
                                ["Fruiting Longevity", "Prolonged harvest season (Continuous production)", "Early plant exhaustion; early dieback from disease"]
                            ]
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "Tool Hygiene and Secateur Maintenance",
                        "content": {
                            "title": "Preventing Viral and Bacterial Cross-Infection",
                            "text": "Capsicums are highly susceptible to systemic viruses like **Tobacco Mosaic Virus (TMV)** and **Potato Virus Y (PVY)**, which spread through infected plant sap on cutting tools:\n\n- Always use sharp, bypass **secateurs** rather than pangas or knives that crush stem bark.\n- Make clean, sloped cuts 5 mm away from the main stem.\n- Disinfect blades between plant rows to ensure complete biosecurity."
                        }
                    },
                    {
                        "type": "suggested_video",
                        "title": "Capsicum and Tomato Pruning Masterclass",
                        "content": {
                            "title": "Capsicum and Tomato Pruning Masterclass",
                            "description": "Close-up horticultural demonstration showing Y-fork identification, lower sucker removal on sweet peppers, and secateur tool sanitization.",
                            "url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
                        }
                    }
                ],
                [
                    {
                        "type": "mini_activity",
                        "title": "Field Practical: Pruning Capsicum Plants in the School Garden",
                        "content": {
                            "title": "Hands-On Capsicum Y-Fork Pruning",
                            "task": "In pairs under teacher supervision:\n\n1. Sanitize your secateurs in disinfectant solution.\n2. Approach a 4-week-old transplanted capsicum plant and locate the main stem Y-fork.\n3. Carefully snip off all lower side shoots and leaves below this junction.\n4. Inspect the cut surfaces to ensure clean, un-torn wounds.\n5. Transfer all pruned foliage into a clean wheelbarrow for composting.",
                            "materials": ["Bypass Secateurs", "Disinfectant Solution (Bleach / Spirit)", "Rags", "Wheelbarrow"],
                            "safety": "Keep fingers clear of cutting jaws. Wash hands after handling plant sap."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Core Summary: Capsicum Pruning",
                        "content": {
                            "title": "Key Takeaways",
                            "text": "- **Pruning capsicum** opens the canopy, suppresses fungal diseases, and maximizes fruit size.\n- **Clear all side shoots and leaves below the primary Y-fork** to establish a clean base.\n- **Retain 2 to 4 strong main branches** above the fork for heavy fruiting.\n- **Always sanitize secateurs** to prevent spreading plant viruses via sap."
                        }
                    }
                ],
                [
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Capsicum Y-Fork Pruning Rationale",
                        "content": {
                            "question": "Why is it mandatory for commercial greenhouse farmers to remove all lateral shoots and leaves below the first primary Y-fork on capsicum plants?",
                            "options": [
                                "It forces capsicum fruits to grow underground like potatoes",
                                "It creates a 15–20 cm clean air-clearance zone that prevents damp soil splash from transmitting fungal pathogens to leaves, while improving air circulation to lower humidity",
                                "It makes the capsicum fruit skin turn solid red within 24 hours",
                                "It completely stops the plant from absorbing any water"
                            ],
                            "answer": "B",
                            "explanation": "Lower leaves and side shoots close to the ground sit in a stagnant, humid microclimate and are easily splashed with wet soil during watering. Soil carries destructive fungal and bacterial pathogens (e.g. bacterial spot, damping off). Pruning all growth below the primary Y-fork creates a clean stem that prevents soil splash, maximizes ventilation, and directs sugars into upper fruiting branches."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 3: Single-Stem Pruning of Tomatoes
        # =====================================================================
        {
            "unit_order": 3,
            "unit_name": "Single-Stem Pruning of Tomatoes",
            "unit_description": "Tomato indeterminate branching habit, lateral suckers in leaf axils, single-stem removal mechanics, vertical staking/trellising, and greenhouse high-density economics vs labor and sunscald trade-offs.",
            "lesson_title": "Single-Stem Tomato Pruning and Vertical Training",
            "pages": [
                [
                    {
                        "type": "suggested_image",
                        "title": "High-Density Greenhouse Single-Stem Tomato Production",
                        "content": {
                            "title": "High-Density Greenhouse Single-Stem Tomato Production",
                            "caption": "Commercial greenhouse indeterminate tomato plants trained vertically on suspended twine using the single-stem pruning system."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Single-Stem Tomato Pruning",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Identify the botanical location of **lateral suckers in tomato leaf axils**.",
                                "Describe the **single-stem pruning and vertical trellising** system in indeterminate tomatoes.",
                                "Execute the manual **pinch-and-twist** suckering method safely.",
                                "Analyze the economic benefits (large fruit size, high-density yield) and management trade-offs (labor cost, sunscald risk)."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Tomato Growth Habit and the 'Lateral Sucker'",
                        "content": {
                            "title": "Understanding Tomato Branching Biology",
                            "text": "Tomato plants (*Solanum lycopersicum*) are highly vigorous, sprawling vines. At every **leaf axil**—the V-shaped angle where a leaf petiole joins the main stem—the plant initiates a fast-growing lateral branch called a **sucker**.\n\n- If left unmanaged, each sucker develops its own leaves, flower trusses, and sub-suckers, transforming the single plant into a dense, tangled, low-yielding bush.\n- In commercial greenhouse production, unpruned tomatoes collapse under their own weight, contact damp ground, and succumb to early blight."
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "What is Single-Stem Pruning?",
                        "content": {
                            "title": "Training the Central Leader",
                            "text": "In the **single-stem pruning system**, only the single, central main shoot of the tomato plant is allowed to grow vertically.\n\n- **Systematic Suckering**: The grower inspects the plant weekly and pinches off every single lateral sucker emerging from the leaf axils along the entire height of the plant.\n- **Vertical Staking & Trellising**: Because a single stem carries heavy fruit trusses (up to 15 kg of tomatoes), it cannot support itself. It is clipped to vertical polypropylene twine suspended from greenhouse overhead wires or tied to wooden stakes."
                        }
                    },
                    {
                        "type": "step_process",
                        "title": "Protocol: The Pinch-and-Twist Suckering Method",
                        "content": {
                            "title": "Manual Tomato Suckering Technique",
                            "steps": [
                                "1. **Target Young Suckers (5–10 cm long)**: Remove suckers when they are young and tender. Removing large, woody suckers leaves massive wounds that invite disease.",
                                "2. **Grip the Sucker Base**: Hold the base of the sucker firmly between your thumb and index finger.",
                                "3. **Pinch and Snap Sideways**: Bend the sucker sharply to one side until it snaps cleanly off the leaf axil. Do not pull downward, as this strips the green skin of the main stem.",
                                "4. **Prune in the Morning**: Perform suckering on warm, sunny mornings so that the small wound dries and calluses rapidly before night humidity sets in.",
                                "5. **Wind Stem Around String**: Gently wind the flexible growing tip around the vertical trellis twine clockwise."
                            ]
                        }
                    }
                ],
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Tomato Leaf Axil Anatomy: Sucker Identification & Pinching",
                        "content": {
                            "title": "Tomato Leaf Axil Anatomy: Sucker Identification & Pinching",
                            "caption": "Botanical diagram of a tomato stem illustrating the Main Stem, the Leaf Petiole, the emerging Lateral Sucker in the V-axil, and the clean pinch-and-twist removal technique."
                        }
                    },
                    {
                        "type": "comparison_table",
                        "title": "Advantages vs Disadvantages of Single-Stem Pruning",
                        "content": {
                            "title": "Single-Stem Pruning Trade-off Matrix",
                            "headers": ["Agronomic Parameter", "Advantages of Single-Stem", "Disadvantages / Management Risks"],
                            "rows": [
                                ["Individual Fruit Size", "Maximum size, heavy weight, uniform shape (Grade 1)", "Fewer total fruits per plant compared to multiple stems"],
                                ["Planting Density", "Allows high density (30–45 cm spacing; 25,000 plants/ha)", "Requires substantial initial investment in greenhouse trellising"],
                                ["Disease Management", "Superb airflow & light; rapid drying suppresses Early/Late Blight", "Sunscald risk: sparse canopy exposes fruits to hot midday sun"],
                                ["Spray Efficiency", "Pesticides and foliar feeds coat 100% of leaves uniformly", "High labor demand: requires weekly suckering and de-leafing"],
                                ["Harvesting Speed", "All fruit trusses clearly visible at eye level; fast picking", "Accidental snapping of main growing tip terminates plant growth"]
                            ]
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "Managing the Risk of Fruit Sunscald",
                        "content": {
                            "title": "Protecting Exposed Fruit Trusses",
                            "text": "Because single-stem pruning strips away excess foliage, developing green tomato fruits can be exposed to intense, direct solar radiation:\n\n- **Sunscald Symptoms**: White, bleached, leathery, sunken patches develop on the sun-facing side of the tomato skin, ruining market grade.\n- **Remedy**: In high-temperature open-field zones, growers maintain 30% shade netting or transition to a multiple-stem system to provide natural leaf canopy shading."
                        }
                    },
                    {
                        "type": "mini_activity",
                        "title": "Field Practical: Sucker Identification and Manual Pinching",
                        "content": {
                            "title": "Hands-On Tomato Suckering Lab",
                            "task": "In the school vegetable garden or greenhouse:\n\n1. Locate a growing indeterminate tomato plant.\n2. Identify the main stem, three leaf petioles, and the lateral suckers emerging from the leaf axils.\n3. Practice the pinch-and-twist method on three suckers (<5 cm long).\n4. Inspect the wounds to confirm zero bark tearing.\n5. Tie the main stem loosely to its support stake using a figure-8 knot.",
                            "materials": ["Growing Tomato Plants", "Support Stakes / Twine", "Sisal String"],
                            "safety": "Handle tomato vines gently to avoid snapping the main growing tip."
                        }
                    }
                ],
                [
                    {
                        "type": "key_takeaway",
                        "title": "Core Summary: Single-Stem Tomato Pruning",
                        "content": {
                            "title": "Key Takeaways",
                            "text": "- **Lateral suckers** emerge in the V-shaped leaf axils between leaf petioles and the main stem.\n- **Single-stem pruning** removes 100% of suckers, training one central vertical leader.\n- **Maximizes fruit size and greenhouse planting density** (Grade 1 premium quality).\n- **Use the pinch-and-twist method** on sunny mornings to ensure rapid wound healing."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Anatomical Location of Tomato Suckers",
                        "content": {
                            "question": "Where on a tomato plant does a lateral sucker originate, and how should a farm worker remove it cleanly without damaging the main stem?",
                            "options": [
                                "From the underground root tip; dig it out with a hand spade",
                                "In the V-shaped leaf axil between the leaf petiole and the main stem; pinch the base between thumb and forefinger and snap sideways using the pinch-and-twist method",
                                "From the center of a red ripe fruit; cut it out with a kitchen knife",
                                "From the edge of the flower petals; pull it downward vigorously"
                            ],
                            "answer": "B",
                            "explanation": "Lateral suckers develop exclusively within the leaf axils (the V-shaped junction where leaf petioles meet the main stem). The correct removal method is to pinch the tender sucker base and snap it sideways (pinch-and-twist). Pulling downward must be avoided, as it tears the outer epidermal bark of the main stem, creating an open wound for bacterial and fungal infection."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 4: Multiple-Stem Pruning of Tomatoes
        # =====================================================================
        {
            "unit_order": 4,
            "unit_name": "Multiple-Stem Pruning of Tomatoes",
            "unit_description": "Two/three stem configuration, selecting the vigorous sucker below the first flower cluster, open-field solar protection (sunscald defense), and comparison against single-stem systems.",
            "lesson_title": "Multiple-Stem Tomato Pruning and Open-Field Management",
            "pages": [
                [
                    {
                        "type": "suggested_image",
                        "title": "Open-Field Tomato Production with Staked Multiple Stems",
                        "content": {
                            "title": "Open-Field Tomato Production with Staked Multiple Stems",
                            "caption": "Open-field tomato cultivation using the multiple-stem pruning system, showing heavy fruit clusters protected by a dense, healthy leaf canopy."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Multiple-Stem Tomato Pruning",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Describe the **multiple-stem (two-stem or three-stem)** pruning system in tomato production.",
                                "Identify and select the strong sucker **immediately below the first flower cluster** to form the second stem.",
                                "Explain how multiple-stem canopy cover protects fruit clusters from **solar sunscald** in open fields.",
                                "Compare single-stem and multiple-stem systems across yield, fruit size, spacing, and labor."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "What is Multiple-Stem Pruning?",
                        "content": {
                            "title": "Balancing Fruit Count and Canopy Shading",
                            "text": "The **multiple-stem pruning system** is a growth-regulation strategy where the grower retains the main central stem plus **one or two carefully selected lateral suckers**, allowing them to grow into full-sized, productive main branches while pinching off all other suckers.\n\n- It is the standard system for **open-field tomato cultivation** across Kenya, where intense tropical sunshine requires adequate leaf canopy to shield fruits from sunburn, and where staking materials are limited."
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "Selecting and Establishing the Secondary Stem",
                        "content": {
                            "title": "The First Flower Cluster Rule",
                            "text": "Not all suckers are equal. To establish a balanced, highly productive two-stem plant, the farmer follows a strict botanical rule:\n\n1. **Locate the First Flower Truss**: Observe the main stem until the first cluster of yellow flowers appears.\n2. **Identify the Sub-Floral Sucker**: Locate the strong, thick lateral sucker emerging in the leaf axil **immediately below this first flower cluster**.\n3. **Why this Sucker?**: Biologically, this specific sucker receives maximum vascular sap flow and hormonal vigor from the plant crown. It develops rapidly into a strong, vertical leader that matches the main stem in thickness and fruit yield.\n4. **Remove All Other Suckers**: Pinch off all lower suckers near the ground and all subsequent suckers along both stems.\n5. **Support Both Stems**: Tie both stems to separate wooden stakes (V-shaped staking) or dual strings."
                        }
                    },
                    {
                        "type": "comparison_table",
                        "title": "Single-Stem vs Multiple-Stem Tomato Systems",
                        "content": {
                            "title": "Comprehensive Tomato Pruning Comparison",
                            "headers": ["Agronomic Feature", "Single-Stem System", "Multiple-Stem System (Two Stems)"],
                            "rows": [
                                ["Optimal Environment", "Commercial Greenhouses & High Tunnels", "Open-Field Commercial Production"],
                                ["Plant Spacing", "Narrow (30–45 cm apart; 25,000 plants/ha)", "Wide (60–75 cm apart; 15,000 plants/ha)"],
                                ["Fruit Size per Tomato", "Maximum / Extra Large (Supermarket Grade 1)", "Medium to Large (Standard Market Grade)"],
                                ["Total Fruits per Plant", "Lower fruit count (Focused on size)", "Significantly higher total fruit count per plant"],
                                ["Canopy Shading & Sunscald", "Sparse foliage; High sunscald risk", "Dense leaf canopy; Complete fruit shading"],
                                ["Labor & Trellising", "Intensive weekly suckering; single high string", "Moderate suckering; requires dual stakes / V-trellis"]
                            ]
                        }
                    }
                ],
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Single-Stem vs Multiple-Stem Tomato Pruning Architecture",
                        "content": {
                            "title": "Single-Stem vs Multiple-Stem Tomato Pruning Architecture",
                            "caption": "Comparative anatomical diagram showing a Single-Stem tomato plant (all axils cleared, single vertical stake) alongside a Two-Stem plant (secondary leader established below first flower cluster, supported by V-stakes)."
                        }
                    },
                    {
                        "type": "step_process",
                        "title": "Protocol: Training a Two-Stem Open-Field Tomato Plant",
                        "content": {
                            "title": "Step-by-Step Two-Stem Establishment",
                            "steps": [
                                "1. **Plant at 60 cm Spacing**: Transplant seedlings into open-field rows spaced 60 cm apart.",
                                "2. **Clear Lower Base**: Pinch off the first 2–3 suckers near the soil line to keep the bottom 15 cm clean.",
                                "3. **Tag the Flower Sub-Sucker**: When the first flower cluster appears, allow the sucker immediately below it to grow unchecked.",
                                "4. **Install Dual Stakes**: Drive two 1.8-meter wooden stakes in a V-shape on either side of the plant base.",
                                "5. **Tie Stems Continuously**: Tie the main stem to Stake A and the secondary stem to Stake B using soft sisal twine.",
                                "6. **Maintain Weekly Suckering**: Remove any new sub-suckers emerging along both stems."
                            ]
                        }
                    }
                ],
                [
                    {
                        "type": "mini_activity",
                        "title": "Field Practical: Establishing a Two-Stem Demonstration Tomato Plant",
                        "content": {
                            "title": "Selecting and Training the Secondary Leader",
                            "task": "In the school tomato plot:\n\n1. Identify three tomato plants that have developed their first flower cluster.\n2. Locate and tag the strong sucker immediately below the flower truss using a piece of colored yarn.\n3. Pinch off all other lateral suckers on the plant.\n4. Drive two wooden stakes into the ground at a 20° outward angle and tie the two stems securely.",
                            "materials": ["Tomato Plants with First Flowers", "Colored Yarn / Tags", "Wooden Stakes", "Sisal Twine"],
                            "safety": "Drive stakes into soil carefully without striking fingers."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Core Summary: Multiple-Stem Pruning",
                        "content": {
                            "title": "Key Takeaways",
                            "text": "- **Multiple-stem systems** allow the main stem plus 1–2 selected suckers to develop.\n- **Always select the sucker immediately below the first flower cluster** for maximum vigor.\n- **Ideal for open-field farming**, providing dense leaf canopy that prevents fruit sunscald.\n- **Requires wider spacing (60–75 cm)** and produces higher total fruit counts per plant."
                        }
                    }
                ],
                [
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Selecting the Optimal Sucker",
                        "content": {
                            "question": "When training an open-field tomato plant to a two-stem system, which specific lateral sucker must the farmer preserve and cultivate as the secondary leader?",
                            "options": [
                                "The very first tiny sucker at the soil surface",
                                "The robust lateral sucker located immediately below the first flower cluster on the main stem",
                                "The youngest sucker emerging at the top of the shoot tip",
                                "Any sucker that has yellow, wilted leaves"
                            ],
                            "answer": "B",
                            "explanation": "The lateral sucker emerging directly beneath the first flower cluster is biologically the most vigorous sucker on the tomato vine. It receives high vascular nutrient flow, grows at an equal rate to the main leader, balances the physical weight of the plant, and rapidly produces productive flower trusses."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 5: Pruning Perennial Crops
        # =====================================================================
        {
            "unit_order": 5,
            "unit_name": "Pruning Perennial Crops",
            "unit_description": "Growth regulation of woody perennials (coffee, tea, fruit trees), single-stem system (capped at 1.5–1.8 m) vs multiple-stem systems, and cutting back (rejuvenation pruning at 15–30 cm) to stimulate fresh root-crown suckers.",
            "lesson_title": "Pruning Perennial Crops and Rejuvenation Systems",
            "pages": [
                [
                    {
                        "type": "suggested_image",
                        "title": "Perennial Tea and Coffee Plantation Pruning",
                        "content": {
                            "title": "Perennial Tea and Coffee Plantation Pruning",
                            "caption": "A well-managed smallholder perennial plantation in Kenya showing pruned, capped bushes maintaining an accessible horizontal plucking table."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Perennial Crop Pruning",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Explain the long-term agronomic purpose of pruning **perennial crops (coffee, tea, fruit trees)**.",
                                "Compare the **single-stem (capped trunk)** and **multiple-stem** training configurations in coffee.",
                                "Define **'cutting back' (rejuvenation pruning)** and explain how it stimulates new productive cycles from the root crown.",
                                "Execute angled pruning cuts using pruning saws and secateurs to shed rainwater."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Why Prune Perennial Crops?",
                        "content": {
                            "title": "Managing Decades of Tree Productivity",
                            "text": "Unlike short-season annual vegetables, perennial crops (coffee, tea, citrus, avocado, macadamia) remain productive in the field for 20 to 50+ years.\n\n- **Long-Term Objectives of Perennial Pruning**:\n  1. **Control Tree Height**: Keep canopies at an accessible height ($1.5\\text{--}1.8\\text{ m}$) for easy manual harvesting and chemical spraying without ladders.\n  2. **Remove Unproductive Wood**: Eliminate old, woody, dead, or diseased branches that consume sap without producing flowers.\n  3. **Stimulate Biennial Bearing Balance**: Prevent trees from over-bearing one year and crashing into exhaustion the next season.\n  4. **Open Canopy to Solar Light**: Ensure sunlight penetrates to the interior branches to initiate flower buds."
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "Single-Stem vs Multiple-Stem Perennial Systems",
                        "content": {
                            "title": "Training Coffee and Fruit Trees",
                            "text": "### 1. Single-Stem System (Capped Central Trunk)\n- The tree is trained to grow on a single central trunk, which is **capped (topped) at a height of 1.5 m to 1.8 m** by cutting off the apical growing point.\n- **Effect**: Capping breaks apical dominance, forcing the tree to develop strong, horizontal lateral branches at waist height.\n- **Advantages**: Compact, sturdy bush; highly resistant to wind damage; makes weeding, spraying, and manual berry picking effortless.\n\n### 2. Multiple-Stem System (Cyclic Suckers)\n- The young tree is cut back near the ground early to stimulate 2 to 4 upright vertical stems.\n- **Advantages**: Produces higher initial crop yields; enables cyclic regeneration where old stems are cut back in rotation every 4–6 years to maintain perpetual young wood."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "What is 'Cutting Back' (Rejuvenation Pruning)?",
                        "content": {
                            "title": "Regenerating Old, Exhausted Plantations",
                            "text": "Over 10 to 15 years, coffee bushes become tall, woody, and severely unproductive ('senescent'). Their old branches produce very few berries.\n\n- **The Cutting Back Operation**: Using a sharp pruning saw, the farmer saws off the entire old trunk **15 cm to 30 cm above ground level at a 45° downward angle**.\n- **The Biological Response**: The extensive, established root system remains healthy underground. Driven by immense root pressure, the cut stump produces dozens of vigorous, fresh vegetative suckers.\n- **Selection**: The farmer selects the 2–3 strongest upright suckers to form new trunks and removes the rest. Within 18 months, the bush is fully rejuvenated and producing peak yields without the huge cost of uprooting and replanting!"
                        }
                    }
                ],
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Perennial Crop Pruning: Capping vs Multiple-Stem vs Cutting Back",
                        "content": {
                            "title": "Perennial Crop Pruning: Capping vs Multiple-Stem vs Cutting Back",
                            "caption": "Stratigraphic tree architecture diagram comparing Capped Single-Stem (1.5 m topped trunk), Multiple-Stem (3 vertical leaders), and Cutting Back (old stump cut at 20 cm regenerating fresh suckers)."
                        }
                    },
                    {
                        "type": "comparison_table",
                        "title": "Perennial Pruning Configurations Comparison",
                        "content": {
                            "title": "Perennial Systems Matrix",
                            "headers": ["System", "Pruning Method", "Key Advantages", "Primary Management Challenge"],
                            "rows": [
                                ["Single-Stem (Capped)", "Main trunk topped at 1.5–1.8 m; lateral branching", "Compact canopy; easy ground harvesting; wind resistant", "Requires constant desuckering to maintain single trunk"],
                                ["Multiple-Stem", "2–4 vertical stems trained from base", "Higher early yields; easy cyclic branch replacement", "Canopy grows tall over years; requires ladder harvesting"],
                                ["Cutting Back (Rejuvenation)", "Entire bush sawed off at 15–30 cm above ground", "Completely regenerates old trees without replanting cost", "Zero harvest yield for 12–18 months during sucker regrowth"]
                            ]
                        }
                    }
                ],
                [
                    {
                        "type": "step_process",
                        "title": "Protocol: Making Clean Angled Pruning Cuts",
                        "content": {
                            "title": "Surgical Standards for Woody Pruning",
                            "steps": [
                                "1. **Use Sharp Pruning Saws & Loppers**: Never use dull pangas that hack and split hardwood stems.",
                                "2. **Cut at a 45° Downward Angle**: Angle the cut away from the bud so rainwater slides off instantly.",
                                "3. **Avoid Horizontal Flat Cuts**: Flat horizontal cuts allow rainwater to pool on the wound, creating a breeding ground for wood-rotting fungi.",
                                "4. **Apply Tree Wound Paste / Copper Fungicide**: Paint large saw wounds (>2 cm diameter) with wound sealant or copper paste to block fungal spore entry.",
                                "5. **Clear Old Clippings**: Remove all dead, diseased wood from the plantation floor and compost or burn infected branches."
                            ]
                        }
                    },
                    {
                        "type": "mini_activity",
                        "title": "Field Practical: Auditing Coffee / Fruit Tree Architecture",
                        "content": {
                            "title": "Observing Perennial Tree Pruning Systems",
                            "task": "Visit a school coffee plot, tea hedge, or fruit orchard:\n\n1. Inspect 5 trees. Determine whether they are trained as single-stem (capped trunk) or multiple-stem.\n2. Look for evidence of 'cutting back' (thick base stumps with young vertical suckers).\n3. Inspect existing pruning cuts to see if they were made at a 45° downward angle.\n4. Record findings and sketch the branching architecture in your notebook.",
                            "materials": ["Field Notebook", "Measuring Tape", "Camera / Sketchpad"],
                            "safety": "Watch for low overhanging branches."
                        }
                    }
                ],
                [
                    {
                        "type": "key_takeaway",
                        "title": "Core Summary: Perennial Pruning",
                        "content": {
                            "title": "Key Takeaways",
                            "text": "- **Perennial pruning** controls tree height (1.5–1.8 m), removes old wood, and regulates yields.\n- **Single-stem capping** forces horizontal branching for effortless ground harvesting.\n- **Multiple-stem systems** allow cyclic stem replacement every 4–6 years.\n- **Cutting back (at 15–30 cm)** completely regenerates old, senescent trees using existing roots.\n- **Always make cuts at a 45° downward angle** to shed rainwater and prevent fungal wood rot."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Rejuvenation Pruning Rationale",
                        "content": {
                            "question": "A farmer inherits a 15-year-old coffee farm where the bushes are 4 meters tall, woody, and producing virtually zero berries. Why is 'cutting back' (rejuvenation pruning) the most cost-effective and agronomically sound solution?",
                            "options": [
                                "Cutting back turns the coffee trees into shade trees",
                                "Sawing the old trunks down to 15–30 cm above ground utilizes the massive, healthy existing root system to push out vigorous new suckers, fully restoring peak coffee production within 18 months at zero replanting cost",
                                "Cutting back kills the coffee roots and fertilizes the soil with dead wood",
                                "Cutting back makes the berries grow on the leaves instead of stems"
                            ],
                            "answer": "B",
                            "explanation": "Uprooting an old plantation and buying new seedlings requires immense capital and takes 4–5 years to bear fruit. In contrast, 'cutting back' senescent coffee bushes 15–30 cm above ground preserves the mature, deep root network. The root pressure forces a flush of vigorous, juvenile suckers that mature into high-yielding trunks within 18 months, regenerating the plantation at negligible cost."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 6: Top-Dressing Materials and Timing
        # =====================================================================
        {
            "unit_order": 6,
            "unit_name": "Top-Dressing Materials and Timing",
            "unit_description": "Role of nitrogen in chlorophyll synthesis and vegetative growth, inorganic fertilizers (CAN, Urea, Ammonium Sulphate) vs organic options (liquid manure, poultry manure), and critical application timing windows (knee-high maize V6 stage, 2-3 weeks post-transplanting for vegetables).",
            "lesson_title": "Top-Dressing Fertilizer Chemistry and Application Timing",
            "pages": [
                [
                    {
                        "type": "suggested_image",
                        "title": "Knee-High Maize Field at Optimal Top-Dressing Window",
                        "content": {
                            "title": "Knee-High Maize Field at Optimal Top-Dressing Window",
                            "caption": "A commercial maize field at the critical knee-high (V6) vegetative growth stage, exhibiting high biological demand for fast-acting nitrogen top-dressing."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Top-Dressing Materials & Timing",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Define **top-dressing** as the application of fast-acting fertilizers to growing crops.",
                                "Analyze the physiological role of **Nitrogen ($N$)** in chlorophyll synthesis and leaf canopy expansion.",
                                "Compare inorganic top-dressing fertilizers (**CAN, Urea, Ammonium Sulphate**) against organic feeds (**liquid manure**).",
                                "Identify critical application timing: **knee-high stage (V6)** for cereals and **2–3 weeks post-transplanting** for vegetables."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "What is Top-Dressing?",
                        "content": {
                            "title": "Feeding the Active Vegetative Engine",
                            "text": "**Top-dressing** is the application of fast-acting, highly soluble fertilizers to the soil surface around growing crops during their active vegetative and early reproductive growth stages.\n\n- While planting fertilizers (such as DAP, SSP, or basal compost) supply phosphorus ($P$) for early root development in the planting hole, top-dressing supplies fast-release nitrogen ($N$) to power rapid leaf development and stem elongation."
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "The Biochemical Role of Nitrogen (N)",
                        "content": {
                            "title": "The Powerhouse of Plant Photosynthesis",
                            "text": "Nitrogen is the fundamental building block of life in plants:\n\n1. **Chlorophyll Molecule**: Nitrogen is the central constituent of the chlorophyll molecule ($C_{55}H_{72}O_5N_4Mg$), which captures sunlight to manufacture sugars during photosynthesis.\n2. **Proteins & Enzymes**: Synthesizes amino acids and metabolic enzymes required for rapid cellular division in growing shoots.\n3. **Canopy Expansion**: Drives the formation of large, deep green leaves, maximizing the light-intercepting surface area of the crop."
                        }
                    },
                    {
                        "type": "comparison_table",
                        "title": "Top-Dressing Fertilizer Options Comparison",
                        "content": {
                            "title": "Top-Dressing Fertilizer Characteristics",
                            "headers": ["Fertilizer Name", "Nutrient Content", "Soil Acidity Effect", "Agronomic Advantages & Precautions"],
                            "rows": [
                                ["Calcium Ammonium Nitrate (CAN)", "21% – 26% N + 10% Calcium", "Neutral (Does not acidify soil)", "Safest, most popular top-dress; calcium strengthens cell walls; ideal for acidic soils"],
                                ["Urea", "46% Nitrogen (Highly concentrated)", "Slightly acidifying", "Cheapest cost per unit N; must be incorporated into moist soil to avoid volatilization"],
                                ["Ammonium Sulphate", "21% N + 24% Sulphur", "Strongly acidifying", "Provides essential sulfur; recommended only for alkaline/calcareous soils"],
                                ["Liquid Manure / Compost Tea", "1% – 3% N + Micronutrients + Microbes", "Neutral / Soil buffering", "100% organic, zero financial cost; enhances soil biological food web"]
                            ]
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "Precise Application Timing Windows",
                        "content": {
                            "title": "Aligning Fertilizer Delivery with Plant Uptake Curves",
                            "text": "Applying top-dressing too early or too late wastes expensive inputs. Fertilizer must be applied during rapid growth transitions:\n\n### 1. Cereal Crops (Maize, Sorghum, Wheat)\n- **The Knee-High Stage (V6 Leaf Stage, 3–4 Weeks After Emergence)**: The plant initiates exponential stem elongation and floral ear differentiation. Nitrogen uptake spikes from $0.5\\text{ kg/ha/day}$ to over $4.0\\text{ kg/ha/day}$!\n- *Second Booster*: A second light top-dressing can be applied just prior to tasseling.\n\n### 2. Horticultural Vegetables (Capsicum, Tomato, Cabbage, Kales)\n- **First Top-Dressing (2–3 Weeks After Transplanting)**: Once seedlings recover from transplanting shock and establish root contact.\n- **Second Top-Dressing (Onset of Flowering / Fruit Set)**: Powers flower retention and fruit expansion."
                        }
                    },
                    {
                        "type": "step_process",
                        "title": "Protocol: Brewing Organic Liquid Manure",
                        "content": {
                            "title": "On-Farm Liquid Fertilizer Production",
                            "steps": [
                                "1. **Fill Drum with Water**: Add 50 liters of clean fresh water to a plastic drum.",
                                "2. **Fill Gunny Sack with Manure**: Place 10 kg of fresh, high-nitrogen poultry or cattle manure inside a porous burlap sack.",
                                "3. **Suspend Sack**: Tie the sack to a wooden crossbar and submerge it like a giant tea bag inside the drum.",
                                "4. **Ferment for 14 Days**: Cover the drum and stir daily to aerate the solution.",
                                "5. **Dilute and Apply**: Dilute the dark brown liquid 1:10 with clean water and pour around vegetable root zones."
                            ]
                        }
                    }
                ],
                [
                    {
                        "type": "mini_activity",
                        "title": "Field Investigation: Maize Nitrogen Growth Trial",
                        "content": {
                            "title": "Demonstrating the Impact of Knee-High CAN Application",
                            "task": "On the school agriculture plot, mark two adjacent rows of knee-high maize:\n\n1. Row A: Top-dress with 10g CAN per plant using the ring method and water.\n2. Row B (Control): Zero top-dressing applied.\n3. Measure plant height, stalk diameter, and leaf greenness (using a color chart) weekly for 3 weeks.\n4. Present a bar graph comparing vegetative growth rates.",
                            "materials": ["Knee-High Maize Plot", "CAN Fertilizer", "Weighing Scale", "Measuring Tape", "Color Chart"],
                            "safety": "Wash hands with soap and water after handling synthetic fertilizer granules."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Core Summary: Top-Dressing Materials & Timing",
                        "content": {
                            "title": "Key Takeaways",
                            "text": "- **Top-dressing** delivers fast-acting nitrogen ($N$) during active vegetative growth.\n- **CAN (21–26% N)** is the preferred neutral fertilizer for acid-sensitive Kenyan soils.\n- **Urea (46% N)** is highly concentrated but must be buried to stop ammonia gas loss.\n- **Top-dress maize at knee-high (V6 stage)** and vegetables **2–3 weeks post-transplanting**."
                        }
                    }
                ],
                [
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Selecting Non-Acidifying Fertilizers",
                        "content": {
                            "question": "A farmer in Western Kenya with acidic soil (pH 4.8) needs to top-dress a commercial maize crop. Why is Calcium Ammonium Nitrate (CAN) agronomically superior to Ammonium Sulphate for this farm?",
                            "options": [
                                "CAN turns maize cobs into pure gold",
                                "CAN contains calcium carbonate, which neutralizes acidity and maintains soil pH, whereas Ammonium Sulphate releases strong sulfuric acid that would further acidify the soil and trigger severe aluminum toxicity",
                                "Ammonium Sulphate is only used to feed livestock",
                                "CAN repels all caterpillars automatically"
                            ],
                            "answer": "B",
                            "explanation": "Calcium Ammonium Nitrate (CAN) is chemically buffered with calcium carbonate, giving it a near-neutral effect on soil pH. Ammonium Sulphate is a strongly acidifying fertilizer that generates excess hydrogen ($H^+$) and sulfate ions. Applying Ammonium Sulphate on an already acidic soil (pH 4.8) will drive the pH below 4.5, triggering lethal aluminum toxicity and severe phosphorus lockup."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 7: Top-Dressing Application Methods
        # =====================================================================
        {
            "unit_order": 7,
            "unit_name": "Top-Dressing Application Methods",
            "unit_description": "Application techniques: broadcasting vs banding vs ring application at drip line vs foliar sprays; preventing chemical stem fertilizer burn; covering with soil to prevent ammonia volatilization; environmental eutrophication.",
            "lesson_title": "Top-Dressing Application Methods and Environmental Safety",
            "pages": [
                [
                    {
                        "type": "suggested_image",
                        "title": "Top-Dressing Fertilizer Application in Vegetable Rows",
                        "content": {
                            "title": "Top-Dressing Fertilizer Application in Vegetable Rows",
                            "caption": "A farm worker applying pre-measured fertilizer granules in precision rings around vegetable crops at the outer leaf drip line."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Top-Dressing Application Methods",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Compare top-dressing methods: **broadcasting, banding, ring application**, and **foliar spraying**.",
                                "Execute the step-by-step **ring application protocol at the crop drip line** for spaced vegetables.",
                                "Explain the biological mechanism of **chemical fertilizer burn** when granules contact stems.",
                                "Analyze the environmental threat of **eutrophication (algae blooms and fish suffocation)** from fertilizer runoff."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Top-Dressing Application Methods",
                        "content": {
                            "title": "Matching Application Method to Crop Spacing",
                            "text": "1. **Broadcasting**: Uniformly scattering fertilizer granules across the entire field surface. Suitable only for dense, close-spaced crops like pasture grasses, wheat, or barley. *Highly wasteful for spaced row crops*.\n2. **Banding (Row Placement)**: Placing a continuous narrow line of fertilizer in a shallow 5 cm furrow along the crop row, 10 cm away from stems. Standard for row cereals like maize and sorghum.\n3. **Ring Application**: Digging a circular trench around individual plants at the outer drip line, depositing fertilizer, and covering with soil. The gold standard for widely spaced horticultural crops (capsicum, tomatoes, cabbages, fruit trees).\n4. **Foliar Spraying**: Dissolving specialized soluble fertilizers (e.g. high-N foliar feed) in water and misting onto leaves for immediate stomatal absorption."
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "The Ring Application Protocol at the Drip Line",
                        "content": {
                            "title": "Precision Feeding at the Active Root Zone",
                            "text": "For spaced vegetables like capsicum and tomatoes, **Ring Application** maximizes nutrient uptake while preventing chemical damage:\n\n### 1. Identifying the 'Drip Line'\n- The drip line is the imaginary circular perimeter directly below the outermost tips of the plant's leaves.\n- This is where the plant's active, fine **feeder roots and root hairs** are concentrated in the soil.\n\n### 2. The Step-by-Step Procedure\n- **Dig the Ring**: Using a hand trowel or stick, scratch a shallow circular trench (2–5 cm deep) around the plant exactly at the drip line (typically 8–15 cm from the stem).\n- **Deposit Fertilizer**: Sprinkle the measured dose (e.g. 10g CAN or 1 handful of chicken manure) evenly into the trench.\n- **Cover with Soil**: Seal the trench immediately with loose soil to prevent nitrogen volatilization into the atmosphere.\n- **Water Immediately**: Irrigate the bed to dissolve the fertilizer and carry nutrient ions directly to the root hairs."
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Fertilizer Ring Application Diagram at Crop Drip Line",
                        "content": {
                            "title": "Fertilizer Ring Application Diagram at Crop Drip Line",
                            "caption": "Overhead schematic showing the central plant stem, the 10 cm safety zone, the outer leaf drip line, the circular 3 cm trench, and the covered fertilizer granules."
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "The Biological Hazard of Chemical 'Fertilizer Burn'",
                        "content": {
                            "title": "Why Fertilizer Must Never Touch the Stem",
                            "text": "Inorganic fertilizers (CAN, Urea, NPK) are concentrated mineral salts. If placed directly against tender plant stems:\n\n- **Osmotic Desiccation**: The high salt concentration outside the stem creates a severe osmotic gradient. Water is pulled *out* of the plant stem cells into the fertilizer granule.\n- **Stem Girdling**: The stem tissues shrivel, turn brown, and die (chemical scorching). The vascular xylem and phloem collapse, killing the entire plant within 48 hours!"
                        }
                    },
                    {
                        "type": "comparison_table",
                        "title": "Top-Dressing Methods Comparison Matrix",
                        "content": {
                            "title": "Application Methods Matrix",
                            "headers": ["Method", "Target Crop Spacing", "Nutrient Efficiency", "Risk of Fertilizer Burn / Runoff"],
                            "rows": [
                                ["Ring Application", "Wide-spaced crops (Tomatoes, Capsicum, Citrus)", "Highest (Direct delivery to feeder roots)", "Zero risk if placed at drip line and covered"],
                                ["Banding (Row)", "Row crops (Maize, Beans, Cotton, Sugarcane)", "High (Concentrated along active root zone)", "Low if placed 10 cm away from plant line"],
                                ["Broadcasting", "Dense pasture grasses, Wheat, Barley", "Low for row crops (Feeds weeds; high leaching)", "High risk of leaf burn if applied to wet leaves"],
                                ["Foliar Spraying", "Horticultural vegetables during rapid growth", "Fastest uptake (Direct stomatal absorption)", "Low risk if diluted to correct concentration"]
                            ]
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "Environmental Threat: Eutrophication from Fertilizer Runoff",
                        "content": {
                            "title": "Protecting Local Water Ecosystems",
                            "text": "When farmers apply excessive fertilizer or leave granules unburied on bare soil, heavy rainfall washes the soluble nitrogen into nearby streams, rivers, and lakes:\n\n1. **Algal Bloom**: The influx of nitrogen stimulates a massive population explosion of aquatic green algae and water hyacinth across the water surface.\n2. **Sunlight Blockade**: The dense algae mat blocks sunlight from reaching underwater aquatic plants, causing them to die.\n3. **Decomposition & Oxygen Depletion**: Aerobic bacteria decompose the dead algae, consuming virtually all dissolved oxygen ($O_2$) in the water.\n4. **Fish Suffocation (Dead Zones)**: Fish, crabs, and aquatic organisms suffocate and die en masse, creating foul-smelling dead water bodies that ruin community drinking water supplies."
                        }
                    },
                    {
                        "type": "step_process",
                        "title": "Protocol: Best Management Practices for Fertilizer Safety",
                        "content": {
                            "title": "4 Rules for Responsible Fertilizer Stewardship",
                            "steps": [
                                "1. **Always Apply at the Drip Line**: Keep fertilizer 8–15 cm away from main stems to prevent osmotic burning.",
                                "2. **Cover with Soil Immediately**: Burying granules stops ammonia gas volatilization and cuts storm runoff.",
                                "3. **Never Apply Before Heavy Downpours**: Check weather forecasts; applying fertilizer before severe storms causes 100% runoff into rivers.",
                                "4. **Maintain Grass Buffer Strips**: Plant 3-meter wide Vetiver or Napier grass filter strips along riverbanks to trap any escaping fertilizer."
                            ]
                        }
                    },
                    {
                        "type": "suggested_video",
                        "title": "Correct Top-Dressing and Fertilizer Ring Application",
                        "content": {
                            "title": "Correct Top-Dressing and Fertilizer Ring Application",
                            "description": "Step-by-step practical demonstration showing accurate drip-line ring trenching, CAN application dosing, soil covering, and immediate irrigation.",
                            "url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
                        }
                    }
                ],
                [
                    {
                        "type": "mini_activity",
                        "title": "Field Practical: Practicing Precision Ring Application",
                        "content": {
                            "title": "Applying CAN to School Capsicum Plants",
                            "task": "In the school vegetable garden:\n\n1. Select 5 growing capsicum plants.\n2. Identify the outermost leaf tips (the drip line).\n3. Dig a neat 3 cm deep circular trench around each plant at this perimeter.\n4. Apply 10g of CAN fertilizer into the trench, cover with soil, and irrigate immediately.\n5. Confirm that zero fertilizer granules are touching the stems.",
                            "materials": ["5 Capsicum Plants", "CAN Fertilizer", "10g Measuring Spoon", "Hand Trowel", "Watering Can"],
                            "safety": "Wear gloves when handling chemical fertilizers. Wash hands after use."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Core Summary: Application Methods & Safety",
                        "content": {
                            "title": "Key Takeaways",
                            "text": "- **Ring application at the drip line** is the gold standard for spaced vegetable crops.\n- **Never apply fertilizer against the stem** to prevent lethal osmotic chemical burning.\n- **Always cover fertilizer with soil** to stop ammonia volatilization and surface runoff.\n- **Careless fertilizer runoff causes eutrophication**, triggering algae blooms and suffocating fish."
                        }
                    }
                ],
                [
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Preventing Fertilizer Burn and Volatilization",
                        "content": {
                            "question": "A farm worker top-dresses tomato plants by piling 50 grams of dry CAN fertilizer directly against the base of each tomato stem and leaves it uncovered on dry soil. What two serious failures will occur?",
                            "options": [
                                "The tomato fruits will turn into apples, and the soil will freeze",
                                "The high salt concentration against the stem will draw water out of the plant cells causing lethal chemical stem burn, while solar heat will volatilize the uncovered nitrogen into ammonia gas, wasting the farmer's money",
                                "The fertilizer will attract underground earthworms that eat the tomatoes",
                                "The tomato plants will grow 10 meters tall in one night"
                            ],
                            "answer": "B",
                            "explanation": "Piling concentrated fertilizer against tender plant bark creates a severe osmotic gradient that sucks water out of stem cells, causing localized tissue necrosis and plant death (chemical fertilizer burn). Simultaneously, leaving uncovered nitrogen fertilizer on hot, dry soil causes rapid chemical decomposition into ammonia gas ($NH_3$), which volatilizes into the atmosphere, causing massive economic waste."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 8: Field Observation and Records
        # =====================================================================
        {
            "unit_order": 8,
            "unit_name": "Field Observation and Records",
            "unit_description": "Weekly diagnostic crop health walk, visual symptoms of mobile nitrogen deficiency (generalized chlorosis, V-shaped yellowing on older leaves), and designing a 4-column Field Management Logbook.",
            "lesson_title": "Field Scouting, Deficiency Diagnosis, and Farm Logbooks",
            "pages": [
                [
                    {
                        "type": "suggested_image",
                        "title": "Diagnostic Leaf Chlorosis and Nutrient Deficiency Scouting",
                        "content": {
                            "title": "Diagnostic Leaf Chlorosis and Nutrient Deficiency Scouting",
                            "caption": "An agricultural field scout inspecting crop leaves for visual symptoms of nitrogen deficiency chlorosis and pest damage during a weekly field health audit."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Scouting and Record Keeping",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Conduct a systematic weekly **diagnostic field scouting walk** across crop blocks.",
                                "Diagnose visual symptoms of **nitrogen deficiency (chlorosis)** on older leaves and understand nutrient mobility.",
                                "Distinguish nitrogen deficiency from iron deficiency, viral mosaic, and waterlogging.",
                                "Design and maintain a professional **4-Column Field Management Logbook** for agribusiness decision-making."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The Weekly Diagnostic Field Walk",
                        "content": {
                            "title": "Proactive Scouting Prevents Catastrophic Losses",
                            "text": "Successful agribusiness managers do not wait for crops to fail; they conduct systematic **weekly diagnostic field walks**:\n\n1. **Growth Cadence**: Are internodes elongating normally? Is vegetative branching on schedule?\n2. **Pest & Disease Scouting**: Check undersides of leaves for aphids, spider mites, and whiteflies; inspect stems for bacterial wilts or fungal blight spots.\n3. **Soil Moisture & Weeds**: Check soil moisture at 10 cm depth; spot emerging weed flushes before they set seed.\n4. **Nutrient Diagnostic Audit**: Inspect foliage colors to identify mineral deficiencies early."
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "Diagnosing Nitrogen Deficiency (Chlorosis)",
                        "content": {
                            "title": "Why Yellowing Appears on Older Leaves First",
                            "text": "Nitrogen is a **highly mobile nutrient** inside the vascular phloem of plants:\n\n### 1. The Translocation Mechanism\n- When soil nitrogen is exhausted, the plant prioritizes survival by scavenging nitrogen from its older, less productive lower leaves.\n- It hydrolyzes chlorophyll in old leaves and translocates the mobile nitrogen ions upward to nourish the young growing shoot tip and new leaves.\n\n### 2. Characteristic Visual Symptoms\n- **Generalized Lower-Leaf Chlorosis**: The older, bottom leaves turn a pale yellow, while the youngest top leaves remain light green.\n- **V-Shaped Yellowing (Maize / Cereals)**: Yellowing begins at the leaf tip and progresses backward along the central midrib in a distinct V-pattern, while outer leaf margins remain green.\n- **Stunted Stems**: Stems remain thin, fibrous, and woody; plants flower prematurely with tiny yields."
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Nitrogen Deficiency Leaf Chlorosis Diagnostic Progression",
                        "content": {
                            "title": "Nitrogen Deficiency Leaf Chlorosis Diagnostic Progression",
                            "caption": "Diagnostic botanical chart showing the progression of Nitrogen deficiency from a healthy dark-green leaf to the classic V-shaped midrib yellowing starting at the leaf tip on older maize leaves."
                        }
                    }
                ],
                [
                    {
                        "type": "comparison_table",
                        "title": "Visual Nutrient Deficiency Diagnostic Guide",
                        "content": {
                            "title": "Foliar Deficiency Symptoms Comparison",
                            "headers": ["Nutrient Deficient", "Mobility in Plant", "Location of Symptoms", "Visual Foliar Symptoms"],
                            "rows": [
                                ["Nitrogen (N)", "Highly Mobile", "Older Lower Leaves First", "Uniform pale yellowing (chlorosis); V-shaped pattern on maize midribs"],
                                ["Phosphorus (P)", "Mobile", "Older Lower Leaves First", "Distinct purple or reddish-bronze coloration along leaf veins and margins"],
                                ["Potassium (K)", "Mobile", "Older Lower Leaves First", "Marginal scorching and necrosis (burnt edges) with curled leaf tips"],
                                ["Iron (Fe)", "Immobile", "Youngest Top Leaves First", "Interveinal chlorosis (yellow leaves with sharp green veins) on top shoots"],
                                ["Calcium (Ca)", "Immobile", "Growing Shoot Tips & Fruits", "Blossom end rot (black sunken fruit bottoms in tomatoes); cupped young leaves"]
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Designing the Field Management Logbook",
                        "content": {
                            "title": "The Data Backbone of Commercial Agribusiness",
                            "text": "Professional farmers maintain detailed records to evaluate input efficiency and track farm profitability:\n\n- **Date**: Exact date of observation or task.\n- **Block / Plot ID**: Specific field section (e.g. Block B, Greenhouse 2).\n- **Observations / Diagnostics**: Pests, diseases, weed density, or chlorosis noted.\n- **Action Taken & Inputs Used**: Quantities of CAN applied, hours of labor, pruning completed."
                        }
                    }
                ],
                [
                    {
                        "type": "step_process",
                        "title": "Protocol: Responding to an Outbreak of Nitrogen Chlorosis",
                        "content": {
                            "title": "Emergency Remediation Workflow",
                            "steps": [
                                "1. **Confirm Visual Diagnosis**: Verify yellowing is confined to older lower leaves in a V-pattern.",
                                "2. **Check Root Zone Moisture**: Ensure yellowing is not caused by waterlogged root rot.",
                                "3. **Apply Fast-Acting Top-Dress**: Apply 10–15g of CAN per plant in a covered ring at the drip line.",
                                "4. **Apply Emergency Foliar Feed**: Spray a high-nitrogen soluble foliar fertilizer (e.g. 30-10-10 NPK) for immediate 24-hour stomatal uptake.",
                                "5. **Log Event in Farm Records**: Record input costs and monitor greening response over 5–7 days."
                            ]
                        }
                    },
                    {
                        "type": "mini_activity",
                        "title": "Practical Workshop: Designing and Completing a Farm Logbook",
                        "content": {
                            "title": "School Farm Diagnostic Scouting Practical",
                            "task": "1. In your agriculture notebook, draw a structured 5-column Field Logbook (*Date, Block ID, Observation, Action Taken, Input Costs*).\n2. Walk through the school vegetable garden.\n3. Identify any plants exhibiting nitrogen deficiency, pest damage, or excess suckers.\n4. Complete the logbook entry with accurate agronomic prescriptions.",
                            "materials": ["Notebook", "Ruler", "Pen"],
                            "safety": "Maintain clean handwriting and accurate documentation."
                        }
                    }
                ],
                [
                    {
                        "type": "key_takeaway",
                        "title": "Core Summary: Scouting and Records",
                        "content": {
                            "title": "Key Takeaways",
                            "text": "- **Weekly diagnostic field walks** detect nutrient, pest, and moisture issues early.\n- **Nitrogen is mobile**; deficiency symptoms appear on older lower leaves first as V-shaped yellowing.\n- **Immobile nutrient deficiencies (Fe, Ca)** appear on youngest top leaves and fruits first.\n- **Maintaining a Field Logbook** is mandatory for agribusiness financial tracking."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Mobile Nitrogen Deficiency Diagnosis",
                        "content": {
                            "question": "During a weekly farm inspection, a student observes that the bottom older leaves of a maize crop are turning pale yellow in a V-shaped pattern along the midrib, while the top new leaves remain light green. What is the physiological diagnosis?",
                            "options": [
                                "Severe iron toxicity in the soil",
                                "Nitrogen deficiency; because nitrogen is mobile, the plant scavenges nitrogen from old lower leaves and translocates it upward to support new shoot growth",
                                "The maize plants have been attacked by bats",
                                "The maize crop is preparing to produce sweet potatoes"
                            ],
                            "answer": "B",
                            "explanation": "Nitrogen is a mobile nutrient in plant vascular systems. When soil nitrogen is deficient, the plant hydrolyzes chlorophyll in its oldest lower leaves and translocates the nitrogen ions upward to keep young growing shoots alive. This causes the characteristic V-shaped chlorosis on older leaves first, while top leaves remain green."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 9: Importance and Resource Stewardship
        # =====================================================================
        {
            "unit_order": 9,
            "unit_name": "Importance and Resource Stewardship",
            "unit_description": "Agronomic enhancement of Grade 1 premium market produce, net financial return cost-benefit calculations, and environmental stewardship: nitrogen runoff, algae blooms, and aquatic eutrophication.",
            "lesson_title": "Agribusiness Economics and Environmental Stewardship",
            "pages": [
                [
                    {
                        "type": "suggested_image",
                        "title": "Agricultural Watershed and Environmental Conservation",
                        "content": {
                            "title": "Agricultural Watershed and Environmental Conservation",
                            "caption": "A sustainable agricultural landscape in Kenya demonstrating riparian buffer zones protecting clean water bodies from agricultural runoff."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Economics and Environmental Stewardship",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Explain how proper pruning and top-dressing produce **Grade 1 premium market produce**.",
                                "Perform an agribusiness **Cost-Benefit Analysis** to calculate Net Financial Return on top-dressing investments.",
                                "Analyze the ecological mechanism of **eutrophication** caused by fertilizer runoff into freshwater ecosystems.",
                                "Adopt **riparian buffer strips** and precision nutrient management to protect community water resources."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The Agribusiness Value of Premium Produce",
                        "content": {
                            "title": "Quality Dictates Market Price",
                            "text": "In commercial horticulture, farm revenue is determined by the **market grade** of the harvest, not merely total tonnage:\n\n- **Grade 1 Produce**: Large, uniform, clean, thick-walled tomatoes and capsicums free of blemishes, sunscald, or rot. High-end supermarkets, export distributors, and hotels pay a **30% to 60% price premium** for Grade 1 produce.\n- **Grade 2 / Rejects**: Small, blemished, sunscalded, or misshapen fruits sold at a heavy discount in local wholesale markets.\n- **The Field Management Link**: Pruning lateral suckers and precision top-dressing directly transform a low-value, tangled crop into high-value Grade 1 produce."
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "Cost-Benefit Analysis of Top-Dressing",
                        "content": {
                            "title": "Calculating Net Financial Return",
                            "text": "Before purchasing inputs, an agricultural entrepreneur calculates whether the investment will yield a net profit:\n\n$$\\text{Net Financial Return} = (\\text{Yield with Top-Dress} \\times \\text{Price}) - (\\text{Yield without Top-Dress} \\times \\text{Price}) - (\\text{Cost of Fertilizer} + \\text{Labor})$$\n\n### Worked Agribusiness Example (1 Acre of Kales):\n- *Without Top-Dressing*: Yield = 2,000 kg @ KES 20/kg = **KES 40,000 Revenue**.\n- *With CAN Top-Dressing*: Yield = 4,000 kg @ KES 20/kg = **KES 80,000 Revenue**.\n- *Additional Gross Revenue*: KES 80,000 - KES 40,000 = **KES 40,000**.\n- *Total Input Cost*: 2 Bags CAN (KES 7,000) + Labor (KES 2,000) = **KES 9,000**.\n- *Net Additional Profit*: KES 40,000 - KES 9,000 = **+ KES 31,000 Net Profit**!\n- *Conclusion*: Top-dressing generates a 344% return on investment (ROI), making it highly profitable."
                        }
                    },
                    {
                        "type": "comparison_table",
                        "title": "Financial Cost-Benefit Scenarios",
                        "content": {
                            "title": "Agribusiness Return on Investment Scenarios",
                            "headers": ["Scenario", "Gross Revenue (KES)", "Input & Labor Cost (KES)", "Net Profit (KES)", "Agribusiness Decision"],
                            "rows": [
                                ["Option A: No Top-Dress (Low Input)", "40,000", "0 (Zero extra input)", "40,000", "Low risk, but leaves KES 31,000 profit on table"],
                                ["Option B: Precision CAN Top-Dress", "80,000", "9,000 (CAN + Labor)", "71,000", "Optimal (+KES 31,000 net extra profit)"],
                                ["Option C: Excessive Over-Fertilization", "82,000", "25,000 (Excess CAN + Waste)", "57,000", "Flawed (Excess fertilizer costs exceed extra yield)"]
                            ]
                        }
                    }
                ],
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Agricultural Nitrogen Runoff & Aquatic Eutrophication Chain",
                        "content": {
                            "title": "Agricultural Nitrogen Runoff & Aquatic Eutrophication Chain",
                            "caption": "Ecological sequence diagram showing Uncovered Fertilizer -> Stormwater Runoff -> River Influx -> Massive Algae Bloom -> Decomposition Bacteria -> Dissolved Oxygen Depletion -> Fish Suffocation."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Environmental Stewardship: Protecting Aquatic Ecosystems",
                        "content": {
                            "title": "Preventing Eutrophication and Water Pollution",
                            "text": "Agricultural entrepreneurs have a moral and ecological responsibility to protect shared water resources:\n\n- **The Eutrophication Chain**: Broadcast fertilizer washed into rivers triggers explosive algae growth. When algae die, decomposing bacteria consume all dissolved oxygen, creating anaerobic 'dead zones' that kill fish and destroy local livelihoods.\n- **Riparian Buffer Strips**: Planting 3-to-5-meter wide permanent grass and agroforestry buffers along riverbanks filters out 90% of sediment and dissolved nutrients before runoff reaches water bodies."
                        }
                    }
                ],
                [
                    {
                        "type": "mini_activity",
                        "title": "Agribusiness Practical: Calculating Fertilizer Return on Investment",
                        "content": {
                            "title": "Cost-Benefit Math Scenario",
                            "task": "Calculate the net return for a 2-acre tomato farm:\n- Baseline Yield (No top-dress): 6,000 kg @ KES 40/kg.\n- Managed Yield (With pruning + CAN top-dress): 14,000 kg @ KES 50/kg (Grade 1 Premium).\n- Total Costs: 4 Bags CAN (KES 14,000) + Pruning/Trellising Labor (KES 10,000) + Application Labor (KES 4,000).\n\nCalculate:\n1. Baseline Revenue vs Managed Revenue.\n2. Total Additional Cost.\n3. Net Extra Profit generated by professional field management.",
                            "materials": ["Calculator", "Case Study Handout", "Notebook"],
                            "safety": "Verify all mathematical calculations."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Core Summary: Economics and Stewardship",
                        "content": {
                            "title": "Key Takeaways",
                            "text": "- **Pruning and top-dressing elevate produce to Grade 1**, commanding 30–60% price premiums.\n- **Cost-benefit calculations** ensure input expenses do not exceed additional yield revenue.\n- **Fertilizer runoff causes eutrophication**, killing fish and polluting community water.\n- **Riparian grass buffer strips** trap escaping nutrients and safeguard aquatic life."
                        }
                    }
                ],
                [
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Agricultural Eutrophication Mechanism",
                        "content": {
                            "question": "How does careless, heavy broadcasting of synthetic nitrogen fertilizer on a sloping farm directly lead to the mass suffocation of fish in a lake located at the bottom of the valley?",
                            "options": [
                                "Fish eat the fertilizer granules directly and burst",
                                "Rainwater washes excess nitrogen into the lake, triggering an explosive algae bloom; as the dense algae die and decompose, aerobic bacteria consume all dissolved oxygen in the water, suffocating the fish",
                                "Nitrogen fertilizer freezes the lake water solid",
                                "Fertilizer turns all lake fish into terrestrial frogs"
                            ],
                            "answer": "B",
                            "explanation": "This ecological catastrophe is known as eutrophication. Nitrogen is a potent plant nutrient that stimulates massive algae blooms in water bodies. When the algae bloom ends, billions of dead algal cells sink to the bottom. Aerobic decomposing bacteria multiply exponentially and consume all dissolved oxygen ($O_2$) in the water, creating anoxic 'dead zones' where fish and aquatic life suffocate."
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
            "unit_description": "Holistic synthesis of the integrated field management system (pruning + top-dressing + staking synergy), troubleshooting crop canopy failures (vegetable jungle, nitrogen scorch, yellow canopy), practical peer-review rubric, and Summative Topic Assessment.",
            "lesson_title": "Synthesis of Field Management and Summative Assessment",
            "pages": [
                [
                    {
                        "type": "suggested_image",
                        "title": "Harvested Grade-1 Vegetables at Commercial Farm Market",
                        "content": {
                            "title": "Harvested Grade-1 Vegetables at Commercial Farm Market",
                            "caption": "A successful commercial harvest of Grade-1 capsicums, tomatoes, and leafy vegetables produced through disciplined post-planting field management."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Synthesis & Summative Assessment",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Synthesize the **integrated field management system** (pruning, staking, top-dressing, weeding, mulching).",
                                "Troubleshoot common field management failures based on visual canopy and foliar symptoms.",
                                "Execute a standard **peer-review practical evaluation** for pruning and fertilizer application.",
                                "Complete the comprehensive **Summative Topic Assessment** covering all 10 lessons of Topic 4."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The Integrated Field Management Framework",
                        "content": {
                            "title": "The Agronomic Synergy of Post-Planting Care",
                            "text": "In commercial agribusiness, field management practices operate as an interconnected, synergistic system:\n\n- **Pruning** opens the canopy to sunlight and air, eliminating disease pockets.\n- **Staking & Trellising** lifts heavy fruit clusters away from damp soil pathogens.\n- **Top-Dressing** provides the nitrogen fuel required to power rapid fruit filling.\n- **Weeding & Mulching** preserves moisture and eliminates resource theft.\n\n- *If any single component is neglected, the entire production system collapses!*"
                        }
                    }
                ],
                [
                    {
                        "type": "comparison_table",
                        "title": "Field Management Troubleshooting and Diagnostic Guide",
                        "content": {
                            "title": "Field Canopy Diagnostic Matrix",
                            "headers": ["Observed Canopy Symptom", "Underlying Agronomic Failure", "Immediate Corrective Prescription"],
                            "rows": [
                                ["'Vegetable Jungle': Dense tangled vines, tiny rotting fruits on ground", "Failure to prune lateral suckers and stake tomato plants", "Prune lateral suckers immediately, install stakes, tie main stems, clear lower leaves"],
                                ["'Chemical Leaf Scorch': Brown, shriveled, dead stem bark near base", "Fertilizer applied in direct contact with soft stem", "Flush soil with clean water; in future, apply strictly in rings at the drip line"],
                                ["'Yellow Canopy': Bottom leaves uniformly yellowing in V-shape", "Severe Nitrogen deficiency; delayed top-dressing", "Apply 10–15g CAN at drip line and spray emergency high-N foliar feed"],
                                ["'Sunscald': White, leathery sunken patches on exposed tomato fruit", "Excessive single-stem de-leafing in hot, un-shaded open field", "Maintain shade netting or transition to two-stem pruning for leaf canopy protection"]
                            ]
                        }
                    }
                ],
                [
                    {
                        "type": "mini_activity",
                        "title": "Performance Task: Drafting a Commercial Crop Rehabilitation Brief",
                        "content": {
                            "title": "Consultancy Brief: Turning Around a Failing Tomato Project",
                            "task": "A youth group in Meru transplanted 5,000 tomato plants on 2 acres with drip irrigation but neglected field care. You observe:\n1. Tangled, un-staked bushes sprawling on damp mud with grey mold rot.\n2. Pale yellow lower leaves across the field with dry CAN granules scattered on bare soil.\n\n**Your Deliverable**: Draft a 1-page emergency Crop Turnaround Plan detailing:\n1. Pruning, staking, and de-leafing protocols.\n2. Correct CAN ring application and watering procedures.\n3. A 4-column Field Management Logbook template.",
                            "materials": ["Case Study Handout", "Consultancy Template", "Pen"],
                            "safety": "Ensure realistic, professional agribusiness recommendations."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Core Summary: Field Management Mastery",
                        "content": {
                            "title": "Key Takeaways",
                            "text": "- **Field management** protects and fuels crops from emergence to harvest.\n- **Pruning + Staking + Top-Dressing** work in perfect agronomic synergy.\n- **Prune capsicum below the Y-fork**; prune single/multiple stem tomatoes.\n- **Apply top-dressing at the drip line and bury it** to prevent burn and volatilization.\n- **Scout weekly** and maintain a Field Logbook for commercial profitability."
                        }
                    }
                ],
                # Pages 4 to 8: 8 Summative Assessment MCQs
                [
                    {
                        "type": "knowledge_check",
                        "title": "Summative MCQ 1: Purpose of Post-Planting Field Care",
                        "content": {
                            "question": "What is the primary agronomic purpose of implementing comprehensive post-planting field management practices in crop production?",
                            "options": [
                                "To change the crop variety into a perennial forest tree",
                                "To protect and nurture the crop through its vegetative and reproductive stages, enabling it to reach its full genetic yield potential and produce Grade 1 market quality",
                                "To eliminate the need for harvesting crops",
                                "To prevent sunlight from reaching the field"
                            ],
                            "answer": "B",
                            "explanation": "Field management practices (weeding, pruning, top-dressing, staking, mulching) protect the growing crop from biotic stresses (weeds, pests, diseases) and provide continuous nutrients and support, enabling the crop to reach its genetic yield potential and produce premium market-grade harvests."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Summative MCQ 2: Capsicum Y-Fork Pruning Protocol",
                        "content": {
                            "question": "Which specific plant parts must be removed when pruning a young capsicum (sweet pepper) plant to prevent soil-borne fungal diseases?",
                            "options": [
                                "All roots growing beneath the soil surface",
                                "All lateral side shoots and leaves growing on the main stem below the first primary Y-fork",
                                "All flower buds at the very top of the canopy exclusively",
                                "The main stem itself at ground level"
                            ],
                            "answer": "B",
                            "explanation": "Pruning capsicum involves removing all side shoots (suckers) and leaves on the main stem below the first primary Y-fork. This creates a clean 15–20 cm base that elevates foliage off damp soil, eliminates splash-transmitted fungal pathogens, and improves ventilation."
                        }
                    }
                ],
                [
                    {
                        "type": "knowledge_check",
                        "title": "Summative MCQ 3: Single-Stem vs Multiple-Stem Tomato Economics",
                        "content": {
                            "question": "Why is the single-stem pruning system preferred over multiple-stem systems in commercial high-density greenhouse tomato production?",
                            "options": [
                                "Single-stem tomatoes do not require any water or fertilizer",
                                "Single-stem pruning focuses photosynthetic energy into producing extra-large, uniform, Grade 1 premium fruits while allowing narrow upright spacing to maximize yield per square meter",
                                "Single-stem tomatoes are completely immune to all bacterial diseases",
                                "Multiple-stem tomatoes cannot grow indoors under any circumstances"
                            ],
                            "answer": "B",
                            "explanation": "In commercial greenhouses where space and infrastructure are capital-intensive, single-stem pruning allows high-density vertical planting (30–45 cm spacing) and focuses sugars into large, uniform, premium Grade 1 fruits that command high prices in supermarkets and export markets."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Summative MCQ 4: Perennial Rejuvenation Pruning",
                        "content": {
                            "question": "What is 'cutting back' in perennial crop management, and what physiological response does it trigger in an old, unproductive coffee tree?",
                            "options": [
                                "Cutting the root tips to kill the tree permanently",
                                "Sawing the old unproductive trunk down to 15–30 cm above the ground at a 45° angle, which stimulates the established root crown to push out a flush of vigorous new vegetative suckers to regenerate production",
                                "Stripping all green leaves off the tree by hand",
                                "Painting the tree branches with white agricultural lime"
                            ],
                            "answer": "B",
                            "explanation": "Cutting back (rejuvenation pruning) involves sawing old, senescent trunks down to 15–30 cm above ground level. Driven by root pressure from the extensive existing root system, the stump produces vigorous new vegetative suckers that mature into high-yielding productive trunks within 18 months."
                        }
                    }
                ],
                [
                    {
                        "type": "knowledge_check",
                        "title": "Summative MCQ 5: Timing of Top-Dressing in Maize",
                        "content": {
                            "question": "Why is the 'knee-high' growth stage (V6 leaf stage) considered the critical application window for top-dressing maize with nitrogenous fertilizer?",
                            "options": [
                                "It is the only time the farmer is legally allowed to enter the field",
                                "At the knee-high stage, the maize plant begins exponential stem elongation and leaf canopy development, causing its biological demand for nitrogen to spike dramatically",
                                "Maize roots stop absorbing nutrients completely after the knee-high stage",
                                "Knee-high maize plants produce honey that dissolves fertilizer"
                            ],
                            "answer": "B",
                            "explanation": "Crop nutrient uptake follows a sigmoidal growth curve. The knee-high stage marks the transition into rapid vegetative stem elongation and ear differentiation, where nitrogen uptake spikes from 0.5 kg/ha/day to over 4.0 kg/ha/day. Supplying fast-acting nitrogen at this exact stage fuels maximum photosynthetic leaf area."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Summative MCQ 6: Fertilizer Ring Application Precision",
                        "content": {
                            "question": "Where should a farmer dig the circular trench when applying top-dressing fertilizer around a spaced vegetable crop like capsicum or tomato?",
                            "options": [
                                "Directly touching the main stem of the plant",
                                "At the outer leaf drip line (the perimeter beneath the outermost leaf tips) where active feeder root hairs are concentrated",
                                "5 meters away in the neighbor's field",
                                "At the very bottom of the taproot 2 meters underground"
                            ],
                            "answer": "B",
                            "explanation": "Active water- and nutrient-absorbing feeder roots are concentrated directly beneath the outer perimeter of the leaf canopy (the drip line). Digging a shallow ring trench at the drip line delivers fertilizer directly to the root hairs while preventing lethal chemical fertilizer burn against the main stem."
                        }
                    }
                ],
                [
                    {
                        "type": "knowledge_check",
                        "title": "Summative MCQ 7: Mobile Nitrogen Deficiency Diagnosis",
                        "content": {
                            "question": "Why do visual symptoms of nitrogen deficiency (chlorosis) appear on the older, lower leaves of a plant first rather than on the young top leaves?",
                            "options": [
                                "Old leaves are closer to the ground and get dirty",
                                "Nitrogen is a mobile nutrient; when soil nitrogen is deficient, the plant hydrolyzes chlorophyll in older leaves and translocates the mobile nitrogen ions upward to keep young growing shoot tips alive",
                                "Old leaves absorb nitrogen gas directly from the soil air",
                                "Young leaves produce nitrogen internally through photosynthesis"
                            ],
                            "answer": "B",
                            "explanation": "Nitrogen is highly mobile in the plant's vascular phloem. Under nutrient stress, the plant sacrifices its older lower leaves by breaking down chlorophyll and translocating mobile nitrogen upward to sustain new growing shoots. This causes older lower leaves to turn pale yellow (chlorosis) first."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Summative MCQ 8: Agricultural Eutrophication",
                        "content": {
                            "question": "What is the primary ecological mechanism by which excessive agricultural fertilizer runoff causes the death of fish in downstream lakes and rivers?",
                            "options": [
                                "The fertilizer turns the lake water into pure sulfuric acid",
                                "Excess nitrogen washes into the lake, triggering an explosive algae bloom; as the dense algae die and decompose, aerobic bacteria multiply and consume all dissolved oxygen in the water, suffocating fish",
                                "Fish absorb the fertilizer and grow too large to swim",
                                "The fertilizer boils the river water instantly"
                            ],
                            "answer": "B",
                            "explanation": "Eutrophication occurs when excess dissolved nitrogen and phosphorus enter aquatic ecosystems. The nutrient surge stimulates massive algae blooms that block sunlight. When the algae die, decomposing aerobic bacteria consume virtually all dissolved oxygen ($O_2$) in the water, creating anoxic 'dead zones' where fish and other aquatic life suffocate."
                        }
                    }
                ],
                # Page 8: Capstone Summary
                [
                    {
                        "type": "summary",
                        "title": "Topic 4 Capstone Summary: Field Management Mastery",
                        "content": {
                            "title": "Mastery Overview: Grade 10 Field Management Practices",
                            "text": "Congratulations on completing **Topic 4: Field Management Practices**!\n\nYou have mastered:\n- **The Post-Planting Toolkit**: Gapping, thinning, weeding, pruning, top-dressing, staking, and mulching.\n- **Pruning Capsicum**: Clearing lower side shoots below the primary Y-fork to suppress fungal blights and maximize fruit size.\n- **Tomato Pruning Systems**: Single-stem greenhouse vertical trellising vs multiple-stem open-field sunscald protection.\n- **Perennial Crop Management**: Capping coffee at 1.5–1.8 m and cutting back senescent bushes at 15–30 cm for rejuvenation.\n- **Top-Dressing Science**: Fast-acting nitrogen (CAN, Urea, Liquid Manure), knee-high maize timing, and drip-line ring application.\n- **Diagnostic Scouting & Logging**: Diagnosing mobile nitrogen deficiency (V-shaped yellowing on older leaves) and maintaining Field Logbooks.\n- **Agribusiness & Stewardship**: Cost-benefit ROI calculations, Grade 1 produce premiums, and preventing eutrophication in water ecosystems."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Topic 4 Final Takeaway",
                        "content": {
                            "title": "The Agronomist's Management Axiom",
                            "text": "Planting initiates life, but field management guarantees the harvest. Prune with precision, feed at the drip line, scout weekly, and protect the surrounding environment."
                        }
                    }
                ]
            ]
        }
    ]

@transaction.atomic
def ingest_grade10_topic4(replace=False):
    """Executes the complete production ingestion of Grade 10 Agriculture Topic 4: Field Management Practices."""
    print("=" * 80)
    print("STARTING INGESTION: CBC Grade 10 Agriculture — Topic 4: Field Management Practices")
    print("=" * 80)

    curriculum = Curriculum.objects.filter(name__iexact="CBC").first()
    grade = Grade.objects.filter(curriculum=curriculum, name__icontains="10").first()
    subject = Subject.objects.filter(grade=grade, name__iexact="Agriculture").first()

    assert curriculum and grade and subject, "Curriculum/Grade/Subject not found!"

    topic_name = "Field Management Practices"
    topic = Topic.objects.filter(subject=subject, name=topic_name).first()
    if not topic:
        topic = Topic.objects.create(
            subject=subject,
            name=topic_name,
            description="Comprehensive theoretical, practical, and scientific study of post-planting field management, pruning systems, top-dressing, diagnostic crop scouting, and resource stewardship.",
            order=4
        )
        print(f"Created Topic 4: {topic.name} (ID: {topic.id})")
    else:
        topic.order = 4
        topic.description = "Comprehensive theoretical, practical, and scientific study of post-planting field management, pruning systems, top-dressing, diagnostic crop scouting, and resource stewardship."
        topic.save()
        print(f"Resolved Topic 4: {topic.name} (ID: {topic.id})")

    if replace:
        print("Flag --replace active: Clearing existing LearningUnits and Lessons for Topic 4...")
        topic.learning_units.all().delete()
        topic.lessons.all().delete()

    curriculum_data = build_topic4_curriculum()
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
                    "topic_order": 4,
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
                    block_id=f"g10_agri_t4_u{u_order}_p{page_idx}_b{comp_idx}",
                    block_type=b_type,
                    component_type=b_type,
                    title=b_title,
                    content=b_content,
                    order=block_order_counter,
                    page_number=page_idx,
                    component_order=comp_idx,
                    page_title=b_title if comp_idx == 1 else None,
                    metadata={"topic_order": 4, "unit_order": u_order, "page": page_idx}
                )
                block_order_counter += 1
                total_blocks += 1

        print(f"  Ingested Unit {u_order}: {u_name} -> Lesson '{l_title}' ({len(pages)} Pages, {block_order_counter - 1} Blocks)")

    print("=" * 80)
    print(f"INGESTION COMPLETE: Topic 4 '{topic.name}'")
    print(f"  Total Units:   {total_units}")
    print(f"  Total Lessons: {total_lessons}")
    print(f"  Total Pages:   {total_pages}")
    print(f"  Total Blocks:  {total_blocks}")
    print("=" * 80)

if __name__ == "__main__":
    replace_flag = "--replace" in sys.argv
    ingest_grade10_topic4(replace=replace_flag)
