"""
VLearn CBC Grade 10 Geography — Topic 7: Folding
Direct Programmatic Source-Driven Ingestion Engine

Subject: Geography (Grade 10 CBC, Subject ID: 37)
Topic 7: Folding
Source: Grade 10 Geography/07_folding.md

Lessons:
  1. Introduction to Folding and Compressional Forces
  2. Anatomy of a Fold
  3. Symmetrical and Asymmetrical Folds
  4. Advanced Fold Types: Overturned, Recumbent, and Isoclinal
  5. Overthrust Folds and Nappes
  6. Monoclines, Domes, and Basins
  7. Resultant Features of Folding: Fold Mountains
  8. Global Distribution of Fold Mountains
  9. Resultant Features: Ridges, Valleys, Hogbacks, and Cuestas
  10. Significance of Folding to Human Activities
  11. Human Adaptation and Slope Management
  12. Topic Review, Modeling, and Synthesis

Usage:
  ./venv/bin/python curriculum/ingest_cbc_grade10_geography_topic7.py
"""

import os
import sys
import re
import json
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
    """Remove citation brackets ([1], [48], [S1, p. 1]) and normalize whitespace."""
    if not isinstance(raw_str, str):
        return raw_str
    cleaned = re.sub(r'\[(?:\d+|image_\d+|S\d+.*?|[\d,\s]+)\]', '', raw_str)
    cleaned = re.sub(r'[ \t]+', ' ', cleaned)
    return cleaned.strip()

def clean_content_dict(data):
    if isinstance(data, str):
        return clean_text(data)
    elif isinstance(data, list):
        return [clean_content_dict(item) for item in data]
    elif isinstance(data, dict):
        return {k: clean_content_dict(v) for k, v in data.items()}
    return data

