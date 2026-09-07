"""
VLearn Grade 10 Aviation — Topic 368: Airport Business Services (Subject ID: 44, Topic ID: 368)
Production Ingestion Engine

Curriculum: CBC (Curriculum ID: 5)
Grade: Grade 10 (Grade ID: 5, Level: 10)
Subject: Aviation (Subject ID: 44)
Topic: Airport Business Services (Topic ID: 368, Order: 10)

Ingests 5 Comprehensive Learning Units & Lessons (50 Concept Cards):
  1. Passenger-Facing Airport Services (Unit ID: 2927, Order: 0) [10 Cards]
  2. Cargo, Logistics, and Airport Support Services (Unit ID: 2928, Order: 1) [10 Cards]
  3. Airport Business, Consumer Rights, and Financial Literacy (Unit ID: 2929, Order: 2) [10 Cards]
  4. Careers, Emerging Technology, and Sustainability in Airport Services (Unit ID: 2930, Order: 3) [10 Cards]
  5. Integrated Airport-Business Simulation (Unit ID: 2931, Order: 4) [10 Cards]

Usage:
  ./venv/bin/python curriculum/ingest_grade10_aviation_topic368.py [--replace]
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
    """Removes bracket citations [21, 93], internal visual prompt text, and normalizes typography."""
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

def build_topic368_curriculum():
    """Returns the pedagogical page and block structure for Grade 10 Aviation Topic 368."""
    return [
        # =====================================================================
        # LESSON 1: Passenger-Facing Airport Services
        # =====================================================================
        {
            "unit_order": 0,
            "unit_name": "Passenger-Facing Airport Services",
            "unit_description": "Foundations of passenger terminal operations: ticketing, check-in, security screening, baggage reconciliation systems (BRS), and departure gate boarding workflows.",
            "lesson_title": "Passenger-Facing Airport Services",
            "pages": [
                # Card 1 (Page 1): Photographic Hook & Learning Objectives
                [
                    {
                        "type": "suggested_image",
                        "title": "Modern Airport Terminal Passenger Check-in Concourse",
                        "content": {
                            "title": "Modern Airport Terminal Passenger Check-in Concourse",
                            "caption": "A modern airport passenger terminal departure concourse showing self-service kiosks, check-in desks, automated baggage drop lanes, and flight information display systems.",
                            "resolved_image_url": "https://upload.wikimedia.org/wikipedia/commons/e/e7/Taiwan_Taoyuan_International_Airport_Terminal_2_Check-in_Hall_20200815.jpg"
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Learning Focus: Terminal Passenger Flow & Security",
                        "content": {
                            "title": "Learning Focus: Terminal Passenger Flow & Security",
                            "goals": [
                                "Trace the sequential journey of a traveler from curbside arrival through terminal check-in, security screening, and aircraft boarding.",
                                "Explain the operational and legal significance of ticketing contracts and boarding passes in passenger processing.",
                                "Analyze how the Baggage Reconciliation System (BRS) links passenger gate check-in with ramp baggage loading to protect flight security.",
                                "Identify critical security procedures including carry-on baggage X-ray inspection, body scanners, and dangerous goods restrictions."
                            ]
                        }
                    }
                ],
                # Card 2 (Page 2): Key Terminology
                [
                    {
                        "type": "definition_card",
                        "title": "Core Passenger-Facing Aviation Terminology",
                        "content": {
                            "title": "Foundational Terminal Terminology",
                            "definitions": [
                                {
                                    "term": "Passenger Service",
                                    "definition": "The suite of customer-facing terminal business services, including ticketing, check-in, retail, dining, and boarding assistance, designed to facilitate a smooth traveler journey.",
                                    "example": "Ground personnel assisting elderly or unaccompanied minor passengers through airport immigration."
                                },
                                {
                                    "term": "Ticketing",
                                    "definition": "The legal and administrative process where a passenger purchases a contract of carriage from an airline, establishing flight routing, passenger data, and baggage allowances.",
                                    "example": "Booking an electronic ticket (e-ticket) linked to an airline passenger name record (PNR)."
                                },
                                {
                                    "term": "Boarding Pass",
                                    "definition": "A secure physical or digital document containing passenger identity, flight number, departure gate, seat assignment, and encrypted 2D barcode scanned before aircraft boarding.",
                                    "example": "Scanning a smartphone boarding pass at the automated departure gate e-turnstile."
                                },
                                {
                                    "term": "Security Screening",
                                    "definition": "The mandatory inspection of passengers using metal detectors or millimeter-wave body scanners and carry-on luggage using multi-view X-ray machines to prevent prohibited items from entering the airside zone.",
                                    "example": "Passing hand luggage through dual-energy X-ray machines to detect concealed liquid explosives or sharp objects."
                                },
                                {
                                    "term": "Baggage Reconciliation System (BRS)",
                                    "definition": "An automated computer security tracking system that cross-references checked bags with boarded passengers, guaranteeing that no suitcase is flown unless the owner has physically boarded.",
                                    "example": "An automated ramp alert prompting baggage handlers to offload a container when a passenger fails to board at the departure gate."
                                }
                            ]
                        }
                    }
                ],
                # Card 3 (Page 3): Concept Explanation (Terminal Workflow)
                [
                    {
                        "type": "concept_explanation",
                        "title": "The Passenger Terminal Flow System",
                        "content": {
                            "title": "Landside to Airside: The Journey of a Traveler",
                            "text": "Every commercial airport terminal functions as a high-volume, precision sorting mechanism. The terminal layout is divided into two distinct jurisdictional domains:\n\n- **Landside Zone**: The public area open to anyone without security clearance, encompassing terminal access roadways, drop-off curbsides, airline ticketing offices, and check-in counters.\n- **Airside Zone**: The sterile, tightly controlled security zone beyond passport control and checkpoint screening, comprising duty-free retail concourses, passenger departure lounges, jetbridges, and aircraft boarding gates.\n\nMoving between these zones requires passing through successive layers of identity verification, regulatory screening, and bag tagging. This strict division prevents unauthorized individuals, weapons, or uninspected items from reaching active aircraft."
                        }
                    }
                ],
                # Card 4 (Page 4): Technical Diagram (SVG)
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Passenger Terminal Workflow Architecture",
                        "content": {
                            "title": "Passenger Terminal Journey Flowchart",
                            "caption": "A comprehensive end-to-end flowchart tracking the passenger journey from landside curbside arrival through ticketing, baggage drop, security X-ray, immigration, duty-free concourse, gate scanning, and jetbridge boarding."
                        }
                    }
                ],
                # Card 5 (Page 5): Check-in and Baggage Tagging
                [
                    {
                        "type": "concept_explanation",
                        "title": "Check-In and Baggage Tagging Mechanics",
                        "content": {
                            "title": "The Digital and Physical Check-In Pipeline",
                            "text": "When a passenger reaches the check-in area, ground handling agents or automated self-service kiosks execute three vital functions:\n\n1. **Identity & Visa Verification**: Validating the traveler's passport against national biometric immigration databases and destination entry requirements.\n2. **Boarding Pass Generation**: Assigning a seat in accordance with aircraft center of gravity (CG) calculations and producing a secure boarding credential.\n3. **Baggage Acceptance & Automated Weighing**: Weighing luggage on certified digital scales to protect aircraft weight limits. A 10-digit barcoded baggage tag is printed and affixed to the suitcase handle.\n\nThis baggage tag carries critical data: flight number, 3-letter IATA destination code (e.g., NBO for Nairobi JKIA or MBA for Mombasa), transfer stations, and a unique tracking identification number recognized globally."
                        }
                    }
                ],
                # Card 6 (Page 6): Baggage Reconciliation Comparison Table
                [
                    {
                        "type": "comparison_table",
                        "title": "Terminal Security Safeguards vs Convenience Features",
                        "content": {
                            "title": "Operational Distinction Between Security and Convenience",
                            "headers": ["Service Area", "Convenience Function", "Mandatory Safety & Security Rule", "Consequence of Failure"],
                            "rows": [
                                ["Check-in Desk", "Seat selection, frequent flyer points", "Weight limit enforcement, photo identity check", "Overloaded aircraft, unmanifested passengers"],
                                ["Security Screening", "Fast-track priority lanes for families", "X-ray carry-on check, 100ml liquid limits", "Smuggled volatile chemicals or weapons in cabin"],
                                ["Baggage System (BRS)", "Automated conveyor routing to flight carts", "Positive bag-passenger reconciliation", "Unaccompanied suitcase loaded into aircraft hold"],
                                ["Boarding Gate", "Zone-based boarding order, priority calls", "Final barcode scan matched to flight manifest", "Flight departs with passenger count discrepancy"]
                            ]
                        }
                    }
                ],
                # Card 7 (Page 7): Real-World Application (JKIA Terminal 1A)
                [
                    {
                        "type": "real_world_example",
                        "title": "Passenger Flow at Jomo Kenyatta International Airport",
                        "content": {
                            "title": "Digital Transformation at JKIA Terminal 1A",
                            "text": "Jomo Kenyatta International Airport (JKIA) in Nairobi is East Africa's busiest international aviation hub, handling millions of passengers annually. Terminal 1A serves as the primary international departure terminal for flag carrier Kenya Airways and its global alliance partners.\n\nInside Terminal 1A, passenger processing is heavily digitized:\n- **Self-Service Kiosks**: Travelers print their own boarding passes and barcoded bag tags in less than 60 seconds, eliminating long check-in queues.\n- **Automated Self-Bag Drop**: Passengers place their tagged bags directly on automated belt scanners that verify weight and barcode readability before routing them into underground baggage tunnels.\n- **E-Gates**: Automated biometric immigration turnstiles scan e-passports and facial features, allowing Kenyan citizens and registered travelers to complete border clearance in seconds without manual stamp processing."
                        }
                    }
                ],
                # Card 8 (Page 8): Safety Connection (Unaccompanied Baggage Hazard)
                [
                    {
                        "type": "concept_explanation",
                        "title": "Aviation Safety Connection: Unmatched Baggage",
                        "content": {
                            "title": "The Threat of Unaccompanied Baggage and the BRS Protocol",
                            "text": "A passenger checks in two heavy suitcases at 07:00 for an international flight departing at 08:30. The bags are routed through the automated sorting belts and loaded into an aluminum cargo container. At 08:15, the boarding gate closes, but the passenger has failed to board.\n\n- **Hazard**: A piece of checked luggage is sitting in the airplane hold with no owner on board.\n- **Flight Risk**: International civil aviation history (such as Pan Am Flight 103) proved that terrorists could check bags containing time-delay explosive devices and intentionally skip boarding. An unaccompanied bag represents a grave security emergency.\n- **Mandatory Action**: The Baggage Reconciliation System (BRS) sounds an immediate alert at the departure gate and ramp control. Ramp handlers are legally required to stop cargo loading, locate the exact container holding the missing passenger's suitcases, and physically offload them before departure clearance can be granted. No passenger, no bag."
                        }
                    }
                ],
                # Card 9 (Page 9): Video Integration
                [
                    {
                        "type": "suggested_video",
                        "title": "Airport Procedures: Baggage Handling and Security",
                        "content": {
                            "title": "Behind the Scenes: Airport Baggage Handling & Reconciliation",
                            "description": "Examine the unseen automated sorting networks, barcode scanner arrays, and ramp reconciliation systems that process luggage from check-in desks to aircraft cargo holds.",
                            "url": "https://www.youtube.com/watch?v=wBRImzQSG80"
                        }
                    }
                ],
                # Card 10 (Page 10): Formative MCQs
                [
                    {
                        "type": "knowledge_check",
                        "title": "Diagnostic Assessment: Baggage Reconciliation Safety",
                        "content": {
                            "question": "What is the primary safety purpose of the Baggage Reconciliation System (BRS) in a commercial airport terminal?",
                            "options": [
                                "To charge passengers additional penalty fees if their bags exceed structural weight limits.",
                                "To ensure that a checked suitcase is never loaded onto an aircraft unless the passenger who checked it has physically boarded the flight.",
                                "To allow passengers to track their luggage in real-time using a commercial mobile application.",
                                "To clean and disinfect the exterior of suitcases before they are handled by apron ground personnel."
                            ],
                            "answer": "B",
                            "explanation": "The Baggage Reconciliation System (BRS) is a critical security barrier that cross-references passenger gate scans with ramp baggage scans. Under international anti-sabotage regulations, an unaccompanied bag must be offloaded immediately to prevent dangerous devices from being flown without the owner."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Diagnostic Assessment: Checkpoint Liquid Restrictions",
                        "content": {
                            "question": "Why are passengers strictly restricted from bringing liquid containers larger than 100 milliliters through terminal security checkpoints in carry-on bags?",
                            "options": [
                                "Large liquid containers take up excessive physical space in cabin overhead storage bins.",
                                "To force travelers to purchase beverages from commercial duty-free shops in the departure lounge.",
                                "Large volumes of unverified liquids present volatile fire or liquid explosive threats that cannot be safely analyzed by standard checkpoint X-ray scanners.",
                                "Liquid containers over 100ml are too heavy for passengers to carry safely while climbing aircraft stairs."
                            ],
                            "answer": "C",
                            "explanation": "Security X-ray machines detect density but cannot easily distinguish between harmless liquids and volatile liquid explosives or chemical agents in large volumes. Restricting carry-on liquids to containers under 100ml in transparent bags neutralizes this security risk."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 2: Cargo, Logistics, and Airport Support Services
        # =====================================================================
        {
            "unit_order": 1,
            "unit_name": "Cargo, Logistics, and Airport Support Services",
            "unit_description": "Operational dynamics of air freight and ramp support: general vs special cargo logistics, cold chain handling, Unit Load Devices (ULDs), and synchronized aircraft turnarounds.",
            "lesson_title": "Cargo, Logistics, and Airport Support Services",
            "pages": [
                # Card 1 (Page 1): Photographic Hook & Learning Objectives
                [
                    {
                        "type": "suggested_image",
                        "title": "Air Cargo High-Loader Loading Unit Load Devices (ULDs)",
                        "content": {
                            "title": "Air Cargo High-Loader Loading Unit Load Devices (ULDs)",
                            "caption": "An airport ramp scissor-lift high-loader transferring standardized aluminum Unit Load Device (ULD) cargo containers into the main deck cargo door of a freight aircraft.",
                            "resolved_image_url": "https://upload.wikimedia.org/wikipedia/commons/2/2f/Aircraft_cargo_%28ULD%29_loader_in_operaton.jpg"
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Learning Focus: Air Freight Logistics & Ramp Services",
                        "content": {
                            "title": "Learning Focus: Air Freight Logistics & Ramp Services",
                            "goals": [
                                "Differentiate between general cargo, perishable agricultural produce, cold-chain pharmaceuticals, and live animal transport.",
                                "Explain the aerodynamic and structural purpose of standardized Unit Load Devices (ULDs) in aircraft weight and balance.",
                                "Map out the simultaneous Ground Service Equipment (GSE) turnaround sequence including refueling, catering, and pushback.",
                                "Analyze safety protocols surrounding jet fuel hydrant pumping, electrostatic grounding, and ramp collision hazards."
                            ]
                        }
                    }
                ],
                # Card 2 (Page 2): Key Terminology
                [
                    {
                        "type": "definition_card",
                        "title": "Air Cargo & Ramp Support Terminology",
                        "content": {
                            "title": "Essential Cargo & Ground Service Vocabulary",
                            "definitions": [
                                {
                                    "term": "Air Cargo",
                                    "definition": "Freight, goods, and mail transported aboard commercial passenger bellies or dedicated freighter aircraft, classified into general and special cargo.",
                                    "example": "Fresh cut flowers, consumer electronics, and life-saving vaccines shipped across continents."
                                },
                                {
                                    "term": "Unit Load Device (ULD)",
                                    "definition": "A standardized aluminum container or pallet with cargo netting engineered to fit flush into aircraft fuselage contours and lock securely onto cargo hold roller tracks.",
                                    "example": "An LD-3 contoured container loaded with 1,500 kg of consolidated air express parcels."
                                },
                                {
                                    "term": "Turnaround Time",
                                    "definition": "The tightly measured ground window between an aircraft's arrival at the parking gate and its subsequent departure, during which servicing occurs.",
                                    "example": "A 45-minute turnaround for a Boeing 737 involving deplaning, cleaning, fueling, provisioning, and re-boarding."
                                },
                                {
                                    "term": "Ground Service Equipment (GSE)",
                                    "definition": "The fleet of specialized heavy machinery operating on the apron to support aircraft servicing, including pushback tugs, belt loaders, and GPUs.",
                                    "example": "An electric baggage tractor towing a train of luggage carts from the sorting room to the aircraft stand."
                                },
                                {
                                    "term": "Fuel Hydrant System",
                                    "definition": "An underground airport pipeline network that delivers pressurized aviation turbine fuel directly to apron parking stands, eliminating tanker truck traffic.",
                                    "example": "A dispenser truck connecting an intake hose from a tarmac hydrant pit to an aircraft wing fueling receptacle."
                                }
                            ]
                        }
                    }
                ],
                # Card 3 (Page 3): Air Freight Categorization
                [
                    {
                        "type": "concept_explanation",
                        "title": "Air Cargo Logistics Architecture",
                        "content": {
                            "title": "High-Value and Time-Sensitive Global Freight",
                            "text": "Air transport is the fastest and most expensive mode of global freight logistics. Consequently, businesses utilize air cargo primarily for goods characterized by high economic value or extreme time sensitivity:\n\n- **General Cargo**: Durable commodities requiring no specialized temperature regulation, such as microprocessors, telecommunications equipment, designer garments, and industrial machinery spare parts.\n- **Special Cargo**: Shipments demanding strict environmental controls and regulatory oversight:\n  - *Perishable Agricultural Freight*: Fresh-cut roses, herbs, and vegetables that must reach overseas retail shelves within 24 to 48 hours of harvesting.\n  - *Cold-Chain Pharmaceuticals*: Biologics, vaccines, and insulin that spoil if exposed to temperatures outside strict margins (e.g., +2°C to +8°C).\n  - *Live Animals (AVI)*: Racehorses, livestock, or pets transported under IATA Live Animals Regulations (LAR) with veterinary climate control."
                        }
                    }
                ],
                # Card 4 (Page 4): Technical Diagram (SVG)
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Air Cargo Logistics Chain & Ramp Turnaround Architecture",
                        "content": {
                            "title": "Air Cargo Logistics Chain Diagram",
                            "caption": "A technical flow diagram illustrating the journey of air freight: cold storage warehousing, pallet buildup into contoured Unit Load Devices (ULDs), tarmac transfer, scissor-lift high-loading, and fuselage restraint locking."
                        }
                    }
                ],
                # Card 5 (Page 5): The Unit Load Device (ULD)
                [
                    {
                        "type": "concept_explanation",
                        "title": "Engineering of Unit Load Devices (ULDs)",
                        "content": {
                            "title": "Contoured Precision and Structural Weight Efficiency",
                            "text": "Cargo cannot be loaded loosely inside an aircraft hold. Loose items would shift during turbulence, violently altering the aircraft's center of gravity and potentially causing loss of flight control.\n\nTo ensure structural stability and speed, air cargo is consolidated into **Unit Load Devices (ULDs)**:\n\n- **Fuselage Contouring**: Many ULD containers (such as LD-3 or LD-2) feature a chamfered (slanted) bottom corner designed to match the circular inward curvature of aircraft lower cargo deck walls, maximizing cargo hold volume.\n- **Lightweight Composites**: ULDs are constructed from ultra-lightweight aluminum alloys and carbon-fiber composite panels. Every kilogram shaved from container tare weight translates into an extra kilogram of paying cargo payload.\n- **Roller Tracks and Restraint Latches**: Aircraft cargo floors feature motorized omni-directional ball mats and roller tracks. Once rolled into position, mechanical floor locks latch into the ULD base perimeter, securing tons of cargo against 9G forward crash loads."
                        }
                    }
                ],
                # Card 6 (Page 6): The Aircraft Turnaround Choreography
                [
                    {
                        "type": "comparison_table",
                        "title": "Apron Turnaround Support Services Matrix",
                        "content": {
                            "title": "Parallel Ramp Servicing Synchronization",
                            "headers": ["Turnaround Phase", "Equipment Involved", "Operational Duty", "Safety & Environmental Safeguards"],
                            "rows": [
                                ["Deboarding & Unloading", "Jetbridge, belt loader, ULD high-loader", "Disembark passengers, offload baggage and inbound cargo", "Anti-collision buffer zones around aircraft skin"],
                                ["Aircraft Refueling", "Hydrant dispenser, underground fuel line", "Pumping thousands of liters of Jet A-1 into wing tanks", "Electrostatic bonding wire attached before opening fuel caps"],
                                ["Cabin Servicing & Catering", "High-lift catering scissor trucks, cleaning vans", "Restock galleys with chilled food carts, sanitize cabin", "Driver guide marshals and hydraulic stabilizer jacks deployed"],
                                ["Boarding & Pushback", "Heavy towbar pushback tug, bypass pin", "Disconnect ground power, push aircraft onto taxiway", "Cockpit-to-ground intercom headset check, safety circle clear"]
                            ]
                        }
                    }
                ],
                # Card 7 (Page 7): Real-World Application (Kenya Horticulture)
                [
                    {
                        "type": "real_world_example",
                        "title": "East Africa's Horticultural Cargo Lifeline",
                        "content": {
                            "title": "Cold-Chain Flower Exports from JKIA to Amsterdam",
                            "text": "Kenya is one of the world's largest exporters of fresh-cut flowers. Every evening, temperature-controlled refrigerated trucks arrive at the JKIA Cargo Village in Nairobi from farms around Lake Naivasha and Mount Kenya.\n\nAt cold-storage warehouses operated by ground handlers like Swissport and Kenya Airways Cargo:\n- Cut roses are inspected by phytosanitary authorities and packed into pre-cooled ULD pallets wrapped in thermal protective blankets.\n- Massive dedicated freighter aircraft (such as Boeing 777F and 747-8F) open their side main deck cargo doors.\n- Hydraulic high-loaders lift 5-ton pallets into the freighter upper and lower decks.\n- Within 8 hours of takeoff, Kenyan flowers land at Amsterdam Schiphol Airport (AMS), reaching European floral auctions and supermarkets fresh the very next morning."
                        }
                    }
                ],
                # Card 8 (Page 8): Safety Connection (Ramp Fueling & Grounding)
                [
                    {
                        "type": "concept_explanation",
                        "title": "Aviation Safety Connection: Static Grounding in Fueling",
                        "content": {
                            "title": "Electrostatic Hazards During High-Speed Aircraft Refueling",
                            "text": "Commercial jet fuel (Jet A-1) is pumped through ramp hoses at rates exceeding 2,000 liters per minute. The turbulent friction of liquid hydrocarbons moving through composite hoses generates massive static electrical charges on the aircraft metal structure.\n\n- **Hazard**: An accumulated electrostatic charge can create a high-voltage spark between the hose nozzle and the fuel port, igniting flammable kerosene vapors.\n- **Mandatory Procedure**: Before fuel caps are removed or hoses connected, ground technicians must attach a heavy **bonding cable** connecting the fuel dispenser truck to the aircraft ground terminal, and attach an electrostatic grounding wire directly to the airfield tarmac earth grounding point.\n- **Integrity Check**: This equalizes electrical potential and dissipates static charges harmlessly into the earth. Ground handlers must also inspect the ramp for ground vehicle clearance, ensuring no mobile belt loaders or tugs strike the aircraft fuselage skin."
                        }
                    }
                ],
                # Card 9 (Page 9): Video Integration
                [
                    {
                        "type": "suggested_video",
                        "title": "Ramp Operations: Aircraft Turnaround and Ground Handling",
                        "content": {
                            "title": "Fast-Paced Aircraft Turnarounds: Ramp Coordination in Action",
                            "description": "Witness the high-speed choreography of aircraft turnarounds as ground crews synchronize cargo unloading, fuel hydrants, catering lifts, and pushback tugs.",
                            "url": "https://www.youtube.com/watch?v=pAL3GfdWLWM"
                        }
                    }
                ],
                # Card 10 (Page 10): Formative MCQs
                [
                    {
                        "type": "knowledge_check",
                        "title": "Diagnostic Assessment: Aircraft Refueling Electrostatics",
                        "content": {
                            "question": "Why must ground support technicians physically attach electrostatic grounding and bonding wires to an aircraft before pumping Jet A-1 fuel?",
                            "options": [
                                "To charge the aircraft's internal flight deck batteries using electric power from the fuel vehicle.",
                                "To prevent static electricity, generated by high-speed fuel friction, from creating sparks that could ignite volatile fuel vapors.",
                                "To calculate the precise chemical density of the aviation fuel being loaded into wing tanks.",
                                "To enable communication between pilots and ground handlers over a hardwired intercom cable."
                            ],
                            "answer": "B",
                            "explanation": "High-speed fuel flow through hoses generates substantial electrostatic friction. If ungrounded, static discharge sparks can ignite kerosene vapors, triggering catastrophic ramp fires. Grounding and bonding wires safely equalize electrical potential and dissipate charges to earth."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Diagnostic Assessment: Unit Load Device Construction",
                        "content": {
                            "question": "Why are Unit Load Devices (ULDs) constructed from lightweight aluminum alloys and composite materials rather than heavy structural steel?",
                            "options": [
                                "Composite materials are cheap to discard and replace after a single flight.",
                                "Heavy steel containers absorb excessive heat on hot runways, damaging perishable cargo.",
                                "Minimizing container tare weight maximizes allowable cargo and passenger payload while reducing fuel burn and carbon emissions.",
                                "Aluminum containers are magnetically shielded to prevent interference with magnetic compass sensors."
                            ],
                            "answer": "C",
                            "explanation": "Weight is a critical performance factor in aviation. Utilizing lightweight aluminum and composite ULDs minimizes empty container weight, maximizing allowable commercial payload, reducing fuel consumption, and improving flight efficiency."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 3: Airport Business, Consumer Rights, and Financial Literacy
        # =====================================================================
        {
            "unit_order": 2,
            "unit_name": "Airport Business, Consumer Rights, and Financial Literacy",
            "unit_description": "Financial mechanisms and regulatory protections in aviation: aeronautical vs non-aeronautical revenue models, airport operating budgeting, and consumer rights under IATA, KCAA, and KAA.",
            "lesson_title": "Airport Business, Consumer Rights, and Financial Literacy",
            "pages": [
                # Card 1 (Page 1): Photographic Hook & Learning Objectives
                [
                    {
                        "type": "suggested_image",
                        "title": "Jomo Kenyatta International Airport Commercial Terminal Facade",
                        "content": {
                            "title": "Jomo Kenyatta International Airport Commercial Terminal Facade",
                            "caption": "The main commercial passenger terminal building of Jomo Kenyatta International Airport (JKIA) in Nairobi, managed and operated by the Kenya Airports Authority (KAA).",
                            "resolved_image_url": "https://upload.wikimedia.org/wikipedia/commons/a/a6/Jomo_Kenyatta_International_Airport_terminal_building%2C_2025_%2802%29.jpg"
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Learning Focus: Airport Economics & Consumer Rights",
                        "content": {
                            "title": "Learning Focus: Airport Economics & Consumer Rights",
                            "goals": [
                                "Distinguish between aeronautical revenue streams (landing/parking fees) and non-aeronautical commercial revenue streams (retail, parking).",
                                "Analyze airport operating expenses (OPEX) including 24/7 security, ARFF rescue services, and runway pavement maintenance.",
                                "Differentiate the distinct legal roles and jurisdictions of IATA, KCAA, and KAA in protecting civil aviation.",
                                "Evaluate passenger consumer rights and legal entitlements to care, refreshments, and compensation during flight delays and cancellations."
                            ]
                        }
                    }
                ],
                # Card 2 (Page 2): Key Terminology
                [
                    {
                        "type": "definition_card",
                        "title": "Airport Business & Consumer Literacy Vocabulary",
                        "content": {
                            "title": "Core Commercial Aviation Vocabulary",
                            "definitions": [
                                {
                                    "term": "Aeronautical Revenue",
                                    "definition": "Income generated directly from aircraft operations and air traffic services, including runway landing fees, aircraft parking charges, and passenger service charges.",
                                    "example": "An airline paying a fee based on the Maximum Takeoff Weight (MTOW) of an Airbus A330 landing on runway 06."
                                },
                                {
                                    "term": "Non-Aeronautical Revenue",
                                    "definition": "Commercial income earned from airport terminal activities unrelated to flight operations, such as retail store concessions, duty-free leases, parking lots, and advertising.",
                                    "example": "A cafe chain paying monthly rent and a percentage of food sales to the airport authority."
                                },
                                {
                                    "term": "Operating Expenses (OPEX)",
                                    "definition": "The recurring operational costs required to keep an airport functional, compliant, and safe on a continuous daily basis.",
                                    "example": "Paying utility power bills for terminal HVAC, firefighter salaries, and runway rubber removal."
                                },
                                {
                                    "term": "IATA",
                                    "definition": "International Air Transport Association: a global airline trade association representing over 300 airlines that sets worldwide ticketing, baggage, and interline standards.",
                                    "example": "Standardizing international electronic ticket format codes across multiple carrier bookings."
                                },
                                {
                                    "term": "KCAA & KAA",
                                    "definition": "KCAA (Kenya Civil Aviation Authority) regulates national airspace safety, licensing, and consumer protection; KAA (Kenya Airports Authority) manages, builds, and maintains commercial airport infrastructure.",
                                    "example": "KCAA enforcing passenger delay compensation regulations while KAA maintains the runway lighting at Kisumu Airport."
                                }
                            ]
                        }
                    }
                ],
                # Card 3 (Page 3): Airport Financial Architecture
                [
                    {
                        "type": "concept_explanation",
                        "title": "The Airport Business Model",
                        "content": {
                            "title": "Balancing the Aerodrome Balance Sheet",
                            "text": "An international airport is a multifaceted business enterprise. Airport authorities must balance capital expenditures (CAPEX) for runway expansions with ongoing operating expenses (OPEX) while ensuring steady revenue generation:\n\n- **Aeronautical Revenue (Flight Services)**:\n  - *Landing Fees*: Charged to airlines based on the Maximum Takeoff Weight (MTOW) of the aircraft. Heavy long-haul airliners pay significantly more than light turboprops.\n  - *Aircraft Parking Fees*: Hourly or overnight tarmac leasing charges.\n  - *Passenger Facility Charges (PFC)*: A regulatory per-passenger charge bundled directly into every passenger's ticket price.\n- **Non-Aeronautical Revenue (Commercial Services)**:\n  - *Duty-Free & Retail Concessions*: High-margin retail shops and restaurants paying leasing fees and revenue-sharing royalties.\n  - *Ground Transport & Parking*: Multi-story parking garages, taxi concessions, and rental car counters.\n  - *Terminal Advertising*: High-visibility billboards and digital display sponsorships throughout departure and arrivals concourses."
                        }
                    }
                ],
                # Card 4 (Page 4): Technical Diagram (SVG)
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Airport Revenue Model and Financial Architecture",
                        "content": {
                            "title": "Airport Financial Architecture Diagram",
                            "caption": "A financial flow diagram showing the balance between Aeronautical Revenue (landing fees, parking, terminal fees) and Non-Aeronautical Revenue (retail concessions, parking, advertising) offsetting Operating Expenses (security, rescue fire, runway repairs)."
                        }
                    }
                ],
                # Card 5 (Page 5): Regulatory Governance Framework
                [
                    {
                        "type": "concept_explanation",
                        "title": "Regulatory Framework: IATA, KCAA, and KAA",
                        "content": {
                            "title": "Who Does What? Three Tiers of Aviation Authority",
                            "text": "Understanding civil aviation requires mastering the distinct institutional boundaries of global and national bodies:\n\n- **IATA (International Air Transport Association)**:\n  - *Role*: Global airline industry trade association.\n  - *Mandate*: Promotes airline cooperation, standardizes electronic ticketing protocols, publishes dangerous goods handling regulations, and assigns 3-letter airport codes (e.g., NBO) and 2-letter airline codes (e.g., KQ).\n- **KCAA (Kenya Civil Aviation Authority)**:\n  - *Role*: National government regulatory authority.\n  - *Mandate*: The sovereign 'referee' of Kenyan aviation. Issues pilot licenses, inspects aircraft airworthiness, operates Air Traffic Control (ATC) en-route towers, and enforces consumer protection laws.\n- **KAA (Kenya Airports Authority)**:\n  - *Role*: Public airport owner and operator.\n  - *Mandate*: The physical landlord. Builds, operates, secures, and maintains all public commercial airports and airstrips across Kenya (e.g., JKIA, Moi, Kisumu, Eldoret, Malindi)."
                        }
                    }
                ],
                # Card 6 (Page 6): Consumer Rights Responsibility Matrix
                [
                    {
                        "type": "comparison_table",
                        "title": "Institutional Responsibilities Matrix",
                        "content": {
                            "title": "Jurisdictional Matrix: IATA vs KCAA vs KAA",
                            "headers": ["Aviation Issue / Event", "Responsible Body", "Legal Jurisdiction", "Primary Action / Redress"],
                            "rows": [
                                ["Flight delayed 5 hours due to airline crew shortage", "KCAA (Consumer Protection)", "National Law", "Mandates free meals, drinks, communication, and compensation"],
                                ["Standardizing global baggage tracking barcode rules", "IATA", "International Industry Standard", "Establishes uniform Resolution 753 messaging format"],
                                ["Broken security X-ray scanner or pothole on taxiway", "KAA (Airport Management)", "Airport Infrastructure", "Deploys airport engineering crews to repair facilities"],
                                ["Airline refuses to honor valid electronic flight ticket", "KCAA & IATA standards", "National Regulatory Enforcement", "Enforces carriage contract and sanctions airline for non-compliance"]
                            ]
                        }
                    }
                ],
                # Card 7 (Page 7): Real-World Application (Consumer Rights in Action)
                [
                    {
                        "type": "real_world_example",
                        "title": "Passenger Consumer Rights Enforcement in Kenya",
                        "content": {
                            "title": "What Happens When Your Flight is Grounded?",
                            "text": "Under **KCAA Civil Aviation (Consumer Protection) Regulations**, air travelers in Kenya possess clearly defined legal consumer rights:\n\n1. **Right to Information**: Airlines must immediately announce the cause of a flight delay and provide updated departure times every 30 minutes.\n2. **Right to Care (Delays exceeding 2 hours)**: The airline must supply free meals and refreshments suited to the waiting time, plus access to two telephone calls or emails.\n3. **Right to Accommodation (Overnight Delays)**: If a domestic or international flight is delayed overnight, the operating airline is legally obligated to provide free hotel lodging, airport-to-hotel ground transportation, and secure luggage storage.\n4. **Right to Financial Reimbursement**: If an airline cancels a flight or denies boarding due to overbooking, the passenger is entitled to a full refund within a specified window or alternate rerouting at no added expense."
                        }
                    }
                ],
                # Card 8 (Page 8): Safety vs Profit Budgeting
                [
                    {
                        "type": "concept_explanation",
                        "title": "Aviation Safety Connection: Safety vs Commercial Budgeting",
                        "content": {
                            "title": "Why Aviation Safety Never Yields to Commercial Cuts",
                            "text": "During economic downturns, an airport management board might seek to cut operating budgets to remain profitable. For instance, a finance officer might propose reducing Airport Rescue and Firefighting (ARFF) staff or deactivating night-shift security surveillance cameras.\n\n- **Regulatory Non-Negotiable**: Under international ICAO Annex 14 and national KCAA aerodrome licensing requirements, an airport's operational category is legally tied to its emergency response and security readiness.\n- **Consequences**: If an airport reduces its ARFF staffing or equipment, its certified category is instantly downgraded. Widebody airliners carrying hundreds of passengers are prohibited from landing at downgraded airports, immediately cutting off flight operations.\n- **Golden Rule of Aviation Finance**: Safety, rescue capability, and perimeter security are mandatory regulatory baselines; commercial profits can only be pursued once safety compliance is unconditionally guaranteed."
                        }
                    }
                ],
                # Card 9 (Page 9): Video Integration
                [
                    {
                        "type": "suggested_video",
                        "title": "Aviation Regulation: Role of the Civil Aviation Authority",
                        "content": {
                            "title": "National Aviation Governance: Inside the Civil Aviation Authority",
                            "description": "Discover how national civil aviation authorities regulate airspace safety, audit airport infrastructure, license aviation professionals, and protect passenger rights.",
                            "url": "https://www.youtube.com/watch?v=PecMbpWxK9w"
                        }
                    }
                ],
                # Card 10 (Page 10): Formative MCQs
                [
                    {
                        "type": "knowledge_check",
                        "title": "Diagnostic Assessment: Airport Revenue Classification",
                        "content": {
                            "question": "Which of the following income sources is categorized as Non-Aeronautical revenue for an airport business?",
                            "options": [
                                "Aircraft landing fees calculated on Maximum Takeoff Weight.",
                                "Hangar parking fees charged to an airline for parking aircraft overnight.",
                                "Commercial leasing rent paid by a duty-free perfume boutique inside the departure lounge.",
                                "Passenger service charges billed to airlines per departing traveler."
                            ],
                            "answer": "C",
                            "explanation": "Non-Aeronautical revenue represents income generated from commercial, non-flight activities. Leasing terminal floor space to retail boutiques, dining restaurants, car rentals, and terminal parking lots constitutes non-aeronautical revenue."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Diagnostic Assessment: Consumer Protection Authority",
                        "content": {
                            "question": "If a commercial domestic flight in Kenya is delayed for 6 hours due to an airline operational error, which organization has statutory power to enforce passenger compensation and care?",
                            "options": [
                                "The International Air Transport Association (IATA).",
                                "The Kenya Civil Aviation Authority (KCAA).",
                                "The Kenya Airports Authority (KAA).",
                                "The local municipal county tourism development board."
                            ],
                            "answer": "B",
                            "explanation": "The Kenya Civil Aviation Authority (KCAA) is the statutory regulator of civil aviation in Kenya. KCAA establishes and enforces consumer protection regulations that require airlines to supply refreshments, accommodations, and compensation during long operational flight delays."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 4: Careers, Emerging Technology, and Sustainability in Airport Services
        # =====================================================================
        {
            "unit_order": 3,
            "unit_name": "Careers, Emerging Technology, and Sustainability in Airport Services",
            "unit_description": "Future pathways in airport services: automated biometric passenger identity, electric Ground Service Equipment (eGSE), solar-powered terminal ecosystems, and specialized aviation career pathways.",
            "lesson_title": "Careers, Emerging Technology, and Sustainability in Airport Services",
            "pages": [
                # Card 1 (Page 1): Photographic Hook & Learning Objectives
                [
                    {
                        "type": "suggested_image",
                        "title": "Utility-Scale Solar Farm Powering Airport Operations",
                        "content": {
                            "title": "Utility-Scale Solar Farm Powering Airport Operations",
                            "caption": "A utility-scale solar photovoltaic power plant installed on airport buffer lands, supplying clean renewable electricity for terminal operations and electric ground vehicles.",
                            "resolved_image_url": "https://upload.wikimedia.org/wikipedia/commons/c/cc/Solar_Plant_powering_the_Cochin_International_Airport.jpg"
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Learning Focus: Green Tech, Biometrics & Aviation Careers",
                        "content": {
                            "title": "Learning Focus: Green Tech, Biometrics & Aviation Careers",
                            "goals": [
                                "Evaluate emerging biometric facial recognition technologies and AI automation streamlining terminal passenger flows.",
                                "Analyze green airport sustainability initiatives including electric GSE (eGSE), solar energy harvesting, and waste reduction.",
                                "Investigate professional career pathways across passenger terminal management, ramp logistics, and safety auditing.",
                                "Assess safety protocols governing automated robotic ground machinery and human-robot interaction on the ramp."
                            ]
                        }
                    }
                ],
                # Card 2 (Page 2): Key Terminology
                [
                    {
                        "type": "definition_card",
                        "title": "Emerging Airport Technology & Career Vocabulary",
                        "content": {
                            "title": "Modern Airport Technology Vocabulary",
                            "definitions": [
                                {
                                    "term": "eGSE (Electric GSE)",
                                    "definition": "Ground support equipment powered by lithium battery electric drives rather than internal combustion diesel engines, eliminating localized apron exhaust fumes and noise.",
                                    "example": "Zero-emission electric pushback tugs and battery-powered belt loaders plugged into solar charging stations."
                                },
                                {
                                    "term": "Biometric Digital Identity",
                                    "definition": "The algorithmic use of unique physiological markers, such as facial geometric scans, to verify passenger identity seamlessly at check-in, security, and boarding gates.",
                                    "example": "Walking through a boarding turnstile that opens in 2 seconds upon scanning a passenger's face."
                                },
                                {
                                    "term": "Solar-Powered Airport",
                                    "definition": "An aerodrome that utilizes extensive on-site photovoltaic solar farms to generate 100% of its operational electrical demands for terminals, runways, and facilities.",
                                    "example": "Cochin International in India and George Airport in South Africa running entirely on localized solar power."
                                },
                                {
                                    "term": "Ramp Agent / Loadmaster",
                                    "definition": "An aviation professional responsible for physical aircraft turnaround loading, weight and balance distribution, and ramp safety management.",
                                    "example": "Calculating cargo distribution and securing ULD locks inside a widebody aircraft belly hold."
                                },
                                {
                                    "term": "Airport Safety Auditor",
                                    "definition": "A regulatory or airport management professional tasked with inspecting operational aprons, evaluating risk controls, and ensuring compliance with civil aviation safety rules.",
                                    "example": "Auditing ground vehicle speed tracking logs and inspecting fuel hydrant emergency shutoff valves."
                                }
                            ]
                        }
                    }
                ],
                # Card 3 (Page 3): Biometrics and Terminal Automation
                [
                    {
                        "type": "concept_explanation",
                        "title": "Biometric Identity and Automated Passenger Processing",
                        "content": {
                            "title": "Paperless Walk-Through Terminals",
                            "text": "Traditional passenger processing requires showing printed boarding passes and physical passports at multiple touchpoints: terminal entrance, check-in desk, security checkpoint, duty-free registers, and the boarding gate. This creates friction, bottlenecks, and staffing strains.\n\nModern smart airports are deploying **Biometric Single-Token Identity Systems**:\n\n- **Enrollment**: During mobile check-in or at entrance kiosks, high-resolution cameras capture a cryptographic biometric map of the traveler's face and securely link it to their passport and ticket reservation.\n- **Seamless Walk-Through**: As the passenger approaches security turnstiles or aircraft boarding gates, smart overhead cameras match their face against the flight manifest in under 2 seconds.\n- **Benefits**: Physical boarding passes become unnecessary, processing throughput quadruples, and boarding an entire 300-passenger widebody aircraft takes under 15 minutes."
                        }
                    }
                ],
                # Card 4 (Page 4): Technical Diagram (SVG)
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Green Airport and Emerging Aviation Technology Ecosystem",
                        "content": {
                            "title": "Green Sustainable Airport Ecosystem",
                            "caption": "A system architecture graphic showcasing solar panel runway buffer canopies, eGSE electric vehicle charging stations, Sustainable Aviation Fuel (SAF) infrastructure, and automated biometric boarding gates."
                        }
                    }
                ],
                # Card 5 (Page 5): Sustainability and Green Apron Initiatives
                [
                    {
                        "type": "concept_explanation",
                        "title": "Green Apron Sustainability & Clean Energy",
                        "content": {
                            "title": "Decarbonizing the Ground Footprint of Aviation",
                            "text": "While battery-powered commercial passenger airliners are decades away due to aircraft battery weight constraints, the ground operations of an airport can achieve net-zero carbon emissions today:\n\n- **Electric Ground Service Equipment (eGSE)**: Replacing diesel pushback tractors, baggage belt loaders, and cargo high-loaders with high-torque electric vehicles eliminates harmful carbon monoxide and particulate exhaust fumes from active ramp work areas.\n- **Solar Photovoltaic Generation**: Airports possess vast buffer zones between runways and taxiways that must remain clear of physical structures. These flat, clear areas are ideal locations for utility-scale solar farms.\n- **Sustainable Aviation Fuel (SAF) Hydrants**: Airports are integrating dedicated storage tanks and blending infrastructure for Sustainable Aviation Fuels produced from agricultural waste and non-food oils, reducing lifecycle flight emissions by up to 80%."
                        }
                    }
                ],
                # Card 6 (Page 6): Professional Aviation Career Pathways
                [
                    {
                        "type": "comparison_table",
                        "title": "Aviation Business Services Career Pathways",
                        "content": {
                            "title": "Career Opportunities in Modern Airport Operations",
                            "headers": ["Career Role", "Work Domain", "Core Responsibilities", "Key Qualifications & Skills"],
                            "rows": [
                                ["Customer Service Coordinator", "Terminal Landside & Concourse", "Passenger ticketing, boarding pass checks, managing special needs assistance", "Interpersonal communication, multilingual skills, reservation software"],
                                ["Turnaround Coordinator (TRC)", "Airside Apron & Stand", "Synchronizing refueling, catering, baggage loading, and on-time pushback", "Ramp safety certification, high situational awareness, time management"],
                                ["Ramp Safety Auditor", "Airfield & Operations", "Conducting apron hazard inspections, investigating ground damage, enforcing OSHA/KCAA rules", "Aviation safety management systems (SMS), incident investigation"],
                                ["Environmental Sustainability Officer", "Airport Administration", "Monitoring solar generation, terminal waste recycling, carbon footprint accounting", "Environmental science, renewable energy management, green building standards"]
                            ]
                        }
                    }
                ],
                # Card 7 (Page 7): Real-World Application (Solar-Powered Airports)
                [
                    {
                        "type": "real_world_example",
                        "title": "Africa's Pioneer Solar-Powered Airport",
                        "content": {
                            "title": "George Airport: South Africa's 100% Solar-Powered Aerodrome",
                            "text": "In 2016, George Airport in South Africa became the first aerodrome on the African continent to generate 100% of its operating electricity from localized solar power. Featuring an on-site solar farm containing thousands of photovoltaic panels, the plant produces up to 750 kilowatts of clean energy daily.\n\n- **Operational Independence**: The solar farm supplies all energy required for passenger terminal lighting, HVAC climate control, runway approach lighting, and ramp power.\n- **Resilience**: During national grid power outages, the airport operates completely independently on stored clean solar power, eliminating reliance on diesel backup generators.\n- **Replication in Kenya**: George Airport's success has inspired green energy projects across Kenya, where solar canopies are being deployed over airport parking areas at JKIA, Moi International, and Kisumu."
                        }
                    }
                ],
                # Card 8 (Page 8): Safety Connection (Automated Ramp Machinery)
                [
                    {
                        "type": "concept_explanation",
                        "title": "Aviation Safety Connection: Autonomous Robotic GSE",
                        "content": {
                            "title": "Safety Protocols for Self-Driving Luggage Carts and Robotics",
                            "text": "As airports introduce autonomous self-driving baggage carts and robotic container movers, ground operations must ensure human workers and multi-million dollar aircraft remain protected.\n\n- **Collision Hazard**: A robotic baggage cart navigating around a parked Boeing 787 can cause catastrophic structural skin puncture if sensors fail or if human workers cross its unmonitored path.\n- **Safety Protocol & Redundancy**:\n  - *Dedicated Automated Lanes*: Apron surfaces are painted with laser-guided corridors exclusively designated for automated machinery.\n  - *Active LiDAR & Optical Proximity Sensors*: Automated vehicles must incorporate 360-degree LiDAR sensors programmed to initiate emergency braking if a human or obstacle enters within 3 meters.\n  - *External Physical E-Stops*: Every autonomous ramp vehicle is equipped with prominent, physical emergency stop buttons accessible from any angle by ground personnel."
                        }
                    }
                ],
                # Card 9 (Page 9): Video Integration
                [
                    {
                        "type": "suggested_video",
                        "title": "Emerging Airport Tech: Robotics and Humanoid Baggage Handling",
                        "content": {
                            "title": "Robotics & AI in Ground Handling: The Future of Airport Operations",
                            "description": "Discover how airlines and aerodrome operators are testing robotic assistance, autonomous luggage tugs, and AI automation on the commercial apron.",
                            "url": "https://www.youtube.com/watch?v=VqETxTNoG1Y"
                        }
                    }
                ],
                # Card 10 (Page 10): Formative MCQs
                [
                    {
                        "type": "knowledge_check",
                        "title": "Diagnostic Assessment: Electric Ground Equipment Benefits",
                        "content": {
                            "question": "How does transitioning from traditional diesel vehicles to electric Ground Service Equipment (eGSE) improve health and safety on the airport apron?",
                            "options": [
                                "eGSE vehicles are significantly faster than diesel vehicles, allowing drivers to speed across active runways.",
                                "eGSE vehicles are completely automated and eliminate all human ground handling jobs.",
                                "eGSE eliminates toxic tailpipe exhaust fumes (protecting workers from carbon monoxide) and lowers motor noise, improving situational awareness.",
                                "eGSE vehicles are constructed with soft rubber exteriors, eliminating any possibility of damaging aircraft skin."
                            ],
                            "answer": "C",
                            "explanation": "Operating diesel machinery in enclosed baggage handling areas and near aircraft generates dangerous diesel soot and loud motor noise. Electric GSE produces zero localized emissions, protects respiratory health, and operates quietly, allowing ground personnel to hear warning alarms and maintain situational awareness."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Diagnostic Assessment: Aviation Career Responsibilities",
                        "content": {
                            "question": "Which professional career role in airport business services is directly responsible for conducting apron safety audits, investigating ramp damage incidents, and ensuring compliance with civil aviation regulations?",
                            "options": [
                                "Aircraft Ramp Marshaller.",
                                "Airport Safety Auditor / Manager.",
                                "Customer Service Coordinator.",
                                "Environmental Sustainability Officer."
                            ],
                            "answer": "B",
                            "explanation": "The Airport Safety Auditor / Manager oversees the aerodrome's Safety Management System (SMS). They conduct apron hazard audits, investigate ground incidents, and enforce strict compliance with national (KCAA) and international (ICAO) safety regulations."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 5: Integrated Airport-Business Simulation
        # =====================================================================
        {
            "unit_order": 4,
            "unit_name": "Integrated Airport-Business Simulation",
            "unit_description": "Capstone synthesis: multi-departmental flight turnaround coordination, crisis management under Irregular Operations (IROPS), weight and balance calculations, and regulatory safety compliance.",
            "lesson_title": "Integrated Airport-Business Simulation",
            "pages": [
                # Card 1 (Page 1): Photographic Hook & Learning Objectives
                [
                    {
                        "type": "suggested_image",
                        "title": "Collaborative Airport Flightline Ground Operations",
                        "content": {
                            "title": "Collaborative Airport Flightline Ground Operations",
                            "caption": "A coordinated multidisciplinary airport ground team managing aircraft turnaround, flightline safety protocols, and operational dispatch.",
                            "resolved_image_url": "https://upload.wikimedia.org/wikipedia/commons/3/32/A_tale_of_two-_A_team_approach_to_flightline_operations_%288046588%29.jpg"
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Learning Focus: Collaborative Airport Operations & Crisis Management",
                        "content": {
                            "title": "Learning Focus: Collaborative Airport Operations & Crisis Management",
                            "goals": [
                                "Synthesize cross-departmental roles in airport operations including passenger service, ground logistics, airport finance, and regulatory safety.",
                                "Navigate an Irregular Operations (IROPS) scenario balancing missing passenger baggage, severe en-route weather, and aircraft weight limits.",
                                "Execute mandatory safety protocols for positive baggage reconciliation under high-pressure turnaround schedules.",
                                "Finalize, audit, and sign an official flight manifest ensuring legal compliance with civil aviation regulations."
                            ]
                        }
                    }
                ],
                # Card 2 (Page 2): Key Terminology
                [
                    {
                        "type": "definition_card",
                        "title": "Simulation & Operational Crisis Vocabulary",
                        "content": {
                            "title": "Integrated Operations Terminology",
                            "definitions": [
                                {
                                    "term": "Integrated Simulation",
                                    "definition": "A structured multi-role training exercise where students enact real-world aviation roles simultaneously to resolve complex operational crises.",
                                    "example": "A classroom simulation where flight dispatch, ground handlers, and safety inspectors collaborate on an aircraft departure."
                                },
                                {
                                    "term": "Flight Manifest",
                                    "definition": "The legal dispatch document detailing verified passenger counts, cargo and baggage weights, fuel load, and aircraft center of gravity required before takeoff.",
                                    "example": "The captain signing the finalized load sheet confirming total payload is within structural limits."
                                },
                                {
                                    "term": "Irregular Operations (IROPS)",
                                    "definition": "Exceptional operational disruptions caused by severe weather, mechanical defects, or security alerts that derail scheduled flight timetables.",
                                    "example": "A sudden thunderstorm at Wilson Airport causing multi-hour flight holdbacks and passenger delays."
                                },
                                {
                                    "term": "Integrated Operations Control Center (IOCC)",
                                    "definition": "The centralized airline command facility where flight dispatchers, maintenance engineers, crew planners, and passenger coordinators coordinate live flight movements.",
                                    "example": "The Kenya Airways IOCC at JKIA coordinating flight reroutings across African destinations."
                                },
                                {
                                    "term": "Positive Baggage Reconciliation",
                                    "definition": "The mandatory safety procedure requiring 100% verification that every checked bag aboard an aircraft belongs to an onboard, seated traveler.",
                                    "example": "Halting pushback to physically remove an unboarded passenger's bag from the forward hold."
                                }
                            ]
                        }
                    }
                ],
                # Card 3 (Page 3): The Simulation Framework and Teams
                [
                    {
                        "type": "concept_explanation",
                        "title": "The Simulation Command Architecture",
                        "content": {
                            "title": "Multidisciplinary Team Structure",
                            "text": "In commercial aviation, an aircraft cannot push back from the gate through individual effort alone; it demands absolute coordination among specialized operational groups:\n\n1. **Passenger Service Team**: Operates check-in counters and boarding gates, cross-referencing boarding passes and managing delayed travelers.\n2. **Ground & Ramp Logistics Team**: Coordinates baggage cart loading, calculates cargo ULD weights, and monitors fuel hydrant pumping.\n3. **Flight Operations & Flight Crew**: Validates aircraft performance charts, plans extra safety fuel reserves, and verifies center of gravity balance.\n4. **Airport Management & Finance Team**: Tracks terminal operating budgets, balances landing fee revenues against delay compensation expenses, and assigns gates.\n5. **Regulatory & Consumer Protection Audit Team (KCAA)**: Acts as independent oversight inspectors, auditing safety checklists, enforcing passenger consumer rights, and providing legal sign-off on the flight manifest."
                        }
                    }
                ],
                # Card 4 (Page 4): Technical Diagram (SVG)
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Integrated Airport Business Simulation Command Matrix",
                        "content": {
                            "title": "Airport Operations Command Matrix",
                            "caption": "An interconnected command hub illustrating the operational communication flow between Flight Operations, Ground Logistics, Passenger Services, Airport Management, and Regulatory Safety Audits."
                        }
                    }
                ],
                # Card 5 (Page 5): The Crisis Challenge (Flight KQ-102)
                [
                    {
                        "type": "concept_explanation",
                        "title": "The Simulation Challenge: Flight KQ-102",
                        "content": {
                            "title": "A High-Stakes Operational Crisis Scenario",
                            "text": "During the classroom simulation, students manage scheduled commercial **Flight KQ-102** departing from Nairobi to Mombasa. Ten minutes before departure, three critical events occur simultaneously:\n\n- **Event 1 (The Unaccompanied Bag)**: Passenger in seat 12C checked in luggage at the terminal counter but failed to scan their boarding pass at Gate 4.\n- **Event 2 (En-Route Severe Weather)**: Meteorological radars detect severe convective thunderstorms along the flight path, forcing flight dispatch to add 800 kg of additional reserve fuel.\n- **Event 3 (Maximum Takeoff Weight Exceeded)**: Adding 800 kg of safety fuel pushes the aircraft 500 kg beyond its legal Maximum Takeoff Weight (MTOW), requiring cargo offload to remain within legal limits."
                        }
                    }
                ],
                # Card 6 (Page 6): Crisis Decision Flowchart / Table
                [
                    {
                        "type": "comparison_table",
                        "title": "Crisis Management Protocol for Flight KQ-102",
                        "content": {
                            "title": "Collaborative Resolution Workflow",
                            "headers": ["Operational Issue", "Responsible Operational Unit", "Mandatory Action Taken", "Resolution Outcome"],
                            "rows": [
                                ["Unaccompanied Bag (Seat 12C)", "Passenger Service & Ramp Team", "Ramp Supervisor halts pushback; locates suitcase barcode 12C in hold and physically offloads it", "Positive reconciliation restored; security hazard eliminated"],
                                ["Thunderstorm Safety Fuel", "Flight Crew & Flight Dispatch", "Adds 800 kg reserve fuel to allow en-route diversions around storm cells", "Flight safety ensured under stormy weather conditions"],
                                ["500 kg Overweight (MTOW)", "Ground Logistics & Finance Team", "Evaluates freight manifest: holds non-perishable machinery ULD; keeps perishable flowers onboard", "Aircraft returns within legal takeoff weight with minimal financial loss"],
                                ["Passenger Terminal Delay", "KCAA Regulatory Audit Team", "Verifies delayed passengers receive refreshments and updated gate departure announcements", "Full compliance with national consumer protection laws"]
                            ]
                        }
                    }
                ],
                # Card 7 (Page 7): Real-World Application (Airline IOCC)
                [
                    {
                        "type": "real_world_example",
                        "title": "Inside the Airline Integrated Operations Control Center (IOCC)",
                        "content": {
                            "title": "The Nerve Center of Commercial Aviation",
                            "text": "Every major airline operates an **Integrated Operations Control Center (IOCC)** working 24/7/365. At Kenya Airways' headquarters at JKIA in Nairobi, the IOCC brings together flight dispatchers, chief pilots, airframe maintenance controllers, passenger care managers, and crew schedulers in a single amphitheater room.\n\n- **Live Telemetry & Radar**: Wall-sized digital screens track real-time satellite weather radars, global aircraft GPS positions, and live fuel telemetry from aircraft in flight.\n- **Rapid Crisis Response**: When sudden fog blankets Mombasa airport, the IOCC team negotiates within 3 minutes whether to hold in air, divert to Nairobi, or refuel at an alternate field, coordinating passenger hotel accommodations before the aircraft has even touched down."
                        }
                    }
                ],
                # Card 8 (Page 8): Safety Connection (Manifest Airworthiness Sign-Off)
                [
                    {
                        "type": "concept_explanation",
                        "title": "Aviation Safety Connection: The Legal Flight Manifest",
                        "content": {
                            "title": "Why Regulatory Sign-Off is Legally Binding",
                            "text": "Under national and international civil aviation law, an aircraft cannot legally depart the gate without a verified and signed **Flight Manifest and Load Sheet**.\n\n- **Legal Responsibility**: The flight manifest is signed jointly by the Airline Flight Dispatcher, the Ramp Loadmaster, and the Aircraft Captain.\n- **Legal Declaration**: Their physical or cryptographic digital signatures certify under penalty of law that: (1) all onboard bags belong to boarded passengers; (2) total weight is strictly within structural airframe limits; (3) the center of gravity is within aerodynamic limits; and (4) fuel reserves meet legal weather minimums.\n- **Audit Authority**: KCAA and airport safety inspectors conduct unannounced ramp ramp checks to inspect manifests. Falsifying a manifest or departing without proper reconciliation constitutes a severe criminal offense leading to immediate license revocation."
                        }
                    }
                ],
                # Card 9 (Page 9): Video Integration
                [
                    {
                        "type": "suggested_video",
                        "title": "Airport Operations: Landside, Airside, and Terminal Systems",
                        "content": {
                            "title": "Integrated Airport Operations: Managing Complex Facilities",
                            "description": "Understand the comprehensive architecture of commercial airport operations, integrating airside runways, landside concourses, passenger terminals, and regulatory safety frameworks.",
                            "url": "https://www.youtube.com/watch?v=B0Ar5WsUhWs"
                        }
                    }
                ],
                # Card 10 (Page 10): Formative MCQs
                [
                    {
                        "type": "knowledge_check",
                        "title": "Diagnostic Assessment: Turnaround Baggage Reconciliation",
                        "content": {
                            "question": "During the flight turnaround simulation, if a passenger checked luggage but failed to scan their boarding pass at the gate before departure, what is the Ramp Supervisor's mandatory safety action?",
                            "options": [
                                "To transport the suitcase to the destination anyway and invoice the passenger a courier surcharge.",
                                "To move the suitcase into the passenger cabin overhead storage bin so flight attendants can monitor it.",
                                "To immediately halt cargo loading, locate the bag with the matching barcode, and physically remove it from the aircraft hold before takeoff.",
                                "To open and search the suitcase on the active tarmac ramp without security supervisor oversight."
                            ],
                            "answer": "C",
                            "explanation": "The fundamental security rule of positive baggage reconciliation is absolute: no passenger, no bag. Transporting an unaccompanied bag violates international anti-sabotage regulations. Ground crews must stop loading, find the suitcase, and remove it from the aircraft before departure."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Diagnostic Assessment: Flight Manifest Legal Significance",
                        "content": {
                            "question": "Why must the official flight manifest and load sheet be finalized, verified, and signed before the flight crew is permitted to taxi for takeoff?",
                            "options": [
                                "To collect terminal retail sales taxes and transfer them to airport commercial bank accounts.",
                                "To legally certify that passenger baggage has been reconciled, total weight is within structural limits, and safety fuel requirements are met.",
                                "To verify that the airline has sold sufficient inflight duty-free merchandise to achieve profitability on the sector.",
                                "To confirm that the ground cleaning team has washed the exterior cockpit windshields."
                            ],
                            "answer": "B",
                            "explanation": "The flight manifest is the official legal document of flight airworthiness. Signing it certifies that passenger baggage has been verified, structural weight and center-of-gravity limits are respected, and all mandatory civil aviation safety regulations have been satisfied."
                        }
                    }
                ]
            ]
        }
    ]

def ingest_grade10_aviation_topic368(replace=True):
    """Ingests Grade 10 Aviation Topic 368 curriculum data into Nexus/VLearn database."""
    print("=" * 80)
    print("VLEARN INGESTION ENGINE: Grade 10 Aviation — Topic 368 (ID: 368)")
    print("Airport Business Services")
    print("=" * 80)

    curriculum = Curriculum.objects.get(id=5)
    grade = Grade.objects.get(id=5, level=10)
    subject = Subject.objects.get(id=44, grade=grade)

    print(f"[*] Curriculum: {curriculum.name} (ID: {curriculum.id})")
    print(f"[*] Grade:      {grade.name} (ID: {grade.id}, Level: {grade.level})")
    print(f"[*] Subject:    {subject.name} (ID: {subject.id})")

    topic = Topic.objects.get(id=368, subject=subject)
    print(f"[*] Topic:      {topic.name} (ID: {topic.id}, Order: {topic.order})")

    curriculum_data = build_topic368_curriculum()
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
    print("[SUCCESS] Grade 10 Aviation Topic 368 Ingestion Complete!")
    print(f"[*] Total Lessons Ingested: {total_lessons}")
    print(f"[*] Total Pages/Cards:      {total_pages}")
    print(f"[*] Total Blocks Created:   {total_blocks}")
    print("=" * 80)

if __name__ == "__main__":
    replace_flag = "--replace" in sys.argv
    ingest_grade10_aviation_topic368(replace=replace_flag)
