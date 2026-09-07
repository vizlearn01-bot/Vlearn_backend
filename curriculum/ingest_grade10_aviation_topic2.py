"""
VLearn Grade 10 Aviation — Topic 2: Safety in Aviation
Production Ingestion Engine

Curriculum: CBC (Curriculum ID: 5)
Grade: Grade 10 (Grade ID: 5, Level: 10)
Subject: Aviation (Subject ID: 44)
Topic: Safety in Aviation (Topic ID: 248, Order: 1)

Ingests 6 Comprehensive Learning Units & Lessons (~62 Concept Cards):
  1. Safety-First Culture and Personal Responsibility (10 Cards)
  2. PPE and Safe Work-Area Housekeeping (10 Cards)
  3. Physical, Chemical, Electrical, and Ergonomic Hazards (10 Cards)
  4. Common Injuries and Severity (10 Cards)
  5. First Aid and CPR Awareness (11 Cards)
  6. Safety Observation and Aviation Careers (11 Cards)

Usage:
  ./venv/bin/python curriculum/ingest_grade10_aviation_topic2.py [--replace]
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
    text = re.sub(r'\[(?:\d+|image_\d+|S\d+.*?|[\d,\s]+)\]', '', text)
    text = re.sub(r'\[VISUAL:\s*[^\]]+\]', '', text, flags=re.IGNORECASE)
    text = re.sub(r'\[(?:REAL WORLD APPLICATION|PRACTICAL TASK|SAFETY SCENARIO)[^\]]*\]', '', text, flags=re.IGNORECASE)
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

def build_topic2_curriculum():
    """Returns the pedagogical page and block structure for Grade 10 Aviation Topic 2."""
    return [
        # =====================================================================
        # LESSON 1.2.1: Safety-First Culture and Personal Responsibility
        # =====================================================================
        {
            "unit_order": 0,
            "unit_name": "Safety-First Culture and Personal Responsibility",
            "unit_description": "Foundational safety culture, procedural compliance, reporting discipline, situational awareness, and the impact of human factors.",
            "lesson_title": "Safety-First Culture and Personal Responsibility",
            "pages": [
                # Page 1: Visual Hook & Objectives
                [
                    {
                        "type": "suggested_image",
                        "title": "Aircraft Maintenance Technician Calibrating Precision Torque Tools",
                        "content": {
                            "title": "Safety-First Culture in the Hangar",
                            "caption": "An aviation maintenance technician systematically verifying tool calibration before performing flight-critical structural servicing.",
                            "resolved_image_url": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Aircraft_Electronics_Technician_2nd_Class_Roberts_tests_a_torque_wrench_in_the_Aircraft_Intermediate_Maintenance_Department_hangar_-_DPLA_-_0689b07c7fece7f80dfae7c80bf1f3ba.jpeg"
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Learning Focus: Safety Culture and Responsibility",
                        "content": {
                            "title": "Learning Focus: Safety Culture and Responsibility",
                            "goals": [
                                "Define workplace safety, hazards, risks, and organizational safety culture.",
                                "Analyze why personal responsibility and procedural integrity are non-negotiable in aviation.",
                                "Explain the 'Human Factors' model (Dirty Dozen) and how checklists mitigate human error.",
                                "Apply active situational awareness to spot dynamic hazards in active hangar and ramp zones."
                            ]
                        }
                    }
                ],
                # Page 2: Key Terminology
                [
                    {
                        "type": "definition_card",
                        "title": "Safety Culture Terminology",
                        "content": {
                            "title": "Core Safety Concepts",
                            "definitions": [
                                {
                                    "term": "Workplace Safety",
                                    "definition": "The disciplined state where physical, biological, chemical, and operational risks are systematically identified, controlled, and kept below acceptable thresholds.",
                                    "example": "Strictly enforcing zero-smoking rules within 15 meters of fueling aircraft."
                                },
                                {
                                    "term": "Hazard",
                                    "definition": "Any source, situation, condition, or practice with the inherent potential to cause injury, ill health, equipment damage, or environmental contamination.",
                                    "example": "An uncoiled high-voltage power cable lying across a dark hangar walkway."
                                },
                                {
                                    "term": "Risk",
                                    "definition": "The calculated product of the likelihood (probability) that a hazard will cause harm and the severity (consequences) of that potential harm.",
                                    "example": "Evaluating the probability and impact of a technician falling from a 4-meter wing ladder."
                                },
                                {
                                    "term": "Safety Culture",
                                    "definition": "The collective attitudes, shared values, and procedural norms across an organization that prioritize safety above schedule pressures and commercial profit.",
                                    "example": "A technician feeling empowered to halt a flight departure upon finding a hairline crack."
                                },
                                {
                                    "term": "Situational Awareness",
                                    "definition": "The continuous cognitive process of perceiving environmental elements, comprehending their operational meaning, and projecting their future status.",
                                    "example": "Listening for approaching ramp baggage tugs before stepping out from behind an aircraft wing."
                                }
                            ]
                        }
                    }
                ],
                # Page 3: Core Explanation (The Safety Chain)
                [
                    {
                        "type": "concept_explanation",
                        "title": "The Safety-First Mindset: Integrity Over Schedules",
                        "content": {
                            "title": "The Five Links of the Aviation Safety Chain",
                            "text": "In aviation maintenance and operations, cutting corners or skipping steps is never acceptable. A single loose screw, misread torque setting, or unverified hydraulic seal can compromise airworthiness.\n\nEvery professional is held to the **Five Links of Safety**:\n1. **Procedural Obedience**: Always consult the approved Maintenance Manual; never rely on guesswork or memory.\n2. **Housekeeping Discipline**: Maintain clean, unobstructed walkways, toolboxes, and aprons.\n3. **Proactive Reporting**: Report minor anomalies, near-misses, and damaged equipment immediately before they develop into fatal accidents.\n4. **Constant Awareness**: Eliminate daydreaming and distractions on the active airfield.\n5. **Mandatory PPE**: Wear required protective armor for every specific hangar task."
                        }
                    }
                ],
                # Page 4: Technical Diagram Block
                [
                    {
                        "type": "suggested_diagram",
                        "title": "The Aviation Safety Chain and Swiss Cheese Model",
                        "content": {
                            "title": "James Reason's Swiss Cheese Accident Model",
                            "caption": "How organizational culture, engineering defenses, procedural checklists, and personal responsibility align to block active failure trajectories."
                        }
                    }
                ],
                # Page 5: Comparative Analysis Table
                [
                    {
                        "type": "comparison_table",
                        "title": "Comparing Hazardous Mindsets with Professional Safety Culture",
                        "content": {
                            "title": "Hazardous Attitudes vs. Professional Aviation Antidotes",
                            "headers": ["Hazardous Attitude", "Internal Rationalization", "Professional Antidote & Standard"],
                            "rows": [
                                ["Anti-Authority", "'Rules are too strict and slow me down.'", "'Follow the rules; they were written from hard-won lessons.'"],
                                ["Impulsivity", "'Do something quickly, anything!'", "'Not so fast. Think first, evaluate hazards, then act.'"],
                                ["Invulnerability", "'Accidents only happen to other careless people.'", "'It can happen to me; double-check the lock-wire and torque.'"],
                                ["Macho", "'I can lift this 45kg wheel alone to prove my strength.'", "'Taking unnecessary chances is foolish; request a team lift or crane.'"],
                                ["Resignation", "'What is the use? My supervisor will just ignore my hazard report.'", "'I am not helpless. I have the authority and duty to stop unsafe work.'"]
                            ]
                        }
                    }
                ],
                # Page 6: Real-World Case Study (Human Factors in Maintenance)
                [
                    {
                        "type": "real_world_example",
                        "title": "The Danger of Rushing the Sign-Off",
                        "content": {
                            "title": "Case Study: The Midnight Pressure",
                            "text": "At 01:30 AM, a maintenance crew is completing an engine inspection on a chartered executive jet scheduled to depart at 06:00 AM. A technician discovers a microscopic nick on an oil line fitting. Replacing it requires ordering a new seal from stores and delaying departure by 3 hours.\n\nThe ground manager urges: 'It is just a tiny surface scratch. Sign the release certificate so we stay on schedule.'\n\nUnder a true safety-first culture, the technician firmly refuses. An oil line under 3,000 PSI operating pressure could rupture in mid-flight, causing an uncontained engine fire. The line is replaced, preserving human lives. In aviation, schedule integrity never supersedes physical airworthiness."
                        }
                    }
                ],
                # Page 7: Educational Video Integration
                [
                    {
                        "type": "suggested_video",
                        "title": "Human Factors and Hangar Safety Culture",
                        "content": {
                            "title": "Human Factors in Aviation Maintenance",
                            "description": "Examine how fatigue, pressure, distraction, and lack of communication create workplace traps, and see how strict procedural checklists protect technicians.",
                            "url": "https://www.youtube.com/watch?v=FViSA91DP-8"
                        }
                    }
                ],
                # Page 8: Procedural Analysis (The 5-Step Hazard Reporting Procedure)
                [
                    {
                        "type": "step_process",
                        "title": "The 5-Step Aviation Hazard Reporting Protocol",
                        "content": {
                            "title": "Standard Operating Procedure: Reporting a Hazard",
                            "steps": [
                                "1. Stop Unsafe Work: Cease maintenance activity immediately if an uncontrolled hazard or defective tool is identified.",
                                "2. Make the Area Safe: Place high-visibility warning cones or caution tape to prevent colleagues from walking into the danger zone.",
                                "3. Tag Out Equipment: Attach a red 'DO NOT OPERATE' safety tag to the damaged breaker, tool, or aircraft system.",
                                "4. File an Official Hazard Report: Document the specific component part number, location, and observed defect in the Safety Management System (SMS) log.",
                                "5. Verify Resolution: Never remove safety tags or resume aircraft operation until an authorized quality inspector signs off the repair."
                            ]
                        }
                    }
                ],
                # Page 9: Formative Knowledge Check 1
                [
                    {
                        "type": "knowledge_check",
                        "title": "Diagnostic Check: Safety Integrity",
                        "content": {
                            "question": "An apprentice technician notices that a hydraulic line pressure gauge has a visible hairline fracture on its glass bezel. The line supervisor states: 'It still shows pressure, we will fix it next week.' What is the correct, professional response?",
                            "options": [
                                "Follow the supervisor's instruction because seniority takes precedence over individual safety observations.",
                                "Halt operation of the system, tag out the gauge, log the defect in the official maintenance tracking system, and replace it before flight release.",
                                "Cover the cracked glass with transparent tape so inspectors do not flag it during ramp spot-checks.",
                                "Ignore the issue but remind the night shift technician to keep an eye on it."
                            ],
                            "answer": "B",
                            "explanation": "In an aviation safety culture, safety is the personal responsibility of every worker regardless of rank. Operating damaged equipment violates airworthiness standards, and procedures require immediate logging and replacement."
                        }
                    }
                ],
                # Page 10: Formative Knowledge Check 2 & Summary
                [
                    {
                        "type": "knowledge_check",
                        "title": "Diagnostic Check: Situational Awareness",
                        "content": {
                            "question": "How does dynamic 'situational awareness' differ from merely memorizing written safety regulations?",
                            "options": [
                                "Situational awareness means reciting the company health and safety manual verbatim during audits.",
                                "Situational awareness is the continuous cognitive process of actively monitoring physical surroundings, detecting real-time changes, and anticipating potential hazards before accidents occur.",
                                "Situational awareness is an advanced skill exclusive to airline captains and air traffic controllers.",
                                "Situational awareness simply requires knowing where fire alarm pull stations are located."
                            ],
                            "answer": "B",
                            "explanation": "Situational awareness requires active, continuous observation of changing conditions—such as noticing an approaching vehicle or moving propeller—enabling workers to anticipate and evade danger dynamically."
                        }
                    },
                    {
                        "type": "summary",
                        "title": "Core Takeaways: Safety-First Culture",
                        "content": {
                            "title": "Summary & Synthesis",
                            "summary_points": [
                                "Safety is not an obstacle to aviation; it is the fundamental pre-condition of flight.",
                                "Over 80% of aviation incidents trace back to human factors (the Dirty Dozen), including fatigue, complacency, and rushing.",
                                "A healthy safety culture empowers every employee, from apprentice to chief engineer, to halt unsafe operations without fear of reprisal.",
                                "Situational awareness and procedural compliance together form the primary barrier against catastrophic workplace accidents."
                            ]
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 1.2.2: PPE and Safe Work-Area Housekeeping
        # =====================================================================
        {
            "unit_order": 1,
            "unit_name": "PPE and Safe Work-Area Housekeeping",
            "unit_description": "Selection, inspection, and maintenance of Personal Protective Equipment (PPE), hangar housekeeping standards, spill response, and FOD mitigation.",
            "lesson_title": "PPE and Safe Work-Area Housekeeping",
            "pages": [
                # Page 1: Visual Hook & Objectives
                [
                    {
                        "type": "suggested_image",
                        "title": "Industrial Hearing Protection Ear Muffs for Aviation Ramp Safety",
                        "content": {
                            "title": "Aviation Personal Protective Equipment (PPE)",
                            "caption": "Professional acoustic ear defenders designed to attenuate damaging high-decibel jet engine noise on the flight line and hangar floor.",
                            "resolved_image_url": "https://upload.wikimedia.org/wikipedia/commons/0/07/Ear_muff_white_bg.jpg"
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Learning Focus: PPE and Housekeeping",
                        "content": {
                            "title": "Learning Focus: PPE and Housekeeping",
                            "goals": [
                                "Identify, select, inspect, and maintain essential aviation Personal Protective Equipment (PPE).",
                                "Explain the danger of Foreign Object Debris/Damage (FOD) to turbine engines and flight controls.",
                                "Execute the 3 core principles of hangar housekeeping: clear walkways, clean-as-you-go, and immediate spill control.",
                                "Describe proper chemical spill containment using absorbent granules and hazardous waste disposal."
                            ]
                        }
                    }
                ],
                # Page 2: Key Terminology
                [
                    {
                        "type": "definition_card",
                        "title": "PPE and Housekeeping Terminology",
                        "content": {
                            "title": "Workplace Protection Terms",
                            "definitions": [
                                {
                                    "term": "Personal Protective Equipment (PPE)",
                                    "definition": "Specialized gear, clothing, and barrier devices worn by personnel to minimize exposure to physical, chemical, electrical, and mechanical hazards.",
                                    "example": "Impact-resistant safety goggles, acoustic ear defenders, high-visibility reflective vests, and steel-toe boots."
                                },
                                {
                                    "term": "Foreign Object Debris (FOD)",
                                    "definition": "Any loose article, tool, fragment of metal, wire, gravel, or rubbish located on an apron, runway, taxiway, or hangar floor that can cause damage to aircraft.",
                                    "example": "A dropped bolt sucked into a jet engine during taxiing, resulting in catastrophic turbine blade failure."
                                },
                                {
                                    "term": "Housekeeping",
                                    "definition": "The systematic daily discipline of organizing work areas, clearing escape routes, cleaning oil and hydraulic spills, and returning tools to shadow boards.",
                                    "example": "Conducting an end-of-shift FOD walk along the apron to collect stray metal offcuts."
                                },
                                {
                                    "term": "Decibel (dB)",
                                    "definition": "The logarithmic unit used to measure sound intensity. Noise levels above 85 dB require mandatory hearing protection to prevent irreversible sensorineural hearing loss.",
                                    "example": "A running jet engine generates 130–140 dB at close range, which can rupture eardrums without ear defenders."
                                }
                            ]
                        }
                    }
                ],
                # Page 3: Core Explanation (The PPE Armor Layout)
                [
                    {
                        "type": "concept_explanation",
                        "title": "Your Aviation Armor: The PPE Five-Point Ensemble",
                        "content": {
                            "title": "Equipping for the Flight Line and Hangar",
                            "text": "Aircraft hangars and flight lines contain spinning propellers, 3,000 PSI hydraulic lines, intense noise, and toxic solvents. Technicians protect themselves with a five-point PPE ensemble:\n\n1. **Eye & Face Protection**: Polycarbonate safety glasses with side shields protect against metal swarf, safety-wire clippings, and chemical splashes.\n2. **Hearing Protection**: Over-ear acoustic defenders or foam earplugs attenuate roaring turbofans, auxiliary power units (APUs), and pneumatic rivet guns.\n3. **High-Visibility Outerwear**: Florescent orange or yellow reflective vests ensure airport vehicle drivers and taxiing pilots can spot personnel in poor visibility.\n4. **Hand Protection**: Nitrile chemical-resistant gloves shield skin from toxic hydraulic fluids (such as Skydrol) and fuel, while leather gloves protect against burrs and burns.\n5. **Footwear**: Steel-toed safety boots with slip-resistant, fuel-resistant rubber soles protect toes from falling components and prevent slips on oily concrete."
                        }
                    }
                ],
                # Page 4: Technical Diagram Block
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Comprehensive Aviation PPE and Hangar Safety Zones",
                        "content": {
                            "title": "Aviation Technician PPE & Zone Architecture",
                            "caption": "Head-to-toe personal protective equipment layout mapped to hangar safety walkways, FOD hazard bins, and emergency eyewash stations."
                        }
                    }
                ],
                # Page 5: Comparative Housekeeping Table
                [
                    {
                        "type": "comparison_table",
                        "title": "Hangar Housekeeping Best Practices vs. Dangerous Violations",
                        "content": {
                            "title": "Housekeeping Standards on the Airfield",
                            "headers": ["Area / System", "Compliant Professional Standard", "Hazardous Non-Compliant Violation"],
                            "rows": [
                                ["Walkways & Aisles", "Painted yellow borders kept 100% free of cords, parts, and ladders", "Trailing electrical leads and air hoses running across walking corridors"],
                                ["Tool Management", "Shadow boards and cut-out foam trays where every tool is accounted for", "Leaving loose screwdrivers, sockets, or wrenches resting on aircraft horizontal stabilizers"],
                                ["Chemical Fluid Spills", "Immediate perimeter barricade with cones, absorbent clay application, hazmat disposal", "Walking past an oil slick assuming evaporation or leaving it for the janitorial shift"],
                                ["Trash & Metal Scraps", "Dedicated red FOD bins with self-closing lids emptied after each shift", "Tossing safety-wire clippings and rag offcuts onto the concrete hangar floor"]
                            ]
                        }
                    }
                ],
                # Page 6: Real-World Case Study (The Danger of FOD)
                [
                    {
                        "type": "real_world_example",
                        "title": "The Million-Dollar Pebble: How FOD Destroys Jet Engines",
                        "content": {
                            "title": "The Physics of Turbine Blade Ingestion",
                            "text": "On an active taxiway at an international airport, a single 10mm steel nut is dropped during maintenance on a baggage tug. Ten minutes later, a Boeing 787 taxiing for takeoff ingests the loose nut into its high-bypass turbofan.\n\nThe titanium fan blades, spinning at over 3,000 RPM with tip speeds approaching Mach 1, strike the nut. The impact shatters three fan blades, throwing metal fragments into the core compressor, causing an immediate engine surge and catastrophic fire.\n\nThe resulting damage totals 12 million USD in repairs and grounds the aircraft for two weeks. This real-world risk explains why airports conduct coordinated 'FOD Walks' daily, where personnel walk shoulder-to-shoulder scanning every square meter of asphalt."
                        }
                    }
                ],
                # Page 7: Educational Video Integration
                [
                    {
                        "type": "suggested_video",
                        "title": "Aircraft Fueling Hazards, PPE, and Static Bonding",
                        "content": {
                            "title": "Flight Line PPE and Fuel Handling Safety",
                            "description": "Observe professional aircraft fueling operations demonstrating bonding cable attachment, specialized nitrile gloves, eye protection, and emergency fuel shutoff procedures.",
                            "url": "https://www.youtube.com/watch?v=H4L_Coqawz8"
                        }
                    }
                ],
                # Page 8: Procedural Analysis (Hangar Spill Response Protocol)
                [
                    {
                        "type": "step_process",
                        "title": "Emergency Hangar Chemical and Fuel Spill Response",
                        "content": {
                            "title": "The 4-Step Spill Containment Protocol",
                            "steps": [
                                "1. Evacuate & Secure: Immediately clear the perimeter, eliminate all potential ignition sources (no electrical switches or open flames), and place warning cones.",
                                "2. Don Required PPE: Put on splash goggles, an organic vapor respirator, and heavy nitrile chemical gloves before approaching the spill.",
                                "3. Dam and Absorb: Surround the liquid with absorbent spill socks or granules to stop flow toward floor drains, then cover with absorbent pads.",
                                "4. Hazmat Disposal: Sweep used absorbent materials into labeled yellow hazardous waste drums and document the spill in the facility environmental register."
                            ]
                        }
                    }
                ],
                # Page 9: Formative Knowledge Check 1
                [
                    {
                        "type": "knowledge_check",
                        "title": "Diagnostic Check: The Missing Tool",
                        "content": {
                            "question": "While replacing an actuator inside a wing inspection bay, a technician accidentally drops a small 10mm socket wrench inside the wing cavity. The socket cannot be seen. What must the technician do?",
                            "options": [
                                "Close the inspection hatch and proceed with the flight release, as a small socket will not impact structural strength.",
                                "Immediately halt work, report the missing tool, and systematically search the cavity with mirrors, flashlights, or magnetic retrievers until the tool is accounted for.",
                                "Spray expanding foam into the wing to hold the loose tool in place.",
                                "Log that the socket was broken and discarded to pass the tool-count audit."
                            ],
                            "answer": "B",
                            "explanation": "Any loose tool or hardware left inside an aircraft structure is dangerous Foreign Object Debris (FOD) that can jam flight control cables or interfere with hydraulic actuators, causing catastrophic flight failure."
                        }
                    }
                ],
                # Page 10: Formative Knowledge Check 2 & Summary
                [
                    {
                        "type": "knowledge_check",
                        "title": "Diagnostic Check: Acoustic Safety",
                        "content": {
                            "question": "Which item of PPE is mandatory when working within 20 meters of an active aircraft auxiliary power unit (APU) or running jet engine?",
                            "options": [
                                "High-visibility reflective vest",
                                "Acoustic hearing protection (ear defenders or rated earplugs)",
                                "Chemical-resistant apron",
                                "Heavy welding gloves"
                            ],
                            "answer": "B",
                            "explanation": "Turbine engines and APUs generate noise levels well above 120 dB, capable of causing instantaneous and permanent sensorineural hearing damage unless high-attenuation hearing protection is worn."
                        }
                    },
                    {
                        "type": "summary",
                        "title": "Core Takeaways: PPE and Housekeeping",
                        "content": {
                            "title": "Summary & Synthesis",
                            "summary_points": [
                                "PPE represents the final physical barrier protecting workers from noise, chemical splashes, falling objects, and high-visibility hazards.",
                                "FOD (Foreign Object Debris) poses a multi-million-dollar threat to aircraft engines and flight control surfaces.",
                                "Clean-as-you-go tool accountability ensures zero foreign articles are left inside airframes during maintenance.",
                                "Chemical spills must be immediately dammed, absorbed, and disposed of in designated hazardous waste containers."
                            ]
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 1.2.3: Physical, Chemical, Electrical, and Ergonomic Hazards
        # =====================================================================
        {
            "unit_order": 2,
            "unit_name": "Physical, Chemical, Electrical, and Ergonomic Hazards",
            "unit_description": "Classification into four scientific hazard families, hazard identification, the Hierarchy of Controls, and safe ergonomic manual handling.",
            "lesson_title": "Physical, Chemical, Electrical, and Ergonomic Hazards",
            "pages": [
                # Page 1: Visual Hook & Objectives
                [
                    {
                        "type": "suggested_image",
                        "title": "Aviation Technicians Operating in a Heavy Maintenance Hangar",
                        "content": {
                            "title": "Hazard Identification in the Aviation Hangar",
                            "caption": "An active military maintenance bay showing elevated work platforms, hydraulic jacks, and high-voltage ground power cables that require constant hazard control.",
                            "resolved_image_url": "https://upload.wikimedia.org/wikipedia/commons/2/2b/Defense.gov_photo_essay_080721-F-6044B-226.jpg"
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Learning Focus: The Four Hazard Families",
                        "content": {
                            "title": "Learning Focus: The Four Hazard Families",
                            "goals": [
                                "Classify aviation workplace hazards into Physical, Chemical, Electrical, and Ergonomic families.",
                                "Apply the industrial Hierarchy of Controls (Elimination to PPE) to mitigate aviation risks.",
                                "Identify specific hazardous chemical fluids (Skydrol hydraulic fluid, Jet A-1 fuel, solvent degreasers).",
                                "Demonstrate safe ergonomic body mechanics for manual lifting and confined-space airframe work."
                            ]
                        }
                    }
                ],
                # Page 2: Key Terminology
                [
                    {
                        "type": "definition_card",
                        "title": "Hazard Classification Vocabulary",
                        "content": {
                            "title": "The Four Hazard Families",
                            "definitions": [
                                {
                                    "term": "Physical Hazard",
                                    "definition": "Environmental factors that cause physical bodily trauma without chemical interaction, such as extreme noise, spinning machinery, falling objects, slips, and working at heights.",
                                    "example": "Working on scaffolding 5 meters above concrete without a fall-arrest harness."
                                },
                                {
                                    "term": "Chemical Hazard",
                                    "definition": "Substances that cause acute or chronic health damage through toxicity, corrosive burns, respiratory irritation, or combustibility upon contact or inhalation.",
                                    "example": "Organophosphate ester hydraulic fluid (Skydrol) or aromatic hydrocarbon degreasers."
                                },
                                {
                                    "term": "Electrical Hazard",
                                    "definition": "Risks of electrocution, electrical burns, flashover explosions, and static spark ignition caused by energized 115V AC / 28V DC systems or ungrounded equipment.",
                                    "example": "Frayed ground-power cables on a rain-soaked ramp."
                                },
                                {
                                    "term": "Ergonomic Hazard",
                                    "definition": "Biomechanical stressors that inflict muscular or skeletal damage through repetitive strain, heavy manual lifting, or awkward sustained postures in confined spaces.",
                                    "example": "Lifting a 35kg starter-generator with a bent spine or working in a cramped wing root."
                                }
                            ]
                        }
                    }
                ],
                # Page 3: Core Explanation (The Hierarchy of Controls)
                [
                    {
                        "type": "concept_explanation",
                        "title": "The Four Hazard Families and the Hierarchy of Controls",
                        "content": {
                            "title": "Systematic Risk Mitigation",
                            "text": "When confronted with hazards, professional safety engineers do not simply issue earplugs or gloves and hope for the best. They apply the **Hierarchy of Hazard Controls** in strict priority order:\n\n1. **Elimination (Most Effective)**: Completely remove the hazard (e.g., redesigning a component so it no longer requires toxic solvent cleaning).\n2. **Substitution**: Replace the dangerous item with a safer alternative (e.g., swapping a flammable solvent for a biodegradable, water-based degreaser).\n3. **Engineering Controls**: Isolate people from the hazard (e.g., installing physical perimeter guardrails around engine test stands or local exhaust ventilation hoods).\n4. **Administrative Controls**: Alter work procedures (e.g., scheduling mandatory rest rotations to avoid fatigue and implementing strict 'Lock-Out/Tag-Out' protocols).\n5. **Personal Protective Equipment (Least Effective)**: Protect the worker with barrier gear (safety glasses, respirators, ear defenders). PPE is the last line of defense, not the first!"
                        }
                    }
                ],
                # Page 4: Technical Diagram Block
                [
                    {
                        "type": "suggested_diagram",
                        "title": "The Four Aviation Hazard Families and Control Hierarchy",
                        "content": {
                            "title": "Aviation Hazard Taxonomy and Hierarchy of Controls",
                            "caption": "Categorization of Physical, Chemical, Electrical, and Ergonomic hazards alongside the five-tier hierarchy of controls from Elimination to PPE."
                        }
                    }
                ],
                # Page 5: Comparative Hazard Matrix
                [
                    {
                        "type": "comparison_table",
                        "title": "Aviation Hazard Families, Examples, and Engineering Controls",
                        "content": {
                            "title": "Matrix of Aviation Hazards and Required Controls",
                            "headers": ["Hazard Family", "Specific Hangar Scenario", "Primary Bodily Risk", "Preferred Engineering / Admin Control"],
                            "rows": [
                                ["Physical", "Working on tail vertical stabilizer at 8m height", "Severe impact fracture or fatal fall", "Certified scissor lift with locked safety harnesses and anchor lines"],
                                ["Chemical", "Draining Skydrol hydraulic fluid from landing gear", "Chemical eye burns, severe dermatitis", "Safety Data Sheet (SDS) review, full-face splash shield, butyl gloves"],
                                ["Electrical", "Connecting 400Hz Ground Power Unit (GPU) to aircraft", "High-voltage electric shock, arc flash", "Insulated connectors, ground-fault circuit interrupters (GFCI), static bonding wire"],
                                ["Ergonomic", "Removing heavy main landing gear brake assembly (45kg)", "Acute lumbar disc herniation, back muscle tear", "Hydraulic brake-removal lift cart or coordinated two-person team lift"]
                            ]
                        }
                    }
                ],
                # Page 6: Real-World Case Study (Chemical Safety - Skydrol)
                [
                    {
                        "type": "real_world_example",
                        "title": "Handling Skydrol: Aviation's Fire-Resistant Chemical Threat",
                        "content": {
                            "title": "Why Aviation Fluids Require Specialized Protection",
                            "text": "Commercial airliners operate hydraulic systems at extreme pressures (3,000 to 5,000 PSI). To prevent engine heat from igniting hydraulic leaks, airlines use synthetic phosphate-ester fluids known as **Skydrol**.\n\nWhile highly fire-resistant, Skydrol is aggressive to human tissue. If pressurized Skydrol mists into a technician's eyes, it causes agonizing chemical burns and temporary blindness. If it touches skin, it strips natural oils, causing severe dermatitis. Standard latex gloves dissolve in seconds when exposed to Skydrol.\n\nAviation safety procedures dictate that technicians working on hydraulic systems must wear specialized **butyl rubber gloves**, full-face splash shields, and work within 10 seconds of a functioning emergency eyewash fountain."
                        }
                    }
                ],
                # Page 7: Educational Video Integration
                [
                    {
                        "type": "suggested_video",
                        "title": "Hazard Identification in Aircraft Maintenance",
                        "content": {
                            "title": "Interactive Hazard Spotting in the Hangar",
                            "description": "Walk through a virtual aircraft maintenance hangar to identify and classify physical tripping traps, ungrounded cords, chemical containers, and ergonomic lifting errors.",
                            "url": "https://www.youtube.com/watch?v=H4L_Coqawz8"
                        }
                    }
                ],
                # Page 8: Procedural Analysis (Safe Ergonomic Lifting)
                [
                    {
                        "type": "step_process",
                        "title": "Safe Ergonomic Manual Lifting Protocol",
                        "content": {
                            "title": "Standard Operating Procedure: Manual Lifting",
                            "steps": [
                                "1. Assess Weight & Path: Check component weight tag. If over 20kg, do not lift alone. Ensure travel path is clean and non-slip.",
                                "2. Broad Base of Support: Stand with feet shoulder-width apart, placing one foot slightly forward alongside the object.",
                                "3. Bend at the Knees: Lower your body by bending your knees and hips while maintaining a straight, upright spine.",
                                "4. Secure Grip & Close Hold: Grasp the load firmly and pull it close to your chest/torso before lifting.",
                                "5. Power Through the Legs: Rise smoothly using the strong muscles of your thighs and glutes. Never twist your back while lifting!"
                            ]
                        }
                    }
                ],
                # Page 9: Formative Knowledge Check 1
                [
                    {
                        "type": "knowledge_check",
                        "title": "Diagnostic Check: Hazard Classification",
                        "content": {
                            "question": "A technician is using an unventilated solvent bath to degrease wheel bearings. The solvent releases concentrated toxic fumes, causing dizziness and eye irritation. How is this hazard classified?",
                            "options": [
                                "Physical Hazard",
                                "Chemical Hazard",
                                "Ergonomic Hazard",
                                "Biological Hazard"
                            ],
                            "answer": "B",
                            "explanation": "Toxic fumes, solvent vapors, fuels, and corrosive cleaning acids belong directly to the Chemical Hazard family, requiring organic vapor respirators, ventilation, and gloves."
                        }
                    }
                ],
                # Page 10: Formative Knowledge Check 2 & Summary
                [
                    {
                        "type": "knowledge_check",
                        "title": "Diagnostic Check: Hierarchy of Controls",
                        "content": {
                            "question": "According to the industrial Hierarchy of Controls, which method is the most effective way to protect workers from a severe hazard?",
                            "options": [
                                "Issuing heavy personal protective equipment (PPE) such as safety boots and goggles",
                                "Putting up caution signs and warning labels around the hazard area",
                                "Physically eliminating the hazard entirely from the workspace",
                                "Training employees to work faster so they spend less time near the hazard"
                            ],
                            "answer": "C",
                            "explanation": "Elimination is the highest and most effective tier of control because removing the hazard completely eliminates all risk of harm, whereas PPE is the lowest tier and relies on user compliance."
                        }
                    },
                    {
                        "type": "summary",
                        "title": "Core Takeaways: The Four Hazard Families",
                        "content": {
                            "title": "Summary & Synthesis",
                            "summary_points": [
                                "Workplace hazards divide into Physical (forces/falls), Chemical (toxic fluids), Electrical (currents/sparks), and Ergonomic (musculoskeletal strain).",
                                "The Hierarchy of Controls prioritizes Elimination, Substitution, and Engineering defenses before relying on Administrative rules and PPE.",
                                "Aviation chemicals like Skydrol hydraulic fluid require specialized butyl rubber PPE and rapid-access eyewash stations.",
                                "Ergonomic lifting requires bending at the knees, holding loads close to the chest, and powering through the legs to prevent debilitating back injuries."
                            ]
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 1.2.4: Common Injuries and Severity
        # =====================================================================
        {
            "unit_order": 3,
            "unit_name": "Common Injuries and Severity",
            "unit_description": "Types of workplace injuries (lacerations, burns, fractures, electrical shock, sprains vs strains) and classification into minor, serious, and fatal severity tiers.",
            "lesson_title": "Common Injuries and Severity",
            "pages": [
                # Page 1: Visual Hook & Objectives
                [
                    {
                        "type": "suggested_image",
                        "title": "Industrial Medical Trauma First Aid Response Kit",
                        "content": {
                            "title": "Workplace Injury Assessment and Triage",
                            "caption": "A professional trauma first aid kit stocked with sterile gauze, tourniquets, and burn dressings used to treat hangar injuries.",
                            "resolved_image_url": "https://upload.wikimedia.org/wikipedia/commons/a/aa/Adventure_Medical_Kits_Professional_Trauma_Pak_Kit_with_QuikClot_%2841159334595%29.jpg"
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Learning Focus: Common Injuries and Severity",
                        "content": {
                            "title": "Learning Focus: Common Injuries and Severity",
                            "goals": [
                                "Identify common aviation workplace injuries: lacerations, burns, fractures, shocks, sprains, and strains.",
                                "Distinguish precisely between ligament sprains and muscle/tendon strains.",
                                "Classify workplace injuries into Minor, Serious, and Fatal severity levels.",
                                "Formulate immediate communication and escalation protocols for serious medical emergencies."
                            ]
                        }
                    }
                ],
                # Page 2: Key Terminology
                [
                    {
                        "type": "definition_card",
                        "title": "Workplace Injury Terminology",
                        "content": {
                            "title": "Injury Classification Terms",
                            "definitions": [
                                {
                                    "term": "Laceration",
                                    "definition": "A deep cut, tear, or opening in skin tissue caused by sharp sheet metal, sheared rivets, broken glass, or cutting tools.",
                                    "example": "A technician slicing their forearm on a jagged wing trailing edge."
                                },
                                {
                                    "term": "Fracture",
                                    "definition": "A complete or partial crack or break in bone structure, typically caused by falls from ladders or heavy dropped components.",
                                    "example": "A broken wrist resulting from falling backward off aircraft scaffolding."
                                },
                                {
                                    "term": "Sprain",
                                    "definition": "The stretching or tearing of ligaments—the tough, fibrous bands of tissue that connect two bones together at a joint.",
                                    "example": "A severely twisted ankle caused by stepping into an unseen oily floor depression."
                                },
                                {
                                    "term": "Strain",
                                    "definition": "The overstretching or tearing of muscles or tendons—the fibrous cords that connect muscle tissue to bone.",
                                    "example": "A pulled lower back muscle caused by lifting a heavy battery with a twisted spine."
                                },
                                {
                                    "term": "Electric Shock",
                                    "definition": "Physiological trauma caused by electrical current passing through the human body, capable of inducing cardiac arrest, severe internal burns, and respiratory failure.",
                                    "example": "Contacting an ungrounded 115V AC ground power receptacle."
                                }
                            ]
                        }
                    }
                ],
                # Page 3: Core Explanation (The Severity Tiers)
                [
                    {
                        "type": "concept_explanation",
                        "title": "The Three Levels of Workplace Injury Severity",
                        "content": {
                            "title": "Triage and Urgency Classification",
                            "text": "When an accident occurs in a hangar, safety managers must immediately categorize the severity to coordinate emergency medical services:\n\n- **Tier 1: Minor Injuries**:\n  - Small cuts, minor abrasions, first-degree superficial burns, mild muscle soreness.\n  - Can be treated on-site using standard first-aid kit supplies; worker returns to duty quickly.\n\n- **Tier 2: Serious Injuries**:\n  - Deep arterial or venous lacerations, bone fractures, second- or third-degree thermal/chemical burns, electric shocks, concussions.\n  - Requires immediate on-site stabilization followed by rapid escalation to professional paramedics and emergency hospital trauma care.\n\n- **Tier 3: Fatal / Life-Threatening Emergencies**:\n  - Severe crush trauma, electrical ventricular fibrillation (heart stoppage), severed arteries, respiratory arrest.\n  - Requires immediate Hands-Only CPR, automated external defibrillators (AED), and emergency rescue services within seconds to prevent death."
                        }
                    }
                ],
                # Page 4: Technical Diagram Block
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Workplace Injury Severity Hierarchy and Triage Scale",
                        "content": {
                            "title": "Injury Severity Triage Pyramid",
                            "caption": "Three-tiered categorization of Minor, Serious, and Fatal injuries with associated medical escalation pathways."
                        }
                    }
                ],
                # Page 5: Comparative Anatomy Table (Sprain vs. Strain)
                [
                    {
                        "type": "comparison_table",
                        "title": "Anatomical Comparison: Sprain vs. Strain",
                        "content": {
                            "title": "Distinguishing Ligament Sprains from Muscle Strains",
                            "headers": ["Feature", "Sprain (Ligament Injury)", "Strain (Muscle / Tendon Injury)"],
                            "rows": [
                                ["Tissue Involved", "Ligaments (fibrous bands connecting bone to bone)", "Muscles or Tendons (cords connecting muscle to bone)"],
                                ["Typical Location", "Joints: Ankles, wrists, knees", "Muscular bodies: Lower back, hamstrings, shoulders"],
                                ["Primary Cause", "Twisting, wrenching, or falling awkwardly on a joint", "Lifting excessive weight, sudden violent pulling, poor posture"],
                                ["Physical Symptoms", "Rapid localized joint swelling, bruising, joint instability", "Muscle spasms, sharp localized cramping, stiffness, weakness"],
                                ["First Aid Standard", "R.I.C.E. protocol (Rest, Ice, Compression, Elevation)", "Rest, gentle cold therapy, avoiding re-injury loading"]
                            ]
                        }
                    }
                ],
                # Page 6: Real-World Incident Analysis
                [
                    {
                        "type": "real_world_example",
                        "title": "Incident Investigation: The Fall from Engine Scaffolding",
                        "content": {
                            "title": "Hangar Incident Scenario Analysis",
                            "text": "An aircraft technician is inspecting the thrust reverser on a Boeing 777 engine, working from an elevated mobile platform 3 meters high. An oily puddle causes the technician to lose footing and fall to the concrete hangar floor.\n\n- **Injury 1**: Forearm strikes a sharp sheet-metal edge, resulting in a deep, heavily bleeding wound (**Laceration**).\n- **Injury 2**: Lands awkwardly on right foot, causing severe joint inversion (**Sprain**).\n- **Injury 3**: Forearm bone is deformed and unable to support movement (**Fracture**).\n\n**Severity Classification**: This incident is classified as a **Serious Injury**. While the technician is conscious, deep bleeding and bone fractures require immediate immobilization, direct pressure, and immediate emergency ambulance dispatch."
                        }
                    }
                ],
                # Page 7: Educational Video Integration
                [
                    {
                        "type": "suggested_video",
                        "title": "Workplace Injury Response and Severity Triage",
                        "content": {
                            "title": "Classifying and Responding to Workplace Trauma",
                            "description": "Examine how industrial first responders triage lacerations, burns, and fractures, determining when on-site first aid suffices versus emergency medical escalation.",
                            "url": "https://www.youtube.com/watch?v=9g0H2g7sLq8"
                        }
                    }
                ],
                # Page 8: Procedural Analysis (Emergency Incident Escalation)
                [
                    {
                        "type": "step_process",
                        "title": "Emergency Medical Incident Escalation Procedure",
                        "content": {
                            "title": "Action Protocol for Serious Injuries",
                            "steps": [
                                "1. Ensure Scene Safety: Verify that the injured worker is not in contact with live wires, leaking fuel, or falling debris before approaching.",
                                "2. Call for Emergency Assistance: Alert the airport emergency dispatch (or 999/112). Clearly state: exact hangar number, nature of injury, and number of casualties.",
                                "3. Control Life Threats: Apply firm, direct pressure with sterile dressings to severe bleeding lacerations; do not move suspected fractures.",
                                "4. Reassure and Monitor: Keep casualty warm and calm. Continuously check breathing and consciousness until medical paramedics arrive.",
                                "5. Preserve Evidence: Do not alter tools or scaffolding; safety investigators must examine the scene to identify root causes."
                            ]
                        }
                    }
                ],
                # Page 9: Formative Knowledge Check 1
                [
                    {
                        "type": "knowledge_check",
                        "title": "Diagnostic Check: Sprain vs. Strain",
                        "content": {
                            "question": "While pulling a heavy electrical power cable across the ramp, a technician experiences a sudden, sharp, shooting pain in the lumbar region of their lower back. This injury is best diagnosed as a:",
                            "options": [
                                "Sprain (ligament rupture at a bone joint)",
                                "Strain (overstretching or tearing of back muscles or tendons)",
                                "Surface laceration",
                                "Greenstick fracture"
                            ],
                            "answer": "B",
                            "explanation": "Strains involve damage to muscles and tendons, commonly occurring in the lower back due to excessive pulling or lifting forces, whereas sprains involve twisting joints and tearing ligaments."
                        }
                    }
                ],
                # Page 10: Formative Knowledge Check 2 & Summary
                [
                    {
                        "type": "knowledge_check",
                        "title": "Diagnostic Check: Electrical Severity",
                        "content": {
                            "question": "A worker contacts an energized 115V AC line inside an avionics bay, collapses, and is unresponsive with absent breathing. What is the injury severity classification and immediate required action?",
                            "options": [
                                "Minor Injury; give the worker water and allow them to rest for 15 minutes.",
                                "Life-Threatening / Fatal Severity; immediately isolate the electrical power source, summon emergency paramedics, and initiate CPR.",
                                "Ergonomic Hazard; log the event in the monthly posture ergonomics report.",
                                "Non-reportable near-miss incident."
                            ],
                            "answer": "B",
                            "explanation": "An electric shock causing unconsciousness and respiratory arrest is a critical, life-threatening emergency. Power must be isolated first (to prevent rescuer electrocution), followed immediately by emergency medical dispatch and CPR."
                        }
                    },
                    {
                        "type": "summary",
                        "title": "Core Takeaways: Common Injuries and Severity",
                        "content": {
                            "title": "Summary & Synthesis",
                            "summary_points": [
                                "Hangar injuries range from lacerations and chemical burns to fractures and life-threatening electrical shocks.",
                                "Sprains damage fibrous bone-to-bone ligaments, while strains damage muscular bodies and tendons.",
                                "Workplace injuries are stratified into Minor (first-aid treatable), Serious (requiring hospitalization), and Fatal/Life-Threatening tiers.",
                                "In serious accidents, rapid escalation, scene safety verification, and direct pressure on bleeding are critical life-saving actions."
                            ]
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 1.2.5: First Aid and CPR Awareness
        # =====================================================================
        {
            "unit_order": 4,
            "unit_name": "First Aid and CPR Awareness",
            "unit_description": "First-aid response protocols for lacerations, burns, fractures, and electric shock, alongside life-saving Hands-Only CPR techniques.",
            "lesson_title": "First Aid and CPR Awareness",
            "pages": [
                # Page 1: Visual Hook & Objectives
                [
                    {
                        "type": "suggested_image",
                        "title": "Hands-On CPR Training on a Medical Resuscitation Manikin",
                        "content": {
                            "title": "Life-Saving CPR and First Aid Training",
                            "caption": "Trainees practicing high-quality chest compressions on a CPR manikin, mastering the 100–120 compressions-per-minute life-saving cadence.",
                            "resolved_image_url": "https://upload.wikimedia.org/wikipedia/commons/8/81/KM23-_Chuuk_State_Department_of_Education_CPR_Training_%287988095%29.jpg"
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Learning Focus: First Aid and CPR Awareness",
                        "content": {
                            "title": "Learning Focus: First Aid and CPR Awareness",
                            "goals": [
                                "Execute step-by-step first-aid protocols for severe lacerations, thermal/chemical burns, and fractures.",
                                "Apply the critical safety rule for electric shock: isolate power before touching the victim.",
                                "Master the three core steps of Hands-Only CPR: Call Emergency, Position Hands, Compress Hard & Fast.",
                                "Explain how Automated External Defibrillators (AEDs) restore normal heart rhythms in sudden cardiac arrest."
                            ]
                        }
                    }
                ],
                # Page 2: Key Terminology
                [
                    {
                        "type": "definition_card",
                        "title": "First Aid and Resuscitation Vocabulary",
                        "content": {
                            "title": "Life-Saving Terminology",
                            "definitions": [
                                {
                                    "term": "First Aid",
                                    "definition": "Immediate, temporary assistance rendered to a sick or injured person before professional medical personnel arrive, aimed at preserving life, preventing worsening, and promoting recovery.",
                                    "example": "Applying a sterile dressing and pressure bandage to control arterial bleeding."
                                },
                                {
                                    "term": "Cardiopulmonary Resuscitation (CPR)",
                                    "definition": "An emergency lifesaving procedure combining rhythmic chest compressions to maintain artificial blood circulation to the brain and vital organs during cardiac arrest.",
                                    "example": "Hands-Only CPR performed at 100–120 beats per minute to the rhythm of 'Stayin' Alive'."
                                },
                                {
                                    "term": "Automated External Defibrillator (AED)",
                                    "definition": "A portable medical device that automatically analyzes the heart's electrical rhythm and delivers an electric shock (defibrillation) to treat ventricular fibrillation.",
                                    "example": "Wall-mounted AED units located across airport terminals and maintenance hangars."
                                },
                                {
                                    "term": "Cardiac Arrest",
                                    "definition": "The abrupt loss of heart function, breathing, and consciousness caused by an electrical malfunction in the heart.",
                                    "example": "Collapse following high-voltage electric shock from hangar ground equipment."
                                }
                            ]
                        }
                    }
                ],
                # Page 3: Core Explanation (First Aid for Specific Traumas)
                [
                    {
                        "type": "concept_explanation",
                        "title": "First-Aid Protocols for Common Hangar Traumas",
                        "content": {
                            "title": "Immediate Actions for Specific Traumas",
                            "text": "Every aviation student must master four specific trauma responses:\n\n- **1. Severe Bleeding (Lacerations)**: Apply direct, continuous pressure using sterile gauze pads. Elevate the wounded limb above heart level if no fracture is suspected. Never remove blood-soaked pads; add fresh dressings on top and secure firmly.\n- **2. Thermal & Chemical Burns**: Immediately cool thermal burns under cold running water for at least 10–20 minutes. For chemical burns (e.g. battery acid), brush away dry powder then flood with water. Never apply grease, butter, or puncture blisters.\n- **3. Suspected Fractures**: Immobilize the limb in the exact position found using splints or padding. Do not attempt to straighten crooked bones. Check for circulation downstream.\n- **4. Electric Shock**: **RULE NUMBER ONE**: Never touch an electric shock casualty who is still in contact with the live source! You will become a second victim. Shut off the main circuit breaker or push the wire away using a dry wooden pole before providing first aid."
                        }
                    }
                ],
                # Page 4: Technical Diagram Block (First Aid & CPR Flowchart)
                [
                    {
                        "type": "suggested_diagram",
                        "title": "First Aid Emergency Response and Hands-Only CPR Flowchart",
                        "content": {
                            "title": "Emergency First Aid & CPR Decision Algorithm",
                            "caption": "Step-by-step decision flow from scene safety verification, consciousness check, emergency call, to high-cadence chest compressions."
                        }
                    }
                ],
                # Page 5: Comparative Treatment Protocol Table
                [
                    {
                        "type": "comparison_table",
                        "title": "First Aid Treatments Across Traumatic Injury Types",
                        "content": {
                            "title": "First Aid Action Matrix by Injury Type",
                            "headers": ["Injury Type", "Immediate Do's", "Critical Don'ts"],
                            "rows": [
                                ["Severe Laceration", "Apply direct pressure with sterile pads; bandage firmly", "Do not remove embedded objects; do not remove soaked gauze"],
                                ["Thermal Burn", "Flush with cool running water for 10–20 minutes; cover loosely", "Do not apply butter, oil, or ice; do not break skin blisters"],
                                ["Chemical Splash (Eyes/Skin)", "Flush at emergency eyewash for 15+ minutes continuously", "Do not rub eyes; do not apply neutralizing acids/bases"],
                                ["Bone Fracture", "Immobilize with rigid splint and soft padding; support joint", "Do not attempt to push bone back or force limb straight"],
                                ["Electric Shock", "Isolate main power switch first; check breathing; start CPR if needed", "DO NOT touch casualty with bare hands while power is live"]
                            ]
                        }
                    }
                ],
                # Page 6: Real-World Case Study (Hands-Only CPR in Action)
                [
                    {
                        "type": "real_world_example",
                        "title": "Saving a Colleague: The 3 Critical Steps of CPR",
                        "content": {
                            "title": "Hands-Only CPR Saves Lives",
                            "text": "When an adult collapses from sudden cardiac arrest, their brain begins suffering irreversible cell death within 4 to 6 minutes without blood flow. Immediate bystander CPR doubles or triples survival rates.\n\n**The Hands-Only Protocol**:\n1. **Call**: Check responsiveness. If unresponsive with no breathing, shout for help and dial emergency services (999/112). Tell someone: 'Get the AED!'\n2. **Position**: Kneel beside the casualty. Place the heel of one hand in the center of the chest (lower breastbone). Interlock the fingers of your second hand on top. Lock your elbows straight.\n3. **Push Hard & Fast**: Use your upper body weight to compress the chest **5 to 6 cm deep** at a rate of **100 to 120 compressions per minute** (the beat of the song 'Stayin' Alive'). Allow complete chest recoil between compressions. Continue without stopping until paramedics arrive or the AED prompts you."
                        }
                    }
                ],
                # Page 7: Educational Video Integration
                [
                    {
                        "type": "suggested_video",
                        "title": "Hands-Only CPR Demonstration and Practice",
                        "content": {
                            "title": "Mastering High-Quality Chest Compressions",
                            "description": "Watch a certified medical resuscitation demonstration showing exact hand placement, straight-arm posture, compression depth, and cadence.",
                            "url": "https://www.youtube.com/watch?v=M4ACYp75mjU"
                        }
                    }
                ],
                # Page 8: Procedural Analysis (How an AED Operates)
                [
                    {
                        "type": "step_process",
                        "title": "Operating an Automated External Defibrillator (AED)",
                        "content": {
                            "title": "The 4-Step AED Deployment Procedure",
                            "steps": [
                                "1. Power On: Open the lid and press the green power button. The AED will immediately begin speaking audible voice instructions.",
                                "2. Attach Electrode Pads: Peel backing from pads. Stick Pad 1 on the upper right chest (below collarbone); stick Pad 2 on the lower left ribcage.",
                                "3. Clear for Analysis: Plug in connector if required. Ensure NOBODY touches the patient while the device analyzes heart rhythm.",
                                "4. Deliver Shock if Prompted: If the AED advises a shock, loudly shout 'STAND CLEAR!' Ensure everyone is clear, then press the flashing shock button. Immediately resume chest compressions."
                            ]
                        }
                    }
                ],
                # Page 9: Formative Knowledge Check 1
                [
                    {
                        "type": "knowledge_check",
                        "title": "Diagnostic Check: Electrical First Aid",
                        "content": {
                            "question": "A student finds a classmate lying unconscious on a hangar floor with a live 115V AC power cable resting across their leg. What is the very first action the student must take?",
                            "options": [
                                "Immediately grab the classmate's hands and drag them away from the wire.",
                                "Throw a bucket of water over the cable to short-circuit the connection.",
                                "Turn off the main electrical power isolator switch or disconnect the power source before touching the victim.",
                                "Kneel down beside the victim and start chest compressions immediately."
                            ],
                            "answer": "C",
                            "explanation": "Human flesh conducts electricity. Grabbing a victim who is in contact with live current will electrocute the rescuer. You must always isolate the power source first before touching the casualty."
                        }
                    }
                ],
                # Page 10: Formative Knowledge Check 2
                [
                    {
                        "type": "knowledge_check",
                        "title": "Diagnostic Check: CPR Mechanics",
                        "content": {
                            "question": "What is the recommended compression depth and cadence rate for performing adult Hands-Only CPR?",
                            "options": [
                                "1 to 2 cm deep at a rate of 50 compressions per minute",
                                "5 to 6 cm deep at a rate of 100 to 120 compressions per minute",
                                "10 cm deep at a rate of 200 compressions per minute",
                                "Compress only when the patient gasps for breath"
                            ],
                            "answer": "B",
                            "explanation": "Medical resuscitation guidelines mandate adult chest compressions at 5 to 6 cm (approx. 2 inches) depth at a cadence of 100–120 beats per minute to maintain sufficient cerebral perfusion."
                        }
                    }
                ],
                # Page 11: Summary & Core Takeaways
                [
                    {
                        "type": "summary",
                        "title": "Core Takeaways: First Aid and CPR Awareness",
                        "content": {
                            "title": "Summary & Synthesis",
                            "summary_points": [
                                "First aid preserves life, prevents condition deterioration, and promotes recovery until professional medical personnel arrive.",
                                "Electrical currents must be shut off at the main switch before touching shock casualties to prevent secondary electrocution.",
                                "Severe bleeding requires immediate direct pressure; fractures require rigid stabilization in the position found.",
                                "Hands-Only CPR requires hard and fast compressions (5–6 cm deep at 100–120 bpm) in the center of the chest to sustain vital brain circulation."
                            ]
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 1.2.6: Safety Observation and Aviation Careers
        # =====================================================================
        {
            "unit_order": 5,
            "unit_name": "Safety Observation and Aviation Careers",
            "unit_description": "Aviation workplace safety audits, ground turnaround marshalling procedures, and professional aviation safety career pathways.",
            "lesson_title": "Safety Observation and Aviation Careers",
            "pages": [
                # Page 1: Visual Hook & Objectives
                [
                    {
                        "type": "suggested_image",
                        "title": "Aircraft Marshaller Guiding an Aircraft Safely into the Terminal Gate",
                        "content": {
                            "title": "Aviation Ground Safety Operations",
                            "caption": "An airfield ground marshaller using illuminated wand paddles to direct an arriving airliner into the gate, preventing wingtip ramp collisions.",
                            "resolved_image_url": "https://upload.wikimedia.org/wikipedia/commons/1/10/Ground_Crew_Member_Directs_a_RAF_Tristar_Aircraft_MOD_45150114.jpg"
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Learning Focus: Safety Observation and Careers",
                        "content": {
                            "title": "Learning Focus: Safety Observation and Careers",
                            "goals": [
                                "Explain the methodology and purpose of systematic aviation safety audits.",
                                "Trace the mandatory safety turnaround checklist executed by ground handling personnel.",
                                "Identify professional career paths dedicated to aviation safety (Safety Managers, Air Traffic Controllers, Airworthiness Inspectors, Airport Firefighters).",
                                "Relate aviation safety standards to Kenya Civil Aviation Authority (KCAA) and ICAO regulatory frameworks."
                            ]
                        }
                    }
                ],
                # Page 2: Key Terminology
                [
                    {
                        "type": "definition_card",
                        "title": "Safety Observation and Careers Terminology",
                        "content": {
                            "title": "Professional Safety Concepts",
                            "definitions": [
                                {
                                    "term": "Safety Audit",
                                    "definition": "A formal, systematic evaluation of an aviation facility, maintenance shop, or flight operation to verify compliance with safety regulations, quality standards, and procedures.",
                                    "example": "An annual audit of hangar tool calibration records and hazardous chemical storage by civil aviation inspectors."
                                },
                                {
                                    "term": "Ground Handling",
                                    "definition": "The coordinated servicing of an aircraft between landing and its next departure, including marshalling, chocking, baggage loading, fueling, and cabin sanitizing.",
                                    "example": "Ground personnel executing a rapid 45-minute turnaround on an arriving domestic flight."
                                },
                                {
                                    "term": "Aircraft Marshalling",
                                    "definition": "Visual hand-signal communication between ground personnel and cockpit flight crew to guide an aircraft safely along ramps and into parking bays.",
                                    "example": "Using day-glo orange paddles or lighted wands to indicate 'stop', 'turn right', or 'chocks inserted'."
                                },
                                {
                                    "term": "Safety Management System (SMS)",
                                    "definition": "A systematic, data-driven approach to managing aviation safety, encompassing organizational structures, policies, hazard reporting pipelines, and risk mitigation.",
                                    "example": "An airline's digital portal where pilots and engineers log flight turbulence or equipment near-misses."
                                }
                            ]
                        }
                    }
                ],
                # Page 3: Core Explanation (Professional Safety Careers)
                [
                    {
                        "type": "concept_explanation",
                        "title": "The Guardians of the Sky: Aviation Safety Careers",
                        "content": {
                            "title": "Career Pathways in Aviation Safety",
                            "text": "Behind every commercial takeoff is an army of dedicated safety professionals whose primary mission is preventing harm:\n\n- **Airport Safety Manager**: Designs and oversees the airport's Safety Management System (SMS), conducts ramp hazard audits, manages wildlife hazard mitigation (bird-strike prevention), and ensures emergency readiness.\n- **Air Traffic Controller (ATC)**: Manages radar, satellite feeds, and radio frequencies to maintain strict horizontal and vertical separation between aircraft in flight and prevent runway incursions.\n- **Aviation Safety Inspector (Regulator)**: Government officials (e.g. KCAA in Kenya, FAA in the USA) who inspect flight schools, airline maintenance hangars, and pilot logs to enforce international ICAO airworthiness standards.\n- **Airport Firefighter & Rescue Specialist**: Highly trained emergency teams equipped with specialized Aircraft Rescue and Firefighting (ARFF) vehicles capable of reaching any point on the airfield within three minutes."
                        }
                    }
                ],
                # Page 4: Technical Diagram Block
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Aviation Safety Career Ecosystem and Turnaround Safety Protocol",
                        "content": {
                            "title": "Safety Careers & Aircraft Turnaround Cycle",
                            "caption": "Interlocking roles of Safety Managers, ATCs, Ground Marshallers, and Inspectors across the 4-stage arrival-to-departure safety protocol."
                        }
                    }
                ],
                # Page 5: Comparative Career Profile Matrix
                [
                    {
                        "type": "comparison_table",
                        "title": "Profiles of Dedicated Aviation Safety Professions",
                        "content": {
                            "title": "Aviation Safety Career Pathways",
                            "headers": ["Career Role", "Primary Workplace", "Core Safety Responsibility", "Key Training / Licensing"],
                            "rows": [
                                ["Airport Safety Manager", "Airport administration & ramp", "Oversees SMS, audits facility compliance, investigates ramp incidents", "Aviation safety management degree, ICAO SMS certification"],
                                ["Air Traffic Controller", "Control tower & radar center", "Separates aircraft in controlled airspace and active runways", "ATC radar & tower licensing, high spatial awareness qualification"],
                                ["Airworthiness Inspector", "Civil Aviation Authority (KCAA)", "Certifies aircraft airframes, audits maintenance repair organizations", "Licensed Aircraft Maintenance Engineer (LAME) with type ratings"],
                                ["Aircraft Marshaller", "Airport ramp / apron bays", "Guides aircraft with visual wand signals, inserts tire chocks", "Ramp safety certification, airside vehicle driving permit"],
                                ["Airport Firefighter", "Airside fire crash station", "Responds to aircraft fuel fires, executes emergency evacuations", "Specialized ARFF structural and aircraft rescue firefighting certification"]
                            ]
                        }
                    }
                ],
                # Page 6: Real-World Case Study (The Ground Handling Turnaround)
                [
                    {
                        "type": "real_world_example",
                        "title": "Executing a Flawless Turnaround at Jomo Kenyatta International Airport",
                        "content": {
                            "title": "The Four Golden Steps of Ramp Arrival",
                            "text": "When an international flight touches down at JKIA, the ground operations team executes a precision safety sequence:\n\n1. **Pre-Arrival FOD Sweep**: The ramp marshal inspects the parking bay surface, ensuring zero stray bolts or plastic cups are present.\n2. **Marshalling to Gate**: The marshaller guides the captain using crossed wands to signal 'STOP' at the exact nose-wheel parking line.\n3. **Tire Chocking**: Heavy rubber chocks are placed immediately against the nose and main landing gear tires to prevent accidental rolling.\n4. **Static Grounding**: A copper bonding cable is clamped from the aircraft fuselage to the earth terminal before fuel hoses or baggage belts are attached, preventing static sparks."
                        }
                    }
                ],
                # Page 7: Educational Video Integration
                [
                    {
                        "type": "suggested_video",
                        "title": "Aviation Ground Handling, Marshalling, and Turnaround Safety",
                        "content": {
                            "title": "Ramp Operations and Aircraft Turnaround Safety",
                            "description": "Witness high-speed, coordinated ground turnaround operations showing aircraft marshalling, fuel grounding, baggage belt loading, and apron safety checks.",
                            "url": "https://www.youtube.com/watch?v=2f3qE6_79hE"
                        }
                    }
                ],
                # Page 8: Procedural Analysis (Conducting a Safety Audit)
                [
                    {
                        "type": "step_process",
                        "title": "How Aviation Safety Inspectors Conduct a Hangar Audit",
                        "content": {
                            "title": "The 4 Phases of an Aviation Safety Audit",
                            "steps": [
                                "1. Pre-Audit Review: Review aircraft maintenance logs, previous defect entries, technician training records, and tool calibration certificates.",
                                "2. Physical Walkthrough: Inspect hangar walkways, eyewash stations, fire extinguisher pressure gauges, and chemical storage lockers.",
                                "3. Direct Observation: Observe a live maintenance task (such as a landing gear inspection) to verify technicians follow approved technical manuals.",
                                "4. Debrief & Corrective Action: Present findings to the engineering director; issue formal Corrective Action Requests (CAR) for any identified non-compliance."
                            ]
                        }
                    }
                ],
                # Page 9: Formative Knowledge Check 1
                [
                    {
                        "type": "knowledge_check",
                        "title": "Diagnostic Check: Safety Management Roles",
                        "content": {
                            "question": "Which aviation professional is specifically responsible for conducting facility safety audits, tracking hazard reports, and monitoring compliance with airport safety management policies?",
                            "options": [
                                "Air Traffic Controller (ATC)",
                                "Airport Safety Manager",
                                "Commercial Airline Pilot",
                                "Baggage Cargo Loader"
                            ],
                            "answer": "B",
                            "explanation": "The Airport Safety Manager is the certified specialist responsible for administering the Safety Management System (SMS), performing regular workplace audits, and managing hazard mitigations."
                        }
                    }
                ],
                # Page 10: Formative Knowledge Check 2
                [
                    {
                        "type": "knowledge_check",
                        "title": "Diagnostic Check: The Purpose of Audits",
                        "content": {
                            "question": "What is the primary objective of performing regular safety audits in an aircraft maintenance facility?",
                            "options": [
                                "To calculate the total financial cost of spare parts used during the quarter",
                                "To systematically verify that all procedures, equipment, and work areas comply with safety regulations, identifying hazards before they cause an accident",
                                "To test pilot navigation capabilities in flight simulator bays",
                                "To clean the hangar concrete floor at the conclusion of a work shift"
                            ],
                            "answer": "B",
                            "explanation": "A safety audit is a proactive, formal inspection designed to identify systemic deficiencies, ensure procedural compliance, and eliminate hazards before they can result in human injury or aircraft accidents."
                        }
                    }
                ],
                # Page 11: Summary & Core Takeaways
                [
                    {
                        "type": "summary",
                        "title": "Core Takeaways: Safety Observation and Aviation Careers",
                        "content": {
                            "title": "Summary & Synthesis",
                            "summary_points": [
                                "Aviation safety is maintained through structured audits, real-time observation, and comprehensive Safety Management Systems (SMS).",
                                "Ground handling requires strict procedural execution: FOD sweeps, precise marshalling, tire chocking, and electrical grounding.",
                                "Aviation safety offers diverse, highly respected career pathways including Safety Managers, ATCs, Airworthiness Inspectors, and Firefighters.",
                                "Adopting an active safety-first mindset is the foundational qualification for every aspiring aviation professional."
                            ]
                        }
                    }
                ]
            ]
        }
    ]

def ingest_grade10_aviation_topic2(replace=False):
    """Ingests Grade 10 Aviation Topic 2 into the database."""
    print("=" * 80)
    print("VLEARN INGESTION ENGINE: Grade 10 Aviation — Topic 2")
    print("Safety in Aviation")
    print("=" * 80)

    curriculum = Curriculum.objects.get(id=5)
    grade = Grade.objects.get(id=5, level=10)
    subject = Subject.objects.get(id=44, grade=grade)

    print(f"[*] Curriculum: {curriculum.name} (ID: {curriculum.id})")
    print(f"[*] Grade:      {grade.name} (ID: {grade.id}, Level: {grade.level})")
    print(f"[*] Subject:    {subject.name} (ID: {subject.id})")

    topic, created = Topic.objects.get_or_create(
        subject=subject,
        order=1,
        defaults={"name": "Safety in Aviation"}
    )
    if not created:
        topic.name = "Safety in Aviation"
        topic.save()
    print(f"[*] Topic:      {topic.name} (ID: {topic.id})")

    curriculum_data = build_topic2_curriculum()
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
    print("[SUCCESS] Grade 10 Aviation Topic 2 Ingestion Complete!")
    print(f"[*] Total Lessons Ingested: {total_lessons}")
    print(f"[*] Total Pages/Cards:      {total_pages}")
    print(f"[*] Total Blocks Created:   {total_blocks}")
    print("=" * 80)

if __name__ == "__main__":
    replace_flag = "--replace" in sys.argv
    ingest_grade10_aviation_topic2(replace=replace_flag)
