"""
VLearn CBC Grade 9 Agriculture — Topic 4: Organic Gardening
Production Ingestion Engine (Phase 1: Content & Card Architecture)

Curriculum: CBC (Curriculum ID: 5)
Grade: Grade 9 (Level: 9)
Subject: Agriculture
Topic: Organic Gardening (Topic Order: 4)

Decomposed into 8 Learning Units & 8 Published Lessons:
  1. Meaning and Importance of Organic Gardening (6 Pages, 11 Blocks)
  2. Organic Manure from Plant Matter and Animal Waste (6 Pages, 11 Blocks)
  3. Organic Pesticides from Locally Available Materials (6 Pages, 11 Blocks)
  4. Mechanical Weed Control and Organic Foliar Feed (6 Pages, 11 Blocks)
  5. Maintenance of Crops in an Organic Garden (6 Pages, 11 Blocks)
  6. Selecting a Short-Season Crop & Farm Plot Preparation (6 Pages, 11 Blocks)
  7. Practical Crop Establishment (Planting) (6 Pages, 11 Blocks)
  8. Planting and Maintaining the Selected Crop & Capstone (10 Pages, 21 Blocks)

Features:
  - Rich typography with bold key terms and structured markdown bullet points.
  - Step-by-step practical process workflows.
  - Formatted comparison tables, classification matrices, and callouts.
  - Formative scenario MCQs and Topic Summative MCQs with educational explanations.
  - Zero citation bracket leaks, zero meta-tag leaks, and zero raw LaTeX.

Usage:
  ./venv/bin/python curriculum/ingest_cbc_grade9_agriculture_topic4.py [--replace]
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
    # Convert unicode bullets to markdown list items
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
    """Returns the comprehensive pedagogical page and block structure for Topic 4: Organic Gardening."""
    return [
        # =====================================================================
        # LESSON 1: Meaning and Importance of Organic Gardening
        # =====================================================================
        {
            "unit_order": 1,
            "unit_name": "Meaning and Importance of Organic Gardening",
            "unit_description": "Organic gardening definition, avoiding synthetic agrochemicals, cost savings, food safety, and protecting soil biodiversity.",
            "lesson_title": "Meaning and Importance of Organic Gardening",
            "pages": [
                # Page 1: Visual Hook & Learning Objectives
                [
                    {
                        "type": "suggested_image",
                        "title": "Natural Abundance: The Chemical-Free Garden",
                        "content": {
                            "title": "Natural Abundance: The Chemical-Free Garden",
                            "caption": "A healthy, thriving organic vegetable garden producing fresh, chemical-free food using natural compost and botanical sprays."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Learning Objectives: Principles of Organic Gardening",
                        "content": {
                            "title": "What We Will Learn Today",
                            "goals": [
                                "Define **organic gardening** as a sustainable, chemical-free crop production system.",
                                "Identify the 4 forbidden synthetic inputs: chemical fertilizers, herbicides, and toxic pesticides.",
                                "Analyze the **health, environmental, and financial benefits** of organic food production.",
                                "Differentiate between natural organic techniques and synthetic chemical practices."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "What is Organic Gardening?",
                        "content": {
                            "title": "Growing Food with Nature",
                            "text": "**Organic gardening** is the agricultural practice of cultivating food crops—such as vegetables, fruits, legumes, and herbs—using only natural biological compounds and ecological processes.\n\n- **Zero Synthetic Agrochemicals**: Strictly avoids artificial chemical fertilizers, synthetic weed-killers (herbicides), and chemical pesticides.\n- **Natural Substitutes**: Relies on compost manure, green manures, animal droppings, botanical pest extracts, and manual weeding to nourish and protect crops."
                        }
                    }
                ],
                # Page 2: Core Practices of Organic Gardening
                [
                    {
                        "type": "concept_explanation",
                        "title": "The 5 Pillars of Organic Crop Care",
                        "content": {
                            "title": "Active Biological Stewardship",
                            "text": "- **1. Organic Manures**: Building living soil structure using decomposed plant and animal wastes.\n- **2. Organic Foliar Feeds**: Spraying nutrient-rich botanical and manure teas directly onto leaves.\n- **3. Mechanical Weed Control**: Removing weeds physically using hoes, slashers, uprooting, and dry mulches.\n- **4. Botanical Pesticides**: Extracting non-toxic insect repellents from neem seeds, garlic bulbs, and chilli peppers.\n- **5. Crop Rotation & Companion Planting**: Planting diverse crops together to confuse pests and maintain soil balance."
                        }
                    },
                    {
                        "type": "comparison_table",
                        "title": "Comparison: Organic Gardening vs. Synthetic Chemical Agriculture",
                        "content": {
                            "title": "Farming Systems Comparison Matrix",
                            "headers": ["Evaluation Metric", "Organic Gardening", "Synthetic Chemical Agriculture"],
                            "rows": [
                                ["Food Safety & Health", "Zero toxic chemical residues; produce is safe to eat", "Chemical residues on leaves pose toxicity risks to humans"],
                                ["Production Cost", "Minimal; uses free, locally available organic wastes and weeds", "High; requires recurring cash purchases of commercial sprays"],
                                ["Soil Biology", "Nourishes earthworms, fungi, and beneficial soil microbes", "Chemical salts kill soil organisms and harden the ground"],
                                ["Water Channels", "Protects local streams from dangerous chemical runoff", "Causes toxic pollution of water sources and kills aquatic life"]
                            ]
                        }
                    }
                ],
                # Page 3: Visual Matrix Architecture
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Organic Gardening vs. Synthetic Agriculture Matrix",
                        "content": {
                            "title": "Organic Gardening vs. Synthetic Agriculture Matrix",
                            "caption": "Comparison blueprint contrasting chemical hazards and high costs with organic health, soil humus, and zero cash inputs."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Soil Biodiversity: Living Soil vs. Dead Dirt",
                        "content": {
                            "title": "Feeding the Soil Web",
                            "text": "Healthy soil is not just dead dirt! A single handful of organic soil contains billions of living bacteria, fungi, and earthworms. Organic matter feeds these micro-organisms, which break down minerals into absorbable plant food naturally."
                        }
                    }
                ],
                # Page 4: Case Study: Economic & Health Independence
                [
                    {
                        "type": "worked_example",
                        "title": "Homestead Case Study: The Chemical-Free Transition",
                        "content": {
                            "intro": "Mama Auma converted her 1/2-acre vegetable plot from chemical spraying to 100% organic management:",
                            "steps": [
                                "**Cost Reduction**: Replaced 4,500 KES monthly commercial fertilizer purchases with farmyard compost and chicken manure.",
                                "**Pest Control**: Replaced toxic chemical sprays with homemade neem and garlic extracts.",
                                "**Market Premium**: Sells certified chemical-free spinach and kales at a 25% price premium to health-conscious local families.",
                                "**Outcome**: Higher household profit, better family health, and zero medical risks from chemical exposure!"
                            ]
                        }
                    }
                ],
                # Page 5: Formative Knowledge Check
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check: Fundamental Principles",
                        "content": {
                            "question": "Why does practicing organic gardening save farmers money compared to synthetic chemical agriculture?",
                            "options": [
                                "Because organic crops never require any nutrients or water to grow.",
                                "Because it utilizes free, locally available biological resources like crop wastes, weeds, and animal droppings.",
                                "Because chemical companies distribute organic seeds for free.",
                                "Because organic weeding does not require any manual physical effort."
                            ],
                            "answer": "B",
                            "explanation": "Organic gardening relies on free, locally accessible materials (kitchen scraps, plant biomass, animal dung) rather than expensive manufactured agrochemical fertilizers and sprays."
                        }
                    }
                ],
                # Page 6: Summary & Connection Forward
                [
                    {
                        "type": "key_takeaway",
                        "title": "Lesson Summary",
                        "content": {
                            "text": "- **Organic gardening** grows crops using natural biological inputs without synthetic chemicals.\n- Prohibits **chemical fertilizers, synthetic herbicides, and toxic pesticides**.\n- Safeguards **human health, nourishes soil biodiversity, and eliminates cash expenses**.\n- Builds sustainable, long-term food security for families and communities."
                        }
                    },
                    {
                        "type": "transition",
                        "title": "Looking Ahead",
                        "content": {
                            "text": "How do we feed our organic soil effectively? In the next lesson, we examine the three primary forms of organic manure and master the step-by-step construction of a layered compost heap!"
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 2: Organic Manure from Plant Matter and Animal Waste
        # =====================================================================
        {
            "unit_order": 2,
            "unit_name": "Organic Manure from Plant Matter and Animal Waste",
            "unit_description": "Three forms of organic manure (compost, farmyard, green manure), heap vs pit composting, and 5-layer biological heap construction.",
            "lesson_title": "Organic Manure from Plant Matter and Animal Waste",
            "pages": [
                # Page 1: Visual Hook & Learning Objectives
                [
                    {
                        "type": "suggested_image",
                        "title": "Black Gold: Decomposed Organic Manure",
                        "content": {
                            "title": "Black Gold: Decomposed Organic Manure",
                            "caption": "Rich, dark, crumbly finished compost manure ready to enrich crop beds with humus and living soil microbes."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Learning Objectives: Organic Manure Systems",
                        "content": {
                            "title": "What We Will Learn Today",
                            "goals": [
                                "Differentiate between **compost manure, farmyard manure, and green manure**.",
                                "Compare the **Heap Method** (wet areas) vs. the **Pit Method** (dry areas).",
                                "Master the **5-layer biological construction sequence** of a compost heap.",
                                "Explain why regular aeration (turning) accelerates decomposition."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The 3 Forms of Organic Manure",
                        "content": {
                            "title": "Biological Soil Fertilizers",
                            "text": "- **1. Compost Manure**: Decomposed mixture of kitchen waste, dry crop residues, green weeds, and animal droppings piled and decayed together.\n- **2. Farmyard Manure**: Decomposed livestock bedding (straw/hay) that has thoroughly absorbed animal dung and urine inside animal pens.\n- **3. Green Manure**: Fast-growing leguminous crops (beans, desmodium) plowed directly into moist soil while flowering to release succulent nitrogen."
                        }
                    }
                ],
                # Page 2: Composting Mechanics: Heaps vs. Pits
                [
                    {
                        "type": "concept_explanation",
                        "title": "Heap Method vs. Pit Method",
                        "content": {
                            "title": "Adapting to Local Climate",
                            "text": "- **The Above-Ground Heap Method**: Materials are built upward on a raised stick platform. Best for **wet climates or rainy seasons** to prevent water-logging and rot.\n- **The Below-Ground Pit Method**: Materials are layered inside a dug pit. Best for **dry climates or dry seasons** to shield organic matter from drying winds and lock in moisture."
                        }
                    },
                    {
                        "type": "comparison_table",
                        "title": "Composting Methods Comparison",
                        "content": {
                            "title": "Compost Heap vs. Compost Pit",
                            "headers": ["Feature", "Above-Ground Heap Method", "Below-Ground Pit Method"],
                            "rows": [
                                ["Ideal Climate", "High rainfall / wet seasons", "Low rainfall / arid / windy seasons"],
                                ["Drainage & Aeration", "Excellent natural drainage; no water-logging", "Protected from wind; traps moisture inside"],
                                ["Construction", "Built on a raised platform of dry coarse sticks", "Dug 1 meter deep into the ground"],
                                ["Turning Requirement", "Turned every 2-3 weeks to regulate oxygen", "Turned between adjacent pits to aerate"]
                            ]
                        }
                    }
                ],
                # Page 3: The 5-Layer Compost Heap Architecture
                [
                    {
                        "type": "suggested_diagram",
                        "title": "5-Layer Compost Heap Cross-Section Blueprint",
                        "content": {
                            "title": "5-Layer Compost Heap Cross-Section Blueprint",
                            "caption": "Cross-sectional diagram detailing coarse stick base, carbon dry stover, nitrogen green weeds, animal dung activator, and wood ash topsoil cap."
                        }
                    },
                    {
                        "type": "step_process",
                        "title": "Standard Operating Procedure: Layering a Compost Heap",
                        "content": {
                            "title": "Step-by-Step Heap Construction",
                            "steps": [
                                "**Layer 1 (Base - 15cm)**: Lay coarse dry sticks on the ground for air ventilation (aeration) and drainage.",
                                "**Layer 2 (Carbon - 15cm)**: Add dry maize stover, wheat straw, or dry leaves to supply organic carbon.",
                                "**Layer 3 (Nitrogen - 15cm)**: Pack fresh green weeds, grass trimmings, or kitchen scraps to supply nitrogen.",
                                "**Layer 4 (Microbial Activator)**: Spread cow dung or poultry droppings to introduce active decomposing bacteria.",
                                "**Layer 5 (Top Cap & Ash)**: Sprinkle topsoil (adds microbes) and wood ash (regulates acidity and adds potassium), then sprinkle water lightly."
                            ]
                        }
                    }
                ],
                # Page 4: Aeration & Microbial Heat Management
                [
                    {
                        "type": "worked_example",
                        "title": "Microbial Dynamics: The Role of Aeration",
                        "content": {
                            "intro": "Why a compost pile must be turned with a fork jembe every 2 to 3 weeks:",
                            "steps": [
                                "**Aerobic Respiration**: Beneficial decomposer bacteria require oxygen to digest tough plant fibers.",
                                "**Heat Generation**: Active decay generates internal temperatures of 60°C to 70°C, killing weed seeds and harmful germs.",
                                "**Oxygen Depletion**: Without turning, oxygen runs out and foul-smelling anaerobic bacteria take over, slowing decay.",
                                "**Outcome**: Regular turning produces rich, dark, sweet-smelling organic manure in just 8 to 12 weeks!"
                            ]
                        }
                    }
                ],
                # Page 5: Formative Knowledge Check
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check: Composting Mechanics",
                        "content": {
                            "question": "Why is it essential to lay a 15cm base of coarse dry sticks on the ground when starting a compost heap?",
                            "options": [
                                "To provide concentrated nitrogen for the crops.",
                                "To supply wood ash and reduce the pile's acidity.",
                                "To provide bottom air circulation (aeration) and ensure proper drainage.",
                                "To prevent beneficial earthworms from entering the pile."
                            ],
                            "answer": "C",
                            "explanation": "Decomposing microbes need oxygen to thrive. A coarse stick base creates air channels beneath the pile, allowing oxygen to circulate upward and preventing water-logging."
                        }
                    }
                ],
                # Page 6: Summary & Connection Forward
                [
                    {
                        "type": "key_takeaway",
                        "title": "Lesson Summary",
                        "content": {
                            "text": "- The 3 forms of organic manure are **compost manure, farmyard manure, and green manure**.\n- **Heaps** suit wet regions, while **pits** preserve moisture in dry regions.\n- Layering order: **Coarse sticks -> Carbon dry matter -> Green nitrogen -> Dung activator -> Soil/Ash**.\n- Regular **aeration (turning)** provides oxygen, accelerating decay into dark humus."
                        }
                    },
                    {
                        "type": "transition",
                        "title": "Looking Ahead",
                        "content": {
                            "text": "Our soil is enriched with manure, but how do we protect our crops from insect pests without chemical sprays? In the next lesson, we learn how to extract botanical pesticides from neem and garlic!"
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 3: Organic Pesticides from Locally Available Materials
        # =====================================================================
        {
            "unit_order": 3,
            "unit_name": "Organic Pesticides from Locally Available Materials",
            "unit_description": "Botanical pesticide extraction, neem oil (azadirachtin), garlic sulfur spray, rabbit urine repellents, sieving techniques, and nozzle safety.",
            "lesson_title": "Organic Pesticides from Locally Available Materials",
            "pages": [
                # Page 1: Visual Hook & Learning Objectives
                [
                    {
                        "type": "suggested_image",
                        "title": "Nature's Shield: The Neem Tree (Muarubaini)",
                        "content": {
                            "title": "Nature's Shield: The Neem Tree (Muarubaini)",
                            "caption": "Fresh green neem leaves and ripe berries containing natural azadirachtin compounds that repel crop pests."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Learning Objectives: Botanical Crop Protection",
                        "content": {
                            "title": "What We Will Learn Today",
                            "goals": [
                                "Define **organic pesticides** and contrast them with synthetic chemicals.",
                                "Identify 6 natural pest repellents: **neem, garlic, chilli, marigold, rosemary, rabbit urine**.",
                                "Master the step-by-step extraction of **neem seed oil and garlic spray**.",
                                "Explain why **sieving botanical sprays** is essential to prevent sprayer nozzle clogging."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "What are Organic Pesticides?",
                        "content": {
                            "title": "Botanical Plant Defense",
                            "text": "**Organic pesticides** are natural solutions prepared from plant parts or animal wastes that repel, suppress, or eliminate crop pests without toxic chemical residues.\n\n- **Mode of Action**: Unlike synthetic chemicals that kill on contact, botanical sprays act as feeding deterrents, disrupt insect breeding cycles, or repel pests with strong odors."
                        }
                    }
                ],
                # Page 2: Local Botanical Repellent Sources
                [
                    {
                        "type": "comparison_table",
                        "title": "Botanical Pesticide Ingredients & Target Pests",
                        "content": {
                            "title": "Natural Pest Control Ingredients Matrix",
                            "headers": ["Botanical Source", "Active Natural Property", "Target Pests Controlled", "Preparation Action"],
                            "rows": [
                                ["Neem Seeds / Leaves (Muarubaini)", "Bitter Azadirachtin compound", "Aphids, caterpillars, whiteflies, mites", "Crush dried seeds, soak in water, sieve and spray"],
                                ["Garlic Bulbs", "Pungent natural sulfur odor", "Soft-bodied insects, caterpillars, beetles", "Blend into paste, steep 24 hours in water, sieve"],
                                ["Chilli Pepper", "Sharp Capsaicin heat compound", "Chewing pests, leaf-eating caterpillars", "Crush pods, steep in warm water, filter carefully"],
                                ["Mexican Marigold", "Strong essential aromatic oils", "Aphids, nematodes, garden flies", "Chop foliage, boil or soak, strain liquid"],
                                ["Rabbit Urine", "Strong ammonia & concentrated nitrogen", "Aphids, leaf miners (plus foliar feeding)", "Dilute 1:5 with clean water before spraying"]
                            ]
                        }
                    }
                ],
                # Page 3: Preparation Workflows: Neem & Garlic Sprays
                [
                    {
                        "type": "suggested_diagram",
                        "title": "5-Stage Botanical Garlic & Neem Pesticide Extraction Workflow",
                        "content": {
                            "title": "5-Stage Botanical Garlic & Neem Pesticide Extraction Workflow",
                            "caption": "Step-by-step extraction flowchart showing Collect/Peel, Blend/Crush, 24-Hour Steeping, Cloth Sieving, and Nozzle Spraying."
                        }
                    },
                    {
                        "type": "step_process",
                        "title": "Standard Operating Procedure: Preparing Garlic Spray",
                        "content": {
                            "title": "Garlic Extraction Protocol",
                            "steps": [
                                "**1. Blending**: Grind or blend fresh garlic cloves into a smooth, fine paste.",
                                "**2. Mixing**: Add warm water to the paste and stir thoroughly in a clean jar.",
                                "**3. 24-Hour Steeping**: Cover and place the jar in a warm spot for 24 hours to activate pungent sulfur compounds.",
                                "**4. Fine Sieving**: Pour the liquid through a clean cotton cloth or fine sieve to filter out all solid particles.",
                                "**5. Application**: Pour the clear liquid into a spray bottle and spray directly on crop leaves early in the morning or late in the evening."
                            ]
                        }
                    }
                ],
                # Page 4: Equipment Maintenance & Sieving Safety
                [
                    {
                        "type": "callout",
                        "title": "Crucial Sprayer Maintenance Rule",
                        "content": {
                            "title": "Always Filter Botanical Liquids!",
                            "text": "Unfiltered plant fibers or crushed seed particles will instantly clog the tiny nozzle of your hand sprayer, making it impossible to spray. Always pour botanical solutions through a fine cloth filter before filling spray tanks!"
                        }
                    }
                ],
                # Page 5: Formative Knowledge Check
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check: Botanical Extraction",
                        "content": {
                            "question": "Why is it mandatory to sieve botanical extracts through a fine cloth before pouring them into a spray bottle?",
                            "options": [
                                "To make sure the organic pesticide smells pleasant for humans.",
                                "To remove solid plant fibers that would clog the fine nozzle of the sprayer.",
                                "To dilute the chemical strength so it doesn't kill beneficial birds.",
                                "To remove all water from the mixture."
                            ],
                            "answer": "B",
                            "explanation": "Botanical sprays contain plant pulp and fibers. Sifting through a fine cloth or sieve removes these solids, ensuring the sprayer nozzle operates smoothly without clogging."
                        }
                    }
                ],
                # Page 6: Summary & Connection Forward
                [
                    {
                        "type": "key_takeaway",
                        "title": "Lesson Summary",
                        "content": {
                            "text": "- **Organic pesticides** use natural plant extracts to repel and manage crop pests.\n- Common ingredients include **neem seeds, garlic cloves, chilli peppers, and marigold**.\n- Garlic spray requires **24 hours of steeping** to activate natural sulfur compounds.\n- Always **filter botanical sprays** through a fine sieve to protect spray equipment."
                        }
                    },
                    {
                        "type": "transition",
                        "title": "Looking Ahead",
                        "content": {
                            "text": "How do we manage weeds without chemicals, and how do we feed crops directly through their leaves? In the next lesson, we explore mechanical weeding and prepare organic foliar teas!"
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 4: Mechanical Weed Control and Organic Foliar Feed
        # =====================================================================
        {
            "unit_order": 4,
            "unit_name": "Mechanical Weed Control and Organic Foliar Feed",
            "unit_description": "Mechanical weed control (tillage, slashing, uprooting, mulching), leaf stomata absorption, 1:10 manure tea dilution, and Mexican sunflower fermentation.",
            "lesson_title": "Mechanical Weed Control and Organic Foliar Feed",
            "pages": [
                # Page 1: Visual Hook & Learning Objectives
                [
                    {
                        "type": "suggested_image",
                        "title": "Physical Protection: Mulching & Mechanical Care",
                        "content": {
                            "title": "Physical Protection: Mulching & Mechanical Care",
                            "caption": "A neatly mulched vegetable bed with golden dry grass blocking weeds and conserving soil moisture around young crop stems."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Learning Objectives: Weeding & Foliar Feeding",
                        "content": {
                            "title": "What We Will Learn Today",
                            "goals": [
                                "Identify the 4 mechanical weed control methods: **tillage, slashing, uprooting, mulching**.",
                                "Explain how crop leaves absorb liquid nutrients through **stomata pores**.",
                                "Master the critical **1:10 dilution ratio** for animal manure foliar tea.",
                                "Describe the **7-14 day fermentation protocol** for Mexican sunflower green tea."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The 4 Mechanical Weed Control Methods",
                        "content": {
                            "title": "Physical Weeding Without Herbicides",
                            "text": "- **1. Tillage (Cultivation)**: Loosening soil with hand hoes to disrupt weed roots and expose them to drying sun.\n- **2. Slashing**: Cutting tall weeds with pangas or slashers to prevent flowering and seed scattering.\n- **3. Uprooting (Hand Pulling)**: Manually pulling weeds out by the roots in small vegetable beds.\n- **4. Mulching**: Covering bare soil with dry straw or grass to smother weed shoots and block sunlight."
                        }
                    }
                ],
                # Page 2: What is Organic Foliar Feed?
                [
                    {
                        "type": "concept_explanation",
                        "title": "Direct Leaf Feeding Through Stomata",
                        "content": {
                            "title": "Instant Nutrient Uptake",
                            "text": "- **Microscopic Stomata**: The undersides of crop leaves contain thousands of tiny pores called **stomata** that breathe and absorb dissolved moisture.\n- **Rapid Absorption**: Spraying liquid foliar tea onto leaves delivers immediate nitrogen and potassium directly into plant tissues, turning yellow leaves green in days!\n- **Cool-Hours Rule**: Spray ONLY in the cool morning (before 9:00 AM) or evening (after 4:30 PM). Stomata close during midday heat to prevent water loss!"
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Microscopic Leaf Stomata Absorption & 1:10 Dilution Blueprint",
                        "content": {
                            "title": "Microscopic Leaf Stomata Absorption & 1:10 Dilution Blueprint",
                            "caption": "Diagram illustrating open leaf stomata absorbing nutrients, alongside the 1:10 foliar dilution ratio and morning/evening spraying clocks."
                        }
                    }
                ],
                # Page 3: Preparation Protocols: Manure Tea & Mexican Sunflower Tea
                [
                    {
                        "type": "step_process",
                        "title": "Standard Operating Procedure: Animal Manure Foliar Tea",
                        "content": {
                            "title": "Manure Tea Preparation & 1:10 Dilution",
                            "steps": [
                                "**1. Manure Bag Soaking**: Place dry sheep, goat, or poultry manure in a porous sack and submerge in a bucket of water for several hours.",
                                "**2. Extraction & Sieving**: Squeeze the sack and filter the dark brown liquid through a clean cloth.",
                                "**3. The Golden 1:10 Dilution Rule**: Mix **1 liter of raw manure tea with 10 liters of clean water** (1:10 ratio). Undiluted tea will chemically burn and scorch leaves!",
                                "**4. Application**: Spray top and bottom leaf surfaces during cool morning or evening hours."
                            ]
                        }
                    },
                    {
                        "type": "step_process",
                        "title": "Standard Operating Procedure: Mexican Sunflower Green Tea",
                        "content": {
                            "title": "Tithonia Fermentation Protocol",
                            "steps": [
                                "**1. Harvesting**: Harvest 1/2 kg of fresh, succulent Mexican sunflower (Tithonia) leaves.",
                                "**2. Submerging**: Chop leaves and submerge completely in 5 liters of water in a covered plastic container.",
                                "**3. 7 to 14-Day Fermentation**: Keep container covered; stir the mixture daily with a stick.",
                                "**4. Completion Check**: Fermentation is complete when surface bubbling stops and liquid turns dark green.",
                                "**5. Sieving & Spraying**: Filter liquid through a cloth, dilute with water, and spray onto crops."
                            ]
                        }
                    }
                ],
                # Page 4: Common Mistakes: Dilution & Timing Errors
                [
                    {
                        "type": "common_mistake",
                        "title": "Critical Foliar Feeding Mistakes",
                        "content": {
                            "text": "- **Mistake 1: Spraying at Midday**: Under hot direct sun, stomata are closed and water droplets focus sunlight like magnifying lenses, baking and blistering leaf tissues.\n- **Mistake 2: Undiluted Application**: Raw manure liquid contains excessive nitrogen salts that cause severe chemical leaf scorch. Always dilute 1:10!"
                        }
                    }
                ],
                # Page 5: Formative Knowledge Check
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check: Foliar Dilution",
                        "content": {
                            "question": "Why must animal manure foliar tea be diluted with clean water at a 1:10 ratio before being sprayed on crop leaves?",
                            "options": [
                                "To ensure there is enough liquid volume to wash dust off the entire farm.",
                                "To prevent high nutrient concentrations from chemically scorching and burning the crop leaves.",
                                "To make the foliar feed taste sweet for pollinating bees.",
                                "To kill weed seeds on the ground."
                            ],
                            "answer": "B",
                            "explanation": "Concentrated manure tea is extremely high in nitrogen. Applying it raw causes severe chemical fertilizer scorch on delicate leaves. Diluting 1 part tea with 10 parts water ensures safe, rapid leaf absorption."
                        }
                    }
                ],
                # Page 6: Summary & Connection Forward
                [
                    {
                        "type": "key_takeaway",
                        "title": "Lesson Summary",
                        "content": {
                            "text": "- Mechanical weed control includes **tillage, slashing, uprooting, and dry mulching**.\n- **Foliar feed** is absorbed instantly through microscopic **leaf stomata**.\n- Manure tea requires a **1:10 dilution ratio** with clean water.\n- Mexican sunflower tea requires **7 to 14 days of fermentation** with daily stirring.\n- Spray ONLY during **cool morning or evening hours** when stomata are open."
                        }
                    },
                    {
                        "type": "transition",
                        "title": "Looking Ahead",
                        "content": {
                            "text": "How do we coordinate all these tasks into a daily, organized farm routine? In the next lesson, we establish a weekly garden maintenance schedule and learn how to troubleshoot crop stress!"
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 5: Maintenance of Crops in an Organic Garden
        # =====================================================================
        {
            "unit_order": 5,
            "unit_name": "Maintenance of Crops in an Organic Garden",
            "unit_description": "Routine maintenance practices (watering, weeding, aerating, pest monitoring), weekly maintenance schedule, and crop symptom troubleshooting matrix.",
            "lesson_title": "Maintenance of Crops in an Organic Garden",
            "pages": [
                # Page 1: Visual Hook & Learning Objectives
                [
                    {
                        "type": "suggested_image",
                        "title": "Active Stewardship: Daily Crop Monitoring",
                        "content": {
                            "title": "Active Stewardship: Daily Crop Monitoring",
                            "caption": "Students working collaboratively in a school garden, inspecting crop leaves for pests and managing soil moisture."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Learning Objectives: Crop Maintenance Systems",
                        "content": {
                            "title": "What We Will Learn Today",
                            "goals": [
                                "List the 5 primary organic maintenance practices: **watering, weeding, aerating, foliar feeding, pest monitoring**.",
                                "Explain why daily underside leaf inspection is critical for pest detection.",
                                "Draft a structured **Weekly Garden Maintenance Schedule**.",
                                "Troubleshoot common crop symptoms (yellowing, wilting, curling) with organic solutions."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The Need for Continuous Care",
                        "content": {
                            "title": "Farming is a Daily Habit",
                            "text": "Planting seeds is only the beginning! An organic garden thrives only when cared for with regular, structured daily habits. Consistent watering, weed removal, and early pest spotting prevent problems before crops suffer permanent damage."
                        }
                    }
                ],
                # Page 2: The 5 Core Routine Maintenance Tasks
                [
                    {
                        "type": "step_process",
                        "title": "Core Daily & Weekly Maintenance Tasks",
                        "content": {
                            "title": "The 5 Maintenance Practices",
                            "steps": [
                                "**1. Timely Watering**: Water early in the morning or late in the evening to keep soil moist while minimizing evaporation.",
                                "**2. Continuous Weeding**: Pull out emerging weeds by hand or hoe, and maintain a thick dry grass mulch layer.",
                                "**3. Soil Aeration**: Lightly cultivate the topsoil with a hand fork to break soil crusts and let air reach roots.",
                                "**4. Bi-Weekly Foliar Feeding**: Spray diluted (1:10) manure or botanical tea every 14 days for steady trace minerals.",
                                "**5. Underside Leaf Inspection**: Check beneath leaves daily where aphids, caterpillars, and fungal spores hide."
                            ]
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Weekly Garden Maintenance Schedule & Plant Symptom Matrix",
                        "content": {
                            "title": "Weekly Garden Maintenance Schedule & Plant Symptom Matrix",
                            "caption": "Diagram mapping daily team responsibilities (Mon-Sun) alongside a crop symptom diagnostic matrix."
                        }
                    }
                ],
                # Page 3: The Weekly Maintenance Schedule & Diagnostic Matrix
                [
                    {
                        "type": "comparison_table",
                        "title": "Crop Stress Symptom & Organic Remedy Matrix",
                        "content": {
                            "title": "Crop Troubleshooting Guide",
                            "headers": ["Observed Crop Symptom", "Biological Cause", "Corrective Organic Action"],
                            "rows": [
                                ["Yellowing lower leaves, stunted stems", "Nitrogen deficiency or weed root competition", "Weed bed manually and apply diluted 1:10 manure foliar tea"],
                                ["Wilting leaves, hard cracked topsoil", "Severe water stress and dry soil", "Water early in the morning and apply thick dry grass mulch"],
                                ["Tiny green insects clustered under leaves", "Aphid infestation", "Spray homemade botanical neem oil or garlic repellent immediately"],
                                ["White powdery coating on leaf surfaces", "Fungal powdery mildew infection", "Improve air circulation, thin crowded leaves, spray marigold extract"]
                            ]
                        }
                    }
                ],
                # Page 4: Team Accountability in School Farm Projects
                [
                    {
                        "type": "worked_example",
                        "title": "Project Management: The Rotating Roster",
                        "content": {
                            "intro": "Why group work requires clear individual roles:",
                            "steps": [
                                "**The Pitfall of Shared Blame**: If 'everyone' is responsible for watering, no one does it, and seedlings die over the weekend.",
                                "**The Solution**: Form 4 dedicated teams: Team A (Watering), Team B (Weeding & Soil), Team C (Pest Monitoring), Team D (Foliar Prep).",
                                "**Rotation**: Teams rotate duties weekly so every learner masters all practical field skills!",
                                "**Result**: 100% crop survival and fair, shared team accountability."
                            ]
                        }
                    }
                ],
                # Page 5: Formative Knowledge Check
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check: Team Scheduling",
                        "content": {
                            "question": "Why is setting up a structured weekly maintenance schedule with rotating team roles essential for school farm projects?",
                            "options": [
                                "To allow some students to skip field work entirely.",
                                "To ensure daily tasks like watering and pest checking are never forgotten, guaranteeing crop survival.",
                                "To make synthetic chemical fertilizers without teacher supervision.",
                                "To reduce the amount of compost needed in the garden bed."
                            ],
                            "answer": "B",
                            "explanation": "Crops require continuous daily care. A structured schedule assigns clear accountability, ensuring watering, weeding, and pest monitoring occur reliably without gaps."
                        }
                    }
                ],
                # Page 6: Summary & Connection Forward
                [
                    {
                        "type": "key_takeaway",
                        "title": "Lesson Summary",
                        "content": {
                            "text": "- Daily maintenance includes **watering, weeding, aerating, feeding, and monitoring**.\n- Inspect the **undersides of leaves** where insect pests conceal themselves.\n- Use the **symptom-cause matrix** to apply targeted organic remedies.\n- **Rotating team schedules** ensure consistent care and full practical learning."
                        }
                    },
                    {
                        "type": "transition",
                        "title": "Looking Ahead",
                        "content": {
                            "text": "We are ready to start our practical school garden project! In the next lesson, we select our short-season crop and prepare our raised farm bed using manual agricultural tools!"
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 6: Selecting a Short-Season Crop & Farm Plot Preparation
        # =====================================================================
        {
            "unit_order": 6,
            "unit_name": "Selecting a Short-Season Crop & Farm Plot Preparation",
            "unit_description": "Short-season crop selection (radishes, lettuce, beans, peas), site selection, peg-and-string demarcation, tilling, clod breaking, and 1m raised bed construction.",
            "lesson_title": "Selecting a Short-Season Crop & Farm Plot Preparation",
            "pages": [
                # Page 1: Visual Hook & Learning Objectives
                [
                    {
                        "type": "suggested_image",
                        "title": "Fast-Growing Greens: The Raised Crop Bed",
                        "content": {
                            "title": "Fast-Growing Greens: The Raised Crop Bed",
                            "caption": "Young green lettuce and radish seedlings flourishing in straight, neat rows across an elevated organic raised bed."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Learning Objectives: Crop Selection & Bed Preparation",
                        "content": {
                            "title": "What We Will Accomplish Today",
                            "goals": [
                                "Identify 4 short-season crops: **radishes (4 wks), lettuce (6-8 wks), beans (8-10 wks), peas (10-12 wks)**.",
                                "Evaluate 5 selection factors: duration, climate, soil fertility, water availability, team goals.",
                                "Demarcate and construct a **1-meter wide raised agricultural bed**.",
                                "Apply essential farm safety rules regarding gumboots, gloves, and tool handling."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "What is a Short-Season Crop?",
                        "content": {
                            "title": "Fast Harvest for School Terms",
                            "text": "A **short-season crop** is an agricultural crop that completes its growth cycle from seed to harvest within 4 to 12 weeks. They are perfect for school terms, allowing learners to prepare the plot, sow seeds, manage growth, and harvest produce before vacation!"
                        }
                    }
                ],
                # Page 2: Short-Season Crop Selection Matrix
                [
                    {
                        "type": "comparison_table",
                        "title": "Short-Season Crops Profile Matrix",
                        "content": {
                            "title": "Crop Duration & Characteristics Guide",
                            "headers": ["Crop Variety", "Maturity Duration", "Soil & Climate Requirements", "Key Practical Benefit"],
                            "rows": [
                                ["Radishes", "4 weeks (Fastest!)", "Loose sandy-loam soil, moderate moisture", "Produces crunchy edible roots in just 1 month"],
                                ["Lettuce", "6 to 8 weeks", "Fertile compost-rich soil, regular watering", "High-value leafy green with high market demand"],
                                ["French Beans", "8 to 10 weeks", "Warm climate, well-drained soil", "Legume that fixes natural nitrogen into the bed"],
                                ["Garden Peas", "10 to 12 weeks", "Cool climate, trellis support needed", "Produces sweet edible pods and protein-rich vines"]
                            ]
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "1-Meter Raised Agricultural Bed Dimensional Blueprint",
                        "content": {
                            "title": "1-Meter Raised Agricultural Bed Dimensional Blueprint",
                            "caption": "Engineering layout showing a 1m wide by 3m long by 15cm high raised bed with demarcation string and tool positions."
                        }
                    }
                ],
                # Page 3: Step-by-Step Raised Bed Construction
                [
                    {
                        "type": "step_process",
                        "title": "Standard Operating Procedure: Farm Plot Preparation",
                        "content": {
                            "title": "Step-by-Step Bed Construction",
                            "steps": [
                                "**1. Site Selection**: Choose a sunny, well-drained area with access to a water tank.",
                                "**2. Peg & String Demarcation**: Measure a 1m wide by 3m long rectangle using tape and string line.",
                                "**3. Debris Clearing**: Clear away weeds, rocks, glass, and roots with slashers and rakes.",
                                "**4. Primary Tilling**: Dig the soil 20-30cm deep with a jembe (hoe) to invert and loosen the subsoil.",
                                "**5. Clod Breaking**: Break large soil lumps into fine, crumbly soil using a fork jembe or rake.",
                                "**6. Shaping Raised Bed**: Pull soil toward the center to build an elevated mound (15cm high, 1m wide)."
                            ]
                        }
                    },
                    {
                        "type": "callout",
                        "title": "The Golden 1-Meter Width Rule",
                        "content": {
                            "title": "Why Beds Must Be Exactly 1 Meter Wide!",
                            "text": "A width of exactly 1 meter allows students on either side to reach the middle of the bed comfortably to weed and water without ever stepping on the bed and compacting the loose root soil!"
                        }
                    }
                ],
                # Page 4: Safety Protocols During Plot Preparation
                [
                    {
                        "type": "worked_example",
                        "title": "Farm Safety Standards: Tool Handling & PPE",
                        "content": {
                            "intro": "Critical safety guidelines when working on the school farm plot:",
                            "steps": [
                                "**Personal Protective Equipment (PPE)**: Always wear gumboots to protect against sharp stones/thorns and gloves to prevent blisters.",
                                "**Tool Spacing**: Maintain a safe distance of at least 2 meters from any classmate swinging a jembe or slasher.",
                                "**Tool Storage**: Never leave sharp rakes or jembes facing upward on the ground; store tools in the farm shed after work."
                            ]
                        }
                    }
                ],
                # Page 5: Formative Knowledge Check
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check: Bed Dimensions",
                        "content": {
                            "question": "Why is a bed width of exactly 1 meter recommended when constructing vegetable plots on a school farm?",
                            "options": [
                                "Because 1 meter is the maximum size allowed by agricultural laws.",
                                "It allows students to reach the center of the bed from either side without stepping on and compacting the cultivated soil.",
                                "Because weeds are unable to grow on beds that are exactly 1 meter wide.",
                                "To prevent strong winds from blowing away crop seeds."
                            ],
                            "answer": "B",
                            "explanation": "Stepping on cultivated soil crushes air pockets and hardens the ground around roots. A 1-meter wide bed allows students to reach the middle from the side pathways without stepping on the soil."
                        }
                    }
                ],
                # Page 6: Summary & Connection Forward
                [
                    {
                        "type": "key_takeaway",
                        "title": "Lesson Summary",
                        "content": {
                            "text": "- **Short-season crops (radishes, lettuce, beans, peas)** mature within 4 to 12 weeks.\n- Choose crops based on **growth duration, climate, soil, and water availability**.\n- Preparation steps: **Site selection -> Demarcation -> Clearing -> Tilling -> Clod breaking -> Raised bed shaping**.\n- Maintain a **1-meter bed width** to prevent soil compaction and ensure easy maintenance."
                        }
                    },
                    {
                        "type": "transition",
                        "title": "Looking Ahead",
                        "content": {
                            "text": "Our bed is shaped, leveled, and ready! In the next lesson, we get our hands in the soil to sow seeds at precise depths and spacings with row compost enrichment!"
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 7: Practical Crop Establishment (Planting)
        # =====================================================================
        {
            "unit_order": 7,
            "unit_name": "Practical Crop Establishment (Planting)",
            "unit_description": "Straight row planting, sowing depth rule (2-3x thickness), crop spacing targets, row compost enrichment, and gentle rose-nozzle initial watering.",
            "lesson_title": "Practical Crop Establishment (Planting)",
            "pages": [
                # Page 1: Visual Hook & Learning Objectives
                [
                    {
                        "type": "suggested_image",
                        "title": "Precision Sowing: Straight Furrow Rows",
                        "content": {
                            "title": "Precision Sowing: Straight Furrow Rows",
                            "caption": "Hands carefully drawing a shallow seed furrow along a string line and sprinkling crumbly compost before sowing seeds."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Learning Objectives: Seed Sowing & Establishment",
                        "content": {
                            "title": "What We Will Accomplish Today",
                            "goals": [
                                "Sow short-season seeds in straight, measured rows across a raised bed.",
                                "Apply the **sowing depth rule: 2 to 3 times seed thickness**.",
                                "Master crop spacing: **Radishes (5cm), Lettuce (15cm), Beans (10-15cm)**.",
                                "Apply compost directly in furrows and water gently with a fine rose nozzle."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Why Row Planting is Mandatory",
                        "content": {
                            "title": "Orderly Crop Establishment",
                            "text": "Instead of scattering seeds randomly (broadcasting), organic gardeners always sow in straight, measured rows:\n\n- **Uniform Sunlight & Air**: Prevents crowding so every plant receives equal sunlight.\n- **Easy Weeding & Mulching**: Clear pathways between rows allow easy hoeing and mulch application without damaging crops."
                        }
                    }
                ],
                # Page 2: Spacing & Sowing Depth Guidelines
                [
                    {
                        "type": "comparison_table",
                        "title": "Crop Sowing Depth & Spacing Target Matrix",
                        "content": {
                            "title": "Crop Spacing & Depth Specifications",
                            "headers": ["Crop Variety", "Sowing Depth", "Intra-Row Spacing (Plant-to-Plant)", "Inter-Row Spacing (Row-to-Row)"],
                            "rows": [
                                ["Radish Seeds", "1.0 cm (Shallow)", "5 cm apart", "20 cm between rows"],
                                ["Lettuce Seeds", "0.5 cm (Very Shallow)", "15 cm apart", "30 cm between rows"],
                                ["French Beans", "2.5 cm to 3.0 cm", "10 cm to 15 cm apart", "45 cm between rows"],
                                ["Garden Peas", "3.0 cm", "10 cm apart", "40 cm between rows"]
                            ]
                        }
                    },
                    {
                        "type": "callout",
                        "title": "The Golden Sowing Depth Rule",
                        "content": {
                            "title": "Depth = 2 to 3 Times Seed Thickness!",
                            "text": "Burying a seed too deep causes the seedling to exhaust its stored food reserves before reaching the surface. Sowing too shallow exposes the seed to drying winds and birds. Always bury seeds 2 to 3 times their thickness!"
                        }
                    }
                ],
                # Page 3: Step-by-Step Sowing Procedure
                [
                    {
                        "type": "suggested_diagram",
                        "title": "5-Step Row Planting & Furrow Sowing Workflow",
                        "content": {
                            "title": "5-Step Row Planting & Furrow Sowing Workflow",
                            "caption": "Sequential diagram showing String Demarcation, Furrow Drawing, Compost Sprinkling, Seed Placement, and Gentle Rose Watering."
                        }
                    },
                    {
                        "type": "step_process",
                        "title": "Standard Operating Procedure: Seed Sowing",
                        "content": {
                            "title": "Step-by-Step Planting Protocol",
                            "steps": [
                                "**1. Stretch Demarcation Line**: Stretch peg and string tightly across the bed to mark straight rows.",
                                "**2. Draw Shallow Furrow**: Use a pointed wooden stick to draw a straight groove along the string.",
                                "**3. Sprinkle Compost**: Spread a thin layer of decomposed compost manure along the furrow floor to nourish roots.",
                                "**4. Place Seeds**: Space seeds precisely according to crop spacing rules (e.g. 5cm for radishes).",
                                "**5. Cover & Press**: Cover with loose topsoil and press down lightly with fingertips to ensure seed-to-soil contact.",
                                "**6. Gentle Rose Watering**: Water the bed using a watering can fitted with a fine rose nozzle."
                            ]
                        }
                    }
                ],
                # Page 4: Critical Watering Precautions
                [
                    {
                        "type": "common_mistake",
                        "title": "Dangerous Initial Watering Error",
                        "content": {
                            "text": "NEVER pour water forcefully from a bucket or hose pipe onto newly planted seedbeds! The heavy water torrent will wash away the loose topsoil, displacing and exposing your seeds. Always use a watering can with a fine rose nozzle that splits water into a gentle rain."
                        }
                    }
                ],
                # Page 5: Formative Knowledge Check
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check: Sowing Depth",
                        "content": {
                            "question": "Based on the fundamental agricultural planting depth rule, how deep should short-season crop seeds be buried in the soil?",
                            "options": [
                                "At least 15cm deep to keep them completely dark.",
                                "Scattered on top of dry straw without any soil cover.",
                                "At a depth equal to 2 to 3 times the thickness of the seed itself.",
                                "Pushed down into the subsoil until they touch the hard pan."
                            ],
                            "answer": "C",
                            "explanation": "The standard agronomic rule is to bury seeds at a depth equal to 2 to 3 times their thickness. Sowing deeper prevents shoot emergence, while sowing shallower causes seeds to dry out."
                        }
                    }
                ],
                # Page 6: Summary & Connection Forward
                [
                    {
                        "type": "key_takeaway",
                        "title": "Lesson Summary",
                        "content": {
                            "text": "- **Row planting** ensures even sunlight, air circulation, and easy maintenance.\n- Plant seeds at a depth of **2 to 3 times seed thickness**.\n- Enrich row trenches with **decomposed compost manure** before sowing.\n- Water newly sown seedbeds **gently with a fine rose-nozzle watering can**."
                        }
                    },
                    {
                        "type": "transition",
                        "title": "Looking Ahead",
                        "content": {
                            "text": "Our crops are sown and watered! In our final lesson, we learn how to manage long-term plot maintenance, keep daily observation journals, and complete the Topic Capstone Assessment!"
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 8: Planting and Maintaining the Selected Crop & Capstone
        # =====================================================================
        {
            "unit_order": 8,
            "unit_name": "Planting and Maintaining the Selected Short-Season Crop",
            "unit_description": "Active growth phase care, shared stewardship, garden journal tracking, video review of Kenyan school farm, and 10 topic summative MCQs.",
            "lesson_title": "Planting and Maintaining the Selected Short-Season Crop & Capstone",
            "pages": [
                # Page 1: Visual Hook & Practical Objectives
                [
                    {
                        "type": "suggested_image",
                        "title": "Shared Stewardship: The Thriving School Plot",
                        "content": {
                            "title": "Shared Stewardship: The Thriving School Plot",
                            "caption": "Students working cooperatively around lush green vegetable beds, watering plants, adding mulch, and recording data in journals."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Learning Objectives: Plot Maintenance & Capstone",
                        "content": {
                            "title": "What We Will Accomplish Today",
                            "goals": [
                                "Manage an active short-season crop through its seedling, vegetative, and flowering stages.",
                                "Keep a **Daily Garden Journal** tracking stem height, leaf color, soil moisture, and inputs.",
                                "Review a real-world video of Kenyan school garden projects.",
                                "Demonstrate complete curriculum mastery by passing the **Topic Summative Assessment**."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The Power of Shared Stewardship",
                        "content": {
                            "title": "Teamwork in Agriculture",
                            "text": "A thriving school farm plot is built on collaborative teamwork. Dividing duties into morning watering, midday pest inspection, and evening weeding ensures crops remain protected from environmental stress every single day!"
                        }
                    }
                ],
                # Page 2: Keeping a Daily Garden Journal
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Daily Garden Observation Journal & Collaborative Stewardship Cycle",
                        "content": {
                            "title": "Daily Garden Observation Journal & Collaborative Stewardship Cycle",
                            "caption": "Diagram detailing garden journal tracking columns (Height, Leaf Health, Soil Moisture, Tasks) alongside the 3-team daily care rotation."
                        }
                    },
                    {
                        "type": "comparison_table",
                        "title": "Sample Daily Garden Journal Log Template",
                        "content": {
                            "title": "Weekly Observation Log Example",
                            "headers": ["Project Week", "Average Crop Height", "Leaf & Pest Health Observations", "Maintenance Action Executed"],
                            "rows": [
                                ["Week 1 (Sprouts)", "2.5 cm", "Tiny green shoots emerging evenly; zero pests observed", "Gentle morning rose-nozzle watering; bed damp"],
                                ["Week 3 (Vegetative)", "11.0 cm", "Dark green leaves; 3 caterpillars spotted on leaf margin", "Hand-picked caterpillars; sprayed fresh botanical garlic extract"],
                                ["Week 5 (Flowering)", "26.0 cm", "Pale yellow veins on lower leaves; soil surface dry", "Weeded bed; applied dry grass mulch; sprayed 1:10 foliar tea"],
                                ["Week 7 (Maturity)", "32.0 cm", "Succulent, crisp, healthy heads ready for harvest", "Harvested fresh chemical-free produce for school meal!"]
                            ]
                        }
                    }
                ],
                # Page 3: Dynamic Crop Care Decision Protocol
                [
                    {
                        "type": "step_process",
                        "title": "Standard Operating Procedure: Dynamic Organic Care",
                        "content": {
                            "title": "Troubleshooting Field Problems",
                            "steps": [
                                "**If Soil is Dry**: Water immediately in the morning and reinforce the dry grass mulch layer to block evaporation.",
                                "**If Weeds Emerge**: Perform shallow weeding with a hand fork or hand-pull weeds before they flower.",
                                "**If Leaves Yellow**: Apply diluted (1:10) manure tea in the evening to supply rapid nitrogen.",
                                "**If Pests Appear**: Sieve and spray botanical neem seed oil or garlic repellent immediately in the evening."
                            ]
                        }
                    }
                ],
                # Page 4: Teamwork & Field Reflection
                [
                    {
                        "type": "mini_activity",
                        "title": "Field Reflection & Group Presentation",
                        "content": {
                            "title": "Presenting Your Plot Results",
                            "instruction": "Review your group's garden journal. Present your crop growth chart to the class: explain what botanical sprays you used, how you handled weed competition, and how your team shared watering responsibilities!"
                        }
                    }
                ],
                # Page 5: Formative Knowledge Check & Topic Master Summary
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check: Evening Spraying Timing",
                        "content": {
                            "question": "Why should organic botanical pest repellents and foliar feeds be sprayed on crop leaves during the cool evening rather than during the hot midday sun?",
                            "options": [
                                "Because insect pests only feed in total darkness.",
                                "Midday heat closes leaf stomata to prevent water loss, and intense sunlight on wet leaves causes severe heat scorch.",
                                "Because students are legally forbidden from entering garden beds during daytime hours.",
                                "To prevent weed seeds from germinating in the furrow."
                            ],
                            "answer": "B",
                            "explanation": "Leaf stomata close during hot midday hours to prevent water loss. Spraying in the cool evening ensures open stomata for nutrient absorption and prevents direct sun rays from baking wet leaf surfaces."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Topic 4 Master Summary: Sustainable Organic Gardening",
                        "content": {
                            "text": "- **Organic gardening** produces nutritious, chemical-free food while protecting living soil biodiversity.\n- **Composting and animal manure** provide free, long-term soil structure and moisture retention.\n- **Botanical sprays (neem, garlic)** manage pests safely without toxic chemical residues.\n- **Mechanical weeding, row planting, and 1m raised beds** optimize root health and labor efficiency."
                        }
                    }
                ],
                # Page 6: Topic Video Review
                [
                    {
                        "type": "suggested_video",
                        "title": "Topic Video Review: Mixed Organic Farming Explained",
                        "content": {
                            "title": "Topic Video Review: Mixed Organic Farming Explained",
                            "url": "https://www.youtube.com/watch?v=Ei5z_0Lxmic",
                            "resolved_video_id": "Ei5z_0Lxmic",
                            "caption": "Watch this comprehensive CBC Grade 9 Agriculture lesson explaining mixed organic farming systems, composting, soil conservation, and biological pest control in Kenya."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Key Things to Observe in the Video",
                        "content": {
                            "title": "Focus Questions for Video Reflection",
                            "text": "- **1. Natural Soil Care**: Observe how organic compost restores crumbly humus to depleted soils.\n- **2. Safe Pest Defense**: Notice how botanical extracts are prepared and applied without toxic hazards.\n- **3. Crop Diversity**: Note the intercropping of legumes with leafy vegetables to maintain natural fertility."
                        }
                    }
                ],
                # Page 7: Topic Assessment Part 1 (Questions 1 to 2)
                [
                    {
                        "type": "knowledge_check",
                        "title": "Topic Assessment - Question 1: Forbidden Inputs",
                        "content": {
                            "question": "A student wants to establish an organic garden bed of lettuce. Which of the following inputs is completely forbidden in their organic garden?",
                            "options": [
                                "Decomposed chicken droppings.",
                                "Botanical neem seed oil spray.",
                                "Manufactured synthetic chemical weed-killer (herbicide).",
                                "Dry grass straw mulch."
                            ],
                            "answer": "C",
                            "explanation": "Organic gardening strictly prohibits manufactured synthetic chemical weed-killers (herbicides), chemical fertilizers, and toxic pesticides. Compost, neem oil, and organic grass mulches are natural, permitted inputs."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Topic Assessment - Question 2: Farmyard Manure Definition",
                        "content": {
                            "question": "Which form of organic manure is made specifically from livestock beddings (like straw or hay) mixed with animal droppings and urine in animal shelters?",
                            "options": [
                                "Green manure.",
                                "Compost manure.",
                                "Farmyard manure.",
                                "Liquid foliar manure."
                            ],
                            "answer": "C",
                            "explanation": "Farmyard manure is prepared specifically from animal bedding (straw or hay) that has absorbed livestock urine and dung in animal pens. Green manure is plowed living legumes, and compost is piled mixed organic wastes."
                        }
                    }
                ],
                # Page 8: Topic Assessment Part 2 (Questions 3 to 5)
                [
                    {
                        "type": "knowledge_check",
                        "title": "Topic Assessment - Question 3: Compost Base Layer",
                        "content": {
                            "question": "When constructing a layered compost heap, what is the biological purpose of laying a 15cm base of coarse dry sticks on the ground first?",
                            "options": [
                                "To supply high levels of nitrogen to feed the crops.",
                                "To add wood ash and reduce the pile's acidity.",
                                "To provide bottom air circulation (aeration) and ensure proper drainage.",
                                "To prevent beneficial earthworms from entering the pile."
                            ],
                            "answer": "C",
                            "explanation": "Decomposing microbes require oxygen (aeration). A base layer of coarse sticks creates air channels beneath the heap, allowing air to circulate from below and preventing water-logging."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Topic Assessment - Question 4: Garlic Spray Preparation",
                        "content": {
                            "question": "What is the correct procedure for preparing a natural pest repellent spray from fresh kitchen garlic bulbs?",
                            "options": [
                                "Boil whole garlic bulbs in water for three days, then spray immediately.",
                                "Blend bulbs into a fine paste, mix with warm water, steep in a warm place for 24 hours, and sieve before spraying.",
                                "Soak whole bulbs in cold water for 10 minutes and scatter them around the garden bed.",
                                "Mix raw garlic paste with synthetic chemical weed-killer and apply at midday."
                            ],
                            "answer": "B",
                            "explanation": "Garlic spray is prepared by blending cloves into a paste, mixing with warm water, steeping for 24 hours to activate natural pungent sulfur compounds, and sieving through a cloth to prevent nozzle clogging."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Topic Assessment - Question 5: Botanical Fermentation Duration",
                        "content": {
                            "question": "When preparing green foliar tea by fermenting succulent Mexican sunflower (Tithonia) leaves in water, how long must the mixture ferment?",
                            "options": [
                                "Only 1 to 2 hours.",
                                "Exactly 24 hours.",
                                "Between 7 to 14 days with daily stirring.",
                                "At least 6 months."
                            ],
                            "answer": "C",
                            "explanation": "Green botanical foliar teas require a fermentation period of 7 to 14 days with daily stirring to thoroughly break down leafy plant tissues and release locked potassium and phosphorus."
                        }
                    }
                ],
                # Page 9: Topic Assessment Part 3 (Questions 6 to 8)
                [
                    {
                        "type": "knowledge_check",
                        "title": "Topic Assessment - Question 6: Undiluted Manure Tea Scorch",
                        "content": {
                            "question": "If a student sprays highly concentrated, undiluted manure compost tea directly onto young crop leaves, what is the most likely biological consequence?",
                            "options": [
                                "The leaves will grow three times larger within 24 hours.",
                                "The high nitrogen concentration will chemically scorch and burn the crop leaves.",
                                "The plant will permanently stop absorbing water through its roots.",
                                "Beneficial honeybees will immediately eat the crop leaves."
                            ],
                            "answer": "B",
                            "explanation": "Manure compost tea has high nitrogen and mineral salts. Applying it undiluted causes severe chemical fertilizer scorch. It must always be diluted with water at a 1:10 ratio."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Topic Assessment - Question 7: Mulch Weed Suppression",
                        "content": {
                            "question": "Why does covering cultivated soil rows with a thick layer of dry grass mulch act as a highly effective weed control method?",
                            "options": [
                                "Mulch releases synthetic poison into the soil.",
                                "Mulch physically covers the ground, smothering emerging shoots and blocking the sunlight weeds need to grow.",
                                "Mulch attracts rodents to chew up weed stems.",
                                "Mulch dries out the soil so weed seeds dehydrate."
                            ],
                            "answer": "B",
                            "explanation": "Mulching suppresses weeds physically: it covers bare soil, smothers emerging weed seedlings, and blocks sunlight, preventing weeds from photosynthesizing."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Topic Assessment - Question 8: Short-Season Crop Selection",
                        "content": {
                            "question": "Your school garden team has exactly 6 weeks remaining before the term closes. Which of the following crops is most suitable to grow and harvest within this time limit?",
                            "options": [
                                "Cassava (takes 9 to 12 months to mature).",
                                "Maize (takes 4 to 5 months to mature).",
                                "Radishes (takes 4 weeks to mature).",
                                "Sorghum (takes 3 to 4 months to mature)."
                            ],
                            "answer": "C",
                            "explanation": "Radishes are fast-maturing short-season root crops that take only 4 weeks from sowing to harvest, fitting comfortably within a 6-week window."
                        }
                    }
                ],
                # Page 10: Topic Assessment Part 4 (Questions 9 to 10)
                [
                    {
                        "type": "knowledge_check",
                        "title": "Topic Assessment - Question 9: Sowing Depth Application",
                        "content": {
                            "question": "When sowing bean seeds on a prepared raised bed, how deep should the seeds be buried based on standard agricultural sowing depth guidelines?",
                            "options": [
                                "Exactly 15cm deep (the length of a hand-span) to protect from birds.",
                                "Scattered on top of dry grass mulch without any soil covering.",
                                "At a depth equal to 2 to 3 times the thickness of the seed itself.",
                                "Pushed down into the subsoil until they touch the base rocks."
                            ],
                            "answer": "C",
                            "explanation": "The fundamental sowing depth rule states that a seed must be buried at a depth equal to 2 to 3 times its own thickness. Sowing deeper exhausts seed energy, while sowing shallower causes dehydration."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Topic Assessment - Question 10: Stomata Biology & Spray Timing",
                        "content": {
                            "question": "Why must organic botanical pest repellents and foliar feeds be sprayed on crop leaves only during the cool morning or late evening hours?",
                            "options": [
                                "Leaf stomata pores close during midday heat to prevent water loss, and intense sunlight on wet leaves causes severe heat scorch.",
                                "Because insect pests are asleep at midday and cannot be repelled.",
                                "To prevent water from dripping into the soil beds.",
                                "Because students are forbidden from working in school farm beds during the daytime."
                            ],
                            "answer": "A",
                            "explanation": "Crop leaves absorb sprays through microscopic stomata pores, which close during hot midday hours to prevent water loss. Spraying in the cool morning or evening ensures open stomata for nutrient absorption and prevents sunlight from burning wet leaf tissues."
                        }
                    }
                ]
            ]
        }
    ]

def ingest_cbc_grade9_agriculture_topic4(replace: bool = True):
    """Executes the database transaction to ingest Topic 4 into CBC Grade 9 Agriculture."""
    print("=" * 80)
    print("STARTING CONTENT INGESTION: CBC GRADE 9 AGRICULTURE — TOPIC 4")
    print("=" * 80)

    with transaction.atomic():
        # 1. Resolve Hierarchy
        curriculum, _ = Curriculum.objects.get_or_create(
            name="CBC",
            defaults={"description": "Competency Based Curriculum"}
        )
        grade, _ = Grade.objects.get_or_create(
            curriculum=curriculum,
            name="Grade 9",
            defaults={"level": 9, "description": "Junior Secondary School Grade 9"}
        )
        subject, _ = Subject.objects.get_or_create(
            grade=grade,
            name="Agriculture",
            defaults={"description": "Grade 9 Agriculture (CBC)"}
        )

        print(f"[*] Hierarchy Resolved: {curriculum.name} -> {grade.name} -> {subject.name}")

        # 2. Resolve Topic
        topic_name = "Organic Gardening"
        if replace:
            existing_topics = Topic.objects.filter(subject=subject, name=topic_name)
            if existing_topics.exists():
                print(f"[*] Found existing topic '{topic_name}' (ID: {existing_topics.first().id}). Deleting for clean replace...")
                existing_topics.delete()

        topic, created = Topic.objects.get_or_create(
            subject=subject,
            name=topic_name,
            defaults={
                "order": 4,
                "description": "Comprehensive organic gardening systems: chemical-free agriculture, compost heap layering, botanical neem and garlic pesticides, mechanical weed control, foliar feeds, short-season crop selection, raised bed construction, and precision seed sowing."
            }
        )
        print(f"[*] Topic: '{topic.name}' (ID: {topic.id}, Created: {created})")

        # 3. Ingest Units and Lessons
        curriculum_data = build_topic4_curriculum()
        total_units = len(curriculum_data)
        total_lessons = 0
        total_pages = 0
        total_blocks = 0

        for unit_data in curriculum_data:
            u_order = unit_data["unit_order"]
            u_name = clean_text(unit_data["unit_name"])
            u_desc = clean_text(unit_data["unit_description"])
            l_title = clean_text(unit_data["lesson_title"])
            pages_data = unit_data["pages"]

            unit = LearningUnit.objects.create(
                topic=topic,
                name=u_name,
                order=u_order,
                description=u_desc
            )

            lesson = Lesson.objects.create(
                topic=topic,
                learning_unit=unit,
                title=l_title,
                status="published",
                version=1
            )
            total_lessons += 1

            block_order = 0
            for page_idx, page_blocks in enumerate(pages_data, start=1):
                total_pages += 1
                page_title = None

                for comp_idx, b_data in enumerate(page_blocks, start=1):
                    b_type = b_data["type"]
                    b_title = clean_text(b_data.get("title", ""))
                    b_content = clean_dict(b_data.get("content", {}))

                    if not page_title and b_title:
                        page_title = b_title

                    LessonBlock.objects.create(
                        lesson=lesson,
                        block_id=f"g9_agri_t4_u{u_order}_p{page_idx}_b{comp_idx}",
                        block_type=b_type,
                        component_type=b_type,
                        title=b_title,
                        content=b_content,
                        page_number=page_idx,
                        page_title=page_title,
                        component_order=comp_idx,
                        order=block_order
                    )
                    block_order += 1
                    total_blocks += 1

            print(f"  [+] Ingested Unit {u_order}: '{u_name}' -> Lesson ID {lesson.id} ({len(pages_data)} Pages, {block_order} Blocks)")

        print("\n" + "=" * 80)
        print(f"[SUCCESS] Ingestion Complete for Topic 4: '{topic.name}'")
        print(f"[*] Units Created:   {total_units}")
        print(f"[*] Lessons Created: {total_lessons}")
        print(f"[*] Total Pages:     {total_pages}")
        print(f"[*] Total Blocks:    {total_blocks}")
        print("=" * 80)

if __name__ == "__main__":
    replace_flag = "--replace" in sys.argv or True
    ingest_cbc_grade9_agriculture_topic4(replace=replace_flag)