# =============================================================================
# TOPIC 7 LESSON DEFINITIONS (12 LESSONS)
# =============================================================================
LESSONS_DATA = [
    # Lesson 1: Introduction to Folding and Compressional Forces
    {
        "unit_order": 1,
        "unit_name": "Introduction to Folding and Compressional Forces",
        "lesson_title": "Introduction to Folding and Compressional Forces",
        "pages": [
            {
                "page_number": 1,
                "page_title": "Folding Dynamics & Learning Goals",
                "blocks": [
                    {
                        "block_type": "suggested_image",
                        "component_type": "suggested_image",
                        "title": "Dramatic Folded Strata in Mountain Outcrops",
                        "content": {"text": "Folded sedimentary rock strata showing severe buckling and wavy crustal distortion under intense tectonic compression."}
                    },
                    {
                        "block_type": "learning_goal",
                        "component_type": "learning_goal",
                        "title": "Lesson Objectives: Introduction to Folding",
                        "content": {
                            "text": (
                                "By the end of this lesson, you will be able to:\n\n"
                                "- Explain the concept of folding as a fundamental process of crustal distortion\n"
                                "- Describe the role of horizontal compressional forces in initiating folding\n"
                                "- Explain how high temperature and confining pressure cause plastic deformation in deep rock strata"
                            )
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Prerequisite Spark: The Bunched Cloth Analogy",
                        "content": {
                            "text": (
                                "Have you ever pushed a tablecloth or a rug from opposite ends? Instead of sliding smoothly, "
                                "the fabric bunches up, forming a series of ridges and troughs. In exactly the same way, "
                                "solid rocks within the Earth's crust behave like plastic sheets when squeezed by massive "
                                "tectonic forces over millions of years, bending upward and downward to form mountains and valleys."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 2,
                "page_title": "Core Definitions: Folding & Crustal Stress",
                "blocks": [
                    {
                        "block_type": "definition_card",
                        "component_type": "definition_card",
                        "title": "Key Geological Definitions",
                        "content": {
                            "definitions": [
                                {
                                    "term": "Folding",
                                    "definition": "The process by which crustal rocks are distorted and bent upwards or downwards due to horizontal compressional forces within the Earth's crust.",
                                    "simple": "The bending and buckling of rock layers under lateral tectonic pressure."
                                },
                                {
                                    "term": "Compressional Forces",
                                    "definition": "Tectonic forces that squeeze or push crustal rocks together, usually acting at convergent plate boundaries.",
                                    "simple": "Squeezing forces that compress and shorten the Earth's crust."
                                },
                                {
                                    "term": "Plastic Deformation",
                                    "definition": "The permanent change in shape of a solid rock without fracturing, occurring under high temperature and confining pressure deep in the crust.",
                                    "simple": "Rock bending smoothly without breaking due to intense subterranean heat and pressure."
                                }
                            ]
                        }
                    }
                ]
            },
            {
                "page_number": 3,
                "page_title": "Mechanism of Compressional Folding",
                "blocks": [
                    {
                        "block_type": "diagram",
                        "component_type": "diagram",
                        "title": "Compressional Stress & Crustal Shortening Sequence",
                        "content": {
                            "caption": "Sequence of rock deformation: Frame A shows horizontal, undisturbed sedimentary strata squeezed by opposing inward compressional forces. Frame B shows the shortened crust buckled into alternating upfolds and downfolds."
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "The Tectonic Drivers and Squeezing Process",
                        "content": {
                            "text": (
                                "Under normal conditions at the Earth's surface, rocks are brittle and break when stressed. "
                                "However, deep within the Earth's crust, high temperatures and immense confining pressure allow rocks to undergo **plastic deformation**.\n\n"
                                "1. **The Tectonic Drivers**:\n"
                                "- When two tectonic plates collide at convergent boundaries, they generate immense horizontal compressional forces.\n\n"
                                "2. **The Squeezing Process**:\n"
                                "- As compressional forces squeeze the rock layers, they cannot expand horizontally. Instead, they buckle, shortening the horizontal distance and expanding vertically.\n"
                                "- This process occurs primarily in relatively young sedimentary rock strata, which are more flexible and layered than older crystalline rocks.\n\n"
                                "3. **Observe, Process, Result**:\n"
                                "- *Observation*: Layered sedimentary rocks exhibit a wavy, folded appearance.\n"
                                "- *Process*: Horizontal compression squeezes the strata from opposite directions.\n"
                                "- *Result*: The horizontal layers bend, shortening the crust and creating elevated ridges and low-lying troughs."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 4,
                "page_title": "Kenyan Context & Critical Distinctions",
                "blocks": [
                    {
                        "block_type": "case_study",
                        "component_type": "case_study",
                        "title": "Kenyan Case Study: Ancient Basement Folds",
                        "content": {
                            "text": (
                                "While Kenya is best known for the Great Rift Valley (which was formed by tensional forces and faulting), "
                                "the ancient Precambrian Basement rocks of the central and western highlands (such as around Machakos, "
                                "Kitui, and Kakamega) show clear signs of intense ancient folding that occurred billions of years ago "
                                "before these rocks were deeply metamorphosed, hardened, and eroded."
                            )
                        }
                    },
                    {
                        "block_type": "misconception_alert",
                        "component_type": "misconception_alert",
                        "title": "Common Misconceptions: Folding vs. Faulting",
                        "content": {
                            "text": (
                                "**Crucial Distinction: Folding vs. Faulting**\n\n"
                                "- **Folding** occurs when rock layers bend without breaking (plastic deformation under high temperature and confining pressure).\n"
                                "- **Faulting** occurs when rock layers fracture and displace along a crack (brittle deformation under tensional, compressional, or shear stress near the surface).\n\n"
                                "Never confuse folding (bending) with faulting (cracking and displacement)."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 5,
                "page_title": "Formative Assessment: Lesson 1",
                "blocks": [
                    {
                        "block_type": "multiple_choice_question",
                        "component_type": "multiple_choice_question",
                        "title": "Question 1: Primary Tectonic Force in Folding",
                        "content": {
                            "question": "Which tectonic force is primarily responsible for the process of folding?",
                            "options": [
                                "Tensional forces pulling the crust apart",
                                "Compressional forces squeezing rock layers together",
                                "Shear forces sliding crustal blocks horizontally past each other",
                                "Gravitational forces causing sudden crustal collapse"
                            ],
                            "correct_answer": "Compressional forces squeezing rock layers together",
                            "explanation": "Folding is caused by horizontal compressional forces that push rock layers together, causing them to bend and buckle. Tensional forces cause faulting and rifting, shear forces cause strike-slip faults, and gravitational forces cause mass wasting."
                        }
                    },
                    {
                        "block_type": "multiple_choice_question",
                        "component_type": "multiple_choice_question",
                        "title": "Question 2: Deep Crustal Plastic Deformation",
                        "content": {
                            "question": "Why do rocks undergo folding rather than fracturing deep within the Earth's crust?",
                            "options": [
                                "Because deep rocks are cold and brittle",
                                "Because deep sedimentary rocks are dry and loose",
                                "High temperatures and confining pressure make deep rocks undergo plastic deformation",
                                "Tectonic forces deep in the Earth are always extremely weak"
                            ],
                            "correct_answer": "High temperatures and confining pressure make deep rocks undergo plastic deformation",
                            "explanation": "Deep within the crust, extreme heat and the immense weight of overlying rocks (confining pressure) make rocks ductile, allowing them to bend plastically instead of shattering like brittle surface rocks."
                        }
                    }
                ]
            }
        ]
    },

    # Lesson 2: Anatomy of a Fold
    {
        "unit_order": 2,
        "unit_name": "Anatomy of a Fold",
        "lesson_title": "Anatomy of a Fold",
        "pages": [
            {
                "page_number": 1,
                "page_title": "Fold Anatomy & Learning Goals",
                "blocks": [
                    {
                        "block_type": "suggested_image",
                        "component_type": "suggested_image",
                        "title": "Natural Anticline and Syncline Outcrops",
                        "content": {"text": "A geological rock exposure displaying clear upward arching anticlines and downward trough synclines."}
                    },
                    {
                        "block_type": "learning_goal",
                        "component_type": "learning_goal",
                        "title": "Lesson Objectives: Anatomy of a Fold",
                        "content": {
                            "text": (
                                "By the end of this lesson, you will be able to:\n\n"
                                "- Identify and label the structural components of a fold (anticline, syncline, limb, axial plane, crest, trough, hinge line)\n"
                                "- Differentiate between anticlines and synclines based on rock layer age and geometry\n"
                                "- Describe the geometric role of the fold axis and axial plane"
                            )
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Prerequisite Spark: The Corrugated Iron Sheet",
                        "content": {
                            "text": (
                                "Think of a corrugated iron sheet (mabati) used for roofing across Kenya. The sheet is not flat; "
                                "it has alternating raised ridges and dipped troughs. In geological terminology, the raised waves are "
                                "'anticlines' and the dipped channels are 'synclines'. Geologists use these structural anatomical terms "
                                "to map underground rock geometry for engineering, mining, and water extraction."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 2,
                "page_title": "Core Anatomical Definitions",
                "blocks": [
                    {
                        "block_type": "definition_card",
                        "component_type": "definition_card",
                        "title": "Structural Fold Components",
                        "content": {
                            "definitions": [
                                {
                                    "term": "Anticline",
                                    "definition": "An upward-arching fold where the older rock layers are at the core and the younger layers dip away from the center (forming an 'A' shape).",
                                    "simple": "The upward arch or crest of a geological fold."
                                },
                                {
                                    "term": "Syncline",
                                    "definition": "A downward-arching, trough-like fold where the youngest rock layers are at the core and the older layers dip toward the center (forming a 'U' shape).",
                                    "simple": "The downward trough or dip of a geological fold."
                                },
                                {
                                    "term": "Limbs",
                                    "definition": "The flanking sides or sloping rock layers of a fold that extend away from the crest or trough.",
                                    "simple": "The sloping sides connecting fold crests and troughs."
                                },
                                {
                                    "term": "Axial Plane",
                                    "definition": "An imaginary plane that divides a fold as symmetrically as possible, passing through the hinge of each folded layer.",
                                    "simple": "An imaginary dividing sheet bisecting the fold."
                                },
                                {
                                    "term": "Hinge / Fold Axis",
                                    "definition": "The line of maximum curvature along a folded rock layer.",
                                    "simple": "The central axis line along which rock strata bend most sharply."
                                }
                            ]
                        }
                    }
                ]
            },
            {
                "page_number": 3,
                "page_title": "Structural Anatomy Diagram",
                "blocks": [
                    {
                        "block_type": "diagram",
                        "component_type": "diagram",
                        "title": "3D Anatomical Block Diagram of a Fold",
                        "content": {
                            "caption": "Comprehensive 3D geological block diagram showing an anticline, syncline, limbs, semi-transparent axial plane, fold axis/hinge line, crest, and trough."
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Dissecting the Geological Wave",
                        "content": {
                            "text": (
                                "A single folded structure consists of several precise anatomical parts:\n\n"
                                "1. **The Crest**: The highest point or apex of an upfold (anticline).\n"
                                "2. **The Trough**: The lowest point or base of a downfold (syncline).\n"
                                "3. **The Limbs (Flanks)**: The sections of rock strata between the crest and trough. A fold always has two limbs.\n"
                                "4. **The Axial Plane**: The imaginary surface bisecting the angle between the limbs. If compressional forces were equal from both sides, the axial plane is vertical; if unequal, it tilts.\n"
                                "5. **Stratigraphic Principle**: In an undisturbed anticline, the oldest rock strata reside at the core; in a syncline, the youngest rocks form the central core."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 4,
                "page_title": "Field Observation & Local Context",
                "blocks": [
                    {
                        "block_type": "case_study",
                        "component_type": "case_study",
                        "title": "Field Observation: Road Cuts on Kenyan Highways",
                        "content": {
                            "text": (
                                "When travelling along Kenyan highways through the Rift Valley escarpments (such as the Mai Mahiu or "
                                "Nakuru-Nairobi road cuttings), deep excavations expose stratified volcanic ash and sedimentary beds. "
                                "In several sections, you can observe miniature anticlines and synclines where ancient ash beds were warped "
                                "and bent by localized crustal stresses before solidifying."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 5,
                "page_title": "Formative Assessment: Lesson 2",
                "blocks": [
                    {
                        "block_type": "multiple_choice_question",
                        "component_type": "multiple_choice_question",
                        "title": "Question 1: Downward-Arching Fold",
                        "content": {
                            "question": "What is the term for the downward-arching, trough-like part of a fold?",
                            "options": [
                                "Anticline",
                                "Syncline",
                                "Limb",
                                "Axial Plane"
                            ],
                            "correct_answer": "Syncline",
                            "explanation": "A syncline is the downward-arching, trough-shaped fold ('U' shaped). An anticline is the upward-arching ridge, a limb is the sloping flank, and the axial plane is the imaginary dividing surface."
                        }
                    },
                    {
                        "block_type": "multiple_choice_question",
                        "component_type": "multiple_choice_question",
                        "title": "Question 2: Bisecting Plane",
                        "content": {
                            "question": "The imaginary plane that bisects a fold as symmetrically as possible is known as the:",
                            "options": [
                                "Strike plane",
                                "Hinge line",
                                "Crest plane",
                                "Axial plane"
                            ],
                            "correct_answer": "Axial plane",
                            "explanation": "The axial plane is the imaginary plane that divides the fold into two halves as symmetrically as possible. The hinge line is the linear line of maximum curvature."
                        }
                    }
                ]
            }
        ]
    },

    # Lesson 3: Symmetrical and Asymmetrical Folds
    {
        "unit_order": 3,
        "unit_name": "Symmetrical and Asymmetrical Folds",
        "lesson_title": "Symmetrical and Asymmetrical Folds",
        "pages": [
            {
                "page_number": 1,
                "page_title": "Fold Symmetry & Learning Goals",
                "blocks": [
                    {
                        "block_type": "suggested_image",
                        "component_type": "suggested_image",
                        "title": "Asymmetric Geological Kink Fold in Bedrock",
                        "content": {"text": "A natural rock exposure showing an asymmetric fold where one limb dips significantly steeper than the other."}
                    },
                    {
                        "block_type": "learning_goal",
                        "component_type": "learning_goal",
                        "title": "Lesson Objectives: Symmetrical vs Asymmetrical Folds",
                        "content": {
                            "text": (
                                "By the end of this lesson, you will be able to:\n\n"
                                "- Explain how variations in compressional force magnitude produce symmetrical versus asymmetrical folds\n"
                                "- Differentiate between symmetrical and asymmetrical folds based on limb dip angles and axial plane inclination\n"
                                "- Interpret geological cross-sections showing balanced and unbalanced crustal stresses"
                            )
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Prerequisite Spark: The Two-Sided Push",
                        "content": {
                            "text": (
                                "Imagine pushing a box from opposite sides with exactly equal strength. It stays upright and centered. "
                                "Now imagine a friend pushes much harder from the left than you do from the right. The box tilts and leans "
                                "toward you! This unequal push is exactly how asymmetrical landforms are shaped in nature when tectonic "
                                "forces from one plate boundary exceed opposing resistance."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 2,
                "page_title": "Core Definitions: Fold Symmetry",
                "blocks": [
                    {
                        "block_type": "definition_card",
                        "component_type": "definition_card",
                        "title": "Definitions: Symmetrical and Asymmetrical Folds",
                        "content": {
                            "definitions": [
                                {
                                    "term": "Symmetrical Fold (Simple Fold)",
                                    "definition": "A fold in which the limbs dip at approximately the exact same angle away from a vertical axial plane.",
                                    "simple": "A balanced, upright fold with equal slopes on both sides."
                                },
                                {
                                    "term": "Asymmetrical Fold",
                                    "definition": "A fold in which the limbs dip at different angles from an inclined (tilted) axial plane, with one limb being steeper than the other.",
                                    "simple": "An unbalanced fold with one gentle slope and one steep slope."
                                }
                            ]
                        }
                    }
                ]
            },
            {
                "page_number": 3,
                "page_title": "Comparative Mechanics & Geometry",
                "blocks": [
                    {
                        "block_type": "diagram",
                        "component_type": "diagram",
                        "title": "Symmetrical vs. Asymmetrical Folds Comparison",
                        "content": {
                            "caption": "Side-by-side comparison: Left shows a symmetrical anticline formed by equal forces with a vertical axial plane (45° equal dip). Right shows an asymmetrical anticline formed by unequal forces with an inclined axial plane (25° gentle dip vs. 70° steep dip)."
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Force Dynamics: Equal vs. Unequal Compression",
                        "content": {
                            "text": (
                                "1. **Symmetrical Folds**:\n"
                                "- *Mechanism*: Formed when horizontal compressional forces of equal magnitude act on rock layers from opposite directions.\n"
                                "- *Geometry*: The axial plane is perfectly vertical. Both limbs slope away from the crest (or toward the trough) at identical angles.\n\n"
                                "2. **Asymmetrical Folds**:\n"
                                "- *Mechanism*: Formed when the compressional force from one direction is significantly stronger than the force from the opposite direction.\n"
                                "- *Geometry*: The axial plane is tilted (inclined). One limb is longer with a gentle slope (gentle dip), while the other limb is shorter and much steeper (steep dip)."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 4,
                "page_title": "Formative Assessment: Lesson 3",
                "blocks": [
                    {
                        "block_type": "multiple_choice_question",
                        "component_type": "multiple_choice_question",
                        "title": "Question 1: Formation of Asymmetrical Folds",
                        "content": {
                            "question": "Which of the following conditions leads to the formation of an asymmetrical fold?",
                            "options": [
                                "Compressional forces of equal magnitude acting from opposite sides",
                                "Tensional forces pulling the rock layers apart equally",
                                "Compressional forces of unequal magnitude, where one side is stronger than the other",
                                "Vertical gravitational collapse of an ancient magma chamber"
                            ],
                            "correct_answer": "Compressional forces of unequal magnitude, where one side is stronger than the other",
                            "explanation": "Asymmetrical folds form when compressional forces are unequal, tilting the axial plane and causing one limb to dip steeper than the other. Equal compressional forces produce symmetrical folds."
                        }
                    },
                    {
                        "block_type": "multiple_choice_question",
                        "component_type": "multiple_choice_question",
                        "title": "Question 2: Axial Plane in Symmetrical Folds",
                        "content": {
                            "question": "In a symmetrical fold, the axial plane is:",
                            "options": [
                                "Nearly horizontal",
                                "Perfectbly vertical",
                                "Tilted at a 45-degree angle",
                                "Curved into an 'S' shape"
                            ],
                            "correct_answer": "Perfectbly vertical",
                            "explanation": "By definition, a symmetrical fold has a perfectly vertical axial plane because compressional forces pushing from both sides are equal in magnitude."
                        }
                    }
                ]
            }
        ]
    },

    # Lesson 4: Advanced Fold Types: Overturned, Recumbent, and Isoclinal
    {
        "unit_order": 4,
        "unit_name": "Advanced Fold Types: Overturned, Recumbent, and Isoclinal",
        "lesson_title": "Advanced Fold Types: Overturned, Recumbent, and Isoclinal",
        "pages": [
            {
                "page_number": 1,
                "page_title": "Extreme Fold Structures & Learning Goals",
                "blocks": [
                    {
                        "block_type": "suggested_image",
                        "component_type": "suggested_image",
                        "title": "Recumbent Quartz Mica Schist Fold Structure",
                        "content": {"text": "A geological outcrop in metamorphic bedrock displaying extreme recumbent folding with horizontal limbs."}
                    },
                    {
                        "block_type": "learning_goal",
                        "component_type": "learning_goal",
                        "title": "Lesson Objectives: Advanced Fold Types",
                        "content": {
                            "text": (
                                "By the end of this lesson, you will be able to:\n\n"
                                "- Classify advanced fold types based on escalating tectonic stress (overturned, recumbent, and isoclinal)\n"
                                "- Explain the phenomenon of stratigraphic inversion in overturned and recumbent folds\n"
                                "- Recognize and illustrate the progressive stages of intense crustal deformation"
                            )
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Prerequisite Spark: The Rolling Paper Fold",
                        "content": {
                            "text": (
                                "Have you ever folded a piece of paper, then kept pushing it from one side until the fold fell completely flat "
                                "on the table, lying horizontal? If you do this, the top half of the paper lies directly on top of the bottom half. "
                                "This is exactly what happens to miles of solid crust when tectonic plates collide with extreme force over tens of millions of years!"
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 2,
                "page_title": "Core Definitions: Advanced Fold Types",
                "blocks": [
                    {
                        "block_type": "definition_card",
                        "component_type": "definition_card",
                        "title": "Definitions: Overturned, Recumbent & Isoclinal Folds",
                        "content": {
                            "definitions": [
                                {
                                    "term": "Overturned Fold (Overfold)",
                                    "definition": "An asymmetrical fold where one limb has been pushed past the vertical so that both limbs dip in the same direction, with one limb inverted.",
                                    "simple": "A severely tilted fold where rock layers have rolled past vertical."
                                },
                                {
                                    "term": "Recumbent Fold",
                                    "definition": "An extreme overturned fold where the axial plane is nearly horizontal and both limbs lie flat, parallel to the ground.",
                                    "simple": "A fold that has rolled over completely flat like a folded blanket."
                                },
                                {
                                    "term": "Isoclinal Fold",
                                    "definition": "A fold structure where limbs are parallel to each other and dip in the same direction at identical angles, packed tightly like accordion pleats.",
                                    "simple": "Parallel rock limbs squeezed tightly together by intense uniform compression."
                                }
                            ]
                        }
                    }
                ]
            },
            {
                "page_number": 3,
                "page_title": "The Continuum of Compression",
                "blocks": [
                    {
                        "block_type": "diagram",
                        "component_type": "diagram",
                        "title": "Progressive Fold Evolution: Overturned, Recumbent & Isoclinal",
                        "content": {
                            "caption": "Four-panel progressive deformation sequence: Panel 1 Asymmetrical fold, Panel 2 Overturned fold (limbs dip in same direction), Panel 3 Recumbent fold (horizontal axial plane), Panel 4 Isoclinal fold (tightly compressed parallel limbs)."
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Progressive Stages of Extreme Folding",
                        "content": {
                            "text": (
                                "As compressional tectonic forces intensify over geological time, folds undergo a progressive sequence:\n\n"
                                "1. **Overturned Fold**:\n"
                                "- Compression from one side is so overwhelming that it pushes the anticline over past 90 degrees.\n"
                                "- Both limbs dip in the same direction, and the overturned limb exhibits **stratigraphic inversion** (older rocks resting above younger strata).\n\n"
                                "2. **Recumbent Fold**:\n"
                                "- Under prolonged extreme compression, the axial plane tilts until it is virtually horizontal.\n"
                                "- The rock strata are folded back on themselves like a rolled-up sleeping bag.\n\n"
                                "3. **Isoclinal Fold**:\n"
                                "- Formed when intense, uniform compressional forces squeeze the strata so tightly that the limbs become parallel to each other, sharing identical dip angles."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 4,
                "page_title": "Formative Assessment: Lesson 4",
                "blocks": [
                    {
                        "block_type": "multiple_choice_question",
                        "component_type": "multiple_choice_question",
                        "title": "Question 1: Recumbent Fold Characteristic",
                        "content": {
                            "question": "What is the defining characteristic of a recumbent fold?",
                            "options": [
                                "Its limbs dip in opposite directions at 45 degrees",
                                "Its axial plane is nearly horizontal, with limbs lying parallel to the ground",
                                "It has only one limb that is steep and step-like",
                                "It is formed by tensional forces pulling the crust apart"
                            ],
                            "correct_answer": "Its axial plane is nearly horizontal, with limbs lying parallel to the ground",
                            "explanation": "A recumbent fold is characterized by a nearly horizontal axial plane, meaning the rock layers have been folded over so far that they lie flat, parallel to the ground."
                        }
                    },
                    {
                        "block_type": "multiple_choice_question",
                        "component_type": "multiple_choice_question",
                        "title": "Question 2: Parallel Limb Folds",
                        "content": {
                            "question": "In which fold type are the limbs parallel to each other, dipping in the same direction at the same angle?",
                            "options": [
                                "Symmetrical fold",
                                "Asymmetrical fold",
                                "Isoclinal fold",
                                "Monocline"
                            ],
                            "correct_answer": "Isoclinal fold",
                            "explanation": "In an isoclinal fold, intense compression squeezes the limbs until they are parallel to one another, sharing the same dip direction and angle."
                        }
                    }
                ]
            }
        ]
    },

    # Lesson 5: Overthrust Folds and Nappes
    {
        "unit_order": 5,
        "unit_name": "Overthrust Folds and Nappes",
        "lesson_title": "Overthrust Folds and Nappes",
        "pages": [
            {
                "page_number": 1,
                "page_title": "Thrust Faulting & Learning Goals",
                "blocks": [
                    {
                        "block_type": "suggested_image",
                        "component_type": "suggested_image",
                        "title": "The World-Famous Glarus Thrust Fault",
                        "content": {"text": "A world-renowned geological outcrop in the Swiss Alps showing an overthrust fault where ancient rock layers have ridden over younger strata."}
                    },
                    {
                        "block_type": "learning_goal",
                        "component_type": "learning_goal",
                        "title": "Lesson Objectives: Overthrust Folds and Nappes",
                        "content": {
                            "text": (
                                "By the end of this lesson, you will be able to:\n\n"
                                "- Explain how extreme folding transitions into thrust faulting, producing overthrust folds and nappes\n"
                                "- Define thrust fault, overthrust fold, and nappe\n"
                                "- Describe the mechanics of massive horizontal rock sheet displacement"
                            )
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Prerequisite Spark: The Snapping Ruler Analogy",
                        "content": {
                            "text": (
                                "If you bend a plastic ruler, it curves smoothly at first. But if you keep bending it past its elastic limit, "
                                "*SNAP!* It fractures. Rock strata behave the same way: if they are compressed beyond their plastic limit, "
                                "they fracture along a low-angle crack (thrust fault), and one massive slab of rock climbs up and slides "
                                "kilometers over the adjacent block!"
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 2,
                "page_title": "Core Definitions: Thrust Faults & Nappes",
                "blocks": [
                    {
                        "block_type": "definition_card",
                        "component_type": "definition_card",
                        "title": "Definitions: Overthrusts and Nappes",
                        "content": {
                            "definitions": [
                                {
                                    "term": "Thrust Fault",
                                    "definition": "A low-angle fracture in the Earth's crust along which older rocks are pushed up and over younger rocks under compressional stress.",
                                    "simple": "A low-angle crack along which compressed rock blocks slide over each other."
                                },
                                {
                                    "term": "Overthrust Fold",
                                    "definition": "A severely compressed fold that has fractured along its axial plane, allowing one limb to slide over the other.",
                                    "simple": "A broken fold where the upper block slides over the lower block."
                                },
                                {
                                    "term": "Nappe",
                                    "definition": "A large sheet or body of rock that has been folded, sheared, and displaced horizontally over distances of several kilometers along a thrust fault.",
                                    "simple": "A massive displaced rock sheet that has travelled far from its origin along a thrust plane."
                                }
                            ]
                        }
                    }
                ]
            },
            {
                "page_number": 3,
                "page_title": "The Step-by-Step Transition",
                "blocks": [
                    {
                        "block_type": "diagram",
                        "component_type": "diagram",
                        "title": "Formation of Overthrust Folds and Nappes",
                        "content": {
                            "caption": "Step-by-step diagram: Step A shows a strained recumbent fold with a developing fracture plane. Step B shows fracture along the thrust fault and upward sliding. Step C shows the displaced nappe sheet overriding younger rock strata."
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "The Transition from Fold to Fault",
                        "content": {
                            "text": (
                                "When compressional tectonic stress exceeds the rock's shear strength, folding gives way to faulting:\n\n"
                                "1. **Stage 1: Extreme Compression**: Rocks are squeezed beyond their plastic limit into a strained recumbent fold.\n"
                                "2. **Stage 2: Shearing and Fracturing**: High friction and stress cause a fracture plane to develop along the lower limb (the *thrust fault*).\n"
                                "3. **Stage 3: Displacement (Overthrust)**: The upper limb slips along the low-angle thrust fault and slides horizontally over the lower limb.\n"
                                "4. **Stage 4: Nappe Formation**: The overriding rock sheet (which can be hundreds of meters thick and dozens of kilometers wide) travels far from its original geological position, resting on completely unrelated younger rocks."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 4,
                "page_title": "Formative Assessment: Lesson 5",
                "blocks": [
                    {
                        "block_type": "multiple_choice_question",
                        "component_type": "multiple_choice_question",
                        "title": "Question 1: Fold Fracturing Mechanism",
                        "content": {
                            "question": "When a recumbent fold fractures along its axial plane and one block slides over the other, it forms an:",
                            "options": [
                                "Symmetrical fold",
                                "Overthrust fold",
                                "Anticlinorium",
                                "Monocline"
                            ],
                            "correct_answer": "Overthrust fold",
                            "explanation": "An overthrust fold is created when a recumbent fold fractures due to extreme compression, allowing one block of rock to slide over the other along a low-angle thrust fault."
                        }
                    },
                    {
                        "block_type": "multiple_choice_question",
                        "component_type": "multiple_choice_question",
                        "title": "Question 2: Geological Definition of Nappe",
                        "content": {
                            "question": "What is a 'nappe' in structural geography?",
                            "options": [
                                "A deep depression filled with ocean water",
                                "A small volcanic cinder cone",
                                "A large sheet of rock displaced horizontally over miles along a thrust fault",
                                "A simple step-like bend in horizontal rock layers"
                            ],
                            "correct_answer": "A large sheet of rock displaced horizontally over miles along a thrust fault",
                            "explanation": "A nappe is a massive sheet of rock that has been folded, sheared, and displaced horizontally over several kilometers along a low-angle thrust fault plane."
                        }
                    }
                ]
            }
        ]
    },

    # Lesson 6: Monoclines, Domes, and Basins
    {
        "unit_order": 6,
        "unit_name": "Monoclines, Domes, and Basins",
        "lesson_title": "Monoclines, Domes, and Basins",
        "pages": [
            {
                "page_number": 1,
                "page_title": "Non-Linear Warps & Learning Goals",
                "blocks": [
                    {
                        "block_type": "suggested_image",
                        "component_type": "suggested_image",
                        "title": "The Waterpocket Fold Monocline at Capitol Reef",
                        "content": {"text": "A panoramic geological view of a classic monocline where horizontal rock strata bend into a giant step-like fold."}
                    },
                    {
                        "block_type": "learning_goal",
                        "component_type": "learning_goal",
                        "title": "Lesson Objectives: Monoclines, Domes, and Basins",
                        "content": {
                            "text": (
                                "By the end of this lesson, you will be able to:\n\n"
                                "- Describe the characteristics and vertical formation mechanism of monoclines\n"
                                "- Differentiate between structural domes and structural basins based on rock age distribution\n"
                                "- Explain how vertical uplift, subsidence, and magma intrusion create circular and step-like structures"
                            )
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Prerequisite Spark: The Hidden Book Under the Carpet",
                        "content": {
                            "text": (
                                "Imagine a flat carpet lying on a floor. If you place a thick book beneath one half of the carpet, "
                                "the carpet will bend upward into a step-like slope before flattening out again on top of the book. "
                                "This step-like bend is a **monocline**, and it shows how flexible surface rock layers drape over deep "
                                "vertical fault blocks below!"
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 2,
                "page_title": "Core Definitions: Monoclines, Domes & Basins",
                "blocks": [
                    {
                        "block_type": "definition_card",
                        "component_type": "definition_card",
                        "title": "Definitions: Monocline, Dome, and Basin",
                        "content": {
                            "definitions": [
                                {
                                    "term": "Monocline",
                                    "definition": "A simple, step-like bend in otherwise horizontal or gently dipping rock layers.",
                                    "simple": "A single step-like fold draped over a deep vertical fault."
                                },
                                {
                                    "term": "Structural Dome",
                                    "definition": "A circular or elliptical upward-warping of rock layers where the oldest rocks are exposed at the center and layers dip outward in all directions.",
                                    "simple": "An upward circular bulge with oldest rocks in the center."
                                },
                                {
                                    "term": "Structural Basin",
                                    "definition": "A circular or elliptical downward-warping of rock layers where the youngest rocks are at the center and layers dip inward from all directions.",
                                    "simple": "A downward circular bowl with youngest rocks in the center."
                                }
                            ]
                        }
                    }
                ]
            },
            {
                "page_number": 3,
                "page_title": "3D Structural Comparison",
                "blocks": [
                    {
                        "block_type": "diagram",
                        "component_type": "diagram",
                        "title": "Monoclines, Structural Domes, and Structural Basins",
                        "content": {
                            "caption": "Three-part structural diagram: 1. Monocline draped over a vertical basement fault. 2. Structural Dome showing oldest layers exposed in center dipping outward. 3. Structural Basin showing youngest layers in center dipping inward."
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Mechanics of Vertical Warping",
                        "content": {
                            "text": (
                                "1. **Monoclines (Step Folds)**:\n"
                                "- Formed when deep crystalline basement rock undergoes vertical faulting.\n"
                                "- The flexible sedimentary layers above do not crack; they bend and drape over the fault block like a tablecloth.\n\n"
                                "2. **Structural Domes (Upward Bulges)**:\n"
                                "- Resemble an upside-down bowl. Caused by localized vertical forces such as rising magma intrusions (laccoliths) or salt domes.\n"
                                "- After erosion planes off the top, the **oldest rocks are exposed at the center**, surrounded by concentric rings of younger strata.\n\n"
                                "3. **Structural Basins (Downward Bowls)**:\n"
                                "- Resemble a bowl right-side up. Formed by regional crustal subsidence or sediment loading.\n"
                                "- The **youngest rocks are preserved at the center**, surrounded by older strata dipping inward."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 4,
                "page_title": "Formative Assessment: Lesson 6",
                "blocks": [
                    {
                        "block_type": "multiple_choice_question",
                        "component_type": "multiple_choice_question",
                        "title": "Question 1: Circular Rock Patterns with Oldest Center",
                        "content": {
                            "question": "If you find a geological structure where rock layers form a circular pattern with the OLDEST rocks exposed at the very center, you are looking at a:",
                            "options": [
                                "Syncline",
                                "Structural Basin",
                                "Structural Dome",
                                "Recumbent Fold"
                            ],
                            "correct_answer": "Structural Dome",
                            "explanation": "A structural dome is an upward circular warp. When erosion slices across the top, the oldest, deepest rock layers are exposed in the center, with younger layers dipping outward."
                        }
                    },
                    {
                        "block_type": "multiple_choice_question",
                        "component_type": "multiple_choice_question",
                        "title": "Question 2: Step-Like Fold Identification",
                        "content": {
                            "question": "Which geological feature is characterized by a simple, step-like bend in otherwise horizontal rock strata?",
                            "options": [
                                "Symmetrical fold",
                                "Monocline",
                                "Overfold",
                                "Nappe"
                            ],
                            "correct_answer": "Monocline",
                            "explanation": "A monocline is a single, step-like fold in otherwise horizontal or gently dipping layers, often draped over a deep-seated basement fault."
                        }
                    }
                ]
            }
        ]
    },

    # Lesson 7: Resultant Features of Folding: Fold Mountains
    {
        "unit_order": 7,
        "unit_name": "Resultant Features of Folding: Fold Mountains",
        "lesson_title": "Resultant Features of Folding: Fold Mountains",
        "pages": [
            {
                "page_number": 1,
                "page_title": "Fold Mountain Giants & Learning Goals",
                "blocks": [
                    {
                        "block_type": "suggested_image",
                        "component_type": "suggested_image",
                        "title": "The Towering Himalayan Fold Mountain Range",
                        "content": {"text": "Panoramic view of Mount Everest and the Himalayan fold mountain chain showing towering folded rock peaks and deep glacial valleys."}
                    },
                    {
                        "block_type": "learning_goal",
                        "component_type": "learning_goal",
                        "title": "Lesson Objectives: Fold Mountains Formation",
                        "content": {
                            "text": (
                                "By the end of this lesson, you will be able to:\n\n"
                                "- Explain how large-scale plate convergence builds massive Fold Mountain ranges (orogenesis)\n"
                                "- Describe the three stages of the geosynclinal orogenic cycle\n"
                                "- Relate thick marine sedimentary rock sequences to mountain building"
                            )
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Prerequisite Spark: Earth's Colossal Crumple Zones",
                        "content": {
                            "text": (
                                "If you look at world maps, the highest, most rugged, and longest mountain ranges on Earth—such as the "
                                "snow-capped Himalayas in Asia or the towering Andes in South America—are not volcanoes. They are Fold Mountains! "
                                "They are the colossal 'crumple zones' of our planet, formed where entire tectonic plates crash into each "
                                "other in slow motion over millions of years."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 2,
                "page_title": "Core Definitions: Orogeny & Geosynclines",
                "blocks": [
                    {
                        "block_type": "definition_card",
                        "component_type": "definition_card",
                        "title": "Definitions: Fold Mountains, Orogeny, Geosyncline",
                        "content": {
                            "definitions": [
                                {
                                    "term": "Fold Mountains",
                                    "definition": "Massive mountain ranges created by the folding and uplifting of thick sedimentary rock layers along convergent tectonic plate boundaries.",
                                    "simple": "Great mountain chains formed by colliding tectonic plates squeezing rock strata."
                                },
                                {
                                    "term": "Orogeny",
                                    "definition": "A specific geological period of mountain-building activity caused by plate tectonics, involving folding, faulting, metamorphism, and igneous activity.",
                                    "simple": "The mountain-building episode driven by plate tectonics."
                                },
                                {
                                    "term": "Geosyncline",
                                    "definition": "A vast, elongated, water-filled marine depression where thick layers of sediments accumulate over millions of years before being compressed into mountains.",
                                    "simple": "A giant marine sediment basin that becomes the raw material for fold mountains."
                                }
                            ]
                        }
                    }
                ]
            },
            {
                "page_number": 3,
                "page_title": "The Geosynclinal Orogenic Cycle",
                "blocks": [
                    {
                        "block_type": "diagram",
                        "component_type": "diagram",
                        "title": "Geosynclinal Fold Mountain Formation Stages",
                        "content": {
                            "caption": "Three-stage orogenic cycle: Panel A shows thick sediment accumulation in an oceanic geosyncline. Panel B shows converging plates squeezing and folding the strata. Panel C shows complete ocean basin closure, extreme crustal shortening, and uplift of towering fold mountain ranges."
                        }
                    },
                    {
                        "block_type": "video",
                        "component_type": "video",
                        "title": "Fold Mountain Formation and Continental Collision",
                        "content": {
                            "url": "https://www.youtube.com/watch?v=1O945h3Gq4A",
                            "caption": "Scientific animation illustrating how convergent plate boundaries compress oceanic geosynclines and elevate massive fold mountain ranges like the Himalayas."
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "How Fold Mountains are Born: The Three Stages",
                        "content": {
                            "text": (
                                "The birth of a fold mountain range follows three distinct geological stages:\n\n"
                                "1. **Stage 1: Sedimentation in Geosynclines**:\n"
                                "- Rivers carry vast quantities of sand, mud, and marine shells into a broad ocean basin (geosyncline) between two continental masses.\n"
                                "- Over tens of millions of years, these compress into sedimentary rocks thousands of meters thick.\n\n"
                                "2. **Stage 2: Compression and Buckling**:\n"
                                "- The tectonic plates flanking the basin begin converging.\n"
                                "- Immense horizontal compressional forces squeeze the sediment strata, forcing them to buckle into tight folds on the ocean floor.\n\n"
                                "3. **Stage 3: Uplift and Mountain Building**:\n"
                                "- As the plates collide fully, the ocean basin closes completely.\n"
                                "- Unable to sink into the dense mantle, the rock strata are forced skyward, producing towering mountain ridges, deep synclinal valleys, and complex thrust faults."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 4,
                "page_title": "African Continental Context",
                "blocks": [
                    {
                        "block_type": "case_study",
                        "component_type": "case_study",
                        "title": "African Context: Atlas & Cape Fold Mountains",
                        "content": {
                            "text": (
                                "While East Africa's relief is characterized by volcanic peaks (like Mt. Kenya and Mt. Kilimanjaro) and "
                                "fault-block mountains (like the Ruwenzori), other parts of Africa feature famous Fold Mountain systems:\n\n"
                                "- **The Atlas Mountains** (North Africa: Morocco, Algeria, Tunisia): Formed by the convergence of the African and Eurasian plates.\n"
                                "- **The Cape Fold Mountains** (South Africa): Formed during an ancient orogenic episode, displaying parallel ridges and valleys of sandstone and shale."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 5,
                "page_title": "Formative Assessment: Lesson 7",
                "blocks": [
                    {
                        "block_type": "multiple_choice_question",
                        "component_type": "multiple_choice_question",
                        "title": "Question 1: Plate Boundary Type for Fold Mountains",
                        "content": {
                            "question": "Fold Mountains are formed primarily along which type of plate boundary?",
                            "options": [
                                "Divergent plate boundaries (plates pulling apart)",
                                "Convergent plate boundaries (plates colliding)",
                                "Transform plate boundaries (plates sliding past each other)",
                                "Hotspots in the middle of oceanic plates"
                            ],
                            "correct_answer": "Convergent plate boundaries (plates colliding)",
                            "explanation": "Fold mountains are formed by horizontal compressional forces, which occur when tectonic plates collide at convergent plate boundaries."
                        }
                    },
                    {
                        "block_type": "multiple_choice_question",
                        "component_type": "multiple_choice_question",
                        "title": "Question 2: Meaning of Geosyncline",
                        "content": {
                            "question": "What is a 'geosyncline' in the context of mountain building?",
                            "options": [
                                "A high volcanic plateau",
                                "A deep fracture in a rock layer",
                                "A vast, water-filled basin where thick layers of sediments accumulate before compression",
                                "An imaginary vertical line through a fold crest"
                            ],
                            "correct_answer": "A vast, water-filled basin where thick layers of sediments accumulate before compression",
                            "explanation": "A geosyncline is the deep marine basin where sediment accumulates over millions of years, later serving as the raw rock material compressed and folded into mountain ranges."
                        }
                    }
                ]
            }
        ]
    },

    # Lesson 8: Global Distribution of Fold Mountains
    {
        "unit_order": 8,
        "unit_name": "Global Distribution of Fold Mountains",
        "lesson_title": "Global Distribution of Fold Mountains",
        "pages": [
            {
                "page_number": 1,
                "page_title": "World Fold Belts & Learning Goals",
                "blocks": [
                    {
                        "block_type": "suggested_image",
                        "component_type": "suggested_image",
                        "title": "The Atlas Fold Mountains of North Africa",
                        "content": {"text": "A scenic landscape view of the Atlas Fold Mountains in Morocco showing rugged linear folded ridges and arid valleys."}
                    },
                    {
                        "block_type": "learning_goal",
                        "component_type": "learning_goal",
                        "title": "Lesson Objectives: Global Fold Mountain Distribution",
                        "content": {
                            "text": (
                                "By the end of this lesson, you will be able to:\n\n"
                                "- Locate and identify major Fold Mountain systems on a world map (Himalayas, Alps, Andes, Rockies, Appalachians, Atlas)\n"
                                "- Relate the geographic distribution of fold mountains to active and ancient convergent plate margins\n"
                                "- Distinguish between young fold mountains (Alpine orogeny) and old fold mountains (Caledonian/Hercynian orogenies)"
                            )
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Prerequisite Spark: Why Do Mountains Form Lines?",
                        "content": {
                            "text": (
                                "If you look at a globe, why do mountains form long, continuous spines instead of being scattered randomly? "
                                "The Rockies run like a spine down western North America, the Andes hug the entire western coast of South America, "
                                "and the Himalayas form an uninterrupted arc across southern Asia. These linear belts trace the exact boundary lines "
                                "where the Earth's tectonic plates are colliding today!"
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 2,
                "page_title": "Major Global Fold Mountain Ranges",
                "blocks": [
                    {
                        "block_type": "diagram",
                        "component_type": "diagram",
                        "title": "Global Distribution Map of Major Fold Mountain Belts",
                        "content": {
                            "caption": "World map illustrating the major fold mountain belts aligned along tectonic plate boundaries: Himalayas, Alps, Andes, Rockies, Appalachians, Atlas, and Great Dividing Range."
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "The World's Great Mountain Belts",
                        "content": {
                            "text": (
                                "1. **The Himalayas (Asia)**:\n"
                                "- Formed by the ongoing continent-continent collision between the Indian Plate and the Eurasian Plate.\n"
                                "- Because both plates are buoyant continental crust, neither subducts; they crumple skyward, forming the highest peaks on Earth (including Mt. Everest).\n\n"
                                "2. **The Andes (South America)**:\n"
                                "- Formed along a subduction zone where the oceanic Nazca Plate dives beneath the continental South American Plate.\n"
                                "- Combines intense crustal folding with active volcanism along the Pacific Rim.\n\n"
                                "3. **The Rocky Mountains (North America)**:\n"
                                "- A vast cordillera formed by complex compression, subduction, and uplift along the western North American margin.\n\n"
                                "4. **The Alps (Europe)**:\n"
                                "- Formed by the northward collision of the African Plate with the Eurasian Plate, folding the ancient sediments of the Tethys Sea into complex nappes."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 3,
                "page_title": "Young vs. Old Fold Mountains",
                "blocks": [
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Young Fold Mountains vs. Old Fold Mountains",
                        "content": {
                            "text": (
                                "Geographers classify fold mountains into two main chronological groups:\n\n"
                                "1. **Young Fold Mountains (Alpine System - ~65 million years old to present)**:\n"
                                "- *Examples*: Himalayas, Alps, Andes, Rockies, Atlas.\n"
                                "- *Characteristics*: Extremely high, sharp, jagged, snow-capped peaks with steep slopes and deep V-shaped valleys. Highly active seismically (earthquakes).\n\n"
                                "2. **Old Fold Mountains (Pre-Alpine - >200 million years old)**:\n"
                                "- *Examples*: Appalachian Mountains (USA), Urals (Russia), Cape Fold Mountains (South Africa), Great Dividing Range (Australia).\n"
                                "- *Characteristics*: Lower elevations, rounded crests, gentle slopes, heavily eroded by wind, rain, and ice over hundreds of millions of years."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 4,
                "page_title": "Formative Assessment: Lesson 8",
                "blocks": [
                    {
                        "block_type": "multiple_choice_question",
                        "component_type": "multiple_choice_question",
                        "title": "Question 1: Collision Plates for Himalayas",
                        "content": {
                            "question": "The towering Himalayas in Asia were formed by the collision of which two tectonic plates?",
                            "options": [
                                "The African Plate and the South American Plate",
                                "The Pacific Plate and the Nazca Plate",
                                "The Indian Plate and the Eurasian Plate",
                                "The Arabian Plate and the Australian Plate"
                            ],
                            "correct_answer": "The Indian Plate and the Eurasian Plate",
                            "explanation": "The Himalayas are the result of the Indian Plate colliding with the Eurasian Plate in a continent-continent collision that continues to push the mountains higher today."
                        }
                    },
                    {
                        "block_type": "multiple_choice_question",
                        "component_type": "multiple_choice_question",
                        "title": "Question 2: Volcanism in Andes vs Himalayas",
                        "content": {
                            "question": "Why do we find active volcanoes along the Andes Fold Mountains, but very few active volcanoes in the Himalayas?",
                            "options": [
                                "The Andes are formed by rifting, while the Himalayas are formed by folding",
                                "The Andes involve oceanic-continental subduction which melts rock into magma, while the Himalayas involve continent-continent collision with no subduction melting",
                                "The Himalayas are ancient and inactive, while the Andes are young",
                                "The Himalayas consist entirely of granite with no magma underneath"
                            ],
                            "correct_answer": "The Andes involve oceanic-continental subduction which melts rock into magma, while the Himalayas involve continent-continent collision with no subduction melting",
                            "explanation": "The Andes are formed by oceanic crust subducting under continental crust, carrying water down to melt mantle rock into magma. The Himalayas involve two buoyant continental plates colliding without deep oceanic slab subduction."
                        }
                    }
                ]
            }
        ]
    },

    # Lesson 9: Resultant Features: Ridges, Valleys, Hogbacks, and Cuestas
    {
        "unit_order": 9,
        "unit_name": "Resultant Features: Ridges, Valleys, Hogbacks, and Cuestas",
        "lesson_title": "Resultant Features: Ridges, Valleys, Hogbacks, and Cuestas",
        "pages": [
            {
                "page_number": 1,
                "page_title": "Erosion of Folded Strata & Learning Goals",
                "blocks": [
                    {
                        "block_type": "suggested_image",
                        "component_type": "suggested_image",
                        "title": "Dinosaur Ridge Hogback Formation in Colorado",
                        "content": {"text": "A sharp-crested hogback ridge exposing steeply dipping sandstone rock strata with symmetrical erosional flanks."}
                    },
                    {
                        "block_type": "learning_goal",
                        "component_type": "learning_goal",
                        "title": "Lesson Objectives: Ridges, Valleys, Hogbacks, Cuestas",
                        "content": {
                            "text": (
                                "By the end of this lesson, you will be able to:\n\n"
                                "- Describe how differential erosion shapes folded terrain into parallel ridges and valleys\n"
                                "- Differentiate between a hogback and a cuesta based on rock dip angle and slope symmetry\n"
                                "- Identify dip slopes and scarp slopes on geological diagrams and topographic maps"
                            )
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Prerequisite Spark: Nature's Sculpting Tool",
                        "content": {
                            "text": (
                                "Not all folded landscapes remain simple waves. Over millions of years, rain, wind, and rivers attack the folded "
                                "rock layers. Because some rock layers (like quartzite or hard sandstone) are tough and resist erosion, "
                                "while other layers (like shale or clay) are soft and wash away easily, differential erosion carves the land into "
                                "a spectacular landscape of sharp ridges and deep parallel valleys!"
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 2,
                "page_title": "Core Definitions: Differential Erosion Landforms",
                "blocks": [
                    {
                        "block_type": "definition_card",
                        "component_type": "definition_card",
                        "title": "Definitions: Hogback, Cuesta, Differential Erosion",
                        "content": {
                            "definitions": [
                                {
                                    "term": "Differential Erosion",
                                    "definition": "The process where softer rock layers erode at a faster rate than harder, more resistant rocks, producing distinctive elevated ridges and low-lying valleys.",
                                    "simple": "Unequal wearing away of soft and hard rock strata by wind, water, and ice."
                                },
                                {
                                    "term": "Hogback",
                                    "definition": "A sharp-crested, steep-sided ridge formed by steeply dipping (greater than 30° to 45°) resistant rock strata, with approximately symmetrical slopes on both sides.",
                                    "simple": "A sharp, symmetrical rock ridge formed by steeply tilted resistant strata."
                                },
                                {
                                    "term": "Cuesta",
                                    "definition": "An asymmetrical ridge formed by gently dipping (less than 20°) rock strata, featuring one long gentle dip slope and one short, steep scarp slope.",
                                    "simple": "An asymmetrical ridge with a gentle dip slope on one side and a steep cliff on the other."
                                }
                            ]
                        }
                    }
                ]
            },
            {
                "page_number": 3,
                "page_title": "Hogbacks vs. Cuestas Geometry",
                "blocks": [
                    {
                        "block_type": "diagram",
                        "component_type": "diagram",
                        "title": "Cross-Section: Hogback vs. Cuesta Asymmetry",
                        "content": {
                            "caption": "Side-by-side geological cross-section: Left shows a Hogback with steeply dipping strata (>30°) forming a sharp, symmetrical spine. Right shows a Cuesta with gently dipping strata (<20°) featuring a long, gentle dip slope and a steep, cliff-like scarp slope."
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Formation Dynamics of Ridges, Hogbacks & Cuestas",
                        "content": {
                            "text": (
                                "1. **Parallel Ridges and Valleys**:\n"
                                "- Rivers exploit the fractured crests of anticlines or soft shale beds in synclines, excavating deep valleys.\n"
                                "- The hard sandstone and limestone layers stand out as elevated, parallel ridges.\n\n"
                                "2. **Hogbacks (Steeply Dipping Strata)**:\n"
                                "- When strata are tilted steeply (dip > 30° to 45°), the resistant layer protrudes vertically like the spine of a wild boar.\n"
                                "- Both the dip slope and the scarp slope have similar steep inclinations, creating a symmetrical profile.\n\n"
                                "3. **Cuestas (Gently Dipping Strata)**:\n"
                                "- When strata dip gently (dip < 20°), erosion cuts an asymmetrical ridge.\n"
                                "- **Dip Slope**: The long, gentle slope that follows the geological inclination of the resistant rock layer.\n"
                                "- **Scarp Slope (Escarpment)**: The steep, cliff-like face where erosion has sheared through the rock strata."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 4,
                "page_title": "Formative Assessment: Lesson 9",
                "blocks": [
                    {
                        "block_type": "multiple_choice_question",
                        "component_type": "multiple_choice_question",
                        "title": "Question 1: Asymmetrical Ridge Identification",
                        "content": {
                            "question": "A ridge formed by gently dipping rock layers, featuring a long, gentle slope on one side and a steep, cliff-like drop on the other, is called a:",
                            "options": [
                                "Hogback",
                                "Cuesta",
                                "Synclinal valley",
                                "Structural dome"
                            ],
                            "correct_answer": "Cuesta",
                            "explanation": "A cuesta is an asymmetrical ridge formed by gently dipping strata, featuring a gentle 'dip slope' and a steep 'scarp slope'. A hogback has steep, symmetrical slopes."
                        }
                    },
                    {
                        "block_type": "multiple_choice_question",
                        "component_type": "multiple_choice_question",
                        "title": "Question 2: Relief Shaping by Differential Erosion",
                        "content": {
                            "question": "Which process is primarily responsible for carving folded rock layers into alternating parallel ridges and valleys?",
                            "options": [
                                "Thermal expansion of minerals",
                                "Differential erosion of alternating hard and soft rock layers",
                                "Deep chemical weathering in limestone basins",
                                "Horizontal movement along strike-slip faults"
                            ],
                            "correct_answer": "Differential erosion of alternating hard and soft rock layers",
                            "explanation": "Differential erosion is the key process: rivers erode soft layers (like shale) to create valleys, while hard, resistant layers (like quartzite or sandstone) remain standing as elevated ridges."
                        }
                    }
                ]
            }
        ]
    },

    # Lesson 10: Significance of Folding to Human Activities
    {
        "unit_order": 10,
        "unit_name": "Significance of Folding to Human Activities",
        "lesson_title": "Significance of Folding to Human Activities",
        "pages": [
            {
                "page_number": 1,
                "page_title": "Human Significance & Learning Goals",
                "blocks": [
                    {
                        "block_type": "suggested_image",
                        "component_type": "suggested_image",
                        "title": "Highland Agriculture and Human Settlements in Mountain Valleys",
                        "content": {"text": "Mountain valley settlements with terraced agricultural slopes and winding transport infrastructure in folded terrain."}
                    },
                    {
                        "block_type": "learning_goal",
                        "component_type": "learning_goal",
                        "title": "Lesson Objectives: Human Significance of Folding",
                        "content": {
                            "text": (
                                "By the end of this lesson, you will be able to:\n\n"
                                "- Analyse the positive economic impacts of folding (water catchments, minerals, HEP generation, tourism, forestry)\n"
                                "- Evaluate the negative challenges posed by folded terrain (transport barriers, rain shadows, landslides)\n"
                                "- Relate folded landscapes to resource exploitation and regional development"
                            )
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Prerequisite Spark: Why Live in Rugged Mountains?",
                        "content": {
                            "text": (
                                "Why do millions of people choose to live in steep, rugged mountain valleys despite the constant risk of landslides? "
                                "Fold mountains are much more than beautiful scenery. They are the primary 'water towers' of our planet, the treasure "
                                "chests of precious minerals, and key engines of tourism, agriculture, and clean hydroelectric power!"
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 2,
                "page_title": "Economic Benefits of Folding",
                "blocks": [
                    {
                        "block_type": "diagram",
                        "component_type": "diagram",
                        "title": "Significance of Fold Mountains to Human Activities",
                        "content": {
                            "caption": "Comprehensive infographic contrasting positive economic benefits (water towers, HEP dams, mineral veins, tourism) with physical challenges (transport barrier passes, rain shadow aridity, landslide hazards)."
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Positive Impacts of Folding",
                        "content": {
                            "text": (
                                "1. **Water Catchment Areas (Water Towers)**:\n"
                                "- Fold mountains force moist air masses to rise, cool, and condense, triggering heavy **orographic rainfall**.\n"
                                "- They are heavily forested and feed perennial rivers that supply water to millions downstream (e.g., the Indus and Ganges from the Himalayas).\n\n"
                                "2. **Mineral Wealth and Ore Concentration**:\n"
                                "- Intense heat and pressure during folding and metamorphism concentrate valuable metallic minerals (copper, gold, silver, lead, tin) into accessible hydrothermal veins.\n\n"
                                "3. **Hydroelectric Power (HEP) Potential**:\n"
                                "- High elevation differences and fast-flowing mountain rivers create ideal natural conditions for constructing HEP dams.\n\n"
                                "4. **Tourism, Recreation, and Forestry**:\n"
                                "- Glaciated peaks, deep canyons, and alpine meadows attract mountaineering, skiing, and ecotourism. Mountain slopes support valuable timber forests."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 3,
                "page_title": "Physical Challenges & Hazards",
                "blocks": [
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Negative Impacts and Physical Barriers",
                        "content": {
                            "text": (
                                "1. **Formidable Transport Barriers**:\n"
                                "- Rugged ridges and deep gorges make road, railway, and pipeline construction astronomically expensive, requiring winding hairpin passes, bridges, and deep tunnels.\n\n"
                                "2. **Rain Shadow Effect (Aridity)**:\n"
                                "- While windward mountain slopes receive abundant rain, leeward slopes experience descending, warming air that creates dry, semi-arid rain shadow zones unsuitable for rain-fed farming.\n\n"
                                "3. **Geo-Hazards (Landslides & Earthquakes)**:\n"
                                "- Steep slopes and active tectonic compression trigger devastating landslides, mudflows, and rockfalls during heavy rains and earthquakes, destroying villages and blocking roads."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 4,
                "page_title": "Formative Assessment: Lesson 10",
                "blocks": [
                    {
                        "block_type": "multiple_choice_question",
                        "component_type": "multiple_choice_question",
                        "title": "Question 1: Mountains as Water Catchments",
                        "content": {
                            "question": "How do Fold Mountains act as important water catchments?",
                            "options": [
                                "They are made of porous volcanic ash that stores water like a sponge",
                                "Their high elevations force moist air to rise, cool, and condense, producing heavy orographic rainfall that feeds rivers",
                                "They prevent river water from evaporating by blocking all sunlight",
                                "They consist entirely of glaciers that never melt"
                            ],
                            "correct_answer": "Their high elevations force moist air to rise, cool, and condense, producing heavy orographic rainfall that feeds rivers",
                            "explanation": "Mountains force moist air upwards. As air rises, it cools and condenses (orographic rainfall), feeding rivers and acting as vital regional water catchments."
                        }
                    },
                    {
                        "block_type": "multiple_choice_question",
                        "component_type": "multiple_choice_question",
                        "title": "Question 2: Economic Challenge of Fold Mountains",
                        "content": {
                            "question": "What is a major negative economic impact of Fold Mountains on regional development?",
                            "options": [
                                "They contain absolutely no valuable minerals",
                                "They prevent orographic rainfall from occurring",
                                "They present formidable transport barriers, making road and railway construction extremely expensive",
                                "They prevent any form of tourism"
                            ],
                            "correct_answer": "They present formidable transport barriers, making road and railway construction extremely expensive",
                            "explanation": "Steep slopes, rugged ridges, and deep canyons make infrastructure construction very costly, requiring expensive tunnels, bridges, and winding passes vulnerable to landslides."
                        }
                    }
                ]
            }
        ]
    },

    # Lesson 11: Human Adaptation and Slope Management
    {
        "unit_order": 11,
        "unit_name": "Human Adaptation and Slope Management",
        "lesson_title": "Human Adaptation and Slope Management",
        "pages": [
            {
                "page_number": 1,
                "page_title": "Slope Management & Learning Goals",
                "blocks": [
                    {
                        "block_type": "suggested_image",
                        "component_type": "suggested_image",
                        "title": "Terraced Mountain Agriculture in Highland Valleys",
                        "content": {"text": "Step terracing on steep mountain slopes showing stable agricultural cultivation and soil conservation."}
                    },
                    {
                        "block_type": "learning_goal",
                        "component_type": "learning_goal",
                        "title": "Lesson Objectives: Human Adaptation & Slope Management",
                        "content": {
                            "text": (
                                "By the end of this lesson, you will be able to:\n\n"
                                "- Examine how mountain communities adapt to living in steep folded terrain\n"
                                "- Explain sustainable slope management techniques (terracing, contour farming, strip cropping, afforestation)\n"
                                "- Analyse local Kenyan soil conservation strategies in highland counties (Murang'a, Nyeri, Kisii)"
                            )
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Prerequisite Spark: The Giant Mountain Staircase",
                        "content": {
                            "text": (
                                "If you try to cultivate crops on a steep hillside, what happens when a torrential rainstorm hits? "
                                "Water rushes down at high speed, stripping away the fertile topsoil and carving deep gullies. "
                                "To survive and farm in mountainous terrain, humans have become landscape engineers, turning steep, "
                                "perilous slopes into productive giant staircases through terracing and contour management!"
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 2,
                "page_title": "Core Definitions: Slope Management",
                "blocks": [
                    {
                        "block_type": "definition_card",
                        "component_type": "definition_card",
                        "title": "Definitions: Terracing, Contour Ploughing, Afforestation",
                        "content": {
                            "definitions": [
                                {
                                    "term": "Terracing",
                                    "definition": "The practice of carving flat, step-like benches into steep slopes to reduce surface runoff velocity and prevent catastrophic soil erosion.",
                                    "simple": "Cutting flat step-like benches into steep hills to farm safely and retain soil."
                                },
                                {
                                    "term": "Contour Ploughing",
                                    "definition": "Ploughing and planting crops across the slope, following natural contour lines, to create miniature ridges that trap water and soil.",
                                    "simple": "Ploughing horizontally across hillsides to block downhill water runoff."
                                },
                                {
                                    "term": "Afforestation",
                                    "definition": "Planting trees on bare hillsides and ridge tops to stabilize soil with dense root networks and reduce landslide hazards.",
                                    "simple": "Planting trees on slopes to anchor soil and prevent mudslides."
                                }
                            ]
                        }
                    }
                ]
            },
            {
                "page_number": 3,
                "page_title": "Sustainable Slope Management Architecture",
                "blocks": [
                    {
                        "block_type": "diagram",
                        "component_type": "diagram",
                        "title": "Unmanaged vs. Managed Mountain Slopes",
                        "content": {
                            "caption": "Side-by-side comparison: Left shows an unmanaged eroding slope with vertical plow lines, gully erosion, and landslide scars. Right shows a sustainably managed slope featuring step terracing, contour grass strips, water retention benches, and hilltop afforestation."
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Slope Management Technologies",
                        "content": {
                            "text": (
                                "1. **Terrace Agriculture (Bench & Fanya Juu Terraces)**:\n"
                                "- By constructing flat steps supported by stone walls or earth bunds, the kinetic energy of runoff water is neutralized.\n"
                                "- Water infiltrates deep into the soil profile rather than washing topsoil downhill.\n\n"
                                "2. **Contour Planting & Grass Strips**:\n"
                                "- Planting rows of vetiver or Napier grass along elevation contours creates natural silt traps that filter runoff water.\n\n"
                                "3. **Afforestation & Reforestation**:\n"
                                "- Tree roots penetrate deep into the subsoil, binding loose soil particles and anchoring them to the underlying bedrock, preventing shallow landslides."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 4,
                "page_title": "Kenyan Highland Case Study",
                "blocks": [
                    {
                        "block_type": "case_study",
                        "component_type": "case_study",
                        "title": "Kenyan Case Study: Murang'a, Nyeri, and Kisii Highlands",
                        "content": {
                            "text": (
                                "In the steep, rolling hills of Murang'a, Nyeri, and Kisii counties, population pressure has forced smallholders "
                                "to farm slopes exceeding 30 degrees. Farmers utilize *Fanya Juu* and bench terraces combined with dense hedges of "
                                "Napier grass along contour ridges. This retains soil moisture for intensive tea, coffee, and banana cultivation "
                                "while preventing localized mudslides during heavy long rains."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 5,
                "page_title": "Formative Assessment: Lesson 11",
                "blocks": [
                    {
                        "block_type": "multiple_choice_question",
                        "component_type": "multiple_choice_question",
                        "title": "Question 1: Flat Step-Like Benches on Slopes",
                        "content": {
                            "question": "Which soil conservation practice involves carving flat, step-like benches into steep mountain slopes to reduce water runoff?",
                            "options": [
                                "Windbreaking",
                                "Terracing",
                                "Crop rotation",
                                "Strip cropping"
                            ],
                            "correct_answer": "Terracing",
                            "explanation": "Terracing involves cutting step-like flat benches into steep hillsides to slow runoff, retain moisture, and prevent soil erosion."
                        }
                    },
                    {
                        "block_type": "multiple_choice_question",
                        "component_type": "multiple_choice_question",
                        "title": "Question 2: Afforestation and Landslide Prevention",
                        "content": {
                            "question": "Why is afforestation (planting trees) highly effective at preventing landslides on steep mountain slopes?",
                            "options": [
                                "Trees block all rain from reaching the ground",
                                "Tree roots act as natural anchors, binding soil particles together and anchoring them to the bedrock",
                                "Tree leaves chemically harden the soil",
                                "Trees flat out flatten the slope over time"
                            ],
                            "correct_answer": "Tree roots act as natural anchors, binding soil particles together and anchoring them to the bedrock",
                            "explanation": "Dense tree root networks bind soil particles together and anchor the soil mantle to the underlying bedrock, preventing gravity from pulling water-saturated soil downhill."
                        }
                    }
                ]
            }
        ]
    },

    # Lesson 12: Topic Review, Modeling, and Synthesis
    {
        "unit_order": 12,
        "unit_name": "Topic Review, Modeling, and Synthesis",
        "lesson_title": "Topic Review, Modeling, and Synthesis",
        "pages": [
            {
                "page_number": 1,
                "page_title": "Synthesis & Learning Goals",
                "blocks": [
                    {
                        "block_type": "suggested_image",
                        "component_type": "suggested_image",
                        "title": "Complex Geological Fold Formations",
                        "content": {"text": "A panoramic cliff section showing multi-layered geological folds and rock strata synthesis."}
                    },
                    {
                        "block_type": "learning_goal",
                        "component_type": "learning_goal",
                        "title": "Lesson Objectives: Folding Synthesis & Modeling",
                        "content": {
                            "text": (
                                "By the end of this lesson, you will be able to:\n\n"
                                "- Synthesize the complete lifecycle of folding from compressional stress to human adaptation\n"
                                "- Construct physical and digital models demonstrating fold geometry and progressive deformation\n"
                                "- Apply structural folding concepts to evaluate real-world geological landscapes"
                            )
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Prerequisite Spark: The Big Picture Synthesis",
                        "content": {
                            "text": (
                                "Across Topic 7, we have explored how invisible tectonic plate collisions deep beneath the Earth's surface "
                                "generate massive compressional forces that buckle solid rock layers into towering mountains, sculpt spectacular "
                                "cuestas and hogbacks, and challenge human engineers to innovate with terracing, tunnels, and clean energy systems."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 2,
                "page_title": "Comprehensive Topic Review Matrix",
                "blocks": [
                    {
                        "block_type": "diagram",
                        "component_type": "diagram",
                        "title": "Interactive Fold Deformation Continuum & Modeling",
                        "content": {
                            "caption": "Synthesis diagram showing the progressive deformation spectrum from simple symmetrical folds to asymmetrical, overturned, recumbent, and overthrust nappes under escalating tectonic force."
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "The Lifecycle of a Folded Landscape",
                        "content": {
                            "text": (
                                "The complete folding continuum encompasses five key pillars:\n\n"
                                "1. **Tectonic Driver**: Convergent plate boundaries generate horizontal compressional forces.\n"
                                "2. **Plastic Deformation**: Deep heat and pressure cause sedimentary strata to buckle into anticlines (upfolds) and synclines (downfolds).\n"
                                "3. **Structural Diversity**: Increasing force creates symmetrical, asymmetrical, overturned, recumbent, and overthrust nappes.\n"
                                "4. **Differential Sculpting**: Weathering and rivers carve folded strata into parallel ridges, valleys, hogbacks, and cuestas.\n"
                                "5. **Human Adaptation**: Communities adapt via bench terracing, contour farming, HEP generation, and mineral exploration."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 3,
                "page_title": "Hands-on Modeling Activity",
                "blocks": [
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Hands-on Practical Modeling: Layered Clay Folds",
                        "content": {
                            "text": (
                                "You can easily demonstrate folding principles in the classroom or at home:\n\n"
                                "- **Materials**: 3 or 4 flat strips of different colored plasticine, playdough, or clay.\n"
                                "- **Step 1**: Stack the strips horizontally to represent undisturbed sedimentary strata in a geosyncline.\n"
                                "- **Step 2**: Place your hands on opposite ends and apply steady, equal inward force. Observe how the layers buckle into symmetrical anticlines and synclines.\n"
                                "- **Step 3**: Apply stronger force from your right hand than your left. Observe the transition into an asymmetrical fold with a tilted axial plane.\n"
                                "- **Step 4**: Push firmly until the fold rolls flat on the table, demonstrating a recumbent fold.\n"
                                "- **Step 5**: Use a thin ruler to slice the lower limb and slide the top clay sheet forward, simulating a thrust fault and nappe!"
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 4,
                "page_title": "Formative Assessment: Lesson 12",
                "blocks": [
                    {
                        "block_type": "multiple_choice_question",
                        "component_type": "multiple_choice_question",
                        "title": "Question 1: Equal Push in Clay Modeling",
                        "content": {
                            "question": "During your practical modeling activity with layered clay, pushing with equal force from both sides produces which type of fold?",
                            "options": [
                                "Asymmetrical fold",
                                "Symmetrical fold",
                                "Recumbent fold",
                                "Overthrust fold"
                            ],
                            "correct_answer": "Symmetrical fold",
                            "explanation": "When compressional forces are equal from both directions, the clay layers buckle symmetrically, creating limbs with equal slopes and a vertical axial plane."
                        }
                    },
                    {
                        "block_type": "multiple_choice_question",
                        "component_type": "multiple_choice_question",
                        "title": "Question 2: Full Lifecycle Sequence",
                        "content": {
                            "question": "Which sequence correctly summarizes the lifecycle of a folded landscape?",
                            "options": [
                                "Erosion -> Volcanic Eruption -> Tensional Fracturing -> Soil Loss",
                                "Compressional Stress -> Plastic Deformation -> Alternating Landforms -> Differential Erosion and Human Adaptation",
                                "Sea level rise -> Earthquakes -> Landslides -> Desertification",
                                "Faulting -> Sinking -> Basin filling -> Hotspot activity"
                            ],
                            "correct_answer": "Compressional Stress -> Plastic Deformation -> Alternating Landforms -> Differential Erosion and Human Adaptation",
                            "explanation": "The standard geological process sequence is: compressional forces act on strata (stress), causing rocks to buckle (plastic deformation), creating landforms (anticlines/synclines), which are sculpted by weather (differential erosion) and managed by communities (human adaptation)."
                        }
                    }
                ]
            }
        ]
    }
]

# =============================================================================
# INGESTION RUNNER
# =============================================================================
def run_ingestion():
    print("=" * 80)
    print("VLearn CBC Grade 10 Geography — Topic 7: Folding Ingestion Engine")
    print("=" * 80)

    with transaction.atomic():
        # 1. Verify Curriculum
        curriculum = Curriculum.objects.filter(name__iexact="CBC").first()
        if not curriculum:
            raise RuntimeError("Curriculum 'CBC' not found in database!")

        # 2. Verify Grade
        grade = Grade.objects.filter(curriculum=curriculum, name__icontains="10").first()
        if not grade:
            raise RuntimeError("Grade 10 not found under CBC!")

        # 3. Verify Subject
        subject = Subject.objects.filter(id=37).first() or Subject.objects.filter(grade=grade, name="Geography").first()
        if not subject:
            raise RuntimeError("Subject 'Geography' (ID: 37) not found under Grade 10!")

        # 4. Get or Create Topic 7
        topic, t_created = Topic.objects.get_or_create(
            subject=subject,
            order=7,
            defaults={
                "name": "Folding",
                "description": "Comprehensive study of folding, fold anatomy, fold types, resultant features, global distribution, and human significance."
            }
        )
        topic.name = "Folding"
        topic.description = "Comprehensive study of folding, fold anatomy, fold types, resultant features, global distribution, and human significance."
        topic.save()
        print(f"Topic 7: {topic.name} (ID: {topic.id}, Subject: {subject.name})")

        total_blocks_created = 0

        # Ingest each of the 12 lessons
        for les_data in LESSONS_DATA:
            u_order = les_data["unit_order"]
            u_name = les_data["unit_name"]
            les_title = les_data["lesson_title"]

            unit, u_created = LearningUnit.objects.get_or_create(
                topic=topic,
                order=u_order,
                defaults={"name": u_name, "description": f"Learning unit for {u_name}"}
            )
            unit.name = u_name
            unit.save()

            lesson, l_created = Lesson.objects.get_or_create(
                topic=topic,
                learning_unit=unit,
                defaults={
                    "title": les_title,
                    "status": "published",
                    "version": 1
                }
            )
            lesson.title = les_title
            lesson.status = "published"
            lesson.version = 1
            lesson.save()

            # Clean previous blocks for idempotency
            lesson.blocks.all().delete()

            block_seq = 1
            for page in les_data["pages"]:
                p_num = page["page_number"]
                p_title = clean_text(page["page_title"])

                for comp_order, blk in enumerate(page["blocks"], start=1):
                    b_type = blk["block_type"]
                    c_type = blk.get("component_type", b_type)
                    b_title = clean_text(blk.get("title", p_title))
                    b_content = clean_content_dict(blk.get("content", {}))

                    LessonBlock.objects.create(
                        lesson=lesson,
                        page_number=p_num,
                        page_title=p_title,
                        order=block_seq,
                        component_order=comp_order,
                        block_type=b_type,
                        component_type=c_type,
                        title=b_title,
                        content=b_content
                    )
                    block_seq += 1
                    total_blocks_created += 1

            print(f" -> Ingested Unit {u_order}: {les_title} ({len(les_data['pages'])} pages, {block_seq - 1} blocks)")

    print("=" * 80)
    print(f"Ingestion completed successfully for Grade 10 Geography Topic 7! (Total Blocks: {total_blocks_created})")
    print("=" * 80)

if __name__ == "__main__":
    run_ingestion()
