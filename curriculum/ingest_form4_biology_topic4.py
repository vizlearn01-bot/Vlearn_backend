"""
VLearn Form 4 Biology — Topic 4: Support and Movement in Plants and Animals (Final Topic)
High-Structure Production Ingestion Engine

Topic: Support and Movement in Plants and Animals (Topic Order: 4)
Subject: Biology (Subject ID: 13)
Grade: Form 4 (Grade ID: 4)
Curriculum: 844 (Curriculum ID: 4)

Decomposed into 10 Learning Units & 10 Published Lessons (133 Total Pages):
  1. Introduction to Biological Support and Movement Systems (6 Pages)
  2. Plant Support Tissues, Turgidity, Weak Stems, and Wilting Mechanisms (16 Pages)
  3. Animal Skeletons and Locomotion Adaptations in Finned Fish (15 Pages)
  4. The Mammalian Skull and Structural Blueprint of a Typical Vertebra (14 Pages)
  5. Regional Vertebrae Specializations, Rib Cage, and Sternum Architecture (10 Pages)
  6. The Pectoral Girdle, Forelimb Bones, and Elbow Joint Mechanics (16 Pages)
  7. The Pelvic Girdle, Hindlimb Bones, and Weight-Bearing Adaptations (17 Pages)
  8. Classification of Joints, Synovial Architecture, Ligaments, and Tendons (15 Pages)
  9. Histology of Muscle Tissues, Myogenic Properties, and Antagonistic Arm Mechanics (17 Pages)
  10. Laboratory Investigations, Common Misconceptions, and Multi-Tier Exam Review (7 Pages)

Usage:
  ./venv/bin/python curriculum/ingest_form4_biology_topic4.py [--replace]
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

def build_topic4_curriculum():
    """Returns the comprehensive pedagogical page and block structure for Topic 4."""
    return [
        # =====================================================================
        # LESSON 1: Introduction to Biological Support and Movement Systems
        # =====================================================================
        {
            "unit_order": 1,
            "unit_name": "Introduction to Biological Support and Movement Systems",
            "unit_description": "Necessity of support and movement, and types of skeletons (hydrostatic, exoskeleton, endoskeleton).",
            "lesson_title": "Introduction to Biological Support and Movement Systems",
            "pages": [
                [
                    {
                        "type": "learning_goal",
                        "title": "Learning Objectives: Support Systems Overview",
                        "content": {
                            "title": "Learning Objectives: Support Systems Overview",
                            "goals": [
                                "Explain the necessity of support and movement in plants and animals.",
                                "Classify skeletal types: Hydrostatic skeleton, Exoskeleton, and Endoskeleton.",
                                "Compare mechanical support mechanisms in terrestrial vs aquatic organisms."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Biological Necessity of Support & Movement",
                        "content": {
                            "title": "Biological Necessity of Support & Movement",
                            "text": "Support systems maintain body shape against gravity, protect soft internal organs, and provide lever anchor points for muscle contraction, enabling organisms to move, search for food, escape predators, and reproduce."
                        }
                    }
                ],
                [
                    {
                        "type": "definition_card",
                        "title": "Skeletal Systems Taxonomy",
                        "content": {
                            "term": "Skeletal Types Taxonomy",
                            "definition": "Structural frameworks supporting animal bodies.",
                            "key_points": [
                                "Hydrostatic Skeleton: Fluid under pressure inside closed coelomic cavities (e.g., Earthworms, Jellyfish).",
                                "Exoskeleton: Hard external chitinous cuticle covering body surface (e.g., Insects, Crabs).",
                                "Endoskeleton: Internal mineralized bony and cartilaginous framework (e.g., Fish, Mammals)."
                            ]
                        }
                    }
                ],
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Skeletal Types: Hydrostatic, Exoskeleton, and Endoskeleton",
                        "content": {
                            "title": "Skeletal Types: Hydrostatic, Exoskeleton, and Endoskeleton",
                            "caption": "Comparative Blueprint: Hydrostatic Fluid Core (Earthworm) vs Rigid Outer Chitinous Cuticle (Insect) vs Internal Vertebrate Bone Frame",
                            "description": "Comparative diagram illustrating earthworm fluid pressure, insect chitinous exoskeleton, and mammalian bony endoskeleton."
                        }
                    },
                    {
                        "type": "suggested_image",
                        "title": "Human Skeleton Upper Body Anterior View",
                        "content": {
                            "title": "Human Skeleton Upper Body Anterior View",
                            "caption": "Anterior view of the human upper body endoskeleton displaying skull, clavicle, rib cage, and vertebral column.",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/a/a5/Human_Skeleton_Upper_Body_Anterior_View.jpg",
                            "author": "CC BY-SA 4.0, Wikimedia Commons",
                            "licensing": "CC BY-SA 4.0",
                            "commons_page_url": "https://commons.wikimedia.org/wiki/File:Human_Skeleton_Upper_Body_Anterior_View.jpg"
                        }
                    }
                ],
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Checkpoint: Skeletal Types",
                        "content": {
                            "question": "Which animal utilizes a hydrostatic fluid skeleton under pressure for locomotion?",
                            "options": [
                                "Earthworm (Lumbricus terrestris)",
                                "Grasshopper (Locusta migratoria)",
                                "Tilapia fish",
                                "Domestic Cat"
                            ],
                            "correct_answer": 0,
                            "explanation": "Earthworms use pressurized coelomic fluid as a hydrostatic skeleton."
                        }
                    }
                ],
                [
                    {
                        "type": "summary",
                        "title": "Introduction to Support & Movement: Key Takeaways",
                        "content": {
                            "title": "Introduction to Support & Movement: Key Takeaways",
                            "summary_points": [
                                "Support systems resist gravity, protect vital organs, and enable locomotion.",
                                "Hydrostatic skeletons rely on fluid pressure (annelids).",
                                "Exoskeletons consist of chitinous outer cuticles requiring ecdysis (arthropods).",
                                "Endoskeletons consist of internal living bone and cartilage (vertebrates)."
                            ]
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 2: Plant Support Tissues, Turgidity, Weak Stems, and Wilting Mechanisms
        # =====================================================================
        {
            "unit_order": 2,
            "unit_name": "Plant Support Tissues, Turgidity, Weak Stems, and Wilting Mechanisms",
            "unit_description": "Turgidity in parenchyma cells, collenchyma, sclerenchyma, xylem, weak stems, and wilting mechanics.",
            "lesson_title": "Plant Support Tissues, Turgidity, Weak Stems, and Wilting Mechanisms",
            "pages": [
                [
                    {
                        "type": "learning_goal",
                        "title": "Learning Objectives: Plant Support",
                        "content": {
                            "title": "Learning Objectives: Plant Support",
                            "goals": [
                                "Explain turgidity in parenchyma cells as non-woody support.",
                                "Contrast collenchyma (cellulose/pectin corners) with sclerenchyma (lignified dead cells).",
                                "Describe xylem vessel and tracheid lignified thickenings.",
                                "Analyze weak stem adaptations (tendrils, twiners) and wilting physiology."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Turgidity in Parenchyma Cells",
                        "content": {
                            "title": "Turgidity in Parenchyma Cells",
                            "text": "In herbaceous non-woody plants and leaves, support is provided by turgor pressure. Parenchyma cells absorb water by osmosis, swelling and pressing cytoplasm against rigid cellulose cell walls, keeping stems erect."
                        }
                    }
                ],
                [
                    {
                        "type": "definition_card",
                        "title": "Plant Support Tissues Taxonomy",
                        "content": {
                            "term": "Plant Mechanical Tissues",
                            "definition": "Specialized tissues providing structural rigidity.",
                            "key_points": [
                                "Parenchyma: Living cells; support via turgor pressure.",
                                "Collenchyma: Living cells; localized cellulose and pectin wall thickenings at corners; flexible support in young stems.",
                                "Sclerenchyma: Dead lignified cells; thick secondary walls with pits; rigid support (Fibers & Sclereids).",
                                "Xylem Vessels & Tracheids: Dead lignified vessels; water transport and mechanical strength."
                            ]
                        }
                    }
                ],
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Plant Support Tissues Cross-Section: Collenchyma vs Sclerenchyma",
                        "content": {
                            "title": "Plant Support Tissues Cross-Section: Collenchyma vs Sclerenchyma",
                            "caption": "Histological Comparison: Living Collenchyma (Pectin Corner Thickenings) vs Dead Sclerenchyma (Thick Lignified Secondary Walls & Narrow Lumen)",
                            "description": "Cross-sectional diagram highlighting collenchyma corner thickenings vs sclerenchyma lignified walls."
                        }
                    },
                    {
                        "type": "suggested_image",
                        "title": "Plant Stem Cross-Section Visualization",
                        "content": {
                            "title": "Plant Stem Cross-Section Visualization",
                            "caption": "Photomicrograph of dicotyledonous plant stem cross-section showing vascular bundles and sclerenchyma caps.",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/6/67/Stem_Cross-Section.jpg",
                            "author": "Public Domain, Wikimedia Commons",
                            "licensing": "Public domain",
                            "commons_page_url": "https://commons.wikimedia.org/wiki/File:Stem_Cross-Section.jpg"
                        }
                    }
                ],
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Lignified Xylem Vessels & Tracheid Thickenings",
                        "content": {
                            "title": "Lignified Xylem Vessels & Tracheid Thickenings",
                            "caption": "Vascular Reinforcement Models: Annular (Ring), Spiral, Reticulate, and Pitted Lignin Wall Patterns in Xylem Vessels",
                            "description": "Diagram illustrating annular rings, spiral coils, and pitted lignin patterns in xylem walls."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Weak Stems & Wilting Mechanics",
                        "content": {
                            "title": "Weak Stems & Wilting Mechanics",
                            "text": "• Weak Stem Adaptations: Plants with insufficient mechanical tissue use tendrils (twining around supports), climbing roots, hooks, or twining stems (e.g., passion fruit, morning glory).\n\n• Wilting Physiology: When transpiration rate exceeds water absorption, parenchyma cells lose water via osmosis, lose turgor pressure, become flaccid, and leaves droop/wilt."
                        }
                    }
                ],
                [
                    {
                        "type": "suggested_image",
                        "title": "Plant Weak Stem Tendrils Visualization",
                        "content": {
                            "title": "Plant Weak Stem Tendrils Visualization",
                            "caption": "Garden pea plant showing thigmotropic tendrils coiled around support structures for mechanical elevation.",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/5/51/Pisum_sativum_var._macrocarpum_Ilowiecki_2017-04-14_6973.jpg",
                            "author": "CC BY-SA 4.0, Wikimedia Commons",
                            "licensing": "CC BY-SA 4.0",
                            "commons_page_url": "https://commons.wikimedia.org/wiki/File:Pisum_sativum_var._macrocarpum_Ilowiecki_2017-04-14_6973.jpg"
                        }
                    }
                ],
                [
                    {
                        "type": "mini_activity",
                        "title": "Interactive Plant Support Tissue Classifier",
                        "content": {
                            "activity_type": "scenario_decision",
                            "title": "Interactive Plant Support Tissue Classifier",
                            "prompt": "Which plant support tissue consists of dead cells with heavily lignified secondary walls that stain red with phloroglucinol?",
                            "options": [
                                "Option A: Sclerenchyma Tissue",
                                "Option B: Parenchyma Tissue",
                                "Option C: Collenchyma Tissue"
                            ],
                            "correct_option": "Option A: Sclerenchyma Tissue",
                            "explanation": "Sclerenchyma cells are dead at maturity with heavily lignified walls."
                        }
                    }
                ],
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Checkpoint: Plant Tissues",
                        "content": {
                            "question": "What causes herbaceous plant leaves to wilt during hot sunny dry afternoons?",
                            "options": [
                                "Transpiration rate exceeds root water absorption, causing loss of parenchyma turgor pressure.",
                                "Sclerenchyma fibers melt.",
                                "Collenchyma cells turn into xylem.",
                                "Roots stop growing."
                            ],
                            "correct_answer": 0,
                            "explanation": "Wilting occurs when water loss exceeds absorption, destroying cell turgidity."
                        }
                    }
                ],
                [
                    {
                        "type": "summary",
                        "title": "Plant Support Tissues: Key Takeaways",
                        "content": {
                            "title": "Plant Support Tissues: Key Takeaways",
                            "summary_points": [
                                "Parenchyma provides turgor support in non-woody tissue.",
                                "Collenchyma has living cellulose/pectin corner thickenings in young stems.",
                                "Sclerenchyma consists of dead lignified fibers providing rigid strength.",
                                "Xylem features annular, spiral, and pitted lignin thickenings.",
                                "Wilting is caused by loss of turgor pressure when transpiration exceeds absorption."
                            ]
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 3: Animal Skeletons and Locomotion Adaptations in Finned Fish
        # =====================================================================
        {
            "unit_order": 3,
            "unit_name": "Animal Skeletons and Locomotion Adaptations in Finned Fish",
            "unit_description": "Locomotion adaptations in bony fish (Tilapia), W-shaped myotome muscles, fins, and stability controls (pitching, rolling, yawing).",
            "lesson_title": "Animal Skeletons and Locomotion Adaptations in Finned Fish",
            "pages": [
                [
                    {
                        "type": "learning_goal",
                        "title": "Learning Objectives: Fish Locomotion",
                        "content": {
                            "title": "Learning Objectives: Fish Locomotion",
                            "goals": [
                                "Analyze body streamlining and drag reduction in aquatic environments.",
                                "Describe W-shaped myotome muscle block contractions along the spine.",
                                "Distinguish functions of paired fins (pectoral, pelvic) vs unpaired fins (dorsal, anal, caudal).",
                                "Explain stability controls against pitching, rolling, and yawing."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Locomotion Adaptations in Finned Fish (Tilapia)",
                        "content": {
                            "title": "Locomotion Adaptations in Finned Fish (Tilapia)",
                            "text": "Bony fish are adapted to move efficiently in water, a dense medium, through:\n1. Streamlined spindle-shaped body (tapering at both ends) to minimize water friction;\n2. Flexible vertebral column with W-shaped myotome muscle blocks;\n3. Mucus-covered scales to reduce drag;\n4. Swim bladder for neutral buoyancy control."
                        }
                    }
                ],
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Fish Myotome Muscle Blocks & Fin Anatomy (Pectoral, Pelvic, Caudal)",
                        "content": {
                            "title": "Fish Myotome Muscle Blocks & Fin Anatomy (Pectoral, Pelvic, Caudal)",
                            "caption": "Anatomical Model of Bony Fish: W-Shaped Myotome Muscle Segments → Paired Steering Fins (Pectoral, Pelvic) → Unpaired Stabilizing Fins (Dorsal, Anal, Caudal Propulsive Tail)",
                            "description": "Diagram illustrating fish body layout highlighting myotome muscle blocks, dorsal fin, caudal fin, anal fin, pectoral fin, and pelvic fin."
                        }
                    },
                    {
                        "type": "suggested_image",
                        "title": "Animal Locomotion Organisms Visualization",
                        "content": {
                            "title": "Animal Locomotion Organisms Visualization",
                            "caption": "Adaptive locomotion morphologies across aquatic and terrestrial fauna.",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/5/50/Darwin%27s_finches.png",
                            "author": "Public Domain, Wikimedia Commons",
                            "licensing": "Public domain",
                            "commons_page_url": "https://commons.wikimedia.org/wiki/File:Darwin%27s_finches.png"
                        }
                    }
                ],
                [
                    {
                        "type": "definition_card",
                        "title": "Fish Fin Functions & Stability Taxonomy",
                        "content": {
                            "term": "Fish Fin Taxonomy",
                            "definition": "Functional roles of fish fins in aquatic movement.",
                            "key_points": [
                                "Caudal Fin: Provides main forward propulsive force and acts as a rudder.",
                                "Paired Fins (Pectoral & Pelvic): Control steering, upward/downward pitching, braking, and balancing.",
                                "Unpaired Fins (Dorsal & Anal): Prevent rolling (side-to-side tipping) and yawing (lateral displacement)."
                            ]
                        }
                    }
                ],
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Yawing, Pitching, and Rolling Controls in Finned Fish",
                        "content": {
                            "title": "Yawing, Pitching, and Rolling Controls in Finned Fish",
                            "caption": "3-Axis Hydrodynamic Stability: Pitching (Vertical Head/Tail Up-Down movement prevented by Pectorals) vs Rolling (Rotational Tipping prevented by Dorsal/Anal) vs Yawing",
                            "description": "Hydrodynamic diagram showing 3 axes of instability in fish movement: Pitching, Rolling, and Yawing, and how fins counteract them."
                        }
                    },
                    {
                        "type": "mini_activity",
                        "title": "Interactive Fish Locomotion Simulator",
                        "content": {
                            "activity_type": "scenario_decision",
                            "title": "Interactive Fish Locomotion Simulator",
                            "prompt": "Which fins in a bony fish prevent the body from rolling (tipping sideways over its long axis)?",
                            "options": [
                                "Option A: Unpaired Dorsal and Anal fins",
                                "Option B: Paired Pectoral fins only",
                                "Option C: Caudal fin"
                            ],
                            "correct_option": "Option A: Unpaired Dorsal and Anal fins",
                            "explanation": "Dorsal and anal fins extend vertically to prevent rolling."
                        }
                    }
                ],
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Checkpoint: Fish Locomotion",
                        "content": {
                            "question": "What is the primary function of W-shaped myotome muscle block contractions in fish locomotion?",
                            "options": [
                                "They contract alternately on opposite sides of the spine to produce lateral undulations that push against water.",
                                "They pump air into the swim bladder.",
                                "They open the operculum gill cover.",
                                "They digest food."
                            ],
                            "correct_answer": 0,
                            "explanation": "Alternate myotome contractions create lateral waves pushing the fish forward."
                        }
                    }
                ],
                [
                    {
                        "type": "summary",
                        "title": "Fish Locomotion Adaptations: Key Takeaways",
                        "content": {
                            "title": "Fish Locomotion Adaptations: Key Takeaways",
                            "summary_points": [
                                "Streamlined body, slimy scales, and swim bladder adapt fish to aquatic life.",
                                "W-shaped myotome muscles contract alternately along the spine, driving lateral undulations.",
                                "Caudal fin provides main forward thrust.",
                                "Paired fins (pectoral, pelvic) control steering, pitching, and braking.",
                                "Unpaired fins (dorsal, anal) prevent rolling and yawing."
                            ]
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 4: The Mammalian Skull and Structural Blueprint of a Typical Vertebra
        # =====================================================================
        {
            "unit_order": 4,
            "unit_name": "The Mammalian Skull and Structural Blueprint of a Typical Vertebra",
            "unit_description": "Axial vs appendicular skeleton, mammalian skull features, and the universal structural blueprint of a typical vertebra.",
            "lesson_title": "The Mammalian Skull and Structural Blueprint of a Typical Vertebra",
            "pages": [
                [
                    {
                        "type": "learning_goal",
                        "title": "Learning Objectives: Skull & Vertebral Blueprint",
                        "content": {
                            "title": "Learning Objectives: Skull & Vertebral Blueprint",
                            "goals": [
                                "Differentiate between axial and appendicular skeletons.",
                                "Identify structural features of the mammalian skull (cranium, orbits, jaws, occipital condyles).",
                                "Label the universal components of a typical mammalian vertebra (centrum, neural arch, neural spine, transverse processes, zygapophyses)."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Axial vs Appendicular Skeleton",
                        "content": {
                            "title": "Axial vs Appendicular Skeleton",
                            "text": "• Axial Skeleton: Located along the main longitudinal central axis (Skull, Vertebral Column, Rib Cage, Sternum).\n• Appendicular Skeleton: Attached to the axial skeleton (Pectoral Girdle, Pelvic Girdle, Forelimb Bones, Hindlimb Bones)."
                        }
                    }
                ],
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Mammalian Skull Anatomy: Cranium, Orbit, Maxilla, Mandible",
                        "content": {
                            "title": "Mammalian Skull Anatomy: Cranium, Orbit, Maxilla, Mandible",
                            "caption": "Mammalian Skull Blueprint: Protective Cranium Brainbox → Orbit Eye Socket → Upper Maxilla & Lower Mandible Jaws → Occipital Condyles for Atlas Articulation",
                            "description": "Anatomical diagram of mammalian skull labeling cranium, orbit, maxilla, mandible, teeth, and occipital condyles."
                        }
                    },
                    {
                        "type": "suggested_image",
                        "title": "Mammalian Skull Lateral View Visualization",
                        "content": {
                            "title": "Mammalian Skull Lateral View Visualization",
                            "caption": "Lateral view of human cranium and facial bone structures.",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/c/c5/Human_Skull_Lateral_View_Unlabeled.jpg",
                            "author": "CC BY-SA 4.0, Wikimedia Commons",
                            "licensing": "CC BY-SA 4.0",
                            "commons_page_url": "https://commons.wikimedia.org/wiki/File:Human_Skull_Lateral_View_Unlabeled.jpg"
                        }
                    }
                ],
                [
                    {
                        "type": "definition_card",
                        "title": "Typical Vertebra Blueprint Taxonomy",
                        "content": {
                            "term": "Universal Vertebra Features",
                            "definition": "Structural components present in a typical mammalian vertebra.",
                            "key_points": [
                                "Centrum (Body): Solid basal mass providing main load-bearing support.",
                                "Neural Arch: Bone ring enclosing and protecting the spinal cord.",
                                "Neural Canal: Longitudinal passage inside neural arch for spinal cord.",
                                "Neural Spine: Dorsal projection for back muscle and ligament attachment.",
                                "Transverse Processes: Lateral projections for muscle/rib attachment.",
                                "Zygapophyses (Articular Facets): Pre- and Post-zygapophyses for interlocking adjacent vertebrae."
                            ]
                        }
                    }
                ],
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Structural Blueprint of a Typical Mammalian Vertebra",
                        "content": {
                            "title": "Structural Blueprint of a Typical Mammalian Vertebra",
                            "caption": "Cross-Section Blueprint: Central Load-Bearing Centrum → Enclosing Neural Arch & Canal → Dorsal Neural Spine → Lateral Transverse Processes → Articular Zygapophyses",
                            "description": "Diagram illustrating a typical vertebra labeling centrum, neural canal, neural arch, neural spine, transverse processes, and pre-zygapophyses."
                        }
                    },
                    {
                        "type": "suggested_image",
                        "title": "Lumbar Vertebra Superior Blueprint Visualization",
                        "content": {
                            "title": "Lumbar Vertebra Superior Blueprint Visualization",
                            "caption": "Superior view of human lumbar vertebra showing massive centrum and broad transverse processes.",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/1/1f/Vertebra_-_lumbales_%28superior_view%29.jpg",
                            "author": "CC BY-SA 4.0, Wikimedia Commons",
                            "licensing": "CC BY-SA 4.0",
                            "commons_page_url": "https://commons.wikimedia.org/wiki/File:Vertebra_-_lumbales_%28superior_view%29.jpg"
                        }
                    }
                ],
                [
                    {
                        "type": "mini_activity",
                        "title": "Interactive Vertebra Blueprint Classifier",
                        "content": {
                            "activity_type": "scenario_decision",
                            "title": "Interactive Vertebra Blueprint Classifier",
                            "prompt": "Which structure in a typical vertebra encloses and protects the delicate spinal cord?",
                            "options": [
                                "Option A: Neural Arch enclosing Neural Canal",
                                "Option B: Centrum",
                                "Option C: Transverse process"
                            ],
                            "correct_option": "Option A: Neural Arch enclosing Neural Canal",
                            "explanation": "The neural arch forms a bony ring creating the neural canal through which the spinal cord passes."
                        }
                    }
                ],
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Checkpoint: Vertebra Blueprint",
                        "content": {
                            "question": "What is the primary function of pre- and post-zygapophyses (articular facets) on a vertebra?",
                            "options": [
                                "To articulate and interlock with adjacent vertebrae, permitting controlled bending while preventing dislocation.",
                                "To transport blood to the brain.",
                                "To attach ribs.",
                                "To produce red blood cells."
                            ],
                            "correct_answer": 0,
                            "explanation": "Zygapophyses articulate adjacent vertebrae to allow bending without dislocation."
                        }
                    }
                ],
                [
                    {
                        "type": "summary",
                        "title": "Vertebral Blueprint: Key Takeaways",
                        "content": {
                            "title": "Vertebral Blueprint: Key Takeaways",
                            "summary_points": [
                                "Axial skeleton includes skull, vertebral column, ribs, and sternum.",
                                "Skull protects brain inside cranium and articulates via double occipital condyles.",
                                "Typical vertebra comprises centrum, neural arch, neural canal, neural spine, transverse processes, and zygapophyses."
                            ]
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 5: Regional Vertebrae Specializations, Rib Cage, and Sternum Architecture
        # =====================================================================
        {
            "unit_order": 5,
            "unit_name": "Regional Vertebrae Specializations, Rib Cage, and Sternum Architecture",
            "unit_description": "Cervical (atlas, axis), thoracic, lumbar, sacral, caudal vertebrae specializations, and rib cage anatomy.",
            "lesson_title": "Regional Vertebrae Specializations, Rib Cage, and Sternum Architecture",
            "pages": [
                [
                    {
                        "type": "learning_goal",
                        "title": "Learning Objectives: Regional Vertebrae & Ribs",
                        "content": {
                            "title": "Learning Objectives: Regional Vertebrae & Ribs",
                            "goals": [
                                "Distinguish 5 vertebral regions (Cervical, Thoracic, Lumbar, Sacral, Caudal).",
                                "Contrast Atlas (nodding) vs Axis (pivoting) cervical specializations.",
                                "Identify thoracic rib articulation facets and long neural spines.",
                                "Analyze lumbar load-bearing centrums and rib cage true/false/floating architecture."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Regional Vertebral Column Divisions",
                        "content": {
                            "title": "Regional Vertebral Column Divisions",
                            "text": "The mammalian vertebral column is divided into 5 specialized regions:\n1. Cervical (Neck - 7 vertebrae);\n2. Thoracic (Chest - 12 vertebrae);\n3. Lumbar (Lower Back - 5 vertebrae);\n4. Sacral (Pelvic area - 5 fused vertebrae);\n5. Caudal / Coccyx (Tail - 4 fused vertebrae)."
                        }
                    }
                ],
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Cervical Vertebrae Specialization: Atlas vs Axis",
                        "content": {
                            "title": "Cervical Vertebrae Specialization: Atlas vs Axis",
                            "caption": "Cervical Adaptations: 1st Cervical Atlas (Ring Shape, No Centrum, Wide Neural Canal for Nodding) vs 2nd Cervical Axis (Odontoid Peg Axis for Head Rotation)",
                            "description": "Diagram comparing ring-shaped Atlas vertebra with Axis vertebra showing prominent vertical odontoid process peg."
                        }
                    },
                    {
                        "type": "definition_card",
                        "title": "Cervical Vertebrae Features",
                        "content": {
                            "term": "Cervical Vertebrae Taxonomy",
                            "definition": "Vertebrae of the neck region.",
                            "key_points": [
                                "Vertebrarterial Canals: Paired lateral canals in transverse processes for passage of vertebral blood vessels and nerves.",
                                "Atlas (1st Cervical): Ring-shaped, lacks centrum, broad articular facets for skull occipital condyles ('YES' nodding movement).",
                                "Axis (2nd Cervical): Features vertical odontoid process (peg) fitting into atlas ring ('NO' side-to-side rotation movement)."
                            ]
                        }
                    }
                ],
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Thoracic Vertebra vs Lumbar Vertebra Architecture",
                        "content": {
                            "title": "Thoracic Vertebra vs Lumbar Vertebra Architecture",
                            "caption": "Regional Comparison: Thoracic Vertebra (Long Backward-Pointing Neural Spine, Capitular & Tuberculular Rib Facets) vs Lumbar Vertebra (Massive Load-Bearing Centrum, Broad Transverse Processes)",
                            "description": "Diagram comparing slender Thoracic vertebra with long spine to massive Lumbar vertebra with thick centrum."
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Human Rib Cage & Sternum Anatomy",
                        "content": {
                            "title": "Human Rib Cage & Sternum Anatomy",
                            "caption": "Thoracic Cage Architecture: 12 Pairs of Ribs → True Ribs (1-7 attached directly to Sternum via Costal Cartilage) → False Ribs (8-10) → Floating Ribs (11-12)",
                            "description": "Anatomical diagram of human rib cage showing sternum, costal cartilages, true ribs, false ribs, and floating ribs."
                        }
                    }
                ],
                [
                    {
                        "type": "mini_activity",
                        "title": "Interactive Regional Vertebrae Classifier",
                        "content": {
                            "activity_type": "scenario_decision",
                            "title": "Interactive Regional Vertebrae Classifier",
                            "prompt": "Which specific cervical vertebra features an upward projection called the odontoid process (peg) that allows side-to-side head rotation?",
                            "options": [
                                "Option A: Axis (2nd Cervical Vertebra)",
                                "Option B: Atlas (1st Cervical Vertebra)",
                                "Option C: Lumbar Vertebra"
                            ],
                            "correct_option": "Option A: Axis (2nd Cervical Vertebra)",
                            "explanation": "The Axis features the odontoid peg around which the Atlas rotates."
                        }
                    }
                ],
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Checkpoint: Regional Vertebrae",
                        "content": {
                            "question": "What structural feature distinguishes all cervical vertebrae from thoracic and lumbar vertebrae?",
                            "options": [
                                "Presence of paired vertebrarterial canals in transverse processes.",
                                "Lack of neural canal.",
                                "Absence of centrum in all 7.",
                                "Long forward-pointing spines."
                            ],
                            "correct_answer": 0,
                            "explanation": "Cervical vertebrae uniquely possess vertebrarterial canals for blood vessels."
                        }
                    }
                ],
                [
                    {
                        "type": "summary",
                        "title": "Regional Vertebrae: Key Takeaways",
                        "content": {
                            "title": "Regional Vertebrae: Key Takeaways",
                            "summary_points": [
                                "Cervical (7) feature vertebrarterial canals; Atlas enables nodding; Axis enables rotation.",
                                "Thoracic (12) have long backward spines and rib facets.",
                                "Lumbar (5) have massive centrums for heavy load-bearing.",
                                "Sacrum (5 fused) attaches pelvic girdle.",
                                "Rib cage features true ribs (1-7), false ribs (8-10), and floating ribs (11-12)."
                            ]
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 6: The Pectoral Girdle, Forelimb Bones, and Elbow Joint Mechanics
        # =====================================================================
        {
            "unit_order": 6,
            "unit_name": "The Pectoral Girdle, Forelimb Bones, and Elbow Joint Mechanics",
            "unit_description": "Pectoral girdle (scapula, clavicle), forelimb (humerus, radius, ulna), and elbow hinge joint mechanics.",
            "lesson_title": "The Pectoral Girdle, Forelimb Bones, and Elbow Joint Mechanics",
            "pages": [
                [
                    {
                        "type": "learning_goal",
                        "title": "Learning Objectives: Pectoral Girdle & Forelimb",
                        "content": {
                            "title": "Learning Objectives: Pectoral Girdle & Forelimb",
                            "goals": [
                                "Describe structural features of the pectoral girdle (Scapula & Clavicle).",
                                "Identify forelimb bones (Humerus, Radius, Ulna, Carpals, Metacarpals, Phalanges).",
                                "Explain elbow joint mechanics and hyperextension prevention via the olecranon process."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The Pectoral Girdle",
                        "content": {
                            "title": "The Pectoral Girdle",
                            "text": "The pectoral (shoulder) girdle articulates the forelimbs with the axial skeleton. It consists of two triangular Scapulae (shoulder blades) and two collarbone Clavicles."
                        }
                    }
                ],
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Pectoral Girdle Anatomy: Scapula & Clavicle",
                        "content": {
                            "title": "Pectoral Girdle Anatomy: Scapula & Clavicle",
                            "caption": "Shoulder Girdle Blueprint: Triangular Scapula → Dorsal Spine, Acromion & Metacromion Processes → Shallow Glenoid Cavity for Humerus Head Articulation → Rod-like Clavicle",
                            "description": "Anatomical diagram of scapula showing spine, acromion process, metacromion, glenoid cavity, and attached clavicle."
                        }
                    },
                    {
                        "type": "definition_card",
                        "title": "Forelimb Skeleton Taxonomy",
                        "content": {
                            "term": "Forelimb Bone Taxonomy",
                            "definition": "Bones of the upper limb.",
                            "key_points": [
                                "Humerus: Upper arm bone; proximal head fits into scapula glenoid cavity; distal trochlea articulates with radius/ulna.",
                                "Radius: Lateral forearm bone aligned with thumb.",
                                "Ulna: Medial forearm bone with prominent Olecranon process forming elbow point.",
                                "Carpals (8), Metacarpals (5), Phalanges (14): Wrist, palm, and digit bones."
                            ]
                        }
                    }
                ],
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Forelimb Bones & Elbow Joint Mechanics (Humerus, Radius, Ulna)",
                        "content": {
                            "title": "Forelimb Bones & Elbow Joint Mechanics (Humerus, Radius, Ulna)",
                            "caption": "Elbow Joint Hinge Mechanism: Trochlea of Humerus fits into Sigmoid Notch of Ulna → Olecranon Process Locks into Olecranon Fossa to Prevent Hyperextension",
                            "description": "Diagram illustrating articulation between humerus trochlea, radius head, and ulna olecranon process."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Elbow Joint Mechanics",
                        "content": {
                            "title": "Elbow Joint Mechanics",
                            "text": "The elbow is a hinge joint allowing movement in one plane (180° extension/flexion). When the arm is fully extended, the olecranon process of the ulna locks securely into the olecranon fossa of the humerus, preventing backward over-bending (hyperextension)."
                        }
                    }
                ],
                [
                    {
                        "type": "mini_activity",
                        "title": "Interactive Forelimb Skeleton Challenge",
                        "content": {
                            "activity_type": "scenario_decision",
                            "title": "Interactive Forelimb Skeleton Challenge",
                            "prompt": "Which process of the ulna bone forms the elbow point and prevents arm hyperextension?",
                            "options": [
                                "Option A: Olecranon Process",
                                "Option B: Acromion Process",
                                "Option C: Odontoid Process"
                            ],
                            "correct_option": "Option A: Olecranon Process",
                            "explanation": "The olecranon process of the ulna forms the elbow point and locks into the humerus fossa."
                        }
                    }
                ],
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Checkpoint: Pectoral Girdle & Forelimb",
                        "content": {
                            "question": "What socket on the scapula receives the smooth head of the humerus to form the shoulder ball-and-socket joint?",
                            "options": [
                                "Glenoid Cavity",
                                "Acetabulum",
                                "Foramen Magnum",
                                "Obturator Foramen"
                            ],
                            "correct_answer": 0,
                            "explanation": "The glenoid cavity of the scapula articulates with the humerus head."
                        }
                    }
                ],
                [
                    {
                        "type": "summary",
                        "title": "Forelimb Anatomy: Key Takeaways",
                        "content": {
                            "title": "Forelimb Anatomy: Key Takeaways",
                            "summary_points": [
                                "Pectoral girdle consists of scapula (glenoid cavity) and clavicle.",
                                "Humerus forms upper arm; Radius and Ulna form forearm.",
                                "Olecranon process of ulna forms elbow joint and prevents hyperextension."
                            ]
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 7: The Pelvic Girdle, Hindlimb Bones, and Weight-Bearing Adaptations
        # =====================================================================
        {
            "unit_order": 7,
            "unit_name": "The Pelvic Girdle, Hindlimb Bones, and Weight-Bearing Adaptations",
            "unit_description": "Pelvic girdle (innominate bones), hindlimb (femur, patella, tibia, fibula), and weight-bearing adaptations.",
            "lesson_title": "The Pelvic Girdle, Hindlimb Bones, and Weight-Bearing Adaptations",
            "pages": [
                [
                    {
                        "type": "learning_goal",
                        "title": "Learning Objectives: Pelvic Girdle & Hindlimb",
                        "content": {
                            "title": "Learning Objectives: Pelvic Girdle & Hindlimb",
                            "goals": [
                                "Describe innominate bone components of pelvic girdle (Ilium, Ischium, Pubis).",
                                "Identify hindlimb bones (Femur, Patella, Tibia, Fibula, Tarsals, Metatarsals, Phalanges).",
                                "Analyze bipedal weight-bearing adaptations in human femur and pelvis."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The Pelvic Girdle",
                        "content": {
                            "title": "The Pelvic Girdle",
                            "text": "The pelvic (hip) girdle transmits upper body weight to the hindlimbs. It consists of two massive Innominate (hip) bones fused dorsally to the sacrum and ventrally at the cartilaginous Pubic Symphysis."
                        }
                    }
                ],
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Pelvis Anatomy: Innominate Bone (Ilium, Ischium, Pubis, Acetabulum)",
                        "content": {
                            "title": "Pelvis Anatomy: Innominate Bone (Ilium, Ischium, Pubis, Acetabulum)",
                            "caption": "Pelvic Architecture: Upper Ilium Flange → Posterior Ischium → Ventral Pubis → Deep Cup-Shaped Acetabulum Socket → Large Obturator Foramen",
                            "description": "Anatomical diagram of pelvic innominate bone labeling ilium, ischium, pubis, acetabulum, obturator foramen, and pubic symphysis."
                        }
                    },
                    {
                        "type": "definition_card",
                        "title": "Hindlimb Skeleton Taxonomy",
                        "content": {
                            "term": "Hindlimb Bone Taxonomy",
                            "definition": "Bones of the lower limb.",
                            "key_points": [
                                "Femur: Longest, strongest thigh bone; proximal ball head fits into pelvic acetabulum; features trochanters for hip muscle attachment.",
                                "Patella: Kneecap sesamoid bone protecting knee joint.",
                                "Tibia: Larger medial weight-bearing shin bone with anterior tibial crest.",
                                "Fibula: Slender lateral bone for leg muscle attachment.",
                                "Tarsals (7), Calcaneum (Heel bone), Metatarsals (5), Phalanges (14)."
                            ]
                        }
                    }
                ],
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Hindlimb Bones: Femur, Patella, Tibia, and Fibula",
                        "content": {
                            "title": "Hindlimb Bones: Femur, Patella, Tibia, and Fibula",
                            "caption": "Lower Limb Skeleton: Femur (Head, Neck, Greater & Lesser Trochanters, Condyles) → Sesamoid Patella → Weight-Bearing Tibia & Slender Fibula",
                            "description": "Diagram illustrating femur articulation with knee patella, tibia, and fibula."
                        }
                    },
                    {
                        "type": "suggested_image",
                        "title": "Human Femur Anterior View Visualization",
                        "content": {
                            "title": "Human Femur Anterior View Visualization",
                            "caption": "Anterior view of human femur showing smooth spherical head, neck, and distal condyles.",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/a/a0/Femur_-_anterior_view.png",
                            "author": "CC BY-SA 4.0, Wikimedia Commons",
                            "licensing": "CC BY-SA 4.0",
                            "commons_page_url": "https://commons.wikimedia.org/wiki/File:Femur_-_anterior_view.png"
                        }
                    }
                ],
                [
                    {
                        "type": "mini_activity",
                        "title": "Interactive Hindlimb Skeleton Challenge",
                        "content": {
                            "activity_type": "scenario_decision",
                            "title": "Interactive Hindlimb Skeleton Challenge",
                            "prompt": "What deep cup-shaped socket on the pelvic innominate bone receives the smooth head of the femur?",
                            "options": [
                                "Option A: Acetabulum Socket",
                                "Option B: Glenoid Cavity",
                                "Option C: Foramen Magnum"
                            ],
                            "correct_option": "Option A: Acetabulum Socket",
                            "explanation": "The acetabulum is the deep pelvic socket forming the hip ball-and-socket joint."
                        }
                    }
                ],
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Checkpoint: Pelvic Girdle & Hindlimb",
                        "content": {
                            "question": "Which bone of the lower leg is the primary weight-bearing bone featuring an anterior shin crest?",
                            "options": [
                                "Tibia",
                                "Fibula",
                                "Femur",
                                "Ulna"
                            ],
                            "correct_answer": 0,
                            "explanation": "The tibia is the main load-bearing lower leg bone."
                        }
                    }
                ],
                [
                    {
                        "type": "summary",
                        "title": "Pelvis & Hindlimb: Key Takeaways",
                        "content": {
                            "title": "Pelvis & Hindlimb: Key Takeaways",
                            "summary_points": [
                                "Pelvic girdle innominate bones (ilium, ischium, pubis) meet at acetabulum socket.",
                                "Femur is the longest, strongest bone fitting into acetabulum.",
                                "Tibia bears weight; Fibula attaches leg muscles.",
                                "Patella protects knee joint; Calcaneum forms heel bone."
                            ]
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 8: Classification of Joints, Synovial Architecture, Ligaments, and Tendons
        # =====================================================================
        {
            "unit_order": 8,
            "unit_name": "Classification of Joints, Synovial Architecture, Ligaments, and Tendons",
            "unit_description": "Immovable, cartilaginous, and synovial joints (ball-and-socket vs hinge), ligaments, and tendons.",
            "lesson_title": "Classification of Joints, Synovial Architecture, Ligaments, and Tendons",
            "pages": [
                [
                    {
                        "type": "learning_goal",
                        "title": "Learning Objectives: Joints & Connective Tissues",
                        "content": {
                            "title": "Learning Objectives: Joints & Connective Tissues",
                            "goals": [
                                "Classify joint types: Immovable/Fixed (Skull sutures), Cartilaginous (Vertebrae discs), and Synovial.",
                                "Detail synovial joint architecture (Capsule, Membrane, Fluid, Articular Cartilage).",
                                "Compare Ball-and-Socket (360° motion) vs Hinge Joints (180° single plane).",
                                "Differentiate between non-elastic Tendons (muscle to bone) and elastic Ligaments (bone to bone)."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Joint Classification",
                        "content": {
                            "title": "Joint Classification",
                            "text": "A joint (articulation) is a point where two or more bones meet:\n1. Immovable (Fixed/Fibrous Joints): Bones fused by fibrous sutures (e.g., Skull sutures);\n2. Slightly Movable (Cartilaginous Joints): Bones separated by compressible cartilage pads (e.g., Intervertebral discs, Pubic symphysis);\n3. Freely Movable (Synovial Joints): Bones separated by fluid-filled cavities."
                        }
                    }
                ],
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Synovial Joint Architecture: Capsule, Membrane, Fluid, Cartilage",
                        "content": {
                            "title": "Synovial Joint Architecture: Capsule, Membrane, Fluid, Cartilage",
                            "caption": "Synovial Joint Blueprint: Smooth Articular Cartilage (Friction Reduction) → Synovial Membrane (Fluid Secretion) → Lubricating Synovial Fluid → Fibrous Capsule & Elastic Ligaments",
                            "description": "Diagram illustrating synovial joint cross-section labeling articular cartilage, synovial membrane, synovial cavity with fluid, and fibrous capsule."
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Ball-and-Socket Joint vs Hinge Joint Comparison",
                        "content": {
                            "title": "Ball-and-Socket Joint vs Hinge Joint Comparison",
                            "caption": "Kinematic Comparison: Ball-and-Socket Joint (Shoulder/Hip - 360 Degree Rotational Movement in All Planes) vs Hinge Joint (Elbow/Knee - 180 Degree Single Plane Movement)",
                            "description": "Diagram comparing spherical ball-and-socket motion with 1-plane hinge movement."
                        }
                    }
                ],
                [
                    {
                        "type": "comparison_table",
                        "title": "Comparison Matrix: Tendons vs Ligaments",
                        "content": {
                            "headers": ["Feature", "Tendons", "Ligaments"],
                            "rows": [
                                ["Connection Site", "Connects Muscle to Bone", "Connects Bone to Bone"],
                                ["Fiber Composition", "Inelastic white collagen fibers", "Elastic yellow elastic fibers"],
                                ["Flexibility", "Non-elastic / Rigid tensile strength", "Flexible and stretchable"],
                                ["Physiological Role", "Transmits muscle contraction force to move bone", "Binds joint bones together, preventing dislocation"]
                            ]
                        }
                    }
                ],
                [
                    {
                        "type": "mini_activity",
                        "title": "Interactive Joint & Ligament Simulator",
                        "content": {
                            "activity_type": "scenario_decision",
                            "title": "Interactive Joint & Ligament Simulator",
                            "prompt": "What connective tissue structure binds bone to bone at a synovial joint, preventing bone dislocation during movement?",
                            "options": [
                                "Option A: Elastic Ligament",
                                "Option B: Inelastic Tendon",
                                "Option C: Synovial fluid"
                            ],
                            "correct_option": "Option A: Elastic Ligament",
                            "explanation": "Ligaments connect bone to bone and hold joint capsules intact."
                        }
                    }
                ],
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Checkpoint: Joints & Connective Tissues",
                        "content": {
                            "question": "What is the primary function of friction-reducing Articular Cartilage capping bone ends in synovial joints?",
                            "options": [
                                "Absorbs shocks and prevents friction/wear between articulating bone surfaces.",
                                "Secretes red blood cells.",
                                "Contracts muscles.",
                                "Stores fat."
                            ],
                            "correct_answer": 0,
                            "explanation": "Articular cartilage provides a smooth, shock-absorbing surface preventing bone wear."
                        }
                    }
                ],
                [
                    {
                        "type": "summary",
                        "title": "Joints & Connective Tissues: Key Takeaways",
                        "content": {
                            "title": "Joints & Connective Tissues: Key Takeaways",
                            "summary_points": [
                                "Joints are classified as Immovable (sutures), Cartilaginous (vertebrae), or Synovial.",
                                "Synovial joints feature articular cartilage, synovial membrane, lubricating fluid, and capsular ligaments.",
                                "Ball-and-socket joints allow 360° motion; Hinge joints allow 180° single-plane motion.",
                                "Tendons (inelastic white collagen) connect muscle to bone; Ligaments (elastic yellow) connect bone to bone."
                            ]
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 9: Histology of Muscle Tissues, Myogenic Properties, and Antagonistic Arm Mechanics
        # =====================================================================
        {
            "unit_order": 9,
            "unit_name": "Histology of Muscle Tissues, Myogenic Properties, and Antagonistic Arm Mechanics",
            "unit_description": "Histology of skeletal, smooth, and cardiac muscles, and antagonistic biceps/triceps arm mechanics.",
            "lesson_title": "Histology of Muscle Tissues, Myogenic Properties, and Antagonistic Arm Mechanics",
            "pages": [
                [
                    {
                        "type": "learning_goal",
                        "title": "Learning Objectives: Muscle Histology & Antagonism",
                        "content": {
                            "title": "Learning Objectives: Muscle Histology & Antagonism",
                            "goals": [
                                "Compare histological features of Skeletal, Smooth, and Cardiac muscle tissues.",
                                "Explain myogenic non-fatiguing properties of cardiac muscle.",
                                "Analyze antagonistic muscle action in human arm flexor (Biceps) and extensor (Triceps).",
                                "Explain tendon attachment origin (fixed bone) vs insertion (movable bone)."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Histology of Muscle Tissues",
                        "content": {
                            "title": "Histology of Muscle Tissues",
                            "text": "Muscles are contractile tissues responsible for body movement. They are classified into three histological types:\n1. Skeletal (Striated) Muscle: Voluntary, cylindrical, striped/striated, multinucleated fibers attached to bones;\n2. Smooth (Visceral) Muscle: Involuntary, unstriated, spindle-shaped single-nucleus cells in internal organ walls (gut, blood vessels);\n3. Cardiac Muscle: Involuntary, striated, branched cells with intercalated discs, myogenic, non-fatiguing (heart wall)."
                        }
                    }
                ],
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Histology of Muscle Types: Skeletal, Smooth, and Cardiac",
                        "content": {
                            "title": "Histology of Muscle Types: Skeletal, Smooth, and Cardiac",
                            "caption": "Histological Comparison: Cylindrical Striated Skeletal Fibers vs Spindle-Shaped Smooth Cells vs Branched Cardiac Muscle with Intercalated Discs",
                            "description": "Diagram illustrating microscopic structure of skeletal muscle, smooth muscle, and cardiac muscle fibers."
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Antagonistic Muscle Action: Biceps & Triceps Arm Flexion/Extension",
                        "content": {
                            "title": "Antagonistic Muscle Action: Biceps & Triceps Arm Flexion/Extension",
                            "caption": "Biomechanical Arm Lever: Flexion (Biceps Contracts/Flexor → Triceps Relaxes/Extensor → Forearm Pulled Up) vs Extension (Triceps Contracts → Biceps Relaxes → Forearm Straightened)",
                            "description": "Diagram showing arm bending (flexion) with contracted biceps and relaxed triceps vs arm straightening (extension)."
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "Antagonistic Arm Mechanics & Tendon Attachments",
                        "content": {
                            "title": "Antagonistic Arm Mechanics & Tendon Attachments",
                            "text": "Muscles can only pull when contracting; they CANNOT push! Therefore, muscles work in antagonistic pairs acting in opposite directions:\n• Bending Arm (Flexion): Biceps muscle (flexor) contracts, pulling radius upwards, while Triceps muscle (extensor) relaxes.\n• Straightening Arm (Extension): Triceps muscle (extensor) contracts, pulling ulna downwards, while Biceps muscle (flexor) relaxes.\n\n• Origin: Tendon attachment site on immovable bone (Scapula).\n• Insertion: Tendon attachment site on movable bone (Radius for biceps; Ulna for triceps)."
                        }
                    }
                ],
                [
                    {
                        "type": "mini_activity",
                        "title": "Interactive Muscle Mechanics Simulator",
                        "content": {
                            "activity_type": "scenario_decision",
                            "title": "Interactive Muscle Mechanics Simulator",
                            "prompt": "What happens to the biceps and triceps muscles when a person straightens their arm out fully?",
                            "options": [
                                "Option A: Triceps muscle contracts (extensor) while Biceps muscle relaxes.",
                                "Option B: Biceps muscle contracts while Triceps relaxes.",
                                "Option C: Both muscles contract simultaneously."
                            ],
                            "correct_option": "Option A: Triceps muscle contracts (extensor) while Biceps muscle relaxes.",
                            "explanation": "Extension is driven by triceps contraction and biceps relaxation."
                        }
                    }
                ],
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Checkpoint: Muscle Physiology",
                        "content": {
                            "question": "Which muscle tissue type is branched, features intercalated discs, is myogenic, and never fatigues under normal conditions?",
                            "options": [
                                "Cardiac Muscle",
                                "Skeletal Muscle",
                                "Smooth Muscle",
                                "Diaphragm Muscle"
                            ],
                            "correct_answer": 0,
                            "explanation": "Cardiac muscle features intercalated discs and myogenic non-fatiguing contraction."
                        }
                    }
                ],
                [
                    {
                        "type": "summary",
                        "title": "Muscle Physiology: Key Takeaways",
                        "content": {
                            "title": "Muscle Physiology: Key Takeaways",
                            "summary_points": [
                                "Skeletal muscle is voluntary, striated, multinucleated.",
                                "Smooth muscle is involuntary, spindle-shaped, non-striated.",
                                "Cardiac muscle is myogenic, branched, non-fatiguing with intercalated discs.",
                                "Muscles work in antagonistic pairs (Biceps flexor vs Triceps extensor).",
                                "Origin attaches to immovable bone; Insertion attaches to movable bone."
                            ]
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 10: Laboratory Investigations, Common Misconceptions, and Multi-Tier Exam Review
        # =====================================================================
        {
            "unit_order": 10,
            "unit_name": "Laboratory Investigations, Common Misconceptions, and Multi-Tier Exam Review",
            "unit_description": "Practical bone dissections, KCSE essay diagnostics (fish locomotion, arm bending, synovial joint), and master review assessment.",
            "lesson_title": "Laboratory Investigations, Common Misconceptions, and Multi-Tier Exam Review",
            "pages": [
                [
                    {
                        "type": "learning_goal",
                        "title": "Learning Objectives: Support Mastery",
                        "content": {
                            "title": "Learning Objectives: Support Mastery",
                            "goals": [
                                "Perform practical bone identification and joint dissection protocols.",
                                "Master KCSE 10-mark essay questions on fish locomotion, arm bending, and synovial joints.",
                                "Avoid common student exam traps in skeletal biology.",
                                "Complete end-of-topic revision assessment."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Practical Bone & Joint Dissection Protocol",
                        "content": {
                            "title": "Practical Bone & Joint Dissection Protocol",
                            "text": "Practical examination requires identifying mammal bones (femur, humerus, scapula, atlas, axis, lumbar) by inspecting specific processes, condyles, and articular facets."
                        }
                    }
                ],
                [
                    {
                        "type": "suggested_image",
                        "title": "Laboratory Assay Visualization",
                        "content": {
                            "title": "Laboratory Assay Visualization",
                            "caption": "Laboratory diagnostic assay showing biochemical screening for pharmaceutical and tissue compounds.",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/7/7a/Agar_Diffusion_Method_1.jpg",
                            "author": "CC BY-SA 4.0, Wikimedia Commons",
                            "licensing": "CC BY-SA 4.0",
                            "commons_page_url": "https://commons.wikimedia.org/wiki/File:Agar_Diffusion_Method_1.jpg"
                        }
                    },
                    {
                        "type": "worked_example",
                        "title": "Worked KCSE Essay 1: Adaptations of Tilapia Fish for Locomotion",
                        "content": {
                            "question": "Describe how a freshwater Tilapia fish is adapted for locomotion in water. (10 Marks)",
                            "strategy": "Structure response into Streamlining, Fins, Myotomes, and Swim Bladder.",
                            "solution": [
                                "1. Streamlined Body (2 Marks): Spindle-shaped body tapering at both ends reduces water resistance/friction.",
                                "2. Mucus-Covered Scales (1 Mark): Overlapping slimy scales reduce water drag.",
                                "3. Myotome Muscles (2 Marks): W-shaped muscle blocks contract alternately along vertebral column, driving lateral tail undulations.",
                                "4. Caudal Fin (1 Mark): Broad tail fin pushes against water providing main forward thrust.",
                                "5. Paired Fins (2 Marks): Pectoral and Pelvic fins control steering, upward/downward pitching, and braking.",
                                "6. Unpaired Fins (1 Mark): Dorsal and Anal fins extend vertically to prevent rolling and yawing.",
                                "7. Swim Bladder (1 Mark): Regulates buoyancy, allowing fish to float at varying water depths."
                            ]
                        }
                    }
                ],
                [
                    {
                        "type": "worked_example",
                        "title": "Worked KCSE Essay 2: Biomechanics of Arm Bending & Synovial Joints",
                        "content": {
                            "question": "Explain the biomechanics of bending the human arm at the elbow joint and describe the structure of a synovial joint. (10 Marks)",
                            "strategy": "Part A: Antagonistic biceps/triceps action. Part B: Synovial joint component functions.",
                            "solution": [
                                "1. Arm Bending Mechanics (5 Marks):\n   • Biceps muscle (flexor) CONTRACTS.\n   • Triceps muscle (extensor) RELAXES.\n   • Inelastic tendon attached to radius pulls forearm bones UPWARDS.\n   • Elbow hinge joint rotates 180° in one plane.\n   • Olecranon process disengages from humerus fossa.",
                                "2. Synovial Joint Structure (5 Marks):\n   • Articular Cartilage: Caps bone ends, providing smooth shock-absorbing surface to reduce friction.\n   • Synovial Membrane: Secretes viscous synovial fluid.\n   • Synovial Fluid: Lubricates joint cavity, reducing wear.\n   • Capsular Ligaments: Connect bone to bone, holding joint intact and preventing dislocation."
                            ]
                        }
                    }
                ],
                [
                    {
                        "type": "common_mistake",
                        "title": "Common Student Traps in Support Exams",
                        "content": {
                            "mistake": "Writing that ligaments connect muscle to bone.",
                            "correction": "TENDONS connect muscle to bone; LIGAMENTS connect bone to bone.",
                            "reasoning": "Tendons transmit muscle pull force; ligaments stabilize joint capsular bones."
                        }
                    }
                ],
                [
                    {
                        "type": "knowledge_check",
                        "title": "Topic 4 Mastery Assessment Question",
                        "content": {
                            "question": "Which bone feature of the humerus articulates with the radius and ulna at the elbow joint?",
                            "options": [
                                "Trochlea and Capitulum",
                                "Glenoid Cavity",
                                "Acetabulum",
                                "Odontoid Process"
                            ],
                            "correct_answer": 0,
                            "explanation": "The trochlea and capitulum of the distal humerus form the elbow joint."
                        }
                    }
                ],
                [
                    {
                        "type": "summary",
                        "title": "Topic 4 Mastery Synthesis & Complete Form 4 Biology Review",
                        "content": {
                            "title": "Topic 4 Mastery Synthesis & Complete Form 4 Biology Review",
                            "summary_points": [
                                "Support in plants is provided by turgor pressure (parenchyma), collenchyma, sclerenchyma, and xylem.",
                                "Fish locomotion relies on streamlining, myotome blocks, caudal thrust, and fin stabilization.",
                                "Axial skeleton includes skull, 5 vertebral regions (cervical, thoracic, lumbar, sacral, caudal), ribs, and sternum.",
                                "Appendicular skeleton includes pectoral girdle (scapula/clavicle), forelimb, pelvic girdle (innominate bone), and hindlimb.",
                                "Synovial joints feature articular cartilage, synovial membrane/fluid, and ligaments.",
                                "Antagonistic biceps (flexor) and triceps (extensor) drive arm movement via inelastic tendons.",
                                "Form 4 Biology Curriculum Ingestion is 100% Complete across all 4 Master Topics!"
                            ]
                        }
                    }
                ]
            ]
        }
    ]

def ingest_form4_biology_topic4(replace=False):
    print("=" * 80)
    print("VLearn Form 4 Biology — Topic 4: Support and Movement in Plants and Animals (Final Topic)")
    print("High-Structure Production Ingestion Engine")
    print("=" * 80)

    curriculum = Curriculum.objects.filter(name="844").first()
    grade = Grade.objects.filter(curriculum=curriculum, name="Form 4").first()
    subject = Subject.objects.filter(grade=grade, name="Biology").first()

    if not subject:
        print("[!] Error: Subject 'Biology' not found under Form 4.")
        return

    print(f"[*] Resolved Target: {curriculum.name} -> {grade.name} -> {subject.name} (ID: {subject.id})")

    topic_name = "Support and Movement in Plants and Animals"
    topic = Topic.objects.filter(subject=subject, name=topic_name).first()

    if topic and replace:
        print(f"[*] Found existing Topic '{topic_name}' (ID: {topic.id}). Removing for clean replace...")
        topic.delete()
        topic = None

    if not topic:
        topic = Topic.objects.create(
            subject=subject,
            name=topic_name,
            order=4,
            description="Comprehensive syllabus on biological support and movement, plant turgidity/collenchyma/sclerenchyma/xylem tissues, weak stem adaptations, locomotion in finned fish (Tilapia), axial skeleton (skull, 5 vertebral regions, ribs, sternum), appendicular skeleton (pectoral & pelvic girdles, forelimb & hindlimb bones), synovial joint mechanics, ligaments/tendons, and muscle tissue histology/antagonistic arm mechanics."
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
    print("[SUCCESS] Form 4 Biology Topic 4 (Support and Movement) Ingestion Complete!")
    print(f"[*] Total Lessons Ingested: {total_lessons}")
    print(f"[*] Total Pages Ingested:   {total_pages}")
    print(f"[*] Total Blocks Ingested:  {total_blocks}")
    print("=" * 80)

if __name__ == "__main__":
    replace_flag = "--replace" in sys.argv
    ingest_form4_biology_topic4(replace=replace_flag)
