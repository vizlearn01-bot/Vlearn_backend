"""
VLearn Form 4 Geography — Topic 4: Energy
High-Structure Production Ingestion Engine

Topic: Energy (Topic Order: 4)
Subject: Geography (Subject ID: 18)
Grade: Form 4 (Grade ID: 4)
Curriculum: 844 (Curriculum ID: 4)

Decomposed into 6 Learning Units & 6 Published Lessons (80 Total Pages):
  1. Classification and Renewable Energy Resources (12 Pages)
  2. Biomass, Animal Power, and Non-Renewable Fossil Energy (12 Pages)
  3. Site-Selection Factors & Hydroelectric Development in East Africa (14 Pages)
  4. Geothermal Power Potential in the Kenyan Rift Valley (12 Pages)
  5. The Global Energy/Oil Crisis: Causes, Case Studies, and Impacts (14 Pages)
  6. Energy Management, Conservation Strategies, and KCSE Synthesis (16 Pages)

Usage:
  ./venv/bin/python curriculum/ingest_form4_geography_topic4.py [--replace]
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
    """Removes bracket citations [36], [41], [49] and cleans double spaces."""
    if not text:
        return ""
    text = re.sub(r'\[(?:\d+|image_\d+|S\d+.*?|[\d,\s]+)\]', '', text)
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

def build_topic4_curriculum():
    """Returns the comprehensive pedagogical page and block structure for Topic 4."""
    return [
        # =====================================================================
        # LESSON 1: Classification and Renewable Energy Resources
        # =====================================================================
        {
            "unit_order": 1,
            "unit_name": "Classification and Renewable Energy Resources",
            "unit_description": "Foundational energy classifications, principles of solar, wind, geothermal, hydroelectric, and marine energy systems.",
            "lesson_title": "Classification and Renewable Energy Resources",
            "pages": [
                # Page 1
                [
                    {
                        "type": "learning_goal",
                        "title": "Learning Objectives: Energy Classification & Renewables",
                        "content": {
                            "title": "Learning Objectives: Energy Classification & Renewables",
                            "goals": [
                                "Define energy and distinguish between renewable and non-renewable energy resources.",
                                "Analyze solar thermal collectors vs photovoltaic electrical generation.",
                                "Examine wind energy conversion, mechanical windmills, and maritime dhow transport.",
                                "Evaluate geothermal steam extraction and hydroelectric power generation principles."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Welcome to Topic 4: Energy",
                        "content": {
                            "title": "Welcome to Topic 4: Energy",
                            "text": "Energy is defined as the fundamental power required to carry out physical, mechanical, or biological work—from domestic lighting to industrial manufacturing. Energy resources are classified into two primary categories: Renewable (inexhaustible or continuously replenished) and Non-Renewable (finite geological deposits that exhaust upon consumption)."
                        }
                    }
                ],
                # Page 2
                [
                    {
                        "type": "definition_card",
                        "title": "Geographical Classification of Energy Resources",
                        "content": {
                            "term": "Renewable vs Non-Renewable Energy",
                            "definition": "Renewable energy resources naturally regenerate and recycle continuously without depletion, whereas Non-Renewable energy resources exist in finite geological quantities that deplete permanently through use.",
                            "key_points": [
                                "Renewable Sources: Solar, Wind, Geothermal, Hydroelectric (HEP), Waves/Tides, Biomass, Animal Power.",
                                "Non-Renewable Sources: Coal, Petroleum (Crude Oil), Natural Gas, Uranium (Nuclear Fuel).",
                                "Sustainability Imperative: Transitioning to renewable energy mitigates global climate change and reduces import debt."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Energy as a Production Catalyst",
                        "content": {
                            "title": "Energy as a Production Catalyst",
                            "text": "In industrial geography, energy serves as the essential catalyst that transforms raw agricultural and mineral inputs into manufactured consumer goods. Access to cheap, reliable power directly determines a nation's level of economic development."
                        }
                    }
                ],
                # Page 3
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Solar Photovoltaic vs Thermal Collector Engineering",
                        "content": {
                            "title": "Solar Photovoltaic vs Thermal Collector Engineering",
                            "caption": "Engineering Comparison of Solar Thermal Water-Heating Panels and Semiconductor Photovoltaic Electrical Generation",
                            "description": "Diagram contrasting black coiled pipe solar thermal collectors with silicon semiconductor photovoltaic (PV) cells charging chemical storage batteries."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Solar Energy Harvesting Technologies",
                        "content": {
                            "title": "Solar Energy Harvesting Technologies",
                            "text": "The sun is the ultimate source of virtually all energy on Earth. Solar energy is tapped via two distinct technologies:\n\n1. Thermal (Heat) Energy: Solar collector panels feature black-painted coiled pipes through which water circulates and absorbs solar heat. Concentrating mirrors also focus solar rays directly onto crop driers and solar cookers.\n\n2. Electrical Energy: Photovoltaic (PV) cells made of silicon semiconductors absorb photons, releasing electrons to generate direct electric current stored in chemical batteries for night-time domestic lighting."
                        }
                    }
                ],
                # Page 4
                [
                    {
                        "type": "concept_explanation",
                        "title": "Trade-Offs of Solar Energy Adoption",
                        "content": {
                            "title": "Trade-Offs of Solar Energy Adoption",
                            "text": "• Advantages: Infinite and free raw resource; zero atmospheric carbon emissions; minimal maintenance after installation; storable in batteries for off-grid rural lighting.\n\n• Limitations: High initial capital outlay for panels and inverter systems; low power density (cannot run heavy industrial machinery directly); intermittent supply during overcast weather and night hours; battery disposal hazards."
                        }
                    },
                    {
                        "type": "callout",
                        "title": "Geographical Advantage: Kenya's Equatorial Solar Potential",
                        "content": {
                            "type": "tip",
                            "title": "Geographical Advantage: Kenya's Equatorial Solar Potential",
                            "text": "Kenya's location on the Equator guarantees over 300 days of high solar radiation annually, making off-grid solar kits highly effective for rural household electrification."
                        }
                    }
                ],
                # Page 5
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Kinetic Energy Conversion in Wind Turbine Generators",
                        "content": {
                            "title": "Kinetic Energy Conversion in Wind Turbine Generators",
                            "caption": "Mechanical Aerodynamics of Windmills and High-Capacity Wind Turbine Electrical Generators",
                            "description": "Visual diagram showing wind flow rotating aerodynamic turbine blades, driving a high-speed shaft, gear box, electrical generator, and transformer substation."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Wind Power Aerodynamics",
                        "content": {
                            "title": "Wind Power Aerodynamics",
                            "text": "Wind power converts the kinetic energy of moving air masses into mechanical power (for pumping borehole water or grinding grain) or grid electricity (via wind turbine generators). Wind energy is most viable in unobstructed semi-arid plains, mountain passes (e.g., Ngong Hills), and coastal corridors."
                        }
                    }
                ],
                # Page 6
                [
                    {
                        "type": "suggested_image",
                        "title": "Commercial Solar Installation in Kenya",
                        "content": {
                            "title": "Commercial Solar Installation in Kenya",
                            "caption": "Rooftop photovoltaic (PV) solar panel installation delivering clean renewable power to rural facilities in Kenya.",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/7/7a/Solar_Installation_in_Kenya.jpg",
                            "author": "PowerAfricaSolar, Wikimedia Commons",
                            "licensing": "CC BY-SA 4.0",
                            "commons_page_url": "https://commons.wikimedia.org/wiki/File:Solar_Installation_in_Kenya.jpg"
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Off-Grid Solar Electrification in Kenya",
                        "content": {
                            "title": "Off-Grid Solar Electrification in Kenya",
                            "text": "Pay-as-you-go solar technology has enabled millions of rural Kenyan households to bypass expensive grid extension costs, replacing dangerous kerosene tin lamps with clean LED lighting, phone charging, and television entertainment."
                        }
                    }
                ],
                # Page 7
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Geothermal Power Generation Mechanism Harnessing Volcanic Steam at Olkaria",
                        "content": {
                            "title": "Geothermal Power Generation Mechanism Harnessing Volcanic Steam at Olkaria",
                            "caption": "Subsurface Hydrothermal Circulation: Magmatic Heat, Deep Borehole Steam Extraction, and Surface Turbine Generators",
                            "description": "Cross-section showing rainwater seeping through rock fissures to contact superheated magma, flashing into high-pressure steam, rising via steel-cased boreholes to spin electrical turbines."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Geothermal Steam Harvesting Mechanics",
                        "content": {
                            "title": "Geothermal Steam Harvesting Mechanics",
                            "text": "Geothermal power harnesses underground volcanic heat. Surface rainwater percolates deep into Rift Valley fault lines, coming into contact with superheated magmatic rocks. The water flashes into high-pressure steam (>300°C), which is piped via deep drilled wells to drive heavy steam turbines at stations like Olkaria."
                        }
                    }
                ],
                # Page 8
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Operational Mechanics of Hydroelectric Power (HEP) Generation",
                        "content": {
                            "title": "Operational Mechanics of Hydroelectric Power (HEP) Generation",
                            "caption": "Hydraulic Blueprint of an Dam Station: Reservoir Storage, Penstock Intake, Water Turbine, and High-Voltage Grid Lines",
                            "description": "Engineering cross-section showing concrete dam wall, deep reservoir, control gate, inclined penstock pipe, Francis/Kaplan water turbine, electrical generator, and tailrace outlet."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Hydroelectric Power (HEP) Principles",
                        "content": {
                            "title": "Hydroelectric Power (HEP) Principles",
                            "text": "HEP converts the potential and kinetic energy of falling river water into electricity. A massive concrete dam impounds a river to create a high-head reservoir. Water is released through inclined penstock pipes under immense gravitational pressure to spin water turbines connected to high-voltage grid generators."
                        }
                    }
                ],
                # Page 9
                [
                    {
                        "type": "concept_explanation",
                        "title": "Tides and Wave Energy Barrages",
                        "content": {
                            "title": "Tides and Wave Energy Barrages",
                            "text": "Marine renewable energy taps the gravitational pull of the moon and sun (tides) and surface wind friction (ocean waves). Tidal barrages built across narrow coastal estuaries feature bidirectional water turbines that spin as rising high tides enter and falling low tides recede."
                        }
                    }
                ],
                # Page 10
                [
                    {
                        "type": "mini_activity",
                        "title": "Interactive Renewable Energy Selection Challenge",
                        "content": {
                            "activity_type": "scenario_decision",
                            "title": "Interactive Renewable Energy Selection Challenge",
                            "prompt": "A semi-arid school in Machakos with abundant sunshine and an adjacent cattle market requires power for evening study and pumping borehole water. Which combination is most viable?",
                            "options": [
                                "Option A: Solar Photovoltaic Panels for lighting + Biogas Digester using cattle manure for pumping.",
                                "Option B: Geothermal Steam Well + Coastal Wave Barrage.",
                                "Option C: Nuclear Reactor Core + Coal Blast Furnace."
                            ],
                            "correct_option": "Option A: Solar Photovoltaic Panels for lighting + Biogas Digester using cattle manure for pumping.",
                            "explanation": "Semi-arid Machakos has exceptional solar radiation for PV lighting, and local cattle manure feeds a low-cost biogas digester. Geothermal requires volcanic rift structures, and wave barrages require ocean estuaries."
                        }
                    }
                ],
                # Page 11
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Checkpoint: Renewable Energy Resources",
                        "content": {
                            "question": "What primary physical advantage makes geothermal power more reliable for Kenya's national grid during a severe drought compared to HEP?",
                            "options": [
                                "Geothermal steam is generated continuously by magmatic heat deep underground, completely unaffected by surface rainfall or reservoir levels.",
                                "Geothermal plants require no steel piping or turbines.",
                                "Geothermal power can only be generated at night when temperatures drop.",
                                "Geothermal energy is harvested directly from ocean waves."
                            ],
                            "correct_answer": 0,
                            "explanation": "Geothermal energy taps deep magmatic heat below the water table, providing continuous, drought-resistant base-load power regardless of surface rainfall."
                        }
                    }
                ],
                # Page 12
                [
                    {
                        "type": "summary",
                        "title": "Renewable Energy: Key Takeaways",
                        "content": {
                            "title": "Renewable Energy: Key Takeaways",
                            "summary_points": [
                                "Energy is classified into Renewable (inexhaustible/replenished) and Non-Renewable (finite/exhaustible).",
                                "Solar energy is harvested via thermal heat collectors (coiled black pipes) and photovoltaic semiconductor cells.",
                                "Wind energy converts kinetic air movement into mechanical or electrical power.",
                                "Geothermal power pipes magmatic high-pressure steam from deep volcanic fissures (Olkaria).",
                                "HEP converts falling water kinetic energy into grid electricity via dam penstocks and water turbines."
                            ]
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 2: Biomass, Animal Power, and Non-Renewable Fossil Energy
        # =====================================================================
        {
            "unit_order": 2,
            "unit_name": "Biomass, Animal Power, and Non-Renewable Fossil Energy",
            "unit_description": "Biomass forms (wood fuel, power alcohol, biogas), animal power, and geological formation of coal, petroleum, natural gas, and nuclear uranium.",
            "lesson_title": "Biomass, Animal Power, and Non-Renewable Fossil Energy",
            "pages": [
                # Page 1
                [
                    {
                        "type": "learning_goal",
                        "title": "Learning Objectives: Biomass & Non-Renewables",
                        "content": {
                            "title": "Learning Objectives: Biomass & Non-Renewables",
                            "goals": [
                                "Evaluate wood fuel overexploitation and deforestation risks in developing nations.",
                                "Examine the bio-energy production of power alcohol and biogas (methane).",
                                "Trace the geological formation of coal, petroleum, and natural gas strata.",
                                "Analyze fractional distillation by-products and nuclear fission energy trade-offs."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Biomass and Exhaustible Fossil Energy",
                        "content": {
                            "title": "Biomass and Exhaustible Fossil Energy",
                            "text": "Biomass encompasses all energy derived from plant and animal organic matter. While biomass can be sustainably renewed through afforestation, non-renewable fossil fuels (coal, petroleum, natural gas, uranium) represent finite geological deposits laid down over millions of years."
                        }
                    }
                ],
                # Page 2
                [
                    {
                        "type": "concept_explanation",
                        "title": "Wood Fuel and Deforestation Threats",
                        "content": {
                            "title": "Wood Fuel and Deforestation Threats",
                            "text": "Wood fuel (firewood, charcoal, sawdust) is the primary domestic energy source for over 80% of rural African households:\n\n• Deforestation Crisis: Wood fuel is only renewable if consumption is balanced by aggressive tree planting. Over-cutting leads to deforestation, accelerated soil erosion, water tower destruction, and desertification.\n\n• Bio-Fuels (Power Alcohol): Fermenting sugarcane molasses, corn, or cassava produces bio-ethanol, which is blended with petrol (gasohol) to power motor vehicles."
                        }
                    },
                    {
                        "type": "callout",
                        "title": "Environmental Warning: Charcoal Burning",
                        "content": {
                            "type": "warning",
                            "title": "Environmental Warning: Charcoal Burning",
                            "text": "Traditional earth-kiln charcoal burning converts only 15% of wood biomass into usable energy, wasting 85% of wood volume and driving severe forest destruction in dry woodlands."
                        }
                    }
                ],
                # Page 3
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Biogas Anaerobic Digester & Organic Fertilizer Nutrient Cycle",
                        "content": {
                            "title": "Biogas Anaerobic Digester & Organic Fertilizer Nutrient Cycle",
                            "caption": "Airtight Underground Anaerobic Fermentation of Livestock Waste Producing Methane Gas and Nitrogen-Rich Bio-Slurry",
                            "description": "Schematic blueprint showing manure mixing tank, airtight masonry digester dome, bio-gas pipe valve to kitchen stove, and bio-slurry overflow channel to agricultural fields."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Biogas (Methane) Technology",
                        "content": {
                            "title": "Biogas (Methane) Technology",
                            "text": "Biogas is generated by feeding human sewage and animal manure into an airtight anaerobic digester. Methanogenic bacteria decompose the waste in the absence of oxygen, releasing methane gas piped directly for domestic cooking. The leftover liquid slurry forms an exceptional nitrogen-rich organic fertilizer."
                        }
                    }
                ],
                # Page 4
                [
                    {
                        "type": "suggested_image",
                        "title": "Ngong Hills Wind Power Farm in Kenya",
                        "content": {
                            "title": "Ngong Hills Wind Power Farm in Kenya",
                            "caption": "High-capacity commercial wind turbines generating clean electrical power along the wind-swept Ngong Hills ridge near Nairobi.",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/7/72/Ngong_Hills_Wind_Farm.jpg",
                            "author": "Singularity Preparation, Wikimedia Commons",
                            "licensing": "CC BY-SA 4.0",
                            "commons_page_url": "https://commons.wikimedia.org/wiki/File:Ngong_Hills_Wind_Farm.jpg"
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Commercial Wind Power in Kenya",
                        "content": {
                            "title": "Commercial Wind Power in Kenya",
                            "text": "The Ngong Hills and Lake Turkana Wind Power (LTWP) projects feed clean kinetic energy directly into Kenya's national grid. LTWP in Marsabit is Africa's largest wind farm, utilizing steady desert wind corridors."
                        }
                    }
                ],
                # Page 5
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Draught Animal Harness Mechanics & Agricultural Work Rates",
                        "content": {
                            "title": "Draught Animal Harness Mechanics & Agricultural Work Rates",
                            "caption": "Mechanical Harness Systems for Oxen Ploughing and Pack Donkey Transport in Rural Geography",
                            "description": "Diagram illustrating wooden neck yoke mechanics on draught oxen pulling mouldboard ploughs and pack saddle balancing on donkeys traversing rugged terrain."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Draught Animal Power in Rural Economies",
                        "content": {
                            "title": "Draught Animal Power in Rural Economies",
                            "text": "Domesticated animals (oxen, donkeys, camels) provide indispensable mechanical energy in rural agriculture and transport. Oxen pull ploughs and weeding carts, while camels and donkeys carry grain loads across steep, unpaved rural tracks inaccessible to motor vehicles."
                        }
                    }
                ],
                # Page 6
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Geological Coal Formation Process Flow: Swamps to Carboniferous Strata",
                        "content": {
                            "title": "Geological Coal Formation Process Flow: Swamps to Carboniferous Strata",
                            "caption": "Four-Stage Geological Evolution of Ancient Organic Plant Matter into Compacted High-Carbon Coal Seams",
                            "description": "Geological timeline showing 1. Ancient swamp vegetation; 2. Anoxic sediment burial; 3. Compaction into Peat & Lignite; 4. Immense heat/pressure forming Anthracite coal seams."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Geological Coal Formation & Industrial Smelting",
                        "content": {
                            "title": "Geological Coal Formation & Industrial Smelting",
                            "text": "Coal is a dark carbonaceous sedimentary rock formed from ancient forest matter buried under heavy clay and mud deposits millions of years ago. Intense heat and overburden pressure drive out oxygen and moisture, concentrating carbon (Anthracite). Coal is the vital reducing agent and heat source in blast furnace iron smelting."
                        }
                    }
                ],
                # Page 7
                [
                    {
                        "type": "suggested_image",
                        "title": "Open Pit Coal Mining Operations",
                        "content": {
                            "title": "Open Pit Coal Mining Operations",
                            "caption": "Massive open-pit coal extraction displaying heavy machinery excavating high-carbon coal seams.",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/d/da/TurowCoalMine.jpg",
                            "author": "Wikimedia Commons",
                            "licensing": "CC BY-SA 4.0",
                            "commons_page_url": "https://commons.wikimedia.org/wiki/File:TurowCoalMine.jpg"
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Environmental Impacts of Coal Mining",
                        "content": {
                            "title": "Environmental Impacts of Coal Mining",
                            "text": "Coal extraction triggers severe environmental degradation, including open-pit landscape scarring, acid mine drainage contaminating water tables, and high sulphur dioxide emissions causing destructive acid rain."
                        }
                    }
                ],
                # Page 8
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Petroleum & Natural Gas Geological Trap & Fractional Distillation Column",
                        "content": {
                            "title": "Petroleum & Natural Gas Geological Trap & Fractional Distillation Column",
                            "caption": "Subsurface Anticlinal Trap Geology and Refinery Fractional Distillation Boiling-Point Separation",
                            "description": "Left: Anticlinal rock fold trapping Natural Gas above Petroleum over Water. Right: Fractional distillation column separating crude oil into LPG, Petrol, Kerosene, Diesel, Lubricants, Bitumen."
                        }
                    },
                    {
                        "type": "definition_card",
                        "title": "Petroleum Fractional Distillation By-Products",
                        "content": {
                            "term": "Petroleum Refining",
                            "definition": "The industrial process of heating crude oil in a fractional distillation column to separate hydrocarbons into distinct products based on boiling point.",
                            "key_points": [
                                "Light Fractions (<100°C): Refinery gas, Liquid Petroleum Gas (LPG), Gasoline (Petrol).",
                                "Medium Fractions (150–300°C): Aviation Jet Fuel, Kerosene (Paraffin), Diesel Oil.",
                                "Heavy Residuals (>350°C): Heavy Fuel Oil, Lubricating Engine Oils, Paraffin Wax, Bitumen (Asphalt)."
                            ]
                        }
                    }
                ],
                # Page 9
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Nuclear Power Reactor Fission & Thermal Exchange System",
                        "content": {
                            "title": "Nuclear Power Reactor Fission & Thermal Exchange System",
                            "caption": "Nuclear Fission Energy: Reactor Core, Control Rods, Pressurized Water Coolant Loop, and Steam Turbine Generator",
                            "description": "Engineering schematic of nuclear reactor core containing Uranium fuel rods, boron control rods, primary pressurized water loop, heat exchanger steam generator, turbine, and cooling tower."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Uranium & Nuclear Fission Energy",
                        "content": {
                            "title": "Uranium & Nuclear Fission Energy",
                            "text": "Nuclear power is generated by splitting heavy Uranium-235 atomic nuclei (fission) inside a fortified reactor core. The immense heat released boils water into steam that spins high-output electrical turbines. While nuclear power produces zero carbon emissions during operation, storing radioactive nuclear waste for thousands of years presents grave environmental challenges."
                        }
                    }
                ],
                # Page 10
                [
                    {
                        "type": "mini_activity",
                        "title": "Interactive Energy Classification Matrix",
                        "content": {
                            "activity_type": "matching_challenge",
                            "title": "Interactive Energy Classification Matrix",
                            "prompt": "Classify each energy source as Renewable or Non-Renewable:\n1. Biogas (Methane) tapped from livestock digesters.\n2. Anthracite Coal excavated from deep sedimentary seams.\n3. Uranium-235 heavy metal used in nuclear reactors.",
                            "options": [
                                "Option A: 1-Renewable, 2-Non-Renewable, 3-Non-Renewable",
                                "Option B: 1-Non-Renewable, 2-Renewable, 3-Renewable",
                                "Option C: 1-Renewable, 2-Renewable, 3-Non-Renewable"
                            ],
                            "correct_option": "Option A: 1-Renewable, 2-Non-Renewable, 3-Non-Renewable",
                            "explanation": "Biogas continuously naturally regenerates from biological wastes (Renewable). Coal and Uranium exist in finite, exhaustible geological reserves (Non-Renewable)."
                        }
                    }
                ],
                # Page 11
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Checkpoint: Non-Renewable Energy",
                        "content": {
                            "question": "Which petroleum refinement product is collected at the lowest temperature at the top of a fractional distillation column?",
                            "options": [
                                "Heavy Bitumen (Asphalt)",
                                "Liquid Petroleum Gas (LPG) and Gasoline",
                                "Lubricating Engine Oil",
                                "Industrial Kerosene"
                            ],
                            "correct_answer": 1,
                            "explanation": "Light hydrocarbon gases (LPG) and petrol have the lowest boiling points and vaporize to condense at the top of the distillation column."
                        }
                    }
                ],
                # Page 12
                [
                    {
                        "type": "summary",
                        "title": "Fossil & Biomass Energy: Key Takeaways",
                        "content": {
                            "title": "Fossil & Biomass Energy: Key Takeaways",
                            "summary_points": [
                                "Wood fuel overexploitation causes severe deforestation, soil erosion, and water catchment loss.",
                                "Biogas digesters convert organic animal wastes into clean methane gas and nitrogen fertilizer slurry.",
                                "Coal forms from ancient swamp vegetation compacted under heavy sedimentary overburden.",
                                "Petroleum and natural gas occur in anticlinal rock traps and refine into petrol, diesel, kerosene, and LPG.",
                                "Nuclear fission of Uranium-235 provides high energy density with zero carbon emissions but creates radioactive waste hazards."
                            ]
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 3: Site-Selection Factors & Hydroelectric Development in East Africa
        # =====================================================================
        {
            "unit_order": 3,
            "unit_name": "Site-Selection Factors & Hydroelectric Development in East Africa",
            "unit_description": "Physical and human site-selection criteria for HEP dams, case study of the Seven Forks Scheme on River Tana, and African HEP projects.",
            "lesson_title": "Site-Selection Factors & Hydroelectric Development in East Africa",
            "pages": [
                # Page 1
                [
                    {
                        "type": "learning_goal",
                        "title": "Learning Objectives: HEP Site Selection & Projects",
                        "content": {
                            "title": "Learning Objectives: HEP Site Selection & Projects",
                            "goals": [
                                "Analyze the physical site-selection factors required for hydroelectric dam construction.",
                                "Examine the human and economic requirements for HEP development.",
                                "Trace the downstream dam cascade of the Seven Forks Scheme on River Tana.",
                                "Evaluate the multi-purpose benefits and environmental problems of the Seven Forks Scheme."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Hydroelectric Power Infrastructure",
                        "content": {
                            "title": "Hydroelectric Power Infrastructure",
                            "text": "Hydroelectric power (HEP) is the largest source of electricity in East Africa, accounting for over 70% of Kenya's domestic generation. Because dam construction requires billions of shillings, site selection demands rigorous geographical and hydrological analysis."
                        }
                    }
                ],
                # Page 2
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Physical Site-Selection Engineering Blueprint for a Hydroelectric Dam",
                        "content": {
                            "title": "Physical Site-Selection Engineering Blueprint for a Hydroelectric Dam",
                            "caption": "Engineering Blueprint Illustrating Ideal Topographical, Geological, and Hydrological Dam Conditions",
                            "description": "Annotated diagram showing steep waterfall gradient, deep narrow gorge, hard impervious basement bedrock, large river volume, and sparse population buffer."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Physical Site-Selection Criteria",
                        "content": {
                            "title": "Physical Site-Selection Criteria",
                            "text": "1. Large and Constant Water Volume: Permanent, high-discharge rivers (e.g., River Tana, River Nile) to ensure year-round generation.\n\n2. Steep Gradient (Rapids / Waterfalls): Steep elevation drops maximize kinetic energy to spin heavy water turbines.\n\n3. Deep and Narrow Valley:\n• Deep: Ensures massive reservoir water storage capacity.\n• Narrow: Reduces the horizontal concrete dam wall length, lowering construction costs.\n\n4. Hard and Impervious Basement Bedrock:\n• Hard: Provides a stable structural foundation for the massive weight of the concrete dam.\n• Impervious: Prevents water loss through underground seepage and infiltration."
                        }
                    }
                ],
                # Page 3
                [
                    {
                        "type": "concept_explanation",
                        "title": "Human and Economic Site-Selection Factors",
                        "content": {
                            "title": "Human and Economic Site-Selection Factors",
                            "text": "1. Sparse Population Density: Dam reservoirs submerge vast land areas. Sites must be sparsely populated to minimize human relocation and land compensation expenses.\n\n2. Proximity to Industrial & Urban Markets: High-voltage electricity must be transmitted to major urban centers (Nairobi, Thika) and factories to ensure commercial profitability.\n\n3. High Financial Capital: Construction requires immense capital for dam engineering, turbines, transmission lines, and compensation payments."
                        }
                    },
                    {
                        "type": "callout",
                        "title": "Geographical Insight: Seepage Prevention",
                        "content": {
                            "type": "tip",
                            "title": "Geographical Insight: Seepage Prevention",
                            "text": "Constructing a dam over porous, faulted limestone or sandstone causes water to seep underground, failing to build up the necessary hydraulic head."
                        }
                    }
                ],
                # Page 4
                [
                    {
                        "type": "suggested_image",
                        "title": "Akosombo Hydroelectric Dam Project",
                        "content": {
                            "title": "Akosombo Hydroelectric Dam Project",
                            "caption": "The massive Akosombo Hydroelectric Dam on the Volta River in Ghana, demonstrating large-scale African HEP infrastructure.",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/2/2d/Akosombo_Dam.jpg",
                            "author": "Public Domain, Wikimedia Commons",
                            "licensing": "Public domain",
                            "commons_page_url": "https://commons.wikimedia.org/wiki/File:Akosombo_Dam.jpg"
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "African Hydroelectric Engineering",
                        "content": {
                            "title": "African Hydroelectric Engineering",
                            "text": "Large African dams like Akosombo (Ghana), Owen Falls / Nalubaale (Uganda), and Masinga (Kenya) impound massive artificial lakes that power national industries while providing regional water storage."
                        }
                    }
                ],
                # Page 5
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Spatial Map of the River Tana Cascade: The Seven Forks Scheme",
                        "content": {
                            "title": "Spatial Map of the River Tana Cascade: The Seven Forks Scheme",
                            "caption": "Downstream Hydrological Spatial Sequence of the Five Dams along River Tana in Kenya",
                            "description": "Map displaying Mt. Kenya catchment, River Tana flow, Masinga Dam, Kamburu Dam, Gitaru Dam, Kindaruma Dam, Kiambere Dam, and proposed Mutonga/Grand Falls sites."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The Seven Forks Scheme Cascade Sequence",
                        "content": {
                            "title": "The Seven Forks Scheme Cascade Sequence",
                            "text": "River Tana, originating from the moist Mt. Kenya and Aberdare highlands, is Kenya's largest river. The Seven Forks Scheme consists of five interconnected HEP stations built in downstream sequence:\n\n1. Masinga Dam (1981): Upstream master reservoir.\n2. Kamburu Dam (1974).\n3. Gitaru Dam (1978).\n4. Kindaruma Dam (1968): The pioneer station.\n5. Kiambere Dam (1988): Downstream station."
                        }
                    }
                ],
                # Page 6
                [
                    {
                        "type": "concept_explanation",
                        "title": "Evolution of Kenyan Power Generation",
                        "content": {
                            "title": "Evolution of Kenyan Power Generation",
                            "text": "Prior to the Seven Forks Scheme, Kenya relied on minor run-of-the-river stations (Mesco on River Maragua, Ndula on River Thika), thermal diesel generators at Kipevu, and imported electricity from Uganda's Owen Falls Dam (connected in 1955). The Seven Forks development secured national energy self-reliance."
                        }
                    }
                ],
                # Page 7
                [
                    {
                        "type": "concept_explanation",
                        "title": "Masinga Dam: The Master Regulator",
                        "content": {
                            "title": "Masinga Dam: The Master Regulator",
                            "text": "Masinga Dam is the critical centerpiece of the Seven Forks Scheme:\n\n• Hydraulic Regulation: It has the largest reservoir surface area (Lake Masinga). During heavy rains, it impounds floodwaters; during dry seasons, it releases regulated water to keep all four downstream stations (Kamburu, Gitaru, Kindaruma, Kiambere) generating power continuous.\n\n• Multi-Purpose Value: Supports commercial inland fisheries, provides water for Mwea rice irrigation, offers tourist recreation at Masinga Lodge, and acts as a highway bridge across River Tana."
                        }
                    }
                ],
                # Page 8
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Masinga Reservoir Multi-Purpose Hydrological Flow Control",
                        "content": {
                            "title": "Masinga Reservoir Multi-Purpose Hydrological Flow Control",
                            "caption": "Hydrological Balance: Wet-Season Storage vs Regulated Dry-Season Discharge to Downstream Dam Turbines",
                            "description": "Flowchart showing Masinga Dam regulating river discharge to sustain Kamburu, Gitaru, Kindaruma, and Kiambere power generation during severe dry spells."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Economic Benefits of the Seven Forks Scheme",
                        "content": {
                            "title": "Economic Benefits of the Seven Forks Scheme",
                            "text": "• Industrial Power: Provides bulk electricity to KenGen and KPLC, driving manufacturing in Nairobi and Thika.\n• Agricultural Irrigation: Provides water for large-scale crop schemes.\n• Transport Linkages: Concrete dam walls serve as bridges across River Tana, connecting Embu, Machakos, and Kitui counties.\n• Employment & Fisheries: Created thousands of jobs and established commercial freshwater fisheries."
                        }
                    }
                ],
                # Page 9
                [
                    {
                        "type": "concept_explanation",
                        "title": "Problems Facing the Seven Forks Scheme",
                        "content": {
                            "title": "Problems Facing the Seven Forks Scheme",
                            "text": "1. Siltation: Deforestation in the Mt. Kenya catchment causes heavy topsoil erosion into River Tana. Silt accumulation reduces reservoir capacity and clogs turbine intake tunnels, requiring expensive dredging.\n\n2. Water Level Fluctuations: Severe droughts reduce river inflow, forcing KPLC to institute national power rationing.\n\n3. High Capital Costs for Spare Parts: Heavy reliance on expensive imported turbines and foreign technical expatriates."
                        }
                    }
                ],
                # Page 10
                [
                    {
                        "type": "callout",
                        "title": "Environmental Impact: Reservoir Siltation",
                        "content": {
                            "type": "warning",
                            "title": "Environmental Impact: Reservoir Siltation",
                            "text": "Uncontrolled clearing of steep slopes in Murang'a and Nyeri leads to high silt loads in River Tana, threatening to fill Masinga Reservoir within decades unless upstream catchment afforestation is enforced."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Upstream Catchment Management",
                        "content": {
                            "title": "Upstream Catchment Management",
                            "text": "KenGen partners with the Water Resources Authority (WRA) to fund soil conservation, terracing, and tree planting along River Tana tributaries to trap silt before it reaches Masinga Dam."
                        }
                    }
                ],
                # Page 11
                [
                    {
                        "type": "comparison_table",
                        "title": "HEP Schemes in East Africa: Kenya vs Uganda",
                        "content": {
                            "headers": ["Feature", "Seven Forks Scheme (Kenya)", "Owen Falls / Nalubaale Dam (Uganda)"],
                            "rows": [
                                ["Primary River Source", "River Tana (Mt. Kenya catchment)", "River Nile (Lake Victoria natural outlet)"],
                                ["Scheme Layout", "Cascade of 5 distinct dams (Masinga to Kiambere)", "Single massive storage dam across Lake Victoria outlet"],
                                ["Hydrological Storage", "Relies on artificial Masinga Lake reservoir", "Natural storage provided by Lake Victoria"],
                                ["Cross-Border Trade", "Historically imported electricity from Uganda", "Exports 30 MW of bulk electricity to Kenya"],
                                ["Industrial Impact", "Powers Nairobi, Thika & highland industries", "Catalyzed industrial growth of Jinja Town"]
                            ]
                        }
                    }
                ],
                # Page 12
                [
                    {
                        "type": "mini_activity",
                        "title": "Interactive HEP Dam Site Evaluator",
                        "content": {
                            "activity_type": "scenario_decision",
                            "title": "Interactive HEP Dam Site Evaluator",
                            "prompt": "An engineering firm is choosing between two sites on a river. Site A is a shallow, wide valley in porous limestone with dense settlements. Site B is a deep, narrow gorge in hard granite bedrock with waterfalls and sparse population. Which site is suitable?",
                            "options": [
                                "Option A: Site A (Wide valley allows larger surface area).",
                                "Option B: Site B (Deep narrow gorge, hard impervious bedrock, high waterfall head, low relocation costs).",
                                "Option C: Neither site can support dam construction."
                            ],
                            "correct_option": "Option B: Site B (Deep narrow gorge, hard impervious bedrock, high waterfall head, low relocation costs).",
                            "explanation": "Site B meets all physical and human criteria: deep narrow gorge minimizes dam wall cost, hard granite prevents seepage, waterfalls provide kinetic energy, and sparse population lowers relocation costs."
                        }
                    }
                ],
                # Page 13
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Checkpoint: Seven Forks & African HEP",
                        "content": {
                            "question": "Which dam in the Seven Forks Scheme functions as the master hydrological regulator for the entire downstream cascade?",
                            "options": [
                                "Kindaruma Dam",
                                "Masinga Dam",
                                "Kiambere Dam",
                                "Gitaru Dam"
                            ],
                            "correct_answer": 1,
                            "explanation": "Masinga Dam has the largest storage reservoir, regulating river discharge to sustain all downstream power stations during dry seasons."
                        }
                    }
                ],
                # Page 14
                [
                    {
                        "type": "summary",
                        "title": "Hydroelectric Power: Key Takeaways",
                        "content": {
                            "title": "Hydroelectric Power: Key Takeaways",
                            "summary_points": [
                                "HEP site selection requires large water volume, steep waterfalls, deep narrow gorges, and hard impervious bedrock.",
                                "The Seven Forks Scheme on River Tana features Masinga, Kamburu, Gitaru, Kindaruma, and Kiambere dams.",
                                "Masinga Dam is the master regulator, storing wet-season runoff to maintain dry-season downstream power generation.",
                                "Major challenges include water level fluctuations during droughts, reservoir siltation from upstream deforestation, and high capital costs.",
                                "Uganda's Owen Falls Dam at Jinja exports bulk electricity to Kenya, leveraging Lake Victoria as a natural reservoir."
                            ]
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 4: Geothermal Power Potential in the Kenyan Rift Valley
        # =====================================================================
        {
            "unit_order": 4,
            "unit_name": "Geothermal Power Potential in the Kenyan Rift Valley",
            "unit_description": "Volcanic geothermal geology of the Great Rift Valley, Olkaria Geothermal Complex, and reasons why Kenya prioritizes geothermal over HEP.",
            "lesson_title": "Geothermal Power Potential in the Kenyan Rift Valley",
            "pages": [
                # Page 1
                [
                    {
                        "type": "learning_goal",
                        "title": "Learning Objectives: Geothermal Potential",
                        "content": {
                            "title": "Learning Objectives: Geothermal Potential",
                            "goals": [
                                "Examine the volcanic geological origin of geothermal steam in the Great Rift Valley.",
                                "Analyze the operation of the Olkaria Geothermal Power Station near Lake Naivasha.",
                                "Identify potential geothermal sites along the Kenyan Rift (Lake Bogoria, Eburu, Menengai).",
                                "Evaluate four key reasons why Kenya prioritizes geothermal expansion over HEP."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Rift Valley Volcanic Energy Potential",
                        "content": {
                            "title": "Rift Valley Volcanic Energy Potential",
                            "text": "Kenya possesses immense geothermal energy potential concentrated along the floor of the Great Rift Valley. This tectonic belt stretches from Lake Magadi in the south through Lake Naivasha, Menengai, and Lake Bogoria to Lake Turkana in the north."
                        }
                    }
                ],
                # Page 2
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Thematic Map of Kenya Rift Valley Geothermal Energy Belt",
                        "content": {
                            "title": "Thematic Map of Kenya Rift Valley Geothermal Energy Belt",
                            "caption": "Spatial Distribution of Exploited and Unexploited Geothermal Fields along the Great Rift Valley Fault System",
                            "description": "Thematic map plotting Olkaria (Naivasha), Eburu, Menengai Crater, Lake Bogoria geysers, Lake Baringo, Suswa-Longonot, and Lake Turkana geothermal prospects."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Spatial Distribution of Geothermal Resources",
                        "content": {
                            "title": "Spatial Distribution of Geothermal Resources",
                            "text": "The Rift Valley's crustal thinning and active fault lines bring magmatic heat near the surface. Major prospects include:\n\n• Olkaria (Naivasha): The premier producing field generating over 800 MW.\n• Lake Bogoria: Holds the highest unexploited potential with active hot springs and geysers.\n• Menengai Crater & Eburu: Active drilling fields undergoing grid connection."
                        }
                    }
                ],
                # Page 3
                [
                    {
                        "type": "concept_explanation",
                        "title": "Olkaria Geothermal Complex (Naivasha)",
                        "content": {
                            "title": "Olkaria Geothermal Complex (Naivasha)",
                            "text": "Olkaria, located south of Lake Naivasha inside Hell's Gate National Park, is Africa's largest geothermal power complex. Operating through multiple power plants (Olkaria I to V), it contributes over 30% of Kenya's total grid electricity, providing continuous base-load power."
                        }
                    }
                ],
                # Page 4
                [
                    {
                        "type": "suggested_image",
                        "title": "Olkaria V Geothermal Power Station",
                        "content": {
                            "title": "Olkaria V Geothermal Power Station",
                            "caption": "The modern Olkaria V Geothermal Power Station in Naivasha, displaying high-pressure steam pipes and turbine generation buildings.",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/a/a4/Olkaria_V_Geothermal_Power_Station.jpg",
                            "author": "Bbossoxx, Wikimedia Commons",
                            "licensing": "CC BY-SA 4.0",
                            "commons_page_url": "https://commons.wikimedia.org/wiki/File:Olkaria_V_Geothermal_Power_Station.jpg"
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Clean Base-Load Power at Olkaria",
                        "content": {
                            "title": "Clean Base-Load Power at Olkaria",
                            "text": "Olkaria's steam wells tap underground reservoirs up to 3,000 meters deep. Condensed steam is re-injected deep into the bedrock to maintain reservoir pressure and sustain indefinite steam production."
                        }
                    }
                ],
                # Page 5
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Drought Resilience Matrix: Geothermal Base-Load vs Hydro Level Fluctuation",
                        "content": {
                            "title": "Drought Resilience Matrix: Geothermal Base-Load vs Hydro Level Fluctuation",
                            "caption": "Comparative Power Output Graph: Continuous Geothermal Base-Load vs Seasonal HEP Reservoir Fluctuations",
                            "description": "Comparative line graph showing flat, uninterrupted geothermal electricity output during severe dry seasons contrasted with sharp declines in hydroelectric power generation."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Why Kenya Prioritizes Geothermal over HEP",
                        "content": {
                            "title": "Why Kenya Prioritizes Geothermal over HEP",
                            "text": "1. Drought Immunity: Geothermal steam is continuous and completely unaffected by surface rainfall or reservoir levels, providing reliable base-load power during severe droughts.\n\n2. Low Running Costs: Once steam wells are drilled, geothermal requires no expensive imported fuel to spin turbines.\n\n3. Immense Rift Valley Potential: Kenya has over 10,000 MW of unexploited geothermal potential along the Rift Valley.\n\n4. Environmental Cleanliness: Produces zero carbon emissions during generation, helping to green the national grid."
                        }
                    }
                ],
                # Page 6
                [
                    {
                        "type": "concept_explanation",
                        "title": "Unexploited Volcanic Geothermal Fields",
                        "content": {
                            "title": "Unexploited Volcanic Geothermal Fields",
                            "text": "• Lake Bogoria: Features active geysers shooting boiling water up to 5 meters high. The underlying magmatic heat source offers massive unexploited power capacity.\n\n• Menengai Crater: A giant volcanic caldera near Nakuru where KenGen and Geothermal Development Company (GDC) have drilled multiple high-capacity steam wells."
                        }
                    }
                ],
                # Page 7
                [
                    {
                        "type": "callout",
                        "title": "Geothermal Re-injection Technology",
                        "content": {
                            "type": "tip",
                            "title": "Geothermal Re-injection Technology",
                            "text": "After spinning turbines, hot condensed water is pumped back deep into the geothermal aquifer via re-injection wells. This prevents groundwater depletion and eliminates surface thermal pollution."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Systemic Problems of Energy Development in Kenya",
                        "content": {
                            "title": "Systemic Problems of Energy Development in Kenya",
                            "text": "• Inadequate Financial Capital: High initial drilling costs (a single geothermal well costs KSh 600 million).\n• Small Connection Market: High rural connection fees limit power demand.\n• Long Transmission Distances: Power stations in the Rift Valley or dry Nyika plains are far from consuming cities, causing transmission losses."
                        }
                    }
                ],
                # Page 8
                [
                    {
                        "type": "concept_explanation",
                        "title": "Structural Energy Development Bottlenecks",
                        "content": {
                            "title": "Structural Energy Development Bottlenecks",
                            "text": "Kenya also faces slow rural adoption of solar and wind due to high panel installation costs, alongside severe wood fuel overexploitation that causes deforestationfeedback loops."
                        }
                    }
                ],
                # Page 9
                [
                    {
                        "type": "worked_example",
                        "title": "Worked KCSE Question: Olkaria Geothermal Development",
                        "content": {
                            "question": "Explain four reasons why the government of Kenya is actively expanding geothermal power generation at Olkaria. (8 Marks)",
                            "strategy": "State the factor clearly, explain the operational mechanism in Kenya, and link it directly to grid stability.",
                            "solution": [
                                "1. Reliability during Droughts: Geothermal steam is tapped from deep underground magmatic heat, making generation continuous and completely immune to surface rainfall drops that cause HEP rationing. (2 Marks)",
                                "2. Abundant Rift Valley Potential: Kenya possesses over 10,000 MW of geothermal potential along the Great Rift Valley, offering a vast domestic resource to meet rising industrial power demand. (2 Marks)",
                                "3. Lower Long-Term Running Costs: Once steam wells are drilled, geothermal stations require no fuel to spin turbines, drastically reducing operational costs compared to diesel generators. (2 Marks)",
                                "4. Environmental Sustainability: Geothermal generation produces zero carbon emissions, reducing greenhouse gas pollution and diversifying the national energy mix. (2 Marks)"
                            ]
                        }
                    }
                ],
                # Page 10
                [
                    {
                        "type": "mini_activity",
                        "title": "Interactive Energy Grid Balance Simulator",
                        "content": {
                            "activity_type": "scenario_decision",
                            "title": "Interactive Energy Grid Balance Simulator",
                            "prompt": "Kenya experiences a 10-month severe drought causing River Tana dam levels to fall by 60%. How should the national grid operator rebalance power supply to prevent city blackouts?",
                            "options": [
                                "Option A: Increase base-load dispatch from Olkaria Geothermal and Lake Turkana Wind while running thermal backup.",
                                "Option B: Shut down Olkaria Geothermal and rely exclusively on River Tana dams.",
                                "Option C: Drain all remaining water from Masinga Dam in one day."
                            ],
                            "correct_option": "Option A: Increase base-load dispatch from Olkaria Geothermal and Lake Turkana Wind while running thermal backup.",
                            "explanation": "Geothermal and wind are drought-immune base-load sources that maintain grid stability when hydroelectric dam reservoirs drop during extended dry spells."
                        }
                    }
                ],
                # Page 11
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Checkpoint: Geothermal Energy",
                        "content": {
                            "question": "Which volcanic region along the Kenyan Rift Valley holds the highest unexploited geothermal potential characterized by active geysers and hot springs?",
                            "options": [
                                "Lake Bogoria",
                                "Mount Elgon",
                                "Kikuyu Escarpment",
                                "Mombasa Island"
                            ],
                            "correct_answer": 0,
                            "explanation": "Lake Bogoria features extensive active geysers and hot springs, representing Kenya's largest unexploited geothermal steam field."
                        }
                    }
                ],
                # Page 12
                [
                    {
                        "type": "summary",
                        "title": "Geothermal Development: Key Takeaways",
                        "content": {
                            "title": "Geothermal Development: Key Takeaways",
                            "summary_points": [
                                "Geothermal steam is generated by magmatic heat beneath the Great Rift Valley fault system.",
                                "Olkaria (Naivasha) is Africa's premier geothermal station, providing over 30% of Kenya's grid electricity.",
                                "Unexploited fields include Lake Bogoria (geysers), Menengai Crater, Eburu, and Suswa.",
                                "Kenya prioritizes geothermal because it is drought-immune, has low running costs, utilizes abundant Rift potential, and is environmentally clean.",
                                "Key energy challenges include high drilling capital, siltation, long transmission lines, and wood fuel overexploitation."
                            ]
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 5: The Global Energy/Oil Crisis: Causes, Case Studies, and Impacts
        # =====================================================================
        {
            "unit_order": 5,
            "unit_name": "The Global Energy/Oil Crisis: Causes, Case Studies, and Impacts",
            "unit_description": "Economic dynamics of global oil crises, historical case studies (1973, 1991, 2003), and cascading impacts on developing economies.",
            "lesson_title": "The Global Energy/Oil Crisis: Causes, Case Studies, and Impacts",
            "pages": [
                # Page 1
                [
                    {
                        "type": "learning_goal",
                        "title": "Learning Objectives: The Global Oil Crisis",
                        "content": {
                            "title": "Learning Objectives: The Global Oil Crisis",
                            "goals": [
                                "Define an oil crisis and analyze its global macroeconomic causes.",
                                "Examine three historical oil crisis case studies (1973 Arab-Israeli War, 1991 & 2003 Persian Gulf Wars).",
                                "Trace the cascading systemic impacts of crude oil price spikes on developing nations like Kenya.",
                                "Analyze how oil crises accelerate rural deforestation and environmental degradation."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Understanding Global Oil Crises",
                        "content": {
                            "title": "Understanding Global Oil Crises",
                            "text": "An oil crisis occurs when global demand for petroleum significantly exceeds available supply, or when major oil-producing nations restrict output, triggering sharp, unsustainable spikes in global crude oil prices."
                        }
                    }
                ],
                # Page 2
                [
                    {
                        "type": "concept_explanation",
                        "title": "Root Causes of Global Oil Supply Disruptions",
                        "content": {
                            "title": "Root Causes of Global Oil Supply Disruptions",
                            "text": "1. Over-Reliance on Petroleum: Modern transportation and industrial manufacturing are heavily dependent on liquid crude oil.\n\n2. Middle East Geopolitics: Political conflicts in the Persian Gulf disrupt major production fields.\n\n3. OPEC Production Quotas: The Organization of the Petroleum Exporting Countries (OPEC) restricts daily crude output to manipulate global prices.\n\n4. Strategic Reserve Accumulation: Industrialized nations hoard petroleum reserves, limiting open-market supply."
                        }
                    },
                    {
                        "type": "callout",
                        "title": "Economic Reality: Cartel Price Control",
                        "content": {
                            "type": "tip",
                            "title": "Economic Reality: Cartel Price Control",
                            "text": "OPEC controls over 40% of global crude oil production. A minor percentage reduction in OPEC daily barrel quotas causes immediate price surges across non-producing nations like Kenya."
                        }
                    }
                ],
                # Page 3
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Cascading Systemic Macroeconomic Impacts of a Global Oil Crisis",
                        "content": {
                            "title": "Cascading Systemic Macroeconomic Impacts of a Global Oil Crisis",
                            "caption": "Cascading Economic Flowchart: Crude Oil Price Spike Triggering Inflation, Fertilizer Shortages, Debt, and Deforestation",
                            "description": "Flowchart showing crude oil price surge -> high import bill -> currency devaluation -> expensive fertilizer -> reduced crop yields -> industrial layoffs -> wood fuel pressure."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Cascading Systemic Macroeconomic Impacts",
                        "content": {
                            "title": "Cascading Systemic Macroeconomic Impacts",
                            "text": "When crude oil prices jump, the negative economic consequences cascade rapidly through oil-importing developing countries:\n\n• Balance of Trade Deficit: Import bills soar, draining national foreign exchange reserves.\n• Hyper-Inflation & Currency Devaluation: Increased transport fuel costs drive up food and consumer prices while weakening local currency value.\n• Agricultural Decline: Petroleum-based chemical fertilizers become unaffordable, reducing crop yields and causing food insecurity."
                        }
                    }
                ],
                # Page 4
                [
                    {
                        "type": "concept_explanation",
                        "title": "Historical Case Study 1: The 1973–1974 Arab-Israeli War Crisis",
                        "content": {
                            "title": "Historical Case Study 1: The 1973–1974 Arab-Israeli War Crisis",
                            "text": "• Trigger: War broke out between Israel and Arab nations in October 1973.\n• Mechanism: Arab OPEC members imposed an oil embargo on Western nations (such as the USA) that backed Israel, cutting daily production.\n• Result: Global crude oil prices quadrupled from $3 to $12 per barrel, causing severe stagflation, factory closures, and global economic recession."
                        }
                    }
                ],
                # Page 5
                [
                    {
                        "type": "concept_explanation",
                        "title": "Historical Case Study 2: The 1991 First Persian Gulf War",
                        "content": {
                            "title": "Historical Case Study 2: The 1991 First Persian Gulf War",
                            "text": "• Trigger: Iraq invaded Kuwait in August 1990 over disputed oil fields and OPEC production quotas.\n• Environmental Warfare: Retreating Iraqi forces set fire to over 600 Kuwaiti oil wells and dumped 465 million gallons of crude oil into the Persian Gulf.\n• Result: Crude oil prices doubled rapidly, while UN trade embargoes against Iraq severely restricted global market supply."
                        }
                    },
                    {
                        "type": "callout",
                        "title": "Environmental Catastrophe: Kuwaiti Oil Fires",
                        "content": {
                            "type": "warning",
                            "title": "Environmental Catastrophe: Kuwaiti Oil Fires",
                            "text": "The 1991 Kuwaiti oil well fires burned for eight months, consuming 6 million barrels of crude oil daily and blanketing the Middle East in toxic black soot."
                        }
                    }
                ],
                # Page 6
                [
                    {
                        "type": "concept_explanation",
                        "title": "Historical Case Study 3: The 2003 Second Persian Gulf War",
                        "content": {
                            "title": "Historical Case Study 3: The 2003 Second Persian Gulf War",
                            "text": "• Trigger: US-led coalition forces invaded Iraq in March 2003.\n• Economic Shock: Military conflict disrupted Iraqi oil exports, driving global oil prices from $35 per barrel to over $50 by 2004.\n• OPEC Response: OPEC was forced to increase its daily crude output quota by 8% to stabilize volatile global energy markets."
                        }
                    }
                ],
                # Page 7
                [
                    {
                        "type": "suggested_image",
                        "title": "Commercial Petroleum Oil Refinery",
                        "content": {
                            "title": "Commercial Petroleum Oil Refinery",
                            "caption": "A large-scale commercial petroleum oil refinery showing distillation towers and storage tanks.",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/0/0e/Altona_Oil_Refinery_Victoria.jpg",
                            "author": "Public Domain, Wikimedia Commons",
                            "licensing": "Public domain",
                            "commons_page_url": "https://commons.wikimedia.org/wiki/File:Altona_Oil_Refinery_Victoria.jpg"
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Refining Infrastructure and Fuel Pricing",
                        "content": {
                            "title": "Refining Infrastructure and Fuel Pricing",
                            "text": "Oil refineries require constant crude oil feeds. When crude prices surge, refineries pass costs to petrol stations, raising transport fares and manufacturing overheads nationwide."
                        }
                    }
                ],
                # Page 8
                [
                    {
                        "type": "concept_explanation",
                        "title": "Impact on Tourism, Foreign Debt, and Deforestation",
                        "content": {
                            "title": "Impact on Tourism, Foreign Debt, and Deforestation",
                            "text": "• Tourism Decline: Rising jet fuel costs raise international airline fares, discouraging foreign tourists from traveling to Kenya.\n• Debt Accumulation: Governments borrow heavily at high interest rates to subsidize fuel imports, diverting funds from healthcare and education.\n• Deforestation Feedback Loop: As kerosene and LPG become unaffordable, low-income urban and rural families switch back to charcoal and firewood, accelerating forest destruction."
                        }
                    }
                ],
                # Page 9
                [
                    {
                        "type": "concept_explanation",
                        "title": "The Oil Crisis Deforestation Cascade",
                        "content": {
                            "title": "The Oil Crisis Deforestation Cascade",
                            "text": "The link between global oil prices and local forest cover highlights ecological interconnectedness. High LPG gas prices directly force household energy substitution toward wood fuel, increasing tree cutting in vulnerable dryland forests."
                        }
                    }
                ],
                # Page 10
                [
                    {
                        "type": "suggested_image",
                        "title": "Lake Bogoria Geysers and Steam Vents",
                        "content": {
                            "title": "Lake Bogoria Geysers and Steam Vents",
                            "caption": "Active volcanic geysers and steam vents erupting along the shores of Lake Bogoria in the Great Rift Valley.",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/8/8c/200812_kenya-107_%283213939312%29.jpg",
                            "author": "Franco Pecchio, Wikimedia Commons",
                            "licensing": "CC BY 2.0",
                            "commons_page_url": "https://commons.wikimedia.org/wiki/File:200812_kenya-107_(3213939312).jpg"
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Rift Valley Volcanic Steam Features",
                        "content": {
                            "title": "Rift Valley Volcanic Steam Features",
                            "text": "Geothermal features like Lake Bogoria's geysers demonstrate Kenya's massive natural steam reserves, which provide a clean domestic alternative to imported crude oil."
                        }
                    }
                ],
                # Page 11
                [
                    {
                        "type": "worked_example",
                        "title": "Worked KCSE Question: Oil Crisis & Deforestation Cascades",
                        "content": {
                            "question": "Explain three ways in which a sharp increase in global crude oil prices leads to environmental degradation in rural Kenya. (6 Marks)",
                            "strategy": "Trace the step-by-step economic substitution flow from expensive oil to local environmental pressure.",
                            "solution": [
                                "1. Increased Kerosene and LPG Prices: High crude oil prices make cooking gas (LPG) and kerosene unaffordable for low-income households, forcing them to switch back to wood fuel and charcoal. (2 Marks)",
                                "2. Accelerated Forest Clearing: Rising charcoal demand causes rural populations to cut down forests faster than trees grow, destroying vegetation cover and water catchment towers. (2 Marks)",
                                "3. Severe Soil Erosion: Deforestation leaves soils bare, leading to severe rainwater erosion, gulley formation, and reservoir siltation downstream. (2 Marks)"
                            ]
                        }
                    }
                ],
                # Page 12
                [
                    {
                        "type": "mini_activity",
                        "title": "Interactive Macroeconomic Crisis Simulator",
                        "content": {
                            "activity_type": "scenario_decision",
                            "title": "Interactive Macroeconomic Crisis Simulator",
                            "prompt": "Global crude oil prices spike by 80% due to Middle East war conflicts. What is the immediate impact on Kenya's agricultural sector?",
                            "options": [
                                "Option A: Petroleum-based chemical fertilizers become unaffordable, leading to lower crop yields and food price inflation.",
                                "Option B: Crop yields double due to increased solar radiation.",
                                "Option C: Agricultural transport costs drop to zero."
                            ],
                            "correct_option": "Option A: Petroleum-based chemical fertilizers become unaffordable, leading to lower crop yields and food price inflation.",
                            "explanation": "Chemical fertilizers require petroleum inputs and oil-powered transport, so crude oil spikes make fertilizers expensive, reducing crop yields."
                        }
                    }
                ],
                # Page 13
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Checkpoint: The Global Oil Crisis",
                        "content": {
                            "question": "How did the 1973 Arab-Israeli War trigger a global oil crisis?",
                            "options": [
                                "Arab OPEC nations imposed an oil embargo on Western countries supporting Israel, cutting supply and quadrupling prices.",
                                "Oil was discovered in massive quantities in Europe, causing prices to crash.",
                                "Nuclear power stations replaced all oil refineries.",
                                "The United Nations banned all oil transport across the Atlantic."
                            ],
                            "correct_answer": 0,
                            "explanation": "Arab OPEC members used oil as a political weapon, imposing an embargo on Western allies of Israel, which quadrupled global crude prices."
                        }
                    }
                ],
                # Page 14
                [
                    {
                        "type": "summary",
                        "title": "The Oil Crisis: Key Takeaways",
                        "content": {
                            "title": "The Oil Crisis: Key Takeaways",
                            "summary_points": [
                                "An oil crisis occurs when global demand exceeds supply or OPEC cuts output, causing crude price surges.",
                                "Key historical case studies include 1973 (Arab-Israeli embargo), 1991 (First Persian Gulf War), and 2003 (Second Persian Gulf War).",
                                "Cascading impacts on Kenya include balance of trade deficits, inflation, expensive fertilizers, lower crop yields, and high foreign debt.",
                                "High LPG gas prices force household energy substitution toward charcoal, accelerating deforestation."
                            ]
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 6: Energy Management, Conservation Strategies, and KCSE Synthesis
        # =====================================================================
        {
            "unit_order": 6,
            "unit_name": "Energy Management, Conservation Strategies, and KCSE Synthesis",
            "unit_description": "Energy management vs conservation frameworks, energy-saving technologies (Jiko stoves, solar heaters), and KCSE revision exam breakdown.",
            "lesson_title": "Energy Management, Conservation Strategies, and KCSE Synthesis",
            "pages": [
                # Page 1
                [
                    {
                        "type": "learning_goal",
                        "title": "Learning Objectives: Energy Management & Conservation",
                        "content": {
                            "title": "Learning Objectives: Energy Management & Conservation",
                            "goals": [
                                "Differentiate clearly between Energy Management policies and Energy Conservation measures.",
                                "Analyze national energy management strategies (public transport, engine caps, agroforestry, grid diversification).",
                                "Examine consumer conservation technologies (insulated Kenya Ceramic Jikos, solar water heaters, biogas).",
                                "Master KCSE structured exam questions and model answers for Topic 4."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Sustainable Energy Policy Framework",
                        "content": {
                            "title": "Sustainable Energy Policy Framework",
                            "text": "Achieving energy security requires a dual strategy: Energy Management (national planning, policy regulation, and resource diversification) and Energy Conservation (reducing energy waste and maximizing consumer efficiency)."
                        }
                    }
                ],
                # Page 2
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Energy Management vs Energy Conservation Dual Policy Framework",
                        "content": {
                            "title": "Energy Management vs Energy Conservation Dual Policy Framework",
                            "caption": "Bifurcated Strategic Framework: National Management Policies (Planning & Grid Diversification) vs Household Conservation (Efficiency & Waste Reduction)",
                            "description": "Strategic framework diagram separating Management policies (vehicle import caps, public transport, afforestation, geothermal expansion) from Conservation practices (Jiko stoves, turning off lights, regular engine servicing)."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Geographical Distinction: Management vs Conservation",
                        "content": {
                            "title": "Geographical Distinction: Management vs Conservation",
                            "text": "• Energy Management: Macro-level government planning, regulatory policies, resource allocation, and grid diversification (e.g., expanding Olkaria geothermal, building public bus lanes, regulating large-engine car imports).\n\n• Energy Conservation: Micro-level actions by consumers and industries to eliminate energy waste and improve efficiency (e.g., using insulated Kenya Ceramic Jikos, switching off idle lights, servicing car engines)."
                        }
                    }
                ],
                # Page 3
                [
                    {
                        "type": "concept_explanation",
                        "title": "National Energy Management Measures",
                        "content": {
                            "title": "National Energy Management Measures",
                            "text": "1. Vehicle Engine Capacity Regulation: Levying higher import tariffs on high-engine-capacity luxury vehicles that consume excessive fuel.\n\n2. Public Transit Promotion: Developing high-capacity public transport systems (Standard Gauge Railway, Bus Rapid Transit) to reduce private car reliance and fuel waste.\n\n3. Infrastructure Optimization: Designing bypass highways and flyovers to eliminate urban traffic congestion where idling engines waste fuel."
                        }
                    }
                ],
                # Page 4
                [
                    {
                        "type": "concept_explanation",
                        "title": "Agroforestry & Grid Diversification Management",
                        "content": {
                            "title": "Agroforestry & Grid Diversification Management",
                            "text": "• Afforestation & Agroforestry: Enforcing national tree planting and promoting farm agroforestry to secure sustainable wood fuel supplies while protecting river catchments.\n\n• Grid Diversification: Investing in geothermal, solar, and wind energy to reduce reliance on imported oil and drought-vulnerable HEP."
                        }
                    }
                ],
                # Page 5
                [
                    {
                        "type": "concept_explanation",
                        "title": "Household & Industrial Energy Conservation Measures",
                        "content": {
                            "title": "Household & Industrial Energy Conservation Measures",
                            "text": "1. Switching Off Idle Appliances: Turning off lights, computers, and water heaters when not in use.\n\n2. Regular Vehicle Engine Servicing: Maintaining correct tire pressure and engine tuning to maximize fuel combustion efficiency.\n\n3. Insulated Energy-Saving Stoves: Replacing open three-stone fires with insulated Kenya Ceramic Jikos (KCJ).\n\n4. Domestic Solar & Biogas Adoption: Installing rooftop solar water heaters and farm biogas digesters."
                        }
                    }
                ],
                # Page 6
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Insulated Fuel-Efficient Stoves (Jiko) Thermal Efficiency Design",
                        "content": {
                            "title": "Insulated Fuel-Efficient Stoves (Jiko) Thermal Efficiency Design",
                            "caption": "Cross-Section Comparison: Open Three-Stone Fire Thermal Waste vs Insulated Kenya Ceramic Jiko (KCJ) Heat Retention",
                            "description": "Diagram contrasting open three-stone fire (85% heat loss) with Kenya Ceramic Jiko featuring insulating clay liner, metal casing, draft door, and 50% wood fuel savings."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Thermal Efficiency of the Kenya Ceramic Jiko (KCJ)",
                        "content": {
                            "title": "Thermal Efficiency of the Kenya Ceramic Jiko (KCJ)",
                            "text": "The Kenya Ceramic Jiko (KCJ) features an inner insulating ceramic clay liner encased in a metal frame. The clay liner retains heat and directs it upward to the cooking pot, reducing charcoal consumption by 50% compared to traditional open metal stoves."
                        }
                    }
                ],
                # Page 7
                [
                    {
                        "type": "concept_explanation",
                        "title": "Adopting Solar Water Heaters & Farm Biogas",
                        "content": {
                            "title": "Adopting Solar Water Heaters & Farm Biogas",
                            "text": "Mandating rooftop solar water heaters in urban residential developments replaces high-wattage electric immersion heaters, significantly reducing national peak-hour electricity demand."
                        }
                    },
                    {
                        "type": "callout",
                        "title": "Policy Mandate: Solar Water Heating Regulations",
                        "content": {
                            "type": "tip",
                            "title": "Policy Mandate: Solar Water Heating Regulations",
                            "text": "The Energy and Petroleum Regulatory Authority (EPRA) mandates that all commercial and residential buildings using over 100 liters of hot water daily must install solar water heating systems."
                        }
                    }
                ],
                # Page 8
                [
                    {
                        "type": "worked_example",
                        "title": "KCSE Exam Strategy: Answering 'Explain' Energy Questions",
                        "content": {
                            "question": "Explain three measures the government of Kenya can take to manage energy resources sustainably. (6 Marks)",
                            "strategy": "State the management policy clearly, explain how it operates, and connect it directly to energy reduction or sustainability.",
                            "solution": [
                                "1. Promoting Public Transport Systems: Developing high-capacity bus transit and railways reduces the number of private motor vehicles on roads, cutting overall national petrol consumption. (2 Marks)",
                                "2. Enforcing Afforestation and Agroforestry Policies: Encouraging farmers to plant fast-growing trees on farm boundaries provides a sustainable source of firewood and charcoal while protecting water catchments. (2 Marks)",
                                "3. Grid Diversification into Renewables: Investing in geothermal, wind, and solar power reduces national reliance on expensive imported petroleum and drought-vulnerable HEP. (2 Marks)"
                            ]
                        }
                    }
                ],
                # Page 9
                [
                    {
                        "type": "common_mistake",
                        "title": "Common Student Mistakes in Energy Classification & HEP Sites",
                        "content": {
                            "mistake": "Confusing Geothermal energy with Hydroelectric power or listing Coal as a renewable resource.",
                            "correction": "Geothermal taps underground magmatic steam (Olkaria), whereas HEP taps surface river water (Seven Forks). Coal is an exhaustible fossil fuel (Non-Renewable).",
                            "reasoning": "In KCSE exams, clear distinction between magmatic steam (geothermal) and surface river flow (hydroelectric) is essential for full marks."
                        }
                    }
                ],
                # Page 10
                [
                    {
                        "type": "worked_example",
                        "title": "End-of-Topic Revision Exam: Short Answer Section",
                        "content": {
                            "question": "(a) Define energy. (2 Marks)\n(b) Name three non-renewable fossil fuels. (3 Marks)\n(c) State three potential geothermal sites in Kenya, excluding Olkaria. (3 Marks)",
                            "strategy": "Provide precise geographical definitions and factual location names.",
                            "solution": [
                                "(a) Energy is the power required to carry out physical, mechanical, or biological work. (2 Marks)",
                                "(b) Coal, Petroleum (Crude Oil), Natural Gas. (3 Marks)",
                                "(c) Lake Bogoria, Menengai Crater, Eburu (also Lake Baringo, Suswa). (3 Marks)"
                            ]
                        }
                    }
                ],
                # Page 11
                [
                    {
                        "type": "worked_example",
                        "title": "End-of-Topic Revision Exam: Structured Case Studies",
                        "content": {
                            "question": "(a) State four physical factors considered when choosing an HEP dam site. (4 Marks)\n(b) Describe three benefits of the Seven Forks Scheme to Kenya's economy. (6 Marks)",
                            "strategy": "List exact physical requirements (water volume, gradient, gorge, bedrock) and explain multi-purpose economic benefits.",
                            "solution": [
                                "(a) 1. Large, constant water volume. 2. Steep gradient (waterfalls/rapids). 3. Deep, narrow river gorge. 4. Hard, impervious basement bedrock. (4 Marks)",
                                "(b) 1. Industrial Power: Supplies bulk electricity to factories in Nairobi and Thika. 2. Irrigation Water: Provides water for local agricultural schemes. 3. Fisheries & Infrastructure: Reservoirs establish commercial freshwater fisheries, and dam walls serve as bridges across River Tana. (6 Marks)"
                            ]
                        }
                    }
                ],
                # Page 12
                [
                    {
                        "type": "worked_example",
                        "title": "End-of-Topic Revision Exam: Oil Crisis Essay Model",
                        "content": {
                            "question": "Explain four macroeconomic problems experienced by developing countries like Kenya during a global oil crisis. (8 Marks)",
                            "strategy": "Link global crude price spikes to local trade deficits, inflation, agricultural decline, and foreign debt burdens.",
                            "solution": [
                                "1. Severe Balance of Trade Deficit: High crude import bills cause national foreign exchange reserves to drain rapidly, making import spending far exceed export earnings. (2 Marks)",
                                "2. Hyper-Inflation and Transport Costs: Rising fuel prices increase transport fares and goods transport costs, devaluing local currency purchasing power. (2 Marks)",
                                "3. Agricultural Decline: Petroleum-based chemical fertilizers become unaffordable for farmers, leading to reduced crop yields and food insecurity. (2 Marks)",
                                "4. Foreign Debt Accumulation: Nations are forced to borrow heavily at high interest rates simply to fund basic petroleum imports, diverting funds from health and education. (2 Marks)"
                            ]
                        }
                    }
                ],
                # Page 13
                [
                    {
                        "type": "mini_activity",
                        "title": "Interactive Energy Management Policy Challenge",
                        "content": {
                            "activity_type": "scenario_decision",
                            "title": "Interactive Energy Management Policy Challenge",
                            "prompt": "As Director of Energy, you must select the most effective policy to reduce household wood fuel consumption and halt deforestation. Which policy measure should you prioritize?",
                            "options": [
                                "Option A: Subsidize local production of insulated Kenya Ceramic Jikos (KCJ) and expand farm agroforestry.",
                                "Option B: Ban all cooking stove usage in rural areas.",
                                "Option C: Import expensive coal for household kitchen use."
                            ],
                            "correct_option": "Option A: Subsidize local production of insulated Kenya Ceramic Jikos (KCJ) and expand farm agroforestry.",
                            "explanation": "Insulated KCJ stoves cut wood fuel consumption by 50%, while farm agroforestry provides a sustainable wood supply, directly halting deforestation."
                        }
                    }
                ],
                # Page 14
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Checkpoint 1: Management vs Conservation",
                        "content": {
                            "question": "Which of the following represents a national Energy Management policy rather than a consumer Conservation measure?",
                            "options": [
                                "Turning off household lights when leaving a room.",
                                "Levying higher import tariffs on high-engine-capacity luxury motor vehicles.",
                                "Servicing a car engine to improve fuel combustion.",
                                "Using a solar water heater at home."
                            ],
                            "correct_answer": 1,
                            "explanation": "Levying higher import tariffs on large-engine cars is a macro-level government policy (Energy Management), whereas the others are consumer efficiency actions (Conservation)."
                        }
                    }
                ],
                # Page 15
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Checkpoint 2: Conservation Technologies",
                        "content": {
                            "question": "How does the Kenya Ceramic Jiko (KCJ) cut household charcoal consumption by 50% compared to traditional open stoves?",
                            "options": [
                                "It burns petroleum liquid gas instead of charcoal.",
                                "Its inner insulating ceramic clay liner retains heat and directs it upward to the pot, eliminating thermal waste.",
                                "It operates using wind turbine electricity.",
                                "It requires no air intake draft."
                            ],
                            "correct_answer": 1,
                            "explanation": "The inner ceramic clay liner insulates the firebox, retaining heat and focusing it directly on the cooking pot to cut charcoal use by half."
                        }
                    }
                ],
                # Page 16
                [
                    {
                        "type": "summary",
                        "title": "Topic 4 Mastery Synthesis & Complete Review",
                        "content": {
                            "title": "Topic 4 Mastery Synthesis & Complete Review",
                            "summary_points": [
                                "Energy is classified into Renewable (solar, wind, geothermal, hydro, tides, biomass, animals) and Non-Renewable (coal, petroleum, gas, uranium).",
                                "Solar energy utilizes thermal heat panels and semiconductor photovoltaic cells.",
                                "Geothermal power taps magmatic high-pressure steam along the Great Rift Valley (Olkaria, Lake Bogoria).",
                                "HEP site selection requires large water volume, waterfalls, deep narrow gorges, and hard impervious bedrock.",
                                "The Seven Forks Scheme features Masinga, Kamburu, Gitaru, Kindaruma, and Kiambere dams along River Tana.",
                                "Oil crises are caused by OPEC quotas and Middle East geopolitics, driving inflation, agricultural fertilizer decline, and deforestation.",
                                "Energy Management operates at policy level (public transport, engine caps, afforestation); Energy Conservation operates at consumer level (KCJ stoves, solar heaters, turning off lights)."
                            ]
                        }
                    }
                ]
            ]
        }
    ]

def ingest_form4_geography_topic4(replace=False):
    print("=" * 80)
    print("VLearn Form 4 Geography — Topic 4: Energy")
    print("High-Structure Production Ingestion Engine")
    print("=" * 80)

    curriculum = Curriculum.objects.filter(name="844").first()
    if not curriculum:
        print("[!] Error: Curriculum '844' not found.")
        return

    grade = Grade.objects.filter(curriculum=curriculum, name="Form 4").first()
    if not grade:
        print("[!] Error: Grade 'Form 4' not found.")
        return

    subject = Subject.objects.filter(grade=grade, name="Geography").first()
    if not subject:
        print("[!] Error: Subject 'Geography' not found under Form 4.")
        return

    print(f"[*] Resolved Target: {curriculum.name} -> {grade.name} -> {subject.name} (ID: {subject.id})")

    topic_name = "Energy"
    topic = Topic.objects.filter(subject=subject, name=topic_name).first()

    if topic and replace:
        print(f"[*] Found existing Topic '{topic_name}' (ID: {topic.id}). Removing for clean replace...")
        topic.delete()
        topic = None

    if not topic:
        topic = Topic.objects.create(
            subject=subject,
            name=topic_name,
            order=4,
            description="Comprehensive syllabus on energy classification, renewable & non-renewable resources, River Tana HEP cascade, Olkaria geothermal, global oil crises, and management & conservation."
        )
        print(f"[+] Created Topic: {topic.name} (ID: {topic.id})")
    else:
        print(f"[*] Using existing Topic: {topic.name} (ID: {topic.id})")

    curriculum_data = build_topic4_curriculum()
    total_lessons = 0
    total_pages = 0
    total_blocks = 0

    with transaction.atomic():
        for unit_data in curriculum_data:
            unit_order = unit_data["unit_order"]
            unit_name = unit_data["unit_name"]
            unit_desc = unit_data["unit_description"]
            lesson_title = unit_data["lesson_title"]
            pages_data = unit_data["pages"]

            learning_unit, _ = LearningUnit.objects.get_or_create(
                topic=topic,
                order=unit_order,
                defaults={"name": unit_name, "description": unit_desc}
            )

            lesson = Lesson.objects.filter(topic=topic, learning_unit=learning_unit).first()
            if lesson:
                lesson.blocks.all().delete()
            else:
                lesson = Lesson.objects.create(
                    topic=topic,
                    learning_unit=learning_unit,
                    title=lesson_title,
                    status="published",
                    version=1
                )
            print(f"  [+] Ingesting Lesson {unit_order}: {lesson.title} (ID: {lesson.id})")

            block_order = 10
            lesson_page_count = len(pages_data)

            for page_idx, page_blocks in enumerate(pages_data, 1):
                first_block_title = page_blocks[0].get("title", f"Page {page_idx}")
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
            print(f"      [OK] Ingested {lesson_page_count} Pages for Lesson {unit_order}.")

    print("=" * 80)
    print("[SUCCESS] Form 4 Geography Topic 4 Ingestion Complete!")
    print(f"[*] Total Lessons Ingested: {total_lessons}")
    print(f"[*] Total Pages Ingested:   {total_pages}")
    print(f"[*] Total Blocks Ingested:  {total_blocks}")
    print("=" * 80)

if __name__ == "__main__":
    replace_flag = "--replace" in sys.argv
    ingest_form4_geography_topic4(replace=replace_flag)
