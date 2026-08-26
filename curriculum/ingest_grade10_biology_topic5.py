"""
VLearn Grade 10 Biology — Topic 5: Plant Nutrition and Photosynthesis
Production Ingestion Engine (4 Comprehensive Lessons)

Curriculum: CBC (Curriculum ID: 5)
Grade: Grade 10 (Grade ID: 5, Level: 10)
Subject: Biology (Grade 10 CBC)
Topic: Plant Nutrition and Photosynthesis (Topic Order: 5)

Structured into 4 Comprehensive Learning Units & 4 Published Lessons (39 Concept Cards):
  1. Types of Nutrition in Plants (9 Pages)
  2. Leaf and Chloroplast Structure in Photosynthesis (10 Pages)
  3. Light and Dark Stages of Photosynthesis (10 Pages)
  4. Investigating Starch and Factors Affecting Photosynthesis (10 Pages)

Usage:
  ./venv/bin/python curriculum/ingest_grade10_biology_topic5.py [--replace]
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
    """Removes bracket citations [139, 211], visual prompt text, and cleans double spaces."""
    if not text:
        return ""
    # Remove bracket citations like [139], [139, 211], [image_1]
    text = re.sub(r'\[(?:\d+|image_\d+|S\d+.*?|[\d,\s]+)\]', '', text)
    # Remove internal visual generation tags
    text = re.sub(r'\[VISUAL:\s*[^\]]+\]', '', text, flags=re.IGNORECASE)
    # Normalize unicode bullets into markdown list dashes
    text = re.sub(r'^[ \t]*[•\u2022][ \t]*', '- ', text, flags=re.MULTILINE)
    text = re.sub(r'([^\n])[ \t]+[•\u2022][ \t]+', r'\1\n- ', text)
    text = re.sub(r'^([^\n\-\*\d\>#][^\n]*)\n(- |\* )', r'\1\n\n\2', text, flags=re.MULTILINE)
    text = re.sub(r'[ \t]+', ' ', text)
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
    """Returns the comprehensive pedagogical page and block structure for Grade 10 Biology Topic 5."""
    return [
        # =====================================================================
        # LESSON 5.1: Types of Nutrition in Plants
        # =====================================================================
        {
            "unit_order": 1,
            "unit_name": "Types of Nutrition in Plants",
            "unit_description": "Autotrophic vs heterotrophic plant nutrition modes (parasitic Cuscuta, symbiotic Rhizobium in legumes, insectivorous nitrogen traps, and saprophytism).",
            "lesson_title": "Types of Nutrition in Plants",
            "pages": [
                # Page 1: Introduction & Learning Focus
                [
                    {
                        "type": "learning_goal",
                        "title": "Learning Focus: Plant Nutrition Strategies",
                        "content": {
                            "title": "Learning Focus: Plant Nutrition Strategies",
                            "goals": [
                                "Compare autotrophic and heterotrophic nutrition in the plant kingdom.",
                                "Describe specialized plant nutrition modes: parasitic, saprophytic, symbiotic (mutualistic), and insectivorous.",
                                "Relate these specialized feeding adaptations to environmental selection pressures (nutrient-poor soils, shade, host availability)."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The Diversity of Plant Feeding Strategies",
                        "content": {
                            "title": "The Diversity of Plant Feeding Strategies",
                            "text": "When we think of plants, we picture green leaves quietly absorbing sunlight. But the plant kingdom has evolved diverse ecological strategies.\n\nThere are 'thief' plants that steal food from their neighbors, plants that form cooperative business partnerships with soil bacteria, and even carnivorous plants that hunt and digest insects! In this lesson, we examine autotrophic and heterotrophic plant feeding adaptations."
                        }
                    }
                ],
                # Page 2: Key Terms
                [
                    {
                        "type": "definition_card",
                        "title": "Plant Nutrition Vocabulary",
                        "content": {
                            "term": "Essential Plant Trophic Terminology",
                            "definition": "Key concepts in autotrophic synthesis and specialized heterotrophic plant feeding.",
                            "key_points": [
                                "Autotrophic Nutrition: A mode of nutrition where an organism manufactures organic food molecules from simple inorganic raw materials using light energy.",
                                "Heterotrophic Nutrition: A mode of nutrition where an organism cannot make its own food and must consume pre-manufactured organic compounds.",
                                "Parasitic Plant: A non-photosynthetic or partially photosynthetic plant that attaches to a living host to draw water and nutrients via haustoria, causing harm.",
                                "Symbiosis (Mutualism): A close ecological relationship between two different species where both organisms derive biological benefits.",
                                "Insectivorous Plant: A photosynthetic plant that traps and digests insects to obtain vital nitrogen in acidic, nutrient-deficient soils."
                            ]
                        }
                    }
                ],
                # Page 3: Autotrophic vs Heterotrophic Nutrition Overview
                [
                    {
                        "type": "concept_explanation",
                        "title": "Autotrophic Solar Synthesis vs. Heterotrophic Adaptation",
                        "content": {
                            "title": "Autotrophic Solar Synthesis vs. Heterotrophic Adaptation",
                            "text": "1. **Autotrophic Nutrition (Photosynthesis)**:\n- Most plants possess **chlorophyll** inside chloroplasts to trap sunlight, synthesizing glucose from $CO_2$ and $H_2O$.\n- This autotrophic production forms the energetic foundation of terrestrial food webs.\n\n2. **Heterotrophic Plant Lifestyles**:\n- When environmental conditions prevent photosynthesis (dense forest understories, loss of chlorophyll) or soils lack critical minerals (waterlogged acidic bogs), plants evolve alternative feeding strategies:\n  - **Parasitism** (*Cuscuta* / Dodder)\n  - **Mutualism** (*Rhizobium* in legume root nodules)\n  - **Insectivory** (Pitcher plants, Venus flytraps)\n  - **Saprophytism** (Extracellular decay digestion)"
                        }
                    }
                ],
                # Page 4: Specialized Plant Feeding Strategies SVG
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Specialized Plant Feeding Strategies & Adaptations",
                        "content": {
                            "description": "Three-panel comparative vector diagram: 1. Parasitic Cuscuta vine wrapping around a host stem, with penetrating haustoria tapping into host xylem and phloem; 2. Symbiotic legume root nodules housing nitrogen-fixing Rhizobium bacteria exchanging nitrates for sucrose; 3. Insectivorous Pitcher plant modified leaf trap secreting protease enzymes to absorb amino acids.",
                            "caption": "Morphological adaptations of parasitic, symbiotic, and insectivorous plant feeding modes."
                        }
                    }
                ],
                # Page 5: Comparative Feeding Strategies Table
                [
                    {
                        "type": "comparison_table",
                        "title": "Specialized Heterotrophic Plant Adaptations",
                        "content": {
                            "headers": ["Trophic Strategy", "Representative Species", "Key Structural Adaptations", "Ecological Mechanism & Nutrient Exchange"],
                            "rows": [
                                ["Parasitism", "Cuscuta (Dodder vine)", "Yellow, leafless vines lacking chlorophyll; penetrating **haustoria**", "Haustoria invade host stem, tapping phloem for sucrose and xylem for water; stunts and withers host crop"],
                                ["Symbiosis (Mutualism)", "Rhizobium in legume root nodules (beans, peas)", "Specialized cortical root nodules housing bacteria", "Mutual benefit: Bacteria convert atmospheric $N_2$ into soluble nitrates for plant proteins; plant provides sugars and shelter"],
                                ["Insectivory (Carnivory)", "Pitcher plant (Nepenthes), Venus Flytrap", "Modified leaf traps, sweet nectar lures, digestive protease secretion", "Grows in acidic, nitrogen-poor bogs; photosynthesizes for sugars but digests insects to harvest nitrogen for protein synthesis"],
                                ["Saprophytism", "Specialized non-green plants and fungi", "Extracellular hyphal digestive enzymes", "Secretes enzymes onto dead decaying organic matter, absorbing digested soluble nutrients across cell membranes"]
                            ]
                        }
                    }
                ],
                # Page 6: Cuscuta & Legume Root Nodules Image
                [
                    {
                        "type": "suggested_image",
                        "title": "Cuscuta Parasitic Vine and Legume Root Nodules",
                        "content": {
                            "description": "High-resolution photograph showing a yellow Dodder vine (Cuscuta) tightly coiled around an agricultural host stem, alongside an excavated legume root system displaying prominent spherical Rhizobium root nodules.",
                            "caption": "Real-world manifestations of specialized plant nutrition: parasitic Cuscuta stealing host sap and symbiotic Rhizobium root nodules fixing atmospheric nitrogen."
                        }
                    }
                ],
                # Page 7: Common Misconception: Insectivorous Nitrogen Hunting
                [
                    {
                        "type": "common_misconception",
                        "title": "Misconception: Insectivorous Plants Eat Insects for Energy",
                        "content": {
                            "misconception": "Insectivorous plants like Venus flytraps and pitcher plants eat insects to obtain energy and do not photosynthesize.",
                            "correction": "Insectivorous plants are green and possess abundant chlorophyll; they manufacture ALL their carbohydrates and sugars through normal photosynthesis! They trap insects strictly to harvest nitrogen, which is absent in waterlogged acidic bogs. Nitrogen is essential for building proteins and nucleic acids."
                        }
                    }
                ],
                # Page 8: Deep Dive Educational Video
                [
                    {
                        "type": "suggested_video",
                        "title": "Deep Dive: Plant Nutrition — Autotrophs, Parasites, and Carnivorous Plants",
                        "content": {
                            "description": "Educational documentary examining the diverse modes of plant nutrition, parasitic haustoria mechanics, legume root nodule symbiosis, and carnivorous plant digestive enzymes."
                        }
                    }
                ],
                # Page 9: Knowledge Check & Summary
                [
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Parasitic Vine Infestation",
                        "content": {
                            "question": "A farmer in Kakamega notices that a leafless, orange vine has wrapped around her passion fruit plants, causing them to wither. Microscopic analysis shows the vine has structures penetrating the host plant's stem. What is the feeding mode of this orange vine, and what are the penetrating structures called?",
                            "options": [
                                "Symbiotic feeding; root nodules",
                                "Parasitic feeding; haustoria",
                                "Saprophytic feeding; rhizoids",
                                "Insectivorous feeding; trigger hairs"
                            ],
                            "correct_answer": "B",
                            "explanation": "The vine is a parasitic plant (Cuscuta / Dodder) that lacks leaves and chlorophyll. It uses specialized sucker-like root organs called haustoria to physically penetrate the host's vascular bundles to steal manufactured sugars and water, causing the host to wither."
                        }
                    },
                    {
                        "type": "summary",
                        "title": "Lesson Summary: Plant Nutrition Strategies",
                        "content": {
                            "title": "Lesson Summary: Plant Nutrition Strategies",
                            "points": [
                                "Autotrophic plants use chlorophyll to manufacture organic food via photosynthesis.",
                                "Parasitic plants (Cuscuta) lack chlorophyll and steal sap using penetrating haustoria.",
                                "Symbiotic legumes house nitrogen-fixing Rhizobium bacteria in root nodules.",
                                "Insectivorous plants photosynthesize for sugars but trap insects to obtain nitrogen in acidic soils."
                            ]
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 5.2: Leaf and Chloroplast Structure in Photosynthesis
        # =====================================================================
        {
            "unit_order": 2,
            "unit_name": "Leaf and Chloroplast Structure in Photosynthesis",
            "unit_description": "Internal and external leaf anatomy adaptations (lamina, cuticle, palisade/spongy mesophyll, stomata, veins) and chloroplast ultrastructure (grana thylakoids, stroma matrix).",
            "lesson_title": "Leaf and Chloroplast Structure in Photosynthesis",
            "pages": [
                # Page 1: Introduction & Learning Focus
                [
                    {
                        "type": "learning_goal",
                        "title": "Learning Focus: Leaf & Chloroplast Anatomy",
                        "content": {
                            "title": "Learning Focus: Leaf & Chloroplast Anatomy",
                            "goals": [
                                "Relate the external and internal physical structure of a leaf to its photosynthetic role.",
                                "Describe the ultrastructure of a chloroplast as seen under an electron microscope.",
                                "Relate specific chloroplast compartments (grana thylakoids and stroma matrix) to light and dark reactions."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Nature's Solar-Harvesting Masterpiece",
                        "content": {
                            "title": "Nature's Solar-Harvesting Masterpiece",
                            "text": "If you were engineered to build the ultimate solar energy collector, you would make it broad, flat, and wafer-thin to capture maximum sunlight while allowing carbon dioxide gas to penetrate instantly.\n\nYou would also coat it in a transparent waterproof film to prevent drying out. Nature engineered this exact masterpiece: the **green leaf**."
                        }
                    }
                ],
                # Page 2: Key Terms
                [
                    {
                        "type": "definition_card",
                        "title": "Leaf & Chloroplast Vocabulary",
                        "content": {
                            "term": "Essential Photosynthetic Anatomical Terms",
                            "definition": "Key structural components of leaves and subcellular chloroplast organelles.",
                            "key_points": [
                                "Lamina: The broad, flat, green blade of a leaf providing an expansive surface area for sunlight interception.",
                                "Palisade Mesophyll: Columnar, tightly-packed cells located beneath the upper epidermis packed with dense chloroplasts to maximize light capture.",
                                "Spongy Mesophyll: Loosely arranged irregular cells with large intercellular air spaces allowing rapid gas diffusion.",
                                "Stroma: The gel-like, enzyme-rich fluid matrix inside a chloroplast where dark stage carbon fixation occurs.",
                                "Granum (plural Grana): A stack of disc-like thylakoid membranes containing chlorophyll where light stage reactions occur."
                            ]
                        }
                    }
                ],
                # Page 3: Internal Leaf Anatomy Adaptations
                [
                    {
                        "type": "concept_explanation",
                        "title": "Internal Leaf Stratification & Photosynthetic Adaptations",
                        "content": {
                            "title": "Internal Leaf Stratification & Photosynthetic Adaptations",
                            "text": "The leaf is structured to maximize light interception and gas exchange while minimizing water loss:\n\n- **Waxy Cuticle & Upper Epidermis**: Transparent to allow sunlight to reach photosynthetic cells while preventing evaporative water loss.\n- **Palisade Mesophyll**: Columnar cells packed vertically beneath the upper epidermis, containing the highest density of chloroplasts to maximize light capture.\n- **Spongy Mesophyll**: Loosely arranged cells with vast intercellular air spaces that circulate $CO_2$ and $O_2$ freely.\n- **Stomatal Pores & Guard Cells**: Concentrated on the lower epidermis; guard cells regulate stomatal aperture for gas exchange.\n- **Vascular Bundles (Veins)**: **Xylem** delivers water and dissolved minerals; **Phloem** translocates manufactured sugars away to storage sinks."
                        }
                    }
                ],
                # Page 4: Stratified 3D Leaf & Chloroplast SVG
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Stratified 3D Dicot Leaf Anatomy & Chloroplast Ultrastructure",
                        "content": {
                            "description": "Dual-panel diagram. Panel A: Stratified 3D cross-section of a dicot leaf showing waxy cuticle, upper epidermis, columnar palisade mesophyll packed with chloroplasts, spongy mesophyll with intercellular air spaces, vascular bundle with xylem and phloem, lower epidermis, and guard cells with stomatal pore. Panel B: Chloroplast ultrastructure showing double membrane, thylakoid grana stacks, connecting lamellae, fluid stroma, circular DNA, and starch granules.",
                            "caption": "Structural integration between leaf tissue architecture and subcellular chloroplast organelles."
                        }
                    }
                ],
                # Page 5: Chloroplast Subcellular Organelle
                [
                    {
                        "type": "concept_explanation",
                        "title": "The Chloroplast: Subcellular Solar Engine",
                        "content": {
                            "title": "The Chloroplast: Subcellular Solar Engine",
                            "text": "Photosynthesis is coordinated inside double-membrane-bound organelles called **chloroplasts**:\n\n1. **Double Outer & Inner Membrane**: Encloses the chloroplast and regulates metabolite transport.\n2. **Thylakoid Grana**: Disc-shaped membrane sacs stacked like plates into **grana**. Thylakoid membranes contain green **chlorophyll** pigments that trap photon energy for the light stage.\n3. **Intergranal Lamellae**: Tubular membranes connecting adjacent grana stacks.\n4. **Fluid Stroma**: The protein-rich gel matrix surrounding the grana, housing enzymes, circular DNA, ribosomes, and starch granules for the dark stage."
                        }
                    }
                ],
                # Page 6: Leaf Transverse Section Micrograph
                [
                    {
                        "type": "suggested_image",
                        "title": "Transverse Section of Dicot Leaf under Light Microscope at 200x",
                        "content": {
                            "description": "High-clarity stained light micrograph of a dicot leaf cross-section showing upper epidermis, tightly packed columnar palisade mesophyll cells, spongy mesophyll with air spaces, vascular bundle vein, and lower stomata.",
                            "caption": "Photomicrograph of a dicot leaf cross-section at 200x magnification showing palisade and spongy mesophyll stratification."
                        }
                    }
                ],
                # Page 7: Structure-Function Summary Table
                [
                    {
                        "type": "comparison_table",
                        "title": "Leaf Structure-to-Function Adaptations",
                        "content": {
                            "headers": ["Leaf Anatomical Feature", "Structural Adaptation", "Photosynthetic Function"],
                            "rows": [
                                ["Leaf Lamina", "Broad, flat, and wafer-thin", "Maximizes surface area for sunlight interception; minimizes diffusion distance for $CO_2$"],
                                ["Cuticle & Upper Epidermis", "Transparent, single cell layer with waxy coating", "Allows light to penetrate directly to palisade cells; prevents desiccation"],
                                ["Palisade Mesophyll", "Vertically elongated cells densely packed with chloroplasts", "Captures maximum sunlight entering from the upper leaf surface"],
                                ["Spongy Mesophyll", "Irregular loosely packed cells with large air spaces", "Enables rapid internal diffusion of $CO_2$ to palisade cells and $O_2$ to stomata"],
                                ["Vascular Bundle (Vein)", "Contains lignified xylem tubes and phloem sieve tubes", "Xylem delivers water for photolysis; phloem translocates sucrose away to storage organs"],
                                ["Stomata & Guard Cells", "Microscopic pores primarily on lower epidermis", "Regulates gaseous exchange ($CO_2$ in, $O_2$ out) while minimizing water vapor loss"]
                            ]
                        }
                    }
                ],
                # Page 8: Deep Dive Educational Video
                [
                    {
                        "type": "suggested_video",
                        "title": "Deep Dive: Leaf Anatomy and Chloroplast Structure",
                        "content": {
                            "description": "Video presentation exploring the microscopic stratification of foliage leaves, palisade cell adaptations, and chloroplast thylakoid grana ultrastructure."
                        }
                    }
                ],
                # Page 9: Knowledge Check
                [
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Leaf Color Variation",
                        "content": {
                            "question": "Under a microscope, a student observes that the upper surface of a hibiscus leaf is a much deeper, darker green than the pale green lower surface. Which anatomical feature explains this difference?",
                            "options": [
                                "The upper cuticle contains green waxy pigments.",
                                "The lower epidermis is transparent, whereas the upper epidermis is filled with chlorophyll.",
                                "Palisade mesophyll cells are densely packed with chloroplasts and are located directly beneath the upper epidermis to capture maximum sunlight.",
                                "Spongy mesophyll cells have larger chloroplasts than palisade cells."
                            ],
                            "correct_answer": "C",
                            "explanation": "The palisade mesophyll layer is positioned directly beneath the transparent upper epidermis to intercept incoming sunlight. Because palisade cells contain the highest concentration of chloroplasts, the upper surface of the leaf appears distinctly darker green than the lower surface."
                        }
                    }
                ],
                # Page 10: Summary
                [
                    {
                        "type": "summary",
                        "title": "Lesson Summary: Leaf & Chloroplast Anatomy",
                        "content": {
                            "title": "Lesson Summary: Leaf & Chloroplast Anatomy",
                            "points": [
                                "Leaf lamina, thinness, and transparent cuticle maximize light capture and rapid gas diffusion.",
                                "Palisade mesophyll is adapted for sunlight absorption; spongy mesophyll enables internal gas circulation.",
                                "Chloroplasts feature thylakoid grana stacks (for light trapping) and a fluid stroma (for sugar synthesis).",
                                "Vascular xylem delivers water; phloem translocates manufactured carbohydrates."
                            ]
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 5.3: Light and Dark Stages of Photosynthesis
        # =====================================================================
        {
            "unit_order": 3,
            "unit_name": "Light and Dark Stages of Photosynthesis",
            "unit_description": "Biochemical pathways of the Light-Dependent Stage (grana photolysis, ATP synthesis) and Light-Independent Stage (stroma CO2 fixation, glucose synthesis, starch storage).",
            "lesson_title": "Light and Dark Stages of Photosynthesis",
            "pages": [
                # Page 1: Introduction & Learning Focus
                [
                    {
                        "type": "learning_goal",
                        "title": "Learning Focus: Molecular Stages of Photosynthesis",
                        "content": {
                            "title": "Learning Focus: Molecular Stages of Photosynthesis",
                            "goals": [
                                "Explain the reactants, products, and biochemical occurrences of the Light-Dependent Stage.",
                                "Explain the chemical reactions, enzyme activities, and occurrences of the Light-Independent (Dark) Stage.",
                                "Detail how the chemical products of the light stage drive the dark stage."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The Two-Part Molecular Assembly Line",
                        "content": {
                            "title": "The Two-Part Molecular Assembly Line",
                            "text": "Photosynthesis is often summarized as: carbon dioxide + water $\\rightarrow$ glucose + oxygen. But inside the cell, this is a sophisticated two-part biochemical assembly line.\n\nThe first stage uses physical solar light energy to split water molecules. The second stage uses the captured chemical energy to assemble sugars."
                        }
                    }
                ],
                # Page 2: Key Terms
                [
                    {
                        "type": "definition_card",
                        "title": "Photosynthetic Bioenergetics Vocabulary",
                        "content": {
                            "term": "Essential Photosynthetic Reaction Terminology",
                            "definition": "Key concepts in chloroplast molecular pathways.",
                            "key_points": [
                                "Light-Dependent Reaction: The first stage of photosynthesis occurring in thylakoid grana, where trapped light energy splits water and synthesizes ATP and hydrogen ions.",
                                "Light-Independent Reaction (Dark Stage): The second stage of photosynthesis occurring in the stroma, where $CO_2$ is reduced to glucose using ATP and hydrogen ions from the light stage.",
                                "Photolysis: The light-driven chemical splitting of water molecules into hydrogen ions ($H^+$), electrons, and oxygen gas ($O_2$).",
                                "Adenosine Triphosphate (ATP): The high-energy nucleotide molecule that transfers chemical energy to power dark stage carbon reduction.",
                                "Carbon Fixation: The incorporation of inorganic carbon ($CO_2$) into organic carbohydrates (glucose)."
                            ]
                        }
                    }
                ],
                # Page 3: Overview of the Two Stages
                [
                    {
                        "type": "concept_explanation",
                        "title": "Coordination Between the Light and Dark Stages",
                        "content": {
                            "title": "Coordination Between the Light and Dark Stages",
                            "text": "Photosynthesis operates as two distinct, sequential chemical pathways occurring in different compartments of the chloroplast:\n\n1. **The Light-Dependent Stage (in Grana Thylakoids)**: Absorbs solar energy, splits $H_2O$ via photolysis, releases $O_2$, and generates ATP and $H^+$ ions.\n2. **The Light-Independent Stage / Dark Stage (in Stroma)**: Consumes ATP and $H^+$ ions to fix $CO_2$ into glucose, which is rapidly converted to insoluble starch."
                        }
                    }
                ],
                # Page 4: Molecular Flowchart SVG
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Molecular Flowchart: Light and Dark Stages of Photosynthesis",
                        "content": {
                            "description": "Dynamic biochemical flowchart showing chloroplast interior. Left (Granum): Traps Light and Water (H2O), performs Photolysis, releases Oxygen (O2) byproduct, and exports ATP and H+ ions. Right (Stroma): Absorbs CO2, consumes ATP and H+ ions, performs Carbon Fixation, and exports Glucose and stored Starch.",
                            "caption": "Biochemical coupling between thylakoid light-dependent photolysis and stromal dark-stage carbon fixation."
                        }
                    }
                ],
                # Page 5: The Light-Dependent Stage in Detail
                [
                    {
                        "type": "step_process",
                        "title": "The Molecular Mechanism of the Light Stage (Grana)",
                        "content": {
                            "title": "The Molecular Mechanism of the Light Stage (Grana)",
                            "steps": [
                                {
                                    "step_number": 1,
                                    "title": "Light Energy Absorption",
                                    "description": "Chlorophyll pigments in thylakoid membranes absorb photons, exciting electrons to higher energy levels."
                                },
                                {
                                    "step_number": 2,
                                    "title": "Photolysis of Water",
                                    "description": "Trapped light energy powers the enzymatic splitting of water molecules:\n$$2\\text{H}_2\\text{O} \\xrightarrow{\\text{Light Energy}} 4\\text{H}^+ + 4e^- + \\text{O}_2\\text{ (gas)}$$"
                                },
                                {
                                    "step_number": 3,
                                    "title": "Oxygen Gas Release",
                                    "description": "Oxygen ($O_2$) is released as a metabolic byproduct, diffusing out through stomata or utilized by mitochondria for plant respiration."
                                },
                                {
                                    "step_number": 4,
                                    "title": "ATP Synthesis & Product Transfer",
                                    "description": "Electron energy drives photophosphorylation ($\\text{ADP} + \\text{P} \\rightarrow \\text{ATP}$). ATP and $H^+$ ions diffuse out of the grana into the stroma."
                                }
                            ]
                        }
                    }
                ],
                # Page 6: The Dark Stage & Starch Storage
                [
                    {
                        "type": "concept_explanation",
                        "title": "The Light-Independent Stage (Dark Stage) & Starch Synthesis",
                        "content": {
                            "title": "The Light-Independent Stage (Dark Stage) & Starch Synthesis",
                            "text": "The dark stage occurs in the fluid **stroma**:\n\n1. **Carbon (IV) Oxide Fixation & Reduction**:\n- $CO_2$ gas diffuses into the stroma.\n- Using chemical energy from ATP and reducing power from $H^+$ ions, $CO_2$ is reduced to form simple carbohydrates (glucose):\n$$\\text{CO}_2 + 4\\text{H}^+ \\xrightarrow{\\text{ATP Energy}} (\\text{CH}_2\\text{O})_n + \\text{H}_2\\text{O}$$\n\n2. **Polymerization into Insoluble Starch**:\n- Simple glucose is highly soluble and osmotically active. If allowed to accumulate, it would draw excessive water into cells via osmosis, disrupting osmotic balance.\n- Plant cells immediately polymerize glucose into **starch**, which is insoluble and osmotically inert, storing it safely in the stroma."
                        }
                    }
                ],
                # Page 7: TEM Chloroplast Grana Micrograph
                [
                    {
                        "type": "suggested_image",
                        "title": "Transmission Electron Micrograph of Chloroplast Grana and Stroma",
                        "content": {
                            "description": "High-resolution Transmission Electron Micrograph (TEM) of a plant chloroplast showing parallel stacks of dark thylakoid grana connected by lamellae and surrounded by the granular fluid stroma matrix.",
                            "caption": "Transmission electron micrograph (TEM) showing the stacked thylakoid grana (site of light photolysis) and fluid stroma (site of dark carbon fixation)."
                        }
                    }
                ],
                # Page 8: Common Misconception: Dark Stage Timing
                [
                    {
                        "type": "common_misconception",
                        "title": "Misconception: The Dark Stage Only Occurs at Night",
                        "content": {
                            "misconception": "Because it is called the 'Dark Stage', this phase of photosynthesis only occurs at night in the dark.",
                            "correction": "The dark stage is 'light-independent' (does not directly require photons), but it requires a continuous supply of short-lived ATP and $H^+$ ions produced by the light stage. Therefore, most dark-stage carbon fixation occurs during the daytime when the light stage is actively running!"
                        }
                    }
                ],
                # Page 9: Deep Dive Educational Video
                [
                    {
                        "type": "suggested_video",
                        "title": "Deep Dive: Photosynthesis — Light-Dependent and Light-Independent Reactions",
                        "content": {
                            "description": "Comprehensive video guide explaining chlorophyll photon excitation, photolysis of water, ATP generation, Calvin cycle carbon fixation, and starch polymerization."
                        }
                    }
                ],
                # Page 10: Knowledge Check & Summary
                [
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Photosynthesis in Complete Darkness",
                        "content": {
                            "question": "If a healthy green plant is placed in a sealed room with carbon dioxide but in complete darkness, which of the following will occur within a few minutes?",
                            "options": [
                                "The dark stage will continue normally because it does not require light.",
                                "The light stage will stop, and the dark stage will also stop once existing pools of ATP and hydrogen ions are exhausted.",
                                "Photolysis will increase to compensate for the darkness.",
                                "The plant will produce starch instead of glucose."
                            ],
                            "correct_answer": "B",
                            "explanation": "Although the dark stage is light-independent, it depends entirely on ATP and hydrogen ions produced by the light stage. In complete darkness, photolysis stops immediately. As soon as the stroma's limited pool of ATP and H+ is depleted, the dark stage halts."
                        }
                    },
                    {
                        "type": "summary",
                        "title": "Lesson Summary: Molecular Stages of Photosynthesis",
                        "content": {
                            "title": "Lesson Summary: Molecular Stages of Photosynthesis",
                            "points": [
                                "The Light Stage in thylakoid grana splits water ($2H_2O \\rightarrow 4H^+ + 4e^- + O_2$) and generates ATP.",
                                "The Dark Stage in the stroma utilizes ATP and $H^+$ to reduce $CO_2$ into glucose.",
                                "Glucose is rapidly converted into insoluble starch to prevent cellular osmotic disruption.",
                                "The dark stage relies on light-stage products and proceeds primarily during daylight."
                            ]
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 5.4: Investigating Starch and Factors Affecting Photosynthesis
        # =====================================================================
        {
            "unit_order": 4,
            "unit_name": "Investigating Starch and Factors Affecting Photosynthesis",
            "unit_description": "Safe leaf starch testing protocols, experimental investigations of necessary factors (light, CO2, chlorophyll), and analysis of limiting factor rate curves.",
            "lesson_title": "Investigating Starch and Factors Affecting Photosynthesis",
            "pages": [
                # Page 1: Introduction & Learning Focus
                [
                    {
                        "type": "learning_goal",
                        "title": "Learning Focus: Starch Testing & Limiting Factors",
                        "content": {
                            "title": "Learning Focus: Starch Testing & Limiting Factors",
                            "goals": [
                                "Explain and carry out the steps to safely test a green leaf for the presence of starch.",
                                "Design and interpret controlled experiments investigating factors necessary for photosynthesis: light, carbon dioxide, and chlorophyll.",
                                "Analyze the concept and kinetic rate curves of limiting factors (light intensity, CO2 concentration, temperature)."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Proving Photosynthesis in the Laboratory",
                        "content": {
                            "title": "Proving Photosynthesis in the Laboratory",
                            "text": "How do scientists prove that a leaf has performed photosynthesis? We cannot see glucose molecules forming with our naked eyes.\n\nHowever, because plants rapidly convert glucose into **starch**, we can use chemical reagents to detect starch and prove photosynthesis has occurred. In this lesson, we master these essential practical investigations."
                        }
                    }
                ],
                # Page 2: Key Terms
                [
                    {
                        "type": "definition_card",
                        "title": "Photosynthesis Investigation Vocabulary",
                        "content": {
                            "term": "Essential Experimental Terminology",
                            "definition": "Key concepts in photosynthesis laboratory assays and kinetic regulation.",
                            "key_points": [
                                "Destarching: Keeping a potted plant in complete darkness for 48 hours to ensure all pre-existing starch is converted to sugar and translocated away.",
                                "Limiting Factor: An environmental factor in shortest supply that directly restricts the rate of a physiological process.",
                                "Variegated Leaf: A leaf exhibiting green patches (with chlorophyll) and white/yellow patches (lacking chlorophyll)."
                            ]
                        }
                    }
                ],
                # Page 3: Safe Leaf Starch Test Protocol
                [
                    {
                        "type": "step_process",
                        "title": "The Four-Step Protocol for Testing a Leaf for Starch",
                        "content": {
                            "title": "The Four-Step Protocol for Testing a Leaf for Starch",
                            "steps": [
                                {
                                    "step_number": 1,
                                    "title": "Boil in Water (Kill Protoplasm)",
                                    "description": "Place the leaf in boiling water for 5–10 minutes. This kills the living protoplasm, breaks cell membranes, and denatures all enzymes, halting metabolic reactions."
                                },
                                {
                                    "step_number": 2,
                                    "title": "Boil in Ethanol in Water Bath (Decolorization)",
                                    "description": "Place boiled leaf into a tube of methylated spirit in a hot water bath. (NEVER heat ethanol over an open flame!). Ethanol dissolves green chlorophyll, turning the leaf white/pale."
                                },
                                {
                                    "step_number": 3,
                                    "title": "Rinse in Warm Water (Softening)",
                                    "description": "Dip the brittle, alcohol-dehydrated leaf into warm water to wash away alcohol residues and restore flexibility."
                                },
                                {
                                    "step_number": 4,
                                    "title": "Add Iodine on White Tile",
                                    "description": "Spread the pale leaf flat on a clean white tile. Add drops of yellow-brown Iodine solution. Result: Starch turns blue-black; absence of starch remains yellow-brown."
                                }
                            ]
                        }
                    }
                ],
                # Page 4: Factor Experiments & Limiting Curves SVG
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Photosynthesis Factor Experiments & Limiting Factor Response Curves",
                        "content": {
                            "description": "Composite diagram. Top panel: Three experimental factor setups: 1. Light shield (aluminum foil strip); 2. Carbon dioxide deprivation (leaf in flask with NaOH pellets); 3. Chlorophyll requirement (variegated Coleus leaf). Bottom panel: Three limiting factor response curves: CO2 concentration curve (rise then plateau), Light intensity curve (rise then plateau), and Temperature curve (rise to 35-40°C optimum with thermal denaturation plunge above 40°C).",
                            "caption": "Experimental setups for investigating necessary factors alongside environmental limiting factor kinetic response curves."
                        }
                    }
                ],
                # Page 5: Experiments Proving Necessary Factors
                [
                    {
                        "type": "comparison_table",
                        "title": "Experiments Investigating Necessary Photosynthetic Factors",
                        "content": {
                            "headers": ["Factor Investigated", "Experimental Setup & Treatment", "Expected Starch Test Observation", "Biological Scientific Deduction"],
                            "rows": [
                                ["Light Energy", "Destarch plant; cover middle portion of leaf with opaque aluminum foil; expose to sunlight for 5 hours", "Uncovered exposed areas turn **Blue-Black**; covered dark area remains **Yellow-Brown**", "Light is indispensable for photolysis and powering the light stage of photosynthesis"],
                                ["Carbon (IV) Oxide ($CO_2$)", "Destarch plant; seal one leaf inside a conical flask containing solid Sodium Hydroxide (NaOH) pellets; expose to sun", "Leaf inside CO₂-free flask remains **Yellow-Brown**; control leaf outside turns **Blue-Black**", "Carbon (IV) oxide is a necessary raw chemical reactant for stromal glucose synthesis"],
                                ["Chlorophyll Pigment", "Expose a variegated plant (*Coleus* or *Tradescantia*) to sunlight for 5 hours; test leaf for starch", "Originally green areas turn **Blue-Black**; originally white/yellow areas remain **Yellow-Brown**", "Chlorophyll is the mandatory pigment required to absorb photon energy for photosynthesis"]
                            ]
                        }
                    }
                ],
                # Page 6: Diagnostic Starch Test Results Image
                [
                    {
                        "type": "suggested_image",
                        "title": "Diagnostic Leaf Starch Test: Positive Blue-Black vs Negative Brown-Yellow",
                        "content": {
                            "description": "High-clarity photograph of starch test results on a variegated leaf and light-shielded leaf, showing sharp contrast between blue-black iodine staining in photosynthetic regions and unstained yellow-brown areas.",
                            "caption": "Diagnostic Iodine starch test results demonstrating localized starch synthesis in light-exposed, chlorophyll-containing leaf zones."
                        }
                    }
                ],
                # Page 7: Environmental Limiting Factors Table
                [
                    {
                        "type": "comparison_table",
                        "title": "Environmental Limiting Factors Governing Photosynthesis Rate",
                        "content": {
                            "headers": ["Limiting Factor", "Physiological Role in Photosynthesis", "Effect of Increase on Rate", "Plateau / Denaturation Mechanism"],
                            "rows": [
                                ["Carbon Dioxide ($CO_2$) Concentration", "Carbon substrate for glucose synthesis in stroma", "Rate increases as more $CO_2$ is fixed by enzymes", "Plateaus when enzyme active sites in stroma become fully saturated; light or temperature becomes limiting"],
                                ["Light Intensity", "Drives photolysis of water and ATP synthesis in grana", "Rate increases proportionally as more chlorophyll molecules absorb photons", "Plateaus when chlorophyll light-harvesting complexes reach maximum photon absorption capacity"],
                                ["Temperature", "Controls kinetic energy of stromal enzymes (e.g. RuBisCO)", "Rate doubles for every 10°C rise up to optimum (~35–40°C)", "Above 40°C, thermal energy breaks hydrogen bonds, denaturing enzymes; rate plunges rapidly to zero"]
                            ]
                        }
                    }
                ],
                # Page 8: Deep Dive Educational Video
                [
                    {
                        "type": "suggested_video",
                        "title": "Deep Dive: Investigating Starch and Limiting Factors in Photosynthesis",
                        "content": {
                            "description": "Laboratory demonstration showing safe leaf starch testing in water baths, destarching procedures, light/CO2 factor setups, and graphical limiting factor analysis."
                        }
                    }
                ],
                # Page 9: Knowledge Check
                [
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Carbon Dioxide Deprivation Experiment",
                        "content": {
                            "question": "A biology student sets up an experiment to prove that Carbon (IV) oxide is necessary for photosynthesis. She places a destarched potted plant in the sun, with one leaf sealed inside a flask containing sodium hydroxide pellets. After 5 hours, she performs a starch test. What is the correct step to perform first, and what will the iodine color be on the experimental leaf?",
                            "options": [
                                "Boil the leaf in methylated spirit directly over a flame; blue-black.",
                                "Boil the leaf in water for 10 minutes; yellow-brown.",
                                "Wash the leaf in cold water; yellow-brown.",
                                "Boil the leaf in iodine solution; blue-black."
                            ],
                            "correct_answer": "B",
                            "explanation": "The mandatory first step in any leaf starch test is boiling the leaf in water for 5–10 minutes to kill the protoplasm and halt all metabolic enzyme reactions. Because Sodium Hydroxide chemically absorbed all CO2 inside the flask, the leaf could not synthesize starch, causing the iodine to remain yellow-brown."
                        }
                    }
                ],
                # Page 10: Summary
                [
                    {
                        "type": "summary",
                        "title": "Lesson Summary: Starch Testing & Limiting Factors",
                        "content": {
                            "title": "Lesson Summary: Starch Testing & Limiting Factors",
                            "points": [
                                "Leaf starch testing involves boiling in water, ethanol decolorization in a water bath, and iodine staining.",
                                "Destarching plants for 48 hours ensures that pre-existing starch is removed prior to factor testing.",
                                "Controlled experiments prove that light, carbon dioxide, and chlorophyll are all indispensable for photosynthesis.",
                                "Photosynthetic rates are regulated by limiting factors ($CO_2$, light intensity, and temperature enzyme kinetics)."
                            ]
                        }
                    }
                ]
            ]
        }
    ]

def ingest_grade10_biology_topic5(replace=False):
    """Executes the database ingestion for Grade 10 Biology Topic 5."""
    print("=" * 80)
    print("VLearn Grade 10 Biology — Ingestion Engine")
    print("Topic 5: Plant Nutrition and Photosynthesis (CBC Curriculum ID: 5)")
    print("=" * 80)

    # 1. Resolve Curriculum
    curriculum = Curriculum.objects.filter(name="CBC").first() or Curriculum.objects.filter(id=5).first()
    if not curriculum:
        print("[!] Fatal: Curriculum 'CBC' (ID: 5) not found in database!")
        return

    print(f"[*] Curriculum: {curriculum.name} (ID: {curriculum.id})")

    # 2. Resolve Grade
    grade = Grade.objects.filter(curriculum=curriculum, name="Grade 10").first() or Grade.objects.filter(curriculum=curriculum, level=10).first()
    if not grade:
        print("[!] Fatal: Grade 'Grade 10' under CBC not found in database!")
        return

    print(f"[*] Grade: {grade.name} (ID: {grade.id}, Level: {grade.level})")

    # 3. Resolve Subject under Grade 10 CBC (Strict Scope Isolation)
    subject, created = Subject.objects.get_or_create(
        grade=grade,
        name="Biology",
        defaults={"description": "Grade 10 Biology Curriculum under CBC senior secondary science pathway."}
    )
    print(f"[*] Subject: {subject.name} under {grade.name} (ID: {subject.id})")

    # 4. Resolve Topic 5
    topic_name = "Plant Nutrition and Photosynthesis"
    topic = Topic.objects.filter(subject=subject, name=topic_name).first()

    if topic and replace:
        print(f"[*] Found existing Topic '{topic_name}' (ID: {topic.id}). Performing clean replacement of child units/lessons...")
        topic.learning_units.all().delete()
        topic.lessons.all().delete()
    elif not topic:
        topic = Topic.objects.create(
            subject=subject,
            name=topic_name,
            order=5,
            description="Comprehensive syllabus on plant nutrition modes (autotrophic, parasitic, mutualistic, insectivorous), leaf and chloroplast structure, light and dark stages of photosynthesis, starch testing, and limiting factors."
        )
        print(f"[+] Created Topic: {topic.name} (ID: {topic.id})")
    else:
        print(f"[*] Using existing Topic: {topic.name} (ID: {topic.id})")

    curriculum_data = build_topic5_curriculum()
    total_lessons = 0
    total_pages = 0
    total_blocks = 0

    with transaction.atomic():
        for unit_data in curriculum_data:
            unit_order = unit_data["unit_order"]
            unit_name = unit_data["unit_name"]
            unit_desc = unit_data["unit_description"]
            lesson_title = unit_data["lesson_title"]
            pages_data = unit_data["pages"]

            learning_unit, _ = LearningUnit.objects.get_or_create(
                topic=topic,
                order=unit_order,
                defaults={"name": unit_name, "description": unit_desc}
            )

            learning_unit.name = unit_name
            learning_unit.description = unit_desc
            learning_unit.save()

            lesson = Lesson.objects.filter(topic=topic, learning_unit=learning_unit).first()
            if lesson:
                lesson.blocks.all().delete()
                lesson.title = lesson_title
                lesson.status = "published"
                lesson.version = 1
                lesson.save()
            else:
                lesson = Lesson.objects.create(
                    topic=topic,
                    learning_unit=learning_unit,
                    title=lesson_title,
                    status="published",
                    version=1
                )
            print(f"  [+] Ingesting Lesson {unit_order}: {lesson.title} (Lesson ID: {lesson.id})")

            block_order = 10
            lesson_page_count = len(pages_data)

            for page_idx, page_blocks in enumerate(pages_data, 1):
                first_block_title = page_blocks[0].get("title", f"Concept Card {page_idx}")
                for b_data in page_blocks:
                    b_type = b_data["type"]
                    b_title = b_data.get("title", first_block_title)
                    b_content = clean_dict(b_data.get("content", {}))

                    LessonBlock.objects.create(
                        lesson=lesson,
                        page_number=page_idx,
                        page_title=first_block_title,
                        title=b_title,
                        block_type=b_type,
                        component_type=b_type,
                        component_order=block_order,
                        order=block_order,
                        content=b_content,
                        metadata={}
                    )
                    block_order += 10
                    total_blocks += 1

            total_lessons += 1
            total_pages += lesson_page_count
            print(f"      [OK] Ingested {lesson_page_count} Concept Cards for Lesson {unit_order}.")

    print("=" * 80)
    print("[SUCCESS] Grade 10 Biology Topic 5 Ingestion Complete!")
    print(f"[*] Total Lessons Ingested: {total_lessons}")
    print(f"[*] Total Pages/Cards:      {total_pages}")
    print(f"[*] Total Blocks Created:   {total_blocks}")
    print("=" * 80)

if __name__ == "__main__":
    replace_flag = "--replace" in sys.argv
    ingest_grade10_biology_topic5(replace=replace_flag)
