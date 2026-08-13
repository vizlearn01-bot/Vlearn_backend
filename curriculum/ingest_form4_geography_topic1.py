"""
VLearn Form 4 Geography — Topic 1: Land Reclamation and Rehabilitation
Authoritative High-Structure Ingestion Engine

Subject: Geography (Subject ID: 18)
Grade: Form 4 (Grade ID: 4)
Curriculum: 844 (Curriculum ID: 4)
Topic 1: Land Reclamation and Rehabilitation

Architecture:
  5 Learning Units / Lessons:
  - Lesson 1: Foundations of Land Reclamation and Rehabilitation (12 Pages)
  - Lesson 2: Irrigation Systems and Water Management (14 Pages)
  - Lesson 3: Swamp Drainage and Pest Control (14 Pages)
  - Lesson 4: Land Rehabilitation and Kenyan Irrigation Schemes (18 Pages)
  - Lesson 5: Land Reclamation in the Netherlands and Comparative Analysis (16 Pages)
  Total: 74 Pages, ~220 Granular Lesson Blocks

Features:
  - Complete fidelity to lessons.md source material
  - Automated regex cleaning of all bracket citations ([1], [121], [S1, p. 1])
  - Pedagogical flow: Locate -> Observe -> Describe -> Interpret -> Explain -> Apply
  - Clean Title Case headings, bullet points, numbered steps, comparison tables
  - Dedicated slots for 16 Vector SVGs and 4 Wikimedia Commons photographic assets
  - Idempotent and transactional database execution

Usage:
  ./venv/bin/python curriculum/ingest_form4_geography_topic1.py [--replace]
"""

import os
import sys
import re
import argparse
import django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from django.db import transaction
from curriculum.models import (
    Curriculum, Grade, Subject, Topic,
    LearningUnit, Lesson, LessonBlock
)

def clean_text(raw_str):
    """Remove source citation brackets like [1], [2, 3], [121], [S1, p. 1] and normalize whitespace."""
    if not isinstance(raw_str, str):
        return raw_str
    # Remove bracket citations like [1], [2, 3], [121], [S1, p. 1], [image_0]
    cleaned = re.sub(r'\[(?:\d+|image_\d+|S\d+.*?|[\d,\s]+)\]', '', raw_str)
    # Normalize double spaces and trim
    cleaned = re.sub(r'[ \t]+', ' ', cleaned)
    return cleaned.strip()

def clean_content_dict(data):
    """Recursively clean text within content dicts or lists."""
    if isinstance(data, str):
        return clean_text(data)
    elif isinstance(data, list):
        return [clean_content_dict(item) for item in data]
    elif isinstance(data, dict):
        return {k: clean_content_dict(v) for k, v in data.items()}
    return data


# =============================================================================
# LESSON 1 DATA — Foundations of Land Reclamation and Rehabilitation (12 Pages)
# =============================================================================
LESSON_1_DATA = {
    "unit_order": 1,
    "unit_name": "Foundations of Land Reclamation and Rehabilitation",
    "lesson_title": "Foundations of Land Reclamation and Rehabilitation",
    "pages": [
        # Page 1: Hook & Goals
        {
            "page_number": 1,
            "page_title": "Transforming Wastelands into Productive Landscapes",
            "blocks": [
                {
                    "block_type": "learning_goal",
                    "component_type": "learning_goal",
                    "title": "Module 1.1 Learning Goals",
                    "content": {
                        "text": (
                            "By the end of this lesson, you will be able to:\n\n"
                            "- Define and distinguish with precision between **Land Reclamation** and **Land Rehabilitation**\n"
                            "- Explain the critical economic and social importance of reclamation and rehabilitation in Kenya\n"
                            "- Identify and classify the general scientific methods used to reclaim wastelands and restore ruined lands\n"
                            "- Avoid common examination misconceptions regarding irrigation and reclamation"
                        )
                    }
                },
                {
                    "block_type": "suggested_image",
                    "component_type": "suggested_image",
                    "title": "Haller Park Rehabilitation Sanctuary in Mombasa",
                    "content": {
                        "text": "Lush rehabilitated tropical forest, walking trails, and wetland lakes inside the former Bamburi limestone quarry pit in Mombasa, Kenya."
                    }
                },
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "Geographic Hook: The Metamorphosis of Haller Park",
                    "content": {
                        "text": (
                            "Looking at the thriving biodiversity of Haller Park in Mombasa today—filled with towering Casuarina and neem trees, "
                            "flourishing fish ponds, and diverse wildlife—would you ever guess that this land was once an arid, barren, deep scar "
                            "in the earth left by industrial limestone quarrying?\n\n"
                            "This remarkable transformation demonstrates the power of geographical science. Human communities have the capacity "
                            "both to transform previously unusable natural wastelands into valuable assets, and to heal ecosystems that have been "
                            "severely degraded by human activity."
                        )
                    }
                }
            ]
        },
        # Page 2: Land Pressure in Kenya
        {
            "page_number": 2,
            "page_title": "The Land Pressure Crisis in Kenya",
            "blocks": [
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "Why Land Management Matters in Kenya",
                    "content": {
                        "text": (
                            "Kenya's population is expanding rapidly, creating intense competition for finite spatial resources. "
                            "The country faces a fundamental geographical challenge:\n\n"
                            "- **Only approximately 20%** of Kenya's total land area is classified as having **high-to-medium agricultural potential**.\n"
                            "- **Over 80%** of the country consists of **Arid and Semi-Arid Lands (ASALs)**, characterized by low, erratic rainfall and fragile soils.\n\n"
                            "With the national population concentrated in the arable highlands and Lake Victoria basin, land fragmentation, soil exhaustion, "
                            "and urban encroachment have created severe land shortages. Transforming uncultivated wastelands (deserts, swamps, pest bushlands) "
                            "and healing damaged landscapes (quarries, eroded hillsides) is vital for national food security and economic survival."
                        )
                    }
                },
                {
                    "block_type": "suggested_diagram",
                    "component_type": "suggested_diagram",
                    "title": "Agricultural Potential and Arable Land Distribution in Kenya",
                    "content": {
                        "text": "Thematic map of Kenya illustrating the 20% high-potential agricultural highlands versus the 80% Arid and Semi-Arid Lands (ASALs)."
                    }
                },
                {
                    "block_type": "callout",
                    "component_type": "callout",
                    "title": "Core Geographical Insight",
                    "content": {
                        "text": "Because high-potential arable land is strictly limited to 20% of Kenya's surface area, agricultural expansion can only occur through scientific reclamation of drylands and wetlands, or rehabilitation of degraded soils."
                    }
                }
            ]
        },
        # Page 3: Definition of Land Reclamation
        {
            "page_number": 3,
            "page_title": "Core Concept: Land Reclamation",
            "blocks": [
                {
                    "block_type": "definition_card",
                    "component_type": "definition_card",
                    "title": "Land Reclamation",
                    "content": {
                        "term": "Land Reclamation",
                        "definition": "The process of converting unproductive wasteland into productive agricultural or settlement land suitable for growing crops and keeping livestock."
                    }
                },
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "Characteristics of Reclaimed Land",
                    "content": {
                        "text": (
                            "In land reclamation, the target area was **previously unusable or unproductive in its natural, undisturbed state**.\n\n"
                            "Common types of wasteland requiring reclamation include:\n\n"
                            "- **Arid and Semi-Arid Lands (ASALs):** Dry deserts and scrublands lacking sufficient moisture for rainfed agriculture.\n"
                            "- **Waterlogged Swamps and Marshes:** Water-saturated depressions with oxygen-depleted soils and high flood risk.\n"
                            "- **Pest-Infested Forests and Bushlands:** Dense vegetation harbouring disease vectors such as tsetse flies and mosquitoes."
                        )
                    }
                }
            ]
        },
        # Page 4: Definition of Land Rehabilitation
        {
            "page_number": 4,
            "page_title": "Core Concept: Land Rehabilitation",
            "blocks": [
                {
                    "block_type": "definition_card",
                    "component_type": "definition_card",
                    "title": "Land Rehabilitation",
                    "content": {
                        "term": "Land Rehabilitation",
                        "definition": "The process of restoring damaged, degraded, or exhausted land back to its former productive and ecologically stable state."
                    }
                },
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "Characteristics of Rehabilitated Land",
                    "content": {
                        "text": (
                            "In land rehabilitation, the target land **was once productive**, but has subsequently been ruined or rendered barren by:\n\n"
                            "- **Human Exploitation:** Surface mining, open-cast quarrying, severe deforestation, over-cultivation, or industrial pollution.\n"
                            "- **Overgrazing:** Excessive livestock numbers exceeding the carrying capacity of the pasture, stripping vegetative cover.\n"
                            "- **Natural Degradation:** Catastrophic gully erosion, sheet wash, desertification, or topsoil depletion."
                        )
                    }
                }
            ]
        },
        # Page 5: Common Exam Trap
        {
            "page_number": 5,
            "page_title": "Exam Trap: Reclamation vs Irrigation",
            "blocks": [
                {
                    "block_type": "common_mistake",
                    "component_type": "common_mistake",
                    "title": "Do Not Equate Reclamation with Irrigation",
                    "content": {
                        "text": (
                            "A very common mistake in KCSE examination papers is writing that 'Land Reclamation is the process of irrigating dry land'.\n\n"
                            "**Why this is incorrect:** Irrigation is merely **one specific method** of land reclamation! Reclamation also includes "
                            "swamp drainage, tsetse fly eradication, mosquito control, and clearing unproductive bushlands. Always define land reclamation "
                            "broadly as the conversion of wasteland into productive agricultural or settlement land."
                        )
                    }
                },
                {
                    "block_type": "callout",
                    "component_type": "callout",
                    "title": "Summary Comparison",
                    "content": {
                        "text": "**Reclamation:** Making naturally unusable land productive for the first time.\n\n**Rehabilitation:** Restoring previously useful land that was subsequently degraded back to health."
                    }
                }
            ]
        },
        # Page 6: Primary Objectives
        {
            "page_number": 6,
            "page_title": "Primary Objectives of Reclamation in Kenya",
            "blocks": [
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "The Strategic Need for Reclamation",
                    "content": {
                        "text": (
                            "Why must national governments, development agencies, and communities invest substantial capital and engineering expertise "
                            "into land reclamation? The curriculum identifies two primary strategic objectives:\n\n"
                            "### 1. Intensify National Food Production\n"
                            "To meet the nutritional demands of Kenya's rapidly expanding population and eliminate reliance on expensive food imports, "
                            "reclamation brings previously idle semi-arid plains (e.g., Mwea, Perkerra) and drained river basins into active, high-yield cultivation.\n\n"
                            "### 2. Overcome Land Shortage and Relieve Population Pressure\n"
                            "High-potential agricultural areas such as the Central Highlands, Kisii, and the Kano Plains suffer from extreme population density "
                            "and severe land fragmentation. Reclaiming new frontiers creates fresh settlement schemes, providing landless families with productive farms."
                        )
                    }
                }
            ]
        },
        # Page 7: Overview of Methods
        {
            "page_number": 7,
            "page_title": "Classification of Land Management Methods",
            "blocks": [
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "The Dual Branches of Land Modification",
                    "content": {
                        "text": (
                            "Geographers categorize land management and modification techniques into two distinct operational branches:\n\n"
                            "- **Land Reclamation Methods (Wasteland Conversion):**\n"
                            "  1. Irrigation Farming (supplementing water in dry areas)\n"
                            "  2. Swamp Drainage (removing excess water from waterlogged soils)\n"
                            "  3. Pest Control (eradicating disease vectors like tsetse flies and mosquitoes)\n\n"
                            "- **Land Rehabilitation Methods (Restoring Degraded Land):**\n"
                            "  1. Afforestation and Reafforestation (planting trees to bind soil and restore microclimate)\n"
                            "  2. Soil Conservation Measures (terracing, grass strips, mulching, contour bunds)\n"
                            "  3. Quarry Backfilling (filling mining craters and restoring vegetative cover)\n"
                            "  4. Controlled Grazing (paddock rotation to prevent overgrazing)"
                        )
                    }
                },
                {
                    "block_type": "suggested_diagram",
                    "component_type": "suggested_diagram",
                    "title": "Classification Hierarchy of Land Management Methods",
                    "content": {
                        "text": "Conceptual branching diagram mapping Land Management into Land Reclamation (Irrigation, Swamp Drainage, Pest Control) and Land Rehabilitation (Afforestation, Soil Conservation, Quarry Filling, Controlled Grazing)."
                    }
                }
            ]
        },
        # Page 8: Interactive Scenario Sorting
        {
            "page_number": 8,
            "page_title": "Interactive Scenario Classification",
            "blocks": [
                {
                    "block_type": "mini_activity",
                    "component_type": "mini_activity",
                    "title": "Classify Real-World Kenyan Environmental Scenarios",
                    "content": {
                        "text": (
                            "**Task:** Examine the four real-world scenarios below and determine whether each represents **Land Reclamation** or **Land Rehabilitation**.\n\n"
                            "1. **Scenario A:** A construction firm fills deep open pits left behind by sand harvesting with rocks, layers fertile soil on top, and plants Casuarina seedlings.\n"
                            "   - *Classification:* **Land Rehabilitation** (Restoring land ruined by mining back to a productive state).\n\n"
                            "2. **Scenario B:** A cooperative of farmers digs canal diversion channels from the Athi River into dry, dusty semi-arid plains to cultivate onions and maize.\n"
                            "   - *Classification:* **Land Reclamation** (Converting an unproductive, naturally dry wasteland into agricultural farmland).\n\n"
                            "3. **Scenario C:** A local community digs deep open drainage trenches across the waterlogged Yala Delta marshlands to evacuate excess water for vegetable cultivation.\n"
                            "   - *Classification:* **Land Reclamation** (Converting a naturally waterlogged wetland wasteland into cultivable fields).\n\n"
                            "4. **Scenario D:** A rancher in Kajiado divides severely overgrazed and eroded pasture into fenced paddocks, rotates cattle herds, and plants vetiver grass contour strips.\n"
                            "   - *Classification:* **Land Rehabilitation** (Restoring degraded pasture land damaged by overstocking)."
                        )
                    }
                }
            ]
        },
        # Page 9: Knowledge Check 1
        {
            "page_number": 9,
            "page_title": "Knowledge Checkpoint: Core Concepts",
            "blocks": [
                {
                    "block_type": "knowledge_check",
                    "component_type": "knowledge_check",
                    "title": "Concept Diagnostic: Reclamation vs Rehabilitation",
                    "content": {
                        "check_type": "multiple_choice",
                        "question": "Which of the following scenarios is the most accurate example of Land Rehabilitation?",
                        "options": [
                            "Draining a papyrus swamp in the Lake Victoria basin to plant sugarcane",
                            "Diverting permanent river water through canals into a dry semi-arid desert",
                            "Backfilling an abandoned limestone quarry pit and planting indigenous trees",
                            "Spraying insecticide traps to clear a virgin bushland of tsetse flies"
                        ],
                        "answer": "C",
                        "explanation": "Option C is correct because quarry backfilling restores land that was previously productive but was subsequently ruined by human industrial mining (rehabilitation). Options A, B, and D represent reclamation because they convert naturally unusable wastelands (swamps, deserts, pest bushlands) into farmland."
                    }
                }
            ]
        },
        # Page 10: Knowledge Check 2
        {
            "page_number": 10,
            "page_title": "Knowledge Checkpoint: Kenya's Land Potential",
            "blocks": [
                {
                    "block_type": "knowledge_check",
                    "component_type": "knowledge_check",
                    "title": "Concept Diagnostic: National Arable Baseline",
                    "content": {
                        "check_type": "multiple_choice",
                        "question": "Approximately what percentage of Kenya's total land area is classified as high-to-medium agricultural potential?",
                        "options": [
                            "About 5%",
                            "About 20%",
                            "About 50%",
                            "About 80%"
                        ],
                        "answer": "B",
                        "explanation": "Only about 20% of Kenya's total land area possesses high-to-medium agricultural potential, leaving over 80% as Arid and Semi-Arid Lands (ASALs). This spatial imbalance creates intense population pressure and makes land reclamation indispensable."
                    }
                }
            ]
        },
        # Page 11: Summary
        {
            "page_number": 11,
            "page_title": "Foundations: Key Takeaways",
            "blocks": [
                {
                    "block_type": "summary",
                    "component_type": "summary",
                    "title": "Module 1.1 Summary",
                    "content": {
                        "text": (
                            "### Key Conceptual Takeaways\n\n"
                            "- **Land Reclamation:** The process of converting unproductive natural wastelands (deserts, swamps, pest forests) into productive agricultural and settlement land.\n"
                            "- **Land Rehabilitation:** The process of restoring ruined or degraded land (quarries, overgrazed pastures, eroded slopes) back to its former productive state.\n"
                            "- **National Imperative:** Driven by rapid population growth and the geographical constraint that only 20% of Kenya is naturally arable.\n"
                            "- **Method Taxonomy:** Reclamation encompasses irrigation, swamp drainage, and pest eradication; Rehabilitation encompasses afforestation, soil conservation, quarry restoration, and paddock grazing."
                        )
                    }
                }
            ]
        },
        # Page 12: Transition
        {
            "page_number": 12,
            "page_title": "Looking Ahead: Irrigation Systems",
            "blocks": [
                {
                    "block_type": "transition",
                    "component_type": "transition",
                    "title": "Advancing to Irrigation Systems",
                    "content": {
                        "text": (
                            "Now that you understand the conceptual foundations of land modification, we turn in Lesson 2 to the most widespread "
                            "method of dryland reclamation: **Irrigation Systems and Water Management**.\n\n"
                            "We will investigate the physical factors governing irrigation water demand, examine six distinct irrigation engineering methods, "
                            "and evaluate the multi-purpose role of dams in modern agricultural hydrology."
                        )
                    }
                }
            ]
        }
    ]
}


