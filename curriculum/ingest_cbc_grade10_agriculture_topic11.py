"""
VLearn CBC Grade 10 Agriculture — Topic 11: Beekeeping (Apiculture)
Production Ingestion Engine (Deep Senior Secondary Pedagogical Edition)

Curriculum: CBC (ID: 5)
Grade: Grade 10 (ID: 5, Level: 10)
Subject: Agriculture
Topic: Beekeeping (Topic Order: 11)

Decomposed into 8 Learning Units & 8 Published Lessons:
  1. Apiary Siting (5 Pages, 11 Blocks)
  2. Beekeeping Equipment and Protective Gear (5 Pages, 11 Blocks)
  3. Benefits and Ecological Importance of Beekeeping (5 Pages, 11 Blocks)
  4. Stocking a Hive I (Capturing a Swarm and Bait Hives) (5 Pages, 11 Blocks)
  5. Stocking a Hive II (Nucleus Colonies and Package Bees) (5 Pages, 11 Blocks)
  6. Safe Apiary Management Practices (5 Pages, 11 Blocks)
  7. Honey Harvesting Process (Preparation and Extraction) (5 Pages, 11 Blocks)
  8. Module Review and Practical Assessment (8 Pages, 17 Blocks)
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
    """Removes bracket citations and normalizes unicode bullets into standard markdown list items."""
    if not text:
        return ""
    text = re.sub(r'\[(?:\d+|image_\d+|S\d+.*?|[\d,\s]{2,})\]', '', text)
    text = re.sub(r'^[ \t]*[•\u2022][ \t]*', '- ', text, flags=re.MULTILINE)
    text = re.sub(r'([^\n])[ \t]+[•\u2022][ \t]+', r'\1\n- ', text)
    text = re.sub(r'^([^\n\-\*\d\>#][^\n]*)\n(- |\* )', r'\1\n\n\2', text, flags=re.MULTILINE)
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

def build_topic11_curriculum():
    """Returns the comprehensive pedagogical page and block structure for Grade 10 Topic 11: Beekeeping (Apiculture)."""
    return [
        # =====================================================================
        # LESSON 1: Apiary Siting
        # =====================================================================
        {
            "unit_order": 1,
            "unit_name": "Apiary Siting",
            "unit_description": "Definition of apiculture; environmental siting factors (forage within 2–3 km, shallow water source with floating stones/debris, partial canopy shade, windbreak, good drainage); safety distance buffers from schools, roads, and livestock kraals.",
            "lesson_title": "Apiary Siting Dynamics, Microclimate Factors, and Public Safety Buffers",
            "pages": [
                [
                    {
                        "type": "suggested_image",
                        "title": "Beehives Positioned in a Shaded Agronomic Apiary Garden",
                        "content": {
                            "title": "Beehives Positioned in a Shaded Agronomic Apiary Garden",
                            "caption": "A well-sited commercial apiary located under partial tree canopy shade, protected by windbreaks and situated close to clean foraging vegetation."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Apiary Siting",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Define **apiculture (beekeeping)** within sustainable livestock production.",
                                "Analyze environmental siting factors (**bee pasture/forage radius, shallow water sources, wind shelter, drainage**).",
                                "Calculate **safe buffer distances** from human dwellings, schools, roads, and livestock kraals.",
                                "Design an **optimal apiary layout** resistant to predators (honey badgers, safari ants)."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "What is Apiculture?",
                        "content": {
                            "title": "The Science and Agribusiness of Honey Bees",
                            "text": "**Apiculture (beekeeping)** is the deliberate management of honey bee colonies (*Apis mellifera*) in man-made hives to produce honey, beeswax, propolis, royal jelly, and provide vital pollination services.\n\n- **Non-Competitive Agribusiness**: Beekeeping requires minimal land ($<0.1\\text{ hectare}$ for an apiary), low capital investment, and does not compete with traditional crops or livestock for pasture.\n- **Ecological Keystone**: Honey bees are the primary pollinators of terrestrial flowering ecosystems and commercial food crops."
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "Environmental and Biological Siting Requirements",
                        "content": {
                            "title": "Aligning the Apiary with Bee Biology",
                            "text": "1. **Abundant Bee Pasture (Forage)**: Hives must be located within a **2 to 3 km radius** of flowering trees, crops (sunflowers, legumes, avocados, coffee), and wild flora providing continuous nectar and pollen.\n2. **Shallow, Clean Water Source**: Bees consume water to dilute honey for larvae and evaporate water for hive evaporative cooling. Water points must be shallow or fitted with floating twigs/gravel to prevent bees from drowning.\n3. **Shade and Wind Protection**: Place hives under partial tree shade to prevent melting wax combs in the hot afternoon, while allowing morning sunlight to stimulate early foraging. A dense hedge or tree row blocks prevailing winds that drain flight energy.\n4. **Well-Drained Ground**: Avoid damp, waterlogged swamps; high humidity promotes chalkbrood and fungal infections inside the hive."
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Optimal Apiary Siting Layout & Safety Buffers",
                        "content": {
                            "title": "Optimal Apiary Siting Layout & Safety Buffers",
                            "caption": "Site architecture blueprint: 1 Central Shaded Hives on Grease-Coated Stands, 2 Thick Windbreak Live Fence, 3 Shallow Water Point with Floating Twigs, 4 Safety Buffer Zone (≥100m from classrooms/homesteads), 5 2km Foraging Radius."
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "Public Safety, Bio-Security, and Predator Defense",
                        "content": {
                            "title": "Protecting Humans, Animals, and the Colony",
                            "text": "- **Human & Animal Safety Buffers**: Hives must be located **at least 100 meters away** from schools, playgrounds, public roads, and livestock kraals to prevent defensive stinging frenzies.\n- **Predator Defenses**:\n  - *Honey Badgers*: Suspend hives from high, strong galvanized wires ($1.5\\text{ m}$ height) or mount on sturdy iron-pipe stands.\n  - *Safari Ants*: Apply motor grease or used engine oil to hive stand legs, or place stand legs inside cans of soapy water/oil.\n  - *Vandalism*: Install a secure thorny perimeter live fence with a lockable gate."
                        }
                    },
                    {
                        "type": "comparison_table",
                        "title": "Optimal Apiary Siting vs Deficient Site Conditions",
                        "content": {
                            "title": "Apiary Site Selection Matrix",
                            "headers": ["Site Factor", "Optimal Apiary Site", "Unsuitable Hazardous Site", "Agricultural Consequence"],
                            "rows": [
                                ["Forage Proximity", "Within 0.5–2 km of blooming crops/trees", "Over 5 km barren desert or monoculture", "Low honey yield; colony absconding"],
                                ["Water Source", "Shallow stream / trough with floating gravel", "Deep uncovered open tanks", "High worker bee drowning mortality"],
                                ["Canopy & Shade", "Partial light tree shade (east-facing sun)", "Direct unshaded scorching sun or deep swamp", "Melted wax combs; excessive hive humidity"],
                                ["Wind Shelter", "Thick live fence blocking prevailing winds", "Open windswept hilltop ridge", "Flight exhaustion; chilled brood"],
                                ["Public Distance", ">100 m from classrooms & livestock kraals", "Adjacent to school playground or cattle pen", "Mass stinging attacks; public safety emergencies"]
                            ]
                        }
                    }
                ],
                [
                    {
                        "type": "mini_activity",
                        "title": "Field Practical: Apiary Site Audit and Checklist Evaluation",
                        "content": {
                            "title": "Apiary Location Audit Lab",
                            "task": "1. Survey your school compound or local community farm.\n2. Use a 4-point rubric: Forage within 2km (0–5), Water proximity (0–5), Wind/Shade protection (0–5), Safety distance >100m from classrooms (0–5).\n3. Calculate total suitability score (Target: >16/20).\n4. Draft a site recommendation report.",
                            "materials": ["Measuring Wheel / Tape", "Compass", "Site Audit Rubric Sheet"],
                            "safety": "Maintain safe distance from any active wild bee swarms."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Core Summary: Apiary Siting",
                        "content": {
                            "title": "Key Takeaways",
                            "text": "- **Site apiaries within 2–3 km of flowering bee pasture**.\n- **Provide shallow water with floating stones** to prevent drowning.\n- **Maintain a $\\ge 100\\text{ m}$ safety buffer** from schools, roads, and kraals.\n- **Protect hive legs with grease barriers** against safari ants."
                        }
                    }
                ],
                [
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Rationale for Safety Distance Buffers",
                        "content": {
                            "question": "Why is it strictly mandatory under agricultural safety regulations to locate an apiary at least 100 meters away from school classrooms, pedestrian paths, and livestock kraals?",
                            "options": [
                                "Bees cannot fly more than 50 meters from their hive",
                                "Honey bees are defensive insects; loud noises, machinery vibrations, or sudden disturbances near classrooms and kraals can trigger defensive stinging attacks, endangering human life and livestock",
                                "The smell of school food causes honey to ferment inside the hive",
                                "Bees will steal chalk from classrooms"
                            ],
                            "answer": "B",
                            "explanation": "Honey bees (*Apis mellifera*) are territorial and defensive of their brood and honey stores. Vibrations from machinery, shouts, or passing cattle can trigger mass defensive stinging attacks. Maintaining a minimum 100m buffer zone ensures the colony remains undisturbed and protects students and farm animals."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 2: Beekeeping Equipment and Protective Gear
        # =====================================================================
        {
            "unit_order": 2,
            "unit_name": "Beekeeping Equipment and Protective Gear",
            "unit_description": "Hive types (traditional log vs Kenya Top Bar Hive vs Langstroth modular hive with 6.4–9.5 mm bee space); essential tools (bee smoker disrupting alarm pheromone, L-shaped hive tool, soft bee brush); full white PPE suit, wire veil, leather gloves, gumboots.",
            "lesson_title": "Apiary Engineering: Hive Architecture, 'Bee Space', Smokers, and Protective PPE",
            "pages": [
                [
                    {
                        "type": "suggested_image",
                        "title": "Beekeeper Wearing Full Protective White Suit and Smoker",
                        "content": {
                            "title": "Beekeeper Wearing Full Protective White Suit and Smoker",
                            "caption": "A beekeeper completely geared in a smooth white canvas bee suit, wire-mesh veil, long leather gauntlet gloves, and gumboots while inspecting an apiary."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Equipment & PPE",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Compare 3 hive architectures: **Traditional Log Hive, Kenya Top Bar Hive (KTBH), and Langstroth Hive**.",
                                "Explain the revolutionary biological concept of **'Bee Space' ($6.4\\text{--}9.5\\text{ mm}$)**.",
                                "Master the operation and biochemical calming mechanism of the **Bee Smoker (isopentyl acetate suppression)**.",
                                "Assemble and inspect the complete **Beekeeping Personal Protective Equipment (PPE)** ensemble."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Comparative Hive Technologies",
                        "content": {
                            "title": "From Destructive Harvesting to Modular Precision",
                            "text": "1. **Traditional Log Hive**: Hollowed tree trunk with fixed combs. Harvesting requires crushing the entire comb, destroying eggs/brood and killing thousands of bees.\n2. **Kenya Top Bar Hive (KTBH)**: Intermediate trapezoidal wooden box with sloping sides ($60^\\circ$) and movable wooden top bars ($32\\text{--}35\\text{ mm}$ width). Bees build individual hanging combs, allowing selective honey harvesting without disturbing the brood nest.\n3. **Langstroth Hive**: Modern modular vertical-stacking hive system with movable wooden frames holding beeswax foundation sheets. Allows machine centrifugal honey extraction where intact wax combs are returned to the hive for immediate refilling!"
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "The Discovery of 'Bee Space'",
                        "content": {
                            "title": "The Golden Architectural Measurement",
                            "text": "- **Definition**: Discovered by Rev. Lorenzo Langstroth in 1851, **Bee Space** is a precise gap of **$6.4\\text{ to }9.5\\text{ mm}$ (approx. $8\\text{ mm}$)**.\n- **Biological Rule**:\n  - If a gap is **$<6.4\\text{ mm}$**, bees glue it shut with **propolis** (bee glue).\n  - If a gap is **$>9.5\\text{ mm}$**, bees build irregular wild **burr comb** across the space.\n  - If a gap is maintained **between $6.4\\text{ and }9.5\\text{ mm}$**, bees leave it completely open as a passageway, allowing frames to remain easily removable!"
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Essential Beekeeping Tools & Full Protective PPE Suit",
                        "content": {
                            "title": "Essential Beekeeping Tools & Full Protective PPE Suit",
                            "caption": "Equipment blueprint: 1 Bellows Bee Smoker (Puffs cool white smoke), 2 L-shaped Steel Hive Tool, 3 Soft-Bristled Bee Brush, 4 White Canvas Bee Suit with Integrated Wire-Mesh Veil, 5 Heavy Leather Gauntlets & Gumboots."
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "Essential Tools and Protective Gear",
                        "content": {
                            "title": "Operating Safely in the Apiary",
                            "text": "1. **Bee Smoker**: Burns dry natural fuel (maize cobs, coconut husks). The cool white smoke disrupts the alarm pheromone (**isopentyl acetate**) released by guard bees and induces bees to engorge on honey, making them docile.\n2. **Hive Tool**: Heavy flat steel bar used to pry open propolis-sealed lids and lift frame lugs.\n3. **Bee Brush**: Soft horsehair brush used to sweep bees off honeycombs without crushing them.\n4. **Why White Suits?**: Bees are evolutionary programmed to attack dark, hairy surfaces (resembling honey badgers or bears). Smooth, white fabric does not trigger aggressive reflexes."
                        }
                    },
                    {
                        "type": "comparison_table",
                        "title": "Comparison of Traditional, KTBH, and Langstroth Hives",
                        "content": {
                            "title": "Beekeeping Hive Systems Comparison Matrix",
                            "headers": ["Feature / Attribute", "Traditional Log Hive", "Kenya Top Bar Hive (KTBH)", "Modern Langstroth Hive"],
                            "rows": [
                                ["Cost of Construction", "Very low (Local hollowed log)", "Moderate (Locally made timber)", "High (Precision machined timber)"],
                                ["Comb Type", "Fixed wild combs", "Movable hanging combs", "Movable framed combs with foundation"],
                                ["Brood Preservation", "Destroyed during harvest", "Preserved (Brood separated)", "100% preserved (Queen excluder used)"],
                                ["Honey Extraction Method", "Crushing and squeezing", "Crushing / Solar wax melting", "Centrifugal spinning (Comb reused)"],
                                ["Annual Honey Yield", "5 – 10 kg/hive", "15 – 25 kg/hive", "30 – 50 kg/hive"]
                            ]
                        }
                    }
                ],
                [
                    {
                        "type": "mini_activity",
                        "title": "Classroom Practical: Smoker Lighting and Cool Smoke Generation Lab",
                        "content": {
                            "title": "Smoker Operation Practicum",
                            "task": "1. Pack dry wood shavings, maize cobs, or dry grass into the burner chamber.\n2. Ignite fuel from the bottom and pump the bellows until glowing coals form.\n3. Pack green grass on top to filter sparks and produce cool, dense white smoke.\n4. Test smoke on the back of your hand (must feel cool, never hot or burning).",
                            "materials": ["Bee Smoker", "Dry Maize Cobs", "Matches", "Green Leaves"],
                            "safety": "Never blow hot sparks onto bees or dry pasture."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Core Summary: Equipment & PPE",
                        "content": {
                            "title": "Key Takeaways",
                            "text": "- **Langstroth hives preserve combs** using centrifugal extractors.\n- **Bee space is $6.4\\text{--}9.5\\text{ mm}$**, preventing propolis or burr comb.\n- **Smoke suppresses isopentyl acetate alarm pheromones**, calming the colony.\n- **Always wear smooth, white PPE**; bees attack dark, rough surfaces."
                        }
                    }
                ],
                [
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: The Architectural Concept of 'Bee Space'",
                        "content": {
                            "question": "What happens if the gap between wooden frames inside a Langstroth beehive is built wider than 9.5 mm?",
                            "options": [
                                "The bees will glue the frames together with propolis",
                                "The bees will build irregular wild burr combs in the open gap, joining the frames together and making them impossible to remove without tearing the comb",
                                "The bees will abandon the hive immediately",
                                "The queen will refuse to lay worker eggs"
                            ],
                            "answer": "B",
                            "explanation": "Bee space is precisely 6.4mm to 9.5mm. If a gap exceeds 9.5mm, bees treat it as an open cavity and build wild cross-combs (burr comb). If a gap is under 6.4mm, bees seal it with propolis. Only within 6.4–9.5mm do bees leave the space open as a clean walking corridor."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 3: Benefits and Ecological Importance of Beekeeping
        # =====================================================================
        {
            "unit_order": 3,
            "unit_name": "Benefits and Ecological Importance of Beekeeping",
            "unit_description": "Direct products (honey, beeswax, propolis, royal jelly, pollen); indirect crop pollination services (flower fidelity, yield increase in avocados/sunflowers/legumes, biodiversity); smallholder revenue calculations.",
            "lesson_title": "Direct Hive Commodities, Cross-Pollination Ecology, and Agribusiness Financials",
            "pages": [
                [
                    {
                        "type": "suggested_image",
                        "title": "Honey Bee Foraging on Flower and Collecting Pollen",
                        "content": {
                            "title": "Honey Bee Foraging on Flower and Collecting Pollen",
                            "caption": "A worker honey bee gathering nectar and carrying bright yellow pollen in its corbicula (pollen basket), demonstrating the vital ecological service of floral cross-pollination."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Benefits & Pollination",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Catalog the direct commercial commodities harvested from an apiary (**honey, beeswax, propolis, royal jelly, bee venom**).",
                                "Explain how **flower fidelity and insect cross-pollination** multiply agricultural crop yields.",
                                "Analyze the role of honey bees in preserving wild forest biodiversity.",
                                "Calculate **gross revenue and net profit margins** for a smallholder apiary enterprise."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Direct Commercial Hive Products",
                        "content": {
                            "title": "Harvesting Value from the Hive",
                            "text": "1. **Raw Honey**: High-energy natural sweetener containing fructose and glucose, rich in antioxidants and antimicrobial enzymes (inhibine/glucose oxidase).\n2. **Beeswax**: Secreted by abdominal wax glands of young worker bees. Used for candle manufacturing, cosmetics, lip balms, pharmaceutical ointments, and comb foundation sheets.\n3. **Propolis (Bee Glue)**: Resinous plant exudate collected by bees to sanitize the hive. High demand in pharmaceuticals for natural antibiotic, antifungal, and antiviral tinctures.\n4. **Royal Jelly & Pollen**: High-protein superfoods rich in B-vitamins, lipids, and amino acids, sold at premium health prices."
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "The Ecological and Agricultural Pollination Miracle",
                        "content": {
                            "title": "The Billion-Dollar Free Agricultural Service",
                            "text": "- **Flower Fidelity**: A foraging worker bee visits flowers of the **exact same plant species** on a single foraging trip, maximizing successful pollen transfer.\n- **Yield Multiplier**: Entomophilous crops (avocado, passion fruit, sunflower, coffee, legumes, watermelon) achieve **$30\\text{--}100\\%$ higher fruit set, larger fruit size, and uniform seed fill** when hives are sited near fields!\n- **Global Food Security**: Over $35\\%$ of human food crops rely directly on insect pollination, with honey bees providing $>80\\%$ of all commercial pollination labor."
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Economic Products of Apiculture & Crop Pollination Dynamics",
                        "content": {
                            "title": "Economic Products of Apiculture & Crop Pollination Dynamics",
                            "caption": "Apiculture value chain: Direct Products (Honey, Beeswax, Propolis, Royal Jelly) + Indirect Agribusiness Dividends (Avocado, Coffee & Sunflower Crop Cross-Pollination) -> High Smallholder Revenue."
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "Agribusiness Profitability Calculation Exercise",
                        "content": {
                            "title": "Financial Model: 10 Langstroth Hives Enterprise",
                            "text": "Consider a smallholder beekeeper operating **10 Langstroth Hives** in Kenya:\n\n- **Average Yield per Hive**: $30\\text{ kg of refined honey/year}$ ($2\\text{ harvests of }15\\text{ kg}$).\n- **Total Annual Production**: $10 \\times 30\\text{ kg} = 300\\text{ kg of honey}$.\n- **Wholesale Price**: $\\text{KES }900\\text{ per kg}$.\n\n$$\\text{Gross Revenue} = 300\\text{ kg} \\times \\text{KES }900 = \\text{KES }270,000$$\n\n- **Annual Operating Costs** (Packaging jars, labels, smoker fuel, stand maintenance): $\\text{KES }30,000$.\n\n$$\\text{Net Profit} = \\text{KES }270,000 - \\text{KES }30,000 = \\text{KES }240,000\\text{ per year}!$$"
                        }
                    },
                    {
                        "type": "comparison_table",
                        "title": "Economic Valuation of Hive Products and Pollination",
                        "content": {
                            "title": "Apiculture Commercial Value Matrix",
                            "headers": ["Commodity / Service", "Primary Source in Hive", "Commercial Market Application", "Economic Value Rating"],
                            "rows": [
                                ["Refined Table Honey", "Nectar processed by workers", "Food sweetener, natural medicine, brewing", "High (KES 800–1,200/kg)"],
                                ["Beeswax Blocks", "Worker abdominal wax glands", "Cosmetics, candles, shoe polish, foundation", "High (KES 1,000–1,500/kg)"],
                                ["Raw Propolis", "Resin collected from tree buds", "Pharmaceutical tinctures, throat sprays", "Very High (KES 2,000–4,000/kg)"],
                                ["Crop Pollination", "Worker floral foraging trips", "30–100% yield boost in avocado & coffee", "Invaluable (Doubles crop harvest revenue)"]
                            ]
                        }
                    }
                ],
                [
                    {
                        "type": "mini_activity",
                        "title": "Field Practical: Floral Pollination Foraging Survey",
                        "content": {
                            "title": "Bee Flower Fidelity Lab",
                            "task": "1. Spend 20 minutes observing blooming flowers in a bean, sunflower, or avocado plot.\n2. Count the number of honey bees vs other wild insects visiting the blossoms.\n3. Observe whether individual bees switch plant species or stay loyal to one flower type.\n4. Record the color and size of pollen pellets in the bees' hind leg pollen baskets (corbiculae).",
                            "materials": ["Clipboard", "Stopwatch", "Camera / Phone"],
                            "safety": "Do not swat or disturb foraging bees."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Core Summary: Benefits & Pollination",
                        "content": {
                            "title": "Key Takeaways",
                            "text": "- **Direct products include honey, beeswax, and propolis**.\n- **Bees exhibit flower fidelity**, maximizing cross-pollination efficiency.\n- **Pollination increases avocado, coffee, and legume yields** by $30\\text{--}100\\%$.\n- **A 10-hive Langstroth apiary generates over KES 240,000 net profit**."
                        }
                    }
                ],
                [
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Indirect Value of Bee Pollination",
                        "content": {
                            "question": "Which of the following represents the single most economically valuable contribution of honey bees to a mixed crop-livestock smallholder farm in Kenya?",
                            "options": [
                                "The production of propolis used to seal cracks in wooden cattle sheds",
                                "The active cross-pollination of horticultural crops (avocados, passion fruits, legumes), which dramatically boosts fruit set, size, and marketable harvest yields",
                                "The bees scaring away crop-destroying birds with their buzzing sounds",
                                "The bees converting synthetic pesticides into organic fertilizer"
                            ],
                            "answer": "B",
                            "explanation": "While honey and beeswax generate immediate cash, the economic value of honey bees as agricultural pollinators is far greater. By fertilizing blossoms with high flower fidelity, bees ensure maximum fruit set, larger uniform fruit size, and drastically higher crop yields across avocados, coffee, legumes, and oilseeds."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 4: Stocking a Hive I (Capturing a Swarm and Bait Hives)
        # =====================================================================
        {
            "unit_order": 4,
            "unit_name": "Stocking a Hive I (Capturing a Swarm and Bait Hives)",
            "unit_description": "Natural swarming biology; step-by-step wild swarm capture (swarm box/net, securing queen with Nasonov pheromone); bait hive preparation with beeswax, propolis, and lemon grass essential oil.",
            "lesson_title": "Stocking Methodologies I: Swarming Biology, Cluster Capture, and Bait Hive Pheromones",
            "pages": [
                [
                    {
                        "type": "suggested_image",
                        "title": "Wild Honey Bee Swarm Clustered on a Tree Branch",
                        "content": {
                            "title": "Wild Honey Bee Swarm Clustered on a Tree Branch",
                            "caption": "A natural reproductive honey bee swarm clustered tightly around the queen on a low tree limb while scout bees search for a permanent cavity."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Swarm Capture & Baiting",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Explain **swarming** as a natural colony reproductive behavior.",
                                "Execute the step-by-step protocol for **capturing a wild bee swarm cluster**.",
                                "Explain the biological necessity of **securing the queen bee inside the catcher box**.",
                                "Prepare and deploy **bait hives using lemon grass oil, beeswax, and propolis**."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The Biology of Swarming",
                        "content": {
                            "title": "Colony Reproduction in the Wild",
                            "text": "**Swarming** is the natural mechanism by which honey bee colonies reproduce and propagate their genetics across the ecosystem:\n\n- **Trigger**: Occurs during abundant nectar flow when the brood nest becomes overcrowded.\n- **The Departure**: The old queen leaves the hive with approximately $50\\text{--}60\\%$ of the worker workforce, leaving behind capped queen cells to rear a new virgin queen.\n- **Temporary Cluster**: The departing swarm clusters on a tree branch while scout bees search for a dark, dry, secure cavity.\n- **Docile Temperament**: Clustered swarm bees have gorged on honey reserves and have no brood comb to defend, making them remarkably gentle and easy to capture!"
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "Step-by-Step Wild Swarm Capture Protocol",
                        "content": {
                            "title": "Securing the Colony Safely",
                            "text": "1. **Wear Full Protective PPE**: Always suit up completely with veil and gloves.\n2. **Position the Swarm Catcher Box / Net**: Hold a well-ventilated collection box or canvas swarm net directly beneath the hanging cluster.\n3. **The Firm Downward Shake**: Give the branch a single, sharp downward shake. The bee cluster will drop into the catcher box.\n4. **THE QUEEN PRINCIPLE**: If the **queen bee** is inside the box, the remaining worker bees will voluntarily march in, guided by her **Nasonov attraction pheromone**.\n5. **Transfer at Dusk**: Leave the box shaded until sunset, then transfer frames into the permanent hive."
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Swarm Capture & Bait Hive Pheromone Preparation",
                        "content": {
                            "title": "Swarm Capture & Bait Hive Pheromone Preparation",
                            "caption": "Stocking methodologies: Left: Swarm Cluster Capture (Box directly below, sharp shake, securing queen) | Right: Bait Hive Architecture (Mounted 2–3m high in tree, rubbed with Lemon Grass Oil & Beeswax)."
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "Bait Hive Technology & Pheromone Attractants",
                        "content": {
                            "title": "Passive, Low-Labor Apiary Colonization",
                            "text": "- **What is a Bait Hive?**: A clean, empty hive box positioned strategically to attract passing scout bees searching for a nesting home.\n- **Pheromone Attractants**:\n  - **Lemon Grass Essential Oil (*Cymbopogon*)**: Contains citral and geraniol, which chemically mimic the bee's natural **Nasonov orientation pheromone**.\n  - **Melted Beeswax & Propolis**: Rubbing the inner walls and entrance with wax and propolis gives the hive an established, sterile colony aroma.\n  - **Old Dark Brood Comb**: Placing one clean, empty dark comb inside is the most potent natural scout attractant.\n- **Siting**: Mount the bait hive **$2\\text{ to }3\\text{ meters}$ high** in a semi-shaded tree facing east near water."
                        }
                    },
                    {
                        "type": "comparison_table",
                        "title": "Swarm Capture vs Bait Hive Stocking Comparison",
                        "content": {
                            "title": "Stocking Strategy Matrix",
                            "headers": ["Stocking Parameter", "Direct Wild Swarm Capture", "Passive Bait Hive Deployment"],
                            "rows": [
                                ["Capital Cost", "Zero (Uses existing boxes/nets)", "Zero (Uses standard hive box)"],
                                ["Labor Requirement", "Active (Locating & climbing to shake cluster)", "Passive (Set it and wait for scouts)"],
                                ["Colonization Speed", "Instant (Colony secured in minutes)", "Seasonal (Relies on swarming season)"],
                                ["Colony Temperament", "Variable (Wild genetics)", "Variable (Local indigenous bees)"],
                                ["Success Rate", "High (If queen is captured inside box)", "Moderate to High (When baited with lemon grass)"]
                            ]
                        }
                    }
                ],
                [
                    {
                        "type": "mini_activity",
                        "title": "Laboratory Practical: Bait Hive Pheromone Preparation Lab",
                        "content": {
                            "title": "Bait Hive Scenting Practicum",
                            "task": "1. Clean and scrape the interior of an empty Top Bar or Langstroth hive box.\n2. Melt 50g of clean beeswax and brush along top bars / frame guides.\n3. Apply 3–5 drops of pure lemon grass essential oil around the entrance hole and inner lid.\n4. Mount the hive 2.5 meters high in a secure school farm tree facing east.",
                            "materials": ["Empty Hive Box", "Beeswax", "Lemon Grass Oil", "Mounting Wires"],
                            "safety": "Ensure secure ladder work when mounting hives in trees."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Core Summary: Swarm Capture & Baiting",
                        "content": {
                            "title": "Key Takeaways",
                            "text": "- **Swarming is natural colony reproduction**; bees are calm while clustering.\n- **Securing the queen inside the catcher box** guarantees worker compliance.\n- **Lemon grass oil mimics Nasonov pheromones**, attracting scout bees.\n- **Mount bait hives 2–3 meters high** in shaded trees."
                        }
                    }
                ],
                [
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Rationale for Queen Capture",
                        "content": {
                            "question": "When capturing a wild bee swarm hanging from a tree branch, why is it absolutely essential to ensure that the queen bee drops inside the collection container?",
                            "options": [
                                "The queen is the only bee with wings and must fly the workers to the new hive",
                                "The worker bees are bound to the queen by her Nasonov and queen mandibular pheromones; if she is inside the box, the workers will voluntarily follow her scent and settle peacefully",
                                "The queen bee eats the container to make wax",
                                "Without the queen, worker bees turn into wasps within 30 minutes"
                            ],
                            "answer": "B",
                            "explanation": "Colony cohesion is governed by pheromones. If the queen drops into the collection container, worker bees fanning at the entrance release Nasonov pheromones, guiding the entire airborne swarm to march inside. If the queen is left on the branch, the workers will abandon the box and return to her."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 5: Stocking a Hive II (Nucleus Colonies and Package Bees)
        # =====================================================================
        {
            "unit_order": 5,
            "unit_name": "Stocking a Hive II (Nucleus Colonies and Package Bees)",
            "unit_description": "Nucleus colonies (4–5 frames of brood, honey, queen, workers); frame-by-frame transfer in exact sequence; package bees (1–2 kg loose bees + queen cage with slow-release sugar candy plug to prevent balling).",
            "lesson_title": "Stocking Methodologies II: Nucleus Colony Transfers, Package Bees, and Slow-Release Queen Cages",
            "pages": [
                [
                    {
                        "type": "suggested_image",
                        "title": "Beekeeper Inspecting a Wooden Frame Covered with Worker Bees and Brood",
                        "content": {
                            "title": "Beekeeper Inspecting a Wooden Frame Covered with Worker Bees and Brood",
                            "caption": "A beekeeper lifting a brood frame from an established nucleus colony, verifying the presence of pearly-white larvae, capped honey, and a mated laying queen."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Nuc & Package Stocking",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Define a **nucleus colony (nuc)** and identify its 5 critical biological components.",
                                "Execute the step-by-step **frame-by-frame nuc transfer protocol** without crushing bees.",
                                "Explain the **package bees methodology** and queen cage architecture.",
                                "Analyze why a **slow-release sugar candy plug** prevents worker bees from balling and killing an unfamiliar queen."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "What is a Nucleus Colony (Nuc)?",
                        "content": {
                            "title": "The Fully Functional Mini-Colony",
                            "text": "A **nucleus colony (nuc)** is a small, established, actively laying colony contained in a compact 4–5 frame transport box:\n\n- **Components**: Contains **4 to 5 standard frames** holding capped worker brood, open eggs/larvae, pollen reserves, capped honey, a certified mated **laying queen**, and thousands of worker bees.\n- **High Reliability**: Unlike wild swarms (which must build comb from scratch), a nuc is already established and expands to full production capacity within **4 to 6 weeks**!"
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "Frame-by-Frame Transfer Protocol",
                        "content": {
                            "title": "Zero-Crush Transfer Technique",
                            "text": "1. **Set Up & Light Smoke**: Place the permanent Langstroth hive box on its stand. Puff gentle cool smoke into the nuc entrance.\n2. **Maintain Frame Sequence**: Gently lift each frame using a hive tool. Transfer the frames into the permanent hive in the **EXACT SAME sequential order and orientation** they occupied in the nuc (preserving the central brood nest core).\n3. **Insert Blank Foundation Frames**: Fill the remaining outer spaces with new wax foundation frames to allow expansion.\n4. **Shake Residue Bees**: Shake any loose bees remaining in the nuc transport box into the top of the new hive, close the lid, and let them settle."
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Nucleus Colony Frame Transfer & Queen Cage Integration",
                        "content": {
                            "title": "Nucleus Colony Frame Transfer & Queen Cage Integration",
                            "caption": "Technical stocking guide: Left: 5-Frame Nuc Transfer into Langstroth Hive (Preserving Brood Core) | Right: Package Bees Queen Cage with Slow-Release Sugar Candy Plug (Prevents Queen Balling)."
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "Package Bees and the Queen Cage Candy Plug",
                        "content": {
                            "title": "Introducing Foreign Queens Without Fatal Aggression",
                            "text": "- **Package Bees**: A screened box containing $1.0\\text{ to }1.5\\text{ kg}$ of loose worker bees (approx. 10,000 bees), a can of sugar syrup, and a separate **queen cage**.\n- **The Threat of Queen Balling**: If an unfamiliar queen is released instantly, the foreign worker bees do not recognize her scent and will attack, surround, and overheat her to death (**balling the queen**).\n- **The Slow-Release Solution**: The queen is suspended in a wooden cage sealed with a **hard sugar candy plug**. Over **48 to 72 hours**, the workers slowly eat through the sugar plug. By the time the queen emerges, the workers have absorbed her pheromones and accept her peacefully as their mother!"
                        }
                    },
                    {
                        "type": "suggested_video",
                        "title": "How to Transfer a Nucleus Bee Colony to a Langstroth Hive",
                        "content": {
                            "title": "How to Transfer a Nucleus Bee Colony to a Langstroth Hive",
                            "description": "Agronomic video guide demonstrating frame inspection, queen verification, sequential frame transfer, and foundation insertion.",
                            "url": "https://www.youtube.com/watch?v=nucs-transfer-guide"
                        }
                    }
                ],
                [
                    {
                        "type": "comparison_table",
                        "title": "Stocking Methods Comparison Matrix",
                        "content": {
                            "title": "Hive Stocking Methodology Matrix",
                            "headers": ["Stocking Method", "Startup Cost", "Time to First Honey Harvest", "Risk of Absconding", "Technical Skill Required"],
                            "rows": [
                                ["Wild Swarm Capture", "Free (KES 0)", "4 – 6 Months (Must build comb)", "Moderate (May leave if dissatisfied)", "Moderate (Climbing & handling)"],
                                ["Bait Hive Attraction", "Free (KES 0)", "4 – 6 Months", "Low (Chose site voluntarily)", "Low (Passive placement)"],
                                ["Nucleus Colony (Nuc)", "Moderate (KES 4,000–6,000)", "6 – 8 Weeks (Rapid expansion)", "Very Low (Brood anchors colony)", "Low to Moderate"],
                                ["Package Bees + Queen", "Moderate (KES 3,500–5,000)", "3 – 4 Months", "Low (Once queen is accepted)", "High (Requires candy release care)"]
                            ]
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Core Summary: Nucs & Package Bees",
                        "content": {
                            "title": "Key Takeaways",
                            "text": "- **Nucleus colonies contain 4–5 established frames** with a mated queen.\n- **Transfer nuc frames in the exact same sequence** to protect brood.\n- **Package bees require a slow-release queen cage**.\n- **The sugar candy plug prevents queen balling** over 48–72 hours."
                        }
                    }
                ],
                [
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Rationale for Queen Cage Sugar Plug",
                        "content": {
                            "question": "Why is a queen bee shipped with package bees housed inside a separate wooden cage sealed with a hard sugar candy plug, rather than being released freely with the workers?",
                            "options": [
                                "The queen requires concentrated sugar to produce eggs during transit",
                                "The package worker bees are strangers to the queen; the 48–72 hour delay while workers eat through the candy plug allows them to groom her, absorb her pheromones, and accept her without attacking and balling her to death",
                                "The sugar plug prevents the queen from flying out through the transport mesh",
                                "To teach the worker bees how to chew candy"
                            ],
                            "answer": "B",
                            "explanation": "Package bees are assembled from diverse colonies and do not recognize the queen's pheromones. If released immediately, they would treat her as an invader and kill her (balling). The sugar candy plug forces a 2–3 day delay, during which her scent permeates the hive, ensuring full acceptance upon emergence."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 6: Safe Apiary Management Practices
        # =====================================================================
        {
            "unit_order": 6,
            "unit_name": "Safe Apiary Management Practices",
            "unit_description": "Routine 1–2 week hive inspections (stand at side/rear, cool smoke, queen laying check); seasonal 1:1 sugar syrup feeding; swarm prevention; biological defense (grease barriers on posts against safari ants, hanging wires against honey badgers, wax moth and foulbrood control).",
            "lesson_title": "Apiary Management: Routine Hive Inspections, Dearth Feeding, and Pest & Disease Defense",
            "pages": [
                [
                    {
                        "type": "suggested_image",
                        "title": "Beekeeper Puffing Cool Smoke into Hive During Routine Inspection",
                        "content": {
                            "title": "Beekeeper Puffing Cool Smoke into Hive During Routine Inspection",
                            "caption": "A beekeeper using a smoker to calm honey bees before removing hive lids, standing safely at the side of the entrance to avoid obstructing worker flight lines."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Apiary Management",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Execute **routine hive inspections every 1–2 weeks** safely.",
                                "Formulate and administer **seasonal 1:1 sugar syrup supplemental feeds**.",
                                "Deploy **swarm prevention strategies** (adding supers, splitting colonies).",
                                "Defend hives against major pests (**safari ants, honey badgers, wax moths**) and diseases (**foulbrood**)."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Routine Inspection Protocols & Smoker Mastery",
                        "content": {
                            "title": "The Bi-Weekly Colony Health Audit",
                            "text": "1. **Safe Physical Positioning**: Always stand at the **side or rear of the hive**—never stand directly in front of the entrance hole, which blocks foraging flight paths and triggers guard bee attacks.\n2. **The 3-Step Smoke Routine**:\n- Step 1: Puff 2–3 gentle puffs of cool white smoke into the entrance; wait **60 seconds**.\n- Step 2: Pry the lid open slightly and puff smoke under the inner cover.\n- Step 3: Puff smoke across frame tops.\n3. **Inspection Checklist**: Verify the queen's presence (fresh eggs in cell bottoms and healthy pearly-white C-shaped larvae), assess honey/pollen stores, check for queen swarm cells, and inspect for pests."
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "Dearth Feeding and Swarm Prevention",
                        "content": {
                            "title": "Active Colony Sustenance & Management",
                            "text": "- **Dearth Season Supplemental Feeding**: During prolonged dry seasons or cold rains when floral nectar ceases, feed colonies **1:1 sugar-to-water syrup** or pollen substitutes in clean internal feeders. This prevents colony starvation and stops them from **absconding** (completely abandoning the hive).\n- **Swarm Prevention**: When strong colonies fill all frames during peak honey flow, they prepare to swarm (rearing queen cells). Prevent workforce loss by **adding empty honey supers on top**, removing excess queen cups, or artificially splitting the colony into a new nuc."
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Apiary Pest Defense & Safari Ant Post Grease Barriers",
                        "content": {
                            "title": "Apiary Pest Defense & Safari Ant Post Grease Barriers",
                            "caption": "Integrated pest defense system: 1 Heavy-Duty Grease / Used Engine Oil Barrier on Stand Legs (Blocks Safari Ants), 2 Suspended 1.5m Steel Cables (Blocks Honey Badgers), 3 Entrances Squeezed to 8mm (Blocks Wax Moths), 4 Clean Apiary Undergrowth."
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "Pest & Disease Defense Systems",
                        "content": {
                            "title": "Guarding the Apiary from Biological Invaders",
                            "text": "1. **Safari Ants (*Dorylus* spp.)**: Can slaughter an entire colony in hours.\n- *Defense*: Apply a **10 cm thick ring of motor grease or used engine oil** on all hive stand posts, or place legs in water/oil tins. Keep grass slashed low around stands.\n2. **Honey Badgers (*Mellivora capensis*)**: Heavy predators that smash wooden boxes.\n- *Defense*: Suspend hives from high galvanized steel wires ($1.5\\text{ m}$ height) or build welded angle-iron cages.\n3. **Wax Moths (*Galleria mellonella*)**: Caterpillars tunnel through and destroy combs in weak hives. Maintain strong colonies and reduce entrance size.\n4. **Foulbrood (Bacterial Spores)**: American/European Foulbrood rots larvae into a dark, foul-smelling goo. Infected frames must be burned immediately."
                        }
                    },
                    {
                        "type": "comparison_table",
                        "title": "Major Apiary Pests, Damage, and Organic Defense Protocols",
                        "content": {
                            "title": "Apiary Pest Defense Matrix",
                            "headers": ["Apiary Pest / Pathogen", "Type of Threat", "Damage Inflicted", "Recommended Preventative Control"],
                            "rows": [
                                ["Safari Ants (Dorylus)", "Carnivorous ant swarm", "Invasively kills all bees; loots honey", "Grease / used engine oil barrier on stand legs"],
                                ["Honey Badger", "Carnivorous mammal", "Smashes wooden hives; eats brood/honey", "Suspend hives on 1.5m steel wires / iron cages"],
                                ["Greater Wax Moth", "Lepidopteran pest", "Caterpillars eat wax combs, destroying frames", "Maintain strong colonies; trap adult moths"],
                                ["Small Hive Beetle", "Coleopteran pest", "Larvae ferment honey into slime", "Install oil traps inside hive; compact soil"],
                                ["Foulbrood Bacteria", "Bacterial brood pathogen", "Rots larvae; causes sour foul odor", "Sterilize tools; burn heavily infected frames"]
                            ]
                        }
                    }
                ],
                [
                    {
                        "type": "mini_activity",
                        "title": "Field Practical: Applying Grease Barriers and Preparing 1:1 Sugar Syrup",
                        "content": {
                            "title": "Apiary Defense & Supplemental Feeding Practicum",
                            "task": "1. Clear grass and undergrowth within a 3-meter radius of the school apiary stands.\n2. Apply a thick 10 cm band of automotive grease around each hive support post.\n3. Boil 1 liter of clean water, dissolve 1 kg of white cane sugar (1:1 ratio), and let it cool.\n4. Fill an internal entrance feeder and install it into a weak hive.",
                            "materials": ["Automotive Grease", "1kg Cane Sugar", "Clean Water", "Feeder Bottle"],
                            "safety": "Ensure syrup is fully cooled before feeding to avoid scalding bees."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Core Summary: Apiary Management",
                        "content": {
                            "title": "Key Takeaways",
                            "text": "- **Inspect hives every 1–2 weeks**, standing at the side/rear.\n- **Feed 1:1 sugar syrup during dry dearth periods** to prevent absconding.\n- **Prevent swarming by adding supers** during peak nectar flows.\n- **Grease stand posts to block safari ants**; hang hives to deter honey badgers."
                        }
                    }
                ],
                [
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Safari Ant Prevention Strategy",
                        "content": {
                            "question": "A smallholder beekeeper observes safari ants advancing toward her apiary in central Kenya. What is the most effective and safe preventative barrier to deploy?",
                            "options": [
                                "Spray broad-spectrum organophosphate chemical insecticides directly into the hive entrances",
                                "Apply a thick 10cm ring of automotive grease or used engine oil around all hive stand support posts and slash surrounding vegetation",
                                "Remove the bees and keep them in the living room",
                                "Pour boiling water over the top of the hives"
                            ],
                            "answer": "B",
                            "explanation": "Automotive grease or used engine oil creates a sticky, hydrophobic mechanical barrier that crawling safari ants cannot cross. Spraying synthetic insecticides (Option A) would contaminate the honey and kill the bee colony itself."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 7: Honey Harvesting Process (Preparation and Extraction)
        # =====================================================================
        {
            "unit_order": 7,
            "unit_name": "Honey Harvesting Process (Preparation and Extraction)",
            "unit_description": "Honey ripeness (75–80% capped comb cells, <18% moisture); smoke and bee brushing; extraction in bee-proof room (heated uncapping knife/fork, centrifugal extractor, multi-stage filtering, 24–48h settling, skimming foam, hermetic bottling).",
            "lesson_title": "Honey Harvesting Mechanics: Ripeness Capping, Uncapping, Centrifugal Extraction, and Bottling",
            "pages": [
                [
                    {
                        "type": "suggested_image",
                        "title": "Honeycomb Frame with Capped Ripe Honey Cells",
                        "content": {
                            "title": "Honeycomb Frame with Capped Ripe Honey Cells",
                            "caption": "A prime honey frame showing over 80% of cells sealed with white beeswax capping, indicating moisture content below 18% and perfect ripeness for harvesting."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Honey Harvesting & Processing",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Identify the biological indicator of **honey ripeness ($75\\text{--}80\\%$ capped cells, $<18\\%$ moisture)**.",
                                "Execute safe **frame harvesting protocols** (smoking, lifting, bee brushing, lidded buckets).",
                                "Operate a **heated uncapping knife and centrifugal honey extractor**.",
                                "Execute **multi-stage mesh filtering, 48-hour settling, foam skimming, and hermetic bottling**."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Determining Honey Ripeness: The 80% Capping Rule",
                        "content": {
                            "title": "The Moisture Threshold of Quality Honey",
                            "text": "Honey must be harvested **only when fully ripe**:\n\n- **The Evaporation Process**: Worker bees regurgitate nectar into cells and fan their wings continuously to evaporate water until moisture drops **below $18\\%$**.\n- **The Wax Cap**: Once moisture reaches $\\le 18\\%$, worker bees seal the cell with a thin airtight beeswax cap.\n- **THE HARVEST RULE**: A frame is ready for extraction when at least **$75\\text{ to }80\\%$ of the comb cells are capped**!\n- *DANGER OF UNCAPPED HONEY*: Uncapped honey has high water content ($>20\\%$). Harvesting uncapped honey allows wild yeasts (*Saccharomyces*) to ferment sugars into alcohol and acetic acid, souring and ruining the entire batch!"
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "Harvesting Honey Frames from the Apiary",
                        "content": {
                            "title": "Extracting Frames Without Triggering Robbing",
                            "text": "1. **Preparation**: Put on full PPE; prepare the smoker and **clean food-grade buckets with airtight lids**.\n2. **Calm the Colony**: Blow gentle smoke into the entrance; open the super lid and identify fully capped frames.\n3. **Remove and Brush**: Lift the frame. Give it a gentle shake over the open hive to dislodge most bees, then use a **soft bee brush** to sweep remaining bees back into the hive.\n4. **THE AIRTIGHT COVER RULE**: Place harvested frames into a lidded bucket immediately. Open honey frames in the apiary trigger an uncontrollable **robbing frenzy** among neighboring hives!"
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Step-by-Step Honey Harvesting & Centrifugal Extraction Pipeline",
                        "content": {
                            "title": "Step-by-Step Honey Harvesting & Centrifugal Extraction Pipeline",
                            "caption": "Complete processing pipeline: 1 Selection of ≥80% Capped Frames -> 2 Uncapping with Heated Knife -> 3 Centrifugal Extractor Spinning -> 4 Multi-Stage Mesh Filtration -> 5 48h Settling Tank & Foam Skimming -> 6 Clean Glass Jar Bottling."
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "Extraction, Multi-Stage Filtration, Settling, and Bottling",
                        "content": {
                            "title": "The Hygienic Processing Suite",
                            "text": "Processing must occur in a clean, screened, **bee-proof room**:\n1. **Uncapping**: Use a heated **uncapping knife** or uncapping fork to slice off the thin wax caps from both sides of the comb into an uncapping tray.\n2. **Centrifugal Extraction**: Place uncapped frames into a **centrifugal honey extractor**. Hand-cranking or motor spinning generates centrifugal force that flings liquid honey against the outer stainless-steel wall without damaging the delicate comb structure (allowing frames to be returned to hives!).\n3. **Multi-Stage Filtration**: Pass honey through a coarse sieve ($1\\text{ mm}$) to remove large wax pieces, followed by a fine nylon mesh ($200\\text{ microns}$) to remove micro-debris.\n4. **Settling & Skimming**: Let honey stand in a settling tank for **24 to 48 hours**. Air bubbles and pollen foam rise to the surface and are skimmed off.\n5. **Hermetic Packaging**: Bottle clear honey into sterile, dry glass jars with airtight lids."
                        }
                    },
                    {
                        "type": "comparison_table",
                        "title": "Honey Extraction Methods Comparison",
                        "content": {
                            "title": "Extraction Technologies Matrix",
                            "headers": ["Extraction Parameter", "Traditional Squeeze Pressing", "Solar Wax Melting Extraction", "Centrifugal Mechanical Extractor"],
                            "rows": [
                                ["Comb Preservation", "Destroyed (Crushed completely)", "Melted (Combs destroyed)", "100% Intact (Preserved for immediate reuse)"],
                                ["Honey Purity", "Cloudy (Contains crushed brood/wax)", "Darkened by heat degradation", "Crystal clear, raw, unheated, premium quality"],
                                ["Bees Energy Saved", "Zero (Bees must rebuild combs)", "Zero (Bees must rebuild combs)", "Massive (Saves 8kg honey per 1kg wax rebuilt!)"],
                                ["Processing Speed", "Slow and messy", "Slow (Weather dependent)", "Rapid (Extracts 20 frames in 15 minutes)"]
                            ]
                        }
                    }
                ],
                [
                    {
                        "type": "mini_activity",
                        "title": "Laboratory Practical: Multi-Stage Honey Filtration and Moisture Testing",
                        "content": {
                            "title": "Honey Processing and Quality Testing Lab",
                            "task": "1. Set up a multi-stage filter stack (Coarse stainless sieve on top, fine nylon mesh underneath).\n2. Pour raw extracted honey through the filters into a clean settling bucket.\n3. Use an optical honey refractometer: place 2 drops on the prism and read moisture % (Target: <18%).\n4. Bottle filtered honey into a sanitized glass jar and seal hermetically.",
                            "materials": ["Raw Honey", "Filter Stack", "Honey Refractometer", "Glass Jars"],
                            "safety": "Wear sterile aprons and hairnets; maintain strict food hygiene."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Core Summary: Harvesting & Processing",
                        "content": {
                            "title": "Key Takeaways",
                            "text": "- **Harvest only when $\\ge 75\\text{--}80\\%$ of cells are capped** ($<18\\%$ moisture).\n- **Centrifugal extractors fling honey out** while preserving the wax comb.\n- **Multi-stage filtration removes wax bits** and micro-debris.\n- **Settle honey for 24–48 hours** to skim off air foam before hermetic bottling."
                        }
                    }
                ],
                [
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Rationale for 80% Comb Capping",
                        "content": {
                            "question": "Why is it an essential quality and agricultural standard to harvest honeycombs only when at least 75% to 80% of the cells are sealed with wax capping?",
                            "options": [
                                "Uncapped honey is too hard to spin in an extractor",
                                "Capped honey has been reduced by bees to below 18% moisture; harvesting uncapped honey introduces high water content that allows wild yeasts to ferment and spoil the honey into sour vinegar",
                                "The wax caps contain food coloring that makes honey dark",
                                "Uncapped cells contain bee venom that must dry out"
                            ],
                            "answer": "B",
                            "explanation": "Bees cap cells only when they have evaporated water down to safe levels (<18% moisture). Uncapped honey has high moisture content (>20%). Harvesting uncapped honey allows osmotic wild yeasts (*Zygosaccharomyces*) to ferment the sugars, producing carbon dioxide foam, alcohol, and acetic acid (sour spoilage)."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 8: Module Review and Practical Assessment
        # =====================================================================
        {
            "unit_order": 8,
            "unit_name": "Module Review and Practical Assessment",
            "unit_description": "Master apiculture synthesis; Case of the Foamy Honey diagnostic audit; 8 Summative Topic Assessment MCQs covering the complete Topic 11 module.",
            "lesson_title": "Synthesis of Apiculture Systems, Quality Diagnostics, and Summative Assessment",
            "pages": [
                [
                    {
                        "type": "suggested_image",
                        "title": "Pure Golden Harvested Honey Displayed in Sealed Glass Jars",
                        "content": {
                            "title": "Pure Golden Harvested Honey Displayed in Sealed Glass Jars",
                            "caption": "Clear, premium-grade bottled honey jars displayed for market sale, representing the culmination of proper apiary siting, hive management, and hygienic extraction."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Synthesis & Summative Assessment",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Synthesize the **complete Beekeeping (Apiculture) framework**.",
                                "Complete the **'Case of the Foamy Honey' diagnostic quality audit**.",
                                "Draft a **Smallholder Apiculture Agribusiness Proposal**.",
                                "Complete the comprehensive **Summative Topic Assessment** covering all 8 lessons of Topic 11."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Master Apiculture Enterprise Systems & Quality Synthesis",
                        "content": {
                            "title": "The Unified Framework of Modern Apiculture",
                            "text": "1. **Siting**: $2\\text{--}3\\text{ km}$ forage, shallow water, windbreaks, $\\ge 100\\text{ m}$ safety buffer from schools and kraals.\n2. **Hives & Bee Space**: Langstroth modular boxes utilizing $6.4\\text{--}9.5\\text{ mm}$ bee space; KTBH intermediate bars; traditional log hives.\n3. **Tools & PPE**: Bee smoker (isopentyl acetate suppression), L-tool, soft brush, full white canvas suit.\n4. **Stocking**: Swarm cluster capture, lemon grass baited hives, nucleus colony transfers (preserving frame sequence), package bees with candy-plug cages.\n5. **Management**: Bi-weekly inspections, 1:1 sugar dearth feeding, post grease barriers against safari ants, wire hanging against honey badgers.\n6. **Harvesting & Purity**: $80\\%$ capping indicator ($<18\\%$ moisture), centrifugal extraction, multi-stage filtering, 48h settling, hermetic glass packaging."
                        }
                    }
                ],
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Master Apiculture Enterprise Systems & Quality Synthesis",
                        "content": {
                            "title": "Master Apiculture Enterprise Systems & Quality Synthesis",
                            "caption": "Master apiculture architecture: 1 Apiary Siting & Safety -> 2 Hive Architecture & Tools -> 3 Stocking Protocols -> 4 Routine Pest Management -> 5 Harvesting & Extraction -> 6 Premium Marketed Commodities & Crop Pollination."
                        }
                    },
                    {
                        "type": "comparison_table",
                        "title": "Master Apiculture Troubleshooting and Action Guide",
                        "content": {
                            "title": "Apiculture Diagnostic Action Matrix",
                            "headers": ["Apiary Observation / Crisis", "Root Cause Diagnosis", "Immediate Corrective Action", "Long-Term Prevention"],
                            "rows": [
                                ["Harvested bottled honey forms white foam and smells sour", "Harvested uncapped frames (>20% moisture); yeast fermentation", "Discard fermented batch or use for cooking vinegar", "Enforce the 80% capping rule (<18% moisture)"],
                                ["Safari ants marching up hive stand posts", "Undergrowth bridging to hive; lack of barrier", "Apply 10cm grease/oil band on posts immediately", "Clear grass in 3m radius; maintain grease rings"],
                                ["Bees building irregular wild cross-combs between frames", "Frame spacing exceeds 9.5mm (Violation of Bee Space)", "Trim burr comb with hive tool; space frames correctly", "Use precision 35mm self-spacing Langstroth frames"],
                                ["Colony suddenly absconds (leaves hive empty)", "Starvation during dry dearth / severe ant invasion", "Clean and bait empty hive with lemon grass oil", "Provide 1:1 sugar syrup feeding during dry seasons"],
                                ["Worker bees balling and stinging a newly introduced queen", "Queen released too rapidly before pheromone adaptation", "Rescue queen into cage; re-candy the exit plug", "Ensure 48–72h slow-release sugar candy plug"]
                            ]
                        }
                    }
                ],
                [
                    {
                        "type": "mini_activity",
                        "title": "Performance Task: The 'Case of the Foamy Honey' Quality Audit",
                        "content": {
                            "title": "Commercial Honey Quality Consulting Case",
                            "task": "A student harvested honey from 5 uncapped combs, crushed them in a cloth, filtered once, and bottled immediately. After 3 weeks, bottles swelled, foamed, and smelled sour.\n\n**Your Deliverable**: Write a Diagnostic Quality Report:\n1. Explain the biochemical cause of this spoilage (moisture, Osmophilic yeasts, fermentation).\n2. Detail 3 quality errors committed during harvesting and processing.\n3. Explain how using Langstroth hives, refractometers, and centrifugal extractors prevents this loss.",
                            "materials": ["Case Handout", "Response Template", "Pen"],
                            "safety": "Ensure rigorous, evidence-based recommendations."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Core Summary: Apiculture Mastery",
                        "content": {
                            "title": "Key Takeaways",
                            "text": "- **Siting balances forage biology with public safety**.\n- **Langstroth hives preserve comb structure** via bee space.\n- **Protect colonies with grease barriers** and dearth feeding.\n- **Harvest only 80% capped honey** to prevent fermentation."
                        }
                    }
                ],
                # Pages 4 to 8: 8 Summative Assessment MCQs
                [
                    {
                        "type": "knowledge_check",
                        "title": "Summative MCQ 1: Biological Rationale of Bee Space",
                        "content": {
                            "question": "What is the biological significance of maintaining the exact 'Bee Space' (6.4 mm to 9.5 mm) between frames inside a Langstroth beehive?",
                            "options": [
                                "It is the maximum distance a bee can jump inside the hive",
                                "Within this precise measurement, bees leave the corridor open as a clear walking passageway without sealing it with propolis (<6.4mm) or building wild burr combs (>9.5mm)",
                                "It forces the queen to lay only worker bee eggs",
                                "It prevents cold wind from blowing into the honey super"
                            ],
                            "answer": "B",
                            "explanation": "Rev. Lorenzo Langstroth discovered that bees respect a 6.4–9.5mm gap (bee space) as a natural hallway. If smaller, they propolize it; if larger, they build cross-comb. Maintaining bee space allows frames to be lifted cleanly without breaking combs."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Summative MCQ 2: Biochemical Calming Mechanism of Bee Smoke",
                        "content": {
                            "question": "How does puffing cool white smoke from a bee smoker into a hive entrance physiologically calm honey bees during an inspection?",
                            "options": [
                                "The smoke puts all the bees into a deep comatose sleep",
                                "The smoke masks and disrupts the alarm pheromone (isopentyl acetate) and triggers an innate survival reflex causing bees to engorge on honey, making them heavy and docile",
                                "The smoke burns the bees' stingers so they cannot sting",
                                "The smoke makes the queen fly out of the hive"
                            ],
                            "answer": "B",
                            "explanation": "Smoke acts in two ways: it chemically masks isopentyl acetate (the alarm pheromone released by guard bees), preventing panic transmission, and it triggers a fire-survival reflex where bees gorge on honey, making them physically distended, calm, and disinclined to sting."
                        }
                    }
                ],
                [
                    {
                        "type": "knowledge_check",
                        "title": "Summative MCQ 3: Agronomic Role of Flower Fidelity",
                        "content": {
                            "question": "Why are honey bees considered far more effective commercial crop pollinators than other wild insects (such as flies, beetles, and butterflies)?",
                            "options": [
                                "Honey bees eat all the crop leaves to let sunlight hit the flowers",
                                "Honey bees exhibit 'flower fidelity' (visiting the exact same flower species repeatedly during a single foraging flight), ensuring precise and efficient pollen transfer between compatible blossoms",
                                "Honey bees only visit flowers that are sprayed with synthetic chemicals",
                                "Honey bees carry flowers back into the hive to pollinate them inside"
                            ],
                            "answer": "B",
                            "explanation": "Honey bees practice flower constancy (fidelity). A bee foraging on avocado or sunflower will exclusively visit avocado or sunflower blossoms on that foraging trip, ensuring that compatible pollen is deposited directly on the stigmas of the same species."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Summative MCQ 4: Lemon Grass Oil Pheromone Mimicry",
                        "content": {
                            "question": "Why is lemon grass essential oil widely used by beekeepers to prepare and bait empty hives to attract wild honey bee swarms?",
                            "options": [
                                "It makes the wooden hive taste sweet like sugar",
                                "It contains citral and geraniol, chemical compounds that closely mimic the honey bee's natural Nasonov orientation and scout attractant pheromone",
                                "It kills all bacteria on the outside of the hive",
                                "It turns worker bees into queen bees"
                            ],
                            "answer": "B",
                            "explanation": "Lemon grass essential oil contains high levels of citral and geraniol, the primary chemical components of the Nasonov pheromone that worker bees release to mark water sources and ideal cavity nest sites, making it an irresistible attractant for scout bees."
                        }
                    }
                ],
                [
                    {
                        "type": "knowledge_check",
                        "title": "Summative MCQ 5: Slow-Release Queen Cage Mechanism",
                        "content": {
                            "question": "What is the primary danger of releasing a newly purchased queen bee directly into a package bee colony without using a slow-release sugar candy plug?",
                            "options": [
                                "The queen will immediately lay 100,000 eggs in one hour",
                                "The foreign worker bees will perceive her unfamiliar pheromones as an alien intruder and will attack, sting, and overheat her to death (queen balling)",
                                "The queen will eat all the worker bees",
                                "The queen will refuse to walk on wooden frames"
                            ],
                            "answer": "B",
                            "explanation": "Package bees are strangers to the queen. Releasing her immediately triggers aggressive defensive reflexes known as 'balling', where workers cluster tightly around her until she suffocates or overheats. The 48–72h candy plug delay allows her scent to spread and be accepted."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Summative MCQ 6: Mechanical Centrifugal Extractor Efficiency",
                        "content": {
                            "question": "What is the major physiological and economic advantage of using a centrifugal honey extractor with Langstroth frames compared to traditional comb crushing and squeezing?",
                            "options": [
                                "It turns raw honey into solid wax bars",
                                "It uses centrifugal force to fling honey out while keeping the delicate wax comb intact, allowing combs to be returned to the hive and saving bees from consuming 8kg of honey to rebuild 1kg of wax",
                                "It boils the honey inside the extractor to pasteurize it",
                                "It separates the honey into water and sugar"
                            ],
                            "answer": "B",
                            "explanation": "Honey bees must consume approximately 8 kg of honey to metabolically secrete 1 kg of beeswax. Centrifugal extractors empty the combs without structural damage, allowing intact combs to be returned to the colony, channeling all bee energy into immediate honey refilling."
                        }
                    }
                ],
                [
                    {
                        "type": "knowledge_check",
                        "title": "Summative MCQ 7: Cause of Fermentation in Harvested Honey",
                        "content": {
                            "question": "A beekeeper bottles honey harvested from uncapped honeycombs. Three weeks later, the jars swell, foam, and develop a sour vinegar smell. What is the scientific cause?",
                            "options": [
                                "The honey was stored in glass jars rather than plastic buckets",
                                "Uncapped honey contains over 20% moisture, which allows osmophilic wild yeasts to ferment sugars into alcohol and carbon dioxide, turning the honey sour",
                                "The bees collected pollen from poisonous weeds",
                                "The smoker fuel contained too much carbon"
                            ],
                            "answer": "B",
                            "explanation": "Uncapped nectar has not been ripened by bees and contains >20% water. High moisture creates a hospitable environment for osmophilic yeasts (*Zygosaccharomyces*) to ferment glucose and fructose into ethanol and carbon dioxide, which oxidizes into acetic acid (vinegar sourness)."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Summative MCQ 8: Organic Safari Ant Defense",
                        "content": {
                            "question": "How can a commercial apiary in Kenya be effectively and safely protected against destructive safari ant (Dorylus) invasions without poisoning the bees?",
                            "options": [
                                "Spraying organophosphate insecticides into the hive entrances twice a week",
                                "Applying a 10cm wide continuous band of motor grease or used engine oil around all hive stand posts and slashing surrounding grass",
                                "Moving the hives into a closed classroom",
                                "Painting the hives with red chili pepper powder"
                            ],
                            "answer": "B",
                            "explanation": "Motor grease or used engine oil forms a sticky, hydrophobic mechanical barrier that crawling safari ants cannot cross. Keeping undergrowth cleared prevents ants from using grass blades as bridges, providing 100% protection with zero chemical risk to the bees."
                        }
                    }
                ],
                # Page 8: Capstone Summary
                [
                    {
                        "type": "summary",
                        "title": "Topic 11 Capstone Summary: Beekeeping (Apiculture) Mastery",
                        "content": {
                            "title": "Mastery Overview: Grade 10 Beekeeping, Ecology & Agribusiness",
                            "text": "Congratulations on mastering **Topic 11: Beekeeping (Apiculture)**!\n\nYou have mastered:\n- **Apiary Siting Dynamics**: 2–3 km forage radius, shallow water points with floating debris, windbreaks, and $\\ge 100\\text{ m}$ public safety buffers.\n- **Hive Architecture & Bee Space**: Traditional vs KTBH vs Langstroth systems; the $6.4\\text{--}9.5\\text{ mm}$ bee space; smoker isopentyl acetate suppression.\n- **Direct Commodities & Pollination**: Honey, beeswax, propolis, royal jelly; flower fidelity and crop pollination multiplying avocado/coffee yields; enterprise ROI.\n- **Stocking Protocols**: Wild swarm cluster capture, lemon grass pheromone bait hives, nuc sequential frame transfer, and slow-release queen cages.\n- **Routine Apiary Management**: Bi-weekly inspections, 1:1 sugar dearth feeding, swarm prevention, grease barriers against safari ants, wire cable hanging against honey badgers.\n- **Harvesting & Processing**: The 80% capping rule (<18% moisture), centrifugal extraction preserving combs, multi-stage filtering, 48h settling, and hermetic glass packaging."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Topic 11 Final Takeaway",
                        "content": {
                            "title": "The Sustainable Apiculture Maxim",
                            "text": "Beekeeping harmonizes high-value agribusiness with vital environmental stewardship. Respect bee space, enforce safety buffers, protect comb infrastructure, and harvest only fully capped honey to build thriving, profitable apiculture enterprises."
                        }
                    }
                ]
            ]
        }
    ]

@transaction.atomic
def ingest_grade10_topic11(replace=False):
    """Executes the complete production ingestion of Grade 10 Agriculture Topic 11: Beekeeping (Apiculture)."""
    print("=" * 80)
    print("STARTING INGESTION: CBC Grade 10 Agriculture — Topic 11: Beekeeping")
    print("=" * 80)

    curriculum = Curriculum.objects.filter(name__iexact="CBC").first()
    grade = Grade.objects.filter(curriculum=curriculum, name__icontains="10").first()
    subject = Subject.objects.filter(grade=grade, name__iexact="Agriculture").first()

    assert curriculum and grade and subject, "Curriculum/Grade/Subject not found!"

    topic_name = "Beekeeping"
    topic = Topic.objects.filter(subject=subject, name=topic_name).first()
    if not topic:
        topic = Topic.objects.create(
            subject=subject,
            name=topic_name,
            description="Comprehensive theoretical, ecological, and practical study of apiculture: apiary siting, bee space, Langstroth and KTBH hives, swarm capture and baiting, nucleus transfers, apiary pest management, honey harvesting, and centrifugal extraction.",
            order=11
        )
        print(f"Created Topic 11: {topic.name} (ID: {topic.id})")
    else:
        topic.order = 11
        topic.description = "Comprehensive theoretical, ecological, and practical study of apiculture: apiary siting, bee space, Langstroth and KTBH hives, swarm capture and baiting, nucleus transfers, apiary pest management, honey harvesting, and centrifugal extraction."
        topic.save()
        print(f"Resolved Topic 11: {topic.name} (ID: {topic.id})")

    if replace:
        print("Flag --replace active: Clearing existing LearningUnits and Lessons for Topic 11...")
        topic.learning_units.all().delete()
        topic.lessons.all().delete()

    curriculum_data = build_topic11_curriculum()
    total_units = 0
    total_lessons = 0
    total_pages = 0
    total_blocks = 0

    for item in curriculum_data:
        u_order = item["unit_order"]
        u_name = item["unit_name"]
        u_desc = item["unit_description"]
        l_title = item["lesson_title"]
        pages = item["pages"]

        unit, u_created = LearningUnit.objects.get_or_create(
            topic=topic,
            order=u_order,
            defaults={"name": u_name, "description": u_desc}
        )
        if not u_created:
            unit.name = u_name
            unit.description = u_desc
            unit.save()
        total_units += 1

        lesson, l_created = Lesson.objects.get_or_create(
            topic=topic,
            learning_unit=unit,
            defaults={
                "title": l_title,
                "status": "published",
                "version": 1,
                "immutable_metadata": {
                    "author": "VLearn Senior Curriculum Agent",
                    "grade": "Grade 10",
                    "subject": "Agriculture",
                    "topic_order": 11,
                    "unit_order": u_order
                }
            }
        )
        if not l_created:
            lesson.title = l_title
            lesson.status = "published"
            lesson.version = 1
            lesson.save()

        lesson.blocks.all().delete()
        total_lessons += 1

        block_order_counter = 1
        for page_idx, page_blocks in enumerate(pages, start=1):
            total_pages += 1
            for comp_idx, block_def in enumerate(page_blocks, start=1):
                b_type = block_def["type"]
                b_title = clean_text(block_def.get("title", ""))
                b_content = clean_dict(block_def.get("content", {}))

                LessonBlock.objects.create(
                    lesson=lesson,
                    block_id=f"g10_agri_t11_u{u_order}_p{page_idx}_b{comp_idx}",
                    block_type=b_type,
                    component_type=b_type,
                    title=b_title,
                    content=b_content,
                    order=block_order_counter,
                    page_number=page_idx,
                    component_order=comp_idx,
                    page_title=b_title if comp_idx == 1 else None,
                    metadata={"topic_order": 11, "unit_order": u_order, "page": page_idx}
                )
                block_order_counter += 1
                total_blocks += 1

        print(f"  Ingested Unit {u_order}: {u_name} -> Lesson '{l_title}' ({len(pages)} Pages, {block_order_counter - 1} Blocks)")

    print("=" * 80)
    print(f"INGESTION COMPLETE: Topic 11 '{topic.name}'")
    print(f"  Total Units:   {total_units}")
    print(f"  Total Lessons: {total_lessons}")
    print(f"  Total Pages:   {total_pages}")
    print(f"  Total Blocks:  {total_blocks}")
    print("=" * 80)

if __name__ == "__main__":
    replace_flag = "--replace" in sys.argv
    ingest_grade10_topic11(replace=replace_flag)
