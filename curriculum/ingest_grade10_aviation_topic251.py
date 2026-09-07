"""
VLearn Grade 10 Aviation — Topic 251: Airport Safety and Operations
Production Ingestion Engine

Curriculum: CBC (Curriculum ID: 5)
Grade: Grade 10 (Grade ID: 5, Level: 10)
Subject: Aviation (Subject ID: 44)
Topic: Airport Safety and Operations (Topic ID: 251, Order: 4)

Ingests 5 Comprehensive Learning Units & Lessons (~52 Concept Cards):
  1. Airport Zones: Landside, Terminal, and Airside (10 Cards)
  2. Safety Measures in Airport Areas (11 Cards)
  3. Airport Safety Signs and Movement Rules (10 Cards)
  4. Demonstrating Airport Safety Procedures (10 Cards)
  5. Airport Safety Careers and Observation (11 Cards)

Usage:
  ./venv/bin/python curriculum/ingest_grade10_aviation_topic251.py [--replace]
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
    """Removes bracket citations [10, 71], internal visual prompt text, and normalizes typography."""
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

def build_topic251_curriculum():
    """Returns the pedagogical page and block structure for Grade 10 Aviation Topic 251."""
    return [
        # =====================================================================
        # LESSON 1: Airport Zones: Landside, Terminal, and Airside
        # =====================================================================
        {
            "unit_order": 0,
            "unit_name": "Airport Zones: Landside, Terminal, and Airside",
            "unit_description": "Explore the physical and regulatory zones of an airport, distinguishing aerodromes from airports and mapping the transition between public, transitional, and secure operational areas.",
            "lesson_title": "Airport Zones: Landside, Terminal, and Airside",
            "pages": [
                # Card 1: Visual Hook & Learning Objectives
                [
                    {
                        "type": "suggested_image",
                        "title": "Jomo Kenyatta International Airport Terminal Architecture",
                        "content": {
                            "title": "Jomo Kenyatta International Airport Terminal Architecture",
                            "caption": "The exterior terminal building at Jomo Kenyatta International Airport (JKIA) in Nairobi, illustrating the architectural boundary between public landside areas and secure operational aviation zones.",
                            "resolved_image_url": "https://upload.wikimedia.org/wikipedia/commons/6/61/Jomo_Kenyatta_International_Airport_terminal_building.jpg"
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Learning Focus: Airport Zones",
                        "content": {
                            "title": "Learning Focus: Airport Zones",
                            "goals": [
                                "Distinguish between a general aerodrome and a certified commercial airport.",
                                "Identify the three fundamental airport zones: Landside, Terminal, and Airside.",
                                "Trace the physical transition and security screening sequence from public curbside to secure boarding gate.",
                                "Explain why strict access controls and physical perimeter barriers are vital to airport security."
                            ]
                        }
                    }
                ],
                # Card 2: Foundational Terminology
                [
                    {
                        "type": "definition_card",
                        "title": "Core Airport Zoning Terminology",
                        "content": {
                            "title": "Core Technical Vocabulary",
                            "definitions": [
                                {
                                    "term": "Aerodrome",
                                    "definition": "Any defined area on land or water (including buildings, installations, and equipment) intended to be used either wholly or in part for the arrival, departure, and surface movement of aircraft.",
                                    "example": "A remote grass bush airstrip in the Maasai Mara or a sea-plane docking cove."
                                },
                                {
                                    "term": "Airport",
                                    "definition": "A certified aerodrome that satisfies specific national and international regulatory standards, equipped with commercial passenger terminals, cargo handling facilities, and customs/security infrastructure.",
                                    "example": "Jomo Kenyatta International Airport (JKIA) or Moi International Airport Mombasa."
                                },
                                {
                                    "term": "Landside",
                                    "definition": "The public area of the airport where passengers, visitors, and ground transportation have unrestricted access without an airline ticket or security badge.",
                                    "example": "Public access roads, parking garages, and public ticketing lobbies."
                                },
                                {
                                    "term": "Terminal",
                                    "definition": "The transitional building where passengers check in, undergo mandatory security and border screening, and prepare to board departing flights.",
                                    "example": "Check-in counters, passenger security lanes, and boarding departure gates."
                                },
                                {
                                    "term": "Airside",
                                    "definition": "The highly secured and restricted operational area of the aerodrome where aircraft operate, park, refuel, and maneuver under strict air traffic control.",
                                    "example": "Aircraft parking aprons, taxiways, active runways, and maintenance hangars."
                                }
                            ]
                        }
                    }
                ],
                # Card 3: Aerodrome vs Airport Concept Explanation
                [
                    {
                        "type": "concept_explanation",
                        "title": "Distinguishing Aerodromes from Airports",
                        "content": {
                            "title": "The Hierarchy of Flight Facilities",
                            "text": "Before examining specific airport zones, we must clarify a fundamental aviation distinction:\n\n- **Every airport is an aerodrome**, but **not every aerodrome is an airport**.\n- An **aerodrome** is the broad legal and scientific term for any location prepared for aircraft takeoff, landing, and surface movement. A grassy airstrip in a national park used by wildlife safari charters is an aerodrome: it has a runway, windsock, and tie-down spots, but lacks commercial terminals or customs offices.\n- An **airport** is a fully certified, high-infrastructure aerodrome. It must comply with international standards (such as ICAO Annex 14) and national civil aviation regulations (such as Kenya Civil Aviation Authority protocols). It provides passenger security screening, automated baggage carousels, air traffic control towers, and international border clearance."
                        }
                    }
                ],
                # Card 4: Technical Diagram Block
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Airport 3-Zone Architecture: Landside, Terminal, and Airside",
                        "content": {
                            "title": "Airport Three-Zone Security Blueprint",
                            "caption": "Architectural breakdown illustrating how public landside roadways transition through terminal security barriers into restricted airside aprons, taxiways, and runways."
                        }
                    }
                ],
                # Card 5: Comparative Zone Analysis Table
                [
                    {
                        "type": "comparison_table",
                        "title": "Comparative Analysis: The Three Airport Operational Zones",
                        "content": {
                            "title": "Airport Operational Zones Matrix",
                            "headers": ["Zone", "Access Level", "Key Facilities", "Security Requirement"],
                            "rows": [
                                ["Landside", "Unrestricted Public", "Roadways, parking lots, bus drops, public terminal concourse", "No ticket or government ID required for entry"],
                                ["Terminal (Transitional)", "Mixed / Filtered", "Check-in desks, security scanners, customs, departure gates", "Boarding pass and government-issued travel identification"],
                                ["Airside", "Strictly Restricted", "Parking apron, taxiways, active runways, hangars, fuel farms", "Valid crew badge, airside driving permit, or escort"]
                            ]
                        }
                    }
                ],
                # Card 6: Real-World Case Study (JKIA Nairobi)
                [
                    {
                        "type": "real_world_example",
                        "title": "Zoning Architecture at Jomo Kenyatta International Airport (JKIA)",
                        "content": {
                            "title": "Layered Defense in Kenya's Primary Hub",
                            "text": "At **Jomo Kenyatta International Airport (JKIA)** in Nairobi, the zoning concept is applied through layered physical boundaries:\n\n- **Landside Perimeter**: Vehicles entering from Airport South Road must first pass through an outer vehicular screening checkpoint before approaching terminal parking structures.\n- **Terminal Separator**: Terminals 1A, 1B, 1C, 1D, and Terminal 2 serve as physical barriers. Passengers in the departure hall can look through floor-to-ceiling glass directly onto the tarmac, but cannot step through without clearing immigration and security.\n- **Airside Apron**: Only certified ground handlers, Kenya Airways flight crew, and authorized fuelers wearing high-visibility gear and background-cleared identity badges operate on the tarmac.\n- **Perimeter Security**: Steel fencing with intrusion sensors and CCTV cameras surrounds the entire multi-kilometer airfield boundary to prevent unauthorized entry."
                        }
                    }
                ],
                # Card 7: Educational Video Integration
                [
                    {
                        "type": "suggested_video",
                        "title": "Airport Operations: Aerodrome, Airport, Landside, Terminal, and Airside",
                        "content": {
                            "title": "Airport Operations: Visual Layout and Zoning Principles",
                            "description": "Visual walkthrough of real airport physical layouts, illustrating the spatial and regulatory distinctions between landside public roadways, passenger terminals, and airside aircraft operational aprons.",
                            "url": "https://www.youtube.com/watch?v=B0Ar5WsUhWs"
                        }
                    }
                ],
                # Card 8: Safety Connection & Operational Boundaries
                [
                    {
                        "type": "concept_explanation",
                        "title": "Airside Boundary Breaches: Hazards and Responses",
                        "content": {
                            "title": "The Dangers of Unauthorized Airside Entry",
                            "text": "Consider what happens if an untrained person enters the airside zone through an open service door:\n\n- **Physical Hazards**: Active aprons are filled with dynamic risks: spinning jet turbines capable of sucking in human bodies, 600 km/h hot jet blast exhaust, reversing baggage tractors, and high-voltage ground power cables.\n- **Operational Lockdown**: An unauthorized person on the airside triggers an immediate security alert. Ground movements halt, landing planes may be instructed to hold or go around, and security tactical units intercept the intruder.\n- **Golden Rule**: Passengers and non-cleared staff must remain inside marked public corridors. Crossing onto airside surfaces is strictly prohibited except via enclosed jet bridges or supervised passenger transfer vehicles."
                        }
                    }
                ],
                # Card 9: Formative Knowledge Check 1
                [
                    {
                        "type": "knowledge_check",
                        "title": "Formative Check: Aerodrome vs. Airport Classification",
                        "content": {
                            "question": "Which of the following statements accurately describes the difference between an aerodrome and an airport?",
                            "options": [
                                "Airports are used only for military fighter jets, while aerodromes are used only for civilian hot-air balloons.",
                                "All airports are aerodromes, but not all aerodromes are airports, as airports must meet specific regulatory certification standards.",
                                "An aerodrome always contains passenger shops, customs terminals, and baggage carousels, while an airport is simply a dirt landing strip.",
                                "Aerodromes are restricted to water landings, while airports must be built on flat land."
                            ],
                            "answer": "B",
                            "explanation": "The term 'aerodrome' is the comprehensive technical and legal definition for any defined area prepared for aircraft operations. An 'airport' is a specialized, certified aerodrome equipped with commercial passenger terminals, cargo infrastructure, and customs clearance."
                        }
                    }
                ],
                # Card 10: Formative Knowledge Check 2 & Unit Summary
                [
                    {
                        "type": "knowledge_check",
                        "title": "Formative Check: Identifying Operational Zones",
                        "content": {
                            "question": "A passenger is standing at the public check-in desk inside an airport terminal building buying a flight ticket. Which airport zone are they currently occupying?",
                            "options": [
                                "The Airside Operational Zone",
                                "The Active Runway Zone",
                                "The Landside portion of the Terminal",
                                "The Flight Deck Zone"
                            ],
                            "answer": "C",
                            "explanation": "The check-in lobby is situated within the terminal building, but because it is freely accessible to the general public before security screening, it represents the landside portion of the terminal."
                        }
                    },
                    {
                        "type": "summary",
                        "title": "Key Takeaways: Airport Zones",
                        "content": {
                            "title": "Core Unit Synthesis",
                            "summary_points": [
                                "An aerodrome is any defined area for aircraft takeoff and landing; an airport is a certified commercial facility with terminals and customs.",
                                "Landside encompasses unrestricted public spaces including access roadways, car parks, and curbside check-in concourses.",
                                "The Terminal serves as a transitional filter separating public visitors from screened, ticketed passengers.",
                                "Airside comprises high-security operational zones including aprons, taxiways, and runways where only authorized personnel may enter."
                            ]
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 2: Safety Measures in Airport Areas
        # =====================================================================
        {
            "unit_order": 1,
            "unit_name": "Safety Measures in Airport Areas",
            "unit_description": "Analyze airside and landside hazards including Foreign Object Debris (FOD), jet blast, prop wash, and electrical bonding protocols during aircraft fueling.",
            "lesson_title": "Safety Measures in Airport Areas",
            "pages": [
                # Card 1: Visual Hook & Learning Objectives
                [
                    {
                        "type": "suggested_image",
                        "title": "Crew Conducting a Coordinated Airfield FOD Walk-Down",
                        "content": {
                            "title": "Coordinated Foreign Object Debris (FOD) Inspection",
                            "caption": "Aviation crew members walking in a coordinated line to inspect the surface and collect loose debris, preventing catastrophic foreign object ingestion by high-thrust aircraft turbine engines.",
                            "resolved_image_url": "https://upload.wikimedia.org/wikipedia/commons/8/8f/US_Navy_030309-N-9964S-019_Crew_members_gather_on_the_ship%27s_bow_to_participate_in_a_foreign_object_damage_%28FOD%29_walk-down.jpg"
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Learning Focus: Airport Safety Measures",
                        "content": {
                            "title": "Learning Focus: Airport Safety Measures",
                            "goals": [
                                "Identify critical hazards across Landside, Terminal, and Airside environments.",
                                "Explain the causes and severe consequences of Foreign Object Debris (FOD) engine ingestion.",
                                "Analyze the aerodynamic forces and thermal risks of jet blast and propeller wash.",
                                "Describe the precise step-by-step electrical bonding and grounding procedures used during aircraft refueling."
                            ]
                        }
                    }
                ],
                # Card 2: Foundational Terminology
                [
                    {
                        "type": "definition_card",
                        "title": "Aviation Safety and Hazard Terminology",
                        "content": {
                            "title": "Core Technical Vocabulary",
                            "definitions": [
                                {
                                    "term": "Foreign Object Debris (FOD)",
                                    "definition": "Any loose item, substance, or particle on an airfield surface (such as loose bolts, rocks, luggage tags, or soda cans) that could potentially damage aircraft structures or engines.",
                                    "example": "A dropped steel wrench on a taxiway that gets drawn into a jet turbine."
                                },
                                {
                                    "term": "Jet Blast",
                                    "definition": "The rapid, high-temperature, high-velocity exhaust stream produced behind an operating turbine jet engine.",
                                    "example": "Thrust exhaust exceeding 600 km/h capable of flipping baggage carts or injuring workers."
                                },
                                {
                                    "term": "Prop Wash",
                                    "definition": "The high-velocity airflow pushed rearward by spinning propeller blades on turboprop or piston aircraft.",
                                    "example": "Turbulent wind blast that can dislodge loose ground equipment on an apron."
                                },
                                {
                                    "term": "Electrical Bonding & Grounding",
                                    "definition": "Connecting the aircraft airframe and fueling vehicle to a common grounding point using conductive cables to safely dissipate static electricity.",
                                    "example": "Attaching a heavy copper clamp to an apron earthing rod before opening fuel valves."
                                },
                                {
                                    "term": "Blast Deflector Fence",
                                    "definition": "A curved aerodynamic barrier made of heavy steel installed behind aircraft run-up and parking positions to redirect hot jet exhaust safely skyward.",
                                    "example": "Perimeter blast walls protecting airport access roads and terminal glass."
                                }
                            ]
                        }
                    }
                ],
                # Card 3: Zone Hazards and Safety Controls Matrix
                [
                    {
                        "type": "comparison_table",
                        "title": "Airport Safety Measures by Operational Zone",
                        "content": {
                            "title": "Airport Safety Measures Matrix",
                            "headers": ["Zone", "Primary Hazards", "Mandatory Safety Controls"],
                            "rows": [
                                ["Landside", "Vehicular traffic collisions, pedestrian falls, unattended luggage security threats", "Strict roadway speed limits, zebra crossings, continuous CCTV patrols, vehicle screening checkpoints"],
                                ["Terminal", "Unscreened weapons/contraband, passenger stampedes, baggage conveyor belt entrapment", "Metal detectors, multi-view baggage X-ray scanners, fire sprinkler systems, emergency escape pathways"],
                                ["Airside", "FOD ingestion, jet blast/prop wash, fuel vapor ignition, high-noise hearing loss", "Daily walk-down FOD sweeps, blast deflector fences, electrical bonding cords, mandatory hi-vis vests and ear defenders"]
                            ]
                        }
                    }
                ],
                # Card 4: Technical Diagram Block
                [
                    {
                        "type": "suggested_diagram",
                        "title": "FOD Turbine Ingestion Vector & Refueling Grounding Circuit",
                        "content": {
                            "title": "Aviation Hazard Mechanics: FOD Ingestion and Fueling Safety",
                            "caption": "Engineering diagram contrasting the devastating impact of debris ingestion into a jet turbine compressor with the protective static dissipation circuit of fuel grounding cables."
                        }
                    }
                ],
                # Card 5: Foreign Object Debris (FOD) Ingestion Mechanics
                [
                    {
                        "type": "concept_explanation",
                        "title": "Foreign Object Debris (FOD): Mechanisms and Prevention",
                        "content": {
                            "title": "The Threat of Loose Debris on the Airfield",
                            "text": "A commercial turbofan engine running at takeoff power draws in over 1,000 cubic meters of air every second. The intake creates a powerful vortex like a giant vacuum cleaner:\n\n- **Turbine Blade Ingestion**: If a stray bolt or pebble is sucked into the intake, it strikes fan blades spinning at up to 15,000 RPM. The metal blade shatters, sending titanium fragments through subsequent compressor stages, causing engine fire and catastrophic thrust loss.\n- **Tire Blowout Hazard**: Airfield debris can slash heavy airliner tires rolling at 250 km/h during takeoff, causing tire disintegration that can puncture fuel tanks or damage hydraulic lines.\n- **FOD Sweeps**: To eliminate FOD, airports conduct daily coordinated walk-downs where personnel march shoulder-to-shoulder scanning the tarmac, supplemented by magnetic sweeper trucks that collect metallic objects."
                        }
                    }
                ],
                # Card 6: Jet Blast and Blast Deflector Engineering
                [
                    {
                        "type": "concept_explanation",
                        "title": "Jet Blast, Prop Wash, and Aerodynamic Deflectors",
                        "content": {
                            "title": "Taming High-Energy Exhaust Gases",
                            "text": "Jet blast is not merely wind—it is a concentrated torrent of superheated gas and kinetic force:\n\n- **Force Profile**: A wide-body airliner at breakaway thrust generates exhaust winds exceeding 600 km/h with temperatures reaching 300°C. This force can effortlessly overturn maintenance vans, shatter terminal windows, or launch ground personnel into the air.\n- **Safety Zones**: Ground crews must obey strict exclusion zones marked on the tarmac behind aircraft engines during pushback and taxi.\n- **Blast Deflector Fences**: Airports install curved, heavy-gauge steel louvered walls behind engine testing positions and parking stands. The aerodynamic curve redirects horizontal high-speed gas straight upward into the atmosphere, creating a protective wind-shadow behind the barrier."
                        }
                    }
                ],
                # Card 7: Educational Video Integration
                [
                    {
                        "type": "suggested_video",
                        "title": "Jet Fuel Safety: Hazards, PPE, and Grounding Protocols",
                        "content": {
                            "title": "Aircraft Refueling Safety: Static Bonding and PPE",
                            "description": "Demonstrates the vital procedures for handling volatile aviation jet fuels, highlighting static electrical bonding cables, grounding stakes, exclusion zones, and protective equipment.",
                            "url": "https://www.youtube.com/watch?v=H4L_Coqawz8"
                        }
                    }
                ],
                # Card 8: Fueling Safety and Static Electrical Bonding Sequence
                [
                    {
                        "type": "step_process",
                        "title": "Standard Operating Procedure: Aircraft Refueling Bonding Sequence",
                        "content": {
                            "title": "Step-by-Step Aircraft Fuel Grounding Sequence",
                            "steps": [
                                {
                                    "step_number": 1,
                                    "title": "Ground Stake Connection",
                                    "description": "Connect the primary grounding cable from the fuel bowser or hydrant dispenser to the certified earth ground stake embedded in the concrete apron."
                                },
                                {
                                    "step_number": 2,
                                    "title": "Chassis-to-Airframe Bonding",
                                    "description": "Connect a heavy conductive copper bonding wire between the fuel truck metal chassis and the designated grounding lug on the aircraft airframe."
                                },
                                {
                                    "step_number": 3,
                                    "title": "Fuel Nozzle Bonding",
                                    "description": "Attach the nozzle bonding cable to the fuel receiver receptacle before uncapping the fuel port or connecting pressure delivery hoses."
                                },
                                {
                                    "step_number": 4,
                                    "title": "Safe Disconnection Order",
                                    "description": "After fuel delivery is complete and the cap is resealed, disconnect cables in exact reverse order: nozzle cable first, airframe bond second, ground stake last."
                                }
                            ]
                        }
                    }
                ],
                # Card 9: Real-World Case Study (Moi International Airport Mombasa)
                [
                    {
                        "type": "real_world_example",
                        "title": "Airside FOD Mitigation at Moi International Airport",
                        "content": {
                            "title": "Coastal Environmental Hazards in Mombasa",
                            "text": "At **Moi International Airport** in Mombasa, high coastal humidity and marine salt-spray accelerate metal oxidation on ground service equipment:\n\n- **Corrosion Risks**: Vibrations from heavy cargo loaders can cause corroded bolts, nuts, and washers to shear off and drop onto taxiways.\n- **Magnetic Sweep Sweepers**: The Kenya Airports Authority (KCAA/KAA) operates specialized runway sweeper vehicles equipped with industrial electromagnets that comb the runway and apron every morning before the arrival of scheduled international flights.\n- **Preventative Culture**: Ramp handlers are trained to report and retrieve any loose hardware immediately, embodying the aviation principle: 'See FOD, pick up FOD'."
                        }
                    }
                ],
                # Card 10: Formative Knowledge Check 1
                [
                    {
                        "type": "knowledge_check",
                        "title": "Formative Check: Purpose of Blast Deflector Fences",
                        "content": {
                            "question": "Why are blast deflector fences installed around aircraft parking aprons and engine testing areas?",
                            "options": [
                                "To block heavy tropical rain from wetting passenger terminal windows.",
                                "To deflect high-velocity, hot exhaust gases from running jet engines upward, protecting ground vehicles and personnel.",
                                "To prevent passengers from climbing over the fences to touch parked aircraft wings.",
                                "To guide migratory birds away from nesting inside maintenance hangars."
                            ],
                            "answer": "B",
                            "explanation": "Operating jet engines produce intense thrust with exhaust speeds over 600 km/h. Blast deflector fences use curved steel slats to redirect this hazardous horizontal force upward into the sky, shielding ground workers and terminal buildings."
                        }
                    }
                ],
                # Card 11: Formative Knowledge Check 2 & Unit Summary
                [
                    {
                        "type": "knowledge_check",
                        "title": "Formative Check: Aircraft Fueling Grounding Protocols",
                        "content": {
                            "question": "Before starting fuel pumping operations, a ground crew member connects a copper wire from the fuel truck to a metal ground stake and the aircraft's metal frame. What safety risk is this action preventing?",
                            "options": [
                                "Propeller damage from prop wash wind forces.",
                                "Engine ingestion of loose metal fasteners.",
                                "Static electricity sparking and igniting highly flammable fuel vapors.",
                                "Corrosion of the aircraft wings due to coastal sea salt."
                            ],
                            "answer": "C",
                            "explanation": "Fuel flowing through high-pressure hoses generates static electrical charge due to friction. Grounding and bonding equalizes electrical potential and bleeds static safely into the earth, preventing an electrical spark that could ignite volatile fuel vapors."
                        }
                    },
                    {
                        "type": "summary",
                        "title": "Key Takeaways: Airport Safety Measures",
                        "content": {
                            "title": "Core Unit Synthesis",
                            "summary_points": [
                                "Landside safety focuses on traffic flow, vehicle screening, and public access control.",
                                "Foreign Object Debris (FOD) represents an extreme threat to turbine engines and high-speed tires, requiring daily walk-downs and magnetic sweeps.",
                                "Jet blast produces devastating kinetic and thermal forces safely mitigated by exclusion zones and blast deflector fences.",
                                "Aircraft refueling requires disciplined 3-point static bonding to prevent explosive ignition of fuel vapors."
                            ]
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 3: Airport Safety Signs and Movement Rules
        # =====================================================================
        {
            "unit_order": 2,
            "unit_name": "Airport Safety Signs and Movement Rules",
            "unit_description": "Decode the universal color-coded airfield signage system (Mandatory, Location, Direction, and Warning) and master apron pedestrian and vehicular movement rules.",
            "lesson_title": "Airport Safety Signs and Movement Rules",
            "pages": [
                # Card 1: Visual Hook & Learning Objectives
                [
                    {
                        "type": "suggested_image",
                        "title": "Airfield Taxiway Guidance Signs and Pavement Markings",
                        "content": {
                            "title": "Standardized Airfield Guidance Signage",
                            "caption": "Standardized black location signs and yellow direction indicators positioned along an active airfield taxiway, providing unambiguous navigation guidance to pilots and ground vehicle operators.",
                            "resolved_image_url": "https://upload.wikimedia.org/wikipedia/commons/b/b1/Taxiway_8255.JPG"
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Learning Focus: Airfield Signage & Movement Rules",
                        "content": {
                            "title": "Learning Focus: Airfield Signage & Movement Rules",
                            "goals": [
                                "Classify airfield signs into Mandatory, Location, Direction, and Warning categories.",
                                "Apply universal pilot memory mnemonics: 'Black square, you're there' and 'Yellow array points the way'.",
                                "Identify runway Hold Short lines and explain the causes and prevention of runway incursions.",
                                "Outline strict airside movement protocols for pedestrians, support vehicles, and taxiing aircraft."
                            ]
                        }
                    }
                ],
                # Card 2: Foundational Terminology
                [
                    {
                        "type": "definition_card",
                        "title": "Airfield Navigation and Signage Terminology",
                        "content": {
                            "title": "Core Technical Vocabulary",
                            "definitions": [
                                {
                                    "term": "Mandatory Instruction Sign",
                                    "definition": "A critical red sign with bold white lettering indicating a mandatory stopping point where aircraft and vehicles must halt before entering an active runway or critical zone.",
                                    "example": "A red placard reading '15-33' marking the entrance to Runway 15-33."
                                },
                                {
                                    "term": "Location Sign",
                                    "definition": "A sign featuring a black background with yellow lettering and a yellow border that confirms the exact taxiway or runway the pilot or vehicle is currently on.",
                                    "example": "A black sign showing the yellow letter 'B' confirming you are on Taxiway Bravo."
                                },
                                {
                                    "term": "Direction Sign",
                                    "definition": "A yellow sign with black lettering and arrows indicating the turning direction and designation of intersecting taxiways.",
                                    "example": "A yellow sign displaying 'A →' indicating that turning right leads to Taxiway Alpha."
                                },
                                {
                                    "term": "Runway Incursion",
                                    "definition": "Any unauthorized occurrence on an active aerodrome runway involving an aircraft, vehicle, person, or animal that creates a collision hazard.",
                                    "example": "A baggage cart driving across an active runway without Air Traffic Control clearance."
                                },
                                {
                                    "term": "Hold Short Line",
                                    "definition": "A physical pavement marking consisting of two solid and two dashed yellow lines painted across a taxiway marking the exact stop threshold before a runway.",
                                    "example": "Stopping on the solid line side until receiving verbal tower clearance."
                                }
                            ]
                        }
                    }
                ],
                # Card 3: Universal Airport Sign Families Matrix
                [
                    {
                        "type": "comparison_table",
                        "title": "Universal Airfield Sign Families and Color Codes",
                        "content": {
                            "title": "Universal Airfield Sign Matrix",
                            "headers": ["Sign Family", "Color Scheme", "Operational Meaning", "Memory Rule / Example"],
                            "rows": [
                                ["Mandatory Instruction", "Red background, white lettering", "Absolute stop required; do not cross without explicit ATC clearance", "Red = Stop / Runway entrance [ 15-33 ]"],
                                ["Location Sign", "Black background, yellow lettering", "Identifies the current taxiway or runway you are currently on", "'Black square, you're there' [ B ]"],
                                ["Direction Sign", "Yellow background, black lettering", "Identifies designation and turn direction of intersecting taxiways", "'Yellow array points the way' [ A → ]"],
                                ["Warning / Caution", "Yellow or Orange with black hazard graphics", "Alerts personnel to hazards such as low-flying aircraft or jet blast", "Caution: Jet Blast Hazard Zone"]
                            ]
                        }
                    }
                ],
                # Card 4: Technical Diagram Block
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Airfield Universal Sign Matrix & Pavement Markings",
                        "content": {
                            "title": "Airfield Visual Navigation Matrix",
                            "caption": "Comprehensive guide illustrating Mandatory Runway Hold signs, Location taxiway markers, Direction arrows, and pavement Hold Short line geometry."
                        }
                    }
                ],
                # Card 5: Runway Incursions and Pavement Hold Short Lines
                [
                    {
                        "type": "concept_explanation",
                        "title": "Runway Incursions and Pavement Hold Short Discipline",
                        "content": {
                            "title": "Preventing the Deadliest Airfield Hazard",
                            "text": "A **runway incursion** is among the most hazardous events in aviation. Because landing aircraft touch down at speeds exceeding 250 km/h, an unexpected vehicle or plane on the runway can result in a fatal catastrophe:\n\n- **The Hold Short Line**: Painted across taxiways leading to runways are four parallel yellow lines: two solid lines on the taxiway side and two dashed lines on the runway side.\n- **Stop Threshold**: Approaching the runway, you face the **solid lines**. You must stop completely before your nose gear crosses the first solid line.\n- **Tower Clearance Mandatory**: You may cross only when Air Traffic Control (ATC) states your exact vehicle callsign and issues verbal clearance: *'Maintain vehicle two, cross Runway 06.'*\n- **Exiting the Runway**: When vacating a runway, crossing from the dashed side to the solid side is permitted without stopping, clearing the runway quickly for following traffic."
                        }
                    }
                ],
                # Card 6: Airside Movement Rules: Pedestrians and Vehicles
                [
                    {
                        "type": "concept_explanation",
                        "title": "Movement Rules for Pedestrians and Ground Vehicles",
                        "content": {
                            "title": "Operational Discipline on the Active Apron",
                            "text": "Operating on the airside requires adherence to strict traffic and pedestrian safety rules:\n\n- **Pedestrian Corridors**: Unescorted walking on the apron is strictly forbidden. Personnel must use painted green walking lanes and remain within designated service envelopes.\n- **Mandatory PPE**: High-visibility reflective vests and hearing protection (ear defenders) must be worn at all times.\n- **Right-of-Way Hierarchy**: Aircraft under tow or taxiing under engine power **always have absolute right-of-way**. Emergency vehicles (ARFF) have second priority, followed by scheduled passenger shuttle buses, and lastly ground servicing tractors.\n- **Apron Speed Limits**: Vehicles on the ramp must observe strict speed limits (typically 20 km/h on open apron roads and 5 km/h in the vicinity of parked aircraft)."
                        }
                    }
                ],
                # Card 7: Educational Video Integration
                [
                    {
                        "type": "suggested_video",
                        "title": "Airport Signs, Markings, and Lighting Explained",
                        "content": {
                            "title": "Airfield Signage and Markings Cockpit Walkthrough",
                            "description": "An in-depth cockpit and ground-level perspective explaining how runway markings, taxiway centerlines, illuminated signage, and hold-short lines direct pilots safely across active aerodromes.",
                            "url": "https://www.youtube.com/watch?v=Yacx4jNQlgo"
                        }
                    }
                ],
                # Card 8: Real-World Case Study (Wilson Airport Nairobi)
                [
                    {
                        "type": "real_world_example",
                        "title": "Airfield Navigation Rigor at Wilson Airport",
                        "content": {
                            "title": "Complex Runway Geometry in Nairobi",
                            "text": "**Wilson Airport** in Nairobi is one of the busiest general aviation and flight training hubs in Africa, featuring two intersecting runways (Runway 07/25 and Runway 14/32) and numerous taxiways:\n\n- **Intensive Traffic Mix**: Student pilots, turboprop safari charters, and humanitarian relief flights share the airfield constantly.\n- **Airside Driving Certification**: Anyone driving a maintenance vehicle, fuel truck, or baggage tug at Wilson Airport must complete specialized airfield training and pass an exam identifying all signs, markings, and radio phraseology.\n- **Zero Tolerance**: Missing a red mandatory hold sign or crossing a hold-short line without ATC clearance results in immediate revocation of airside driving privileges and mandatory re-training."
                        }
                    }
                ],
                # Card 9: Formative Knowledge Check 1
                [
                    {
                        "type": "knowledge_check",
                        "title": "Formative Check: Mandatory Airfield Sign Action",
                        "content": {
                            "question": "A ground support vehicle is taxiing on the airfield and approaches an illuminated sign with a solid red background and white lettering reading '08-26'. What action must the driver take?",
                            "options": [
                                "Speed up to cross the runway as quickly as possible.",
                                "Stop completely and do not cross the painted hold line until explicit verbal clearance is received from the Air Traffic Control tower.",
                                "Drive slowly across the runway while flashing the vehicle headlights.",
                                "Ignore the sign because red signs apply only to heavy multi-engine commercial airliners."
                            ],
                            "answer": "B",
                            "explanation": "A red sign with white lettering is a Mandatory Instruction Sign designating a runway holding position. All vehicles, pedestrians, and aircraft must stop and hold their position until Air Traffic Control issues explicit verbal radio clearance to cross."
                        }
                    }
                ],
                # Card 10: Formative Knowledge Check 2 & Unit Summary
                [
                    {
                        "type": "knowledge_check",
                        "title": "Formative Check: Decoding Location Signs",
                        "content": {
                            "question": "You are driving a service vehicle on the airport ramp and observe an illuminated sign displaying a black background with a yellow letter 'C'. What information does this sign convey?",
                            "options": [
                                "'Caution: low flying helicopters operating ahead.'",
                                "'Check-in terminal building is located to your left.'",
                                "'You are currently located on Taxiway Charlie.'",
                                "'Clearance has been canceled by air traffic control.'"
                            ],
                            "answer": "C",
                            "explanation": "Using the standard aviation pilot memory tip 'Black square, you're there', a black sign with yellow lettering is a Location Sign confirming the specific taxiway (Taxiway Charlie) currently being occupied."
                        }
                    },
                    {
                        "type": "summary",
                        "title": "Key Takeaways: Airport Signs & Movement Rules",
                        "content": {
                            "title": "Core Unit Synthesis",
                            "summary_points": [
                                "Mandatory Signs (Red/White) require an immediate halt and cannot be passed without explicit Air Traffic Control clearance.",
                                "Location Signs (Black/Yellow) confirm current position ('Black square, you're there').",
                                "Direction Signs (Yellow/Black) provide navigational guidance to intersecting routes ('Yellow array points the way').",
                                "Runway Hold Short lines mark the boundary between taxiways and active runways to prevent catastrophic runway incursions."
                            ]
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 4: Demonstrating Airport Safety Procedures
        # =====================================================================
        {
            "unit_order": 3,
            "unit_name": "Demonstrating Airport Safety Procedures",
            "unit_description": "Structure the five-step passenger screening sequence, emergency terminal evacuation routes, and critical classroom simulation protocols.",
            "lesson_title": "Demonstrating Airport Safety Procedures",
            "pages": [
                # Card 1: Visual Hook & Learning Objectives
                [
                    {
                        "type": "suggested_image",
                        "title": "Passenger Security Screening Checkpoint in an International Terminal",
                        "content": {
                            "title": "Terminal Passenger Security Screening",
                            "caption": "Aviation security personnel conducting non-intrusive personal screening at a secure terminal checkpoint to prevent unauthorized weapons, liquids, or prohibited items from entering restricted airside areas.",
                            "resolved_image_url": "https://upload.wikimedia.org/wikipedia/commons/9/9b/Security_screening_selectee.jpg"
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Learning Focus: Demonstrating Airport Safety Procedures",
                        "content": {
                            "title": "Learning Focus: Demonstrating Airport Safety Procedures",
                            "goals": [
                                "Detail the 5-step passenger and baggage security screening sequence.",
                                "Distinguish prohibited weapons from dangerous goods restrictions, notably lithium-ion battery fire hazards.",
                                "Analyze terminal emergency evacuation protocols, alarm responses, and assembly procedures.",
                                "Demonstrate structured teamwork and situational awareness in classroom simulation drills."
                            ]
                        }
                    }
                ],
                # Card 2: Foundational Terminology
                [
                    {
                        "type": "definition_card",
                        "title": "Terminal Safety and Emergency Terminology",
                        "content": {
                            "title": "Core Technical Vocabulary",
                            "definitions": [
                                {
                                    "term": "Security Screening",
                                    "definition": "The technical and physical inspection of passengers and their baggage using X-ray scanners, walk-through metal detectors, and explosive trace detection to intercept prohibited items.",
                                    "example": "Passing carry-on luggage through multi-energy X-ray machines at the security checkpoint."
                                },
                                {
                                    "term": "Emergency Evacuation Plan",
                                    "definition": "A pre-established, diagrammed procedure for clearing all occupants rapidly and safely from terminal buildings to designated muster points during a crisis.",
                                    "example": "Following illuminated green running-man exit signs during a terminal fire alarm."
                                },
                                {
                                    "term": "Prohibited Items",
                                    "definition": "Articles or substances that could be used as weapons or pose severe danger to aircraft safety and are legally banned from carriage into secure airside areas or aircraft cabins.",
                                    "example": "Knives, firearms, explosive materials, and flammable aerosols."
                                },
                                {
                                    "term": "Thermal Runaway",
                                    "definition": "An uncontrollable, rapid self-heating chemical reaction within a damaged or defective lithium-ion battery that produces intense fire and toxic gases.",
                                    "example": "A short-circuited high-capacity power bank catching fire in an enclosed space."
                                },
                                {
                                    "term": "Assembly Point",
                                    "definition": "A designated open, safe outdoor area situated far from terminal structures and active taxiways where evacuated occupants gather for roll-call.",
                                    "example": "Marked muster fields in landside parking lots or fenced airside perimeter zones."
                                }
                            ]
                        }
                    }
                ],
                # Card 3: Five-Step Passenger Screening Sequence
                [
                    {
                        "type": "step_process",
                        "title": "The Five-Step Passenger Security Screening Chain",
                        "content": {
                            "title": "Step-by-Step Passenger Screening Chain",
                            "steps": [
                                {
                                    "step_number": 1,
                                    "title": "Travel Document & Boarding Pass Verification",
                                    "description": "Security personnel verify the traveler's authentic passport and scan the electronic boarding pass to authenticate departure access."
                                },
                                {
                                    "step_number": 2,
                                    "title": "Personal Divestment of Metals and Electronics",
                                    "description": "The traveler places jackets, belts, loose coins, watches, and large electronics (laptops, tablets) into screening plastic trays."
                                },
                                {
                                    "step_number": 3,
                                    "title": "X-Ray Baggage Conveyance",
                                    "description": "Carry-on bags and trays enter the dual-energy X-ray tunnel where automated algorithms and screeners examine internal contents for weapons and liquids."
                                },
                                {
                                    "step_number": 4,
                                    "title": "Personal Body Screening",
                                    "description": "The passenger passes through a walk-through metal detector (WTMD) or millimeter-wave whole-body scanner to detect concealed metallic and non-metallic threats."
                                },
                                {
                                    "step_number": 5,
                                    "title": "Item Re-claim or Secondary Physical Search",
                                    "description": "Cleared items are retrieved by the passenger. Any suspicious anomaly triggers a manual bag search or explosive trace swab inspection."
                                }
                            ]
                        }
                    }
                ],
                # Card 4: Technical Diagram Block
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Passenger Security Screening Sequence & Emergency Evacuation Flowchart",
                        "content": {
                            "title": "Terminal Operational Flowcharts: Security and Evacuation",
                            "caption": "Dual visual process model showing the linear passenger screening chain contrasted with the branched emergency terminal evacuation protocol."
                        }
                    }
                ],
                # Card 5: Prohibited Items and Lithium-Ion Battery Hazards
                [
                    {
                        "type": "concept_explanation",
                        "title": "Dangerous Goods: The Lithium-Ion Battery Hazard",
                        "content": {
                            "title": "Why Power Banks Are Banned from Checked Baggage",
                            "text": "Passengers often wonder why airport check-in agents ask: *'Do you have any spare lithium batteries or power banks in your checked suitcase?'*\n\n- **Thermal Runaway**: Lithium-ion batteries pack immense energy. If dropped, crushed, or manufactured with internal defects, they can enter **thermal runaway**, reaching temperatures over 600°C within seconds and spraying fiery jets of molten chemicals.\n- **The Cargo Hold Risk**: If a lithium battery catches fire inside a suitcase in the pressurized cargo bay under the passenger cabin, automated fire extinguishing systems (like Halon gas) may suppress flames, but cannot cool down the battery core. The heat can reignite and burn through the aircraft skin.\n- **Cabin Carry-On Rule**: In the passenger cabin, flight attendants have fire-containment thermal bags and water to extinguish and cool burning devices immediately. Therefore, spare power banks must always travel in carry-on baggage and are strictly prohibited in checked hold luggage."
                        }
                    }
                ],
                # Card 6: Terminal Emergency Evacuation Procedures
                [
                    {
                        "type": "concept_explanation",
                        "title": "Terminal Emergency Evacuation Procedures",
                        "content": {
                            "title": "Orderly Evacuation Protocols in High-Density Facilities",
                            "text": "In the event of an active fire alarm, structural emergency, or critical security threat, airport terminal occupants follow structured life-safety protocols:\n\n- **Immediate Alarm Response**: Audible horn sirens and high-intensity strobe flashes activate across all concourses alongside automated multilingual public address warnings.\n- **Halt Operations Immediately**: All check-in transactions, boarding queues, and retail sales stop instantly. Staff secure cash drawers and direct passengers to exit doors.\n- **Follow Green Exit Signs**: Occupants walk steadily toward the nearest illuminated green emergency exit sign. Never use escalators or elevators during an evacuation.\n- **Zero Backtracking**: Passengers must never return to retrieve luggage, purchases, or passports. Human life and rapid egress take absolute priority over property."
                        }
                    }
                ],
                # Card 7: Educational Video Integration
                [
                    {
                        "type": "suggested_video",
                        "title": "Emergency Medical Response: Hands-Only CPR in Aviation Terminals",
                        "content": {
                            "title": "Terminal Emergency Care: Hands-Only CPR",
                            "description": "Demonstrates the vital lifesaving technique of Hands-Only CPR, highlighting chest compression rate and rhythm (100–120 bpm) essential for medical first responders in crowded airport passenger concourses.",
                            "url": "https://www.youtube.com/watch?v=hblmFtbyYKQ"
                        }
                    }
                ],
                # Card 8: Real-World Case Study (Eldoret International Airport Drills)
                [
                    {
                        "type": "real_world_example",
                        "title": "Annual Full-Scale Emergency Drills at Eldoret International Airport",
                        "content": {
                            "title": "Simulating Disasters to Validate Emergency Readiness",
                            "text": "Every two years, **Eldoret International Airport** conducts a comprehensive, full-scale emergency simulation mandated by the International Civil Aviation Organization (ICAO) and KCAA:\n\n- **Multi-Agency Integration**: The drill simulates an aircraft gear collapse or terminal fire, mobilizing the airport rescue and firefighting team, Uasin Gishu County fire engines, police bomb disposal units, and local hospital ambulances.\n- **Evacuation Testing**: Hundreds of volunteer students act as passengers, allowing airport authorities to test terminal public address clarity, evacuation bottleneck clearance times, triage tents, and family assistance center workflows.\n- **Audited Performance**: Strict records are evaluated to ensure response times meet international standards (such as fire rescue reaching any runway point within three minutes)."
                        }
                    }
                ],
                # Card 9: Formative Knowledge Check 1
                [
                    {
                        "type": "knowledge_check",
                        "title": "Formative Check: Lithium-Ion Battery Restrictions",
                        "content": {
                            "question": "Why are high-capacity lithium-ion power banks strictly prohibited from being placed inside checked baggage in the aircraft cargo hold?",
                            "options": [
                                "They add too much weight to the aircraft cargo compartment balance.",
                                "They can overheat and enter thermal runaway, producing intense fires that are extremely difficult to detect and extinguish inside an unmanned cargo bay.",
                                "They generate electromagnetic waves that jam the aircraft satellite navigation antennas.",
                                "They emit odors that attract pests and rodents into the cargo bay."
                            ],
                            "answer": "B",
                            "explanation": "Lithium-ion batteries carry the risk of thermal runaway, leading to rapid, high-temperature fires. In the passenger cabin, crew can immediately extinguish and cool the device with water, whereas an undetected fire in the cargo hold can cause catastrophic structural failure."
                        }
                    }
                ],
                # Card 10: Formative Knowledge Check 2 & Unit Summary
                [
                    {
                        "type": "knowledge_check",
                        "title": "Formative Check: Terminal Fire Evacuation Action",
                        "content": {
                            "question": "If an audible fire alarm sounds inside the airport terminal, what is the correct safety response for passenger check-in staff?",
                            "options": [
                                "Lock all checked baggage inside desk drawers and wait for passengers to return.",
                                "Immediately halt passenger processing, leave non-essential items behind, and guide passengers toward the nearest illuminated green Emergency Exit.",
                                "Finish checking in the current passenger's suitcases to avoid flight departure delays.",
                                "Run down into the baggage basement to retrieve their personal belongings."
                            ],
                            "answer": "B",
                            "explanation": "Under standard aviation emergency operating procedures, human life safety overrides commercial operations and flight schedules. Staff must cease processing immediately and usher passengers out through marked emergency exits without backtracking for belongings."
                        }
                    },
                    {
                        "type": "summary",
                        "title": "Key Takeaways: Airport Safety Procedures",
                        "content": {
                            "title": "Core Unit Synthesis",
                            "summary_points": [
                                "The 5-step security screening sequence ensures prohibited weapons, liquids, and dangerous items do not enter the secure airside.",
                                "Lithium-ion batteries present severe thermal runaway fire risks and must strictly be carried in cabin baggage, never in checked baggage.",
                                "Terminal emergency evacuations prioritize human life over property, requiring immediate response without backtracking for possessions.",
                                "Regular multi-agency simulation drills maintain emergency preparedness and ensure compliance with KCAA and ICAO safety standards."
                            ]
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 5: Airport Safety Careers and Observation
        # =====================================================================
        {
            "unit_order": 4,
            "unit_name": "Airport Safety Careers and Observation",
            "unit_description": "Examine the roles of Air Traffic Controllers, Airport Security Officers, Ground Handlers, Airport Firefighters (ARFF), and Safety Managers within a unified SMS framework.",
            "lesson_title": "Airport Safety Careers and Observation",
            "pages": [
                # Card 1: Visual Hook & Learning Objectives
                [
                    {
                        "type": "suggested_image",
                        "title": "Rosenbauer Panther Aircraft Rescue and Firefighting (ARFF) Crash Tender",
                        "content": {
                            "title": "Rosenbauer Panther ARFF Crash Tender",
                            "caption": "A specialized heavy ARFF crash vehicle stationed on an airport ramp, engineered for high-speed acceleration and massive chemical foam delivery to suppress intense aircraft jet fuel fires.",
                            "resolved_image_url": "https://upload.wikimedia.org/wikipedia/commons/f/fc/Airport_crash_tender_-_Rosenbauer_Panther_-_Airport_Budapest_%289437%29.jpg"
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Learning Focus: Airport Safety Careers",
                        "content": {
                            "title": "Learning Focus: Airport Safety Careers",
                            "goals": [
                                "Examine the core responsibilities of five essential airport safety professions.",
                                "Differentiate the specialized equipment and operational environments of ARFF, ATC, Ramp Handlers, Security, and Safety Managers.",
                                "Explain how a centralized Safety Management System (SMS) coordinates safety reporting across all departments.",
                                "Analyze the multi-agency sequence of actions required during an airside fuel spill or aircraft emergency."
                            ]
                        }
                    }
                ],
                # Card 2: Foundational Terminology
                [
                    {
                        "type": "definition_card",
                        "title": "Airport Safety Careers Terminology",
                        "content": {
                            "title": "Core Technical Vocabulary",
                            "definitions": [
                                {
                                    "term": "Air Traffic Controller (ATC)",
                                    "definition": "A licensed aviation professional who manages the safe, orderly, and expeditious flow of aircraft on runways, taxiways, and throughout designated airspace.",
                                    "example": "Ground controllers issuing taxi routes and Tower controllers issuing landing clearances."
                                },
                                {
                                    "term": "Airport Security Officer (AVSEC)",
                                    "definition": "A certified officer responsible for safeguarding civil aviation against acts of unlawful interference through screening, patrols, and surveillance.",
                                    "example": "Officers screening passenger luggage and monitoring terminal CCTV surveillance."
                                },
                                {
                                    "term": "Ground Handling Specialist",
                                    "definition": "Airside personnel who service aircraft on the parking apron, including marshalling, chocking, baggage loading, and ground power connection.",
                                    "example": "A ramp agent using illuminated wands to guide an aircraft safely into its gate."
                                },
                                {
                                    "term": "ARFF Firefighter",
                                    "definition": "An Aircraft Rescue and Firefighting specialist trained to operate high-performance crash tenders and extinguish intense volatile aviation fuel fires.",
                                    "example": "Crews operating high-capacity foam cannons on rapid-intervention crash tenders."
                                },
                                {
                                    "term": "Safety Management System (SMS)",
                                    "definition": "A systematic, data-driven framework implemented across an aerodrome to proactively identify hazards, analyze operational risks, and maintain continuous safety oversight.",
                                    "example": "Auditing runway asphalt friction and running non-punitive incident reporting systems."
                                }
                            ]
                        }
                    }
                ],
                # Card 3: The Airport Safety Team Ecosystem Matrix
                [
                    {
                        "type": "comparison_table",
                        "title": "The Airport Safety Professions Matrix",
                        "content": {
                            "title": "Airport Safety Careers Matrix",
                            "headers": ["Career Role", "Primary Operating Zone", "Core Safety Tools", "Key Mandate"],
                            "rows": [
                                ["Air Traffic Controller (ATC)", "Control Tower / Airside", "Ground radar, VHF radios, electronic flight strips", "Ensure collision-free separation between moving aircraft and ground vehicles"],
                                ["Airport Security Officer (AVSEC)", "Terminal & Landside Gates", "X-ray scanners, walk-through metal detectors, perimeter CCTV", "Prevent unauthorized weapons, prohibited items, and illegal airside entry"],
                                ["Ground Handling Agent", "Airside Apron / Ramp", "Marshalling wands, wheel chocks, static bonding wires, hi-vis PPE", "Safely service parked aircraft without damage to airframes or personnel"],
                                ["ARFF Airport Firefighter", "Airside Fire Station & Ramp", "Heavy foam crash tenders, thermal imaging cameras, heat-resistant bunker suits", "Rescue aircraft occupants and suppress catastrophic fuel fires within 3 minutes"],
                                ["Airport Safety Manager", "Administration / Entire Aerodrome", "SMS risk assessment matrices, runway friction testers, audit checklists", "Develop proactive safety policies, conduct audits, and investigate near-miss incidents"]
                            ]
                        }
                    }
                ],
                # Card 4: Technical Diagram Block
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Airport Safety Team Ecosystem & Operational Integration",
                        "content": {
                            "title": "Airport Collaborative Safety Ecosystem",
                            "caption": "Organizational network showing how the Airport Safety Manager and SMS framework unify the operational actions of ATC, ARFF, Ramp Handlers, and Security Officers."
                        }
                    }
                ],
                # Card 5: Airside Control and Rescue: ATC and ARFF
                [
                    {
                        "type": "concept_explanation",
                        "title": "Airside Guardians: Air Traffic Controllers and ARFF Crews",
                        "content": {
                            "title": "Precision Guidance and Rapid Suppression",
                            "text": "The airside requires continuous technical coordination and immediate emergency capability:\n\n- **Air Traffic Controllers**: Operating from the glass aerodrome tower, ATCs act as the nerve center. Tower controllers oversee takeoff and landing spacing on active runways, while Ground controllers direct fuel trucks, baggage tugs, and taxiing jets through complex intersections to eliminate runway incursions.\n- **ARFF Firefighters**: Aviation fuel fires burn at temperatures exceeding 1,000°C. ARFF crews operate specialized crash trucks capable of accelerating from 0 to 80 km/h in under 25 seconds while carrying up to 12,000 liters of water and Aqueous Film-Forming Foam (AFFF). International regulations require ARFF vehicles to reach any point of an active commercial runway within three minutes of an alarm."
                        }
                    }
                ],
                # Card 6: Apron & Terminal Defense: Ramp Agents and Security
                [
                    {
                        "type": "concept_explanation",
                        "title": "Ramp and Terminal Defenders: Ground Handlers and Security",
                        "content": {
                            "title": "Frontline Operations and Boundary Protection",
                            "text": "Safety is maintained at every contact point between passenger and airplane:\n\n- **Ground Handling Specialists**: When an aircraft docks, ramp agents position heavy rubber wheel chocks against the tires to prevent rolling, position safety cones around wingtips and engine cowlings, connect ground power units (GPUs), and inspect the airframe for surface damage.\n- **Aviation Security (AVSEC) Officers**: Working in terminals and at perimeter access gates, security officers verify that every individual entering the airside possesses a valid security pass. They screen cargo consignments and patrol fence lines to eliminate contraband and trespass hazards."
                        }
                    }
                ],
                # Card 7: Educational Video Integration
                [
                    {
                        "type": "suggested_video",
                        "title": "Human Factors in Aviation Safety and Maintenance",
                        "content": {
                            "title": "Human Factors in Airport Operations",
                            "description": "Explores how psychological awareness, fatigue management, clear communication, and structured safety checklists prevent critical human errors in aviation operations.",
                            "url": "https://www.youtube.com/watch?v=FViSA91DP-8"
                        }
                    }
                ],
                # Card 8: Emergency Collaboration: The Apron Fuel Spill Scenario
                [
                    {
                        "type": "concept_explanation",
                        "title": "Collaborative Response: Multi-Agency Fuel Spill Protocol",
                        "content": {
                            "title": "The Safety Team in Action: Coordinated Hazard Response",
                            "text": "When a pressurized fuel hose ruptures during aircraft turnaround, spilling 150 liters of volatile jet fuel onto the apron, the entire safety team synchronizes:\n\n- **1. Ground Handler**: Instantly activates the emergency fuel shutoff switch, evacuates the immediate parking bay, and alerts the cockpit crew.\n- **2. Tower ATC**: Notified by radio, the ground controller closes adjacent taxiways and holds all taxiing aircraft away from volatile vapor clouds.\n- **3. ARFF Firefighters**: Crash tenders arrive on scene within two minutes, blanketing the fuel pool with chemical foam to prevent ignition from hot brake assemblies.\n- **4. Safety Manager**: Initiates a formal SMS incident investigation to determine why the hose failed, ordering fleet-wide inspections of fueling couplings."
                        }
                    }
                ],
                # Card 9: Real-World Case Study (Wilson Airport Safety Committee)
                [
                    {
                        "type": "real_world_example",
                        "title": "Wilson Airport Safety Committee and SMS Oversight",
                        "content": {
                            "title": "Collaborative Risk Management in Practice",
                            "text": "At **Wilson Airport** in Nairobi, the Airport Safety Manager convenes monthly Safety Action Group meetings uniting representatives from all airfield stakeholders:\n\n- **Cross-Disciplinary Team**: Flight instructors from pilot academies, charter airline dispatchers, ground fuel vendors, Kenya Police Air Wing officers, and KCAA air traffic controllers meet face-to-face.\n- **Hazard Reporting**: If a pilot notes that wild birds congregate near Runway 25 or a ramp agent reports poor evening floodlighting near Apron 2, the issue is logged into the SMS matrix.\n- **Corrective Actions**: The Safety Manager assigns resources to install sonic bird repellents and upgrade ramp LED lighting, proving that safety is a continuous collaborative cycle."
                        }
                    }
                ],
                # Card 10: Formative Knowledge Check 1
                [
                    {
                        "type": "knowledge_check",
                        "title": "Formative Check: Surface Aircraft Movement Authority",
                        "content": {
                            "question": "Which airport professional possesses the certified regulatory authority to direct the movement of aircraft on active taxiways and runways to ensure safe physical separation?",
                            "options": [
                                "Airport Security Officer (AVSEC)",
                                "Air Traffic Controller (ATC)",
                                "Ramp Ground Handling Agent",
                                "Airport Safety Manager"
                            ],
                            "answer": "B",
                            "explanation": "Air Traffic Controllers (specifically Ground and Tower controllers) are legally certified and equipped with radio communication and ground radar to issue binding taxi, takeoff, and landing clearances that maintain safe separation between aircraft."
                        }
                    }
                ],
                # Card 11: Formative Knowledge Check 2 & Unit Summary
                [
                    {
                        "type": "knowledge_check",
                        "title": "Formative Check: Aircraft Rescue & Firefighting (ARFF) Vehicles",
                        "content": {
                            "question": "An airport firefighter operates specialized Aircraft Rescue and Firefighting (ARFF) vehicles. Why does their operational equipment differ fundamentally from standard city fire engines?",
                            "options": [
                                "Airport firefighters only extinguish small wastebasket fires inside passenger terminals.",
                                "Aircraft crashes involve vast volumes of volatile aviation fuel, demanding high-speed acceleration and roof turrets that spray chemical foam to smother liquid fires instantly.",
                                "Standard municipal fire engines are too heavy to drive on engineered airport tarmac.",
                                "Airport firefighters are primarily responsible for loading oversized passenger baggage."
                            ],
                            "answer": "B",
                            "explanation": "Aviation fuel fires burn with extreme heat and spread across concrete surfaces rapidly. ARFF crash tenders are built for off-road speed (0-80 km/h in <25s) and carry specialized foam systems (AFFF) with roof turrets capable of blanketing burning jet fuel from a safe distance."
                        }
                    },
                    {
                        "type": "summary",
                        "title": "Key Takeaways: Airport Safety Careers",
                        "content": {
                            "title": "Core Unit Synthesis",
                            "summary_points": [
                                "Airfield safety relies on an interconnected ecosystem of ATCs, ARFF crews, ramp agents, security officers, and safety managers.",
                                "Air Traffic Controllers ensure surface and airborne separation, while ARFF provides rapid, specialized fuel-fire suppression.",
                                "Ground handlers protect airframes and ramp personnel through strict chocking, bonding, and marshalling protocols.",
                                "The Airport Safety Manager uses the Safety Management System (SMS) to investigate hazards proactively and cultivate a culture of open reporting."
                            ]
                        }
                    }
                ]
            ]
        }
    ]

def ingest_grade10_aviation_topic251(replace=False):
    """Executes the ingestion of Topic 251 for Grade 10 Aviation."""
    print("=" * 80)
    print("VLearn Curriculum Ingestion Engine: Grade 10 Aviation — Topic 251")
    print("=" * 80)

    # 1. Fetch Topic 251 strictly
    topic = Topic.objects.filter(id=251, subject_id=44).first()
    if not topic:
        print("[ERROR] Topic 251 (Subject ID: 44) not found in database!")
        sys.exit(1)

    print(f"[*] Target Topic: [{topic.id}] {topic.name} (Order: {topic.order})")
    print(f"[*] Subject:      [{topic.subject.id}] {topic.subject.name} (Grade: {topic.subject.grade.name})")

    curriculum_data = build_topic251_curriculum()

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
    print("[SUCCESS] Grade 10 Aviation Topic 251 Ingestion Complete!")
    print(f"[*] Total Lessons Ingested: {total_lessons}")
    print(f"[*] Total Pages/Cards:      {total_pages}")
    print(f"[*] Total Blocks Created:   {total_blocks}")
    print("=" * 80)

if __name__ == "__main__":
    replace_flag = "--replace" in sys.argv
    ingest_grade10_aviation_topic251(replace=replace_flag)