# =============================================================================
# LESSON 2 DATA — Irrigation Systems and Water Management (14 Pages)
# =============================================================================
LESSON_2_DATA = {
    "unit_order": 2,
    "unit_name": "Irrigation Systems and Water Management",
    "lesson_title": "Irrigation Systems and Water Management",
    "pages": [
        # Page 1: Hook & Goals
        {
            "page_number": 1,
            "page_title": "The Science of Artificial Watering",
            "blocks": [
                {
                    "block_type": "learning_goal",
                    "component_type": "learning_goal",
                    "title": "Module 1.2 Learning Goals",
                    "content": {
                        "text": (
                            "By the end of this lesson, you will be able to:\n\n"
                            "- Define irrigation and identify regions where it is geographically necessary\n"
                            "- Analyze the four physical and human factors governing irrigation water demand\n"
                            "- Describe and compare the hydraulic mechanisms of the six primary irrigation methods\n"
                            "- Evaluate the multi-purpose benefits and environmental hazards associated with irrigation dams"
                        )
                    }
                },
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "What is Irrigation?",
                    "content": {
                        "text": (
                            "**Irrigation** is the artificial application of water to land or soil to supplement inadequate rainfall, "
                            "sustain continuous crop production, or overcome seasonal dry periods.\n\n"
                            "In Kenya, irrigation is indispensable across the vast Arid and Semi-Arid Lands (ASALs), transforming water-deficient "
                            "plains into prolific commercial agricultural hubs."
                        )
                    }
                }
            ]
        },
        # Page 2: Factors Determining Water Requirements
        {
            "page_number": 2,
            "page_title": "Factors Determining Irrigation Water Requirements",
            "blocks": [
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "Why Water Requirements Differ Across Schemes",
                    "content": {
                        "text": (
                            "Irrigation schemes do not require uniform volumes of water. The exact quantity of water needed depends on four "
                            "interconnected physical and human parameters:"
                        )
                    }
                },
                {
                    "block_type": "comparison_table",
                    "component_type": "comparison_table",
                    "title": "Parameters Governing Irrigation Water Demand",
                    "content": {
                        "headers": ["Governing Factor", "How It Affects Water Demand", "Hydrological / Agronomic Principle"],
                        "rows": [
                            ["Climate", "Arid areas with high temperatures and low/unreliable rainfall require vast water volumes; humid areas require less.", "High solar radiation accelerates evapotranspiration rates from crop leaves and soil."],
                            ["Soils", "Coarse sandy soils require significantly more water than heavy clay soils.", "Sandy soils have large pore spaces and low water-retention capacity; clay soils retain moisture for extended periods."],
                            ["Crop Type", "Paddy rice requires continuous waterlogged/flooded conditions; vegetables require well-drained moist soils.", "Different crop species exhibit distinct physiological transpiration and root aeration requirements."],
                            ["Size of Fields", "Large commercial schemes require massive water volumes; smallholder market plots require modest volumes.", "Direct proportional scaling relationship between total acreage under cultivation and total hydraulic demand."]
                        ]
                    }
                }
            ]
        },
        # Page 3: Soil Texture & Hydraulics
        {
            "page_number": 3,
            "page_title": "Soil Texture and Infiltration Hydraulics",
            "blocks": [
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "Soil Physics in Irrigation Design",
                    "content": {
                        "text": (
                            "Understanding soil texture is fundamental to selecting the correct irrigation technology:\n\n"
                            "- **Sandy Soils (Coarse-Textured):** Exhibit rapid infiltration and high percolation rates. Water drains away rapidly past the root zone. "
                            "Flooding sandy soils causes massive water waste; they require frequent, localized micro-irrigation (such as trickle or drip systems).\n\n"
                            "- **Clay Soils (Fine-Textured):** Characterized by high density and tiny pore spaces. They hold immense water volumes and form impermeable seals when wet. "
                            "This high water-retention capacity makes heavy clay (such as black cotton soil) ideally suited for basin flooding in wet paddy rice cultivation."
                        )
                    }
                },
                {
                    "block_type": "callout",
                    "component_type": "callout",
                    "title": "Key Soil Principle",
                    "content": {
                        "text": "Sandy soil = Low retention + High infiltration -> Use Trickle/Drip.\nClay soil = High retention + Slow infiltration -> Use Basin/Flood."
                    }
                }
            ]
        },
        # Page 4: Overview of Six Methods
        {
            "page_number": 4,
            "page_title": "The Six Methods of Irrigation",
            "blocks": [
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "Hydraulic Classification of Irrigation Systems",
                    "content": {
                        "text": (
                            "Geographers classify irrigation into six key methods based on technological sophistication, topographic gradient, "
                            "and crop requirements:\n\n"
                            "1. Water Lifting Method (manual bucket extraction)\n"
                            "2. Flood / Basin Irrigation (field inundation enclosed by earth bunds)\n"
                            "3. Sprinkler / Overhead Irrigation (pressurized aerial spray)\n"
                            "4. Trickle Irrigation (punctured pipes at plant base)\n"
                            "5. Canal Irrigation (engineered gravity channels)\n"
                            "6. Drip Irrigation (inverted root bottles)"
                        )
                    }
                },
                {
                    "block_type": "suggested_diagram",
                    "component_type": "suggested_diagram",
                    "title": "Engineering Schematics of the Six Primary Irrigation Methods",
                    "content": {
                        "text": "Six comparative technical cross-sections illustrating water lifting, flood/basin, sprinkler/overhead, trickle pipes, open canal gravity flow, and localized bottle drip irrigation."
                    }
                }
            ]
        },
        # Page 5: Method 1 & 2
        {
            "page_number": 5,
            "page_title": "Water Lifting and Basin/Flood Irrigation",
            "blocks": [
                {
                    "block_type": "definition_card",
                    "component_type": "definition_card",
                    "title": "Water Lifting Method",
                    "content": {
                        "term": "Water Lifting Method",
                        "definition": "A low-cost, manual method where water is extracted directly from a river, well, or waterhole using buckets or watering cans and applied by hand to individual crops."
                    }
                },
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "Suitability of Water Lifting",
                    "content": {
                        "text": (
                            "**Suitability:** Widely practiced by smallholder farmers on vegetable plots and market gardens immediately adjacent to a permanent river or shallow water table. "
                            "It requires minimal capital investment but is labor-intensive and limited to small acreages."
                        )
                    }
                },
                {
                    "block_type": "definition_card",
                    "component_type": "definition_card",
                    "title": "Flood / Basin Irrigation",
                    "content": {
                        "term": "Flood / Basin Irrigation",
                        "definition": "A surface irrigation method where river water is diverted into feeder canals and channeled onto flat fields enclosed by low earth retaining walls (bunds), submerging the entire soil surface."
                    }
                },
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "Suitability of Basin Irrigation",
                    "content": {
                        "text": (
                            "**Suitability:** The standard method used in large-scale government irrigation schemes (such as Mwea and Ahero). It requires flat terrain for uniform water spreading "
                            "and heavy clay soils (black cotton soil) that retain standing water for waterlogged crops like wet paddy rice."
                        )
                    }
                }
            ]
        },
        # Page 6: Method 3 & 4
        {
            "page_number": 6,
            "page_title": "Sprinkler and Trickle Irrigation",
            "blocks": [
                {
                    "block_type": "definition_card",
                    "component_type": "definition_card",
                    "title": "Sprinkler / Overhead Irrigation",
                    "content": {
                        "term": "Sprinkler / Overhead Irrigation",
                        "definition": "A pressurized system where water is pumped through buried or surface pipes and sprayed into the air through rotating nozzles, falling onto crops like natural rainfall."
                    }
                },
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "Suitability of Sprinkler Irrigation",
                    "content": {
                        "text": (
                            "**Suitability:** Widely used on undulating terrain where leveling land for flood irrigation would cause severe soil erosion. "
                            "Commonly used on commercial horticultural farms, coffee estates, and recreational golf courses."
                        )
                    }
                },
                {
                    "block_type": "definition_card",
                    "component_type": "definition_card",
                    "title": "Trickle Irrigation",
                    "content": {
                        "term": "Trickle Irrigation",
                        "definition": "An advanced micro-irrigation system where flexible plastic pipes perforated with tiny emitter holes are laid along crop rows, releasing water drop-by-drop directly at the base of each plant."
                    }
                },
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "Suitability of Trickle Irrigation",
                    "content": {
                        "text": (
                            "**Suitability:** The premier method in commercial floriculture and high-value export horticulture (e.g., cut roses and carnations around Lake Naivasha). "
                            "It achieves near 100% water-use efficiency with minimal evaporation losses."
                        )
                    }
                }
            ]
        },
        # Page 7: Method 5 & 6
        {
            "page_number": 7,
            "page_title": "Canal Diversion and Bottle Drip Irrigation",
            "blocks": [
                {
                    "block_type": "definition_card",
                    "component_type": "definition_card",
                    "title": "Canal Irrigation",
                    "content": {
                        "term": "Canal Irrigation",
                        "definition": "An open-channel hydraulic system where water is diverted from a permanent river or dam and conveyed through engineered earth or concrete channels across arid plains by gravity flow."
                    }
                },
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "Suitability of Canal Irrigation",
                    "content": {
                        "text": (
                            "**Suitability:** Extensively used to convey bulk water over long distances across semi-arid plains. A prime historical Kenyan example is the "
                            "**Yatta Canal** in Machakos, which diverts water from the Thika River to sustain agricultural communities across the dry Yatta Plateau."
                        )
                    }
                },
                {
                    "block_type": "definition_card",
                    "component_type": "definition_card",
                    "title": "Inverted Bottle Drip Irrigation",
                    "content": {
                        "term": "Bottle Drip Irrigation",
                        "definition": "A low-cost, grassroots conservation technique where recycled plastic or glass bottles filled with water are inverted directly into the soil next to a plant's root system."
                    }
                },
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "Suitability of Bottle Drip Irrigation",
                    "content": {
                        "text": (
                            "**Suitability:** Highly effective for smallholders in drought-prone ASAL regions growing young fruit trees, localized vegetable patches, or domestic tree nurseries with zero capital."
                        )
                    }
                }
            ]
        },
        # Page 8: Water Management & Dams
        {
            "page_number": 8,
            "page_title": "Water Management: Multi-Purpose Dams",
            "blocks": [
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "Controlling River Hydrology with Dams",
                    "content": {
                        "text": (
                            "Because river discharge in tropical environments fluctuates drastically between rainy and dry seasons, relying on natural river flow alone "
                            "causes severe water deficits during crop maturation. Geographers and engineers construct concrete or earth dams across river valleys "
                            "to impound water in large artificial reservoirs.\n\n"
                            "These reservoirs regulate seasonal flow, store excess floodwaters, and ensure a reliable, continuous year-round gravity supply for feeder canals."
                        )
                    }
                },
                {
                    "block_type": "suggested_diagram",
                    "component_type": "suggested_diagram",
                    "title": "Cross-Section and Hydraulic Features of a Multi-Purpose Dam",
                    "content": {
                        "text": "Cross-section of a concrete dam wall across a river valley showing the upstream reservoir, control sluice gates, irrigation canal intake, sediment accumulation basin, and integrated HEP turbine penstocks."
                    }
                }
            ]
        },
        # Page 9: Evaluation of Dams
        {
            "page_number": 9,
            "page_title": "Economic and Ecological Evaluation of Dams",
            "blocks": [
                {
                    "block_type": "comparison_table",
                    "component_type": "comparison_table",
                    "title": "Multi-Purpose Benefits vs Environmental Hazards of Dams",
                    "content": {
                        "headers": ["Dimension", "Specific Geographical Impact", "Underlying Mechanism"],
                        "rows": [
                            ["Advantage", "Hydroelectric Power (HEP) Generation", "Falling water from the reservoir head drives water turbines connected to electrical generators."],
                            ["Advantage", "Commercial Fish Farming (Aquaculture)", "Large artificial reservoirs provide ideal habitats for stocking Tilapia, Nile perch, and Carp."],
                            ["Advantage", "Domestic and Industrial Water Supply", "Impounded fresh water is treated and piped to adjacent urban centers and rural settlements."],
                            ["Advantage", "Downstream Flood Mitigation", "Dams absorb peak storm discharge, preventing destructive seasonal river flooding downstream."],
                            ["Hazard", "Waterborne Disease Proliferation", "Stagnant, slow-moving reservoir water creates vast breeding grounds for Anopheles mosquitoes (Malaria) and freshwater snails (Bilharzia)."],
                            ["Hazard", "Risk of Drowning", "Unfenced reservoir shores and deep canals present continuous drowning hazards to local residents and livestock."],
                            ["Hazard", "Catastrophic Dam Breakage", "Structural failure or extreme silt-induced overtopping can unleash catastrophic flash floods, destroying downstream settlements and farmland."]
                        ]
                    }
                }
            ]
        },
        # Page 10: Interactive Extension Activity
        {
            "page_number": 10,
            "page_title": "Agricultural Extension Decision Matrix",
            "blocks": [
                {
                    "block_type": "mini_activity",
                    "component_type": "mini_activity",
                    "title": "Agricultural Officer Advisory Challenge",
                    "content": {
                        "text": (
                            "**Scenario:** You are an agricultural extension officer in Kenya advising three distinct farming operations. Recommend the optimal irrigation method for each:\n\n"
                            "1. **Farmer Onyango:** Cultivating high-value export carnations on loose sandy soil where water is scarce and expensive.\n"
                            "   - *Recommendation:* **Trickle Irrigation** (Sandy soil drains rapidly; trickle lines deliver water directly to the root zone with zero evaporation waste).\n\n"
                            "2. **Farmer Mutua:** Managing a small 0.25-acre cabbage patch immediately on the bank of the Athi River with very limited capital.\n"
                            "   - *Recommendation:* **Water Lifting Method** (Proximity to the river and small plot size make manual buckets cheap, effective, and free of expensive infrastructure).\n\n"
                            "3. **National Irrigation Board (NIB):** Establishing a 5,000-hectare commercial rice scheme on flat alluvial clay plains.\n"
                            "   - *Recommendation:* **Flood / Basin Irrigation** (Paddy rice requires 10cm standing water, flat terrain permits uniform flooding, and heavy clay soil holds water without rapid percolation)."
                        )
                    }
                }
            ]
        },
        # Page 11: Field Evidence Yatta Canal
        {
            "page_number": 11,
            "page_title": "Field Evidence: The Yatta Canal Scheme",
            "blocks": [
                {
                    "block_type": "suggested_image",
                    "component_type": "suggested_image",
                    "title": "Engineered Water Diversion along the Yatta Canal in Machakos",
                    "content": {
                        "text": "Open engineered canal channel diverting river water across semi-arid plains to sustain smallholder farming on the Yatta Plateau."
                    }
                },
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "The Yatta Canal: Transforming the Plateau",
                    "content": {
                        "text": (
                            "The **Yatta Canal** in Machakos County represents one of Kenya's most famous gravity-fed canal reclamation projects. "
                            "Constructed to divert water from the Thika and Athi river catchments, the 60-kilometer open canal cuts across the dry, rain-deficient "
                            "Yatta Plateau.\n\n"
                            "By harnessing natural gravitational head, the canal delivers continuous fresh water to thousands of smallholder farmers, "
                            "turning an otherwise drought-stricken landscape into an oasis of maize, fruit orchards, and horticulture."
                        )
                    }
                }
            ]
        },
        # Page 12: Knowledge Check 1
        {
            "page_number": 12,
            "page_title": "Knowledge Checkpoint: Irrigation Hydraulics",
            "blocks": [
                {
                    "block_type": "knowledge_check",
                    "component_type": "knowledge_check",
                    "title": "Concept Diagnostic: Soil and Method Selection",
                    "content": {
                        "check_type": "multiple_choice",
                        "question": "Why is Flood/Basin irrigation particularly suitable for paddy rice cultivation on black cotton clay soil?",
                        "options": [
                            "Sandy soil allows rapid infiltration, keeping the plant roots aerated",
                            "Black cotton clay soil has high water retention and becomes impermeable, maintaining the flooded conditions required by rice",
                            "Basin irrigation relies on pressurized pipes that spray water over large areas",
                            "Clay soil causes rapid evaporation, cooling the surrounding microclimate"
                        ],
                        "answer": "B",
                        "explanation": "Paddy rice requires waterlogged or flooded conditions. Black cotton clay soil consists of extremely fine particles that swell when wet, forming an impermeable layer that prevents water from percolating away. Combined with flat terrain and earth bunds, basin flooding maintains the required water depth efficiently."
                    }
                }
            ]
        },
        # Page 13: Knowledge Check 2
        {
            "page_number": 13,
            "page_title": "Knowledge Checkpoint: Multi-Purpose Dams",
            "blocks": [
                {
                    "block_type": "knowledge_check",
                    "component_type": "knowledge_check",
                    "title": "Concept Diagnostic: Evaluating Dam Impacts",
                    "content": {
                        "check_type": "multiple_choice",
                        "question": "Which of the following is a major environmental hazard directly caused by the creation of large, stagnant irrigation reservoirs?",
                        "options": [
                            "Severe soil salinity caused by rapid wind erosion",
                            "Proliferation of disease vectors such as mosquitoes (Malaria) and snails (Bilharzia)",
                            "Immediate collapse of downstream fish populations due to excess river oxygen",
                            "Reduction in national Hydroelectric Power generating capacity"
                        ],
                        "answer": "B",
                        "explanation": "Stagnant and slow-moving water bodies created by artificial reservoirs act as fertile breeding grounds for Anopheles mosquitoes, which transmit Malaria, and aquatic snails, which serve as intermediate hosts for Bilharzia (Schistosomiasis)."
                    }
                }
            ]
        },
        # Page 14: Summary
        {
            "page_number": 14,
            "page_title": "Irrigation Systems: Key Takeaways",
            "blocks": [
                {
                    "block_type": "summary",
                    "component_type": "summary",
                    "title": "Module 1.2 Summary",
                    "content": {
                        "text": (
                            "### Key Conceptual Takeaways\n\n"
                            "- **Definition:** Irrigation is the artificial application of water to sustain continuous agriculture in drylands or during dry seasons.\n"
                            "- **Demand Factors:** Water requirement is governed by Climate (evaporation rate), Soils (sand vs clay retention), Crop Type (paddy vs vegetables), and Field Size.\n"
                            "- **Method Taxonomy:** 6 primary methods spanning manual water lifting, basin flooding, overhead sprinklers, trickle emitter lines, open gravity canals, and localized bottle drip.\n"
                            "- **Dam Hydrology:** Multi-purpose dams provide continuous irrigation water, generate HEP, support fish farming, and control floods, but carry risks of vector-borne diseases and dam breach."
                        )
                    }
                }
            ]
        }
    ]
}


