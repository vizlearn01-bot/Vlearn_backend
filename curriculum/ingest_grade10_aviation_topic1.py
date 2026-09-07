"""
VLearn Grade 10 Aviation — Topic 1: Foundations of Aviation Technology
Production Ingestion Engine

Curriculum: CBC (Curriculum ID: 5)
Grade: Grade 10 (Grade ID: 5, Level: 10)
Subject: Aviation (Subject ID: 44)
Topic: Foundations of Aviation Technology (Topic ID: 247, Order: 0)

Ingests 5 Comprehensive Learning Units & Lessons (~52 Concept Cards):
  1. Why Aviation Technology Matters (10 Cards)
  2. Historical Milestones in the Development of Aircraft (10 Cards)
  3. Contributions of Key Aviation Pioneers (10 Cards)
  4. Categories and Functions of Aircraft (11 Cards)
  5. Demonstrating Lift, Buoyancy, and Aviation Development (11 Cards)

Usage:
  ./venv/bin/python curriculum/ingest_grade10_aviation_topic1.py [--replace]
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
    """Removes bracket citations [54, 55], internal visual prompt text, and normalizes typography."""
    if not text:
        return ""
    # Remove bracket citations like [54], [54, 55], [image_1]
    text = re.sub(r'\[(?:\d+|image_\d+|S\d+.*?|[\d,\s]+)\]', '', text)
    # Remove internal visual generation tags
    text = re.sub(r'\[VISUAL:\s*[^\]]+\]', '', text, flags=re.IGNORECASE)
    # Remove practical task and application internal markers
    text = re.sub(r'\[(?:REAL WORLD APPLICATION|PRACTICAL TASK|SAFETY SCENARIO)[^\]]*\]', '', text, flags=re.IGNORECASE)
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

def build_topic1_curriculum():
    """Returns the pedagogical page and block structure for Grade 10 Aviation Topic 1."""
    return [
        # =====================================================================
        # LESSON 1.1.1: Why Aviation Technology Matters
        # =====================================================================
        {
            "unit_order": 0,
            "unit_name": "Why Aviation Technology Matters",
            "unit_description": "Definition of aviation technology versus industry, global connectivity, logistics chains, and foundational safety mindset.",
            "lesson_title": "Why Aviation Technology Matters",
            "pages": [
                # Page 1: Visual Hook & Learning Objectives
                [
                    {
                        "type": "suggested_image",
                        "title": "A Boeing 777 Freighter Loading High-Value Cargo on the Ramp",
                        "content": {
                            "title": "A Boeing 777 Freighter Loading High-Value Cargo on the Ramp",
                            "caption": "A modern wide-body cargo airliner preparing for a long-haul intercontinental flight, demonstrating the coordination of aeronautical engineering and logistics.",
                            "resolved_image_url": "https://upload.wikimedia.org/wikipedia/commons/7/74/Boeing_777F_%28Korean_Air%29_HL8251_LHR_%286890952991%29.jpg"
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Learning Focus: Why Aviation Technology Matters",
                        "content": {
                            "title": "Learning Focus: Why Aviation Technology Matters",
                            "goals": [
                                "Define aviation technology and distinguish it from the broader aviation industry.",
                                "Analyze how aviation networks establish global economic and cultural connectivity.",
                                "Trace the multi-step technical logistics chain required for air cargo transport.",
                                "Explain why an uncompromising safety-first mindset is the absolute foundation of all aviation operations."
                            ]
                        }
                    }
                ],
                # Page 2: Key Terminology
                [
                    {
                        "type": "definition_card",
                        "title": "Foundational Aviation Terminology",
                        "content": {
                            "title": "Core Technical Vocabulary",
                            "definitions": [
                                {
                                    "term": "Aviation Technology",
                                    "definition": "The practical application of aeronautical science, mechanical engineering, avionics, and physics to design, construct, operate, and maintain aircraft.",
                                    "example": "Developing fuel-efficient turbofan engines and fly-by-wire computer systems."
                                },
                                {
                                    "term": "Aviation Industry",
                                    "definition": "The global commercial ecosystem encompassing airlines, air cargo operators, airport management companies, tourism agencies, and civil aviation regulators.",
                                    "example": "Passenger ticket reservation platforms and international air route scheduling."
                                },
                                {
                                    "term": "Aircraft",
                                    "definition": "Any human-engineered vehicle supported by atmospheric buoyancy or the aerodynamic reaction of air over rigid or rotating surfaces.",
                                    "example": "Fixed-wing airliners, gliders, helicopters, and airships."
                                },
                                {
                                    "term": "Aerodrome",
                                    "definition": "A defined area on land or water equipped with runways, taxiways, aprons, and navigation aids for the arrival, departure, and surface movement of aircraft.",
                                    "example": "Jomo Kenyatta International Airport (JKIA) or Wilson Airport in Nairobi."
                                },
                                {
                                    "term": "Connectivity",
                                    "definition": "The rapid aerial linkage of cities, countries, and continents that enables international trade, emergency medical evacuation, and cultural exchange.",
                                    "example": "Transporting fresh Naivasha cut flowers to Amsterdam flower auctions in under 24 hours."
                                }
                            ]
                        }
                    }
                ],
                # Page 3: Core Explanation (Technology vs Industry)
                [
                    {
                        "type": "concept_explanation",
                        "title": "The Aviation Ecosystem: Technology vs. Industry",
                        "content": {
                            "title": "The Interlocking Wings of Aviation",
                            "text": "To master aviation, you must first separate the **scientific foundation** from the **commercial engine**:\n\n- **Aviation Technology** is the scientific and technical core. It includes aerodynamic airfoil design, gas turbine propulsion, structural metallurgy, avionics radar, and strict hangar maintenance protocols. Without technology, aircraft could not leave the ground.\n- **Aviation Industry** is the economic engine. It includes flight scheduling, passenger hospitality, cargo logistics, international air law compliance, and fleet financing. Without the industry, aircraft would have no passengers to carry or freight to deliver.\n\nThese two domains work in permanent symbiosis. Every technical advancement—such as lighter carbon-fiber composites—directly expands airline range and profitability."
                        }
                    }
                ],
                # Page 4: Technical Diagram Block
                [
                    {
                        "type": "suggested_diagram",
                        "title": "The Aviation Technology and Industry Ecosystem",
                        "content": {
                            "title": "Aviation Ecosystem Framework",
                            "caption": "How scientific aeronautics, engineering, air traffic management, and commercial operations interconnect to sustain global flight."
                        }
                    }
                ],
                # Page 5: Comparative Analysis Table
                [
                    {
                        "type": "comparison_table",
                        "title": "Contrasting Aviation Technology with the Aviation Industry",
                        "content": {
                            "title": "Aviation Technology vs. Aviation Industry",
                            "headers": ["Aspect", "Aviation Technology", "Aviation Industry"],
                            "rows": [
                                ["Primary Focus", "Aerodynamics, propulsion, avionics, structural physics", "Commercial operations, passenger travel, business logistics"],
                                ["Key Personnel", "Aeronautical engineers, licensed aircraft technicians, avionics specialists", "Airline managers, flight dispatchers, ticketing agents, cabin crew"],
                                ["Core Objectives", "Airworthiness, mechanical reliability, fuel efficiency, system safety", "Customer satisfaction, route profitability, network growth, schedule reliability"],
                                ["Regulatory Basis", "Airworthiness directives, engineering manuals, maintenance type certifications", "Air service licenses, bilateral air agreements, consumer protection rules"]
                            ]
                        }
                    }
                ],
                # Page 6: Real-World Logistics Case Study
                [
                    {
                        "type": "real_world_example",
                        "title": "The Naivasha-to-Amsterdam Cold Chain",
                        "content": {
                            "title": "From Kenyan Greenhouses to European Markets",
                            "text": "Consider a harvest of fresh red roses picked near Lake Naivasha at 10:00 AM on Tuesday. By 6:00 AM Wednesday morning, those exact roses are displayed in a florist in the Netherlands.\n\nThis speed is achieved through a synchronized technological chain:\n- **Refrigerated Transport**: Sealed cold-trucks maintain 2°C temperature from Naivasha to Jomo Kenyatta International Airport (JKIA).\n- **High-Deck Cargo Palletization**: Hydraulic scissor-loaders slide specialized aircraft containers (Unit Load Devices) through wide cargo doors.\n- **Aeronautical Dispatch**: Flight dispatchers compute wind vectors, jet streams, and weight-and-balance formulas.\n- **Radar Navigation**: Air Traffic Control guides the aircraft along high-altitude airways across airspace boundaries."
                        }
                    }
                ],
                # Page 7: Educational Video Integration
                [
                    {
                        "type": "suggested_video",
                        "title": "Why Aviation Technology Matters: The Scale of Global Flight",
                        "content": {
                            "title": "The Global Aviation System in Action",
                            "description": "Examine the technical precision, engineering checks, and air traffic control systems that coordinate hundreds of thousands of daily flights worldwide.",
                            "url": "https://www.youtube.com/watch?v=g9oVFRG1PGQ"
                        }
                    }
                ],
                # Page 8: Safety Connection & Redundancy
                [
                    {
                        "type": "concept_explanation",
                        "title": "The Safety-First Mandate in Aviation",
                        "content": {
                            "title": "No Shoulders in the Sky",
                            "text": "In ground transportation, a motorist experiencing engine trouble can pull onto the road shoulder. In aviation, an aircraft cruising at 37,000 feet cannot simply pull over.\n\nFor this reason, aviation engineering is built upon **system redundancy** and **strict checklist discipline**:\n- **Dual & Triple Redundancy**: Critical flight systems (such as hydraulic flight controls, electrical generators, and altitude sensors) have secondary and tertiary backups.\n- **Zero Guesswork**: Every inspection, fuel calculation, and torque setting follows approved manufacturer procedures.\n- **Human Factors Awareness**: Technicians and pilots are trained to prevent fatigue, miscommunication, and hurry from compromising airworthiness."
                        }
                    }
                ],
                # Page 9: Formative Knowledge Check 1
                [
                    {
                        "type": "knowledge_check",
                        "title": "Diagnostic Check: Technology vs. Industry",
                        "content": {
                            "question": "An aeronautical engineer conducts wind-tunnel tests on a newly contoured wingtip winglet to reduce induced drag. How is this activity best classified?",
                            "options": [
                                "A commercial aviation marketing initiative",
                                "An aviation technology development",
                                "An airport passenger logistics service",
                                "A civil land transport investigation"
                            ],
                            "answer": "B",
                            "explanation": "Testing aerodynamic shapes and analyzing drag forces in wind tunnels is fundamental engineering research, which falls directly under aviation technology rather than commercial marketing or airport passenger services."
                        }
                    }
                ],
                # Page 10: Formative Knowledge Check 2 & Summary
                [
                    {
                        "type": "knowledge_check",
                        "title": "Diagnostic Check: Global Connectivity",
                        "content": {
                            "question": "Which of the following best describes the primary value of global aviation connectivity?",
                            "options": [
                                "Maximizing ticket sales revenues for international airline alliances",
                                "Creating high-speed, reliable aerial corridors between geographical regions to support trade, tourism, and humanitarian relief",
                                "Restricting passenger baggage weights to reduce airport check-in queues",
                                "Forcing all international travel to transit through a single central hub"
                            ],
                            "answer": "B",
                            "explanation": "Aviation connectivity is defined by its ability to rapidly link distant cities and continents, enabling high-value trade, rapid medical supply delivery, and cultural exchange that land or sea routes cannot match in speed."
                        }
                    },
                    {
                        "type": "summary",
                        "title": "Core Takeaways: Why Aviation Technology Matters",
                        "content": {
                            "title": "Summary & Synthesis",
                            "summary_points": [
                                "Aviation technology represents the applied engineering, aerodynamic, and maintenance science enabling flight.",
                                "The aviation industry is the commercial framework that utilizes aircraft to generate economic value and global mobility.",
                                "Aviation connectivity powers international logistics chains, transporting perishable agricultural produce and emergency medical aid across continents overnight.",
                                "Safety is the foundational imperative of all aviation technology, governed by strict checklists, dual redundancy, and zero tolerance for procedural shortcuts."
                            ]
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 1.1.2: Historical Milestones in the Development of Aircraft
        # =====================================================================
        {
            "unit_order": 1,
            "unit_name": "Historical Milestones in the Development of Aircraft",
            "unit_description": "Chronological progression from lighter-than-air buoyancy balloons to gliders, powered three-axis airplanes, helicopters, and jetliners.",
            "lesson_title": "Historical Milestones in the Development of Aircraft",
            "pages": [
                # Page 1: Visual Hook & Objectives
                [
                    {
                        "type": "suggested_image",
                        "title": "The Wright Flyer Taking Off at Kitty Hawk, December 17, 1903",
                        "content": {
                            "title": "The Birth of Controlled, Powered Flight",
                            "caption": "Orville Wright piloting the 1903 Flyer over the sands of Kill Devil Hills, North Carolina, as Wilbur Wright watches from the ground.",
                            "resolved_image_url": "https://upload.wikimedia.org/wikipedia/commons/8/86/First_flight2.jpg"
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Learning Focus: Historical Flight Milestones",
                        "content": {
                            "title": "Learning Focus: Historical Flight Milestones",
                            "goals": [
                                "Sequence the major technological eras of aviation from 1783 to the modern era.",
                                "Explain how human flight transitioned from unpowered, wind-dependent balloons to steered, powered aircraft.",
                                "Analyze the technological leaps enabling vertical flight in rotary-wing helicopters.",
                                "Contrast early wood-and-fabric airframes with modern carbon-fiber composite jet aircraft."
                            ]
                        }
                    }
                ],
                # Page 2: Key Terminology
                [
                    {
                        "type": "definition_card",
                        "title": "Historical Milestones Terminology",
                        "content": {
                            "title": "Milestone Concepts",
                            "definitions": [
                                {
                                    "term": "Hot-Air Balloon",
                                    "definition": "A lighter-than-air craft consisting of an airtight envelope containing heated air, which generates upward buoyancy because it is less dense than the surrounding cold atmosphere.",
                                    "example": "The Montgolfier brothers' paper-lined linen balloon launched in Paris in 1783."
                                },
                                {
                                    "term": "Glider",
                                    "definition": "An unpowered heavier-than-air aircraft that relies on rigid, stationary wings to produce aerodynamic lift when descending through air currents.",
                                    "example": "Sir George Cayley's pioneering 1853 carriage glider."
                                },
                                {
                                    "term": "Fixed-Wing Aircraft",
                                    "definition": "A powered, heavier-than-air vehicle that generates continuous lift from stationary wings as it is propelled forward by an engine.",
                                    "example": "The 1903 Wright Flyer and modern Boeing/Airbus jetliners."
                                },
                                {
                                    "term": "Rotary-Wing Aircraft",
                                    "definition": "A heavier-than-air machine that generates lift and propulsion using overhead blades (rotors) rotating around a central vertical shaft.",
                                    "example": "Igor Sikorsky's VS-300 helicopter."
                                },
                                {
                                    "term": "Jet Propulsion",
                                    "definition": "An engine mechanism that continuously compresses atmospheric air, mixes it with aviation fuel, ignites it, and expels high-velocity exhaust gases to produce forward thrust.",
                                    "example": "Turbofan engines powering commercial airliners at transonic speeds."
                                }
                            ]
                        }
                    }
                ],
                # Page 3: Core Explanation (The 5 Great Eras)
                [
                    {
                        "type": "concept_explanation",
                        "title": "The Five Eras of Aeronautical Evolution",
                        "content": {
                            "title": "From Floating Bubbles to Supersonic Jets",
                            "text": "Human flight did not arrive in a single breakthrough. It was conquered in five successive engineering eras:\n\n1. **The Buoyant Flotation Era (1783)**: Pioneers trapped heated air inside silk and paper bags, floating on buoyant air displacement. However, balloons were wind-blown and could not be steered.\n2. **The Aerodynamic Glider Era (1853)**: Inventors discarded flapping wings and proved that rigid, curved wings could support human weight when pulled forward through the air.\n3. **The Powered, Controlled Flight Era (1903)**: The Wright brothers married an internal combustion engine with aerodynamic three-axis flight control, creating the first practical airplane.\n4. **The Rotary-Wing Era (1939)**: Helicopters bypassed the need for long runways by rotating wings overhead, achieving stationary hover and vertical takeoff.\n5. **The Modern Jet & Composite Era (1950s–Present)**: Jet turbines and lightweight carbon composites unlocked intercontinental flight at 35,000+ feet with extreme reliability."
                        }
                    }
                ],
                # Page 4: Technical Diagram Block
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Chronological Timeline of Aviation Breakthroughs",
                        "content": {
                            "title": "Aviation Milestones Timeline",
                            "caption": "From 1783 Montgolfier hot-air balloons through Cayley gliders, Wright three-axis control, Sikorsky helicopters, to the modern jet age."
                        }
                    }
                ],
                # Page 5: Comparative Evolution Table
                [
                    {
                        "type": "comparison_table",
                        "title": "Technological Evolution Across Flight Eras",
                        "content": {
                            "title": "Milestone Comparison: Lift, Propulsion & Steering",
                            "headers": ["Era & Vehicle", "Method of Lift", "Method of Propulsion", "Directional Steering Mechanism"],
                            "rows": [
                                ["Montgolfier Balloon (1783)", "Buoyancy (heated air density)", "None (carried by atmospheric wind)", "Uncontrolled (dependent on wind direction)"],
                                ["Cayley Glider (1853)", "Aerodynamic lift from fixed curved wing", "Gravity / tow line descent", "Fixed cruciform tailplane (rudder/elevator)"],
                                ["Wright Flyer (1903)", "Aerodynamic lift from biplane wings", "12 hp lightweight petrol piston engine", "Three-axis control (wing-warping, forward canard, rear rudder)"],
                                ["Sikorsky Helicopter (1939)", "Rotating overhead aerodynamic rotor blades", "Piston / turboshaft engine", "Cyclic pitch, collective pitch, and anti-torque tail rotor"],
                                ["Modern Jetliner (Present)", "High-speed supercritical wing airfoils", "High-bypass turbofan jet engines", "Fly-by-wire hydraulic ailerons, elevators, spoilers, and rudder"]
                            ]
                        }
                    }
                ],
                # Page 6: Real-World Material Transformation
                [
                    {
                        "type": "real_world_example",
                        "title": "From Spruce Wood to Carbon Fiber Composites",
                        "content": {
                            "title": "The Structural Revolution of Aircraft Design",
                            "text": "The 1903 Wright Flyer was built from spruce wood, muslin fabric, and bicycle chains. While light, wood is vulnerable to moisture rot, insect damage, and structural splintering under aerodynamic stress.\n\nIn the 1930s, aviation shifted to lightweight aluminum alloys (Duralumin), which allowed pressurized, all-metal monocoque fuselages.\n\nToday, modern airliners like the Boeing 787 Dreamliner and Airbus A350 are constructed with more than 50% carbon-fiber reinforced polymers (CFRP). Carbon composites are lighter than aluminum, immune to metal fatigue and corrosion, and allow higher cabin humidity for passenger comfort."
                        }
                    }
                ],
                # Page 7: Educational Video Integration
                [
                    {
                        "type": "suggested_video",
                        "title": "Chronology of Human Flight: From Gliders to Jets",
                        "content": {
                            "title": "Archival Journey of Flight Milestones",
                            "description": "Watch historical flight footage showing early glider launches, the Wright Flyer at Kitty Hawk, early rotary-wing experiments, and early jet aircraft.",
                            "url": "https://www.youtube.com/watch?v=NpqU3eSeS1c"
                        }
                    }
                ],
                # Page 8: Procedural Analysis
                [
                    {
                        "type": "step_process",
                        "title": "Evolutionary Milestones in Aeronautical Control",
                        "content": {
                            "title": "The 4 Critical Steps to Solving Flight",
                            "steps": [
                                "Step 1: Overcoming Gravity (Buoyancy) — Utilizing Archimedes' principle to rise using hot air, but with zero directional guidance.",
                                "Step 2: Understanding Aerodynamic Surfaces — Separating the lifting surface (fixed wing) from propulsion, eliminating ornithopter flapping.",
                                "Step 3: Mastering 3D Directional Equilibrium — Implementing coordinated controls across roll, pitch, and yaw axes to prevent fatal stall-spins.",
                                "Step 4: Continuous High-Velocity Propulsion — Transitioning from low-power piston propellers to gas turbine jet compression for global travel."
                            ]
                        }
                    }
                ],
                # Page 9: Formative Knowledge Check 1
                [
                    {
                        "type": "knowledge_check",
                        "title": "Diagnostic Check: Historical Sequence",
                        "content": {
                            "question": "Which of the following correctly lists aviation milestones in chronological order from earliest to most recent?",
                            "options": [
                                "Rotary-wing aircraft → Fixed-wing aircraft → Gliders → Hot-air balloons",
                                "Hot-air balloons → Gliders → Fixed-wing aircraft → Rotary-wing aircraft",
                                "Gliders → Hot-air balloons → Rotary-wing aircraft → Jet aircraft",
                                "Hot-air balloons → Rotary-wing aircraft → Gliders → Jet aircraft"
                            ],
                            "answer": "B",
                            "explanation": "Human flight began with Montgolfier hot-air balloons in 1783, progressed to Sir George Cayley's unpowered gliders in the 19th century, achieved powered fixed-wing flight with the Wrights in 1903, and developed practical helicopters with Sikorsky in the late 1930s."
                        }
                    }
                ],
                # Page 10: Formative Knowledge Check 2 & Summary
                [
                    {
                        "type": "knowledge_check",
                        "title": "Diagnostic Check: The Balloon Dilemma",
                        "content": {
                            "question": "What primary engineering limitation prevented early hot-air balloons from serving as reliable, scheduled inter-city passenger transportation?",
                            "options": [
                                "They were heavier than the surrounding atmospheric air.",
                                "They lacked mechanical propulsion and steering control systems, making their flight paths entirely dependent on prevailing wind currents.",
                                "They were constructed from heavy steel plates that required excessive fuel.",
                                "They could only generate lift during cold nighttime hours."
                            ],
                            "answer": "B",
                            "explanation": "While hot-air balloons generated effective upward buoyancy, they lacked engines and aerodynamic rudders to propel and steer themselves against the wind, rendering scheduled point-to-point transportation impossible."
                        }
                    },
                    {
                        "type": "summary",
                        "title": "Core Takeaways: Historical Milestones in Aircraft Development",
                        "content": {
                            "title": "Summary & Synthesis",
                            "summary_points": [
                                "Flight evolved through distinct stages: buoyancy flotation, unpowered gliding, controlled powered flight, vertical rotary flight, and modern jet propulsion.",
                                "Sir George Cayley made the foundational conceptual leap by separating the systems of lift, thrust, and control in a fixed-wing configuration.",
                                "The Wright brothers conquered the critical problem of 3D spatial stability through their innovative three-axis control system.",
                                "Technological advances in lightweight alloys and carbon-fiber composites transformed frail, dangerous wood-and-fabric gliders into intercontinental passenger airliners."
                            ]
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 1.1.3: Contributions of Key Aviation Pioneers
        # =====================================================================
        {
            "unit_order": 2,
            "unit_name": "Contributions of Key Aviation Pioneers",
            "unit_description": "The transformative breakthroughs of the Montgolfier Brothers, Sir George Cayley, the Wright Brothers, and Igor Sikorsky.",
            "lesson_title": "Contributions of Key Aviation Pioneers",
            "pages": [
                # Page 1: Visual Hook & Objectives
                [
                    {
                        "type": "suggested_image",
                        "title": "Igor Sikorsky Flying the Experimental VS-300 Helicopter in 1939",
                        "content": {
                            "title": "Pioneering Vertical Flight and Hover Control",
                            "caption": "Aviation pioneer Igor Sikorsky test-piloting his VS-300 helicopter, the design that established the modern single main rotor and anti-torque tail rotor configuration.",
                            "resolved_image_url": "https://upload.wikimedia.org/wikipedia/commons/9/9d/Sikorsky_UH-60_Blackhawk_3869_%282076016691%29.jpg"
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Learning Focus: Key Aviation Pioneers",
                        "content": {
                            "title": "Learning Focus: Key Aviation Pioneers",
                            "goals": [
                                "Identify the specific technical problems solved by four principal aviation pioneers.",
                                "Explain why Sir George Cayley is revered as the 'Father of Aviation'.",
                                "Analyze the mechanics of the Wright brothers' three-axis control system (roll, pitch, and yaw).",
                                "Explain how Igor Sikorsky solved the rotational torque dilemma in rotary-wing flight."
                            ]
                        }
                    }
                ],
                # Page 2: Key Terminology
                [
                    {
                        "type": "definition_card",
                        "title": "Aviation Pioneers Terminology",
                        "content": {
                            "title": "Pioneering Principles",
                            "definitions": [
                                {
                                    "term": "Buoyant Lift (Montgolfier)",
                                    "definition": "The upward force resulting from fluid displacement, demonstrated in 1783 when heated air inside an envelope created lower density than the cooler ambient atmosphere.",
                                    "example": "Hot-air balloons and modern gas airships."
                                },
                                {
                                    "term": "Fixed-Wing Concept (Cayley)",
                                    "definition": "The radical insight that an aircraft wing should remain rigid and stationary to produce lift, while forward propulsion and steering control are managed by completely separate systems.",
                                    "example": "All modern airplanes with stationary wings and separate engines."
                                },
                                {
                                    "term": "Three-Axis Control (Wrights)",
                                    "definition": "A mechanical system enabling the pilot to steer an aircraft across its three rotational axes: longitudinal (roll), lateral (pitch), and vertical (yaw).",
                                    "example": "Ailerons for bank, elevators for climb/dive, and rudder for directional heading."
                                },
                                {
                                    "term": "Anti-Torque Tail Rotor (Sikorsky)",
                                    "definition": "A small, vertically mounted auxiliary rotor on the tail boom that counteracts the spinning reaction force (torque) generated by the main overhead rotor blades.",
                                    "example": "The tail rotor seen on standard single-rotor helicopters."
                                }
                            ]
                        }
                    }
                ],
                # Page 3: Core Explanation (The Big Four Pioneers)
                [
                    {
                        "type": "concept_explanation",
                        "title": "The Four Masterminds of Atmospheric Flight",
                        "content": {
                            "title": "Four Pioneers, Four Solved Puzzles",
                            "text": "Every pilot in the cockpit of a modern airliner stands upon the shoulders of four key inventors:\n\n- **Joseph & Étienne Montgolfier (1783)**: Solved the problem of **rising into the air**. By harnessing thermal expansion, they proved human beings could break free of Earth's surface safely.\n- **Sir George Cayley (1804–1853)**: Solved the problem of **aircraft architecture**. Before Cayley, inventors tried to build machines with flapping wings (ornithopters). Cayley proved that flapping is mechanically inefficient; a rigid, fixed wing pulled forward by an engine produces stable, predictable lift.\n- **Orville & Wilbur Wright (1903)**: Solved the problem of **three-dimensional balance**. Other inventors had engines and gliders but crashed fatally. The Wrights realized that flight is a dynamic balancing act requiring active steering across roll, pitch, and yaw.\n- **Igor Sikorsky (1939)**: Solved the problem of **vertical takeoff and hover**. He conquered rotational torque by adding a vertical tail rotor, inventing the modern practical helicopter."
                        }
                    }
                ],
                # Page 4: Technical Diagram Block (Three-Axis Control)
                [
                    {
                        "type": "suggested_diagram",
                        "title": "The Three-Axis Flight Control System",
                        "content": {
                            "title": "Three Aircraft Rotational Axes",
                            "caption": "Roll (longitudinal axis via ailerons), Pitch (lateral axis via elevators), and Yaw (vertical axis via the rudder)."
                        }
                    }
                ],
                # Page 5: Comparative Pioneer Matrix
                [
                    {
                        "type": "comparison_table",
                        "title": "Aviation Pioneers and Their Core Breakthroughs",
                        "content": {
                            "title": "Matrix of Pioneers, Principles, and Legacy",
                            "headers": ["Pioneer", "Primary Invention", "Underlying Scientific Law", "Legacy in Modern Flight"],
                            "rows": [
                                ["Montgolfier Brothers (France)", "Hot-Air Balloon (1783)", "Thermal density differentials (Archimedes' Principle)", "Thermal ballooning, atmospheric research aerostats"],
                                ["Sir George Cayley (UK)", "Fixed-Wing Architecture & Glider (1853)", "Separation of lift, propulsion, and directional control", "Standard airframe layout of all commercial passenger jets"],
                                ["Wright Brothers (USA)", "Three-Axis Aeronautical Control (1903)", "Aerodynamic moments & differential wing surface pressure", "Primary flight control surfaces (ailerons, elevators, rudder)"],
                                ["Igor Sikorsky (USA/Russia)", "Single-Rotor Practical Helicopter (1939)", "Newton's third law of motion (anti-torque reaction balance)", "Search and rescue helicopters, medical air ambulances"]
                            ]
                        }
                    }
                ],
                # Page 6: Real-World Case Study (Three-Axis Flight Control)
                [
                    {
                        "type": "real_world_example",
                        "title": "How a Modern Pilot Uses the Wright Brothers' System",
                        "content": {
                            "title": "Banking, Climbing, and Turning a Jetliner",
                            "text": "When a pilot flies a Boeing 737 from Nairobi to Mombasa, every maneuver uses the exact control axes invented by Orville and Wilbur Wright:\n\n- **Roll (Longitudinal Axis)**: Turning the cockpit control wheel deflects the **ailerons** on the outer wings in opposite directions, causing one wing to rise and the other to drop, banking the aircraft into a turn.\n- **Pitch (Lateral Axis)**: Pulling the control column backward deflects the rear **elevators** upward, forcing the tail down and pointing the nose up to climb.\n- **Yaw (Vertical Axis)**: Pressing the left or right foot pedals deflects the vertical **rudder**, swinging the nose left or right to align with the runway during crosswind landings."
                        }
                    }
                ],
                # Page 7: Educational Video Integration
                [
                    {
                        "type": "suggested_video",
                        "title": "The Wright Brothers Three-Axis Control System Explained",
                        "content": {
                            "title": "3D Physics of Three-Axis Steering",
                            "description": "Examine a 3D aerodynamic model of the 1903 Wright Flyer demonstrating how wing-warping, forward canard elevators, and rear rudders produce coordinated flight.",
                            "url": "https://www.youtube.com/watch?v=1O94ThV6vQw"
                        }
                    }
                ],
                # Page 8: Procedural Analysis (Solving Rotor Torque)
                [
                    {
                        "type": "step_process",
                        "title": "How Sikorsky Solved the Helicopter Torque Dilemma",
                        "content": {
                            "title": "Newton's Third Law in Rotary Flight",
                            "steps": [
                                "The Problem: An engine spins the heavy overhead rotor blades clockwise. According to Newton's Third Law (equal and opposite reaction), the helicopter fuselage wants to spin uncontrollably counter-clockwise.",
                                "Failed Attempts: Early inventors tried twin main rotors spinning in opposite directions, which was excessively heavy and complex.",
                                "Sikorsky's Breakthrough: Igor Sikorsky added a small, vertical tail rotor at the end of a long tail boom.",
                                "The Result: The tail rotor blows air sideways, creating an opposing horizontal force that cancels out the fuselage spin, allowing stable hover and precision flight."
                            ]
                        }
                    }
                ],
                # Page 9: Formative Knowledge Check 1
                [
                    {
                        "type": "knowledge_check",
                        "title": "Diagnostic Check: The Father of Aviation",
                        "content": {
                            "question": "Why is Sir George Cayley universally honored in aeronautical history as the 'Father of Aviation'?",
                            "options": [
                                "He piloted the first heavier-than-air powered aircraft with an internal combustion engine.",
                                "He designed the first practical helicopter capable of hovering in place.",
                                "He established the fixed-wing layout, scientifically separating the systems that generate lift, forward thrust, and flight control.",
                                "He proved that hot air inside an envelope could lift heavy passengers via buoyancy."
                            ],
                            "answer": "C",
                            "explanation": "Sir George Cayley revolutionized flight theory by breaking away from flapping-wing ornithopters and formulating the fixed-wing configuration, proving that wings should generate lift while separate engines provide thrust."
                        }
                    }
                ],
                # Page 10: Formative Knowledge Check 2 & Summary
                [
                    {
                        "type": "knowledge_check",
                        "title": "Diagnostic Check: The Wright Brothers' Secret",
                        "content": {
                            "question": "What was the critical technological breakthrough that enabled the Wright brothers to achieve controlled flight in 1903 when other well-funded pioneers had crashed?",
                            "options": [
                                "They fitted their aircraft with heavy steam boilers for extra horsepower.",
                                "They invented three-axis aerodynamic control, allowing the pilot to balance and steer the machine in roll, pitch, and yaw.",
                                "They developed an automatic electronic computer to stabilize the aircraft.",
                                "They built their propellers out of heavy solid cast iron."
                            ],
                            "answer": "B",
                            "explanation": "While others focused solely on bigger engines, the Wright brothers realized that an aircraft in flight is unstable and must be actively steered in three dimensions. Their three-axis control system was the true breakthrough of 1903."
                        }
                    },
                    {
                        "type": "summary",
                        "title": "Core Takeaways: Contributions of Key Aviation Pioneers",
                        "content": {
                            "title": "Summary & Synthesis",
                            "summary_points": [
                                "The Montgolfier brothers proved humans could leave the ground through buoyant hot-air flotation.",
                                "Sir George Cayley defined the modern airplane by separating fixed lifting wings from engines and tail controls.",
                                "The Wright brothers solved the puzzle of spatial equilibrium by inventing three-axis aerodynamic control.",
                                "Igor Sikorsky mastered rotary-wing mechanics by implementing the anti-torque tail rotor, unlocking vertical flight and hover."
                            ]
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 1.1.4: Categories and Functions of Aircraft
        # =====================================================================
        {
            "unit_order": 3,
            "unit_name": "Categories and Functions of Aircraft",
            "unit_description": "Scientific categorization into Lighter-Than-Air (LTA) and Heavier-Than-Air (HTA), fixed-wing vs rotary-wing, and civil/cargo/military functions.",
            "lesson_title": "Categories and Functions of Aircraft",
            "pages": [
                # Page 1: Visual Hook & Objectives
                [
                    {
                        "type": "suggested_image",
                        "title": "A Modern Semi-Rigid Zeppelin NT Airship in Flight",
                        "content": {
                            "title": "Lighter-Than-Air Aeronautical Engineering",
                            "caption": "A modern Zeppelin NT airship cruising smoothly, illustrating buoyant lift generation combined with vectored propeller propulsion.",
                            "resolved_image_url": "https://upload.wikimedia.org/wikipedia/commons/c/cb/German_Zeppelin_NT_over_the_St.Gallen-Altenrhein_Airport.jpg"
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Learning Focus: Aircraft Categories and Functions",
                        "content": {
                            "title": "Learning Focus: Aircraft Categories and Functions",
                            "goals": [
                                "Categorize all aerial vehicles into Lighter-Than-Air (LTA) and Heavier-Than-Air (HTA) classes.",
                                "Contrast the mechanical principles of balloons, airships, fixed-wing aircraft, and helicopters.",
                                "Analyze the distinct operational roles of commercial passenger airliners, cargo freighters, general aviation, and military aircraft.",
                                "Select the optimal aircraft type for specific real-world geographical and logistical missions."
                            ]
                        }
                    }
                ],
                # Page 2: Key Terminology
                [
                    {
                        "type": "definition_card",
                        "title": "Aircraft Classification Vocabulary",
                        "content": {
                            "title": "Classification Terminology",
                            "definitions": [
                                {
                                    "term": "Lighter-Than-Air (LTA)",
                                    "definition": "Aircraft that achieve atmospheric lift primarily through hydrostatic buoyancy, utilizing lifting gases (helium or hot air) that have lower density than surrounding air.",
                                    "example": "Free balloons, steerable airships (dirigibles), and tethered aerostats."
                                },
                                {
                                    "term": "Heavier-Than-Air (HTA)",
                                    "definition": "Aircraft whose total weight exceeds that of the displaced air, requiring forward motion over aerodynamic lifting surfaces to generate dynamic lift.",
                                    "example": "Airplanes, gliders, helicopters, and autogyros."
                                },
                                {
                                    "term": "Airship (Dirigible)",
                                    "definition": "A powered, steerable lighter-than-air aircraft equipped with engines, rudders, and elevators for controlled aerial navigation.",
                                    "example": "Rigid and semi-rigid airships like the Zeppelin NT."
                                },
                                {
                                    "term": "General Aviation (GA)",
                                    "definition": "All civil aviation operations excluding scheduled commercial passenger and cargo airline services, encompassing pilot training, crop spraying, and private recreation.",
                                    "example": "Single-engine Cessna 172 flight training aircraft."
                                },
                                {
                                    "term": "Rotary-Wing Aircraft",
                                    "definition": "A heavier-than-air craft that generates lift and propulsion using horizontally spinning rotor blades, enabling vertical takeoff, landing, and stationary hover.",
                                    "example": "Search-and-rescue helicopters."
                                }
                            ]
                        }
                    }
                ],
                # Page 3: Core Explanation (The Classification Tree)
                [
                    {
                        "type": "concept_explanation",
                        "title": "The Master Taxonomy of Aircraft",
                        "content": {
                            "title": "How Does It Fly? The Fundamental Division",
                            "text": "Every aircraft in global civil and military operation falls under one of two primary scientific divisions:\n\n1. **Lighter-Than-Air (LTA)**:\n   - Operates on the principle of **buoyancy** (Archimedes' Principle).\n   - Rises without forward velocity because its envelope is filled with warm air or low-density helium.\n   - Divided into **free balloons** (drift with wind), **airships/dirigibles** (have engines and rudders to steer), and **tethered aerostats** (cable-anchored surveillance platforms).\n\n2. **Heavier-Than-Air (HTA)**:\n   - Operates on the principle of **aerodynamic lift** (Bernoulli's Principle and Newton's Third Law).\n   - Must maintain forward airspeed to force air over curved wing airfoils.\n   - Divided into **Fixed-Wing** (rigid wings propelled by jet or piston engines) and **Rotary-Wing** (spinning overhead blades generating lift and propulsion simultaneously)."
                        }
                    }
                ],
                # Page 4: Technical Diagram Block
                [
                    {
                        "type": "suggested_diagram",
                        "title": "The Complete Aircraft Classification Hierarchy",
                        "content": {
                            "title": "Taxonomy of Aircraft: LTA vs. HTA",
                            "caption": "Hierarchical breakdown of lighter-than-air vs. heavier-than-air vehicles, branching into fixed-wing, rotary-wing, airships, and operational roles."
                        }
                    }
                ],
                # Page 5: Comparative Analysis Table
                [
                    {
                        "type": "comparison_table",
                        "title": "Comparing Aircraft Categories and Operational Roles",
                        "content": {
                            "title": "Comparative Profiles of Aircraft Types",
                            "headers": ["Category", "Lifting Mechanism", "Runway Requirement", "Primary Real-World Mission"],
                            "rows": [
                                ["Free Hot-Air Balloon (LTA)", "Static thermal buoyancy", "None (open field launch)", "Recreational sightseeing, localized meteorological atmospheric soundings"],
                                ["Steerable Airship (LTA)", "Static gas buoyancy + vectored thrust", "Short mooring mast area", "Aerial sports broadcasting, long-endurance border surveillance"],
                                ["Commercial Airliner (HTA)", "Dynamic lift from fixed high-speed wings", "Long paved concrete runways (2,000–3,500m)", "Mass rapid transit of passengers and belly-hold cargo across continents"],
                                ["Dedicated Freighter (HTA)", "Dynamic lift from heavy reinforced wings", "Standard international runways with cargo ramps", "Heavy intercontinental machinery, automotive parts, and fresh agricultural produce"],
                                ["Light General Aviation (HTA)", "Dynamic lift from high-lift trainer wings", "Short paved or unpaved dirt airstrips (600–1,200m)", "Student pilot flight instruction, wildlife aerial tracking, agricultural crop-dusting"],
                                ["Helicopter (HTA Rotary)", "Dynamic lift from spinning overhead rotor blades", "Zero runway needed (helipads, forest clearings, vessel decks)", "Remote search and rescue, emergency air ambulances, offshore oil-rig transport"]
                            ]
                        }
                    }
                ],
                # Page 6: Mission Matching Case Study
                [
                    {
                        "type": "real_world_example",
                        "title": "Selecting the Right Aircraft for Kenya's Diverse Terrain",
                        "content": {
                            "title": "Matching Mission Requirements to Airframe Dynamics",
                            "text": "Kenya's varied geography demands precise aircraft selection:\n\n- **Mission A: Naivasha to Europe**: 40 tonnes of fresh roses require a wide-body **Boeing 777 Freighter** operating from JKIA's 4,117m paved runway.\n- **Mission B: Maasai Mara Safari Tourism**: Tourists landing on short bush strips (e.g., Keekorok airstrip) fly in **Cessna Grand Caravans**—rugged turboprops designed for short takeoff and landing (STOL) on gravel runways.\n- **Mission C: Mount Kenya Hiker Rescue**: A climber stranded on an icy cliff at 14,000 feet requires an **Airbus H125 rotary-wing helicopter**, which can hover in thin air, hoist the patient with a rescue winch, and land directly on a hospital helipad."
                        }
                    }
                ],
                # Page 7: Educational Video Integration
                [
                    {
                        "type": "suggested_video",
                        "title": "Lighter-Than-Air vs. Heavier-Than-Air Flight Comparison",
                        "content": {
                            "title": "Observing Aerodynamic vs. Buoyant Flight",
                            "description": "Witness the dramatic differences in launch physics, forward velocity, and maneuvering between hot-air balloons, airliners, and helicopters.",
                            "url": "https://www.youtube.com/watch?v=gg_wNRHxFug"
                        }
                    }
                ],
                # Page 8: Procedural Analysis (Aircraft Selection Algorithm)
                [
                    {
                        "type": "step_process",
                        "title": "Aeronautical Mission Decision Framework",
                        "content": {
                            "title": "How Flight Planners Select an Aircraft",
                            "steps": [
                                "Step 1: Assess Runway Availability — Does the destination have a paved 3,000m runway, an unpaved grass strip, or no landing surface at all?",
                                "Step 2: Evaluate Payload & Range — Are you carrying 300 passengers 7,000km, or 1 injured patient 80km?",
                                "Step 3: Determine Speed Requirements — Does the mission require 900 km/h cruising speed, or stationary 0 km/h hover capability?",
                                "Step 4: Balance Operating Costs — Turbine helicopters cost significantly more per flight hour than light fixed-wing airplanes, requiring justification by terrain access."
                            ]
                        }
                    }
                ],
                # Page 9: Formative Knowledge Check 1
                [
                    {
                        "type": "knowledge_check",
                        "title": "Diagnostic Check: Rescue Operations",
                        "content": {
                            "question": "A mountain rescue squad must evacuate an injured trekker from a steep, rocky ravine in Mount Kenya National Park where no roads, airstrips, or flat clearings exist. Which aircraft is most appropriate?",
                            "options": [
                                "A commercial four-engine jetliner",
                                "A high-altitude passenger airship",
                                "A rotary-wing helicopter equipped with a hoist winch",
                                "A tethered aerostat weather balloon"
                            ],
                            "answer": "C",
                            "explanation": "Helicopters generate lift with overhead rotors and can hover stationary in place without a runway, making them uniquely capable of winching casualties from rugged cliffs and mountainsides."
                        }
                    }
                ],
                # Page 10: Formative Knowledge Check 2
                [
                    {
                        "type": "knowledge_check",
                        "title": "Diagnostic Check: Balloons vs. Airships",
                        "content": {
                            "question": "What is the primary physical and mechanical distinction between a free hot-air balloon and an airship (dirigible)?",
                            "options": [
                                "Balloons are heavier-than-air vehicles, while airships are lighter-than-air.",
                                "Airships possess engines and aerodynamic control surfaces for directional steering, whereas free balloons drift entirely at the mercy of prevailing winds.",
                                "Balloons operate using high-speed jet turbines, while airships rely on glider wings.",
                                "Airships are permanently anchored to the ground by heavy steel mooring cables."
                            ],
                            "answer": "B",
                            "explanation": "Both balloons and airships are lighter-than-air vehicles that generate lift through buoyancy; however, airships are equipped with propulsion engines and rudders to steer independently, whereas balloons drift with wind currents."
                        }
                    }
                ],
                # Page 11: Summary & Core Takeaways
                [
                    {
                        "type": "summary",
                        "title": "Core Takeaways: Categories and Functions of Aircraft",
                        "content": {
                            "title": "Summary & Synthesis",
                            "summary_points": [
                                "Aircraft divide into Lighter-Than-Air (buoyancy displacement) and Heavier-Than-Air (dynamic aerodynamic lift) families.",
                                "Airships differ from balloons by possessing propulsion engines and steering controls for scheduled navigation.",
                                "Fixed-wing airplanes offer high passenger/cargo capacity and fast cruise speeds, but require long prepared runways.",
                                "Rotary-wing helicopters provide unmatched vertical takeoff, landing, and stationary hover capability, vital for medical evacuation and mountain rescue."
                            ]
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 1.1.5: Demonstrating Lift, Buoyancy, and Aviation Development
        # =====================================================================
        {
            "unit_order": 4,
            "unit_name": "Demonstrating Lift, Buoyancy, and Aviation Development",
            "unit_description": "Experimental physics of flight, comparing buoyant flotation with aerodynamic airfoil lift, paper glider modeling, and aerodrome safety boundaries.",
            "lesson_title": "Demonstrating Lift, Buoyancy, and Aviation Development",
            "pages": [
                # Page 1: Visual Hook & Objectives
                [
                    {
                        "type": "suggested_image",
                        "title": "Aerodynamic Paper Glider Folded for Maximum Glide Ratio",
                        "content": {
                            "title": "Aerodynamic Modeling in the Classroom",
                            "caption": "A precision-folded paper glider demonstrating cambered wings and winglet balance, embodying the aerodynamic principles of fixed-wing flight.",
                            "resolved_image_url": "https://upload.wikimedia.org/wikipedia/commons/b/bc/Glybbs_Paper_Plane.jpg"
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Learning Focus: Demonstrating Lift and Buoyancy",
                        "content": {
                            "title": "Learning Focus: Demonstrating Lift and Buoyancy",
                            "goals": [
                                "Contrast the physical mechanisms generating buoyant lift versus dynamic aerodynamic lift.",
                                "Execute safe classroom modeling experiments using folded paper gliders to evaluate glide ratios.",
                                "Analyze how wing aspect ratio and elevon control surfaces alter aircraft pitch and stability.",
                                "Enforce mandatory safety boundaries prohibiting model launches near aerodromes and high-voltage power lines."
                            ]
                        }
                    }
                ],
                # Page 2: Key Terminology
                [
                    {
                        "type": "definition_card",
                        "title": "Experimental Flight Terminology",
                        "content": {
                            "title": "Aerodynamic Physics Vocabulary",
                            "definitions": [
                                {
                                    "term": "Aerodynamic Lift",
                                    "definition": "The mechanical upward force generated by the forward motion of a cambered wing through air, creating a pressure differential between the upper and lower surfaces.",
                                    "example": "Lift supporting a flying paper airplane or a commercial Boeing 787."
                                },
                                {
                                    "term": "Buoyant Lift",
                                    "definition": "The static upward force exerted on an object immersed in a fluid (or air) equal to the weight of the fluid displaced, requiring zero forward airspeed.",
                                    "example": "A helium balloon floating stationary inside a hangar."
                                },
                                {
                                    "term": "Aerodynamic Model",
                                    "definition": "A physical, mathematical, or scaled digital representation of an aircraft used to investigate aerodynamic forces, airflow stability, and glide efficiency.",
                                    "example": "Folded paper gliders and wind-tunnel scale models."
                                },
                                {
                                    "term": "Glide Ratio",
                                    "definition": "The ratio of horizontal distance traveled forward to the vertical distance lost during unpowered flight.",
                                    "example": "A glider with a 10:1 glide ratio travels 10 meters forward for every 1 meter it descends."
                                }
                            ]
                        }
                    }
                ],
                # Page 3: Core Explanation (Floating vs. Flying)
                [
                    {
                        "type": "concept_explanation",
                        "title": "The Physics of Beating Gravity: Floating vs. Flying",
                        "content": {
                            "title": "Two Distinct Solutions to Gravity",
                            "text": "To conquer gravity, aeronautics exploits two fundamentally different physical principles:\n\n- **Buoyancy (Static Flotation)**:\n  - Governed by **Archimedes' Principle**.\n  - An object rises because its average density is less than the surrounding atmosphere.\n  - Generates lift without any forward velocity. A balloon can sit motionless in midair.\n\n- **Aerodynamic Lift (Dynamic Pressure)**:\n  - Governed by **Bernoulli's Principle** and **Newton's Third Law of Motion**.\n  - An object requires constant **forward airspeed** provided by thrust or gravity.\n  - Air travels faster over the curved upper surface of a wing, creating lower atmospheric pressure above than below ($P_{lower} > P_{upper}$), producing an upward net force ($L$).\n  - When a paper airplane runs out of forward speed due to drag, aerodynamic lift collapses, and gravity pulls it to the ground."
                        }
                    }
                ],
                # Page 4: Technical Diagram Block
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Aerodynamic Airfoil Lift vs. Hydrostatic Buoyant Lift",
                        "content": {
                            "title": "Physics Comparison: Airfoil vs. Buoyant Envelope",
                            "caption": "Airflow acceleration and pressure differential across an airfoil versus fluid displacement in a buoyant envelope."
                        }
                    }
                ],
                # Page 5: Comparative Analysis Table
                [
                    {
                        "type": "comparison_table",
                        "title": "Direct Comparison: Buoyancy vs. Aerodynamic Lift",
                        "content": {
                            "title": "Buoyancy vs. Aerodynamic Lift Mechanics",
                            "headers": ["Parameter", "Buoyant Lift (Flotation)", "Aerodynamic Lift (Flight)"],
                            "rows": [
                                ["Physical Law", "Archimedes' Principle (fluid displacement)", "Bernoulli's Principle & Newton's 3rd Law (flow deflection)"],
                                ["Forward Speed", "Zero airspeed required (can float stationary)", "Strict minimum forward airspeed required (stall speed)"],
                                ["Primary Mechanism", "Less dense gas (helium/hot air) trapped in envelope", "Pressure difference created by air rushing over cambered wing"],
                                ["Limiting Factor", "Envelope volume and gas leakage / cooling", "Thrust, drag, air density, and angle of attack"],
                                ["Classroom Model", "Lightweight sealed gas balloon", "Folded paper glider dart or wide-wing soaring glider"]
                            ]
                        }
                    }
                ],
                # Page 6: Step-by-Step Practical Investigation
                [
                    {
                        "type": "step_process",
                        "title": "Classroom Aerodynamic Glider Investigation",
                        "content": {
                            "title": "Step-by-Step Flight Investigation Procedure",
                            "steps": [
                                "1. Airframe Folding (Design A - Dart): Fold an A4 sheet into a narrow, sharp-nosed classic dart optimized for high speed and direct penetration.",
                                "2. Airframe Folding (Design B - Wide Glider): Fold a second A4 sheet into a wide, broad-winged glider with turned-up wingtips (winglets) for maximum lift.",
                                "3. Controlled Launch Protocol: Stand in an unobstructed school hall. Ensure launch zone is clear of people. Release both models horizontally with identical forward thrust.",
                                "4. Metric Recording: Measure the total distance flown and elapsed flight time using a stopwatch. Calculate average glide speed and glide ratio.",
                                "5. Control Surface Modification: Make two small 5mm cuts at the trailing edge of both wings to create 'elevons'. Bend them slightly upward and observe the resulting nose-up pitch behavior."
                            ]
                        }
                    }
                ],
                # Page 7: Educational Video Integration
                [
                    {
                        "type": "suggested_video",
                        "title": "The Aerodynamics of Paper Airplanes: Lift, Drag, and Control",
                        "content": {
                            "title": "Aerodynamic Principles of Folded Paper Models",
                            "description": "Discover how changing center of gravity, dihedral angles, and trailing-edge elevons alters lift and stability on folded paper gliders.",
                            "url": "https://www.youtube.com/watch?v=fwfqMPJ0WNY"
                        }
                    }
                ],
                # Page 8: Aviation Safety Rules for Models
                [
                    {
                        "type": "concept_explanation",
                        "title": "Aviation Safety Rules and Model Launch Boundaries",
                        "content": {
                            "title": "Critical Safety Boundaries for Student Experiments",
                            "text": "While classroom modeling is vital for learning, strict safety rules apply to all aerial experiments:\n\n- **No Hazardous Heating**: Open flame burners or compressed gas canisters must never be used by students for buoyancy demonstrations.\n- **Zero Proximity to Aerodromes**: Model gliders, radio-controlled drones, or kites must **never be launched within 10 km of an active airport, aerodrome, or runway approach path**. A model ingested into a turbofan engine can cause catastrophic engine explosion and fatal crashes.\n- **Clearance from Power Lines**: Never fly models near high-voltage electrical distribution lines due to severe electrocution hazards."
                        }
                    }
                ],
                # Page 9: Formative Knowledge Check 1
                [
                    {
                        "type": "knowledge_check",
                        "title": "Diagnostic Check: Glider Energy Balance",
                        "content": {
                            "question": "A student throws a paper glider across a classroom. It glides steadily for 6 seconds before descending gently to the floor. Why does the glider eventually land instead of flying indefinitely?",
                            "options": [
                                "The buoyant gas trapped inside the paper fibers gradually cools down.",
                                "Aerodynamic drag continuously opposes forward motion, reducing airspeed until the wings can no longer produce enough lift to counteract the aircraft's weight.",
                                "The atmospheric air pressure inside the classroom drops to zero.",
                                "The paper material absorbs moisture from the air, instantly quadrupling its structural weight."
                            ],
                            "answer": "B",
                            "explanation": "Because a paper glider lacks an engine to supply forward thrust, aerodynamic drag gradually slows the glider down. As airspeed decreases, dynamic lift decays until gravity pulls the aircraft down to the ground."
                        }
                    }
                ],
                # Page 10: Formative Knowledge Check 2
                [
                    {
                        "type": "knowledge_check",
                        "title": "Diagnostic Check: Safety Boundaries",
                        "content": {
                            "question": "Which of the following represents an illegal and life-threatening safety hazard when operating model gliders, kites, or aerial drones?",
                            "options": [
                                "Launching folded paper gliders inside an empty school classroom",
                                "Flying models in an open sports field located 200 meters from an active commercial airport runway approach path",
                                "Constructing models from 80gsm lightweight drawing paper",
                                "Testing paper aircraft when there is zero ambient wind"
                            ],
                            "answer": "B",
                            "explanation": "Operating any unmanned aerial vehicle, kite, or model aircraft near airport runways creates a severe hazard of Foreign Object Damage (FOD) or collision with landing aircraft, violating civil aviation regulations."
                        }
                    }
                ],
                # Page 11: Summary & Core Takeaways
                [
                    {
                        "type": "summary",
                        "title": "Core Takeaways: Demonstrating Lift and Buoyancy",
                        "content": {
                            "title": "Summary & Synthesis",
                            "summary_points": [
                                "Buoyancy lifts aircraft statically through fluid displacement, while aerodynamic lift requires forward airspeed across curved wings.",
                                "Paper gliders provide authentic aerodynamic models to study wing aspect ratio, glide ratio, and control surface deflection.",
                                "Deflecting the trailing edges of wings upward (elevons) increases downward force on the tail, pitching the aircraft nose upward.",
                                "Model aviation experiments must strictly honor civil aviation safety regulations, never operating near runways or electrical transmission lines."
                            ]
                        }
                    }
                ]
            ]
        }
    ]

def ingest_grade10_aviation_topic1(replace=False):
    """Ingests Grade 10 Aviation Topic 1 into the database."""
    print("=" * 80)
    print("VLEARN INGESTION ENGINE: Grade 10 Aviation — Topic 1")
    print("Foundations of Aviation Technology")
    print("=" * 80)

    curriculum = Curriculum.objects.get(id=5)
    grade = Grade.objects.get(id=5, level=10)
    subject = Subject.objects.get(id=44, grade=grade)

    print(f"[*] Curriculum: {curriculum.name} (ID: {curriculum.id})")
    print(f"[*] Grade:      {grade.name} (ID: {grade.id}, Level: {grade.level})")
    print(f"[*] Subject:    {subject.name} (ID: {subject.id})")

    topic, created = Topic.objects.get_or_create(
        subject=subject,
        order=0,
        defaults={"name": "Foundations of Aviation Technology"}
    )
    if not created:
        topic.name = "Foundations of Aviation Technology"
        topic.save()
    print(f"[*] Topic:      {topic.name} (ID: {topic.id})")

    curriculum_data = build_topic1_curriculum()
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
                # Update existing lesson
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
    print("[SUCCESS] Grade 10 Aviation Topic 1 Ingestion Complete!")
    print(f"[*] Total Lessons Ingested: {total_lessons}")
    print(f"[*] Total Pages/Cards:      {total_pages}")
    print(f"[*] Total Blocks Created:   {total_blocks}")
    print("=" * 80)

if __name__ == "__main__":
    replace_flag = "--replace" in sys.argv
    ingest_grade10_aviation_topic1(replace=replace_flag)
