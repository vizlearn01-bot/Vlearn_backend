"""
VLearn Grade 10 Aviation — Topic 364: Aircraft Technical Drawing
Production Ingestion Engine

Curriculum: CBC
Subject: Aviation (Subject ID: 44)
Topic: Aircraft Technical Drawing (Topic ID: 364, Order: 6)

Ingests 5 Comprehensive Learning Units & Lessons (50 Concept Cards):
  1. Purpose of Aircraft-Related Drawings (Unit Order 0)
  2. Isometric Principles and Instruments (Unit Order 1)
  3. Drawing Aircraft-Related Forms: The Crating Method (Unit Order 2)
  4. Dimensioning and Technical Notes (Unit Order 3)
  5. Drawing Interpretation in Aircraft Work (Unit Order 4)

Usage:
  ./venv/bin/python curriculum/ingest_grade10_aviation_topic364.py [--replace]
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
    """Removes bracket citations, internal visual prompt markers, and normalizes typography."""
    if not text:
        return ""
    # Remove bracket citations like [10], [71], [10, 71]
    text = re.sub(r'\[(?:\d+|image_\d+|S\d+.*?|[\d,\s]+)\]', '', text)
    # Remove internal visual generation tags
    text = re.sub(r'\[VISUAL:\s*[^\]]+\]', '', text, flags=re.IGNORECASE)
    # Remove practical task, scenario and application internal markers
    text = re.sub(r'\[(?:REAL WORLD APPLICATION|PRACTICAL TASK|SAFETY SCENARIO|SCENARIO)[^\]]*\]', '', text, flags=re.IGNORECASE)
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

def build_topic364_curriculum():
    """Returns the pedagogical page and block structure for Grade 10 Aviation Topic 364."""
    return [
        # =====================================================================
        # LESSON 1: Purpose of Aircraft-Related Drawings
        # =====================================================================
        {
            "unit_order": 0,
            "unit_name": "Purpose of Aircraft-Related Drawings",
            "unit_description": "Examine the role of technical drawings in aviation safety, distinguishing freehand sketches from certified engineering blueprints, and navigating Illustrated Parts Catalogs and Aircraft Maintenance Manuals.",
            "lesson_title": "Purpose of Aircraft-Related Drawings",
            "pages": [
                # Card 1: Visual Hook & Learning Focus
                [
                    {
                        "type": "suggested_image",
                        "title": "Historical Wright Brothers Airplane Blueprint Drawing",
                        "content": {
                            "title": "Historical Wright Brothers Airplane Blueprint Drawing",
                            "caption": "The original 1903 Wright Airplane engineering blueprint, showcasing how precise technical line drawings, dimensions, and standardized views establish the universal visual language of flight safety.",
                            "resolved_image_url": "https://upload.wikimedia.org/wikipedia/commons/4/4c/The_Original_%22Wright%22_1903_Airplane_Drawing%2C_Blueprint_-_NARA_-_61631965.jpg"
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Learning Focus: Technical Drawings in Aviation",
                        "content": {
                            "title": "Learning Focus: Technical Drawings in Aviation",
                            "goals": [
                                "Identify the vital purpose of technical drawings as the standardized universal language of aerospace engineering.",
                                "Distinguish informal freehand sketches from certified, scale-accurate engineering technical drawings.",
                                "Navigate the complementary roles of the Aircraft Maintenance Manual (AMM) and Illustrated Parts Catalog (IPC).",
                                "Understand the strict regulatory authority and airworthiness boundaries embedded in engineering blueprints."
                            ]
                        }
                    }
                ],
                # Card 2: Foundational Terminology
                [
                    {
                        "type": "definition_card",
                        "title": "Core Technical Drawing Terminology",
                        "content": {
                            "title": "Core Technical Vocabulary",
                            "definitions": [
                                {
                                    "term": "Technical Drawing",
                                    "definition": "A highly precise, scale-accurate graphical representation communicating design specifications, exact dimensions, materials, tolerances, and assembly sequences.",
                                    "example": "A certified airframe blueprint showing the rivet pitch and aluminum alloy grade for a wing spar splice."
                                },
                                {
                                    "term": "Pictorial Drawing",
                                    "definition": "A three-dimensional representation of an object on a flat sheet, displaying length, width, and height simultaneously in a single view.",
                                    "example": "An isometric rendering of an engine mount bracket showing all three faces at once."
                                },
                                {
                                    "term": "Orthographic Projection",
                                    "definition": "A drafting method representing an object using separate two-dimensional views (Front, Top, and Side) projected at right angles to display true shapes.",
                                    "example": "A multi-view drawing showing the exact profile and hole locations of a landing gear trunnion."
                                },
                                {
                                    "term": "Aircraft Maintenance Manual (AMM)",
                                    "definition": "The manufacturer's regulatory technical publication containing detailed step-by-step procedures, clearances, and torque values for servicing and repairing aircraft systems.",
                                    "example": "AMM ATA Chapter 27 detailing the exact procedure and drawing for elevator push-pull rod rigging."
                                },
                                {
                                    "term": "Illustrated Parts Catalog (IPC)",
                                    "definition": "A standardized manual featuring 3D exploded-view diagrams of all aircraft systems, linking numbered visual components to certified part numbers and quantities.",
                                    "example": "IPC Chapter 32 showing the exploded assembly of a nosewheel steering actuator."
                                }
                            ]
                        }
                    }
                ],
                # Card 3: Why Visuals Matter in Aerospace Maintenance
                [
                    {
                        "type": "concept_explanation",
                        "title": "The Language of Airworthiness: Why Visuals Matter",
                        "content": {
                            "title": "Eliminating Ambiguity in High-Stakes Aerospace Systems",
                            "text": "In commercial aviation, modern aircraft contain millions of precision parts, kilometers of electrical wiring, and high-pressure hydraulic lines. Technicians and aerospace engineers across the globe must communicate with zero ambiguity.\n\n- **The Language Barrier**: If an engineer in Seattle tells a maintenance technician in Nairobi that a wing bracket is 'the curved metal piece near the hydraulic line that feels loose,' that description is completely useless and dangerous.\n- **Universal Standardization**: Technical drawings solve this problem through standardized lines, symbols, projections, and numerical notations recognized by civil aviation authorities worldwide (such as ICAO, KCAA, FAA, and EASA).\n- **Regulatory Integrity**: Every repair, modification, and inspection must strictly conform to certified drawings. Guesswork is completely prohibited in aviation maintenance."
                        }
                    }
                ],
                # Card 4: Technical Diagram Block
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Illustrated Parts Catalog (IPC) Exploded Wheel Hub Assembly",
                        "content": {
                            "title": "Illustrated Parts Catalog (IPC) Exploded Wheel Hub Assembly",
                            "caption": "Standardized 3D exploded-view diagram showing how aircraft wheel components align sequentially along a central axis, with numbered callouts linked to the certified parts data table."
                        }
                    }
                ],
                # Card 5: Freehand Sketch vs. Technical Drawing Comparison Table
                [
                    {
                        "type": "comparison_table",
                        "title": "Comparative Analysis: Freehand Sketch vs. Engineering Technical Drawing",
                        "content": {
                            "title": "Sketching vs. Engineering Drawing Matrix",
                            "headers": ["Attribute", "Freehand Sketch", "Technical Drawing (Blueprint)"],
                            "rows": [
                                ["Creation Method", "Drawn quickly without drafting instruments or CAD tools", "Constructed with precision drafting instruments, CAD systems, and exact geometry"],
                                ["Scale & Precision", "Roughly proportional or unscaled; lacks precision tolerances", "Drawn to strict mathematical scale with defined millimetric tolerances (e.g. ±0.05 mm)"],
                                ["Regulatory Status", "Informal study; completely unauthorized for manufacturing or repair", "Legally certified document carrying airworthiness authority and engineering sign-offs"],
                                ["Information Depth", "Basic outline or concept idea", "Comprehensive: material specifications, heat treatments, finishes, torque values, and revisions"],
                                ["Aviation Application", "Initial brainstorming or quick field damage location notation", "Aircraft fabrication, structural repair manuals (SRM), and formal return-to-service releases"]
                            ]
                        }
                    }
                ],
                # Card 6: Real-World Aviation Case Study
                [
                    {
                        "type": "real_world_example",
                        "title": "Structural Repair at Wilson Airport: Cessna 208 Caravan",
                        "content": {
                            "title": "Precision Blueprint Compliance on Kenya's Safari Fleets",
                            "text": "At Wilson Airport in Nairobi, a maintenance team receives a Cessna 208 Caravan that experienced skin damage from a bird strike on an unpaved bush airstrip in Samburu.\n\n- **Consulting the SRM**: The technician does not invent a patch. They retrieve the official Cessna Structural Repair Manual (SRM).\n- **Reading the Engineering Drawing**: The technical drawing specifies the exact dimensions for the 2024-T3 aluminum doubler plate, the required 2.5D rivet edge margin, and the precise rivet pitch (spacing between rivets).\n- **Consequences of Non-Compliance**: If a technician estimated the rivet spacing freehand, aerodynamic drag and airframe flexing would concentrate stress along the patch seam, causing skin tear and catastrophic in-flight decompression."
                        }
                    }
                ],
                # Card 7: Educational Video Integration
                [
                    {
                        "type": "suggested_video",
                        "title": "Translating 2D Orthographic Projections into 3D Isometric Views",
                        "content": {
                            "title": "Translating 2D Orthographic Projections into 3D Isometric Views",
                            "description": "Visual demonstration of how three-dimensional isometric engineering drawings are constructed and correlated with flat 2D orthographic plans (Top, Front, Side views).",
                            "url": "https://www.youtube.com/watch?v=h_u0BHKJ0yk"
                        }
                    }
                ],
                # Card 8: Safety Connection & Procedural Boundaries
                [
                    {
                        "type": "concept_explanation",
                        "title": "Airworthiness Hazards: The Danger of Guesswork in Maintenance",
                        "content": {
                            "title": "Scenario: Machining Bushings Without Certified Blueprints",
                            "text": "Consider a maintenance workshop where a technician needs to replace a worn brass bushing in an elevator control linkage. The technician sketches the bushing on scratch paper, measures the worn part with a wooden ruler, and machines a new piece on a shop lathe.\n\n- **The Latent Hazard**: The worn part had already lost 0.15 mm of material. By copying a worn component without consulting the manufacturer's blueprint, the new bushing is machined undersized.\n- **The In-Flight Risk**: Under flight vibrations and aerodynamic elevator loads, the loose bushing vibrates excessively, causing rapid hinge flutter. This can lead to structural detachment of the elevator and complete loss of pitch control.\n- **Mandatory Safe Practice**: Never manufacture, modify, or install aircraft parts based on informal sketches or physical part copying. Always obtain the certified engineering drawing from the manufacturer's technical records."
                        }
                    }
                ],
                # Card 9: Formative Knowledge Check 1
                [
                    {
                        "type": "knowledge_check",
                        "title": "Formative Check: Freehand Sketch vs. Technical Drawing",
                        "content": {
                            "question": "What is the primary difference between an informal freehand sketch and a certified technical drawing in aircraft maintenance?",
                            "options": [
                                "Freehand sketches are drawn in red pencil, whereas technical drawings must always use green drafting ink.",
                                "Freehand sketches are unscaled initial visual concepts, whereas technical drawings are mathematically precise, scale-accurate legal documents carrying regulatory airworthiness authority.",
                                "Freehand sketches can only be read by computers, while technical drawings are read only by pilots.",
                                "Freehand sketches are used exclusively to overhaul jet engines, while technical drawings are reserved for cabin carpet layouts."
                            ],
                            "answer": "B",
                            "explanation": "In aviation, every component must meet rigorous dimensional tolerances and material standards. A freehand sketch lacks mathematical scale, certified tolerances, and engineering approval stamps, so it cannot be legally used to manufacture or clear aircraft parts for flight."
                        }
                    }
                ],
                # Card 10: Formative Knowledge Check 2 & Lesson Summary
                [
                    {
                        "type": "knowledge_check",
                        "title": "Formative Check: Purpose of the Illustrated Parts Catalog (IPC)",
                        "content": {
                            "question": "When an aircraft maintenance technician needs to identify the exact certified Part Number and assembly order for a landing gear hydraulic seal, which document must they consult?",
                            "options": [
                                "The Pilot's Operating Handbook (POH).",
                                "The Illustrated Parts Catalog (IPC).",
                                "The Air Traffic Control Radar Operating Manual.",
                                "The Airport Runway Surface Friction Index."
                            ],
                            "answer": "B",
                            "explanation": "The Illustrated Parts Catalog (IPC) is specifically designed to provide 3D exploded-view diagrams of every aircraft system, linking each numbered physical component directly to its official manufacturer Part Number, nomenclature, and required quantity."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Lesson Summary: Purpose of Aircraft-Related Drawings",
                        "content": {
                            "title": "Key Takeaways: Aircraft Technical Drawings",
                            "text": "- **Universal Precision**: Technical drawings are the unambiguous, scale-accurate graphical language that ensures global airworthiness.\n- **AMM vs. IPC**: The Aircraft Maintenance Manual (AMM) details procedural steps, torque specifications, and tolerances, while the Illustrated Parts Catalog (IPC) provides exploded 3D visual assemblies and exact part numbers.\n- **Zero Tolerance for Guesswork**: Fabricating or repairing aircraft components from freehand sketches or worn samples is strictly prohibited under civil aviation regulations."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 2: Isometric Principles and Instruments
        # =====================================================================
        {
            "unit_order": 1,
            "unit_name": "Isometric Principles and Instruments",
            "unit_description": "Master the mathematical foundation of isometric projection, including the three 120-degree axes, the 30-degree rule, and the proper utilization of drafting instruments such as T-squares and set squares.",
            "lesson_title": "Isometric Principles and Instruments",
            "pages": [
                # Card 1: Visual Hook & Learning Focus
                [
                    {
                        "type": "suggested_image",
                        "title": "Engineering Drafting Instruments and Set Squares",
                        "content": {
                            "title": "Engineering Drafting Instruments and Set Squares",
                            "caption": "Precision drafting set squares and millimeter scales used to construct exact 30-degree isometric axes and verify geometric angles in aerospace engineering layouts.",
                            "resolved_image_url": "https://upload.wikimedia.org/wikipedia/commons/5/55/GeoDreieck-Ingen-Proj-Mark.jpg"
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Learning Focus: Isometric Principles and Tools",
                        "content": {
                            "title": "Learning Focus: Isometric Principles and Tools",
                            "goals": [
                                "Explain the geometric structure of the three isometric axes and the fundamental 30-degree rule.",
                                "Understand why isometric drawings maintain true, measurable proportions without vanishing point distortion.",
                                "Identify and correctly position standard drafting instruments: T-squares, 30/60-degree set squares, and isometric grids.",
                                "Differentiate between isometric lines (measurable) and non-isometric lines (plotted endpoints)."
                            ]
                        }
                    }
                ],
                # Card 2: Foundational Terminology
                [
                    {
                        "type": "definition_card",
                        "title": "Core Isometric Geometry Terminology",
                        "content": {
                            "title": "Core Technical Vocabulary",
                            "definitions": [
                                {
                                    "term": "Isometric Axis",
                                    "definition": "One of three coordinate axes (one vertical at 90°, and two receding at 30° left and right from the horizontal) that form the structural framework of an isometric drawing.",
                                    "example": "The central vertex where height, length, and width origin lines meet at 120-degree angles."
                                },
                                {
                                    "term": "30/60-Degree Set Square",
                                    "definition": "A triangular drawing instrument containing one 90° right angle, one 30° angle, and one 60° angle, used in conjunction with a T-square to draft isometric receding lines.",
                                    "example": "Sliding the 30° edge along the T-square blade to draw the receding base of a bracket."
                                },
                                {
                                    "term": "Isometric Line",
                                    "definition": "Any line on a drawing that runs parallel to one of the three principal isometric axes; these lines can be measured directly with a scale ruler.",
                                    "example": "The vertical front corner or 30-degree top edge of a rectangular mounting block."
                                },
                                {
                                    "term": "Non-Isometric Line",
                                    "definition": "Any edge on an object that is inclined and does not run parallel to any of the three isometric axes; cannot be measured directly with a ruler.",
                                    "example": "The sloping chamfer of an aerodynamic wedge or fairing."
                                },
                                {
                                    "term": "Horizontal Baseline",
                                    "definition": "A true horizontal reference line drawn lightly with a T-square from which the 30-degree angles of the receding isometric axes are measured.",
                                    "example": "The bottom construction line guiding the layout of a drafting sheet."
                                }
                            ]
                        }
                    }
                ],
                # Card 3: The Three Axes and the 30-Degree Rule
                [
                    {
                        "type": "concept_explanation",
                        "title": "The Geometry of Isometric Projection: The 30-Degree Rule",
                        "content": {
                            "title": "Building the Three-Dimensional Framework",
                            "text": "The word **isometric** comes from Greek roots meaning 'equal measure' (*iso* = equal, *metric* = measure).\n\n- **The Three Axes**: Every isometric drawing is structured around three primary axes meeting at a single central point (vertex), forming an inverted letter **Y**:\n  - **Vertical Axis**: Represents **height**, drawn at 90 degrees to the horizontal baseline.\n  - **Right Receding Axis**: Represents **length**, sloping upward to the right at exactly **30 degrees** from the horizontal baseline.\n  - **Left Receding Axis**: Represents **width**, sloping upward to the left at exactly **30 degrees** from the horizontal baseline.\n- **Angular Separation**: The angle between any two adjacent axes is exactly **120 degrees** (360° / 3 = 120°).\n- **Why 30 Degrees?**: In artistic perspective drawings, parallel lines converge toward a distant vanishing point, which causes objects to shrink and prevents direct measurements. In isometric drawing, **parallel lines remain strictly parallel**, preserving measurable proportions everywhere on the page."
                        }
                    }
                ],
                # Card 4: Technical Diagram Block
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Drafting Setup for Isometric Axes and 30-Degree Alignment",
                        "content": {
                            "title": "Drafting Setup for Isometric Axes and 30-Degree Alignment",
                            "caption": "Precision drafting layout illustrating the alignment of the horizontal T-square, 30/60-degree set square positions, and the resulting 120-degree isometric axis geometry."
                        }
                    }
                ],
                # Card 5: Graphical Projection Methods Comparison Table
                [
                    {
                        "type": "comparison_table",
                        "title": "Comparative Analysis: Technical Graphical Projection Types",
                        "content": {
                            "title": "Projection Methods Comparison",
                            "headers": ["Projection Type", "Axis Orientation", "Parallel Lines", "Direct Scale Measurability"],
                            "rows": [
                                ["Isometric", "Vertical at 90°; receding edges at 30° left and right (120° apart)", "Strictly parallel; no vanishing points", "Directly measurable along all three principal axes"],
                                ["Oblique (Cavalier/Cabinet)", "Front face is flat (0°/90°); depth recedes at 45°", "Parallel along receding depth lines", "Measurable on front face; depth is either true scale or halved"],
                                ["Perspective (1, 2, or 3 Point)", "Converges toward horizon vanishing points", "Converge; parallel lines meet at horizon", "Not measurable with a ruler; dimensions shrink with distance"],
                                ["Orthographic (Multi-view)", "Separated 2D planes (Top, Front, Side at 90°)", "Parallel within each discrete 2D projection", "100% scale accurate; true shape and true dimensions displayed"]
                            ]
                        }
                    }
                ],
                # Card 6: Real-World Drafting Application
                [
                    {
                        "type": "real_world_example",
                        "title": "Avionics Hangar Fabrication: Custom Radio Mounting Trays",
                        "content": {
                            "title": "Field Drafting with Isometric Grid Paper",
                            "text": "When avionics technicians at an aviation maintenance facility in Nairobi need to fabricate a customized mounting bracket for a newly installed ADS-B transponder, they work directly on **isometric grid paper**.\n\n- **Isometric Pre-Printed Lines**: The grid paper has lines pre-printed at 30-degree angles and vertical intervals of 5 mm.\n- **Direct Proportions**: The technician sketches the sheet-metal bracket's flanges, mounting holes, and stiffener ribs. Because each grid triangle corresponds to true 5 mm increments, the technician can transfer dimensions directly to a sheet-metal shearing and bending brake without performing complex trigonometric calculations."
                        }
                    }
                ],
                # Card 7: Educational Video Integration
                [
                    {
                        "type": "suggested_video",
                        "title": "The Evolution of Standardized Aviation Drafting and Manufacturing",
                        "content": {
                            "title": "The Evolution of Standardized Aviation Drafting and Manufacturing",
                            "description": "Historical perspective on how early aviation pioneers transitioned from guesswork sketches to standardized engineering drawings, enabling team manufacturing and airworthiness.",
                            "url": "https://www.youtube.com/watch?v=NpqU3eSeS1c"
                        }
                    }
                ],
                # Card 8: Drafting Instrument Errors & Safety Consequences
                [
                    {
                        "type": "concept_explanation",
                        "title": "Drafting Precision Hazards: The Cost of Angular Distortion",
                        "content": {
                            "title": "Scenario: Estimating Receding Angles Without Set Squares",
                            "text": "Imagine a drafter who misplaces their 30/60-degree set square and attempts to draw an isometric bracket by estimating angles freehand, drawing the left axis at 20 degrees and the right axis at 45 degrees.\n\n- **Geometric Distortion**: The axes are non-standard and non-isometric. Parallel planes warp, and geometric symmetry is lost.\n- **Fabrication Hazard**: When the sketch is sent to a machinist to drill mounting holes, the distorted visual representation leads the machinist to misread hole centerlines.\n- **Airworthiness Failure**: Once installed on the aircraft engine bulkhead, the misaligned bracket places uneven shear stress on mounting fasteners, causing fatigue cracking during high-RPM engine operation.\n- **Standard Rule**: Always lock drafting instruments against the T-square or use verified isometric grid paper to guarantee exact 30-degree angles."
                        }
                    }
                ],
                # Card 9: Formative Knowledge Check 1
                [
                    {
                        "type": "knowledge_check",
                        "title": "Formative Check: The 30-Degree Isometric Rule",
                        "content": {
                            "question": "At what angle must the left and right receding axes be drawn relative to the horizontal baseline to construct a standard isometric drawing?",
                            "options": [
                                "45 degrees to the horizontal baseline.",
                                "90 degrees to the horizontal baseline.",
                                "30 degrees to the horizontal baseline.",
                                "60 degrees to the horizontal baseline."
                            ],
                            "answer": "C",
                            "explanation": "In standard isometric projection, both the length and width receding axes are constructed at exactly 30 degrees to the horizontal baseline, creating an equal 120-degree separation between all three axes."
                        }
                    }
                ],
                # Card 10: Formative Knowledge Check 2 & Lesson Summary
                [
                    {
                        "type": "knowledge_check",
                        "title": "Formative Check: True Proportions in Isometric Drawing",
                        "content": {
                            "question": "Why are parallel edges of an aircraft bracket drawn as parallel lines in isometric drawing rather than converging toward a vanishing point?",
                            "options": [
                                "Parallel lines prevent the drawing paper from tearing under pencil pressure.",
                                "Parallel lines maintain consistent, true scale proportions across the entire drawing, allowing technicians to take direct measurements with a scale ruler.",
                                "Parallel lines are required by law so that drawings cannot be photocopied.",
                                "Vanishing points are only used for supersonic military fighter aircraft."
                            ],
                            "answer": "B",
                            "explanation": "Unlike perspective drawings where distant lines shrink toward a vanishing point, isometric drawings keep parallel lines strictly parallel. This preserves true scale proportions along all isometric axes, enabling technicians to verify physical dimensions directly with a ruler."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Lesson Summary: Isometric Principles and Instruments",
                        "content": {
                            "title": "Key Takeaways: Isometric Principles",
                            "text": "- **Tri-Axial Geometry**: Built on three axes meeting at 120 degrees: one vertical (height) and two receding at 30 degrees (length and width).\n- **Scale Measurability**: Measurements can be taken directly along all isometric lines using a scale ruler.\n- **Precision Instruments**: A T-square combined with a 30/60-degree set square ensures perfect 30-degree receding angles, preventing visual and dimensional distortion."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 3: Drawing Aircraft-Related Forms: The Crating Method
        # =====================================================================
        {
            "unit_order": 2,
            "unit_name": "Drawing Aircraft-Related Forms: The Crating Method",
            "unit_description": "Apply the step-by-step crating method to construct complex 3D aircraft components, including stepped L-blocks, inclined aerodynamic wedges, and foreshortened isometric circles (ellipses).",
            "lesson_title": "Drawing Aircraft-Related Forms: The Crating Method",
            "pages": [
                # Card 1: Visual Hook & Learning Focus
                [
                    {
                        "type": "suggested_image",
                        "title": "Axonometric and Isometric Projections of Stepped Blocks",
                        "content": {
                            "title": "Axonometric and Isometric Projections of Stepped Blocks",
                            "caption": "Step-by-step geometric projection of structured blocks and prisms, demonstrating how enclosing bounding boxes enable accurate construction of complex 3D forms.",
                            "resolved_image_url": "https://upload.wikimedia.org/wikipedia/commons/4/4c/Axonometric_projections.png"
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Learning Focus: The Crating Method",
                        "content": {
                            "title": "Learning Focus: The Crating Method",
                            "goals": [
                                "Master the three-stage crating method for constructing complex geometric shapes in isometric projection.",
                                "Construct stepped forms (such as L-shaped aircraft brackets) using bounding box construction lines.",
                                "Plot non-isometric lines for inclined aerodynamic wedges and chamfers.",
                                "Construct isometric circles (ellipses) inside isometric square boxes using the four-centered oval technique."
                            ]
                        }
                    }
                ],
                # Card 2: Foundational Terminology
                [
                    {
                        "type": "definition_card",
                        "title": "Core Crating and Form Construction Terminology",
                        "content": {
                            "title": "Core Technical Vocabulary",
                            "definitions": [
                                {
                                    "term": "Crating Method",
                                    "definition": "A drafting technique where a complex or curved 3D object is constructed by first lightly drawing an enclosing rectangular box ('crate') of maximum overall dimensions, and then carving away unwanted volume.",
                                    "example": "Drawing an 80 × 50 × 40 mm box before shaping an L-bracket inside it."
                                },
                                {
                                    "term": "Construction Line",
                                    "definition": "A very light, thin pencil line (drawn with 2H or 4H pencil) used to lay out geometry; these lines guide the final drawing and are erased or faded out.",
                                    "example": "The light dashed outer bounding crate lines framing a mounting flange."
                                },
                                {
                                    "term": "Object (Outline) Line",
                                    "definition": "A thick, dark, solid line (drawn with HB pencil) representing the final visible edges and boundaries of the physical component.",
                                    "example": "The dark solid profile defining the finished edges of an aircraft bracket."
                                },
                                {
                                    "term": "Isometric Ellipse",
                                    "definition": "The geometrical representation of a true circle projected onto a 30-degree isometric plane, appearing as a smooth, symmetrical, squashed oval.",
                                    "example": "The circular inspection hole on an aircraft wing access panel drawn in 3D."
                                },
                                {
                                    "term": "Four-Center Approximation Method",
                                    "definition": "A geometric drafting technique used to draw an isometric ellipse inside an isometric square using four compass arcs struck from obtuse and acute corner centers.",
                                    "example": "Constructing an isometric circle on the top face of a fuel tank boss."
                                }
                            ]
                        }
                    }
                ],
                # Card 3: The Three-Stage Crating Method
                [
                    {
                        "type": "concept_explanation",
                        "title": "The Crating Principle: Systematic 3D Construction",
                        "content": {
                            "title": "From Bounding Box to Finished Aerospace Part",
                            "text": "Attempting to draw a complex shaped part (like an angled wing fitting or stepped bracket) freehand in 3D almost always results in skewed angles and distorted proportions. The **Crating Method** guarantees mathematical accuracy in three disciplined stages:\n\n- **Stage 1: The Bounding Crate (Outer Box)**: Determine the object's maximum dimensions: Total Length, Total Width, and Total Height. Using light construction lines, draft an isometric rectangular box of these exact dimensions. This box sets the absolute spatial boundary: nothing on the component can extend outside this crate.\n- **Stage 2: Plotting Internal Features**: Measure along the crate's edges to locate cutouts, steps, slopes, or holes. Project these lines parallel to the 30-degree isometric axes across the faces of the box.\n- **Stage 3: Darkening Object Outlines**: Trace over the final, visible edges with heavy, dark object lines. Unused construction lines are erased or left as faint background references."
                        }
                    }
                ],
                # Card 4: Technical Diagram Block
                [
                    {
                        "type": "suggested_diagram",
                        "title": "The Three-Stage Crating Method: L-Bracket Construction",
                        "content": {
                            "title": "The Three-Stage Crating Method: L-Bracket Construction",
                            "caption": "Step-by-step visual progression showing the initial light bounding crate (Stage 1), plotting step cutouts and projections (Stage 2), and darkening the final finished bracket outline (Stage 3)."
                        }
                    }
                ],
                # Card 5: Drawing Isometric Curves and Ellipses Table
                [
                    {
                        "type": "comparison_table",
                        "title": "Comparative Analysis: Circles in 2D Orthographic vs. 3D Isometric",
                        "content": {
                            "title": "Circular Features Geometry Comparison",
                            "headers": ["Feature", "2D Orthographic View", "3D Isometric View"],
                            "rows": [
                                ["Visual Appearance", "True, un-distorted circle (constant radius 360°)", "Symmetrical squashed oval (foreshortened ellipse)"],
                                ["Drafting Instrument", "Standard drafting compass set to nominal radius", "Isometric ellipse template or four-center compass construction"],
                                ["Bounding Guide", "Square with sides perpendicular (90°) to each other", "Isometric rhombus (slanted square) with 60° and 120° corner angles"],
                                ["Measurability", "Diameter can be measured directly across any angle", "Nominal diameter is verified only along major/minor axes or midpoints of bounding rhombus"],
                                ["Common Aerospace Application", "Drill template for rivet or bolt holes on flat sheet", "Exploded-view IPC drawings of wheel bearings, hydraulic cylinders, and fuel ports"]
                            ]
                        }
                    }
                ],
                # Card 6: Real-World Aviation Application
                [
                    {
                        "type": "real_world_example",
                        "title": "Airframe Modification: Engine Cowling Fuel Drain Cutout",
                        "content": {
                            "title": "Fabricating Angled Cowl Penetrations",
                            "text": "When aircraft maintenance engineers modify an engine cowling to accommodate a relocated fuel strainer drain line, they must draft a shop sketch showing the angled circular opening.\n\n- **The Common Mistake**: An inexperienced drafter might draw a perfect circle on the slanted 3D cowling sketch with a standard compass. The sketch appears visually warped and fails to show how the circular fuel line aligns with the curved skin.\n- **Applying Crating**: The technician drafts an isometric square on the cowling surface matching the pipe's outer diameter, locates the midpoints, and constructs a precise isometric ellipse. The resulting shop drawing accurately portrays clearance between the pipe and cowling edge, preventing chafing during engine vibration."
                        }
                    }
                ],
                # Card 7: Educational Video Integration
                [
                    {
                        "type": "suggested_video",
                        "title": "Step-by-Step Isometric Sketching Using the Crating Method",
                        "content": {
                            "title": "Step-by-Step Isometric Sketching Using the Crating Method",
                            "description": "Practical drafting tutorial demonstrating how to lay out an initial light bounding box, carve internal features, and produce professional isometric sketches with proper line weighting.",
                            "url": "https://www.youtube.com/watch?v=x9L9Vfj0UFE"
                        }
                    }
                ],
                # Card 8: Drafting Procedural Pitfalls & Safety Connection
                [
                    {
                        "type": "concept_explanation",
                        "title": "Drafting Integrity: The Peril of Freehand Curve Guessing",
                        "content": {
                            "title": "Scenario: Non-Isometric Lines and Sloping Wing Ribs",
                            "text": "An aircraft structural drafter is tasked with drawing an inclined rib flange that tapers from 50 mm at the front spar to 20 mm at the rear spar.\n\n- **The Drafting Hazard**: The drafter attempts to measure the sloping edge directly with a scale ruler along the taper angle, treating it as an isometric line.\n- **The Geometric Reality**: Inclined edges are **non-isometric lines**. Because they do not run parallel to the 30-degree axes, they are foreshortened and cannot be measured with a ruler.\n- **The Proper Technique**: The drafter must crate the rib, measure the 50 mm height on the front vertical axis, measure the 20 mm height on the rear vertical axis, and connect the two plotted points with a straightedge.\n- **Safety Impact**: If a technician cuts raw aluminum based on a direct ruler reading of a non-isometric line, the rib flange will be cut too short, compromising wing torsional stiffness."
                        }
                    }
                ],
                # Card 9: Formative Knowledge Check 1
                [
                    {
                        "type": "knowledge_check",
                        "title": "Formative Check: Purpose of the Bounding Crate",
                        "content": {
                            "question": "Why is a light bounding box (crate) drawn first when using the crating method to sketch a complex aircraft bracket?",
                            "options": [
                                "To ensure that the drawing paper does not get soaked by drafting ink.",
                                "To establish the maximum height, length, and width boundaries, ensuring all internal features, steps, and curves remain in true proportion.",
                                "To create a decorative frame that will be displayed in the aircraft passenger cabin.",
                                "The bounding box represents the shipping container used by cargo freighters."
                            ],
                            "answer": "B",
                            "explanation": "The crating method relies on constructing an initial light bounding box of maximum dimensions. This box establishes the exact outer spatial limits of the object, allowing internal steps, cutouts, and curves to be plotted accurately and in true proportion."
                        }
                    }
                ],
                # Card 10: Formative Knowledge Check 2 & Lesson Summary
                [
                    {
                        "type": "knowledge_check",
                        "title": "Formative Check: Circles in Isometric Projection",
                        "content": {
                            "question": "How does a circular inspection hole appear when drawn on an isometric surface?",
                            "options": [
                                "As a perfect circle that can be drawn with a standard compass set to the nominal radius.",
                                "As a horizontal straight line with sharp arrowheads.",
                                "As a foreshortened, symmetrical oval known as an isometric ellipse.",
                                "As a solid three-dimensional pyramid."
                            ],
                            "answer": "C",
                            "explanation": "Because isometric planes are inclined at 30 degrees to the viewer, all circular features undergo visual foreshortening along one axis, appearing as a symmetrical ellipse. It must be constructed within an isometric square rather than drawn as a true circle."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Lesson Summary: Drawing Aircraft-Related Forms (The Crating Method)",
                        "content": {
                            "title": "Key Takeaways: The Crating Method",
                            "text": "- **Three-Stage Progression**: 1. Bounding box (outer limits) -> 2. Plot internal cutouts and slopes -> 3. Darken visible object outlines.\n- **Non-Isometric Lines**: Sloping or inclined edges cannot be measured directly; their endpoints must be plotted along isometric axes and joined.\n- **Ellipses in 3D**: Circular holes appear as isometric ellipses and are constructed inside 30-degree isometric square guides."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 4: Dimensioning and Technical Notes
        # =====================================================================
        {
            "unit_order": 3,
            "unit_name": "Dimensioning and Technical Notes",
            "unit_description": "Master the rigorous rules of technical dimensioning in aviation drawings, including extension lines, dimension lines, tolerance limits, units, material specifications, and title blocks.",
            "lesson_title": "Dimensioning and Technical Notes",
            "pages": [
                # Card 1: Visual Hook & Learning Focus
                [
                    {
                        "type": "suggested_image",
                        "title": "Standardized Engineering Drawing with Dimensions and Notes",
                        "content": {
                            "title": "Standardized Engineering Drawing with Dimensions and Notes",
                            "caption": "Precision technical engineering blueprint demonstrating standardized extension lines, arrowheads, tolerance specifications, and title block notations.",
                            "resolved_image_url": "https://upload.wikimedia.org/wikipedia/commons/0/03/DIN_69893_hsk_63a_drawing.png"
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Learning Focus: Dimensioning and Technical Notes",
                        "content": {
                            "title": "Learning Focus: Dimensioning and Technical Notes",
                            "goals": [
                                "Identify the anatomy of a dimension: extension lines, dimension lines, arrowheads, and numerical values.",
                                "Apply the strict rules of isometric dimensioning: parallel alignment, line gaps, and non-overlapping layouts.",
                                "Interpret engineering tolerances (e.g. ±0.05 mm) and understand their vital role in airworthiness and interchangeability.",
                                "Read and extract critical data from the drawing Title Block and Technical Notes column."
                            ]
                        }
                    }
                ],
                # Card 2: Foundational Terminology
                [
                    {
                        "type": "definition_card",
                        "title": "Core Dimensioning and Notation Terminology",
                        "content": {
                            "title": "Core Technical Vocabulary",
                            "definitions": [
                                {
                                    "term": "Dimensioning",
                                    "definition": "The practice of adding precise numerical measurements, units, symbols, and notes to a technical drawing to define the physical geometry, thickness, and location of features.",
                                    "example": "Annotating a bracket with a 60 mm length and 12 mm hole diameter."
                                },
                                {
                                    "term": "Extension Line",
                                    "definition": "A thin, solid line projected outward from an object's boundary to establish the start and end limits of a dimension line, starting with a visible gap from the object.",
                                    "example": "A line extending 15 mm outward from the edge of a flange, leaving a 1.5 mm gap at the corner."
                                },
                                {
                                    "term": "Dimension Line",
                                    "definition": "A thin line terminating in sharp, closed arrowheads, drawn parallel to the edge being measured and spanning between extension lines.",
                                    "example": "The line carrying the centered number '45 mm' indicating bracket width."
                                },
                                {
                                    "term": "Tolerance",
                                    "definition": "The total allowable variation in a physical dimension from its nominal specification, defining the acceptable boundary for safe fit and operation.",
                                    "example": "A wing attachment pin specified as 25.00 mm with a tolerance of ±0.02 mm."
                                },
                                {
                                    "term": "Title Block",
                                    "definition": "A standardized bordered box at the bottom right corner of an engineering drawing containing drawing number, part name, scale, revision letter, material, and approval signatures.",
                                    "example": "The block stating 'PART NO: 204-011-002, REV: C, ALL DIMENSIONS IN MM'."
                                }
                            ]
                        }
                    }
                ],
                # Card 3: The Anatomy of a Dimension and Isometric Rules
                [
                    {
                        "type": "concept_explanation",
                        "title": "Anatomy of a Dimension: Standards of Precision Drafting",
                        "content": {
                            "title": "Clean, Unambiguous Measurement Architecture",
                            "text": "A technical drawing without dimensions is merely an artistic picture. To convert a drawing into a legal manufacturing blueprint, dimensions must follow strict standards:\n\n- **The 1.5 mm Gap Rule**: Extension lines must never touch the physical outline of the part. A clear gap of approximately 1.5 mm must be left between the object corner and the extension line so the reader does not confuse measurement guides with part boundaries.\n- **Arrowhead Standards**: Arrowheads must be thin, sharp, closed, and blackened (approximately 3 mm long by 1 mm wide, maintaining a 3:1 aspect ratio).\n- **Aligned Dimension Placement**: Numbers are placed in the center of the dimension line, slightly hovering above it. In isometric drawing, dimensions must run parallel to the 30-degree isometric axes—never drawn flat horizontal across a 3D view.\n- **Hierarchy of Dimensions**: Smaller detailed dimensions are placed closest to the object (minimum 10 mm away), while overall dimensions are placed farther out to prevent crossing lines."
                        }
                    }
                ],
                # Card 4: Technical Diagram Block
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Standardized Isometric Dimensioning and Annotation Blueprint",
                        "content": {
                            "title": "Standardized Isometric Dimensioning and Annotation Blueprint",
                            "caption": "Precision engineering layout illustrating proper extension line offsets, parallel 30-degree dimension line alignment, title block information, and common drafting errors to avoid."
                        }
                    }
                ],
                # Card 5: Dimensioning Systems and Standards Comparison Table
                [
                    {
                        "type": "comparison_table",
                        "title": "Comparative Analysis: Aligned vs. Unidirectional Dimensioning",
                        "content": {
                            "title": "Dimensioning Systems Matrix",
                            "headers": ["System", "Number Orientation", "Reading Direction", "Primary Application"],
                            "rows": [
                                ["Aligned System", "Numbers run parallel to dimension lines (inclined along 30° axes)", "Read from the bottom or right side of the drafting sheet", "Standard practice in isometric drawings, mechanical drafting, and aerospace blueprints"],
                                ["Unidirectional System", "Numbers are always oriented horizontally regardless of line angle", "Read exclusively from the bottom of the page", "Common in architectural plans, large civil engineering layouts, and computer-aided drafting (CAD)"],
                                ["Chain Dimensioning", "Dimensions placed end-to-end in a continuous line", "Read sequentially along a single datum line", "Used for hole patterns; beware of tolerance buildup errors"],
                                ["Datum (Baseline) Dimensioning", "All dimensions originate from a single common baseline edge", "Read independently from datum plane zero", "Standard in aerospace machining to eliminate tolerance accumulation"]
                            ]
                        }
                    }
                ],
                # Card 6: Real-World Unit Mismatch Case Study
                [
                    {
                        "type": "real_world_example",
                        "title": "Unit Confusion in Aerospace: The Mars Climate Orbiter Loss",
                        "content": {
                            "title": "Why 'ALL DIMENSIONS IN MM' Is a Critical Safety Rule",
                            "text": "In 1999, NASA lost the $327 million Mars Climate Orbiter because one engineering software team used Imperial units (pound-seconds) while another team assumed metric units (Newton-seconds).\n\n- **Aviation Implication**: In aircraft maintenance, mixing up millimeters and inches can cause catastrophic structural failure. A 10 mm bolt hole is approximately 0.39 inches; if an engineer mistakes it for a 3/8-inch (9.525 mm) hole, the bolt will not fit or will be forced, damaging the internal threads.\n- **The Mandatory Title Block Check**: Aviation technicians are trained to check the drawing Title Block before picking up tools. If the title block states **'ALL DIMENSIONS IN MM UNLESS OTHERWISE SPECIFIED'**, no imperial conversion assumptions may be made."
                        }
                    }
                ],
                # Card 7: Educational Video Integration
                [
                    {
                        "type": "suggested_video",
                        "title": "Professional Technical Dimensioning and Drafting Standards",
                        "content": {
                            "title": "Professional Technical Dimensioning and Drafting Standards",
                            "description": "Comprehensive tutorial demonstrating the proper drafting sequence for dimensioning: laying out extension lines, pulling parallel dimension lines, and correctly placing numerical tolerances.",
                            "url": "https://www.youtube.com/watch?v=NSlz_PSm7wY"
                        }
                    }
                ],
                # Card 8: Tolerances, Fit, and Safety Connections
                [
                    {
                        "type": "concept_explanation",
                        "title": "Tolerance and Airworthiness: The Critical Window of Safety",
                        "content": {
                            "title": "Scenario: Replacing a Flap Linkage Pin Without Respecting Tolerances",
                            "text": "A technician is machining a replacement stainless steel pivot pin for a wing flap track. The drawing specifies a diameter of **20.00 mm with a tolerance of ±0.02 mm**.\n\n- **Understanding the Window**: The pin's diameter is legally acceptable only between **19.98 mm and 20.02 mm**.\n- **The Safety Hazard**: The technician machines the pin to 20.10 mm (0.08 mm oversize), believing that 'a tight fit is even better for safety.'\n- **The Failure Mode**: During flight in cold cruising altitudes (-50°C), thermal contraction causes the aluminum flap track housing to shrink faster than the steel pin. The oversize pin seizes solid inside the bushing. When the pilot attempts to deploy flaps on approach to landing, the flap motor shears its drive shaft, leaving the aircraft in an asymmetrical flap condition.\n- **Rule**: Tolerances are life-and-death parameters. Never alter or exceed specified dimensional limits."
                        }
                    }
                ],
                # Card 9: Formative Knowledge Check 1
                [
                    {
                        "type": "knowledge_check",
                        "title": "Formative Check: Extension Line Gap Rule",
                        "content": {
                            "question": "Why must a 1.5 mm gap be left between the physical edge of an aircraft part and the start of a dimension extension line?",
                            "options": [
                                "To reduce the amount of drafting pencil graphite consumed on the drawing sheet.",
                                "To prevent the extension lines from being visually confused with the actual physical outlines and boundaries of the part.",
                                "To allow thermal expansion of the paper when stored in hot maintenance hangars.",
                                "The gap is used to indicate where paint primer should not be sprayed."
                            ],
                            "answer": "B",
                            "explanation": "If extension lines touched the object's corners directly, the drawing would blend together into a confusing geometric web. The 1.5 mm gap provides a clear visual break, separating the physical component from its measurement guidelines."
                        }
                    }
                ],
                # Card 10: Formative Knowledge Check 2 & Lesson Summary
                [
                    {
                        "type": "knowledge_check",
                        "title": "Formative Check: Interpreting Engineering Tolerances",
                        "content": {
                            "question": "An aircraft structural blueprint indicates a critical bolt hole diameter of 12.00 mm with a specified tolerance of ±0.05 mm. Which of the following measured hole diameters is acceptable for airworthiness sign-off?",
                            "options": [
                                "11.90 mm",
                                "12.08 mm",
                                "12.03 mm",
                                "12.10 mm"
                            ],
                            "answer": "C",
                            "explanation": "A nominal dimension of 12.00 mm with a tolerance of ±0.05 mm defines an acceptable range between 11.95 mm (12.00 - 0.05) and 12.05 mm (12.00 + 0.05). Only 12.03 mm falls within this allowable airworthiness boundary."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Lesson Summary: Dimensioning and Technical Notes",
                        "content": {
                            "title": "Key Takeaways: Dimensioning Standards",
                            "text": "- **Dimension Anatomy**: Extension lines (with 1.5 mm gap), dimension lines (with sharp closed arrowheads), and centered hovering numbers.\n- **Isometric Alignment**: Dimension lines must run parallel to 30-degree isometric axes, never flat horizontal.\n- **Title Block Authority**: Governs the entire drawing: units (e.g. 'ALL DIMENSIONS IN MM'), material alloys (e.g. 2024-T3), and overall tolerances (e.g. ±0.1 mm)."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 5: Drawing Interpretation in Aircraft Work
        # =====================================================================
        {
            "unit_order": 4,
            "unit_name": "Drawing Interpretation in Aircraft Work",
            "unit_description": "Develop advanced drawing interpretation skills for maintenance operations, integrating Illustrated Parts Catalogs (IPC) with Aircraft Maintenance Manuals (AMM), resolving part discrepancies, and following ATA chapter indexing.",
            "lesson_title": "Drawing Interpretation in Aircraft Work",
            "pages": [
                # Card 1: Visual Hook & Learning Focus
                [
                    {
                        "type": "suggested_image",
                        "title": "Aircraft Structural Maintainers Interpreting Engineering Blueprints",
                        "content": {
                            "title": "Aircraft Structural Maintainers Interpreting Engineering Blueprints",
                            "caption": "Aviation maintenance technicians actively reviewing technical engineering drawings and blueprints in an aircraft hangar before conducting structural airframe repairs.",
                            "resolved_image_url": "https://upload.wikimedia.org/wikipedia/commons/4/49/Behind_the_Blueprint-_35th_MXG_Structural_Maintainers_at_Work_%289487278%29.jpg"
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Learning Focus: Drawing Interpretation in Maintenance",
                        "content": {
                            "title": "Learning Focus: Drawing Interpretation in Maintenance",
                            "goals": [
                                "Read and interpret 3D exploded-view drawings and cross-reference component callouts with parts catalog tables.",
                                "Trace the structural relationship between AMM task procedures and IPC assembly schematics.",
                                "Navigate the standard Air Transport Association (ATA) 100 chapter indexing system used across global aviation.",
                                "Follow mandatory safety procedures when resolving discrepancies between physical aircraft parts and technical drawings."
                            ]
                        }
                    }
                ],
                # Card 2: Foundational Terminology
                [
                    {
                        "type": "definition_card",
                        "title": "Core Technical Manual Interpretation Vocabulary",
                        "content": {
                            "title": "Core Technical Vocabulary",
                            "definitions": [
                                {
                                    "term": "Drawing Interpretation",
                                    "definition": "The professional ability to mentally translate 2D and 3D lines, symbols, dimensions, and notes on a technical drawing into a complete understanding of a physical aircraft system.",
                                    "example": "Reading an exploded fuel valve diagram to determine the exact seating direction of an internal O-ring seal."
                                },
                                {
                                    "term": "Cross-Referencing",
                                    "definition": "The procedural act of linking a numbered visual item callout on a schematic to its official Part Number, description, and quantity in an adjacent data table.",
                                    "example": "Tracing callout 'Item 14' on an IPC drawing to find 'PN 404-012 Seal, Fluorosilicone'."
                                },
                                {
                                    "term": "ATA Chapter System",
                                    "definition": "A standardized numerical indexing system created by the Air Transport Association to organize technical data across all commercial aircraft types uniformly.",
                                    "example": "ATA Chapter 27 always covers Flight Controls; ATA Chapter 32 always covers Landing Gear."
                                },
                                {
                                    "term": "Exploded-View Schematic",
                                    "definition": "A pictorial drawing showing a mechanical assembly separated into its individual components along common central axes, illustrating the exact sequence of assembly.",
                                    "example": "An exploded drawing of a turboprop propeller governor showing flyweights, springs, and valves."
                                },
                                {
                                    "term": "Engineering Order (EO)",
                                    "definition": "A legally binding engineering document detailing mandatory alterations, inspections, or part replacements, accompanied by certified updated technical drawings.",
                                    "example": "An EO instructing technicians to install reinforced wing strut attachment brackets."
                                }
                            ]
                        }
                    }
                ],
                # Card 3: Navigating the AMM and IPC Ecosystem
                [
                    {
                        "type": "concept_explanation",
                        "title": "The Technical Manual Trinity: How Technicians Work",
                        "content": {
                            "title": "Interlocking Maintenance Documentation",
                            "text": "When an aircraft technician troubleshoots a mechanical fault, they do not read a manual cover-to-cover; they navigate a synchronized system of engineering publications:\n\n- **Aircraft Maintenance Manual (AMM)**: Answers **HOW** to perform the work. Provides step-by-step procedural instructions, safety warnings, required support equipment, bolt torque values, and functional testing steps.\n- **Illustrated Parts Catalog (IPC)**: Answers **WHAT** and **WHERE**. Contains 3D isometric exploded-view drawings showing every single bolt, nut, washer, bracket, and seal, linked to certified part numbers.\n- **Structural Repair Manual (SRM)**: Answers **HOW TO RESTORE INTEGRITY**. Provides specialized drawings and allowable damage limits for sheet-metal and composite airframe structures.\n- **The ATA Chapter Index**: Because every manual uses the same ATA chapter numbers (e.g. Chapter 28 is always Fuel, Chapter 29 is always Hydraulics), a technician can cross-reference across manuals in seconds."
                        }
                    }
                ],
                # Card 4: Technical Diagram Block
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Technical Drawing Interpretation and Repair Workflow Flowchart",
                        "content": {
                            "title": "Technical Drawing Interpretation and Repair Workflow Flowchart",
                            "caption": "Six-step operational flowchart showing how a technician progresses from pilot defect report through AMM task procedures, IPC schematic cross-referencing, tolerance auditing, and return-to-service certification."
                        }
                    }
                ],
                # Card 5: Core ATA Chapters in Aircraft Maintenance Table
                [
                    {
                        "type": "comparison_table",
                        "title": "Comparative Reference: Key ATA 100 System Chapters",
                        "content": {
                            "title": "Standardized ATA Chapter Reference",
                            "headers": ["ATA Chapter", "System Title", "Typical Drawing Types Included", "Sample Maintenance Task"],
                            "rows": [
                                ["ATA 24", "Electrical Power", "Single-line electrical schematics, wire harness routing diagrams", "Replacing generator control units and auditing circuit breaker wiring"],
                                ["ATA 27", "Flight Controls", "Cable routing isometric drawings, bellcrank assemblies, rigging diagrams", "Rigging aileron pushrods and replacing flap actuator hinge bearings"],
                                ["ATA 28", "Fuel Systems", "Plumbing schematics, exploded fuel tank sender units, selector valve layouts", "Replacing high-pressure engine fuel boost pump filters and seals"],
                                ["ATA 29", "Hydraulic Power", "Hydraulic flow diagrams, reservoir and manifold exploded views", "Overhauling hydraulic landing gear retraction actuators and relief valves"],
                                ["ATA 32", "Landing Gear", "Exploded wheel hub assemblies, brake disc stacks, oleo strut schematics", "Inspecting nosewheel steering torque links and repacking wheel bearings"]
                            ]
                        }
                    }
                ],
                # Card 6: Real-World Maintenance Case Study
                [
                    {
                        "type": "real_world_example",
                        "title": "Digital Blueprint Navigation: Tablet Tech at Nairobi AMOs",
                        "content": {
                            "title": "Modern Digital Maintenance Operations",
                            "text": "At Wilson Airport and JKIA, modern Approved Maintenance Organizations (AMOs) have replaced paper binders with ruggedized digital tablets connected to cloud-based technical libraries.\n\n- **Dynamic Exploded Views**: When inspecting the propeller governor on a Cessna Caravan, the technician navigates to IPC ATA Chapter 61 (Propellers). On their tablet, they can zoom in on the 3D isometric drawing, rotate views, and tap on callout 'Item 8' to instantly reveal its manufacturer part number and current inventory availability.\n- **Real-Time Revision Verification**: Digital platforms ensure the technician is always viewing the latest revision letter of the blueprint, eliminating the risk of using obsolete paper drawings with outdated torque limits."
                        }
                    }
                ],
                # Card 7: Educational Video Integration
                [
                    {
                        "type": "suggested_video",
                        "title": "Aviation Chart and Airfield Diagram Real-Time Interpretation",
                        "content": {
                            "title": "Aviation Chart and Airfield Diagram Real-Time Interpretation",
                            "description": "Demonstration of spatial interpretation in aviation, showing how pilots and technicians translate 2D technical charts and airport diagrams into real-world 3D spatial awareness.",
                            "url": "https://www.youtube.com/watch?v=1A1zidPsNCA"
                        }
                    }
                ],
                # Card 8: Part Mismatches & Airworthiness Safety Boundaries
                [
                    {
                        "type": "concept_explanation",
                        "title": "Drawing Discrepancies: Protocol for Unapproved Part Mismatches",
                        "content": {
                            "title": "Scenario: The Missing Washer on a Fuel Line Support Bracket",
                            "text": "A technician removing an engine fuel line bracket finds that the old part was bolted directly against the crankcase without a washer. However, the official **IPC exploded-view drawing clearly indicates a cadmium-plated spacer washer (Item 5)** between the bracket and the engine casing.\n\n- **The Tempting Shortcut**: The technician thinks, 'The old bracket flew for 500 hours without a washer, so I can reinstall it the same way.'\n- **The Latent Disaster**: Without the washer, the fuel line sits 2 mm closer to the engine exhaust manifold heat shield. Over time, engine vibration causes the line to chafe against the shield, wearing through the aluminum tube and sparking an in-flight engine fire.\n- **Mandatory Discrepancy Protocol**:\n  1. The certified technical drawing and AMM instructions are always the final legal authority over previous physical installations.\n  2. When a physical installation contradicts the drawing, halt the procedure immediately.\n  3. Consult the aircraft's historical logbooks and Engineering Orders to verify if an authorized modification was performed.\n  4. Reinstall the assembly strictly in accordance with certified blueprint specifications."
                        }
                    }
                ],
                # Card 9: Formative Knowledge Check 1
                [
                    {
                        "type": "knowledge_check",
                        "title": "Formative Check: Exploded-View Drawings in the IPC",
                        "content": {
                            "question": "Why does the Illustrated Parts Catalog (IPC) use 3D exploded-view drawings rather than standard 2D photographs of completed aircraft assemblies?",
                            "options": [
                                "Photographs are completely illegal to publish in civil aviation manuals.",
                                "Exploded views separate components along common centerlines, revealing internal washers, seals, bearings, and the exact order of assembly that are hidden in assembled photographs.",
                                "Exploded-view drawings make the aircraft significantly lighter during transcontinental flights.",
                                "Exploded views are used exclusively to train airport baggage sorting personnel."
                            ],
                            "answer": "B",
                            "explanation": "A photograph of an assembled component only shows its outer shell. An exploded-view drawing pulls every internal component apart along a central axis, making the exact sequence of assembly, internal seals, bearings, and part callouts immediately visible to technicians."
                        }
                    }
                ],
                # Card 10: Formative Knowledge Check 2 & Lesson Summary
                [
                    {
                        "type": "knowledge_check",
                        "title": "Formative Check: Handling Drawing Discrepancies",
                        "content": {
                            "question": "If an aircraft technician discovers that a physical bracket installed on an engine does not match the engineering drawing in the manufacturer's manual, what is the mandatory safety action?",
                            "options": [
                                "Use a machine shop hammer to force the physical bracket to resemble the drawing shape.",
                                "Halt work immediately, quarantine the component, and consult the aircraft's historical logbooks and engineering registry to resolve the discrepancy before proceeding.",
                                "Throw away the manufacturer's manual and draw a new sketch based on the physical bracket.",
                                "Install the unmatched part anyway to avoid delaying scheduled commercial flights."
                            ],
                            "answer": "B",
                            "explanation": "Any mismatch between an installed part and the official technical drawing is a serious airworthiness discrepancy. It could signify an unapproved bogus part or an unrecorded modification. Work must stop immediately, the part must be quarantined, and certified engineering records must be consulted."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Lesson Summary: Drawing Interpretation in Aircraft Work",
                        "content": {
                            "title": "Key Takeaways: Drawing Interpretation",
                            "text": "- **Exploded Views & Cross-Referencing**: Exploded schematics show assembly order; item callouts connect to part number tables in the IPC.\n- **Manual Synergy**: AMM dictates procedure and torque, while IPC dictates parts identification and positioning.\n- **Strict Authority**: Certified technical drawings override previous installation states; any discrepancy requires immediate work stoppage and engineering investigation."
                        }
                    }
                ]
            ]
        }
    ]

def ingest_grade10_aviation_topic364(replace=False):
    """Executes the ingestion of Topic 364 for Grade 10 Aviation."""
    print("=" * 80)
    print("VLearn Curriculum Ingestion Engine: Grade 10 Aviation — Topic 364")
    print("Topic: Aircraft Technical Drawing")
    print("=" * 80)

    # 1. Fetch Topic 364 strictly
    topic = Topic.objects.filter(id=364, subject_id=44).first()
    if not topic:
        print("[ERROR] Topic 364 (Subject ID: 44) not found in database!")
        sys.exit(1)

    print(f"[*] Target Topic: [{topic.id}] {topic.name} (Order: {topic.order})")
    print(f"[*] Subject:      [{topic.subject.id}] {topic.subject.name} (Grade: {topic.subject.grade.name})")

    curriculum_data = build_topic364_curriculum()

    total_lessons = 0
    total_pages = 0
    total_blocks = 0

    with transaction.atomic():
        for unit_data in curriculum_data:
            u_order = unit_data["unit_order"]
            u_name = unit_data["unit_name"]
            u_desc = unit_data["unit_description"]
            l_title = unit_data["lesson_title"]
            pages_data = unit_data["pages"]

            learning_unit, _ = LearningUnit.objects.get_or_create(
                topic=topic,
                order=u_order,
                defaults={"name": u_name, "description": u_desc}
            )
            learning_unit.name = u_name
            learning_unit.description = u_desc
            learning_unit.save()

            # Find or create lesson
            lesson = Lesson.objects.filter(topic=topic, learning_unit=learning_unit).first()
            if lesson:
                lesson.blocks.all().delete()
                lesson.title = l_title
                lesson.status = "published"
                lesson.version = 1
                lesson.save()
            else:
                lesson = Lesson.objects.create(
                    topic=topic,
                    learning_unit=learning_unit,
                    title=l_title,
                    status="published",
                    version=1
                )

            print(f"  [+] Ingesting Lesson {u_order + 1}: {lesson.title} (Lesson ID: {lesson.id})")

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
            print(f"      [OK] Ingested {lesson_page_count} Concept Cards for Lesson {u_order + 1}.")

    print("=" * 80)
    print("[SUCCESS] Grade 10 Aviation Topic 364 Ingestion Complete!")
    print(f"[*] Total Lessons Ingested: {total_lessons}")
    print(f"[*] Total Pages/Cards:      {total_pages}")
    print(f"[*] Total Blocks Created:   {total_blocks}")
    print("=" * 80)

if __name__ == "__main__":
    replace_flag = "--replace" in sys.argv
    ingest_grade10_aviation_topic364(replace=replace_flag)