# =============================================================================
# LESSON 3 DATA — Swamp Drainage and Pest Control (14 Pages)
# =============================================================================
LESSON_3_DATA = {
    "unit_order": 3,
    "unit_name": "Swamp Drainage and Pest Control",
    "lesson_title": "Swamp Drainage and Pest Control",
    "pages": [
        # Page 1: Hook & Goals
        {
            "page_number": 1,
            "page_title": "Reclaiming Wet and Pest-Infested Lands",
            "blocks": [
                {
                    "block_type": "learning_goal",
                    "component_type": "learning_goal",
                    "title": "Module 1.3 Learning Goals",
                    "content": {
                        "text": (
                            "By the end of this lesson, you will be able to:\n\n"
                            "- Explain the environmental and agronomic problems caused by waterlogged soils\n"
                            "- Describe the three scientific engineering processes used in swamp drainage\n"
                            "- Analyze the objectives and achievements of the Yala and Bunyala drainage schemes\n"
                            "- Explain how controlling pests (mosquitoes, rodents, and tsetse flies) constitutes land reclamation\n"
                            "- Evaluate the multi-tier ICIPE tsetse fly control program in East Africa"
                        )
                    }
                },
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "The Dual Obstacles: Excess Water and Insect Vectors",
                    "content": {
                        "text": (
                            "While irrigation addresses areas with too little water, vast tracts of high-potential land in Kenya cannot be farmed "
                            "because they contain **too much water** (swamps and marshes) or are overrun by **deadly biological vectors** (tsetse flies and mosquitoes).\n\n"
                            "Reclaiming these lands requires specialized drainage hydraulics and biological vector management."
                        )
                    }
                }
            ]
        },
        # Page 2: Problems of Waterlogged Land
        {
            "page_number": 2,
            "page_title": "The Geography of Waterlogged Lands",
            "blocks": [
                {
                    "block_type": "definition_card",
                    "component_type": "definition_card",
                    "title": "Swamp",
                    "content": {
                        "term": "Swamp",
                        "definition": "A wetland feature characterized by permanently or seasonally waterlogged, saturated soil dominated by water-tolerant vegetation such as reeds, papyrus, and sedges."
                    }
                },
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "Agronomic Problems of Excess Soil Water",
                    "content": {
                        "text": (
                            "Why are natural swamps unsuitable for conventional crop farming?\n\n"
                            "1. **Root Hypoxia (Oxygen Starvation):** Saturated soils fill all pore spaces with water, excluding atmospheric oxygen. "
                            "Most crop root systems cannot respire in anaerobic soils, causing root rot and crop failure.\n\n"
                            "2. **Vector and Pathogen Habitats:** Warm, stagnant wetland waters create extensive breeding zones for disease vectors, "
                            "especially malaria-carrying mosquitoes and bilharzia-transmitting snails.\n\n"
                            "3. **Severe Flooding Hazards:** Low-lying swamp basins receive uncontrolled runoff from surrounding highlands, causing seasonal inundation "
                            "that destroys settlements, livestock, and infrastructure."
                        )
                    }
                }
            ]
        },
        # Page 3: Three Drainage Processes
        {
            "page_number": 3,
            "page_title": "Three Mechanisms of Swamp Drainage",
            "blocks": [
                {
                    "block_type": "step_process",
                    "component_type": "step_process",
                    "title": "Engineering Mechanisms of Swamp Drainage",
                    "content": {
                        "procedure": [
                            "Digging Open Drainage Ditches and Trenches: A network of open, graded ditches is excavated across the wetland. Water seeps out of the saturated soil into the ditches and drains away by natural gravity into permanent river channels.",
                            "Planting Eucalyptus Bio-Drainage Trees: Eucalyptus trees possess exceptionally high transpiration rates, absorbing massive volumes of ground water through deep taproots and transpiring it into the atmosphere to systematically lower the water table.",
                            "Laying Subsurface Perforated Drainage Pipes: Flexible or clay pipes perforated with small entry holes are buried at the base of deep trenches. Excess groundwater infiltrates into the pipes and flows away underground by gravity, leaving the topsoil dry and cultivable."
                        ]
                    }
                },
                {
                    "block_type": "suggested_diagram",
                    "component_type": "suggested_diagram",
                    "title": "Mechanisms of Swamp Drainage and Water Table Drawdown",
                    "content": {
                        "text": "Three-part hydraulic cross-section comparing open gravity ditches, eucalyptus bio-transpiration pumping, and subsurface perforated pipe grids lowering the subterranean water table."
                    }
                }
            ]
        },
        # Page 4: Biological Drainage Case Study
        {
            "page_number": 4,
            "page_title": "Bio-Drainage: Eucalyptus at Kakuzi (Makuyu)",
            "blocks": [
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "The Kakuzi Bio-Drainage Model",
                    "content": {
                        "text": (
                            "A prominent Kenyan case study in biological drainage is found at **Kakuzi in Makuyu (Murang'a County)**.\n\n"
                            "To reclaim unproductive, waterlogged valley bottoms without incurring massive earth-moving costs, extensive plantations of "
                            "**Eucalyptus trees** were established across the wet terrain. Due to their aggressive rooting depth and extraordinarily rapid transpiration rates, "
                            "the eucalyptus trees effectively acted as living biological water pumps, drying out the swampy valleys and converting them into "
                            "productive agricultural and agroforestry land."
                        )
                    }
                },
                {
                    "block_type": "callout",
                    "component_type": "callout",
                    "title": "Environmental Caution with Eucalyptus",
                    "content": {
                        "text": "While eucalyptus is a superb tool for drying swamps, planting it near freshwater springs, wetlands, or riverbanks in dry areas can dangerously deplete the water table and dry up local community streams."
                    }
                }
            ]
        },
        # Page 5: Yala and Bunyala Schemes
        {
            "page_number": 5,
            "page_title": "Case Study: Yala and Bunyala Drainage Schemes",
            "blocks": [
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "Reclaiming the Lake Victoria Lowlands",
                    "content": {
                        "text": (
                            "The **Yala and Bunyala Drainage Schemes** represent Kenya's largest national swamp drainage projects:\n\n"
                            "- **Location:** Reclaimed lands are situated on the lower courses of **River Yala** (Yala Delta) and **River Nzoia** (Bunyala) in Western Kenya, adjacent to Lake Victoria.\n"
                            "- **Timeline:** Conceived and launched in **1970** by the national government in partnership with international development agencies.\n"
                            "- **Hydraulic Strategy:** Construction of diversion canals, dykes, and deep drainage channels to evacuate floodwaters from the vast papyrus swamps."
                        )
                    }
                },
                {
                    "block_type": "suggested_diagram",
                    "component_type": "suggested_diagram",
                    "title": "Spatial Layout of the Yala Delta and Bunyala Drainage Schemes",
                    "content": {
                        "text": "Spatial map of western Kenya showing Lake Victoria, River Yala, River Nzoia, the Kano Plains, flood diversion dykes, and the 800-hectare reclaimed agricultural boundary."
                    }
                }
            ]
        },
        # Page 6: Objectives vs Achievements Yala/Bunyala
        {
            "page_number": 6,
            "page_title": "Evaluation of Yala and Bunyala Schemes",
            "blocks": [
                {
                    "block_type": "comparison_table",
                    "component_type": "comparison_table",
                    "title": "Strategic Objectives vs Tangible Achievements of Yala/Bunyala",
                    "content": {
                        "headers": ["Project Parameter", "Strategic Objective", "Tangible Achievement Realized"],
                        "rows": [
                            ["Agricultural Expansion", "Drain waterlogged marshlands to create new fertile farmland for crop cultivation and livestock.", "Over 800 hectares of prime land successfully reclaimed for maize, beans, and vegetable farming."],
                            ["Population Pressure", "Relieve severe human congestion on the densely populated Kano Plains by opening new settlement frontiers.", "Hundreds of landless families resettled on planned agricultural plots."],
                            ["Flood Mitigation", "Control destructive seasonal river inundations from the lower Nzoia and Yala river catchments.", "Engineered flood dykes and diversion canals have significantly reduced downstream flood disasters."],
                            ["Disease Control", "Eradicate breeding habitats for disease vectors (mosquitoes, tsetse flies, snails).", "Substantial reduction in local incidence of Malaria and Bilharzia across the reclaimed delta."],
                            ["Infrastructure", "Open up a remote, marshy, and inaccessible area to national trade and transport.", "Road networks, drainage canals, and market trading centers established throughout the basin."]
                        ]
                    }
                }
            ]
        },
        # Page 7: Pest Control as Reclamation
        {
            "page_number": 7,
            "page_title": "Pest Control as a Form of Land Reclamation",
            "blocks": [
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "Why Pest Eradication is Land Reclamation",
                    "content": {
                        "text": (
                            "Pests render hundreds of square kilometers of fertile land completely uninhabitable and agriculturally idle. "
                            "Controlling agricultural and medical vectors is therefore a direct form of **Land Reclamation**—it transforms uninhabitable wastelands "
                            "into safe zones for human settlement and farming.\n\n"
                            "### Control of Mosquitoes\n"
                            "- Fumigation and residual chemical spraying in houses\n"
                            "- Draining stagnant pools and marshes to eliminate breeding habitats\n"
                            "- Clearing overgrown bush and grass near human homesteads\n\n"
                            "### Control of Rodents, Birds, and Mammalian Pests\n"
                            "- Mechanical trapping, rodenticides, and bait poisoning\n"
                            "- Visual scarecrows, noise explosives, and hunting in grain fields"
                        )
                    }
                }
            ]
        },
        # Page 8: Tsetse Fly Menace
        {
            "page_number": 8,
            "page_title": "The Tsetse Fly Challenge in East Africa",
            "blocks": [
                {
                    "block_type": "definition_card",
                    "component_type": "definition_card",
                    "title": "Tsetse Fly (Glossina)",
                    "content": {
                        "term": "Tsetse Fly",
                        "definition": "A blood-sucking dipteran insect vector that transmits Trypanosomes, causing lethal Sleeping Sickness (Trypanosomiasis) in humans and Nagana in cattle."
                    }
                },
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "Habitat and Geographic Distribution",
                    "content": {
                        "text": (
                            "Tsetse flies require warm, humid climates and dense, shaded bushy vegetation for resting and breeding. "
                            "Prominent tsetse fly-infested territories in East Africa include the **Lambwe Valley in Kenya** (surrounding Ruma National Park) "
                            "and the vast **Miombo Woodlands in Tanzania**.\n\n"
                            "In these zones, the presence of tsetse flies historically prevented cattle rearing and forced human abandonment of highly fertile soils."
                        )
                    }
                }
            ]
        },
        # Page 9: ICIPE Programme
        {
            "page_number": 9,
            "page_title": "The ICIPE Tsetse Eradication Programme",
            "blocks": [
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "Scientific Vector Management by ICIPE",
                    "content": {
                        "text": (
                            "The **International Centre of Insect Physiology and Ecology (ICIPE)** spearheaded groundbreaking integrated tsetse fly eradication programs "
                            "across East Africa, notably at the Miombo Woodland and the Lambwe Valley.\n\n"
                            "### Strategic Objectives of the ICIPE Program:\n"
                            "1. **Eliminate the insect vector** to release fertile, unused land for agricultural cultivation and livestock settlement.\n"
                            "2. **Treat infected humans and cattle** to arrest the transmission cycle of sleeping sickness and Nagana.\n"
                            "3. **Develop environmentally sustainable, non-polluting vector control technologies** that avoid broad-spectrum chemical insecticides."
                        )
                    }
                }
            ]
        },
        # Page 10: Six Tsetse Control Methods
        {
            "page_number": 10,
            "page_title": "Six Scientific Tsetse Eradication Methods",
            "blocks": [
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "Integrated Tsetse Management Measures",
                    "content": {
                        "text": (
                            "ICIPE and regional vector authorities deployed an integrated six-stage strategy:\n\n"
                            "1. **Selective Bush Clearing:** Removing low, shaded undergrowth without clear-felling large trees. This removes the humid breeding microclimate, exposing adult flies and pupae to solar desiccation.\n"
                            "2. **Ground and Aerial Insecticide Spraying:** Targeted spraying of synthetic pyrethroids (previously DDT, which was phased out due to toxic bioaccumulation in food chains).\n"
                            "3. **Sterilisation of Males (Sterile Insect Technique):** Male tsetse flies are bred, sterilized using radiation or chemicals, and released. Mating with wild females yields no offspring, causing population collapse.\n"
                            "4. **Insecticide-Impregnated Cloth Traps:** Deploying blue-and-black cloth traps coated with biodegradable insecticide or adhesive. The dark silhouette mimics an animal host, attracting and killing the flies.\n"
                            "5. **Creation of 5 km Buffer Zones:** Clearing a wide 5-kilometer corridor of dense bush and converting it to active cropland. Tsetse flies cannot cross this wide, sunlit barrier.\n"
                            "6. **Selective Culling of Wild Host Reservoirs:** Regulated control of wild animal hosts (e.g., bushbucks, warthogs) that provide blood meals for the fly population."
                        )
                    }
                },
                {
                    "block_type": "suggested_diagram",
                    "component_type": "suggested_diagram",
                    "title": "ICIPE Tsetse Fly Trap Mechanism and Buffer Zone Barrier",
                    "content": {
                        "text": "Technical diagram showing the optical attraction mechanism of the blue-and-black cloth tsetse fly trap and the 5km cleared agricultural buffer zone ecological barrier."
                    }
                }
            ]
        },
        # Page 11: Interactive Case Study
        {
            "page_number": 11,
            "page_title": "Interactive Vector Analysis",
            "blocks": [
                {
                    "block_type": "mini_activity",
                    "component_type": "mini_activity",
                    "title": "Case Study Analysis: Why Integrated Control Succeeded",
                    "content": {
                        "text": (
                            "**Historical Analysis:** In early colonial tsetse eradication programs, authorities relied almost exclusively on wide-scale DDT aerial spraying. "
                            "Within several years, tsetse populations rebounded while beneficial honeybees and bird species were decimated.\n\n"
                            "**Geographical Question:** Why was ICIPE's integrated multi-tier approach (traps + sterilization + buffer zones) vastly more successful?\n\n"
                            "- *Answer:* Integrated vector management combines biological barriers (buffer zones that flies cannot cross), species-specific traps (zero collateral damage to bees), and population genetics (sterile males), providing permanent eradication without toxic chemical pollution."
                        )
                    }
                }
            ]
        },
        # Page 12: Knowledge Check 1
        {
            "page_number": 12,
            "page_title": "Knowledge Checkpoint: Swamp Drainage",
            "blocks": [
                {
                    "block_type": "knowledge_check",
                    "component_type": "knowledge_check",
                    "title": "Concept Diagnostic: Drainage Mechanisms",
                    "content": {
                        "check_type": "multiple_choice",
                        "question": "How did the planting of Eucalyptus plantations at Kakuzi successfully reclaim waterlogged valley lands?",
                        "options": [
                            "Eucalyptus roots chemically neutralize acidic peat soils",
                            "Eucalyptus trees have exceptionally high transpiration rates, extracting massive volumes of groundwater and lowering the water table",
                            "Eucalyptus leaves create a canopy that completely blocks rainwater from reaching the soil",
                            "Eucalyptus bark releases natural insecticides that kill all subterranean burrowing insects"
                        ],
                        "answer": "B",
                        "explanation": "Eucalyptus species possess deep taproots and an extraordinarily high rate of transpiration. They absorb large quantities of moisture from waterlogged soil and release it into the atmosphere as water vapor, effectively functioning as living biological drainage pumps."
                    }
                }
            ]
        },
        # Page 13: Knowledge Check 2
        {
            "page_number": 13,
            "page_title": "Knowledge Checkpoint: Tsetse Eradication",
            "blocks": [
                {
                    "block_type": "knowledge_check",
                    "component_type": "knowledge_check",
                    "title": "Concept Diagnostic: Sterile Insect Technique",
                    "content": {
                        "check_type": "multiple_choice",
                        "question": "In the ICIPE tsetse fly control program, what is the biological principle behind the sterilization of male flies?",
                        "options": [
                            "Sterilized males kill the female flies during mating",
                            "Sterilized males transmit a deadly virus to the rest of the fly population",
                            "When sterilized males mate with wild females, fertilization fails to occur, causing the population to decline rapidly",
                            "Sterilized males are unable to feed on human or livestock blood"
                        ],
                        "answer": "C",
                        "explanation": "The Sterile Insect Technique (SIT) relies on releasing millions of chemically or radiation-sterilized male flies. Because female tsetse flies typically mate only once in their lifetime, mating with a sterile male results in non-viable eggs, causing the overall fly population to collapse."
                    }
                }
            ]
        },
        # Page 14: Summary
        {
            "page_number": 14,
            "page_title": "Swamp Drainage & Pest Control: Key Takeaways",
            "blocks": [
                {
                    "block_type": "summary",
                    "component_type": "summary",
                    "title": "Module 1.3 Summary",
                    "content": {
                        "text": (
                            "### Key Conceptual Takeaways\n\n"
                            "- **Swamp Problems:** Waterlogged soils cause crop root hypoxia, harbor malaria/bilharzia vectors, and suffer severe flood risks.\n"
                            "- **Drainage Techniques:** Open gravity ditches, high-transpiration eucalyptus bio-drainage (Kakuzi model), and subsurface perforated pipe grids.\n"
                            "- **Yala & Bunyala:** 1970 drainage project in the Lake Victoria basin reclaiming over 800 hectares of fertile arable land and relieving Kano Plains congestion.\n"
                            "- **Pest Control as Reclamation:** Vector eradication releases fertile land for human settlement and agriculture.\n"
                            "- **ICIPE Tsetse Management:** Multi-tier program combining selective bush clearing, male sterilization, blue/black cloth traps, and 5km agricultural buffer zones."
                        )
                    }
                }
            ]
        }
    ]
}


