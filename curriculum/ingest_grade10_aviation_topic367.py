"""
VLearn Grade 10 Aviation — Topic 367: The Airport: Structure and Operations (Subject ID: 44, Topic ID: 367)
Production Ingestion Engine

Curriculum: CBC (Curriculum ID: 5)
Grade: Grade 10 (Grade ID: 5, Level: 10)
Subject: Aviation (Subject ID: 44)
Topic: The Airport: Structure and Operations (Topic ID: 367, Order: 9)

Ingests 5 Comprehensive Learning Units & Lessons (50 Concept Cards):
  1. Categories of Airports (Kenya & International) (Unit order: 0, Unit ID: 2922) [10 Cards]
  2. Functions of Major Areas of an Airport (Unit order: 1, Unit ID: 2923) [10 Cards]
  3. Runway Designation and Numbering (Unit order: 2, Unit ID: 2924) [10 Cards]
  4. Runway Visual Markings and Signs (Unit order: 3, Unit ID: 2925) [10 Cards]
  5. Airport Operations & Air Traffic Control (Unit order: 4, Unit ID: 2926) [10 Cards]

Usage:
  ./venv/bin/python curriculum/ingest_grade10_aviation_topic367.py [--replace]
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
    # Clean latex glitches like $ightarrow$
    text = text.replace(r'$ightarrow$', '→').replace(r'$\rightarrow$', '→')
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

def build_topic367_curriculum():
    """Returns the pedagogical page and block structure for Grade 10 Aviation Topic 367."""
    return [
        # =====================================================================
        # LESSON 1: Categories of Airports (Kenya & International)
        # =====================================================================
        {
            "unit_order": 0,
            "unit_id": 2922,
            "unit_name": "Categories of Airports (Kenya & International)",
            "unit_description": "Classification of aerodromes and certified airports: exploring ICAO airport reference codes, Categories A through E, Kenyan aerodromes from international hubs to safari airstrips, and emergency services.",
            "lesson_title": "Categories of Airports (Kenya & International)",
            "pages": [
                # Card 1 (Page 1): Photographic Hook & Learning Objectives
                [
                    {
                        "type": "suggested_image",
                        "title": "Jomo Kenyatta International Airport Aerial Overview",
                        "content": {
                            "title": "Jomo Kenyatta International Airport Aerial Overview",
                            "caption": "An aerial perspective of Jomo Kenyatta International Airport (JKIA) in Nairobi, Kenya's primary Category A international hub handling widebody long-haul aircraft.",
                            "resolved_image_url": "https://upload.wikimedia.org/wikipedia/commons/8/87/Jomo_Kenyatta_International_Airport_%28JKIA%29.jpg"
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Learning Focus: Airport Categories & Classifications",
                        "content": {
                            "title": "Learning Focus: Airport Categories & Classifications",
                            "goals": [
                                "Distinguish between a general aerodrome and a certified commercial airport based on international safety regulations.",
                                "Classify aerodromes into standard Categories A through E based on runway length, pavement strength, and handling capability.",
                                "Categorize major Kenyan aerodromes including JKIA, Wilson Airport, Kisumu, and Maasai Mara safari airstrips.",
                                "Evaluate how Aircraft Rescue and Firefighting (ARFF) categories dictate aircraft operational permissions."
                            ]
                        }
                    }
                ],
                # Card 2 (Page 2): Key Terminology
                [
                    {
                        "type": "definition_card",
                        "title": "Foundational Airport Classification Terminology",
                        "content": {
                            "title": "Core Airport & Aerodrome Vocabulary",
                            "definitions": [
                                {
                                    "term": "Aerodrome",
                                    "definition": "Any defined area on land or water, including buildings and equipment, intended wholly or in part for the arrival, departure, and surface movement of aircraft.",
                                    "example": "A grass bush strip in the Maasai Mara or a floating marine helipad."
                                },
                                {
                                    "term": "Airport",
                                    "definition": "A certified aerodrome meeting stringent civil aviation safety, security, perimeter fencing, and passenger processing standards for scheduled commercial operations.",
                                    "example": "Jomo Kenyatta International Airport (JKIA) in Nairobi."
                                },
                                {
                                    "term": "Kenya Airports Authority (KAA)",
                                    "definition": "The statutory body established by law to construct, operate, maintain, and manage certified aerodromes across Kenya.",
                                    "example": "KAA manages major facilities including JKIA, Moi International, and Wilson Airport."
                                },
                                {
                                    "term": "Category A Hub",
                                    "definition": "A premier international gateway engineered with heavy-duty paved runways over 3,000 meters, full customs and border security, and high-tier emergency response.",
                                    "example": "Moi International Airport Mombasa accommodating long-haul international flights."
                                },
                                {
                                    "term": "ARFF",
                                    "definition": "Aircraft Rescue and Firefighting: the dedicated airport emergency rescue unit certified to extinguish high-intensity aviation fuel fires within strict response times.",
                                    "example": "JKIA maintains Category 9 ARFF readiness to protect widebody aircraft."
                                }
                            ]
                        }
                    }
                ],
                # Card 3 (Page 3): Concept Explanation: Aerodromes vs. Airports
                [
                    {
                        "type": "concept_explanation",
                        "title": "Aerodromes Versus Certified Airports",
                        "content": {
                            "title": "The Regulatory Distinction in Aviation Infrastructure",
                            "text": "The terms 'aerodrome' and 'airport' are frequently used interchangeably, but civil aviation law establishes an essential regulatory distinction:\n\n- **All airports are aerodromes, but not all aerodromes are airports.**\n- An **aerodrome** is the overarching technical term for any designated area on land or water designed for aircraft operations. An unpaved dirt strip on an agricultural ranch or a private helicopter landing spot is an aerodrome.\n- An **airport** is an aerodrome that has satisfied exhaustive certification criteria under the Kenya Civil Aviation Authority (KCAA) and ICAO Annex 14. Certification mandates secure perimeter fencing, lighted paved runways, terminal passenger screening, navigation aids, and specialized emergency rescue crews.\n\nWithout formal certification, an airfield cannot accept scheduled commercial airline flights carrying fare-paying passengers."
                        }
                    }
                ],
                # Card 4 (Page 4): Technical Diagram (SVG Placeholder)
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Airport Classification Pyramid & Operational Capabilities",
                        "content": {
                            "title": "Airport Classification Hierarchy",
                            "caption": "A tiered architectural pyramid comparing Categories A through E, showing runway length requirements, pavement strength ratings, aircraft handling capacities, and Kenyan aerodrome examples."
                        }
                    }
                ],
                # Card 5 (Page 5): In-Depth Concept: The Five Airport Categories
                [
                    {
                        "type": "concept_explanation",
                        "title": "The Five Airport Categories (Categories A through E)",
                        "content": {
                            "title": "Operational Capabilities Across Airport Tiers",
                            "text": "Aviation regulatory bodies classify aerodromes into five operational categories:\n\n- **Category A (Major International Hubs)**: Engineered for intercontinental widebody jets (Boeing 777, Airbus A350). Features runways exceeding 3,000 meters, round-the-clock customs and immigration, instrument landing systems, and ARFF Category 9 or 10. Key Kenyan examples include Jomo Kenyatta International Airport (JKIA) and Moi International Airport Mombasa.\n- **Category B (Major Domestic & Regional Airports)**: Accommodates regional airliners and turboprops (Embraer 190, Dash 8). Features paved runways of 2,000 to 3,000 meters and scheduled domestic networks. Examples include Kisumu International Airport and Eldoret International Airport.\n- **Category C (County & Secondary Airstrips)**: Handles light commercial charters and utility turboprops (Cessna Caravan, Twin Otter). Features runways of 1,200 to 1,800 meters. Examples include Malindi Airport and Ukunda Airstrip.\n- **Category D (Unpaved Local Bush Airstrips)**: Remote dirt, grass, or murram strips under 1,200 meters. These lack control towers and terminal buildings; pilots announce intentions on common advisory frequencies. Examples include Keekorok and Musiara airstrips in the Maasai Mara.\n- **Category E (Specialized & Military Aerodromes)**: Private airfields, agricultural airstrips, or defense air bases such as Laikipia Air Base, restricted to authorized flight operations."
                        }
                    }
                ],
                # Card 6 (Page 6): Comparison Table
                [
                    {
                        "type": "comparison_table",
                        "title": "Comparison of Airport Categories A to E",
                        "content": {
                            "title": "Technical and Operational Airport Matrix",
                            "headers": ["Category", "Primary Aircraft Handled", "Runway Surface & Length", "Emergency Response (ARFF)", "Kenyan Example"],
                            "rows": [
                                ["Category A", "Heavy widebody jets (B777, B787, A350)", "Paved asphalt/concrete (>3,000 m)", "Category 9 or 10", "JKIA Nairobi, Moi Int'l Mombasa"],
                                ["Category B", "Regional jets and heavy turboprops (E190, Dash 8)", "Paved asphalt (2,000 – 3,000 m)", "Category 5 to 7", "Kisumu, Eldoret, Wilson"],
                                ["Category C", "Light utility turboprops (Cessna Caravan)", "Paved or compacted gravel (1,200 – 1,800 m)", "Category 3 to 4", "Malindi Airport, Ukunda Airstrip"],
                                ["Category D", "Single-engine bush planes (C172, C206)", "Unpaved grass/dirt (<1,200 m)", "None / Portable fire extinguishers", "Keekorok (Maasai Mara), Samburu"],
                                ["Category E", "Military fighters, trainers, crop dusters", "Specialized paved or unpaved", "Dedicated military rescue", "Laikipia Air Base, private ranches"]
                            ]
                        }
                    }
                ],
                # Card 7 (Page 7): Real-World Example: Wilson Airport Operational Dynamics
                [
                    {
                        "type": "real_world_example",
                        "title": "Wilson Airport: High Traffic in a Category B Framework",
                        "content": {
                            "title": "Wilson Airport: Africa's Busiest General Aviation Hub",
                            "text": "Wilson Airport in Nairobi represents one of the busiest aerodromes in Africa in terms of aircraft movements, recording hundreds of takeoffs and landings daily. However, regulatory classification depends on infrastructure capacity rather than flight count.\n\nBecause Wilson's primary runways (Runway 07/25 at 1,463 meters and Runway 14/32 at 1,560 meters) are not long enough or structurally rated to support heavy widebody passenger airliners, Wilson is classified as a Category B aerodrome. It serves as Kenya's premier operational springboard for domestic safari tourism, air ambulance medevac flights, humanitarian missions, and advanced flight training academies."
                        }
                    }
                ],
                # Card 8 (Page 8): Safety Scenario: Emergency Diversion Planning
                [
                    {
                        "type": "concept_explanation",
                        "title": "Emergency Diversions & Airport Capabilities",
                        "content": {
                            "title": "Safety Protocols in Emergency Airfield Selection",
                            "text": "When an aircraft suffers an in-flight emergency—such as an uncontained engine fire or critical cabin depressurization—the flight crew must execute an immediate diversion. Selecting an aerodrome requires balancing distance against airfield rescue infrastructure:\n\n- **The Danger**: Diverting a fast, 40-passenger regional turboprop to a nearby Category D bush airstrip introduces severe risks: the short unpaved runway may cause runway excursion, and zero firefighting personnel are available to suppress fuel fires.\n- **Standard Operating Procedure**: Flight crews cross-check their Flight Management System (FMS) to identify the nearest suitable aerodrome possessing adequate runway length (Category B or C) and an active Aircraft Rescue and Firefighting (ARFF) station.\n- **Rescue Readiness**: An ARFF team must be capable of deploying foam crash tenders to any spot on the airfield within three minutes of emergency alarm sounding."
                        }
                    }
                ],
                # Card 9 (Page 9): Curated Video Integration
                [
                    {
                        "type": "suggested_video",
                        "title": "Airport Operations: Aerodromes, Airside & Landside Basics",
                        "content": {
                            "title": "Understanding Airport Structure and Operations",
                            "description": "Examine how certified airports organize surface infrastructure, manage security barriers between public and operational zones, and ensure international compliance.",
                            "url": "https://www.youtube.com/watch?v=B0Ar5WsUhWs"
                        }
                    }
                ],
                # Card 10 (Page 10): Formative Knowledge Checks
                [
                    {
                        "type": "knowledge_check",
                        "title": "Diagnostic Check: Aerodrome vs. Airport Distinction",
                        "content": {
                            "question": "What is the primary regulatory difference between an aerodrome and a certified airport?",
                            "options": [
                                "Aerodromes are located only on water surfaces, while airports are built exclusively on land.",
                                "All airports are certified aerodromes meeting strict regulatory safety, security, and operational standards, whereas an aerodrome is any defined area used for aircraft movement.",
                                "Airports are managed exclusively by airline pilots, whereas aerodromes are run by maintenance engineers.",
                                "Aerodromes handle military aircraft exclusively, while airports handle civilian passengers."
                            ],
                            "answer": "B",
                            "explanation": "Aerodrome is the broad technical term for any surface (land or water) where aircraft operate. An airport is a certified aerodrome that satisfies stringent national and international standards including security barriers, rescue services, and navigational equipment."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Diagnostic Check: Jomo Kenyatta International Airport Classification",
                        "content": {
                            "question": "Under which regulatory category is Jomo Kenyatta International Airport (JKIA) classified, and what is its primary operational capability?",
                            "options": [
                                "Category D; accommodating single-engine bush aircraft on unpaved safari strips.",
                                "Category B; restricted to domestic turboprops and regional flight training operations.",
                                "Category A; engineered with long paved runways and high-tier ARFF facilities to handle heavy international widebody aircraft.",
                                "Category E; dedicated to private agricultural spraying and military fighter testing."
                            ],
                            "answer": "C",
                            "explanation": "JKIA is Kenya's primary Category A international hub. Its 4,110-meter paved runway, full instrument landing aids, round-the-clock border customs, and Category 9 ARFF emergency response allow it to accommodate long-haul widebody airliners."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 2: Functions of Major Areas of an Airport
        # =====================================================================
        {
            "unit_order": 1,
            "unit_id": 2923,
            "unit_name": "Functions of Major Areas of an Airport",
            "unit_description": "Airport spatial architecture and operational zoning: Landside public areas, secure Airside transit, terminal processing, apron/ramp ground handling, taxiway movement networks, active runways, and maintenance hangars.",
            "lesson_title": "Functions of Major Areas of an Airport",
            "pages": [
                # Card 1 (Page 1): Photographic Hook & Learning Objectives
                [
                    {
                        "type": "suggested_image",
                        "title": "Commercial Jet on Active Airport Terminal Apron",
                        "content": {
                            "title": "Commercial Jet on Active Airport Terminal Apron",
                            "caption": "A widebody commercial airliner parked on the terminal apron receiving ground handling, baggage loading, and fueling services in the secure airside zone.",
                            "resolved_image_url": "https://upload.wikimedia.org/wikipedia/commons/0/07/Qatar_Airways_Airbus_A380-800_at_Heathrow_Airport_Terminal_4_before_Flying_to_Doha%2C_6_Jan_2015.jpg"
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Learning Focus: Functional Airport Zones",
                        "content": {
                            "title": "Learning Focus: Functional Airport Zones",
                            "goals": [
                                "Differentiate between the public Landside zone and the restricted Airside operational zone.",
                                "Trace passenger, baggage, and aircraft movement through the central terminal building.",
                                "Analyze the functions of airfield operational areas including ramps, taxiways, runways, and maintenance hangars.",
                                "Examine safety protocols on active aprons including high-visibility gear and Foreign Object Debris (FOD) control."
                            ]
                        }
                    }
                ],
                # Card 2 (Page 2): Key Terminology
                [
                    {
                        "type": "definition_card",
                        "title": "Essential Airfield Zoning Terminology",
                        "content": {
                            "title": "Airfield Architectural Vocabulary",
                            "definitions": [
                                {
                                    "term": "Landside",
                                    "definition": "The unrestricted public sector of an airport encompassing access roads, parking complexes, public transit stations, and ticketing lobbies.",
                                    "example": "Family members dropping off travelers outside the terminal departures concourse."
                                },
                                {
                                    "term": "Airside",
                                    "definition": "The secure, perimeter-controlled airfield zone containing aircraft gates, aprons, taxiways, runways, and maintenance hangars accessible only to screened personnel.",
                                    "example": "The ramp where aircraft refuel and embark passengers."
                                },
                                {
                                    "term": "Terminal Building",
                                    "definition": "The central processing facility that connects landside ground transportation with airside aircraft boarding gates.",
                                    "example": "Passengers clearing passport control and security scanners inside Terminal 1A at JKIA."
                                },
                                {
                                    "term": "Apron (Ramp)",
                                    "definition": "The paved, heavy-load surface adjacent to the terminal where aircraft park for passenger boarding, cargo loading, and ground servicing.",
                                    "example": "Ground support equipment connecting high-pressure fuel hoses and electrical ground power to an aircraft."
                                },
                                {
                                    "term": "Taxiway",
                                    "definition": "A paved path designated for slow surface movement (taxiing) of aircraft rolling between parking aprons and active runways.",
                                    "example": "Taxiway Alpha guiding departing airliners to the runway holding point."
                                },
                                {
                                    "term": "Runway",
                                    "definition": "A dedicated, straight strip of engineered asphalt or concrete reserved exclusively for aircraft takeoff acceleration and landing rollout.",
                                    "example": "Runway 06 at JKIA built to absorb the impact of 300-ton aircraft landings."
                                },
                                {
                                    "term": "Hangar",
                                    "definition": "A large, climate-sheltered steel structure dedicated to aircraft scheduled inspections, component overhauls, and structural repairs.",
                                    "example": "Kenya Airways technical maintenance hangar conducting C-checks on commercial jets."
                                }
                            ]
                        }
                    }
                ],
                # Card 3 (Page 3): Concept Explanation: Landside vs. Airside
                [
                    {
                        "type": "concept_explanation",
                        "title": "Airfield Spatial Architecture: Landside and Airside",
                        "content": {
                            "title": "The Security Boundary and Passenger Flow",
                            "text": "Airports are divided into two fundamental operational domains separated by a physical security barrier:\n\n- **The Landside Zone (Public Access)**: Welcomes passengers, visitors, and commercial vehicles. It contains car parks, public bus stops, and ticketing concourses where tickets are purchased and heavy baggage is checked.\n- **The Terminal Building (The Transition Bridge)**: Serves as the security filter. Passengers undergo metal detection and carry-on baggage X-ray screening, followed by immigration passport checks. Once past this threshold, travelers are in the secure airside departures lounge.\n- **The Airside Zone (Restricted Operations)**: Strict access controls govern entry. Only badged aviation personnel and ticketed, screened passengers may enter. This zone contains all aircraft movement infrastructure: aprons, taxiways, runways, and maintenance facilities."
                        }
                    }
                ],
                # Card 4 (Page 4): Technical Diagram (SVG Placeholder)
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Comprehensive Airport Zoning & Operational Layout Map",
                        "content": {
                            "title": "Airport Functional Zoning Schematic",
                            "caption": "A detailed layout map illustrating the landside public zone, terminal security boundary, apron parking stands, yellow-lined taxiway networks, white-marked active runways, control tower, and maintenance hangars."
                        }
                    }
                ],
                # Card 5 (Page 5): In-Depth Concept: Airside Operational Areas
                [
                    {
                        "type": "concept_explanation",
                        "title": "Airside Operational Areas: Ramp, Taxiways, Runways & Hangars",
                        "content": {
                            "title": "Functions of Dedicated Airfield Pavements",
                            "text": "Every segment of airside pavement serves a specialized aeronautical function:\n\n- **The Apron (Ramp)**: The industrial hive of the airport. Aircraft park on designated stands to undergo rapid turnaround operations: passenger boarding via jet bridges or air stairs, baggage loading via conveyor belts, pressurized wing fueling from underground hydrants or tankers, and cabin catering. Personnel must wear high-visibility vests and hearing protection.\n- **Taxiways**: The airfield road network. Aircraft roll at controlled speeds (typically 15 to 20 knots) along yellow-painted centerlines. Aircraft cannot take off or land on taxiways; their purpose is safe transit between aprons and runways.\n- **Runways**: The primary flight surfaces. Engineered to withstand tremendous touchdown forces and thermal loads from braking aircraft. Runways use white markings and white lighting, and access is strictly controlled by Tower Air Traffic Control.\n- **Hangars**: Industrial aircraft garages where licensed aircraft maintenance engineers (LAME) perform preventive maintenance, avionics testing, and major overhauls."
                        }
                    }
                ],
                # Card 6 (Page 6): Comparison Table
                [
                    {
                        "type": "comparison_table",
                        "title": "Airport Operational Zones: Roles, Markings & Access Rules",
                        "content": {
                            "title": "Functional Characteristics of Airport Zones",
                            "headers": ["Zone", "Primary Operational Purpose", "Pavement Markings", "Speed / Movement Rules", "Access Authorization"],
                            "rows": [
                                ["Landside", "Public drop-off, parking, passenger check-in", "Standard road traffic lines", "Standard vehicular road limits", "Unrestricted public access"],
                                ["Terminal (Airside)", "Passenger boarding gates, duty-free transit", "Interior concourse signage", "Pedestrian walking pace", "Screened ticketed passengers & badged staff"],
                                ["Apron / Ramp", "Aircraft parking, fueling, baggage loading", "Yellow stand lines, equipment staging boxes", "Vehicles restricted (15-25 km/h)", "Airside security badge & PPE mandatory"],
                                ["Taxiways", "Aircraft surface transit between ramp & runway", "Solid yellow centerline & yellow edge lines", "Controlled taxi speed (15-20 knots)", "Aircraft with ATC taxi clearance & authorized tugs"],
                                ["Runways", "Takeoff acceleration and landing deceleration", "Bold white threshold, numbers & centerline", "High flight speeds (120-250 km/h)", "Tower ATC takeoff or landing clearance only"],
                                ["Hangars", "Heavy aircraft maintenance, repair, and storage", "Epoxy workshop floor & safety clearance lines", "Towed/winched aircraft movement only", "Authorized maintenance engineers & inspectors"]
                            ]
                        }
                    }
                ],
                # Card 7 (Page 7): Real-World Example: Aircraft Turnaround at JKIA
                [
                    {
                        "type": "real_world_example",
                        "title": "Airside Ground Handling Turnaround at JKIA",
                        "content": {
                            "title": "The Orchestrated 45-Minute Aircraft Turnaround",
                            "text": "When a Boeing 737 arrives at Jomo Kenyatta International Airport, a tightly choreographed sequence begins on the apron:\n\n- **Chocks & Power**: As soon as the jet halts, ground crew place heavy rubber wheel chocks and connect external Ground Power Units (GPU) to supply electricity while engines shut down.\n- **Passenger Debarkation**: The passenger boarding bridge docks at the forward door, allowing travelers to enter Terminal 1A.\n- **Baggage & Catering**: Lower-deck cargo doors open; belt loaders transfer baggage into tractor tugs, while catering trucks lift supplies to galley doors.\n- **Refueling**: A specialized fuel hydrant truck connects to the underground fuel main and pumps thousands of liters of Jet A-1 into the wing tanks.\n- **Pushback**: A heavy towbarless pushback tractor pushes the aircraft backward into the taxiway lane, freeing the stand for incoming traffic."
                        }
                    }
                ],
                # Card 8 (Page 8): Safety Scenario: Apron Hazards and Foreign Object Debris
                [
                    {
                        "type": "concept_explanation",
                        "title": "Airfield Hazards: FOD and Ground Vehicle Control",
                        "content": {
                            "title": "Mitigating Collision Risks on the Airfield",
                            "text": "The apron and taxiways present intense industrial risks requiring rigorous discipline:\n\n- **Foreign Object Debris (FOD)**: Any loose object—such as a dropped bolt, luggage tag, plastic cup, or gravel stone—poses severe danger. If sucked into a running jet engine spinning at 10,000 RPM, it can destroy turbine blades and cause in-flight catastrophic engine failure. Airfield teams conduct daily walking FOD inspections.\n- **Vehicle Incursions**: Ground vehicle drivers must use painted service roads and never cut across taxiways without radio clearance from Ground Control. Crossing onto an active runway or taxiway risks a devastating collision with moving aircraft.\n- **Engine Ingestion & Jet Blast**: Running turbofans produce suction hazard zones ahead of the inlet cowl and hurricane-force exhaust blast behind the tail, requiring strict safety standoff distances."
                        }
                    }
                ],
                # Card 9 (Page 9): Curated Video Integration
                [
                    {
                        "type": "suggested_video",
                        "title": "Inside Modern Airport Airside Infrastructure",
                        "content": {
                            "title": "Airport Airside and Terminal Operations Tour",
                            "description": "Take a behind-the-scenes walkthrough of an international airport terminal, observing passenger flows, ramp operations, and the boundary separating landside from airside.",
                            "url": "https://www.youtube.com/watch?v=YmlfheAGx0E"
                        }
                    }
                ],
                # Card 10 (Page 10): Formative Knowledge Checks
                [
                    {
                        "type": "knowledge_check",
                        "title": "Diagnostic Check: Surface Movement Pavements",
                        "content": {
                            "question": "Which functional area of an airport is engineered strictly for the slow surface movement (taxiing) of aircraft between parking aprons and active runways?",
                            "options": [
                                "Aircraft Hangar",
                                "Runway",
                                "Taxiway",
                                "Passenger Check-In Lobby"
                            ],
                            "answer": "C",
                            "explanation": "Taxiways are designated paved paths connecting aprons, hangars, and runways. They are designed for slow, controlled ground maneuvering and are marked with yellow lines to distinguish them from runways."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Diagnostic Check: Apron Operational Hazards",
                        "content": {
                            "question": "Why is the apron (ramp) classified as one of the most hazardous operational zones on an airport airfield?",
                            "options": [
                                "It consists of unpaved, slippery mud tracks that cause aircraft tires to skid.",
                                "It combines high-density activity where aircraft maneuver alongside moving fuel tankers, baggage tugs, and operating jet engines in close quarters.",
                                "Unsupervised passengers are permitted to walk freely across active taxiways.",
                                "High-voltage lightning discharges occur exclusively across ramp parking stands."
                            ],
                            "answer": "B",
                            "explanation": "The apron is an active industrial work environment where ground crew, baggage tractors, fuel hydrant trucks, and catering lifts operate directly adjacent to running turbine engines and moving aircraft, creating major collision and hearing hazards."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 3: Runway Designation and Numbering
        # =====================================================================
        {
            "unit_order": 2,
            "unit_id": 2924,
            "unit_name": "Runway Designation and Numbering",
            "unit_description": "Mathematical calculation and physical layout of runway numbers: 360° magnetic headings, rounding to nearest 10 degrees, 180° reciprocal calculation, parallel runway suffixes (L, C, R), and magnetic variation.",
            "lesson_title": "Runway Designation and Numbering",
            "pages": [
                # Card 1 (Page 1): Photographic Hook & Learning Objectives
                [
                    {
                        "type": "suggested_image",
                        "title": "Runway Designation Marking Numbers Detail",
                        "content": {
                            "title": "Runway Designation Marking Numbers Detail",
                            "caption": "A close-up view of painted runway numbers and parallel suffix letters demonstrating magnetic heading alignment and reciprocal airfield geometry.",
                            "resolved_image_url": "https://upload.wikimedia.org/wikipedia/commons/7/78/15R-33L_-_Aeropuerto_de_Madrid-Barajas_-_detail.jpg"
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Learning Focus: Runway Designation Mathematics",
                        "content": {
                            "title": "Learning Focus: Runway Designation Mathematics",
                            "goals": [
                                "Explain how magnetic compass headings determine two-digit runway designation numbers.",
                                "Apply the standard rounding formula to convert three-digit magnetic headings into runway numbers (01 to 36).",
                                "Calculate reciprocal runway designations using the 180-degree (+/- 18) formula.",
                                "Identify parallel runway nomenclature using Left (L), Center (C), and Right (R) suffixes."
                            ]
                        }
                    }
                ],
                # Card 2 (Page 2): Key Terminology
                [
                    {
                        "type": "definition_card",
                        "title": "Essential Runway Designation Terminology",
                        "content": {
                            "title": "Runway Alignment & Heading Vocabulary",
                            "definitions": [
                                {
                                    "term": "Magnetic Heading",
                                    "definition": "The direction an aircraft nose or runway centerline points relative to Magnetic North, measured in degrees from 000° to 360° on a compass.",
                                    "example": "A compass reading of 090° points due magnetic East."
                                },
                                {
                                    "term": "Runway Designation",
                                    "definition": "The formal two-digit number (from 01 to 36) painted in bold white paint on the runway threshold, derived from its magnetic azimuth.",
                                    "example": "A runway pointing toward 062° is designated Runway 06."
                                },
                                {
                                    "term": "Reciprocal Runway",
                                    "definition": "The opposite end of the same strip of runway pavement, oriented exactly 180 degrees away from the primary threshold.",
                                    "example": "Runway 09 has a reciprocal end designated as Runway 27 (09 + 18 = 27)."
                                },
                                {
                                    "term": "Parallel Runways",
                                    "definition": "Two or more side-by-side runways aligned along identical magnetic headings, distinguished by letter suffixes (L, R, C).",
                                    "example": "Runway 36L (Left) and Runway 36R (Right) at high-capacity international hubs."
                                },
                                {
                                    "term": "Magnetic Variation",
                                    "definition": "The angular difference between True Geographic North and Magnetic North, which causes runways to be periodically re-numbered over decades.",
                                    "example": "Earth's shifting magnetic pole requiring runway numbers to be repainted."
                                }
                            ]
                        }
                    }
                ],
                # Card 3 (Page 3): Concept Explanation: The Compass-to-Runway Formula
                [
                    {
                        "type": "concept_explanation",
                        "title": "The Compass-to-Runway Calculation Formula",
                        "content": {
                            "title": "How Magnetic Headings Become Runway Numbers",
                            "text": "In aviation, runway names are not arbitrary street labels. They are precise mathematical representations of magnetic direction. A circle is divided into 360 degrees:\n\n- **000° / 360°**: Magnetic North\n- **090°**: Magnetic East\n- **180°**: Magnetic South\n- **270°**: Magnetic West\n\nTo establish a runway's official designation number, airport engineers follow a precise three-step algorithm:\n\n1. **Measure**: Determine the magnetic heading of the runway centerline from the perspective of an approaching aircraft.\n2. **Round**: Round the three-digit heading to the nearest 10 degrees (values ending in 5 or higher round up).\n3. **Drop the Zero**: Eliminate the trailing zero, leaving a two-digit integer between 01 and 36.\n\n*Worked Examples*:\n- A runway aligned with heading **088°** rounds to 090° → **Runway 09**.\n- A runway aligned with heading **274°** rounds to 270° → **Runway 27**.\n- A runway aligned with heading **357°** rounds to 360° → **Runway 36**.\n- A runway aligned with heading **003°** rounds to 000° (360°) → **Runway 36**."
                        }
                    }
                ],
                # Card 4 (Page 4): Technical Diagram (SVG Placeholder)
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Magnetic Runway Designation Circle & Reciprocal Geometry",
                        "content": {
                            "title": "Runway Orientation Compass Rose",
                            "caption": "A 360-degree compass circle illustrating magnetic runway designations, rounding rules, reciprocal 180-degree opposite pairings (such as 06/24 and 09/27), and parallel suffixes."
                        }
                    }
                ],
                # Card 5 (Page 5): In-Depth Concept: Reciprocals and Parallel Runways
                [
                    {
                        "type": "concept_explanation",
                        "title": "Reciprocal End Calculations and Parallel Runways",
                        "content": {
                            "title": "Opposite Runway Ends and Parallel Identifiers",
                            "text": "Every physical strip of runway pavement is reversible. Aircraft take off and land into the prevailing wind to maximize airflow and aerodynamic lift. Therefore, every runway possesses two numbers, painted on opposite ends:\n\n- **The Reciprocal Rule (+/- 18)**: Because a straight line represents 180 degrees, the two ends always differ by exactly 18 in runway digits.\n  - If the primary number is **18 or less**, ADD 18: 06 + 18 = 24 (Runway 06/24).\n  - If the primary number is **greater than 18**, SUBTRACT 18: 27 - 18 = 09 (Runway 09/27).\n\n**Parallel Runways**:\nWhen high-traffic airports construct parallel runways sharing the same magnetic orientation, letter suffixes identify each strip from the cockpit perspective:\n- **L (Left)**: The runway positioned on the pilot's left side during approach.\n- **R (Right)**: The runway positioned on the pilot's right side.\n- **C (Center)**: The middle runway when three parallel strips exist (e.g., 36L, 36C, 36R).\n\n*Reciprocal Suffix Flip*: When the active direction reverses, Left and Right swap: the reciprocal of **18L** is **36R**, and the reciprocal of **18R** is **36L**."
                        }
                    }
                ],
                # Card 6 (Page 6): Comparison Table
                [
                    {
                        "type": "comparison_table",
                        "title": "Runway Heading Calculation and Reciprocal Pairs",
                        "content": {
                            "title": "Runway Designation Calculation Matrix",
                            "headers": ["Measured Heading", "Rounded Heading", "Primary Designation", "Reciprocal Math", "Reciprocal Designation", "Airfield Example"],
                            "rows": [
                                ["062°", "060°", "Runway 06", "06 + 18", "Runway 24", "JKIA (Nairobi)"],
                                ["071°", "070°", "Runway 07", "07 + 18", "Runway 25", "Wilson Airport (Nairobi)"],
                                ["142°", "140°", "Runway 14", "14 + 18", "Runway 32", "Wilson Airport (Cross Runway)"],
                                ["033°", "030°", "Runway 03", "03 + 18", "Runway 21", "Moi Int'l (Mombasa)"],
                                ["268°", "270°", "Runway 27", "27 - 18", "Runway 09", "Kisumu International Airport"],
                                ["184°", "180°", "Runway 18", "18 + 18", "Runway 36", "Standard North-South Runway"]
                            ]
                        }
                    }
                ],
                # Card 7 (Page 7): Real-World Example: Runway 06/24 at JKIA
                [
                    {
                        "type": "real_world_example",
                        "title": "Runway 06/24 at Jomo Kenyatta International Airport",
                        "content": {
                            "title": "Operational Dynamics of JKIA's Primary Runway",
                            "text": "Jomo Kenyatta International Airport operates a single primary commercial runway designated as **Runway 06/24**, measuring 4,110 meters in length and 45 meters in width:\n\n- **Landing on Runway 06**: When prevailing winds blow from the Northeast, aircraft approach on a magnetic heading of approximately 058° to 062°. The pilots observe the massive white number **06** painted on the threshold asphalt.\n- **Landing on Runway 24**: When afternoon wind shifts blow from the Southwest, controllers direct arriving aircraft to approach on heading 238° to 242°, landing on **Runway 24**.\n- **Magnetic Pole Drift**: Because Earth's molten iron core creates shifting magnetic fields, magnetic declination changes over time. When magnetic drift exceeds 5 degrees, civil aviation authorities repaint runway numbers worldwide to maintain navigation integrity."
                        }
                    }
                ],
                # Card 8 (Page 8): Safety Scenario: Wrong Runway Landing Prevention
                [
                    {
                        "type": "concept_explanation",
                        "title": "Cross-Checking Runway Designations and Preventing Incursions",
                        "content": {
                            "title": "Aviation Safety: Alleviating Wrong-Runway Errors",
                            "text": "Landing on the incorrect runway or landing downwind can lead to catastrophic accidents:\n\n- **The Threat**: If an air traffic controller clears a flight to land on Runway 06, but the crew mistakenly lines up with Runway 24, the aircraft would land with a severe tailwind directly facing aircraft accelerating for takeoff on the same strip.\n- **Cockpit Verification Procedure**: Airline standard operating procedures mandate a 'triple check' before touchdown:\n  1. The pilot flying visually confirms the bold white numbers painted on the threshold pavement.\n  2. The pilot monitoring verifies that the aircraft's magnetic compass and heading indicator match the cleared runway heading within 10 degrees.\n  3. If visual markings or compass headings disagree with ATC clearance, the crew must immediately execute a missed approach (go-around)."
                        }
                    }
                ],
                # Card 9 (Page 9): Curated Video Integration
                [
                    {
                        "type": "suggested_video",
                        "title": "Runway Markings, Signs, and Numbering Explained",
                        "content": {
                            "title": "Runway Designation and Compass Mathematics",
                            "description": "Watch how compass bearings correspond directly to the bold numbers painted on runway thresholds, and see how parallel runway letters guide landing pilots.",
                            "url": "https://www.youtube.com/watch?v=Yacx4jNQlgo"
                        }
                    }
                ],
                # Card 10 (Page 10): Formative Knowledge Checks
                [
                    {
                        "type": "knowledge_check",
                        "title": "Diagnostic Check: Runway Number Calculation",
                        "content": {
                            "question": "If an aircraft approaches to land on a runway heading of 184° magnetic, what two-digit designation number is painted on the runway threshold?",
                            "options": [
                                "18",
                                "18.4",
                                "08",
                                "36"
                            ],
                            "answer": "A",
                            "explanation": "To determine the runway designation, take the magnetic heading (184°), round it to the nearest 10 degrees (180°), and drop the trailing zero. This yields Runway 18. Decimals are never used in runway numbering."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Diagnostic Check: Reciprocal Runway Mathematics",
                        "content": {
                            "question": "An airport runway threshold is designated as Runway 12. What designation number is painted on the reciprocal (opposite) end of this same strip of pavement?",
                            "options": [
                                "12R",
                                "24",
                                "30",
                                "02"
                            ],
                            "answer": "C",
                            "explanation": "Opposite runway ends are oriented 180 degrees apart, corresponding to a difference of 18 in runway numbers. Because 12 is less than 18, add 18: 12 + 18 = 30. The reciprocal end is Runway 30."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 4: Runway Visual Markings and Signs
        # =====================================================================
        {
            "unit_order": 3,
            "unit_id": 2925,
            "unit_name": "Runway Visual Markings and Signs",
            "unit_description": "Airfield visual aids and pavement markings: Color coding (white runway vs yellow taxiway), threshold stripes, centerline, aiming point markers, touchdown zones, hold-short lines, and mandatory instruction signs.",
            "lesson_title": "Runway Visual Markings and Signs",
            "pages": [
                # Card 1 (Page 1): Photographic Hook & Learning Objectives
                [
                    {
                        "type": "suggested_image",
                        "title": "Taxiway Hold-Short Lines at Runway Crossing",
                        "content": {
                            "title": "Taxiway Hold-Short Lines at Runway Crossing",
                            "caption": "Pavement markings showing double solid and double dashed yellow hold-short lines where a taxiway intersects an active runway, accompanied by mandatory airfield instruction signs.",
                            "resolved_image_url": "https://upload.wikimedia.org/wikipedia/commons/0/03/ATL_TWY_B_-_RWY_Crossing_%2813534655025%29.jpg"
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Learning Focus: Runway Visual Markings & Airfield Signs",
                        "content": {
                            "title": "Learning Focus: Runway Visual Markings & Airfield Signs",
                            "goals": [
                                "Differentiate white runway markings from yellow taxiway markings across the airfield.",
                                "Identify key runway pavement markings including threshold zebra stripes, centerline, aiming points, and touchdown zones.",
                                "Analyze the safety function of runway holding position lines (hold-short double solid/dashed lines).",
                                "Interpret mandatory airfield signs and airport surface guidance indicators."
                            ]
                        }
                    }
                ],
                # Card 2 (Page 2): Key Terminology
                [
                    {
                        "type": "definition_card",
                        "title": "Essential Airfield Visual Markings Terminology",
                        "content": {
                            "title": "Pavement Markings & Signage Vocabulary",
                            "definitions": [
                                {
                                    "term": "Runway Threshold",
                                    "definition": "The beginning of the portion of the runway usable for landing, marked with bold longitudinal white stripes.",
                                    "example": "Eight parallel white stripes indicating a 100-foot-wide runway threshold."
                                },
                                {
                                    "term": "Aiming Point",
                                    "definition": "Two prominent, thick solid white rectangular blocks painted 1,000 feet (300 meters) down the runway serving as the primary visual descent target for landing pilots.",
                                    "example": "Pilots maintaining a 3-degree glidepath aimed directly between the aiming point blocks."
                                },
                                {
                                    "term": "Touchdown Zone (TDZ)",
                                    "definition": "The designated segment of the runway past the threshold where landing aircraft should touch wheels, marked by pairs of rectangular white bars at 500-foot intervals.",
                                    "example": "Touching down within the first 3,000 feet of pavement to ensure adequate stopping distance."
                                },
                                {
                                    "term": "Hold-Short Line",
                                    "definition": "A critical airfield pavement marking consisting of four yellow lines (two solid, two dashed) indicating the boundary where an aircraft must halt before entering a runway.",
                                    "example": "Stopping before the two solid yellow lines until Tower ATC issues crossing clearance."
                                },
                                {
                                    "term": "Mandatory Instruction Sign",
                                    "definition": "A high-visibility airfield sign with white characters on a red background denoting an entrance to an active runway or critical safety zone.",
                                    "example": "A red sign reading '06-24' marking the holding point for Runway 06/24."
                                }
                            ]
                        }
                    }
                ],
                # Card 3 (Page 3): Concept Explanation: White Runway Markings
                [
                    {
                        "type": "concept_explanation",
                        "title": "Runway Pavement Markings: The Language of White Paint",
                        "content": {
                            "title": "Visual Aids for Safe Takeoffs and Landings",
                            "text": "Under international civil aviation regulations (ICAO Annex 14), color coding is strictly enforced:\n\n- **White paint is reserved exclusively for runway flight surfaces.**\n- **Yellow paint is reserved exclusively for taxiways, aprons, and surface holding zones.**\n\nKey white markings painted on precision runways include:\n\n1. **Threshold Zebra Stripes**: Parallel longitudinal white bars marking the start of landing pavement. The number of stripes indicates physical runway width (4 stripes = 60 ft; 6 stripes = 75 ft; 8 stripes = 100 ft; 12 stripes = 150 ft; 16 stripes = 200 ft).\n2. **Runway Designation Numbers**: Massive white numerals painted immediately past the threshold indicating magnetic orientation.\n3. **Runway Centerline**: A bold, dashed white line along the physical center of the runway, providing lateral guidance during 250 km/h landing rollouts and takeoff runs.\n4. **Aiming Point**: Two large, solid white rectangular blocks located exactly 1,000 feet (300 meters) from the threshold. Pilots align their visual descent path directly with these blocks.\n5. **Touchdown Zone Markers**: Symmetrical groupings of 1, 2, or 3 rectangular white bars painted on both sides of the centerline at 500-foot intervals."
                        }
                    }
                ],
                # Card 4 (Page 4): Technical Diagram (SVG Placeholder)
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Standard Runway Visual Markings & Airfield Signage Schematic",
                        "content": {
                            "title": "Runway Visual Markings Overview",
                            "caption": "An engineering schematic of precision runway markings detailing threshold stripes, runway numbers, dashed centerline, aiming point blocks, touchdown zone bars, taxiway holding position lines, and mandatory signs."
                        }
                    }
                ],
                # Card 5 (Page 5): In-Depth Concept: Taxiway Yellow Markings & Hold-Short Lines
                [
                    {
                        "type": "concept_explanation",
                        "title": "Taxiway Markings and the Critical Hold-Short Line",
                        "content": {
                            "title": "The Golden Rule of Airfield Ground Movement",
                            "text": "Taxiways are engineered for slow-speed ground taxiing and use high-contrast **yellow paint**:\n\n- **Taxiway Centerline**: A single solid continuous yellow line that pilots keep centered under their aircraft's nose gear.\n- **Taxiway Edge Lines**: Double solid yellow lines indicating pavement boundaries not designed to support aircraft weight.\n- **Runway Holding Position Marking (The Hold-Short Line)**:\n  This is the single most vital safety marking on any airfield. It consists of **four yellow lines** spanning across the taxiway:\n  - **Two Solid Lines** on the taxiway side.\n  - **Two Dashed Lines** on the runway side.\n\n**The Universal Safety Rule**:\n- When an aircraft is taxiing from an apron toward a runway, it encounters the **solid lines first**. The pilot **must halt completely** before the solid lines. No part of the aircraft (including the nose radome) may cross this line without explicit clearance from Air Traffic Control.\n- When an aircraft is exiting an active runway, it encounters the **dashed lines first**. The pilot can roll across the dashed lines immediately to clear the runway without waiting for secondary clearance."
                        }
                    }
                ],
                # Card 6 (Page 6): Comparison Table
                [
                    {
                        "type": "comparison_table",
                        "title": "Airfield Pavement Markings and Signage Matrix",
                        "content": {
                            "title": "Summary of Airfield Visual Markings",
                            "headers": ["Marking / Sign Name", "Paint / Sign Color", "Visual Pattern", "Airfield Location", "Operational Safety Purpose"],
                            "rows": [
                                ["Threshold Markings", "White", "Parallel longitudinal zebra stripes", "Runway beginning", "Defines start of landing zone and indicates runway width"],
                                ["Aiming Point", "White", "Two broad solid rectangular blocks", "1,000 ft (300 m) past threshold", "Visual target for descent path to ensure touchdown beyond threshold"],
                                ["Touchdown Zone", "White", "Pairs of 1, 2, or 3 rectangular bars", "500-foot intervals past threshold", "Delineates safe stopping touchdown zone along the first 3,000 ft"],
                                ["Runway Centerline", "White", "Evenly spaced dashed white line", "Exact center of runway", "Provides lateral alignment guidance during high-speed rollouts"],
                                ["Hold-Short Line", "Yellow", "Two solid lines & two dashed lines", "Taxiway entrance to runway", "Mandatory stop barrier preventing unauthorized runway entry"],
                                ["Mandatory Sign", "White on Red background", "Runway numbers (e.g., '06-24')", "Adjacent to hold-short line", "Identifies active runway intersection requiring ATC clearance"]
                            ]
                        }
                    }
                ],
                # Card 7 (Page 7): Real-World Example: Airfield Markings at Moi Airport
                [
                    {
                        "type": "real_world_example",
                        "title": "Pavement Transition at Moi International Airport",
                        "content": {
                            "title": "Navigating from Runway to Apron in Mombasa",
                            "text": "When a Boeing 737 lands on Runway 03 at Moi International Airport in Mombasa, the pilot touches down near the white aiming point blocks and decelerates along the dashed white centerline.\n\nAs the airliner slows to 15 knots, the pilot turns off the active runway onto Taxiway Alpha. The moment the main gear clears the yellow dashed hold-short lines, the pavement markings transition from wide white stripes to a narrow solid **yellow centerline**. Looking to the side, the crew observes a red mandatory holding sign with white text '03-21'. This transition confirms the aircraft is clear of the active runway envelope and entering the taxiway network."
                        }
                    }
                ],
                # Card 8 (Page 8): Safety Scenario: The Danger of Runway Incursions
                [
                    {
                        "type": "concept_explanation",
                        "title": "Runway Incursions and Hold-Short Violations",
                        "content": {
                            "title": "Preventing Catastrophic Ground Collisions",
                            "text": "A **runway incursion** is any unauthorized occurrence on an active runway involving an aircraft, vehicle, or person:\n\n- **The Scenario**: In foggy weather, a student pilot taxiing along Taxiway Echo fails to notice the yellow double solid hold-short lines on the pavement. The aircraft rolls onto the edge of Runway 24 without clearance just as a jet airliner is accelerating for takeoff.\n- **The Risk**: High-speed collisions on runways represent the deadliest category of aviation accidents in history (such as the 1977 Tenerife disaster).\n- **Mitigation Protocols**: Pilots must treat hold-short lines as an impassable wall until verbal ATC clearance is issued and read back. If visibility is compromised, pilots stop immediately and request progressive taxi instructions."
                        }
                    }
                ],
                # Card 9 (Page 9): Curated Video Integration
                [
                    {
                        "type": "suggested_video",
                        "title": "Aerial Perspective of Runway Visual Markings",
                        "content": {
                            "title": "Runway Markings Explained From the Air",
                            "description": "Examine how runway threshold stripes, aiming point blocks, and yellow hold-short lines appear to a pilot flying on final approach and during airfield taxiing.",
                            "url": "https://www.youtube.com/watch?v=eZuutXV7fqY"
                        }
                    }
                ],
                # Card 10 (Page 10): Formative Knowledge Checks
                [
                    {
                        "type": "knowledge_check",
                        "title": "Diagnostic Check: Airfield Pavement Color Coding",
                        "content": {
                            "question": "Under international aviation standards, what does the color of painted pavement markings indicate about an aircraft's position?",
                            "options": [
                                "White paint represents taxiways and aprons, while yellow paint represents active runways.",
                                "White paint represents active runway flight surfaces, while yellow paint represents taxiways, aprons, and holding points.",
                                "Green paint represents runways, while red paint represents parking ramps.",
                                "Blue paint represents runways, while white paint represents aircraft maintenance hangars."
                            ],
                            "answer": "B",
                            "explanation": "Under ICAO Annex 14 standards, white paint is reserved strictly for active runway surfaces (threshold, centerline, aiming point), while yellow paint is used exclusively for taxiways, parking ramps, and holding position lines."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Diagnostic Check: Hold-Short Line Rules",
                        "content": {
                            "question": "When approaching an active runway on a taxiway, you encounter a Hold-Short line consisting of two solid yellow lines and two dashed yellow lines. What is the mandatory safety rule?",
                            "options": [
                                "You must stop completely before crossing the solid yellow lines unless you have received positive clearance from Air Traffic Control.",
                                "You must always stop before dashed lines, but solid lines may be crossed at any time without clearance.",
                                "You should accelerate across the solid lines as quickly as possible to avoid obstructing ground vehicles.",
                                "You may cross any line without clearance if no other aircraft is visually observed in the sky."
                            ],
                            "answer": "A",
                            "explanation": "When approaching a runway from the taxiway, you face the two solid yellow lines first. These solid lines form a mandatory stop barrier that must never be crossed without explicit Air Traffic Control clearance."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 5: Airport Operations & Air Traffic Control
        # =====================================================================
        {
            "unit_order": 4,
            "unit_id": 2926,
            "unit_name": "Airport Operations & Air Traffic Control",
            "unit_description": "Air traffic management, aerodrome control tower operations, and the flight communication sequence: Clearance Delivery, Ground Control, Tower Local Control, pushback, taxi routing, takeoff clearance, and mandatory readback protocols.",
            "lesson_title": "Airport Operations & Air Traffic Control",
            "pages": [
                # Card 1 (Page 1): Photographic Hook & Learning Objectives
                [
                    {
                        "type": "suggested_image",
                        "title": "Air Traffic Controllers in Control Tower Cab",
                        "content": {
                            "title": "Air Traffic Controllers in Control Tower Cab",
                            "caption": "Certified air traffic controllers managing surface ground taxiing, runway departures, and arriving aircraft from the elevated glass cab of an airport control tower.",
                            "resolved_image_url": "https://upload.wikimedia.org/wikipedia/commons/0/09/Air_traffic_heathrow.JPG"
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Learning Focus: ATC Tower Operations & Flight Flow",
                        "content": {
                            "title": "Learning Focus: ATC Tower Operations & Flight Flow",
                            "goals": [
                                "Identify the specialized operational responsibilities of Clearance Delivery, Ground Control, and Tower Control.",
                                "Trace the chronological flight progression and radio hand-offs from terminal gate pushback to airborne departure.",
                                "Explain why mandatory radio readback protocols prevent critical aviation miscommunications.",
                                "Apply standardized radiotelephony procedures in airport ground operations."
                            ]
                        }
                    }
                ],
                # Card 2 (Page 2): Key Terminology
                [
                    {
                        "type": "definition_card",
                        "title": "Essential Air Traffic Management Terminology",
                        "content": {
                            "title": "Airfield Traffic Control Vocabulary",
                            "definitions": [
                                {
                                    "term": "Air Traffic Control (ATC)",
                                    "definition": "A ground-based service provided by certified controllers who direct aircraft on the ground and in controlled airspace to prevent collisions and maintain orderly flow.",
                                    "example": "KCAA air traffic controllers coordinating movements across Kenyan airspace."
                                },
                                {
                                    "term": "Control Tower Cab",
                                    "definition": "The top room of an airport control tower with 360-degree panoramic glass windows providing controllers an unobstructed view of all runways and taxiways.",
                                    "example": "The control tower cab at Wilson Airport overlooking Runways 07/25 and 14/32."
                                },
                                {
                                    "term": "Ground Control",
                                    "definition": "The specific ATC position responsible for managing aircraft and vehicle movements on taxiways and aprons, excluding active runways.",
                                    "example": "Ground Control issuing a taxi routing: 'Taxi to Runway 07 via Taxiway Alpha, hold short of Runway 07'."
                                },
                                {
                                    "term": "Tower Control (Local Control)",
                                    "definition": "The ATC position with sole authority over active runways and immediate airport airspace, responsible for issuing takeoff and landing clearances.",
                                    "example": "Tower Control transmitting: 'Runway 06, wind 080 at 10 knots, cleared for takeoff'."
                                },
                                {
                                    "term": "Clearance Delivery",
                                    "definition": "The ATC position that issues initial flight route authorizations, assigned altitudes, and transponder squawk codes before engine start.",
                                    "example": "Delivering an instrument flight plan clearance to a commercial flight before gate pushback."
                                },
                                {
                                    "term": "Readback",
                                    "definition": "The mandatory procedure where a pilot repeats key safety instructions (runway numbers, hold-short orders, altitudes) verbatim over the radio to verify mutual understanding.",
                                    "example": "Pilot repeating: 'Hold short of Runway 07, Five Yankee Bravo Alpha'."
                                }
                            ]
                        }
                    }
                ],
                # Card 3 (Page 3): Concept Explanation: The Three Controllers in the Tower
                [
                    {
                        "type": "concept_explanation",
                        "title": "The Three Tower Positions: Division of Responsibilities",
                        "content": {
                            "title": "Specialized Frequencies for Airfield Coordination",
                            "text": "Inside the control tower cab, managing hundreds of simultaneous flights requires splitting duties across discrete radio frequencies:\n\n1. **Clearance Delivery (The Planner)**:\n   - **Duty**: The first contact point for departing pilots while parked at the terminal gate.\n   - **Function**: Verifies the filed flight plan, assigns the initial climbing altitude, provides the departure route, and issues a 4-digit transponder squawk code.\n2. **Ground Control (The Traffic Coordinator)**:\n   - **Duty**: Controls all surface movements on the ramps, aprons, and taxiways.\n   - **Function**: Coordinates aircraft pushback from the gate, directs engine start sequences, and issues yellow-line taxi routes up to—but never onto—active runways.\n3. **Tower Control / Local Control (The Runway Commander)**:\n   - **Duty**: Exercises absolute authority over active runway surfaces and local airspace (typically up to 5 nautical miles and 3,000 feet).\n   - **Function**: Authorizes aircraft to cross, line up on, take off from, or land on runways. No pilot may touch a runway without direct Tower authorization."
                        }
                    }
                ],
                # Card 4 (Page 4): Technical Diagram (SVG Placeholder)
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Air Traffic Control Airspace & Aerodrome Tower Control Sequence",
                        "content": {
                            "title": "ATC Operational Hand-off Sequence",
                            "caption": "A workflow diagram mapping the sequence of radio hand-offs and controller responsibilities from gate pushback, taxi routing, runway holding point, takeoff roll, to departure radar."
                        }
                    }
                ],
                # Card 5 (Page 5): In-Depth Concept: The Gate-to-Takeoff Progression
                [
                    {
                        "type": "concept_explanation",
                        "title": "Step-by-Step Flight Progression: Gate to Airborne Departure",
                        "content": {
                            "title": "Chronological Execution of an Airport Departure",
                            "text": "A scheduled departure follows a disciplined chronological sequence of controller hand-offs:\n\n1. **Pre-Flight Clearance**: The crew contacts Clearance Delivery on 121.6 MHz to receive their route clearance: *'Kenya 540, cleared to Kisumu via flight plan route, climb and maintain 7,000 feet, squawk 4215'*.\n2. **Pushback & Engine Start**: The crew switches to Ground Control on 121.9 MHz: *'Wilson Ground, Kenya 540, stand 3, request push and start'*. Ground checks taxiway traffic and approves pushback.\n3. **Taxiing to Runway**: Ground issues a taxi clearance: *'Kenya 540, taxi to Runway 07 via Taxiway Alpha, hold short of Runway 07'*. The pilot taxis along the yellow centerline and halts before the solid lines.\n4. **Hand-Off to Tower**: Ground instructs: *'Kenya 540, contact Tower on 118.1'*. The crew checks in: *'Wilson Tower, Kenya 540, holding short Runway 07'*\n5. **Takeoff Clearance**: The Tower controller ensures separation from other aircraft and transmits: *'Kenya 540, Runway 07, wind 090 at 12 knots, cleared for takeoff'*\n6. **Airborne Departure**: Once climbing past 1,000 feet, Tower transfers the flight to Radar Departure Control on 119.7 MHz."
                        }
                    }
                ],
                # Card 6 (Page 6): Comparison Table
                [
                    {
                        "type": "comparison_table",
                        "title": "ATC Tower Positions, Areas of Authority & Sample Phraseology",
                        "content": {
                            "title": "ATC Operating Positions Matrix",
                            "headers": ["Controller Position", "Area of Authority", "Primary Responsibility", "Operating VHF Frequency", "Standard Radio Transmission"],
                            "rows": [
                                ["Clearance Delivery", "Parked aircraft at gate / stand", "Verifies flight plan, assigns altitude & squawk code", "121.6 – 121.8 MHz", "'Cleared to Mombasa via flight plan, climb 9,000 ft, squawk 2104'"],
                                ["Ground Control", "Aprons, ramps, and taxiways", "Pushback clearance, engine starts, taxi routing to hold lines", "121.7 – 121.9 MHz", "'Taxi to Runway 06 via Alpha and Bravo, hold short Runway 06'"],
                                ["Tower Local Control", "Active runways & 5 NM airspace", "Runway crossings, takeoff clearances, landing clearances", "118.1 – 118.7 MHz", "'Runway 06, wind 060 at 10 knots, cleared for takeoff'"],
                                ["Radar Departure", "Terminal maneuvering airspace (>5 NM)", "Radar vectoring, altitude climbs, enroute sequencing", "119.7 – 125.5 MHz", "'Radar contact, turn right heading 320, climb to flight level 180'"]
                            ]
                        }
                    }
                ],
                # Card 7 (Page 7): Real-World Example: Multi-Runway Operations at Wilson Airport
                [
                    {
                        "type": "real_world_example",
                        "title": "Tower Traffic Management at Wilson Airport",
                        "content": {
                            "title": "Coordinating Intersecting Runways at Wilson",
                            "text": "Wilson Airport operates two intersecting runways: Runway 07/25 and Runway 14/32. This geometry requires extraordinary vigilance from the Tower controller:\n\n- **Intersecting Traffic**: An arriving safari charter may be landing on Runway 07 while a training Cessna is departing from Runway 14. Because the two runways cross each other, the controller must calculate ground rollout speeds with split-second precision.\n- **Hold-Short Interventions**: If the landing charter rolls past the intersection before slowing down, the departing trainer must be held on the ground. The Tower controller instructs the trainer: *'Hold short of Runway 07, landing traffic'*\n- **Follow-Me Guidance**: When international pilots unfamiliar with Wilson arrive, Ground Control dispatches a yellow 'Follow-Me' operations vehicle with flashing yellow beacons to escort the aircraft safely to its parking hangar."
                        }
                    }
                ],
                # Card 8 (Page 8): Safety Scenario: Mandatory Readback Protocols
                [
                    {
                        "type": "concept_explanation",
                        "title": "The Safety Imperative: Why Readbacks Save Lives",
                        "content": {
                            "title": "Eliminating Communication Errors in Aviation",
                            "text": "Human speech is prone to distortion, hearing errors, and assumption, especially across low-fidelity VHF radio frequencies:\n\n- **The Risk**: A controller says: *'Taxi to Runway 09, hold short of Runway 09'*. A hurried pilot hears only *'Taxi to Runway 09'* and crosses onto the active runway into the path of a landing jet.\n- **The Readback Rule**: International regulations make verbatim readbacks legally mandatory. The pilot must repeat: *'Taxi to Runway 09, hold short of Runway 09, Kenya 540'*.\n- **Hearback Responsibility**: The controller must actively listen to the pilot's readback. If the pilot misstates a single digit, taxiway letter, or altitude, the controller instantly intervenes: *'Correction, hold short of Runway 09'*.\n- **Golden Axiom**: In aviation radiotelephony, silence does NOT equal consent. Never assume clearance without positive verbal verification."
                        }
                    }
                ],
                # Card 9 (Page 9): Curated Video Integration
                [
                    {
                        "type": "suggested_video",
                        "title": "Standard Aviation Radiotelephony and Pilot-ATC Communication",
                        "content": {
                            "title": "ATC Ground and Tower Communications in Practice",
                            "description": "Listen to real-world pilot and air traffic control communications, demonstrating professional pushback requests, taxi instructions, and takeoff clearances.",
                            "url": "https://www.youtube.com/watch?v=0t8tL6Mtp4E"
                        }
                    }
                ],
                # Card 10 (Page 10): Formative Knowledge Checks
                [
                    {
                        "type": "knowledge_check",
                        "title": "Diagnostic Check: Ground Movement Authority",
                        "content": {
                            "question": "Which Air Traffic Control unit is responsible for managing all aircraft and ground vehicle movements on taxiways and ramps, excluding active runways?",
                            "options": [
                                "Clearance Delivery",
                                "Tower Control (Local Control)",
                                "Ground Control",
                                "Radar Departure Control"
                            ],
                            "answer": "C",
                            "explanation": "Ground Control manages all surface movement on taxiways, ramps, and non-runway airfield areas, coordinating pushbacks, engine starts, and taxi routing up to the runway hold-short lines."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Diagnostic Check: Mandatory Readback Purpose",
                        "content": {
                            "question": "Why is it mandatory for a pilot to read back (repeat) taxiway hold-short and runway clearances issued by Air Traffic Control?",
                            "options": [
                                "To allow the student pilot to practice spoken English over the radio.",
                                "To confirm to the controller that the pilot has heard, understood, and will comply with the exact instruction, eliminating critical communication errors.",
                                "Because VHF radios automatically delete transmissions that are not echoed within five seconds.",
                                "To inform cabin passengers of departure progress over the public address system."
                            ],
                            "answer": "B",
                            "explanation": "The readback/hearback process ensures that the pilot has received the exact clearance intended by the controller. Repeating runway numbers, taxiway letters, and hold instructions allows any misunderstanding to be corrected immediately."
                        }
                    }
                ]
            ]
        }
    ]

def ingest_grade10_aviation_topic367(replace=False):
    print("=" * 80)
    print("STARTING INGESTION: Grade 10 Aviation — Topic 367: The Airport: Structure and Operations")
    print("=" * 80)

    curriculum = Curriculum.objects.filter(id=5).first()
    grade = Grade.objects.filter(id=5, level=10).first()
    subject = Subject.objects.filter(id=44, grade=grade).first()
    topic = Topic.objects.filter(id=367, subject=subject).first()

    if not topic:
        print("[ERROR] Topic 367 (The Airport: Structure and Operations) not found under Subject 44!")
        return

    print(f"[*] Target Subject: {subject.name} (ID: {subject.id})")
    print(f"[*] Target Topic:   {topic.name} (ID: {topic.id}, Order: {topic.order})")

    curriculum_data = build_topic367_curriculum()

    total_lessons = 0
    total_pages = 0
    total_blocks = 0

    with transaction.atomic():
        for unit_data in curriculum_data:
            u_order = unit_data["unit_order"]
            u_id = unit_data.get("unit_id")
            u_name = unit_data["unit_name"]
            u_desc = unit_data["unit_description"]
            l_title = unit_data["lesson_title"]
            pages_data = unit_data["pages"]

            if u_id:
                learning_unit = LearningUnit.objects.filter(id=u_id, topic=topic).first()
            else:
                learning_unit = None

            if not learning_unit:
                learning_unit, created = LearningUnit.objects.get_or_create(
                    topic=topic,
                    order=u_order,
                    defaults={"name": u_name, "description": u_desc}
                )
            learning_unit.name = u_name
            learning_unit.description = u_desc
            learning_unit.order = u_order
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

            print(f"  [+] Ingesting Lesson {u_order + 1}: {lesson.title} (Lesson ID: {lesson.id}, LU ID: {learning_unit.id})")

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
    print("[SUCCESS] Grade 10 Aviation Topic 367 Ingestion Complete!")
    print(f"[*] Total Lessons Ingested: {total_lessons}")
    print(f"[*] Total Pages/Cards:      {total_pages}")
    print(f"[*] Total Blocks Created:   {total_blocks}")
    print("=" * 80)

if __name__ == "__main__":
    replace_flag = "--replace" in sys.argv
    ingest_grade10_aviation_topic367(replace=replace_flag)
