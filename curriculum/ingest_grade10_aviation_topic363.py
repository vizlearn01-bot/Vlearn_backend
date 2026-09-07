"""
VLearn Grade 10 Aviation — Topic 363: Aircraft Tools and Materials
Production Ingestion Engine

Curriculum: CBC (Curriculum ID: 5)
Grade: Grade 10 (Grade ID: 5, Level: 10)
Subject: Aviation (Subject ID: 44)
Topic: Aircraft Tools and Materials (Topic ID: 363, Order: 5)

Ingests 5 Comprehensive Learning Units & Lessons (50 Concept Cards):
  1. Aircraft Materials: Metals (Unit Order 0, 10 Cards)
  2. Aircraft Materials: Non-Metals and Composites (Unit Order 1, 10 Cards)
  3. Aircraft Hand Tools: Cutting, Striking, and Holding (Unit Order 2, 10 Cards)
  4. Aircraft Hand Tools: Marking, Measuring, and Powered Tools (Unit Order 3, 10 Cards)
  5. Safety Precautions, Maintenance, and Tool Care (Unit Order 4, 10 Cards)

Usage:
  ./venv/bin/python curriculum/ingest_grade10_aviation_topic363.py [--replace]
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
    """Removes bracket citations [10, 71], internal visual prompt tags, and normalizes typography."""
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

def build_topic363_curriculum():
    """Returns the pedagogical page and block structure for Grade 10 Aviation Topic 363."""
    return [
        # =====================================================================
        # LESSON 1: Aircraft Materials: Metals (Unit Order 0)
        # =====================================================================
        {
            "unit_order": 0,
            "unit_name": "Aircraft Materials: Metals",
            "unit_description": "Explore the physical and metallurgical properties of aerospace metals—aluminum, steel, titanium, and magnesium alloys—and their structural applications in aircraft construction.",
            "lesson_title": "Aircraft Materials: Metals",
            "pages": [
                # Card 1: Visual Hook & Learning Objectives
                [
                    {
                        "type": "suggested_image",
                        "title": "All-Metal Aircraft Airframe Architecture",
                        "content": {
                            "title": "All-Metal Aircraft Airframe Architecture",
                            "caption": "A light aircraft featuring an all-metal semi-monocoque aluminum alloy fuselage skin and wing assembly riveted to internal structural bulkheads and ribs.",
                            "resolved_image_url": "https://upload.wikimedia.org/wikipedia/commons/5/51/Cessna_172_Skyhawk%2C_S2-AFH.jpg"
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Learning Focus: Aerospace Metallurgy",
                        "content": {
                            "title": "Learning Focus: Aerospace Metallurgy",
                            "goals": [
                                "Distinguish pure chemical metals from high-performance aerospace alloys.",
                                "Analyze the physical properties and primary aircraft applications of Aluminum, Steel, Titanium, and Magnesium.",
                                "Understand the engineering balance between high tensile strength and low density.",
                                "Explain the mechanism of galvanic corrosion and how dissimilar metals are insulated."
                            ]
                        }
                    }
                ],
                # Card 2: Foundational Terminology
                [
                    {
                        "type": "definition_card",
                        "title": "Core Aerospace Metallurgy Vocabulary",
                        "content": {
                            "title": "Core Technical Vocabulary",
                            "definitions": [
                                {
                                    "term": "Alloy",
                                    "definition": "A metallic substance composed of two or more elements fused together to enhance tensile strength, hardness, or corrosion resistance.",
                                    "example": "Duralumin (aluminum alloyed with copper, magnesium, and manganese) used in wing spars."
                                },
                                {
                                    "term": "Tensile Strength",
                                    "definition": "The maximum pulling or stretching stress a material can withstand before necking, yielding, or fracturing.",
                                    "example": "Wing lower skin panels experiencing strong tensile pulling forces during flight."
                                },
                                {
                                    "term": "Yield Strength",
                                    "definition": "The precise stress boundary where a metal stops behaving elastically and begins to suffer irreversible plastic deformation.",
                                    "example": "Landing gear shock struts absorbing hard touchdown energy within elastic limits."
                                },
                                {
                                    "term": "Galvanic Corrosion",
                                    "definition": "An electrochemical reaction occurring when two dissimilar metals make electrical contact in the presence of an electrolyte, rapidly eroding the more anodic metal.",
                                    "example": "Corrosion occurring when steel bolts are installed directly into aluminum sheet metal without sealant."
                                },
                                {
                                    "term": "Alclad",
                                    "definition": "A high-strength aluminum alloy sheet covered on both sides with a thin, metallurgically bonded layer of commercially pure aluminum for galvanic defense.",
                                    "example": "Exterior aircraft fuselage skin panels exposed to rain and coastal air."
                                }
                            ]
                        }
                    }
                ],
                # Card 3: Core Metallurgical Concepts
                [
                    {
                        "type": "concept_explanation",
                        "title": "Aerospace Metals: Balancing Strength and Weight",
                        "content": {
                            "title": "The High-Stakes Aerospace Trade-Off",
                            "text": "Every aircraft is an exercise in overcoming the pull of Earth's gravity while resisting tremendous aerodynamic pressures:\n\n- **Pure Metals vs. Alloys**: Pure elemental metals such as pure aluminum or pure iron are structurally soft, ductile, and weak. Aerospace engineers formulate **alloys**—engineered mixtures combining base metals with alloying agents like copper, zinc, magnesium, or chromium to block crystal dislocations and multiply strength.\n- **Strength-to-Weight Ratio**: The key metric in aerospace engineering is tensile strength divided by density. A material may be extremely strong (like cast iron), but if it is excessively dense, the aircraft will be too heavy to generate sufficient lift economically.\n- **Fatigue Life**: Aircraft experience thousands of pressurization and flight turbulence cycles. Structural metals must resist cyclic fatigue cracking over decades of operational service."
                        }
                    }
                ],
                # Card 4: Technical Diagram Blueprint
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Aircraft Structural Metal Distribution Blueprint",
                        "content": {
                            "title": "Airframe Metal Distribution Blueprint",
                            "caption": "Schematic breakdown displaying where aluminum alloys, steel alloys, titanium alloys, and magnesium are deployed across an airframe based on local stress and thermal conditions."
                        }
                    }
                ],
                # Card 5: Comparative Analysis Table
                [
                    {
                        "type": "comparison_table",
                        "title": "Comparative Analysis: The Four Core Aerospace Metals",
                        "content": {
                            "title": "Aerospace Metals Specification Matrix",
                            "headers": ["Metal Alloy", "Density (g/cm³)", "Primary Aviation Uses", "Core Engineering Trade-off"],
                            "rows": [
                                ["Aluminum Alloys (e.g. 2024, 7075)", "2.7 (Light)", "Fuselage skins, wing ribs, spars, bulkheads", "Vulnerable to galvanic corrosion; copper alloys require pure Alclad barrier coatings"],
                                ["Steel Alloys (Chrome-Moly, Stainless)", "7.8 (Dense)", "Landing gear struts, wheel axles, engine mounts, high-shear bolts", "Heavy mass; requires corrosion-inhibiting cadmium plating or primer paint"],
                                ["Titanium Alloys (Ti-6Al-4V)", "4.5 (Moderate)", "Jet engine compressor blades, firewalls, exhaust ducts, wing-joint fittings", "Exceptional strength up to 600°C; very expensive to mine, forge, and machine"],
                                ["Magnesium Alloys", "1.7 (Ultra-light)", "Engine accessory gearbox housings, wheel hubs, non-structural brackets", "Highly vulnerable to moisture corrosion and flammable in fine shavings/powder"]
                            ]
                        }
                    }
                ],
                # Card 6: Real-World Aviation Case Study
                [
                    {
                        "type": "real_world_example",
                        "title": "Landing Gear Maintenance Inspection at Wilson Airport",
                        "content": {
                            "title": "Non-Destructive Testing on Wilson Airport Charter Fleets",
                            "text": "At **Wilson Airport** in Nairobi, maintenance engineers servicing a twin-turboprop **Beechcraft King Air** must inspect the landing gear assemblies after scheduled operating cycles:\n\n- **Concentrated Impact**: On touchdown, the entire 5,000 kg mass of the aircraft slams onto the runway. Shock struts are forged from heat-treated chromium-nickel-molybdenum steel to withstand sudden compressive impact without bending.\n- **The Corrosion Risk**: Tropical rainfall and washdown chemicals can seep beneath damaged paint, causing hydrogen embrittlement and micro-cracking in the steel.\n- **Inspection Protocol**: Technicians apply **Magnetic Particle Inspection (MPI)**. They magnetize the steel strut and dust it with iron oxide particles suspended in fluid. Even invisible micro-cracks disrupt the magnetic field, glowing under ultraviolet inspection lamps to catch flaws before an axle fails."
                        }
                    }
                ],
                # Card 7: Educational Video Integration
                [
                    {
                        "type": "suggested_video",
                        "title": "Materials in Aerospace: Aluminum, Titanium & Composites",
                        "content": {
                            "title": "Metallurgy and Materials in Aerospace Engineering",
                            "description": "Visual breakdown of crystal structures, yield strength tests, and high-temperature performance of aerospace aluminum, titanium, and modern alloys.",
                            "url": "https://www.youtube.com/watch?v=CGiR4LxaLO0"
                        }
                    }
                ],
                # Card 8: Safety Connection & Galvanic Hazards
                [
                    {
                        "type": "concept_explanation",
                        "title": "The Hidden Threat of Galvanic Corrosion",
                        "content": {
                            "title": "Dissimilar Metal Hazards and Isolation Techniques",
                            "text": "Consider a maintenance scenario where an untrained technician fastens an aluminum skin panel with bare stainless steel screws because 'steel is stronger':\n\n- **The Electrochemical Cell**: Aluminum and steel have widely separated electrical potentials on the galvanic scale. When moisture or humidity penetrates the fastener hole, a miniature battery forms.\n- **The Structural Failure**: Aluminum acts as the sacrificial anode and corrodes rapidly into powdery white aluminum oxide. The rivet hole enlarges, the fastener pulls loose, and the pressurized skin panel tears free in flight.\n- **Approved Isolation Practice**: Aircraft mechanics must only use approved aluminum fasteners on aluminum airframes. Where steel bolts must pass through aluminum fittings, mechanics apply wet zinc-chromate or epoxy barrier sealants to ensure complete electrical isolation."
                        }
                    }
                ],
                # Card 9: Formative Knowledge Check 1
                [
                    {
                        "type": "knowledge_check",
                        "title": "Formative Check: Material Selection for Landing Gear",
                        "content": {
                            "question": "Why do aerospace engineers construct commercial aircraft landing gear struts and wheel axles from high-strength steel alloys rather than aluminum alloys, despite steel being nearly three times heavier?",
                            "options": [
                                "Steel is completely immune to rust and chemical attack from de-icing fluids.",
                                "Steel provides exceptional hardness, wear resistance, and high tensile yield strength capable of absorbing intense, repeated touchdown impact forces without permanent bending.",
                                "Aluminum is strongly magnetic and would cause catastrophic interference with the cockpit magnetic compass.",
                                "Steel alloys become significantly lighter than aluminum when flying at cold high-altitude temperatures."
                            ],
                            "answer": "B",
                            "explanation": "Landing gear assemblies experience massive concentrated compressive impact forces upon touchdown. Aluminum alloys would undergo permanent plastic deformation or crack under repeated landing loads. High-tensile steel provides the required yield toughness, fatigue endurance, and wear resistance to ensure safe landing cycles."
                        }
                    }
                ],
                # Card 10: Formative Knowledge Check 2
                [
                    {
                        "type": "knowledge_check",
                        "title": "Formative Check: Preventing Galvanic Corrosion",
                        "content": {
                            "question": "What structural protection method is mandatory when installing copper-alloyed aluminum skin panels on an aircraft to prevent galvanic corrosion?",
                            "options": [
                                "Heating the aluminum panels with an open flame torch until the crystalline structure melts together.",
                                "Applying motor oil over the raw fastener joints daily to keep them wet.",
                                "Using pure aluminum Alclad outer surface layers and inserting non-conductive barrier sealants to prevent moisture-driven electrical contact between dissimilar metals.",
                                "Replacing all metallic structural rivets with quick-drying household plastic adhesive."
                            ],
                            "answer": "C",
                            "explanation": "Galvanic corrosion requires electrical contact between dissimilar metals in the presence of an electrolyte. Metallurgically bonded pure aluminum cladding (Alclad) acts as a sacrificial barrier layer, and insulating chemical sealants break the electrical conductive circuit, preventing catastrophic corrosion."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 2: Aircraft Materials: Non-Metals and Composites (Unit Order 1)
        # =====================================================================
        {
            "unit_order": 1,
            "unit_name": "Aircraft Materials: Non-Metals and Composites",
            "unit_description": "Analyze advanced composite materials—carbon fiber, fiberglass, and Kevlar—alongside legacy wood and fabrics, evaluating their resin matrix systems and delamination risks.",
            "lesson_title": "Aircraft Materials: Non-Metals and Composites",
            "pages": [
                # Card 1: Visual Hook & Learning Objectives
                [
                    {
                        "type": "suggested_image",
                        "title": "Advanced Composite Commercial Airliner Airframe",
                        "content": {
                            "title": "Advanced Composite Commercial Airliner Airframe",
                            "caption": "A Boeing 787 Dreamliner featuring an airframe structure constructed with over 50% advanced carbon fiber reinforced polymer composites for superior fuel efficiency and fatigue life.",
                            "resolved_image_url": "https://upload.wikimedia.org/wikipedia/commons/5/55/Saudi_Arabian_Airlines_Boeing_787-10_Dreamliner_London_Gatwick_Airport.jpg"
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Learning Focus: Advanced Composites",
                        "content": {
                            "title": "Learning Focus: Advanced Composites",
                            "goals": [
                                "Define the two-phase structural anatomy of a composite: reinforcement fibers and resin matrix.",
                                "Compare the properties and aviation applications of Carbon Fiber, Fiberglass, Kevlar, and Sitka Spruce.",
                                "Explain how directional fiber orientation (anisotropy) allows customized structural strength.",
                                "Understand composite delamination and the necessity of Non-Destructive Testing (NDT)."
                            ]
                        }
                    }
                ],
                # Card 2: Foundational Terminology
                [
                    {
                        "type": "definition_card",
                        "title": "Core Composite Materials Vocabulary",
                        "content": {
                            "title": "Core Technical Vocabulary",
                            "definitions": [
                                {
                                    "term": "Composite Material",
                                    "definition": "A structural material made by combining two or more distinct substances—reinforcing fibers and a bonding matrix—that remain physically separate on a microscopic scale while producing superior combined performance.",
                                    "example": "Carbon Fiber Reinforced Polymer (CFRP) used in modern airliner wing skins."
                                },
                                {
                                    "term": "Matrix (Resin)",
                                    "definition": "The polymer glue (typically thermosetting epoxy) that binds structural reinforcement fibers together, transferring stresses between fibers and preventing them from buckling.",
                                    "example": "Epoxy resin cured under heat and pressure inside an autoclave."
                                },
                                {
                                    "term": "Delamination",
                                    "definition": "A dangerous structural flaw where bonded internal plies of a composite separate from one another, creating an invisible internal void that drastically reduces load capacity.",
                                    "example": "Internal layer separation caused by an accidental ground vehicle impact against a wing."
                                },
                                {
                                    "term": "Anisotropic",
                                    "definition": "Exhibiting different physical and mechanical properties when loaded in different directions.",
                                    "example": "A composite laminate displaying high tensile strength along fiber threads, but lower strength perpendicular to them."
                                },
                                {
                                    "term": "Radome",
                                    "definition": "A weatherproof dielectric aerodynamic dome covering an aircraft radar antenna, built from materials transparent to radio frequency waves.",
                                    "example": "The fiberglass nose cone housing the forward weather radar on passenger jets."
                                }
                            ]
                        }
                    }
                ],
                # Card 3: Core Composite Anatomy
                [
                    {
                        "type": "concept_explanation",
                        "title": "The Two-Phase Architecture of Composites",
                        "content": {
                            "title": "Reinforcement Fibers and the Polymeric Matrix",
                            "text": "Advanced composites operate much like reinforced concrete in civil engineering:\n\n- **Reinforcement Phase (Tension Bearers)**: The structural fibers (carbon, glass, or aramid threads) possess extraordinary tensile strength. Like steel rebar in concrete, they carry pulling loads along their longitudinal axis.\n- **Matrix Phase (Compression & Shear Transfer)**: The cured epoxy resin surrounds and encases every fiber. The matrix supports the fibers against buckling under compression, transfers shear forces between plies, and protects the fibers from moisture, fuel, and chemical abrasion.\n- **Quasi-Isotropic Layup**: Because single unidirectional plies are strong only in one direction, engineers stack plies in alternating orientations (0°, 45°, -45°, 90°) to construct laminates that withstand forces from all angles."
                        }
                    }
                ],
                # Card 4: Technical Diagram Blueprint
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Carbon Fiber Composite Laminate Ply Architecture",
                        "content": {
                            "title": "Composite Laminate Microstructure Blueprint",
                            "caption": "Cutaway diagram illustrating how multidirectional fiber plies (0°, 45°, 90°) are suspended within a cured epoxy matrix to engineer multidirectional airframe strength."
                        }
                    }
                ],
                # Card 5: Comparative Non-Metals Analysis Table
                [
                    {
                        "type": "comparison_table",
                        "title": "Comparative Analysis: Non-Metals and Advanced Composites",
                        "content": {
                            "title": "Aerospace Non-Metals Matrix",
                            "headers": ["Material System", "Key Mechanical Property", "Primary Aviation Uses", "Core Limitation"],
                            "rows": [
                                ["Carbon Fiber (CFRP)", "Exceptional stiffness-to-weight, zero metal fatigue", "Fuselage barrels, wing skins, vertical stabilizers", "Brittle under impact; vulnerable to hidden internal delamination"],
                                ["Fiberglass (GFRP)", "Dielectric (radar transparent), cost-effective", "Nose radomes, fairings, passenger cabin overhead bins", "Heavier and less rigid than carbon fiber"],
                                ["Kevlar (Aramid)", "Supreme impact resistance, puncture absorption", "Engine blade-containment cowls, cargo bay floor liners", "Low compressive strength; absorbs atmospheric moisture if unsealed"],
                                ["Sitka Spruce & Aircraft Fabric", "High elasticity, light weight, easily shaped with hand tools", "Vintage aircraft restoration, aerobatic biplanes, gliders", "Susceptible to biological rot, insect infestation, and UV solar degradation"]
                            ]
                        }
                    }
                ],
                # Card 6: Real-World Industry Application
                [
                    {
                        "type": "real_world_example",
                        "title": "Wing Flex Dynamics on the Boeing 787 Dreamliner",
                        "content": {
                            "title": "Fatigue-Free Wing Aerodynamics in Modern Aviation",
                            "text": "When observing a **Boeing 787 Dreamliner** take off from an international runway, passengers notice the wingtips flexing dramatically upward by nearly three meters:\n\n- **Elastic Performance**: This dramatic flex is safely engineered through advanced **carbon fiber composites**. The continuous carbon fibers in the wing spars stretch elastically without entering plastic deformation.\n- **Zero Metal Fatigue**: If an aluminum wing flexed to this degree repeatedly, it would rapidly develop microscopic fatigue cracks around fastener holes. Carbon fiber composites distribute aerodynamic loads without crystalline fatigue, drastically extending the airframe's service lifespan.\n- **Weight Savings**: Replacing metal skin and rib assemblies with molded composite single-piece barrels reduces airframe weight by 20%, resulting in significant fuel burn reductions."
                        }
                    }
                ],
                # Card 7: Educational Video Integration
                [
                    {
                        "type": "suggested_video",
                        "title": "From Metals to Composites: Decoding Aircraft Materials",
                        "content": {
                            "title": "Manufacturing and Testing Advanced Aircraft Composites",
                            "description": "Visual guide demonstrating how dry carbon fiber weaves are molded, vacuum-bagged, and cured under high pressure in industrial autoclaves.",
                            "url": "https://www.youtube.com/watch?v=2Q5MFjibiX0"
                        }
                    }
                ],
                # Card 8: Safety Connection & Hidden Delamination
                [
                    {
                        "type": "concept_explanation",
                        "title": "The Critical Danger of Barely Visible Impact Damage (BVID)",
                        "content": {
                            "title": "Why Visual Inspection Fails on Composite Airframes",
                            "text": "Consider a hangar ground operation where a motorized baggage tug lightly bumps into the composite fuselage of an aircraft:\n\n- **The Optical Deception**: When metal is struck, it deforms and leaves an obvious dent. High-performance composite panels, however, bounce back elastically, leaving the outer paint looking completely intact.\n- **The Subsurface Crisis**: Deep inside the laminate, the shock wave shatters the epoxy matrix and separates the fiber plies—a defect known as **delamination** or Barely Visible Impact Damage (BVID).\n- **In-Flight Risk**: When the cabin pressurizes at 35,000 feet, hoop tension concentrates at the hollow delaminated void, which can rip open under pressure.\n- **Mandatory Response**: Every reported ground impact requires **Non-Destructive Testing (NDT)** using ultrasonic phased-array scanners or acoustic tap hammers to confirm internal bond integrity."
                        }
                    }
                ],
                # Card 9: Formative Knowledge Check 1
                [
                    {
                        "type": "knowledge_check",
                        "title": "Formative Check: Radome Material Selection",
                        "content": {
                            "question": "Why must an aircraft nose radome (the dome housing the forward weather radar) be constructed from fiberglass rather than carbon fiber?",
                            "options": [
                                "Fiberglass is significantly stiffer and lighter than carbon fiber during supersonic flight.",
                                "Carbon fiber contains electrically conductive fibers that block and reflect radar signals, whereas fiberglass is electrically non-conductive and transparent to radio frequencies.",
                                "Fiberglass is completely water-soluble and washes clean automatically during flight in rainstorms.",
                                "Carbon fiber attracts lightning strikes into the cockpit sensitive electronics."
                            ],
                            "answer": "B",
                            "explanation": "Weather radar requires unobstructed transmission and reception of electromagnetic radio waves. Carbon fiber composites contain conductive crystalline carbon filaments that act as a Faraday shield, reflecting radar pulses. Fiberglass is a dielectric insulator, permitting clear radio frequency transmission without signal distortion."
                        }
                    }
                ],
                # Card 10: Formative Knowledge Check 2
                [
                    {
                        "type": "knowledge_check",
                        "title": "Formative Check: Understanding Composite Delamination",
                        "content": {
                            "question": "What makes composite internal delamination particularly dangerous during pre-flight maintenance inspections?",
                            "options": [
                                "Delaminated resin glows bright red in sunlight, distracting runway ground controllers.",
                                "Severe internal ply separation can occur beneath the surface following a minor ground impact without leaving any visible dent, crack, or scratch on the outer painted skin.",
                                "Delamination instantly drains all electrical power from the aircraft navigation batteries.",
                                "Delaminated composite plies dissolve into toxic poisonous gas when exposed to freezing air."
                            ],
                            "answer": "B",
                            "explanation": "Advanced composite laminates absorb impacts elastically, snapping back into shape. While the exterior surface may appear unblemished, the internal fiber plies can separate (delaminate). This hidden defect compromises structural strength and can fail catastrophically under flight pressure loads if not detected using acoustic or ultrasonic NDT instruments."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 3: Aircraft Hand Tools: Cutting, Striking, and Holding (Unit Order 2)
        # =====================================================================
        {
            "unit_order": 2,
            "unit_name": "Aircraft Hand Tools: Cutting, Striking, and Holding",
            "unit_description": "Master precision aviation hand tools—color-coded snips, hacksaw pitch selection, ball-peen vs. soft mallets, and Cleco temporary sheet metal clamping fasteners.",
            "lesson_title": "Aircraft Hand Tools: Cutting, Striking, and Holding",
            "pages": [
                # Card 1: Visual Hook & Learning Objectives
                [
                    {
                        "type": "suggested_image",
                        "title": "Aircraft Sheet Metal Cleco Fasteners",
                        "content": {
                            "title": "Aircraft Sheet Metal Cleco Fasteners",
                            "caption": "Spring-loaded Cleco temporary sheet metal fasteners used by aircraft structural mechanics to clamp pre-drilled aluminum skin panels into precise alignment prior to permanent riveting.",
                            "resolved_image_url": "https://upload.wikimedia.org/wikipedia/commons/5/57/Cleco_3.2_and_4.8mm_temporary_fasteners.jpg"
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Learning Focus: Cutting, Striking, and Holding Hand Tools",
                        "content": {
                            "title": "Learning Focus: Hand Tool Precision",
                            "goals": [
                                "Decode the color-coding system of aviation snips (Red, Green, Yellow) for directional sheet metal cutting.",
                                "Apply the Rule of Pitch for hacksaw blades when cutting aircraft tubing and brackets.",
                                "Distinguish ball-peen hammers from soft-faced mallets to prevent surface bruising and stress risers.",
                                "Operate Cleco temporary fasteners and pliers to maintain precise structural alignment during sheet metal assembly."
                            ]
                        }
                    }
                ],
                # Card 2: Foundational Terminology
                [
                    {
                        "type": "definition_card",
                        "title": "Core Aircraft Hand Tools Vocabulary",
                        "content": {
                            "title": "Core Technical Vocabulary",
                            "definitions": [
                                {
                                    "term": "Aviation Snips",
                                    "definition": "Compound-action hand shears designed to slice through sheet aluminum without twisting the stock, color-coded by cutting curvature.",
                                    "example": "Red-handled snips used by sheet metal mechanics to cut counter-clockwise circles."
                                },
                                {
                                    "term": "Cleco Fastener",
                                    "definition": "A spring-loaded expanding steel clamping pin inserted into drilled holes to hold overlapping metal sheets securely together prior to riveting.",
                                    "example": "Copper-bodied 1/8-inch Clecos securing a fuselage repair doubler plate."
                                },
                                {
                                    "term": "Pitch (Hacksaw)",
                                    "definition": "The spacing of cutting teeth on a blade, expressed in teeth per inch (TPI).",
                                    "example": "A 32 TPI fine-tooth blade chosen to cut thin-walled hydraulic aluminum tubing."
                                },
                                {
                                    "term": "Soft-Faced Mallet",
                                    "definition": "A striking tool featuring heads made of rubber, plastic, wood, or brass designed to shape sheet metal without marring the protective cladding.",
                                    "example": "A shot-filled rubber mallet used to form wing rib flanges over wooden forming blocks."
                                },
                                {
                                    "term": "Stress Riser",
                                    "definition": "A localized surface scratch, dent, or sharp notch that concentrates mechanical stresses, initiating rapid fatigue cracking under cyclic flight loads.",
                                    "example": "A gouge left by toothed slip-joint pliers on an aluminum flight control pushrod."
                                }
                            ]
                        }
                    }
                ],
                # Card 3: Cutting Tools Engineering
                [
                    {
                        "type": "concept_explanation",
                        "title": "Cutting Tools: Snips, Hacksaws, and Files",
                        "content": {
                            "title": "Precision Cutting Mechanics in Sheet Metal Fabrication",
                            "text": "Cutting aircraft sheet metal requires techniques that prevent warping, curling, or leaving stress-concentrating micro-burrs:\n\n- **Decoding Aviation Snips**:\n  - **Red Snips (Left Cut)**: Cut tight curves to the left (counter-clockwise). The waste scrap curls up and away to the right, keeping the main sheet flat.\n  - **Green Snips (Right Cut)**: Cut curves to the right (clockwise). Waste curls away to the left.\n  - **Yellow Snips (Straight Cut)**: Cut straight lines and gentle, wide-radius curves.\n- **Hacksaw Rule of Pitch**: At least **two consecutive teeth** must engage the metal thickness at all times. Using coarse blades on thin tubing causes teeth to straddle the edge, snapping teeth off and jamming the cut.\n- **Aircraft Filing Protocol**: Files cut only on the forward stroke. Mechanics must never drag a file backwards, as reverse friction rolls over the hardened cutting teeth and ruins the file."
                        }
                    }
                ],
                # Card 4: Technical Diagram Blueprint
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Sheet Metal Assembly and Tool Operations Blueprint",
                        "content": {
                            "title": "Sheet Metal Fabrication & Clamping Blueprint",
                            "caption": "Engineering diagram illustrating overlapping sheet metal panels secured by spring-loaded Cleco fasteners, trimmed with aviation snips, and formed using a soft-faced mallet."
                        }
                    }
                ],
                # Card 5: Tool Functional Matrix Table
                [
                    {
                        "type": "comparison_table",
                        "title": "Functional Tool Matrix: Aviation Hand Tools",
                        "content": {
                            "title": "Aviation Hand Tool Operational Guide",
                            "headers": ["Tool Type", "Aviation Specific Design", "Correct Operational Technique", "Critical Safety Rule"],
                            "rows": [
                                ["Aviation Snips", "Compound-action serrated blades, color-coded handles", "Rest flat blade on sheet; keep scrap curling away from layout line", "Never cut hardened steel wire or bolts; snips are for soft sheet alloys"],
                                ["Aviation Hacksaw", "High-speed steel flexible blade (18 to 32 TPI)", "Maintain 50-60 strokes/min; ensure >= 2 teeth contact stock", "Install blade with teeth pointing forward away from handle"],
                                ["Ball-Peen Hammer", "Hardened forged carbon steel; flat face and hemispherical peen", "Use flat face for driving steel punches; peen for forming hand rivets", "Never strike finished aluminum skin panels directly with a steel hammer"],
                                ["Soft-Faced Mallet", "Rubber, plastic, or brass non-marring striking faces", "Deliver controlled blows to form sheet metal over wooden form blocks", "Inspect head for embedded metal chips that could scratch Alclad skins"],
                                ["Cleco Fasteners", "Spring-loaded expanding split-pin clamping mechanism", "Compress with Cleco pliers; insert into aligned hole; release to clamp", "Place a Cleco in every 3rd or 4th hole to prevent sheet metal bulging during drilling"]
                            ]
                        }
                    }
                ],
                # Card 6: Real-World Industry Application
                [
                    {
                        "type": "real_world_example",
                        "title": "Wing Leading-Edge Sheet Metal Repair at Nairobi Hangars",
                        "content": {
                            "title": "Flawless Alignment During Bird-Strike Skin Replacement",
                            "text": "In commercial aircraft hangars at **Nairobi**, technicians frequently repair wing leading edges damaged by bird strikes:\n\n- **Layout and Trim**: Mechanics select 2024-T3 Alclad sheet metal and use **Yellow Aviation Snips** to cut a replacement patch.\n- **Precision Clamping**: Hundreds of rivet holes must be match-drilled through the patch into internal wing ribs. Without clamping, drill vibration causes sheets to slip, producing oval, misaligned holes.\n- **Cleco Deployment**: Technicians insert **Cleco fasteners** every three holes as drilling proceeds. The spring tension clamps the sheets together under 25 pounds of force, keeping the surface tight and aerodynamic before permanent flush riveting."
                        }
                    }
                ],
                # Card 7: Educational Video Integration
                [
                    {
                        "type": "suggested_video",
                        "title": "Aircraft Hand Tools and Measuring Devices",
                        "content": {
                            "title": "Demonstrating Aviation Sheet Metal Hand Tools",
                            "description": "Practical demonstration of aviation snips, hacksaw pitch selection, Cleco fastener insertion pliers, and proper edge deburring technique.",
                            "url": "https://www.youtube.com/watch?v=NSlz_PSm7wY"
                        }
                    }
                ],
                # Card 8: Safety Connection & Tool-Induced Stress Risers
                [
                    {
                        "type": "concept_explanation",
                        "title": "Stress Risers and Improper Tool Selection",
                        "content": {
                            "title": "How Incorrect Tool Usage Causes In-Flight Catastrophic Failure",
                            "text": "Consider a technician adjusting an engine throttle linkage rod using common hardware serrated slip-joint pliers:\n\n- **The Mechanical Damage**: The hardened steel serrations bite into the smooth aluminum pushrod, gouging sharp micro-notches into the surface.\n- **Stress Concentration**: In flight, engine vibration creates cyclic bending stresses. Stress lines concentrate at the sharp bottom of each jaw scratch.\n- **Fatigue Propagation**: A microscopic fatigue crack initiates at the notch root and tears through the pushrod within 50 flight hours, disconnecting engine power control.\n- **Aviation Standard**: Technicians must use smooth-jaw **duckbill pliers**, wrap protective tape around sensitive parts, or use brass-jaw clamping tools to prevent scratching aircraft components."
                        }
                    }
                ],
                # Card 9: Formative Knowledge Check 1
                [
                    {
                        "type": "knowledge_check",
                        "title": "Formative Check: Aviation Snip Color Decoding",
                        "content": {
                            "question": "Why are aviation sheet metal snip handles manufactured with distinct color codes (Red, Green, Yellow)?",
                            "options": [
                                "The colors designate the thickness gauge of hardened stainless steel armor they are rated to slice.",
                                "The colors indicate the cutting curve direction (Red cuts Left, Green cuts Right, Yellow cuts Straight), ensuring waste metal curls away without warping the primary airframe sheet.",
                                "The colors correspond to standard electrical circuit voltage warnings inside the aircraft avionics bay.",
                                "The colors indicate whether the tool should be operated in high-altitude freezing temperatures."
                            ],
                            "answer": "B",
                            "explanation": "Aviation snips use compound-action jaws shaped for directional clearance. Red-handled snips cut to the left, curling scrap to the right; green-handled snips cut to the right, curling scrap to the left; and yellow-handled snips cut straight lines. Selecting the proper direction prevents buckling the finished skin panel."
                        }
                    }
                ],
                # Card 10: Formative Knowledge Check 2
                [
                    {
                        "type": "knowledge_check",
                        "title": "Formative Check: Mallet vs. Hammer Selection",
                        "content": {
                            "question": "Why must an aircraft structural technician use a soft-faced mallet (rubber, plastic, or wood) rather than a steel ball-peen hammer when forming aluminum skin panels?",
                            "options": [
                                "Steel ball-peen hammers are far too lightweight to bend aluminum sheet metal.",
                                "Soft-faced mallets distribute the striking force evenly without marring, bruising, or scratching the pure aluminum Alclad layer, preventing stress risers and corrosion cracking.",
                                "Steel ball-peen hammers generate magnetic radiation that erases cockpit flight recorder memory chips.",
                                "Soft-faced mallets contain internal heating elements that anneal the metal during striking."
                            ],
                            "answer": "B",
                            "explanation": "Striking soft aluminum with a hardened steel hammer dents the surface and scratches through the protective pure-aluminum cladding (Alclad). These indentations become stress risers that initiate fatigue cracks under aerodynamic vibrations. Soft-faced mallets cushion the blow, forming the metal smoothly without surface damage."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 4: Aircraft Hand Tools: Marking, Measuring, and Powered Tools (Unit Order 3)
        # =====================================================================
        {
            "unit_order": 3,
            "unit_name": "Aircraft Hand Tools: Marking, Measuring, and Powered Tools",
            "unit_description": "Examine precision marking tools, Vernier calipers, micrometers, and spark-free pneumatic tools utilized in aerospace manufacturing and assembly.",
            "lesson_title": "Aircraft Hand Tools: Marking, Measuring, and Powered Tools",
            "pages": [
                # Card 1: Visual Hook & Learning Objectives
                [
                    {
                        "type": "suggested_image",
                        "title": "Precision Metric Vernier Caliper",
                        "content": {
                            "title": "Precision Metric Vernier Caliper",
                            "caption": "A precision stainless steel vernier caliper equipped with external measuring jaws, internal measuring nibs, and a sliding depth rod for verifying micro-tolerances in aviation manufacturing.",
                            "resolved_image_url": "https://upload.wikimedia.org/wikipedia/commons/c/c2/Mahr_MarCal_16_N_vernier_caliper.png"
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Learning Focus: Marking, Measuring, and Powered Tools",
                        "content": {
                            "title": "Learning Focus: Precision Measurement and Pneumatics",
                            "goals": [
                                "Explain why steel scribes are prohibited on structural airframe parts and identify approved marking tools.",
                                "Read and interpret three-way Vernier caliper measurements (outer diameter, inner diameter, depth).",
                                "Operate precision outside micrometers down to 0.001 mm utilizing the ratchet stop.",
                                "Explain the safety and operational advantages of spark-free pneumatic tools over electric tools in aviation hangars."
                            ]
                        }
                    }
                ],
                # Card 2: Foundational Terminology
                [
                    {
                        "type": "definition_card",
                        "title": "Core Measuring and Powered Tools Vocabulary",
                        "content": {
                            "title": "Core Technical Vocabulary",
                            "definitions": [
                                {
                                    "term": "Vernier Caliper",
                                    "definition": "A high-precision sliding scale measuring tool capable of measuring outside dimensions, inside hole diameters, and recess depths to within 0.02 mm.",
                                    "example": "Measuring the inner diameter of an airframe bushing prior to press-fit installation."
                                },
                                {
                                    "term": "Outside Micrometer",
                                    "definition": "An ultra-precision screw thread instrument capable of measuring material thicknesses down to one-thousandth of a millimeter (0.001 mm).",
                                    "example": "Measuring the wall thickness of an aircraft hydraulic pressure tube."
                                },
                                {
                                    "term": "Ratchet Stop",
                                    "definition": "A spring-loaded mechanism on a micrometer thimble that slips once uniform contact pressure is applied, preventing over-tightening and distorted readings.",
                                    "example": "Clicking the ratchet three times to ensure consistent measurement force."
                                },
                                {
                                    "term": "Pneumatic Tool",
                                    "definition": "A mechanical power tool driven by compressed air rather than an electric motor.",
                                    "example": "An air drill turning at 3,000 RPM used inside an aircraft fuel cell bay."
                                },
                                {
                                    "term": "Pneumatic Rivet Gun",
                                    "definition": "An air-powered cyclic hammer that drives a rivet set against a solid rivet while a bucking bar flattens the shop head on the reverse side.",
                                    "example": "A 3X pneumatic rivet gun driving 1/8-inch 2117 aluminum rivets into a fuselage lap joint."
                                }
                            ]
                        }
                    }
                ],
                # Card 3: Marking and Measuring Principles
                [
                    {
                        "type": "concept_explanation",
                        "title": "Microscopic Tolerances: Calipers and Micrometers",
                        "content": {
                            "title": "The Science of Aerospace Dimensional Verification",
                            "text": "In aviation engineering, components operate under extreme dynamic stresses where fractions of a millimeter dictate airworthiness:\n\n- **The Three Measurements of a Caliper**:\n  - **Outside Jaws**: Measure component outer diameters, bolt shank dimensions, and sheet thicknesses.\n  - **Inside Jaws**: Measure hole diameters, bushing clearances, and slot widths.\n  - **Depth Rod**: Extends from the bottom beam to measure blind hole depths and counterbore recesses.\n- **Outside Micrometer Operation**: Built with a precision ground spindle having 0.5 mm pitch threads. Turning the thimble advances the spindle toward the stationary anvil. Technicians read the sleeve scale (whole and half millimeters) and the thimble scale (hundredths of a millimeter), yielding 0.001 mm resolution.\n- **Marking Rules**: Steel scribes scratch through the Alclad protective layer and notch the metal. Technicians must strictly use soft graphite pencils, fine felt-tip markers, or layout dye on structural airframes."
                        }
                    }
                ],
                # Card 4: Technical Diagram Blueprint
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Vernier Caliper and Outside Micrometer Anatomy Blueprint",
                        "content": {
                            "title": "Precision Measuring Instruments Blueprint",
                            "caption": "Detailed engineering layout showing the anatomy and operational scales of a metric Vernier caliper and outside micrometer with ratchet stop."
                        }
                    }
                ],
                # Card 5: Measuring & Power Tool Comparison Table
                [
                    {
                        "type": "comparison_table",
                        "title": "Comparative Analysis: Precision Measuring and Power Tools",
                        "content": {
                            "title": "Aviation Precision Tools Reference Matrix",
                            "headers": ["Tool Instrument", "Measurement Range / Type", "Primary Aircraft Task", "Operating Protocol"],
                            "rows": [
                                ["Vernier Caliper", "0 - 150 mm (0.02 mm resolution)", "Bushings, bolt diameters, sheet thickness, hole depths", "Inspect zero mark alignment; apply light thumb pressure on sliding jaw"],
                                ["Outside Micrometer", "0 - 25 mm (0.001 mm resolution)", "Valve stems, hydraulic tubing wall thickness, skin doublers", "Always use the ratchet stop; clean anvil and spindle faces before measuring"],
                                ["Bevel Protractor", "0° - 360° angular measurement", "Flight control surface travel angles (ailerons, elevators, flaps)", "Lock clamping knob firmly against surface before reading vernier degree scale"],
                                ["Pneumatic Air Drill", "Rotary compressed air motor (up to 4,000 RPM)", "Match-drilling rivet holes through airframe skin and ribs", "Hold 90° perpendicular to skin; use light feed pressure to prevent sheet dimpling"],
                                ["Pneumatic Rivet Gun", "Cyclic air hammer (2X, 3X, 4X ratings)", "Driving solid aircraft structural rivets against bucking bars", "Regulate air pressure at tool inlet; keep rivet set firmly centered on rivet head"]
                            ]
                        }
                    }
                ],
                # Card 6: Real-World Industry Application
                [
                    {
                        "type": "real_world_example",
                        "title": "Turbine Blade Tip-Clearance Measurement",
                        "content": {
                            "title": "Sub-Millimeter Tolerances in Jet Engine Maintenance",
                            "text": "Inside high-bypass turbofan jet engines operating on commercial passenger routes, dimensional accuracy is a matter of life and death:\n\n- **Compressor Clearance**: The gap between spinning titanium compressor blade tips and the stationary shroud casing is typically less than **0.50 millimeters**.\n- **Precision Gauging**: Technicians utilize calibrated feeler gauges, dial indicators, and depth micrometers to verify clearance at eight radial positions around the engine circumference.\n- **Performance Impact**: If the gap increases by just 0.1 mm due to casing wear, high-pressure air leaks backward, causing engine compressor stalls. If the gap is too small, thermal expansion at cruise altitude will cause blades to rub against the shroud, triggering uncontained engine destruction."
                        }
                    }
                ],
                # Card 7: Educational Video Integration
                [
                    {
                        "type": "suggested_video",
                        "title": "How to Read a Metric Vernier Caliper",
                        "content": {
                            "title": "Precision Measurement Tutorial: Metric Vernier Calipers",
                            "description": "Step-by-step visual instruction on reading main beam millimeter graduations and aligning Vernier scale divisions down to 0.02 mm accuracy.",
                            "url": "https://www.youtube.com/watch?v=vkPlzmalvN4"
                        }
                    }
                ],
                # Card 8: Safety Connection & Hangar Explosion Hazards
                [
                    {
                        "type": "concept_explanation",
                        "title": "Pneumatic vs. Electric Tools: Preventing Hangar Explosions",
                        "content": {
                            "title": "Intrinsic Safety in Volatile Fuel-Vapor Environments",
                            "text": "Consider why commercial airline maintenance facilities strictly ban standard household electric drills:\n\n- **Volatile Atmosphere**: Aviation fuel (Jet A-1 and Avgas 100LL) constantly produces volatile hydrocarbons during tank venting, defueling, or maintenance.\n- **The Brush-Motor Spark**: Electric tools utilize commutators and carbon brushes that generate miniature electrical sparks every rotation. In a fuel-vapor atmosphere, this spark immediately causes a catastrophic hangar explosion.\n- **Pneumatic Superiority**: Compressed air motors produce **zero electrical sparks**, generate no thermal heat, and are 60% lighter than electric motors, eliminating technician muscle fatigue during overhead drilling inside fuselage wings."
                        }
                    }
                ],
                # Card 9: Formative Knowledge Check 1
                [
                    {
                        "type": "knowledge_check",
                        "title": "Formative Check: Pneumatic Tool Safety in Hangars",
                        "content": {
                            "question": "Why are pneumatic (compressed air) power tools universally preferred over electric power tools in aircraft maintenance hangars?",
                            "options": [
                                "Pneumatic tools are disposable and cost less than common hardware nails.",
                                "Pneumatic motors contain no electrical circuits or carbon brushes and cannot generate sparks, eliminating the risk of igniting volatile fuel vapors in the hangar atmosphere.",
                                "Electric tools are restricted because their cables interfere with ground weather radars.",
                                "Pneumatic tools are much heavier, which helps technicians force drills through hardened steel without motors."
                            ],
                            "answer": "B",
                            "explanation": "Aviation maintenance hangars frequently contain volatile fuel vapors and cleaning solvents. Standard electric tools generate internal sparks at commutator brushes, creating severe explosion risks. Air-powered pneumatic tools are spark-free, cool-running, and significantly lighter for overhead operations."
                        }
                    }
                ],
                # Card 10: Formative Knowledge Check 2
                [
                    {
                        "type": "knowledge_check",
                        "title": "Formative Check: Prohibited Marking Practices",
                        "content": {
                            "question": "Why is an aircraft technician strictly forbidden from using a hardened steel scribe to scratch layout lines onto structural aluminum alloy sheets?",
                            "options": [
                                "The scribe scratch creates a sharp microscopic groove (stress riser) that removes protective Alclad and rapidly propagates into a catastrophic fatigue crack under cyclic flight vibrations.",
                                "The steel tip melts the aluminum surface through spontaneous chemical friction.",
                                "Scribes are magnetized tools that instantly invert aircraft artificial horizon flight instruments.",
                                "Scribe marks are completely invisible under ultraviolet inspection lighting."
                            ],
                            "answer": "A",
                            "explanation": "Scratching structural aluminum with a hardened steel scribe breaches the protective Alclad pure-aluminum cladding and forms a sharp surface notch known as a stress riser. Under cyclic flight pressurization and aerodynamic turbulence, tensile stress concentrates at the scratch root, leading to rapid structural fatigue failure."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 5: Safety Precautions, Maintenance, and Tool Care (Unit Order 4)
        # =====================================================================
        {
            "unit_order": 4,
            "unit_name": "Safety Precautions, Maintenance, and Tool Care",
            "unit_description": "Master Foreign Object Debris (FOD) prevention, tool control shadow drawers, torque wrench spring calibration, and systematic tool inspection protocols.",
            "lesson_title": "Safety Precautions, Maintenance, and Tool Care",
            "pages": [
                # Card 1: Visual Hook & Learning Objectives
                [
                    {
                        "type": "suggested_image",
                        "title": "Aviation Maintenance Technician Testing a Torque Wrench",
                        "content": {
                            "title": "Aviation Maintenance Technician Testing a Torque Wrench",
                            "caption": "An aviation maintenance technician conducting calibration testing and inspection of a precision torque wrench in an aircraft intermediate maintenance department hangar.",
                            "resolved_image_url": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Aircraft_Electronics_Technician_2nd_Class_Roberts_tests_a_torque_wrench_in_the_Aircraft_Intermediate_Maintenance_Department_hangar_-_DPLA_-_0689b07c7fece7f80dfae7c80bf1f3ba.jpeg"
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Learning Focus: Safety Precautions, Maintenance, and Tool Care",
                        "content": {
                            "title": "Learning Focus: Tool Accountability and Calibration",
                            "goals": [
                                "Identify Foreign Object Debris (FOD) hazards and trace how forgotten tools cause flight disasters.",
                                "Implement 100% Tool Control using two-color high-contrast shadow boards and foam drawers.",
                                "Master the storage protocol for torque wrenches to preserve internal spring calibration.",
                                "Execute routine tool cleaning, lubrication, quarantine, and certified calibration procedures."
                            ]
                        }
                    }
                ],
                # Card 2: Foundational Terminology
                [
                    {
                        "type": "definition_card",
                        "title": "Core Tool Care and Safety Vocabulary",
                        "content": {
                            "title": "Core Technical Vocabulary",
                            "definitions": [
                                {
                                    "term": "Foreign Object Debris (FOD)",
                                    "definition": "Any loose item, hardware scrap, rag, or forgotten tool left inside an aircraft structure or operational area that can damage equipment or cause flight failure.",
                                    "example": "A forgotten 1/4-inch drive socket rolling under flight control rudder pulleys."
                                },
                                {
                                    "term": "Shadow Board / Drawer",
                                    "definition": "A visual tool management system utilizing customized, contrasting two-color foam cutouts where each tool has a single designated slot, revealing missing tools instantly.",
                                    "example": "A black foam top layer over high-visibility neon yellow foam in an aircraft mechanic's toolbox."
                                },
                                {
                                    "term": "Tool Calibration",
                                    "definition": "The formal laboratory process of verifying and adjusting measuring instruments or torque devices against certified national measurement standards.",
                                    "example": "Sending micrometer sets to an accredited metrology lab every twelve months."
                                },
                                {
                                    "term": "Torque Wrench Creep",
                                    "definition": "Permanent mechanical relaxation and loss of calibration elasticity that occurs when a micrometer torque wrench is stored under high spring compression.",
                                    "example": "A torque wrench reading 20% below actual torque after being stored compressed at 80 ft-lbs."
                                },
                                {
                                    "term": "Tool Quarantine",
                                    "definition": "The immediate isolation of a cracked, damaged, or uncalibrated tool into a locked red disposal box to prevent accidental use on airframes.",
                                    "example": "Quarantining an air drill with a bent chuck until certified repair or replacement."
                                }
                            ]
                        }
                    }
                ],
                # Card 3: The Danger of FOD in Flight
                [
                    {
                        "type": "concept_explanation",
                        "title": "Foreign Object Debris: The Deadly Consequences",
                        "content": {
                            "title": "How a Single Forgotten Tool Destroys an Aircraft",
                            "text": "In aviation, a misplaced tool is never merely an inconvenience; it is a life-threatening structural hazard:\n\n- **Flight Control Jams**: Aircraft flight surfaces (ailerons, elevators, rudders) are actuated by stainless steel control cables running through internal pulleys. A small screwdriver forgotten in the empennage can slide into a pulley bracket during turbulence, jamming the elevator and rendering the aircraft unpitchable.\n- **Jet Engine Compressor Destruction**: A forgotten bolt or wrench left on an engine cowl can be ingested into the jet intake at takeoff. At 10,000 RPM, the hard steel tool shatters titanium turbine blades, triggering catastrophic uncontained engine failure and structural fire.\n- **Electrical Short Circuits**: Metal tools falling across 115V AC aircraft electrical buses cause immediate wire arc burning, cockpit instrument blackout, and in-flight cabin fires."
                        }
                    }
                ],
                # Card 4: Technical Diagram Blueprint
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Aviation Tool Control Shadow Drawer and Sign-Off Workflow",
                        "content": {
                            "title": "Hangar Tool Control & Shadow Board Blueprint",
                            "caption": "Architectural diagram showing a high-contrast shadow foam drawer with a missing tool alert flag alongside the 5-step maintenance sign-off procedure."
                        }
                    }
                ],
                # Card 5: Tool Care and Maintenance Protocol Table
                [
                    {
                        "type": "comparison_table",
                        "title": "Maintenance Protocols: Aviation Tool Care Schedule",
                        "content": {
                            "title": "Aviation Tool Maintenance and Care Matrix",
                            "headers": ["Tool Category", "Preventive Maintenance Task", "Correct Storage Protocol", "Calibration Requirement"],
                            "rows": [
                                ["Torque Wrenches", "Wipe down with dry lint-free cloth; inspect drive tang for rounding", "Always dial internal micrometer spring back to lowest scale mark", "Mandatory annual lab recalibration; valid calibration sticker attached"],
                                ["Calipers & Micrometers", "Clean ground measuring faces; apply thin film of non-gumming oil", "Store in form-fitting velvet-lined hard cases; jaws slightly open", "Verify zero datum before each shift; annual certified gauge block verification"],
                                ["Aviation Snips & Cutters", "Clean off metal shavings; oil pivot hinge pin weekly", "Store closed with safety locking catch engaged in shadowed drawer", "Sharpen or replace when blades develop microscopic chips or burrs"],
                                ["Pneumatic Drills & Riveters", "Add 2-3 drops of pneumatic tool oil into air inlet nipple daily", "Hang on dedicated air tool racks or store in shadowed pneumatic drawers", "Verify air motor RPM and regulator pressure setting monthly"],
                                ["Files & Cutting Broaches", "Clean metal swarf from teeth using a brass file card wire brush", "Store in individual protective sleeves; never pile metal-on-metal", "Inspect cutting face regularly; scrap when teeth become dull or rounded"]
                            ]
                        }
                    }
                ],
                # Card 6: Real-World Industry Application
                [
                    {
                        "type": "real_world_example",
                        "title": "100% Digital Tool Accountability at Kenya Airways",
                        "content": {
                            "title": "Strict Tool Management Protocols in Modern Hangars",
                            "text": "At the **Kenya Airways Technical Engineering Base** at JKIA Nairobi, tool control is monitored under automated oversight:\n\n- **Digital Check-Out**: Every mechanic holds an electronic badge that unlocks their allocated mobile tool chest. Every individual tool features an engraved serial number and laser barcode.\n- **Contrasting Shadow Foam**: Every drawer uses two-color foam: a black upper layer and a neon red or yellow base. If a single 1/2-inch socket is missing, the bright red background stands out immediately from across the hangar bay.\n- **The Golden Release Rule**: Before the Chief Inspector signs the final Certificate of Release to Service (CRS), the mechanic must scan every drawer. If one slot remains vacant, the aircraft is grounded, and maintenance teams conduct a full systematic search until the tool is accounted for."
                        }
                    }
                ],
                # Card 7: Educational Video Integration
                [
                    {
                        "type": "suggested_video",
                        "title": "The Human Factors in Aircraft Maintenance",
                        "content": {
                            "title": "Human Factors and Error Prevention in Aviation Maintenance",
                            "description": "Exploration of cognitive fatigue, rushing, and procedural discipline in aviation maintenance hangars, illustrating how tool control checklists prevent accidents.",
                            "url": "https://www.youtube.com/watch?v=FViSA91DP-8"
                        }
                    }
                ],
                # Card 8: Safety Connection & Torque Calibration Hazards
                [
                    {
                        "type": "concept_explanation",
                        "title": "Torque Wrench Spring Creep and Structural Danger",
                        "content": {
                            "title": "The Critical Science of Torque Wrench Unloading",
                            "text": "Consider a maintenance technician torquing critical cylinder head bolts to 75 ft-lbs who throws the wrench back into their locker without adjusting the dial:\n\n- **Spring Creep**: The internal calibrated steel spring remains under intense mechanical compression. Over days in storage, the steel crystal lattice undergoes microscopic relaxation (creep).\n- **Loss of Calibration**: When next used, the relaxed spring clicks prematurely at only 55 ft-lbs even though the barrel scale indicates 75 ft-lbs.\n- **Flight Catastrophe**: The engine cylinder head bolts remain under-torqued. Under combustion pressures and engine vibration, the bolts back out, blowing the cylinder head off the engine block in flight.\n- **Mandatory Golden Rule**: Technicians must always wind the torque wrench adjustment sleeve down to its lowest graduation mark before storage, fully relieving internal spring tension."
                        }
                    }
                ],
                # Card 9: Formative Knowledge Check 1
                [
                    {
                        "type": "knowledge_check",
                        "title": "Formative Check: Purpose of Shadow Tool Boards",
                        "content": {
                            "question": "What is the primary flight safety purpose of utilizing contrasting two-color foam shadow drawers in aviation maintenance toolboxes?",
                            "options": [
                                "To keep the metal tools warm during high-altitude freezing weather conditions.",
                                "To allow technicians and inspectors to instantly detect any missing tool at the conclusion of a maintenance shift, preventing tools from being abandoned inside the airframe as Foreign Object Debris (FOD).",
                                "To prevent tools from becoming magnetized by runway navigation instruments.",
                                "To weigh the tools automatically before and after each flight."
                            ],
                            "answer": "B",
                            "explanation": "A forgotten tool left inside an aircraft engine bay or control run can jam flight controls or destroy spinning turbines. Shadow drawers utilize form-fitting slots with contrasting bright foam underneath, making an absent tool instantly visible so the aircraft is grounded until the tool is located."
                        }
                    }
                ],
                # Card 10: Formative Knowledge Check 2
                [
                    {
                        "type": "knowledge_check",
                        "title": "Formative Check: Torque Wrench Storage Protocol",
                        "content": {
                            "question": "Why must an aircraft mechanic always wind a micrometer torque wrench back to its lowest graduation mark prior to storing it?",
                            "options": [
                                "To allow the internal hydraulic fluid to drain out into the toolbox reservoir.",
                                "To relieve mechanical tension on the internal calibrated spring, preventing spring creep and permanent loss of measurement accuracy on future critical engine assemblies.",
                                "To make the torque wrench significantly lighter and easier to transport across the tarmac.",
                                "To prevent the hardened ratchet drive handle from falling off the tool body."
                            ],
                            "answer": "B",
                            "explanation": "Micrometer torque wrenches measure torque via a precision calibrated internal spring. If stored under high tension, the steel spring undergoes permanent microscopic relaxation (creep). This alters the spring constant, causing future torque readings to be dangerously inaccurate and leading to under-torqued engine components."
                        }
                    }
                ]
            ]
        }
    ]

def ingest_grade10_aviation_topic363(replace: bool = True):
    """Ingests Grade 10 Aviation Topic 363 with 5 Lessons and 50 Concept Cards."""
    print("=" * 80)
    print("VLearn Production Ingestion: Grade 10 Aviation — Topic 363")
    print("Topic: Aircraft Tools and Materials")
    print("=" * 80)

    curriculum_data = build_topic363_curriculum()

    with transaction.atomic():
        subject = Subject.objects.get(id=44)
        topic = Topic.objects.get(id=363, subject=subject)

        print(f"[*] Target Subject: {subject.name} (ID: {subject.id})")
        print(f"[*] Target Topic:   {topic.name} (ID: {topic.id}, Order: {topic.order})")

        total_lessons = 0
        total_pages = 0
        total_blocks = 0

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
    print("[SUCCESS] Grade 10 Aviation Topic 363 Ingestion Complete!")
    print(f"[*] Total Lessons Ingested: {total_lessons}")
    print(f"[*] Total Pages/Cards:      {total_pages}")
    print(f"[*] Total Blocks Created:   {total_blocks}")
    print("=" * 80)

if __name__ == "__main__":
    replace_flag = "--replace" in sys.argv
    ingest_grade10_aviation_topic363(replace=replace_flag)
