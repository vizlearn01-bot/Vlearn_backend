"""
VLearn Form 4 Geography — Topic 2: Fishing
Production Curriculum Ingestion Engine

Topic: Fishing
Grade: Form 4 (Grade ID: 4)
Subject: Geography (Subject ID: 18)
Curriculum: 844 (Curriculum ID: 4)

Decomposed Learning Units & Lessons:
  Unit 1: Foundations of Fishing and Geographical Factors (12 Pages)
  Unit 2: Classification and Traditional Fishing Methods (12 Pages)
  Unit 3: Modern Commercial Fishing Methods and Ecological Impact (12 Pages)
  Unit 4: Major World Marine Fishing Grounds (14 Pages)
  Unit 5: East African and Kenyan Fisheries (16 Pages)
  Unit 6: Comparative Analysis (Kenya vs Japan) and Fisheries Management (16 Pages)

Total Pages: 82
Total Blocks: 130+

Usage:
  ./venv/bin/python curriculum/ingest_form4_geography_topic2.py --replace
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
from curriculum.models import Curriculum, Grade, Subject, Topic, LearningUnit, Lesson, LessonBlock

# Regex cleaner for bracket citations like [13], [14, 24], [S1, p. 1]
BRACKET_CITATION_RE = re.compile(r'\s*\[(?:\d+|image_\d+|S\d+.*?|[\d,\s]+)\]')

def clean_text(text: str) -> str:
    if not text or not isinstance(text, str):
        return text
    cleaned = BRACKET_CITATION_RE.sub('', text)
    cleaned = cleaned.replace(r'\(', '').replace(r'\)', '').replace(r'$$', '')
    return cleaned.strip()

def clean_block_content(content: dict) -> dict:
    if not isinstance(content, dict):
        return content
    res = {}
    for k, v in content.items():
        if isinstance(v, str):
            res[k] = clean_text(v)
        elif isinstance(v, list):
            new_list = []
            for item in v:
                if isinstance(item, str):
                    new_list.append(clean_text(item))
                elif isinstance(item, dict):
                    new_list.append(clean_block_content(item))
                elif isinstance(item, list):
                    new_list.append([clean_text(x) if isinstance(x, str) else x for x in item])
                else:
                    new_list.append(item)
            res[k] = new_list
        elif isinstance(v, dict):
            res[k] = clean_block_content(v)
        else:
            res[k] = v
    return res


# =============================================================================
# TOPIC 2 LESSON DEFINITIONS (82 PAGES)
# =============================================================================

LESSONS_CONFIG = [
    # -------------------------------------------------------------------------
    # LESSON 1: Foundations of Fishing and Geographical Factors (12 Pages)
    # -------------------------------------------------------------------------
    {
        "unit_order": 1,
        "unit_name": "Foundations of Fishing and Geographical Factors",
        "lesson_title": "Foundations of Fishing and Geographical Factors",
        "pages": [
            {
                "page_number": 1,
                "page_title": "Introduction to Fishing and Aquatic Exploitation",
                "blocks": [
                    {
                        "block_type": "learning_goal",
                        "component_type": "learning_goal",
                        "title": "Learning Goals: Foundations of Fishing",
                        "content": {
                            "text": (
                                "By the end of this lesson, you should be able to:\n"
                                "1. Define the terms **fishing** and **fishery** using precise geographical vocabulary.\n"
                                "2. Explain the five primary physical factors that govern global marine and freshwater fish distribution.\n"
                                "3. Analyze the six human socio-economic drivers essential for commercial fishery development."
                            )
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Fishing as a Primary Economic Activity",
                        "content": {
                            "text": (
                                "Fishing is one of the oldest primary economic activities of humankind, dealing with the extraction of valuable aquatic resources. "
                                "Across the globe, aquatic bodies—ranging from vast oceans to inland lakes and rivers—sustain complex biological food webs. "
                                "The spatial distribution of fisheries is not random; it is strictly controlled by a combination of physical oceanographic conditions and human economic systems."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 2,
                "page_title": "Defining Fishing and Fisheries",
                "blocks": [
                    {
                        "block_type": "definition_card",
                        "component_type": "definition_card",
                        "title": "Geographical Definition of Fishing and Fishery",
                        "content": {
                            "term": "Fishing & Fishery",
                            "definition": (
                                "**Fishing** is the act of catching fish and exploiting other aquatic animals (such as crabs, lobsters, seals, and whales).\n\n"
                                "A **Fishery** refers to a specific geographic area or water body where aquatic resources are commercially or traditionally exploited. Fisheries exist in both saltwater (marine) and freshwater environments."
                            )
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Scope of Aquatic Exploitation",
                        "content": {
                            "text": (
                                "While finfish (such as tilapia, salmon, tuna, and cod) represent the largest harvest volume, geographical fisheries also include the extraction of crustaceans (crabs, prawns, lobsters), molluscs (oysters, squid), and marine mammals (seals, whales) in designated polar and temperate zones."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 3,
                "page_title": "Physical Factor 1: Continental Shelf & Plankton",
                "blocks": [
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "The Photic Zone and Continental Shelves",
                        "content": {
                            "text": (
                                "Plankton are microscopic marine organisms (phytoplankton and zooplankton) that form the foundational base of all aquatic food chains. "
                                "Phytoplankton require solar radiation for photosynthesis, which restricts their thriving zone to the **photic zone**—water depths shallower than **180 metres**.\n\n"
                                "Consequently, broad, gently sloping **continental shelves** provide extensive sunlit shallows where plankton multiply in vast numbers, attracting massive shoals of fish."
                            )
                        }
                    },
                    {
                        "block_type": "suggested_diagram",
                        "component_type": "suggested_diagram",
                        "title": "Continental Shelf & Photic Zone Cross-Section",
                        "content": {
                            "text": "Cross-sectional engineering schematic showing sunlight penetration across a shallow continental shelf (0 to 180m), photic zone plankton blooms, and fish shoals."
                        }
                    }
                ]
            },
            {
                "page_number": 4,
                "page_title": "Physical Factor 2: Nature of the Coastline",
                "blocks": [
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Indented Coasts, Fiords, and Spawning Bays",
                        "content": {
                            "text": (
                                "The physical configuration of the shoreline plays a vital role in marine ecology:\n"
                                "1. **Spawning and Breeding Grounds:** Highly indented coastlines featuring sheltered bays, estuaries, and drowned glaciated valleys (**fiords**) provide calm, predator-sheltered water ideal for egg laying and juvenile fish development.\n"
                                "2. **Natural Harbours:** Deep, sheltered coastal inlets protect fishing vessels from violent ocean storms and provide natural anchorages for modern fishing ports."
                            )
                        }
                    },
                    {
                        "block_type": "callout",
                        "component_type": "callout",
                        "title": "Geographical Principle: Smooth vs Indented Coasts",
                        "content": {
                            "callout_type": "important",
                            "text": "Smooth, unindented coastlines exposed to open ocean swells make vessel beaching dangerous and lack calm, sheltered bays required for fish breeding. In contrast, glaciated fiord coastlines (such as in Norway and Alaska) represent the world's finest natural fishery harbours."
                        }
                    }
                ]
            },
            {
                "page_number": 5,
                "page_title": "Physical Factor 3: Relief of Adjacent Land",
                "blocks": [
                    {
                        "block_type": "suggested_image",
                        "component_type": "suggested_image",
                        "title": "Glaciated Fiord Coastline in Norway Providing Natural Sheltered Inlets",
                        "content": {
                            "text": "Steep, mountainous glaciated fiords in Western Norway where rugged land topography limits crop farming, driving communities to marine fishing."
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "The Economic Push Factor of Mountainous Relief",
                        "content": {
                            "text": (
                                "In countries characterized by steep, rugged, and mountainous topography—such as Japan, Norway, and British Columbia (Canada)—the land is severely unsuited for commercial crop farming.\n\n"
                                "This lack of arable agricultural land acts as a powerful geographical **push factor**, compelling coastal populations to exploit the sea as their primary source of food protein, employment, and national revenue."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 6,
                "page_title": "Physical Factor 4: Climatic Water Temperatures",
                "blocks": [
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Water Temperature and Plankton Proliferation",
                        "content": {
                            "text": (
                                "Ocean water temperature directly controls the biological productivity of marine ecosystems:\n\n"
                                "• **Cool Temperate Waters (10°C to 15°C):** Cool waters facilitate the massive flourishing of plankton. This supports immense, single-species shoals of fish (e.g., millions of herring, cod, or mackerel), enabling highly cost-effective commercial harvesting.\n\n"
                                "• **Warm Tropical Waters (>20°C):** Warm water temperatures severely restrict plankton growth. Although tropical seas exhibit high species diversity (many different species), the total population of any single commercial species remains relatively low."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 7,
                "page_title": "Physical Factor 5: Ocean Current Convergence",
                "blocks": [
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Current Convergence and Nutrient Upwelling",
                        "content": {
                            "text": (
                                "The convergence of warm and cold ocean currents creates the world's richest fishing zones:\n"
                                "1. **Nutrient Upwelling:** When dense cold currents collide with warm surface currents, a dynamic vertical circulation (upwelling) carries mineral-rich organic nutrients from the ocean floor up to the sunlit photic zone.\n"
                                "2. **Water Oxygenation:** The violent vertical mixing enriches the water with dissolved oxygen, vital for marine respiration.\n"
                                "3. **Temperature Moderation:** Cold currents cool tropical seas (e.g., Benguela Current along SW Africa; Canary Current along NW Africa), creating optimal thermal conditions for plankton."
                            )
                        }
                    },
                    {
                        "block_type": "suggested_diagram",
                        "component_type": "suggested_diagram",
                        "title": "Ocean Current Convergence & Nutrient Upwelling Mechanism",
                        "content": {
                            "text": "Cross-sectional diagram showing the convergence of warm and cold ocean currents, vertical convective overturn, nutrient upwelling from the seabed, and dense plankton blooms."
                        }
                    }
                ]
            },
            {
                "page_number": 8,
                "page_title": "Human Factors Influencing Fishing",
                "blocks": [
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Socio-Economic Drivers of Modern Fisheries",
                        "content": {
                            "text": (
                                "Even where physical conditions are ideal, commercial exploitation requires robust human systems:\n\n"
                                "1. **Labour Supply:** Commercial fishing and fish processing require abundant skilled and semi-skilled labor for vessel navigation, net handling, filleting, and canning.\n"
                                "2. **Market Demand & Diet:** High-density populations with strong purchasing power and established fish-eating cultures (such as Japan, China, Western Europe, and the USA) provide sustained demand.\n"
                                "3. **Preservation & Cold Chains:** Because fish is highly perishable, modern fleets rely on refrigerated mother ships, ice plants, and cold-storage distribution networks.\n"
                                "4. **Capital Investment:** Immense capital is necessary to purchase modern trawlers, pay trained crews, and construct processing factories.\n"
                                "5. **Advanced Technology:** Utilization of radar, sonar, echo-sounders, and satellite imagery to accurately locate submerged fish shoals."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 9,
                "page_title": "Physical vs Human Factor Synthesis",
                "blocks": [
                    {
                        "block_type": "comparison_table",
                        "component_type": "comparison_table",
                        "title": "Geographical Factors Controlling World Fisheries",
                        "content": {
                            "headers": ["Category", "Key Determinant", "Geographical Mechanism", "Global Example"],
                            "rows": [
                                ["Physical", "Photic Zone Depth", "Sunlight reaches <180m, maximizing plankton photosynthesis", "Grand Bank, North Sea"],
                                ["Physical", "Coastline Indentation", "Fiords and bays provide calm spawning zones and natural ports", "Norwegian Coast, Japan"],
                                ["Physical", "Rugged Land Relief", "Lack of arable soils pushes populations toward maritime economy", "Japan, Norway, Alaska"],
                                ["Physical", "Current Convergence", "Upwelling lifts deep organic nutrients into the photic zone", "Kuroshiwo + Oyashiwo (Japan)"],
                                ["Human", "Market & Culture", "Densely populated nations maintain high domestic demand", "Japan, SE Asia, Western Europe"],
                                ["Human", "Advanced Technology", "Sonar and factory trawlers permit continuous deep-sea harvest", "Northwest Pacific, North Atlantic"]
                            ]
                        }
                    }
                ]
            },
            {
                "page_number": 10,
                "page_title": "Interactive Factor-to-Effect Matching",
                "blocks": [
                    {
                        "block_type": "mini_activity",
                        "component_type": "mini_activity",
                        "title": "Geographical Reasoning: Factor-to-Effect Matching",
                        "content": {
                            "activity_type": "matching_scenario",
                            "instructions": "Match each geographical factor with its correct physical or human effect.",
                            "pairs": [
                                {"factor": "Rugged, mountainous adjacent relief", "effect": "Restricts agriculture, forcing reliance on the sea for livelihood"},
                                {"factor": "Photic zone boundary (<180m depth)", "effect": "Enables solar penetration for phytoplankton photosynthesis"},
                                {"factor": "Cold ocean current washing tropical coast", "effect": "Cools surface water to induce plankton blooms"},
                                {"factor": "Highly indented fiord coastline", "effect": "Provides sheltered spawning bays and storm-protected harbours"}
                            ]
                        }
                    }
                ]
            },
            {
                "page_number": 11,
                "page_title": "Knowledge Checkpoint: Foundations of Fishing",
                "blocks": [
                    {
                        "block_type": "knowledge_check",
                        "component_type": "knowledge_check",
                        "title": "Concept Diagnostic: Oceanographic Drivers",
                        "content": {
                            "check_type": "multiple_choice",
                            "question": "Why are broad continental shelves significantly more productive fishing grounds than deep oceanic trenches exceeding 2,000 metres?",
                            "options": [
                                "Deep oceanic trenches lack salt, making them uninhabitable for marine fish",
                                "Continental shelves lie within the sunlit photic zone (<180m), allowing massive plankton photosynthesis to support fish shoals",
                                "Deep trenches have warm water temperatures that instantly kill marine plankton",
                                "Continental shelves are completely free of ocean currents and waves"
                            ],
                            "answer": "B",
                            "explanation": "Phytoplankton require sunlight to carry out photosynthesis. Sunlight penetrates effectively only down to about 180 metres (the photic zone). Broad continental shelves lie within this shallow zone, allowing rich plankton growth that sustains large fish populations, whereas deep ocean trenches are dark and biological deserts by comparison."
                        }
                    }
                ]
            },
            {
                "page_number": 12,
                "page_title": "Foundations of Fishing: Key Takeaways",
                "blocks": [
                    {
                        "block_type": "summary",
                        "component_type": "summary",
                        "title": "Summary: Foundations of Fishing and Geographical Factors",
                        "content": {
                            "key_points": [
                                "Fishing involves the harvesting of finfish, crustaceans, molluscs, and marine mammals across marine and freshwater fisheries.",
                                "The 5 primary physical controls are: broad continental shelves (<180m photic zone), indented fiord coastlines, mountainous adjacent relief (push factor), cool temperate water temperatures, and ocean current convergences.",
                                "Current convergences (e.g., Gulf Stream/Labrador or Kuroshiwo/Oyashiwo) drive vertical nutrient upwelling and oxygenation.",
                                "Human exploitation depends on skilled labour, accessible capital, electronic fish-detection gear (sonar/radar), and robust cold-chain preservation networks."
                            ]
                        }
                    }
                ]
            }
        ]
    },

    # -------------------------------------------------------------------------
    # LESSON 2: Classification and Traditional Fishing Methods (12 Pages)
    # -------------------------------------------------------------------------
    {
        "unit_order": 2,
        "unit_name": "Classification and Traditional Fishing Methods",
        "lesson_title": "Classification and Traditional Fishing Methods",
        "pages": [
            {
                "page_number": 1,
                "page_title": "Introduction to Fishery Classification",
                "blocks": [
                    {
                        "block_type": "learning_goal",
                        "component_type": "learning_goal",
                        "title": "Learning Goals: Types & Traditional Methods",
                        "content": {
                            "text": (
                                "By the end of this lesson, you should be able to:\n"
                                "1. Classify fisheries into four distinct ecological types based on depth, distance from shore, and salinity.\n"
                                "2. Differentiate between Pelagic and Demersal fish species and their environmental adaptations.\n"
                                "3. Describe the mechanics, gear, and limitations of seven traditional fishing methods."
                            )
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Spatial and Ecological Zonation of Fisheries",
                        "content": {
                            "text": (
                                "Fisheries are classified into distinct ecological categories based on water depth, distance from the shore, and water salinity. "
                                "Understanding these zones is essential because each zone requires specialized harvesting gear adapted to the behavior and habitat of target fish species."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 2,
                "page_title": "The Four Primary Types of Fishing",
                "blocks": [
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "The Four Fishery Domains",
                        "content": {
                            "text": (
                                "1. **Pelagic Fishing:** Harvesting fish that live and swim in large shoals close to the surface of open ocean waters (e.g., tuna, mackerel, herring, sardines).\n\n"
                                "2. **Demersal Fishing:** Harvesting bottom-dwelling fish that live and feed on or near the deep ocean seabed (e.g., cod, haddock, halibut, pollock).\n\n"
                                "3. **Inshore Fishing:** Conducted close to the shoreline in shallow, sheltered bays, estuaries, and tidal mangrove creeks for high-value crustaceans (crabs, prawns, lobsters).\n\n"
                                "4. **Freshwater Fishing:** Practiced in inland lakes, rivers, streams, ponds, and flooded paddy fields (e.g., tilapia, Nile perch, trout, mudfish)."
                            )
                        }
                    },
                    {
                        "block_type": "suggested_diagram",
                        "component_type": "suggested_diagram",
                        "title": "The Four Types of Fishing Taxonomy Tree & Depth Profile",
                        "content": {
                            "text": "Taxonomic hierarchy and ocean depth profile diagram illustrating Pelagic (surface), Demersal (benthic seabed), Inshore (estuarine), and Freshwater (inland) fishery domains."
                        }
                    }
                ]
            },
            {
                "page_number": 3,
                "page_title": "Pelagic vs Demersal Fish Characteristics",
                "blocks": [
                    {
                        "block_type": "comparison_table",
                        "component_type": "comparison_table",
                        "title": "Comparison: Pelagic vs Demersal Fisheries",
                        "content": {
                            "headers": ["Feature", "Pelagic Fishery", "Demersal Fishery"],
                            "rows": [
                                ["Habitat Zone", "Surface to upper photic layer of open seas", "Deep ocean floor and benthic seabed"],
                                ["Key Species", "Herring, Mackerel, Sardines, Tuna, Menhaden", "Cod, Haddock, Halibut, Alaska Pollock"],
                                ["Shoaling Habit", "Dense, massive surface shoals", "Scattered bottom-feeding populations"],
                                ["Dominant Modern Gear", "Purse Seining, Drift Nets", "Bottom Trawling, Long Lining"],
                                ["Ecological Vulnerability", "Susceptible to over-encirclement of entire schools", "Severe sea floor and coral habitat destruction"]
                            ]
                        }
                    }
                ]
            },
            {
                "page_number": 4,
                "page_title": "Traditional Method 1: Woven Basket Traps",
                "blocks": [
                    {
                        "block_type": "definition_card",
                        "component_type": "definition_card",
                        "title": "Woven Basket Method",
                        "content": {
                            "term": "Basket Trap",
                            "definition": (
                                "A conical or cylindrical woven basket fitted with an inverted, funnel-shaped entrance. "
                                "Baited with food and placed in shallow river pools or lake fringes. Fish enter easily following the funnel taper but cannot find the small exit opening to escape."
                            )
                        }
                    },
                    {
                        "block_type": "suggested_diagram",
                        "component_type": "suggested_diagram",
                        "title": "Mechanics of Traditional Basket Trap and Gill Netting",
                        "content": {
                            "text": "Technical illustration contrasting the non-return funnel mechanism of a traditional woven basket trap with the operculum-trapping action of a gill net mesh."
                        }
                    }
                ]
            },
            {
                "page_number": 5,
                "page_title": "Traditional Method 2 & 3: Harpoons and Barriers",
                "blocks": [
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Harpooning (Spearing) and Reed Barriers",
                        "content": {
                            "text": (
                                "• **Harpooning (Spearing):** A pointed stick, metal spear, or bow-and-arrow is cast directly at visible fish in clear, shallow waters. This method is highly selective (catching one fish at a time) but is dangerous in waters inhabited by hippos and crocodiles.\n\n"
                                "• **Barrier Method:** Temporary dams or fences woven from sticks, reeds, and mud are erected across flooded river channels. When floodwaters recede after rains, fish are stranded on the upstream side and easily scooped by hand or basket."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 6,
                "page_title": "Traditional Method 4 & 5: Herbs & Lantern Fishing",
                "blocks": [
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Organic Plant Toxins and Night Lantern Attraction",
                        "content": {
                            "text": (
                                "• **Herb Stunning:** Crushed roots, bark, or leaves of specific toxic plants are sprinkled into calm, sluggish river pools. The natural chemical extracts deoxygenate the water or stun the fish, causing them to float to the surface where they are gathered by hand.\n\n"
                                "• **Lamp and Net (Lantern Fishing):** Practiced on Lake Victoria and Lake Tanganyika to catch **Dagaa / Omena** (*Rastrineobola argentea*). Pressure paraffin lamps mounted on the bows of wooden canoes attract light-sensitive fish to the surface at night, where they are scooped with fine hand nets."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 7,
                "page_title": "Traditional Method 6 & 7: Hook & Line and Gill Nets",
                "blocks": [
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Line Hooking and Gill Net Mesh Action",
                        "content": {
                            "text": (
                                "• **Hook and Line:** A baited metal or bone hook attached to a single line and sinker is cast into the water. When a fish swallows the bait, the hook catches in its mouth, and the fisherman immediately pulls it ashore.\n\n"
                                "• **Gill Nets:** Vertical curtains of netting suspended in the water column using surface floats and bottom weights. The mesh size is precisely calibrated: fish swim into the mesh, their heads pass through, but their bodies cannot. When attempting to reverse out, their gill covers (**opercula**) catch in the twine, trapping them securely."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 8,
                "page_title": "Traditional Artisanal Fishing in Practice",
                "blocks": [
                    {
                        "block_type": "suggested_image",
                        "component_type": "suggested_image",
                        "title": "Traditional Wooden Dhows on the Coastal Waters of Kenya",
                        "content": {
                            "text": "Artisanal fishermen operating traditional wooden dhows and dugout canoes along the East African coast using hand lines and cast nets."
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Socio-Economic Nature of Traditional Fishing",
                        "content": {
                            "text": (
                                "Traditional methods are characterized by low capital requirements, handmade non-motorized craft (dugout canoes, dhows), and localized subsistence consumption. "
                                "While ecologically low-impact when practiced at small scales, their total yield cannot meet the food security demands of rapidly expanding urban populations."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 9,
                "page_title": "Common Exam Mistakes: Gear vs Methods",
                "blocks": [
                    {
                        "block_type": "common_mistake",
                        "component_type": "common_mistake",
                        "title": "Exam Trap: Gill Netting vs Cast Netting",
                        "content": {
                            "mistake": "Describing gill netting as sweeping or enclosing all fish like a bag net.",
                            "correction": "Gill nets are passive vertical walls designed with specific mesh apertures that selectively catch mature fish by their gill covers (opercula) as they swim forward.",
                            "exam_tip": "In KCSE questions, emphasize that gill nets are size-selective depending on mesh size, whereas purse seines and trawls are active sweeping gear."
                        }
                    }
                ]
            },
            {
                "page_number": 10,
                "page_title": "Interactive Traditional Gear Evaluation",
                "blocks": [
                    {
                        "block_type": "mini_activity",
                        "component_type": "mini_activity",
                        "title": "Traditional Gear Assessment Matrix",
                        "content": {
                            "activity_type": "gear_classification",
                            "instructions": "Evaluate the selectivity and catch volume of each traditional fishing method.",
                            "data": [
                                {"method": "Spearing / Harpooning", "selectivity": "Extremely High (1 fish at a time)", "volume": "Subsistence only", "risk": "Dangerous (Crocodiles/Hippos)"},
                                {"method": "Woven Basket Trap", "selectivity": "Moderate (size dependent on opening)", "volume": "Low to Moderate", "risk": "Safe in shallow pools"},
                                {"method": "Lantern Night Fishing", "selectivity": "Low (attracts all phototaxic shoals)", "volume": "High (Omena shoals)", "risk": "Night storm exposure"},
                                {"method": "Gill Net", "selectivity": "High (controlled by mesh size)", "volume": "Moderate to High", "risk": "Net tangling in weeds"}
                            ]
                        }
                    }
                ]
            },
            {
                "page_number": 11,
                "page_title": "Knowledge Checkpoint: Traditional Fishing",
                "blocks": [
                    {
                        "block_type": "knowledge_check",
                        "component_type": "knowledge_check",
                        "title": "Concept Diagnostic: Mechanics of Gill Netting",
                        "content": {
                            "check_type": "multiple_choice",
                            "question": "How does a legally regulated gill net selectively capture mature fish while conserving juvenile breeding stock?",
                            "options": [
                                "The net uses electric currents that repel small juvenile fish",
                                "The mesh size is large enough to allow small fish to swim through freely, while mature fish pass their heads through and get trapped by their gill covers (opercula)",
                                "The net is dragged along the seabed to scoop only heavy bottom-dwelling adult fish",
                                "The net emits chemical odours that only attract fully grown adult fish"
                            ],
                            "answer": "B",
                            "explanation": "A properly sized gill net functions mechanically: juvenile fish easily pass straight through the mesh openings without hindrance. Mature fish can only fit their heads through; when they attempt to back out, the twine catches behind their gill covers (opercula), preventing escape."
                        }
                    }
                ]
            },
            {
                "page_number": 12,
                "page_title": "Traditional Methods: Key Takeaways",
                "blocks": [
                    {
                        "block_type": "summary",
                        "component_type": "summary",
                        "title": "Summary: Classification and Traditional Fishing Methods",
                        "content": {
                            "key_points": [
                                "Fisheries are divided into Pelagic (surface ocean), Demersal (benthic ocean floor), Inshore (estuarine shallows), and Freshwater (inland lakes/rivers).",
                                "Pelagic species (tuna, mackerel, sardines) swim in surface shoals; Demersal species (cod, haddock) feed on the ocean floor.",
                                "Traditional methods include woven baskets, harpooning, reed barriers, herb stunning, lantern night fishing (Dagaa), hook & line, and gill nets.",
                                "Gill netting is a passive, size-selective method that traps fish by the operculum, whereas traditional artisanal gear remains low-yield and subsistence-based."
                            ]
                        }
                    }
                ]
            }
        ]
    },

    # -------------------------------------------------------------------------
    # LESSON 3: Modern Commercial Fishing Methods and Ecological Impact (12 Pages)
    # -------------------------------------------------------------------------
    {
        "unit_order": 3,
        "unit_name": "Modern Commercial Fishing Methods and Ecological Impact",
        "lesson_title": "Modern Commercial Fishing Methods and Ecological Impact",
        "pages": [
            {
                "page_number": 1,
                "page_title": "The Commercial Fishing Revolution",
                "blocks": [
                    {
                        "block_type": "learning_goal",
                        "component_type": "learning_goal",
                        "title": "Learning Goals: Commercial Fishing & Ecology",
                        "content": {
                            "text": (
                                "By the end of this lesson, you should be able to:\n"
                                "1. Explain the engineering mechanics of Purse Seining, Trawling, and Long Lining.\n"
                                "2. Analyze the operational role of modern factory trawlers and on-board processing.\n"
                                "3. Evaluate the severe ecological impacts of industrial gear (benthic destruction, bycatch, overfishing)."
                            )
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Mechanization of the Marine Harvest",
                        "content": {
                            "text": (
                                "Modern commercial fishing is characterized by heavy capital investment, motorized vessels, synthetic fiber nets, electronic sonar detection, and mechanical winches. "
                                "These methods can extract hundreds of tonnes of fish in a single haul, revolutionizing global food production while creating unprecedented ecological pressures on marine habitats."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 2,
                "page_title": "Commercial Method 1: Purse Seining",
                "blocks": [
                    {
                        "block_type": "definition_card",
                        "component_type": "definition_card",
                        "title": "Purse Seining Definition & Target",
                        "content": {
                            "term": "Purse Seining",
                            "definition": (
                                "A commercial fishing method designed to encircle massive surface shoals of pelagic fish (such as herring, sardines, and tuna) using a giant wall of netting. "
                                "The top edge is kept afloat by cork floats, while the weighted bottom edge is cinched shut like a drawstring purse using a heavy steel cable."
                            )
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Step-by-Step Operation of a Purse Seine",
                        "content": {
                            "text": (
                                "1. **Locating the Shoal:** Sonar, spotter helicopters, or radar detect a dense surface school of pelagic fish.\n"
                                "2. **Encirclement:** A small skiff boat deploys one end of the seine net, circling rapidly around the shoal while paying out the net from the main vessel.\n"
                                "3. **Pursing:** Once the circle is closed, a mechanical winch pulls the bottom purse wire tight, closing the bottom of the net into a bowl shape and preventing fish from diving.\n"
                                "4. **Hauling:** The net is drawn aboard, and a hydraulic vacuum hose or dip net pumps thousands of fish into refrigerated hold tanks."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 3,
                "page_title": "Engineering Schematics of Purse Seining",
                "blocks": [
                    {
                        "block_type": "suggested_diagram",
                        "component_type": "suggested_diagram",
                        "title": "Operational Mechanics of Purse Seining (Surface Pelagic)",
                        "content": {
                            "text": "Detailed vector schematic illustrating the 4 stages of purse seining: shoal encirclement, surface floatline, leadline, bottom purse cable cinching, and catch pumping."
                        }
                    },
                    {
                        "block_type": "callout",
                        "component_type": "callout",
                        "title": "Ecological Danger of Purse Seining",
                        "content": {
                            "callout_type": "warning",
                            "text": "Purse seines are highly non-selective when enclosing schools. If spotter technology detects a spawning aggregation, an entire regional cohort can be wiped out in hours, risking immediate population collapse."
                        }
                    }
                ]
            },
            {
                "page_number": 4,
                "page_title": "Commercial Method 2: Trawling",
                "blocks": [
                    {
                        "block_type": "definition_card",
                        "component_type": "definition_card",
                        "title": "Trawling Definition & Target",
                        "content": {
                            "term": "Bottom Trawling",
                            "definition": (
                                "A commercial method where a large, funnel-shaped bag net (trawl net) is dragged along the deep ocean floor by a powerful trawler vessel to sweep up demersal fish (cod, haddock, halibut, pollock) and benthic crustaceans (prawns)."
                            )
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Components of a Trawl Net",
                        "content": {
                            "text": (
                                "• **Otter Boards (Trawl Doors):** Heavy steel hydrodynamic plates that act like kites, spreading the mouth of the net horizontally as water flows over them.\n\n"
                                "• **Headrope & Footrope:** The upper mouth has plastic floats, while the lower footrope is fitted with heavy steel bobbins or rubber discs that roll across the seabed.\n\n"
                                "• **Cod-End:** The narrow, reinforced rear pocket of the net where all swept fish accumulate under immense water pressure."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 5,
                "page_title": "Engineering Schematics of Bottom Trawling",
                "blocks": [
                    {
                        "block_type": "suggested_diagram",
                        "component_type": "suggested_diagram",
                        "title": "Bottom Trawling Operations and Benthic Habitat Disruption",
                        "content": {
                            "text": "Engineering schematic of a bottom trawler towing an otter trawl net along the seabed, showing otter boards, weighted footrope, cod-end accumulation, and seabed gouging."
                        }
                    },
                    {
                        "block_type": "callout",
                        "component_type": "callout",
                        "title": "Environmental Impact: Habitat Destruction",
                        "content": {
                            "callout_type": "caution",
                            "text": "Bottom trawling is the marine equivalent of clear-cutting a forest. Heavy steel otter boards and weighted footropes pulverize deep-sea coral reefs, destroy sponge beds, and generate massive volumes of discarded juvenile bycatch."
                        }
                    }
                ]
            },
            {
                "page_number": 6,
                "page_title": "Commercial Method 3: Line Fishing (Long Lining)",
                "blocks": [
                    {
                        "block_type": "definition_card",
                        "component_type": "definition_card",
                        "title": "Long Lining Definition & Target",
                        "content": {
                            "term": "Long Lining",
                            "definition": (
                                "A commercial method utilizing a single mainline that stretches from 10 to over 100 kilometres in length, suspended horizontally in the water. "
                                "Thousands of shorter vertical branch lines (snoods), each armed with a baited hook, hang from the mainline to target large predatory pelagic (tuna, swordfish) and demersal (cod, halibut) fish."
                            )
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Long Line Deployment and Radio Tracking",
                        "content": {
                            "text": (
                                "The mainline is deployed off the stern of the vessel at speeds up to 10 knots. Buoys and radio transmitters mark the position of the line across open ocean waters. "
                                "After soaking for several hours, the vessel retrieves the line using a mechanical hauler, systematically unhooking the fish and transferring them to flash-freezing lockers."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 7,
                "page_title": "Factory Trawlers and On-Board Processing",
                "blocks": [
                    {
                        "block_type": "suggested_image",
                        "component_type": "suggested_image",
                        "title": "Commercial Trawler Winching Up a Heavy Marine Net",
                        "content": {
                            "text": "Industrial commercial trawler winching up a massive net of deep-sea catch on the deck for automated mechanized processing."
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "The Industrial Factory Ship",
                        "content": {
                            "text": (
                                "Modern factory ships are floating industrial processing plants. Operating for 3 to 6 months at sea without docking, they feature:\n"
                                "1. **Automated Filleting Lines:** Computerized machines that gut, scale, fillet, and de-bone fish within minutes of capture.\n"
                                "2. **Plate Freezers:** Blast freezers that drop fish temperature to -40°C, locking in freshness.\n"
                                "3. **Fishmeal Plants:** Transforming fish waste (heads, viscera, bones) into protein meal and fish oil for animal feed."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 8,
                "page_title": "Comparative Matrix: Commercial Fishing Gear",
                "blocks": [
                    {
                        "block_type": "comparison_table",
                        "component_type": "comparison_table",
                        "title": "Engineering Comparison of Commercial Fishing Methods",
                        "content": {
                            "headers": ["Gear Type", "Target Ecological Zone", "Target Species", "Deployment Mechanism", "Major Environmental Drawback"],
                            "rows": [
                                ["Purse Seine", "Surface Pelagic", "Herring, Sardines, Tuna, Mackerel", "Surrounds shoals from sides & bottom with cinching cable", "Non-selective; risks total collapse of schooling cohorts"],
                                ["Bottom Trawl", "Deep Seabed Demersal", "Cod, Haddock, Halibut, Pollock, Prawns", "Funnel bag dragged across seabed held open by otter boards", "Catastrophic destruction of coral reefs and benthic habitats"],
                                ["Long Line", "Mid-Water & Demersal", "Tuna, Swordfish, Halibut, Shark", "10–100 km mainline with thousands of baited branch hooks", "Incidental bycatch of seabirds (albatross), turtles, and sharks"],
                                ["Drift Net", "Surface Pelagic", "Salmon, Squid, Mackerel", "Vertical curtain drifting with ocean current", "Ghost fishing when lost; high marine mammal entanglement"]
                            ]
                        }
                    }
                ]
            },
            {
                "page_number": 9,
                "page_title": "Ecological Crises of Industrial Fishing",
                "blocks": [
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Four Severe Ecological Crises",
                        "content": {
                            "text": (
                                "1. **Overexploitation & Stock Collapse:** Industrial efficiency extracts fish faster than natural biological reproduction rates (e.g., Grand Bank cod collapse in 1992).\n\n"
                                "2. **Bycatch & Discards:** Non-target species (dolphins, sea turtles, immature fish) caught in nets are discarded dead overboard.\n\n"
                                "3. **Benthic Habitat Destruction:** Trawl doors scour deep furrows in the seabed, pulverizing ancient cold-water coral reefs.\n\n"
                                "4. **Ghost Fishing:** Abandoned or lost non-biodegradable synthetic nylon nets drift indefinitely, trapping and killing marine life for decades."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 10,
                "page_title": "Interactive Commercial Gear Selection",
                "blocks": [
                    {
                        "block_type": "mini_activity",
                        "component_type": "mini_activity",
                        "title": "Commercial Fleet Operations Scenario",
                        "content": {
                            "activity_type": "gear_selection_simulation",
                            "instructions": "Select the appropriate commercial fishing gear for each target species and oceanographic condition.",
                            "scenarios": [
                                {"target": "Dense school of surface-swimming Sardines in shallow coastal water", "optimal_gear": "Purse Seine with surface skiff", "rationale": "Surrounds and cinches school without contacting bottom"},
                                {"target": "Solitary Halibut feeding on the sandy seabed at 300m depth", "optimal_gear": "Bottom Long Line or Demersal Trawl", "rationale": "Reaches benthic layer where demersal flatfish feed"},
                                {"target": "Scattered Yellowfin Tuna migrating across open high-seas waters", "optimal_gear": "Pelagic Long Line with radio buoys", "rationale": "Covers vast linear ocean distances for apex predators"}
                            ]
                        }
                    }
                ]
            },
            {
                "page_number": 11,
                "page_title": "Knowledge Checkpoint: Commercial Operations",
                "blocks": [
                    {
                        "block_type": "knowledge_check",
                        "component_type": "knowledge_check",
                        "title": "Concept Diagnostic: Trawling vs Seining",
                        "content": {
                            "check_type": "multiple_choice",
                            "question": "Which commercial fishing method causes the most severe physical destruction to the marine benthic (seabed) ecosystem, and why?",
                            "options": [
                                "Purse Seining, because the surface floats block sunlight from reaching the seabed",
                                "Bottom Trawling, because heavy steel otter boards and weighted footropes drag across the ocean floor, crushing corals and destroying benthic habitats",
                                "Long Lining, because baited hooks release toxic chemicals into deep water",
                                "Lantern Fishing, because bright night lights permanently blind deep-sea organisms"
                            ],
                            "answer": "B",
                            "explanation": "Bottom trawling involves dragging immense, heavily weighted funnel nets and steel otter boards directly across the fragile seabed. This physical scouring crushes coral structures, uproots deep-sea sponge communities, and destroys the delicate benthic habitats that demersal fish rely on for breeding and shelter."
                        }
                    }
                ]
            },
            {
                "page_number": 12,
                "page_title": "Commercial Methods: Key Takeaways",
                "blocks": [
                    {
                        "block_type": "summary",
                        "component_type": "summary",
                        "title": "Summary: Modern Commercial Fishing Methods and Ecological Impact",
                        "content": {
                            "key_points": [
                                "Purse Seining targets surface pelagic shoals by surrounding them and drawing a bottom cable tight like a drawstring purse.",
                                "Bottom Trawling drags a funnel net with otter boards and weighted footropes across the ocean seabed for demersal species.",
                                "Long Lining deploys mainlines up to 100 km long with thousands of baited snoods for predatory pelagic and demersal fish.",
                                "Factory ships process, fillet, and flash-freeze fish at sea, enabling multi-month high-seas operations.",
                                "Major ecological hazards include benthic habitat pulverization, massive juvenile bycatch, ghost fishing, and commercial stock collapse."
                            ]
                        }
                    }
                ]
            }
        ]
    },

    # -------------------------------------------------------------------------
    # LESSON 4: Major World Marine Fishing Grounds (14 Pages)
    # -------------------------------------------------------------------------
    {
        "unit_order": 4,
        "unit_name": "Major World Marine Fishing Grounds",
        "lesson_title": "Major World Marine Fishing Grounds",
        "pages": [
            {
                "page_number": 1,
                "page_title": "Global Distribution of Commercial Fisheries",
                "blocks": [
                    {
                        "block_type": "learning_goal",
                        "component_type": "learning_goal",
                        "title": "Learning Goals: World Fishing Grounds",
                        "content": {
                            "text": (
                                "By the end of this lesson, you should be able to:\n"
                                "1. Locate the four major Northern Hemisphere commercial marine fishing grounds on a world map.\n"
                                "2. Explain the physical and human factors driving productivity in each major marine region.\n"
                                "3. Analyze notable Southern Hemisphere upwelling fisheries (Humboldt, Benguela, Canary).\n"
                                "4. Construct structured, comparative KCSE essay responses on global fisheries."
                            )
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Why the Northern Hemisphere Dominates Global Fisheries",
                        "content": {
                            "text": (
                                "Commercial marine fishing is overwhelmingly concentrated in the temperate latitudes of the Northern Hemisphere. "
                                "This global asymmetry is driven by the presence of broad continental shelves, dynamic ocean current convergences, rugged glaciated coastlines, and densely populated industrial nations with massive market demand."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 2,
                "page_title": "Global Thematic Map of Fishing Grounds",
                "blocks": [
                    {
                        "block_type": "suggested_diagram",
                        "component_type": "suggested_diagram",
                        "title": "Global Thematic Map of Major World Fishing Grounds & Ocean Currents",
                        "content": {
                            "text": "World map illustrating the 4 major Northern Hemisphere fishing grounds (NW Atlantic, NE Atlantic, NW Pacific, NE Pacific), Southern upwelling zones, and intersecting warm and cold ocean currents."
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "The Four Major World Fishing Grounds",
                        "content": {
                            "text": (
                                "The world's four preeminent commercial fishing grounds are:\n"
                                "1. **Northwest Atlantic:** Eastern coast of North America (Grand Bank).\n"
                                "2. **Northeast Atlantic:** Western coast of Europe (North Sea, Norwegian coast).\n"
                                "3. **Northwest Pacific:** Eastern coast of Asia (Japan, China, Sea of Okhotsk) — *the world's largest*.\n"
                                "4. **Northeast Pacific:** Western coast of North America (Alaska, British Columbia, Oregon)."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 3,
                "page_title": "Northwest Atlantic Fishing Grounds (Grand Bank)",
                "blocks": [
                    {
                        "block_type": "suggested_diagram",
                        "component_type": "suggested_diagram",
                        "title": "Spatial Map of the Northwest Atlantic & Grand Bank Current Convergence",
                        "content": {
                            "text": "Regional spatial map showing the Grand Bank off Newfoundland, meeting of the cold Labrador Current and warm Gulf Stream, shallow banks (<180m), and fishing ports."
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Geographical Drivers of the Grand Bank",
                        "content": {
                            "text": (
                                "• **Vast Continental Shelf:** Includes the Grand Bank, George Bank, and Sable Bank with broad shallow waters within the photic zone.\n\n"
                                "• **Current Convergence:** The meeting of the **cold Labrador Current** and the **warm Gulf Stream Current** triggers massive upwelling of seabed nutrients, cools the water to ideal plankton temperatures, and keeps the area ice-free for most of the year.\n\n"
                                "• **Harsh Adjacent Climate & Relief:** Eastern Canada and New England experience severe winters and rocky glaciated soils unsuited for agriculture, forcing historical development of fishing.\n\n"
                                "• **Affluent Urban Market:** High-density urban corridors of the USA and Canada provide huge immediate purchasing power.\n\n"
                                "• **Target Species:** Cod (historically dominant), herring, mackerel, haddock, and lobsters."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 4,
                "page_title": "Northeast Atlantic Grounds (Western Europe)",
                "blocks": [
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Physical and Human Factors in Western Europe",
                        "content": {
                            "text": (
                                "• **Location:** Extends along the coasts of Norway, Great Britain, Denmark, Germany, and France, encompassing the shallow **North Sea** and **Dogger Bank**.\n\n"
                                "• **Indented Coastline & Fiords:** Western Norway's glaciated fiords provide calm, sheltered spawning waters protected from Atlantic gales, as well as natural ice-free deep-water harbours.\n\n"
                                "• **Warm North Atlantic Drift:** Keeps Western European ports completely ice-free year-round despite high northern latitudes.\n\n"
                                "• **Glacial Nutrient Enrichment:** Ancient glaciers transported mineral-rich sediments into the shallow North Sea basin, providing trace minerals for plankton growth.\n\n"
                                "• **Densely Populated Market:** Over 500 million European consumers with high purchasing power and modern road/rail cold chains.\n\n"
                                "• **Target Species:** Herring, cod, mackerel, and flatfish."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 5,
                "page_title": "Northeast Pacific Grounds (Pacific Northwest)",
                "blocks": [
                    {
                        "block_type": "suggested_image",
                        "component_type": "suggested_image",
                        "title": "Coho Salmon Spawning Run in the Pacific Northwest Rushing Rivers",
                        "content": {
                            "text": "Mature Pacific Salmon migrating upstream through rushing freshwater rivers in Alaska and British Columbia to reach ancestral spawning gravel beds."
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "The Salmon Empire of the Pacific Northwest",
                        "content": {
                            "text": (
                                "• **Location:** Extends from the Aleutian Islands and Alaska down through British Columbia (Canada) to Washington, Oregon, and Northern California.\n\n"
                                "• **Pristine Freshwater Spawning Rivers:** Mountainous coastal watersheds feed thousands of unpolluted, cold, rushing freshwater streams where **Pacific Salmon** migrate upstream to spawn.\n\n"
                                "• **North Pacific Current:** Warms the coastal waters and prevents freezing in Alaskan and Canadian harbours.\n\n"
                                "• **Mountainous Forested Relief:** Rugged coastal mountains make agriculture impossible, channeling regional capital into timber logging and salmon canning.\n\n"
                                "• **Target Species:** Salmon (Sockeye, Pink, Coho, Chinook), halibut, herring, and king crab."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 6,
                "page_title": "Northwest Pacific Grounds (East Asia & Japan)",
                "blocks": [
                    {
                        "block_type": "suggested_diagram",
                        "component_type": "suggested_diagram",
                        "title": "Spatial Map of the Northwest Pacific Ground & Kuroshiwo/Oyashiwo Convergence",
                        "content": {
                            "text": "Regional map of Northeast Asia, showing the meeting of the warm Kuroshiwo and cold Oyashiwo currents, Sea of Okhotsk, Sea of Japan, broad Asian shelf, and major fishing ports."
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "The World's Preeminent Fishing Ground",
                        "content": {
                            "text": (
                                "• **Location:** Stretches along Northeast Asia, encompassing Japan, Eastern Russia (Kamchatka, Sea of Okhotsk), Korea, and the China Sea. **This is the largest and most productive fishing ground on Earth.**\n\n"
                                "• **Current Convergence:** The meeting of the **warm Kuroshiwo (Kuro Siwo) Current** and the **cold Oyashiwo (Oya Siwo) Current** produces the planet's most intense marine upwelling, dense plankton blooms, and ideal water oxygenation.\n\n"
                                "• **Broad Asian Continental Shelf:** Extensive shallow photic zone surrounding the Japanese archipelago and Yellow Sea.\n\n"
                                "• **Indented Coastline:** Thousands of sheltered bays and islands providing breeding habitats and world-class ports (Yokohama, Nagasaki, Hakodate).\n\n"
                                "• **Massive Market & Diet:** Hundreds of millions of consumers in Japan, China, and Korea where fish is a staple daily protein source."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 7,
                "page_title": "Southern Hemisphere & Upwelling Grounds",
                "blocks": [
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Major Southern Upwelling Fisheries",
                        "content": {
                            "text": (
                                "While Northern waters dominate total catch, notable Southern and tropical upwelling zones produce immense harvests:\n\n"
                                "1. **West Coast of South America (Peru & Chile):** Driven by the **cold Peruvian (Humboldt) Current**. Strong offshore winds trigger massive coastal upwelling, sustaining the world's largest single-species harvest of **Anchoveta** (processed into fishmeal).\n\n"
                                "2. **Southwest Africa (Namibia & South Africa):** Washed by the **cold Benguela Current**, generating powerful upwelling along the desert coast for pilchards and hake.\n\n"
                                "3. **Northwest Africa (Mauritania & Morocco):** Washed by the **cold Canary Current**, cooling tropical waters across a broad continental shelf."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 8,
                "page_title": "Four-Way World Fishing Ground Matrix",
                "blocks": [
                    {
                        "block_type": "comparison_table",
                        "component_type": "comparison_table",
                        "title": "Comparative Matrix: The 4 Major World Marine Grounds",
                        "content": {
                            "headers": ["Fishing Ground", "Ocean Basin", "Current Convergence", "Key Species", "Major Physical Advantage"],
                            "rows": [
                                ["Northwest Atlantic", "N. Atlantic", "Gulf Stream (Warm) + Labrador (Cold)", "Cod, Herring, Mackerel, Lobster", "Broad Grand Bank shallows (<180m) and intense nutrient upwelling"],
                                ["Northeast Atlantic", "N. Atlantic", "Warm North Atlantic Drift", "Herring, Cod, Mackerel, Flatfish", "Glaciated Norwegian fiords for spawning & ice-free year-round ports"],
                                ["Northeast Pacific", "N. Pacific", "North Pacific Current (Warm)", "Pacific Salmon, Halibut, Crab", "Clean mountain freshwater rivers for anadromous salmon spawning"],
                                ["Northwest Pacific", "N. Pacific", "Kuroshiwo (Warm) + Oyashiwo (Cold)", "Salmon, Cod, Sardines, Mackerel, Tuna", "World's largest shelf + richest convergence plankton blooms"]
                            ]
                        }
                    }
                ]
            },
            {
                "page_number": 9,
                "page_title": "Geographical Reasoning: Northern vs Southern Asymmetry",
                "blocks": [
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Why Are Global Fisheries Concentrated in the North?",
                        "content": {
                            "text": (
                                "In geographical examinations, students are often asked to explain the global imbalance between Northern and Southern fisheries:\n\n"
                                "1. **Land-to-Water Ratio & Continental Shelves:** The Northern Hemisphere possesses vast continental landmasses with extensive, broad continental shelves. In contrast, Southern Hemisphere coastlines (e.g., East Africa, Western South America) drop off steeply into deep oceanic abysses with narrow shelves.\n\n"
                                "2. **Population & Market Concentration:** Over 85% of the world's population lives in the Northern Hemisphere, providing immense domestic markets with high capital capacity.\n\n"
                                "3. **Industrialization & Fleet Capital:** Developed Northern economies possessed the historical capital to build gigantic factory trawler fleets and electronic detection systems."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 10,
                "page_title": "Worked KCSE Exam Question: Northwest Atlantic",
                "blocks": [
                    {
                        "block_type": "worked_example",
                        "component_type": "worked_example",
                        "title": "Worked KCSE Question: Explaining Northwest Atlantic Dominance",
                        "content": {
                            "question": "Explain three physical factors that have favored the development of commercial fishing in the Northwest Atlantic fishing grounds. [6 marks]",
                            "model_answer": (
                                "1. **Current Convergence:** The convergence of the warm Gulf Stream and the cold Labrador Current causes intense vertical upwelling of organic nutrients from the ocean floor to the photic zone, stimulating dense plankton blooms that support large shoals of fish.\n\n"
                                "2. **Broad Continental Shelf:** The presence of an extensive, shallow continental shelf (such as the Grand Bank) provides vast areas shallower than 180 metres where sunlight penetrates, facilitating rapid phytoplankton photosynthesis.\n\n"
                                "3. **Harsh Adjacent Land Climate & Relief:** The adjacent landmass of Eastern Canada and New England experiences severe winter cold and rugged glaciated soils that make crop farming unprofitable, pushing the population toward marine fishing as a primary livelihood."
                            ),
                            "examiner_commentary": "Full 6/6 marks awarded. Notice that each point clearly identifies the factor, explains the physical oceanographic mechanism, and links it directly to commercial fish abundance or human livelihood push."
                        }
                    }
                ]
            },
            {
                "page_number": 11,
                "page_title": "Interactive World Ground Locator",
                "blocks": [
                    {
                        "block_type": "mini_activity",
                        "component_type": "mini_activity",
                        "title": "Global Ocean Currents & Fisheries Locator",
                        "content": {
                            "activity_type": "ocean_mapping_drill",
                            "instructions": "Pair each major commercial fishing ground with its intersecting ocean currents and dominant commercial species.",
                            "drill_data": [
                                {"ground": "Northwest Atlantic (Grand Bank)", "currents": "Gulf Stream + Labrador Current", "species": "Cod, Herring, Lobster"},
                                {"ground": "Northwest Pacific (Japan / Sea of Okhotsk)", "currents": "Kuroshiwo + Oyashiwo Current", "species": "Salmon, Mackerel, Sardines"},
                                {"ground": "Northeast Atlantic (North Sea / Norway)", "currents": "North Atlantic Drift (Warm)", "species": "Herring, Cod, Flatfish"},
                                {"ground": "West Coast of South America (Peru)", "currents": "Peruvian / Humboldt Current", "species": "Anchoveta (Fishmeal)"}
                            ]
                        }
                    }
                ]
            },
            {
                "page_number": 12,
                "page_title": "Knowledge Checkpoint 1: Atlantic Grounds",
                "blocks": [
                    {
                        "block_type": "knowledge_check",
                        "component_type": "knowledge_check",
                        "title": "Concept Diagnostic: Atlantic Currents & Topography",
                        "content": {
                            "check_type": "multiple_choice",
                            "question": "Which ocean current is responsible for keeping the fishing ports of Western Norway ice-free throughout the severe winter season?",
                            "options": [
                                "The Cold Labrador Current",
                                "The Warm North Atlantic Drift Current",
                                "The Cold Benguela Current",
                                "The Warm Mozambique Current"
                            ],
                            "answer": "B",
                            "explanation": "The Warm North Atlantic Drift (an extension of the Gulf Stream) washes the western coastline of Europe. It raises water temperatures along the Norwegian and British coasts, preventing harbours from freezing over and allowing commercial fishing to operate throughout the year."
                        }
                    }
                ]
            },
            {
                "page_number": 13,
                "page_title": "Knowledge Checkpoint 2: Pacific Grounds",
                "blocks": [
                    {
                        "block_type": "knowledge_check",
                        "component_type": "knowledge_check",
                        "title": "Concept Diagnostic: Northwest Pacific Productivity",
                        "content": {
                            "check_type": "multiple_choice",
                            "question": "What primary physical oceanographic phenomenon makes the Northwest Pacific the most productive marine fishing ground in the world?",
                            "options": [
                                "The complete absence of tides and waves in the Sea of Japan",
                                "The convergence of the warm Kuroshiwo and cold Oyashiwo currents over a broad continental shelf, driving massive nutrient upwelling and plankton blooms",
                                "The discharge of artificial chemical fertilizers by Japanese coastal rivers",
                                "The presence of deep ocean trenches exceeding 8,000 metres that protect fish from surface storms"
                            ],
                            "answer": "B",
                            "explanation": "The convergence of the warm Kuroshiwo (Kuro Siwo) and cold Oyashiwo (Oya Siwo) currents over the broad East Asian continental shelf produces intense vertical upwelling of organic nutrients, optimal cool water temperatures, and high oxygenation, creating the planet's richest plankton haven."
                        }
                    }
                ]
            },
            {
                "page_number": 14,
                "page_title": "World Grounds: Key Takeaways",
                "blocks": [
                    {
                        "block_type": "summary",
                        "component_type": "summary",
                        "title": "Summary: Major World Marine Fishing Grounds",
                        "content": {
                            "key_points": [
                                "Global commercial fisheries are concentrated in the Northern Hemisphere temperate zones due to broad continental shelves, current convergences, and high market demand.",
                                "Northwest Atlantic (Grand Bank): Gulf Stream + Labrador convergence over shallow banks; harsh adjacent winter climate.",
                                "Northeast Atlantic (Western Europe): Glaciated Norwegian fiords for spawning/ports; North Atlantic Drift keeps ports ice-free.",
                                "Northeast Pacific: North Pacific Current; pristine rushing rivers for Pacific Salmon spawning; mountainous logging/fishing economy.",
                                "Northwest Pacific (Japan/East Asia): World's largest fishery driven by Kuroshiwo + Oyashiwo convergence over a broad shelf.",
                                "Southern upwelling zones (Peru, Namibia, Mauritania) are driven by cold Humboldt, Benguela, and Canary currents."
                            ]
                        }
                    }
                ]
            }
        ]
    },

    # -------------------------------------------------------------------------
    # LESSON 5: East African and Kenyan Fisheries (16 Pages)
    # -------------------------------------------------------------------------
    {
        "unit_order": 5,
        "unit_name": "East African and Kenyan Fisheries",
        "lesson_title": "East African and Kenyan Fisheries (Marine, Lake Victoria, and Aquaculture)",
        "pages": [
            {
                "page_number": 1,
                "page_title": "Overview of the East African Fishery Landscape",
                "blocks": [
                    {
                        "block_type": "learning_goal",
                        "component_type": "learning_goal",
                        "title": "Learning Goals: Kenyan Fisheries",
                        "content": {
                            "text": (
                                "By the end of this lesson, you should be able to:\n"
                                "1. Account for the low contribution of marine fishing in Kenya (10%) compared to inland freshwater fisheries (90%).\n"
                                "2. Evaluate the geographical success factors and severe challenges facing Lake Victoria fisheries.\n"
                                "3. Analyze the operations, species, and extension network of fish farming (aquaculture) in Kenya."
                            )
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Kenya's Fishery Paradox: Inland Dominance",
                        "content": {
                            "text": (
                                "In Kenya, fishing is heavily skewed toward inland freshwater bodies. "
                                "Marine fishing along the Indian Ocean coastline contributes only about **10%** of the national catch, while inland freshwater lakes—predominantly **Lake Victoria**—contribute over **90%** of total fish production."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 2,
                "page_title": "Marine Fishing in Kenya: Physical & Economic Bottlenecks",
                "blocks": [
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Why is Kenya's Marine Catch So Low?",
                        "content": {
                            "text": (
                                "1. **Narrow Continental Shelf:** The East African coastline drops off very steeply into deep oceanic waters, leaving a very narrow shelf with limited shallow photic zones (<180m).\n\n"
                                "2. **Warm Tropical Waters:** The Indian Ocean is warm and washed by the **warm Mozambique Current**, which severely restricts plankton proliferation.\n\n"
                                "3. **Coral Reef Obstructions:** Continuous offshore fringing coral reefs tear and destroy commercial drag nets.\n\n"
                                "4. **Simple Artisanal Equipment:** Local coastal communities rely on non-motorized wooden dhows, dugouts, and hand gear incapable of venturing into deep high-seas waters.\n\n"
                                "5. **Foreign Deep-Sea Competition:** Advanced commercial trawlers from Japan, South Korea, and Europe fish in Kenya's deep Exclusive Economic Zone (EEZ), outcompeting local fishermen."
                            )
                        }
                    },
                    {
                        "block_type": "suggested_diagram",
                        "component_type": "suggested_diagram",
                        "title": "Profile of the Kenyan Marine Coastline (Narrow Shelf vs Indian Ocean)",
                        "content": {
                            "text": "Cross-sectional elevation profile of the Kenyan coast, illustrating the narrow continental shelf, steep seabed drop-off, offshore coral reef barrier, and warm Mozambique Current."
                        }
                    }
                ]
            },
            {
                "page_number": 3,
                "page_title": "Freshwater (Inland) Fisheries in Kenya",
                "blocks": [
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Survey of Kenyan Inland Water Fisheries",
                        "content": {
                            "text": (
                                "Inland freshwater bodies are calm, highly productive, and easily navigated with small wooden craft:\n\n"
                                "• **Lake Victoria:** The undisputed powerhouse of Kenyan fishing, producing the overwhelming bulk of tilapia, Nile perch, and omena.\n\n"
                                "• **Rift Valley Freshwater Lakes:** Lake Naivasha (black bass, tilapia) and Lake Baringo (tilapia, mudfish).\n\n"
                                "• **Lake Turkana:** The **only alkaline (salty) lake** in Kenya that supports commercial fishing (Nile perch, tilapia).\n\n"
                                "• **Other Lakes & River Basins:** Lakes Jipe and Chala (Taita Taveta), oxbow lakes along the lower Tana River (Balisa, Shakababo), and Yala Delta lakes (Sare, Kanyaboli)."
                            )
                        }
                    },
                    {
                        "block_type": "suggested_diagram",
                        "component_type": "suggested_diagram",
                        "title": "Spatial Map of Inland Freshwater Fisheries and Hatcheries in Kenya",
                        "content": {
                            "text": "Thematic map of Kenya showing major fishing lakes (Victoria, Naivasha, Baringo, Turkana, Jipe), river systems (Tana, Athi), and government fish hatcheries (Sagana, Kabaru, Kibos, Aruba)."
                        }
                    }
                ]
            },
            {
                "page_number": 4,
                "page_title": "Case Study: Lake Victoria Fisheries Powerhouse",
                "blocks": [
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Lake Victoria: Setting and Dominant Species",
                        "content": {
                            "text": (
                                "Lake Victoria is the second-largest freshwater lake in the world, shared among **Kenya (6%)**, **Uganda (46%)**, and **Tanzania (49%)**.\n\n"
                                "Despite owning only 6% of the lake surface, Kenya maintains an intensely developed fishing sector landing three primary commercial species:\n"
                                "1. **Nile Perch (*Lates niloticus*):** Large predatory fish filleted for lucrative export to European markets.\n"
                                "2. **Tilapia (*Oreochromis niloticus*):** Highly popular table fish sold fresh or fried in domestic urban markets.\n"
                                "3. **Omena / Dagaa (*Rastrineobola argentea*):** Small silvery sardine-like fish harvested at night for human consumption and animal feed protein."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 5,
                "page_title": "Spatial Layout and Landing Beaches of Lake Victoria",
                "blocks": [
                    {
                        "block_type": "suggested_diagram",
                        "component_type": "suggested_diagram",
                        "title": "Lake Victoria Basin, Catchment, and Major Landing Beaches",
                        "content": {
                            "text": "Spatial map of the Kenyan sector of Lake Victoria (Winam Gulf), showing major landing beaches (Kisumu, Mbita, Asembo, Homa Bay), river inlets (Nzoia, Yala, Nyando), and Migingo Island."
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Factors Favoring Fishing on Lake Victoria",
                        "content": {
                            "text": (
                                "• **Shallow Sunlit Waters:** Relatively shallow depths allow sunlight to reach the lake bed, stimulating rich phytoplankton and zooplankton growth.\n\n"
                                "• **Numerous Landing Beaches & Inlets:** Features sheltered bays, beaches, and islands (e.g., Asembo, Mbita, Luanda Kotieno) that serve as safe boat landing and trade centers.\n\n"
                                "• **Dense Surrounding Market:** Densely populated lake basin and adjacent urban centers (Kisumu, Kakamega, Eldoret, Nairobi) maintain massive consumer demand.\n\n"
                                "• **Fish-Eating Dietary Culture:** The local Luo, Luhya, and Abasuba communities have deeply embedded fish-eating traditions.\n\n"
                                "• **Fishermen's Co-operatives:** Co-operative societies assist with landing fee administration, net procurement, and bargaining."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 6,
                "page_title": "Authentic Fishing Operations on Lake Victoria",
                "blocks": [
                    {
                        "block_type": "suggested_image",
                        "component_type": "suggested_image",
                        "title": "Artisanal Wooden Fishing Boats and Operations on Lake Victoria in Kisumu",
                        "content": {
                            "text": "Artisanal wooden fishing boats docked along the shoreline of Lake Victoria in Kisumu with nets and sun-drying frames."
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Operations: From Night Haul to Cold Export",
                        "content": {
                            "text": (
                                "Fishermen depart in motorized or paddle canoes in late afternoon to set gill nets or lantern lines for Omena. "
                                "Catch is landed at dawn at designated Beach Management Units (BMUs). Nile perch is immediately weighed and loaded into refrigerated trucks bound for filleting factories in Kisumu, while Omena is sun-dried on raised grass mats."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 7,
                "page_title": "Environmental & Geopolitical Challenges of Lake Victoria",
                "blocks": [
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Five Critical Challenges Facing Lake Victoria",
                        "content": {
                            "text": (
                                "1. **Overexploitation & Illegal Nets:** Heavy fishing pressure has depleted stocks. Unlicensed fishermen use illegal small-meshed **mosquito nets**, indiscriminately destroying juvenile fingerlings.\n\n"
                                "2. **Nile Perch Predation:** The historical introduction of the predatory Nile perch caused the mass extinction of over 200 native haplochromine fish species.\n\n"
                                "3. **Water Hyacinth (*Eichhornia crassipes*):** This invasive floating weed carpets bays, blocking vessel navigation, choking oxygen exchange, and entangling nets.\n\n"
                                "4. **Boundary Conflicts (Migingo Island):** Disputed jurisdictional boundaries between Kenya and Uganda result in arrests of Kenyan fishermen and confiscation of gear.\n\n"
                                "5. **Exploitative Middlemen & Lack of Cold Storage:** Due to a lack of cold-storage facilities at landing beaches, fishermen are forced to sell fresh fish at throwaway prices to middlemen with insulated trucks."
                            )
                        }
                    },
                    {
                        "block_type": "suggested_diagram",
                        "component_type": "suggested_diagram",
                        "title": "Ecological Food Web Disruption & Invasive Hyacinth in Lake Victoria",
                        "content": {
                            "text": "Ecological food-web diagram showing Nile Perch predation on native Tilapia, agricultural nutrient runoff fueling Water Hyacinth mats, and resultant deoxygenation."
                        }
                    }
                ]
            },
            {
                "page_number": 8,
                "page_title": "Lake Victoria Problems & Remedial Interventions",
                "blocks": [
                    {
                        "block_type": "comparison_table",
                        "component_type": "comparison_table",
                        "title": "Matrix: Lake Victoria Challenges vs Remedial Solutions",
                        "content": {
                            "headers": ["Major Problem", "Ecological / Economic Effect", "Remedial Management Intervention"],
                            "rows": [
                                ["Mosquito Net Usage", "Destruction of juvenile fish and stock collapse", "Strict patrols by Beach Management Units to confiscate illegal mesh"],
                                ["Water Hyacinth Weed", "Blocks navigation and causes fish deoxygenation", "Mechanical harvesting, bio-control beetles (*Neochetina*), and manual removal"],
                                ["Migingo Boundary Disputes", "Harassment and loss of gear for fishermen", "Joint Kenya-Uganda cross-border diplomatic lake patrols and joint licensing"],
                                ["Lack of Cold Storage", "Post-harvest spoilage and exploitation by middlemen", "Establishing solar-powered cold rooms and cooling hubs at landing beaches"],
                                ["Industrial Effluent Pollution", "Toxic chemical dumping and eutrophication", "Enforcing NEMA regulations and effluent pre-treatment by factories"]
                            ]
                        }
                    }
                ]
            },
            {
                "page_number": 9,
                "page_title": "Fish Farming (Aquaculture) in Kenya",
                "blocks": [
                    {
                        "block_type": "definition_card",
                        "component_type": "definition_card",
                        "title": "Aquaculture in Kenya",
                        "content": {
                            "term": "Fish Farming (Aquaculture)",
                            "definition": (
                                "The artificial breeding, rearing, and harvesting of fish in specially constructed earthen ponds, tanks, or floating cages under controlled environmental conditions to supplement natural catches and alleviate pressure on wild fisheries."
                            )
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Pond Construction and Site Selection",
                        "content": {
                            "text": (
                                "Successful fish pond establishment requires specific geographical conditions:\n"
                                "• **Soil Texture:** Soils must have high **clay or loamy content** to ensure an impervious floor that retains water without seeping.\n"
                                "• **Water Supply:** Located near a permanent, unpolluted river or stream to provide continuous fresh water via gravity inlet canals.\n"
                                "• **Gentle Slope:** A mild gradient allows easy drainage through a bottom drainage monk when harvesting."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 10,
                "page_title": "Aquaculture Pond Design & Agronomy",
                "blocks": [
                    {
                        "block_type": "suggested_diagram",
                        "component_type": "suggested_diagram",
                        "title": "Engineering Cross-Section of an Aquaculture Fish Pond and Water Flow",
                        "content": {
                            "text": "Engineering schematic of an earthen fish pond showing water inlet channel, clay lining, monk drainage sluice, surface overflow pipe, and oxygenating aquatic plants."
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Species Reared and Feeding Protocols",
                        "content": {
                            "text": (
                                "• **Tilapia (*Oreochromis niloticus*):** The most popular pond species because it breeds rapidly, resists diseases, and tolerates variable water conditions.\n\n"
                                "• **Trout (*Salmo trutta*):** Reared exclusively in cool, fast-flowing, oxygen-rich mountain streams on the slopes of **Mount Kenya** and the **Aberdares**.\n\n"
                                "• **Mudfish / Catfish (*Clarias gariepinus*):** Reared in warm, muddy ponds; highly resilient to low oxygen.\n\n"
                                "• **Feeding & Aeration:** Fish are fed on agricultural by-products (wheat/rice bran), commercial pellets, and green manure. Aquatic plants are grown in ponds to release oxygen via photosynthesis."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 11,
                "page_title": "Government Fish Hatcheries Network",
                "blocks": [
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Kenya's National Hatcheries and Extension Chain",
                        "content": {
                            "text": (
                                "To support smallholder farmers, the Kenyan government established strategic fish breeding stations that produce certified young fish (**fingerlings**):\n\n"
                                "1. **Sagana Fish Hatchery (Kirinyaga County):** Kenya's primary warm-water research center for breeding improved fast-growing Tilapia and Catfish.\n"
                                "2. **Kabaru Fish Hatchery (Nyeri County):** Cold-water trout breeding station located in the Mount Kenya highlands.\n"
                                "3. **Kibos Fish Hatchery (Kisumu County):** Lake Basin fingerling breeding center.\n"
                                "4. **Aruba Fish Hatchery (Taita Taveta):** Serving coastal and southeastern dryland fish farmers."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 12,
                "page_title": "Economic Value of Kenyan Fisheries",
                "blocks": [
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "National Economic Significance of Fishing",
                        "content": {
                            "text": (
                                "• **Employment Creation:** Directly employs over 100,000 artisanal fishermen, boat builders, net menders, fish mongers, and factory processing workers.\n\n"
                                "• **Foreign Exchange Earnings:** Export of processed Nile perch fillets to European and Asian markets generates vital foreign currency.\n\n"
                                "• **Animal Feed Production:** Omena provides an essential high-protein ingredient for manufacturing livestock and poultry feeds.\n\n"
                                "• **Industrial Raw Materials:** Fish oils are used in cosmetics and pharmaceuticals, and fish skin is tanned into exotic leather."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 13,
                "page_title": "Interactive Kenyan Fishery Decision Simulator",
                "blocks": [
                    {
                        "block_type": "mini_activity",
                        "component_type": "mini_activity",
                        "title": "Kenyan Fishery Management Decision Challenge",
                        "content": {
                            "activity_type": "fisheries_management_simulation",
                            "instructions": "Determine the correct geographical solution for each fishery management dilemma in Kenya.",
                            "scenarios": [
                                {"dilemma": "A smallholder in Kirinyaga wants to dig a fish pond on porous sandy soil near a stream", "action": "Recommend clay lining / compaction or selecting an impermeable clay/loam site", "reason": "Sandy soil allows rapid water seepage, drying out the pond"},
                                {"dilemma": "Lake Victoria fishermen report declining catches and tiny juvenile tilapia in their nets", "action": "Enforce minimum net mesh size regulations and impound illegal mosquito nets", "reason": "Protects juvenile breeding stock from recruitment overfishing"},
                                {"dilemma": "A farmer in Nyeri on Mount Kenya slopes wants to rear cold-water Trout", "action": "Obtain certified fingerlings from Kabaru Hatchery and divert cool, rushing river water", "reason": "Trout require cool, well-oxygenated, fast-flowing mountain water"}
                            ]
                        }
                    }
                ]
            },
            {
                "page_number": 14,
                "page_title": "Knowledge Checkpoint 1: Marine vs Inland Kenya",
                "blocks": [
                    {
                        "block_type": "knowledge_check",
                        "component_type": "knowledge_check",
                        "title": "Concept Diagnostic: Kenyan Marine Limitations",
                        "content": {
                            "check_type": "multiple_choice",
                            "question": "Which combination of physical factors explains why Kenya's marine fishing catch is vastly smaller than its freshwater catch?",
                            "options": [
                                "The presence of a broad, shallow continental shelf combined with freezing polar ocean currents",
                                "A narrow continental shelf, warm Mozambique current that limits plankton, and coral reef net obstructions",
                                "The complete absence of fish species in the Indian Ocean basin",
                                "Dense forests along the coast that block fishermen from accessing the sea"
                            ],
                            "answer": "B",
                            "explanation": "Kenya's marine coastline has an extremely narrow continental shelf that drops off steeply into deep water, is washed by the warm Mozambique current which discourages plankton growth, and features offshore coral reefs that damage commercial nets. These physical constraints severely limit marine harvest compared to highly productive inland lakes."
                        }
                    }
                ]
            },
            {
                "page_number": 15,
                "page_title": "Knowledge Checkpoint 2: Lake Victoria & Aquaculture",
                "blocks": [
                    {
                        "block_type": "knowledge_check",
                        "component_type": "knowledge_check",
                        "title": "Concept Diagnostic: Soil Selection for Fish Ponds",
                        "content": {
                            "check_type": "multiple_choice",
                            "question": "Why must commercial fish ponds in Kenya be constructed in areas with heavy clay or loamy soils?",
                            "options": [
                                "Clay soil provides essential minerals that fish directly eat as food",
                                "Clay soil is highly impervious, preventing water from seeping away and maintaining stable pond water levels",
                                "Clay soil attracts wild birds that feed the fingerlings",
                                "Sandy soils are too difficult for excavating with hand tools"
                            ],
                            "answer": "B",
                            "explanation": "Pond aquaculture requires water to be held securely without continuous loss. Clay and clay-loam soils consist of fine, compact particles that swell when wet, creating an impermeable barrier that stops downward water infiltration and maintains stable water depths."
                        }
                    }
                ]
            },
            {
                "page_number": 16,
                "page_title": "Kenyan Fisheries: Key Takeaways",
                "blocks": [
                    {
                        "block_type": "summary",
                        "component_type": "summary",
                        "title": "Summary: East African and Kenyan Fisheries",
                        "content": {
                            "key_points": [
                                "In Kenya, inland freshwater fisheries account for 90% of total catch, while marine fishing accounts for only 10%.",
                                "Marine bottlenecks: narrow continental shelf, warm Mozambique current, coral reef obstructions, simple craft, and foreign trawler competition.",
                                "Lake Victoria is the freshwater powerhouse, producing Nile perch (export), Tilapia (table), and Omena (diet & feed).",
                                "Lake Victoria faces overfishing, illegal mosquito nets, water hyacinth weed, Migingo boundary disputes, and exploitative middlemen.",
                                "Aquaculture relies on impervious clay ponds, permanent river water, and fingerlings from government hatcheries (Sagana, Kabaru, Kibos, Aruba)."
                            ]
                        }
                    }
                ]
            }
        ]
    },

    # -------------------------------------------------------------------------
    # LESSON 6: Comparative Analysis (Kenya vs Japan) and Fisheries Management (16 Pages)
    # -------------------------------------------------------------------------
    {
        "unit_order": 6,
        "unit_name": "Comparative Analysis (Kenya vs Japan) and Fisheries Management",
        "lesson_title": "Comparative Analysis (Kenya vs Japan) and Fisheries Management",
        "pages": [
            {
                "page_number": 1,
                "page_title": "Introduction to Comparative Geographies",
                "blocks": [
                    {
                        "block_type": "learning_goal",
                        "component_type": "learning_goal",
                        "title": "Learning Goals: Comparative Analysis & Conservation",
                        "content": {
                            "text": (
                                "By the end of this lesson, you should be able to:\n"
                                "1. Perform a rigorous, exam-standard comparative analysis of the fishing industries in Kenya and Japan across eight distinct criteria.\n"
                                "2. Differentiate between fisheries **management** (planning/research) and fisheries **conservation** (protection/restrictions).\n"
                                "3. Evaluate the seven core conservation strategies applied in Kenya and East Africa.\n"
                                "4. Master model answers for full-length KCSE structured essay questions."
                            )
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Contrasting Fishery Economies",
                        "content": {
                            "text": (
                                "Japan is the foremost commercial fishing nation in the world, producing approximately one-sixth of the global marine catch. "
                                "Comparing Japan's highly industrialized marine superpower sector with Kenya's developing, inland-focused industry reveals critical geographical insights into how oceanography, relief, technology, and culture shape national development."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 2,
                "page_title": "Japan's Industrial Fishing Dominance",
                "blocks": [
                    {
                        "block_type": "suggested_image",
                        "component_type": "suggested_image",
                        "title": "Commercial Tuna Auction and Processing at Tsukiji Fish Market in Japan",
                        "content": {
                            "text": "High-value commercial Bluefin Tuna lined up for wholesale auction and computerized processing at a major Japanese seafood terminal."
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Key Features of the Japanese Fishing Sector",
                        "content": {
                            "text": (
                                "• **Deep-Sea Global Reach:** Japanese fleets operate across international waters in the Pacific, Atlantic, and Indian Oceans.\n\n"
                                "• **Cutting-Edge Technology:** Computer-controlled factory trawlers, satellite shoal detection, sonar, radar, and robotic fish processing.\n\n"
                                "• **Cultural Staple:** Fish is the primary dietary protein across all Japanese social classes, ensuring immense domestic demand.\n\n"
                                "• **Advanced Co-operatives:** Japanese fisheries co-operatives provide substantial capital financing, modern vessel insurance, and direct port marketing."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 3,
                "page_title": "Eight-Point Comparative Matrix: Kenya vs Japan",
                "blocks": [
                    {
                        "block_type": "comparison_table",
                        "component_type": "comparison_table",
                        "title": "Comprehensive Eight-Point Comparative Matrix: Kenya vs Japan",
                        "content": {
                            "headers": ["Comparison Criteria", "🇰🇪 Kenya Fishing Industry", "🇯🇵 Japan Fishing Industry"],
                            "rows": [
                                ["Primary Location", "Dominated by inland freshwater lakes (Lake Victoria produces >90% of total catch).", "Dominated by deep-sea marine fishing in the Northwest Pacific and international waters."],
                                ["Distance from Shore", "Restricted to shallow inshore lake waters and coastal fringes a few kilometres out.", "Deep-sea long-range fleets operating thousands of kilometres out across open oceans."],
                                ["Shelf & Current Conditions", "Narrow continental shelf with warm Mozambique current that restricts plankton growth.", "Broad continental shelf with converging Kuroshiwo (warm) and Oyashiwo (cold) currents causing rich upwelling."],
                                ["Market Demand & Diet", "Lower domestic market; fish consumption is mostly restricted to specific cultural communities.", "Extremely high nationwide market demand; fish is an ancient, universal staple daily diet."],
                                ["Species Harvested", "Freshwater species: Tilapia, Nile perch, Omena, and Mudfish.", "Marine species: Cod, Salmon, Mackerel, Alaska pollock, Sardines, and Tuna."],
                                ["Marketing Systems", "Mostly sold by individual artisanal fishermen to private middlemen at landing beaches.", "Dominated by highly organized national co-operatives offering advanced credit and direct auctions."],
                                ["Foreign Competition", "Local coastal fishermen face severe competition from foreign deep-sea trawlers in their EEZ.", "Highly self-sufficient; national fleet dominates territorial and international fishing grounds."],
                                ["Technological Level", "Low to medium technology; relies on wooden canoes, simple dhows, and manual nets.", "World-leading technology; computerized factory trawlers, sonar, radar, and satellite fish tracking."]
                            ]
                        }
                    }
                ]
            },
            {
                "page_number": 4,
                "page_title": "Visual Contrast: Kenya vs Japan Settings",
                "blocks": [
                    {
                        "block_type": "suggested_diagram",
                        "component_type": "suggested_diagram",
                        "title": "Kenya vs Japan Fishing Technology and Oceanographic Setting Contrast",
                        "content": {
                            "text": "Side-by-side comparative cross-section contrasting Kenya's inland freshwater lake setting and artisanal canoes with Japan's ocean current convergence and high-seas factory trawlers."
                        }
                    }
                ]
            },
            {
                "page_number": 5,
                "page_title": "Worked KCSE Comparative Essay Breakdown",
                "blocks": [
                    {
                        "block_type": "worked_example",
                        "component_type": "worked_example",
                        "title": "Model Comparative Essay: Accounting for Japan's Dominance",
                        "content": {
                            "question": "Account for the highly developed nature of the marine fishing industry in Japan compared to Kenya. [6 marks]",
                            "model_answer": (
                                "1. **Ocean Currents:** Japan enjoys the convergence of the warm Kuroshiwo and cold Oyashiwo currents, which creates intense vertical upwelling and rich plankton blooms; **whereas** Kenya's marine waters are washed by the warm Mozambique current, which discourages plankton growth.\n\n"
                                "2. **Continental Shelf:** Japan possesses an extensive, broad continental shelf with shallow photic waters ideal for fish breeding; **unlike** Kenya, where the marine continental shelf is very narrow and drops steeply into deep ocean water.\n\n"
                                "3. **Topography (Relief):** In Japan, over 80% of the terrain is rugged and mountainous, making crop farming impossible and pushing the population toward marine fishing; **on the other hand**, Kenya has rich arable highlands that support agriculture, reducing the historical push toward ocean exploitation.\n\n"
                                "4. **Technology:** Japan uses advanced automated refrigerated factory ships and electronic sonar fish finders; **while** Kenya relies largely on small, non-motorized wooden craft with simple hand nets."
                            ),
                            "examiner_commentary": "Full 6/6 marks awarded. Notice the mandatory use of comparative connectives (whereas, unlike, on the other hand, while) and the balanced point-by-point presentation for both nations."
                        }
                    }
                ]
            },
            {
                "page_number": 6,
                "page_title": "Fisheries Management: Scientific Planning & Control",
                "blocks": [
                    {
                        "block_type": "definition_card",
                        "component_type": "definition_card",
                        "title": "Defining Fisheries Management",
                        "content": {
                            "term": "Fisheries Management",
                            "definition": (
                                "The scientific planning, monitoring, and administration of aquatic resources and habitats to ensure maximum sustainable economic and nutritional harvest without degrading the biological productivity of the aquatic ecosystem."
                            )
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Three Core Management Measures",
                        "content": {
                            "text": (
                                "1. **Scientific Research Stations:** Establishing institutes like KMFRI (Kenya Marine and Fisheries Research Institute) and hatcheries (Sagana, Kabaru) to breed fast-growing fingerlings, monitor water quality, and track fish migration patterns.\n\n"
                                "2. **Public Environmental Education:** Training farmers to avoid cultivating steep riverbanks to prevent soil erosion and siltation of breeding grounds. Educating factory managers on treating toxic effluents before discharging into rivers and lakes.\n\n"
                                "3. **River & Lake Monitoring:** Regular government surveillance to prevent illegal river diversion or unauthorized damming, which causes severe water level drops in spawning areas."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 7,
                "page_title": "Fisheries Conservation: Protecting Species",
                "blocks": [
                    {
                        "block_type": "definition_card",
                        "component_type": "definition_card",
                        "title": "Defining Fisheries Conservation",
                        "content": {
                            "term": "Fisheries Conservation",
                            "definition": (
                                "The active preservation, protection, and legal regulation of fish species and aquatic habitats to prevent overexploitation, extinction, and the irreversible destruction of marine and freshwater food webs."
                            )
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Differentiating Management from Conservation",
                        "content": {
                            "text": (
                                "In geographical examinations, always maintain this distinction:\n\n"
                                "• **Management** is proactive planning, research, infrastructure development, and education to maximize sustainable yield.\n\n"
                                "• **Conservation** is legal restriction, protection, quotas, closed seasons, and gear regulation to prevent stock collapse."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 8,
                "page_title": "The Seven Conservation Strategies in Kenya",
                "blocks": [
                    {
                        "block_type": "suggested_diagram",
                        "component_type": "suggested_diagram",
                        "title": "The Seven Core Strategies for Sustainable Fisheries Conservation",
                        "content": {
                            "text": "Flowchart diagram illustrating the 7 strategic conservation pillars: net mesh regulation, closed seasons, licensing quotas, lake restocking, aquaculture promotion, infrastructure, and naval patrols."
                        }
                    },
                    {
                        "block_type": "step_process",
                        "component_type": "step_process",
                        "title": "Seven Core Conservation Interventions",
                        "content": {
                            "steps": [
                                {"step_number": 1, "title": "Banning Small-Meshed Nets", "description": "Outlawing small mosquito nets to allow young juvenile fish to escape, mature, and breed."},
                                {"step_number": 2, "title": "Enforcing Closed Breeding Seasons", "description": "Declaring temporary bans on fishing during peak spawning periods to protect breeding fish."},
                                {"step_number": 3, "title": "Licensing & Catch Quotas", "description": "Issuing licenses to registered fishermen and establishing Total Allowable Catch limits."},
                                {"step_number": 4, "title": "Artificial Restocking of Lakes", "description": "Releasing millions of hatchery-bred fingerlings into overexploited natural water bodies."},
                                {"step_number": 5, "title": "Promoting Aquaculture (Fish Ponds)", "description": "Encouraging inland fish farming to satisfy market demand and reduce pressure on wild lakes."},
                                {"step_number": 6, "title": "Infrastructure Upgrading", "description": "Tarmacking remote access roads (e.g., Kitale–Kalokol) to disperse fishing pressure across multiple fisheries."},
                                {"step_number": 7, "title": "Marine Naval Patrols", "description": "Conducting continuous coast guard patrols to prevent illegal foreign trawler poaching in Kenya's EEZ."}
                            ]
                        }
                    }
                ]
            },
            {
                "page_number": 9,
                "page_title": "Case Study: The Kitale–Kalokol Highway",
                "blocks": [
                    {
                        "block_type": "callout",
                        "component_type": "callout",
                        "title": "Strategic Infrastructure: Kitale–Kalokol Road",
                        "content": {
                            "callout_type": "important",
                            "text": "The construction of the all-weather tarmac road connecting Kitale to Kalokol on the western shores of Lake Turkana is a premier example of conservation infrastructure. By enabling fresh fish from underutilized Lake Turkana to reach major urban markets quickly, it directly relieves intense overexploitation on Lake Victoria."
                        }
                    }
                ]
            },
            {
                "page_number": 10,
                "page_title": "Common Exam Mistakes in Comparative Questions",
                "blocks": [
                    {
                        "block_type": "common_mistake",
                        "component_type": "common_mistake",
                        "title": "Exam Trap: One-Sided Comparative Answers",
                        "content": {
                            "mistake": "Writing: 'Japan uses advanced automated ships and sonar detection equipment' without mentioning Kenya.",
                            "correction": "Always write balanced statements linking both nations: 'Japan utilizes advanced automated refrigerated ships and sonar detection, whereas Kenya relies mostly on non-motorized wooden canoes with manual gear.'",
                            "exam_tip": "In KCSE Section B comparative questions, an unlinked isolated statement about one country earns ZERO marks. Both sides must be explicitly compared."
                        }
                    }
                ]
            },
            {
                "page_number": 11,
                "page_title": "KCSE Structured Practice Questions (Part 1)",
                "blocks": [
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "KCSE Structured Questions & Revision Guide",
                        "content": {
                            "text": (
                                "### Practice Question 1 (Short Answer)\n"
                                "1. (a) Define the term **fishery**. [2 marks]\n"
                                "   *Model Answer:* A fishery is a specific geographical water body or area where aquatic resources (such as fish, crabs, and molluscs) are exploited.\n\n"
                                "2. (b) Name the only **alkaline lake** in Kenya that supports a commercial fishing industry. [1 mark]\n"
                                "   *Model Answer:* Lake Turkana.\n\n"
                                "3. (c) State three modern commercial methods of fishing. [3 marks]\n"
                                "   *Model Answer:* (i) Purse Seining, (ii) Bottom Trawling, (iii) Long Lining."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 12,
                "page_title": "KCSE Structured Practice Questions (Part 2 — Essay)",
                "blocks": [
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "KCSE Full-Length Essay Model Answers",
                        "content": {
                            "text": (
                                "### Practice Question 2 (Structured Essay — 12 Marks)\n"
                                "(a) Explain four problems experienced by fish farmers in Kenya. [8 marks]\n"
                                "1. **High Pond Construction Cost:** Digging and lining clay ponds and buying inlet pipes requires high initial capital that smallholders lack.\n"
                                "2. **Inadequate Fingerling Supply:** Certified government hatcheries are few and distant, leading to high transport costs and fingerling mortality.\n"
                                "3. **Predator Infestation:** Birds (kingfishers, pelicans), snakes, and monitor lizards prey heavily on pond fish.\n"
                                "4. **Lack of Technical Extension:** Inadequate fisheries extension officers to advise farmers on water aeration, feed rations, and disease control.\n\n"
                                "(b) State four measures the government of Kenya has taken to conserve its fisheries. [4 marks]\n"
                                "• Banning the use of small-meshed mosquito nets.\n"
                                "• Enacting closed breeding seasons during spawning periods.\n"
                                "• Licensing fishermen and enforcing catch quotas.\n"
                                "• Restocking depleted natural lakes with hatchery-bred fingerlings."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 13,
                "page_title": "Interactive Comparative Reasoning Challenge",
                "blocks": [
                    {
                        "block_type": "mini_activity",
                        "component_type": "mini_activity",
                        "title": "KCSE Comparative Sentence Construction Challenge",
                        "content": {
                            "activity_type": "comparative_synthesis",
                            "instructions": "Pair the appropriate contrast coordinating conjunctions to form valid KCSE comparative statements.",
                            "examples": [
                                {"criterion": "Market Demand", "statement": "In Japan, fish is an ancient, universally consumed daily dietary staple across the entire nation; whereas in Kenya, fish consumption is largely restricted to communities living around the lake basin and coast."},
                                {"criterion": "Technology", "statement": "Japan operates computerized factory trawlers equipped with satellite fish tracking and blast freezers; while Kenya relies primarily on artisanal wooden dhows and manual gill nets."},
                                {"criterion": "Shelf Setting", "statement": "Japan's waters are characterized by a wide continental shelf and the convergence of the Kuroshiwo and Oyashiwo currents; unlike Kenya, which features a narrow shelf washed by the warm Mozambique current."}
                            ]
                        }
                    }
                ]
            },
            {
                "page_number": 14,
                "page_title": "Knowledge Checkpoint 1: Kenya vs Japan Comparison",
                "blocks": [
                    {
                        "block_type": "knowledge_check",
                        "component_type": "knowledge_check",
                        "title": "Concept Diagnostic: Comparative Geographies",
                        "content": {
                            "check_type": "multiple_choice",
                            "question": "Which of the following is a fundamental SIMILARITY between the fishing industries of Kenya and Japan?",
                            "options": [
                                "Both countries derive over 90% of their total fish catch from inland freshwater lakes",
                                "Both countries practice fish farming (aquaculture) and face challenges related to aquatic pollution and resource overexploitation",
                                "Both countries operate gigantic high-seas refrigerated factory fleets across the Arctic Ocean",
                                "Both countries have an identical domestic per-capita fish consumption rate"
                            ],
                            "answer": "B",
                            "explanation": "While their scales and technologies differ, Kenya and Japan share fundamental similarities: both practice aquaculture (fish farming) to supplement natural catches, both face serious water pollution challenges (agricultural runoff in Kenya, industrial effluents/heavy metals in Japan), and both confront overexploitation of coastal resources."
                        }
                    }
                ]
            },
            {
                "page_number": 15,
                "page_title": "Knowledge Checkpoint 2: Management and Conservation",
                "blocks": [
                    {
                        "block_type": "knowledge_check",
                        "component_type": "knowledge_check",
                        "title": "Concept Diagnostic: Fisheries Conservation Measures",
                        "content": {
                            "check_type": "multiple_choice",
                            "question": "Why is the enforcement of a temporary 'Closed Season' considered a highly effective fisheries conservation strategy?",
                            "options": [
                                "It allows fishermen to repair roads and construct new fish processing factories",
                                "It halts fishing during peak spawning periods, allowing mature fish to lay eggs and replenish stock without human disruption",
                                "It completely eliminates all natural predators such as Nile perch and water birds",
                                "It cools ocean water temperatures to stimulate plankton multiplication"
                            ],
                            "answer": "B",
                            "explanation": "A closed season temporarily outlaws fishing activities during the specific biological window when fish migrate to shallow spawning grounds to breed and lay eggs. By protecting breeding adults and newly hatched fingerlings during this critical phase, the aquatic population can naturally replenish."
                        }
                    }
                ]
            },
            {
                "page_number": 16,
                "page_title": "Topic 2 Mastery Synthesis & Final Review",
                "blocks": [
                    {
                        "block_type": "summary",
                        "component_type": "summary",
                        "title": "Topic 2 Mastery Checklist: Fishing",
                        "content": {
                            "key_points": [
                                "Physical Factors: Broad continental shelf (<180m photic zone), indented fiord coastlines, mountainous adjacent relief (push factor), cool temperate waters (10-15°C), and current convergences (nutrient upwelling).",
                                "Types & Traditional Gear: Pelagic vs Demersal vs Inshore vs Freshwater. Traditional gear includes basket traps, harpoons, barriers, herbs, night lamps (Omena), and gill nets.",
                                "Modern Commercial Gear: Purse Seining (surface shoals), Bottom Trawling (deep seabed sweep with otter boards), Long Lining (100km baited lines), and Factory Ships.",
                                "World Fishing Grounds: Northwest Atlantic (Grand Bank / Gulf Stream + Labrador), Northeast Atlantic (North Sea / Norway fiords), Northeast Pacific (Salmon), Northwest Pacific (Japan / Kuroshiwo + Oyashiwo).",
                                "Kenya Fisheries: 90% inland freshwater (Lake Victoria, Naivasha, Turkana) vs 10% marine. Lake Victoria challenges include mosquito nets, Nile perch predation, water hyacinth, and boundary disputes.",
                                "Aquaculture: Impervious clay ponds, permanent stream water, and fingerlings from Sagana, Kabaru, Kibos, and Aruba hatcheries.",
                                "Kenya vs Japan: Deep-sea marine superpower with high technology and massive domestic market vs developing inland freshwater fishery with artisanal craft.",
                                "Conservation: Banning mosquito nets, closed breeding seasons, licensing quotas, lake restocking, aquaculture, and naval EEZ patrols."
                            ]
                        }
                    }
                ]
            }
        ]
    }
]


# =============================================================================
# INGESTION EXECUTION PIPELINE
# =============================================================================

def ingest_form4_geography_topic2(replace=False):
    print("=" * 80)
    print("VLearn Form 4 Geography — Topic 2: Fishing")
    print("High-Structure Production Ingestion Engine")
    print("=" * 80)

    # 1. Resolve Hierarchy
    curriculum = Curriculum.objects.filter(name="844").first()
    if not curriculum:
        raise ValueError("Curriculum 844 not found!")

    grade = Grade.objects.filter(curriculum=curriculum, name="Form 4").first()
    if not grade:
        raise ValueError("Grade Form 4 not found!")

    subject = Subject.objects.filter(grade=grade, name="Geography").first()
    if not subject:
        raise ValueError("Subject Geography not found under Form 4!")

    print(f"[*] Resolved Target: {curriculum.name} -> {grade.name} -> {subject.name} (ID: {subject.id})")

    # 2. Get or Create Topic 2
    topic, created = Topic.objects.get_or_create(
        subject=subject,
        order=2,
        defaults={
            "name": "Fishing",
            "description": "Comprehensive analysis of global and East African fisheries, physical and human factors, traditional and modern methods, world fishing grounds, Kenyan inland and marine fisheries, comparative analysis with Japan, and sustainable conservation."
        }
    )
    if not created and replace:
        topic.name = "Fishing"
        topic.description = "Comprehensive analysis of global and East African fisheries, physical and human factors, traditional and modern methods, world fishing grounds, Kenyan inland and marine fisheries, comparative analysis with Japan, and sustainable conservation."
        topic.save()
        print(f"[*] Updating existing Topic: {topic.name} (ID: {topic.id})")
    else:
        print(f"[+] Topic: {topic.name} (ID: {topic.id})")

    total_lessons = 0
    total_pages = 0
    total_blocks = 0

    # 3. Ingest Lessons Transactionally
    with transaction.atomic():
        for l_cfg in LESSONS_CONFIG:
            u_order = l_cfg["unit_order"]
            u_name = l_cfg["unit_name"]
            l_title = l_cfg["lesson_title"]
            pages_data = l_cfg["pages"]

            # Get or create LearningUnit
            unit, _ = LearningUnit.objects.get_or_create(
                topic=topic,
                order=u_order,
                defaults={"name": u_name, "description": f"Learning Unit {u_order}: {u_name}"}
            )
            unit.name = u_name
            unit.save()

            # Get or create Lesson
            lesson, l_created = Lesson.objects.get_or_create(
                topic=topic,
                learning_unit=unit,
                defaults={
                    "title": l_title,
                    "status": "published",
                    "version": 1
                }
            )
            lesson.title = l_title
            lesson.status = "published"
            lesson.version = 1
            lesson.save()

            if not l_created and replace:
                cleared_count = lesson.blocks.count()
                lesson.blocks.all().delete()
                print(f"  [*] Found Existing Lesson: {lesson.title} (ID: {lesson.id})")
                print(f"      [!] Cleared {cleared_count} existing blocks for clean rebuild.")
            else:
                print(f"  [+] Created Lesson: {lesson.title} (ID: {lesson.id})")

            # Ingest Blocks Page by Page
            b_order = 1
            lesson_page_count = len(pages_data)
            total_pages += lesson_page_count
            total_lessons += 1

            for page in pages_data:
                p_num = page["page_number"]
                p_title = clean_text(page["page_title"])
                blocks = page["blocks"]

                for blk in blocks:
                    b_type = blk["block_type"]
                    c_type = blk.get("component_type", b_type)
                    b_title = clean_text(blk.get("title", p_title))
                    b_content = clean_block_content(blk.get("content", {}))

                    LessonBlock.objects.create(
                        lesson=lesson,
                        page_number=p_num,
                        page_title=p_title,
                        title=b_title,
                        block_type=b_type,
                        component_type=c_type,
                        component_order=b_order,
                        order=b_order,
                        content=b_content,
                        metadata={}
                    )
                    b_order += 1
                    total_blocks += 1

            print(f"      [OK] Ingested {lesson_page_count} Pages for Lesson {u_order}.")

    print("=" * 80)
    print("[SUCCESS] Form 4 Geography Topic 2 Ingestion Complete!")
    print(f"[*] Total Lessons Ingested: {total_lessons}")
    print(f"[*] Total Pages Ingested:   {total_pages}")
    print(f"[*] Total Blocks Ingested:  {total_blocks}")
    print("=" * 80)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Ingest Form 4 Geography Topic 2: Fishing")
    parser.add_argument("--replace", action="store_true", help="Replace existing lesson blocks")
    args = parser.parse_args()
    ingest_form4_geography_topic2(replace=args.replace)
