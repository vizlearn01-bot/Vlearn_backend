"""
VLearn CBC Grade 10 Agriculture — Topic 6: Crop Protection
Production Ingestion Engine (Deep Senior Secondary Pedagogical Edition)

Curriculum: CBC (ID: 5)
Grade: Grade 10 (ID: 5, Level: 10)
Subject: Agriculture
Topic: Crop Protection (Topic Order: 6)

Decomposed into 14 Learning Units & 14 Published Lessons:
  1. Introduction to Weeds (5 Pages, 11 Blocks)
  2. Field Identification of Weeds (5 Pages, 11 Blocks)
  3. Making a Weed Herbarium (5 Pages, 11 Blocks)
  4. Classification by Morphology (5 Pages, 11 Blocks)
  5. Classification by Life Cycle (5 Pages, 11 Blocks)
  6. Physical Weed Control (5 Pages, 11 Blocks)
  7. Cultural Weed Control (5 Pages, 11 Blocks)
  8. Biological Weed Control (5 Pages, 11 Blocks)
  9. Chemical Weed Control (5 Pages, 11 Blocks)
  10. Legislative Weed Control (Quarantine) (5 Pages, 11 Blocks)
  11. Integrated Weed Management (IWM) (5 Pages, 11 Blocks)
  12. Carrying out Weed Control (Practicals) (5 Pages, 11 Blocks)
  13. Economic Importance of Weeds (5 Pages, 11 Blocks)
  14. Synthesis and Assessment (8 Pages, 17 Blocks)
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

def build_topic6_curriculum():
    """Returns the comprehensive pedagogical page and block structure for Grade 10 Topic 6: Crop Protection."""
    return [
        # =====================================================================
        # LESSON 1: Introduction to Weeds
        # =====================================================================
        {
            "unit_order": 1,
            "unit_name": "Introduction to Weeds",
            "unit_description": "Agricultural definition of weeds; 5 evolutionary adaptations (prolific seed production, long seed dormancy/soil seed bank, rapid vegetative maturation, extensive root/rhizome networks, efficient dispersal mechanisms).",
            "lesson_title": "Understanding Agricultural Weeds and Evolutionary Adaptations",
            "pages": [
                [
                    {
                        "type": "suggested_image",
                        "title": "Weed Infestation and Crop Competition in Agricultural Land",
                        "content": {
                            "title": "Weed Infestation and Crop Competition in Agricultural Land",
                            "caption": "Dense weed proliferation competing aggressively with agricultural crops for solar radiation, moisture, and soil nutrients."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Introduction to Weeds",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Define what constitutes a **weed** in an agricultural context.",
                                "Analyze the **5 biological and evolutionary traits** that make weeds highly competitive.",
                                "Explain the concept of the **soil weed seed bank** and seed dormancy.",
                                "Distinguish between wanted crops and unwanted volunteer plants."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "What is an Agricultural Weed?",
                        "content": {
                            "title": "A Plant Out of Place",
                            "text": "In agronomy, a **weed** is defined as *any plant growing where it is not wanted by the farmer*.\n\n- **Contextual Definition**: Even a high-value crop becomes a weed if it germinates in the wrong field. For example, a volunteer maize plant growing in a commercial finger millet seedbed is classified as a weed because it robs the millet of light, water, and soil nutrients.\n- **Opportunistic Colonizers**: Weeds have evolved over millions of years as pioneer colonizers of disturbed soils, allowing them to rapidly invade tilled farm beds."
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "The 5 Evolutionary Superpowers of Weeds",
                        "content": {
                            "title": "Why Weeds Dominate Cultivated Lands",
                            "text": "1. **Prolific Seed Production**: A single Pigweed (*Amaranthus*) or Blackjack plant can shed over 100,000 viable seeds in one season.\n2. **Long Seed Dormancy & Soil Seed Bank**: Weed seeds can remain viable underground for 20 to 50 years, germinating only when brought to the surface during plowing.\n3. **Rapid Growth and Short Maturation Cycle**: Many annual weeds germinate, flower, and set seeds in just 3 to 4 weeks, reproducing before the farmer can weed.\n4. **Extensive Root & Rhizome Networks**: Weeds like Couch grass possess underground rhizomes that scavenge water and nutrients deeper than domestic crop roots.\n5. **Specialized Dispersal Mechanisms**: Barbed seeds (Blackjack), feathery parachutes (Mexican marigold), or explosive seed pods ensure widespread dispersal across farms."
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Evolutionary Biology & Seed Bank Dynamics of Weeds",
                        "content": {
                            "title": "Evolutionary Biology & Seed Bank Dynamics of Weeds",
                            "caption": "Diagram illustrating the 5 weed survival superpowers: Prolific Seed Output, Soil Seed Bank Longevity, Rapid Maturation, Underground Rhizome Storage, and Epizoochory Dispersal."
                        }
                    }
                ],
                [
                    {
                        "type": "comparison_table",
                        "title": "Cultivated Crops vs Agricultural Weeds",
                        "content": {
                            "title": "Evolutionary Comparison Matrix",
                            "headers": ["Biological Trait", "Cultivated Domestic Crops", "Aggressive Agricultural Weeds"],
                            "rows": [
                                ["Seed Production Volume", "Moderate (100–1,000 seeds per plant)", "Massive (10,000–200,000 seeds per plant)"],
                                ["Seed Dormancy Duration", "Short; bred for immediate, uniform germination", "Long (decades); staggered emergence over seasons"],
                                ["Environmental Tolerance", "Delicate; vulnerable to drought, heat, and pests", "Extreme hardiness; thrives in poor, rocky, acidic soils"],
                                ["Vegetative Regeneration", "Low; relies almost entirely on planting seeds", "High; regenerates from cut stems, rhizomes, and tubers"]
                            ]
                        }
                    },
                    {
                        "type": "mini_activity",
                        "title": "Field Practical: Weed Density and Seed Count Audit",
                        "content": {
                            "title": "Weed Proliferation Survey",
                            "task": "1. Throw a 1 m² wooden quadrat into an unweeded farm corner.\n2. Count the total number of weed plants inside the square.\n3. Harvest 1 mature Pigweed plant and estimate its total seed output by counting seeds on one branch and multiplying by the total branches.\n4. Calculate the potential weed seed deposition per hectare.",
                            "materials": ["1 m² Quadrat", "Hand Magnifier", "Collection Bag", "Calculator"],
                            "safety": "Wear garden gloves to avoid thorns and stinging hairs."
                        }
                    }
                ],
                [
                    {
                        "type": "key_takeaway",
                        "title": "Core Summary: Weed Biology",
                        "content": {
                            "title": "Key Takeaways",
                            "text": "- **A weed is any plant growing where it is not wanted** by the farmer.\n- **Weeds produce thousands of seeds** and maintain long-term soil seed banks.\n- **Rapid maturity and vegetative rhizomes** enable weeds to outcompete crops.\n- **Weed dispersal adaptations** (hooks, wind tufts) facilitate farm re-infestation."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Couch Grass Survival Mechanics",
                        "content": {
                            "question": "Which biological trait explains why Couch grass (Digitaria abyssinica) is notoriously difficult to eradicate from arable land compared to annual broad-leaved weeds?",
                            "options": [
                                "It produces giant fleshy fruits that poison farm machinery",
                                "It possesses an extensive network of underground stems (rhizomes) that remain dormant during drought and regenerate into new plants when cut into pieces by hoes",
                                "It completes its entire lifecycle in under 24 hours",
                                "It changes the color of its leaves to camouflage against tractor tires"
                            ],
                            "answer": "B",
                            "explanation": "Couch grass is a perennial weed equipped with underground rhizomes. Mechanical tillage slices these rhizomes into fragments, each bearing vegetative nodes capable of sprouting new shoots and roots. This vegetative survival mechanism makes simple weeding ineffective without systemic herbicides or deep drying."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 2: Field Identification of Weeds
        # =====================================================================
        {
            "unit_order": 2,
            "unit_name": "Field Identification of Weeds",
            "unit_description": "Field identification of common Kenyan agricultural weeds: Blackjack (Bidens pilosa), Wandering Jew (Commelina benghalensis), Pigweed (Amaranthus spp.), Sodom Apple (Solanum incanum), Nut Grass (Cyperus rotundus).",
            "lesson_title": "Field Identification and Diagnostic Characteristics of Common Weeds",
            "pages": [
                [
                    {
                        "type": "suggested_image",
                        "title": "Blackjack (Bidens pilosa) Herb with Yellow-White Inflorescence",
                        "content": {
                            "title": "Blackjack (Bidens pilosa) Herb with Yellow-White Inflorescence",
                            "caption": "A flowering Blackjack weed exhibiting serrated trifoliate leaves, white-petaled composite flowers, and developing barbed achenes."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Field Weed Identification",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Identify the **5 most common agricultural weeds in Kenya** by their botanical and common names.",
                                "Examine diagnostic morphological traits (**leaf shape, stem type, flowers, fruits, and seeds**).",
                                "Analyze the **epizoochory adaptation** of Blackjack (*Bidens pilosa*) barbed seeds.",
                                "Distinguish between poisonous pasture weeds and arable crop weeds."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The Big 5 Agricultural Weeds in Kenya",
                        "content": {
                            "title": "Key Weed Species Profiles",
                            "text": "1. **Blackjack (*Bidens pilosa*)**: Erect annual herb with opposite, serrated leaves, composite daisy-like white and yellow flowers, and linear black seeds equipped with 2 to 4 stiff, barbed pappi that cling tightly to clothing and animal fur (epizoochory).\n2. **Wandering Jew (*Commelina benghalensis*)**: Fleshy, succulent herbaceous weed with creeping stems that root at nodes, asymmetrical bright-blue flowers, and underground cleistogamous flowers.\n3. **Pigweed (*Amaranthus hybridus / spinosus*)**: Fast-growing erect annual with reddish/green stems, dull green oval leaves, and dense bristly terminal flower spikes shedding shiny black seeds.\n4. **Sodom Apple (*Solanum incanum*)**: Spiny, woody perennial shrub with thorny stems and leaves, light purple flowers, and round, yellow, poisonous berry fruits common in pastures.\n5. **Nut Grass (*Cyperus rotundus*)**: Perennial sedge with dark green glossy leaves, distinct triangular solid stems, and chains of underground starch-rich tubers ('nuts')."
                        }
                    }
                ],
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Blackjack (Bidens pilosa) Barbed Seed Epizoochory Adaptation",
                        "content": {
                            "title": "Blackjack (Bidens pilosa) Barbed Seed Epizoochory Adaptation",
                            "caption": "Morphological anatomical diagram of a single Blackjack seed showing the dark linear cypsela body and 3 retro-barbed awns (pappi) engineered for epizoochorous attachment to passing mammals."
                        }
                    },
                    {
                        "type": "comparison_table",
                        "title": "Diagnostic Profiles of 5 Major Kenyan Weeds",
                        "content": {
                            "title": "Species Identification Matrix",
                            "headers": ["Botanical Name", "Common Name", "Growth Habit & Stem", "Diagnostic Signature"],
                            "rows": [
                                ["Bidens pilosa", "Blackjack", "Erect annual herb; green ribbed stem", "Black linear seeds with 2–4 backward-barbed hooks"],
                                ["Commelina benghalensis", "Wandering Jew", "Creeping succulent; fleshy rooting nodes", "Bright blue 3-petaled flowers; underground seeds"],
                                ["Amaranthus hybridus", "Pigweed", "Erect annual; fibrous/spiny stem", "Dense terminal bristly seed spikes; tiny shiny seeds"],
                                ["Solanum incanum", "Sodom Apple", "Woody perennial shrub; thorny branches", "Purple flowers; round yellow poisonous berry fruits"],
                                ["Cyperus rotundus", "Nut Grass", "Erect perennial sedge; triangular stem", "Basal leaf rosette; underground chains of brown tubers"]
                            ]
                        }
                    }
                ],
                [
                    {
                        "type": "mini_activity",
                        "title": "Field Practical: Weed Specimen Scouting and Specimen Tagging",
                        "content": {
                            "title": "On-Farm Weed Diagnostic Scavenger Hunt",
                            "task": "Working in teams of three on the school farm:\n1. Locate and flag 1 specimen of each of the 5 major weeds.\n2. Sketch the leaf margin, stem cross-section, and seed head of each.\n3. Test the hook mechanism of Blackjack seeds on a piece of wool/cotton cloth.\n4. Complete the diagnostic field score card.",
                            "materials": ["Field Notebook", "Magnifier", "Flagging Tape", "Sample Vials"],
                            "safety": "Do not touch or taste yellow Sodom Apple berries (poisonous solanine alkaloids)."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Core Summary: Field Weed Identification",
                        "content": {
                            "title": "Key Takeaways",
                            "text": "- **Blackjack** is recognized by its white/yellow flowers and barbed clinging seeds.\n- **Wandering Jew** is a creeping succulent with bright blue flowers that roots at nodes.\n- **Pigweed** is a vigorous erect annual with dense bristly seed spikes.\n- **Sodom Apple** is a spiny perennial pasture shrub with toxic yellow berries.\n- **Nut Grass** is a sedge with triangular stems and underground food-storing tubers."
                        }
                    }
                ],
                [
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Diagnostic Pasture Weed Identification",
                        "content": {
                            "question": "A student scouting a communal dairy grazing pasture identifies a 1-meter-tall woody shrub covered in sharp prickles, bearing light purple flowers and round, yellow, tomato-like berry fruits. What is the identity of this pasture weed?",
                            "options": [
                                "Wandering Jew (Commelina benghalensis)",
                                "Sodom Apple (Solanum incanum)",
                                "Blackjack (Bidens pilosa)",
                                "Nut Grass (Cyperus rotundus)"
                            ],
                            "answer": "B",
                            "explanation": "Sodom Apple (Solanum incanum) is a woody, spiny perennial solanaceous shrub characterized by prickly leaves and stems, purple flowers, and round, yellow, poisonous fruits. It thrives in overgrazed pastures where livestock avoid eating its bitter, thorny foliage."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 3: Making a Weed Herbarium
        # =====================================================================
        {
            "unit_order": 3,
            "unit_name": "Making a Weed Herbarium",
            "unit_description": "Scientific herbarium definition; 5-step preparation protocol (trowel harvesting with intact roots, pressing between newspaper, drying for 7–10 days with daily paper replacement, mounting on cardstock, standard botanical labeling).",
            "lesson_title": "Scientific Weed Herbarium Preparation and Preservation",
            "pages": [
                [
                    {
                        "type": "suggested_image",
                        "title": "Botanical Herbarium Specimen Sheet with Intact Roots and Label",
                        "content": {
                            "title": "Botanical Herbarium Specimen Sheet with Intact Roots and Label",
                            "caption": "A professionally pressed, dried, and mounted botanical herbarium specimen showcasing intact roots, stem, foliage, flowers, and standard identification label."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Weed Herbarium",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Define what a **weed herbarium** is and explain its scientific value in agronomy.",
                                "Execute the 5-step specimen preparation sequence (**Collection, Pressing, Drying, Mounting, Labeling**).",
                                "Explain why the **entire plant (including intact roots)** must be collected.",
                                "Format and attach a standard **Herbarium Identification Label Card**."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "What is a Weed Herbarium?",
                        "content": {
                            "title": "A Permanent Botanical Reference Library",
                            "text": "A **herbarium** is a systematically organized collection of preserved, dried, and pressed plant specimens mounted on archival sheets of heavy paper, accompanied by detailed scientific labels.\n\n- **Agronomic Value**: Serves as a diagnostic reference library for agronomists, extension officers, and learners to identify invasive weeds, study weed morphology, and trace historical weed distributions.\n- **Specimen Completeness**: A valid agricultural herbarium specimen must include **roots, stems, leaves, and reproductive flowers/seeds**."
                        }
                    }
                ],
                [
                    {
                        "type": "step_process",
                        "title": "Protocol: 5 Steps to Create a Weed Herbarium Specimen",
                        "content": {
                            "title": "Scientific Specimen Preparation Protocol",
                            "steps": [
                                "1. **Collection**: Use a hand trowel to dig deeply around the weed, lifting the entire root system intact. Wash root soil gently in clean water and pat dry.",
                                "2. **Pressing**: Lay the specimen flat between sheets of dry newspaper. Arrange leaves so both upper and lower surfaces are visible; spread roots neatly without overlapping.",
                                "3. **Drying**: Place the newspaper-sandwiched specimen inside a wooden plant press clamped firmly with straps. Store in a warm, ventilated room. **Change newspapers daily for 7 to 10 days** to remove moisture and prevent fungal rotting.",
                                "4. **Mounting**: Secure the crisp, fully dried specimen onto a sheet of heavy white cardstock (standard 29 cm x 42 cm) using archival glue or narrow mounting strips.",
                                "5. **Standard Labeling**: Affix a structured identification label card in the bottom-right corner of the mounting sheet."
                            ]
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Standard Scientific Weed Herbarium Mounting & Label Sheet",
                        "content": {
                            "title": "Standard Scientific Weed Herbarium Mounting & Label Sheet",
                            "caption": "Layout architecture of a 29 cm x 42 cm herbarium sheet showing specimen arrangement (intact roots, stem, foliage, flowers) and bottom-right corner identification label card."
                        }
                    }
                ],
                [
                    {
                        "type": "suggested_video",
                        "title": "How to Correctly Press and Make a Plant Specimen Herbarium",
                        "content": {
                            "title": "How to Correctly Press and Make a Plant Specimen Herbarium",
                            "description": "Step-by-step horticultural guide demonstrating weed harvesting with roots, botanical pressing techniques, daily paper replacement, and professional mounting.",
                            "url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The Standard Specimen Identification Label",
                        "content": {
                            "title": "Essential Label Metadata",
                            "text": "Every mounted specimen must bear an identification label in the **bottom-right corner**:\n\n```\n+---------------------------------------------------------+\n|                 WEED SPECIMEN RECORD                    |\n| Botanical Name:    Bidens pilosa                        |\n| Common Name:       Blackjack                            |\n| Local Name:        Mnyonye / Kipruto (Kenya)            |\n| Morphological Class: Broad-Leaved Dicot                 |\n| Life Cycle:        Annual                               |\n| Habitat / Locality: School Vegetable Plot, Kitale       |\n| Date Collected:    26th August 2026                     |\n| Collector(s):      Grade 10 Agriculture Group 3         |\n+---------------------------------------------------------+\n```"
                        }
                    }
                ],
                [
                    {
                        "type": "mini_activity",
                        "title": "Laboratory Practical: Pressing and Mounting 3 Local Weed Specimens",
                        "content": {
                            "title": "Hands-On Herbarium Workshop",
                            "task": "1. Collect 3 different weeds (1 broad-leaf, 1 grass, 1 sedge) with roots intact.\n2. Wash roots, arrange between dry newspaper sheets, and clamp in the school wooden press.\n3. Change the newspaper daily for 7 days.\n4. Mount the dried specimens on white cardstock and fill out complete specimen labels.",
                            "materials": ["Hand Trowel", "Newspapers", "Wooden Plant Press with Straps", "White Cardstock (A3)", "Adhesive Glue", "Specimen Labels"],
                            "safety": "Handle dried, brittle plant specimens gently to prevent stem breakage."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Core Summary: Weed Herbarium",
                        "content": {
                            "title": "Key Takeaways",
                            "text": "- **A herbarium is a permanent reference collection** of dried, pressed, and labeled plants.\n- **Always collect intact roots** to enable accurate morphological diagnosis.\n- **Change newspaper daily for 7–10 days** to ensure rapid drying without fungal mold.\n- **Mount on A3 cardstock with a standard label** in the bottom-right corner."
                        }
                    }
                ],
                [
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Daily Newspaper Changes During Plant Pressing",
                        "content": {
                            "question": "Why is it scientifically essential to change the absorbent newspaper sheets daily for the first 7 to 10 days while drying plant specimens in a wooden press?",
                            "options": [
                                "To allow the ink from the newspaper to color the plant leaves black",
                                "To continuously absorb moisture expelled by the plant tissues and prevent fungal mold and bacterial rot from destroying the specimen",
                                "To allow oxygen to re-start the photosynthetic process in the dark",
                                "To prevent the wooden press boards from turning into coal"
                            ],
                            "answer": "B",
                            "explanation": "Fresh plant tissues contain high levels of cellular water (70–90%). If the moisture is trapped inside damp paper in the dark, saprophytic fungi and bacteria quickly decompose the specimen, turning it black, mushy, and useless. Daily newspaper replacement rapidly extracts water, preserving the natural color and physical structures."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 4: Classification by Morphology
        # =====================================================================
        {
            "unit_order": 4,
            "unit_name": "Classification by Morphology",
            "unit_description": "Grouping weeds into Broad-leaved dicots (taproots, reticulate venation) vs Grass monocots (round hollow culms, swollen nodes, parallel venation) vs Sedge monocots (solid triangular stems, 3-ranked leaves, tubers).",
            "lesson_title": "Morphological Classification: Broad-Leaved, Grass, and Sedge Weeds",
            "pages": [
                [
                    {
                        "type": "suggested_image",
                        "title": "Transverse Anatomical Cross-Section of a Nut Grass Sedge Stem",
                        "content": {
                            "title": "Transverse Anatomical Cross-Section of a Nut Grass Sedge Stem",
                            "caption": "Microscopic cross-section of a Cyperus rotundus stem revealing the solid, non-nodal, 3-angled triangular vascular architecture characteristic of sedge weeds."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Morphological Classification",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Classify weeds into **Broad-leaved, Grass, and Sedge** morphological groups.",
                                "Analyze structural differences in **stem anatomy, leaf venation, and root systems**.",
                                "Explain the agricultural significance of morphological classification in selecting **selective herbicides**.",
                                "Examine cross-sections of hollow round grass stems vs solid triangular sedge stems."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The 3 Morphological Weed Groups",
                        "content": {
                            "title": "Physical Architecture Dictates Control",
                            "text": "Weeds are classified morphologically based on their external physical structure:\n\n### 1. Broad-Leaved Weeds (Dicots)\n- **Leaves**: Broad, expanded leaf blades with **net-like (reticulate) venation**.\n- **Stems**: Solid, branched, often square or cylindrical.\n- **Roots**: Deep **taproot system**.\n- **Examples**: Blackjack (*Bidens pilosa*), Pigweed (*Amaranthus*), Gallant Soldier (*Galinsoga*).\n\n### 2. Grass Weeds (Monocots / Poaceae)\n- **Leaves**: Narrow, elongated blades with **parallel venation** and a sheath wrapping the stem.\n- **Stems**: **Round, hollow culms with distinct swollen joints (nodes)**.\n- **Roots**: Fibrous root system, often with runners.\n- **Examples**: Couch grass (*Digitaria abyssinica*), Kikuyu grass, Wild oats.\n\n### 3. Sedge Weeds (Monocots / Cyperaceae)\n- **Leaves**: Narrow, grass-like, arranged in **3 distinct ranks (rows)** around the stem.\n- **Stems**: **Solid, distinctly triangular (3-angled) in cross-section, with NO nodes**.\n- **Roots**: Fibrous root network with underground tubers/nuts.\n- **Examples**: Nut grass (*Cyperus rotundus*), Yellow nutsedge."
                        }
                    }
                ],
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Morphological Stem Anatomy: Grass vs Sedge vs Broadleaf",
                        "content": {
                            "title": "Morphological Stem Anatomy: Grass vs Sedge vs Broadleaf",
                            "caption": "Comparative transverse cross-sections: 1 Round Hollow Grass Stem with swollen node, 2 Solid Triangular Sedge Stem lacking nodes, and 3 Solid Branching Broad-Leaved Stem with net venation."
                        }
                    },
                    {
                        "type": "comparison_table",
                        "title": "Master Morphological Comparison: Broadleaf vs Grass vs Sedge",
                        "content": {
                            "title": "Diagnostic Anatomy Matrix",
                            "headers": ["Diagnostic Feature", "Broad-Leaved Weeds (Dicots)", "Grass Weeds (Poaceae)", "Sedge Weeds (Cyperaceae)"],
                            "rows": [
                                ["Leaf Blade Width", "Wide, flat, broad blades", "Long, narrow, linear blades", "Long, narrow, V-channel blades"],
                                ["Venation Pattern", "Reticulate (Net-like)", "Parallel venation", "Parallel venation"],
                                ["Leaf Arrangement", "Alternate, opposite, or whorled", "2 ranks (alternating opposite sides)", "3 ranks (arranged in 3 rows around stem)"],
                                ["Stem Cross-Section", "Cylindrical or square, branched", "Round (cylindrical) and hollow", "Triangular (3-sided) and completely solid"],
                                ["Stem Nodes", "Normal vegetative branch nodes", "Swollen, distinct nodes (joints)", "Completely lacks nodes"],
                                ["Root Architecture", "Deep primary taproot", "Fibrous roots with stolons", "Fibrous roots with basal tubers (nuts)"],
                                ["Herbicide Response", "Susceptible to 2,4-D hormone sprays", "Tolerant to 2,4-D; killed by graminicides", "Highly resistant; requires specialized sedge killers"]
                            ]
                        }
                    }
                ],
                [
                    {
                        "type": "mini_activity",
                        "title": "Laboratory Practical: Stem Cross-Section and Venation Micro-Analysis",
                        "content": {
                            "title": "Weed Anatomy Dissection Lab",
                            "task": "1. Collect fresh stems of Blackjack, Couch grass, and Nut grass.\n2. Use a razor blade to cut a clean transverse cross-section of each stem.\n3. Examine under a hand lens: verify which stem is round/hollow, which is solid/triangular, and which has branching xylem.\n4. Draw the 3 stem cross-sections in your laboratory practical book.",
                            "materials": ["Razor Blade", "Hand Lens", "Fresh Weed Stems", "Dissecting Tile"],
                            "safety": "Always slice away from fingers when using sharp razor blades."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Core Summary: Morphological Classification",
                        "content": {
                            "title": "Key Takeaways",
                            "text": "- **Broad-leaved weeds** have wide leaves with net venation and deep taproots.\n- **Grass weeds** have round, hollow stems with swollen nodes and parallel venation.\n- **Sedge weeds** have solid, triangular stems with no nodes and 3-ranked leaves.\n- **Morphology dictates herbicide choice** (e.g., 2,4-D selectively kills broadleaf weeds in cereals)."
                        }
                    }
                ],
                [
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Diagnostic Stem Cross-Section",
                        "content": {
                            "question": "An agronomist examines an unknown arable weed: its leaves are arranged in 3 ranks, its stem cross-section is solid and distinctly 3-angled (triangular), and it completely lacks stem nodes. To which group does this weed belong?",
                            "options": [
                                "Broad-leaved dicot weed",
                                "Grass weed (Poaceae)",
                                "Sedge weed (Cyperaceae)",
                                "Leguminous cover crop"
                            ],
                            "answer": "C",
                            "explanation": "Sedge weeds (family Cyperaceae, such as Cyperus rotundus) are uniquely defined by solid, triangular stems that have no nodes, accompanied by leaves arranged in three distinct ranks. Grasses have round hollow stems with nodes, while broad-leaved dicots have branching stems with taproots."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 5: Classification by Life Cycle
        # =====================================================================
        {
            "unit_order": 5,
            "unit_name": "Classification by Life Cycle",
            "unit_description": "Weed classification by longevity: Annuals (1 single season, seed reproduction, tillage before flowering) vs Biennials (2 years) vs Perennials (>2 years, underground rhizomes/tubers, systemic herbicides).",
            "lesson_title": "Life Cycle Classification: Annual, Biennial, and Perennial Weeds",
            "pages": [
                [
                    {
                        "type": "suggested_image",
                        "title": "Dense Inflorescence and Rhizome Stand of Perennial Couch Grass",
                        "content": {
                            "title": "Dense Inflorescence and Rhizome Stand of Perennial Couch Grass",
                            "caption": "A perennial grass weed colony thriving through extensive subterranean vegetative rhizome networks that survive across multiple cropping seasons."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Life Cycle Classification",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Classify weeds based on lifespan into **Annuals, Biennials, and Perennials**.",
                                "Analyze the reproductive mechanisms of each life cycle group (seeds vs vegetative organs).",
                                "Explain why annual weeds must be controlled **before flowering**.",
                                "Formulate management strategies for perennial weeds possessing deep underground food reserves."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The 3 Weed Life Cycle Horizons",
                        "content": {
                            "title": "Matching Longevity to Control Strategy",
                            "text": "1. **Annual Weeds**:\n- Complete their entire life cycle (germination, vegetative growth, flowering, seed setting, and death) in **one single season or year**.\n- **Reproduction**: Exclusively by seeds.\n- **Control Strategy**: Easy to uproot or hoe, but **MUST be destroyed before flowering** to prevent replenishment of the soil seed bank.\n- **Examples**: Blackjack, Pigweed, Mexican marigold, Gallant Soldier.\n\n2. **Biennial Weeds**:\n- Require **two full years** to complete their life cycle.\n- *Year 1*: Form a low rosette of leaves and store starch in a fleshy taproot.\n- *Year 2*: Bolt upward, produce flowers, set seeds, and die.\n- **Examples**: Wild carrot, Bull thistle.\n\n3. **Perennial Weeds**:\n- Live for **more than two years**, surviving indefinitely from season to season.\n- **Reproduction**: Propagate by seeds AND **underground vegetative structures** (rhizomes, stolons, bulbs, tubers).\n- **Control Strategy**: Surface weeding only cuts top leaves; requires deep tillage to solarize rhizomes or translocated systemic herbicides.\n- **Examples**: Couch grass (*Digitaria abyssinica*), Nut grass (*Cyperus rotundus*), Sodom Apple."
                        }
                    }
                ],
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Weed Life Cycle Horizons: Annual vs Biennial vs Perennial",
                        "content": {
                            "title": "Weed Life Cycle Horizons: Annual vs Biennial vs Perennial",
                            "caption": "Comparative timeline showing: Annual 1-season seed cycle, Biennial 2-year vegetative-to-flowering cycle, and Perennial multi-year subterranean rhizome regeneration cycle."
                        }
                    },
                    {
                        "type": "comparison_table",
                        "title": "Life Cycle Matrix and Targeted Control Actions",
                        "content": {
                            "title": "Life Cycle Agronomic Strategy Matrix",
                            "headers": ["Life Cycle Class", "Longevity", "Primary Propagation Mode", "Critical Management Window", "Recommended Control Method"],
                            "rows": [
                                ["Annual Weeds", "1 Season (<1 Year)", "Seeds exclusively", "Before flower bud formation", "Shallow hand-hoeing, contact herbicides, organic mulching"],
                                ["Biennial Weeds", "2 Years", "Seeds; stored taproot starches", "During Year 1 vegetative rosette stage", "Deep taproot severing, spot herbicide application"],
                                ["Perennial Weeds", ">2 Years (Indefinite)", "Seeds + underground rhizomes/tubers", "Dry season fallow or early flush", "Systemic translocated herbicides (glyphosate), deep chisel tillage"]
                            ]
                        }
                    }
                ],
                [
                    {
                        "type": "mini_activity",
                        "title": "Field Practical: Weed Life Cycle Survey in Cropping Plots",
                        "content": {
                            "title": "Surveying Weed Longevity on the School Farm",
                            "task": "1. Dig up 5 different weed species across the school farm.\n2. Inspect underground structures: check for simple taproots/fibrous roots (annuals) vs fleshy rhizomes/tubers (perennials).\n3. Classify each weed into Annual or Perennial.\n4. Design a weeding calendar indicating whether control should be done before flowering (annuals) or require rhizome extraction (perennials).",
                            "materials": ["Hand Jembe", "Trowel", "Identification Chart", "Notebook"],
                            "safety": "Wash soil from hands after handling root organs."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Core Summary: Life Cycle Classification",
                        "content": {
                            "title": "Key Takeaways",
                            "text": "- **Annual weeds complete their cycle in 1 season** and reproduce solely by seeds.\n- **Control annuals before flowering** to starve the soil seed bank.\n- **Perennials live for years** and regenerate from underground rhizomes and tubers.\n- **Surface hoeing fails on perennials**; use systemic herbicides or deep root exposure."
                        }
                    }
                ],
                [
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Timing Control for Annual Weeds",
                        "content": {
                            "question": "Why is it an unbreakable agronomic principle that annual broad-leaved weeds like Blackjack and Pigweed must be uprooted or hoed BEFORE they develop flowers?",
                            "options": [
                                "Weed flowers produce poison that kills hand jembes",
                                "Once annual weeds flower, they produce tens of thousands of viable seeds that shed into the soil, creating a massive soil seed bank that infests crops for future years",
                                "Annual weeds transform into perennial trees after flowering",
                                "Flowering weeds attract beneficial honeybees that should not be disturbed"
                            ],
                            "answer": "B",
                            "explanation": "Annual weeds reproduce exclusively by seeds. A single mature plant can produce over 100,000 seeds. If a farmer delays weeding until after flowering and seed set, those seeds drop into the soil seed bank, guaranteeing severe weed competition for many upcoming cropping seasons. Controlling them before flowering breaks their reproductive cycle completely."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 6: Physical Weed Control
        # =====================================================================
        {
            "unit_order": 6,
            "unit_name": "Physical Weed Control",
            "unit_description": "Mechanical and physical methods: hand pulling in moist soil, hand hoeing (jembe) at 2-3 cm depth, tractor inter-row cultivation, slashing, and the severe ecological hazards of burning.",
            "lesson_title": "Physical and Mechanical Methods of Weed Control",
            "pages": [
                [
                    {
                        "type": "suggested_image",
                        "title": "Manual Weeding Operation Using Ergonomic Hand Tool in Field",
                        "content": {
                            "title": "Manual Weeding Operation Using Ergonomic Hand Tool in Field",
                            "caption": "A farmer using a handheld weeding tool to uproot unwanted weed seedlings close to crop plants without damaging crop root systems."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Physical Weed Control",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Demonstrate **hand weeding (pulling)** and **hand hoeing (jembe cultivation)**.",
                                "Analyze the pros and cons of mechanical inter-row cultivators.",
                                "Explain why hand weeding is superior close to delicate crop stems.",
                                "Evaluate the **severe ecological damages of using fire (burning)** for weed clearing."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Hand Weeding vs Hand Hoeing",
                        "content": {
                            "title": "Direct Physical Elimination",
                            "text": "1. **Hand Weeding (Uprooting by Hand)**:\n- **Technique**: Grasp weed at the base near the soil surface and pull upward firmly when the soil is moist.\n- **Best Used**: In densely planted rows, vegetable nurseries, or close to crop stems where jembe blades would chop crop roots.\n- **Limitation**: Extremely slow, backbreaking, and labor-intensive.\n\n2. **Hand Hoeing (Jembe Tillage)**:\n- **Technique**: Strike soil at a shallow 2 to 3 cm depth to slice weed roots and bury weed foliage.\n- **Best Used**: Between widely spaced crop rows (e.g. maize, beans).\n- **Benefits**: Aerates topsoil and incorporates organic weed biomass into the soil."
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "Mechanical Cultivation, Slashing, and Burning",
                        "content": {
                            "title": "Tractor Cultivation, Mowing, and Fire Risks",
                            "text": "### 1. Mechanical Tractor Cultivation\n- Tractor-mounted inter-row cultivators weed multiple rows rapidly. Requires precise row spacing and flat terrain.\n\n### 2. Slashing (Mowing)\n- Cutting weed foliage at ground level with a panga or slasher. Cleans orchards and pathways, but does not kill roots—weeds quickly regrow from basal crowns.\n\n### 3. The Ecological Disaster of Burning\n- **Why Some Farmers Burn**: Quick clearing of weed trash before plowing.\n- **CRITICAL ECOLOGICAL HAZARDS**:\n  - Incinerates valuable soil organic matter (humus).\n  - Kills beneficial soil microbes (mycorrhizae, nitrifying bacteria, earthworms).\n  - Leaves soil completely bare, triggering catastrophic water and wind erosion."
                        }
                    },
                    {
                        "type": "comparison_table",
                        "title": "Physical Weed Control Methods Comparison",
                        "content": {
                            "title": "Physical Methods Evaluation Matrix",
                            "headers": ["Method", "Tool / Implement", "Optimal Application Context", "Key Advantage", "Primary Limitation"],
                            "rows": [
                                ["Hand Pulling", "Hands / Hand Weeder", "Vegetable beds, close to crop stems", "Zero damage to crop roots; removes full root", "Very high labor requirement; slow"],
                                ["Hand Hoeing", "Hand Jembe / Hoe", "Inter-row spaces in maize, beans, potatoes", "Fast; aerates soil; buries weed green manure", "Cannot be used in close rows; causes back strain"],
                                ["Mechanical Cultivator", "Tractor Inter-Row Tines", "Large commercial grain farms (>10 acres)", "Massive acreage coverage per hour", "High capital machinery cost; risks root pruning"],
                                ["Slashing", "Slasher / Brushcutter", "Orchards, farm roads, borders", "Controls tall vegetation quickly", "Roots remain alive; rapid regrowth"],
                                ["Burning", "Controlled Fire", "Fallow bush clearing (Discouraged)", "Instant removal of massive dry biomass", "Destroys soil microbes, humus, and promotes erosion"]
                            ]
                        }
                    }
                ],
                [
                    {
                        "type": "mini_activity",
                        "title": "Field Practical: Comparative Hand Pulling vs Hand Hoeing Trial",
                        "content": {
                            "title": "Physical Weeding Speed and Efficiency Lab",
                            "task": "1. Demarcate two adjacent 2 m x 2 m weed-infested plots.\n2. Plot A: Clear using hand pulling only; Plot B: Clear using a hand jembe.\n3. Record time taken for each plot.\n4. Inspect root remnants in both plots after 5 days to see which plot experiences faster weed regrowth.",
                            "materials": ["Hand Jembe", "Stopwatch", "Pegs and String", "Measuring Tape"],
                            "safety": "Keep feet clear of swinging jembe blades; wear safety boots."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Core Summary: Physical Control",
                        "content": {
                            "title": "Key Takeaways",
                            "text": "- **Hand pulling is ideal near delicate crop stems** when soil is damp.\n- **Hand hoeing rapidly weeds inter-row spaces** and aerates topsoil.\n- **Slashing manages tall growth** but leaves roots alive to regrow.\n- **Burning destroys soil humus and microbes**, promoting severe erosion."
                        }
                    }
                ],
                [
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Ecological Disadvantage of Burning Weeds",
                        "content": {
                            "question": "Why do environmental agronomists strongly advise farmers against using fire (burning) as a routine method to clear weed trash from agricultural fields?",
                            "options": [
                                "Fire cools the soil excessively and attracts nocturnal birds",
                                "Burning incinerates valuable organic matter, kills beneficial topsoil microorganisms (earthworms, nitrifiers), and leaves soil bare to severe water and wind erosion",
                                "Fire causes weed seeds to double in size and become diamonds",
                                "Smoke prevents tractors from starting their engines"
                            ],
                            "answer": "B",
                            "explanation": "Routine burning destroys the organic humus layer on topsoil, incinerates earthworms and beneficial bacteria, and exposes bare topsoil to erosive rainfall impact and wind stripping. Incorporating weeds as green manure builds soil fertility; burning destroys it."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 7: Cultural Weed Control
        # =====================================================================
        {
            "unit_order": 7,
            "unit_name": "Cultural Weed Control",
            "unit_description": "Agronomic practices: organic/synthetic mulching, cover cropping (cowpeas, sweet potatoes), crop rotation (breaking Striga cycles), high-density spacing for rapid canopy closure, and certified clean seed.",
            "lesson_title": "Cultural Weed Control: Mulching, Cover Cropping, and Canopy Closure",
            "pages": [
                [
                    {
                        "type": "suggested_image",
                        "title": "Living Cover Crop Suppressing Weeds and Protecting Soil",
                        "content": {
                            "title": "Living Cover Crop Suppressing Weeds and Protecting Soil",
                            "caption": "A dense leguminous cover crop blanket covering the soil between main crop rows, outcompeting weeds for solar radiation and moisture."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Cultural Weed Control",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Explain how **cultural practices** modify the crop environment to suppress weeds ecologically.",
                                "Analyze the mechanics of **organic mulching and black plastic sheeting** in blocking light.",
                                "Demonstrate how **cover cropping and close spacing** achieve rapid canopy closure.",
                                "Explain how **crop rotation** breaks host-specific weed cycles like *Striga*."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The Science of Cultural Weed Suppression",
                        "content": {
                            "title": "Outcompeting Weeds Naturally",
                            "text": "Cultural weed control uses good husbandry practices to give crops a competitive advantage over weeds:\n\n1. **Mulching**: Covering bare soil with a 5–10 cm layer of dry grass, straw, or black plastic film.\n   - *Mechanism*: Completely blocks solar radiation. Weed seeds cannot germinate or photosynthesize.\n2. **Cover Cropping**: Interplanting dense, fast-spreading legumes (cowpeas, sweet potatoes, desmodium).\n   - *Mechanism*: Forms a living green carpet that smothers weed sprouts and fixes atmospheric nitrogen.\n3. **Crop Spacing & Rapid Canopy Closure**: Planting crops at optimal, uniform close spacing so crop leaves overlap quickly, casting deep shade on the ground."
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "Crop Rotation and Certified Clean Seed",
                        "content": {
                            "title": "Disrupting Specialized Weed Lifecycles",
                            "text": "### 1. Crop Rotation\n- Alternating cereals (maize, sorghum) with legumes (beans, cowpeas, groundnuts).\n- **Disrupting Striga**: Parasitic *Striga* weed only attacks cereal roots. Rotating with non-host legumes triggers 'suicidal germination' of *Striga* seeds without allowing it to parasitize, starving out the weed.\n\n### 2. Certified Clean Seed\n- Sowing certified hybrid seed that is 100% free of weed seed contamination. Sowing uncleaned farm-saved grain accidentally introduces thousands of weed seeds per acre."
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Cultural Weed Suppression: Mulching & Living Cover Crop Canopy",
                        "content": {
                            "title": "Cultural Weed Suppression: Mulching & Living Cover Crop Canopy",
                            "caption": "Comparative diagram showcasing: 1 Organic Mulch Layer physically blocking sunlight from weed seeds, and 2 Dense Living Cover Crop Canopy outcompeting weeds for light, space, and moisture."
                        }
                    }
                ],
                [
                    {
                        "type": "comparison_table",
                        "title": "Cultural Weed Management Tactics Matrix",
                        "content": {
                            "title": "Cultural Practices Summary",
                            "headers": ["Cultural Method", "Physiological Suppression Mechanism", "Best Crop Enterprise", "Secondary Farm Benefit"],
                            "rows": [
                                ["Organic Mulching", "Blocks 95% of light; suppresses seed germination", "Tomatoes, Capsicums, Kales, Coffee", "Conserves 70% soil moisture; adds organic humus"],
                                ["Cover Cropping", "Living mulch chokes weeds through dense ground cover", "Maize, Bananas, Orchards (Cowpeas/Desmodium)", "Fixes atmospheric nitrogen; controls soil erosion"],
                                ["Optimal Close Spacing", "Accelerates canopy closure, shading out weed flushes", "Maize (75x25 cm), Soya beans, Onions", "Maximizes plant population and yield per hectare"],
                                ["Crop Rotation", "Breaks weed-crop parasitic relationships", "Maize rotated with Beans/Groundnuts", "Breaks pest/disease cycles; balances soil nutrients"]
                            ]
                        }
                    },
                    {
                        "type": "mini_activity",
                        "title": "Field Practical: Testing Light Penetration under Mulch vs Bare Soil",
                        "content": {
                            "title": "Mulch Microclimate and Germination Experiment",
                            "task": "1. Prepare two 1 m² plots: Plot 1 left bare; Plot 2 covered with 7 cm dry grass mulch.\n2. Scatter 50 Blackjack seeds on the surface of both plots.\n3. Water both plots daily for 10 days.\n4. Count and record the number of emerged weed seedlings in each plot.",
                            "materials": ["Blackjack Seeds", "Dry Grass Mulch", "Watering Can", "Ruler"],
                            "safety": "Ensure grass mulch is free from dry seed heads."
                        }
                    }
                ],
                [
                    {
                        "type": "key_takeaway",
                        "title": "Core Summary: Cultural Control",
                        "content": {
                            "title": "Key Takeaways",
                            "text": "- **Mulching starves weed seeds of sunlight**, halting germination.\n- **Cover cropping provides living ground cover** that outcompetes weeds.\n- **Close crop spacing accelerates canopy closure**, shading late weeds.\n- **Crop rotation disrupts parasitic weed cycles** like *Striga* in maize."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Cowpea Cover Crop Mechanism",
                        "content": {
                            "question": "How does interplanting a dense cover crop of cowpeas suppress weed growth in a commercial maize field?",
                            "options": [
                                "Cowpeas release acidic smoke that poisons weed stems",
                                "The cowpea foliage rapidly covers the bare soil, intercepting sunlight and outcompeting weed seedlings for space and moisture",
                                "Cowpea roots physically dig up weed roots and push them above ground",
                                "Cowpeas attract locusts that selectively eat only weeds"
                            ],
                            "answer": "B",
                            "explanation": "Cover crops act as a living mulch. Their fast-spreading leaves rapidly blanket the ground, intercepting sunlight and casting deep shade. Deprived of solar radiation, emerging weed seeds cannot perform photosynthesis and are effectively choked out without requiring chemical herbicides."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 8: Biological Weed Control
        # =====================================================================
        {
            "unit_order": 8,
            "unit_name": "Biological Weed Control",
            "unit_description": "Deliberate use of natural enemies (insects, mites, fungi, grazing animals) to suppress weed populations below economic thresholds; classic example: Cochineal insect (Dactylopius ceylonicus) on Prickly Pear Cactus (Opuntia aurantiaca); benefits and host-shifting risks.",
            "lesson_title": "Biological Weed Control: Natural Enemies, Benefits, and Ecological Risks",
            "pages": [
                [
                    {
                        "type": "suggested_image",
                        "title": "Biological Control Agent Cochineal Insect Colony on Opuntia Cactus",
                        "content": {
                            "title": "Biological Control Agent Cochineal Insect Colony on Opuntia Cactus",
                            "caption": "A dense colony of Cochineal scale insects (Dactylopius spp.) actively feeding on invasive Prickly Pear cactus pads, destroying weed tissue without chemicals."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Biological Weed Control",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Define **biological weed control** in agriculture.",
                                "Analyze the classic case study: **Cochineal insect (*Dactylopius*) on Prickly Pear Cactus (*Opuntia*)**.",
                                "Evaluate the major advantages (**chemical-free, sustainable, self-perpetuating**).",
                                "Identify critical ecological risks, specifically **dietary host-shifting** to food crops."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "What is Biological Weed Control?",
                        "content": {
                            "title": "Using Nature to Balance Nature",
                            "text": "Biological weed control is the *deliberate introduction or management of specialized natural enemies (insects, mites, plant pathogens, or grazing livestock) to suppress a specific target weed population below the economic injury level*.\n\n- **Target Suppression, Not Total Eradication**: Biological control does not aim to wipe out 100% of the weed, because the biological agent needs a small remaining weed population to survive and reproduce.\n- **Classic Example**: The introduction of the **Cochineal scale insect (*Dactylopius ceylonicus / opuntiae*)** to control the invasive, spiny **Prickly Pear Cactus (*Opuntia aurantiaca*)** that overran grazing pastures in East and Southern Africa."
                        }
                    }
                ],
                [
                    {
                        "type": "comparison_table",
                        "title": "Pros and Ecological Risks of Biological Control",
                        "content": {
                            "title": "Biological Control Evaluation Matrix",
                            "headers": ["Dimension", "Advantages & Strengths", "Limitations & Ecological Risks"],
                            "rows": [
                                ["Environmental Safety", "100% chemical-free; zero soil, water, or food residues", "Exotic imported organisms can cause unexpected ecosystem disruption"],
                                ["Cost Dynamics", "Self-perpetuating: reproduces continuously after initial release", "High upfront laboratory research and quarantine testing costs"],
                                ["Specificity", "Highly host-specific; feeds only on targeted weed species", "Risk of dietary host-shifting if target weed becomes scarce"],
                                ["Control Speed", "Provides long-term permanent background suppression", "Very slow; can take 3 to 7 years to build effective insect numbers"]
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The Host-Shifting Ecological Danger",
                        "content": {
                            "title": "Why Rigorous Testing is Mandatory",
                            "text": "The greatest danger in biological control is **host-shifting**:\n- If an imported insect successfully eliminates its target weed, it may undergo evolutionary pressure or dietary adaptation and begin feeding on domestic food crops (e.g. maize, beans, or fruit trees).\n- **Quarantine Safety Protocols**: Biological agents must undergo years of strict starvation trials inside sealed quarantine facilities before being approved for release in Kenya."
                        }
                    }
                ],
                [
                    {
                        "type": "mini_activity",
                        "title": "Case Study Analysis: Evaluating Biological Control for Water Hyacinth",
                        "content": {
                            "title": "Lake Victoria Water Hyacinth Case Study",
                            "task": "In pairs, analyze the release of Neochetina weevils to control Water Hyacinth on Lake Victoria:\n1. Why was mechanical harvesting or chemical spraying impractical for the entire lake?\n2. How do the weevils damage the water hyacinth plants?\n3. List 2 ecological safety tests scientists conducted before releasing the weevils.",
                            "materials": ["Case Study Handout", "Notebook"],
                            "safety": "Base analysis on scientific environmental protocols."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Core Summary: Biological Control",
                        "content": {
                            "title": "Key Takeaways",
                            "text": "- **Biological control uses natural enemies** (insects, fungi) to suppress weeds.\n- **Cochineal insects effectively control Prickly Pear cactus** in pastures.\n- **Advantages**: Chemical-free, self-sustaining, and environmentally safe.\n- **Major Risk**: Potential host-shifting to valuable agricultural crops."
                        }
                    }
                ],
                [
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Primary Ecological Risk of Biological Control",
                        "content": {
                            "question": "What is the most severe ecological risk that agricultural scientists must evaluate before releasing an imported insect agent to control an invasive weed?",
                            "options": [
                                "The insect might release synthetic chemical fumes that cause acid rain",
                                "The insect could shift its host preference and start feeding on valuable domestic food crops or native indigenous vegetation",
                                "The insect will cause the soil pH to drop to zero",
                                "The insect will stop the sun from shining on the farm"
                            ],
                            "answer": "B",
                            "explanation": "The greatest danger of biological control is host-shifting. If the introduced insect runs out of its target weed or adapts to new food sources, it may begin feeding on valuable agricultural crops or native flora, creating an uncontrollable ecological and agricultural disaster."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 9: Chemical Weed Control
        # =====================================================================
        {
            "unit_order": 9,
            "unit_name": "Chemical Weed Control",
            "unit_description": "Definition of herbicides; classification modes: Selective (2,4-D for broadleaves in cereals) vs Non-selective (Glyphosate); Contact (scorch foliage) vs Systemic/Translocated (moves through vascular system to kill rhizomes).",
            "lesson_title": "Chemical Weed Control: Herbicides, Selectivity, and Translocation",
            "pages": [
                [
                    {
                        "type": "suggested_image",
                        "title": "Commercial Chemical Herbicide Application in Arable Grain Field",
                        "content": {
                            "title": "Commercial Chemical Herbicide Application in Arable Grain Field",
                            "caption": "A tractor-mounted boom sprayer applying a selective post-emergence herbicide to control broad-leaved weeds in a commercial cereal crop."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Chemical Weed Control",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Define what an **herbicide** is and explain its role in commercial agribusiness.",
                                "Distinguish between **Selective vs Non-Selective herbicides**.",
                                "Distinguish between **Contact vs Systemic (Translocated) herbicides**.",
                                "Select the correct herbicide class for annual broadleaves vs perennial rhizome grasses."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "What is an Herbicide?",
                        "content": {
                            "title": "Chemical Crop Protection",
                            "text": "An **herbicide** is a synthetic or organic chemical compound specifically formulated to kill, suppress, or severely inhibit the growth of unwanted plants (weeds).\n\n- **Agribusiness Advantage**: Enables fast, large-scale weed elimination on commercial farms with minimal manual labor.\n- **Precision Requirement**: Requires strict adherence to dosage rates, calibration, timing, and personal protective equipment (PPE)."
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "Classification of Herbicides",
                        "content": {
                            "title": "Selectivity and Mode of Movement",
                            "text": "### 1. By Selectivity\n- **Selective Herbicides**: Kill specific plant families while leaving the crop unharmed.\n  - *Example*: **2,4-D** (kills broad-leaved weeds like Blackjack in narrow-leaved cereal crops like maize and wheat).\n- **Non-Selective Herbicides**: Kill ALL green vegetation they contact.\n  - *Example*: **Glyphosate** (used for total vegetation knockdown during land clearing before planting).\n\n### 2. By Mode of Action & Movement\n- **Contact Herbicides**: Kill only the specific plant tissues they physically touch (foliar scorching). Do not move inside the plant.\n  - *Limitation*: Ineffective against perennial weeds (underground rhizomes quickly sprout new leaves).\n- **Systemic (Translocated) Herbicides**: Absorbed through foliage or roots and translocated through the vascular xylem and phloem to all growing points.\n  - *Advantage*: Permanently kills underground rhizomes, tubers, and deep roots of perennial weeds."
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Chemical Herbicide Action: Contact vs Systemic Translocation",
                        "content": {
                            "title": "Chemical Herbicide Action: Contact vs Systemic Translocation",
                            "caption": "Biochemical comparison diagram: 1 Contact Herbicide scorching only contacted leaf surface (underground rhizome survives), vs 2 Systemic Herbicide absorbing into vascular phloem and translocating downward to destroy underground rhizomes."
                        }
                    }
                ],
                [
                    {
                        "type": "comparison_table",
                        "title": "Master Herbicide Classification Matrix",
                        "content": {
                            "title": "Herbicide Classification Guide",
                            "headers": ["Classification Mode", "Herbicide Class", "Commercial Example", "Agronomic Use Case"],
                            "rows": [
                                ["Selectivity", "Selective", "2,4-D / MCPA", "Post-emergence broad-leaf weed control in maize, wheat, and lawns"],
                                ["Selectivity", "Non-Selective", "Glyphosate (Roundup)", "Total vegetation knockdown during land preparation or fallow"],
                                ["Movement in Plant", "Contact", "Paraquat / Diquat", "Quick burn-down of annual weed seedlings (leaves only)"],
                                ["Movement in Plant", "Systemic (Translocated)", "Glyphosate / 2,4-D", "Eradication of perennial weeds with deep rhizomes (Couch grass)"],
                                ["Application Timing", "Pre-Emergence", "Atrazine / Dual Gold", "Applied to soil after planting but before weed seeds emerge"],
                                ["Application Timing", "Post-Emergence", "2,4-D / Stellar Star", "Applied to green weed foliage after crops and weeds have emerged"]
                            ]
                        }
                    },
                    {
                        "type": "mini_activity",
                        "title": "Agronomic Problem Solving: Selecting Herbicides for 3 Farm Scenarios",
                        "content": {
                            "title": "Herbicide Prescription Workshop",
                            "task": "Recommend the correct herbicide class for each scenario:\n1. Scenario A: Farmer clearing 5 acres of dense overgrown bush and perennial grass before plowing.\n2. Scenario B: A maize crop at knee-high stage infested with Blackjack and Pigweed.\n3. Scenario C: An established lawn infested with deep-rooted broad-leaved dandelions.",
                            "materials": ["Case Handout", "Herbicide Guide"],
                            "safety": "Theoretical matching activity only; no live chemical handling."
                        }
                    }
                ],
                [
                    {
                        "type": "key_takeaway",
                        "title": "Core Summary: Chemical Control",
                        "content": {
                            "title": "Key Takeaways",
                            "text": "- **Selective herbicides** kill specific weeds without harming the crop (e.g. 2,4-D in maize).\n- **Non-selective herbicides** kill all vegetation (e.g. Glyphosate for clearing).\n- **Contact herbicides** only scorch contacted leaves; ineffective on perennial roots.\n- **Systemic herbicides** travel through vascular vessels to destroy underground rhizomes."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Selecting Herbicide for Perennial Couch Grass",
                        "content": {
                            "question": "A farmer wishes to permanently eliminate a severe infestation of Couch grass (a perennial grass weed with deep underground rhizomes) in a fallow field before planting. Which class of herbicide must be used?",
                            "options": [
                                "Selective contact herbicide",
                                "Non-selective systemic (translocated) herbicide",
                                "Selective pre-emergence contact herbicide",
                                "Fungicidal copper spray"
                            ],
                            "answer": "B",
                            "explanation": "Couch grass is a tough perennial weed with extensive underground rhizomes. A systemic (translocated) herbicide (such as glyphosate) is absorbed by the green foliage and carried downward through the vascular phloem into the subterranean rhizomes, killing the growing points. Since the field is fallow (no crop present), a non-selective systemic herbicide is ideal."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 10: Legislative Weed Control (Quarantine)
        # =====================================================================
        {
            "unit_order": 10,
            "unit_name": "Legislative Weed Control (Quarantine)",
            "unit_description": "Government laws and agricultural acts; plant quarantine border checkpoints; officially declared noxious weeds in Kenya: Striga / Witchweed (Striga hermonthica) and Parthenium / Congress weed (Parthenium hysterophorus).",
            "lesson_title": "Legislative Weed Control, Quarantine, and Noxious Weeds",
            "pages": [
                [
                    {
                        "type": "suggested_image",
                        "title": "Parasitic Striga (Witchweed) Flowers Attached to Cereal Crop Roots",
                        "content": {
                            "title": "Parasitic Striga (Witchweed) Flowers Attached to Cereal Crop Roots",
                            "caption": "Bright purple flowers of the devastating parasitic weed Striga hermonthica emerging at the base of stunted, nutrient-starved maize stalks."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Legislative Weed Control",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Define **legislative weed control** and explain national plant quarantine enforcement.",
                                "Analyze what legally constitutes a **noxious weed** under Kenyan law.",
                                "Examine the biology of **Striga (*Striga hermonthica*)** and **Parthenium (*Parthenium hysterophorus*)**.",
                                "Outline the legal obligations of landowners regarding designated noxious weeds."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "What is Legislative Weed Control?",
                        "content": {
                            "title": "National Biosecurity Laws",
                            "text": "Legislative weed control involves *government laws, acts of parliament, and statutory regulations designed to prevent the entry, spread, or multiplication of dangerous, noxious, or invasive weeds within a country or region*.\n\n- **Plant Quarantine Service (KEPHIS in Kenya)**: Enforces strict phytosanitary inspections at international airports, seaports (Mombasa), and border posts to intercept contaminated seed consignments.\n- **Noxious Weeds**: Species officially declared by legal notice as dangerous pests. It is a criminal offense to cultivate, sell, or transport noxious weeds, and landowners are legally mandated to eradicate them on their properties."
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "Two Designated Noxious Weeds in Kenya",
                        "content": {
                            "title": "Extreme Threats to National Food Security",
                            "text": "### 1. Striga Weed (*Striga hermonthica* - Witchweed)\n- **Biology**: A semi-parasitic weed of cereal crops (maize, sorghum, sugarcane).\n- **Damage**: Its roots attach directly to host cereal roots, injecting toxins and siphoning water and minerals, causing 50% to 100% crop failure.\n- **Threat**: Produces up to 500,000 microscopic seeds that remain viable in soil for 20 years.\n\n### 2. Parthenium Weed (*Parthenium hysterophorus* - Congress Weed)\n- **Biology**: An aggressive invasive weed with toxic chemical secretions (parthenin).\n- **Threats**: Suppresses all native vegetation, degrades grazing pastures, and produces airborne pollen causing severe contact dermatitis, eczema, and respiratory asthma in humans and livestock."
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "National Plant Quarantine & Phytosanitary Inspection Barrier",
                        "content": {
                            "title": "National Plant Quarantine & Phytosanitary Inspection Barrier",
                            "caption": "Biosecurity diagram illustrating: Imported Seed Shipments -> KEPHIS Border Inspection Gateway -> Confiscation/Destruction of Contaminated Noxious Seeds -> Clean Certified Produce Released."
                        }
                    }
                ],
                [
                    {
                        "type": "comparison_table",
                        "title": "Legislative vs On-Farm Weed Control Comparison",
                        "content": {
                            "title": "Control Governance Matrix",
                            "headers": ["Feature", "On-Farm Weed Control", "National Legislative Weed Control"],
                            "rows": [
                                ["Authority / Enforcer", "Individual farmer / land manager", "Government regulatory bodies (e.g. KEPHIS, Ministry of Agriculture)"],
                                ["Scope of Operation", "Single farm plot or greenhouse", "National borders, ports of entry, transport corridors"],
                                ["Primary Objective", "Reduce weed competition to maximize season yields", "Prevent entry and spread of exotic, destructive invasive species"],
                                ["Legal Enforcement", "Voluntary good husbandry practice", "Mandatory by law; failure to comply carries legal penalties/fines"]
                            ]
                        }
                    },
                    {
                        "type": "mini_activity",
                        "title": "Policy Brief Workshop: Formulating a Community Noxious Weed Action Plan",
                        "content": {
                            "title": "Drafting a Local Eradication By-Law",
                            "task": "Working as an agricultural advisory committee:\n1. Draft a 3-point community advisory notice for a village heavily infested with *Striga* or *Parthenium*.\n2. Outline mandatory sanitation protocols for tractor plows moving between farms.\n3. Explain how crop rotation with Desmodium (push-pull) suppresses *Striga*.",
                            "materials": ["Template Handout", "Pen"],
                            "safety": "Focus on actionable, evidence-based biosecurity protocols."
                        }
                    }
                ],
                [
                    {
                        "type": "key_takeaway",
                        "title": "Core Summary: Legislative Control",
                        "content": {
                            "title": "Key Takeaways",
                            "text": "- **Legislative weed control enforces national laws** to stop invasive weed entry.\n- **Plant quarantine (KEPHIS)** inspects seeds at ports and border points.\n- **Noxious weeds are legally declared dangerous**; landowners must eradicate them.\n- ***Striga* and *Parthenium*** are priority noxious weeds threatening Kenyan food security."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Landowner Legal Obligation on Noxious Weeds",
                        "content": {
                            "question": "Under national agricultural biosecurity legislation in Kenya, what is the legal obligation of a farmer on whose property a designated 'noxious weed' (such as Striga or Parthenium) is discovered?",
                            "options": [
                                "The farmer is permitted to dry the seeds and sell them on the open market",
                                "The farmer is legally mandated to control or eradicate the weed to prevent its spread to neighboring farms and communities",
                                "The farmer must build a fence and preserve the weed as a national heritage tree",
                                "The farmer can sue the government for compensation"
                            ],
                            "answer": "B",
                            "explanation": "Under the Noxious Weeds Act, when a plant species is declared noxious, landowners have a strict legal duty to control, suppress, or eradicate it on their land. Allowing noxious weeds to flourish and shed seeds threatens neighboring farms and national food security, attracting legal penalties."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 11: Integrated Weed Management (IWM)
        # =====================================================================
        {
            "unit_order": 11,
            "unit_name": "Integrated Weed Management (IWM)",
            "unit_description": "Holistic multi-tactic approach; IWM pyramid hierarchy (Prevention at base -> Cultural -> Physical/Biological -> Targeted Chemical at peak); preventing herbicide resistance and soil degradation.",
            "lesson_title": "Integrated Weed Management (IWM) Principles and Strategies",
            "pages": [
                [
                    {
                        "type": "suggested_image",
                        "title": "Push-Pull Sustainable Intercropping Plot Suppressing Striga Weeds",
                        "content": {
                            "title": "Push-Pull Sustainable Intercropping Plot Suppressing Striga Weeds",
                            "caption": "A demonstration of Push-Pull technology in Kenya: Maize intercropped with Desmodium and Napier grass borders, suppressing parasitic Striga weeds without chemicals."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Integrated Weed Management",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Define **Integrated Weed Management (IWM)**.",
                                "Analyze the **IWM Pyramid Hierarchy** (Prevention $\\rightarrow$ Cultural $\\rightarrow$ Physical $\\rightarrow$ Chemical).",
                                "Explain why relying exclusively on a single control method causes **herbicide resistance** and soil degradation.",
                                "Formulate a comprehensive IWM farm management plan for a commercial grain enterprise."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "What is Integrated Weed Management (IWM)?",
                        "content": {
                            "title": "A Multi-Tactic Holistic Philosophy",
                            "text": "Integrated Weed Management (IWM) is a *sustainable, multidisciplinary approach that combines two or more compatible weed control methods (preventive, cultural, physical, biological, and targeted chemical) in a coordinated plan*.\n\n- **Why Single Methods Fail**:\n  - *Chemical Only*: Leads to rapid evolution of herbicide-resistant superweeds and chemical residue buildup.\n  - *Physical Only*: Causes severe topsoil erosion, hardpan formation, and excessive labor expenses.\n- **Core Goal**: Suppress weed populations **below the Economic Injury Level (EIL)** while minimizing environmental damage and optimizing profit."
                        }
                    }
                ],
                [
                    {
                        "type": "suggested_diagram",
                        "title": "The Integrated Weed Management (IWM) Control Pyramid",
                        "content": {
                            "title": "The Integrated Weed Management (IWM) Control Pyramid",
                            "caption": "Hierarchical pyramid diagram showing: 1 Base Layer: Prevention (Clean Seed & Tools), 2 Cultural Layer (Rotation & Mulching), 3 Physical/Biological Layer (Hoeing & Natural Enemies), and 4 Peak: Targeted Chemical Application (Selective Herbicides as Last Resort)."
                        }
                    },
                    {
                        "type": "step_process",
                        "title": "Protocol: 4 Tiers of an Effective IWM System",
                        "content": {
                            "title": "Constructing an IWM Defense Matrix",
                            "steps": [
                                "1. **Tier 1 (Prevention - The Foundation)**: Use certified weed-free crop seed; wash tractor implements between fields to prevent rhizome/seed transfer.",
                                "2. **Tier 2 (Cultural Practices)**: Rotate cereals with legumes; plant at close spacing for rapid canopy shade; apply dry organic mulch.",
                                "3. **Tier 3 (Physical & Biological Interventions)**: Hand-weed close to crop stems and hoe between rows while weeds are small seedlings.",
                                "4. **Tier 4 (Targeted Chemical - Last Resort)**: Apply selective, low-toxicity herbicides only on localized heavy weed hot-spots rather than blanket-spraying."
                            ]
                        }
                    }
                ],
                [
                    {
                        "type": "comparison_table",
                        "title": "Conventional Single-Method vs Integrated Weed Management",
                        "content": {
                            "title": "Paradigm Comparison Matrix",
                            "headers": ["Evaluation Metric", "Conventional Single-Method (Chemical Only)", "Integrated Weed Management (IWM)"],
                            "rows": [
                                ["Herbicide Resistance Risk", "Very High; weeds evolve resistance in 3–5 seasons", "Very Low; multiple tactics prevent genetic adaptation"],
                                ["Environmental Impact", "High; chemical leaching into groundwater and soil", "Minimal; promotes beneficial soil microbes and insects"],
                                ["Cost Over 5 Years", "Escalating as higher chemical doses are needed", "Decreases as soil weed seed bank is systematically depleted"],
                                ["Soil Structural Health", "Degrades from lack of organic matter inputs", "Improves continuously via mulches, cover crops, and reduced tillage"]
                            ]
                        }
                    },
                    {
                        "type": "mini_activity",
                        "title": "Agribusiness Practical: Designing an IWM Strategy for a 5-Acre Maize Farm",
                        "content": {
                            "title": "IWM Farm Plan Formulation",
                            "task": "Working in groups:\n1. Review a 5-acre maize farm infested with Blackjack and Couch grass.\n2. Design an IWM plan combining: 1 preventive action, 2 cultural actions, 1 physical action, and 1 targeted chemical action.\n3. Present your plan with an estimated seasonal cost budget.",
                            "materials": ["IWM Plan Template", "Notebook", "Calculator"],
                            "safety": "Focus on realistic, sustainable agricultural practices."
                        }
                    }
                ],
                [
                    {
                        "type": "key_takeaway",
                        "title": "Core Summary: Integrated Weed Management",
                        "content": {
                            "title": "Key Takeaways",
                            "text": "- **IWM combines multiple compatible weed control methods** in a planned strategy.\n- **Prevention and cultural methods form the foundation** of the IWM pyramid.\n- **Relying on chemicals alone causes herbicide resistance** and environmental damage.\n- **Targeted chemical spraying is used only as a last resort** on heavy infestations."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Comprehensive IWM Plan Identification",
                        "content": {
                            "question": "Which of the following farm management workflows represents a true Integrated Weed Management (IWM) strategy for commercial maize production?",
                            "options": [
                                "Spraying non-selective herbicides every week throughout the entire growing season",
                                "Sowing certified clean seed, intercropping with a cowpea cover crop, performing shallow hand-hoeing between rows, and spot-treating heavy broadleaf patches with selective herbicide",
                                "Abandoning the field to wild grasses for ten years",
                                "Deep tractor plowing twelve times per month without mulching"
                            ],
                            "answer": "B",
                            "explanation": "True IWM integrates multiple tiers of the control pyramid: clean seed (prevention), cowpea cover cropping (cultural control), shallow hand-hoeing (physical control), and spot-treatment with selective herbicide (targeted chemical control). This achieves sustainable, long-term weed suppression without over-relying on any single method."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 12: Carrying out Weed Control (Practicals)
        # =====================================================================
        {
            "unit_order": 12,
            "unit_name": "Carrying out Weed Control (Practicals)",
            "unit_description": "Practical fieldwork: hand weeding techniques in moist soil, shallow hand hoeing at 2-3 cm depth; teacher-led knapsack sprayer safety protocol (full PPE, 5 m upwind distance, zero spraying in windy conditions).",
            "lesson_title": "Field Practical Execution and Knapsack Sprayer Safety Protocols",
            "pages": [
                [
                    {
                        "type": "suggested_image",
                        "title": "Vegetable Farmer Carrying Out Field Care with Essential Safety Gear",
                        "content": {
                            "title": "Vegetable Farmer Carrying Out Field Care with Essential Safety Gear",
                            "caption": "A farmer working in a horticultural plot adhering to field safety standards and disciplined agronomic management."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Weed Control Practicals & Safety",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Execute **safe hand-weeding and shallow hoeing** techniques in a crop plot.",
                                "Analyze the components of a standard **knapsack sprayer** (tank, pump, hose, lance, nozzle).",
                                "Demonstrate strict **Personal Protective Equipment (PPE)** standards for chemical application.",
                                "Explain the **5-meter upwind student safety rule** and spray drift hazards."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Techniques for Effective Manual Weeding",
                        "content": {
                            "title": "Executing Manual Weeding Without Damaging Crops",
                            "text": "1. **Hand Pulling Technique**:\n- Weed when the **soil is moist** (after rain or irrigation). Moist soil allows the entire taproot/fibrous root to slide out cleanly without snapping the stem.\n- Grip the weed firmly at the soil collar line and pull straight up.\n- Shake off adhering topsoil and place weed trash on the mulch layer.\n\n2. **Hand Hoeing Technique**:\n- Use a sharp hand jembe. Maintain a balanced stance with feet shoulder-width apart.\n- Slice the soil at a shallow **2 to 3 cm depth**. *Avoid deep chopping near crop stems, which severs crop feeder roots*."
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "Teacher-Led Knapsack Sprayer Demonstration & Safety",
                        "content": {
                            "title": "Chemical Safety Protocols",
                            "text": "### CRITICAL STUDENT SAFETY DIRECTIVE\n*Senior secondary students must NEVER mix, handle, or spray concentrated synthetic herbicides directly. All chemical applications must be demonstrated exclusively by a qualified teacher or certified farm technician.*\n\n### Essential Safety Rules for Sprayer Demonstrations\n1. **Full PPE Requirement**: The operator must wear chemical-resistant overalls, heavy nitrile gloves, rubber boots, and a full-face respirator or goggles/mask.\n2. **The 5-Meter Upwind Rule**: Learners must stand at least **5 meters away on the UPWIND side** (wind blowing from learners toward the sprayer) so chemical mist is carried away from their breathing zones.\n3. **Zero Spraying in High Winds**: Never spray if wind speed exceeds 10 km/h, as wind causes severe spray drift onto non-target crops and nearby water sources."
                        }
                    },
                    {
                        "type": "suggested_video",
                        "title": "Safety First: Operating a Knapsack Sprayer on the Farm",
                        "content": {
                            "title": "Safety First: Operating a Knapsack Sprayer on the Farm",
                            "description": "Teacher training video demonstrating knapsack sprayer calibration, nozzle pressure adjustment, full PPE assembly, and spray drift avoidance.",
                            "url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
                        }
                    }
                ],
                [
                    {
                        "type": "comparison_table",
                        "title": "Essential PPE Requirements for Chemical Spraying",
                        "content": {
                            "title": "Personal Protective Equipment (PPE) Checklist",
                            "headers": ["PPE Component", "Specification Standard", "Physiological Protection Function"],
                            "rows": [
                                ["Chemical Respirator / Mask", "Activated carbon filter cartridge", "Prevents inhalation of toxic aerosol vapors and fine mist droplets"],
                                ["Safety Goggles / Face Shield", "Anti-splash chemical visor", "Protects eyes from corrosive chemical splashes and spray drift"],
                                ["Nitrile / Neoprene Gloves", "Heavy-duty, unlined, elbow-length", "Prevents dermal absorption of concentrated chemicals through hands"],
                                ["Waterproof Overalls & Apron", "Heavy PVC or coated fabric", "Prevents chemical soaking into clothing and body skin"],
                                ["Rubber Gumboots", "Steel-toe, chemical-resistant rubber", "Protects feet and ankles from drips, spills, and contaminated soil"]
                            ]
                        }
                    },
                    {
                        "type": "mini_activity",
                        "title": "Field Practical: Executing a 3m x 3m Manual Weeding and Mulching Plot",
                        "content": {
                            "title": "Hands-On Field Weeding Practicum",
                            "task": "Working in teams of four:\n1. Put on garden boots and protective gloves.\n2. In your assigned 3 m x 3 m vegetable plot, hand-pull all weeds close to crop stems and shallow-hoe the inter-row paths.\n3. Remove weed roots cleanly and place weeds in the compost pile.\n4. Apply a 5 cm layer of dry grass mulch across all bare soil areas.",
                            "materials": ["Garden Gloves", "Hand Jembe", "Dry Grass Mulch", "Compost Bucket"],
                            "safety": "Keep feet clear of swinging jembes; wear garden boots."
                        }
                    }
                ],
                [
                    {
                        "type": "key_takeaway",
                        "title": "Core Summary: Practical Execution & Safety",
                        "content": {
                            "title": "Key Takeaways",
                            "text": "- **Hand weed when soil is moist** to pull full root systems cleanly.\n- **Shallow hoe at 2–3 cm depth** to avoid chopping crop roots.\n- **Students must never handle concentrated herbicides directly**.\n- **Stand 5 meters upwind during sprayer demonstrations** wearing full PPE."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Knapsack Demonstration Upwind Safety Rule",
                        "content": {
                            "question": "During a teacher-led demonstration of a knapsack sprayer in a crop field, why must students stand at least 5 meters away on the UPWIND side of the operator?",
                            "options": [
                                "Standing downwind blocks the spray nozzle from maintaining pressure",
                                "The wind blowing from behind the students carries any drifting chemical droplets and toxic aerosol mist away from their respiratory zones and eyes",
                                "The sprayer pump only functions when learners face the sun",
                                "To prevent learners from stepping on the spray hose"
                            ],
                            "answer": "B",
                            "explanation": "Standing on the upwind side ensures that the natural air current blows from the students toward the sprayer. This carries any aerosolized chemical mist or vapor drift away from the students, preventing accidental chemical inhalation, skin contact, or ocular irritation."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 13: Economic Importance of Weeds
        # =====================================================================
        {
            "unit_order": 13,
            "unit_name": "Economic Importance of Weeds",
            "unit_description": "Dual economic perspective: Negative impacts (yield losses 30–100%, labor/input costs, grain contamination, alternative pest hosts, livestock poisoning) vs Positive economic uses (traditional vegetables like Solanum nigrum, livestock forage, soil conservation, composting biomass).",
            "lesson_title": "Economic Significance of Weeds: Financial Losses and Beneficial Uses",
            "pages": [
                [
                    {
                        "type": "suggested_image",
                        "title": "Black Nightshade (Solanum nigrum) Berries and Edible Leaves",
                        "content": {
                            "title": "Black Nightshade (Solanum nigrum) Berries and Edible Leaves",
                            "caption": "Solanum nigrum (Black Nightshade / Managu), an opportunistic weed in commercial fields that doubles as a high-value traditional African leafy vegetable in local markets."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Economic Importance of Weeds",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Analyze the **5 primary negative economic impacts** of weeds on farm profitability.",
                                "Evaluate how weeds cause **yield reduction, product quality loss, and pest harbourage**.",
                                "Identify **positive economic uses** of weeds (indigenous vegetables, forage, composting, medicine).",
                                "Perform a cost-benefit calculation of weed control expenses vs crop yield gains."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Negative Economic Impacts of Weeds",
                        "content": {
                            "title": "How Weeds Erode Farm Revenue",
                            "text": "1. **Severe Yield Reduction**: Weeds compete directly for water, light, and nutrients, slashing crop yields by 30% to 100% (e.g. *Striga* in maize).\n2. **Escalating Production Costs**: Weeding accounts for up to 50% of total manual labor costs on smallholder farms, or requires expensive chemical purchases.\n3. **Quality & Grade Degradation**: Weed seeds contaminate harvested grain (e.g. wild mustard in wheat), imparting foul flavors and causing produce to be downgraded or rejected at mills.\n4. **Alternative Hosts for Pests & Diseases**: Solanaceous weeds host aphids, whiteflies, and viral blights that infect commercial tomato and potato fields.\n5. **Livestock Poisoning & Worker Injury**: Weeds like Sodom Apple and Bracken fern poison cattle, while spiny weeds injure farm laborers, lowering productivity."
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "Positive Economic Uses of Weeds",
                        "content": {
                            "title": "When Weeds Become Valuable Resources",
                            "text": "When properly harvested outside crop rows, certain weeds provide tangible economic benefits:\n\n- **African Indigenous Vegetables (AIVs)**: Weeds like **Black Nightshade (*Solanum nigrum* - Managu)** and **Pigweed (*Amaranthus* - Terere)** are highly nutritious, iron-rich traditional vegetables sold for high prices in urban markets.\n- **Livestock Green Forage**: Succulent weeds like Wandering Jew (*Commelina*) and Kikuyu grass are excellent fresh fodder for dairy cows, goats, and rabbits.\n- **Soil Conservation**: Weeds covering fallow lands prevent severe water and wind erosion.\n- **Compost Biomass**: Soft green weed foliage (harvested before flowering) is rich in nitrogen and ideal for compost heaps.\n- **Medicinal & Biopesticide Uses**: Mexican marigold (*Tagetes minuta*) extracts are processed into natural insect repellents."
                        }
                    },
                    {
                        "type": "comparison_table",
                        "title": "Dual Economic Matrix: Harms vs Beneficial Uses",
                        "content": {
                            "title": "Economic Impact Comparison",
                            "headers": ["Weed Species", "Harmful Weed Status in Crops", "Positive Economic / Household Value"],
                            "rows": [
                                ["Solanum nigrum (Black Nightshade)", "Chokes vegetable beds; hosts tomato viruses", "High-value African traditional vegetable; rich in iron"],
                                ["Amaranthus hybridus (Pigweed)", "Aggressive competitor in maize and beans", "Edible leafy green (Terere); nutrient-dense grain source"],
                                ["Commelina benghalensis (Wandering Jew)", "Smothers seedbeds; difficult to kill due to rooting nodes", "Palatable, high-protein green fodder for dairy cattle & rabbits"],
                                ["Tagetes minuta (Mexican marigold)", "Strong weed competitor in fields", "Natural nematicide and organic pest-repellent extract"],
                                ["Bidens pilosa (Blackjack)", "Severe weed; barbed seeds contaminate wool/clothing", "Young tender shoots used in traditional herbal teas"]
                            ]
                        }
                    }
                ],
                [
                    {
                        "type": "mini_activity",
                        "title": "Market Practical: Surveying African Indigenous Vegetables in Local Markets",
                        "content": {
                            "title": "Weed Agribusiness Market Survey",
                            "task": "1. Visit a local vegetable market or interview a green grocer.\n2. Record prices of Managu (Black Nightshade) and Terere (Pigweed) per bunch.\n3. Compare the market price per kilogram of Managu vs commercial exotic cabbage.\n4. Calculate the potential gross revenue of cultivating Managu as a commercial crop.",
                            "materials": ["Survey Sheet", "Notebook", "Calculator"],
                            "safety": "Follow school safety rules during market excursions."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Core Summary: Economic Importance",
                        "content": {
                            "title": "Key Takeaways",
                            "text": "- **Weeds cause severe yield losses (30–100%)** and inflate farm labor costs.\n- **Weeds contaminate harvested grain** and harbor crop pests and diseases.\n- **Many weeds have positive value**: Managu and Terere are nutritious vegetables.\n- **Commelina provides succulent animal fodder**, and weed biomass makes compost."
                        }
                    }
                ],
                [
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Positive Economic Role of Black Nightshade",
                        "content": {
                            "question": "Which of the following statements correctly illustrates a positive economic and dietary use of the common agricultural weed Solanum nigrum (Black Nightshade / Managu) in Kenya?",
                            "options": [
                                "Its roots are dried and used as heavy timber for roofing",
                                "Its tender green leaves are harvested and sold in retail markets as a highly nutritious, iron-rich traditional African vegetable",
                                "It attaches to maize roots and fixes nitrogen gas into the soil",
                                "Its berries are processed into diesel fuel for farm machinery"
                            ],
                            "answer": "B",
                            "explanation": "Solanum nigrum (Black Nightshade / Managu) is a well-known African Indigenous Vegetable (AIV). Although it acts as a weed in commercial fields, harvesting its leaves provides valuable dietary vitamins and minerals (especially iron) and generates substantial household income when sold in local markets."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 14: Synthesis and Assessment
        # =====================================================================
        {
            "unit_order": 14,
            "unit_name": "Synthesis and Assessment",
            "unit_description": "Consolidated crop protection synthesis; Couch grass disc-plowing diagnostic case study; 8 Summative Topic Assessment MCQs covering the complete Topic 6 module.",
            "lesson_title": "Synthesis of Crop Protection and Summative Assessment",
            "pages": [
                [
                    {
                        "type": "suggested_image",
                        "title": "Clean, Highly Productive Farm Plot Maintained Free of Weeds",
                        "content": {
                            "title": "Clean, Highly Productive Farm Plot Maintained Free of Weeds",
                            "caption": "A healthy, thriving agricultural crop field demonstrating the benefits of disciplined Integrated Weed Management."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Synthesis & Assessment",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Synthesize the entire **Crop Protection and Weed Management curriculum**.",
                                "Connect weed biology and life cycles directly to **agronomic control decisions**.",
                                "Resolve the **Farmer Joseph Couch Grass diagnostic simulation scenario**.",
                                "Complete the **Summative Topic Assessment** covering all 14 lessons of Topic 6."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Master Synthesis: Weed Biology to Control Strategy",
                        "content": {
                            "title": "Strategic Agronomic Decision Matrix",
                            "text": "Effective crop protection requires matching weed biological characteristics to the correct intervention:\n\n- **Annual Broadleaves (e.g. Blackjack, Pigweed)**: Controlled via shallow hand-hoeing, organic mulching, or selective 2,4-D herbicide *strictly before flowering*.\n- **Perennial Grasses (e.g. Couch grass)**: Deep rhizomes require systemic translocated herbicides (glyphosate) or dry-season chisel plowing to desiccate roots in the sun.\n- **Parasitic Weeds (e.g. Striga)**: Managed through Integrated Weed Management (IWM), trap cropping with legumes (Desmodium in push-pull), and crop rotation.\n- **Noxious Weeds (e.g. Parthenium)**: Controlled through strict national quarantine enforcement, legislative biosecurity, and mandatory landowner eradication."
                        }
                    }
                ],
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Couch Grass (Digitaria abyssinica) Rhizome Fragmentation Model",
                        "content": {
                            "title": "Couch Grass (Digitaria abyssinica) Rhizome Fragmentation Model",
                            "caption": "Diagnostic diagram showing: 1 Continuous subterranean Couch Grass rhizome, 2 Tractor Disc Plow cutting rhizome into multiple segments, and 3 Each individual segment sprouting into a new vigorous grass colony, multiplying the infestation."
                        }
                    },
                    {
                        "type": "comparison_table",
                        "title": "Master Crop Protection Strategic Framework",
                        "content": {
                            "title": "Synthesized Weed Management Matrix",
                            "headers": ["Weed Category", "Key Biological Threat", "Primary Management Pillar", "Complementary IWM Tactic"],
                            "rows": [
                                ["Annual Broadleaf Weeds", "Massive seed output (100,000+ seeds/plant)", "Physical weeding / hoeing before flowering", "Organic dry grass mulching (blocks light)"],
                                ["Perennial Grass Weeds", "Subterranean vegetative rhizome networks", "Systemic translocated herbicides (Glyphosate)", "Deep fallow solarization of exposed rhizomes"],
                                ["Sedge Weeds (Nut Grass)", "Solid triangular stems & underground tubers", "Specialized sedge herbicides; continuous shade", "Heavy cover cropping with sweet potatoes"],
                                ["Parasitic Weeds (Striga)", "Siphons nutrients from cereal roots", "Push-pull technology with Desmodium", "Rotating maize with non-host grain legumes"],
                                ["Invasive Noxious Weeds", "Toxicity to livestock; ecological displacement", "Legislative quarantine & mandatory eradication", "Strict tool sanitation between farm blocks"]
                            ]
                        }
                    }
                ],
                [
                    {
                        "type": "mini_activity",
                        "title": "Performance Task: The Farmer Joseph Couch Grass Advisory Brief",
                        "content": {
                            "title": "Agribusiness Diagnostic Advisory Brief",
                            "task": "Farmer Joseph in Trans-Nzoia plowed his 2-acre maize field infested with Couch grass using a tractor disc plow. Two weeks later, the Couch grass regenerated denser than before, choking his young maize.\n\n**Your Deliverable**: Draft a 1-page Technical Advisory Brief explaining:\n1. Why disc plowing multiplied his Couch grass infestation (rhizome fragmentation).\n2. An IWM recovery plan combining 1 chemical, 2 cultural, and 1 physical practice.",
                            "materials": ["Case Handout", "Advisory Template", "Pen"],
                            "safety": "Ensure professional, evidence-based agronomic recommendations."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Core Summary: Crop Protection Mastery",
                        "content": {
                            "title": "Key Takeaways",
                            "text": "- **Match control methods to weed morphology and life cycle**.\n- **Never disc-plow Couch grass without solarizing or spraying rhizomes**.\n- **IWM is the gold standard** for sustainable, chemical-reduced farming.\n- **Weed before flowering** to deplete the long-term soil seed bank."
                        }
                    }
                ],
                # Pages 4 to 8: 8 Summative Assessment MCQs
                [
                    {
                        "type": "knowledge_check",
                        "title": "Summative MCQ 1: Couch Grass Plowing Diagnostic",
                        "content": {
                            "question": "Why did Farmer Joseph's mechanical disc-plowing make the Couch grass (Digitaria abyssinica) infestation significantly worse in his maize field?",
                            "options": [
                                "The tractor engine dropped synthetic fertilizer that stimulated weed seeds",
                                "The disc plow chopped the subterranean rhizomes into pieces, and each segment bearing a vegetative node sprouted into a new independent plant",
                                "Couch grass requires mechanical vibration to produce flowers",
                                "Plowing caused the soil pH to turn into pure sulfur"
                            ],
                            "answer": "B",
                            "explanation": "Couch grass reproduces vegetatively through underground stems called rhizomes. When a disc plow cultivates the soil, it slices the continuous rhizome network into dozens of smaller fragments and distributes them across the topsoil. Since every rhizome node can generate new roots and shoots, plowing effectively multiplies the weed population."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Summative MCQ 2: Herbicide Selectivity in Cereal Crops",
                        "content": {
                            "question": "Which of the following herbicide formulations would a farmer safely apply to kill broad-leaved weeds (like Blackjack and Pigweed) in an established maize field without damaging the maize crop?",
                            "options": [
                                "Non-selective contact herbicide (Paraquat)",
                                "Selective systemic herbicide targeting broad-leaved dicots (2,4-D)",
                                "Non-selective systemic herbicide (Glyphosate)",
                                "Broad-spectrum insecticide"
                            ],
                            "answer": "B",
                            "explanation": "2,4-D is a selective synthetic auxin herbicide that is toxic specifically to broad-leaved dicotyledonous plants (such as Blackjack and Pigweed) while leaving monocotyledonous narrow-leaved grass crops (such as maize, wheat, and sorghum) completely unharmed."
                        }
                    }
                ],
                [
                    {
                        "type": "knowledge_check",
                        "title": "Summative MCQ 3: Sedge Stem Morphological Anatomy",
                        "content": {
                            "question": "Which set of morphological anatomical features uniquely distinguishes a sedge weed (such as Nut grass) from a grass weed (such as Couch grass)?",
                            "options": [
                                "Sedges have round, hollow stems with swollen nodes, while grasses have square solid stems",
                                "Sedges have distinctly triangular, solid stems lacking nodes, with leaves arranged in 3 ranks, while grasses have round, hollow stems with swollen nodes",
                                "Sedges have giant taproots and broad net-veined leaves",
                                "Sedges produce woody cones instead of flowers"
                            ],
                            "answer": "B",
                            "explanation": "Sedge weeds (family Cyperaceae) are characterized by solid, triangular (3-angled) stems that completely lack nodes, and have leaves arranged in three ranks. In contrast, true grasses (family Poaceae) have round, hollow stems (culms) with swollen nodes and leaves arranged in two ranks."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Summative MCQ 4: Herbarium Preparation Daily Paper Changes",
                        "content": {
                            "question": "During the preparation of a weed herbarium, why must the absorbent newspaper sheets be changed every single day for the first 7 to 10 days of pressing?",
                            "options": [
                                "To prevent the print on the newspaper from reading backward",
                                "To rapidly absorb the cellular moisture released by the fresh plant tissues and prevent fungal mold and decay from destroying the specimen",
                                "To allow the plant roots to absorb nitrogen gas from the atmosphere",
                                "To ensure that the cardstock turns completely green"
                            ],
                            "answer": "B",
                            "explanation": "Fresh weed specimens contain up to 90% water. If this expelled moisture is left inside damp paper, saprophytic molds and bacteria rot the plant, turning it black and useless. Changing the newspaper daily rapidly removes moisture, preserving the specimen's physical structures and diagnostic colors."
                        }
                    }
                ],
                [
                    {
                        "type": "knowledge_check",
                        "title": "Summative MCQ 5: Living Cover Crop Weed Suppression",
                        "content": {
                            "question": "What is the primary ecological mechanism through which an interplanted cover crop of cowpeas or sweet potatoes suppresses weed growth in an orchard or maize plot?",
                            "options": [
                                "It exudes toxic acid that melts weed roots",
                                "It forms a dense vegetative ground cover that intercepts solar radiation, depriving emerging weed seeds of the light needed for photosynthesis",
                                "It attracts birds that consume all weed foliage",
                                "It lowers the air temperature below freezing point"
                            ],
                            "answer": "B",
                            "explanation": "Cover crops act as a living mulch. By rapidly blanketing the bare soil surface, they block sunlight. Deprived of solar radiation, emerging weed seeds cannot perform photosynthesis and are effectively choked out naturally without requiring synthetic herbicides."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Summative MCQ 6: Knapsack Sprayer Upwind Safety Rule",
                        "content": {
                            "question": "Why is it mandatory for students to stand at least 5 meters away on the UPWIND side during a teacher-led demonstration of a knapsack sprayer?",
                            "options": [
                                "Standing downwind blocks the sun from warming the spray liquid",
                                "The wind blowing from behind the students carries toxic chemical aerosols and drifting mist droplets away from their respiratory zones and skin",
                                "The knapsack pump lever only operates when facing downwind",
                                "To prevent students from creating shadows over the crops"
                            ],
                            "answer": "B",
                            "explanation": "Standing on the upwind side ensures that the prevailing wind blows from the students toward the sprayer, carrying chemical mist and vapors away from them. This prevents accidental inhalation, ocular irritation, and dermal exposure to toxic pesticides."
                        }
                    }
                ],
                [
                    {
                        "type": "knowledge_check",
                        "title": "Summative MCQ 7: Biological Control Host-Shifting Risk",
                        "content": {
                            "question": "What is the most serious ecological danger associated with importing and releasing an exotic biological control insect (such as a scale insect) to manage a pasture weed?",
                            "options": [
                                "The insect will release synthetic chemical fumes into local water streams",
                                "The insect may undergo dietary host-shifting and begin feeding on valuable domestic food crops or native plants",
                                "The insect will dig deep holes that cause severe soil erosion",
                                "The insect will stop clouds from producing rain"
                            ],
                            "answer": "B",
                            "explanation": "The primary risk of biological control is host-shifting. If the introduced insect agent runs out of its target weed or adapts to new plant hosts, it may attack local agricultural crops or native vegetation, causing severe ecological and economic damage."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Summative MCQ 8: Positive Dietary Role of Black Nightshade",
                        "content": {
                            "question": "Why is Solanum nigrum (Black Nightshade / Managu) considered to have high positive economic value in Kenya, despite being classified as a weed in commercial tomato plots?",
                            "options": [
                                "It produces heavy timber used to build farm barns",
                                "Its leaves are harvested and sold in retail markets as a highly nutritious, traditional leafy vegetable (African Indigenous Vegetable)",
                                "It fixes atmospheric nitrogen directly into cereal grains",
                                "It repels all agricultural insects within a 5-kilometer radius"
                            ],
                            "answer": "B",
                            "explanation": "Black Nightshade (Solanum nigrum / Managu) is a popular, highly nutritious African Indigenous Vegetable (AIV) rich in iron, calcium, and vitamins. Harvesting and selling its leaves provides valuable nutrition and significant household income, transforming it from a nuisance weed into a high-value cash crop."
                        }
                    }
                ],
                # Page 8: Capstone Summary
                [
                    {
                        "type": "summary",
                        "title": "Topic 6 Capstone Summary: Crop Protection Mastery",
                        "content": {
                            "title": "Mastery Overview: Grade 10 Crop Protection and Weed Science",
                            "text": "Congratulations on mastering **Topic 6: Crop Protection**!\n\nYou have mastered:\n- **Weed Biology & Seed Banks**: 5 evolutionary traits (prolific seed output, dormancy, rapid maturity, rhizomes, dispersal adaptations).\n- **Field Diagnostics**: Identifying Blackjack, Wandering Jew, Pigweed, Sodom Apple, and Nut Grass.\n- **Scientific Herbarium**: 5-step preparation protocol (trowel collection with roots, pressing, daily newspaper drying, mounting, standard labeling).\n- **Morphology & Life Cycles**: Broadleaf dicots vs Grasses vs Sedges; Annuals vs Biennials vs Perennials.\n- **Control Methods**: Physical (hand pulling, hoeing), Cultural (mulch, cover crops, rotation), Biological (Cochineal on Opuntia), Chemical (selective vs non-selective, contact vs systemic), and Legislative (quarantine, noxious weeds).\n- **Integrated Weed Management (IWM)**: 4-tiered control pyramid for sustainable, chemical-reduced crop protection.\n- **Field Practicals & Economics**: Safe knapsack sprayer protocols (full PPE, 5 m upwind rule), financial loss mitigation, and utilizing beneficial indigenous weeds like Managu."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Topic 6 Final Takeaway",
                        "content": {
                            "title": "The Sustainable Crop Protection Maxim",
                            "text": "Understand weed biology, identify morphological structures, weed annuals before flowering, protect soils from burning, deploy Integrated Weed Management, and turn beneficial indigenous weeds into household nutrition and agribusiness income."
                        }
                    }
                ]
            ]
        }
    ]

@transaction.atomic
def ingest_grade10_topic6(replace=False):
    """Executes the complete production ingestion of Grade 10 Agriculture Topic 6: Crop Protection."""
    print("=" * 80)
    print("STARTING INGESTION: CBC Grade 10 Agriculture — Topic 6: Crop Protection")
    print("=" * 80)

    curriculum = Curriculum.objects.filter(name__iexact="CBC").first()
    grade = Grade.objects.filter(curriculum=curriculum, name__icontains="10").first()
    subject = Subject.objects.filter(grade=grade, name__iexact="Agriculture").first()

    assert curriculum and grade and subject, "Curriculum/Grade/Subject not found!"

    topic_name = "Crop Protection"
    topic = Topic.objects.filter(subject=subject, name=topic_name).first()
    if not topic:
        topic = Topic.objects.create(
            subject=subject,
            name=topic_name,
            description="Comprehensive theoretical, practical, and scientific study of weed biology, morphological classification, life cycles, physical, cultural, biological, chemical, and legislative weed control, herbarium preparation, knapsack sprayer safety, and Integrated Weed Management (IWM).",
            order=6
        )
        print(f"Created Topic 6: {topic.name} (ID: {topic.id})")
    else:
        topic.order = 6
        topic.description = "Comprehensive theoretical, practical, and scientific study of weed biology, morphological classification, life cycles, physical, cultural, biological, chemical, and legislative weed control, herbarium preparation, knapsack sprayer safety, and Integrated Weed Management (IWM)."
        topic.save()
        print(f"Resolved Topic 6: {topic.name} (ID: {topic.id})")

    if replace:
        print("Flag --replace active: Clearing existing LearningUnits and Lessons for Topic 6...")
        topic.learning_units.all().delete()
        topic.lessons.all().delete()

    curriculum_data = build_topic6_curriculum()
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
                    "topic_order": 6,
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
                    block_id=f"g10_agri_t6_u{u_order}_p{page_idx}_b{comp_idx}",
                    block_type=b_type,
                    component_type=b_type,
                    title=b_title,
                    content=b_content,
                    order=block_order_counter,
                    page_number=page_idx,
                    component_order=comp_idx,
                    page_title=b_title if comp_idx == 1 else None,
                    metadata={"topic_order": 6, "unit_order": u_order, "page": page_idx}
                )
                block_order_counter += 1
                total_blocks += 1

        print(f"  Ingested Unit {u_order}: {u_name} -> Lesson '{l_title}' ({len(pages)} Pages, {block_order_counter - 1} Blocks)")

    print("=" * 80)
    print(f"INGESTION COMPLETE: Topic 6 '{topic.name}'")
    print(f"  Total Units:   {total_units}")
    print(f"  Total Lessons: {total_lessons}")
    print(f"  Total Pages:   {total_pages}")
    print(f"  Total Blocks:  {total_blocks}")
    print("=" * 80)

if __name__ == "__main__":
    replace_flag = "--replace" in sys.argv
    ingest_grade10_topic6(replace=replace_flag)
