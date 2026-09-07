"""
VLearn Grade 10 Aviation — Topic 366: Aerodynamics of Flight (Subject ID: 44, Topic ID: 366)
Production Ingestion Engine

Curriculum: CBC (Curriculum ID: 5)
Grade: Grade 10 (Grade ID: 5, Level: 10)
Subject: Aviation (Subject ID: 44)
Topic: Aerodynamics of Flight (Topic ID: 366, Order: 8)

Ingests 5 Comprehensive Learning Units & Lessons (50 Concept Cards):
  1. Airfoil & Lift Generation (Unit order: 0) [10 Cards]
  2. The Four Forces of Flight (Unit order: 1) [10 Cards]
  3. Three Axes of Rotation & Flight Controls (Unit order: 2) [10 Cards]
  4. Aerodynamic Hazards: Stalls (Unit order: 3) [10 Cards]
  5. Wingtip Vortices & Wake Turbulence (Unit order: 4) [10 Cards]

Usage:
  ./venv/bin/python curriculum/ingest_grade10_aviation_topic366.py [--replace]
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
    """Removes bracket citations [88, 89], internal visual prompt text, and normalizes typography."""
    if not text:
        return ""
    # Remove bracket citations e.g. [88], [88, 89], [image_1]
    text = re.sub(r'\[(?:\d+|image_\d+|S\d+.*?|[\d,\s]+)\]', '', text)
    # Remove internal visual generation tags
    text = re.sub(r'\[VISUAL:\s*[^\]]+\]', '', text, flags=re.IGNORECASE)
    # Remove practical task, scenario, and application internal markers
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

def build_topic366_curriculum():
    """Returns the pedagogical page and block structure for Grade 10 Aviation Topic 366."""
    return [
        # =====================================================================
        # LESSON 1: Airfoil & Lift Generation
        # =====================================================================
        {
            "unit_order": 0,
            "unit_name": "Airfoil & Lift Generation",
            "unit_description": "Foundations of aerodynamic lift: understanding airfoil geometry (camber, chord line, leading and trailing edges), relative wind, Angle of Attack, Bernoulli's Principle, and Newton's Third Law.",
            "lesson_title": "Airfoil & Lift Generation",
            "pages": [
                # Card 1 (Page 1): Photographic Hook & Learning Objectives
                [
                    {
                        "type": "suggested_image",
                        "title": "Aerodynamic Airfoil Profile and Lift Streamlines",
                        "content": {
                            "title": "Aerodynamic Airfoil Profile and Lift Streamlines",
                            "caption": "A cross-sectional diagram and physical model of an asymmetric aerodynamic airfoil cutting through oncoming airflow to generate aerodynamic lift.",
                            "resolved_image_url": "https://upload.wikimedia.org/wikipedia/commons/a/a2/Airfoil_lift_and_drag.jpg"
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Learning Focus: Airfoil Anatomy and Lift Dynamics",
                        "content": {
                            "title": "Learning Focus: Airfoil Anatomy and Lift Dynamics",
                            "goals": [
                                "Identify key geometric features of an airfoil: leading edge, trailing edge, chord line, and camber profile.",
                                "Distinguish between relative wind and aircraft pitch attitude.",
                                "Analyze lift generation using both Bernoulli's Principle (pressure differential) and Newton's Third Law (downwash deflection).",
                                "Explain how altering the Angle of Attack affects lift and how wing flaps increase lift at slow speeds."
                            ]
                        }
                    }
                ],
                # Card 2 (Page 2): Key Terminology
                [
                    {
                        "type": "definition_card",
                        "title": "Foundational Aerodynamics Terminology",
                        "content": {
                            "title": "Core Airfoil and Lift Vocabulary",
                            "definitions": [
                                {
                                    "term": "Airfoil",
                                    "definition": "A structure (such as a wing, propeller blade, or rotor blade) designed with a specific curved cross-section to produce an aerodynamic force when moving through the air.",
                                    "example": "The curved cross-sectional shape of an aircraft wing slicing through the atmosphere."
                                },
                                {
                                    "term": "Relative Wind",
                                    "definition": "The direction of oncoming airflow relative to the aircraft wing's motion, moving parallel and directly opposite to the flight path.",
                                    "example": "Air flowing directly toward a climbing aircraft's wings regardless of horizontal ground orientation."
                                },
                                {
                                    "term": "Chord Line",
                                    "definition": "An imaginary straight reference line drawn directly from the leading edge of an airfoil to its trailing edge.",
                                    "example": "Pilots and aerodynamicists measure wing angles relative to this reference line."
                                },
                                {
                                    "term": "Camber",
                                    "definition": "The curvature profile of an airfoil surface; upper camber refers to the top curvature, while lower camber refers to the bottom curvature.",
                                    "example": "An asymmetric wing has high upper camber to accelerate airflow across its upper skin."
                                },
                                {
                                    "term": "Angle of Attack (AOA)",
                                    "definition": "The acute angle formed between the chord line of the airfoil and the direction of the oncoming relative wind.",
                                    "example": "Pitching the nose up increases the Angle of Attack, increasing aerodynamic lift."
                                }
                            ]
                        }
                    }
                ],
                # Card 3 (Page 3): Airfoil Anatomy & Geometry
                [
                    {
                        "type": "concept_explanation",
                        "title": "Anatomy of an Airfoil",
                        "content": {
                            "title": "Geometric Architecture of an Aircraft Wing",
                            "text": "If you cut a wing in half from front to back, you will see its airfoil shape. An airfoil is an engineered structure designed to produce a usable aerodynamic force when moving through air.\n\nKey geometric components include:\n\n- **Leading Edge**: The rounded front edge of the wing that first cuts through the oncoming air.\n- **Trailing Edge**: The thin, tapered rear edge of the wing where upper and lower airflows rejoin.\n- **Chord Line**: An imaginary straight line connecting the leading edge directly to the trailing edge. It acts as the primary geometric baseline for measuring aerodynamic angles.\n- **Camber Profile**: Standard wings feature an asymmetric cross-section. The upper surface has a pronounced, bulged curve (**high upper camber**), while the bottom surface is relatively flat (**low lower camber**).\n\nThis asymmetric profile forces oncoming air molecules to separate and navigate distinctly shaped contours on their journey from the leading edge to the trailing edge."
                        }
                    }
                ],
                # Card 4 (Page 4): Technical Diagram (SVG)
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Airfoil Geometry, Flow Dynamics, and Pressure Gradient",
                        "content": {
                            "title": "Airfoil Anatomy & Lift Generation Diagram",
                            "caption": "A comprehensive aerodynamic schematic showing camber, chord line, leading/trailing edges, Angle of Attack, and the Bernoulli low-pressure suction gradient generating upward lift."
                        }
                    }
                ],
                # Card 5 (Page 5): Lift Physics: Bernoulli vs. Newton
                [
                    {
                        "type": "concept_explanation",
                        "title": "Dual Mechanisms of Lift: Bernoulli and Newton",
                        "content": {
                            "title": "How Physics Lifts Heavy Aircraft",
                            "text": "Lift is not created by a single isolated phenomenon. Instead, it is the result of pressure differentials described by Bernoulli's Principle combined with physical air deflection governed by Newton's Third Law:\n\n- **Bernoulli's Principle (Pressure Suction)**:\n  1. As relative wind meets the leading edge, air traveling over the curved upper camber is forced through a constricted stream tube, accelerating to higher velocity.\n  2. Bernoulli's Principle states that as fluid velocity increases, static pressure decreases. Fast-moving air across the upper surface creates a low-pressure zone.\n  3. Slower-moving air underneath experiences higher static pressure. This vertical pressure imbalance generates an upward suction force—lift.\n\n- **Newton's Third Law (Deflection and Downwash)**:\n  1. As the wing moves forward at an angle of attack, the lower surface physically deflects oncoming air downward.\n  2. Air adhering to the curved top surface (the Coanda effect) is also swept downward off the trailing edge as downwash.\n  3. Newton's Third Law states that every action has an equal and opposite reaction: forcing thousands of kilograms of air downward produces an equal upward reaction on the wing."
                        }
                    }
                ],
                # Card 6 (Page 6): Dynamic Lift Factors Table
                [
                    {
                        "type": "comparison_table",
                        "title": "Key Factors Determining Aerodynamic Lift",
                        "content": {
                            "title": "Aerodynamic Variables Influencing Lift Generation",
                            "headers": ["Variable", "Physical Change", "Impact on Lift", "Operational Significance"],
                            "rows": [
                                ["Airspeed (V)", "Doubling forward velocity", "Increases lift fourfold (Lift scales with V squared)", "Takeoff requires reaching specific rotation speed (Vr)"],
                                ["Angle of Attack (AOA)", "Tilting nose up relative to wind", "Increases lift up to critical stall angle", "Pilot controls climb and descent rates via pitch controls"],
                                ["Air Density (rho)", "High altitude or high temperature", "Decreases lift due to fewer molecules per m³", "Requires longer takeoff run at high-elevation airfields"],
                                ["Camber & Area (S)", "Deploying trailing-edge flaps", "Increases effective camber and wing surface", "Generates high lift at low speeds for safe landings"]
                            ]
                        }
                    }
                ],
                # Card 7 (Page 7): Real-World Application (High-Lift Flaps on Boeing 737)
                [
                    {
                        "type": "real_world_example",
                        "title": "High-Lift Flaps and Slats at Nairobi Airport",
                        "content": {
                            "title": "Camber Transformation During Takeoff and Landing",
                            "text": "If you observe a commercial airliner like a Boeing 737 at Jomo Kenyatta International Airport (JKIA), you will notice that its cruise wings are engineered for high-speed efficiency with relatively thin airfoils.\n\nHowever, during takeoff and landing, aircraft must fly safely at low speeds:\n\n- **Slats Extension**: Leading-edge slats extend forward and downward, smoothing airflow at high angles of attack and delaying separation.\n- **Trailing-Edge Flaps**: Fowler flaps telescope rearward and tilt downward, simultaneously expanding wing surface area and dramatically increasing upper camber.\n- **Operational Advantage**: This artificial increase in camber creates massive low-speed lift, enabling an 80-tonne airliner to land smoothly on Nairobi's runway without stalling at low approach speeds."
                        }
                    }
                ],
                # Card 8 (Page 8): Safety Connection: High-Elevation Operations
                [
                    {
                        "type": "concept_explanation",
                        "title": "Safety Doctrine: High Density Altitude Performance",
                        "content": {
                            "title": "Managing Lift Performance in Thin Mountain Air",
                            "text": "Aerodynamic lift is directly proportional to atmospheric air density. When ambient temperatures rise and airfields sit at high elevations—such as Eldoret or Nakuru in Kenya—the air becomes thin and less dense, a condition known as high density altitude:\n\n- **Aviation Hazard**: Thin air contains fewer air molecules per cubic meter. With fewer molecules striking the lower wing and accelerating over the upper camber, the wing generates significantly less lift at a given true airspeed.\n- **Operational Consequences**: An aircraft takes much longer to accelerate to flying speed, requiring a substantially longer runway distance to achieve liftoff. Climb performance is degraded.\n- **Pilot Action**: Before departure on hot afternoons, pilots consult takeoff performance charts, verify available runway margins, and reduce payload or passenger count to ensure safe clearance over obstacles."
                        }
                    }
                ],
                # Card 9 (Page 9): Educational Video Integration
                [
                    {
                        "type": "suggested_video",
                        "title": "Airfoil Geometry and Aerodynamic Lift Generation",
                        "content": {
                            "title": "AFOQT Exam Prep: Airfoil and Lift Generation",
                            "description": "Watch how oncoming relative wind splits at the leading edge, and observe how velocity differentials, Bernoulli pressure gradients, and angle of attack combine to produce aerodynamic lift.",
                            "url": "https://www.youtube.com/watch?v=dpNCU37z4vU"
                        }
                    }
                ],
                # Card 10 (Page 10): Formative Knowledge Checks & Summary
                [
                    {
                        "type": "knowledge_check",
                        "title": "Diagnostic Check: Angle of Attack Definition",
                        "content": {
                            "question": "What is defined as the acute angle formed between the chord line of an aircraft wing and the direction of the oncoming relative wind?",
                            "options": [
                                "Angle of Incidence",
                                "Angle of Attack (AOA)",
                                "Dihedral Angle",
                                "Pitch Angle"
                            ],
                            "answer": "B",
                            "explanation": "The Angle of Attack (AOA) is the dynamic angle measured between the chord line and the relative wind. The pilot manipulates AOA using the elevator to control the magnitude of lift generated by the wing."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Diagnostic Check: Bernoulli's Principle in Lift Generation",
                        "content": {
                            "question": "According to Bernoulli's Principle, how does the velocity of airflow over a curved upper camber relate to static pressure acting on the wing?",
                            "options": [
                                "As airflow velocity increases, static pressure remains constant",
                                "As airflow velocity decreases, static pressure decreases",
                                "As airflow velocity increases, static pressure decreases, creating an upward lifting force",
                                "High-velocity airflow creates high pressure above the wing, pushing it down"
                            ],
                            "answer": "C",
                            "explanation": "Bernoulli's Principle dictates that an increase in fluid velocity results in a simultaneous decrease in static pressure. Because air accelerates over the curved upper camber, low pressure forms above the wing, allowing higher pressure below to generate lift."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 2: The Four Forces of Flight
        # =====================================================================
        {
            "unit_order": 1,
            "unit_name": "The Four Forces of Flight",
            "unit_description": "Mastering the four primary aerodynamic forces: Lift, Weight, Thrust, and Drag; equilibrium conditions in unaccelerated level flight, climb/descent dynamics, and parasite vs. induced drag.",
            "lesson_title": "The Four Forces of Flight",
            "pages": [
                # Card 1 (Page 1): Photographic Hook & Learning Objectives
                [
                    {
                        "type": "suggested_image",
                        "title": "Light Aircraft Maintaining Stable Cruising Flight",
                        "content": {
                            "title": "Light Aircraft Maintaining Stable Cruising Flight",
                            "caption": "A light general aviation aircraft cruising in straight-and-level unaccelerated flight, maintaining balanced physical equilibrium among Lift, Weight, Thrust, and Drag.",
                            "resolved_image_url": "https://upload.wikimedia.org/wikipedia/commons/8/84/Cessna_172_RG_in_flight_by_Don_Ramey_Logan.jpg"
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Learning Focus: The Four Forces of Flight",
                        "content": {
                            "title": "Learning Focus: The Four Forces of Flight",
                            "goals": [
                                "Identify and describe the four fundamental forces acting on an aircraft: Lift, Weight, Thrust, and Drag.",
                                "Analyze the state of physical equilibrium in straight-and-level unaccelerated cruising flight.",
                                "Explain force transitions during climbing, descending, accelerating, and decelerating flight.",
                                "Distinguish between parasite drag (friction/form) and induced drag (byproduct of lift)."
                            ]
                        }
                    }
                ],
                # Card 2 (Page 2): Key Terminology
                [
                    {
                        "type": "definition_card",
                        "title": "The Four Forces Terminology",
                        "content": {
                            "title": "Core Flight Dynamics Vocabulary",
                            "definitions": [
                                {
                                    "term": "Lift",
                                    "definition": "The upward aerodynamic force generated by the wings that directly opposes the downward pull of gravity.",
                                    "example": "Lift must equal weight to maintain constant cruising altitude."
                                },
                                {
                                    "term": "Weight",
                                    "definition": "The downward gravitational force pulling the mass of the aircraft toward the center of the Earth.",
                                    "example": "Aircraft weight decreases in flight as fuel is consumed by engines."
                                },
                                {
                                    "term": "Thrust",
                                    "definition": "The forward propulsion force produced by engines or propellers that overcomes aerodynamic drag.",
                                    "example": "Turbofan engines produce thousands of pounds of forward thrust."
                                },
                                {
                                    "term": "Drag",
                                    "definition": "The rearward retarding force caused by friction and disruption of airflow opposing the aircraft's forward motion.",
                                    "example": "Streamlined fuselage shapes are designed to minimize total drag."
                                },
                                {
                                    "term": "Equilibrium",
                                    "definition": "A state of balance where all opposing physical forces are equal and opposite, resulting in zero net acceleration.",
                                    "example": "In unaccelerated straight-and-level cruise, Lift equals Weight and Thrust equals Drag."
                                }
                            ]
                        }
                    }
                ],
                # Card 3 (Page 3): The Opposing Pairs of Forces
                [
                    {
                        "type": "concept_explanation",
                        "title": "Opposing Force Pairs in Flight",
                        "content": {
                            "title": "The Four-Way Tug-of-War in the Atmosphere",
                            "text": "Every aircraft in flight is engaged in a continuous, dynamic four-way physical contest among four primary forces acting through its center of gravity:\n\n- **Lift opposes Weight (Vertical Axis)**:\n  - Lift is produced by the aerodynamic design of the wings and angle of attack.\n  - Weight is the gravitational force acting on the total mass of the airplane, fuel, passengers, and cargo.\n  - When Lift equals Weight, the airplane maintains a constant altitude.\n\n- **Thrust opposes Drag (Horizontal Axis)**:\n  - Thrust is generated by the powerplant (propellers, turbofans, or jets) driving the aircraft forward.\n  - Drag is the natural atmospheric resistance that retards forward motion.\n  - When Thrust equals Drag, the airplane maintains a constant airspeed.\n\nIt is a common misconception that Lift must exceed Weight for a plane to maintain level flight. When forces are balanced, the aircraft experiences zero vertical and zero horizontal acceleration."
                        }
                    }
                ],
                # Card 4 (Page 4): Technical Diagram (SVG)
                [
                    {
                        "type": "suggested_diagram",
                        "title": "The Four Forces of Flight Vector Equilibrium Diagram",
                        "content": {
                            "title": "Force Vectors in Unaccelerated Level Flight",
                            "caption": "An aerodynamic force vector schematic showing Lift pointing upward, Weight pointing downward, Thrust pointing forward, and Drag pointing backward in perfect equilibrium."
                        }
                    }
                ],
                # Card 5 (Page 5): Unaccelerated Flight vs. Maneuvering Flight
                [
                    {
                        "type": "concept_explanation",
                        "title": "Equilibrium Dynamics and Flight Transitions",
                        "content": {
                            "title": "How Changing Force Balances Alters Aircraft Flight Paths",
                            "text": "Flight path changes occur when a pilot alters the balance of the four forces:\n\n- **Straight-and-Level Cruise**: Lift = Weight, and Thrust = Drag. The aircraft maintains constant altitude and constant airspeed.\n- **Initiating a Climb**: The pilot momentarily increases engine power and pitches up, creating excess thrust and a temporary surplus in vertical force. Once stabilized in a constant-speed climb, the forces rebalance into a steady state with tilted vectors.\n- **Accelerating Flight**: When the pilot advances the throttle, Thrust exceeds Drag. The aircraft accelerates. Higher airspeed increases airflow over the wings, which automatically increases Lift. To avoid climbing, the pilot must trim the nose slightly down to reduce Angle of Attack, establishing a new equilibrium at higher speed.\n- **Decelerating Flight**: Reducing throttle causes Drag to exceed Thrust. The airplane decelerates until the forces match at the new lower speed."
                        }
                    }
                ],
                # Card 6 (Page 6): Parasite Drag vs. Induced Drag Table
                [
                    {
                        "type": "comparison_table",
                        "title": "Aerodynamic Drag Classification: Parasite vs. Induced",
                        "content": {
                            "title": "Differentiating Parasite and Induced Drag Components",
                            "headers": ["Drag Category", "Physical Origin", "Airspeed Relationship", "Design Minimization Technique"],
                            "rows": [
                                ["Form Drag (Parasite)", "Airflow resistance against bluff shapes (fuselage, struts)", "Increases with the square of speed (V squared)", "Streamlined fairings and aerodynamic tear-drop profiles"],
                                ["Skin Friction (Parasite)", "Microscopic friction between air and metal skin", "Increases with the square of speed (V squared)", "Flush rivets, smooth composite skins, and polished paint"],
                                ["Interference Drag (Parasite)", "Eddies where structures meet (wing root to fuselage)", "Increases with the square of speed (V squared)", "Aerodynamic wing fillets and fairings"],
                                ["Induced Drag", "Byproduct of lift generation and wingtip vortices", "Decreases as airspeed increases (highest at slow speeds)", "High aspect-ratio wings and vertical winglets"]
                            ]
                        }
                    }
                ],
                # Card 7 (Page 7): Real-World Application (Regional Jet Streamlining)
                [
                    {
                        "type": "real_world_example",
                        "title": "Streamlining and Fuel Efficiency in Commercial Aviation",
                        "content": {
                            "title": "Reducing Parasite Drag on Modern Regional Airliners",
                            "text": "In commercial aviation, fuel represents up to 35% of total operating expenses. Minimizing aerodynamic drag directly reduces the thrust required, saving millions of liters of jet fuel annually.\n\nOn modern airliners such as the Bombardier CRJ-900 operated across East Africa:\n\n- **Flush Riveting**: Thousands of exterior rivets are installed flush with the aluminum skin, creating an ultra-smooth boundary layer that minimizes skin friction drag.\n- **Aerodynamic Fairings**: Landing gear assemblies retract fully into enclosed wheel wells covered by mechanical doors to eliminate tremendous form drag during cruise.\n- **Wing-Fuselage Fairings**: Smooth curved fillets are built where the wings join the fuselage, smoothing turbulent boundary layer interference."
                        }
                    }
                ],
                # Card 8 (Page 8): Safety Connection: In-Flight Structural Icing
                [
                    {
                        "type": "concept_explanation",
                        "title": "Safety Doctrine: Structural Icing and Force Disruption",
                        "content": {
                            "title": "Catastrophic Force Imbalance Caused by Airframe Icing",
                            "text": "When flying through cold clouds containing supercooled water droplets, ice can rapidly accumulate on the leading edges of wings, tailplanes, and propellers:\n\n- **Disruption of Lift**: A layer of rough ice as thin as coarse sandpaper disrupts the smooth boundary layer over the upper camber, reducing maximum lift by up to 30%.\n- **Explosion of Drag**: Ice accretion creates severe form and friction drag, increasing total aircraft drag by up to 100% to 300%.\n- **Addition of Weight**: The physical weight of accumulated ice adds hundreds of kilograms of downward force.\n- **Thrust Deficit**: Engine propellers may collect ice, degrading thrust efficiency. The aircraft may no longer produce enough thrust to overcome drag or enough lift to support weight, causing an uncommanded descent.\n- **Pilot Action**: Pilots immediately activate pneumatic de-icing boots or thermal anti-ice systems and exit the icing cloud layer by climbing, descending, or diverting."
                        }
                    }
                ],
                # Card 9 (Page 9): Educational Video Integration
                [
                    {
                        "type": "suggested_video",
                        "title": "The Four Forces of Flight Explained Simply",
                        "content": {
                            "title": "Principles of Flight: Lift, Weight, Thrust, and Drag",
                            "description": "Examine how the four fundamental aerodynamic forces interact, observe animated vector balances during unaccelerated cruising flight, and see how thrust and drag shifts produce climbs and descents.",
                            "url": "https://www.youtube.com/watch?v=imDKWTt5cfk"
                        }
                    }
                ],
                # Card 10 (Page 10): Formative Knowledge Checks & Summary
                [
                    {
                        "type": "knowledge_check",
                        "title": "Diagnostic Check: Equilibrium in Level Cruising Flight",
                        "content": {
                            "question": "When an aircraft is in steady, straight-and-level, unaccelerated flight, what is the exact physical relationship between the four forces?",
                            "options": [
                                "Lift is twice the weight, and Thrust is twice the drag",
                                "Lift equals Weight, and Thrust equals Drag",
                                "Thrust must be greater than Drag, and Lift must be greater than Weight",
                                "Lift is less than Weight, and Thrust is less than Drag"
                            ],
                            "answer": "B",
                            "explanation": "In unaccelerated straight-and-level flight, the aircraft is in a state of static equilibrium: net acceleration is zero. Therefore, opposing forces must be equal in magnitude: Lift equals Weight, and Thrust equals Drag."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Diagnostic Check: Parasite Drag Definition",
                        "content": {
                            "question": "What type of aerodynamic resistance is caused by the physical friction and structural form of the aircraft moving through air, independent of lift creation?",
                            "options": [
                                "Induced Drag",
                                "Friction Lift",
                                "Parasite Drag",
                                "Thrust Drag"
                            ],
                            "answer": "C",
                            "explanation": "Parasite drag comprises all aerodynamic resistance not associated with lift creation, including skin friction from air flowing across the skin, form drag caused by the aircraft's shape, and interference drag at structural junctions."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 3: Three Axes of Rotation & Flight Controls
        # =====================================================================
        {
            "unit_order": 2,
            "unit_name": "Three Axes of Rotation & Flight Controls",
            "unit_description": "Aircraft rotations in 3D space: Longitudinal (Roll/Ailerons), Lateral (Pitch/Elevator), and Vertical (Yaw/Rudder) axes; control surface deflections and coordinated cockpit inputs.",
            "lesson_title": "Three Axes of Rotation & Flight Controls",
            "pages": [
                # Card 1 (Page 1): Photographic Hook & Learning Objectives
                [
                    {
                        "type": "suggested_image",
                        "title": "Aircraft Primary Flight Control Surfaces and Cockpit Inputs",
                        "content": {
                            "title": "Aircraft Primary Flight Control Surfaces and Cockpit Inputs",
                            "caption": "A light aircraft showing hinged flight control surfaces (ailerons, elevator, and rudder) that deflect airflow to rotate the plane around its three axes.",
                            "resolved_image_url": "https://upload.wikimedia.org/wikipedia/commons/0/02/Aircraft_controls_%2816436200715%29.jpg"
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Learning Focus: Three Rotational Axes and Flight Controls",
                        "content": {
                            "title": "Learning Focus: Three Rotational Axes and Flight Controls",
                            "goals": [
                                "Identify the three mutually perpendicular axes of aircraft rotation intersecting at the Center of Gravity (CG).",
                                "Pair each rotational movement (Roll, Pitch, Yaw) with its respective axis and primary flight control surface.",
                                "Explain the aerodynamic deflection mechanism by which ailerons, elevators, and rudders exert rotational moments.",
                                "Describe how pilots coordinate yoke and rudder pedal inputs to execute coordinated banking turns."
                            ]
                        }
                    }
                ],
                # Card 2 (Page 2): Key Terminology
                [
                    {
                        "type": "definition_card",
                        "title": "Flight Controls and Axes Terminology",
                        "content": {
                            "title": "Core Flight Dynamics Vocabulary",
                            "definitions": [
                                {
                                    "term": "Center of Gravity (CG)",
                                    "definition": "The theoretical point where an aircraft's total weight is concentrated and balanced, serving as the pivot point for all rotational motions.",
                                    "example": "All rotations around pitch, roll, and yaw occur through the aircraft's center of gravity."
                                },
                                {
                                    "term": "Longitudinal Axis & Roll",
                                    "definition": "The imaginary line extending from the nose to the tail of the aircraft; rotation around it is called roll, controlled by ailerons.",
                                    "example": "Turning the control yoke rolls the wings side to side around the longitudinal axis."
                                },
                                {
                                    "term": "Lateral Axis & Pitch",
                                    "definition": "The imaginary horizontal line running from wingtip to wingtip; rotation around it is called pitch, controlled by the elevator.",
                                    "example": "Pulling back on the yoke pitches the aircraft's nose upward around the lateral axis."
                                },
                                {
                                    "term": "Vertical Axis & Yaw",
                                    "definition": "The imaginary line passing vertically through the Center of Gravity; rotation around it is called yaw, controlled by the rudder.",
                                    "example": "Depressing the left rudder pedal yaws the nose to the left around the vertical axis."
                                },
                                {
                                    "term": "Ailerons",
                                    "definition": "Hinged primary flight control surfaces located on the outer trailing edges of wings that move differentially to produce roll.",
                                    "example": "When the left aileron hinges up, the right aileron hinges down."
                                }
                            ]
                        }
                    }
                ],
                # Card 3 (Page 3): The Three Axes Described
                [
                    {
                        "type": "concept_explanation",
                        "title": "The Three Mutually Perpendicular Axes",
                        "content": {
                            "title": "Navigating Three-Dimensional Airspace",
                            "text": "Unlike ground vehicles that maneuver only across a two-dimensional surface, an airplane moves through 3D space. It rotates around three imaginary axes that intersect at its Center of Gravity (CG):\n\n1. **The Longitudinal Axis (Nose to Tail)**:\n   - **Movement**: **Roll** (banking the wings side-to-side).\n   - **Control Surface**: **Ailerons** mounted on outer wing trailing edges.\n   - **Cockpit Input**: Turning the control yoke or moving the control stick left or right.\n\n2. **The Lateral Axis (Wingtip to Wingtip)**:\n   - **Movement**: **Pitch** (tilting the nose up or down).\n   - **Control Surface**: **Elevator** mounted on the horizontal stabilizer.\n   - **Cockpit Input**: Pushing the yoke forward (nose down) or pulling it backward (nose up).\n\n3. **The Vertical Axis (Top to Bottom through CG)**:\n   - **Movement**: **Yaw** (swinging the nose left or right).\n   - **Control Surface**: **Rudder** mounted on the vertical stabilizer.\n   - **Cockpit Input**: Pressing the left or right foot rudder pedals on the cockpit floor."
                        }
                    }
                ],
                # Card 4 (Page 4): Technical Diagram (SVG)
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Aircraft Rotational Axes and Primary Flight Control Surfaces",
                        "content": {
                            "title": "Aircraft 3 Axes & Flight Controls Diagram",
                            "caption": "An isometric engineering diagram illustrating the Longitudinal, Lateral, and Vertical axes intersecting at the Center of Gravity, with paired control surfaces and rotational movements."
                        }
                    }
                ],
                # Card 5 (Page 5): Aerodynamic Deflection and Moment Arms
                [
                    {
                        "type": "concept_explanation",
                        "title": "How Control Surfaces Deflect Airflow",
                        "content": {
                            "title": "Aerodynamic Deflection and Moment Arm Leverage",
                            "text": "Flight control surfaces are movable hinged airfoils. When deflected into the slipstream, they alter the camber and local angle of attack, creating an aerodynamic force that pivots the plane:\n\n- **Roll Dynamics (Differential Ailerons)**:\n  - Turning the yoke left raises the left aileron upward and lowers the right aileron downward.\n  - The lowered right aileron increases camber and lift, lifting the right wing.\n  - The raised left aileron decreases camber and lift, dropping the left wing. The airplane rolls left.\n\n- **Pitch Dynamics (Elevator Leverage)**:\n  - Pulling the control yoke backward hinges the elevator upward.\n  - Deflecting air upward creates a downward aerodynamic force on the tail.\n  - Because the tail is far behind the Center of Gravity, this downward force acts through a long moment arm, tilting the tail down and pitching the nose upward.\n\n- **Yaw Dynamics (Rudder Deflection)**:\n  - Stepping on the right rudder pedal hinges the rudder to the right.\n  - Oncoming air deflects rightward, pushing the tail fin to the left.\n  - Pivoting around the CG, the nose swings (yaws) toward the right."
                        }
                    }
                ],
                # Card 6 (Page 6): Axes and Controls Matrix Table
                [
                    {
                        "type": "comparison_table",
                        "title": "Rotational Axes, Motion Types, and Flight Control Inputs",
                        "content": {
                            "title": "The Flight Control Surface and Axes Matrix",
                            "headers": ["Axis of Rotation", "Directional Orientation", "Rotational Motion", "Primary Control Surface", "Cockpit Pilot Input"],
                            "rows": [
                                ["Longitudinal Axis", "Nose to tail through fuselage", "Roll (wing bank)", "Ailerons (wing trailing edge)", "Rotate control yoke or move stick left/right"],
                                ["Lateral Axis", "Wingtip to wingtip horizontally", "Pitch (nose up/down)", "Elevator (horizontal tail)", "Push yoke forward (down) / pull yoke back (up)"],
                                ["Vertical Axis", "Top of cabin straight down through CG", "Yaw (nose left/right)", "Rudder (vertical tail fin)", "Press left or right foot rudder pedals"]
                            ]
                        }
                    }
                ],
                # Card 7 (Page 7): Real-World Application (Mechanical Linkages in Cessna 172)
                [
                    {
                        "type": "real_world_example",
                        "title": "Mechanical Control Linkages in Training Aircraft",
                        "content": {
                            "title": "Cables, Pulleys, and Pushrods in General Aviation",
                            "text": "If you look inside the wing and tail inspection panels of a Cessna 172 light trainer, you will see a network of stainless steel control cables, precision pulleys, bellcranks, and pushrods:\n\n- **Mechanical Interlock**: The ailerons are interconnected by a continuous loop of tensioned control cables. When the pilot turns the yoke left, cables simultaneously pull the left aileron bellcrank up and the right bellcrank down.\n- **Direct Tactile Feedback**: In light training aircraft, there are no hydraulic boosters or electronic computers between the pilot and the surfaces. The air rushing across the ailerons exerts physical resistance directly back to the pilot's hands on the yoke.\n- **Control Rigidity**: Pre-flight inspection requires the pilot to verify full, free, and correct movement of every surface to ensure cables are seated and no foreign objects jam the linkages."
                        }
                    }
                ],
                # Card 8 (Page 8): Safety Connection: Jammed Flight Controls
                [
                    {
                        "type": "concept_explanation",
                        "title": "Safety Doctrine: Pre-Flight Flight Control Checks",
                        "content": {
                            "title": "Verifying Flight Control Integrity Before Departure",
                            "text": "Before every takeoff, aviation regulations mandate that pilots perform a thorough 'Full and Free' flight control verification:\n\n- **The Operational Hazard**: A control cable can become frayed, a gust lock can accidentally be left installed on the tail, or a loose maintenance tool can jam a control bellcrank inside the wing.\n- **The In-Flight Risk**: If an aileron jams in flight, the pilot will lose the ability to level the wings. If an elevator jams in a nose-down position, the aircraft will dive toward the ground with no pitch recovery mechanism.\n- **Correct Procedure**: While stationary on the ramp before engine run-up, the pilot moves the control yoke to its full forward, backward, left, and right stops, while looking out the window to visually verify that the left aileron goes up when turning left, the right aileron goes up when turning right, and the elevator moves upward when pulling back."
                        }
                    }
                ],
                # Card 9 (Page 9): Educational Video Integration
                [
                    {
                        "type": "suggested_video",
                        "title": "The Three Axes of Rotation on an Aircraft",
                        "content": {
                            "title": "Yaw, Pitch, and Roll Flight Dynamics Demonstration",
                            "description": "Watch real cockpit control inputs translate into external surface movements, showing how aileron, elevator, and rudder deflections rotate the airplane around its three axes.",
                            "url": "https://www.youtube.com/watch?v=53rzgOpFnIs"
                        }
                    }
                ],
                # Card 10 (Page 10): Formative Knowledge Checks & Summary
                [
                    {
                        "type": "knowledge_check",
                        "title": "Diagnostic Check: Rotational Axes Identification",
                        "content": {
                            "question": "Which imaginary axis runs from the nose of the aircraft to the tail, and what is the name of the rotational movement that occurs around it?",
                            "options": [
                                "Lateral Axis; Pitch",
                                "Vertical Axis; Yaw",
                                "Longitudinal Axis; Roll",
                                "Horizontal Axis; Slide"
                            ],
                            "answer": "C",
                            "explanation": "The Longitudinal Axis extends through the aircraft from nose to tail. Rotational movement around this axis is called Roll (banking the wings), which is controlled primarily by the ailerons."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Diagnostic Check: Pitch Control Input and Surface Deflection",
                        "content": {
                            "question": "If a pilot wishes to pitch the nose of an aircraft downward, what cockpit control input must they apply, and which control surface moves in what direction?",
                            "options": [
                                "Push the control wheel forward; the elevator moves downward",
                                "Pull the control wheel backward; the rudder moves to the left",
                                "Turn the control wheel left; the left aileron moves upward",
                                "Step on the right rudder pedal; the horizontal stabilizer rotates"
                            ],
                            "answer": "A",
                            "explanation": "Pushing the control wheel forward hinges the elevator downward. This increases camber at the tail, generating upward aerodynamic lift at the horizontal stabilizer. Pivoting about the CG, this lifts the tail and pitches the nose down."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 4: Aerodynamic Hazards: Stalls
        # =====================================================================
        {
            "unit_order": 3,
            "unit_name": "Aerodynamic Hazards: Stalls",
            "unit_description": "Critical aerodynamics: defining aerodynamic stalls, critical angle of attack (15°-18°), boundary layer separation, cockpit stall warnings, and the universal 3-step recovery procedure.",
            "lesson_title": "Aerodynamic Hazards: Stalls",
            "pages": [
                # Card 1 (Page 1): Photographic Hook & Learning Objectives
                [
                    {
                        "type": "suggested_image",
                        "title": "High Angle of Attack Airflow Separation and Vapor Condensation",
                        "content": {
                            "title": "High Angle of Attack Airflow Separation and Vapor Condensation",
                            "caption": "A high-performance aircraft maneuvering at high Angle of Attack, showing intense boundary layer condensation and vortex separation across the lifting surfaces.",
                            "resolved_image_url": "https://upload.wikimedia.org/wikipedia/commons/a/a8/FA-18C_vapor_LEX_and_wingtip_1.jpg"
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Learning Focus: Aerodynamic Stalls and Recovery",
                        "content": {
                            "title": "Learning Focus: Aerodynamic Stalls and Recovery",
                            "goals": [
                                "Define an aerodynamic stall and dispel the misconception that stalls are caused by engine failure.",
                                "Identify the Critical Angle of Attack (typically 15° to 18°) as the sole direct trigger of a stall.",
                                "Describe the physical mechanism of boundary layer separation and turbulent wake formation over the upper camber.",
                                "Recognize cockpit stall warning indicators and execute the universal 3-step stall recovery procedure."
                            ]
                        }
                    }
                ],
                # Card 2 (Page 2): Key Terminology
                [
                    {
                        "type": "definition_card",
                        "title": "Stall Dynamics Terminology",
                        "content": {
                            "title": "Core Aerodynamic Stall Vocabulary",
                            "definitions": [
                                {
                                    "term": "Aerodynamic Stall",
                                    "definition": "A sudden, drastic reduction in lift caused by the separation of airflow from the wing's upper surface when the critical angle of attack is exceeded.",
                                    "example": "A stalled wing can no longer support aircraft weight, causing a rapid descent."
                                },
                                {
                                    "term": "Critical Angle of Attack",
                                    "definition": "The specific angle of attack (typically 15° to 18° for subsonic airfoils) beyond which airflow separates and maximum lift coefficient collapses.",
                                    "example": "Exceeding 16° AOA causes immediate boundary layer tearing and stall."
                                },
                                {
                                    "term": "Boundary Layer",
                                    "definition": "The thin layer of air immediately adjacent to the aircraft skin that is slowed down by surface viscosity and friction.",
                                    "example": "Maintaining a smooth, attached boundary layer is essential for lift generation."
                                },
                                {
                                    "term": "Airflow Separation",
                                    "definition": "The physical detachment of the boundary layer from the airfoil surface, creating a turbulent, low-energy wake.",
                                    "example": "At high AOA, airflow separates near the trailing edge and moves forward toward the leading edge."
                                },
                                {
                                    "term": "Stick Shaker & Buffet",
                                    "definition": "Tactile warning sensations indicating an impending stall, caused by turbulent wake buffet on the tail or an automated cockpit motor shaking the yoke.",
                                    "example": "The stick shaker vibrates violently 5 to 10 knots above the actual stall speed."
                                }
                            ]
                        }
                    }
                ],
                # Card 3 (Page 3): The True Cause of a Stall
                [
                    {
                        "type": "concept_explanation",
                        "title": "The Single Universal Cause of an Aerodynamic Stall",
                        "content": {
                            "title": "Dispelling the Low Speed and Engine Failure Myths",
                            "text": "Among student pilots and the general public, two persistent misconceptions exist regarding stalls:\n\n1. **Myth 1: Stalls are caused by engine failure.**\n   - *Fact*: Gliders have no engines, yet they fly safely for hours. Conversely, an aircraft with engines roaring at 100% full power will stall immediately if pitched up excessively.\n2. **Myth 2: Stalls only occur at slow flight speeds.**\n   - *Fact*: While stalls frequently occur during slow flight (such as during landing approaches), an aircraft can be stalled at 250 knots during an abrupt, aggressive high-G pull-up.\n\n**The Universal Aerodynamic Law**: An aircraft wing stalls for one reason and one reason only—**exceeding the Critical Angle of Attack (AOA)**.\n\nRegardless of airspeed, engine power, gross weight, or bank angle, whenever the acute angle between the wing's chord line and the relative wind exceeds the critical limit (typically 15° to 18°), the wing stalls."
                        }
                    }
                ],
                # Card 4 (Page 4): Technical Diagram (SVG)
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Stall Dynamics: Increasing Angle of Attack & Airflow Separation",
                        "content": {
                            "title": "Aerodynamic Stall & Boundary Layer Separation",
                            "caption": "A comparative aerodynamic schematic contrasting attached laminar flow at 5° AOA with catastrophic boundary layer detachment, turbulent eddy formation, and loss of lift at 22° AOA."
                        }
                    }
                ],
                # Card 5 (Page 5): The Physics of Airflow Separation
                [
                    {
                        "type": "concept_explanation",
                        "title": "Boundary Layer Separation Physics",
                        "content": {
                            "title": "How Airflow Detaches from the Upper Camber",
                            "text": "Understanding what happens along the upper skin of the wing during an approaching stall reveals why lift collapses so quickly:\n\n1. **Low Angle of Attack (Normal Cruise, ~4° - 6°)**:\n   - Streamlines hug the curved upper camber smoothly.\n   - The boundary layer remains firmly attached from leading edge to trailing edge.\n   - Suction is uniform, drag is low, and ample lift is generated.\n\n2. **Approaching Critical Angle (~12° - 15°)**:\n   - As the wing pitches up, air molecules must overcome a steep adverse pressure gradient to remain attached.\n   - The boundary layer begins to slow down near the trailing edge and bubble upward.\n\n3. **Exceeding the Critical Angle (>18°)**:\n   - The kinetic energy of the boundary layer is insufficient to follow the extreme curvature.\n   - Airflow separates completely from the upper skin, breaking into chaotic, swirling turbulent vortices.\n   - Lift plummets by up to 70-80% in milliseconds, while drag increases drastically, causing the aircraft to sink rapidly."
                        }
                    }
                ],
                # Card 6 (Page 6): Stall Warning Indicators Table
                [
                    {
                        "type": "comparison_table",
                        "title": "Stall Warning Systems and Physiological Cues",
                        "content": {
                            "title": "Cockpit Indicators of an Impending Aerodynamic Stall",
                            "headers": ["Indicator Type", "Physical Origin", "Cockpit Cue / Sensation", "Pilot Action Required"],
                            "rows": [
                                ["Aerodynamic Buffeting", "Turbulent wing wake striking horizontal stabilizer", "Physical vibration of the airframe and floorboards", "Recognize stall onset; immediately reduce AOA"],
                                ["Flight Control Mushiness", "Reduced dynamic airflow velocity over ailerons", "Sluggish, unresponsive feel in control yoke", "Acknowledge low-energy state; avoid abrupt rolls"],
                                ["Acoustic Warning Horn", "Suction reed switch on leading edge activated at high AOA", "Continuous loud high-pitched horn in cockpit", "Lower the nose immediately before full stall"],
                                ["Mechanical Stick Shaker", "Angle of attack sensor triggers unbalance electric motor", "Violent tactile vibration of pilot's control yoke", "Push yoke forward; apply full engine power"]
                            ]
                        }
                    }
                ],
                # Card 7 (Page 7): Real-World Application (Stall Training at Flight School)
                [
                    {
                        "type": "real_world_example",
                        "title": "Controlled Stall Training in Flight Training",
                        "content": {
                            "title": "Practicing Stall Recognition and Recovery in General Aviation",
                            "text": "Every pilot licensed by the Kenya Civil Aviation Authority (KCAA) must master intentional stalls during flight training at airfields like Wilson or Malindi:\n\n- **Safety Altitude**: Stall practice is conducted at a safe operational altitude, typically above 3,000 feet above ground level, ensuring adequate recovery airspace.\n- **Power-Off Stall (Landing Simulation)**:\n  1. The student throttles the engine to idle and gently raises the nose to hold altitude as airspeed bleeds away.\n  2. The stall warning horn sounds. The controls feel soft and mushy.\n  3. At the stall break, the nose drops abruptly and a shudder passes through the airframe.\n- **Muscle Memory Recovery**: The student immediately pushes the yoke forward to break the stall, levels the wings with rudder and ailerons, and advances the throttle to full power, recovering with minimal altitude loss."
                        }
                    }
                ],
                # Card 8 (Page 8): The Universal 3-Step Stall Recovery Procedure
                [
                    {
                        "type": "concept_explanation",
                        "title": "The Universal 3-Step Stall Recovery Procedure",
                        "content": {
                            "title": "The Standard Operating Procedure for Stall Recovery",
                            "text": "When an aircraft stalls, the pilot must execute three standardized recovery steps in exact sequence without panic:\n\n1. **Step 1: Reduce the Angle of Attack (PUSH YOKE FORWARD)**:\n   - *The Single Most Critical Step*: Lowering the nose reduces the angle of attack below the critical limit.\n   - Relative wind immediately reattaches smoothly across the upper camber, restoring lift in a fraction of a second.\n   - *Caution*: Pulling back on the yoke in panic deepens the stall and can trigger an unrecoverable spin.\n\n2. **Step 2: Roll Wings Level (COORDINATE AILERONS & RUDDER)**:\n   - Level the wings using coordinated rudder and aileron inputs to ensure total lift is oriented vertically upward rather than banked sideways.\n\n3. **Step 3: Apply Maximum Smooth Power (ADVANCE THROTTLE)**:\n   - Smoothly advance the throttle to full forward power to minimize altitude loss and accelerate the airplane safely away from stall speed."
                        }
                    }
                ],
                # Card 9 (Page 9): Educational Video Integration
                [
                    {
                        "type": "suggested_video",
                        "title": "Airflow Behavior During a Flight Stall Demonstration",
                        "content": {
                            "title": "What Happens to Airflow During a Stall? Flight Training",
                            "description": "Observe real-time tuft testing on an aircraft wing as increasing Angle of Attack leads to boundary layer detachment, wild tuft fluttering, and sudden loss of lift.",
                            "url": "https://www.youtube.com/watch?v=xxLNVRxNJZA"
                        }
                    }
                ],
                # Card 10 (Page 10): Formative Knowledge Checks & Summary
                [
                    {
                        "type": "knowledge_check",
                        "title": "Diagnostic Check: Primary Cause of an Aerodynamic Stall",
                        "content": {
                            "question": "What is the primary physical cause of an aerodynamic stall in all fixed-wing aircraft?",
                            "options": [
                                "Complete mechanical failure of the propulsion engine",
                                "Flying at an altitude higher than the aircraft's service ceiling",
                                "Exceeding the critical angle of attack of the wing",
                                "Flying too fast in turbulent convective weather conditions"
                            ],
                            "answer": "C",
                            "explanation": "An aerodynamic stall is caused exclusively by exceeding the critical angle of attack. When this angle is exceeded, smooth airflow tears away from the upper camber, causing an immediate collapse of lift."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Diagnostic Check: Primary Stall Recovery Action",
                        "content": {
                            "question": "What is the first and most critical action a pilot must take to recover from an aerodynamic stall?",
                            "options": [
                                "Pull back on the control wheel to climb away from the ground",
                                "Turn on the auxiliary fuel pump and cycle the engine ignition",
                                "Reduce the angle of attack by pushing the control wheel forward to lower the nose",
                                "Roll the aircraft into a steep bank to turn away from obstacles"
                            ],
                            "answer": "C",
                            "explanation": "To recover from any stall, airflow must reattach to the upper surface of the wing. The only way to achieve this is to reduce the Angle of Attack below the critical limit by pushing the control yoke forward."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 5: Wingtip Vortices & Wake Turbulence
        # =====================================================================
        {
            "unit_order": 4,
            "unit_name": "Wingtip Vortices & Wake Turbulence",
            "unit_description": "Aviation wake turbulence: generation of counter-rotating wingtip vortices, 'Heavy, Clean, and Slow' maximum strength configuration, vortex sinking/drift dynamics, and ATC separation criteria.",
            "lesson_title": "Wingtip Vortices & Wake Turbulence",
            "pages": [
                # Card 1 (Page 1): Photographic Hook & Learning Objectives
                [
                    {
                        "type": "suggested_image",
                        "title": "Wingtip Vortex Generation Trailing an Aircraft",
                        "content": {
                            "title": "Wingtip Vortex Generation Trailing an Aircraft",
                            "caption": "A flight demonstration revealing energetic counter-rotating wingtip vortices spiraling backward from the outer edges of the lifting wings.",
                            "resolved_image_url": "https://upload.wikimedia.org/wikipedia/commons/f/fe/Airplane_vortex_edit.jpg"
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Learning Focus: Wingtip Vortices and Wake Turbulence",
                        "content": {
                            "title": "Learning Focus: Wingtip Vortices and Wake Turbulence",
                            "goals": [
                                "Explain the aerodynamic pressure differential mechanism that creates counter-rotating wingtip vortices.",
                                "Identify the aircraft configuration producing the most hazardous wake turbulence: Heavy, Clean, and Slow.",
                                "Describe the three-dimensional sinking and crosswind drifting behaviors of wake turbulence funnels.",
                                "Apply standard ATC runway separation rules and pilot avoidance flight paths during takeoff and landing."
                            ]
                        }
                    }
                ],
                # Card 2 (Page 2): Key Terminology
                [
                    {
                        "type": "definition_card",
                        "title": "Wake Turbulence Terminology",
                        "content": {
                            "title": "Core Vortex and Turbulence Vocabulary",
                            "definitions": [
                                {
                                    "term": "Wingtip Vortices",
                                    "definition": "Tightly spinning, counter-rotating funnels of high-energy air generated at the tips of an aircraft's wings whenever lift is being produced.",
                                    "example": "High-pressure air under the wing wraps around the tip toward the low-pressure upper surface."
                                },
                                {
                                    "term": "Wake Turbulence",
                                    "definition": "The hazardous turbulent atmosphere left behind an aircraft in flight, primarily consisting of its descending wingtip vortices.",
                                    "example": "A light trainer encountering the wake of a heavy jet can suffer an uncommanded roll."
                                },
                                {
                                    "term": "Heavy, Clean, and Slow",
                                    "definition": "The flight configuration that produces the strongest wake vortices: heavy gross weight, flaps/gear retracted (clean), and slow speed (high AOA).",
                                    "example": "A fully loaded Boeing 777 immediately following rotation generates peak vortex intensity."
                                },
                                {
                                    "term": "Vortex Sinking",
                                    "definition": "The downward descent of wake vortices behind an aircraft at a rate of 400 to 500 feet per minute, leveling off about 900 feet below the flight path.",
                                    "example": "Vortices sink into the approach corridor below a descending jet."
                                },
                                {
                                    "term": "Winglets",
                                    "definition": "Vertical or angled aerodynamic wingtip extensions designed to disrupt wingtip vortex roll, reducing induced drag and wake turbulence.",
                                    "example": "Turned-up winglets on a Boeing 737 reduce drag and fuel burn."
                                }
                            ]
                        }
                    }
                ],
                # Card 3 (Page 3): How Wingtip Vortices Form
                [
                    {
                        "type": "concept_explanation",
                        "title": "The Aerodynamic Genesis of Wingtip Vortices",
                        "content": {
                            "title": "Fluid Dynamics at the Wingtips",
                            "text": "Whenever an aircraft wing produces aerodynamic lift, a fundamental pressure differential exists:\n\n1. **Pressure Differential**: Air across the upper camber is at lower pressure, while air underneath the wing is at higher pressure.\n2. **The Lateral Escape Path**: Air is a fluid and naturally moves from regions of high pressure toward regions of low pressure. While the solid wing surface prevents vertical mixing across the span, at the outer wingtip there is no physical barrier.\n3. **Outward and Upward Roll**: High-pressure air beneath the wing curls outward past the tip, curls upward over the upper surface, and rushes into the low-pressure zone.\n4. **Counter-Rotating Funnels**: As the aircraft flies forward, this continuous curling action generates two horizontal, tightly spinning tornadoes trailing behind the aircraft:\n   - The **left wingtip vortex** rotates **clockwise** (viewed from behind).\n   - The **right wingtip vortex** rotates **counter-clockwise** (viewed from behind)."
                        }
                    }
                ],
                # Card 4 (Page 4): Technical Diagram (SVG)
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Wingtip Vortices Formation, Wake Turbulence & Separation Matrix",
                        "content": {
                            "title": "Wake Turbulence Dynamics & Avoidance Matrix",
                            "caption": "An engineering schematic illustrating counter-rotating wingtip vortex funnels sinking behind a heavy transport jet, vortex drift dynamics, and safe flight paths for trailing aircraft."
                        }
                    }
                ],
                # Card 5 (Page 5): Factors Governing Vortex Strength
                [
                    {
                        "type": "concept_explanation",
                        "title": "The 'Heavy, Clean, and Slow' Principle",
                        "content": {
                            "title": "Why Heavy Transports Generate the Most Lethal Vortices",
                            "text": "The strength of wake vortices depends directly on the amount of lift being generated and the concentration of that lift across the wingtips. Maximum vortex energy is produced when an aircraft is **Heavy, Clean, and Slow**:\n\n- **Heavy**: A massive 400-tonne airliner like a Boeing 777 or Airbus A350 requires immense total lift to remain airborne. Greater lift requires a much higher pressure differential, which violently accelerates the roll of air at the wingtips.\n- **Clean**: When wing flaps and slats are retracted ('clean' configuration), lift is concentrated heavily toward the outer wingtips rather than spread evenly across the inboard wing span, creating much tighter, more energetic vortex cores.\n- **Slow**: Flying at slow airspeeds (such as immediately after takeoff rotation) requires the aircraft to fly at a high Angle of Attack. High AOA maximizes the pressure disparity between upper and lower surfaces, generating peak wake vortex strength."
                        }
                    }
                ],
                # Card 6 (Page 6): Vortex Behavior and Sinking Characteristics
                [
                    {
                        "type": "comparison_table",
                        "title": "Vortex Behavior: Sinking, Drift, and Dissipation Dynamics",
                        "content": {
                            "title": "Behavioral Characteristics of Atmospheric Wake Vortices",
                            "headers": ["Dynamic Behavior", "Rate / Measurement", "Physical Consequence", "Pilot Operational Safeguard"],
                            "rows": [
                                ["Vertical Descent", "400 to 500 feet per minute", "Vortices sink beneath generating aircraft, leveling off 800-1000 ft below", "Stay on or above the glide path of a preceding large aircraft"],
                                ["Crosswind Lateral Drift", "3 to 5 knot crosswind", "Vortices drift sideways onto parallel runways or runway centerline", "Anticipate vortex drift when landing on parallel runway systems"],
                                ["Ground Effect Lateral Spread", "Within 100 to 200 feet of ground", "Vortices rebound and move laterally outwards at 2 to 3 knots", "Be vigilant during flare and ground rollout behind departing jets"],
                                ["Atmospheric Dissipation", "2 to 3 minutes typical life", "Atmospheric turbulence and wind shear break down vortex cores", "Observe mandatory ATC time separation (2 to 3 minutes)"]
                            ]
                        }
                    }
                ],
                # Card 7 (Page 7): Real-World Application (Winglets on Commercial Airliners)
                [
                    {
                        "type": "real_world_example",
                        "title": "Aviation Engineering: Winglets and Induced Drag Reduction",
                        "content": {
                            "title": "How Wingtip Devices Mitigate Vortices and Save Fuel",
                            "text": "If you look closely at modern airliners operating at international airports, you will observe upturned vertical surfaces at the tips of their wings called **winglets** or **sharklets**:\n\n- **Physical Barrier**: A winglet acts as a vertical aerodynamic dam. It physically impedes the high-pressure air below the wing from curling freely around the wingtip into the upper low-pressure zone.\n- **Vortex Attenuation**: By breaking up and dispersing the vortex before it can roll into a concentrated funnel, winglets significantly shrink the wake turbulence footprint trailing behind the plane.\n- **Induced Drag Reduction**: Because wingtip vortices consume engine power to spin the air (creating induced drag), winglets reduce total aircraft drag by 4% to 6%, saving hundreds of thousands of liters of aviation fuel annually."
                        }
                    }
                ],
                # Card 8 (Page 8): Safety Connection: Takeoff and Landing Avoidance Rules
                [
                    {
                        "type": "concept_explanation",
                        "title": "Safety Doctrine: Wake Turbulence Flight Paths",
                        "content": {
                            "title": "Standard Procedures for Avoiding Wake Turbulence",
                            "text": "Wake vortices begin the exact instant an aircraft's nose wheel leaves the ground (liftoff/rotation) and cease the exact moment the main landing wheels touch down on landing.\n\nPilots follow strict procedural flight paths to guarantee clean air:\n\n- **Departing Behind a Large Jet**:\n  1. The trailing light aircraft must rotate (lift off) **prior** to the point where the preceding jet rotated.\n  2. The pilot must climb **above** and upwind of the jet's climbing flight path to remain in clean air above the sinking vortices.\n\n- **Landing Behind a Large Jet**:\n  1. The trailing pilot must establish an approach path **above** the preceding jet's glide path.\n  2. The pilot must plan their touchdown point **beyond** the point where the preceding jet's wheels touched the runway pavement.\n\n- **ATC Separation**: Air Traffic Control enforces mandatory 2-to-3-minute radar delays behind heavy aircraft categories."
                        }
                    }
                ],
                # Card 9 (Page 9): Educational Video Integration
                [
                    {
                        "type": "suggested_video",
                        "title": "Ground Effect and Wake Turbulence Explained",
                        "content": {
                            "title": "Ground Effect and Wake Turbulence Explained (EASY)",
                            "description": "Watch smoke-visualization wind tunnel tests demonstrating wingtip vortex formation and see graphical animations showing safe takeoff and landing avoidance corridors.",
                            "url": "https://www.youtube.com/watch?v=-34-Igi5UMc"
                        }
                    }
                ],
                # Card 10 (Page 10): Formative Knowledge Checks & Summary
                [
                    {
                        "type": "knowledge_check",
                        "title": "Diagnostic Check: Strongest Wake Turbulence Configuration",
                        "content": {
                            "question": "In what specific flight configuration does an aircraft generate the strongest, most violent wingtip vortices?",
                            "options": [
                                "Light weight, clean wing configuration, and fast cruise speed",
                                "Heavy weight, clean wing configuration, and slow speed (high angle of attack)",
                                "Heavy weight, fully extended flaps, and high speed",
                                "Light weight, extended landing gear, and landing speed"
                            ],
                            "answer": "B",
                            "explanation": "Wingtip vortex intensity is directly proportional to lift generated and angle of attack. A heavy aircraft requires maximum lift; a clean configuration (flaps up) concentrates lift at wingtips; and slow speed forces a high Angle of Attack, producing maximum vortex strength."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Diagnostic Check: Landing Separation and Touchdown Geometry",
                        "content": {
                            "question": "If you are landing a light aircraft behind a large commercial passenger jet, where must you plan to touch down on the runway to safely avoid the jet's wake turbulence?",
                            "options": [
                                "Before the point where the large jet's nose wheel touched down",
                                "Exactly on top of the jet's tire markings at the start of the runway",
                                "Beyond the point where the large jet's wheels touched down",
                                "On the grass adjacent to the runway to avoid the pavement entirely"
                            ],
                            "answer": "C",
                            "explanation": "Wingtip vortices are generated only while the wing produces lift. Once the jet touches down, lift ceases and vortex generation stops. Touching down beyond the preceding jet's touchdown point ensures the trailing aircraft remains in clean, undisturbed air."
                        }
                    }
                ]
            ]
        }
    ]

@transaction.atomic
def ingest_grade10_aviation_topic366(replace=True):
    """Ingests Grade 10 Aviation Topic 366 (Aerodynamics of Flight) into database."""
    print("=" * 80)
    print("VLEARN CURRICULUM INGESTION: Grade 10 Aviation — Topic 366 (ID: 366)")
    print("Aerodynamics of Flight")
    print("=" * 80)

    # 1. Verify Scope Isolation
    curriculum = Curriculum.objects.get(id=5)
    grade = Grade.objects.get(id=5, level=10)
    subject = Subject.objects.get(id=44, grade=grade)
    topic = Topic.objects.get(id=366, subject=subject)

    print(f"[*] Verified Curriculum: {curriculum.name} (ID: {curriculum.id})")
    print(f"[*] Verified Grade: {grade.name} (Level: {grade.level})")
    print(f"[*] Verified Subject: {subject.name} (ID: {subject.id})")
    print(f"[*] Verified Topic: {topic.name} (ID: {topic.id}, Order: {topic.order})")

    if replace:
        print("[*] Ingestion mode: REPLACE. Purging existing Topic 366 lessons & blocks...")
        existing_lessons = Lesson.objects.filter(topic=topic)
        count = existing_lessons.count()
        existing_lessons.delete()
        print(f"[*] Purged {count} existing lessons under Topic 366.")

    topic_data = build_topic366_curriculum()

    total_lessons_created = 0
    total_blocks_created = 0

    for u_idx, unit_info in enumerate(topic_data):
        u_order = unit_info["unit_order"]
        u_name = unit_info["unit_name"]
        u_desc = unit_info["unit_description"]
        l_title = unit_info["lesson_title"]
        pages = unit_info["pages"]

        # Fetch existing LearningUnit
        lu, _ = LearningUnit.objects.get_or_create(
            topic=topic,
            order=u_order,
            defaults={
                "name": u_name,
                "description": u_desc
            }
        )
        if lu.name != u_name:
            lu.name = u_name
            lu.description = u_desc
            lu.save()

        print(f"\n---> Ingesting Unit {u_order} (ID: {lu.id}): {lu.name}")

        lesson = Lesson.objects.create(
            topic=topic,
            learning_unit=lu,
            title=l_title,
            status="published",
            version=1
        )
        total_lessons_created += 1
        print(f"  [+] Created Published Lesson {lesson.id}: {lesson.title}")

        block_order_counter = 0

        for page_num_0, page_blocks in enumerate(pages):
            page_num = page_num_0 + 1

            for block_def in page_blocks:
                b_type = block_def["type"]
                b_title = clean_text(block_def["title"])
                b_content = clean_dict(block_def["content"])

                # Determine page title based on block
                page_title = b_title

                LessonBlock.objects.create(
                    lesson=lesson,
                    block_type=b_type,
                    title=b_title,
                    content=b_content,
                    order=block_order_counter,
                    page_number=page_num,
                    page_title=page_title,
                    component_type=b_type,
                    component_order=block_order_counter
                )
                block_order_counter += 1
                total_blocks_created += 1

        print(f"      Created {block_order_counter} blocks across 10 pages.")

    print("\n" + "=" * 80)
    print("INGESTION SUMMARY")
    print("=" * 80)
    print(f"Total Lessons Created: {total_lessons_created}")
    print(f"Total Blocks Created:  {total_blocks_created}")
    print("=" * 80)

if __name__ == "__main__":
    replace_flag = "--replace" in sys.argv or True
    ingest_grade10_aviation_topic366(replace=replace_flag)