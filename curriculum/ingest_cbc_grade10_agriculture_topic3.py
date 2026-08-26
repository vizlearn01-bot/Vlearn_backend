"""
VLearn CBC Grade 10 Agriculture — Topic 3: Land Preparation
Production Ingestion Engine (Deep Senior Secondary Pedagogical Edition)

Curriculum: CBC (ID: 5)
Grade: Grade 10 (ID: 5, Level: 10)
Subject: Agriculture
Topic: Land Preparation (Topic Order: 3)

Decomposed into 12 Learning Units & 12 Published Lessons:
  1. Purpose and Sequence of Land Preparation (6 Pages, 12 Blocks)
  2. Land Clearing (6 Pages, 12 Blocks)
  3. Primary Cultivation (6 Pages, 13 Blocks)
  4. Secondary Cultivation (6 Pages, 12 Blocks)
  5. Tertiary Operations (6 Pages, 12 Blocks)
  6. Tool Selection and Safety (6 Pages, 12 Blocks)
  7. Zero Tillage (6 Pages, 13 Blocks)
  8. Minimum Tillage (6 Pages, 12 Blocks)
  9. Assessing Land for a Selected Crop (6 Pages, 12 Blocks)
  10. Preparing a Demonstration Plot (6 Pages, 12 Blocks)
  11. Effects of Proper Land Preparation (6 Pages, 12 Blocks)
  12. Synthesis and Practical Assessment (9 Pages, 18 Blocks)
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

def build_topic3_curriculum():
    """Returns the comprehensive pedagogical page and block structure for Grade 10 Topic 3: Land Preparation."""
    return [
        # =====================================================================
        # LESSON 1: Purpose and Sequence of Land Preparation
        # =====================================================================
        {
            "unit_order": 1,
            "unit_name": "Purpose and Sequence of Land Preparation",
            "unit_description": "Definition of land preparation, 5 core agronomic reasons (aeration, root penetration, weed burial, pest disruption, infiltration), and the 4-stage sequential flow (Clearing, Primary, Secondary, Tertiary).",
            "lesson_title": "Purpose and Sequential Operations in Land Preparation",
            "pages": [
                [
                    {
                        "type": "suggested_image",
                        "title": "Agricultural Plowing and Seedbed Preparation",
                        "content": {
                            "title": "Agricultural Plowing and Seedbed Preparation",
                            "caption": "A tractor plowing and turning over compacted soil to create an aerated, structured seedbed for crop planting."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Land Preparation Fundamentals",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Define **land preparation** in commercial crop production.",
                                "Analyze the five core **agronomic reasons** for preparing agricultural land.",
                                "Outline the strict **4-stage sequence of tillage operations**: Clearing $\\rightarrow$ Primary Tillage $\\rightarrow$ Secondary Tillage $\\rightarrow$ Tertiary Operations.",
                                "Explain why reversing or skipping tillage stages damages soil structure and equipment."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "What is Land Preparation?",
                        "content": {
                            "title": "The Foundation of Crop Production",
                            "text": "**Land preparation** refers to the mechanical and physical manipulation of agricultural soil to create an optimal, highly favorable environment for seed germination, seedling emergence, and rapid root expansion.\n\n- Transforming hard, compacted, weed-choked fallow land into a refined, porous seedbed is the essential starting point of any profitable farming enterprise.\n- Planting directly into unprepared, compacted soil leads to poor seed germination, seedling suffocations, weed choking, and low harvest yields."
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "Five Core Agronomic Reasons for Land Preparation",
                        "content": {
                            "title": "Why Farmers Invest Labor and Capital into Tillage",
                            "text": "1. **Enhancing Soil Aeration**: Loosening consolidated topsoil opens up continuous macro-pores, supplying atmospheric oxygen ($O_2$) needed for root cell respiration and beneficial aerobic bacteria.\n2. **Facilitating Root Penetration**: Soft, crumbly soil offers zero mechanical impedance, allowing delicate taproots and lateral roots to expand deeply into subsoil moisture reserves.\n3. **Physical Weed Eradication**: Inverting the soil uproots growing weeds and buries them deep below the surface, suffocating weed seedlings and preventing competition for sunlight and nutrients.\n4. **Disrupting Pest and Disease Cycles**: Turning the soil brings buried soil-dwelling pests (cutworms, white grubs, beetle pupae) and fungal spores to the surface, exposing them to solar heat, desiccation, and predatory birds.\n5. **Improving Water Infiltration**: Broken soil absorbs rainfall and irrigation water rapidly, preventing sheet erosion and surface runoff while storing capillary moisture in the root zone."
                        }
                    },
                    {
                        "type": "definition_card",
                        "title": "Key Term: Seedbed",
                        "content": {
                            "term": "Seedbed",
                            "definition": "A prepared topsoil layer with optimal physical tilth, moisture, and aeration created to support seed germination, seedling emergence, and early root anchoring.",
                            "example": "A finely raked nursery bed prepared for tiny cabbage and tomato seeds."
                        }
                    }
                ],
                [
                    {
                        "type": "suggested_diagram",
                        "title": "The 4-Stage Land Preparation Sequence Flowchart",
                        "content": {
                            "title": "The 4-Stage Land Preparation Sequence Flowchart",
                            "caption": "Sequential flowchart showing Stage 1: Land Clearing (slashers/mattocks), Stage 2: Primary Cultivation (jembes/disc ploughs), Stage 3: Secondary Cultivation (rakes/harrows), and Stage 4: Tertiary Operations (ridges/beds)."
                        }
                    },
                    {
                        "type": "comparison_table",
                        "title": "The 4 Sequential Stages of Land Preparation",
                        "content": {
                            "title": "Sequential Tillage Stages Comparison",
                            "headers": ["Stage", "Tillage Operation", "Primary Purpose", "Standard Tools & Implements"],
                            "rows": [
                                ["Stage 1", "Land Clearing", "Remove surface brush, trees, tall weeds, and stones", "Slasher, Panga, Axe, Mattock, Bulldozer"],
                                ["Stage 2", "Primary Cultivation", "Deep soil breaking (15–30 cm) and furrow inversion", "Hand Jembe, Fork Jembe, Mouldboard/Disc Plough"],
                                ["Stage 3", "Secondary Cultivation", "Refine rough clods into fine crumb tilth (5–15 cm)", "Hand Rake, Disc Harrow, Spring-Tine Harrow, Rotavator"],
                                ["Stage 4", "Tertiary Operations", "Custom shaping: ridges, raised beds, furrows, rollers", "Jembe (ridging), Rake (bedding), Roller, Furrower"]
                            ]
                        }
                    }
                ],
                [
                    {
                        "type": "step_process",
                        "title": "Logical Flow of Seedbed Operations",
                        "content": {
                            "title": "Why Order Matters in Land Preparation",
                            "steps": [
                                "1. **Never skip Land Clearing**: Clearing prevents thick woody stumps and surface rocks from shattering expensive tractor plough shears or jamming disc bearings.",
                                "2. **Perform Primary Tillage First**: Primary implements possess the heavy weight and cutting power needed to shatter consolidated soil crusts.",
                                "3. **Follow with Secondary Tillage**: Lightweight secondary implements (rakes, harrows) can only pulverize and level soil that has already been loosened by primary digging.",
                                "4. **Conclude with Tertiary Shaping**: Beds and ridges require fine, loose, secondary-tilled soil to be mounded neatly without large unbroken clods."
                            ]
                        }
                    },
                    {
                        "type": "callout",
                        "title": "Agronomic Principle: Soil Timing",
                        "content": {
                            "title": "The Moisture Window for Tillage",
                            "text": "Cultivating soil when it is **too wet** causes clay particles to smear into impermeable platy clods that dry like concrete. Cultivating when **too dry** requires massive tractor power and pulverizes soil into fine dust that blows away in the wind. Optimal tillage occurs when soil is moist and friable (crumbling easily in the hand)."
                        }
                    }
                ],
                [
                    {
                        "type": "mini_activity",
                        "title": "Practical Field Investigation: Soil Compaction vs Loosened Tilth",
                        "content": {
                            "title": "Testing Soil Penetration Resistance",
                            "task": "1. Visit the school farm. Locate a hard, uncultivated cattle path (representing unprepared land) and a recently tilled vegetable bed.\n2. Attempt to push a 30 cm wooden stick vertically into the soil in both locations using uniform hand pressure.\n3. Measure and record the penetration depth in centimeters.\n4. Explain how this mechanical resistance affects young crop root elongation and seedling survival.",
                            "materials": ["30 cm Wooden Ruler / Stick", "Notebook", "Pen"],
                            "safety": "Do not use excessive force that could break the stick and cause splinters."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Core Summary: Land Preparation Sequence",
                        "content": {
                            "title": "Key Takeaways",
                            "text": "- **Land preparation** creates the optimal physical environment for crop establishment.\n- **Agronomic benefits** include aeration, root growth, weed burial, pest disruption, and infiltration.\n- **Strict sequence**: 1. Clearing $\\rightarrow$ 2. Primary Tillage $\\rightarrow$ 3. Secondary Tillage $\\rightarrow$ 4. Tertiary Operations.\n- **Secondary tools** cannot work on unplowed land; operations must follow strict chronological order."
                        }
                    }
                ],
                [
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Sequential Tillage Logic",
                        "content": {
                            "question": "Why is it agronomically and mechanically incorrect for a farmer to operate a tractor disc harrow across a field before performing primary plowing with a disc plough?",
                            "options": [
                                "Disc harrows are only allowed to run at night by law",
                                "Disc harrows are lightweight secondary implements designed to slice loose soil clods; they lack the heavy weight and cutting depth to penetrate or break a consolidated, undisturbed soil crust",
                                "Disc harrows automatically spray chemical pesticides that kill all crops",
                                "Primary plowing is only performed after seeds have already germinated"
                            ],
                            "answer": "B",
                            "explanation": "Secondary tillage implements like disc harrows or spring-tine harrows are lightweight and engineered to refine and level soil that has already been loosened. If driven across unbroken, hard ground, the harrow discs will simply ride along the surface without cutting into the soil, causing severe wear and damage to the implement bearings."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 2: Land Clearing
        # =====================================================================
        {
            "unit_order": 2,
            "unit_name": "Land Clearing",
            "unit_description": "Definition of land clearing, manual tools (slasher, panga, axe, mattock) and mechanical implements (bulldozer), and the destructive ecological consequences of burning vs composting.",
            "lesson_title": "Land Clearing Methods and Ecological Stewardship",
            "pages": [
                [
                    {
                        "type": "suggested_image",
                        "title": "Land Clearing and Debris Removal in Agriculture",
                        "content": {
                            "title": "Land Clearing and Debris Removal in Agriculture",
                            "caption": "Clearing overgrown woody vegetation, shrubs, and roots from a farm plot to prepare the surface for primary tillage."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Land Clearing",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Define **land clearing** in agricultural land development.",
                                "Select the correct hand tools (**slasher, panga, axe, mattock**) and machinery (**bulldozer**) for clearing specific vegetation types.",
                                "Analyze the severe **ecological and biological damages** caused by burning cleared vegetation (slash-and-burn).",
                                "Adopt sustainable **composting and mulching** alternatives for cleared biomass."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "What is Land Clearing?",
                        "content": {
                            "title": "Preparing the Field Surface",
                            "text": "**Land clearing** is the removal of surface vegetative cover, tall weeds, woody shrubs, tree stumps, and surface boulders from a newly selected or fallow farm plot.\n\n- It is the mandatory first stage of land preparation. Leaving dense weeds, woody saplings, or underground stumps in the field obstructs primary digging and severely damages expensive tractor plough discs, shear pins, and jembe handles."
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "Tools and Implements for Land Clearing",
                        "content": {
                            "title": "Matching the Clearing Tool to the Vegetation",
                            "text": "Farmers select clearing equipment based on vegetation density and farm scale:\n\n### 1. Manual Hand Tools\n- **Slasher**: A curved, long-handled steel blade used in an upright swinging motion to cut tall grass, annual weeds, and herbaceous vegetation without excessive back fatigue.\n- **Panga (Machete)**: A heavy, flat steel blade used for cutting woody shrubs, thick branches, and small tree saplings.\n- **Axe**: A heavy wedge-shaped steel head on a wooden handle, used for felling large trees and splitting thick hardwood logs.\n- **Mattock**: A heavy dual-headed tool featuring a pick on one side and a hoe blade on the other, specifically engineered for digging out tough underground roots and prying up tree stumps.\n\n### 2. Heavy Mechanical Machinery\n- **Bulldozer / Tree Pusher**: A high-horsepower crawler tractor equipped with a front steel blade, used on large commercial estates to push over mature trees, uproot large boulders, and clear heavy forest debris."
                        }
                    },
                    {
                        "type": "comparison_table",
                        "title": "Manual Clearing Tools Comparison Matrix",
                        "content": {
                            "title": "Land Clearing Tool Selection Guide",
                            "headers": ["Tool Name", "Blade / Head Design", "Target Vegetation", "Primary Agricultural Advantage"],
                            "rows": [
                                ["Slasher", "Long handle, angled thin blade", "Tall grasses, annual weeds", "Rapid cutting while standing upright"],
                                ["Panga (Machete)", "Short handle, heavy broad blade", "Woody shrubs, saplings, thick vines", "High chopping impact force"],
                                ["Axe", "Heavy wedge-shaped head", "Mature trees, thick logs", "Deep wood penetration for felling"],
                                ["Mattock", "Dual head (Pick + Hoe blade)", "Underground roots, tree stumps, stones", "High prying leverage to uproot stumps"],
                                ["Bulldozer", "Tractor-mounted front steel blade", "Large rocks, dense forest cover", "Clears hectares of heavy debris rapidly"]
                            ]
                        }
                    }
                ],
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Land Clearing Tools and Composting vs Burning",
                        "content": {
                            "title": "Land Clearing Tools and Composting vs Burning",
                            "caption": "Visual comparison contrasting destructive burning (killing microbes, destroying SOM, triggering erosion) against regenerative composting (retaining organic carbon, building soil humus)."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The Destructive Nature of Burning (Slash-and-Burn)",
                        "content": {
                            "title": "Why Modern Agriculture Forbids Field Burning",
                            "text": "While burning cleared vegetation may seem fast and convenient, it causes catastrophic, long-term soil degradation:\n\n1. **Destruction of Soil Organic Matter (SOM)**: Fire incinerates surface biomass, converting valuable organic carbon and nitrogen into atmospheric gases ($CO_2, NO_x$) instead of building soil humus.\n2. **Sterilization of Beneficial Microorganisms**: Intense heat travels into the top 5 cm of soil, cooking and killing earthworms, *Rhizobium* bacteria, and mycorrhizal fungi.\n3. **Accelerated Soil Erosion**: Burning leaves the soil bare and charred, stripping away protective mulch and allowing wind and raindrops to wash away topsoil.\n4. **Air Pollution & Carbon Emissions**: Smoke releases harmful particulates that cause respiratory illness while emitting greenhouse gases that drive climate change.\n\n- **The Sustainable Solution**: Cleared organic material should be gathered into heaps, chopped, and converted into **high-grade compost manure** or used as protective soil mulch."
                        }
                    }
                ],
                [
                    {
                        "type": "step_process",
                        "title": "Protocol: Sustainable Land Clearing Workflow",
                        "content": {
                            "title": "Eco-Friendly Clearing and Biomass Recycling",
                            "steps": [
                                "1. **Cut Tall Grass**: Use slashers to cut tall grass and soft weeds down to ground level.",
                                "2. **Chop Shrubs and Saplings**: Use pangas to chop woody shrubs and branches into manageable 30 cm lengths.",
                                "3. **Uproot Stumps with Mattocks**: Dig around root collars and use the pick-end of a mattock to sever roots and pry stumps out of the ground.",
                                "4. **Gather and Sort Biomass**: Separate woody timber (for farm firewood/fencing) from green leafy trash.",
                                "5. **Transfer Leafy Trash to Compost Site**: Transport all grass, weed foliage, and soft green matter to the farm compost pit to produce organic fertilizer."
                            ]
                        }
                    },
                    {
                        "type": "callout",
                        "title": "Environmental Fact: Soil Heat Damage",
                        "content": {
                            "title": "Soil Temperatures Under Brush Fires",
                            "text": "Surface brush fires can reach temperatures exceeding $400^\\circ\\text{C}$. This intense heat completely volatilizes soil nitrogen and sulfur, turns clay minerals into brittle brick-like crusts, and destroys 100% of biological life in the topsoil!"
                        }
                    }
                ],
                [
                    {
                        "type": "mini_activity",
                        "title": "Field Practical: Eco-Friendly Clearing of a Garden Plot",
                        "content": {
                            "title": "Practical Clearing and Biomass Harvesting",
                            "task": "In groups of five, clear an overgrown $2\\text{ m} \\times 2\\text{ m}$ school demonstration plot:\n\n1. Use slashers and pangas to cut vegetation cleanly at soil level.\n2. Use a mattock to extract thick taproots and woody stumps.\n3. Gather all cleared organic biomass into a wheelbarrow and transport it to the school composting area—do not burn any material!\n4. Inspect the cleared plot to ensure it is free of surface obstructions for primary digging.",
                            "materials": ["Slashers", "Pangas", "Mattock", "Wheelbarrow", "Leather Gloves"],
                            "safety": "Wear heavy leather gloves and safety boots. Maintain a 3-meter working distance from peers."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Core Summary: Land Clearing",
                        "content": {
                            "title": "Key Takeaways",
                            "text": "- **Land clearing** removes surface biomass and stumps to protect primary tillage tools.\n- **Match tools to task**: Slashers for grass, Pangas for shrubs, Axes for trees, Mattocks for stumps.\n- **Never burn cleared trash**: Burning destroys organic carbon, sterilizes soil biology, and triggers erosion.\n- **Recycle cleared biomass** into nutrient-rich compost manure."
                        }
                    }
                ],
                [
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Eco-Friendly Biomass Management",
                        "content": {
                            "question": "A farmer clears 2 acres of dense bushland to establish a passion fruit orchard. The farm hand suggests setting fire to the huge piles of dry brushwood to 'clean the field and fertilize it with ash.' Why should the farmer reject this burning proposal?",
                            "options": [
                                "Burning will cause passion fruit vines to turn purple immediately",
                                "Burning incinerates valuable organic carbon, sterilizes beneficial soil microbes, destroys topsoil structure, and accelerates severe erosion, whereas composting the biomass preserves nutrients and builds soil humus",
                                "Ash from brush fires contains poisonous mercury that kills all crops",
                                "Burning attracts swarms of desert locusts to the farm"
                            ],
                            "answer": "B",
                            "explanation": "Setting fire to cleared brush destroys irreplaceable soil organic matter (SOM) and converts nitrogen into gas. The extreme heat cooks and sterilizes earthworms, mycorrhizal fungi, and nitrogen-fixing bacteria, while exposing the bare soil to erosion. Recycling the cleared brush into compost retains organic carbon, feeds soil biology, and dramatically enhances long-term soil moisture and fertility."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 3: Primary Cultivation
        # =====================================================================
        {
            "unit_order": 3,
            "unit_name": "Primary Cultivation",
            "unit_description": "Definition of primary cultivation, manual tools (hand jembe, fork jembe), tractor implements (mouldboard plough vs disc plough), and subsoiling to shatter compacted hardpans.",
            "lesson_title": "Primary Cultivation and Deep Tillage Implements",
            "pages": [
                [
                    {
                        "type": "suggested_image",
                        "title": "Mouldboard Plough in Primary Cultivation",
                        "content": {
                            "title": "Mouldboard Plough in Primary Cultivation",
                            "caption": "A tractor pulling a heavy mouldboard plough, cutting and inverting deep soil furrow slices to break compacted ground."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Primary Cultivation",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Define **primary cultivation** as the first deep mechanical manipulation of soil.",
                                "Compare manual digging tools: **hand jembe** vs **fork jembe** in sticky clay soils.",
                                "Analyze the mechanical operation and soil suitability of **mouldboard ploughs** vs **disc ploughs**.",
                                "Explain how **subsoilers** shatter deep impermeable **hardpans** up to $60\\text{ cm}$ depth."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "What is Primary Cultivation?",
                        "content": {
                            "title": "Breaking the Earth's Crust",
                            "text": "**Primary cultivation** (also known as primary tillage or deep plowing) is the initial deep mechanical working of soil following land clearing.\n\n- It involves cutting, shattering, lifting, and inverting the soil to a depth of **15 cm to 30 cm**.\n- **Primary Objectives**: Break the consolidated, hard soil crust, bury crop residues and weeds to decompose, incorporate organic manures, and expose buried soil pests to solar heat and predators."
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "Manual Primary Tillage Tools",
                        "content": {
                            "title": "Hand Jembe vs Fork Jembe",
                            "text": "On smallholder farms and garden plots, primary digging is done manually:\n\n### 1. Hand Jembe (Common Hoe)\n- Consists of a flat, solid steel blade attached to a wooden handle at an acute angle ($<90^\\circ$).\n- Designed to chop into the soil, pry up slices, and invert them. Ideal for light to medium loamy soils.\n- *Limitation*: In heavy wet clay, sticky soil adheres to the broad flat blade, creating high suction drag and exhausting the farmer.\n\n### 2. Fork Jembe\n- Features 4 to 5 heavy, thick, tapered steel prongs instead of a solid flat blade.\n- **Superior in Heavy Sticky Clay**: Soil does not stick to the prongs, dramatically reducing suction drag.\n- **Superior for Couch Grass Infestations**: Digs under rhizomatous grass roots (*Digitaria scalarum*) and lifts root mats out intact without slicing them into thousands of regenerating fragments."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Tractor Implements: Mouldboard Plough vs Disc Plough",
                        "content": {
                            "title": "Comparing Primary Tractor Implements",
                            "text": "On commercial farms, primary plowing uses animal-drawn or tractor-mounted implements:\n\n### 1. Mouldboard Plough (The Inversion Master)\n- Uses a sharp horizontal **share** to cut the furrow slice and a curved steel **mouldboard** that lifts and rolls the soil over a full $180^\\circ$.\n- **Best suited for**: Clean, stone-free loams and clay loams. Provides unmatched weed burial and green manure incorporation.\n- *Limitation*: Cannot be used in stony, dry, or stump-infested soils where the static rigid share will bend, snap, or jam.\n\n### 2. Disc Plough (The Tough Terrain Specialist)\n- Consists of heavy, concave, rotating tempered steel discs mounted on heavy-duty bearings.\n- **Best suited for**: Stony, hard, dry, trashy, or root-infested soils. The rolling circular discs cut through roots and roll over hard rock obstructions without breaking."
                        }
                    }
                ],
                [
                    {
                        "type": "comparison_table",
                        "title": "Mouldboard Plough vs Disc Plough Comparison Matrix",
                        "content": {
                            "title": "Tractor Primary Plough Comparison",
                            "headers": ["Feature", "Mouldboard Plough", "Disc Plough"],
                            "rows": [
                                ["Cutting Mechanism", "Static share cuts; curved mouldboard turns slice", "Concave rotating steel discs cut and scoop"],
                                ["Furrow Inversion", "Complete 180° inversion (Superior weed burial)", "Partial, loose churning and mixing"],
                                ["Suitable Soils", "Clean, stone-free, arable loam soils", "Stony, hard, dry, sticky, root-infested rough ground"],
                                ["Obstruction Response", "Rigid; breaks or jams against boulders/stumps", "Discs roll smoothly over rocks and stumps"],
                                ["Draft Power Requirement", "Moderate to high in clean soils", "High draft power; heavy tractor weight needed"]
                            ]
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Primary Tillage Implements: Mouldboard vs Disc vs Subsoiler",
                        "content": {
                            "title": "Primary Tillage Implements: Mouldboard vs Disc vs Subsoiler",
                            "caption": "Engineering cross-section comparing the 180° furrow inversion of a Mouldboard Plough, the rolling action of a Disc Plough, and the 60 cm deep hardpan shattering action of a Subsoiler shank."
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "Subsoiling: Shattering Deep Hardpans",
                        "content": {
                            "title": "Restoring Subsurface Drainage and Root Access",
                            "text": "Years of continuous mechanized plowing at a constant depth ($20\\text{ cm}$) or heavy tractor tire traffic compresses the subsoil into a rock-hard, impervious layer called a **plow pan** or **hardpan**.\n\n- **Agronomic Consequences of Hardpans**: Blocks vertical drainage (causing topsoil waterlogging), stops root penetration (causing shallow, crooked roots), and triggers violent surface runoff.\n- **The Subsoiler**: A heavy, narrow, vertical steel shank equipped with a pointed wedge at the tip. It is pulled through the soil at depths of **40 cm to 60 cm** to shatter and crack the hardpan without bringing infertile subsoil to the surface."
                        }
                    },
                    {
                        "type": "suggested_video",
                        "title": "Tractor Tillage Implements in Action",
                        "content": {
                            "title": "Tractor Tillage Implements in Action",
                            "description": "Field demonstration showcasing mouldboard plows turning clean soil, disc plows rolling through rough terrain, and heavy subsoilers cracking deep hardpans.",
                            "url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
                        }
                    }
                ],
                [
                    {
                        "type": "mini_activity",
                        "title": "Field Practical: Evaluating Hand Jembe vs Fork Jembe in Clay",
                        "content": {
                            "title": "Manual Tillage Implement Comparison",
                            "task": "1. In a wet, sticky clay patch on the school farm, have two learners dig adjacent 1-meter rows simultaneously: one using a standard hand jembe and one using a fork jembe.\n2. Compare digging effort, blade stickiness/suction drag, and the condition of uprooted weed rhizomes.\n3. Record observations and explain why fork jembes are agronomically superior in heavy soils.",
                            "materials": ["Hand Jembe", "Fork Jembe", "Stopwatch", "Notepad"],
                            "safety": "Maintain a 3-meter safety distance between diggers."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Core Summary: Primary Cultivation",
                        "content": {
                            "title": "Key Takeaways",
                            "text": "- **Primary cultivation (15–30 cm)** breaks consolidated crusts and inverts weeds.\n- **Fork jembe** is optimal for sticky clay and lifting out couch grass rhizomes intact.\n- **Mouldboard plough** provides complete 180° weed burial in clean, stone-free loam.\n- **Disc plough** rolls over rocks, stumps, and hard ground without breaking.\n- **Subsoiler (40–60 cm)** shatters underground hardpans to restore drainage."
                        }
                    }
                ],
                [
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Selecting Implements for Rough Ground",
                        "content": {
                            "question": "A farmer in Laikipia clears a 10-acre parcel that contains numerous buried stones, dry hard-baked soil, and thick acacia roots. Which primary tillage implement should the tractor operator hitch?",
                            "options": [
                                "A light wooden garden rake",
                                "A mouldboard plough",
                                "A heavy disc plough",
                                "A lawnmower"
                            ],
                            "answer": "C",
                            "explanation": "A disc plough is specifically engineered for rough, stony, hard, and root-infested land. Its heavy, concave, rotating steel discs cut through roots and roll smoothly over buried boulders and stumps without breaking or jamming. A mouldboard plough has a rigid static share that would catch on stones and roots, bending or shattering the implement."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 4: Secondary Cultivation
        # =====================================================================
        {
            "unit_order": 4,
            "unit_name": "Secondary Cultivation",
            "unit_description": "Definition of secondary cultivation, understanding soil 'tilth', fine tilth for small seeds vs coarse tilth for large seeds, and implements (rakes, disc harrows, spring-tine harrows, rotavators).",
            "lesson_title": "Secondary Cultivation and Soil Tilth Optimization",
            "pages": [
                [
                    {
                        "type": "suggested_image",
                        "title": "Tractor Disc Harrowing to Refine Seedbed Tilth",
                        "content": {
                            "title": "Tractor Disc Harrowing to Refine Seedbed Tilth",
                            "caption": "A tractor pulling a disc harrow across a primary-plowed field, shattering large soil clods into fine, crumbly seedbed tilth."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Secondary Cultivation",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Define **secondary cultivation** and its role in seedbed preparation.",
                                "Explain the agricultural concept of **soil tilth**.",
                                "Differentiate between **fine tilth** (small-seeded crops) and **coarse cloddy tilth** (large-seeded crops).",
                                "Identify manual tools (**hand rake**) and tractor implements (**disc harrow, spring-tine harrow, rotavator**)."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "What is Secondary Cultivation?",
                        "content": {
                            "title": "Refining the Rough Seedbed",
                            "text": "**Secondary cultivation** (or secondary tillage) encompasses all mechanical operations carried out *after* primary cultivation and *before* planting.\n\n- While primary plowing leaves the field rough, uneven, and covered in large clods with large air voids, secondary cultivation works at a shallower depth (**5 cm to 15 cm**) to break clods, remove weed debris, level the surface, and produce an optimal **tilth**."
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "Understanding Soil 'Tilth'",
                        "content": {
                            "title": "Matching Tilth to Seed Size",
                            "text": "**Soil tilth** describes the physical condition of a prepared seedbed in terms of its aggregate size, crumb structure, and suitability for supporting seed germination and early seedling growth:\n\n### 1. Fine Tilth (Smooth, Crumbly, Powdery)\n- Soil clods are broken down into small, millimeter-sized crumb aggregates.\n- **Mandatory for Small Seeds**: Tiny seeds with limited food reserves (carrots, onions, cabbages, kales, tomatoes) require intimate **seed-to-soil contact** to draw capillary moisture.\n- *Risk*: Over-pulverizing soil into fine dust risks surface crusting (capping) after heavy rain and increases wind erosion.\n\n### 2. Coarse / Medium Tilth (Cloddy, Granular)\n- Leaves small clods ($2\\text{--}5\\text{ cm}$) on the surface.\n- **Ideal for Large Seeds**: Large seeds with strong emergence force (maize, beans, peas, sunflowers, cotton) germinate easily through clods while rough surface aggregates resist soil erosion and crusting."
                        }
                    },
                    {
                        "type": "comparison_table",
                        "title": "Fine Tilth vs Coarse Tilth Requirements",
                        "content": {
                            "title": "Crop Seed Size and Required Tilth",
                            "headers": ["Parameter", "Fine Seedbed Tilth", "Coarse / Medium Seedbed Tilth"],
                            "rows": [
                                ["Aggregate Size", "< 5 mm crumbly granules", "20 – 50 mm clods with loose earth"],
                                ["Target Crop Types", "Small-seeded crops (Carrots, Onions, Kales, Cabbage)", "Large-seeded crops (Maize, Beans, Groundnuts, Cotton)"],
                                ["Germination Mechanism", "Maximizes capillary water contact for tiny seeds", "Provides strong anchoring while resisting soil capping"],
                                ["Tillage Operations", "Plowing + 2x Harrowing + Fine Raking", "Plowing + 1x Light Harrowing (or Strip Tillage)"],
                                ["Vulnerability", "Prone to surface crusting and wind erosion if over-milled", "Resistant to crusting; excellent rainwater infiltration"]
                            ]
                        }
                    }
                ],
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Soil Tilth Comparison: Fine vs Coarse Granular Tilth",
                        "content": {
                            "title": "Soil Tilth Comparison: Fine vs Coarse Granular Tilth",
                            "caption": "Cross-sectional comparison showing fine crumb tilth providing 100% capillary contact for tiny carrot seeds versus coarse tilth accommodating vigorous maize seedling emergence while preventing soil capping."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Implements Used in Secondary Cultivation",
                        "content": {
                            "title": "Manual and Mechanical Secondary Tools",
                            "text": "### 1. Hand Rake\n- A manual tool featuring a horizontal steel bar with closely spaced downward tines on a long handle.\n- Used in vegetable beds to crush small clods, comb out uprooted weed stolons, and drag soil into a perfectly level surface for precision seed sowing.\n\n### 2. Disc Harrow\n- Features sets of rotating steel discs (gangs) set at an angle to pulverize clods, chop weed residues, and mix topsoil.\n\n### 3. Spring-Tine Harrow\n- Utilizes flexible, vibrating C-shaped spring-steel tines. As they drag through the soil, they vibrate vigorously, shattering clods, leveling the ground, and pulling buried couch grass roots to the surface.\n\n### 4. Rotavator (Rotary Tiller)\n- A power-take-off (PTO) driven implement with high-speed L-shaped rotating blades that pulverizes soil and incorporates compost into a fine tilth in a single fast pass."
                        }
                    }
                ],
                [
                    {
                        "type": "step_process",
                        "title": "Protocol: Preparing a Fine Nursery Bed Tilth",
                        "content": {
                            "title": "Creating Seedbed Tilth for Horticultural Crops",
                            "steps": [
                                "1. **Inspect Primary Tilled Ground**: Ensure primary clods have dried slightly so they shatter easily upon impact.",
                                "2. **Break Large Clods**: Use a fork jembe or disc harrow to shatter clods down to 2–3 cm diameter.",
                                "3. **Apply and Mix Organic Compost**: Spread 5–10 kg/m² of well-rotted compost and incorporate into the top 10 cm.",
                                "4. **Rake and Comb**: Draw a hand rake back and forth to break remaining surface clods and remove loose stones and weed roots.",
                                "5. **Level the Bed Surface**: Use the flat back of the rake to create an even, horizontal surface ready for precision seed drilling."
                            ]
                        }
                    },
                    {
                        "type": "callout",
                        "title": "Agronomic Warning: Soil Capping",
                        "content": {
                            "title": "Beware of Over-Pulverization",
                            "text": "Over-harrowing a dry field mills soil into fine flour-like dust. When hit by heavy rainfall, the dust dissolves into a muddy slurry that bakes in the sun to form an impermeable **surface crust (cap)**. This crust physically traps emerging seedlings underground and blocks rainwater infiltration!"
                        }
                    }
                ],
                [
                    {
                        "type": "mini_activity",
                        "title": "Lab Investigation: Seed-to-Soil Contact and Germination",
                        "content": {
                            "title": "Comparing Germination in Clods vs Fine Tilth",
                            "task": "1. Take two clear plastic cups.\n   - Fill Cup A with large, unbroken 3 cm soil clods (representing primary tilled soil).\n   - Fill Cup B with fine, crumbly, sifted garden soil (good fine tilth).\n2. Place 5 bean seeds on the soil surface of both cups at 2 cm depth.\n3. Add 30 ml of water to both cups and observe daily for 7 days.\n4. Record germination speed and uniformity. Notice how seeds in Cup A dry out in air gaps while Cup B germinates rapidly.",
                            "materials": ["2 Clear Plastic Cups", "Soil Clods", "Sifted Fine Soil", "10 Bean Seeds", "Water"],
                            "safety": "Keep workstations tidy."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Core Summary: Secondary Cultivation",
                        "content": {
                            "title": "Key Takeaways",
                            "text": "- **Secondary cultivation (5–15 cm)** pulverizes clods, levels soil, and optimizes tilth.\n- **Tilth** is the physical fitness of a seedbed for supporting seed germination.\n- **Fine tilth** is required for small seeds (carrots, onions, cabbages).\n- **Coarse tilth** is optimal for large seeds (maize, beans) to prevent soil capping.\n- **Avoid over-pulverization** to protect soil from surface crusting and erosion."
                        }
                    }
                ],
                [
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Matching Tilth to Crop Requirements",
                        "content": {
                            "question": "A vegetable farmer in Nyandarua is preparing a nursery bed to sow high-value carrot and onion seeds. Why must the farmer achieve an exceptionally fine tilth free of stones and hard clods?",
                            "options": [
                                "Carrot seeds will turn into potatoes if planted in rough soil",
                                "Tiny carrot and onion seeds require close capillary contact with fine soil particles to absorb moisture, while obstruction by clods or stones causes carrot taproots to split, fork, and deform, making them unmarketable",
                                "Fine tilth prevents the sun from shining on the carrot leaves",
                                "Onion seeds require solid rock to develop strong flavor"
                            ],
                            "answer": "B",
                            "explanation": "Carrot and onion seeds are tiny and carry very limited energy stores. They require an exceptionally fine tilth to ensure immediate capillary moisture absorption for germination. Furthermore, carrot taproots are highly sensitive to physical impedance; if a growing carrot root hits a hard clod or stone, it branches and forks into deformed, unmarketable roots."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 5: Tertiary Operations
        # =====================================================================
        {
            "unit_order": 5,
            "unit_name": "Tertiary Operations",
            "unit_description": "Specialized crop-specific field structures: ridging for root/tuber crops (sweet/Irish potatoes), raised beds for vegetables, soil rolling for fine seeds, leveling boards, and furrow opening.",
            "lesson_title": "Tertiary Operations and Field Structural Shaping",
            "pages": [
                [
                    {
                        "type": "suggested_image",
                        "title": "Agricultural Ridges for Potato and Tuber Cultivation",
                        "content": {
                            "title": "Agricultural Ridges for Potato and Tuber Cultivation",
                            "caption": "Parallel raised soil ridges constructed along field contours to provide loose, aerated mounded soil for root and tuber expansion."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Tertiary Operations",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Define **tertiary operations** in agricultural land preparation.",
                                "Analyze the agronomic advantages of **ridging** for root and tuber crops (**sweet potatoes, Irish potatoes, cassava**).",
                                "Explain the purpose of **raised vegetable beds**, **soil rolling**, **leveling**, and **furrow opening**.",
                                "Match specific Kenyan crop enterprises to their required tertiary field structures."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "What are Tertiary Operations?",
                        "content": {
                            "title": "Customizing the Field Architecture",
                            "text": "**Tertiary operations** are the final, highly specialized soil-shaping tasks performed on a prepared field before or during planting.\n\n- Unlike primary and secondary tillage, which prepare the entire field uniformly, tertiary operations are **crop-specific** and **topography-specific**.\n- They create specialized structural micro-environments in the soil to optimize drainage, accommodate root/tuber physiology, and streamline weeding and harvesting."
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "Ridging and Raised Bed Forming",
                        "content": {
                            "title": "Mounded Soil Structures for Agricultural Success",
                            "text": "### 1. Ridging (Mounded Ridges and Furrows)\n- Constructing parallel raised mounds of loose soil ($25\\text{--}35\\text{ cm}$ high) separated by drainage furrows.\n- **Crucial for Root and Tuber Crops**: Essential for **sweet potatoes, Irish potatoes, cassava, and yams**.\n- **Agronomic Advantages**:\n  - *Low Resistance*: Provides a deep, loose volume of aerated soil for tubers to expand rapidly without physical resistance.\n  - *Drainage Protection*: Elevates roots above standing water, preventing lethal tuber rots during heavy rains.\n  - *Harvesting Ease*: Makes lifting tubers at maturity effortless, preventing hoe damage to crops.\n\n### 2. Raised Vegetable Beds\n- Flat-topped, elevated blocks of soil ($15\\text{ cm}$ high, $1\\text{ m}$ wide) bordered by sunken footpaths.\n- **Crucial for High-Value Vegetables**: Spinach, kales, cabbages, tomatoes, capsicums.\n- Prevents foot traffic compaction in the root zone, improves drainage in wet seasons, and simplifies irrigation."
                        }
                    },
                    {
                        "type": "comparison_table",
                        "title": "Tertiary Soil Structures and Crop Compatibility",
                        "content": {
                            "title": "Tertiary Operations Matrix",
                            "headers": ["Tertiary Structure", "Physical Dimensions", "Target Crop Enterprises", "Primary Agronomic Function"],
                            "rows": [
                                ["Ridges", "25–35 cm high mounds, V-furrows", "Sweet potatoes, Irish potatoes, Cassava, Groundnuts", "Deep loose soil for tuber expansion; prevents waterlogging rot"],
                                ["Raised Beds", "15 cm high, 1 m wide flat top", "Cabbage, Kales, Spinach, Tomatoes, Carrots", "Prevents foot compaction; concentrates compost; easy weeding"],
                                ["Rolling", "Lightly compressed smooth surface", "Pasture grasses, Lucerne, Fine brassica seeds", "Ensures firm seed-to-soil contact; prevents wind blow-away"],
                                ["Leveling", "Uniform flat plane across field", "Paddy rice, Basin/furrow irrigated crops", "Guarantees even water distribution; eliminates flood pooling"],
                                ["Furrows", "10–15 cm deep V-shaped channels", "Sugarcane, Maize, Drip-irrigated row crops", "Precision seed placement; directs irrigation water flow"]
                            ]
                        }
                    }
                ],
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Tertiary Field Structures: Raised Beds vs Ridges vs Furrows",
                        "content": {
                            "title": "Tertiary Field Structures: Raised Beds vs Ridges vs Furrows",
                            "caption": "Architectural cross-section showing a 15 cm Raised Vegetable Bed with flat top and side paths versus 30 cm Mounded Tillage Ridges with V-shaped drainage furrows for sweet potato tuber expansion."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Leveling, Rolling, and Furrow Opening",
                        "content": {
                            "title": "Precision Finishing Operations",
                            "text": "### 1. Field Leveling\n- Dragging a heavy wooden beam or tractor leveller across the cultivated field to eliminate high spots and depressions.\n- Eliminates low hollows where water pools and drowns crops, ensuring uniform furrow irrigation in crops like rice and sugarcane.\n\n### 2. Soil Rolling\n- Dragging a cylindrical steel or concrete roller over loose soil after sowing fine, tiny seeds (like pasture grasses, lucerne, or teff).\n- Lightly compresses loose surface aggregates, pressing soil firmly around seeds to enhance capillary water uptake and prevent seeds from blowing away.\n\n### 3. Furrow Opening\n- Slicing narrow V-shaped channels along planting rows using a ridger body or hand jembe for laying drip lines, placing fertilizers, and sowing row crops at uniform depth."
                        }
                    }
                ],
                [
                    {
                        "type": "step_process",
                        "title": "Protocol: Constructing Contour Ridges on Sloping Land",
                        "content": {
                            "title": "Step-by-Step Ridge Construction",
                            "steps": [
                                "1. **Determine Contour Lines**: Use an A-frame or line level to mark horizontal contour lines across the slope.",
                                "2. **Mark Row Spacing**: Set string lines along the contour at 75–90 cm intervals.",
                                "3. **Dig and Mound Soil**: Using a hand jembe, dig topsoil from both sides and heap it into the center along the string line.",
                                "4. **Shape Ridge Geometry**: Form a continuous mound 30 cm high with a broad base and loose, rounded crest.",
                                "5. **Install Cross-Ties (Tied Ridges)**: Build small earth barriers every 3–5 meters across the furrows to trap rainwater and prevent downhill runoff."
                            ]
                        }
                    },
                    {
                        "type": "callout",
                        "title": "Conservation Fact: Tied Ridging in ASALs",
                        "content": {
                            "title": "Harvesting Rain in Semi-Arid Counties",
                            "text": "In dryland areas like Machakos and Kitui, farmers construct **tied ridges** (ridges connected by perpendicular cross-dams). Tied ridges trap 100% of storm runoff in small micro-basins, forcing rainwater to soak deeply into the root zone instead of escaping as runoff!"
                        }
                    }
                ],
                [
                    {
                        "type": "mini_activity",
                        "title": "Field Practical: Constructing Ridges vs Raised Beds",
                        "content": {
                            "title": "Hands-On Field Structural Shaping",
                            "task": "On a $2\\text{ m} \\times 2\\text{ m}$ prepared area in the school garden:\n\n1. Divide the plot into two halves.\n2. On Half A: Construct two parallel 30 cm high ridges with a central drainage furrow.\n3. On Half B: Construct one 15 cm high, 1-meter wide flat-topped raised vegetable bed using a hand rake.\n4. Discuss which local crops should be planted on each structure.",
                            "materials": ["Hand Jembe", "Hand Rake", "Measuring Tape", "Pegs and Sisal String"],
                            "safety": "Handle tools safely and maintain proper working distance."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Core Summary: Tertiary Operations",
                        "content": {
                            "title": "Key Takeaways",
                            "text": "- **Tertiary operations** are specialized, crop-specific soil-shaping tasks.\n- **Ridges (30 cm high)** are essential for tuber expansion in sweet potatoes and Irish potatoes.\n- **Raised beds (15 cm high)** prevent waterlogging and compaction in vegetable crops.\n- **Soil rolling** packs loose soil around fine grass seeds to ensure germination.\n- **Leveling** eliminates standing water hollows and ensures uniform irrigation."
                        }
                    }
                ],
                [
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Matching Tertiary Operations to Tubers",
                        "content": {
                            "question": "A farmer in Kabarnet intends to plant 1 acre of sweet potatoes on heavy clay loam soil. Why should the farmer construct raised ridges rather than planting sweet potato vines directly on a flat, un-ridged field?",
                            "options": [
                                "Ridges make sweet potato leaves grow into the clouds",
                                "Ridges provide a deep mound of loose, well-aerated soil that allows sweet potato tubers to expand without physical resistance, while preventing waterlogging root rot during heavy rains and making harvesting effortless",
                                "Sweet potato vines refuse to grow unless they are 2 meters above sea level",
                                "Ridging automatically turns clay loam soil into pure sand"
                            ],
                            "answer": "B",
                            "explanation": "Sweet potatoes develop large underground storage roots (tubers). Planting on flat, heavy clay restricts tuber expansion due to soil density and risks fatal rotting during waterlogged conditions. Raised ridges provide an aerated, loose volume of soil for unhindered tuber expansion, excellent gravitational drainage, and effortless harvesting without slicing tubers with hoes."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 6: Tool Selection and Safety
        # =====================================================================
        {
            "unit_order": 6,
            "unit_name": "Tool Selection and Safety",
            "unit_description": "Task-tool matching, essential safety rules (3-meter spacing, PPE boots/gloves, handle integrity), and tool maintenance protocols (cleaning, file sharpening, oiling rust prevention, shed storage).",
            "lesson_title": "Tool Selection, Farm Safety, and Maintenance Protocols",
            "pages": [
                [
                    {
                        "type": "suggested_image",
                        "title": "Agricultural Hand Tools for Land Preparation",
                        "content": {
                            "title": "Agricultural Hand Tools for Land Preparation",
                            "caption": "A collection of well-maintained agricultural hand tools including jembes, hoes, pangas, and rakes ready for field tillage."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Tool Safety & Maintenance",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Match specific land preparation operations with the correct **farm hand tools**.",
                                "Apply essential **field safety regulations** (including the mandatory **3-meter working distance** and PPE).",
                                "Inspect tools for physical hazards (loose, cracked, or splintered handles).",
                                "Execute routine tool maintenance: **cleaning, file sharpening, rust prevention with oil**, and proper storage."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Task-Tool Matching in Land Preparation",
                        "content": {
                            "title": "Choosing the Right Implement for Maximum Efficiency",
                            "text": "Using the wrong tool for an agricultural task causes operator fatigue, slows progress, and damages expensive equipment:\n\n- **Clearing Tall Grass**: Use a **slasher** (not a panga, which requires constant stooping and causes back strain).\n- **Chopping Woody Stems**: Use a **panga (machete)** or an **axe** for heavy logs.\n- **Primary Breaking of Hard Ground**: Use a heavy **hand jembe**.\n- **Digging Sticky Clay / Couch Grass**: Use a **fork jembe** to prevent suction drag and lift roots intact.\n- **Refining and Leveling Vegetable Beds**: Use a **hand rake**."
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "Essential Safety Rules in Tillage Operations",
                        "content": {
                            "title": "Preventing Accidents on the Farm",
                            "text": "Land preparation tools possess heavy, sharp steel heads that can inflict severe injuries if handled carelessly:\n\n1. **Maintain a 3-Meter Safe Working Distance**: When working in a group (e.g. digging with jembes or swinging slashers), maintain at least **3 meters** spacing from the nearest person to prevent accidental strikes.\n2. **Wear Personal Protective Equipment (PPE)**:\n   - *Heavy Safety Boots*: Protect toes and feet from falling tool blades or sharp rocks.\n   - *Leather Work Gloves*: Prevent palm blisters and thorn scratches.\n   - *Safety Goggles*: Shield eyes from flying wood splinters and stone chips when clearing bush.\n3. **Inspect Handles Before Use**: Never use a jembe, axe, or slasher with a loose, cracked, or splintered wooden handle. A loose metal head can fly off mid-swing with lethal velocity!\n4. **Carry Tools Correctly**: Always carry sharp tools (pangas, slashers) with blades pointed downwards and facing away from your body."
                        }
                    },
                    {
                        "type": "comparison_table",
                        "title": "Safety Protocols and Protective Measures",
                        "content": {
                            "title": "Farm Safety Standards Matrix",
                            "headers": ["Safety Risk", "Hazard Source", "Standard Precaution", "Mandatory PPE"],
                            "rows": [
                                ["Tool Collision / Swing Strikes", "Swinging jembes, axes, slashers near peers", "Maintain strict 3-meter physical spacing", "Safety Boots"],
                                ["Detached Flying Metal Heads", "Loose, cracked, or rotten wooden handles", "Inspect and wedge tool heads securely before work", "Heavy Gloves"],
                                ["Foot / Toe Severing", "Dropping heavy blades or mis-striking stones", "Keep feet spread wide behind the digging line", "Steel-toe Boots"],
                                ["Eye Splinter Injuries", "Chopping brittle branches and shattering rocks", "Clear brittle debris; swing with controlled force", "Safety Goggles / Visor"],
                                ["Palm Friction Blisters", "Prolonged gripping of rough wooden handles", "Sand smooth handles; maintain firm ergonomic grip", "Leather Work Gloves"]
                            ]
                        }
                    }
                ],
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Land Preparation Tool Safety and Maintenance Standards",
                        "content": {
                            "title": "Land Preparation Tool Safety and Maintenance Standards",
                            "caption": "Safety poster diagram illustrating the 3-meter safe working distance, proper tool carrying posture, handle wedging inspection, and the 4-step maintenance cycle (clean, dry, sharpen, oil)."
                        }
                    },
                    {
                        "type": "step_process",
                        "title": "The 4-Step Tool Maintenance and Storage Protocol",
                        "content": {
                            "title": "Routine Maintenance for Farm Tools",
                            "steps": [
                                "1. **Wash and Clean**: Immediately after field use, scrape off clinging soil and wash with clean water to prevent moisture from initiating rust.",
                                "2. **Dry Thoroughly**: Wipe metal heads dry with a clean rag.",
                                "3. **Sharpen Cutting Edges**: Use a flat metal bastard file or whetstone at a 30° angle to maintain a sharp, beveled cutting edge on pangas, slashers, and jembe blades.",
                                "4. **Apply Protective Oil**: Rub a thin film of clean vegetable oil or used engine oil over all exposed metal surfaces to seal against oxygen and moisture.",
                                "5. **Store on Wall Racks**: Hang tools neatly on peg racks in a secure, dry tool shed with sharp blades facing the wall and away from walkways."
                            ]
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "The Chemistry of Rust Prevention",
                        "content": {
                            "title": "Why Oiling Tools Stops Corrosion",
                            "text": "Farm hand tools are manufactured from carbon steel (iron alloy). When iron is exposed to atmospheric oxygen ($O_2$) and water ($H_2O$), an electrochemical oxidation reaction occurs:\n\n$$4\\text{Fe} + 3\\text{O}_2 + 6\\text{H}_2\\text{O} \\rightarrow 4\\text{Fe(OH)}_3 \\rightarrow 2\\text{Fe}_2\\text{O}_3 \\cdot 3\\text{H}_2\\text{O} \\text{ (Rust)}$$\n\n- Rust weakens the steel, causing blades to become dull, pitted, and brittle.\n- Applying oil creates an impermeable, hydrophobic barrier that seals the metal surface away from oxygen and moisture, completely halting corrosion."
                        }
                    },
                    {
                        "type": "mini_activity",
                        "title": "Practical Workshop: Restoring and Maintaining School Farm Tools",
                        "content": {
                            "title": "Tool Maintenance and Sharpening Practical",
                            "task": "In the school agriculture workshop:\n\n1. Select a dirty, rusty hand jembe.\n2. Use a wire brush to scrub away dried soil and rust scale.\n3. Secure the blade in a bench vise and use a flat file to sharpen the beveled cutting edge.\n4. Check the handle; if loose, drive a wooden/metal wedge into the handle eye.\n5. Wipe dry, apply a light coat of oil, and hang the tool on its designated shed rack.",
                            "materials": ["Rusty Hand Jembe", "Wire Brush", "Flat Metal File", "Bench Vise", "Oil & Rag"],
                            "safety": "Wear safety goggles and heavy leather gloves when filing metal."
                        }
                    }
                ],
                [
                    {
                        "type": "key_takeaway",
                        "title": "Core Summary: Tool Safety & Maintenance",
                        "content": {
                            "title": "Key Takeaways",
                            "text": "- **Match tools to tasks** to maximize efficiency and avoid back strain.\n- **Maintain a strict 3-meter working distance** during all manual digging.\n- **Inspect handles** for splits or loose heads before every work session.\n- **Clean, dry, sharpen, and oil** all metal tools to prevent rust and extend tool life.\n- **Store tools on secure racks** in a locked shed."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Tillage Safety and Maintenance",
                        "content": {
                            "question": "While leading a student practical in the school farm, you notice a student swinging a hand jembe whose metal head wobbles loosely on a cracked wooden handle. What immediate action must be taken and why?",
                            "options": [
                                "Tell the student to swing faster before the head falls off",
                                "Immediately stop the student from working; a loose metal head can fly off the handle mid-swing and cause catastrophic injury to nearby peers. The tool must be repaired by replacing the handle or driving a secure wedge into the eye before use",
                                "Pour cold water on the handle to freeze it in place",
                                "Tape the handle with paper tape and continue digging"
                            ],
                            "answer": "B",
                            "explanation": "A loose tool head on a cracked handle is an extreme safety hazard. Centrifugal force during a digging swing can cause the heavy, sharp steel head to detach and fly through the air with lethal force, striking nearby workers. The operation must be halted immediately, and the tool repaired with a new sound handle and tightly driven wedge."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 7: Zero Tillage
        # =====================================================================
        {
            "unit_order": 7,
            "unit_name": "Zero Tillage",
            "unit_description": "Definition of zero tillage (no-till farming) as conservation agriculture, seed placement mechanisms (direct seeders, punch-planters), permanent residue management, water conservation, and herbicide trade-offs.",
            "lesson_title": "Zero Tillage (No-Till) and Conservation Agriculture",
            "pages": [
                [
                    {
                        "type": "suggested_image",
                        "title": "No-Till Crop Emergence Through Crop Residue",
                        "content": {
                            "title": "No-Till Crop Emergence Through Crop Residue",
                            "caption": "Vigorous crop seedlings emerging directly through undisturbed soil covered in thick protective mulch in a zero-tillage field."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Zero Tillage",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Define **zero tillage (no-till)** as a foundational pillar of **Conservation Agriculture**.",
                                "Explain how seeds and fertilizers are placed directly into undisturbed soil using **zero-till seeders** and **hand punch-planters**.",
                                "Analyze the agronomic benefits of **permanent mulch cover** (moisture retention, erosion control, carbon buildup).",
                                "Evaluate the management challenges of zero-till, including **chemical herbicide dependence**."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "What is Zero Tillage (No-Till)?",
                        "content": {
                            "title": "Farming Without Plowing",
                            "text": "**Zero tillage** (also called no-till farming or direct drilling) is an advanced conservation farming system where the soil is left completely undisturbed from harvest to planting.\n\n- There is zero primary plowing, zero secondary harrowing, and zero tertiary bed construction.\n- The soil surface remains permanently covered by natural vegetation, thick cover crop mulch, or crop residues (stover/straw) from previous seasons.\n- Seeds are sown directly into the untilled ground through narrow, precision slits."
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "Seed Placement and Weed Management in Zero-Till",
                        "content": {
                            "title": "How No-Till Systems Operate",
                            "text": "### 1. Precision Seed Placement\n- **Tractor-Mounted Zero-Till Seeders**: Equipped with heavy, sharp rolling coulter discs that slice a narrow 2 cm slit through surface residue and soil. A seed boot drops seed and fertilizer into the slot, and a trailing press wheel firmly closes the slit.\n- **Manual Smallholder Tools (Poti-Poti / Hand Punch-Planter)**: A pointed metal jab-planter that punches individual seed holes through the mulch layer without disturbing the surrounding soil profile.\n\n### 2. Weed Management Without Tillage\n- In the absence of mechanical plowing, weeds are controlled through:\n  - **Thick Organic Mulch**: A dense blanket of crop residues blocks sunlight, preventing dormant weed seeds from germinating.\n  - **Strategic Herbicide Application**: Applying non-selective, systemic knockdown herbicides (e.g. glyphosate) prior to planting to terminate existing vegetation."
                        }
                    },
                    {
                        "type": "comparison_table",
                        "title": "Zero Tillage vs Conventional Clean Tillage",
                        "content": {
                            "title": "Tillage Systems Comparison Matrix",
                            "headers": ["Agronomic Metric", "Conventional Clean Tillage", "Zero Tillage (Conservation Agriculture)"],
                            "rows": [
                                ["Soil Disturbance", "100% of field plowed, inverted, and harrowed bare", "0% disturbance; narrow 2 cm seed slit only"],
                                ["Surface Cover", "Bare exposed soil; residues buried", "Permanent 100% cover of crop residue / mulch"],
                                ["Soil Moisture Retention", "High evaporation loss; dries rapidly", "Maximum conservation; mulch acts as vapor barrier"],
                                ["Erosion Risk", "Extreme (Wind blow & water sheet wash)", "Virtually Zero (Residues absorb raindrop energy)"],
                                ["Tractor Fuel & Labor", "High expense (Multiple mechanical passes)", "60–80% savings in diesel fuel and tractor hours"],
                                ["Weed Control Method", "Mechanical burying and harrowing", "Heavy mulch smothering + systemic herbicides"]
                            ]
                        }
                    }
                ],
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Conservation Agriculture: Zero Tillage Seed Placement & Residue Model",
                        "content": {
                            "title": "Conservation Agriculture: Zero Tillage Seed Placement & Residue Model",
                            "caption": "Cross-sectional engineering diagram showing a rolling coulter slicing through surface crop residue, depositing seed/fertilizer into undisturbed soil, and sealing the slit with a packing wheel."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Ecological Advantages and Agricultural Limitations",
                        "content": {
                            "title": "Balancing the Benefits and Trade-offs",
                            "text": "### Key Advantages\n- **Drought Resilience**: Permanent mulch cover reduces surface evaporation by up to 70%, conserving soil moisture in Kenya's semi-arid counties.\n- **Soil Biological Regeneration**: Undisturbed soil preserves earthworm burrows, mycorrhizal fungal networks, and natural crumb aggregate structures.\n- **Carbon Sequestration**: Soil organic carbon is preserved and builds steadily over decades.\n\n### Limitations & Challenges\n- **Chemical Herbicide Reliance**: Heavy dependence on chemical herbicides raises environmental and cost concerns.\n- **Equipment Capital Cost**: Specialized tractor zero-till drills are expensive for smallholder farmers.\n- **Weed Flora Shifts**: Tough perennial weeds with deep rhizomes can proliferate if not managed carefully."
                        }
                    }
                ],
                [
                    {
                        "type": "step_process",
                        "title": "Protocol: Establishing a Zero-Till Maize Field",
                        "content": {
                            "title": "Step-by-Step No-Till Establishment",
                            "steps": [
                                "1. **Harvest Previous Crop and Retain Stover**: Harvest maize/wheat and spread all straw and stover evenly across the field as mulch.",
                                "2. **Apply Knockdown Herbicide**: Spray a non-selective systemic herbicide across the field 10–14 days before planting to terminate green weeds.",
                                "3. **Direct Drill Seeds**: Use a zero-till planter or manual punch-planter to sow certified maize seeds directly through the mulch into moist undisturbed soil.",
                                "4. **Monitor Early Weed Flushes**: Hand-pull rogue weeds or apply selective post-emergence herbicides if weed pressure emerges.",
                                "5. **Maintain Continuous Residue**: Never graze cattle on the field or burn crop stover after harvest."
                            ]
                        }
                    },
                    {
                        "type": "callout",
                        "title": "Conservation Fact: The 3 Pillars of CA",
                        "content": {
                            "title": "The Global Conservation Agriculture Standard",
                            "text": "Conservation Agriculture (CA) is recognized worldwide by the FAO based on three inseparable principles: 1. Minimum soil disturbance (Zero Till), 2. Permanent organic soil cover (Mulch/Cover crops), and 3. Diversified crop rotations (Legumes + Cereals)."
                        }
                    }
                ],
                [
                    {
                        "type": "mini_activity",
                        "title": "Lab Demonstration: Runoff and Erosion in Zero-Till vs Bare Soil",
                        "content": {
                            "title": "Simulating Soil Erosion in Tillage Trays",
                            "task": "1. Prepare two wooden trays ($50\\text{ cm} \\times 30\\text{ cm}$) set at a 15° slope:\n   - Tray A: Filled with loose, finely plowed bare soil (conventional clean tillage).\n   - Tray B: Filled with untilled soil covered by a dense 5 cm layer of dry straw mulch (zero tillage).\n2. Slowly pour 2 liters of water over the top of both trays using a watering can.\n3. Collect runoff water in clear glass jars at the base.\n4. Compare water clarity: Tray A produces muddy, sediment-heavy runoff (severe erosion), while Tray B produces clear runoff with zero soil loss.",
                            "materials": ["2 Erosion Trays", "Bare Soil", "Straw Mulch", "Watering Can", "2 Glass Jars"],
                            "safety": "Clean up spilled water to prevent slipping."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Core Summary: Zero Tillage",
                        "content": {
                            "title": "Key Takeaways",
                            "text": "- **Zero tillage** leaves soil completely undisturbed, planting directly through mulch.\n- **Coulters and punch-planters** place seeds in narrow slits without plowing.\n- **Saves up to 80%** in tractor fuel and machinery wear.\n- **Dramatically cuts soil erosion** and conserves moisture in drylands.\n- **Requires careful weed management** and crop residue preservation."
                        }
                    }
                ],
                [
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Zero Tillage in Drought Conditions",
                        "content": {
                            "question": "Why does zero tillage produce significantly higher maize yields than conventional clean plowing in semi-arid regions of Kenya during seasons with erratic, low rainfall?",
                            "options": [
                                "Zero-till machines add artificial water directly to maize seeds",
                                "The permanent mulch and crop residue cover acts as a physical barrier that drastically reduces soil water evaporation, keeping the root zone moist during dry spells while untilled soil pores draw capillary water",
                                "Untilled soil repels all sunlight, keeping plants in total darkness",
                                "Zero tillage eliminates the need for crop roots to absorb water"
                            ],
                            "answer": "B",
                            "explanation": "In semi-arid drylands, water is the primary limiting factor for crop growth. Conventional clean plowing exposes bare, hot soil to the sun and wind, causing rapid evaporation of soil moisture. Zero tillage maintains a permanent protective blanket of crop residues that shields the soil from solar radiation, drastically reducing evaporation and conserving precious root zone moisture for crop survival."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 8: Minimum Tillage
        # =====================================================================
        {
            "unit_order": 8,
            "unit_name": "Minimum Tillage",
            "unit_description": "Definition of minimum tillage as a practical compromise, common techniques (strip tillage/zone tillage, stubble mulching, permanent ridges), and agronomic benefits (organic carbon preservation, 40-60% fuel savings).",
            "lesson_title": "Minimum Tillage and Strip Tillage Systems",
            "pages": [
                [
                    {
                        "type": "suggested_image",
                        "title": "Strip Tillage Demonstration on Commercial Farmland",
                        "content": {
                            "title": "Strip Tillage Demonstration on Commercial Farmland",
                            "caption": "A tractor demonstrating strip tillage, cultivating narrow 15 cm planting bands while leaving the wide inter-row spaces undisturbed and protected under crop mulch."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Minimum Tillage",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Define **minimum tillage** as a conservation system restricting soil disturbance to essential planting zones.",
                                "Analyze core minimum tillage practices: **strip tillage (zone tillage)**, **stubble mulching**, and **permanent ridges**.",
                                "Compare minimum tillage against conventional clean tillage across soil health, fuel consumption, and labor metrics.",
                                "Design a strip tillage field layout for commercial cereal and legume production."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "What is Minimum Tillage?",
                        "content": {
                            "title": "The Strategic Agronomic Compromise",
                            "text": "**Minimum tillage** is a soil conservation farming approach that minimizes the frequency, depth, and area of mechanical soil disturbance.\n\n- It serves as a practical, highly effective compromise between intensive conventional tillage (which plows 100% of the field bare) and zero tillage (which forbids all tillage).\n- In minimum tillage, soil is cultivated **only where it is strictly necessary** to place the seed and establish early roots, while the surrounding field area remains untilled and covered in protective residues."
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "Primary Minimum Tillage Techniques",
                        "content": {
                            "title": "Practical Methods in Minimum Cultivation",
                            "text": "Farmers implement minimum tillage through several proven techniques:\n\n### 1. Strip Tillage (Zone Tillage)\n- Only a narrow band or strip (**10 cm to 15 cm wide**) along each crop row is tilled to create a fine, warm seedbed.\n- The wide inter-row area (**45 cm to 60 cm**) remains completely undisturbed and blanketed with crop mulch to suppress weeds, retain moisture, and support machinery traffic without soil compaction.\n\n### 2. Stubble Mulching\n- Uses specialized tractor-drawn subterranean sweeps (wide V-shaped horizontal blades) that slide 10 cm beneath the soil surface.\n- Cuts weed roots and loosens topsoil without inverting the soil or burying the protective straw stubble on the surface.\n\n### 3. Permanent Ridges\n- Re-using existing soil ridges season after season. Only the planting crest of the ridge is lightly loosened to sow the new crop, eliminating the heavy fuel and labor cost of rebuilding ridges annually."
                        }
                    },
                    {
                        "type": "comparison_table",
                        "title": "Conventional Tillage vs Minimum Tillage Comparison",
                        "content": {
                            "title": "Tillage Systems Comparison Matrix",
                            "headers": ["Parameter", "Conventional Clean Tillage", "Minimum Tillage (Strip Tillage)"],
                            "rows": [
                                ["Cultivated Field Area", "100% of field surface disturbed", "Only 20–25% of field area disturbed (Row strips only)"],
                                ["Fuel & Machinery Costs", "High (Multiple heavy tractor passes)", "40% to 60% savings in diesel fuel and tractor hours"],
                                ["Organic Matter Retention", "Fast burnout (Oxygen spike causes rapid decay)", "Preserved within undisturbed inter-row zones"],
                                ["Soil Moisture Evaporation", "High evaporation across entire field", "Low evaporation; inter-rows act as moisture reservoir"],
                                ["Weed Seed Germination", "Brings buried dormant weed seeds to surface", "Keeps weed seeds dormant in undisturbed zones"]
                            ]
                        }
                    }
                ],
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Strip Tillage (Zone Tillage) Field Architecture",
                        "content": {
                            "title": "Strip Tillage (Zone Tillage) Field Architecture",
                            "caption": "Field layout diagram illustrating the 15 cm cultivated planting strip (fine crumb tilth with seed/fertilizer) flanked by the 45 cm undisturbed residue-covered mulch zones."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Agronomic and Financial Benefits of Minimum Tillage",
                        "content": {
                            "title": "Why Modern Agribusiness Adopts Strip Tillage",
                            "text": "1. **40% to 60% Reduction in Operational Costs**: Eliminating secondary harrowing and reducing tillage width cuts tractor fuel consumption, operator labor, and machinery maintenance in half.\n2. **Preservation of Soil Humus**: Conventional plowing aerates soil excessively, triggering a microbial feeding frenzy that rapidly oxidizes and burns off soil organic carbon as $CO_2$ gas. Minimum tillage protects soil humus inside undisturbed aggregates.\n3. **Optimal Seedling Micro-Climate**: The tilled strip warms up quickly in the morning sun to accelerate seed germination, while the mulched inter-row protects root moisture during afternoon heat."
                        }
                    }
                ],
                [
                    {
                        "type": "step_process",
                        "title": "Protocol: Setting Up a Strip-Tilled Maize and Bean Plot",
                        "content": {
                            "title": "Field Layout for Strip Tillage",
                            "steps": [
                                "1. **Map Crop Rows**: Establish parallel row lines spaced 75 cm apart using marker pegs and string.",
                                "2. **Cultivate Planting Strips**: Using a hand hoe or strip-till unit, cultivate a narrow 15 cm wide strip along each line to a depth of 15 cm.",
                                "3. **Apply Compost and Fertilizer**: Mix organic compost or basal fertilizer exclusively within the 15 cm tilled strip.",
                                "4. **Mulch Undisturbed Inter-Rows**: Cover the remaining 60 cm wide spaces between rows with dry maize stover or grass mulch.",
                                "5. **Plant Seeds**: Sow maize or bean seeds at the recommended in-row spacing within the loosened strips."
                            ]
                        }
                    },
                    {
                        "type": "callout",
                        "title": "Economics: Fuel Savings in Commercial Farming",
                        "content": {
                            "title": "Slashing Production Costs",
                            "text": "On a 100-acre commercial farm, conventional plowing and double harrowing consumes approximately 2,200 liters of diesel fuel. Transitioning to strip tillage reduces fuel consumption to under 900 liters—saving over KES 250,000 in fuel costs in a single season!"
                        }
                    }
                ],
                [
                    {
                        "type": "mini_activity",
                        "title": "Field Practical: Establishing a Strip-Tillage School Plot",
                        "content": {
                            "title": "Executing Strip Tillage on a 3m x 3m Garden Plot",
                            "task": "1. On a $3\\text{ m} \\times 3\\text{ m}$ weed-covered plot, mark three parallel planting lines spaced 75 cm apart.\n2. Dig only a narrow 15 cm strip along each line using hand hoes, creating a fine tilth.\n3. Leave the 60 cm inter-row spaces completely un-dug, and lay thick grass mulch over them.\n4. Compare physical labor and time required against fully digging a 3m x 3m plot.",
                            "materials": ["Hand Hoes", "Measuring Tape", "Sisal String & Pegs", "Dry Grass Mulch"],
                            "safety": "Maintain safe working distances during hoe work."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Core Summary: Minimum Tillage",
                        "content": {
                            "title": "Key Takeaways",
                            "text": "- **Minimum tillage** restricts cultivation exclusively to the seed row zone.\n- **Strip tillage** tills a 15 cm band while leaving 45–60 cm mulched inter-rows.\n- **Cuts fuel and labor costs by 40–60%** compared to conventional clean plowing.\n- **Preserves soil organic matter (humus)** by avoiding excessive soil aeration.\n- **Stubble mulching** uses subsurface sweeps to cut weeds without inverting trash."
                        }
                    }
                ],
                [
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Mechanism of Strip Tillage",
                        "content": {
                            "question": "How does strip tillage (zone tillage) provide the dual benefits of rapid seedling emergence and high soil conservation?",
                            "options": [
                                "It converts soil into liquid fertilizer that dissolves all weeds",
                                "The narrow 15 cm tilled strip provides a warm, loose, fine seedbed for rapid seed germination, while the wide undisturbed mulched inter-row prevents erosion, conserves soil moisture, and protects organic matter",
                                "It forces crops to grow exclusively at night",
                                "It freezes the soil to prevent insects from moving"
                            ],
                            "answer": "B",
                            "explanation": "Strip tillage combines the best features of clean tillage and zero tillage. The cultivated 15 cm strip provides a loose, warm, fine seedbed that ensures rapid seed-to-soil contact and fast seedling emergence. Meanwhile, the untilled, mulched inter-rows preserve soil moisture, block weed growth, protect soil organic matter from oxidizing, and prevent rainfall erosion."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 9: Assessing Land for a Selected Crop
        # =====================================================================
        {
            "unit_order": 9,
            "unit_name": "Assessing Land for a Selected Crop",
            "unit_description": "Pre-tillage site evaluation checklist (soil texture, slope/topography, subsoil compaction, weed flora), matching seedbed architecture to crop root systems (carrots, cabbages, potatoes, maize), and formulating tillage recommendations.",
            "lesson_title": "Pre-Tillage Site Assessment and Crop-Matching Protocols",
            "pages": [
                [
                    {
                        "type": "suggested_image",
                        "title": "Agricultural Officer Inspecting Field Soil and Crop Land",
                        "content": {
                            "title": "Agricultural Officer Inspecting Field Soil and Crop Land",
                            "caption": "An agricultural officer surveying soil compaction, slope, and weed flora on a farm field before formulating a tillage prescription."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Site Assessment",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Execute a systematic **pre-tillage site assessment** covering soil texture, slope, compaction, and weed flora.",
                                "Match specific **crop root systems** (carrots, brassicas, potatoes, maize) to customized seedbed structures.",
                                "Analyze the hazards of applying clean conventional tillage on **steep slopes (>15%)**.",
                                "Formulate a professional **Tillage Recommendation Report** for commercial agribusiness clients."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Why Conduct a Pre-Tillage Site Assessment?",
                        "content": {
                            "title": "Precision Planning Replaces Costly Mistakes",
                            "text": "Before hiring tractors or deploying manual labor, a professional farmer must systematically evaluate the physical and ecological status of the field.\n\n- Tilling blindly without assessing soil conditions leads to wasted capital (e.g. paying for subsoiling on non-compacted fields), severe erosion (e.g. clean-plowing steep hillsides), or crop failure (e.g. planting carrots in stony, unrefined clods)."
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "The 4-Point Site Assessment Checklist",
                        "content": {
                            "title": "Key Environmental Parameters to Evaluate",
                            "text": "1. **Soil Texture and Drainage**: Heavy clay soil requires raised beds or ridges to avoid waterlogging; light sandy loams can be planted on flat beds or strip-tilled.\n2. **Topography and Slope**: Steep slopes ($>15\\%$) must never be clean-plowed up and down the hill. Sloping land requires contour strip tillage, terracing, or zero tillage to prevent topsoil loss.\n3. **Soil Compaction and Hardpans**: Dig a $50\\text{ cm}$ inspection test pit. If an impermeable plow pan exists, deep **subsoiling** is mandatory before standard tillage.\n4. **Weed Flora Identification**: Fields infested with perennial rhizomatous weeds (*Couch grass, Nut sedge*) require primary digging with fork jembes to lift rhizomes intact, or pre-plant systemic herbicide application."
                        }
                    },
                    {
                        "type": "comparison_table",
                        "title": "Crop Root Systems and Required Seedbed Architecture",
                        "content": {
                            "title": "Crop-Seedbed Matching Matrix",
                            "headers": ["Crop Enterprise", "Root System Architecture", "Required Seedbed Structure", "Agronomic Rationale"],
                            "rows": [
                                ["Carrots", "Single sensitive taproot", "Deep, stone-free, ultra-fine tilth", "Stones and clods cause taproots to fork and deform"],
                                ["Sweet / Irish Potatoes", "Underground edible tubers", "25–35 cm high contour ridges", "Provides loose aerated soil for tuber expansion; prevents rot"],
                                ["Cabbages / Kales", "Fibrous nursery transplants", "15 cm high raised compost beds", "Prevents waterlogging; concentrates manure; easy weeding"],
                                ["Maize / Beans", "Strong, vigorous seedlings", "Coarse tilth or strip tillage", "Large seeds tolerate clods; prevents soil crusting capping"],
                                ["Paddy Rice", "Shallow fibrous wetland roots", "Flat, puddled impermeable clay basin", "Retains flooded standing water for weed suppression"]
                            ]
                        }
                    }
                ],
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Site Assessment & Crop-Soil Compatibility Decision Matrix",
                        "content": {
                            "title": "Site Assessment & Crop-Soil Compatibility Decision Matrix",
                            "caption": "Decision tree flowchart mapping Slope (<5% vs >15%), Soil Texture (Sand vs Clay), and Crop Type (Tubers vs Cereals vs Vegetables) to the exact tillage prescription."
                        }
                    },
                    {
                        "type": "step_process",
                        "title": "Protocol: Compiling a Farm Tillage Prescription",
                        "content": {
                            "title": "5-Step Land Preparation Planning Workflow",
                            "steps": [
                                "1. **Survey Topography**: Measure slope angle using an A-frame or inclinometer.",
                                "2. **Dig Test Pits**: Check effective topsoil depth and inspect for subsurface plow pans.",
                                "3. **Audit Weed Species**: Identify whether weeds are annual broadleaves or creeping perennial rhizomes.",
                                "4. **Select Tillage Strategy**: Choose between Zero Till, Strip Till, or Conventional Ridging based on crop and slope.",
                                "5. **Schedule Operations**: Time tillage when soil is friable—never when saturated or bone dry."
                            ]
                        }
                    }
                ],
                [
                    {
                        "type": "mini_activity",
                        "title": "Case Study: Formulating a Tillage Recommendation Report",
                        "content": {
                            "title": "Consultancy Scenario: Turning Around a Sloping Farm",
                            "task": "You are hired as an agricultural extension consultant for a 5-acre farm in Meru:\n- *Slope*: 10% gentle slope\n- *Soil*: Clay loam with high moisture retention\n- *Vegetation*: Overgrown with couch grass and thick brush\n- *Intended Crop*: Irish potatoes for commercial urban market\n\n**Your Deliverable**: In pairs, write a 1-page Tillage Prescription detailing:\n1. Recommended clearing tools.\n2. Primary tillage implement choice and weed removal strategy.\n3. Mandatory tertiary structure (ridges along contours) and why it is essential.",
                            "materials": ["Case Study Handout", "Consultancy Form Template", "Pen"],
                            "safety": "Ensure recommendations are agronomically sound and economically viable."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Core Summary: Site Assessment",
                        "content": {
                            "title": "Key Takeaways",
                            "text": "- **Site assessment** evaluates texture, slope, compaction, and weed flora before tillage.\n- **Match seedbeds to crops**: Fine tilth for carrots, Ridges for potatoes, Raised beds for kales.\n- **Never clean-till steep slopes (>15%)** to prevent catastrophic erosion.\n- **Subsoiling is required** only when test pits confirm underground hardpan compaction."
                        }
                    }
                ],
                [
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Tillage Planning on Slopes",
                        "content": {
                            "question": "A farmer is preparing a 5-acre hillside parcel with a 12% slope to plant maize. What tillage configuration should the farmer adopt to prevent severe soil loss during heavy rains?",
                            "options": [
                                "Plow straight up and down the hill with a mouldboard plough",
                                "Implement contour strip tillage or minimum tillage, establishing planting strips across the slope along the natural contours with mulched inter-row buffer strips",
                                "Burn all vegetation and spray water on the soil to make mud",
                                "Plow the entire hillside bare three times to pulverize all soil into fine dust"
                            ],
                            "answer": "B",
                            "explanation": "Plowing up and down a slope creates vertical furrows that act as drainage channels, accelerating runoff velocity and washing topsoil downhill as violent gullies. Implementing contour strip tillage places planting strips perpendicular to the slope along natural contour lines, while mulched inter-row strips act as dams to slow runoff and force rainwater into the soil."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 10: Preparing a Demonstration Plot
        # =====================================================================
        {
            "unit_order": 10,
            "unit_name": "Preparing a Demonstration Plot",
            "unit_description": "Practical planning and layout of a standard 3m x 3m agricultural demonstration plot with pegs and strings, executing the 4-step manual sequence (slashing, primary digging 20-25cm, clod breaking with fork jembe, raking/leveling), and seedbed quality control.",
            "lesson_title": "Demonstration Plot Layout and Practical Manual Tillage",
            "pages": [
                [
                    {
                        "type": "suggested_image",
                        "title": "School Demonstration Garden Plot Preparation",
                        "content": {
                            "title": "School Demonstration Garden Plot Preparation",
                            "caption": "Students working cooperatively on a standard demonstration plot, measuring boundaries with pegs, digging, breaking clods, and leveling the seedbed."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Demonstration Plot Preparation",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Plan dimensions and lay out a standard **$3\\text{ m} \\times 3\\text{ m}$ agricultural demonstration plot** using pegs and sisal string.",
                                "Execute the sequential manual tillage steps: **slashing $\\rightarrow$ primary digging $\\rightarrow$ clod breaking $\\rightarrow$ raking and leveling**.",
                                "Apply **quality control benchmarks** (tilth, cleanliness, levelness, perimeter drainage) to declare a seedbed planting-ready.",
                                "Demonstrate CBC core values of **teamwork, safety, and shared responsibility**."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Planning and Laying Out the Demonstration Plot",
                        "content": {
                            "title": "The 3m x 3m Standard School Plot",
                            "text": "Preparing a physical demonstration plot is a core CBC performance milestone in Senior Secondary Agriculture.\n\n- **Site Selection**: Select a flat or gently sloping, sunny, well-drained area on the school farm with fertile topsoil.\n- **Measuring and Pegging**: Use a 30-meter measuring tape to lay out an exact **$3\\text{ m} \\times 3\\text{ m}$ square**. Drive four wooden pegs securely into the corners and stretch a sisal string tightly between the pegs to establish straight, visible boundaries.\n- **Duty Allocation**: Assign specialized roles within your group (clearing, digging, clod breaking, composting, raking) to maximize teamwork and safety."
                        }
                    }
                ],
                [
                    {
                        "type": "step_process",
                        "title": "The 4-Step Manual Land Preparation Checklist",
                        "content": {
                            "title": "Executing Seedbed Preparation in the Plot",
                            "steps": [
                                "1. **Step 1: Slashing & Biomass Harvesting**: Use slashers to cut tall vegetation cleanly at soil level. Collect cleared biomass in a wheelbarrow and transport to the school compost pit.",
                                "2. **Step 2: Primary Digging (20–25 cm)**: Using hand jembes, dig the entire 3m x 3m plot to a depth of 20–25 cm. Lift and invert each shovel slice to bury surface residues.",
                                "3. **Step 3: Secondary Clod Breaking**: Use fork jembes to shatter large, hard soil clods into 2–3 cm crumbs. Carefully lift out any creeping couch grass stolons or roots to prevent regeneration.",
                                "4. **Step 4: Incorporating Compost & Raking**: Spread 15–20 kg of well-rotted compost across the plot. Use a hand rake to mix manure, crush surface crumbs, and drag the bed into a level plane."
                            ]
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Step-by-Step 3m x 3m Demonstration Plot Layout & Execution",
                        "content": {
                            "title": "Step-by-Step 3m x 3m Demonstration Plot Layout & Execution",
                            "caption": "Architectural field layout showing corner pegging, 3m x 3m string boundaries, primary digging depth (25 cm), fork jembe clod breaking, compost incorporation, and perimeter drainage furrow."
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "Seedbed Quality Control Benchmarks",
                        "content": {
                            "title": "Declaring the Plot Ready for Planting",
                            "text": "Before transplanting seedlings or sowing certified seeds, the group must audit the plot against four strict quality standards:\n\n1. **Tilth Quality**: The top 10 cm must have a crumbly, granular tilth suited to the target crop (fine tilth for vegetables; medium tilth for maize).\n2. **Cleanliness**: The bed must be 100% free of visible couch grass rhizomes, surface stones, plastic trash, and un-decomposed wood chunks.\n3. **Levelness**: The surface must be flat and horizontal, with zero hollows where stormwater can accumulate.\n4. **Perimeter Drainage**: A shallow 10 cm perimeter ditch dug around the plot's exterior to intercept and divert storm runoff safely away from the bed."
                        }
                    },
                    {
                        "type": "suggested_video",
                        "title": "Manual Seedbed Preparation: From Clearing to Fine Nursery Tilth",
                        "content": {
                            "title": "Manual Seedbed Preparation: From Clearing to Fine Nursery Tilth",
                            "description": "Step-by-step extension video demonstrating layout with pegs, primary jembe digging, clod breaking with fork jembes, and fine raking for vegetable production.",
                            "url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
                        }
                    }
                ],
                [
                    {
                        "type": "mini_activity",
                        "title": "Group Performance Task: Preparing a 3m x 3m Demonstration Plot",
                        "content": {
                            "title": "Field Execution and Assessment",
                            "task": "In assigned groups of 5:\n\n1. Measure, peg, and string out a $3\\text{ m} \\times 3\\text{ m}$ demonstration plot.\n2. Safely execute the complete 4-step tillage sequence (slashing $\\rightarrow$ digging $\\rightarrow$ clod breaking $\\rightarrow$ raking).\n3. Dig a shallow drainage trench around the perimeter.\n4. Present your completed seedbed to your teacher for rubric assessment on safety, tilth, and teamwork.",
                            "materials": ["Measuring Tape", "4 Wooden Pegs", "Sisal String", "Slashers", "Jembes", "Fork Jembes", "Hand Rakes", "Compost"],
                            "safety": "Maintain 3-meter safety margins. Wear safety boots and gloves."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Core Summary: Demonstration Plot Preparation",
                        "content": {
                            "title": "Key Takeaways",
                            "text": "- **Standard school plot size** is $3\\text{ m} \\times 3\\text{ m}$, pegged and aligned with strings.\n- **Follow the 4-step sequence**: 1. Slash $\\rightarrow$ 2. Dig (25 cm) $\\rightarrow$ 3. Break clods $\\rightarrow$ 4. Rake/Level.\n- **Physically remove couch grass rhizomes** to prevent rapid weed re-infestation.\n- **Quality standards**: Crumbly tilth, clean of trash, flat surface, perimeter drainage."
                        }
                    }
                ],
                [
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Uprooting Weed Rhizomes During Tillage",
                        "content": {
                            "question": "When students are breaking soil clods with a fork jembe in a 3m x 3m demonstration plot, why is it critical to physically lift out and remove creeping grass rhizomes (like couch grass) rather than chopping and burying them in the soil?",
                            "options": [
                                "Couch grass rhizomes are radioactive and destroy metal tools",
                                "Couch grass reproduces vegetatively from underground rhizome nodes; chopping and burying them will cause thousands of new grass shoots to sprout, rapidly choking the newly planted crops",
                                "Grass rhizomes turn the topsoil into solid granite",
                                "Earthworms refuse to live in soil that contains grass roots"
                            ],
                            "answer": "B",
                            "explanation": "Couch grass (*Digitaria scalarum*) and Nut sedge (*Cyperus rotundus*) are aggressive perennial weeds that reproduce vegetatively from tiny underground rhizomes and tubers. Slicing or burying rhizomes in moist soil simply propagates the weed, causing thousands of new shoots to erupt and choke the crop. Using a fork jembe to lift out the root network intact is essential for clean seedbeds."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 11: Effects of Proper Land Preparation
        # =====================================================================
        {
            "unit_order": 11,
            "unit_name": "Effects of Proper Land Preparation",
            "unit_description": "Physiological mechanisms of proper seedbed preparation: seed-to-soil capillary moisture contact, oxygen diffusion for cellular respiration, unrestricted root elongation, active nutrient transport via ATP, and early weed/pest suppression.",
            "lesson_title": "Agronomic and Physiological Impacts of Proper Seedbeds",
            "pages": [
                [
                    {
                        "type": "suggested_image",
                        "title": "Vigorous Crop Seedling Emergence in Crumbly Seedbed",
                        "content": {
                            "title": "Vigorous Crop Seedling Emergence in Crumbly Seedbed",
                            "caption": "Healthy crop seedlings emerging uniformly through loose, well-aerated, crumbly topsoil with zero physical resistance."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Physiological Effects of Tillage",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Explain how loose crumb tilth enhances **seed-to-soil contact** and accelerates seed germination.",
                                "Analyze how proper soil aeration supplies $O_2$ for root respiration and **active nutrient transport (ATP)**.",
                                "Correlate deep tillage with **unrestricted root elongation** and subsoil moisture access.",
                                "Describe how tillage physically suppresses early weed flushes and soil-borne insect pests."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Maximizing Germination and Seedling Emergence",
                        "content": {
                            "title": "The Physics and Biochemistry of Germination",
                            "text": "A properly prepared seedbed with refined, granular tilth directly governs crop germination and emergence rates:\n\n1. **Intimate Seed-to-Soil Contact**: Fine soil particles wrap snugly around the seed coat. This initiates rapid capillary water absorption (**imbibition**), which activates hydrolytic enzymes that break down starch into glucose to fuel the embryo.\n2. **Oxygen Availability for Respiration**: Loose pore channels supply continuous oxygen ($O_2$) to the germinating seed embryo to power metabolic growth.\n3. **Zero Physical Emergence Resistance**: Before a seedling can photosynthesize, it relies entirely on a fixed packet of energy stored in its cotyledons. In loose crumb tilth, the delicate plumule (shoot) pushes effortlessly to the surface without exhausting its limited energy reserves."
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "Root Architecture and Active Nutrient Uptake",
                        "content": {
                            "title": "Powering the Crop's Underground Engine",
                            "text": "The above-ground harvest is a direct reflection of the underground root architecture:\n\n### 1. Unrestricted Root Elongation and Branching\n- In deep, loose soil ($D_b < 1.3\\text{ g/cm}^3$), primary taproots grow deeply and send out extensive lateral feeding networks.\n- Deep root systems anchor heavy crop canopies against windstorms and reach deep capillary water during mid-season droughts.\n\n### 2. Oxygen-Powered Active Nutrient Transport\n- Crop root hairs absorb essential mineral ions ($H_2PO_4^-, K^+, NO_3^-, Ca^{2+}$) against steep concentration gradients through **active transport**.\n- Active transport is powered by cellular energy (**ATP**) generated during aerobic root respiration:\n\n$$\\text{Glucose } (C_6H_{12}O_6) + 6O_2 \\rightarrow 6CO_2 + 6H_2O + 38\\text{ ATP (Energy)}$$\n\n- In waterlogged or compacted soils lacking oxygen, root respiration halts, ATP generation drops to zero, and the crop starves despite high fertilizer applications!"
                        }
                    },
                    {
                        "type": "comparison_table",
                        "title": "Prepared Crumbly Seedbed vs Compacted Cloddy Soil",
                        "content": {
                            "title": "Agronomic Comparison: Seedbed Conditions",
                            "headers": ["Physiological Parameter", "Well-Prepared Crumbly Seedbed", "Compacted / Cloddy Soil"],
                            "rows": [
                                ["Capillary Water Imbibition", "Rapid & uniform across all seeds", "Slow; seeds sit in dry air voids between clods"],
                                ["Seedling Emergence Rate", "95%+ uniform emergence in 4–6 days", "<50% emergence; shoots exhaust energy underground"],
                                ["Root Architecture", "Deep, vertical taproots with dense lateral hairs", "Shallow, stunted, crooked, L-shaped roots"],
                                ["Active Nutrient Absorption", "High ATP energy; maximum N, P, K uptake", "Low oxygen; roots starve and exhibit nutrient chlorosis"],
                                ["Drought Tolerance", "Roots tap subsoil moisture; highly resilient", "Confined to top 10 cm; wilts rapidly during dry spells"]
                            ]
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "Organic Weed and Pest Suppression Mechanisms",
                        "content": {
                            "title": "Tillage as an Organic Plant Protection Tool",
                            "text": "Proper mechanical land preparation acts as an organic protection shield:\n\n- **Weed Seed Burial & Staling**: Deep plowing buries surface weed seeds beneath their germination depth while bringing dormant seeds to the surface to germinate and be destroyed during secondary harrowing before crop sowing.\n- **Pest Disruption & Solar Desiccation**: Plowing breaks underground nests of cutworms, white grubs, and stalk borers, exposing pupae to the scorching sun (thermal kill) and predatory birds (biological control)."
                        }
                    },
                    {
                        "type": "mini_activity",
                        "title": "Lab Practical: Observing Root Growth in Loose vs Compacted Soil",
                        "content": {
                            "title": "Root Penetration Bottle Experiment",
                            "task": "1. Cut the tops off two clear 1.5-liter plastic bottles:\n   - Bottle A: Fill with moist garden soil and pack it down firmly with a heavy wooden pestle (representing compacted soil).\n   - Bottle B: Fill with loose, aerated, crumbly garden soil.\n2. Plant 1 pre-germinated bean seed at a depth of 2 cm in both bottles.\n3. Place in sunlight and water equally for 10 days.\n4. Carefully cut open the bottles to inspect root length and lateral branching.",
                            "materials": ["2 Clear Plastic Bottles", "Garden Soil", "Wooden Pestle", "Bean Seeds", "Water"],
                            "safety": "Handle cutting blades with care."
                        }
                    }
                ],
                [
                    {
                        "type": "key_takeaway",
                        "title": "Core Summary: Effects of Land Preparation",
                        "content": {
                            "title": "Key Takeaways",
                            "text": "- **Fine tilth** maximizes seed-to-soil capillary moisture contact for rapid germination.\n- **Loose soil** allows delicate shoots to emerge without exhausting cotyledon energy.\n- **Soil aeration supplies oxygen** for root cellular respiration and ATP active nutrient uptake.\n- **Deep tillage** enables deep root anchoring and access to subsoil water reserves."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Soil Aeration and Active Nutrient Absorption",
                        "content": {
                            "question": "Why does a maize plant growing in heavily compacted, waterlogged soil exhibit severe yellowing and nutrient deficiency symptoms even when the soil has high concentrations of NPK fertilizer?",
                            "options": [
                                "NPK fertilizer evaporates instantly when water is present",
                                "Compacted, waterlogged soil lacks oxygen; without oxygen, root cells cannot respire to generate the metabolic energy (ATP) required for active transport of nutrient ions across root membranes",
                                "Maize plants absorb nutrients exclusively through leaf stomata",
                                "Cold water turns all plant roots into solid stone"
                            ],
                            "answer": "B",
                            "explanation": "Plant roots do not absorb mineral nutrients passively; they absorb them against concentration gradients via active transport powered by ATP. Generating ATP requires aerobic cellular respiration, which demands oxygen ($O_2$). In compacted or waterlogged soils lacking macro-pore air channels, root cells suffer oxygen starvation, ATP synthesis drops to zero, and the plant cannot absorb dissolved fertilizer ions."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 12: Synthesis and Practical Assessment
        # =====================================================================
        {
            "unit_order": 12,
            "unit_name": "Synthesis and Practical Assessment",
            "unit_description": "Holistic synthesis of land preparation systems; agribusiness economics vs ecological sustainability; 3-scenario decision matrix; CBC practical performance rubric; and Summative Topic Assessment.",
            "lesson_title": "Synthesis of Land Preparation Systems and Summative Assessment",
            "pages": [
                [
                    {
                        "type": "suggested_image",
                        "title": "Flourishing Commercial Farm Landscape in Kenya",
                        "content": {
                            "title": "Flourishing Commercial Farm Landscape in Kenya",
                            "caption": "A productive commercial farm landscape in Kenya showcasing the integrated management of seedbed preparation, contour ridging, and sustainable tillage systems."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Synthesis & Summative Assessment",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Synthesize the complete land preparation framework from clearing to tertiary operations.",
                                "Evaluate the **economic trade-offs** (fuel, labor, tractor wear) and **ecological impacts** of conventional vs conservation tillage.",
                                "Apply the **3-Scenario Tillage Decision Matrix** to solve authentic farming challenges.",
                                "Complete the comprehensive **Summative Topic Assessment** covering all 12 lessons of Topic 3."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The Land Preparation Strategic Framework",
                        "content": {
                            "title": "Balancing Agribusiness Economics with Soil Stewardship",
                            "text": "Modern agricultural producers must balance economic profitability with long-term soil health:\n\n- **Agribusiness Economics**: Land preparation represents 25% to 40% of initial crop production costs (tractor hire, diesel, labor). Over-tilling increases expenses and destroys soil structure.\n- **Ecological Sustainability**: Repeated deep inversion plowing oxidizes soil organic carbon, creates hardpans, and leaves topsoil vulnerable to wind and water erosion.\n- **Integrated Management**: Matching tillage intensity to crop physiology (e.g. fine raised beds for vegetables, contour ridges for potatoes, strip/zero till for maize) maximizes yield while minimizing production costs."
                        }
                    }
                ],
                [
                    {
                        "type": "comparison_table",
                        "title": "Tillage Decision Matrix: Matching Enterprise, Terrain & Tillage",
                        "content": {
                            "title": "Tillage Systems Decision Matrix",
                            "headers": ["Field Scenario", "Dominant Constraints", "Optimal Tillage Strategy", "Key Agronomic Justification"],
                            "rows": [
                                ["Flat 10-acre semi-arid sandy loam", "Low organic matter, erratic rain, wind erosion", "Zero Tillage / Direct Punch-Planting", "Permanent mulch cover stops evaporation and wind erosion; saves 80% fuel"],
                                ["Sloping (10%) clay loam with hardpan", "Subsoil compaction, high erosion risk, tuber crop", "Subsoiling + Contour Ridging", "Subsoiler shatters hardpan; contour ridges prevent erosion and allow tuber growth"],
                                ["Small intensive 0.5-acre vegetable plot", "High-value seeds (carrots, onions, kales)", "Manual Digging + Raised Compost Beds", "Produces fine, stone-free tilth; concentrates compost; prevents waterlogging"]
                            ]
                        }
                    }
                ],
                [
                    {
                        "type": "mini_activity",
                        "title": "Performance Task: Drafting a Comprehensive Tillage Advisory Brief",
                        "content": {
                            "title": "Consultancy Case: Turning Around a Commercial Farm",
                            "task": "You are hired as a senior agronomist for an agribusiness investor who bought a 20-acre farm in Nakuru with a gentle 6% slope. The field has an underground hardpan at 20 cm, heavy couch grass infestation, and the investor plans to grow 10 acres of hybrid maize and 10 acres of commercial Irish potatoes.\n\n**Your Deliverable**: Draft a 1-page structured Tillage Advisory Brief detailing:\n1. Pre-tillage site preparations and equipment selection.\n2. Subsoiling and primary plowing prescriptions.\n3. Differentiated seedbed structures for maize (strip tillage) vs Irish potatoes (contour ridges).\n4. A seasonal budget comparing fuel savings of your plan against conventional clean plowing.",
                            "materials": ["Case Study Handout", "Consultancy Template", "Calculator", "Pen"],
                            "safety": "Ensure realistic, professional agribusiness recommendations."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Core Summary: Land Preparation Mastery",
                        "content": {
                            "title": "Key Takeaways",
                            "text": "- **Land preparation** is the foundation of crop germination, root growth, and weed suppression.\n- **Sequential stages**: 1. Clearing $\\rightarrow$ 2. Primary Tillage $\\rightarrow$ 3. Secondary Tillage $\\rightarrow$ 4. Tertiary Operations.\n- **Conservation agriculture (Zero & Strip Till)** cuts fuel costs by 40–80% and conserves soil water in drylands.\n- **Match seedbeds to crops**: Fine tilth for carrots, Ridges for potatoes, Raised beds for vegetables."
                        }
                    }
                ],
                # Pages 4 to 8: 8 Summative Assessment MCQs
                [
                    {
                        "type": "knowledge_check",
                        "title": "Summative MCQ 1: Sequence of Land Preparation",
                        "content": {
                            "question": "Which of the following correctly outlines the chronological sequence of operations required to prepare fallow land for vegetable production?",
                            "options": [
                                "Secondary tillage -> Land clearing -> Tertiary operations -> Primary tillage",
                                "Land clearing -> Primary cultivation -> Secondary cultivation -> Tertiary operations",
                                "Tertiary operations -> Secondary tillage -> Primary plowing -> Land clearing",
                                "Primary cultivation -> Tertiary operations -> Land clearing -> Secondary tillage"
                            ],
                            "answer": "B",
                            "explanation": "The strict chronological sequence of land preparation is: 1. Land Clearing (removing surface brush/stumps) -> 2. Primary Cultivation (deep soil breaking 15-30 cm) -> 3. Secondary Cultivation (shattering clods to produce fine tilth) -> 4. Tertiary Operations (shaping beds, ridges, or furrows)."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Summative MCQ 2: Ecological Impact of Field Burning",
                        "content": {
                            "question": "Why is burning cleared vegetation (slash-and-burn) strongly discouraged in modern sustainable agriculture?",
                            "options": [
                                "Burning makes the field too bright for tractor drivers to see",
                                "Burning incinerates valuable organic matter, sterilizes beneficial soil microorganisms (earthworms, Rhizobium), damages topsoil structure, and triggers severe erosion",
                                "Burning causes all weed seeds to turn into diamond crystals",
                                "Burning instantly freezes the topsoil"
                            ],
                            "answer": "B",
                            "explanation": "Setting fire to cleared biomass incinerates valuable organic carbon, releasing it into the atmosphere as greenhouse gases instead of building soil humus. The intense heat cooks and kills beneficial soil biology (earthworms, nitrogen-fixing bacteria, mycorrhizal fungi), destroys water-stable aggregates, and leaves the bare soil vulnerable to wind and water erosion."
                        }
                    }
                ],
                [
                    {
                        "type": "knowledge_check",
                        "title": "Summative MCQ 3: Primary Tillage Implements",
                        "content": {
                            "question": "Under what specific soil conditions is a tractor disc plough preferred over a mouldboard plough for primary cultivation?",
                            "options": [
                                "On completely clean, stone-free, soft loam soil",
                                "On hard, dry, stony, sticky, or root-infested rough ground where rotating discs roll over obstructions without breaking",
                                "In flooded rice paddy basins exclusively",
                                "Only when cultivating sandy greenhouse flower pots"
                            ],
                            "answer": "B",
                            "explanation": "A disc plough features heavy, concave, rotating steel discs that cut through roots and roll over buried rocks, stumps, and hard dry ground without breaking or jamming. A mouldboard plough has a rigid static blade that catches on boulders and roots, bending or breaking the implement."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Summative MCQ 4: Resolving Underground Hardpans",
                        "content": {
                            "question": "What is an agricultural 'hardpan', and which specialized implement is used to shatter it?",
                            "options": [
                                "A hardpan is a metal cooking pot; it is removed using a garden trowel",
                                "A hardpan is a highly compacted, impermeable subsoil layer caused by continuous plowing or heavy traffic; it is shattered using a deep subsoiler (40–60 cm depth) without inverting the soil",
                                "A hardpan is a type of weed; it is sprayed with chemical herbicides",
                                "A hardpan is a puddle of rainwater on the surface; it is swept away with a broom"
                            ],
                            "answer": "B",
                            "explanation": "A hardpan (plow pan) is a dense, compacted layer formed in the subsoil due to repeated tractor plowing at a uniform depth or heavy machinery travel. It restricts root penetration and blocks vertical water drainage. A subsoiler uses a heavy, deep vertical shank (operating at 40-60 cm) to shatter and crack the hardpan without bringing infertile subsoil to the top."
                        }
                    }
                ],
                [
                    {
                        "type": "knowledge_check",
                        "title": "Summative MCQ 5: Soil Tilth and Seed Size",
                        "content": {
                            "question": "Why do small-seeded crops like carrots and onions require a fine seedbed tilth, whereas large-seeded crops like maize perform well in a coarser tilth?",
                            "options": [
                                "Small seeds are afraid of large clods and refuse to sprout",
                                "Tiny seeds have limited energy stores and require intimate seed-to-soil contact to absorb capillary moisture rapidly, whereas large seeds have strong emergence force and coarser tilth prevents soil crusting",
                                "Fine tilth causes large seeds to drown in oxygen",
                                "Carrots absorb nutrients exclusively through air pockets between clods"
                            ],
                            "answer": "B",
                            "explanation": "Small seeds have minimal endosperm energy reserves and small surface areas, requiring intimate contact with fine soil crumbs to absorb moisture through capillary action. Large seeds (maize, beans) possess substantial energy reserves and strong emergence vigor, allowing them to push through coarser clods while rough surface aggregates prevent soil crusting (capping)."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Summative MCQ 6: Agronomic Purpose of Ridging",
                        "content": {
                            "question": "What primary agronomic benefit does constructing raised ridges provide for root and tuber crops such as sweet potatoes and Irish potatoes?",
                            "options": [
                                "Ridges prevent crops from receiving any sunlight",
                                "Ridges provide a deep, loose, aerated mound of soil that allows tubers to expand without physical resistance while elevating roots to prevent waterlogging rot",
                                "Ridges cause tubers to turn into green leaves",
                                "Ridges eliminate the need for crop photosynthesis"
                            ],
                            "answer": "B",
                            "explanation": "Tubers expand underground and require low physical soil resistance. Raised ridges provide a deep volume of loose, well-aerated soil for unhindered tuber expansion, prevent waterlogging tuber rot by draining excess water into furrows, and make harvesting effortless without hoe-damage."
                        }
                    }
                ],
                [
                    {
                        "type": "knowledge_check",
                        "title": "Summative MCQ 7: Field Safety Standards",
                        "content": {
                            "question": "What is the mandatory minimum safe physical working distance that farm workers and students must maintain from each other when digging with hand jembes or swinging slashers?",
                            "options": [
                                "0.5 meters (shoulder to shoulder)",
                                "At least 3.0 meters",
                                "15.0 meters",
                                "Zero meters"
                            ],
                            "answer": "B",
                            "explanation": "When working in groups with swinging manual tools (jembes, slashers, axes), workers must maintain a minimum physical safety clearance of at least 3.0 meters (approximately two arm-and-tool lengths) to ensure that accidental tool slips or wide swings do not strike nearby peers."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Summative MCQ 8: Strip Tillage vs Clean Tillage Economics",
                        "content": {
                            "question": "Why is strip tillage considered both economically and ecologically superior to conventional clean plowing for commercial cereal production in dryland zones?",
                            "options": [
                                "Strip tillage converts tractor diesel into drinking water",
                                "Strip tillage cultivates only a narrow 15 cm planting band (saving 40–60% in tractor fuel and labor) while leaving the wide mulched inter-rows undisturbed to stop erosion and conserve soil moisture",
                                "Strip tillage eliminates the need to plant any seeds",
                                "Strip tillage freezes the soil permanently"
                            ],
                            "answer": "B",
                            "explanation": "Strip tillage restricts mechanical disturbance exclusively to a 15 cm wide planting strip (disturbing only ~20% of the field), cutting diesel fuel and machinery wear by 40–60%. The undisturbed, mulched inter-rows conserve precious soil moisture, stop wind and water erosion, preserve soil humus, and keep weed seeds dormant."
                        }
                    }
                ],
                # Page 9: Capstone Summary
                [
                    {
                        "type": "summary",
                        "title": "Topic 3 Capstone Summary: Land Preparation Mastery",
                        "content": {
                            "title": "Mastery Overview: Grade 10 Land Preparation",
                            "text": "Congratulations on completing **Topic 3: Land Preparation**!\n\nYou have mastered:\n- **Tillage Fundamentals**: The 4-stage sequence (Clearing $\\rightarrow$ Primary $\\rightarrow$ Secondary $\\rightarrow$ Tertiary) and the 5 core agronomic reasons for seedbed preparation.\n- **Land Clearing**: Tool selection (slasher, panga, axe, mattock) and the ecological imperative to compost cleared biomass rather than burn it.\n- **Primary Cultivation**: Hand/fork jembes, mouldboard vs disc plows, and deep subsoiling ($40\\text{--}60\\text{ cm}$) to shatter plow pans.\n- **Secondary Cultivation**: Producing optimal tilth (fine for carrots/onions vs coarse for maize) using rakes, harrows, and rotavators.\n- **Tertiary Operations**: Mounded contour ridges for potato tubers, raised beds for vegetables, leveling, and rolling.\n- **Conservation Agriculture**: Zero tillage direct drilling, strip tillage (40–60% fuel savings), and soil moisture conservation in drylands.\n- **Safety & Demonstration Plots**: 3-meter safety margins, PPE, tool maintenance (clean, sharpen, oil), and executing standard $3\\text{ m} \\times 3\\text{ m}$ demonstration plots."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Topic 3 Final Takeaway",
                        "content": {
                            "title": "The Agronomist's Seedbed Rule",
                            "text": "A great harvest begins before the seed is sown. Prepare the seedbed with care, match the tilth to the seed, protect the soil with conservation practices, and the land will reward you with thriving, bountiful crops."
                        }
                    }
                ]
            ]
        }
    ]

@transaction.atomic
def ingest_grade10_topic3(replace=False):
    """Executes the complete production ingestion of Grade 10 Agriculture Topic 3: Land Preparation."""
    print("=" * 80)
    print("STARTING INGESTION: CBC Grade 10 Agriculture — Topic 3: Land Preparation")
    print("=" * 80)

    curriculum = Curriculum.objects.filter(name__iexact="CBC").first()
    grade = Grade.objects.filter(curriculum=curriculum, name__icontains="10").first()
    subject = Subject.objects.filter(grade=grade, name__iexact="Agriculture").first()

    assert curriculum and grade and subject, "Curriculum/Grade/Subject not found!"

    topic_name = "Land Preparation"
    topic = Topic.objects.filter(subject=subject, name=topic_name).first()
    if not topic:
        topic = Topic.objects.create(
            subject=subject,
            name=topic_name,
            description="Comprehensive theoretical, mechanical, and practical scientific study of land preparation, tillage sequences, implements, conservation agriculture, and seedbed construction.",
            order=3
        )
        print(f"Created Topic 3: {topic.name} (ID: {topic.id})")
    else:
        topic.order = 3
        topic.description = "Comprehensive theoretical, mechanical, and practical scientific study of land preparation, tillage sequences, implements, conservation agriculture, and seedbed construction."
        topic.save()
        print(f"Resolved Topic 3: {topic.name} (ID: {topic.id})")

    if replace:
        print("Flag --replace active: Clearing existing LearningUnits and Lessons for Topic 3...")
        topic.learning_units.all().delete()
        topic.lessons.all().delete()

    curriculum_data = build_topic3_curriculum()
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
                    "topic_order": 3,
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
                    block_id=f"g10_agri_t3_u{u_order}_p{page_idx}_b{comp_idx}",
                    block_type=b_type,
                    component_type=b_type,
                    title=b_title,
                    content=b_content,
                    order=block_order_counter,
                    page_number=page_idx,
                    component_order=comp_idx,
                    page_title=b_title if comp_idx == 1 else None,
                    metadata={"topic_order": 3, "unit_order": u_order, "page": page_idx}
                )
                block_order_counter += 1
                total_blocks += 1

        print(f"  Ingested Unit {u_order}: {u_name} -> Lesson '{l_title}' ({len(pages)} Pages, {block_order_counter - 1} Blocks)")

    print("=" * 80)
    print(f"INGESTION COMPLETE: Topic 3 '{topic.name}'")
    print(f"  Total Units:   {total_units}")
    print(f"  Total Lessons: {total_lessons}")
    print(f"  Total Pages:   {total_pages}")
    print(f"  Total Blocks:  {total_blocks}")
    print("=" * 80)

if __name__ == "__main__":
    replace_flag = "--replace" in sys.argv
    ingest_grade10_topic3(replace=replace_flag)
