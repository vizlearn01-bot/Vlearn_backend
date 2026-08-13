"""
VLearn Form 4 Biology — Topic 2: Evolution
High-Structure Production Ingestion Engine

Topic: Evolution (Topic Order: 2)
Subject: Biology (Subject ID: 13)
Grade: Form 4 (Grade ID: 4)
Curriculum: 844 (Curriculum ID: 4)

Decomposed into 8 Learning Units & 8 Published Lessons (93 Total Pages):
  1. Introduction to Organic Evolution and Views on the Origin of Life (11 Pages)
  2. The Step-by-Step Chemical Evolution Pathway from Prebiotic Gases to Cells (9 Pages)
  3. Palaeontological Stratigraphy, Hominid Evolution, and Biogeography (13 Pages)
  4. Homology, Analogy, Vestigial Structures, Cytology, and Serology (17 Pages)
  5. Lamarck's Hypotheses versus Darwin's Theory of Natural Selection (12 Pages)
  6. Industrial Melanism, Antibiotic and Pesticide Resistance, and Speciation (16 Pages)
  7. Comparative Limb and Wing Laboratory Investigations and Field Study (8 Pages)
  8. Evolutionary Synthesis, Key Glossary, Misconceptions, and Examination Diagnostic (7 Pages)

Usage:
  ./venv/bin/python curriculum/ingest_form4_biology_topic2.py [--replace]
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
    """Removes bracket citations and cleans double spaces."""
    if not text:
        return ""
    text = re.sub(r'\[(?:\d+|image_\d+|S\d+.*?|[\d,\s]+)\]', '', text)
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

def build_topic2_curriculum():
    """Returns the comprehensive pedagogical page and block structure for Topic 2: Evolution."""
    return [
        # =====================================================================
        # LESSON 1: Introduction to Organic Evolution and Views on the Origin of Life
        # =====================================================================
        {
            "unit_order": 1,
            "unit_name": "Introduction to Organic Evolution and Views on the Origin of Life",
            "unit_description": "Meaning of evolution, special creation vs chemical vs organic evolution, prebiotic Earth conditions, and disproof of spontaneous generation.",
            "lesson_title": "Introduction to Organic Evolution and Views on the Origin of Life",
            "pages": [
                # Page 1
                [
                    {
                        "type": "learning_goal",
                        "title": "Learning Objectives: Origin of Life & Evolution",
                        "content": {
                            "title": "Learning Objectives: Origin of Life & Evolution",
                            "goals": [
                                "Define evolution, distinguishing between chemical evolution and organic evolution.",
                                "Examine historical hypotheses regarding the origin of life (Special Creation, Cosmozoan, Chemical Evolution).",
                                "Describe the primeval environmental conditions of early Earth (reducing atmosphere).",
                                "Explain experiments disproving spontaneous generation (Redi, Spallanzani, Pasteur)."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Welcome to Form 4 Biology: Topic 2 Evolution",
                        "content": {
                            "title": "Welcome to Form 4 Biology: Topic 2 Evolution",
                            "text": "Evolution is the continuous process by which living organisms undergo gradual structural, physiological, and behavioral changes over successive generations, resulting in the emergence of new species from ancestral forms."
                        }
                    }
                ],
                # Page 2
                [
                    {
                        "type": "definition_card",
                        "title": "Core Evolution Taxonomy",
                        "content": {
                            "term": "Evolution Definitions Taxonomy",
                            "definition": "Biological process leading to modern biodiversity over geological timescales.",
                            "key_points": [
                                "Organic Evolution: Gradual change of living organisms over time resulting in complex new species.",
                                "Chemical Evolution: Synthesis of organic molecules from inorganic prebiotic gases in primitive oceans.",
                                "Special Creation: Belief that life was created in its present form by a supernatural entity."
                            ]
                        }
                    }
                ],
                # Page 3
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Timeline of Earth & Origin of Life Milestones",
                        "content": {
                            "title": "Timeline of Earth & Origin of Life Milestones",
                            "caption": "Geological Timeline: 4.6 Billion Years Ago (Earth Formation) → 3.8 BYA (Prebiotic Soup) → 3.5 BYA (First Prokaryotes) → Modern Biodiversity",
                            "description": "Linear timeline showing 4.6 BYA Earth, 3.8 BYA Chemical evolution, 3.5 BYA Prokaryotes, 1.5 BYA Eukaryotes, 500 MYA Vertebrates."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Primeval Atmosphere of Early Earth",
                        "content": {
                            "title": "Primeval Atmosphere of Early Earth",
                            "text": "Early Earth possessed a reducing atmosphere devoid of free oxygen gas ($O_2$). It consisted of water vapor ($H_2O$), methane ($CH_4$), ammonia ($NH_3$), and hydrogen ($H_2$). Intense volcanic eruptions, lightning, and cosmic UV radiation provided the energy required for chemical reactions."
                        }
                    }
                ],
                # Page 4
                [
                    {
                        "type": "concept_explanation",
                        "title": "Disproof of Spontaneous Generation",
                        "content": {
                            "title": "Disproof of Spontaneous Generation",
                            "text": "For centuries, people believed in abiogenesis (spontaneous generation — that life arose spontaneously from non-living matter like maggots from decaying meat). Francesco Redi and Louis Pasteur disproved this with swan-neck flask experiments, establishing the Law of Biogenesis: *Omne vivum ex vivo* (all life comes from pre-existing life)."
                        }
                    },
                    {
                        "type": "callout",
                        "title": "Key Concept: Prebiotic Reducing Atmosphere",
                        "content": {
                            "type": "tip",
                            "title": "Key Concept: Prebiotic Reducing Atmosphere",
                            "text": "Free oxygen ($O_2$) would have oxidized and destroyed fragile organic monomers before they could polymerize. The absence of free oxygen was essential for prebiotic chemical evolution."
                        }
                    }
                ],
                # Page 5
                [
                    {
                        "type": "suggested_image",
                        "title": "Prebiotic Molecular Vector Model",
                        "content": {
                            "title": "Prebiotic Molecular Vector Model",
                            "caption": "Diagrammatic representation of a circular bacterial plasmid vector used in recombinant DNA and molecular evolution studies.",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/d/da/Making_of_a_DNA_vaccine.jpg",
                            "author": "Public Domain, Wikimedia Commons",
                            "licensing": "Public domain",
                            "commons_page_url": "https://commons.wikimedia.org/wiki/File:Making_of_a_DNA_vaccine.jpg"
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Hypotheses on the Origin of Life",
                        "content": {
                            "title": "Hypotheses on the Origin of Life",
                            "text": "1. Special Creation: Life created instantaneously by a deity.\n2. Cosmozoan (Panspermia): Spores of life arrived on Earth via meteorites.\n3. Chemical Evolution (Oparin-Haldane Hypothesis): Life originated spontaneously via step-by-step chemical reactions in primordial seas."
                        }
                    }
                ],
                # Page 6
                [
                    {
                        "type": "comparison_table",
                        "title": "Comparison Matrix: Theories on the Origin of Life",
                        "content": {
                            "headers": ["Hypothesis", "Core Premise", "Scientific Testability"],
                            "rows": [
                                ["Special Creation", "Created in present form by divine supernatural power", "Untestable by empirical scientific methods"],
                                ["Cosmozoan (Panspermia)", "Microscopic spores transported to Earth via meteorites", "Partially supported by organic matter in meteorites"],
                                ["Chemical Evolution", "Inorganic gases -> Organic monomers -> Macromolecules -> Protocells", "Empirically supported by Miller-Urey experiment"]
                            ]
                        }
                    }
                ],
                # Page 7
                [
                    {
                        "type": "common_mistake",
                        "title": "Common Student Traps: Defining Evolution",
                        "content": {
                            "mistake": "Stating that evolution means humans evolved directly from modern monkeys.",
                            "correction": "Humans and modern apes share a common ancestral hominid; humans did not evolve from modern monkeys.",
                            "reasoning": "Evolution acts via branching lineages from common ancestors, not direct metamorphosis of modern species into others."
                        }
                    }
                ],
                # Page 8
                [
                    {
                        "type": "mini_activity",
                        "title": "Interactive Origin of Life Classification Simulator",
                        "content": {
                            "activity_type": "scenario_decision",
                            "title": "Interactive Origin of Life Classification Simulator",
                            "prompt": "Which gas was completely absent in the primeval atmosphere of early Earth, allowing organic molecules to accumulate without oxidation?",
                            "options": [
                                "Option A: Free Oxygen (O2).",
                                "Option B: Methane (CH4).",
                                "Option C: Ammonia (NH3)."
                            ],
                            "correct_option": "Option A: Free Oxygen (O2).",
                            "explanation": "Free oxygen was absent in early Earth's reducing atmosphere."
                        }
                    }
                ],
                # Page 9
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Checkpoint: Meaning of Evolution",
                        "content": {
                            "question": "Which scientist conclusively disproved the hypothesis of spontaneous generation using swan-neck flask experiments?",
                            "options": [
                                "Louis Pasteur",
                                "Charles Darwin",
                                "Jean-Baptiste Lamarck",
                                "Gregor Mendel"
                            ],
                            "correct_answer": 0,
                            "explanation": "Louis Pasteur used swan-neck flasks to prove micro-organisms enter from air, disproving spontaneous generation."
                        }
                    }
                ],
                # Page 10
                [
                    {
                        "type": "summary",
                        "title": "Origin of Life: Key Takeaways",
                        "content": {
                            "title": "Origin of Life: Key Takeaways",
                            "summary_points": [
                                "Organic evolution is the gradual development of modern species from simpler ancestral forms.",
                                "Early Earth had a reducing atmosphere (CH4, NH3, H2O, H2) lacking free O2 gas.",
                                "Louis Pasteur disproved spontaneous generation, proving life comes from pre-existing life.",
                                "Chemical evolution explains how simple inorganic gases formed organic monomers in primeval seas."
                            ]
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 2: The Step-by-Step Chemical Evolution Pathway from Prebiotic Gases to Cells
        # =====================================================================
        {
            "unit_order": 2,
            "unit_name": "The Step-by-Step Chemical Evolution Pathway from Prebiotic Gases to Cells",
            "unit_description": "Miller-Urey experiment, prebiotic synthesis of monomers, polymerization into coacervates, RNA world hypothesis, and first protocells.",
            "lesson_title": "The Step-by-Step Chemical Evolution Pathway from Prebiotic Gases to Cells",
            "pages": [
                # Page 1
                [
                    {
                        "type": "learning_goal",
                        "title": "Learning Objectives: Chemical Evolution",
                        "content": {
                            "title": "Learning Objectives: Chemical Evolution",
                            "goals": [
                                "Detail the 4-stage Oparin-Haldane chemical evolution model.",
                                "Explain Stanley Miller & Harold Urey's 1953 laboratory synthesis of amino acids.",
                                "Describe coacervate droplet formation and membrane encapsulation.",
                                "Outline the RNA World hypothesis for self-replicating molecular heredity."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The Oparin-Haldane Hypothesis",
                        "content": {
                            "title": "The Oparin-Haldane Hypothesis",
                            "text": "In the 1920s, Alexander Oparin and J.B.S. Haldane independently proposed that life arose through gradual chemical evolution in the primeval 'hot dilute soup' of prebiotic oceans."
                        }
                    }
                ],
                # Page 2
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Miller-Urey Prebiotic Atmospheric Synthesis Apparatus",
                        "content": {
                            "title": "Miller-Urey Prebiotic Atmospheric Synthesis Apparatus",
                            "caption": "Laboratory Apparatus Blueprint: Boiling Flask (H2O) → Gas Chamber (CH4, NH3, H2) → Electric Spark Gap (Lightning) → Condenser → Amino Acid Trap",
                            "description": "Diagram of Miller-Urey apparatus showing glass tubing, boiling water, gas chamber with electrodes producing sparks, condenser, and U-trap collecting amino acids."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The Miller-Urey Experiment (1953)",
                        "content": {
                            "title": "The Miller-Urey Experiment (1953)",
                            "text": "Stanley Miller and Harold Urey tested chemical evolution in a closed glass apparatus:\n1. Circulated gases ($CH_4, NH_3, H_2O, H_2$);\n2. Applied electric sparks (simulating lightning);\n3. Cooled vapor in a condenser;\n4. Result: Within one week, 15% of carbon formed organic monomers, including amino acids (glycine, alanine) and organic acids, proving organic molecules synthesize spontaneously under prebiotic conditions."
                        }
                    }
                ],
                # Page 3
                [
                    {
                        "type": "concept_explanation",
                        "title": "Polymerization & Coacervate Droplets",
                        "content": {
                            "title": "Polymerization & Coacervate Droplets",
                            "text": "• Polymerization: Monomers dissolved in warm tidal pools concentrated on hot clay minerals, forming polypeptides and nucleic acid chains.\n• Coacervates: Macromolecules aggregated into microscopic spherical droplets surrounded by a water shell (coacervate droplets) capable of absorbing nutrients."
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Coacervate Droplet & Protocell Membrane Formation",
                        "content": {
                            "title": "Coacervate Droplet & Protocell Membrane Formation",
                            "caption": "Microscopic Encapsulation Model: Proteinoid Sphere + Lipid Bilayer Membrane Encapsulating Self-Replicating RNA",
                            "description": "Diagram illustrating macromolecule aggregation into lipid-bounded protocells capable of primitive metabolism."
                        }
                    }
                ],
                # Page 4
                [
                    {
                        "type": "concept_explanation",
                        "title": "The RNA World Hypothesis & First Protocells",
                        "content": {
                            "title": "The RNA World Hypothesis & First Protocells",
                            "text": "RNA was likely the first genetic material because RNA can both store genetic information (like DNA) and act as a catalytic ribozyme enzyme (like proteins). When lipid membranes enclosed self-replicating RNA, the first primitive anaerobic heterotrophic protocells (prokaryotes) emerged 3.5 billion years ago."
                        }
                    }
                ],
                # Page 5
                [
                    {
                        "type": "mini_activity",
                        "title": "Interactive Chemical Evolution Steps Challenge",
                        "content": {
                            "activity_type": "scenario_decision",
                            "title": "Interactive Chemical Evolution Steps Challenge",
                            "prompt": "What key organic building blocks were produced in the Miller-Urey experiment when electric sparks were passed through CH4, NH3, H2O, and H2?",
                            "options": [
                                "Option A: Amino acids and simple organic acids.",
                                "Option B: Complete living bacterial cells.",
                                "Option C: Complex multi-celled organisms."
                            ],
                            "correct_option": "Option A: Amino acids and simple organic acids.",
                            "explanation": "Miller and Urey synthesized organic monomers (amino acids), proving abiotic chemical synthesis."
                        }
                    }
                ],
                # Page 6
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Checkpoint: Chemical Evolution Pathway",
                        "content": {
                            "question": "Why do scientists hypothesize that RNA preceded DNA as the genetic material in early protocells?",
                            "options": [
                                "RNA can store genetic information and act as a catalytic ribozyme enzyme.",
                                "RNA is double-stranded and indestructible.",
                                "RNA requires oxygen to replicate.",
                                "DNA was only invented in 1953."
                            ],
                            "correct_answer": 0,
                            "explanation": "RNA possesses dual capability: informational storage and catalytic enzyme activity (ribozymes)."
                        }
                    }
                ],
                # Page 7
                [
                    {
                        "type": "summary",
                        "title": "Chemical Evolution: Key Takeaways",
                        "content": {
                            "title": "Chemical Evolution: Key Takeaways",
                            "summary_points": [
                                "Chemical evolution progressed: Prebiotic Gases -> Organic Monomers -> Polymers -> Coacervates -> Protocells.",
                                "Miller-Urey experiment proved amino acids synthesize abiotically under spark energy.",
                                "RNA World hypothesis explains early self-replicating genetic systems prior to DNA evolution.",
                                "First living cells were anaerobic, heterotrophic prokaryotes in oxygen-free primordial seas."
                            ]
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 3: Palaeontological Stratigraphy, Hominid Evolution, and Biogeography
        # =====================================================================
        {
            "unit_order": 3,
            "unit_name": "Palaeontological Stratigraphy, Hominid Evolution, and Biogeography",
            "unit_description": "Fossil record, sedimentary rock stratigraphy, radiometric dating, human hominid evolution, continental drift, and Galapagos finch adaptive radiation.",
            "lesson_title": "Palaeontological Stratigraphy, Hominid Evolution, and Biogeography",
            "pages": [
                # Page 1
                [
                    {
                        "type": "learning_goal",
                        "title": "Learning Objectives: Fossils & Biogeography",
                        "content": {
                            "title": "Learning Objectives: Fossils & Biogeography",
                            "goals": [
                                "Explain palaeontology, fossilization mechanics, and sedimentary rock stratigraphy.",
                                "Trace human hominid fossil evolution (Australopithecus to Homo sapiens).",
                                "Analyze biogeographical distribution evidence and continental drift (Pangaea).",
                                "Describe adaptive radiation using Galapagos Darwin's finches."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Palaeontology: The Fossil Record",
                        "content": {
                            "title": "Palaeontology: The Fossil Record",
                            "text": "Palaeontology is the study of fossils — the preserved remains, impressions, or traces of organisms preserved in sedimentary rocks over geological time."
                        }
                    }
                ],
                # Page 2
                [
                    {
                        "type": "suggested_image",
                        "title": "Ammonite Fossil Limestone Stratigraphy",
                        "content": {
                            "title": "Ammonite Fossil Limestone Stratigraphy",
                            "caption": "Preserved Jurassic ammonite fossil embedded in Solnhofen limestone sedimentary rock matrix.",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/5/52/Ammonite_fossil_with_in-situ_aptychi_%28Solnhofen_Limestone%2C_Upper_Jurassic%3B_Bavaria%2C_Germany%29_1_%2836800705542%29.jpg",
                            "author": "CC BY 2.0, Wikimedia Commons",
                            "licensing": "CC BY 2.0",
                            "commons_page_url": "https://commons.wikimedia.org/wiki/File:Ammonite_fossil_with_in-situ_aptychi_%28Solnhofen_Limestone%2C_Upper_Jurassic%3B_Bavaria%2C_Germany%29_1_%2836800705542%29.jpg"
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Geological Stratigraphy & Fossil Layer Deposition",
                        "content": {
                            "title": "Geological Stratigraphy & Fossil Layer Deposition",
                            "caption": "Law of Superposition: Oldest Sedimentary Strata (Simple Invertebrate Fossils at Base) → Youngest Strata (Complex Vertebrates at Surface)",
                            "description": "Cross section diagram of sedimentary rock strata demonstrating older deeper layers containing simple fossils and upper layers containing complex modern fossils."
                        }
                    }
                ],
                # Page 3
                [
                    {
                        "type": "concept_explanation",
                        "title": "Fossilization & Law of Superposition",
                        "content": {
                            "title": "Fossilization & Law of Superposition",
                            "text": "When dead organisms are buried quickly under mud and silt, mineral salts replace organic tissues (petrifaction). According to the Law of Superposition, deeper sedimentary layers are older than upper layers, revealing an evolutionary progression from simple aquatic organisms to complex terrestrial vertebrates."
                        }
                    },
                    {
                        "type": "definition_card",
                        "title": "Limitations of the Fossil Record",
                        "content": {
                            "term": "Palaeontological Gaps",
                            "definition": "The fossil record is incomplete due to soft-bodied organism decay, erosion, and unexcavated strata.",
                            "key_points": [
                                "Soft Tissues: Soft-bodied organisms (jellyfish, worms) decay before fossilizing.",
                                "Geological Distortion: Heat, pressure, and erosion destroy fossils.",
                                "Missing Links: Intermediate ancestral fossils are rare."
                            ]
                        }
                    }
                ],
                # Page 4
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Comparative Hominid Skull Evolution Sequence",
                        "content": {
                            "title": "Comparative Hominid Skull Evolution Sequence",
                            "caption": "Evolutionary Skull Transformation: Australopithecus (450 cc) → Homo habilis (650 cc) → Homo erectus (1000 cc) → Homo sapiens (1400 cc)",
                            "description": "Diagram displaying cranial capacity increase, brow ridge reduction, flatter face, and chin development from Australopithecus to modern human."
                        }
                    },
                    {
                        "type": "suggested_image",
                        "title": "Hominid Skull Replica Evidence",
                        "content": {
                            "title": "Hominid Skull Replica Evidence",
                            "caption": "Museum fossil skull replica of Homo erectus demonstrating prominent brow ridge and intermediate braincase capacity.",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/7/72/Reproducciones_de_cr%C3%A1neos_de_homo_erectus._Museo_Arqueol%C3%B3gico_Nacional_de_Espa%C3%B1a.jpg",
                            "author": "CC BY-SA 4.0, Wikimedia Commons",
                            "licensing": "CC BY-SA 4.0",
                            "commons_page_url": "https://commons.wikimedia.org/wiki/File:Reproducciones_de_cr%C3%A1neos_de_homo_erectus._Museo_Arqueol%C3%B3gico_Nacional_de_Espa%C3%B1a.jpg"
                        }
                    }
                ],
                # Page 5
                [
                    {
                        "type": "concept_explanation",
                        "title": "Hominid Evolutionary Milestones",
                        "content": {
                            "title": "Hominid Evolutionary Milestones",
                            "text": "Human fossil evolution in East Africa (Rift Valley) reveals key trends:\n1. Bipedalism (upright posture);\n2. Increasing cranial capacity (brain size: 450 cc in *Australopithecus* to 1400 cc in *Homo sapiens*);\n3. Reduction in brow ridge and jaw prognathism;\n4. Development of opposable thumbs and tool making."
                        }
                    }
                ],
                # Page 6
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Continental Drift & Adaptive Radiation of Darwin's Finches",
                        "content": {
                            "title": "Continental Drift & Adaptive Radiation of Darwin's Finches",
                            "caption": "Adaptive Radiation Model: Common Ancestral Seed-Eating Finch Branching into Insect-Eating, Cactus-Eating, and Seed-Crushing Beak Morphs",
                            "description": "Diagram illustrating ancestral finch arriving in Galapagos and diversifying into distinct ecological niches."
                        }
                    },
                    {
                        "type": "suggested_image",
                        "title": "Galapagos Darwin's Finches Adaptive Radiation",
                        "content": {
                            "title": "Galapagos Darwin's Finches Adaptive Radiation",
                            "caption": "Historical illustration of Darwin's Galapagos finches displaying varied beak adaptations suited for different food sources.",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/5/50/Darwin%27s_finches.png",
                            "author": "Public Domain, Wikimedia Commons",
                            "licensing": "Public domain",
                            "commons_page_url": "https://commons.wikimedia.org/wiki/File:Darwin%27s_finches.png"
                        }
                    }
                ],
                # Page 7
                [
                    {
                        "type": "concept_explanation",
                        "title": "Biogeography & Adaptive Radiation",
                        "content": {
                            "title": "Biogeography & Adaptive Radiation",
                            "text": "• Biogeography: Study of geographical distribution of plants and animals across continents.\n• Continental Drift: Supercontinent Pangaea broke apart; isolated continents developed unique flora/fauna (e.g., Australian marsupials).\n• Adaptive Radiation: Diversification of a common ancestral species into different ecological niches (e.g., Galapagos finches developing distinct beak shapes for seeds, insects, and cacti)."
                        }
                    }
                ],
                # Page 8
                [
                    {
                        "type": "mini_activity",
                        "title": "Interactive Fossil & Biogeography Simulator",
                        "content": {
                            "activity_type": "scenario_decision",
                            "title": "Interactive Fossil & Biogeography Simulator",
                            "prompt": "What major evolutionary trend is observed when comparing skulls from Australopithecus to Homo habilis, Homo erectus, and Homo sapiens?",
                            "options": [
                                "Option A: Progressive increase in cranial capacity (brain size) and flatter facial profile.",
                                "Option B: Progressive enlargement of canine teeth.",
                                "Option C: Decrease in brain size."
                            ],
                            "correct_option": "Option A: Progressive increase in cranial capacity (brain size) and flatter facial profile.",
                            "explanation": "Hominid fossil skulls show a brain size increase from 450 cc to 1400 cc."
                        }
                    }
                ],
                # Page 9
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Checkpoint: Fossils & Biogeography",
                        "content": {
                            "question": "What evolutionary term describes the rapid diversification of a single ancestral species into multiple specialized forms adapted to different ecological niches?",
                            "options": [
                                "Adaptive Radiation",
                                "Convergent Evolution",
                                "Industrial Melanism",
                                "Special Creation"
                            ],
                            "correct_answer": 0,
                            "explanation": "Adaptive radiation occurs when an ancestral species diversifies into varied niches (e.g., Darwin's finches)."
                        }
                    }
                ],
                # Page 10
                [
                    {
                        "type": "summary",
                        "title": "Palaeontology & Biogeography: Key Takeaways",
                        "content": {
                            "title": "Palaeontology & Biogeography: Key Takeaways",
                            "summary_points": [
                                "Palaeontology studies fossils in sedimentary rock strata (older deeper, younger upper).",
                                "Hominid evolution shows bipedalism and brain size increase (450 cc to 1400 cc).",
                                "Biogeography & continental drift explain unique island/continental fauna.",
                                "Adaptive radiation produces diverse specialized species from a common ancestor (Galapagos finches)."
                            ]
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 4: Homology, Analogy, Vestigial Structures, Cytology, and Serology
        # =====================================================================
        {
            "unit_order": 4,
            "unit_name": "Homology, Analogy, Vestigial Structures, Cytology, and Serology",
            "unit_description": "Homologous structures (pentadactyl limb), analogous structures, vestigial organs, comparative embryology, cell biology, and serological antigen-antibody testing.",
            "lesson_title": "Homology, Analogy, Vestigial Structures, Cytology, and Serology",
            "pages": [
                # Page 1
                [
                    {
                        "type": "learning_goal",
                        "title": "Learning Objectives: Comparative Evidence",
                        "content": {
                            "title": "Learning Objectives: Comparative Evidence",
                            "goals": [
                                "Distinguish between homologous structures (divergent evolution) and analogous structures (convergent evolution).",
                                "Examine the pentadactyl limb in humans, bats, whales, birds, and horses.",
                                "Identify vestigial structures and comparative embryological evidence.",
                                "Analyze cell biology, cytological karyotypes, and serological precipitin test evidence."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Comparative Biological Evidence for Evolution",
                        "content": {
                            "title": "Comparative Biological Evidence for Evolution",
                            "text": "Beyond fossils, evolutionary relationships are proven by comparing anatomical structures, embryonic development, cellular organelles, and blood serum proteins across living species."
                        }
                    }
                ],
                # Page 2
                [
                    {
                        "type": "definition_card",
                        "title": "Homology vs Analogy Taxonomy",
                        "content": {
                            "term": "Homology & Analogy Definitions",
                            "definition": "Anatomical comparison revealing divergent vs convergent evolutionary paths.",
                            "key_points": [
                                "Homologous Structures: Same basic anatomical plan and origin, modified for different functions (e.g., pentadactyl limb). Proves Divergent Evolution.",
                                "Analogous Structures: Different anatomical structures and origins, adapted for the same function (e.g., insect wing vs bird wing). Proves Convergent Evolution."
                            ]
                        }
                    }
                ],
                # Page 3
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Pentadactyl Limb Homology Across Vertebrates",
                        "content": {
                            "title": "Pentadactyl Limb Homology Across Vertebrates",
                            "caption": "Comparative Bone Skeleton Diagram: Basic 5-Digit Plan (Humerus, Radius, Ulna, Carpals, Metacarpals, Phalanges) Modified in Human (Grasping), Bat (Flying), Whale (Swimming), Horse (Running)",
                            "description": "Color-coded skeletal diagram showing pentadactyl limb bone modifications across human arm, bat wing, whale flipper, bird wing, and horse leg."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Homology & Divergent Evolution",
                        "content": {
                            "title": "Homology & Divergent Evolution",
                            "text": "The pentadactyl (5-digit) limb of land vertebrates shares the same basic arrangement of bones (humerus, radius, ulna, carpals, metacarpals, phalanges). Modification for different environments (human manipulation, bat flight, whale swimming, horse galloping) demonstrates divergent evolution from a common ancestral tetrapod."
                        }
                    }
                ],
                # Page 4
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Divergent vs Convergent Evolution Pathways",
                        "content": {
                            "title": "Divergent vs Convergent Evolution Pathways",
                            "caption": "Evolutionary Flowchart: Common Ancestor Diverging into Varied Adaptations (Divergent) vs Unrelated Taxa Converging on Similar Streamlined Shapes (Convergent)",
                            "description": "Flowchart contrasting common ancestor branching outwards (divergent) with unrelated shark, dolphin, and penguin evolving similar streamlined shapes (convergent)."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Analogy & Convergent Evolution",
                        "content": {
                            "title": "Analogy & Convergent Evolution",
                            "text": "Analogous structures perform similar functions but have entirely different embryonic origins and structural blueprints (e.g., chitinous insect wing vs bony feathered bird wing). Unrelated organisms facing similar environmental selection pressures evolve similar adaptations (convergent evolution)."
                        }
                    }
                ],
                # Page 5
                [
                    {
                        "type": "concept_explanation",
                        "title": "Vestigial Structures & Comparative Embryology",
                        "content": {
                            "title": "Vestigial Structures & Comparative Embryology",
                            "text": "• Vestigial Structures: Reduced, functionless organs that were fully functional in ancestral forms (e.g., human appendix, coccyx, nictitating membrane, pelvic bones in whales/pythons).\n• Comparative Embryology: Early embryos of fish, salamanders, tortoises, birds, and humans exhibit identical pharyngeal gill slits, post-anal tails, and two-chambered hearts, proving shared ancestry."
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Comparative Vertebrate Embryology Pathways",
                        "content": {
                            "title": "Comparative Vertebrate Embryology Pathways",
                            "caption": "Embryonic Stage Comparison: Early Vertebrate Embryos (Fish, Salamander, Tortoise, Chick, Human) Displaying Identical Pharyngeal Arches and Post-Anal Tails",
                            "description": "Diagram illustrating early stage embryos looking identical before diverging into adult forms."
                        }
                    }
                ],
                # Page 6
                [
                    {
                        "type": "suggested_image",
                        "title": "Cytological Chromosome Evidence Karyogram",
                        "content": {
                            "title": "Cytological Chromosome Evidence Karyogram",
                            "caption": "Karyogram of human chromosomes showing structural banding patterns nearly identical to chimpanzee chromosome sets.",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/b/b1/Human_karyotype_with_bands_and_sub-bands.png",
                            "author": "CC BY-SA 4.0, Wikimedia Commons",
                            "licensing": "CC BY-SA 4.0",
                            "commons_page_url": "https://commons.wikimedia.org/wiki/File:Human_karyotype_with_bands_and_sub-bands.png"
                        }
                    },
                    {
                        "type": "suggested_image",
                        "title": "Comparative Blood Cytology & Red Cell Smear",
                        "content": {
                            "title": "Comparative Blood Cytology & Red Cell Smear",
                            "caption": "Microscopic blood smear demonstrating universal cellular structure and biochemical membrane properties across mammals.",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/a/a6/Sickle_cell_anemia_smear.jpg",
                            "author": "Public Domain, Wikimedia Commons",
                            "licensing": "Public domain",
                            "commons_page_url": "https://commons.wikimedia.org/wiki/File:Sickle_cell_anemia_smear.jpg"
                        }
                    }
                ],
                # Page 7
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Serological Antigen-Antibody Precipitin Test Matrix",
                        "content": {
                            "title": "Serological Antigen-Antibody Precipitin Test Matrix",
                            "caption": "Biochemical Test Model: Human Serum Injected into Rabbit → Anti-Human Antibodies Mixed with Primate Serum → Precipitation Volume Measures Relationship Closeness",
                            "description": "Flowchart showing anti-human rabbit serum yielding 100% precipitation with human blood, 85% with chimpanzee, 65% with baboon, proving close evolutionary relationship."
                        }
                    },
                    {
                        "type": "worked_example",
                        "title": "Interpreting Serological Precipitin Test Results",
                        "content": {
                            "question": "Anti-human serum prepared in a rabbit was mixed with blood samples from Human, Chimpanzee, Baboon, and Dog. The percentages of protein precipitation were: Human 100%, Chimpanzee 85%, Baboon 64%, Dog 15%. Explain these results in terms of evolutionary relationships.",
                            "strategy": "Relate precipitation percentage to degree of serum protein homology and phylogenetic closeness.",
                            "solution": [
                                "1. Human (100%): Complete antigen-antibody reaction.",
                                "2. Chimpanzee (85%): High precipitation indicates closely matching serum proteins and a recent common ancestor with humans.",
                                "3. Baboon (64%): Moderate precipitation indicates a more distant common ancestor.",
                                "4. Dog (15%): Low precipitation indicates very distant ancestral relationship."
                            ]
                        }
                    }
                ],
                # Page 8
                [
                    {
                        "type": "common_mistake",
                        "title": "Common Student Traps: Homology vs Analogy",
                        "content": {
                            "mistake": "Classifying the wings of a bird and the wings of a butterfly as homologous structures.",
                            "correction": "Bird and butterfly wings are ANALOGOUS structures (different anatomy, same flight function; convergent evolution).",
                            "reasoning": "Bird wings contain internal endoskeleton bones; butterfly wings consist of chitinous exoskeleton extensions."
                        }
                    }
                ],
                # Page 9
                [
                    {
                        "type": "mini_activity",
                        "title": "Interactive Comparative Evidence Classifier",
                        "content": {
                            "activity_type": "scenario_decision",
                            "title": "Interactive Comparative Evidence Classifier",
                            "prompt": "The flipper of a whale and the arm of a human contain the same pentadactyl arrangement of bones, but perform different functions. How are these structures classified?",
                            "options": [
                                "Option A: Homologous structures proving Divergent Evolution.",
                                "Option B: Analogous structures proving Convergent Evolution.",
                                "Option C: Vestigial structures."
                            ],
                            "correct_option": "Option A: Homologous structures proving Divergent Evolution.",
                            "explanation": "Same basic pentadactyl plan modified for swimming vs grasping proves common ancestral origin (divergent evolution)."
                        }
                    }
                ],
                # Page 10
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Checkpoint: Comparative Evidence",
                        "content": {
                            "question": "Which human anatomical structure is considered vestigial?",
                            "options": [
                                "Appendix and Coccyx (tailbone)",
                                "Heart and Lungs",
                                "Femur and Humerus",
                                "Cornea and Lens"
                            ],
                            "correct_answer": 0,
                            "explanation": "The human appendix and coccyx are vestigial structures reduced from functional ancestral organs."
                        }
                    }
                ],
                # Page 11
                [
                    {
                        "type": "summary",
                        "title": "Comparative Anatomy & Serology: Key Takeaways",
                        "content": {
                            "title": "Comparative Anatomy & Serology: Key Takeaways",
                            "summary_points": [
                                "Homologous structures (pentadactyl limb) share same origin, modified for different functions -> Divergent Evolution.",
                                "Analogous structures (insect vs bird wings) share same function, different origins -> Convergent Evolution.",
                                "Vestigial organs (appendix, coccyx) are reduced functionless remnants of functional ancestral organs.",
                                "Comparative embryology, cell biology, and serological precipitin tests confirm phylogenetic relationships."
                            ]
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 5: Lamarck's Hypotheses versus Darwin's Theory of Natural Selection
        # =====================================================================
        {
            "unit_order": 5,
            "unit_name": "Lamarck's Hypotheses versus Darwin's Theory of Natural Selection",
            "unit_description": "Lamarckism (use/disuse & acquired traits), disproof by Weismann, Darwinian Natural Selection (5-step cascade), and Neo-Darwinism.",
            "lesson_title": "Lamarck's Hypotheses versus Darwin's Theory of Natural Selection",
            "pages": [
                # Page 1
                [
                    {
                        "type": "learning_goal",
                        "title": "Learning Objectives: Theories of Evolution",
                        "content": {
                            "title": "Learning Objectives: Theories of Evolution",
                            "goals": [
                                "Detail Jean-Baptiste Lamarck's two hypotheses (Use & Disuse, Inheritance of Acquired Characteristics).",
                                "Explain August Weismann's experimental disproof of Lamarckism.",
                                "Master Charles Darwin's 5-step Theory of Natural Selection.",
                                "Contrast Lamarckian vs Darwinian explanations for evolutionary adaptations."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Theories of Evolutionary Mechanism",
                        "content": {
                            "title": "Theories of Evolutionary Mechanism",
                            "text": "How does evolution occur? Two historical theories offered opposing explanations: Jean-Baptiste Lamarck (1809) proposed acquired inheritance, while Charles Darwin (1859) established Natural Selection."
                        }
                    }
                ],
                # Page 2
                [
                    {
                        "type": "definition_card",
                        "title": "Lamarckism Hypotheses Taxonomy",
                        "content": {
                            "term": "Lamarckism Hypotheses",
                            "definition": "Early 19th-century theory proposed by Jean-Baptiste Lamarck based on acquired physical adaptations.",
                            "key_points": [
                                "1. Law of Use and Disuse: Frequent use of an organ strengthens and enlarges it; disuse leads to deterioration.",
                                "2. Inheritance of Acquired Characteristics: Modifications acquired during an individual's lifetime are passed to offspring (e.g., short-necked giraffes stretching necks to reach high leaves pass long necks to offspring)."
                            ]
                        }
                    }
                ],
                # Page 3
                [
                    {
                        "type": "concept_explanation",
                        "title": "Scientific Disproof of Lamarckism",
                        "content": {
                            "title": "Scientific Disproof of Lamarckism",
                            "text": "Lamarckism was disproved because acquired somatic changes (e.g., muscular growth or amputations) do NOT alter the DNA nucleotide sequence inside germ cells (gametes). August Weismann cut off tails of mice for 22 generations; all offspring were born with normal full-length tails, proving somatic modifications are not inherited."
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Lamarckism vs Darwinism Mechanism Comparison",
                        "content": {
                            "title": "Lamarckism vs Darwinism Mechanism Comparison",
                            "caption": "Side-by-Side Comparison: Lamarck (Stretching Short Neck -> Acquired Long Neck Transmitted) vs Darwin (Pre-existing Genetic Variation -> Selection Pressure Kills Short-Necked -> Long-Necked Variants Survive & Reproduce)",
                            "description": "Comparative diagram contrasting individual stretching (Lamarck) with natural selection filtering pre-existing variation (Darwin)."
                        }
                    }
                ],
                # Page 4
                [
                    {
                        "type": "definition_card",
                        "title": "Darwin's Theory of Natural Selection",
                        "content": {
                            "term": "Natural Selection Definition",
                            "definition": "Process whereby organisms possessing favorable genetic variations best suited to their environment survive, reproduce, and pass their advantageous alleles to offspring.",
                            "key_points": [
                                "1. Overproduction: Organisms produce more offspring than environment can support.",
                                "2. Constancy of Numbers: Population sizes remain relatively stable.",
                                "3. Struggle for Existence: Severe competition for limited resources (food, space, mates).",
                                "4. Variation: Individuals exhibit pre-existing genetic variations.",
                                "5. Survival of the Fittest: Best adapted survive and reproduce."
                            ]
                        }
                    }
                ],
                # Page 5
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Darwinian Natural Selection 5-Step Cascade",
                        "content": {
                            "title": "Darwinian Natural Selection 5-Step Cascade",
                            "caption": "5-Step Evolutionary Cascade: High Reproductive Rate → Population Competition → Pre-Existing Genetic Variation → Selection Pressure → Differential Survival & Inheritance",
                            "description": "Flowchart showing Overproduction -> Competition -> Genetic Variation -> Natural Selection -> Evolutionary Adaptation."
                        }
                    },
                    {
                        "type": "suggested_image",
                        "title": "Artificial Selection in Domesticated Crops",
                        "content": {
                            "title": "Artificial Selection in Domesticated Crops",
                            "caption": "Domesticated pea pods demonstrating selective breeding by humans, serving as Darwin's model for natural selection.",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/5/51/Pisum_sativum_var._macrocarpum_Ilowiecki_2017-04-14_6973.jpg",
                            "author": "CC BY-SA 4.0, Wikimedia Commons",
                            "licensing": "CC BY-SA 4.0",
                            "commons_page_url": "https://commons.wikimedia.org/wiki/File:Pisum_sativum_var._macrocarpum_Ilowiecki_2017-04-14_6973.jpg"
                        }
                    }
                ],
                # Page 6
                [
                    {
                        "type": "concept_explanation",
                        "title": "Neo-Darwinism (Modern Synthetic Theory)",
                        "content": {
                            "title": "Neo-Darwinism (Modern Synthetic Theory)",
                            "text": "Neo-Darwinism merges Darwin's natural selection with modern genetics. It explains that pre-existing variation arises through gene mutations, chromosome mutations, meiotic crossing over, and random fertilisation. Selection acts on genotypes by altering gene frequencies within a population gene pool."
                        }
                    }
                ],
                # Page 7
                [
                    {
                        "type": "worked_example",
                        "title": "Worked KCSE Comparison: Giraffe Neck Evolution",
                        "content": {
                            "question": "Compare how Lamarck and Darwin would explain the evolution of long necks in modern giraffes.",
                            "strategy": "Contrast acquired stretching (Lamarck) with pre-existing variation and selection (Darwin).",
                            "solution": [
                                "Lamarck's Explanation: Ancestral giraffes had short necks. They stretched their necks to reach high tree leaves. Necks elongated through use, and this acquired long neck was passed to offspring.",
                                "Darwin's Explanation: Ancestral giraffes exhibited pre-existing variation in neck lengths (some short, some long). During drought, long-necked giraffes reached high leaves, survived, and reproduced (survival of the fittest). Short-necked giraffes starved. Long-neck alleles were inherited."
                            ]
                        }
                    }
                ],
                # Page 8
                [
                    {
                        "type": "mini_activity",
                        "title": "Interactive Evolutionary Theory Simulator",
                        "content": {
                            "activity_type": "scenario_decision",
                            "title": "Interactive Evolutionary Theory Simulator",
                            "prompt": "Why was Lamarck's hypothesis of 'Inheritance of Acquired Characteristics' rejected by modern biology?",
                            "options": [
                                "Option A: Somatic changes acquired during life do not alter DNA base sequences inside gametes (germ cells).",
                                "Option B: Giraffes do not eat tree leaves.",
                                "Option C: Lamarck did not use microscopes."
                            ],
                            "correct_option": "Option A: Somatic changes acquired during life do not alter DNA base sequences inside gametes (germ cells).",
                            "explanation": "Acquired somatic traits do not alter gametic DNA, so they cannot be inherited."
                        }
                    }
                ],
                # Page 9
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Checkpoint: Lamarck vs Darwin",
                        "content": {
                            "question": "In Darwin's theory of natural selection, what acts as the primary driving force selecting which variants survive?",
                            "options": [
                                "Environmental selection pressures (predators, disease, drought, food scarcity)",
                                "Desire of the organism to improve itself",
                                "Voluntary stretching of limbs",
                                "Supernatural intervention"
                            ],
                            "correct_answer": 0,
                            "explanation": "Environmental selection pressures filter pre-existing genetic variations."
                        }
                    }
                ],
                # Page 10
                [
                    {
                        "type": "summary",
                        "title": "Evolutionary Theories: Key Takeaways",
                        "content": {
                            "title": "Evolutionary Theories: Key Takeaways",
                            "summary_points": [
                                "Lamarckism proposed Use/Disuse and Acquired Inheritance — disproved because somatic traits do not alter gametic DNA.",
                                "Darwinism establishes Natural Selection: Overproduction -> Competition -> Variation -> Differential Survival -> Inheritance.",
                                "Neo-Darwinism combines natural selection with genetics, mutations, and gene pool allele frequency shifts."
                            ]
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 6: Industrial Melanism, Antibiotic and Pesticide Resistance, and Speciation
        # =====================================================================
        {
            "unit_order": 6,
            "unit_name": "Industrial Melanism, Antibiotic and Pesticide Resistance, and Speciation",
            "unit_description": "Industrial melanism in peppered moths, antibiotic resistance in bacteria, pesticide resistance in mosquitoes, and speciation mechanisms.",
            "lesson_title": "Industrial Melanism, Antibiotic and Pesticide Resistance, and Speciation",
            "pages": [
                # Page 1
                [
                    {
                        "type": "learning_goal",
                        "title": "Learning Objectives: Selection in Action & Speciation",
                        "content": {
                            "title": "Learning Objectives: Selection in Action & Speciation",
                            "goals": [
                                "Analyze Industrial Melanism in Peppered Moths (Biston betularia) as observed natural selection.",
                                "Explain the evolution of antibiotic resistance in bacteria and pesticide resistance in mosquitoes.",
                                "Detail speciation mechanisms via geographical and reproductive isolation.",
                                "Distinguish between allopatric and sympatric speciation."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Observed Natural Selection in Modern Times",
                        "content": {
                            "title": "Observed Natural Selection in Modern Times",
                            "text": "Natural selection is not merely an ancient historical concept; it is actively observed today in industrial moth camouflage shifts, bacterial superbugs, and pesticide-resistant mosquitoes."
                        }
                    }
                ],
                # Page 2
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Peppered Moth Industrial Melanism Frequency Shift",
                        "content": {
                            "title": "Peppered Moth Industrial Melanism Frequency Shift",
                            "caption": "Selection Shift: Pre-Industrial Britain (Light Lichen Trees -> Light Moths Camouflaged, Dark Eaten) vs Post-Industrial Pollution (Soot Trees -> Dark Melanic Moths Camouflaged, Light Eaten)",
                            "description": "Comparative diagram illustrating light moth camouflage on lichen bark vs dark melanic moth camouflage on soot-blackened tree trunks."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Industrial Melanism in Peppered Moths (Biston betularia)",
                        "content": {
                            "title": "Industrial Melanism in Peppered Moths (Biston betularia)",
                            "text": "• Pre-Industrial Britain (Before 1850): Tree trunks were covered in pale lichens. Light-colored peppered moths (*typica*) were camouflaged from predatory birds, while rare dark melanic mutants (*carbonaria*) were easily spotted and eaten (99% light moths).\n\n• Post-Industrial Revolution (After 1850): Coal soot killed lichens and blackened tree bark. Dark melanic moths became camouflaged, while light moths were preyed upon. Selection pressure reversed, causing dark moth allele frequency to rise above 95% in industrial areas."
                        }
                    }
                ],
                # Page 3
                [
                    {
                        "type": "concept_explanation",
                        "title": "Antibiotic & Pesticide Resistance",
                        "content": {
                            "title": "Antibiotic & Pesticide Resistance",
                            "text": "• Antibiotic Resistance: In bacterial populations (*Staphylococcus aureus*), random gene mutations confer resistance to antibiotics like penicillin. When antibiotics are applied, normal bacteria die, but resistant mutants survive and multiply, creating resistant superbug strains (MRSA).\n\n• Pesticide Resistance: Widespread spraying of DDT kills susceptible mosquitoes. Rare mutant mosquitoes carrying DDT-resistant enzymes survive and pass resistant alleles to offspring."
                        }
                    },
                    {
                        "type": "suggested_image",
                        "title": "Antibiotic Disk Diffusion Zone of Inhibition",
                        "content": {
                            "title": "Antibiotic Disk Diffusion Zone of Inhibition",
                            "caption": "Agar diffusion plate demonstrating clear zones of inhibition around antibiotic disks, with resistant bacterial colonies growing inside.",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/7/7a/Agar_Diffusion_Method_1.jpg",
                            "author": "CC BY-SA 4.0, Wikimedia Commons",
                            "licensing": "CC BY-SA 4.0",
                            "commons_page_url": "https://commons.wikimedia.org/wiki/File:Agar_Diffusion_Method_1.jpg"
                        }
                    }
                ],
                # Page 4
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Bacterial Antibiotic Resistance Selection Curve",
                        "content": {
                            "title": "Bacterial Antibiotic Resistance Selection Curve",
                            "caption": "Selection Model: Mixed Bacterial Population → Antibiotic Application Kills Susceptible Cells → Resistant Mutants Multiply to Form Dominant Colony",
                            "description": "Flowchart showing normal bacterial population containing rare red resistant mutant, antibiotic treatment destroying green susceptible cells, leaving red mutant to colonize."
                        }
                    }
                ],
                # Page 5
                [
                    {
                        "type": "definition_card",
                        "title": "Speciation & Isolation Mechanisms Taxonomy",
                        "content": {
                            "term": "Speciation Taxonomy",
                            "definition": "Formation of one or more new species from an existing ancestral population.",
                            "key_points": [
                                "Species: Group of organisms possessing similar anatomical features, capable of interbreeding to produce fertile offspring.",
                                "Geographical Isolation: Physical barriers (mountains, rivers, oceans) divide a population.",
                                "Reproductive Isolation: Inability of separated populations to interbreed due to behavioral, physiological, or structural differences.",
                                "Allopatric Speciation: Speciation occurring in geographically isolated populations.",
                                "Sympatric Speciation: Speciation occurring within the same geographical area (e.g., polyploidy in plants)."
                            ]
                        }
                    }
                ],
                # Page 6
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Allopatric Speciation via Geographical Isolation",
                        "content": {
                            "title": "Allopatric Speciation via Geographical Isolation",
                            "caption": "Speciation Pathway: Single Interbreeding Population → Physical River Barrier Division → Independent Mutations & Selection → Reproductive Isolation (New Species)",
                            "description": "Flowchart showing initial uniform population, formation of river barrier, divergence over time, and failure to interbreed when barrier is removed."
                        }
                    }
                ],
                # Page 7
                [
                    {
                        "type": "worked_example",
                        "title": "Worked KCSE Question: Mosquito DDT Resistance",
                        "content": {
                            "question": "Explain how the continuous use of DDT pesticide led to the evolution of DDT-resistant mosquito populations in Kenya. (4 Marks)",
                            "strategy": "Apply Darwinian natural selection steps to pesticide exposure.",
                            "solution": [
                                "1. Pre-existing Variation: The initial mosquito population contained rare random gene mutations conferring DDT resistance. (1 Mark)",
                                "2. Selection Pressure: Application of DDT pesticide acted as a strong environmental selection pressure. (1 Mark)",
                                "3. Differential Survival: Susceptible mosquitoes were killed, while rare DDT-resistant mosquitoes survived (survival of the fittest). (1 Mark)",
                                "4. Inheritance: Resistant survivors reproduced, passing the resistant allele to offspring, increasing DDT resistance frequency over generations. (1 Mark)"
                            ]
                        }
                    }
                ],
                # Page 8
                [
                    {
                        "type": "mini_activity",
                        "title": "Interactive Natural Selection Challenge",
                        "content": {
                            "activity_type": "scenario_decision",
                            "title": "Interactive Natural Selection Challenge",
                            "prompt": "Did the application of DDT cause mosquitoes to mutate and become resistant, or did DDT select for pre-existing resistant mutants?",
                            "options": [
                                "Option A: DDT acted as a selection pressure that selected for pre-existing resistant mutants.",
                                "Option B: DDT directly induced the mutation after mosquitoes felt threatened.",
                                "Option C: Mosquitoes learned to avoid flying into DDT spray."
                            ],
                            "correct_option": "Option A: DDT acted as a selection pressure that selected for pre-existing resistant mutants.",
                            "explanation": "Mutations occur randomly prior to pesticide exposure; DDT simply selects for pre-existing resistant variants."
                        }
                    }
                ],
                # Page 9
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Checkpoint: Selection & Speciation",
                        "content": {
                            "question": "What type of speciation occurs when a physical geographical barrier (like a mountain range or river) separates a single population into isolated groups?",
                            "options": [
                                "Allopatric Speciation",
                                "Sympatric Speciation",
                                "Artificial Selection",
                                "Polyploidy"
                            ],
                            "correct_answer": 0,
                            "explanation": "Allopatric speciation results from geographical isolation by physical barriers."
                        }
                    }
                ],
                # Page 10
                [
                    {
                        "type": "summary",
                        "title": "Natural Selection & Speciation: Key Takeaways",
                        "content": {
                            "title": "Natural Selection & Speciation: Key Takeaways",
                            "summary_points": [
                                "Industrial melanism in peppered moths demonstrates selection pressure shifts reversing allele frequencies.",
                                "Antibiotic and pesticide resistance evolve when drugs select for pre-existing resistant mutants.",
                                "Speciation requires geographical isolation followed by reproductive isolation preventing fertile interbreeding.",
                                "Allopatric speciation involves physical geographic barriers; sympatric speciation occurs within the same area."
                            ]
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 7: Comparative Limb and Wing Laboratory Investigations and Field Study
        # =====================================================================
        {
            "unit_order": 7,
            "unit_name": "Comparative Limb and Wing Laboratory Investigations and Field Study",
            "unit_description": "Practical biology lab investigations on pentadactyl limbs, bird vs insect wing comparative anatomy, and museum/archaeological field studies.",
            "lesson_title": "Comparative Limb and Wing Laboratory Investigations and Field Study",
            "pages": [
                # Page 1
                [
                    {
                        "type": "learning_goal",
                        "title": "Learning Objectives: Practical Evolutionary Biology",
                        "content": {
                            "title": "Learning Objectives: Practical Evolutionary Biology",
                            "goals": [
                                "Execute laboratory dissections comparing pentadactyl bone arrangements in vertebrate forelimbs.",
                                "Perform structural comparison between bird endoskeleton wings and insect chitinous wings.",
                                "Design a field study guide for visiting natural history museums and archaeological sites in Kenya."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Practical Biology: Evolutionary Evidence",
                        "content": {
                            "title": "Practical Biology: Evolutionary Evidence",
                            "text": "Laboratory examination of preserved vertebrate skeletons and wing structures provides hands-on empirical verification of homologous and analogous evolutionary concepts."
                        }
                    }
                ],
                # Page 2
                [
                    {
                        "type": "concept_explanation",
                        "title": "Lab Investigation 1: Pentadactyl Limb Dissection",
                        "content": {
                            "title": "Lab Investigation 1: Pentadactyl Limb Dissection",
                            "text": "Students examine preserved limbs of a frog, bird, rabbit, and human skeleton model:\n1. Identify single proximal bone (Humerus/Femur);\n2. Identify double distal bones (Radius & Ulna / Tibia & Fibula);\n3. Count carpals, metacarpals, and 5 phalanges, recording modifications for hopping, flying, running, and grasping."
                        }
                    }
                ],
                # Page 3
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Comparative Wing Morphology: Bird Endoskeleton vs Insect Exoskeleton",
                        "content": {
                            "title": "Comparative Wing Morphology: Bird Endoskeleton vs Insect Exoskeleton",
                            "caption": "Comparative Laboratory Diagram: Feathered Bony Bird Wing (Homologous Pentadactyl Origin) vs Chitinous Veined Insect Wing (Analogous Exoskeleton Origin)",
                            "description": "Comparative anatomical diagram illustrating internal bone structure of bird wing versus chitinous membrane of insect wing."
                        }
                    },
                    {
                        "type": "comparison_table",
                        "title": "Laboratory Observations: Bird Wing vs Insect Wing",
                        "content": {
                            "headers": ["Feature", "Bird Wing", "Insect Wing"],
                            "rows": [
                                ["Internal Support", "Living endoskeleton bones (humerus, radius, ulna)", "Non-living chitinous exoskeleton veins"],
                                ["Surface Covering", "Feathers attached to skin", "Membranous chitinous cuticle"],
                                ["Embryonic Origin", "Modifications of vertebrate forelimb", "Outgrowths of thoracic body wall"],
                                ["Evolutionary Type", "Homologous to mammal forelimbs", "Analogous to bird wings (Convergent)"]
                            ]
                        }
                    }
                ],
                # Page 4
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Museum Fossil Stratigraphy Lab Dissection Protocol",
                        "content": {
                            "title": "Museum Fossil Stratigraphy Lab Dissection Protocol",
                            "caption": "Practical Observation Guide: Identifying Rock Strata Layers, Index Fossils, and Homologous Bones in Museum Exhibits",
                            "description": "Flowchart outlining museum observation protocol for recording fossil depth, rock type, and comparative skeletal anatomy."
                        }
                    },
                    {
                        "type": "real_world_example",
                        "title": "Field Study Guide: Archaeological Sites in Kenya",
                        "content": {
                            "title": "Field Study Guide: Archaeological Sites in Kenya",
                            "text": "Kenya is the 'Cradle of Humankind'. Key archaeological and palaeontological sites for biology field trips include:\n• Olorgesailie: Hand axe stone tool deposits and prehistoric mammal fossils.\n• Kariandusi: Acheulean stone tool site in the Rift Valley.\n• Fort Ternan: Fossil site of *Kenyapithecus* (14 million years old)."
                        }
                    }
                ],
                # Page 5
                [
                    {
                        "type": "mini_activity",
                        "title": "Interactive Practical Dissection Challenge",
                        "content": {
                            "activity_type": "scenario_decision",
                            "title": "Interactive Practical Dissection Challenge",
                            "prompt": "During a practical examination, a student observes that both a bird wing and a cockroach wing enable flight, but the bird wing contains bones while the cockroach wing contains chitinous veins. What is the correct practical conclusion?",
                            "options": [
                                "Option A: The wings are analogous structures resulting from convergent evolution.",
                                "Option B: The wings are homologous structures resulting from divergent evolution.",
                                "Option C: The bird evolved directly from the cockroach."
                            ],
                            "correct_option": "Option A: The wings are analogous structures resulting from convergent evolution.",
                            "explanation": "Different anatomical blueprints performing the same flight function demonstrates analogy and convergent evolution."
                        }
                    }
                ],
                # Page 6
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Checkpoint: Practical Investigations",
                        "content": {
                            "question": "Which prehistoric hominid fossil site in Kenya is famous for abundant Acheulean hand axes and fossilized animal remains?",
                            "options": [
                                "Olorgesailie and Kariandusi",
                                "Mount Kenya peak",
                                "Mombasa coral reef",
                                "Lake Victoria island"
                            ],
                            "correct_answer": 0,
                            "explanation": "Olorgesailie and Kariandusi in the Kenyan Rift Valley are world-famous hominid fossil and stone tool sites."
                        }
                    }
                ],
                # Page 7
                [
                    {
                        "type": "summary",
                        "title": "Practical Investigations: Key Takeaways",
                        "content": {
                            "title": "Practical Investigations: Key Takeaways",
                            "summary_points": [
                                "Dissection of vertebrate forelimbs confirms the basic 5-digit pentadactyl plan.",
                                "Bird wings (bony endoskeleton) and insect wings (chitinous cuticle) are analogous structures.",
                                "Kenyan archaeological sites (Kariandusi, Olorgesailie, Fort Ternan) provide rich fossil evidence for hominid evolution."
                            ]
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 8: Evolutionary Synthesis, Key Glossary, Misconceptions, and Examination Diagnostic
        # =====================================================================
        {
            "unit_order": 8,
            "unit_name": "Evolutionary Synthesis, Key Glossary, Misconceptions, and Examination Diagnostic",
            "unit_description": "Topic synthesis, decision tree for KCSE evolutionary evidence questions, debunking common misconceptions, and worked KCSE essay diagnostics.",
            "lesson_title": "Evolutionary Synthesis, Key Glossary, Misconceptions, and Examination Diagnostic",
            "pages": [
                # Page 1
                [
                    {
                        "type": "learning_goal",
                        "title": "Learning Objectives: Evolutionary Synthesis & KCSE Review",
                        "content": {
                            "title": "Learning Objectives: Evolutionary Synthesis & KCSE Review",
                            "goals": [
                                "Synthesize all line evidences for evolution (fossils, comparative anatomy, embryology, serology).",
                                "Utilize a decision tree to classify KCSE evolutionary mechanism questions.",
                                "Debunk common student exam misconceptions in evolutionary biology.",
                                "Complete worked KCSE essay diagnostics and topic mastery review."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Master Synthesis of Evolutionary Principles",
                        "content": {
                            "title": "Master Synthesis of Evolutionary Principles",
                            "text": "Evolution is supported by multiple independent lines of scientific evidence: palaeontology, comparative anatomy, comparative embryology, cell biology, biogeography, and serology, operating primarily through natural selection acting on genetic variation."
                        }
                    }
                ],
                # Page 2
                [
                    {
                        "type": "suggested_diagram",
                        "title": "KCSE Evolutionary Evidence & Mechanism Decision Tree",
                        "content": {
                            "title": "KCSE Evolutionary Evidence & Mechanism Decision Tree",
                            "caption": "Diagnostic Decision Tree: Question Topic → Identify Evidence Line (Fossils/Homology/Serology) → Apply 5-Step Darwinian Selection Cascade → Formulate Model Answer",
                            "description": "Flowchart guiding students step-by-step on how to structure KCSE evolutionary essay answers."
                        }
                    },
                    {
                        "type": "common_mistake",
                        "title": "Debunking Common Evolutionary Misconceptions",
                        "content": {
                            "mistake": "Claiming that individual organisms adapt deliberately during their lifetime because they 'need' to change.",
                            "correction": "Natural selection acts on populations, not individuals. Individuals do not mutate on demand; pre-existing favorable genetic variants are selected by environmental pressures.",
                            "reasoning": "Evolution is not goal-directed teleology; it is differential survival of pre-existing random genetic variations."
                        }
                    }
                ],
                # Page 3
                [
                    {
                        "type": "worked_example",
                        "title": "Worked KCSE Essay 1: Evidence from Comparative Anatomy",
                        "content": {
                            "question": "Describe how comparative anatomy provides evidence for evolution. (10 Marks)",
                            "strategy": "Structure answer with Homology (Divergent), Analogy (Convergent), and Vestigial Organs with concrete biological examples.",
                            "solution": [
                                "1. Homologous Structures (4 Marks): Structures possessing the same basic anatomical blueprint and origin modified for different functions (e.g., pentadactyl limb in human arm, bat wing, whale flipper). Proves divergent evolution from a common ancestor.",
                                "2. Analogous Structures (3 Marks): Structures performing similar functions but possessing different anatomical blueprints and origins (e.g., insect wing vs bird wing). Proves convergent evolution under similar selection pressures.",
                                "3. Vestigial Organs (3 Marks): Reduced functionless remnants of organs that were fully functional in ancestral species (e.g., human appendix, coccyx, python pelvic girdle). Proves structural reduction over evolutionary time."
                            ]
                        }
                    }
                ],
                # Page 4
                [
                    {
                        "type": "worked_example",
                        "title": "Worked KCSE Essay 2: Natural Selection Mechanism",
                        "content": {
                            "question": "Describe how natural selection operates to bring about evolution in a population. (10 Marks)",
                            "strategy": "Present 5-step Darwinian cascade: Overproduction -> Competition -> Variation -> Selection -> Inheritance.",
                            "solution": [
                                "1. Overproduction (2 Marks): Organisms produce more offspring than the environment can support.",
                                "2. Struggle for Existence (2 Marks): High numbers lead to intra- and inter-specific competition for limited food, space, and mates.",
                                "3. Genetic Variation (2 Marks): Individuals exhibit pre-existing genetic variations caused by gene mutations and meiotic recombination.",
                                "4. Survival of the Fittest (2 Marks): Environmental selection pressures favor individuals possessing advantageous adaptations; unfit individuals die.",
                                "5. Inheritance & Adaptation (2 Marks): Favorable traits are passed to offspring, increasing advantageous allele frequencies over generations."
                            ]
                        }
                    }
                ],
                # Page 5
                [
                    {
                        "type": "knowledge_check",
                        "title": "Topic 2 Mastery Assessment Question",
                        "content": {
                            "question": "Which sequence correctly traces the 5 steps of Darwinian natural selection in a population?",
                            "options": [
                                "Overproduction → Struggle for existence → Variation → Differential survival → Inheritance of favorable alleles",
                                "Stretching → Acquired trait → Inheritance → Overproduction → Extinction",
                                "Mutation on demand → Adaptation → Overproduction → Speciation",
                                "Special creation → Fixity of species → Migration → Extinction"
                            ],
                            "correct_answer": 0,
                            "explanation": "Natural selection proceeds: Overproduction -> Competition -> Variation -> Selection -> Inheritance."
                        }
                    }
                ],
                # Page 6
                [
                    {
                        "type": "summary",
                        "title": "Topic 2 Mastery Synthesis & Complete Review",
                        "content": {
                            "title": "Topic 2 Mastery Synthesis & Complete Review",
                            "summary_points": [
                                "Evolution is supported by palaeontology, homology/analogy, vestigial organs, embryology, cell biology, and serology.",
                                "Lamarckism (acquired inheritance) was disproved; Darwinian Natural Selection (Neo-Darwinism) is the accepted mechanism.",
                                "Selection operates today in industrial melanism, bacterial antibiotic resistance, and mosquito pesticide resistance.",
                                "Speciation requires geographical and reproductive isolation creating separate gene pools."
                            ]
                        }
                    }
                ]
            ]
        }
    ]

def ingest_form4_biology_topic2(replace=False):
    print("=" * 80)
    print("VLearn Form 4 Biology — Topic 2: Evolution")
    print("High-Structure Production Ingestion Engine")
    print("=" * 80)

    curriculum = Curriculum.objects.filter(name="844").first()
    grade = Grade.objects.filter(curriculum=curriculum, name="Form 4").first()
    subject = Subject.objects.filter(grade=grade, name="Biology").first()

    if not subject:
        print("[!] Error: Subject 'Biology' not found under Form 4.")
        return

    print(f"[*] Resolved Target: {curriculum.name} -> {grade.name} -> {subject.name} (ID: {subject.id})")

    topic_name = "Evolution"
    topic = Topic.objects.filter(subject=subject, name=topic_name).first()

    if topic and replace:
        print(f"[*] Found existing Topic '{topic_name}' (ID: {topic.id}). Removing for clean replace...")
        topic.delete()
        topic = None

    if not topic:
        topic = Topic.objects.create(
            subject=subject,
            name=topic_name,
            order=2,
            description="Comprehensive syllabus on organic evolution, origin of life, chemical evolution, palaeontology, comparative anatomy/embryology/serology, Lamarckism vs Darwinism, natural selection in action, and speciation."
        )
        print(f"[+] Created Topic: {topic.name} (ID: {topic.id})")
    else:
        print(f"[*] Using existing Topic: {topic.name} (ID: {topic.id})")

    curriculum_data = build_topic2_curriculum()
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

            lesson = Lesson.objects.filter(topic=topic, learning_unit=learning_unit).first()
            if lesson:
                lesson.blocks.all().delete()
            else:
                lesson = Lesson.objects.create(
                    topic=topic,
                    learning_unit=learning_unit,
                    title=lesson_title,
                    status="published",
                    version=1
                )
            print(f"  [+] Ingesting Lesson {unit_order}: {lesson.title} (ID: {lesson.id})")

            block_order = 10
            lesson_page_count = len(pages_data)

            for page_idx, page_blocks in enumerate(pages_data, 1):
                first_block_title = page_blocks[0].get("title", f"Page {page_idx}")
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
            print(f"      [OK] Ingested {lesson_page_count} Pages for Lesson {unit_order}.")

    print("=" * 80)
    print("[SUCCESS] Form 4 Biology Topic 2 (Evolution) Ingestion Complete!")
    print(f"[*] Total Lessons Ingested: {total_lessons}")
    print(f"[*] Total Pages Ingested:   {total_pages}")
    print(f"[*] Total Blocks Ingested:  {total_blocks}")
    print("=" * 80)

if __name__ == "__main__":
    replace_flag = "--replace" in sys.argv
    ingest_form4_biology_topic2(replace=replace_flag)