# =============================================================================
# LESSON 4 DATA — Land Rehabilitation and Kenyan Irrigation Schemes (18 Pages)
# =============================================================================
LESSON_4_DATA = {
    "unit_order": 4,
    "unit_name": "Land Rehabilitation and Kenyan Irrigation Schemes",
    "lesson_title": "Land Rehabilitation and Kenyan Irrigation Schemes",
    "pages": [
        # Page 1: Hook & Goals
        {
            "page_number": 1,
            "page_title": "Restoring Land and Managing National Schemes",
            "blocks": [
                {
                    "block_type": "learning_goal",
                    "component_type": "learning_goal",
                    "title": "Module 1.4 Learning Goals",
                    "content": {
                        "text": (
                            "By the end of this lesson, you will be able to:\n\n"
                            "- Describe the nine scientific methods of land rehabilitation\n"
                            "- Explain the physical and human factors influencing the location of the Mwea and Perkerra schemes\n"
                            "- Analyze the agricultural operations, crops, and marketing systems of Mwea and Perkerra\n"
                            "- Evaluate the national benefits, severe challenges, and sustainable solutions for both schemes\n"
                            "- Construct a rigorous comparative matrix contrasting Mwea and Perkerra across all syllabus criteria"
                        )
                    }
                },
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "Restoration and Large-Scale Agricultural Planning",
                    "content": {
                        "text": (
                            "Land management in Kenya operates at two distinct scales: localized ecological rehabilitation of degraded landscapes, "
                            "and large-scale national irrigation schemes that feed the nation.\n\n"
                            "In this lesson, we master the nine methods of land rehabilitation, examine the Haller Park quarry transformation, "
                            "and conduct a deep comparative study of Kenya's two premier irrigation schemes: **Mwea** and **Perkerra**."
                        )
                    }
                }
            ]
        },
        # Page 2: Nine Methods Overview
        {
            "page_number": 2,
            "page_title": "Nine Scientific Methods of Land Rehabilitation",
            "blocks": [
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "The Rehabilitation Toolkit",
                    "content": {
                        "text": (
                            "Rehabilitating degraded or ruined land requires stabilizing the soil structure, replenishing depleted organic humus and mineral nutrients, "
                            "and establishing permanent vegetative cover."
                        )
                    }
                },
                {
                    "block_type": "suggested_diagram",
                    "component_type": "suggested_diagram",
                    "title": "The Nine Scientific Methods of Land Rehabilitation",
                    "content": {
                        "text": "Comprehensive visual landscape illustrating afforestation root binding, bush fallowing, grass contour strips, mulching moisture shields, manure/fertilizer application, paddock rotational grazing, quarry backfilling, drainage trenches, and ASAL drought-resistant crops."
                    }
                }
            ]
        },
        # Page 3: Vegetative Methods
        {
            "page_number": 3,
            "page_title": "Vegetative Rehabilitation Methods",
            "blocks": [
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "Tree Planting, Fallowing, and Cover Crops",
                    "content": {
                        "text": (
                            "### 1. Afforestation and Reafforestation\n"
                            "Planting trees restores damaged land through six distinct physical and microclimatic mechanisms:\n"
                            "- **Root Binding:** Extensive root networks physically bind loose soil particles together, preventing sheetwash and gullying.\n"
                            "- **Raindrop Interception:** Tree foliage intercepts heavy raindrops, absorbing kinetic energy and reducing soil splash erosion.\n"
                            "- **Windbreaks:** Tree lines reduce surface wind speed, checking severe wind erosion in semi-arid plains.\n"
                            "- **Humus Formation:** Decomposing leaf litter adds rich organic humus, restoring soil structure and fertility.\n"
                            "- **Infiltration:** Tree roots open channels in the soil, increasing deep water infiltration and recharging groundwater.\n"
                            "- **Microclimatic Modification:** Transpiring forests release atmospheric moisture, increasing local rainfall and lowering extreme ground temperatures.\n\n"
                            "### 2. Bush Fallowing\n"
                            "Cultivating a field for 2–3 seasons and then leaving it uncultivated to allow natural wild vegetation to regenerate organic matter.\n\n"
                            "### 3. Grass Strips and Cover Crops\n"
                            "Planting dense, spreading crops (e.g., sweet potato vines, beans, peas) or contour grass strips to slow surface runoff and trap eroded sediment."
                        )
                    }
                }
            ]
        },
        # Page 4: Mechanical & Agronomic Methods
        {
            "page_number": 4,
            "page_title": "Mechanical and Agronomic Methods",
            "blocks": [
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "Mulching, Manure, Grazing, and ASAL Crops",
                    "content": {
                        "text": (
                            "### 4. Mulching\n"
                            "Covering exposed topsoil with dry crop residues (maize stalks, straw, dry grass) or polythene sheeting. "
                            "This reduces soil moisture evaporation, checks surface runoff speed, buffers raindrop impact, and decomposes into humus.\n\n"
                            "### 5. Application of Manure and Fertilizers\n"
                            "Replenishing depleted chemical nutrients (nitrogen, phosphorus, potassium) using farmyard organic manure or synthetic fertilizers.\n\n"
                            "### 6. Controlled Grazing\n"
                            "Subdividing large pasturelands into fenced **paddocks** and rotating cattle herds. This prevents overstocking, ensures pasture grasses "
                            "can regenerate, and maintains livestock numbers strictly within the ecological **carrying capacity** of the land.\n\n"
                            "### 7. Filling Quarries (Backfilling)\n"
                            "Refilling industrial excavation pits and open-cast mines with rocks, gravel, and fertile topsoil before re-establishing vegetation.\n\n"
                            "### 8. Drainage Trenches\n"
                            "Excavating trenches across flooded, waterlogged farmlands to drain away standing water.\n\n"
                            "### 9. Planting Drought-Resistant Crops\n"
                            "In Arid and Semi-Arid Lands (ASALs), introducing quick-maturing, drought-tolerant crops such as **Katumani composite maize**, "
                            "sorghum, millet, cassava, and pigeon peas to sustain crop cover despite erratic rains."
                        )
                    }
                }
            ]
        },
        # Page 5: Quarry Restoration Case Study
        {
            "page_number": 5,
            "page_title": "Case Study: Bamburi Nature Trail (Haller Park)",
            "blocks": [
                {
                    "block_type": "suggested_image",
                    "component_type": "suggested_image",
                    "title": "Rehabilitated Limestone Quarry Pit at Haller Park in Mombasa",
                    "content": {
                        "text": "Lush tropical sanctuary with Casuarina trees, fish ponds, and wildlife established inside a formerly barren limestone quarry pit at Bamburi."
                    }
                },
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "The Step-by-Step Transformation of Bamburi",
                    "content": {
                        "text": (
                            "The **Bamburi Nature Trail (now Haller Park)** in Mombasa represents a world-famous model of industrial land rehabilitation:\n\n"
                            "1. **The Problem:** Decades of open-cast limestone quarrying by Bamburi Cement Company left a desolate, barren, deep limestone pit with zero topsoil and high salinity.\n"
                            "2. **Pioneering Vegetation:** Ecologist René Haller planted tough, salt-tolerant **Casuarina equisetifolia** trees whose roots could penetrate bare limestone.\n"
                            "3. **Soil Formation Engine:** Red-legged millipedes were introduced to feed on fallen Casuarina needles, excreting rich organic droppings that formed the first layer of fertile humus.\n"
                            "4. **Ecosystem Maturation:** As topsoil deepened, secondary trees (neem, mahogany), fish aquaculture ponds, and diverse wildlife (crocodiles, hippos, tortoises) were introduced, creating a thriving ecological and tourist sanctuary."
                        )
                    }
                }
            ]
        },
        # Page 6: Kenyan Irrigation Schemes Intro
        {
            "page_number": 6,
            "page_title": "Introduction to Kenyan Irrigation Schemes",
            "blocks": [
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "National Irrigation Board (NIB) Schemes",
                    "content": {
                        "text": (
                            "Large-scale commercial irrigation in Kenya is managed primarily by the **National Irrigation Authority (formerly National Irrigation Board - NIB)**.\n\n"
                            "Most public irrigation schemes were established in the **1950s** by the British colonial administration, originally to engage detainee labor "
                            "during the State of Emergency and settle landless populations. Today, they form the backbone of national rice and seed production."
                        )
                    }
                }
            ]
        },
        # Page 7: Mwea Setting & Origin
        {
            "page_number": 7,
            "page_title": "Mwea Irrigation Scheme: Origin & Setting",
            "blocks": [
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "Geographic Setting of Mwea",
                    "content": {
                        "text": (
                            "- **Location:** Located in **Kirinyaga County (formerly Kirinyaga District, Central Province)** on the expansive Mwea Plains at the southern foot of Mount Kenya.\n"
                            "- **Historical Inception:** Established in **1954** by the colonial government, originally functioning as a detention camp during the 1952 Mau Mau State of Emergency.\n"
                            "- **Primary Purpose:** Reclaim unproductive semi-arid plains, employ detainee labor productively, resettle landless citizens, and produce wet paddy rice."
                        )
                    }
                },
                {
                    "block_type": "suggested_diagram",
                    "component_type": "suggested_diagram",
                    "title": "Topography, Drainage Catchment, and Section Layout of the Mwea Scheme",
                    "content": {
                        "text": "Spatial map of the Mwea Plains in Kirinyaga County showing Mount Kenya drainage, Rivers Thiba and Nyamindi, main feeder canals, and the 4 administrative sections (Mwea, Thiba, Wamumu, Tebere)."
                    }
                }
            ]
        },
        # Page 8: Mwea Locational Factors
        {
            "page_number": 8,
            "page_title": "Factors Influencing the Location of Mwea",
            "blocks": [
                {
                    "block_type": "comparison_table",
                    "component_type": "comparison_table",
                    "title": "Physical and Human Factors Governing Mwea's Location",
                    "content": {
                        "headers": ["Category", "Locational Factor", "Geographical Significance"],
                        "rows": [
                            ["Physical Factor", "Gently Sloping Land", "The gentle slope allows river water to flow naturally by gravity through canals to fields, eliminating expensive fuel pumping costs."],
                            ["Physical Factor", "Black Cotton Soil (Clay)", "Impermeable heavy clay soil has high water retention, holding 10cm standing water required for wet paddy rice."],
                            ["Physical Factor", "Clay Loam Soils", "Well-drained red clay loams on upper ridges provide ideal ground for subsistence food crops and horticulture."],
                            ["Physical Factor", "Permanent Water Supply", "Perennial rivers Thiba and Nyamindi drain the high-rainfall Mount Kenya catchment, providing abundant year-round water."],
                            ["Physical Factor", "Warm Ripening Climate", "High temperatures and sunny weather during the second half of the year provide optimal conditions for rice grain ripening."],
                            ["Human Factor", "Sparse Initial Population", "The semi-arid plains were sparsely populated prior to 1954, allowing scheme establishment without complex land compensation."],
                            ["Human Factor", "Availability of Labor", "Presence of large colonial detainee labor forces during the 1950s enabled extensive manual canal and bund construction."],
                            ["Human Factor", "Proximity to Major Markets", "Close highway proximity to major urban consuming centers including Nairobi, Thika, Embu, and Nyeri."]
                        ]
                    }
                }
            ]
        },
        # Page 9: Mwea Operations & Layout
        {
            "page_number": 9,
            "page_title": "Mwea Operations, Organization & Agronomy",
            "blocks": [
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "Scheme Organization and Agronomic Practice",
                    "content": {
                        "text": (
                            "### Administrative Organization\n"
                            "The scheme is structured into four main sections: **Mwea, Thiba, Wamumu, and Tebere**. "
                            "Tenant farmers reside in **36 planned villages**. Each tenant family is allocated a standard **4-acre plot** for commercial rice cultivation "
                            "plus a mandatory **1/8-acre plot** for a seed nursery.\n\n"
                            "### Irrigation Method & Agronomy\n"
                            "- **Method:** Exclusively **Basin Irrigation**. Fields are leveled and enclosed by low earth bunds, flooded with water to a depth of **10 cm**.\n"
                            "- **Crops Grown:** Wet paddy rice dominates—specifically **Basmati / Pishori** (prized for high aromatic market value) and **Sindano** (high disease resistance). "
                            "Tenants also grow subsistence crops (maize, beans, peas) and horticulture (tomatoes, French beans, melons).\n\n"
                            "### Marketing\n"
                            "Rice is harvested, dried on communal concrete drying floors, milled, and sold directly to urban consumers in Nairobi and Thika."
                        )
                    }
                },
                {
                    "block_type": "suggested_diagram",
                    "component_type": "suggested_diagram",
                    "title": "Basin Flooding and Earth Bund Engineering for Wet Paddy Rice",
                    "content": {
                        "text": "Technical field layout diagram showing feeder canal sluice gates, earthen retaining bunds, 10cm water inundation depth, and seed nursery to main basin transplanting stages."
                    }
                }
            ]
        },
        # Page 10: Perkerra Setting & Origin
        {
            "page_number": 10,
            "page_title": "Perkerra Irrigation Scheme: Origin & Setting",
            "blocks": [
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "Geographic Setting of Perkerra",
                    "content": {
                        "text": (
                            "- **Location:** Situated at **Marigat Division in Baringo County (formerly Baringo District, Rift Valley Province)** near Lake Baringo.\n"
                            "- **Historical Inception:** Established in **1954** by the colonial government, also utilizing detainee labor during the State of Emergency.\n"
                            "- **Primary Objectives:**\n"
                            "  1. Settle nomadic pastoralists (Tugen and Ilchamus/Jemps communities) as settled, sedentary crop farmers.\n"
                            "  2. Reclaim dry ASAL land by utilizing excess floodwaters from the River Perkerra that previously went to waste.\n"
                            "  3. Control seasonal flash flooding of the River Perkerra."
                        )
                    }
                },
                {
                    "block_type": "suggested_diagram",
                    "component_type": "suggested_diagram",
                    "title": "Spatial Layout and River Catchment of the Perkerra Irrigation Scheme",
                    "content": {
                        "text": "Spatial map of Marigat Division in Baringo County showing the River Perkerra catchment, diversion weir, furrow irrigation plots, and contract seed maize cultivation zones."
                    }
                }
            ]
        },
        # Page 11: Perkerra Locational Factors
        {
            "page_number": 11,
            "page_title": "Factors Influencing the Location of Perkerra",
            "blocks": [
                {
                    "block_type": "comparison_table",
                    "component_type": "comparison_table",
                    "title": "Physical and Human Factors Governing Perkerra's Location",
                    "content": {
                        "headers": ["Category", "Locational Factor", "Geographical Significance"],
                        "rows": [
                            ["Physical Factor", "Gently Sloping Land", "Gentle terrain allows gravity flow from the diversion weir and permits tractor mechanization for plowing."],
                            ["Physical Factor", "Fertile Alluvial Loam Soils", "Rich volcanic alluvial soils deposited by river flooding reduce the need for expensive commercial fertilizers."],
                            ["Physical Factor", "Semi-Arid ASAL Climate", "Low, erratic rainfall made artificial irrigation the only viable method for crop agriculture."],
                            ["Physical Factor", "Permanent River Perkerra", "The perennial River Perkerra, draining the Mau Escarpment, provides a dependable water source in a dry basin."],
                            ["Human Factor", "Sparse Population", "The dry, hostile scrubland was sparsely populated, allowing scheme demarcation without land disputes."],
                            ["Human Factor", "Detainee Labor Availability", "Colonial emergency detention labor enabled manual clearing of dense acacia scrub and canal excavation."]
                        ]
                    }
                }
            ]
        },
        # Page 12: Perkerra Operations & Seed Maize
        {
            "page_number": 12,
            "page_title": "Perkerra Operations and Seed Maize Agronomy",
            "blocks": [
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "Operations, Crops, and Contract Marketing",
                    "content": {
                        "text": (
                            "### Irrigation Method: Furrow / Ridge Irrigation\n"
                            "Unlike Mwea's flooded basins, Perkerra uses **Furrow and Ridge Irrigation**. Raised ridges are constructed for planting crops, "
                            "while water is directed along the intervening furrows to soak into the root zone without inundating the crop stems.\n\n"
                            "### Crops Grown & The Seed Maize Contract\n"
                            "- **Primary Cash Crop:** **Commercial Seed Maize**, grown under strict contract for the **Kenya Seed Company (KSC)**.\n"
                            "- **Agronomic Technique:** Seed maize is planted in alternating **male and female lines**. Female lines are cross-pollinated, harvested, and processed for commercial seed; male lines are de-tasseled or consumed.\n"
                            "- **Secondary Crops:** Watermelons, pawpaws, onions, chillies, and cotton.\n\n"
                            "### Organization and Marketing\n"
                            "Each tenant receives a **3–4 acre farm plot** plus a **0.5-acre homestead**. Harvested seed maize is graded, shelled, and delivered "
                            "to the Kenya Seed Company processing plant in **Kitale**, which pays farmers directly."
                        )
                    }
                },
                {
                    "block_type": "callout",
                    "component_type": "callout",
                    "title": "Agronomic Precision Note",
                    "content": {
                        "text": "In hybrid seed maize production at Perkerra, female parent lines are pollinated by male lines. The harvested cobs from female lines are certified for commercial planting seed by the Kenya Seed Company."
                    }
                }
            ]
        },
        # Page 13: Benefits of Schemes
        {
            "page_number": 13,
            "page_title": "Economic and Social Benefits of Kenyan Schemes",
            "blocks": [
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "National and Local Economic Dividends",
                    "content": {
                        "text": (
                            "Both Mwea and Perkerra have delivered vital socio-economic benefits:\n\n"
                            "### Benefits of the Mwea Scheme:\n"
                            "- **Foreign Exchange Savings:** Produces over 80% of Kenya's locally grown rice, saving billions in foreign exchange imports.\n"
                            "- **Employment and Livelihoods:** Directly employs thousands of tenant farmers, millers, transporters, and agricultural laborers.\n"
                            "- **Infrastructure Development:** Spurred construction of tarmac roads, modern schools, electricity grids, and healthcare facilities (e.g., Karira Mission Hospital).\n\n"
                            "### Benefits of the Perkerra Scheme:\n"
                            "- **Sedentary Transformation:** Successfully settled former nomadic pastoralists into productive, commercial crop farmers.\n"
                            "- **National Hybrid Seed Supply:** Serves as a primary multiplication base for certified hybrid seed maize distributed across Kenya.\n"
                            "- **Wasteland Productive Use:** Turned barren, drought-prone scrubland into a fertile commercial oasis."
                        )
                    }
                }
            ]
        },
        # Page 14: Challenges & Solutions
        {
            "page_number": 14,
            "page_title": "Problems Facing Schemes and Their Solutions",
            "blocks": [
                {
                    "block_type": "comparison_table",
                    "component_type": "comparison_table",
                    "title": "Severe Challenges and Implemented Solutions at Mwea and Perkerra",
                    "content": {
                        "headers": ["Scheme", "Severe Problem Faced", "Underlying Cause", "Implemented / Proposed Solution"],
                        "rows": [
                            ["Mwea", "Waterborne Diseases", "Stagnant flooded paddy basins harbor Malaria mosquitoes and Bilharzia snails.", "Insecticide spraying on canals, free medical clinics, and providing treated domestic piped water."],
                            ["Mwea", "Canal Siltation", "Soil erosion upstream in Mount Kenya catchment washes silt into canals, reducing water flow.", "Regular canal dredging, desilting fees, and banning farming along riverbanks upstream."],
                            ["Mwea", "Drought Water Deficits", "Severe dry seasons reduce discharge in Rivers Thiba and Nyamindi.", "Constructing large storage reservoirs (e.g., Thiba Dam) to buffer dry season shortages."],
                            ["Mwea", "Cooperative Mismanagement", "Financial collapse of tenant marketing societies left farmers without credit.", "Reforming cooperative governance and removing political interference."],
                            ["Perkerra", "River Discharge Fluctuation", "River Perkerra volume drops drastically during dry spells, starving furrows.", "Constructing a permanent storage dam on the upper River Perkerra."],
                            ["Perkerra", "Human-Livestock Conflict", "Pastoralists graze livestock on tenant irrigated crops during severe droughts.", "Resolving disputes through local elder committees and fencing scheme boundaries."],
                            ["Perkerra", "Ethnic Tensions", "Historical land competition between local Tugen and Jemps communities.", "Issuing official individual title deeds to secure land tenure."],
                            ["Perkerra", "Remote Market Access", "High transport costs to distant urban markets for perishable pawpaws.", "Organizing farmer transport cooperatives and establishing local cold storage." ]
                        ]
                    }
                }
            ]
        },
        # Page 15: Comparative Matrix
        {
            "page_number": 15,
            "page_title": "Interactive Comparative Matrix: Mwea vs Perkerra",
            "blocks": [
                {
                    "block_type": "mini_activity",
                    "component_type": "mini_activity",
                    "title": "Mwea vs Perkerra Comparative Synthesis",
                    "content": {
                        "text": (
                            "**Task:** Review the complete comparison between Kenya's two flagship schemes across all syllabus dimensions:\n\n"
                            "| Comparison Dimension | Mwea Irrigation Scheme | Perkerra Irrigation Scheme |\n"
                            "|---|---|---|\n"
                            "| **County / Region** | Kirinyaga County (Central Kenya) | Baringo County (Rift Valley) |\n"
                            "| **Primary River Sources** | Rivers Thiba and Nyamindi | River Perkerra |\n"
                            "| **Dominant Soil Type** | Black cotton soil (Heavy Clay) | Fertile Alluvial Loam |\n"
                            "| **Irrigation Method** | Basin / Flood Irrigation (Bunds) | Furrow / Ridge Irrigation |\n"
                            "| **Primary Cash Crop** | Wet Paddy Rice (Basmati / Sindano) | Hybrid Seed Maize (for Kenya Seed Co) |\n"
                            "| **Target Population** | Landless citizens & former detainees | Nomadic pastoralists (Tugen / Jemps) |\n"
                            "| **Major Climatic Problem** | Severe drought water shortages | Extreme river water volume fluctuations |"
                        )
                    }
                }
            ]
        },
        # Page 16: Knowledge Check 1
        {
            "page_number": 16,
            "page_title": "Knowledge Checkpoint: Mwea Scheme",
            "blocks": [
                {
                    "block_type": "knowledge_check",
                    "component_type": "knowledge_check",
                    "title": "Concept Diagnostic: Mwea Locational Factors",
                    "content": {
                        "check_type": "multiple_choice",
                        "question": "Which combination of physical factors most strongly influenced the establishment of the Mwea Irrigation Scheme?",
                        "options": [
                            "Steep mountainous slopes, sandy soils, and high altitude frost",
                            "Gently sloping land for gravity flow, black cotton clay soils for water retention, and permanent rivers Thiba and Nyamindi",
                            "Dense equatorial rainforest vegetation, alluvial gravels, and seasonal boreholes",
                            "Deep limestone quarries, alkaline saline soils, and proximity to the Indian Ocean"
                        ],
                        "answer": "B",
                        "explanation": "Mwea was specifically chosen because the gently sloping plains permit gravity-fed canal flow without expensive pumping, black cotton clay soil holds standing water for paddy rice, and permanent rivers Thiba and Nyamindi drain Mount Kenya to provide reliable water."
                    }
                }
            ]
        },
        # Page 17: Knowledge Check 2
        {
            "page_number": 17,
            "page_title": "Knowledge Checkpoint: Perkerra Scheme",
            "blocks": [
                {
                    "block_type": "knowledge_check",
                    "component_type": "knowledge_check",
                    "title": "Concept Diagnostic: Perkerra Agronomy & Challenges",
                    "content": {
                        "check_type": "multiple_choice",
                        "question": "What is the primary cash crop grown at the Perkerra Irrigation Scheme, and what major environmental challenge affects its production?",
                        "options": [
                            "Wet paddy rice; affected by severe canal frost",
                            "Commercial seed maize grown under contract for Kenya Seed Company; affected by River Perkerra water volume fluctuations",
                            "Tea and pyrethrum; affected by intense waterlogging",
                            "Sisal and sugarcane; affected by coastal tidal saltwater intrusion"
                        ],
                        "answer": "B",
                        "explanation": "Perkerra specializes in commercial hybrid seed maize production under contract with the Kenya Seed Company. Its primary environmental constraint is the severe seasonal fluctuation of discharge in the River Perkerra during dry seasons."
                    }
                }
            ]
        },
        # Page 18: Summary
        {
            "page_number": 18,
            "page_title": "Rehabilitation & Kenyan Schemes: Key Takeaways",
            "blocks": [
                {
                    "block_type": "summary",
                    "component_type": "summary",
                    "title": "Module 1.4 Summary",
                    "content": {
                        "text": (
                            "### Key Conceptual Takeaways\n\n"
                            "- **Rehabilitation Methods:** 9 methods spanning afforestation (root binding, microclimate), bush fallowing, grass strips, mulching, manure, paddock rotation, quarry backfilling (Haller Park), drainage trenches, and ASAL crops.\n"
                            "- **Haller Park Model:** Exhausted limestone quarry transformed through Casuarina trees, red-legged millipedes, humus formation, and wildlife introduction.\n"
                            "- **Mwea Scheme:** Kirinyaga County, Rivers Thiba & Nyamindi, black cotton clay soils, basin flooding, Basmati/Sindano rice, saving foreign exchange.\n"
                            "- **Perkerra Scheme:** Baringo County, River Perkerra, alluvial loams, furrow/ridge irrigation, contract seed maize for Kenya Seed Company, settling nomadic pastoralists."
                        )
                    }
                }
            ]
        }
    ]
}


