"""
VLearn CBC Grade 10 Geography — Topic 9: Earthquakes
Direct Programmatic Source-Driven Ingestion Engine

Subject: Geography (Grade 10 CBC, Subject ID: 37)
Topic 9: Earthquakes (10 Lessons)
Source: Grade 10 Geography/09_earthquakes.md

Lessons:
  1. Introduction to Earthquakes, Focus, Epicentre, and Seismic Waves
  2. Types of Earthquakes and Aftershocks
  3. Global Earthquake Zones and Tectonic Associations
  4. Measuring Earthquakes: Richter vs. Mercalli Scales
  5. Seismographs and Interpreting Earthquake Records
  6. Environmental and Infrastructure Effects of Earthquakes
  7. Case Study: Global and Local Earthquake Risk Comparisons
  8. Earthquake Preparedness, Mitigation, and Emergency Action
  9. Designing Public Safety Communication Messages
  10. Topic Review, Synthesis, and Unit Assessment

Usage:
  ./venv/bin/python curriculum/ingest_cbc_grade10_geography_topic9.py
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
# TOPIC 9 LESSON DEFINITIONS (10 LESSONS)
# =============================================================================
LESSONS_DATA = [
    # Lesson 1: Introduction to Earthquakes, Focus, Epicentre, and Seismic Waves
    {
        "unit_order": 1,
        "unit_name": "Introduction to Earthquakes, Focus, Epicentre, and Seismic Waves",
        "lesson_title": "Introduction to Earthquakes, Focus, Epicentre, and Seismic Waves",
        "pages": [
            {
                "page_number": 1,
                "page_title": "Introduction to Earthquakes & Learning Goals",
                "blocks": [
                    {
                        "block_type": "suggested_image",
                        "component_type": "suggested_image",
                        "title": "Earthquake Surface Rupture and Faulting",
                        "content": {"text": "A photograph showing active ground fracture and surface fault rupture caused by high-energy crustal earthquakes."}
                    },
                    {
                        "block_type": "learning_goal",
                        "component_type": "learning_goal",
                        "title": "Lesson Objectives: Earthquake Anatomy & Waves",
                        "content": {
                            "text": (
                                "By the end of this lesson, you will be able to:\n\n"
                                "- Define an earthquake and distinguish between the subterranean focus and the surface epicentre\n"
                                "- Explain how tectonic stress causes elastic strain accumulation and brittle fault rupture\n"
                                "- Differentiate between compressional primary (P) waves, transverse secondary (S) waves, and destructive surface waves"
                            )
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Prerequisite Spark: The Snapping Dry Branch",
                        "content": {
                            "text": (
                                "Imagine standing on a dry branch on the ground. As you press your foot down, the branch bends slightly, "
                                "storing mechanical energy. Suddenly, with a loud 'snap', the branch fractures, and you feel a sharp vibration travel "
                                "up your leg. This is exactly how the Earth behaves! The crust bends under tectonic stress until it reaches its breaking "
                                "point, snapping and releasing massive vibrational seismic energy."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 2,
                "page_title": "Core Definitions: Focus, Epicentre, and Waves",
                "blocks": [
                    {
                        "block_type": "key_terms",
                        "component_type": "key_terms",
                        "title": "Fundamental Seismic Terminology",
                        "content": {
                            "terms": [
                                {
                                    "term": "Earthquake",
                                    "definition": "A sudden, rapid shaking of the Earth's crust caused by the release of accumulated mechanical energy along a fault plane."
                                },
                                {
                                    "term": "Focus (Hypocentre)",
                                    "definition": "The exact underground point beneath the Earth's surface where rock fractures and seismic energy is first released."
                                },
                                {
                                    "term": "Epicentre",
                                    "definition": "The point on the Earth's surface situated directly vertically above the subterranean focus."
                                },
                                {
                                    "term": "Seismic Waves",
                                    "definition": "Vibrational pulses of energy that propagate outward in all directions through the Earth's interior and along its surface."
                                }
                            ]
                        }
                    }
                ]
            },
            {
                "page_number": 3,
                "page_title": "Mechanics of Fault Rupture & Seismic Wave Anatomy",
                "blocks": [
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Elastic Strain Accumulation & Energy Release",
                        "content": {
                            "text": (
                                "Earthquakes are primarily tectonic in origin. Tectonic plates move continuously due to mantle convection currents, "
                                "but frictional resistance along plate boundaries prevents them from gliding smoothly.\n\n"
                                "1. **Elastic Strain Accumulation:** As plates exert continuous force, rocks along the boundary deform elastically, storing strain energy.\n"
                                "2. **Brittle Fracture:** When shear stress exceeds the rock's frictional yield strength, sudden slippage occurs along a fault plane.\n"
                                "3. **Energy Radiation:** Stored potential energy converts instantly into kinetic vibrational waves radiating outward from the focus."
                            )
                        }
                    },
                    {
                        "block_type": "diagram",
                        "component_type": "diagram",
                        "title": "Earthquake Anatomy: Focus, Epicentre, Fault Line & Wavefronts",
                        "content": {
                            "caption": "Block diagram illustrating the 3D spatial relationship between subterranean focus, surface epicentre, fault plane, and radiating wave fronts.",
                            "svg_placeholder": "SVG_EARTHQUAKE_ANATOMY"
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Body Waves vs. Surface Waves",
                        "content": {
                            "text": (
                                "Seismic energy radiates through the Earth via two major categories of waves:\n\n"
                                "- **Body Waves (Propagate through Earth's interior):**\n"
                                "  • **Primary (P) Waves:** Longitudinal compressional waves that push and pull rock particles in the direction of travel. They are the fastest seismic waves and propagate through both solid rock and liquid layers.\n"
                                "  • **Secondary (S) Waves:** Transverse shear waves that vibrate rock particles perpendicular to the direction of propagation. S-waves are slower than P-waves and can only travel through solid materials.\n\n"
                                "- **Surface Waves (Propagate along the crust's upper boundary):**\n"
                                "  • **Rayleigh & Love Waves:** Move with rolling elliptical and horizontal shear motions. Although they travel slowest, they produce the largest ground displacements and cause the majority of building collapses."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 4,
                "page_title": "Kenyan Relevance: The East African Rift System",
                "blocks": [
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Seismic Activity in the Gregory Rift Valley",
                        "content": {
                            "text": (
                                "In Kenya, earthquake activity is intimately linked with the **East African Rift System (EARS)**. "
                                "Here, the African Plate is actively splitting into the Nubian and Somalian sub-plates. "
                                "Tensional stresses stretch and thin the continental crust, triggering normal faulting and frequent shallow-focus tremors "
                                "in rift counties such as Nakuru, Baringo, Kajiado, Elgeyo Marakwet, and around active calderas like Menengai, Longonot, and Suswa."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 5,
                "page_title": "Common Misconceptions Alert",
                "blocks": [
                    {
                        "block_type": "misconception_callout",
                        "component_type": "misconception_callout",
                        "title": "Misconception: The Epicentre is Underground",
                        "content": {
                            "misconception": "The epicentre is the subterranean spot where the earthquake rupture begins.",
                            "correction": "The underground point of initial rupture is the focus (hypocentre). The epicentre is the surface geographical point situated directly vertical to the focus."
                        }
                    }
                ]
            },
            {
                "page_number": 6,
                "page_title": "Formative Assessment MCQs",
                "blocks": [
                    {
                        "block_type": "multiple_choice_question",
                        "component_type": "multiple_choice_question",
                        "title": "Question 1: Fastest Seismic Wave Type",
                        "content": {
                            "question": "Which type of seismic wave travels fastest and is able to propagate through both solid and liquid mediums?",
                            "options": [
                                {"id": "A", "text": "Secondary (S) Waves"},
                                {"id": "B", "text": "Love Waves"},
                                {"id": "C", "text": "Primary (P) Waves"},
                                {"id": "D", "text": "Rayleigh Waves"}
                            ],
                            "correct_answer": "C",
                            "explanation": "Primary (P) waves are compressional longitudinal body waves. They travel fastest through the Earth's interior and can pass through both solid rocks and liquid mediums (such as the outer core). S-waves cannot propagate through liquids."
                        }
                    },
                    {
                        "block_type": "multiple_choice_question",
                        "component_type": "multiple_choice_question",
                        "title": "Question 2: Geological Term for Subterranean Rupture Point",
                        "content": {
                            "question": "A seismologist reports that an earthquake originated 15 km beneath Nakuru town. What is the geological term for this 15 km depth point?",
                            "options": [
                                {"id": "A", "text": "Epicentre"},
                                {"id": "B", "text": "Focus (Hypocentre)"},
                                {"id": "C", "text": "Fault Scarp"},
                                {"id": "D", "text": "Graben"}
                            ],
                            "correct_answer": "B",
                            "explanation": "The focus (or hypocentre) is the exact point underground where the rock fracture originates. Nakuru town, on the surface directly above, is the epicentre."
                        }
                    }
                ]
            }
        ]
    },

    # Lesson 2: Types of Earthquakes and Aftershocks
    {
        "unit_order": 2,
        "unit_name": "Types of Earthquakes and Aftershocks",
        "lesson_title": "Types of Earthquakes and Aftershocks",
        "pages": [
            {
                "page_number": 1,
                "page_title": "Classification of Earthquakes & Learning Goals",
                "blocks": [
                    {
                        "block_type": "suggested_image",
                        "component_type": "suggested_image",
                        "title": "Earthquake Structural Damage and Shallow Rupture",
                        "content": {"text": "A photograph showing urban building collapse and infrastructure deformation following a shallow-focus earthquake."}
                    },
                    {
                        "block_type": "learning_goal",
                        "component_type": "learning_goal",
                        "title": "Lesson Objectives: Earthquake Depth & Origin",
                        "content": {
                            "text": (
                                "By the end of this lesson, you will be able to:\n\n"
                                "- Classify earthquakes by focal depth (shallow, intermediate, and deep)\n"
                                "- Explain the chronological mechanics of foreshocks, mainshocks, and aftershocks\n"
                                "- Distinguish between tectonic, volcanic, collapse, and explosion earthquakes"
                            )
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Prerequisite Spark: Shifting a Heavy Wardrobe",
                        "content": {
                            "text": (
                                "Have you ever tried to drag a heavy wardrobe across a rough concrete floor? It doesn't glide smoothly. "
                                "It sticks firmly, then suddenly jerks forward with a violent shudder (the main movement), followed by small, "
                                "creaking settlements as the wardrobe stabilizes. This mechanical sequence mirrors foreshocks, mainshocks, and aftershocks!"
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 2,
                "page_title": "Depth Classification: Shallow, Intermediate, and Deep",
                "blocks": [
                    {
                        "block_type": "key_terms",
                        "component_type": "key_terms",
                        "title": "Focal Depth Categories",
                        "content": {
                            "terms": [
                                {
                                    "term": "Shallow-Focus Earthquakes",
                                    "definition": "Earthquakes occurring at depths between 0 and 70 km beneath the crust, accounting for roughly 75% of global seismic energy release."
                                },
                                {
                                    "term": "Intermediate-Focus Earthquakes",
                                    "definition": "Earthquakes originating between 70 km and 300 km depth along descending subduction plates."
                                },
                                {
                                    "term": "Deep-Focus Earthquakes",
                                    "definition": "Earthquakes occurring at depths between 300 km and 700 km along subducting lithospheric slabs in Wadati-Benioff zones."
                                },
                                {
                                    "term": "Aftershocks",
                                    "definition": "Secondary tremors occurring in the same faulted region after the mainshock, generated as adjacent crustal blocks adjust to new stress fields."
                                }
                            ]
                        }
                    },
                    {
                        "block_type": "diagram",
                        "component_type": "diagram",
                        "title": "Focal Depth Classification and Wadati-Benioff Subduction Zone",
                        "content": {
                            "caption": "Diagram showing shallow, intermediate, and deep earthquake hypocentres along a subducting tectonic slab, and the sequence from foreshocks to aftershocks.",
                            "svg_placeholder": "SVG_EARTHQUAKE_DEPTH_TYPES"
                        }
                    }
                ]
            },
            {
                "page_number": 3,
                "page_title": "Earthquake Sequences & Non-Tectonic Causes",
                "blocks": [
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Foreshocks, Mainshocks, and Aftershocks",
                        "content": {
                            "text": (
                                "Earthquake events typically occur in structured temporal clusters:\n\n"
                                "- **Foreshocks:** Minor tremors preceding the primary rupture, caused by localized micro-fracturing along the fault plane.\n"
                                "- **Mainshock:** The largest and most energetic rupture event in the sequence.\n"
                                "- **Aftershocks:** Prolonged secondary earthquakes triggered as the main rupture transfers mechanical strain onto adjacent fault segments. Aftershocks can continue for weeks, months, or years."
                            )
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Non-Tectonic Origins of Earthquakes",
                        "content": {
                            "text": (
                                "While tectonic plate boundary stress generates over 90% of earthquakes, other mechanisms include:\n\n"
                                "- **Volcanic Earthquakes:** Triggered by high-pressure magma forcing pathways through solid rock or gas-driven explosive venting.\n"
                                "- **Collapse Earthquakes:** Localized tremors caused by the structural collapse of underground caverns, sinkholes, or abandoned mine shafts.\n"
                                "- **Explosion Earthquakes:** Artificial seismic waves generated by nuclear detonations or large-scale mining blasting."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 4,
                "page_title": "Common Misconceptions Alert",
                "blocks": [
                    {
                        "block_type": "misconception_callout",
                        "component_type": "misconception_callout",
                        "title": "Misconception: Aftershocks Are Harmless",
                        "content": {
                            "misconception": "Aftershocks are minor and pose no severe danger to people or infrastructure.",
                            "correction": "Even though aftershocks are smaller than the mainshock, they strike structures that are already weakened and cracked, frequently causing total building collapse and posing extreme hazards to rescue workers."
                        }
                    }
                ]
            },
            {
                "page_number": 5,
                "page_title": "Formative Assessment MCQs",
                "blocks": [
                    {
                        "block_type": "multiple_choice_question",
                        "component_type": "multiple_choice_question",
                        "title": "Question 1: Destruction from Shallow Earthquakes",
                        "content": {
                            "question": "Why are shallow-focus earthquakes generally more destructive to human infrastructure than deep-focus earthquakes of the same magnitude?",
                            "options": [
                                {"id": "A", "text": "Deep-focus earthquakes do not produce surface waves."},
                                {"id": "B", "text": "Seismic waves from shallow earthquakes travel a shorter distance, losing less energy before hitting the surface."},
                                {"id": "C", "text": "Shallow-focus earthquakes only occur under major urban cities."},
                                {"id": "D", "text": "Deep-focus earthquakes are absorbed completely by molten mantle magma."}
                            ],
                            "correct_answer": "B",
                            "explanation": "Seismic waves attenuate (lose energy) as they travel through rock. Shallow-focus earthquakes originate close to the surface (0-70 km), delivering dense seismic energy directly into surface structures with minimal geometric dissipation."
                        }
                    },
                    {
                        "block_type": "multiple_choice_question",
                        "component_type": "multiple_choice_question",
                        "title": "Question 2: Secondary Tremors Terminology",
                        "content": {
                            "question": "Following a major magnitude 7.2 earthquake, a region experiences dozens of smaller magnitude 4.5 tremors over the following three weeks. What are these secondary tremors called?",
                            "options": [
                                {"id": "A", "text": "Foreshocks"},
                                {"id": "B", "text": "Volcanic Tremors"},
                                {"id": "C", "text": "Aftershocks"},
                                {"id": "D", "text": "Rayleigh Pulses"}
                            ],
                            "correct_answer": "C",
                            "explanation": "Secondary tremors occurring in the same region following a mainshock as surrounding rock blocks readjust to new stress levels are called aftershocks."
                        }
                    }
                ]
            }
        ]
    },

    # Lesson 3: Global Earthquake Zones and Tectonic Associations
    {
        "unit_order": 3,
        "unit_name": "Global Earthquake Zones and Tectonic Associations",
        "lesson_title": "Global Earthquake Zones and Tectonic Associations",
        "pages": [
            {
                "page_number": 1,
                "page_title": "Global Earthquake Distribution & Learning Goals",
                "blocks": [
                    {
                        "block_type": "suggested_image",
                        "component_type": "suggested_image",
                        "title": "Global Plate Boundaries and the Pacific Ring of Fire",
                        "content": {"text": "A world map illustrating the concentration of earthquake epicentres and volcanic arcs along active tectonic plate margins."}
                    },
                    {
                        "block_type": "learning_goal",
                        "component_type": "learning_goal",
                        "title": "Lesson Objectives: Global Seismic Belts",
                        "content": {
                            "text": (
                                "By the end of this lesson, you will be able to:\n\n"
                                "- Locate and characterize the three primary global earthquake belts\n"
                                "- Correlate earthquake distribution with convergent, divergent, and transform plate boundaries\n"
                                "- Explain why intraplate earthquakes occur in stable continental interiors"
                            )
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Prerequisite Spark: The Jigsaw Puzzle Lines",
                        "content": {
                            "text": (
                                "If you look at a world map plotting thousands of earthquake epicentres, you immediately notice they do not "
                                "scatter randomly. Instead, they trace narrow, continuous ribbons across continents and ocean floors. "
                                "These ribbons mark the active boundary lines of Earth's giant tectonic plates!"
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 2,
                "page_title": "The Three Major Global Earthquake Belts",
                "blocks": [
                    {
                        "block_type": "key_terms",
                        "component_type": "key_terms",
                        "title": "Major Seismic Belts",
                        "content": {
                            "terms": [
                                {
                                    "term": "Circum-Pacific Belt (Ring of Fire)",
                                    "definition": "A 40,000-km horseshoe-shaped subduction belt wrapping around the Pacific Ocean basin, accounting for over 80% of all global earthquakes."
                                },
                                {
                                    "term": "Alpine-Himalayan Belt",
                                    "definition": "A major continental collision zone extending from the Mediterranean across the Middle East into the Himalayas and Southeast Asia."
                                },
                                {
                                    "term": "Mid-Ocean Ridges & Rift Systems",
                                    "definition": "Divergent boundaries (including the Mid-Atlantic Ridge and East African Rift) characterized by shallow, tensional crustal earthquakes."
                                },
                                {
                                    "term": "Intraplate Earthquakes",
                                    "definition": "Seismic events occurring in the interior of tectonic plates, triggered by the reactivation of ancient crustal rift faults under intraplate stress."
                                }
                            ]
                        }
                    },
                    {
                        "block_type": "diagram",
                        "component_type": "diagram",
                        "title": "Global Seismic Belts and Tectonic Plate Margins",
                        "content": {
                            "caption": "Map highlighting the Circum-Pacific Belt, Alpine-Himalayan collision zone, and the Mid-Ocean / East African Rift divergent systems.",
                            "svg_placeholder": "SVG_GLOBAL_SEISMIC_BELTS"
                        }
                    }
                ]
            },
            {
                "page_number": 3,
                "page_title": "Plate Boundary Types & Intraplate Seismicity",
                "blocks": [
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Earthquakes at Different Plate Margins",
                        "content": {
                            "text": (
                                "The nature of seismic activity depends on the boundary mechanics:\n\n"
                                "- **Convergent Subduction Zones (e.g., Japan, Chile, Cascades):** Dense oceanic crust subducts under continental plates, generating deep Wadati-Benioff megathrust earthquakes of magnitude 8.0 to 9.5+.\n"
                                "- **Continental Collision Zones (e.g., Himalayas, Alps):** Continents buckle and thrust upward, generating shallow-to-intermediate destructive ruptures.\n"
                                "- **Divergent & Continental Rift Zones (e.g., East African Rift, Mid-Atlantic Ridge):** Tensional rifting produces shallow earthquakes associated with magma ascent and graben subsidence.\n"
                                "- **Transform Boundaries (e.g., San Andreas Fault):** Plates slide horizontally past one another, producing high-frequency shallow strike-slip earthquakes."
                            )
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Intraplate Earthquakes in Kenya and East Africa",
                        "content": {
                            "text": (
                                "While plate margins produce the vast majority of seismic events, intraplate earthquakes strike stable continental interiors. "
                                "In East Africa, the Gregory Rift (Eastern branch) and Albertine Rift (Western branch) form an active continental rift zone "
                                "that periodically transfers stress to ancient interior basement rocks in counties across central and western Kenya."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 4,
                "page_title": "Common Misconceptions Alert",
                "blocks": [
                    {
                        "block_type": "misconception_callout",
                        "component_type": "misconception_callout",
                        "title": "Misconception: Earthquakes Only Occur at Boundaries",
                        "content": {
                            "misconception": "Earthquakes can only ever happen right along plate boundaries.",
                            "correction": "Although the vast majority occur along plate edges, intraplate earthquakes can strike deep within continental interiors due to ancient, buried fault zones reactivating under regional tectonic stress."
                        }
                    }
                ]
            },
            {
                "page_number": 5,
                "page_title": "Formative Assessment MCQs",
                "blocks": [
                    {
                        "block_type": "multiple_choice_question",
                        "component_type": "multiple_choice_question",
                        "title": "Question 1: Primary Subduction Zone Belt",
                        "content": {
                            "question": "Which global earthquake zone is characterized by the subduction of oceanic plates and accounts for the vast majority of the world's deepest and most powerful earthquakes?",
                            "options": [
                                {"id": "A", "text": "Alpine-Himalayan Belt"},
                                {"id": "B", "text": "Mid-Atlantic Ridge Belt"},
                                {"id": "C", "text": "Circum-Pacific Belt ('Ring of Fire')"},
                                {"id": "D", "text": "East African Gregory Rift"}
                            ],
                            "correct_answer": "C",
                            "explanation": "The Circum-Pacific Belt ('Ring of Fire') is dominated by oceanic subduction zones, producing over 80% of all global earthquakes, including the deepest and highest-magnitude megathrust events."
                        }
                    },
                    {
                        "block_type": "multiple_choice_question",
                        "component_type": "multiple_choice_question",
                        "title": "Question 2: Tectonic Origin of Kenyan Earthquakes",
                        "content": {
                            "question": "What tectonic process best explains the occurrence of earthquakes along the active Gregory Rift Valley in Kenya?",
                            "options": [
                                {"id": "A", "text": "Deep-oceanic plate subduction"},
                                {"id": "B", "text": "Continental crust rifting and divergent tension"},
                                {"id": "C", "text": "Continental-continental collision"},
                                {"id": "D", "text": "Strike-slip motion along a transform boundary"}
                            ],
                            "correct_answer": "B",
                            "explanation": "The East African Rift is an active continental divergent boundary where tensional stresses pull the crust apart, triggering normal faulting and shallow crustal earthquakes."
                        }
                    }
                ]
            }
        ]
    },

    # Lesson 4: Measuring Earthquakes: Richter vs. Mercalli Scales
    {
        "unit_order": 4,
        "unit_name": "Measuring Earthquakes: Richter vs. Mercalli Scales",
        "lesson_title": "Measuring Earthquakes: Richter vs. Mercalli Scales",
        "pages": [
            {
                "page_number": 1,
                "page_title": "Measuring Earthquakes & Learning Goals",
                "blocks": [
                    {
                        "block_type": "suggested_image",
                        "component_type": "suggested_image",
                        "title": "Historical Earthquake Intensity and Damage Survey",
                        "content": {"text": "A photograph showing historical structural damage documentation following a major urban earthquake event."}
                    },
                    {
                        "block_type": "learning_goal",
                        "component_type": "learning_goal",
                        "title": "Lesson Objectives: Magnitude vs. Intensity",
                        "content": {
                            "text": (
                                "By the end of this lesson, you will be able to:\n\n"
                                "- Define earthquake magnitude and explain the logarithmic mathematical nature of the Richter Scale\n"
                                "- Define earthquake intensity and describe the qualitative observational basis of the Modified Mercalli Scale\n"
                                "- Contrast the Richter and Mercalli scales across measurement tools, parameters, and geographic variability"
                            )
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Prerequisite Spark: The Rock in the Pond",
                        "content": {
                            "text": (
                                "If you drop a heavy boulder into a pond, the size of the splash and initial waves at the impact point represents the "
                                "'magnitude' of the drop. But the height of the small ripples reaching the distant shore—and whether they merely wiggle "
                                "a lily pad or overturn a toy boat—represents the 'intensity'. One is the total energy at the source; the other is the local effect at a distance!"
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 2,
                "page_title": "Magnitude & The Logarithmic Richter Scale",
                "blocks": [
                    {
                        "block_type": "key_terms",
                        "component_type": "key_terms",
                        "title": "Measurement Principles",
                        "content": {
                            "terms": [
                                {
                                    "term": "Magnitude",
                                    "definition": "An objective, quantitative measurement of the total mechanical energy released at the focus of an earthquake."
                                },
                                {
                                    "term": "Richter Scale",
                                    "definition": "A logarithmic mathematical scale where each whole-number increase represents a 10-fold increase in wave amplitude and a ~32-fold increase in energy release."
                                },
                                {
                                    "term": "Intensity",
                                    "definition": "A qualitative rating of ground shaking severity, human perception, and structural damage at a specific geographic location."
                                },
                                {
                                    "term": "Modified Mercalli Scale",
                                    "definition": "An observational intensity scale ranging from Roman numerals I (imperceptible) to XII (total catastrophic destruction)."
                                }
                            ]
                        }
                    },
                    {
                        "block_type": "diagram",
                        "component_type": "diagram",
                        "title": "Richter Magnitude vs. Mercalli Intensity Scale Comparison",
                        "content": {
                            "caption": "Comparison chart displaying the exponential energy growth of the Richter scale (x32 energy factor per step) versus observed Mercalli intensity damage grades.",
                            "svg_placeholder": "SVG_RICHTER_VS_MERCALLI"
                        }
                    }
                ]
            },
            {
                "page_number": 3,
                "page_title": "Richter vs. Mercalli Comparison Matrix",
                "blocks": [
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Comparison Matrix: Richter vs. Mercalli",
                        "content": {
                            "text": (
                                "| Feature | Richter Scale | Modified Mercalli Scale |\n"
                                "| :--- | :--- | :--- |\n"
                                "| **What it Measures** | Physical wave amplitude & Energy released at focus | Observed shaking effects and structural damage |\n"
                                "| **Type of Data** | Quantitative (Objective mathematical data) | Qualitative (Subjective observation & engineering audits) |\n"
                                "| **Instrument Used** | Seismometer / Seismograph | Human observers and structural damage reports |\n"
                                "| **Scale Range** | Open-ended (Typically 1.0 to 10.0+) | Roman Numerals (I to XII) |\n"
                                "| **Number of Values**| Exactly one single value per earthquake | Multiple values depending on distance and soil type |"
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 4,
                "page_title": "Common Misconceptions Alert",
                "blocks": [
                    {
                        "block_type": "misconception_callout",
                        "component_type": "misconception_callout",
                        "title": "Misconception: Magnitude 8.0 is Twice Magnitude 4.0",
                        "content": {
                            "misconception": "A magnitude 8.0 earthquake is twice as powerful as a magnitude 4.0 earthquake.",
                            "correction": "Because the Richter scale is logarithmic, each step multiplies energy by ~32. A magnitude 8.0 releases 32 x 32 x 32 x 32 = approximately 1,000,000 times more energy than a magnitude 4.0!"
                        }
                    }
                ]
            },
            {
                "page_number": 5,
                "page_title": "Formative Assessment MCQs",
                "blocks": [
                    {
                        "block_type": "multiple_choice_question",
                        "component_type": "multiple_choice_question",
                        "title": "Question 1: Combining Richter and Mercalli Scales",
                        "content": {
                            "question": "An earthquake occurs off the Kenyan coast. Seismologists record its wave amplitude mathematically, while engineers survey cracked brick walls and fallen chimneys in Mombasa. Which combination of scales are they using?",
                            "options": [
                                {"id": "A", "text": "Richter for wave amplitude; Mercalli for cracked walls."},
                                {"id": "B", "text": "Mercalli for wave amplitude; Richter for cracked walls."},
                                {"id": "C", "text": "Richter for both measurements."},
                                {"id": "D", "text": "Mercalli for both measurements."}
                            ],
                            "correct_answer": "A",
                            "explanation": "The Richter scale quantitatively measures physical wave amplitude recorded on instruments. The Modified Mercalli scale qualitatively rates observed physical damage such as cracked walls and collapsed structures."
                        }
                    },
                    {
                        "block_type": "multiple_choice_question",
                        "component_type": "multiple_choice_question",
                        "title": "Question 2: Logarithmic Energy Growth Calculation",
                        "content": {
                            "question": "Approximately how many times more seismic energy is released by a magnitude 7.0 earthquake compared to a magnitude 5.0 earthquake?",
                            "options": [
                                {"id": "A", "text": "2 times more"},
                                {"id": "B", "text": "20 times more"},
                                {"id": "C", "text": "100 times more"},
                                {"id": "D", "text": "1,000 times more"}
                            ],
                            "correct_answer": "D",
                            "explanation": "Each whole-number increase on the Richter scale corresponds to a ~32-fold increase in released energy. Going from magnitude 5.0 to 7.0 is two steps: 32 x 32 = 1,024, which is approximately 1,000 times more energy."
                        }
                    }
                ]
            }
        ]
    },

    # Lesson 5: Seismographs and Interpreting Earthquake Records
    {
        "unit_order": 5,
        "unit_name": "Seismographs and Interpreting Earthquake Records",
        "lesson_title": "Seismographs and Interpreting Earthquake Records",
        "pages": [
            {
                "page_number": 1,
                "page_title": "Seismology Instruments & Learning Goals",
                "blocks": [
                    {
                        "block_type": "suggested_image",
                        "component_type": "suggested_image",
                        "title": "Seismograph Instrument and Recording Station",
                        "content": {"text": "A photograph showing a scientific seismograph recording drum and seismometer station anchored to bedrock."}
                    },
                    {
                        "block_type": "learning_goal",
                        "component_type": "learning_goal",
                        "title": "Lesson Objectives: Seismographs & Seismograms",
                        "content": {
                            "text": (
                                "By the end of this lesson, you will be able to:\n\n"
                                "- Explain the physics principle of inertia governing seismograph operation\n"
                                "- Identify P-waves, S-waves, and surface waves on a seismogram record\n"
                                "- Calculate the S-P time lag interval and explain how three-station triangulation locates an epicentre"
                            )
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Prerequisite Spark: The Suspended Heavy Keyring",
                        "content": {
                            "text": (
                                "Tie a heavy set of keys to a long piece of string and hold it steady in your hand. If you suddenly jerk your "
                                "hand back and forth quickly, you will notice the heavy keys momentarily remain stationary in mid-air! "
                                "This is **inertia**—a heavy mass resists sudden changes in motion. This physics principle allows seismographs to record ground motion."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 2,
                "page_title": "Operating Principles of the Seismograph",
                "blocks": [
                    {
                        "block_type": "key_terms",
                        "component_type": "key_terms",
                        "title": "Seismic Instrumentation Terms",
                        "content": {
                            "terms": [
                                {
                                    "term": "Seismometer",
                                    "definition": "A sensitive sensor that detects ground vibrations anchored directly to bedrock."
                                },
                                {
                                    "term": "Seismograph",
                                    "definition": "An instrument combining a seismometer and a recording mechanism (drum or digital computer) to produce a permanent record of ground motion."
                                },
                                {
                                    "term": "Seismogram",
                                    "definition": "The graphical trace of ground vibrations recorded by a seismograph."
                                },
                                {
                                    "term": "S-P Interval",
                                    "definition": "The time difference in seconds between the arrival of the first compressional P-wave and the subsequent shear S-wave."
                                }
                            ]
                        }
                    },
                    {
                        "block_type": "diagram",
                        "component_type": "diagram",
                        "title": "Seismograph Mechanical Design & 3-Station Triangulation",
                        "content": {
                            "caption": "Left: Mechanical operation of an inertial-mass seismograph. Right: Triangulation method using 3 seismic stations to pinpoint an epicentre.",
                            "svg_placeholder": "SVG_SEISMOGRAPH_AND_TRIANGULATION"
                        }
                    }
                ]
            },
            {
                "page_number": 3,
                "page_title": "Decoding Seismograms & The Triangulation Method",
                "blocks": [
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Seismogram Wave Arrival Sequence",
                        "content": {
                            "text": (
                                "When analyzing a seismogram record, wave arrivals follow a precise chronological sequence:\n\n"
                                "1. **Microseismic Background Noise:** Minor low-amplitude wiggles caused by wind, ocean surf, or traffic.\n"
                                "2. **P-wave Arrival:** The initial sharp, fast high-frequency spike (first body wave).\n"
                                "3. **S-wave Arrival:** A second, larger set of oscillations arriving after the P-wave.\n"
                                "4. **Surface Wave Train:** The final, largest-amplitude, and most destructive ground oscillations."
                            )
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Epicentre Triangulation Using S-P Intervals",
                        "content": {
                            "text": (
                                "Because P-waves travel approximately 1.7 times faster than S-waves, the time gap between their arrivals (S-P interval) "
                                "widens proportionally with distance from the source.\n\n"
                                "- **One Station:** Yields only distance, creating a circle of possible epicentre locations.\n"
                                "- **Two Stations:** Produce two intersecting circles with two potential focal points.\n"
                                "- **Three Stations (Triangulation):** Produce three circles that intersect at exactly **one unique geographic point**—the epicentre!"
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 4,
                "page_title": "Common Misconceptions Alert",
                "blocks": [
                    {
                        "block_type": "misconception_callout",
                        "component_type": "misconception_callout",
                        "title": "Misconception: One Station Can Pinpoint Location",
                        "content": {
                            "misconception": "A single modern seismograph station can pinpoint the exact geographic location of an earthquake.",
                            "correction": "A single station can only determine epicentral distance (radius of a circle). A minimum of three independent recording stations is mathematically required to triangulate the exact point of intersection."
                        }
                    }
                ]
            },
            {
                "page_number": 5,
                "page_title": "Formative Assessment MCQs",
                "blocks": [
                    {
                        "block_type": "multiple_choice_question",
                        "component_type": "multiple_choice_question",
                        "title": "Question 1: Physics Principle of Seismographs",
                        "content": {
                            "question": "What fundamental physics principle explains why the suspended weight in a seismograph remains stationary while the surrounding frame and recording drum shake with the bedrock?",
                            "options": [
                                {"id": "A", "text": "Elastic Rebound"},
                                {"id": "B", "text": "Inertia"},
                                {"id": "C", "text": "Gravity"},
                                {"id": "D", "text": "Magnetic Induction"}
                            ],
                            "correct_answer": "B",
                            "explanation": "Inertia is the physical property of matter that resists changes in motion. The heavy suspended inertial mass remains stationary due to inertia while the frame and drum move with the ground."
                        }
                    },
                    {
                        "block_type": "multiple_choice_question",
                        "component_type": "multiple_choice_question",
                        "title": "Question 2: S-P Lag Interval Calculation",
                        "content": {
                            "question": "A seismic station records a P-wave at 08:00:10 AM and an S-wave at 08:00:45 AM. What is the S-P interval for this station?",
                            "options": [
                                {"id": "A", "text": "10 seconds"},
                                {"id": "B", "text": "35 seconds"},
                                {"id": "C", "text": "45 seconds"},
                                {"id": "D", "text": "55 seconds"}
                            ],
                            "correct_answer": "B",
                            "explanation": "The S-P interval is the difference between S-wave arrival time and P-wave arrival time: 08:00:45 minus 08:00:10 = 35 seconds."
                        }
                    }
                ]
            }
        ]
    },

    # Lesson 6: Environmental and Infrastructure Effects of Earthquakes
    {
        "unit_order": 6,
        "unit_name": "Environmental and Infrastructure Effects of Earthquakes",
        "lesson_title": "Environmental and Infrastructure Effects of Earthquakes",
        "pages": [
            {
                "page_number": 1,
                "page_title": "Seismic Hazards & Learning Goals",
                "blocks": [
                    {
                        "block_type": "suggested_image",
                        "component_type": "suggested_image",
                        "title": "Soil Liquefaction and Infrastructure Disruption",
                        "content": {"text": "A map and photo documentation of soil liquefaction, building tilt, and ground failure following an earthquake."}
                    },
                    {
                        "block_type": "learning_goal",
                        "component_type": "learning_goal",
                        "title": "Lesson Objectives: Primary & Secondary Hazards",
                        "content": {
                            "text": (
                                "By the end of this lesson, you will be able to:\n\n"
                                "- Differentiate between primary ground shaking and secondary hazards (liquefaction, landslides, tsunamis, fires)\n"
                                "- Explain the physics mechanism of soil liquefaction in water-saturated sediments\n"
                                "- Describe the generation and coastal inundation mechanics of undersea earthquake tsunamis"
                            )
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Prerequisite Spark: The Quivering Sandcastle",
                        "content": {
                            "text": (
                                "Think of building a sandcastle with damp sand on a plastic tray. It stands firm. "
                                "Now, tap the plastic tray underneath rapidly. What happens? The damp sand suddenly loses all structural strength, "
                                "turning into a soupy liquid mess, and your castle sinks. This real-world hazard is called **liquefaction**!"
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 2,
                "page_title": "Primary & Secondary Earthquake Hazards",
                "blocks": [
                    {
                        "block_type": "key_terms",
                        "component_type": "key_terms",
                        "title": "Hazard Terminology",
                        "content": {
                            "terms": [
                                {
                                    "term": "Soil Liquefaction",
                                    "definition": "The temporary transformation of water-saturated, unconsolidated sediment into a fluid mass when pore-water pressure increases during strong seismic shaking."
                                },
                                {
                                    "term": "Tsunami",
                                    "definition": "A series of high-energy, long-wavelength ocean waves generated by sudden vertical displacement of the seafloor during subduction zone earthquakes."
                                },
                                {
                                    "term": "Seismically Triggered Landslide",
                                    "definition": "The rapid downward gravitational movement of rock and soil on unstable slopes triggered by ground vibrations."
                                },
                                {
                                    "term": "Secondary Fire Conflagration",
                                    "definition": "Widespread urban fires caused by ruptured underground gas lines and severed electrical cables following ground displacement."
                                }
                            ]
                        }
                    },
                    {
                        "block_type": "diagram",
                        "component_type": "diagram",
                        "title": "Seismic Hazards Matrix: Liquefaction, Tsunamis & Slope Failures",
                        "content": {
                            "caption": "Diagram showing the mechanics of soil liquefaction, subduction tsunami generation, and seismic slope destabilization.",
                            "svg_placeholder": "SVG_SEISMIC_HAZARDS_LIQUEFACTION"
                        }
                    }
                ]
            },
            {
                "page_number": 3,
                "page_title": "Environmental Impacts on Water Tables & Slopes",
                "blocks": [
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Hydrological and Environmental Disruption",
                        "content": {
                            "text": (
                                "Earthquakes cause profound long-term changes in natural systems:\n\n"
                                "- **Groundwater Table Alteration:** Crustal fracturing opens new subterranean fissures, causing borehole water tables to drop or creating sudden artesian hot springs.\n"
                                "- **River Course Damming:** Seismic landslides can dam river valleys, forming temporary landslide dams that pose catastrophic downstream flash-flood risks if they breach.\n"
                                "- **Kenyan Slope Hazards:** In Kenya's Rift Valley escarpments (such as Elgeyo Marakwet and Kerio Valley), tremors frequently destabilize steep weathered slopes, triggering debris flows."
                            )
                        }
                    },
                    {
                        "block_type": "video",
                        "component_type": "video",
                        "title": "Educational Video: Earthquake Liquefaction and Tsunami Mechanics",
                        "content": {
                            "url": "https://www.youtube.com/watch?v=Cvjwt9nnwXY",
                            "title": "Understanding Earthquake Hazards: Liquefaction, Ground Shaking & Tsunamis",
                            "caption": "Educational visualization of seismic wave propagation, soil liquefaction physics, and coastal tsunami inundation."
                        }
                    }
                ]
            },
            {
                "page_number": 4,
                "page_title": "Common Misconceptions Alert",
                "blocks": [
                    {
                        "block_type": "misconception_callout",
                        "component_type": "misconception_callout",
                        "title": "Misconception: Tsunamis Are Tidal Waves",
                        "content": {
                            "misconception": "Tsunamis are tidal waves caused by ocean tides.",
                            "correction": "Tsunamis have nothing to do with tides! Ocean tides are caused by gravitational attraction of the moon and sun, whereas tsunamis are triggered by tectonic vertical displacement of the seafloor."
                        }
                    }
                ]
            },
            {
                "page_number": 5,
                "page_title": "Formative Assessment MCQs",
                "blocks": [
                    {
                        "block_type": "multiple_choice_question",
                        "component_type": "multiple_choice_question",
                        "title": "Question 1: Process of Soil Liquefaction",
                        "content": {
                            "question": "Which geological process describes loose, water-saturated sand behaving like liquid mud when subjected to intense seismic shaking, causing heavy buildings to tilt or sink?",
                            "options": [
                                {"id": "A", "text": "Surface Rupture"},
                                {"id": "B", "text": "Tsunami Wave Generation"},
                                {"id": "C", "text": "Soil Liquefaction"},
                                {"id": "D", "text": "Elastic Rebound"}
                            ],
                            "correct_answer": "C",
                            "explanation": "Soil liquefaction occurs when ground shaking increases pore-water pressure in wet, unconsolidated granular soil, eliminating friction between sand grains and causing the soil to lose its shear bearing capacity."
                        }
                    },
                    {
                        "block_type": "multiple_choice_question",
                        "component_type": "multiple_choice_question",
                        "title": "Question 2: Undersea Fault Displacement Hazard",
                        "content": {
                            "question": "Undersea earthquakes along subduction zones can displace massive volumes of ocean water vertically. What destructive hazard does this produce?",
                            "options": [
                                {"id": "A", "text": "Pyroclastic Flows"},
                                {"id": "B", "text": "Solfataras"},
                                {"id": "C", "text": "Tsunamis"},
                                {"id": "D", "text": "Geysers"}
                            ],
                            "correct_answer": "C",
                            "explanation": "Sudden vertical displacement of the seafloor along a megathrust fault displaces the water column above, initiating a series of high-energy, fast-traveling tsunami waves."
                        }
                    }
                ]
            }
        ]
    },

    # Lesson 7: Case Study: Global and Local Earthquake Risk Comparisons
    {
        "unit_order": 7,
        "unit_name": "Case Study: Global and Local Earthquake Risk Comparisons",
        "lesson_title": "Case Study: Global and Local Earthquake Risk Comparisons",
        "pages": [
            {
                "page_number": 1,
                "page_title": "Comparative Seismic Vulnerability & Learning Goals",
                "blocks": [
                    {
                        "block_type": "suggested_image",
                        "component_type": "suggested_image",
                        "title": "Structural Vulnerability and Earthquake Aftermath",
                        "content": {"text": "A photograph showing unreinforced masonry building destruction following the 2010 Port-au-Prince, Haiti earthquake."}
                    },
                    {
                        "block_type": "learning_goal",
                        "component_type": "learning_goal",
                        "title": "Lesson Objectives: Risk, Hazard & Vulnerability",
                        "content": {
                            "text": (
                                "By the end of this lesson, you will be able to:\n\n"
                                "- Compare the human and infrastructure toll of equivalent earthquakes in high-resilience vs. high-vulnerability nations (e.g., Japan vs. Haiti)\n"
                                "- Analyze how building codes, governance, and engineering (base isolation) mitigate earthquake mortality\n"
                                "- Evaluate historical earthquake risk and vulnerable geological basins in Kenya"
                            )
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Prerequisite Spark: The Two Toy Houses",
                        "content": {
                            "text": (
                                "If you build two toy houses—one out of interlocking wooden blocks joined with flexible steel screws, "
                                "and another out of loose, heavy brittle bricks stacked without cement—and shake the table vigorously, "
                                "which one survives? The brittle house crumbles instantly. This models the stark contrast between strict "
                                "seismic building engineering and unreinforced construction!"
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 2,
                "page_title": "Disaster Equation: Hazard vs. Vulnerability",
                "blocks": [
                    {
                        "block_type": "key_terms",
                        "component_type": "key_terms",
                        "title": "Risk Analysis Formula",
                        "content": {
                            "terms": [
                                {
                                    "term": "Seismic Hazard",
                                    "definition": "The physical probability and intensity of ground shaking occurring in a specific geographic area."
                                },
                                {
                                    "term": "Vulnerability",
                                    "definition": "The degree to which a community's buildings, infrastructure, economy, and population are susceptible to damage."
                                },
                                {
                                    "term": "Seismic Risk",
                                    "definition": "The expected human loss and destruction, calculated as: Risk = Hazard × Vulnerability ÷ Capacity."
                                },
                                {
                                    "term": "Base Isolation",
                                    "definition": "An earthquake engineering technique mounting buildings on flexible rubber and steel bearings that decouple the superstructure from ground motion."
                                }
                            ]
                        }
                    },
                    {
                        "block_type": "diagram",
                        "component_type": "diagram",
                        "title": "Structural Vulnerability vs. Base Isolation Engineering",
                        "content": {
                            "caption": "Engineering diagram comparing shear collapse of unreinforced masonry against seismic protection via base isolators and tuned mass dampers.",
                            "svg_placeholder": "SVG_SEISMIC_VULNERABILITY_BASE_ISOLATION"
                        }
                    }
                ]
            },
            {
                "page_number": 3,
                "page_title": "Case Study Comparison: Japan (2011) vs. Haiti (2010)",
                "blocks": [
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Comparative Disaster Analysis",
                        "content": {
                            "text": (
                                "| Factor | High-Resilience Region (e.g., Japan 2011 Mw 9.0) | High-Vulnerability Region (e.g., Haiti 2010 Mw 7.0) |\n"
                                "| :--- | :--- | :--- |\n"
                                "| **Building Materials** | Reinforced steel framing, flexible base isolators, safety glass | Brittle unreinforced concrete, heavy slab roofs, unbonded brick |\n"
                                "| **Building Code Laws** | Strictly enforced national seismic codes with strict inspections | Weak or non-existent enforcement; informal hillside settlements |\n"
                                "| **Public Preparedness**| Mandatory nationwide drills, smartphone early warning alerts | Low public awareness, lack of community evacuation plans |\n"
                                "| **Emergency Response**| Rapid automated gas shut-offs, professional disaster taskforces | Limited search-and-rescue equipment, collapsed medical clinics |\n"
                                "| **Shaking Casualties**| Minimal casualties directly from building collapse | Over 200,000 deaths from pancaked multi-story buildings |"
                            )
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "East Africa & Kenya Earthquake Risk Profile",
                        "content": {
                            "text": (
                                "Although Kenya is not a subduction zone, continental rifting creates substantial seismic risk:\n\n"
                                "- **Lake Tanganyika (2005):** A powerful magnitude 6.8 earthquake shook East Africa, sending tremors across Nairobi and cracking buildings.\n"
                                "- **Local Soil Amplification:** In Nairobi and surrounding towns, deep clay basins and unconsolidated sediments can amplify seismic ground shaking, highlighting the need for enforced structural building standards in Kenya."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 4,
                "page_title": "Common Misconceptions Alert",
                "blocks": [
                    {
                        "block_type": "misconception_callout",
                        "component_type": "misconception_callout",
                        "title": "Misconception: Magnitude Alone Dictates Casualties",
                        "content": {
                            "misconception": "High death tolls are caused solely by the magnitude of the earthquake.",
                            "correction": "As the saying goes: 'Earthquakes don't kill people; collapsing buildings do.' Structural vulnerability, poor construction quality, and lack of emergency preparedness are the primary drivers of disaster mortality."
                        }
                    }
                ]
            },
            {
                "page_number": 5,
                "page_title": "Formative Assessment MCQs",
                "blocks": [
                    {
                        "block_type": "multiple_choice_question",
                        "component_type": "multiple_choice_question",
                        "title": "Question 1: Explaining Casualty Disparities",
                        "content": {
                            "question": "Why did the 2010 earthquake in Haiti (magnitude 7.0) cause vastly higher casualties than the 2011 Tohoku earthquake in Japan (magnitude 9.0), which released hundreds of times more energy?",
                            "options": [
                                {"id": "A", "text": "Haiti's earthquake was an ultra-deep event."},
                                {"id": "B", "text": "Japan has no coastal settlements."},
                                {"id": "C", "text": "Haiti had high structural vulnerability due to unreinforced concrete buildings and lack of building code enforcement."},
                                {"id": "D", "text": "Japan's earthquake occurred in an uninhabited desert."}
                            ],
                            "correct_answer": "C",
                            "explanation": "Casualty rates depend heavily on structural vulnerability. In Haiti, poor building design, heavy concrete roofs, and lack of enforced seismic codes led to widespread building collapse, whereas Japan's infrastructure is engineered to withstand violent shaking."
                        }
                    },
                    {
                        "block_type": "multiple_choice_question",
                        "component_type": "multiple_choice_question",
                        "title": "Question 2: Base Isolation Engineering Technique",
                        "content": {
                            "question": "Which structural engineering technique protects skyscrapers by separating the building's superstructure from the shaking foundation using flexible rubber and steel bearings?",
                            "options": [
                                {"id": "A", "text": "Timber pole reinforcement"},
                                {"id": "B", "text": "Base Isolation"},
                                {"id": "C", "text": "Increasing heavy concrete roof slab thickness"},
                                {"id": "D", "text": "Unreinforced masonry stacking"}
                            ],
                            "correct_answer": "B",
                            "explanation": "Base isolation involves mounting buildings on flexible bearings, rubber pads, or shock absorbers that absorb seismic ground accelerations and prevent them from transferring into the building."
                        }
                    }
                ]
            }
        ]
    },

    # Lesson 8: Earthquake Preparedness, Mitigation, and Emergency Action
    {
        "unit_order": 8,
        "unit_name": "Earthquake Preparedness, Mitigation, and Emergency Action",
        "lesson_title": "Earthquake Preparedness, Mitigation, and Emergency Action",
        "pages": [
            {
                "page_number": 1,
                "page_title": "Disaster Preparedness & Learning Goals",
                "blocks": [
                    {
                        "block_type": "suggested_image",
                        "component_type": "suggested_image",
                        "title": "Drop, Cover, and Hold On Safety Demonstration",
                        "content": {"text": "A photograph showing students and citizens demonstrating the proper Drop, Cover, and Hold On emergency earthquake drill."}
                    },
                    {
                        "block_type": "learning_goal",
                        "component_type": "learning_goal",
                        "title": "Lesson Objectives: Preparedness & Mitigation",
                        "content": {
                            "text": (
                                "By the end of this lesson, you will be able to:\n\n"
                                "- Differentiate between structural mitigation and non-structural household preparedness\n"
                                "- Execute the universally recommended personal safety protocol: 'Drop, Cover, and Hold On'\n"
                                "- Assemble a complete household earthquake emergency kit and draft an evacuation plan"
                            )
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Prerequisite Spark: The Practiced Fire Drill",
                        "content": {
                            "text": (
                                "When a fire alarm sounds in a school, you don't pause to deliberate; you walk along the practiced exit route. "
                                "An earthquake provides zero warning sirens. When the floor shakes, your physical reaction must be practiced and "
                                "automatic to protect your head and vital organs from falling debris!"
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 2,
                "page_title": "Structural vs. Non-Structural Mitigation",
                "blocks": [
                    {
                        "block_type": "key_terms",
                        "component_type": "key_terms",
                        "title": "Mitigation Categories",
                        "content": {
                            "terms": [
                                {
                                    "term": "Mitigation",
                                    "definition": "Proactive structural and non-structural actions taken before a hazard strikes to reduce vulnerability and loss of life."
                                },
                                {
                                    "term": "Structural Mitigation",
                                    "definition": "Engineering modifications to load-bearing frames, retrofitting foundations, and bolting walls to resist seismic shear."
                                },
                                {
                                    "term": "Non-Structural Preparedness",
                                    "definition": "Household and institutional measures such as anchoring heavy furniture, stockpiling emergency kits, and practicing evacuation drills."
                                },
                                {
                                    "term": "Drop, Cover, and Hold On",
                                    "definition": "The internationally recognized physical response protocol to survive active earthquake shaking."
                                }
                            ]
                        }
                    },
                    {
                        "block_type": "diagram",
                        "component_type": "diagram",
                        "title": "Drop, Cover, and Hold On Survival Protocol Infographic",
                        "content": {
                            "caption": "Step-by-step physical guide to personal protection during ground shaking: 1. Drop, 2. Cover, 3. Hold On, plus essential survival kit checklist.",
                            "svg_placeholder": "SVG_DROP_COVER_HOLD_ON"
                        }
                    }
                ]
            },
            {
                "page_number": 3,
                "page_title": "The Action Timeline: Before, During, and After",
                "blocks": [
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Chronological Earthquake Action Protocol",
                        "content": {
                            "text": (
                                "Disaster risk reduction requires coordinated actions across three distinct phases:\n\n"
                                "1. **BEFORE the Shaking (Preparation & Mitigation):**\n"
                                "   - Bolt tall bookcases, cupboards, and solar water heaters to wall studs using L-brackets.\n"
                                "   - Store heavy or glass objects on bottom shelves.\n"
                                "   - **Emergency Survival Kit:** Water (3 liters/person/day for 3 days), canned food, flashlight, first-aid kit, and an acoustic emergency whistle.\n\n"
                                "2. **DURING the Shaking (Survival Action):**\n"
                                "   - **Indoors:** DROP to hands and knees, COVER under a sturdy table/desk, and HOLD ON until shaking stops. Do not run outside during active shaking.\n"
                                "   - **Outdoors:** Move to an open field away from buildings, power lines, and tall trees.\n"
                                "   - **In a Vehicle:** Safely pull over away from overpasses and remain inside.\n\n"
                                "3. **AFTER the Shaking (Response & Evacuation):**\n"
                                "   - Check for injuries and apply first aid.\n"
                                "   - Check for gas leaks and turn off the main valve. Do not flip electrical switches.\n"
                                "   - Evacuate via stairs (never use elevators) anticipating aftershocks."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 4,
                "page_title": "Common Misconceptions Alert",
                "blocks": [
                    {
                        "block_type": "misconception_callout",
                        "component_type": "misconception_callout",
                        "title": "Misconception: Stand in a Doorway During Shaking",
                        "content": {
                            "misconception": "Standing in a doorway is the safest position during an earthquake.",
                            "correction": "This is outdated advice from old adobe homes! In modern buildings, doorways are not structurally stronger and offer no protection against flying glass or falling debris. Drop, Cover, and Hold On under a sturdy desk is the safest action."
                        }
                    }
                ]
            },
            {
                "page_number": 5,
                "page_title": "Formative Assessment MCQs",
                "blocks": [
                    {
                        "block_type": "multiple_choice_question",
                        "component_type": "multiple_choice_question",
                        "title": "Question 1: Safest Indoor Action During Shaking",
                        "content": {
                            "question": "What is the universally recommended physical safety action to take if you are inside a classroom when a sudden earthquake tremor strikes?",
                            "options": [
                                {"id": "A", "text": "Run outside to the sports field immediately while the ground is shaking."},
                                {"id": "B", "text": "Stand under a doorway and hold the frame."},
                                {"id": "C", "text": "Drop to your hands and knees, take cover under a sturdy desk, and hold on."},
                                {"id": "D", "text": "Climb onto a chair to avoid the vibrating floor."}
                            ],
                            "correct_answer": "C",
                            "explanation": "'Drop, Cover, and Hold On' protects your head and body from falling debris and prevents you from being thrown to the ground. Running outside during shaking exposes you to falling glass and falling bricks."
                        }
                    },
                    {
                        "block_type": "multiple_choice_question",
                        "component_type": "multiple_choice_question",
                        "title": "Question 2: Non-Structural Preparedness Strategy",
                        "content": {
                            "question": "Which of the following is categorized as a non-structural earthquake preparedness strategy?",
                            "options": [
                                {"id": "A", "text": "Retrofitting a bridge with steel cross-bracing."},
                                {"id": "B", "text": "Bolting tall bookshelves and heavy wardrobes securely to wall studs with L-brackets."},
                                {"id": "C", "text": "Installing rubber base isolators under a hospital foundation."},
                                {"id": "D", "text": "Re-routing highways away from active fault lines."}
                            ],
                            "correct_answer": "B",
                            "explanation": "Bolting furniture is a non-structural preparedness strategy because it secures internal furnishings without modifying the building's load-bearing structural framework."
                        }
                    }
                ]
            }
        ]
    },

    # Lesson 9: Designing Public Safety Communication Messages
    {
        "unit_order": 9,
        "unit_name": "Designing Public Safety Communication Messages",
        "lesson_title": "Designing Public Safety Communication Messages",
        "pages": [
            {
                "page_number": 1,
                "page_title": "Risk Communication & Learning Goals",
                "blocks": [
                    {
                        "block_type": "suggested_image",
                        "component_type": "suggested_image",
                        "title": "Public Disaster Preparedness Education and Drills",
                        "content": {"text": "A photograph showing community emergency services and school students engaging in public disaster preparedness training."}
                    },
                    {
                        "block_type": "learning_goal",
                        "component_type": "learning_goal",
                        "title": "Lesson Objectives: Public Safety Messaging",
                        "content": {
                            "text": (
                                "By the end of this lesson, you will be able to:\n\n"
                                "- Explain the core principles of effective emergency risk communication\n"
                                "- Design concise, actionable public safety posters and 30-second radio PSAs tailored to vulnerable communities\n"
                                "- Critique emergency alerts for clarity, accessibility, and actionable directives"
                            )
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Prerequisite Spark: The Simplified Game Rules",
                        "content": {
                            "text": (
                                "When explaining an emergency game to children, using a 10-page dense rulebook creates panic and confusion. "
                                "A short, memorable slogan with clear visual actions produces immediate understanding. "
                                "Emergency risk communication functions the same way: keep it clear, simple, and instantly actionable!"
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 2,
                "page_title": "Principles of Effective Emergency Communication",
                "blocks": [
                    {
                        "block_type": "key_terms",
                        "component_type": "key_terms",
                        "title": "Risk Communication Concepts",
                        "content": {
                            "terms": [
                                {
                                    "term": "Risk Communication",
                                    "definition": "The rapid, bidirectional exchange of actionable information and safety directives between disaster experts and threatened populations."
                                },
                                {
                                    "term": "Actionable Directives",
                                    "definition": "Specific, unambiguous physical instructions directing individuals on what to do rather than describing theoretical hazards."
                                },
                                {
                                    "term": "Public Service Announcement (PSA)",
                                    "definition": "A short broadcast broadcast message designed to educate communities and guide immediate life-saving behavior."
                                }
                            ]
                        }
                    },
                    {
                        "block_type": "diagram",
                        "component_type": "diagram",
                        "title": "Emergency Public Safety Broadcast & Poster Design Layout",
                        "content": {
                            "caption": "Framework showing the 5 pillars of risk communication (Simplicity, Actionability, Visibility, Target Specificity, Multi-Channel) and public broadcast templates.",
                            "svg_placeholder": "SVG_PUBLIC_SAFETY_BROADCAST"
                        }
                    }
                ]
            },
            {
                "page_number": 3,
                "page_title": "Public Safety Poster & Radio Script Templates",
                "blocks": [
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Poster and Radio Broadcast Templates",
                        "content": {
                            "text": (
                                "Effective emergency communication combines visual posters and audio broadcasts:\n\n"
                                "### 1. Public Safety Poster Template\n"
                                "- **Headline:** DROP, COVER, AND HOLD ON!\n"
                                "- **Sub-headline:** Protect yourself immediately during ground shaking.\n"
                                "- **Visual Actions:**\n"
                                "  1. **DROP:** To your hands and knees.\n"
                                "  2. **COVER:** Under a sturdy desk or table.\n"
                                "  3. **HOLD ON:** Until all shaking ceases.\n"
                                "- **Call to Action:** Prepare your household survival kit and practice regular family drills!\n\n"
                                "### 2. 30-Second Radio PSA Script\n"
                                "- **[Sound Effect: Brief subterranean rumble]**\n"
                                "- **Narrator:** 'Did you feel that? Earthquake shaking begins without warning! If ground tremors strike, do NOT run outside into falling debris. Instantly DROP to your hands and knees. COVER your head and neck beneath a sturdy desk or table. And HOLD ON until shaking stops. Protect yourself and your family. Stay safe, Kenya!'"
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 4,
                "page_title": "Common Misconceptions Alert",
                "blocks": [
                    {
                        "block_type": "misconception_callout",
                        "component_type": "misconception_callout",
                        "title": "Misconception: Alerts Should Explain Science",
                        "content": {
                            "misconception": "Emergency alert messages should explain the geological wave mechanics of the earthquake.",
                            "correction": "During an emergency, people need immediate, unambiguous physical instructions on how to protect their lives, not a geology lecture. Keep emergency messages 100% focused on direct action."
                        }
                    }
                ]
            },
            {
                "page_number": 5,
                "page_title": "Formative Assessment MCQs",
                "blocks": [
                    {
                        "block_type": "multiple_choice_question",
                        "component_type": "multiple_choice_question",
                        "title": "Question 1: Most Effective Emergency Headline",
                        "content": {
                            "question": "Which of the following public service headlines represents the most effective risk communication message during an active earthquake emergency?",
                            "options": [
                                {"id": "A", "text": "'Extensive Lithospheric Tectonic Shear Underway: Exercise Caution!'"},
                                {"id": "B", "text": "'Earthquake! Drop, Cover, and Hold On under a sturdy desk now!'"},
                                {"id": "C", "text": "'Seismic Wave Velocity Discrepancy Detected: Structural Analysis Advised.'"},
                                {"id": "D", "text": "'Notice: Earthquakes are quantified logarithmically on the Richter Scale!'"}
                            ],
                            "correct_answer": "B",
                            "explanation": "Effective emergency messaging must be concise, unambiguous, and immediately actionable, instructing people on the exact physical survival steps to take rather than using abstract technical jargon."
                        }
                    },
                    {
                        "block_type": "multiple_choice_question",
                        "component_type": "multiple_choice_question",
                        "title": "Question 2: Rift Valley Community Message Targeting",
                        "content": {
                            "question": "When designing a public safety campaign for a school located in Naivasha town along the Kenyan Rift Valley, which local preparedness measure is most critical to emphasize?",
                            "options": [
                                {"id": "A", "text": "Evacuating immediately to avoid deep-ocean marine tsunamis."},
                                {"id": "B", "text": "Extinguishing volcanic lava flows with garden hoses."},
                                {"id": "C", "text": "Conducting regular earthquake drills and securing loose classroom furniture to walls."},
                                {"id": "D", "text": "Constructing underground blast shelters against nuclear explosions."}
                            ],
                            "correct_answer": "C",
                            "explanation": "Naivasha is located in the seismically active Gregory Rift Valley. School preparedness must focus on practical, localized actions such as practicing drills and securing classroom furniture to wall studs."
                        }
                    }
                ]
            }
        ]
    },

    # Lesson 10: Topic Review, Synthesis, and Unit Assessment
    {
        "unit_order": 10,
        "unit_name": "Topic Review, Synthesis, and Unit Assessment",
        "lesson_title": "Topic Review, Synthesis, and Unit Assessment",
        "pages": [
            {
                "page_number": 1,
                "page_title": "Topic Synthesis & Learning Goals",
                "blocks": [
                    {
                        "block_type": "suggested_image",
                        "component_type": "suggested_image",
                        "title": "Seismology Monitoring Network and ShakeMap Synthesis",
                        "content": {"text": "A comprehensive scientific seismicity map showing earthquake epicentres, shake intensity zones, and fault lines."}
                    },
                    {
                        "block_type": "learning_goal",
                        "component_type": "learning_goal",
                        "title": "Lesson Objectives: Unit Synthesis & Assessment",
                        "content": {
                            "text": (
                                "By the end of this lesson, you will be able to:\n\n"
                                "- Synthesize the complete seismic chain: plate tectonics -> fault stress -> focus fracture -> wave propagation -> surface impact\n"
                                "- Integrate quantitative seismology (Richter/triangulation) with qualitative disaster mitigation (Mercalli/building codes)\n"
                                "- Demonstrate mastery across all theoretical and applied concepts of the Earthquakes topic"
                            )
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Prerequisite Spark: Connecting the Whole Puzzle",
                        "content": {
                            "text": (
                                "We have traveled from the deep interior of the Earth—where plate movements build up silent, massive stresses in rock—"
                                "to the sudden fracture at the focus, the outward rush of seismic waves, the quantitative measurement on seismographs, "
                                "and finally to our homes and schools, where our personal decisions and preparedness can save our lives. "
                                "Let's bring all these puzzle pieces together!"
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 2,
                "page_title": "The Master Seismic Chain of Events",
                "blocks": [
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "The Unified Seismic Sequence",
                        "content": {
                            "text": (
                                "Understanding earthquakes requires linking each step in the seismic chain of events:\n\n"
                                "1. **Tectonic Driving Forces:** Mantle convection currents drive lithospheric plate motions against frictional boundaries.\n"
                                "2. **Elastic Strain & Fracture:** Rocks reach their elastic limit and rupture at the **focus (hypocentre)**, releasing stored strain.\n"
                                "3. **Wave Radiation:** Primary (compressional) and Secondary (shear) body waves travel through rock, while high-amplitude Surface waves propagate along the crust.\n"
                                "4. **Measurement & Triangulation:** Seismographs record ground motion via inertia. Seismologists calculate the **S-P lag interval** across at least three stations to triangulate the epicentre.\n"
                                "5. **Quantification:** The logarithmic **Richter scale** calculates energy magnitude, while the **Modified Mercalli scale** maps observed structural intensity.\n"
                                "6. **Disaster Mitigation:** Engineered building codes, base isolation, furniture anchoring, and practiced **Drop, Cover, and Hold On** protocols save lives."
                            )
                        }
                    },
                    {
                        "block_type": "diagram",
                        "component_type": "diagram",
                        "title": "Master Synthesis: Geological Cause to Disaster Mitigation",
                        "content": {
                            "caption": "Comprehensive flowchart synthesizing plate tectonics, fault rupture, wave mechanics, seismological triangulation, hazards, and emergency response.",
                            "svg_placeholder": "SVG_EARTHQUAKE_SYNTHESIS"
                        }
                    }
                ]
            },
            {
                "page_number": 3,
                "page_title": "Topic Review & Mastery Checklist",
                "blocks": [
                    {
                        "block_type": "key_terms",
                        "component_type": "key_terms",
                        "title": "Mastery Concept Check",
                        "content": {
                            "terms": [
                                {
                                    "term": "Focus vs. Epicentre",
                                    "definition": "Focus is the subterranean fracture point; Epicentre is the point on the Earth's surface directly above the focus."
                                },
                                {
                                    "term": "P-Waves vs. S-Waves",
                                    "definition": "P-waves are fast compressional waves (travel through solids and liquids); S-waves are slower shear waves (travel only through solids)."
                                },
                                {
                                    "term": "Richter vs. Mercalli",
                                    "definition": "Richter quantitatively measures focused energy logarithmically; Mercalli qualitatively rates surface damage from I to XII."
                                },
                                {
                                    "term": "Triangulation",
                                    "definition": "The geometric process of intersecting three distance circles from three separate seismic stations to pinpoint the epicentre."
                                }
                            ]
                        }
                    }
                ]
            },
            {
                "page_number": 4,
                "page_title": "Comprehensive Unit Assessment MCQs",
                "blocks": [
                    {
                        "block_type": "multiple_choice_question",
                        "component_type": "multiple_choice_question",
                        "title": "Question 1: Triangulating Epicentre Location",
                        "content": {
                            "question": "A seismological station in Eldoret detects an earthquake. P-waves are recorded at 12:15:30 PM, and S-waves are recorded at 12:16:10 PM. If the station uses three separate recordings to find the epicentre, what is this process called?",
                            "options": [
                                {"id": "A", "text": "Logarithmic calibration"},
                                {"id": "B", "text": "Seismological attenuation"},
                                {"id": "C", "text": "Triangulation"},
                                {"id": "D", "text": "Seismic retrofitting"}
                            ],
                            "correct_answer": "C",
                            "explanation": "Triangulation is the mathematical method of drawing three intersecting distance circles from three separate seismic stations to pinpoint the exact location of an earthquake epicentre."
                        }
                    },
                    {
                        "block_type": "multiple_choice_question",
                        "component_type": "multiple_choice_question",
                        "title": "Question 2: Mitigation Measure for Secondary Fires",
                        "content": {
                            "question": "Which structural mitigation measure is most effective for reducing the catastrophic risk of secondary fires following a major urban earthquake?",
                            "options": [
                                {"id": "A", "text": "Installing thick concrete walls on all classroom doorways."},
                                {"id": "B", "text": "Securing tall wooden bookshelves with L-brackets."},
                                {"id": "C", "text": "Installing automated gas shut-off valves triggered by seismic vibrations."},
                                {"id": "D", "text": "Constructing buildings on loose, water-saturated sand deposits."}
                            ],
                            "correct_answer": "C",
                            "explanation": "Automated seismic shut-off valves instantly cut off municipal gas supplies upon detecting ground shaking, preventing severed gas lines from sparking uncontrollable post-earthquake conflagrations."
                        }
                    },
                    {
                        "block_type": "multiple_choice_question",
                        "component_type": "multiple_choice_question",
                        "title": "Question 3: Modified Mercalli Parameter",
                        "content": {
                            "question": "Which parameter does the Modified Mercalli Scale measure to evaluate an earthquake?",
                            "options": [
                                {"id": "A", "text": "The mathematical amplitude of the largest body wave on a seismometer."},
                                {"id": "B", "text": "The exact focal depth of the hypocentre in kilometers."},
                                {"id": "C", "text": "The total physical energy released at the focus in joules."},
                                {"id": "D", "text": "The qualitative damage observed on buildings, landscapes, and human populations."}
                            ],
                            "correct_answer": "D",
                            "explanation": "The Modified Mercalli scale is a qualitative intensity scale based on observed structural destruction, ground deformation, and human sensory perceptions ranging from I (not felt) to XII (total catastrophe)."
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
    print("Starting Ingestion: Grade 10 CBC Geography — Topic 9: Earthquakes")
    print("=" * 80)

    with transaction.atomic():
        # 1. Resolve Hierarchy
        curriculum = Curriculum.objects.filter(name__iexact="CBC").first()
        if not curriculum:
            raise ValueError("Curriculum 'CBC' not found in database!")

        grade = Grade.objects.filter(curriculum=curriculum, name__icontains="10").first()
        if not grade:
            raise ValueError("Grade 10 not found under CBC!")

        subject = Subject.objects.filter(id=37).first() or Subject.objects.filter(grade=grade, name="Geography").first()
        if not subject:
            raise ValueError("Subject 'Geography' (ID: 37) not found under Grade 10!")

        # 2. Get or Create Topic 9
        topic, _ = Topic.objects.get_or_create(
            subject=subject,
            order=9,
            defaults={
                "name": "Earthquakes",
                "description": "Strand 2.0: Natural Systems and Processes - Topic 9: Earthquakes"
            }
        )
        topic.name = "Earthquakes"
        topic.description = "Strand 2.0: Natural Systems and Processes - Topic 9: Earthquakes"
        topic.save()

        print(f"Target Topic: [{topic.id}] Order {topic.order}: {topic.name} under Subject: {subject.name} (Grade 10 CBC)")

        total_blocks_created = 0

        for les_data in LESSONS_DATA:
            u_order = les_data["unit_order"]
            u_name = clean_text(les_data["unit_name"])
            les_title = clean_text(les_data["lesson_title"])

            unit, _ = LearningUnit.objects.get_or_create(
                topic=topic,
                order=u_order,
                defaults={"name": u_name, "description": f"Learning unit for {u_name}"}
            )
            unit.name = u_name
            unit.save()

            lesson, _ = Lesson.objects.get_or_create(
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

            # Clear existing blocks for idempotency
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
    print(f"Ingestion completed successfully for Grade 10 Geography Topic 9! (Total Blocks: {total_blocks_created})")
    print("=" * 80)

if __name__ == "__main__":
    run_ingestion()
