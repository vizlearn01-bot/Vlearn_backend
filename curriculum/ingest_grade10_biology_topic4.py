"""
VLearn Grade 10 Biology — Topic 4: Chemicals of Life
Production Ingestion Engine (4 Comprehensive Lessons)

Curriculum: CBC (Curriculum ID: 5)
Grade: Grade 10 (Grade ID: 5, Level: 10)
Subject: Biology (Grade 10 CBC)
Topic: Chemicals of Life (Topic Order: 4)

Structured into 4 Comprehensive Learning Units & 4 Published Lessons (39 Concept Cards):
  1. Carbohydrates, Lipids, Proteins, and Vitamins (10 Pages)
  2. Water, Mineral Salts, and Cellular Importance (9 Pages)
  3. Food Tests for Carbohydrates, Lipids, Proteins, and Vitamin C (10 Pages)
  4. Enzymes, Catalase, and Factors Affecting Activity (10 Pages)

Usage:
  ./venv/bin/python curriculum/ingest_grade10_biology_topic4.py [--replace]
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
    """Removes bracket citations [67, 69], visual prompt text, and cleans double spaces."""
    if not text:
        return ""
    # Remove bracket citations like [67], [67, 69], [image_1]
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

def build_topic4_curriculum():
    """Returns the comprehensive pedagogical page and block structure for Grade 10 Biology Topic 4."""
    return [
        # =====================================================================
        # LESSON 4.1: Carbohydrates, Lipids, Proteins, and Vitamins
        # =====================================================================
        {
            "unit_order": 1,
            "unit_name": "Carbohydrates, Lipids, Proteins, and Vitamins",
            "unit_description": "Chemical composition, properties, and biological roles of organic biomolecules (carbohydrates, lipids, proteins), condensation and hydrolysis, and vitamin deficiencies.",
            "lesson_title": "Carbohydrates, Lipids, Proteins, and Vitamins",
            "pages": [
                # Page 1: Introduction & Learning Focus
                [
                    {
                        "type": "learning_goal",
                        "title": "Learning Focus: Organic Biomolecules & Vitamins",
                        "content": {
                            "title": "Learning Focus: Organic Biomolecules & Vitamins",
                            "goals": [
                                "Explain the chemical composition, physical properties, and biological functions of carbohydrates, lipids, and proteins.",
                                "Explain the processes of condensation and hydrolysis in building and breaking biomolecules.",
                                "Identify major vitamins, their biological functions, rich dietary sources, and deficiency diseases (scurvy, rickets, night blindness, hemorrhages)."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "What Are Living Organisms Made Of?",
                        "content": {
                            "title": "What Are Living Organisms Made Of?",
                            "text": "If we break your body down to its chemical foundations, you are a collection of carbon, hydrogen, oxygen, nitrogen, and a few other key elements.\n\nThese elements are assembled into four major classes of organic molecules: **carbohydrates, lipids, proteins, and vitamins**. Understanding these 'chemicals of life' is the key to understanding how our bodies build structures, release cellular energy, and fight disease."
                        }
                    }
                ],
                # Page 2: Key Terms
                [
                    {
                        "type": "definition_card",
                        "title": "Biomolecular Chemistry Vocabulary",
                        "content": {
                            "term": "Essential Organic Chemistry Terminology",
                            "definition": "Key concepts in biological macromolecules and energetic nutrition.",
                            "key_points": [
                                "Biochemistry: The study of chemical components, structures, and metabolic reactions occurring inside living organisms.",
                                "Monomer: A simple molecule that serves as the basic repeating unit for synthesizing larger polymer chains.",
                                "Polymer: A large macromolecule composed of multiple repeating monomer units linked by covalent chemical bonds.",
                                "Condensation: A chemical synthesis reaction linking two monomers with the release of a water molecule ($H_2O$).",
                                "Hydrolysis: A chemical splitting reaction breaking polymer bonds through the chemical addition of water.",
                                "Denaturation: A permanent structural alteration in a protein or enzyme caused by heat or extreme pH, destroying its 3D active conformation."
                            ]
                        }
                    }
                ],
                # Page 3: Organic Biomolecules Overview
                [
                    {
                        "type": "concept_explanation",
                        "title": "The Four Major Classes of Organic Biomolecules",
                        "content": {
                            "title": "The Four Major Classes of Organic Biomolecules",
                            "text": "All living cells are built upon carbon-based organic compounds:\n\n- **Carbohydrates**: Built from $C, H, O$ (in a $1:2:1$ ratio). Act as the primary respiratory fuel (glucose) and structural plant cell walls (cellulose).\n- **Lipids (Fats and Oils)**: Built from glycerol and fatty acids. Hydrophobic molecules storing double the energy of carbohydrates per gram, providing thermal insulation and forming cell membranes.\n- **Proteins**: Built from amino acid chains ($C, H, O, N, S$). Essential for growth, tissue repair, enzymes, antibodies, and structural keratin/collagen.\n- **Vitamins**: Organic micro-nutrients required in minute quantities for enzymatic cofactors and metabolic health."
                        }
                    }
                ],
                # Page 4: Biomolecules Concept Map SVG
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Biomolecules Concept Map: Carbohydrates, Lipids, Proteins, and Vitamins",
                        "content": {
                            "description": "Biochemical concept map showing a central hub 'Chemicals of Life' branching into 4 detailed panels: Carbohydrates (monosaccharides, disaccharides, polysaccharides), Lipids (glycerol + 3 fatty acids, energy storage, membranes), Proteins (amino acids, peptide bonds, denaturation, enzymes), and Vitamins (A, C, D, K with functions and deficiency diseases).",
                            "caption": "Structural and physiological classification of the four major classes of biological macromolecules."
                        }
                    }
                ],
                # Page 5: Carbohydrate Classification
                [
                    {
                        "type": "comparison_table",
                        "title": "Classification and Biological Roles of Carbohydrates",
                        "content": {
                            "headers": ["Carbohydrate Class", "Representative Examples", "Physical Properties", "Major Biological Functions"],
                            "rows": [
                                ["Monosaccharides (Simple Sugars)", "Glucose, Fructose, Galactose", "Single sugar units; sweet-tasting; highly soluble in water; crystalline", "Primary respiratory substrate oxidized in cellular respiration to generate ATP; fruit attractants for seed dispersal"],
                                ["Disaccharides (Double Sugars)", "Sucrose (Glucose + Fructose), Maltose, Lactose", "Two monosaccharide units linked by condensation; sweet and water-soluble", "Transport carbohydrate in plant phloem (sucrose); milk sugar powering infant mammalian growth (lactose)"],
                                ["Polysaccharides (Complex Sugars)", "Starch, Glycogen, Cellulose, Chitin", "Massive polymer chains of thousands of glucose units; non-sweet; completely insoluble in water", "Starch: Plant energy storage; Glycogen: Liver/muscle energy storage in animals; Cellulose: Plant cell wall rigidity; Chitin: Fungal walls and arthropod exoskeletons"]
                            ]
                        }
                    }
                ],
                # Page 6: Lipids and Proteins: Structures and Denaturation
                [
                    {
                        "type": "concept_explanation",
                        "title": "Lipids, Proteins, and the Mechanics of Denaturation",
                        "content": {
                            "title": "Lipids, Proteins, and the Mechanics of Denaturation",
                            "text": "1. **Lipids (Fats & Oils)**:\n- Composed of 1 **glycerol** molecule bonded to 3 **fatty acid** chains through condensation.\n- Entirely hydrophobic (insoluble in water) but soluble in organic solvents (alcohol).\n- Provide double the energy yield of carbohydrates per gram ($38\\text{ kJ/g}$ vs $17\\text{ kJ/g}$), thermal insulation under skin, shock absorption around kidneys, and waterproof waxy cuticles on leaves.\n\n2. **Proteins & Denaturation**:\n- Linear polymers of **amino acids** folded into precise three-dimensional conformations.\n- **Denaturation**: High heat (above 45–50°C) or extreme pH breaks delicate hydrogen and ionic bonds holding the protein's 3D structure. The polypeptide chain uncoils, destroying active sites permanently."
                        }
                    }
                ],
                # Page 7: Essential Vitamins & Deficiency Disorders
                [
                    {
                        "type": "comparison_table",
                        "title": "Essential Vitamins, Dietary Sources, and Deficiency Disorders",
                        "content": {
                            "headers": ["Vitamin", "Solubility", "Rich Dietary Sources", "Key Biological Function", "Deficiency Disorder & Symptoms"],
                            "rows": [
                                ["Vitamin A (Retinol)", "Fat-soluble", "Carrots, liver, sweet potatoes, green leafy vegetables", "Maintains visual rhodopsin in retinal rod cells for low-light vision; healthy skin", "Night Blindness: Inability to see in dim light; Xerophthalmia (corneal drying)"],
                                ["Vitamin C (Ascorbic Acid)", "Water-soluble", "Citrus fruits (oranges, lemons), tomatoes, fresh guavas", "Collagen synthesis for gums, capillaries, and rapid wound healing", "Scurvy: Bleeding gums, loose teeth, delayed wound healing, subcutaneous hemorrhages"],
                                ["Vitamin D (Calciferol)", "Fat-soluble", "Oily fish, egg yolk, milk; synthesized in skin exposed to sunlight", "Promotes intestinal absorption of Calcium for strong bone and tooth mineralization", "Rickets (in children): Soft, weak bones that bend under body weight causing bowed legs; Osteomalacia in adults"],
                                ["Vitamin K (Phylloquinone)", "Fat-soluble", "Spinach, cabbage, broccoli, egg yolk, gut flora synthesis", "Essential cofactor in liver for synthesizing blood-clotting prothrombin proteins", "Excessive Bleeding: Blood fails to clot at wounds, causing dangerous continuous hemorrhages"]
                            ]
                        }
                    },
                    {
                        "type": "common_misconception",
                        "title": "Misconception: Megadoses of Vitamin C Give Permanent Cold Immunity",
                        "content": {
                            "misconception": "Taking massive overdoses of Vitamin C supplements will make a person permanently immune to colds and respiratory infections.",
                            "correction": "Vitamin C is a water-soluble vitamin that cannot be stored in the body. Any excess consumed beyond daily metabolic requirements is filtered out by the kidneys and excreted in urine. Excessive megadoses simply waste money and can cause gastrointestinal irritation and kidney stones."
                        }
                    }
                ],
                # Page 8: Dietary Biomolecules Image
                [
                    {
                        "type": "suggested_image",
                        "title": "Rich Dietary Sources of Essential Biomolecules and Vitamins",
                        "content": {
                            "description": "High-resolution photograph displaying a rich balanced nutritional spread: fresh citrus fruits (Vitamin C), carrots and green vegetables (Vitamin A), whole grains (carbohydrates), eggs and oily fish (Proteins & Vitamin D), and nuts and olive oils (Lipids).",
                            "caption": "Balanced dietary sources supplying essential carbohydrates, lipids, proteins, and vitamins required for cellular metabolism and disease prevention."
                        }
                    }
                ],
                # Page 9: Deep Dive Educational Video
                [
                    {
                        "type": "suggested_video",
                        "title": "Deep Dive: Biomolecules — Carbohydrates, Lipids, Proteins, and Vitamins",
                        "content": {
                            "description": "Comprehensive video exploration of biological macromolecules, condensation and hydrolysis reactions, protein 3D structures, and clinical vitamin deficiency syndromes."
                        }
                    }
                ],
                # Page 10: Knowledge Check & Summary
                [
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Pediatric Bone Softening",
                        "content": {
                            "question": "A young child in a rural community presents with soft, painful bones that are bending outwards under his body weight, resulting in severely bowed legs. The family's diet consists mainly of maize porridge and boiled cassava, and the child is kept indoors most of the day. Which nutritional deficiency is this child suffering from?",
                            "options": [
                                "Scurvy due to lack of Vitamin C",
                                "Night blindness due to lack of Vitamin A",
                                "Rickets due to lack of Vitamin D and Calcium",
                                "Anemia due to lack of Iron"
                            ],
                            "correct_answer": "C",
                            "explanation": "Rickets is a bone-softening deficiency disorder caused by insufficient Vitamin D or Calcium. Vitamin D is essential for intestinal absorption of calcium needed for bone mineralization. Unfortified maize/cassava diets lack these nutrients, and lack of sunlight exposure prevents endogenous skin synthesis of Vitamin D."
                        }
                    },
                    {
                        "type": "summary",
                        "title": "Lesson Summary: Biomolecules & Vitamins",
                        "content": {
                            "title": "Lesson Summary: Biomolecules & Vitamins",
                            "points": [
                                "Living matter is built from carbohydrates ($C, H, O$), lipids ($C, H, O$), and proteins ($C, H, O, N, S$).",
                                "Condensation links monomers by releasing water; hydrolysis breaks polymers by adding water.",
                                "Carbohydrates provide fuel (glucose) and structure (cellulose); lipids provide energy storage and insulation; proteins drive growth and enzyme catalysis.",
                                "Vitamins are vital micronutrients preventing specific deficiency diseases: Vitamin A (Night blindness), Vitamin C (Scurvy), Vitamin D (Rickets), and Vitamin K (Hemorrhages)."
                            ]
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 4.2: Water, Mineral Salts, and Cellular Importance
        # =====================================================================
        {
            "unit_order": 2,
            "unit_name": "Water, Mineral Salts, and Cellular Importance",
            "unit_description": "Properties and cellular importance of water (solvent, transport, thermal buffering, turgor, reactant), and physiological roles and deficiencies of mineral ions (Ca2+, Fe2+, Na+, K+, I-).",
            "lesson_title": "Water, Mineral Salts, and Cellular Importance",
            "pages": [
                # Page 1: Introduction & Learning Focus
                [
                    {
                        "type": "learning_goal",
                        "title": "Learning Focus: Water & Mineral Physiology",
                        "content": {
                            "title": "Learning Focus: Water & Mineral Physiology",
                            "goals": [
                                "Explain the unique physical and chemical properties of water that make it indispensable for cellular life.",
                                "Identify the biological roles of major mineral salts: Sodium (Na+), Potassium (K+), Calcium (Ca2+), Iron (Fe2+), and Iodine (I-).",
                                "Relate mineral deficiencies to physiological disorders in plants and animals (anaemia, goitre, rickets, plant chlorosis)."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The Inorganic Matrix of Life",
                        "content": {
                            "title": "The Inorganic Matrix of Life",
                            "text": "If you look at the Earth from space, you see a blue planet covered in water. If you look inside any living cell, you see the exact same thing: water.\n\nYour body is approximately 65% water, and some active cells are up to 90% water. Dissolved within this fluid matrix are charged **mineral ions** that act as the structural anchors and electrical switches of living organisms."
                        }
                    }
                ],
                # Page 2: Key Terms
                [
                    {
                        "type": "definition_card",
                        "title": "Inorganic Biochemistry Vocabulary",
                        "content": {
                            "term": "Essential Inorganic Terminology",
                            "definition": "Key concepts governing aqueous cellular physiology and ionic nutrition.",
                            "key_points": [
                                "Universal Solvent: A liquid (like water) capable of dissolving a wider variety of chemical substances than any other solvent, facilitating biochemical reactions.",
                                "Mineral Salt: An inorganic ionic compound required by living organisms to perform vital physiological and structural functions.",
                                "Ion: An atom or molecule carrying a net electrical charge from losing or gaining valence electrons.",
                                "Osmotic Pressure: The hydrostatic pressure required to prevent the osmotic influx of water across a selectively permeable membrane.",
                                "Haemoglobin: An iron-containing conjugated globular protein in red blood cells that reversibly binds and transports oxygen."
                            ]
                        }
                    }
                ],
                # Page 3: The 5 Cellular Roles of Water
                [
                    {
                        "type": "step_process",
                        "title": "The Five Essential Cellular Roles of Water",
                        "content": {
                            "title": "The Five Essential Cellular Roles of Water",
                            "steps": [
                                {
                                    "step_number": 1,
                                    "title": "Universal Biochemical Solvent",
                                    "description": "Due to molecular polarity, water dissolves ionic salts and polar sugars. Metabolic chemical reactions can ONLY occur when reacting molecules are dissolved in an aqueous solution."
                                },
                                {
                                    "step_number": 2,
                                    "title": "Circulatory & Transport Medium",
                                    "description": "Water forms the fluid basis of blood plasma, lymph, and plant vascular sap (xylem/phloem), transporting dissolved nutrients, gases, hormones, and metabolic wastes."
                                },
                                {
                                    "step_number": 3,
                                    "title": "Thermal Buffer & Evaporative Cooling",
                                    "description": "High specific heat capacity buffers cells against lethal sudden temperature swings; high latent heat of vaporization cools the body through sweat and plant transpiration."
                                },
                                {
                                    "step_number": 4,
                                    "title": "Cellular Turgidity & Mechanical Support",
                                    "description": "Water inflates plant vacuoles, generating turgor pressure that presses cytoplasm firmly against cell walls to support non-woody herbaceous stems upright."
                                },
                                {
                                    "step_number": 5,
                                    "title": "Direct Metabolic Chemical Reactant",
                                    "description": "Water provides hydrogen ions during photolysis in photosynthesis ($2H_2O \\rightarrow 4H^+ + 4e^- + O_2$) and splits peptide/glycosidic bonds during digestive hydrolysis."
                                }
                            ]
                        }
                    }
                ],
                # Page 4: Roles of Water & Mineral Salts Infographic SVG
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Physiological Roles of Water and Essential Mineral Salts",
                        "content": {
                            "description": "Illustrated biochemical infographic. In the center: A hydrated living cell detailing the 4 major aqueous functions (Solvent, Transport, Cooling, Turgidity). Surrounding it: 5 radiating mineral ion badges: Calcium Ca2+ (bone/teeth/clotting), Iron Fe2+ (haemoglobin/anaemia), Sodium & Potassium Na+/K+ (nerve impulses/osmosis), Iodine I- (thyroid thyroxine/goitre), and Magnesium Mg2+ (chlorophyll synthesis).",
                            "caption": "Functional integration of aqueous cellular physiology with essential inorganic mineral ions."
                        }
                    }
                ],
                # Page 5: Roles of Major Mineral Salts
                [
                    {
                        "type": "comparison_table",
                        "title": "Roles, Sources, and Deficiencies of Essential Mineral Salts",
                        "content": {
                            "headers": ["Mineral Ion", "Rich Dietary / Environmental Sources", "Major Biological Functions", "Deficiency Disorder & Symptoms"],
                            "rows": [
                                ["Calcium (Ca2+)", "Milk, cheese, green leafy vegetables, small bony fish (Omena)", "Mineralization of bones and teeth; essential for muscle contraction, nerve impulse transmission, and blood clotting", "Rickets in children; Osteoporosis in adults; severe muscle cramps and tetany"],
                                ["Iron (Fe2+ / Fe3+)", "Red meat, liver, beans, lentils, dark green spinach", "Forms the prosthetic haem group at the core of haemoglobin to bind and transport oxygen", "Anaemia: Low red blood cell count, pale conjunctiva/skin, chronic fatigue, and shortness of breath"],
                                ["Sodium (Na+) & Potassium (K+)", "Table salt (NaCl), bananas, potatoes, sea salt", "Regulates osmotic fluid balance; generates resting and action potentials across nerve axons and muscle fibers", "Severe dehydration, muscular weakness, cramps, and life-threatening cardiac arrhythmias"],
                                ["Iodine (I-)", "Iodized table salt, marine fish, seaweed, kelp", "Essential constituent for the thyroid gland to synthesize thyroxine hormone, regulating basal metabolic rate", "Goitre: Dramatic swelling of the thyroid gland in the neck; Cretinism (mental and physical stunting) in infants"],
                                ["Magnesium (Mg2+) (Plants)", "Soil minerals absorbed by root hairs", "Central coordinating ion in the chlorophyll porphyrin ring for light absorption in photosynthesis", "Chlorosis: Yellowing of plant leaves between veins due to failure to synthesize chlorophyll"]
                            ]
                        }
                    }
                ],
                # Page 6: Blood Micrograph & Haemoglobin Iron Image
                [
                    {
                        "type": "suggested_image",
                        "title": "Scanning Electron Micrograph of Normal Erythrocytes and Haemoglobin Transport",
                        "content": {
                            "description": "Scanning Electron Micrograph (SEM) of normal human red blood cells showing the biconcave disc morphology that carries millions of iron-rich haemoglobin molecules for systemic oxygen delivery.",
                            "caption": "Human red blood cells (erythrocytes) packed with iron-containing haemoglobin; iron deficiency prevents haemoglobin synthesis, causing clinical anaemia."
                        }
                    }
                ],
                # Page 7: Deep Dive Educational Video
                [
                    {
                        "type": "suggested_video",
                        "title": "Deep Dive: Water and Minerals — The Inorganic Chemistry of Life",
                        "content": {
                            "description": "Educational presentation covering the polar properties of water, specific heat capacity, mineral ion physiology, haemoglobin chemistry, and clinical deficiency syndromes."
                        }
                    }
                ],
                # Page 8: Knowledge Check
                [
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Clinical Fatigue & Mineral Deficiency",
                        "content": {
                            "question": "A teenage girl visits a clinic in Marsabit complaining of constant fatigue, dizziness when standing, and pale fingernail beds. She explains that her diet is mostly tea and flatbread. Which mineral ion is she most likely deficient in, and what disorder does she have?",
                            "options": [
                                "Calcium deficiency causing rickets",
                                "Iodine deficiency causing goitre",
                                "Sodium deficiency causing dehydration",
                                "Iron deficiency causing anaemia"
                            ],
                            "correct_answer": "D",
                            "explanation": "Iron is the essential prosthetic element of haemoglobin, which carries oxygen in the bloodstream. A diet deficient in iron prevents sufficient haemoglobin synthesis, resulting in anaemia. Low oxygen delivery to brain and muscle tissues produces chronic fatigue, dizziness, and pallor."
                        }
                    }
                ],
                # Page 9: Summary
                [
                    {
                        "type": "summary",
                        "title": "Lesson Summary: Water & Mineral Physiology",
                        "content": {
                            "title": "Lesson Summary: Water & Mineral Physiology",
                            "points": [
                                "Water serves as the universal solvent, transport medium, thermal buffer, turgor support, and chemical reactant in cells.",
                                "Calcium builds skeletal bone and triggers muscle contraction and blood clotting.",
                                "Iron forms the active core of oxygen-carrying haemoglobin; deficiency causes anaemia.",
                                "Sodium and potassium regulate cellular osmotic balance and electrical nerve impulses.",
                                "Iodine is required for thyroid thyroxine synthesis, preventing goitre."
                            ]
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 4.3: Food Tests for Carbohydrates, Lipids, Proteins, and Vitamin C
        # =====================================================================
        {
            "unit_order": 3,
            "unit_name": "Food Tests for Carbohydrates, Lipids, Proteins, and Vitamin C",
            "unit_description": "Qualitative colorimetric reagents (Iodine, Benedict's + heat, Biuret, Ethanol emulsion, DCPIP), step-by-step protocols, observation vs inference, and laboratory safety.",
            "lesson_title": "Food Tests for Carbohydrates, Lipids, Proteins, and Vitamin C",
            "pages": [
                # Page 1: Introduction & Learning Focus
                [
                    {
                        "type": "learning_goal",
                        "title": "Learning Focus: Qualitative Biochemical Food Tests",
                        "content": {
                            "title": "Learning Focus: Qualitative Biochemical Food Tests",
                            "goals": [
                                "Identify the specific diagnostic chemical reagents used to test for starch, reducing sugars, proteins, lipids, and Vitamin C.",
                                "Describe the step-by-step laboratory procedures and heating methods for food testing.",
                                "Accurately record physical color observations and deduce scientific biological inferences."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Revealing Invisible Nutrients in the Laboratory",
                        "content": {
                            "title": "Revealing Invisible Nutrients in the Laboratory",
                            "text": "If you look at a glass of milk, how do you know what nutrients are inside? You cannot see dissolved proteins or sugars with your naked eye.\n\nAs a biological scientist, you can use specialized chemical reagents that react with specific molecular bonds to produce diagnostic color changes! In this lesson, we master the five core qualitative food tests."
                        }
                    }
                ],
                # Page 2: Key Terms
                [
                    {
                        "type": "definition_card",
                        "title": "Food Testing Reagent Vocabulary",
                        "content": {
                            "term": "Essential Analytical Food Chemistry",
                            "definition": "Key concepts in qualitative colorimetric diagnostic assays.",
                            "key_points": [
                                "Qualitative Test: A chemical assay designed to detect the presence or absence of a target nutrient based on color changes.",
                                "Reagent: A chemical substance of known composition added to a sample to cause a characteristic reaction with target biomolecules.",
                                "Precipitate: An insoluble solid suspension formed out of a clear liquid solution during a chemical reaction.",
                                "Water Bath: A beaker of boiling water used to heat test tubes indirectly, preventing direct contact with open flames.",
                                "DCPIP: Dichlorophenolindophenol, a redox-sensitive deep blue chemical dye that decolorizes (turns clear) when reduced by Vitamin C."
                            ]
                        }
                    }
                ],
                # Page 3: Observation vs Inference & The 5 Qualitative Tests
                [
                    {
                        "type": "concept_explanation",
                        "title": "Distinguishing Scientific Observations from Inferences",
                        "content": {
                            "title": "Distinguishing Scientific Observations from Inferences",
                            "text": "In practical biology exams and laboratory investigations, you must strictly distinguish between:\n\n- **Observation**: What you physically see with your eyes (e.g., *'The clear blue solution turned cloudy green, then yellow, and formed a brick-red precipitate'*).\n- **Inference**: What you logically conclude about the sample (e.g., *'Reducing sugars are present in high concentration'*).\n\nNever write an inference in an observation table, or vice-versa!"
                        }
                    }
                ],
                # Page 4: 5-Tube Food Testing Flow Chart SVG
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Qualitative Food Testing Diagnostic Flow Chart",
                        "content": {
                            "description": "Laboratory flow chart illustrating the 5 diagnostic food tests. Show 5 test tubes containing food samples with reagents added: 1. Iodine -> Blue-black (Starch); 2. Benedict's + boiling water bath -> Brick-red precipitate (Reducing sugars); 3. Biuret (NaOH + CuSO4) -> Purple/Violet (Proteins); 4. Ethanol + Water -> Cloudy white emulsion (Lipids); 5. DCPIP dropwise -> Blue dye decolorizes clear (Vitamin C).",
                            "caption": "Diagnostic colorimetric reactions for identifying carbohydrates, lipids, proteins, and Vitamin C."
                        }
                    }
                ],
                # Page 5: Step-by-Step Food Test Protocols
                [
                    {
                        "type": "comparison_table",
                        "title": "Summary of Qualitative Food Testing Protocols",
                        "content": {
                            "headers": ["Target Nutrient", "Diagnostic Chemical Reagent", "Specific Procedure & Heating Conditions", "Positive Physical Observation", "Negative Physical Observation"],
                            "rows": [
                                ["Starch", "Iodine Solution", "Add 2-3 drops of brown-yellow Iodine directly to cold food sample on white tile or tube", "Turns deep **Blue-Black**", "Remains brown-yellow (no color change)"],
                                ["Reducing Sugars (Glucose, Fructose, Maltose)", "Benedict's Solution (Alkaline Copper Sulfate)", "Add equal volume of Benedict's reagent; **MUST heat in boiling water bath for 3–5 minutes**", "Blue $\\rightarrow$ Green $\\rightarrow$ Yellow $\\rightarrow$ Orange $\\rightarrow$ **Brick-Red Precipitate**", "Remains clear Blue"],
                                ["Proteins", "Biuret Reagent (or NaOH + 1% CuSO4)", "Add 2 cm³ of 10% NaOH to food slurry, then add 2–3 drops of 1% CuSO4 dropwise with shaking", "Turns distinct **Purple / Violet**", "Remains light Blue"],
                                ["Lipids (Fats & Oils)", "Ethanol Emulsion Test", "Dissolve food in 2 cm³ ethanol, shake vigorously, then pour clear ethanol extract into clean water", "Forms a **Cloudy Milky-White Emulsion**", "Remains clear transparent solution"],
                                ["Vitamin C (Ascorbic Acid)", "DCPIP Solution (0.1%)", "Place 1 cm³ of blue DCPIP in tube; add fruit juice drop-by-drop using a dropper, counting drops", "Blue DCPIP dye **Decolorizes completely clear**", "Blue DCPIP dye remains dark blue"]
                            ]
                        }
                    }
                ],
                # Page 6: Practical Investigation: Unknown Slurry Analysis
                [
                    {
                        "type": "step_process",
                        "title": "Practical Protocol: Qualitative Analysis of an Unknown Food Slurry",
                        "content": {
                            "title": "Practical Protocol: Qualitative Analysis of an Unknown Food Slurry",
                            "steps": [
                                {
                                    "step_number": 1,
                                    "title": "Tube A (Starch Test)",
                                    "description": "Place 2 cm³ of slurry in Tube A. Add 3 drops of iodine solution. Result: Turns Blue-Black -> Inference: Starch is present."
                                },
                                {
                                    "step_number": 2,
                                    "title": "Tube B (Reducing Sugar Test)",
                                    "description": "Place 2 cm³ of slurry in Tube B. Add 2 cm³ Benedict's. Heat in boiling water bath 5 mins. Result: Brick-Red precipitate -> Inference: Reducing sugars present."
                                },
                                {
                                    "step_number": 3,
                                    "title": "Tube C (Protein Test)",
                                    "description": "Place 2 cm³ of slurry in Tube C. Add 2 cm³ NaOH + 3 drops CuSO4. Result: Turns Purple -> Inference: Protein is present."
                                },
                                {
                                    "step_number": 4,
                                    "title": "Tube D (Lipid Test)",
                                    "description": "Add 2 cm³ ethanol to sample, shake, and decant into water. Result: Remains clear -> Inference: Lipids are absent."
                                },
                                {
                                    "step_number": 5,
                                    "title": "Tube E (Vitamin C Test)",
                                    "description": "Add slurry drops to 1 cm³ blue DCPIP. Result: Blue dye remains blue -> Inference: Vitamin C is absent."
                                }
                            ]
                        }
                    }
                ],
                # Page 7: Diagnostic Food Test Results Image
                [
                    {
                        "type": "suggested_image",
                        "title": "Diagnostic Biochemical Food Test Color Results",
                        "content": {
                            "description": "High-clarity photograph of laboratory test tubes showing positive food test results: blue-black starch iodine test, brick-red reducing sugar Benedict's test, purple protein Biuret test, and cloudy white lipid emulsion.",
                            "caption": "Diagnostic colorimetric reactions: Benedict's brick-red precipitate, Biuret purple protein reaction, and Iodine blue-black starch complex."
                        }
                    }
                ],
                # Page 8: Laboratory Safety Protocols
                [
                    {
                        "type": "callout",
                        "title": "Critical Laboratory Safety Protocols in Food Testing",
                        "content": {
                            "title": "Critical Laboratory Safety Protocols in Food Testing",
                            "text": "- **Flammable Ethanol**: Ethanol catches fire instantly. **NEVER heat ethanol test tubes directly over a Bunsen burner flame!** Always heat ethanol tubes inside an indirect hot water bath with the burner turned off.\n- **Corrosive Caustic Alkali**: Sodium Hydroxide (NaOH) used in the Biuret test is highly corrosive to skin and eyes. Wear protective safety goggles and flush accidental spills immediately with cold tap water.\n- **Hot Water Baths**: Always use wooden test tube clamps when inserting or retrieving glassware from boiling water baths."
                        }
                    }
                ],
                # Page 9: Deep Dive Educational Video
                [
                    {
                        "type": "suggested_video",
                        "title": "Deep Dive: Qualitative Food Tests — Benedict's, Biuret, Iodine, Ethanol, and DCPIP",
                        "content": {
                            "description": "Laboratory demonstration showing the step-by-step execution of the 5 qualitative food tests, water bath heating techniques, and observation-to-inference deductions."
                        }
                    }
                ],
                # Page 10: Knowledge Check & Summary
                [
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Thermal Energy in Benedict's Test",
                        "content": {
                            "question": "A student wants to test if a slice of ripe mango contains reducing sugars. They crush the mango, add Benedict's solution, and leave the test tube standing on their lab bench. After 10 minutes, they observe that the mixture remains blue and conclude that mangoes contain no reducing sugars. Why is their investigation and conclusion scientifically invalid?",
                            "options": [
                                "Mangoes contain starch, which interferes with the Benedict's test.",
                                "Ripe fruits only contain non-reducing sucrose, which requires an acid hydrolysis test.",
                                "Benedict's test requires thermal energy to drive the chemical reduction of copper (II) ions; without heating in a boiling water bath, the solution will remain blue even when sugars are abundant.",
                                "The student should have added Sodium Hydroxide first to activate the Benedict's reagent."
                            ],
                            "correct_answer": "C",
                            "explanation": "The reduction of copper (II) ions to copper (I) oxide precipitate in Benedict's test is a heat-dependent reaction. Without heating the reaction mixture in a boiling water bath for 3–5 minutes, no color change occurs, producing a false-negative result."
                        }
                    },
                    {
                        "type": "summary",
                        "title": "Lesson Summary: Qualitative Food Tests",
                        "content": {
                            "title": "Lesson Summary: Qualitative Food Tests",
                            "points": [
                                "Iodine detects starch by producing a blue-black coloration.",
                                "Benedict's solution + boiling water bath identifies reducing sugars by forming a brick-red precipitate.",
                                "Biuret reagent (NaOH + $CuSO_4$) tests for proteins, turning purple/violet.",
                                "Ethanol emulsion test identifies lipids by forming a cloudy white suspension upon dilution with water.",
                                "DCPIP decolorizes from dark blue to clear in the presence of Vitamin C."
                            ]
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 4.4: Enzymes, Catalase, and Factors Affecting Activity
        # =====================================================================
        {
            "unit_order": 4,
            "unit_name": "Enzymes, Catalase, and Factors Affecting Activity",
            "unit_description": "Enzyme catalytic mechanisms (lock-and-key model, active site, activation energy), catalase in living tissues (H2O2 breakdown), and rate kinetic curves (temperature, pH, concentration).",
            "lesson_title": "Enzymes, Catalase, and Factors Affecting Activity",
            "pages": [
                # Page 1: Introduction & Learning Focus
                [
                    {
                        "type": "learning_goal",
                        "title": "Learning Focus: Enzyme Action & Catalase Kinetics",
                        "content": {
                            "title": "Learning Focus: Enzyme Action & Catalase Kinetics",
                            "goals": [
                                "Explain the catalytic mechanism of enzyme action using the lock-and-key model.",
                                "Describe the physiological role and presence of catalase in living animal and plant tissues.",
                                "Analyze and interpret enzyme rate curves governing temperature, pH, and substrate/enzyme concentrations."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Biological Accelerators of Cellular Life",
                        "content": {
                            "title": "Biological Accelerators of Cellular Life",
                            "text": "Right now, inside every one of your cells, thousands of chemical reactions are occurring every second. If we tried to perform these reactions on a lab bench without catalysts, they would run so slowly that life would be impossible.\n\nTo drive metabolic speed, life uses remarkable protein catalysts called **enzymes**. In this lesson, we explore how these molecular keys unlock reactions and investigate the environmental factors that govern their speed."
                        }
                    }
                ],
                # Page 2: Key Terms
                [
                    {
                        "type": "definition_card",
                        "title": "Enzyme Kinetics Vocabulary",
                        "content": {
                            "term": "Essential Enzymology Terminology",
                            "definition": "Key concepts governing biological catalysis and protein kinetics.",
                            "key_points": [
                                "Enzyme: A biological catalyst composed of protein that accelerates metabolic reactions by lowering activation energy without being altered or consumed.",
                                "Substrate: The specific reactant molecule that binds to and is chemically converted by an enzyme.",
                                "Active Site: The specialized 3D cleft or pocket on an enzyme where the substrate binds.",
                                "Activation Energy: The minimum threshold energy required to initiate a chemical reaction.",
                                "Catalase: A vital antioxidant enzyme in living tissues that degrades toxic hydrogen peroxide ($H_2O_2$) into water and oxygen gas.",
                                "Optimum Temperature/pH: The specific environmental temperature or pH at which an enzyme operates at its maximum velocity ($V_{max}$)."
                            ]
                        }
                    }
                ],
                # Page 3: Lock-and-Key Model of Catalysis
                [
                    {
                        "type": "step_process",
                        "title": "The Four Stages of the Lock-and-Key Catalytic Mechanism",
                        "content": {
                            "title": "The Four Stages of the Lock-and-Key Catalytic Mechanism",
                            "steps": [
                                {
                                    "step_number": 1,
                                    "title": "Substrate Approach & Complementary Fit",
                                    "description": "The substrate molecule collides with the enzyme. Its 3D molecular shape is complementary to the enzyme's uniquely shaped active site."
                                },
                                {
                                    "step_number": 2,
                                    "title": "Enzyme-Substrate Complex Formation",
                                    "description": "The substrate binds snugly into the active site, forming a temporary Enzyme-Substrate Complex. Chemical bonds within the substrate are strained."
                                },
                                {
                                    "step_number": 3,
                                    "title": "Catalytic Cleavage / Synthesis",
                                    "description": "The enzyme dramatically lowers the activation energy barrier, converting the substrate into reaction products."
                                },
                                {
                                    "step_number": 4,
                                    "title": "Product Release & Enzyme Recycling",
                                    "description": "Products leave the active site. The enzyme remains completely unchanged and immediately available to capture another substrate molecule."
                                }
                            ]
                        }
                    }
                ],
                # Page 4: Lock-and-Key Catalysis & 3-Panel Kinetics SVG
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Enzyme Lock-and-Key Catalysis & Kinetic Response Curves",
                        "content": {
                            "description": "Comprehensive enzyme diagram. Top panel: 4-stage lock-and-key catalytic mechanism showing enzyme active site, substrate binding, enzyme-substrate complex, product release, and unchanged enzyme recycling. Bottom panel: 3 kinetic response curves: 1. Temperature curve (rising to 37°C optimum, steep plunge above 50°C due to denaturation); 2. pH curves (narrow optimum bell-curves contrasting Pepsin at pH 2 vs Amylase at pH 7); 3. Substrate concentration curve (initial linear rise plateauing at Vmax saturation).",
                            "caption": "Biochemical catalytic cycle and environmental kinetic response curves governing enzyme activity."
                        }
                    }
                ],
                # Page 5: Environmental Factors Governing Enzyme Kinetics
                [
                    {
                        "type": "comparison_table",
                        "title": "Environmental Factors Governing Enzyme Reaction Rates",
                        "content": {
                            "headers": ["Environmental Factor", "Low Condition Effect", "Optimum Condition Peak", "Extreme Condition Effect & Denaturation Mechanism"],
                            "rows": [
                                ["Temperature", "Low kinetic energy slows molecule movement; few collisions -> very slow reaction rate", "Optimum (~37–40°C in humans): Maximum collision frequency between substrates and active sites", "High heat (>50°C) causes excessive thermal vibration; breaks weak hydrogen bonds, altering active site shape permanently (Denaturation -> 0 rate)"],
                                ["pH (Acidity / Alkalinity)", "Extreme acidity disrupts ionic charges on active site, altering 3D shape -> Denaturation", "Each enzyme has a specific optimum (Pepsin in stomach: pH 2; Salivary amylase: pH 7; Trypsin in duodenum: pH 8)", "Extreme alkalinity disrupts ionic bonding, denaturing enzyme -> symmetrical bell-shaped rate curve dropping to zero on either side"],
                                ["Substrate Concentration", "Rate is slow because many active sites remain vacant", "Rate rises steadily as more active sites are engaged", "Plateaus at maximum velocity ($V_{max}$) when ALL enzyme active sites are continuously saturated (enzyme concentration becomes limiting)"]
                            ]
                        }
                    }
                ],
                # Page 6: Practical Investigation: Catalase Effervescence
                [
                    {
                        "type": "step_process",
                        "title": "Practical Protocol: Investigating Catalase in Living Tissues",
                        "content": {
                            "title": "Practical Protocol: Investigating Catalase in Living Tissues",
                            "steps": [
                                {
                                    "step_number": 1,
                                    "title": "Tissue Preparation",
                                    "description": "Cut four equal cubes (1 cm³) of fresh liver and Irish potato. Leave two raw; boil the other two in boiling water for 10 minutes."
                                },
                                {
                                    "step_number": 2,
                                    "title": "Raw Liver (Tube A)",
                                    "description": "Add raw liver to 3 cm³ of hydrogen peroxide ($H_2O_2$). Observation: Immediate, violent effervescence. Thick foam relights a glowing splint (Oxygen gas evolved)."
                                },
                                {
                                    "step_number": 3,
                                    "title": "Boiled Liver (Tube B)",
                                    "description": "Add boiled liver to $H_2O_2$. Observation: NO reaction / zero effervescence. High heat denatured the catalase enzyme."
                                },
                                {
                                    "step_number": 4,
                                    "title": "Raw vs Boiled Potato (Tubes C & D)",
                                    "description": "Raw potato produces moderate bubbling ($H_2O_2$ breakdown); boiled potato produces zero bubbling due to denaturation."
                                }
                            ]
                        }
                    },
                    {
                        "type": "callout",
                        "title": "Biochemical Equation of Catalase Action",
                        "content": {
                            "title": "Biochemical Equation of Catalase Action",
                            "text": "$$2\\text{H}_2\\text{O}_2\\text{ (toxic)} \\xrightarrow{\\text{Catalase}} 2\\text{H}_2\\text{O} + \\text{O}_2\\text{ (gas)}$$\nCatalase protects living cells by converting toxic hydrogen peroxide metabolic byproducts into harmless water and oxygen."
                        }
                    }
                ],
                # Page 7: Catalase Effervescence Image
                [
                    {
                        "type": "suggested_image",
                        "title": "Catalase Effervescence & Oxygen Gas Evolution in Living Tissues",
                        "content": {
                            "description": "Laboratory photograph showing active foaming effervescence when hydrogen peroxide is added to fresh liver tissue, alongside a boiled control tube showing zero reaction.",
                            "caption": "Catalase enzymatic breakdown of hydrogen peroxide produces oxygen gas foam in raw tissues, whereas boiling denatures the enzyme, halting gas evolution."
                        }
                    }
                ],
                # Page 8: Deep Dive Educational Video
                [
                    {
                        "type": "suggested_video",
                        "title": "Deep Dive: Enzymes, Catalase, and Factors Affecting Reaction Rates",
                        "content": {
                            "description": "Comprehensive video guide covering the lock-and-key model, activation energy barriers, catalase laboratory practicals, and temperature/pH kinetic response curves."
                        }
                    }
                ],
                # Page 9: Knowledge Check
                [
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Salivary Amylase Temperature Responses",
                        "content": {
                            "question": "A student extracts salivary amylase (an enzyme that digests starch in the mouth) and mixes it with starch in three test tubes. Tube X is kept at 10°C, Tube Y is kept at 37°C, and Tube Z is kept at 80°C. After 30 minutes, they test each tube for starch using iodine. Which set of results and explanations should they expect?",
                            "options": [
                                "Tube X: Blue-black (denatured); Tube Y: Blue-black (digested); Tube Z: Brown (low energy).",
                                "Tube X: Brown (digested); Tube Y: Blue-black (no digestion); Tube Z: Brown (digested).",
                                "Tube X: Blue-black (starch remains because low kinetic energy slowed reactions); Tube Y: Brown (starch digested because temperature was at the optimum); Tube Z: Blue-black (starch remains because the high heat of 80°C permanently denatured the enzyme).",
                                "All tubes turn blue-black because amylase only works in acidic conditions."
                            ],
                            "correct_answer": "C",
                            "explanation": "At 10°C (Tube X), low kinetic energy slows molecular collisions, leaving starch undigested (positive blue-black iodine test). At 37°C (Tube Y), the enzyme is at its optimum temperature and hydrolyzes starch completely into sugars (negative brown iodine test). At 80°C (Tube Z), high thermal energy permanently denatures the enzyme's active site, preventing digestion (positive blue-black iodine test)."
                        }
                    }
                ],
                # Page 10: Summary
                [
                    {
                        "type": "summary",
                        "title": "Lesson Summary: Enzymes & Kinetics",
                        "content": {
                            "title": "Lesson Summary: Enzymes & Kinetics",
                            "points": [
                                "Enzymes are specific protein catalysts that lower activation energy via a lock-and-key active site mechanism.",
                                "Catalase degrades toxic hydrogen peroxide into water and oxygen gas ($2H_2O_2 \\rightarrow 2H_2O + O_2$).",
                                "Reaction rates increase with temperature up to an optimum (~37–40°C), then plunge abruptly due to thermal denaturation.",
                                "Enzymes operate within narrow optimum pH windows; extreme pH disrupts ionic charges and causes denaturation.",
                                "Substrate concentration increases reaction velocity until all active sites reach $V_{max}$ saturation."
                            ]
                        }
                    }
                ]
            ]
        }
    ]

def ingest_grade10_biology_topic4(replace=False):
    """Executes the database ingestion for Grade 10 Biology Topic 4."""
    print("=" * 80)
    print("VLearn Grade 10 Biology — Ingestion Engine")
    print("Topic 4: Chemicals of Life (CBC Curriculum ID: 5)")
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

    # 4. Resolve Topic 4
    topic_name = "Chemicals of Life"
    topic = Topic.objects.filter(subject=subject, name=topic_name).first()

    if topic and replace:
        print(f"[*] Found existing Topic '{topic_name}' (ID: {topic.id}). Performing clean replacement of child units/lessons...")
        topic.learning_units.all().delete()
        topic.lessons.all().delete()
    elif not topic:
        topic = Topic.objects.create(
            subject=subject,
            name=topic_name,
            order=4,
            description="Comprehensive syllabus on organic biomolecules (carbohydrates, lipids, proteins, vitamins), inorganic cellular constituents (water, minerals), qualitative food testing, and enzyme kinetics (lock-and-key, catalase, limiting factors)."
        )
        print(f"[+] Created Topic: {topic.name} (ID: {topic.id})")
    else:
        print(f"[*] Using existing Topic: {topic.name} (ID: {topic.id})")

    curriculum_data = build_topic4_curriculum()
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
    print("[SUCCESS] Grade 10 Biology Topic 4 Ingestion Complete!")
    print(f"[*] Total Lessons Ingested: {total_lessons}")
    print(f"[*] Total Pages/Cards:      {total_pages}")
    print(f"[*] Total Blocks Created:   {total_blocks}")
    print("=" * 80)

if __name__ == "__main__":
    replace_flag = "--replace" in sys.argv
    ingest_grade10_biology_topic4(replace=replace_flag)