# =============================================================================
# LESSON 5 DATA — Land Reclamation in the Netherlands & Comparative Analysis (16 Pages)
# =============================================================================
LESSON_5_DATA = {
    "unit_order": 5,
    "unit_name": "Land Reclamation in the Netherlands and Comparative Analysis",
    "lesson_title": "Land Reclamation in the Netherlands and Comparative Analysis",
    "pages": [
        # Page 1: Hook & Goals
        {
            "page_number": 1,
            "page_title": "Conquering the Sea: Dutch Hydraulic Engineering",
            "blocks": [
                {
                    "block_type": "learning_goal",
                    "component_type": "learning_goal",
                    "title": "Module 1.5 Learning Goals",
                    "content": {
                        "text": (
                            "By the end of this lesson, you will be able to:\n\n"
                            "- Explain how the Netherlands reclaims coastal seabed from the North Sea\n"
                            "- Describe the engineering works and aims of the Zuider Zee Project and Delta Plan\n"
                            "- Detail the seven sequential scientific stages of the polder reclamation process\n"
                            "- Compare land reclamation in Kenya and the Netherlands across six distinct criteria\n"
                            "- Formulate high-scoring KCSE comparative essays using structured geographical reasoning"
                        )
                    }
                },
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "The Dutch Axiom: God Made the Earth, but the Dutch Made the Netherlands",
                    "content": {
                        "text": (
                            "There is a famous geographical saying: *'God created the Earth, but the Dutch created the Netherlands.'*\n\n"
                            "Over centuries, the people of the Netherlands have waged a continuous battle against the North Sea, "
                            "deploying massive dykes, ring canals, and heavy pumping stations to reclaim fertile seabed lying metres below sea level."
                        )
                    }
                }
            ]
        },
        # Page 2: Lowland Geography & Polder Definition
        {
            "page_number": 2,
            "page_title": "The Lowland Geography of the Netherlands",
            "blocks": [
                {
                    "block_type": "definition_card",
                    "component_type": "definition_card",
                    "title": "Polder",
                    "content": {
                        "term": "Polder",
                        "definition": "A low-lying tract of land reclaimed from a body of water (sea, lake, or river floodplain) and enclosed by high protective dykes (seawalls), where the internal water table is manually and continuously regulated by pumping stations."
                    }
                },
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "The Geographic Imperative of Holland",
                    "content": {
                        "text": (
                            "The Netherlands (Holland) is a low-lying, densely populated European nation where a significant portion of the total land area "
                            "lies **below mean sea level**. Without massive engineered seawalls and dykes, vast swathes of the country would be permanently inundated by the North Sea.\n\n"
                            "To protect against storm surges and create farmland for a growing population, the Dutch executed two of the largest hydraulic engineering projects in human history: "
                            "the **Zuider Zee Project** and the **Delta Plan**."
                        )
                    }
                }
            ]
        },
        # Page 3: Zuider Zee Project
        {
            "page_number": 3,
            "page_title": "The Zuider Zee Project",
            "blocks": [
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "Reclaiming the North Sea Inlet",
                    "content": {
                        "text": (
                            "### Timeline and Leadership\n"
                            "Planned and executed under the visionary leadership of Dutch civil engineer **Cornelius Lely** between **1927 and 1932**.\n\n"
                            "### Strategic Objectives\n"
                            "1. Protect central Holland from catastrophic North Sea storm floods.\n"
                            "2. Reclaim expansive new agricultural polders to feed the nation.\n"
                            "3. Create a massive freshwater reservoir by damming tidal sea water.\n\n"
                            "### Key Engineering Works\n"
                            "- **The Afsluitdijk (Enclosing Dam):** A massive 32-kilometer-long sea barrier built across the mouth of the Zuider Zee inlet (connecting North Holland to Friesland).\n"
                            "- **Creation of Lake IJssel:** Damming River IJssel (a distributary of the Rhine) transformed the salty tidal sea inlet into a vast **freshwater lake** called **Lake IJssel**.\n"
                            "- **Four Massive Polders:** Reclaimed four huge contiguous polders: **Wieringermeer, Noordoostpolder (North-East Polder), Eastern Flevoland, and Southern Flevoland**."
                        )
                    }
                },
                {
                    "block_type": "suggested_diagram",
                    "component_type": "suggested_diagram",
                    "title": "The Zuider Zee and Delta Plan Hydraulic Projects in the Netherlands",
                    "content": {
                        "text": "Spatial engineering map of the Netherlands showing the North Sea, the 32km Afsluitdijk enclosing dam, Lake IJssel freshwater lake, the 4 major reclaimed polders, and the South-West Delta Plan sea barriers."
                    }
                }
            ]
        },
        # Page 4: Delta Plan Project
        {
            "page_number": 4,
            "page_title": "The Delta Plan Project",
            "blocks": [
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "Defending the South-West Estuaries",
                    "content": {
                        "text": (
                            "### Origin: The 1953 Flood Catastrophe\n"
                            "In February 1953, a ferocious North Sea storm surge breached coastal dykes in south-western Netherlands, drowning over 1,800 people "
                            "and destroying thousands of square kilometers of farmland. In response, the Dutch parliament enacted the **Delta Plan**.\n\n"
                            "### Major Engineering Works\n"
                            "The project closed off four major sea estuaries by constructing gigantic storm surge dams across the mouths of: "
                            "**Haringvliet, Brouwershavensche Gat, Veersche Gat, and the Eastern Scheldt (Oosterschelde)**.\n\n"
                            "### Key Benefits Realized\n"
                            "- Shortened the exposed coastline by over 700 kilometers, dramatically reducing flood vulnerability.\n"
                            "- Prevented saltwater pollution (salinisation) of inland groundwater and agricultural soils.\n"
                            "- Created fresh water reservoirs and recreational lakes."
                        )
                    }
                }
            ]
        },
        # Page 5: Seven Stages Flowchart
        {
            "page_number": 5,
            "page_title": "The Seven Stages of Polder Reclamation",
            "blocks": [
                {
                    "block_type": "step_process",
                    "component_type": "step_process",
                    "title": "The Seven Sequential Stages of Polder Reclamation",
                    "content": {
                        "procedure": [
                            "Stage 1 — Construct Protective Dykes (Seawalls): Heavy earthen and stone seawalls (dykes) are built in the open sea to completely enclose the portion of seabed earmarked for reclamation.",
                            "Stage 2 — Construct Ring Canals: A wide ring canal is excavated all around the outside perimeter of the enclosed dyke system to receive water pumped out of the enclosed area.",
                            "Stage 3 — Install Heavy Pumping Stations: Massive automated pumping stations (historically windmills; today heavy electric/diesel pumps) pump sea water out of the enclosed basin into the ring canal.",
                            "Stage 4 — Sow Reed Seeds by Aircraft: Once the muddy seabed is exposed, reed seeds (Phragmites) are aerially sown. The fast-growing reeds transpire enormous water volumes, drying the muddy soil and binding its structure.",
                            "Stage 5 — Lay Subsurface Perforated Drainage Pipes: Once reeds dry the surface, trenches are excavated and perforated drainage pipes are buried to systematically lower the water table.",
                            "Stage 6 — Treat Salty Soil with Chemicals (Gypsum): Gypsum (calcium sulphate) and chemical fertilizers are applied to displace toxic sodium ions from the clay soil, lowering salinity.",
                            "Stage 7 — Flush the Land with Fresh Water: Fresh water from Lake IJssel is repeatedly flushed through the soil to leach away residual sea salts, rendering the polder ready for agricultural cultivation and settlement."
                        ]
                    }
                },
                {
                    "block_type": "suggested_diagram",
                    "component_type": "suggested_diagram",
                    "title": "The Seven Sequential Stages of Dutch Polder Reclamation",
                    "content": {
                        "text": "Chronological 7-stage flowchart illustrating dyke construction, ring canal digging, pumping, reed sowing for bio-drying, drainage pipe laying, chemical desalinisation, and freshwater flushing."
                    }
                }
            ]
        },
        # Page 6: Scientific Rationale 1-4
        {
            "page_number": 6,
            "page_title": "Scientific Rationale of Stages 1 to 4",
            "blocks": [
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "Containment, Evacuation, and Bio-Drying",
                    "content": {
                        "text": (
                            "Understanding the scientific principles behind each stage is critical for KCSE exam mastery:\n\n"
                            "- **Stage 1 (Dykes):** Must withstand extreme North Sea tidal forces. Built with a clay core, sand layers, and basalt rock armour.\n"
                            "- **Stage 2 (Ring Canals):** Acts as a high-capacity drainage corridor, carrying evacuated water away to the sea at low tide.\n"
                            "- **Stage 3 (Pumps):** Requires months of continuous pumping to evacuate billions of litres of sea water.\n"
                            "- **Stage 4 (Reeds):** Reeds prevent weeds, their deep roots break up dense seabed mud, and their intense transpiration accelerates soil dehydration."
                        )
                    }
                }
            ]
        },
        # Page 7: Scientific Rationale 5-7
        {
            "page_number": 7,
            "page_title": "Scientific Rationale of Stages 5 to 7",
            "blocks": [
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "Hydraulic Drainage and Desalinisation",
                    "content": {
                        "text": (
                            "- **Stage 5 (Drainage Pipes):** Subterranean perforated pipes provide continuous gravity drainage, preventing waterlogging when farming commences.\n"
                            "- **Stage 6 (Chemical Gypsum Treatment):** Marine clays are saturated with sodium ions ($Na^+$), which cause clay particles to disperse into a sticky, impermeable, unworkable mass. "
                            "Applying gypsum ($CaSO_4$) introduces calcium ions ($Ca^{2+}$), which displace sodium, causing clay particles to aggregate into a crumbly, well-aerated soil structure.\n"
                            "- **Stage 7 (Fresh Water Flushing):** Fresh water dissolved residual chlorine and sodium salts, washing them down into the drainage pipes until soil salinity reaches non-toxic levels for crops."
                        )
                    }
                }
            ]
        },
        # Page 8: Field Evidence Dutch Polder
        {
            "page_number": 8,
            "page_title": "Field Evidence: The Dutch Polder Landscape",
            "blocks": [
                {
                    "block_type": "suggested_image",
                    "component_type": "suggested_image",
                    "title": "Polder Landscape, Protective Dyke, and Drainage Canal in the Netherlands",
                    "content": {
                        "text": "Panoramic view of a Dutch polder showing lush agricultural fields sitting noticeably below the water level of the adjacent protective dyke and ring canal."
                    }
                },
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "Observing the Polder Topography",
                    "content": {
                        "text": (
                            "Notice the unique vertical relationship in this landscape: the cultivated agricultural fields and farmhouse settlements "
                            "sit **several metres lower** than the surface of the adjacent ring canal!\n\n"
                            "The dyke acts as a continuous protective wall, while pumping stations run around the clock to lift seepage water up into the canal."
                        )
                    }
                }
            ]
        },
        # Page 9: Kenya vs Netherlands Matrix
        {
            "page_number": 9,
            "page_title": "Comprehensive Comparison: Kenya vs Netherlands",
            "blocks": [
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "Similarities and Differences",
                    "content": {
                        "text": (
                            "### Similarities Between Kenya and the Netherlands:\n"
                            "1. **Common Objective:** Both countries reclaim land primarily to increase food production, provide settlement space, and control flooding.\n"
                            "2. **Drainage Infrastructure:** Both utilize open drainage ditches and canal networks to manage and channel surface water.\n"
                            "3. **Biological Mechanisms:** Both employ high-transpiration vegetation (eucalyptus in Kenya, reeds in Netherlands) to accelerate soil dewatering."
                        )
                    }
                },
                {
                    "block_type": "suggested_diagram",
                    "component_type": "suggested_diagram",
                    "title": "Kenya vs Netherlands Landscape and Engineering Contrast",
                    "content": {
                        "text": "Cross-sectional comparative illustration contrasting Kenya's inland high plateau reclamation with the Netherlands below-sea-level polder and dyke engineering."
                    }
                },
                {
                    "block_type": "comparison_table",
                    "component_type": "comparison_table",
                    "title": "Six-Point Comparative Matrix: Kenya vs The Netherlands",
                    "content": {
                        "headers": ["Comparison Criteria", "Land Reclamation in Kenya", "Land Reclamation in the Netherlands"],
                        "rows": [
                            ["Landscape & Elevation", "Reclaimed lands are located high above sea level (inland plateaus, river valleys, and lake basins).", "Reclaimed coastal land (polders) was originally the seabed, situated several metres below sea level."],
                            ["Engineering Features", "Relies on simpler engineering: digging open ditches, earthen bunds, manual bush clearing, and gravity furrows.", "Utilizes massive maritime engineering: sea dykes, storm surge barriers, ring canals, and automated pumping stations."],
                            ["Scale of Projects", "Reclaimed land units are relatively small-scale and localized (e.g., Mwea 6,000 ha; Yala 800 ha).", "Executed on a colossal, contiguous national scale (hundreds of thousands of hectares across 4 major polders)."],
                            ["Number of Projects", "Consists of multiple small, scattered independent schemes across the country (Mwea, Perkerra, Yala, Bunyala).", "Focused primarily on two massive, unified national megaprojects (Zuider Zee Project and Delta Plan)."],
                            ["Technological Level", "Utilizes low-to-medium technology (manual labor, gravity flow, basic pumps).", "Involves highly advanced technology (automated pumping, chemical desalinisation, computer-controlled storm barriers)."],
                            ["Distance from the Sea", "Reclaimed lands are situated far inland in the interior of the country.", "Reclaimed land was maritime coastal land taken directly from the North Sea."]
                        ]
                    }
                }
            ]
        },
        # Page 10: Worked Geographical Reasoning
        {
            "page_number": 10,
            "page_title": "Geographical Reasoning: Scale & Technology",
            "blocks": [
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "Why the Netherlands Reclaimed Land on a Larger Scale",
                    "content": {
                        "text": (
                            "In KCSE examinations, students are frequently asked to account for why the Netherlands was able to reclaim land on a vastly larger scale than Kenya.\n\n"
                            "### The Three Underlying Factors:\n"
                            "1. **Capital and Technological Superiority:** The Netherlands possessed immense capital resources and cutting-edge maritime engineering technology (automated pumps, heavy dyke-building dredgers) allowing deep seabed reclamation, whereas Kenya was constrained by limited finances and relied on basic gravity ditches.\n"
                            "2. **Physical Topography:** The shallow coastal seabed of the Zuider Zee formed a single, contiguous, flat marine basin enclosed by shallow shores, permitting huge polder units. In Kenya, reclaimed lands are small, fragmented pockets scattered along narrow river valleys and dry plateau basins.\n"
                            "3. **National Urgency and Coordination:** Facing catastrophic sea flood disasters (1953) and extreme population density, the Dutch government executed unified, highly funded national master plans (Zuider Zee & Delta Plan), whereas Kenya's projects were developed piecemeal as smaller, localized schemes."
                        )
                    }
                }
            ]
        },
        # Page 11: Essay Scaffolding
        {
            "page_number": 11,
            "page_title": "KCSE Comparative Essay Strategy",
            "blocks": [
                {
                    "block_type": "mini_activity",
                    "component_type": "mini_activity",
                    "title": "Mastering Comparative Command Words",
                    "content": {
                        "text": (
                            "**Exam Strategy:** When answering a 'Compare' question in Geography, never write two isolated paragraphs describing each country separately. "
                            "You must link both countries in the **same sentence** using comparative transitional conjunctions:\n\n"
                            "- *'Whereas...'* (e.g., 'Whereas land reclamation in Kenya is carried out inland above sea level, in the Netherlands it is done on the coastal seabed below sea level.')\n"
                            "- *'Unlike...'* (e.g., 'Unlike Kenya which uses simple gravity ditches and manual clearing, the Netherlands utilizes massive sea dykes and automated pumping stations.')\n"
                            "- *'On the other hand...'* (e.g., 'Kenya's reclamation projects are small and scattered across the country; on the other hand, the Netherlands executed two large-scale national megaprojects.')"
                        )
                    }
                }
            ]
        },
        # Page 12: Worked Exam Example
        {
            "page_number": 12,
            "page_title": "Worked Exam Question & Model Answer",
            "blocks": [
                {
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "title": "KCSE Model Question & Scoring Breakdown",
                    "content": {
                        "question": "Explain three physical and technological reasons why the Netherlands was able to reclaim land on a much larger scale than Kenya. (6 Marks)",
                        "steps": [
                            "Step 1 — Technological Disparity: 'The Netherlands utilized highly advanced engineering technology—including the construction of massive protective sea dykes, ring canals, and automated pumping stations—whereas Kenya relied on less advanced technology such as digging simple gravity ditches and manual bush clearing.' (2 Marks)",
                            "Step 2 — Terrain and Marine Topography: 'The physical nature of the terrain differed; in the Netherlands, the shallow coastal seabed of the Zuider Zee formed a contiguous, flat basin allowing massive unified polders, whereas in Kenya, reclaimed lands are small, scattered pockets located inland in river valleys.' (2 Marks)",
                            "Step 3 — Capital Investment & Scale of Organization: 'The Netherlands implemented reclamation through two large-scale, heavily funded national master projects (the Zuider Zee Project and Delta Plan), while Kenya's reclamation has been executed as smaller, independent schemes with limited financial resources.' (2 Marks)"
                        ]
                    }
                }
            ]
        },
        # Page 13: Topic Review Questions
        {
            "page_number": 13,
            "page_title": "Form 4 Topic 1 Review Questions",
            "blocks": [
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "Standard KCSE Examination Revision Prompts",
                    "content": {
                        "text": (
                            "Test your mastery against these five past KCSE examination prompts:\n\n"
                            "1. **Define:** Define the terms *Land Reclamation* and *Land Rehabilitation*. (4 Marks)\n"
                            "2. **State:** State three methods used to reclaim land from waterlogged swamps in Kenya. (3 Marks)\n"
                            "3. **Describe:** Describe how tsetse flies are controlled using the sterile male technique. (3 Marks)\n"
                            "4. **Explain:** Explain four physical factors that influenced the location of the Mwea Irrigation Scheme. (8 Marks)\n"
                            "5. **Compare:** State three similarities and three differences between land reclamation in Kenya and the Netherlands. (6 Marks)"
                        )
                    }
                }
            ]
        },
        # Page 14: Knowledge Check 1
        {
            "page_number": 14,
            "page_title": "Knowledge Checkpoint: Polder Reclamation",
            "blocks": [
                {
                    "block_type": "knowledge_check",
                    "component_type": "knowledge_check",
                    "title": "Concept Diagnostic: 7-Stage Polder Sequence",
                    "content": {
                        "check_type": "multiple_choice",
                        "question": "What is the primary scientific purpose of applying gypsum (calcium sulphate) to reclaimed polder soils in Stage 6 of the Dutch reclamation process?",
                        "options": [
                            "To act as a pesticide that exterminates soil-dwelling nematodes",
                            "To displace toxic sodium ions from marine clay particles, restoring soil aeration and structure",
                            "To absorb excess surface rainwater and prevent the polder from flooding",
                            "To change the color of the soil so it absorbs more solar heat"
                        ],
                        "answer": "B",
                        "explanation": "Marine clay soils from the seabed are saturated with sodium ions (from sea salt), which make the soil sticky, impermeable, and toxic to crops. Applying gypsum supplies calcium ions, which displace the sodium. The sodium is then flushed out with fresh water, leaving a crumbly, fertile soil structure."
                    }
                }
            ]
        },
        # Page 15: Knowledge Check 2
        {
            "page_number": 15,
            "page_title": "Knowledge Checkpoint: Kenya vs Netherlands",
            "blocks": [
                {
                    "block_type": "knowledge_check",
                    "component_type": "knowledge_check",
                    "title": "Concept Diagnostic: Comparative Criteria",
                    "content": {
                        "check_type": "multiple_choice",
                        "question": "Which of the following statements correctly identifies a fundamental difference between land reclamation in Kenya and the Netherlands?",
                        "options": [
                            "Kenya reclaims land from the open seabed, whereas the Netherlands reclaims inland river valleys",
                            "Kenya relies entirely on automated electric pumps, whereas the Netherlands relies on manual water lifting",
                            "Reclaimed land in Kenya is situated high above sea level inland, whereas reclaimed polders in the Netherlands are situated below sea level on the coast",
                            "The Netherlands reclaims land exclusively for nomadic pastoralism, whereas Kenya reclaims land exclusively for export flowers"
                        ],
                        "answer": "C",
                        "explanation": "In Kenya, all reclamation schemes (Mwea, Perkerra, Yala, Bunyala) are located inland on plateaus and river basins high above sea level. In the Netherlands, polders were reclaimed directly from the North Sea coastal seabed and sit metres below mean sea level."
                    }
                }
            ]
        },
        # Page 16: Topic Mastery Checklist
        {
            "page_number": 16,
            "page_title": "Topic 1 Mastery Checklist & Final Synthesis",
            "blocks": [
                {
                    "block_type": "summary",
                    "component_type": "summary",
                    "title": "Form 4 Geography Topic 1 Syllabus Checklist",
                    "content": {
                        "text": (
                            "### Congratulations on Completing Topic 1: Land Reclamation and Rehabilitation!\n\n"
                            "Verify that you can confidently tick off every syllabus benchmark:\n\n"
                            "- [x] I can define and distinguish between Land Reclamation and Land Rehabilitation.\n"
                            "- [x] I can explain the 4 factors determining water demand for irrigation.\n"
                            "- [x] I can describe the 6 methods of irrigation and evaluate the multi-purpose role of dams.\n"
                            "- [x] I can explain how swamp drainage is executed (Kakuzi bio-drainage, Yala/Bunyala projects).\n"
                            "- [x] I can list the 6 integrated tsetse fly control methods developed by ICIPE.\n"
                            "- [x] I can describe the 9 land rehabilitation methods and the Haller Park case study.\n"
                            "- [x] I can analyze the locational factors, operations, crops, and problems of Mwea and Perkerra.\n"
                            "- [x] I can trace the 7 sequential stages of polder reclamation in the Netherlands.\n"
                            "- [x] I can construct a structured 6-point comparative essay contrasting Kenya and the Netherlands."
                        )
                    }
                }
            ]
        }
    ]
}


