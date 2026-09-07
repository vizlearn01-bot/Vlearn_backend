"""
VLearn Grade 10 Aviation — Topic 3: Aircraft Components and Construction (Topic ID: 249)
Production Ingestion Engine

Curriculum: CBC (Curriculum ID: 5)
Grade: Grade 10 (Grade ID: 5, Level: 10)
Subject: Aviation (Subject ID: 44)
Topic: Aircraft Components and Construction (Topic ID: 249, Order: 2)

Ingests 3 Comprehensive Learning Units & Lessons (30 Concept Cards):
  1. Aircraft Anatomy — Fuselage, Wings, Empennage, and Landing Gear (LearningUnit order: 0) [10 Cards]
  2. Power Plant, Control Surfaces, and Aircraft Systems (LearningUnit order: 1) [10 Cards]
  3. Component Identification and Aircraft Comparison (LearningUnit order: 2) [10 Cards]

Usage:
  ./venv/bin/python curriculum/ingest_grade10_aviation_topic3.py [--replace]
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
    """Removes bracket citations [11, 71], internal visual prompt text, and normalizes typography."""
    if not text:
        return ""
    # Remove bracket citations e.g. [11], [11, 71], [image_1]
    text = re.sub(r'\[(?:\d+|image_\d+|S\d+.*?|[\d,\s]+)\]', '', text)
    # Remove internal visual generation tags
    text = re.sub(r'\[VISUAL:\s*[^\]]+\]', '', text, flags=re.IGNORECASE)
    # Remove practical task and application internal markers
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

def build_topic249_curriculum():
    """Returns the pedagogical page and block structure for Grade 10 Aviation Topic 249."""
    return [
        # =====================================================================
        # LESSON 1: Aircraft Anatomy — Fuselage, Wings, Empennage, and Landing Gear
        # =====================================================================
        {
            "unit_order": 0,
            "unit_name": "Aircraft Anatomy: Fuselage, Wings, Empennage, and Landing Gear",
            "unit_description": "Structural anatomy of fixed-wing aircraft, including fuselage construction types, wing spars and ribs, empennage stabilizers, and landing gear systems.",
            "lesson_title": "Aircraft Anatomy — Fuselage, Wings, Empennage, and Landing Gear",
            "pages": [
                # Card 1 (Page 1): Photographic Hook & Learning Objectives
                [
                    {
                        "type": "suggested_image",
                        "title": "A Cessna 172 Skyhawk Light Training Aircraft",
                        "content": {
                            "title": "A Cessna 172 Skyhawk Light Training Aircraft",
                            "caption": "A classic high-wing general aviation aircraft displaying the primary structural components: semi-monocoque fuselage, cantilever wings, empennage tail assembly, and fixed tricycle landing gear.",
                            "resolved_image_url": "https://upload.wikimedia.org/wikipedia/commons/5/51/Cessna_172_Skyhawk%2C_S2-AFH.jpg"
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Learning Focus: Aircraft Structural Anatomy",
                        "content": {
                            "title": "Learning Focus: Aircraft Structural Anatomy",
                            "goals": [
                                "Identify the four major structural assemblies of a fixed-wing aircraft: fuselage, wings, empennage, and landing gear.",
                                "Distinguish between truss, monocoque, and modern semi-monocoque fuselage construction.",
                                "Explain how internal wing spars, ribs, and stressed skin distribute flight loads.",
                                "Analyze landing gear configurations and evaluate the engineering trade-offs of fixed versus retractable undercarriages."
                            ]
                        }
                    }
                ],
                # Card 2 (Page 2): Key Terminology
                [
                    {
                        "type": "definition_card",
                        "title": "Core Structural Terminology",
                        "content": {
                            "title": "Primary Airframe Vocabulary",
                            "definitions": [
                                {
                                    "term": "Fuselage",
                                    "definition": "The central structural body of an aircraft that accommodates the flight crew, passengers, and cargo, serving as the common mounting foundation for wings, empennage, and engines.",
                                    "example": "A pressurized semi-monocoque fuselage housing passenger seating on a commercial transport."
                                },
                                {
                                    "term": "Wings",
                                    "definition": "Airfoil-shaped lifting surfaces attached to either side of the fuselage designed to produce aerodynamic lift as the aircraft moves through the air.",
                                    "example": "High-wing configuration on a bush utility aircraft providing ground clearance and stability."
                                },
                                {
                                    "term": "Empennage",
                                    "definition": "The entire tail assembly of an aircraft, consisting of fixed stabilizers and movable control surfaces that provide directional and pitch stability.",
                                    "example": "The vertical fin and horizontal stabilizer group located at the rear of the airframe."
                                },
                                {
                                    "term": "Landing Gear",
                                    "definition": "The structural undercarriage supporting the aircraft's weight on the ground, absorbing landing impact energy and enabling taxi steering and braking.",
                                    "example": "Tricycle gear arrangement featuring a steerable nosewheel and two main gear assemblies."
                                },
                                {
                                    "term": "Spars",
                                    "definition": "Heavy longitudinal structural beams running from the wing root to the wingtip that carry primary bending and shear loads during flight.",
                                    "example": "Front and rear aluminum alloy I-beam spars running the entire span of the wing."
                                },
                                {
                                    "term": "Ribs",
                                    "definition": "Transverse structural cross-members arranged perpendicular to the spars that give the wing its aerodynamic airfoil profile and transfer skin loads to the spars.",
                                    "example": "Formed sheet-metal ribs spaced evenly along the wing span."
                                }
                            ]
                        }
                    }
                ],
                # Card 3 (Page 3): Fuselage Construction Types
                [
                    {
                        "type": "concept_explanation",
                        "title": "Fuselage Structural Architecture",
                        "content": {
                            "title": "Evolution of Fuselage Construction",
                            "text": "The fuselage functions as the torso of the aircraft, linking all structural assemblies together while sheltering passengers, crew, and avionics. Over the history of aeronautics, three distinct structural designs evolved:\n\n- **Truss Structure**: Constructed from welded steel or aluminum alloy tubing forming a rigid triangular framework. The outer fabric or metal skin carries no structural load. While strong, truss structures are labor-intensive, space-inefficient, and primarily restricted to vintage, light aerobatic, or agricultural utility planes.\n- **Monocoque Structure**: A true single-shell design where the outer skin carries all structural flight and pressurization loads (similar to an eggshell). While highly streamlined and light, any dent, puncture, or buckling of the skin can trigger immediate catastrophic failure of the entire airframe.\n- **Semi-Monocoque Structure**: The universal standard for modern transport and general aviation aircraft. It utilizes internal bulkheads, circular frames, and longitudinal stringers overlaid by a thin, riveted aluminum or composite skin. The internal skeletal framework prevents skin buckling, while the stressed skin shares bending, shear, and torsional loads, delivering supreme structural resilience and weight efficiency."
                        }
                    }
                ],
                # Card 4 (Page 4): Technical Diagram (SVG)
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Aircraft Structural Anatomy: Framework & Components",
                        "content": {
                            "title": "Structural Framework of a Modern Airframe",
                            "caption": "Cutaway view highlighting semi-monocoque fuselage bulkheads and stringers, internal wing spars and ribs, empennage stabilizers, and tricycle landing gear."
                        }
                    }
                ],
                # Card 5 (Page 5): Internal Wing Anatomy & Empennage
                [
                    {
                        "type": "concept_explanation",
                        "title": "Wing Load Transfer & Empennage Stability",
                        "content": {
                            "title": "How Wing and Tail Structures Withstand Flight Forces",
                            "text": "An aircraft wing is subjected to tremendous upward aerodynamic bending loads in flight, downward gravitational loads on the ground, and violent twisting moments in atmospheric turbulence:\n\n- **Spars (The Load-Bearing Beams)**: Wing spars extend spanwise from the fuselage attachment fittings (wing root) to the wingtips. In flight, lift bends the wingtips upward, putting the bottom spar cap under extreme tension and the top spar cap under intense compression. Heavy aircraft often incorporate multiple spars (front, main, and rear) to provide fail-safe structural redundancy.\n- **Ribs (Airfoil Shapers & Load Distributors)**: Ribs are oriented camber-wise (from leading edge to trailing edge). They establish the aerodynamic contour of the airfoil and transmit aerodynamic pressures acting on the skin directly into the heavy spars.\n- **Stressed Skin**: The outer skin provides a smooth aerodynamic boundary and withstands torsional twisting forces through shear stress distribution.\n- **The Empennage (Tail Assembly)**: Operating like the feathers on an arrow, the empennage stabilizes flight. The **Vertical Stabilizer** prevents unwanted yawing (directional stability), while the **Horizontal Stabilizer** counteracts pitching moments (longitudinal stability), ensuring the airframe flies straight and true."
                        }
                    }
                ],
                # Card 6 (Page 6): Landing Gear Systems & Configurations
                [
                    {
                        "type": "comparison_table",
                        "title": "Landing Gear Configurations and Mechanisms",
                        "content": {
                            "title": "Aircraft Undercarriage Comparison",
                            "headers": ["Design Aspect", "Tricycle Landing Gear", "Conventional (Tailwheel) Gear", "Retractable Gear"],
                            "rows": [
                                ["Wheel Layout", "One steerable nosewheel forward, two main gear struts behind center of gravity", "Two main gear struts forward of center of gravity, small tailwheel at rear", "Wheels fold flush into wing bays or fuselage wells during flight"],
                                ["Ground Handling", "Inherently stable; resistant to ground loops; level cabin attitude", "Demands sensitive rudder pedal coordination; susceptible to ground loop swerves", "Eliminates parasitic drag in cruise; requires hydraulic or electric actuators"],
                                ["Primary Usage", "Modern light trainers, business jets, and commercial transport airliners", "Bush aircraft, taildraggers operating on unpaved gravel and grass runways", "High-speed commercial airliners, military aircraft, high-performance singles"],
                                ["Key Advantage", "Superior ground visibility, safe braking, easier crosswind landings", "Lightweight, simple, high propeller ground clearance on rough surfaces", "Significantly increases cruise speed, range, and fuel economy"]
                            ]
                        }
                    }
                ],
                # Card 7 (Page 7): Real-World Application (Wilson Airport)
                [
                    {
                        "type": "real_world_example",
                        "title": "Training Fleet Dynamics at Wilson Airport",
                        "content": {
                            "title": "The Cessna 172 Skyhawk in East African Flight Training",
                            "text": "At Wilson Airport in Nairobi, one of the busiest general aviation hubs in Africa, flight schools rely heavily on the Cessna 172 Skyhawk for ab-initio pilot instruction. The aircraft exemplifies optimal structural choices for training environments:\n\n- **High-Wing Architecture**: Mounting the wing above the cabin places the center of gravity low, imparting natural pendulum stability that automatically restores level flight when perturbed by convective turbulence over the Rift Valley.\n- **Semi-Monocoque Durability**: The riveted aluminum alloy fuselage withstands thousands of repeated takeoff and landing cycles without airframe fatigue.\n- **Fixed Tricycle Gear with Spring Steel Struts**: Eliminates the risk of gear-up landing errors by novice student pilots while the flexible steel main gear absorbs hard landing impacts, protecting the fuselage keel and wing spar attachments."
                        }
                    }
                ],
                # Card 8 (Page 8): Safety Connection & Pre-Flight Inspections
                [
                    {
                        "type": "concept_explanation",
                        "title": "Pre-Flight Walk-Around and Oleo Strut Airworthiness",
                        "content": {
                            "title": "Critical Inspection of Shock Struts and Fasteners",
                            "text": "Before every single flight, standard operating procedures require the pilot-in-command to execute a meticulous physical walk-around inspection (pre-flight check):\n\n- **Oleo-Pneumatic Shock Struts**: The pilot checks the polished chrome piston rod of each landing gear shock strut. The strut uses compressed nitrogen gas to absorb taxi shocks and metered hydraulic fluid to cushion landing impact. The chrome cylinder must be clean, free of grit, and extended to the manufacturer-specified height.\n- **Fluid Leakage Risk**: If hydraulic oil is seen weeping from strut wiper seals, the shock absorber cannot dissipate impact energy. Upon touchdown, the strut will 'bottom out' (metal slamming against metal), generating extreme shock loads capable of cracking wing main spars or snapping gear trunnions.\n- **Mandatory Action**: The pilot must ground the aircraft immediately, tag it out of service, and log a defect report for licensed aircraft maintenance engineers."
                        }
                    }
                ],
                # Card 9 (Page 9): Educational Video Integration
                [
                    {
                        "type": "suggested_video",
                        "title": "Aircraft Components and Primary Structure Walkthrough",
                        "content": {
                            "title": "3D Anatomy of an Airplane: Structure and Parts",
                            "description": "Examine the three-dimensional relationship between the semi-monocoque fuselage, wing internal spars and ribs, empennage stabilizers, and landing gear layout.",
                            "url": "https://www.youtube.com/watch?v=_x5RhNQZrrg"
                        }
                    }
                ],
                # Card 10 (Page 10): Formative Knowledge Checks & Summary
                [
                    {
                        "type": "knowledge_check",
                        "title": "Diagnostic Check: Wing Load-Bearing Structure",
                        "content": {
                            "question": "Which internal structural component of an aircraft wing runs spanwise from the wing root to the wingtip, acting as the primary load-bearing beam carrying upward bending forces during flight?",
                            "options": [
                                "Formed aluminum airfoil ribs",
                                "Longitudinal main spars",
                                "Fuselage structural stringers",
                                "Internal pressure bulkheads"
                            ],
                            "answer": "B",
                            "explanation": "Wing spars are heavy longitudinal structural beams running from the wing root to the wingtip. They are specifically engineered to withstand the intense upward bending moments and shear loads created by aerodynamic lift in flight, transferring those forces safely into the fuselage keel."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Diagnostic Check: Fuselage Construction",
                        "content": {
                            "question": "Why do modern commercial airliners use a semi-monocoque fuselage design rather than a pure monocoque structure?",
                            "options": [
                                "Semi-monocoque airframes are constructed entirely from lightweight treated timber",
                                "Internal frames, bulkheads, and stringers share structural stresses with the stressed outer skin, preventing total catastrophic failure if skin panels are damaged",
                                "Pure monocoque fuselages are too heavy to achieve positive aerodynamic climb rates",
                                "Semi-monocoque construction eliminates the need for wing spar attachment fittings"
                            ],
                            "answer": "B",
                            "explanation": "In a pure monocoque structure, the thin outer skin carries all flight and pressurization loads without internal reinforcement, making it catastrophic if dented or punctured. Semi-monocoque architecture solves this by reinforcing the outer skin with internal bulkheads, frames, and stringers, distributing stresses safely across the entire framework."
                        }
                    },
                    {
                        "type": "summary",
                        "title": "Core Takeaways: Aircraft Structural Anatomy",
                        "content": {
                            "title": "Summary & Synthesis",
                            "summary_points": [
                                "The airframe comprises five fundamental assemblies: fuselage, wings, empennage, landing gear, and power plant.",
                                "Modern aircraft employ semi-monocoque construction, combining internal framework with stressed skin for high strength-to-weight performance.",
                                "Wing spars endure primary bending forces while transverse ribs establish airfoil geometry and transfer aerodynamic pressures.",
                                "Landing gear cushions touchdown impact through oleo struts and provides directional ground steering via tricycle or tailwheel configurations."
                            ]
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 2: Power Plant, Control Surfaces, and Aircraft Systems
        # =====================================================================
        {
            "unit_order": 1,
            "unit_name": "Power Plant, Control Surfaces, and Aircraft Systems",
            "unit_description": "Propulsion principles, three axes of flight (roll, pitch, yaw), primary control surfaces (ailerons, elevators, rudder), secondary controls (flaps), and coordinated maneuvers.",
            "lesson_title": "Power Plant, Control Surfaces, and Aircraft Systems",
            "pages": [
                # Card 1 (Page 1): Photographic Hook & Learning Objectives
                [
                    {
                        "type": "suggested_image",
                        "title": "Modernized Glass Cockpit and Primary Flight Controls",
                        "content": {
                            "title": "Modernized Glass Cockpit and Primary Flight Controls",
                            "caption": "A complex aircraft flight deck displaying dual control yokes, throttle thrust levers, rudder pedal linkages, and electronic flight displays commanding aerodynamic control surfaces.",
                            "resolved_image_url": "https://upload.wikimedia.org/wikipedia/commons/6/6e/C-141C_Glass_Cockpit_Upgrade.JPEG"
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Learning Focus: Flight Controls and Flight Dynamics",
                        "content": {
                            "title": "Learning Focus: Flight Controls and Flight Dynamics",
                            "goals": [
                                "Explain how aircraft power plants produce forward thrust under Newton's Third Law of Motion.",
                                "Define the three mutually perpendicular axes of flight passing through an aircraft's center of gravity.",
                                "Map primary control surfaces (ailerons, elevators, rudder) to their respective flight axes and cockpit inputs.",
                                "Analyze the aerodynamic purpose of secondary control surfaces (flaps) during low-speed takeoff and landing phases."
                            ]
                        }
                    }
                ],
                # Card 2 (Page 2): Key Terminology
                [
                    {
                        "type": "definition_card",
                        "title": "Flight Dynamics & Control Terminology",
                        "content": {
                            "title": "Aerodynamic Control Vocabulary",
                            "definitions": [
                                {
                                    "term": "Power Plant",
                                    "definition": "The complete propulsion subsystem comprising the engine, propeller or jet turbine, and supporting accessories that converts fuel energy into forward aerodynamic thrust.",
                                    "example": "A four-cylinder horizontally opposed piston engine driving a fixed-pitch aluminum propeller."
                                },
                                {
                                    "term": "Three Flight Axes",
                                    "definition": "Three imaginary mutually perpendicular axes intersecting at the aircraft's center of gravity: the longitudinal, lateral, and vertical axes.",
                                    "example": "An aircraft simultaneously rolling about its longitudinal axis and pitching about its lateral axis during a turn."
                                },
                                {
                                    "term": "Ailerons",
                                    "definition": "Hinged primary control surfaces fitted to the outer trailing edges of each wing that deflect oppositely to control roll about the longitudinal axis.",
                                    "example": "Turning the control yoke left causes the left aileron to deflect up and the right aileron to deflect down."
                                },
                                {
                                    "term": "Elevators",
                                    "definition": "Hinged primary control surfaces attached to the horizontal stabilizer trailing edge that deflect together to control pitch attitude about the lateral axis.",
                                    "example": "Pulling back on the control wheel raises the elevators, pushing the tail down and pitching the nose up."
                                },
                                {
                                    "term": "Rudder",
                                    "definition": "A hinged primary control surface attached to the vertical stabilizer trailing edge that deflects left or right to control yaw about the vertical axis.",
                                    "example": "Depressing the right rudder pedal swings the rudder trailing edge to the right, yawing the nose right."
                                },
                                {
                                    "term": "Flaps",
                                    "definition": "Hinged secondary control surfaces installed on the inboard trailing edges of wings that deflect downward together to increase wing camber, lift, and drag at low speeds.",
                                    "example": "Extending 20 degrees of flaps on final approach to reduce landing approach speed."
                                }
                            ]
                        }
                    }
                ],
                # Card 3 (Page 3): Power Plant & Aerodynamic Thrust
                [
                    {
                        "type": "concept_explanation",
                        "title": "The Power Plant: Generating Propulsive Thrust",
                        "content": {
                            "title": "Propulsion Principles & Newton's Third Law",
                            "text": "The power plant is the muscular engine of the aircraft. Without forward propulsion, fixed wings cannot create the airflow necessary to generate aerodynamic lift:\n\n- **Operating Principle**: All aviation power plants operate under **Newton's Third Law of Motion**—for every action, there is an equal and opposite reaction. The power plant accelerates a large mass of air backward; the equal and opposite physical reaction propels the aircraft forward with **Thrust**.\n- **Piston Engines vs. Turbofans**: Light training planes utilize reciprocating internal combustion piston engines to turn a propeller. The propeller blades act as spinning airfoils that bite into the air and drive it rearward. Commercial jetliners utilize high-bypass turbofan engines, drawing in enormous volumes of air, burning aviation fuel in high-pressure combustion chambers, and expelling high-velocity exhaust to deliver tens of thousands of pounds of thrust.\n- **Supporting Systems**: Power plants also drive vital secondary systems: electrical alternators to power cockpit avionics, vacuum pumps for gyroscopic flight instruments, and engine-driven hydraulic pumps for retractable landing gear and control surface servos."
                        }
                    }
                ],
                # Card 4 (Page 4): Technical Diagram (SVG)
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Three Flight Axes and Primary Control Surface Deflections",
                        "content": {
                            "title": "Three Flight Axes and Control Mechanics",
                            "caption": "Orthogonal representation of the Longitudinal (Roll), Lateral (Pitch), and Vertical (Yaw) axes, illustrating corresponding aileron, elevator, and rudder deflections."
                        }
                    }
                ],
                # Card 5 (Page 5): Primary vs. Secondary Control Surfaces
                [
                    {
                        "type": "comparison_table",
                        "title": "Primary and Secondary Flight Control Surfaces",
                        "content": {
                            "title": "Flight Control Kinematics Matrix",
                            "headers": ["Control Surface", "Location on Airframe", "Deflection Direction", "Controlled Axis & Motion", "Cockpit Pilot Input"],
                            "rows": [
                                ["Ailerons", "Outer trailing edges of wings", "Differential (one up, one down)", "Longitudinal axis -> Roll (bank)", "Turn control yoke / stick left or right"],
                                ["Elevators", "Trailing edge of horizontal stabilizer", "Symmetrical (both move together)", "Lateral axis -> Pitch (nose up/down)", "Push yoke forward (pitch down) / Pull back (pitch up)"],
                                ["Rudder", "Trailing edge of vertical stabilizer", "Lateral swing (swings left or right)", "Vertical axis -> Yaw (nose left/right)", "Depress left or right foot rudder pedals"],
                                ["Wing Flaps", "Inboard trailing edges of wings", "Symmetrical downward extension", "Alters lift/drag coefficient (secondary)", "Select flap lever / handle detent position"]
                            ]
                        }
                    }
                ],
                # Card 6 (Page 6): Aerodynamics of Coordinated Flight
                [
                    {
                        "type": "concept_explanation",
                        "title": "Coordinating Controls for Atmospheric Maneuvering",
                        "content": {
                            "title": "The Physics of the Coordinated Turn",
                            "text": "In three-dimensional atmospheric flight, an aircraft cannot turn simply by steering with one control surface. A safe turn requires harmonious coordination of all three primary controls:\n\n- **Initiating the Turn (Roll)**: The pilot turns the yoke left. The left aileron rises (reducing left wing lift), and the right aileron drops (increasing right wing lift). The unbalanced lift banks the wings to the left.\n- **Counteracting Adverse Yaw (Rudder)**: The downward-deflected right aileron creates greater induced drag than the raised left aileron. This drag difference pulls the nose opposite to the turn (adverse yaw to the right). The pilot must simultaneously press the left rudder pedal to overcome adverse yaw, keeping the turn perfectly aligned.\n- **Sustaining Altitude (Elevator)**: When an aircraft banks, the total lift vector tilts sideways. The vertical component supporting the airplane's weight decreases. To prevent the aircraft from sinking, the pilot applies slight backward pressure on the yoke, deflecting elevators upward to maintain level altitude throughout the turn."
                        }
                    }
                ],
                # Card 7 (Page 7): Real-World Application (Heavy Jet Flaps at JKIA)
                [
                    {
                        "type": "real_world_example",
                        "title": "Flap Deployment Operations at JKIA Nairobi",
                        "content": {
                            "title": "High-Lift Devices on Heavy Jets Landing in Thin Air",
                            "text": "Jomo Kenyatta International Airport (JKIA) sits at an elevation of approximately 5,327 feet above sea level. The high altitude reduces air density, requiring higher true airspeeds to generate sufficient lift:\n\n- **Low-Speed Approach Problem**: Modern airliners like the Boeing 787 or Airbus A350 have high cruise speeds with thin, swept wings. Without modification, their stall speeds would exceed 160 knots, requiring impractically long runways and risking blown tires.\n- **Trailing-Edge Flaps & Leading-Edge Slats**: During arrival over Athi River, pilots extend complex multi-slotted Fowler flaps from the wing trailing edge and slats from the leading edge. This increases the total wing surface area and deepens the camber.\n- **Operational Result**: Lift increases dramatically, permitting the heavy airliner to descend smoothly at a manageable 135 knots and stop safely well within runway boundaries."
                        }
                    }
                ],
                # Card 8 (Page 8): Safety Connection & Control Rigging Checks
                [
                    {
                        "type": "concept_explanation",
                        "title": "Pre-Flight Control Rigging & Sense Checks",
                        "content": {
                            "title": "Preventing Reverse-Rigging Catastrophes",
                            "text": "One of the most dangerous maintenance hazards in aviation history is cross-rigging control cables after routine servicing:\n\n- **The Reversal Threat**: If mechanic cables are inadvertently crossed during overhaul, turning the control wheel to the left might force the left aileron down and right aileron up. If an unsuspecting pilot initiates a roll to clear terrain, the airplane will violently bank into the obstacle.\n- **The 'Free and Correct' Verification Protocol**: Pilots perform a rigorous standard pre-flight test before starting engines. The pilot turns the yoke fully to the left, visually looks out the window at the left wing, and verbally confirms: 'Yoke left, left aileron up, right aileron down.' Next, pulling the yoke back: 'Yoke back, elevators deflected upward.' Finally, pressing the right rudder pedal: 'Right pedal, rudder swung right.'\n- **Zero Tolerance**: If any flight control does not move smoothly through its full design travel or moves in an inverted direction, the aircraft is declared immediately unairworthy."
                        }
                    }
                ],
                # Card 9 (Page 9): Educational Video Integration
                [
                    {
                        "type": "suggested_video",
                        "title": "Flight Controls and Aircraft Axes in Motion",
                        "content": {
                            "title": "Flight Control Deflections: Yoke, Cables, and Surfaces",
                            "description": "Observe physical control surfaces deflecting on an active training aircraft as the pilot moves the cockpit yoke and rudder pedals through their full range of motion.",
                            "url": "https://www.youtube.com/watch?v=CAl3PayUW0M"
                        }
                    }
                ],
                # Card 10 (Page 10): Formative Knowledge Checks & Summary
                [
                    {
                        "type": "knowledge_check",
                        "title": "Diagnostic Check: Pitch Control Inputs",
                        "content": {
                            "question": "A pilot wants to establish a climb attitude after takeoff. What mechanical action must the pilot perform with the flight controls?",
                            "options": [
                                "Depress the right rudder pedal firmly to swing the tail",
                                "Rotate the control yoke fully counter-clockwise",
                                "Pull backward on the control yoke, deflecting both elevators upward",
                                "Extend full flaps on both wings simultaneously"
                            ],
                            "answer": "C",
                            "explanation": "Pulling back on the control yoke moves mechanical linkages that deflect the elevators upward into the passing airflow. The air pushes the horizontal tail assembly downward, rotating the aircraft about its lateral axis and pivoting the nose upward into a pitch-up climb attitude."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Diagnostic Check: Aileron Deflection Dynamics",
                        "content": {
                            "question": "When an aircraft is banking into a roll to the right, what are the physical positions of the wing ailerons?",
                            "options": [
                                "Both left and right ailerons are deflected downward symmetrically",
                                "The left aileron is deflected downward (increasing left wing lift) while the right aileron is deflected upward (reducing right wing lift)",
                                "Both left and right ailerons are deflected upward symmetrically",
                                "The right aileron is deflected downward while the left aileron remains in neutral streamline"
                            ],
                            "answer": "B",
                            "explanation": "To initiate a right bank, the aircraft must produce more lift on the left wing and less lift on the right wing. Deflecting the left aileron downward increases left wing camber and lift, lifting that wing up; deflecting the right aileron upward reduces right wing lift, dropping it down, resulting in a clockwise roll to the right."
                        }
                    },
                    {
                        "type": "summary",
                        "title": "Core Takeaways: Flight Controls & Axes",
                        "content": {
                            "title": "Summary & Synthesis",
                            "summary_points": [
                                "Aircraft engines deliver forward thrust by accelerating air rearward in accordance with Newton's Third Law.",
                                "Aircraft rotate about three orthogonal axes passing through the center of gravity: Longitudinal (Roll), Lateral (Pitch), and Vertical (Yaw).",
                                "Primary flight control surfaces comprise ailerons (roll), elevators (pitch), and rudder (yaw).",
                                "Secondary control surfaces, primarily flaps, augment wing camber and lift at slow speeds for safe runway arrivals and departures."
                            ]
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 3: Component Identification and Aircraft Comparison
        # =====================================================================
        {
            "unit_order": 2,
            "unit_name": "Component Identification and Aircraft Comparison",
            "unit_description": "Architectural and functional comparison between fixed-wing and rotary-wing aircraft, six functional families, helicopter rotor dynamics, torque reaction, and landing gear configurations.",
            "lesson_title": "Component Identification and Aircraft Comparison",
            "pages": [
                # Card 1 (Page 1): Photographic Hook & Learning Objectives
                [
                    {
                        "type": "suggested_image",
                        "title": "A Bell 206L LongRanger Rotary-Wing Aircraft in Flight",
                        "content": {
                            "title": "A Bell 206L LongRanger Rotary-Wing Aircraft in Flight",
                            "caption": "A light turbine utility helicopter demonstrating key rotary-wing structural features: spinning overhead main rotor, anti-torque tail rotor on the tail boom, and tubular landing skids.",
                            "resolved_image_url": "https://upload.wikimedia.org/wikipedia/commons/7/78/Bell_206L-4_LongRanger_IV_over_Botafogo_Bay%2C_Rio_de_Janeiro.jpg"
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Learning Focus: Fixed-Wing vs. Rotary-Wing Architecture",
                        "content": {
                            "title": "Learning Focus: Fixed-Wing vs. Rotary-Wing Architecture",
                            "goals": [
                                "Categorize aircraft components into six core functional families: structure, lift, propulsion, stability, control, and ground support.",
                                "Contrast the lift and propulsion mechanisms of fixed-wing airplanes with rotary-wing helicopters.",
                                "Explain how helicopters resolve Newton's third law torque reaction using anti-torque tail rotors.",
                                "Evaluate why tubular landing skids are selected over wheeled landing gear for remote and bush helicopter operations."
                            ]
                        }
                    }
                ],
                # Card 2 (Page 2): Key Terminology
                [
                    {
                        "type": "definition_card",
                        "title": "Aircraft Classification & Rotorcraft Terminology",
                        "content": {
                            "title": "Comparative Aviation Vocabulary",
                            "definitions": [
                                {
                                    "term": "Fixed-Wing Aircraft",
                                    "definition": "A heavier-than-air aircraft whose lifting surfaces are rigidly attached to the airframe, requiring continuous forward motion through the atmosphere to produce aerodynamic lift.",
                                    "example": "A commercial turboprop airliner or single-engine general aviation trainer."
                                },
                                {
                                    "term": "Rotary-Wing Aircraft",
                                    "definition": "A heavier-than-air aircraft supported in flight by the reaction of the air on one or more power-driven rotors spinning about substantially vertical axes.",
                                    "example": "A medical evacuation helicopter capable of vertical takeoff and stationary hover."
                                },
                                {
                                    "term": "Main Rotor Assembly",
                                    "definition": "The overhead spinning blade system consisting of two or more aerodynamic blades mounted to a central rotor hub that generates both vertical lift and directional thrust.",
                                    "example": "A two-bladed semi-rigid teetering main rotor on a utility helicopter."
                                },
                                {
                                    "term": "Tail Rotor",
                                    "definition": "A smaller, vertically spinning rotor mounted at the aft end of the helicopter's tail boom that generates lateral thrust to counteract main rotor torque and provide yaw steering.",
                                    "example": "A variable-pitch two-bladed tail rotor controlled by cockpit anti-torque foot pedals."
                                },
                                {
                                    "term": "Landing Skids",
                                    "definition": "Tubular metal alloy runners mounted beneath a helicopter undercarriage that support the airframe on the ground without requiring rolling wheels or brake assemblies.",
                                    "example": "High-clearance tubular steel skids fitted to bush wildlife surveillance helicopters."
                                },
                                {
                                    "term": "Torque Reaction",
                                    "definition": "The reactive twisting force generated when an engine drives a spinning main rotor, which, under Newton's third law, attempts to spin the helicopter fuselage in the opposite direction.",
                                    "example": "A clockwise main rotor creating a counter-clockwise rotational spin in the fuselage."
                                }
                            ]
                        }
                    }
                ],
                # Card 3 (Page 3): Six Functional Families of Aircraft Components
                [
                    {
                        "type": "concept_explanation",
                        "title": "The Six Functional Families of Aircraft Components",
                        "content": {
                            "title": "Systematic Airframe Classification",
                            "text": "Every physical component on an aircraft, whether an intercontinental airliner or a bush helicopter, belongs to one of six essential functional families:\n\n- **1. Structural Assembly**: Provides the physical envelope, cabin space, and internal load-bearing spine (Fuselage, tail boom, bulkheads, stringers, skin).\n- **2. Lift Generation**: Aerodynamic surfaces contoured to create upward force (Fixed cantilever wings, spinning main rotor blades).\n- **3. Propulsion System**: Converts fuel energy into kinetic force to propel the aircraft (Piston engines, turbofans, turboshaft gearboxes driving rotors).\n- **4. Flight Stability**: Dampens turbulence perturbations to keep the airframe pointing straight (Vertical fin, horizontal tailplane, horizontal stabilizer winglets).\n- **5. Directional Control**: Hinged or pivoting surfaces permitting the pilot to command pitch, roll, and yaw (Ailerons, elevators, rudder, cyclic swashplate, tail rotor).\n- **6. Ground Support**: Absorbs touchdown energy and maintains ground clearance (Tricycle wheels, oleo shock struts, tubular steel landing skids)."
                        }
                    }
                ],
                # Card 4 (Page 4): Technical Diagram (SVG)
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Fixed-Wing vs Rotary-Wing Functional Comparison and Torque Balance",
                        "content": {
                            "title": "Comparative Architecture & Anti-Torque Physics",
                            "caption": "Side-by-side architectural mapping of fixed-wing vs rotary-wing functional components, with an inset diagram illustrating helicopter torque reaction and tail rotor thrust."
                        }
                    }
                ],
                # Card 5 (Page 5): Comparative Analysis Table
                [
                    {
                        "type": "comparison_table",
                        "title": "Fixed-Wing vs Rotary-Wing Engineering Matrix",
                        "content": {
                            "title": "Structural & Operational Comparison",
                            "headers": ["Functional Domain", "Fixed-Wing Aircraft (Airplane)", "Rotary-Wing Aircraft (Helicopter)"],
                            "rows": [
                                ["Lift Mechanism", "Rigid wings requiring continuous forward airspeed generated by thrust", "Power-driven spinning rotor blades creating lift without forward aircraft movement"],
                                ["Takeoff & Landing", "Demands paved or smooth unpaved runways for long takeoff roll", "True Vertical Takeoff and Landing (VTOL) from confined clearings"],
                                ["Low-Speed Ability", "Cannot hover; stalls if airspeed drops below minimum stall threshold", "Capable of sustaining zero-airspeed stationary hover in mid-air"],
                                ["Directional Yaw Control", "Movable vertical rudder mounted on the empennage tail fin", "Tail rotor varying lateral thrust to counter torque and command yaw"],
                                ["Ground Undercarriage", "Pneumatic wheeled landing gear with multi-disc friction brakes", "Tubular steel landing skids (lightweight) or wheels on heavy models"],
                                ["Primary Mission Roles", "High-speed, long-distance passenger transport and cargo logistics", "Search and rescue, bush medical evacuation, sling-load transport, hovering"]
                            ]
                        }
                    }
                ],
                # Card 6 (Page 6): Torque Reaction & Anti-Torque Physics
                [
                    {
                        "type": "concept_explanation",
                        "title": "Helicopter Rotor Dynamics & Torque Balance",
                        "content": {
                            "title": "Newton's Third Law in Helicopter Flight",
                            "text": "The fundamental engineering challenge of rotary-wing flight is managing the torque reaction produced by the spinning main rotor:\n\n- **The Torque Dilemma**: As the turbine engine turns the transmission and spins the heavy main rotor blades clockwise (viewed from above), **Newton's Third Law** dictates that an equal and opposite torque force tries to spin the entire fuselage counter-clockwise. Without compensation, the helicopter would spin uncontrollably in circles.\n- **The Anti-Torque Solution**: The tail rotor is mounted vertically at the end of a long tail boom. Spinning at several thousand revolutions per minute, it acts as a sideways propeller, generating lateral thrust that pushes in the opposite direction of the fuselage spin.\n- **Yaw Steering via Tail Rotor**: The pilot controls foot pedals linked to the tail rotor. Pushing the left or right pedal changes the blade angle (pitch) of the tail rotor. Increasing sideways thrust swings the nose right; decreasing sideways thrust allows engine torque to swing the nose left, giving the pilot surgical yaw control in hover."
                        }
                    }
                ],
                # Card 7 (Page 7): Real-World Application (Kenya Wildlife Conservation)
                [
                    {
                        "type": "real_world_example",
                        "title": "Wildlife Rescue Operations in Tsavo National Park",
                        "content": {
                            "title": "Why Conservationists Rely on Helicopters with Landing Skids",
                            "text": "Across the vast bush wilderness of Tsavo and the Maasai Mara in Kenya, wildlife rangers and veterinarians must respond quickly to injured elephants, rhinos, and lions:\n\n- **The Runway Obstacle**: In dense savannah or thorny scrubland, there are zero flat runways. A fixed-wing patrol plane can spot an injured animal from above but cannot land without crashing into acacia trees or anthills.\n- **Helicopter Skids Advantage**: A turbine helicopter (such as the Bell 206) can hover precisely over the veterinary team, lower supplies, or land directly on uneven ground, thorn bushes, or river gravel bars.\n- **Skid Resilience**: Steel landing skids have no rubber tires to puncture on sharp rocks, no complex hydraulic lines to fail, and distribute the helicopter's weight widely so it does not sink into soft mud."
                        }
                    }
                ],
                # Card 8 (Page 8): Safety Connection: Tail Rotor Hazard Exclusion Zone
                [
                    {
                        "type": "concept_explanation",
                        "title": "Heliport Operations & Tail Rotor Exclusion Zones",
                        "content": {
                            "title": "The Invisible Danger of the Tail Rotor",
                            "text": "Airports and helipads enforce strict safety perimeters around operating rotary-wing aircraft:\n\n- **The Threat of Invisibility**: When running at operational speed, the tail rotor blades spin into a completely invisible blur. Mounted roughly at head-height (4 to 6 feet above the ground) on light utility helicopters, it represents an immediate fatal hazard to ground personnel.\n- **The 180-Degree Exclusion Zone**: Ground safety protocols strictly prohibit walking anywhere behind the helicopter's cabin doors. The entire rear hemisphere encompassing the tail boom and tail rotor is designated an absolute no-entry zone.\n- **Safe Approach Protocol**: Ground crew must always approach and depart from the front 90-degree arc, maintaining direct eye contact with the pilot at all times, crouching low to clear the main rotor disc, and waiting for the pilot's clear thumbs-up signal before walking near the airframe."
                        }
                    }
                ],
                # Card 9 (Page 9): Educational Video Integration
                [
                    {
                        "type": "suggested_video",
                        "title": "How Aircraft Work: Aerodynamics and Propulsion",
                        "content": {
                            "title": "Comparing Aerodynamic Forces: Lift, Thrust, and Rotors",
                            "description": "Explore the physical mechanisms of airflow over fixed wings versus rotating blades, illustrating how pressure differentials produce flight.",
                            "url": "https://www.youtube.com/watch?v=g9oVFRG1PGQ"
                        }
                    }
                ],
                # Card 10 (Page 10): Formative Knowledge Checks & Summary
                [
                    {
                        "type": "knowledge_check",
                        "title": "Diagnostic Check: Helicopter Torque Reaction",
                        "content": {
                            "question": "Under Newton's third law of motion, when a helicopter's engine drives the main rotor blades in a clockwise direction, what reactive physical force is exerted on the fuselage?",
                            "options": [
                                "The fuselage remains completely motionless without any reactive twisting forces",
                                "The fuselage experiences a counter-torque that attempts to spin it in the opposite (counter-clockwise) direction",
                                "The fuselage automatically climbs vertically without requiring blade pitch adjustment",
                                "The fuselage undergoes continuous rolling about its longitudinal axis"
                            ],
                            "answer": "B",
                            "explanation": "Newton's Third Law states that every action produces an equal and opposite reaction. As the engine exerts rotational torque to spin the heavy main rotor clockwise, an equal and opposite reactive torque twists the helicopter fuselage counter-clockwise. The tail rotor produces lateral thrust to neutralize this torque reaction."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Diagnostic Check: Helicopter Undercarriage Selection",
                        "content": {
                            "question": "Why are tubular landing skids commonly installed on light utility helicopters instead of wheeled undercarriages?",
                            "options": [
                                "Landing skids are pressurized with helium to provide auxiliary aerodynamic buoyancy",
                                "Helicopters take off and land vertically without rolling along a runway, so lightweight skids eliminate brake weight and can land safely on rough, uneven terrain",
                                "Skids generate high-speed forward thrust by spinning beneath the fuselage",
                                "Landing skids significantly reduce drag at supersonic flight velocities"
                            ],
                            "answer": "B",
                            "explanation": "Because helicopters take off and land vertically (VTOL), they have no requirement for a high-speed takeoff roll or runway wheel brakes. Tubular steel skids provide a lightweight, rugged, and mechanically simple undercarriage that safely supports the aircraft on rough, sandy, or muddy ground where wheels would sink."
                        }
                    },
                    {
                        "type": "summary",
                        "title": "Core Takeaways: Component Identification & Comparison",
                        "content": {
                            "title": "Summary & Synthesis",
                            "summary_points": [
                                "Aircraft components belong to six functional families: structure, lift, propulsion, stability, control, and ground support.",
                                "Fixed-wing airplanes rely on forward airspeed over rigid wings, whereas rotary-wing helicopters spin rotor blades to create lift and hover.",
                                "Newton's third law torque reaction in helicopters is counteracted by lateral thrust produced by the tail rotor.",
                                "Landing skids offer light helicopters a robust, wheel-free undercarriage well-suited for rugged bush and off-airport operations."
                            ]
                        }
                    }
                ]
            ]
        }
    ]

def ingest_grade10_aviation_topic3(replace=False):
    """Ingests Grade 10 Aviation Topic 249 into the database."""
    print("=" * 80)
    print("VLEARN INGESTION ENGINE: Grade 10 Aviation — Topic 3 (ID: 249)")
    print("Aircraft Components and Construction")
    print("=" * 80)

    curriculum = Curriculum.objects.get(id=5)
    grade = Grade.objects.get(id=5, level=10)
    subject = Subject.objects.get(id=44, grade=grade)

    print(f"[*] Curriculum: {curriculum.name} (ID: {curriculum.id})")
    print(f"[*] Grade:      {grade.name} (ID: {grade.id}, Level: {grade.level})")
    print(f"[*] Subject:    {subject.name} (ID: {subject.id})")

    topic = Topic.objects.get(id=249, subject=subject)
    print(f"[*] Topic:      {topic.name} (ID: {topic.id}, Order: {topic.order})")

    curriculum_data = build_topic249_curriculum()
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

            learning_unit, created = LearningUnit.objects.get_or_create(
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
    print("[SUCCESS] Grade 10 Aviation Topic 249 Ingestion Complete!")
    print(f"[*] Total Lessons Ingested: {total_lessons}")
    print(f"[*] Total Pages/Cards:      {total_pages}")
    print(f"[*] Total Blocks Created:   {total_blocks}")
    print("=" * 80)

if __name__ == "__main__":
    replace_flag = "--replace" in sys.argv
    ingest_grade10_aviation_topic3(replace=replace_flag)
