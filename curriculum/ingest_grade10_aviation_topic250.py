"""
VLearn Grade 10 Aviation — Topic 250: Flight Operations: Aviation Weather
Production Ingestion Engine

Curriculum: CBC (Curriculum ID: 5)
Grade: Grade 10 (Grade ID: 5, Level: 10)
Subject: Aviation (Subject ID: 44)
Topic: Flight Operations: Aviation Weather (Topic ID: 250, Order: 3)

Ingests 5 Comprehensive Learning Units & Lessons (50 Concept Cards):
  1. Elements of Weather in the Atmosphere (Unit Order 0, 10 Cards)
  2. Structure of the Lower Atmosphere: Troposphere and Stratosphere (Unit Order 1, 10 Cards)
  3. Clouds in Flight Operations: Low, Middle, and High Altitude (Unit Order 2, 10 Cards)
  4. Aviation Weather Measurements and Instruments (Unit Order 3, 10 Cards)
  5. Effects of Weather on Flight Operations and Planning Roles (Unit Order 4, 10 Cards)

Usage:
  ./venv/bin/python curriculum/ingest_grade10_aviation_topic250.py [--replace]
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
    Subject, Topic, LearningUnit, Lesson, LessonBlock
)

def clean_text(text: str) -> str:
    """Removes bracket citations [21, 93], internal prompt markers, and normalizes typography."""
    if not text:
        return ""
    # Remove bracket citations like [21], [93], [21, 93]
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

def build_topic250_curriculum():
    """Returns the pedagogical page and block structure for Grade 10 Aviation Topic 250."""
    return [
        # =====================================================================
        # LESSON 1: Elements of Weather in the Atmosphere (Unit Order 0)
        # =====================================================================
        {
            "unit_order": 0,
            "unit_name": "Elements of Weather in the Atmosphere",
            "unit_description": "Explore the physical forces of atmospheric weather—wind, temperature, pressure, humidity, precipitation, and visibility—and their governing influence on aircraft lift, thrust, and directional control.",
            "lesson_title": "Elements of Weather in the Atmosphere",
            "pages": [
                # Card 1: Visual Hook & Learning Objectives
                [
                    {
                        "type": "suggested_image",
                        "title": "Dash 8 Q300 Turboprop Performing a Crosswind Landing",
                        "content": {
                            "title": "Dash 8 Q300 Turboprop Performing a Crosswind Landing",
                            "caption": "A commercial turboprop aircraft executing a crab-angle approach in gusty crosswinds, demonstrating the critical influence of atmospheric wind vectors on runway alignment and flight control.",
                            "resolved_image_url": "https://upload.wikimedia.org/wikipedia/commons/b/b1/Air_Nelson_Q300_crosswind_landing_at_Tauranga_Airport.jpg"
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Learning Focus: Elements of Aviation Weather",
                        "content": {
                            "title": "Learning Focus: Elements of Aviation Weather",
                            "goals": [
                                "Identify the six primary elements of aviation weather: wind, temperature, atmospheric pressure, humidity, precipitation, and visibility.",
                                "Distinguish between headwinds, tailwinds, and crosswinds and explain their operational impact on takeoff and landing.",
                                "Explain how ambient temperature alters air density, wing lift, and engine thrust output.",
                                "Analyze why high humidity diminishes aircraft performance compared to dry air conditions."
                            ]
                        }
                    }
                ],
                # Card 2: Core Technical Vocabulary
                [
                    {
                        "type": "definition_card",
                        "title": "Core Aviation Weather Terminology",
                        "content": {
                            "title": "Essential Atmospheric Vocabulary",
                            "definitions": [
                                {
                                    "term": "Aviation Weather",
                                    "definition": "The precise physical state of the atmosphere at a given time and place, concerning parameters that directly dictate aircraft performance, stability, and flight safety.",
                                    "example": "An airport weather briefing reporting wind 060 degrees at 12 knots and temperature 24 degrees Celsius."
                                },
                                {
                                    "term": "Wind",
                                    "definition": "The horizontal movement of air across the Earth's surface, measured in knots (nautical miles per hour) and named by the direction from which it originates.",
                                    "example": "A surface wind reported as 270/15KT blows from the west at 15 knots."
                                },
                                {
                                    "term": "Atmospheric Pressure",
                                    "definition": "The downward gravitational force exerted on a unit surface area by the weight of the air column extending above it.",
                                    "example": "Standard sea-level pressure of 1013.25 hectopascals (hPa) or 29.92 inches of mercury (inHg)."
                                },
                                {
                                    "term": "Air Density",
                                    "definition": "The mass of air molecules packed per unit volume of space, heavily influenced by temperature, pressure, and moisture content.",
                                    "example": "Dense cold winter air providing maximum lift versus thin warm summer air."
                                },
                                {
                                    "term": "Relative Humidity",
                                    "definition": "The percentage ratio of the actual amount of water vapor in the air compared to the maximum amount the air can hold at that temperature.",
                                    "example": "A humid tropical afternoon with 90% humidity reducing engine combustion efficiency."
                                },
                                {
                                    "term": "Visibility",
                                    "definition": "The greatest horizontal distance at which prominent unlighted objects by day and illuminated objects by night can be clearly seen and identified.",
                                    "example": "Runway visibility dropping below 800 meters during heavy rainfall or dense morning fog."
                                }
                            ]
                        }
                    }
                ],
                # Card 3: Wind Vectors and Runway Operations
                [
                    {
                        "type": "concept_explanation",
                        "title": "Wind Vectors: Headwinds, Tailwinds, and Crosswinds",
                        "content": {
                            "title": "How Wind Directs Aerodynamic Performance",
                            "text": "Because airplanes fly by pushing relative airflow over their aerodynamic surfaces, wind speed and orientation directly determine takeoff and landing safety:\n\n- **Headwind (Frontal Wind):** Wind blowing directly against the nose of the aircraft. A headwind increases airflow over the wings without requiring higher ground speed. This provides free lift, allowing the aircraft to take off at a lower ground speed and shorten both the takeoff roll and landing roll significantly.\n- **Tailwind (Rear Wind):** Wind blowing directly from behind the aircraft. While a tailwind provides a beneficial push during high-altitude cruising flight (saving fuel and reducing flight time), it is hazardous during landing. A tailwind increases the aircraft's ground speed upon touchdown, requiring a dramatically longer runway distance to brake to a halt.\n- **Crosswind (Lateral Wind):** Wind blowing across the runway centerline from the side. A crosswind exerts aerodynamic drift, attempting to push the aircraft sideways off the runway. Pilots must apply specialized crabbed or wing-low sideslip flight control techniques to keep the wheels aligned with the runway centerline."
                        }
                    }
                ],
                # Card 4: Technical Diagram (SVG 1)
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Weather Elements & Aerodynamic Density Dynamics",
                        "content": {
                            "title": "Weather Elements & Aerodynamic Density Dynamics",
                            "caption": "Comparative analysis of atmospheric air density and wind vectors relative to aircraft performance."
                        }
                    }
                ],
                # Card 5: Temperature, Pressure, and Humidity Dynamics
                [
                    {
                        "type": "concept_explanation",
                        "title": "Thermodynamics of Flight: Temperature, Pressure, and Moisture",
                        "content": {
                            "title": "Air Molecule Packing and Engine Thrust",
                            "text": "To an aircraft wing and jet engine, ambient atmospheric conditions dictate the physical concentration of gas molecules:\n\n- **Cold Air (High Density):** In cold air, molecules move slowly and pack tightly together. Dense air provides an abundance of air molecules for wings to deflect downwards (generating robust lift) and for propellers and jet turbines to ingest (generating strong thrust). Takeoff distances are at their shortest.\n- **Hot Air (Low Density):** Heating causes gas molecules to vibrate rapidly and expand outward. Hot air is thin air with fewer molecules per cubic meter. Wings generate less lift, and engines ingest less oxygen for combustion, resulting in degraded climb rates and longer runway requirements.\n- **Atmospheric Pressure:** In high-pressure weather systems, descending dense air enhances engine and aerodynamic performance. In low-pressure systems, rising thin air degrades takeoff and climb capability.\n- **Humidity Effects:** Counterintuitively, humid air is less dense than dry air. A water molecule (H2O, molecular mass ~18) is lighter than a diatomic nitrogen molecule (N2, mass 28) or oxygen molecule (O2, mass 32). When water vapor replaces dry air gases, overall density drops, marginally reducing engine thrust and wing lift."
                        }
                    }
                ],
                # Card 6: Operational Scenario: High Density Altitude
                [
                    {
                        "type": "scenario_card",
                        "title": "High Density Altitude Operations at Wilson Airport",
                        "content": {
                            "title": "Real-World Operational Scenario: Nairobi Afternoon Departure",
                            "scenario": "A charter pilot is planning a Cessna Grand Caravan flight carrying tourists and luggage from Wilson Airport (altitude 5,536 feet above sea level) to the Maasai Mara. At 2:00 PM, the airfield thermometer reaches 32°C.",
                            "hazard": "The combination of high airfield geographic elevation and high ambient temperature causes the air density to plummet, creating a density altitude of nearly 8,500 feet. The aircraft performs as if it were operating from an airport thousands of feet higher.",
                            "flight_risk": "Attempting to take off at maximum certified gross weight would result in sluggish acceleration and an excessively long takeoff roll, risking runway overrun or failing to clear obstacle trees off the runway end.",
                            "correct_action": "The pilot and flight dispatcher recalculate the aircraft takeoff performance chart, offload non-essential baggage or defer fuel upload to reduce gross weight, and schedule departure when ambient temperatures cool down."
                        }
                    }
                ],
                # Card 7: Curated Instructional Video
                [
                    {
                        "type": "suggested_video",
                        "title": "Atmosphere & Temperature in Aviation Meteorology",
                        "content": {
                            "title": "Atmosphere & Temperature in Aviation Meteorology",
                            "url": "https://www.youtube.com/watch?v=G5rCZSQo44A",
                            "description": "Expert flight instructor explains atmospheric physics, air density effects on aircraft performance, and how temperature variations dictate takeoff performance."
                        }
                    }
                ],
                # Card 8: Formative MCQ 1
                [
                    {
                        "type": "knowledge_check",
                        "title": "Formative Assessment: Takeoff Wind Vectors",
                        "content": {
                            "title": "Takeoff Wind Vector Dynamics",
                            "question": "Why is a headwind highly desirable for an aircraft during takeoff and landing?",
                            "options": [
                                "It blows exhaust fumes away from the cockpit windows, improving pilot visibility.",
                                "It increases airflow over the wings to generate extra lift at a lower ground speed, reducing the runway distance required.",
                                "It pushes the aircraft from behind, helping it accelerate faster down the runway.",
                                "It cools down the tires of the landing gear to prevent them from bursting on touchdown."
                            ],
                            "answer": "B",
                            "explanation": "Lift is generated by airspeed (the velocity of air moving across the wings), not ground speed. A headwind provides free airspeed over the aerofoil, enabling the aircraft to achieve liftoff at a significantly lower rolling speed on the ground, which preserves runway space and improves safety margins."
                        }
                    }
                ],
                # Card 9: Formative MCQ 2
                [
                    {
                        "type": "knowledge_check",
                        "title": "Formative Assessment: High Temperature Impact",
                        "content": {
                            "title": "Ambient Temperature and Aerodynamic Performance",
                            "question": "How does a high air temperature affect aircraft performance during takeoff?",
                            "options": [
                                "It increases air density, which helps the wings generate more lift and shortens takeoff roll.",
                                "It has no effect on takeoff roll, but it causes the engine oil to overheat.",
                                "It decreases air density, making the air thin, which reduces wing lift and engine power, thereby requiring a longer takeoff runway.",
                                "It increases engine thrust by allowing fuel to burn faster in hot conditions."
                            ],
                            "answer": "C",
                            "explanation": "Heating air causes gas molecules to expand and disperse, reducing the air density. Because the engine ingests fewer oxygen molecules and the wing deflects fewer air molecules per second, both engine thrust and aerodynamic lift drop substantially, requiring a significantly longer ground roll to attain flight."
                        }
                    }
                ],
                # Card 10: Practical Investigation & Summary
                [
                    {
                        "type": "concept_explanation",
                        "title": "Practical Density Modeling & Lesson Summary",
                        "content": {
                            "title": "Classroom Experiment and Key Takeaways",
                            "text": "### Laboratory Demonstration: Fluid Density Stratification\nTo visualize how temperature changes fluid density, fill a transparent cylinder halfway with cold saltwater colored blue, then gently pour warm freshwater colored red across a spoon onto the top surface. The warm, less dense fluid floats securely above the denser, cold layer. In the atmosphere, warm air pockets similarly rise while cold dense air sinks, generating vertical thermal currents.\n\n### Key Takeaways:\n- **Six Elements:** Wind, temperature, pressure, humidity, precipitation, and visibility govern flight physics.\n- **Takeoff Operations:** Always prioritize takeoff into a headwind to maximize lift and shorten ground distance.\n- **Density Altitude:** High temperatures and high elevation drastically reduce aircraft lift and engine thrust output."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 2: Structure of the Lower Atmosphere: Troposphere and Stratosphere (Unit Order 1)
        # =====================================================================
        {
            "unit_order": 1,
            "unit_name": "Structure of the Lower Atmosphere: Troposphere and Stratosphere",
            "unit_description": "Examine the gaseous composition and layered structure of the lower atmosphere up to 50 km, contrasting the active weather processes of the troposphere with the calm, stable cruising realm of the stratosphere.",
            "lesson_title": "Structure of the Lower Atmosphere: Troposphere and Stratosphere",
            "pages": [
                # Card 1: Visual Hook & Learning Objectives
                [
                    {
                        "type": "suggested_image",
                        "title": "Stratosphere and Troposphere Layers Viewed from Orbit",
                        "content": {
                            "title": "Stratosphere and Troposphere Layers Viewed from Orbit",
                            "caption": "The distinct illuminated stratifications of the Earth's lower atmosphere captured from the International Space Station, showing the dense, cloud-filled troposphere beneath the clear, stable stratosphere.",
                            "resolved_image_url": "https://upload.wikimedia.org/wikipedia/commons/5/53/Fiery_South_Atlantic_Sunset.jpg"
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Learning Focus: Atmospheric Strata in Aviation",
                        "content": {
                            "title": "Learning Focus: Atmospheric Strata in Aviation",
                            "goals": [
                                "State the primary chemical composition of the Earth's dry atmosphere (78% Nitrogen, 21% Oxygen, 1% Trace Gases).",
                                "Describe the structure of the Troposphere and define the standard environmental lapse rate of 2°C per 1,000 feet.",
                                "Identify the Tropopause as the isothermal boundary layer marking the ceiling of conventional weather.",
                                "Analyze why commercial jet airliners cruise in the lower Stratosphere to maximize fuel efficiency and avoid convective turbulence."
                            ]
                        }
                    }
                ],
                # Card 2: Core Technical Vocabulary
                [
                    {
                        "type": "definition_card",
                        "title": "Atmospheric Strata Terminology",
                        "content": {
                            "title": "Technical Vocabulary of Atmospheric Physics",
                            "definitions": [
                                {
                                    "term": "Atmosphere",
                                    "definition": "The multi-layered blanket of gases enveloping the Earth, retained by gravitational attraction and essential for life and flight.",
                                    "example": "A continuous fluid medium extending outward over 500 kilometers above the surface."
                                },
                                {
                                    "term": "Troposphere",
                                    "definition": "The lowest layer of the atmosphere extending from the surface to roughly 11 km (36,000 ft), containing nearly all atmospheric water vapor and weather phenomena.",
                                    "example": "All clouds, convective rain showers, and thermal turbulence occur within this floor."
                                },
                                {
                                    "term": "Standard Lapse Rate",
                                    "definition": "The standard rate at which air temperature drops with increasing altitude in the troposphere, standardly defined as 2°C (1.98°C) per 1,000 feet.",
                                    "example": "At 10,000 feet above sea level, air is approximately 20°C colder than at the surface."
                                },
                                {
                                    "term": "Tropopause",
                                    "definition": "The isothermal boundary zone separating the troposphere from the stratosphere, where temperature ceases to decline and stabilizes at approximately -56.5°C.",
                                    "example": "The anvil top of a severe thunderstorm flattening out as it strikes the tropopause ceiling."
                                },
                                {
                                    "term": "Stratosphere",
                                    "definition": "The atmospheric layer extending from the tropopause to approximately 50 km, characterized by extreme horizontal stability and an inverted temperature profile.",
                                    "example": "Commercial passenger jets cruising smoothly at 39,000 feet above weather clouds."
                                },
                                {
                                    "term": "Ozone Layer",
                                    "definition": "A region within the stratosphere with a high concentration of triatomic oxygen (O3), absorbing energetic solar ultraviolet radiation and warming the upper stratosphere.",
                                    "example": "Solar UV absorption converting radiation into thermal energy between 20 km and 35 km altitude."
                                }
                            ]
                        }
                    }
                ],
                # Card 3: Atmospheric Composition & Tropospheric Structure
                [
                    {
                        "type": "concept_explanation",
                        "title": "Atmospheric Composition & The Troposphere",
                        "content": {
                            "title": "The Gaseous Blend and the Weather Floor",
                            "text": "Before analyzing atmospheric altitude layers, aviators must understand the fluid composition of dry air at sea level:\n\n- **Nitrogen (N2):** Makes up approximately **78%** of atmospheric volume, acting as an inert carrier gas.\n- **Oxygen (O2):** Accounts for approximately **21%**, essential for human respiration and turbine engine combustion.\n- **Trace Gases:** The remaining **1%** is comprised of argon (0.93%), carbon dioxide (0.04%), water vapor, neon, and methane.\n\n### The Troposphere (Surface to ~11 km)\nThe troposphere is the 'weather factory' of planet Earth:\n- **Depth:** Extends from sea level to approximately 11 km (roughly 36,000 ft) on average, reaching up to 18 km near the equator and thinning to 8 km over the polar regions.\n- **Moisture Storage:** Houses approximately 75% of the total atmospheric mass and over 99% of all atmospheric water vapor.\n- **Temperature Lapse:** As an aircraft climbs, ambient temperature drops rapidly at the International Standard Atmosphere (ISA) rate of **2°C per 1,000 feet** (6.5°C per kilometer)."
                        }
                    }
                ],
                # Card 4: Technical Diagram (SVG 2)
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Lower Atmosphere Thermal Profile & Altitude Zones",
                        "content": {
                            "title": "Lower Atmosphere Thermal Profile & Altitude Zones",
                            "caption": "Vertical atmospheric profile showing altitude, temperature lapse rates, and commercial jet cruise altitudes up to 50 km."
                        }
                    }
                ],
                # Card 5: The Stratosphere: The High-Altitude Cruising Floor
                [
                    {
                        "type": "concept_explanation",
                        "title": "The Stratosphere: Why Commercial Jets Cruise High",
                        "content": {
                            "title": "Stability, Temperature Inversion, and Fuel Efficiency",
                            "text": "Positioned immediately above the tropopause boundary, the **Stratosphere** spans from roughly 11 km up to 50 km:\n\n- **Absence of Weather:** The stratosphere is virtually devoid of water vapor. Convective vertical clouds and rainstorms cannot form, creating a glassy, turbulence-free flying environment with pristine visibility.\n- **Temperature Inversion:** In stark contrast to the troposphere, temperature in the stratosphere remains steady initially and then *increases* with altitude, rising from -56°C up to near 0°C at the stratopause. This warming is driven by the **Ozone Layer** (O3), which absorbs solar ultraviolet rays.\n- **Inversion Stability:** Warmer air lying over colder air prevents vertical convection. Air currents are almost purely laminar and horizontal, completely eliminating thunderstorm updrafts.\n- **Jet Fuel Efficiency:** The thin air of the lower stratosphere creates much lower parasite aerodynamic drag against the aircraft fuselage and wings. Jet engines operating at high true airspeeds achieve their maximum fuel efficiency in this zone."
                        }
                    }
                ],
                # Card 6: Operational Flight Scenario: Climbing to Cruise Level
                [
                    {
                        "type": "scenario_card",
                        "title": "Climbing to Flight Level 390 on Nairobi to London Route",
                        "content": {
                            "title": "Operational Flight Profile: Boeing 787 Long-Haul Climb",
                            "scenario": "A Kenya Airways Boeing 787 Dreamliner departs Jomo Kenyatta International Airport (JKIA) bound for London Heathrow, climbing progressively through atmospheric layers.",
                            "hazard": "During the initial climb through the troposphere (surface to 28,000 feet), the aircraft encounters bumpy thermal updrafts, rain cloud decks, and structural airframe icing risks.",
                            "flight_risk": "Prolonged operation in the active troposphere subjects passengers to turbulence, increases fuel burn due to aerodynamic drag, and requires active anti-icing systems.",
                            "correct_action": "The pilots maintain continuous climb thrust, punching through the tropopause at approximately 36,000 feet (where outside air temperature stabilizes at -56°C), and level off at Flight Level 390 (39,000 feet) in the smooth lower stratosphere for high-speed, fuel-efficient cruise."
                        }
                    }
                ],
                # Card 7: Curated Instructional Video
                [
                    {
                        "type": "suggested_video",
                        "title": "PPGS Lesson 11.1 | Weather: Atmospheric Layers",
                        "content": {
                            "title": "PPGS Lesson 11.1 | Weather: Atmospheric Layers",
                            "url": "https://www.youtube.com/watch?v=Id1AGMA0o_c",
                            "description": "Private Pilot Ground School lecture explaining atmospheric composition, vertical temperature profiles, and operational altitude planning for pilots."
                        }
                    }
                ],
                # Card 8: Formative MCQ 1
                [
                    {
                        "type": "knowledge_check",
                        "title": "Formative Assessment: Tropospheric Lapse Rate",
                        "content": {
                            "title": "Standard Environmental Lapse Rate",
                            "question": "What is the standard lapse rate in the troposphere?",
                            "options": [
                                "Temperature increases by 2°C for every 1,000 feet of altitude climbed.",
                                "Temperature remains constant at -56°C regardless of height.",
                                "Temperature decreases by 2°C for every 1,000 feet of altitude climbed.",
                                "Temperature drops by 10°C for every kilometer climbed."
                            ],
                            "answer": "C",
                            "explanation": "In standard aviation meteorology (ISA), air temperature in the troposphere decreases at an average rate of 2°C (precisely 1.98°C) for every 1,000 feet increase in altitude, until reaching the tropopause boundary."
                        }
                    }
                ],
                # Card 9: Formative MCQ 2
                [
                    {
                        "type": "knowledge_check",
                        "title": "Formative Assessment: Stratospheric Jet Operations",
                        "content": {
                            "title": "Stratospheric Flight Optimization",
                            "question": "Why do long-distance commercial passenger jets prefer to cruise in the lower stratosphere?",
                            "options": [
                                "Because the stratosphere contains the highest oxygen levels, helping the engines burn fuel better.",
                                "Because it is free from clouds, weather, and convective turbulence, allowing for a smooth flight and maximum fuel efficiency in thin air.",
                                "Because gravity is weaker in the stratosphere, making the airplane lighter.",
                                "Because pilots can visually navigate by looking at the stars in this layer."
                            ],
                            "answer": "B",
                            "explanation": "The lower stratosphere is devoid of water vapor and vertical convective updrafts, ensuring smooth, non-turbulent passenger flight. Furthermore, the significantly reduced air density lowers aerodynamic parasite drag, enabling jet airliners to cruise at high true airspeeds while burning far less fuel."
                        }
                    }
                ],
                # Card 10: High-Altitude Physiology & Summary
                [
                    {
                        "type": "concept_explanation",
                        "title": "High-Altitude Human Physiology & Summary",
                        "content": {
                            "title": "Cabin Pressurization & Chapter Summary",
                            "text": "### Human Survival at Stratospheric Altitudes\nAlthough the percentage of oxygen remains 21% throughout the lower atmosphere, atmospheric pressure at 39,000 feet is less than one-fourth of sea-level pressure. The partial pressure of oxygen is too low to force oxygen molecules across human lung membranes into the blood. Commercial airliners must therefore utilize engine bleed air systems to pressurize the cabin to an equivalent altitude of 6,000 to 8,000 feet.\n\n### Summary Checklist:\n- **Gaseous Blend:** 78% Nitrogen, 21% Oxygen, 1% trace elements.\n- **Troposphere:** Where all weather lives; cools at 2°C per 1,000 ft.\n- **Tropopause:** The isothermal dividing ceiling at approximately 36,000 ft.\n- **Stratosphere:** Smooth, dry, inverted temperature profile; optimal jet cruise realm."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 3: Clouds in Flight Operations: Low, Middle, and High Altitude (Unit Order 2)
        # =====================================================================
        {
            "unit_order": 2,
            "unit_name": "Clouds in Flight Operations: Low, Middle, and High Altitude",
            "unit_description": "Classify clouds by altitude family into low, middle, high, and vertical development categories, analyzing their formation physics, flight hazards (icing, turbulence, visibility), and safety margins.",
            "lesson_title": "Clouds in Flight Operations: Low, Middle, and High Altitude",
            "pages": [
                # Card 1: Visual Hook & Learning Objectives
                [
                    {
                        "type": "suggested_image",
                        "title": "Massive Cumulonimbus Thunderstorm Cloud with Anvil Top",
                        "content": {
                            "title": "Massive Cumulonimbus Thunderstorm Cloud with Anvil Top",
                            "caption": "A fully developed cumulonimbus incus storm cloud towering through the troposphere, exhibiting the iconic flattened anvil dome produced by violent vertical thermal updrafts.",
                            "resolved_image_url": "https://upload.wikimedia.org/wikipedia/commons/d/d7/Anvil_of_a_Thunderstorm_Cloud.jpg"
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Learning Focus: Clouds and Aviation Safety",
                        "content": {
                            "title": "Learning Focus: Clouds and Aviation Safety",
                            "goals": [
                                "Classify clouds into four families based on altitude: High, Middle, Low, and Clouds with Extensive Vertical Development.",
                                "Identify the physical structure and flight hazards of Cirrus, Stratus, and Cumulus clouds.",
                                "Examine the formation and dangerous phenomena inside Cumulonimbus (CB) thunderstorm cells.",
                                "Apply standard aviation safety separation rules when navigating near severe convective storm clouds."
                            ]
                        }
                    }
                ],
                # Card 2: Core Technical Vocabulary
                [
                    {
                        "type": "definition_card",
                        "title": "Cloud Classification Vocabulary",
                        "content": {
                            "title": "Essential Cloud and Moisture Terminology",
                            "definitions": [
                                {
                                    "term": "Cloud Base",
                                    "definition": "The lowest altitude of the visible portion of a cloud above ground level, where water vapor condenses into liquid droplets.",
                                    "example": "A cloud base reported at 2,500 feet above airport elevation."
                                },
                                {
                                    "term": "Ceiling",
                                    "definition": "The height above the ground of the lowest layer of clouds that covers more than half the sky (reported as broken or overcast).",
                                    "example": "A low ceiling of 500 feet requiring pilots to execute an instrument approach."
                                },
                                {
                                    "term": "Cirrus (Ci)",
                                    "definition": "Detached, thin, wispy high-level clouds composed entirely of ice crystals, indicating high-altitude winds and advancing frontal systems.",
                                    "example": "Feathery white streaks stretching across the sky at 28,000 feet."
                                },
                                {
                                    "term": "Stratus (St)",
                                    "definition": "A low-altitude, uniform, featureless grey sheet covering the sky like a fog bank elevated above the ground.",
                                    "example": "Low stratus decks creating drizzly weather and low surface visibility."
                                },
                                {
                                    "term": "Cumulus (Cu)",
                                    "definition": "Individual, puffy white clouds with flat horizontal bases and distinct cotton-like domes, formed by rising convective thermal air currents.",
                                    "example": "Fair-weather cumulus clouds causing mild afternoon turbulence beneath their bases."
                                },
                                {
                                    "term": "Cumulonimbus (Cb)",
                                    "definition": "A massive, towering vertical storm cloud with an anvil-shaped crown, capable of producing severe turbulence, lightning, hail, and microbursts.",
                                    "example": "A storm cell rising from 2,000 feet to over 45,000 feet that pilots must detour around."
                                }
                            ]
                        }
                    }
                ],
                # Card 3: The Three Cloud Altitude Families
                [
                    {
                        "type": "concept_explanation",
                        "title": "Cloud Families: High, Middle, and Low Altitude",
                        "content": {
                            "title": "Stratifying Clouds by Operational Altitude",
                            "text": "Meteorologists classify clouds into distinct altitude tiers, which informs pilots of the physical state of water they will encounter in flight:\n\n- **High Clouds (Above 20,000 feet):** Composed entirely of delicate ice crystals because temperatures are well below -40°C. Primary types include **Cirrus**, **Cirrostratus**, and **Cirrocumulus**. They do not present structural airframe icing risks because there is no liquid water, but they signal approaching frontal boundaries.\n- **Middle Clouds (6,500 to 20,000 feet):** Prefixed with *Alto-*, including **Altocumulus** and **Altostratus**. These clouds consist of a mixture of ice crystals and **supercooled liquid water droplets** (water colder than 0°C that remains liquid until striking an aircraft wing). Flying through middle clouds poses a severe risk of structural icing.\n- **Low Clouds (Surface to 6,500 feet):** Composed primarily of liquid water droplets. Include **Stratus**, **Stratocumulus**, and **Nimbostratus** (continuous rain cloud). Low clouds frequently drop the cloud ceiling below visual flight rules minimums, forcing aircraft to rely on electronic guidance."
                        }
                    }
                ],
                # Card 4: Technical Diagram (SVG 3)
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Cloud Classification Matrix & Severe Thunderstorm Anatomy",
                        "content": {
                            "title": "Cloud Classification Matrix & Severe Thunderstorm Anatomy",
                            "caption": "Comprehensive cloud altitude diagram showing Cirrus, Altocumulus, Stratus, Cumulus, and a severe Cumulonimbus storm anatomy with 20 NM safety buffer."
                        }
                    }
                ],
                # Card 5: Cumulonimbus: The Aviation Monster
                [
                    {
                        "type": "concept_explanation",
                        "title": "Cumulonimbus: The Anatomy of a Thunderstorm",
                        "content": {
                            "title": "The Most Dangerous Cloud in Aviation",
                            "text": "When the lower atmosphere is warm, moist, and unstable, a harmless cumulus cloud can explosively expand upward into a **Cumulonimbus (Cb)**:\n\n- **Violent Vertical Drafts:** Internal convective updrafts and downdrafts can exceed **6,000 feet per minute** (over 100 km/h vertically), generating forces capable of exceeding the structural stress limits of an aircraft airframe.\n- **Severe Airframe Icing:** Massive quantities of supercooled water droplets freeze immediately upon impact with cold aircraft wings, rapidly degrading aerofoil lift and causing aerodynamic stall.\n- **Destructive Hail:** Large chunks of hail circulating in upper updrafts can shatter cockpit windshields, dent aluminum wing leading edges, and destroy radar nose radomes.\n- **Lightning & Wind Shear:** Lightning discharges can damage avionics and antennae, while intense downward drafts (microbursts) create catastrophic loss-of-lift situations near the ground.\n- **Operational Cardinal Rule:** Aircraft must **never penetrate a cumulonimbus cloud**. Pilots must divert or maintain a mandatory safety standoff margin of at least **20 nautical miles** from the storm core."
                        }
                    }
                ],
                # Card 6: Safety Decision Scenario: Thunderstorm Diversion
                [
                    {
                        "type": "scenario_card",
                        "title": "In-Flight Thunderstorm Encounter and Diversion",
                        "content": {
                            "title": "VFR Cross-Country Flight: Approaching an Anvil Cloud",
                            "scenario": "A student pilot on a solo cross-country navigation flight observes a massive, dark anvil-topped storm cloud directly along their planned flight track 15 miles ahead.",
                            "hazard": "The cloud is a fully active Cumulonimbus producing visible lightning flashes and heavy precipitation curtains, with gust fronts extending outward from its base.",
                            "flight_risk": "Attempting to fly underneath the cloud base or squeeze past within a few miles risks severe turbulence, structural airframe damage, and low-level microburst wind shear.",
                            "correct_action": "The pilot immediately alters heading to remain at least 20 nautical miles clear of the storm cell, contacts Flight Service to obtain updated radar weather data, and diverts to a safe alternate airport if the storm blocks the destination."
                        }
                    }
                ],
                # Card 7: Curated Instructional Video
                [
                    {
                        "type": "suggested_video",
                        "title": "Clouds & Moisture Basics Explained in Flight Theory",
                        "content": {
                            "title": "Clouds & Moisture Basics Explained in Flight Theory",
                            "url": "https://www.youtube.com/watch?v=41BirFo_0UE",
                            "description": "Aviation weather tutorial covering moisture condensation, dew point spread, cloud base calculation, and the operational hazards associated with various cloud formations."
                        }
                    }
                ],
                # Card 8: Formative MCQ 1
                [
                    {
                        "type": "knowledge_check",
                        "title": "Formative Assessment: Stratus Characteristics",
                        "content": {
                            "title": "Low Stratus Cloud Identification",
                            "question": "Which type of cloud is characterized by a low, flat, grey sheet-like structure that restricts ground visibility but does not typically generate severe turbulence?",
                            "options": [
                                "Cirrus",
                                "Cumulus",
                                "Stratus",
                                "Cumulonimbus"
                            ],
                            "answer": "C",
                            "explanation": "Stratus clouds form in stable, layered air, creating a uniform horizontal blanket covering the sky. Because they lack strong vertical convective drafts, they do not produce significant turbulence, but their low ceiling and drizzle severely restrict surface visibility."
                        }
                    }
                ],
                # Card 9: Formative MCQ 2
                [
                    {
                        "type": "knowledge_check",
                        "title": "Formative Assessment: Cumulonimbus Hazards",
                        "content": {
                            "title": "Cumulonimbus Flight Hazard Analysis",
                            "question": "Why are Cumulonimbus clouds considered the most dangerous clouds in aviation?",
                            "options": [
                                "They are made entirely of carbon dioxide, which starves the jet engines of air.",
                                "They contain violent vertical wind drafts, lightning, severe icing, and hail that can cause catastrophic structural damage to an aircraft.",
                                "They block GPS satellite signals, causing the aircraft's navigation systems to fail completely.",
                                "They only form at night, making them completely invisible to pilots."
                            ],
                            "answer": "B",
                            "explanation": "Cumulonimbus storm clouds act as violent thermodynamic engines with vertical wind drafts exceeding 50 knots, destructive hail, intense lightning discharges, and severe icing capable of structurally destroying an aircraft in flight."
                        }
                    }
                ],
                # Card 10: Visual Recognition Guide & Summary
                [
                    {
                        "type": "concept_explanation",
                        "title": "Cloud Observation Guide & Summary",
                        "content": {
                            "title": "Visual Recognition Keys and Operational Rules",
                            "text": "### Quick Identification Decoder:\n- **Cirro- prefix:** High altitude (>20,000 ft), feathery, 100% ice.\n- **Alto- prefix:** Middle altitude (6,500–20,000 ft), mixed ice/water, icing danger.\n- **Stratus / Strato-:** Layered, sheet-like, stable air, visibility hazard.\n- **Cumulus / Cumulo-:** Puffy, cotton-shaped, convective thermal turbulence.\n- **Nimbus / Nimbo-:** Precipitation producer (e.g., Nimbostratus, Cumulonimbus).\n\n### Summary Safety Rule:\nAlways respect convective cloud growth. Never fly beneath or into a cumulonimbus, maintain 20 NM lateral standoff, and always inspect weather radar during flight planning."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 4: Aviation Weather Measurements and Instruments (Unit Order 3)
        # =====================================================================
        {
            "unit_order": 3,
            "unit_name": "Aviation Weather Measurements and Instruments",
            "unit_description": "Examine the operating principles and flight applications of aerodrome meteorological instruments, including thermometers, barometers, anemometers, windsocks, hygrometers, and rain gauges.",
            "lesson_title": "Aviation Weather Measurements and Instruments",
            "pages": [
                # Card 1: Visual Hook & Learning Objectives
                [
                    {
                        "type": "suggested_image",
                        "title": "Calibrated Airfield Windsock Station Beside an Active Runway",
                        "content": {
                            "title": "Calibrated Airfield Windsock Station Beside an Active Runway",
                            "caption": "An illuminated international orange and white windsock providing instantaneous visual verification of wind direction and surface gust velocity adjacent to the touchdown zone.",
                            "resolved_image_url": "https://upload.wikimedia.org/wikipedia/commons/2/2a/Marshland_Airport_windsock_and_runway_-_geograph.org.uk_-_656276.jpg"
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Learning Focus: Aerodrome Meteorological Instruments",
                        "content": {
                            "title": "Learning Focus: Aerodrome Meteorological Instruments",
                            "goals": [
                                "Identify the primary instruments installed at airport weather stations: thermometer, barometer, anemometer, windsock, hygrometer, and rain gauge.",
                                "Explain how outside air temperature measurements govern aircraft density altitude calculations.",
                                "Describe how local barometric pressure data is used to calibrate cockpit altimeters (QNH setting).",
                                "Interpret windsock inflation angles and orientation to deduce surface wind speed and heading."
                            ]
                        }
                    }
                ],
                # Card 2: Core Technical Vocabulary
                [
                    {
                        "type": "definition_card",
                        "title": "Meteorological Instrumentation Terminology",
                        "content": {
                            "title": "Essential Instrumentation Vocabulary",
                            "definitions": [
                                {
                                    "term": "Thermometer",
                                    "definition": "A calibrated instrument used to measure atmospheric temperature, typically housed inside a louvered Stevenson screen to prevent direct solar heating.",
                                    "example": "Reading 28°C on the airfield thermometer to calculate takeoff density altitude."
                                },
                                {
                                    "term": "Barometer",
                                    "definition": "An instrument designed to measure atmospheric pressure, utilizing mercury columns or flexible evacuated aneroid metal capsules.",
                                    "example": "Measuring 1018 hPa on the airport barometer to provide pilots with the local altimeter setting."
                                },
                                {
                                    "term": "Anemometer",
                                    "definition": "A rotating mechanical instrument equipped with spinning cups or ultrasonic sensors to measure horizontal wind velocity in knots.",
                                    "example": "A three-cup anemometer reporting gusts of 22 knots over the runway threshold."
                                },
                                {
                                    "term": "Wind Vane",
                                    "definition": "A balanced aerodynamic fin that pivots freely on a vertical axis to indicate the compass direction from which the wind is blowing.",
                                    "example": "Aligning to point due north (360 degrees) during a polar cold front."
                                },
                                {
                                    "term": "Windsock",
                                    "definition": "A conical, high-visibility fabric sleeve mounted on a pivot mast that reveals both wind direction and approximate wind speed to landing pilots.",
                                    "example": "A fully horizontal windsock warning pilots of crosswinds exceeding 15 knots."
                                },
                                {
                                    "term": "Hygrometer",
                                    "definition": "An instrument designed to measure relative humidity and dew point temperature by assessing moisture absorption or psychrometric cooling.",
                                    "example": "Determining an 85% relative humidity level indicating risk of carburetor icing."
                                }
                            ]
                        }
                    }
                ],
                # Card 3: The Airport Weather Instrument Suite
                [
                    {
                        "type": "concept_explanation",
                        "title": "The Aerodrome Weather Tool Kit",
                        "content": {
                            "title": "Sensor Suite of a Certified Airport Meteorological Station",
                            "text": "Every certified aerodrome maintains an official meteorological observation post or Automated Weather Observing System (AWOS). Each instrument provides critical operational inputs:\n\n- **Thermometer (°C):** Measures ambient air temperature. Used by flight crews to calculate density altitude, compute engine thrust output, and verify takeoff runway roll length.\n- **Barometer (hPa / inHg):** Measures local atmospheric air pressure. The station pressure is converted to sea-level equivalent pressure (**QNH**) and broadcast to pilots to calibrate their cockpit altimeters.\n- **Anemometer (Knots):** Accurately tracks average wind speed and peak gust velocity, ensuring flights do not exceed aircraft structural or crosswind limits.\n- **Wind Vane (Degrees Magnetic):** Directs the control tower in designating the active runway so departures and arrivals take off directly into the wind.\n- **Hygrometer (%):** Measures air moisture content to evaluate engine carburetor icing probability and atmospheric density.\n- **Rain Gauge (mm):** Quantifies precipitation intensity, alerting ground crews to standing water accumulation on runways."
                        }
                    }
                ],
                # Card 4: Technical Diagram (SVG 4)
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Aerodrome Meteorological Sensors & Windsock Speed Analysis",
                        "content": {
                            "title": "Aerodrome Meteorological Sensors & Windsock Speed Analysis",
                            "caption": "Technical diagram showing airport weather station sensors and windsock inflation angle analysis for wind speed estimation."
                        }
                    }
                ],
                # Card 5: How Altimeters Rely on the Barometer
                [
                    {
                        "type": "concept_explanation",
                        "title": "Barometric Pressure and Cockpit Altimeter Calibration",
                        "content": {
                            "title": "The Vital Link Between Ground Pressure and Flight Height",
                            "text": "An aircraft's primary altitude instrument—the **altimeter**—is fundamentally an aneroid barometer graduated in feet:\n\n- **Principle of Operation:** The altimeter senses ambient atmospheric pressure via the aircraft's pitot-static system. As the aircraft climbs, external pressure drops, allowing sealed aneroid capsules inside the instrument to expand and turn the altitude needle.\n- **The Need for Calibration:** Atmospheric pressure is constantly shifting due to weather fronts. If a pilot flies from a high-pressure weather system into a low-pressure area without updating the altimeter subscale (the **Kollsman window**), the instrument will misread.\n- **Aviation Maxim:** *'From High to Low, look out below!'* If flying into lower pressure without resetting the altimeter, the gauge will indicate the plane is higher than it actually is, creating a deadly risk of flying into hills or obstacles.\n- **Controller Setting:** Before landing, air traffic controllers broadcast the current local barometric setting (e.g., 'Altimeter 1016'), ensuring the altimeter displays true field elevation upon touchdown."
                        }
                    }
                ],
                # Card 6: Reading the Runway Windsock
                [
                    {
                        "type": "concept_explanation",
                        "title": "Visual Reading of the Runway Windsock",
                        "content": {
                            "title": "De-coding Direction and Speed from the Air",
                            "text": "The windsock is an ingenious, low-tech safety device positioned near the touchdown zone of runway ends:\n\n- **Direction Determination:** Wind enters through the wide reinforced mouth and exits out the narrow trailing tail. The tail always points **downwind** (the direction towards which the wind is blowing). The wind originates from the opposite direction.\n- **Three-Stage Speed Calibration:**\n  1. **Hanging Limp / Flaccid (< 3 knots):** Indicates light, calm winds with negligible operational impact.\n  2. **Partially Inflated / Angled (7 to 10 knots):** The sock droops at approximately 45 degrees, signaling moderate breezes.\n  3. **Fully Horizontal and Rigid (15+ knots):** The sock is blown completely straight and taut, warning pilots of brisk winds and substantial crosswind drift."
                        }
                    }
                ],
                # Card 7: Curated Instructional Video
                [
                    {
                        "type": "suggested_video",
                        "title": "PPGS Lesson 7.3 | Aircraft Instruments: Altimeter",
                        "content": {
                            "title": "PPGS Lesson 7.3 | Aircraft Instruments: Altimeter",
                            "url": "https://www.youtube.com/watch?v=nS0N69snh14",
                            "description": "Flight training tutorial detailing how atmospheric pressure governs the aneroid altimeter mechanism, subscale calibration, and operational altimetry errors."
                        }
                    }
                ],
                # Card 8: Formative MCQ 1
                [
                    {
                        "type": "knowledge_check",
                        "title": "Formative Assessment: Altimeter Setting",
                        "content": {
                            "title": "Barometric Altimeter Calibration",
                            "question": "Why must a pilot receive the latest barometer reading (altimeter setting) from an air traffic controller before landing?",
                            "options": [
                                "To check if the outside temperature will melt the aircraft's tires.",
                                "To calibrate their cockpit altimeter to ensure it displays the correct height above sea level, preventing them from flying too low.",
                                "To determine the direction and speed of the wind blowing across the runway.",
                                "To calculate the maximum cargo weight the airplane can safely carry."
                            ],
                            "answer": "B",
                            "explanation": "Because local atmospheric pressure varies constantly with moving weather patterns, pilots must adjust their altimeter subscale to match the ground pressure. Without this calibration, the altimeter will provide erroneous height readings, risking premature impact with terrain during low visibility."
                        }
                    }
                ],
                # Card 9: Formative MCQ 2
                [
                    {
                        "type": "knowledge_check",
                        "title": "Formative Assessment: Windsock Interpretation",
                        "content": {
                            "title": "Runway Windsock Evaluation",
                            "question": "If an airport windsock is observed flying completely horizontal and stiff, pointing towards the East, what can a pilot deduce about the runway wind conditions?",
                            "options": [
                                "The wind is calm (less than 3 knots) and blowing from the West.",
                                "The wind is highly humid, indicating an imminent thunderstorm.",
                                "The wind is blowing from the West at a speed of 15 knots or higher.",
                                "The runway is closed due to heavy snow."
                            ],
                            "answer": "C",
                            "explanation": "A windsock aligns with the airflow: air enters the wide mouth in the west and exits the narrow tail in the east, indicating a wind blowing *from* the West. When the sock is completely horizontal and taut, the wind velocity equals or exceeds 15 knots."
                        }
                    }
                ],
                # Card 10: Practical Windsock Modeling & Summary
                [
                    {
                        "type": "concept_explanation",
                        "title": "Model Windsock Fabrication & Chapter Summary",
                        "content": {
                            "title": "Hands-On Modeling Activity & Key Takeaways",
                            "text": "### Classroom Activity: Building a Calibrated Windsock Model\nConstruct a functional schoolyard windsock using a wire coat hanger, lightweight nylon sleeve, string swivel, and a wooden dowel mast:\n1. Shape the wire hanger into a circular hoop of 15 cm diameter.\n2. Stitch or tape a 45 cm tapered nylon cone to the hoop, alternating orange and white stripes.\n3. Attach a freely rotating fishing swivel to the hoop apex and mount atop the wooden mast.\n4. Place in an unobstructed open area of the school field and record wind direction and angle over several days.\n\n### Summary Checklist:\n- **Thermometer:** Drives density altitude and engine thrust calculations.\n- **Barometer:** Essential for altimeter subscale calibration (QNH).\n- **Anemometer & Vane:** Determine runway selection and crosswind components.\n- **Windsock:** Rapid visual speed (limp <3 kt, horizontal >15 kt) and direction guide."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 5: Effects of Weather on Flight Operations and Planning Roles (Unit Order 4)
        # =====================================================================
        {
            "unit_order": 4,
            "unit_name": "Effects of Weather on Flight Operations and Planning Roles",
            "unit_description": "Analyze the impact of severe weather hazards—turbulence, runway aquaplaning, and wind shear—on flight dynamics and evaluate the collaborative roles of meteorologists, dispatchers, air traffic controllers, and pilots in flight safety.",
            "lesson_title": "Effects of Weather on Flight Operations and Planning Roles",
            "pages": [
                # Card 1: Visual Hook & Learning Objectives
                [
                    {
                        "type": "suggested_image",
                        "title": "Commercial Jet Touching Down on a Rain-Soaked Runway",
                        "content": {
                            "title": "Commercial Jet Touching Down on a Rain-Soaked Runway",
                            "caption": "A twin-engine passenger jet landing on a wet runway, dispersing standing surface water while operating under strict crosswind and hydroplaning safety limits.",
                            "resolved_image_url": "https://upload.wikimedia.org/wikipedia/commons/e/e3/Landing_on_a_very_wet_runway_at_St._John%27s_Nfl_%2827595229845%29.jpg"
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Learning Focus: Weather Hazards & Operational Roles",
                        "content": {
                            "title": "Learning Focus: Weather Hazards & Operational Roles",
                            "goals": [
                                "Analyze the aerodynamic and operational impact of three severe weather hazards: turbulence, runway aquaplaning, and low-level wind shear.",
                                "Explain the physical mechanics of dynamic aquaplaning and how standing water destroys tire braking and steering friction.",
                                "Map the collaborative safety chain: Meteorologists, Flight Dispatchers, Air Traffic Controllers (ATC), and Pilots in Command.",
                                "Evaluate flight decision-making during severe microburst encounters, including the Go-Around procedure."
                            ]
                        }
                    }
                ],
                # Card 2: Core Technical Vocabulary
                [
                    {
                        "type": "definition_card",
                        "title": "Flight Operations & Safety Terminology",
                        "content": {
                            "title": "Essential Flight Operations Vocabulary",
                            "definitions": [
                                {
                                    "term": "Turbulence",
                                    "definition": "Irregular, chaotic atmospheric eddies and vertical currents that cause abrupt, rapid fluctuations in an aircraft's flight attitude and altitude.",
                                    "example": "Thermal turbulence experienced when crossing hot desert plains during midday."
                                },
                                {
                                    "term": "Aquaplaning (Hydroplaning)",
                                    "definition": "A condition where standing runway water builds up under an aircraft's high-speed tires, lifting the rubber completely off the asphalt and destroying braking and steering traction.",
                                    "example": "An airliner touching down on 5 mm of standing water and sliding without directional brake control."
                                },
                                {
                                    "term": "Wind Shear",
                                    "definition": "A sudden, drastic change in wind speed and/or direction over a short distance, posing acute danger to aircraft during low-altitude takeoff and landing approaches.",
                                    "example": "A sudden 25-knot loss of airspeed on short final approach forcing a go-around."
                                },
                                {
                                    "term": "Microburst",
                                    "definition": "An intense, highly localized downdraft column descending from a thunderstorm that spreads out radially in all directions upon impacting the surface.",
                                    "example": "A downdraft producing 50-knot surface outflow winds beneath a storm cell."
                                },
                                {
                                    "term": "Flight Dispatcher",
                                    "definition": "A licensed ground professional who analyzes weather forecasts, plans optimized flight routes, calculates fuel reserves, and shares legal flight operational responsibility with the captain.",
                                    "example": "Rerouting a flight around an active storm front and adding 2,000 kg of holding fuel."
                                },
                                {
                                    "term": "Meteorologist",
                                    "definition": "A professional atmospheric scientist who collects observational data, interprets satellite and radar feeds, and prepares certified aviation forecasts (METARs and TAFs).",
                                    "example": "Issuing a Terminal Aerodrome Forecast warning of afternoon thunderstorms."
                                }
                            ]
                        }
                    }
                ],
                # Card 3: Major Aviation Weather Hazards
                [
                    {
                        "type": "concept_explanation",
                        "title": "Aviation Weather Hazards: Turbulence and Wind Shear",
                        "content": {
                            "title": "Atmospheric Forces That Threaten Flight Stability",
                            "text": "When atmospheric conditions turn hostile, they generate physical forces that can challenge aircraft systems and pilot control:\n\n- **Turbulence:** Classified by cause into **Thermal** (rising warm air bubbles), **Mechanical** (wind tumbling over mountain ridges or buildings), and **Clear Air Turbulence (CAT)** (intense wind shear along high-altitude jet streams). Turbulence causes airframe vibration, passenger discomfort, and, in severe cases, structural damage.\n- **Wind Shear & Microbursts:** The most hazardous phase of flight is during final approach when an aircraft is low, slow, and configured with flaps down. A microburst pushes a concentrated shaft of cold air downward that hits the runway and spreads outward:\n  1. The aircraft first encounters a sudden strong **headwind**, causing a temporary surge in airspeed and lift.\n  2. Within seconds, the aircraft enters the central **downdraft**, pushing it toward the ground.\n  3. Finally, the aircraft enters a massive **tailwind**, which abruptly destroys wing airspeed, drops lift catastrophically, and can slam the aircraft short of the runway."
                        }
                    }
                ],
                # Card 4: Technical Diagram (SVG 5)
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Flight Weather Safety Ecosystem & Aquaplaning Dynamics",
                        "content": {
                            "title": "Flight Weather Safety Ecosystem & Aquaplaning Dynamics",
                            "caption": "Infographic showing dynamic runway aquaplaning physics alongside the four-pillar aviation weather safety ecosystem."
                        }
                    }
                ],
                # Card 5: The Physics of Runway Aquaplaning
                [
                    {
                        "type": "concept_explanation",
                        "title": "Runway Aquaplaning: Friction Loss and Braking Failure",
                        "content": {
                            "title": "Tire Hydrodynamics on Wet Runways",
                            "text": "When an aircraft touches down at speeds exceeding 120 knots on a flooded runway, water dynamics create a severe stopping hazard:\n\n- **Mechanics of Dynamic Aquaplaning:** At high rolling speeds, water cannot escape through tire grooves quickly enough. A hydrodynamic pressure wedge builds up in front of the tire, lifting the rubber tread off the pavement. The tire rides entirely atop a thin film of water with zero friction coefficient.\n- **Consequences:** Wheel brakes become totally useless because the tires are not gripping the asphalt. Rudder steering is degraded, and crosswinds can push the sliding aircraft off the runway edge.\n- **Mitigation Strategies:** Certified airports install grooved asphalt runways that channel water sideways. Modern airliners deploy **ground spoilers** upon touchdown to dump wing lift and force aircraft weight onto the landing gear, while engaging engine **thrust reversers** to decelerate aerodynamically without relying on tire friction."
                        }
                    }
                ],
                # Card 6: Operational Scenario: Eldoret Wind Shear Encounter
                [
                    {
                        "type": "scenario_card",
                        "title": "Wind Shear Alert and Go-Around at Eldoret",
                        "content": {
                            "title": "Operational Decision-Making: Aborted Landing Under Wind Shear",
                            "scenario": "A twin-turboprop airliner is on final landing approach into Eldoret International Airport. At 300 feet above the ground, the control tower warns: 'Wind shear alert. 20-knot airspeed loss reported on runway threshold.'",
                            "hazard": "A collapsing rain shaft from a nearby convective shower is generating strong outflow winds across the runway, threatening an immediate loss of airspeed and wing lift.",
                            "flight_risk": "Attempting to continue the landing risks stalling the aircraft or descending prematurely into terrain short of the runway asphalt.",
                            "correct_action": "The pilot immediately executes a Go-Around procedure: advancing throttles to maximum takeoff power, pitching up to climb attitude, calling 'Go-Around, Flaps 15', and climbing away to a safe holding altitude rather than trying to force a hazardous landing."
                        }
                    }
                ],
                # Card 7: Curated Instructional Video
                [
                    {
                        "type": "suggested_video",
                        "title": "Instrument Weather Theory & Operational Hazard Analysis",
                        "content": {
                            "title": "Instrument Weather Theory & Operational Hazard Analysis",
                            "url": "https://www.youtube.com/watch?v=9JeBd7TntfE",
                            "description": "Comprehensive flight training video examining frontal systems, convective hazard development, turbulence mechanisms, and tactical weather decision-making in airline operations."
                        }
                    }
                ],
                # Card 8: Formative MCQ 1
                [
                    {
                        "type": "knowledge_check",
                        "title": "Formative Assessment: Runway Aquaplaning",
                        "content": {
                            "title": "Runway Aquaplaning Hazards",
                            "question": "What is the primary danger of runway aquaplaning during an aircraft landing?",
                            "options": [
                                "The water will splash into the engines, causing them to stall.",
                                "The aircraft tires lose physical contact with the runway surface by riding on a film of water, preventing the brakes from stopping the plane.",
                                "The water makes the runway look like a mirror, blinding the pilot's eyes.",
                                "It causes the aircraft structure to rust instantly."
                            ],
                            "answer": "B",
                            "explanation": "Dynamic aquaplaning occurs when high forward speed and standing water create a hydrodynamic cushion that completely lifts the tires off the pavement. Without direct contact friction between rubber and asphalt, mechanical wheel braking is totally ineffective, creating an acute risk of runway excursion."
                        }
                    }
                ],
                # Card 9: Formative MCQ 2
                [
                    {
                        "type": "knowledge_check",
                        "title": "Formative Assessment: Aviation Weather Roles",
                        "content": {
                            "title": "Professional Weather Responsibilities",
                            "question": "Which professional is primarily responsible for monitoring atmospheric data, predicting storms, and issuing certified aviation weather forecasts?",
                            "options": [
                                "Flight Dispatcher",
                                "Air Traffic Controller",
                                "Meteorologist",
                                "Aircraft Maintenance Technician"
                            ],
                            "answer": "C",
                            "explanation": "Aviation meteorologists are atmospheric scientists specialized in collecting sensor data, interpreting radar and satellite imagery, and publishing certified aviation weather reports (METARs, TAFs, and SIGMET warnings) relied upon by all flight crews."
                        }
                    }
                ],
                # Card 10: The Four Pillars of Aviation Weather Safety & Summary
                [
                    {
                        "type": "concept_explanation",
                        "title": "The Four Pillars of Weather Safety & Topic Summary",
                        "content": {
                            "title": "The Safety Chain and Topic 250 Complete Synthesis",
                            "text": "### The Weather Safety Ecosystem\nFlight safety in dynamic weather is a coordinated team effort:\n1. **Meteorologist:** Observes satellite radar and barometric shifts to predict atmospheric hazards.\n2. **Flight Dispatcher:** Evaluates fuel burn, plans escape routes, and chooses suitable alternate airports.\n3. **Air Traffic Controller:** Monitors real-time radar vectors, provides wind shear warnings, and enforces safe aircraft separation.\n4. **Pilot in Command:** Holds ultimate authority to divert, delay, or initiate a go-around whenever safety is compromised.\n\n### Comprehensive Topic 250 Synthesis:\n- **Weather Elements:** Headwinds benefit takeoff/landing; tailwinds increase landing rollout; hot air degrades lift and thrust.\n- **Atmospheric Layers:** Troposphere contains active weather and cools at 2°C/1,000 ft; Stratosphere provides calm, fuel-efficient cruise.\n- **Cloud Families:** Low stratus restricts visibility; cumulus creates thermal bumps; cumulonimbus demands 20 NM strict avoidance.\n- **Measurements:** Barometer settings calibrate altimeters; windsocks provide visual speed and direction cues.\n- **Operational Roles:** Team coordination protects every flight from turbulence, wind shear, and aquaplaning."
                        }
                    }
                ]
            ]
        }
    ]

def ingest_grade10_aviation_topic250(replace=False):
    """Executes the ingestion of Topic 250 for Grade 10 Aviation."""
    print("=" * 80)
    print("VLearn Curriculum Ingestion Engine: Grade 10 Aviation — Topic 250")
    print("=" * 80)

    # Fetch Topic 250 strictly
    topic = Topic.objects.filter(id=250, subject_id=44).first()
    if not topic:
        print("[ERROR] Topic 250 (Subject ID: 44) not found in database!")
        sys.exit(1)

    print(f"[*] Target Topic: [{topic.id}] {topic.name} (Order: {topic.order})")
    print(f"[*] Subject:      [{topic.subject.id}] {topic.subject.name} (Grade: {topic.subject.grade.name})")

    curriculum_data = build_topic250_curriculum()

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
    print("[SUCCESS] Grade 10 Aviation Topic 250 Ingestion Complete!")
    print(f"[*] Total Lessons Ingested: {total_lessons}")
    print(f"[*] Total Pages/Cards:      {total_pages}")
    print(f"[*] Total Blocks Created:   {total_blocks}")
    print("=" * 80)

if __name__ == "__main__":
    replace_flag = "--replace" in sys.argv
    ingest_grade10_aviation_topic250(replace=replace_flag)