# =============================================================================
# MAIN INGESTION PIPELINE
# =============================================================================

ALL_LESSONS = [
    LESSON_1_DATA,
    LESSON_2_DATA,
    LESSON_3_DATA,
    LESSON_4_DATA,
    LESSON_5_DATA
]

def run_ingestion(replace=False):
    print("=" * 80)
    print("VLearn Form 4 Geography — Topic 1: Land Reclamation and Rehabilitation")
    print("High-Structure Ingestion Engine")
    print("=" * 80)

    with transaction.atomic():
        # 1. Resolve Curriculum, Grade, and Subject
        curriculum = Curriculum.objects.get(name="844")
        grade = Grade.objects.get(curriculum=curriculum, name="Form 4")
        subject = Subject.objects.get(grade=grade, name="Geography")
        print(f"[*] Resolved Target: {curriculum.name} -> {grade.name} -> {subject.name} (ID: {subject.id})")

        # 2. Get or create Topic 1
        topic, created = Topic.objects.get_or_create(
            subject=subject,
            name="Land Reclamation and Rehabilitation",
            defaults={"order": 1, "description": "Form 4 Geography Topic 1: Land Reclamation and Rehabilitation"}
        )
        if not created and replace:
            print(f"[*] Updating existing Topic: {topic.name}")
        else:
            print(f"[{'+' if created else '*'}] Topic: {topic.name} (ID: {topic.id})")

        total_pages = 0
        total_blocks = 0

        # 3. Ingest Each Lesson & Learning Unit
        for l_data in ALL_LESSONS:
            unit_name = l_data["unit_name"]
            unit_order = l_data["unit_order"]
            lesson_title = l_data["lesson_title"]
            pages = l_data["pages"]

            # Get or create Learning Unit
            unit, u_created = LearningUnit.objects.get_or_create(
                topic=topic,
                name=unit_name,
                defaults={"order": unit_order, "description": f"Learning Unit {unit_order}: {unit_name}"}
            )
            if not u_created:
                unit.order = unit_order
                unit.save()

            # Get or create Lesson
            lesson = Lesson.objects.filter(topic=topic, learning_unit=unit).first()
            if not lesson:
                lesson = Lesson.objects.create(
                    topic=topic,
                    learning_unit=unit,
                    title=lesson_title,
                    status="published",
                    version=1
                )
                print(f"  [+] Created Lesson: {lesson.title} (ID: {lesson.id})")
            else:
                lesson.title = lesson_title
                lesson.status = "published"
                lesson.save()
                print(f"  [*] Found Existing Lesson: {lesson.title} (ID: {lesson.id})")

            if replace:
                deleted_count, _ = lesson.blocks.all().delete()
                print(f"      [!] Cleared {deleted_count} existing blocks for clean rebuild.")

            block_order_counter = 10

            for page in pages:
                page_num = page["page_number"]
                page_title = page["page_title"]
                blocks = page["blocks"]
                total_pages += 1

                for comp_idx, block_info in enumerate(blocks, 1):
                    b_type = block_info["block_type"]
                    c_type = block_info["component_type"]
                    b_title = block_info.get("title", page_title)
                    b_content = clean_content_dict(block_info.get("content", {}))

                    block, b_created = LessonBlock.objects.get_or_create(
                        lesson=lesson,
                        page_number=page_num,
                        component_order=comp_idx,
                        defaults={
                            "block_type": b_type,
                            "component_type": c_type,
                            "title": b_title,
                            "page_title": page_title,
                            "order": block_order_counter,
                            "content": b_content,
                            "metadata": {"concept_group": page_title}
                        }
                    )

                    if not b_created:
                        block.block_type = b_type
                        block.component_type = c_type
                        block.title = b_title
                        block.page_title = page_title
                        block.order = block_order_counter
                        block.content = b_content
                        block.metadata = {"concept_group": page_title}
                        block.save()

                    block_order_counter += 10
                    total_blocks += 1

            print(f"      [OK] Ingested {len(pages)} Pages for Lesson {unit_order}.")

        print("=" * 80)
        print(f"[SUCCESS] Form 4 Geography Topic 1 Ingestion Complete!")
        print(f"[*] Total Lessons Ingested: {len(ALL_LESSONS)}")
        print(f"[*] Total Pages Ingested:   {total_pages}")
        print(f"[*] Total Blocks Ingested:  {total_blocks}")
        print("=" * 80)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Ingest Form 4 Geography Topic 1")
    parser.add_argument("--replace", action="store_true", help="Replace existing blocks with a fresh rebuild")
    args = parser.parse_args()

    run_ingestion(replace=args.replace)
