"""
VLearn CBC Grade 10 Agriculture — Topic 1: Agricultural Land
Production Ingestion Engine (Deep Senior Secondary Pedagogical Edition)

Curriculum: CBC (ID: 5)
Grade: Grade 10 (ID: 5, Level: 10)
Subject: Agriculture
Topic: Agricultural Land (Topic Order: 1)

Decomposed into 10 Learning Units & 10 Published Lessons:
  1. Ways of Accessing Land (7 Pages, 13 Blocks)
  2. Utility of Agricultural Land (7 Pages, 13 Blocks)
  3. Natural Factors: Climate and Altitude (7 Pages, 14 Blocks)
  4. Natural Factors: Soil, Topography, and Biotic Factors (8 Pages, 15 Blocks)
  5. Community Land-Use Observation (7 Pages, 13 Blocks)
  6. Land-Productivity Decision Exercise (7 Pages, 13 Blocks)
  7. Importance of Land in Production (7 Pages, 13 Blocks)
  8. Access, Utility and Productivity Synthesis (7 Pages, 13 Blocks)
  9. Applied Local Case Study (Wekesa's Farm) (8 Pages, 15 Blocks)
  10. Module Review, Performance Task & Summative Assessment (9 Pages, 20 Blocks)
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

def build_topic1_curriculum():
    """Returns the comprehensive pedagogical page and block structure for Grade 10 Topic 1: Agricultural Land."""
    return [
        # =====================================================================
        # LESSON 1: Ways of Accessing Land
        # =====================================================================
        {
            "unit_order": 1,
            "unit_name": "Ways of Accessing Land",
            "unit_description": "Land as a finite production factor, methods of accessing agricultural land in Kenya (leasing, inheriting, buying, donation), comparative advantages, legal tenures, and initial capital decisions.",
            "lesson_title": "Ways of Accessing Agricultural Land",
            "pages": [
                [
                    {
                        "type": "suggested_image",
                        "title": "Agricultural Land: The Foundational Factor of Production",
                        "content": {
                            "title": "Agricultural Land: The Foundational Factor of Production",
                            "caption": "A neatly demarcated and deeply ploughed agricultural field illustrating the physical boundaries and finite nature of farm land."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Land Acquisition Methods",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Define **land** as an economic factor of agricultural production and explain its finite, non-reproducible nature.",
                                "Analyze the four primary methods of accessing land in Kenya: **leasing, inheriting, buying, and donation**.",
                                "Evaluate the specific **advantages, disadvantages, and financial trade-offs** of each land tenure system.",
                                "Apply land-access criteria to real-world youth agribusiness start-up scenarios."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Land as a Finite Production Factor",
                        "content": {
                            "title": "The Bedrock of Agricultural Enterprise",
                            "text": "In agricultural economics, **land** is the foundational natural factor of production upon which all farming activities depend. Unlike capital equipment or manufactured inputs (like fertilizers and hybrid seeds) that can be industrially expanded, the physical surface area of the earth is fixed and non-reproducible.\n\n- **Broad Definition**: Agricultural land encompasses the physical soil layer, water bodies, underground aquifers, natural vegetation, microclimate, and topography.\n- **The Agribusiness Reality**: Securing appropriate land with reliable drainage, fertile soil, and legal security is the very first strategic decision every agribusiness entrepreneur must make."
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "Leasing Land: Mechanics and Strategic Trade-Offs",
                        "content": {
                            "title": "Temporary Usage Rights vs Investment Incentives",
                            "text": "**Leasing** is a contractual agreement where a tenant farmer acquires the legal right to use a parcel of land from the titleholder for a specified duration in exchange for periodic rental payments.\n\n### Advantages of Leasing\n- **Low Capital Requirement**: Allows young farmers and start-ups to launch operations without the massive upfront capital needed to purchase real estate.\n- **Operational Flexibility**: Farmers can scale acreage up or down, or relocate to higher-potential zones when market conditions change.\n- **No Permanent Tax Burdens**: Long-term land rates and property taxes remain the legal responsibility of the landowner.\n\n### Disadvantages & Risks\n- **Tenure Insecurity**: The landlord may decline lease renewal, forcing sudden relocation and business interruption.\n- **Disincentive for Long-Term Improvements**: Farmers rarely install expensive drip irrigation systems, stone terraces, or perennial crops (like coffee or macadamia) on leased land.\n- **Fixed Overhead Cost**: Rent must be paid regardless of crop failure, severe drought, or market price collapses."
                        }
                    },
                    {
                        "type": "definition_card",
                        "title": "Key Term: Land Lease Agreement",
                        "content": {
                            "term": "Leasehold Tenure",
                            "definition": "A legal contract granting temporary possession and agricultural use of land for a defined period (e.g. 1 to 5 years) in exchange for agreed periodic financial rent.",
                            "example": "A youth cooperative leasing 3 acres for 2 years to grow fast-maturing tomatoes under drip irrigation."
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "Inheriting Land: Cultural Heritage and Fragmentation",
                        "content": {
                            "title": "Intergenerational Wealth and Practical Bottlenecks",
                            "text": "**Inheritance** is the transfer of land ownership and usage rights from deceased parents or family members to their legal heirs through customary law or formal wills.\n\n### Advantages of Inheritance\n- **Zero Direct Acquisition Cost**: Heirs receive productive assets without draining their savings or acquiring bank debt.\n- **Social Continuity & Stewardship**: High emotional attachment fosters a culture of intergenerational soil conservation and family legacy.\n\n### Critical Disadvantages & Bottlenecks\n- **Excessive Land Fragmentation**: Dividing family acreage among multiple children over generations results in tiny 'micro-plots' (e.g. 0.25 acres) that are economically unviable for commercial farming.\n- **Boundary & Succession Disputes**: Unclear wills or unregistered family land trigger prolonged legal battles that freeze agricultural production for years.\n- **Enterprise Mismatch**: The inherited plot may have steep slopes, poor drainage, or adverse microclimates unsuitable for the heir's desired farming enterprise."
                        }
                    },
                    {
                        "type": "common_misconception",
                        "title": "Misconception: Inherited Land is Ready for Commercial Agribusiness",
                        "content": {
                            "misconception": "Inherited family land can immediately be used as bank collateral for commercial agribusiness loans.",
                            "correction": "Unless the heir undergoes formal legal succession and obtains a distinct Title Deed registered in their own name, commercial financial institutions cannot accept family land as loan collateral.",
                            "why_it_matters": "Unregistered inherited land leaves the farmer capital-constrained and legally vulnerable to family boundary disputes."
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "Outright Purchase and Land Donation",
                        "content": {
                            "title": "Absolute Freehold Ownership vs Conditional Gifts",
                            "text": "### 1. Buying Land (Freehold / Purchase)\n- **Absolute Security of Tenure**: Provides total ownership freedom to make permanent capital investments such as greenhouses, boreholes, zero-grazing units, and orchard trees.\n- **Bankable Asset**: A clean Title Deed is the primary collateral accepted by commercial banks and SACCOs for securing low-interest agricultural development loans.\n- **Asset Value Appreciation**: Fertile farmland near transport corridors appreciates steadily over time.\n- *Major Constraint*: Extremely high capital barrier that drains working capital away from operational inputs.\n\n### 2. Land Donation (Gifts & Grants)\n- **Zero Financial Cost**: Land gifted by family members, charitable NGOs, or government settlement schemes for community self-help groups.\n- *Major Constraint*: Highly rare, subject to strict usage covenants (e.g. strictly for educational or community food production), and the recipient cannot choose the location or soil quality."
                        }
                    },
                    {
                        "type": "comparison_table",
                        "title": "Comparative Matrix of Land Access Methods",
                        "content": {
                            "title": "Comparison of Land Acquisition Methods in Kenya",
                            "headers": ["Acquisition Method", "Capital Requirement", "Security of Tenure", "Long-Term Investment Incentive", "Primary Risk / Drawback"],
                            "rows": [
                                ["Leasing", "Low (Seasonal rent)", "Low to Medium (Fixed lease term)", "Low (Short-term focus)", "Lease termination & recurring rent overhead"],
                                ["Inheritance", "Zero direct purchase cost", "High (once title is transferred)", "High (Ancestral stewardship)", "Severe plot fragmentation & family disputes"],
                                ["Buying", "Very High (Market purchase price)", "Absolute (Freehold Title Deed)", "Highest (Full incentive to invest)", "Drains cash reserves; financial debt risk"],
                                ["Donation", "Zero direct acquisition cost", "Medium to High (Subject to covenant)", "Medium (Restricted by donor terms)", "Strict usage conditions & uncertain availability"]
                            ]
                        }
                    }
                ],
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Land Acquisition Methods Comparison Framework",
                        "content": {
                            "title": "Land Acquisition Methods Comparison Framework",
                            "caption": "Comprehensive comparative diagram mapping capital demands, legal security, and operational suitability across leasing, inheritance, purchase, and donation."
                        }
                    },
                    {
                        "type": "step_process",
                        "title": "Decision Workflow for Choosing Land Access Method",
                        "content": {
                            "title": "Step-by-Step Land Acquisition Strategy for New Farmers",
                            "steps": [
                                "1. **Assess Available Liquid Capital**: Determine whether funds can support land purchase or must be reserved for quality seeds, fertilizers, and irrigation.",
                                "2. **Determine Crop Life-Cycle**: Match short-term annuals (vegetables, maize) with flexible leasing; match perennials (tea, coffee, fruit orchards) with ownership.",
                                "3. **Conduct Title and Boundary Searches**: Verify authentic land registration at the Ministry of Lands before signing purchase deeds or paying lease deposits.",
                                "4. **Evaluate Soil and Microclimate Compatibility**: Test soil pH, drainage, and water availability before entering binding legal agreements."
                            ]
                        }
                    }
                ],
                [
                    {
                        "type": "mini_activity",
                        "title": "Field Investigation: Local Land Tenure Survey",
                        "content": {
                            "title": "Investigating Agricultural Land Access in Your Community",
                            "task": "Interview two local farmers (one growing annual vegetables and one managing a perennial crop or dairy unit):\n\n- Inquire how they accessed their land (leased, inherited, purchased, or communal allocation).\n- Record the advantages and tenure challenges they experience under their current land arrangement.\n- Compile a structured 1-page analytical brief comparing how tenure security influenced their willingness to construct permanent farm infrastructure.",
                            "materials": ["Notebook", "Survey Questionnaire", "Pen"],
                            "safety": "Always conduct community interviews with teacher/parent supervision and respect landholders' privacy."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Core Summary: Land Tenure and Agribusiness",
                        "content": {
                            "title": "Key Takeaways",
                            "text": "- **Land is finite and non-reproducible**, requiring strategic acquisition and conservation.\n- **Leasing** minimizes starting capital but disincentivizes permanent soil conservation structures.\n- **Inherited land** must be legally formalized to resolve family disputes and prevent unsustainable parcel fragmentation.\n- **Buying land** guarantees absolute tenure security and unlocks commercial credit via title deeds."
                        }
                    }
                ],
                [
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Selecting Land Access Strategy",
                        "content": {
                            "question": "A youth agribusiness group has 150,000 KES in startup capital and wants to grow commercial cabbages and sweet peppers for two consecutive seasons. Which land acquisition strategy is most agronomically and financially sound?",
                            "options": [
                                "Spend the entire 150,000 KES as a down payment to purchase a 0.25-acre parcel with a title deed",
                                "Lease a 2-acre fertile plot with river access for two years at 30,000 KES, utilizing remaining funds for quality seeds, drip lines, and fertilizers",
                                "Wait for an international agricultural donor agency to donate fertile land without legal usage restrictions",
                                "Plant cabbages on unregistered communal road reserves to eliminate all rental and land purchase expenses"
                            ],
                            "answer": "B",
                            "explanation": "Leasing is the optimal choice for quick-maturing horticultural crops with limited startup capital. It leaves 120,000 KES of working capital for high-yield seeds, drip irrigation, pest management, and labor. Purchasing land would exhaust all capital and leave no funds for operational inputs, while waiting for donations or encroaching on road reserves carries high uncertainty and legal risk."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 2: Utility of Agricultural Land
        # =====================================================================
        {
            "unit_order": 2,
            "unit_name": "Utility of Agricultural Land",
            "unit_description": "Six primary agricultural utilities of land: broad-acre crop production, livestock rearing, agroforestry, horticulture, aquaculture, and apiculture. Land suitability mapping and carrying capacity.",
            "lesson_title": "Agricultural Utilities and Enterprise Suitability",
            "pages": [
                [
                    {
                        "type": "suggested_image",
                        "title": "Diverse Land Utilities in Modern Agriculture",
                        "content": {
                            "title": "Diverse Land Utilities in Modern Agriculture",
                            "caption": "Smallholder farmers in Kenya demonstrating diverse agricultural land utilities including intensive crop production and integrated animal management."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Agricultural Land Utilities",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Identify and explain the six primary agricultural utilities of land: **crop production, livestock farming, agroforestry, horticulture, aquaculture, and apiculture**.",
                                "Analyze the ecological and physical land requirements for each agricultural utility.",
                                "Define **carrying capacity** in livestock production and explain the risks of overstocking.",
                                "Design an integrated multi-utility farm layout that maximizes farm productivity while protecting natural ecosystems."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The Concept of Agricultural Land Utility",
                        "content": {
                            "title": "Matching Land Characteristics to Production Systems",
                            "text": "**Agricultural land utility** refers to the specific economic and biological purposes for which a piece of land is developed and managed. Because different enterprises require vastly different soil depths, water volumes, topographies, and capital inputs, a successful farmer evaluates their land's unique physical profile to determine the optimal enterprise mix."
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "Broad-Acre Crops and Livestock Production Systems",
                        "content": {
                            "title": "Extensive and Semi-Intensive Utilities",
                            "text": "### 1. Broad-Acre Crop Production\n- **Requirements**: Expansive, relatively flat or gently undulating terrain (0–5% slope) allowing efficient tractor operations, combine harvesting, and uniform planting.\n- **Primary Crops**: Staple grains and industrial crops such as maize, wheat, barley, sorghum, and sugarcane.\n- **Soil Demands**: Deep, fertile soils with medium texture (loam to clay-loam) that hold adequate moisture.\n\n### 2. Livestock Production & Carrying Capacity\n- **Pasture and Fodder**: Utilizing land to grow natural grazing grasses (Rhodes grass, Kikuyu grass) or intensive fodder crops (Napier grass, Desmodium).\n- **Carrying Capacity Principle**: The **carrying capacity** is the maximum number of animal units (e.g. 1 Livestock Unit = 1 mature cow of 450 kg) that a given acreage of pasture can sustain indefinitely without causing pasture degradation or soil compaction.\n- **Overstocking Hazard**: Exceeding the carrying capacity strips grass cover, exposes topsoil to wind and water erosion, and leads to rapid livestock emaciation."
                        }
                    },
                    {
                        "type": "definition_card",
                        "title": "Key Term: Carrying Capacity",
                        "content": {
                            "term": "Carrying Capacity (Livestock)",
                            "definition": "The maximum stocking density of livestock that a specific pasture area can support year after year without depleting pasture biodiversity or causing soil degradation.",
                            "example": "In high-potential fertile highlands, 1 acre of managed Napier grass can support 2 to 3 zero-grazed dairy cows, whereas in semi-arid rangelands, 10 to 15 acres are required per beef animal."
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "Agroforestry and Intensive Horticulture",
                        "content": {
                            "title": "Multi-Story Farming and High-Value Crop Systems",
                            "text": "### 3. Agroforestry (Trees + Crops + Livestock)\n- **The Multi-Functional Utility**: Deliberate integration of multi-purpose woody trees and shrubs with crops and pasture.\n- **Ecological Benefits**: Deep tree roots intercept leaching nutrients and pump them to the surface; tree canopies act as windbreaks and reduce raindrop splash impact; nitrogen-fixing trees (e.g. *Calliandra*, *Leucaena*) naturally enrich the soil.\n- **Economic Harvests**: Provides timber, firewood, bee nectar, and protein-rich animal fodder.\n\n### 4. Horticulture (Fruits, Vegetables, Flowers)\n- **Intensive Management**: Maximizing economic yield per square meter through high capital investment (greenhouses, drip irrigation, shade nets).\n- **Requirements**: Deep, highly fertile, well-drained soils with guaranteed, high-volume irrigation water and rapid access to urban transport markets due to product perishability."
                        }
                    },
                    {
                        "type": "comparison_table",
                        "title": "Horticulture vs Broad-Acre Crop Production",
                        "content": {
                            "title": "Comparative Operational Profile",
                            "headers": ["Dimension", "Intensive Horticulture", "Broad-Acre Crop Production"],
                            "rows": [
                                ["Land Area Required", "Small (0.25 to 2 acres)", "Large (10 to 500+ acres)"],
                                ["Capital Input per Acre", "Very High (Drip kits, greenhouses, seeds)", "Medium (Mechanized field operations)"],
                                ["Labor Intensity", "High (Pruning, trellising, daily picking)", "Low to Medium (Mechanized spraying & harvest)"],
                                ["Water Dependency", "Critical (Continuous year-round irrigation)", "Primarily rain-fed with supplementary irrigation"],
                                ["Perishability & Transport", "Extremely High (Requires immediate cold-chain)", "Low (Grains store dry for months in silos)"]
                            ]
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "Aquaculture and Apiculture Utilities",
                        "content": {
                            "title": "Transforming Low-Lying Basins and Steep Rocky Slopes",
                            "text": "### 5. Aquaculture (Fish Farming)\n- **Land Characteristics**: Requires flat low-lying basins or valley bottoms with **heavy clay soils** (minimum 30–35% clay content) to prevent water seepage through pond dikes.\n- **Water Supply**: Access to unpolluted, permanent gravity-fed streams, springs, or boreholes.\n- **Target Species**: Warm-water species like Nile Tilapia and African Catfish in low/medium altitudes; cold-water Rainbow Trout in high-altitude mountain streams.\n\n### 6. Apiculture (Beekeeping)\n- **Marginal Land Utilization**: Beehives require zero soil fertility, zero cultivation, and minimal physical footprint. They are ideally placed on steep, rocky, or otherwise uncultivable boundary slopes.\n- **Ecological Integration**: Bees provide essential cross-pollination services for horticultural crops (increasing avocado, coffee, and watermelon yields by up to 40%) while producing honey and beeswax."
                        }
                    },
                    {
                        "type": "did_you_know",
                        "title": "Did You Know: Apiculture Multiplier Effect",
                        "content": {
                            "title": "Bees Double Farm Yields",
                            "text": "Installing 5 to 10 beehives on uncultivated rocky field margins not only generates premium honey income but also increases surrounding horticultural fruit and vegetable yields by 20% to 40% through systematic insect cross-pollination!"
                        }
                    }
                ],
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Integrated Multi-Utility Farm Layout Model",
                        "content": {
                            "title": "Integrated Multi-Utility Farm Layout Model",
                            "caption": "Topographical farm zoning diagram illustrating the placement of aquaculture in clay valleys, horticulture on gentle slopes, zero-grazing near homesteads, and apiculture on steep rocky margins."
                        }
                    },
                    {
                        "type": "step_process",
                        "title": "Farm Zoning Protocol for Maximum Efficiency",
                        "content": {
                            "title": "4-Step Zoning Rules for Smallholder Farms",
                            "steps": [
                                "1. **Identify Topographic Extremes**: Allocate steep, rocky, or uncultivable slopes to apiculture and protective agroforestry woodlots.",
                                "2. **Map Soil Drainage and Water**: Position earthen aquaculture fish ponds in clay-rich, low-lying basins; allocate well-drained loams to intensive horticulture.",
                                "3. **Locate Intensive Livestock Near Homestead**: Place dairy sheds and poultry houses close to the farm residence for close supervision, biosecurity, and easy manure transport to crop fields.",
                                "4. **Establish Boundary Windbreaks**: Plant deep-rooted agroforestry trees (e.g. *Grevillea robusta*) along external boundaries to filter wind and supply mulch."
                            ]
                        }
                    }
                ],
                [
                    {
                        "type": "mini_activity",
                        "title": "Practical Activity: School Farm Land-Utility Audit",
                        "content": {
                            "title": "Mapping and Optimizing School Land Utility",
                            "task": "Walk across your school grounds and agricultural demonstration plots:\n\n1. Draw a sketch map demarcating existing utilities (buildings, playing fields, crop plots, livestock pens, waste areas, uncultivated boundaries).\n2. Identify at least two under-utilized or marginal areas (e.g. a steep rocky fence-line or a waterlogged depression).\n3. Formulate a proposal for converting these marginal zones into productive utilities such as an apiary, banana filtration trench, or a fish pond.",
                            "materials": ["A4 Sketch Paper", "Measuring Tape", "Ruler", "Colored Pencils"],
                            "safety": "Wear sturdy footwear and do not disturb active wild beehives without protective bee suits."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Core Summary: Land Utility Matching",
                        "content": {
                            "title": "Key Takeaways",
                            "text": "- **Broad-acre crops** require large, flat terrain for mechanization; **horticulture** demands intensive inputs on fertile, well-drained soil.\n- **Carrying capacity** governs livestock numbers; overstocking causes irreversible soil erosion and pasture death.\n- **Aquaculture** turns waterlogged clay valleys into high-protein fish ponds.\n- **Apiculture** generates high revenue from steep, rocky, uncultivable marginal land while boosting crop pollination."
                        }
                    }
                ],
                [
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Matching Land Characteristics to Utility",
                        "content": {
                            "question": "A farmer in Kisii County has a 2-acre farm featuring a low-lying valley basin with heavy clay soil that remains waterlogged year-round, alongside a steep, rocky, uncultivable hillside boundary. Which combination of enterprises represents the most sustainable land utility?",
                            "options": [
                                "Planting a broad-acre wheat field in the waterlogged valley and building a mechanized dairy shed on the steep rocky hillside",
                                "Constructing an earthen tilapia fish pond in the clay basin and installing a modern top-bar apiary (beehives) on the rocky hillside",
                                "Growing dryland finger millet in the clay basin and establishing a commercial rose greenhouse on the rocky hillside",
                                "Digging sand mines in the clay basin and clearing all hillside vegetation for open cattle grazing"
                            ],
                            "answer": "B",
                            "explanation": "Heavy clay soils in low depressions naturally retain water without seepage, making them ideal for aquaculture fish ponds. Steep rocky hillsides cannot support mechanical cultivation or deep rooting but provide an undisturbed, elevated environment for apiculture (beehives) alongside drought-tolerant trees, turning marginal land into a profitable enterprise."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 3: Natural Factors: Climate and Altitude
        # =====================================================================
        {
            "unit_order": 3,
            "unit_name": "Natural Factors: Climate and Altitude",
            "unit_description": "Natural determinants of land productivity: rainfall amount, reliability, distribution, temperature, solar photoperiod, and altitude lapse rate across Kenyan agro-ecological zones.",
            "lesson_title": "Natural Determinants: Climate and Altitude",
            "pages": [
                [
                    {
                        "type": "suggested_image",
                        "title": "Highland Agro-Climatic Zone: Tea Plantation in Kericho",
                        "content": {
                            "title": "Highland Agro-Climatic Zone: Tea Plantation in Kericho",
                            "caption": "Lush green tea plantations near Kericho, Kenya, showcasing how high altitude and cool, reliable rainfall create ideal conditions for perennial beverage crops."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Climate & Altitude",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Identify the major climatic factors that determine agricultural land productivity: **rainfall, temperature, sunlight, and wind**.",
                                "Analyze rainfall in terms of **total annual volume, reliability, and seasonal distribution** (unimodal vs bimodal).",
                                "Explain the physiological relationship between **altitude, air temperature lapse rate, and crop adaptation**.",
                                "Categorize Kenya's primary agro-ecological zones (Highlands, Mid-Altitude, Lowlands) by climatic potential."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Natural Determinants of Land Productivity",
                        "content": {
                            "title": "The Inherent Environmental Boundaries of Land",
                            "text": "The agricultural yield potential of any parcel of land is fundamentally governed by natural environmental factors. While a farmer can apply fertilizers or build irrigation canals, the macro-climate and elevation set the baseline biological ceiling for what can be grown profitably without prohibitive costs."
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "Rainfall: Quantity, Distribution, and Reliability",
                        "content": {
                            "title": "The Three Pillars of Agricultural Water Availability",
                            "text": "Water is the primary solvent for soil nutrient uptake and the driver of plant transpiration. Farmers must evaluate three distinct aspects of rainfall:\n\n### 1. Total Annual Rainfall Amount\n- **High-Rainfall (>1000 mm/year)**: Central Highlands, Western Kenya, Rift Valley highlands. Supports tea, coffee, pyrethrum, hybrid maize, and intensive dairy.\n- **Medium-Rainfall (500–1000 mm/year)**: Eastern midlands, semi-humid zones. Suited for drought-tolerant maize, beans, pigeon peas, and sunflower.\n- **Low-Rainfall (<500 mm/year)**: Arid and Semi-Arid Lands (ASALs). Suited for sorghum, pearl millet, cowpeas, green grams, and pastoral livestock ranching.\n\n### 2. Rainfall Distribution (Seasonality)\n- **Unimodal (Single extended rainy season)**: Common in parts of North Rift and Western Kenya; supports long-season crops like 8-month highland maize.\n- **Bimodal (Two distinct wet seasons - Long & Short Rains)**: Common in Central and Eastern Kenya; dictates short-season crops (beans, potatoes, vegetables) allowing two harvests per year.\n\n### 3. Rainfall Reliability\n- The predictability of rain onset and cessation. Unpredictable start dates lead to seed scorch and replanting expenses."
                        }
                    },
                    {
                        "type": "comparison_table",
                        "title": "Rainfall Regimes across Kenyan Agricultural Zones",
                        "content": {
                            "title": "Rainfall Classification Matrix",
                            "headers": ["Rainfall Category", "Annual Range", "Key Kenyan Counties", "Suitable Crops & Enterprises"],
                            "rows": [
                                ["High Potential", "> 1,200 mm", "Kiambu, Nandi, Kericho, Kisii, Trans Nzoia", "Tea, Coffee, Irish Potatoes, Exotic Dairy (Friesian/Jersey)"],
                                ["Medium Potential", "750 – 1,200 mm", "Machakos, Embu lower zones, Nakuru, Uasin Gishu", "Maize, Beans, Macadamia, Avocado, Crossbred Dairy"],
                                ["Marginal / Semi-Arid", "400 – 750 mm", "Kitui, Makueni, Tharaka, Laikipia", "Sorghum, Green Grams, Cowpeas, Beef Zebu cattle, Galla Goats"],
                                ["Arid Pastoral", "< 400 mm", "Garissa, Turkana, Wajir, Marsabit", "Camels, Somali Sheep, Red Maasai Sheep, Pasture grazing"]
                            ]
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "Temperature and Solar Radiation (Photoperiod)",
                        "content": {
                            "title": "Drivers of Photosynthesis and Transpiration",
                            "text": "### 1. Temperature\n- **Enzyme Activity**: Plant biochemical reactions (photosynthesis and nutrient assimilation) have optimal thermal ranges (typically 18°C to 28°C for C3 crops; 25°C to 35°C for C4 crops like maize and sugarcane).\n- **High Temperature Stress**: Causes excessive transpiration, pollen sterility in crops like tomatoes, and severe **heat stress** in exotic dairy breeds (e.g. Holstein Friesians), leading to plummeting feed intake and milk yield drops.\n- **Low Temperature & Frost**: Cold highland nights (<10°C) slow crop growth, while freezing frost crystallizes cell water and destroys tissue in tea, tomatoes, and potatoes.\n\n### 2. Sunlight (Photoperiod & Light Intensity)\n- Solar radiation supplies the photon energy for chlorophyll photosynthesis.\n- **Photoperiodism**: Day length triggers flowering and tuber formation in specific crops (e.g. short-day chrysanthemums vs day-neutral tomatoes)."
                        }
                    },
                    {
                        "type": "common_mistake",
                        "title": "Agronomic Error: Introducing Temperate Dairy Breeds into Hot Lowlands",
                        "content": {
                            "mistake": "Importing purebred European Holstein Friesian dairy cattle into hot, low-altitude coastal or semi-arid zones.",
                            "correction": "Friesian cattle lack sweat glands and heat-tolerant pigmentation. In hot lowlands, they suffer acute heat stress, drop milk yields by 70%, and succumb to tick-borne East Coast Fever (ECF). Farmers should use heat-adapted Sahiwal, Boran, or F1 crosses.",
                            "why_it_matters": "Matching livestock genetics to thermal climatic zones prevents devastating animal mortality and financial bankruptcy."
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "Altitude: Elevation and the Environmental Lapse Rate",
                        "content": {
                            "title": "The Vertical Climate Gradient in Agriculture",
                            "text": "**Altitude** is the vertical height of a land parcel above sea level. It exerts a dominant influence over local temperature and atmospheric pressure through the **Environmental Lapse Rate**:\n\n$$\\text{Temperature Drop} \\approx 6.5^\\circ\\text{C} \\text{ per } 1000\\text{ meters elevation gain}$$\n\n### Agro-Ecological Elevation Bands in Kenya\n- **High-Altitude Highlands (> 1,800 m)**: Characterized by cool temperatures (12°C–18°C), high relative humidity, and frequent mists. Prime zones for tea, pyrethrum, wheat, barley, cut flowers, and exotic dairy cows.\n- **Medium-Altitude Midlands (1,000 – 1,800 m)**: Warm-temperate conditions (18°C–25°C). The primary grain and cash crop belt for coffee, maize, beans, bananas, and horticultural fruits.\n- **Low-Altitude Lowlands (< 1,000 m)**: High thermal regimes (>26°C–34°C) with high evaporation rates. Suited for cotton, sisal, cassava, cashew nuts, coconuts, watermelons, beef ranching, and camel husbandry."
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Agro-Ecological Elevation and Enterprise Distribution Diagram",
                        "content": {
                            "title": "Agro-Ecological Elevation and Enterprise Distribution Diagram",
                            "caption": "Vertical profile diagram demonstrating the 6.5°C/1000m lapse rate and matching crops (tea/pyrethrum in highlands, coffee/maize in midlands, sisal/cotton/coconuts in coastal lowlands)."
                        }
                    }
                ],
                [
                    {
                        "type": "suggested_video",
                        "title": "Agro-Ecological Zones and Climate Adaptation in East Africa",
                        "content": {
                            "title": "Agro-Ecological Zones and Climate Adaptation in East Africa",
                            "description": "Explores how altitude, temperature gradients, and rainfall variability dictate crop distribution and farming systems across East African agro-climatic zones.",
                            "url": "https://www.youtube.com/watch?v=e3Vkv2j7CqI"
                        }
                    },
                    {
                        "type": "step_process",
                        "title": "Protocol: Analyzing Local Agro-Climatic Suitability",
                        "content": {
                            "title": "How to Conduct an Agro-Climatic Evaluation for a Farm",
                            "steps": [
                                "1. **Determine Exact Elevation (GPS / Altimeter)**: Measure height above sea level to calculate expected mean minimum and maximum thermal ranges.",
                                "2. **Retrieve 10-Year Local Rainfall Records**: Check total annual millimeters, dry spell frequency, and unimodal vs bimodal seasonality from local meteorological stations.",
                                "3. **Check Pest and Disease Pressures**: Note that hot, low-altitude zones harbor higher tick and insect pest populations, whereas cool, humid highlands promote fungal blights.",
                                "4. **Select Certified Ecological Seed Varieties**: Choose seed packages certified for your exact altitude (e.g. Kenya Seed highland 600-series maize vs lowland dryland 500-series)."
                            ]
                        }
                    }
                ],
                [
                    {
                        "type": "mini_activity",
                        "title": "Data Activity: Mapping Local Altitude and Crop Profile",
                        "content": {
                            "title": "Analyzing Your Sub-County Agro-Climatic Profile",
                            "task": "1. Use a smartphone GPS app, school barometer, or topographic map to find the exact altitude of your school compound in meters above sea level.\n2. Calculate the estimated mean temperature difference between your school and Mombasa (sea level = 0 m).\n3. List the top 3 commercial crops grown in your sub-county and justify why their thermal and rainfall requirements align with your local altitude.",
                            "materials": ["Smartphone / GPS App", "Notebook", "Calculator"],
                            "safety": "Ensure proper digital hygiene when using mobile devices during field sessions."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Core Summary: Climate and Elevation",
                        "content": {
                            "title": "Key Takeaways",
                            "text": "- **Rainfall amount, distribution, and reliability** determine whether farming is rain-fed, supplementary irrigated, or pastoral.\n- **Air temperature drops ~6.5°C per 1,000 meters of elevation**, shaping vertical crop bands.\n- **Highlands (>1800m)** support cool-season crops (tea, pyrethrum, potatoes) and exotic dairy.\n- **Lowlands (<1000m)** require heat-tolerant, drought-resistant crops (sorghum, cowpeas, cotton) and zebu/camel livestock."
                        }
                    }
                ],
                [
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Climatic Influence on Enterprise Choice",
                        "content": {
                            "question": "A farmer relocates from a highland farm in Limuru (elevation 2,100 m) to a newly acquired plot in Kitui lowlands (elevation 750 m). Why would attempting to grow commercial Irish potatoes and pyrethrum without shade and refrigeration result in economic failure?",
                            "options": [
                                "The air pressure in Kitui is too low for plant respiration to occur",
                                "The significantly higher temperatures (approx. 8.8°C warmer) accelerate evapotranspiration, inhibit tuberization in potatoes, and prevent flower bud initiation in pyrethrum",
                                "Kitui soils have too many earthworms that physically consume potato tubers underground",
                                "High-altitude crops like potatoes require salt spray from ocean winds to produce flowers"
                            ],
                            "answer": "B",
                            "explanation": "Due to the lapse rate (approx. 6.5°C per 1000 m), dropping from 2,100 m to 750 m (a 1,350 m drop) increases mean temperatures by roughly 8.8°C. Irish potatoes require cool temperatures (15°C–20°C) for tuber initiation; high heat causes excessive vegetative growth with zero tubers. Pyrethrum requires cold night temperatures to trigger pyrethrin flower synthesis, failing completely in hot lowland environments."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 4: Natural Factors: Soil, Topography, and Biotic Factors
        # =====================================================================
        {
            "unit_order": 4,
            "unit_name": "Natural Factors: Soil, Topography, and Biotic Factors",
            "unit_description": "Soil chemical and physical properties (pH, depth, texture, structure, fertility), topographic parameters (slope gradient, aspect, drainage catena), and biotic agents (Rhizobium, mycorrhizae, pollinators vs pests and pathogens).",
            "lesson_title": "Soil, Topography, and Biotic Influences",
            "pages": [
                [
                    {
                        "type": "suggested_image",
                        "title": "Soil Profile Horizons and Structural Layers",
                        "content": {
                            "title": "Soil Profile Horizons and Structural Layers",
                            "caption": "A deep soil profile pit displaying distinct horizon layers: organic topsoil (A-horizon), mineral subsoil (B-horizon), and weathered parent rock (C-horizon)."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Soil, Topography & Biotics",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Analyze key **soil properties** determining land productivity: soil depth, texture, structure, nutrient fertility, and pH.",
                                "Evaluate how **topographic slope percentage, aspect, and drainage** dictate soil erosion risk and enterprise suitability.",
                                "Differentiate between **beneficial biotic agents** (decomposers, *Rhizobium*, pollinators) and **harmful biotic threats** (pests, weeds, pathogens).",
                                "Interpret a **topographical catena diagram** to match soil drainage regimes with compatible crops."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The Edaphic and Topographic Matrix",
                        "content": {
                            "title": "The Living Medium of Plant Nutrition",
                            "text": "While climate dictates atmospheric energy and water inputs, the **soil** (edaphic factor) and the **lay of the land** (topography) determine the physical anchor, moisture reservoir, nutrient exchange capacity, and mechanical accessibility of agricultural land."
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "Key Soil Properties Determining Fertility",
                        "content": {
                            "title": "Soil Physics and Chemical Dynamics",
                            "text": "### 1. Effective Soil Depth\n- **Deep Soils (> 100 cm)**: Provide unrestricted rooting volume for deep taproot perennials (coffee, fruit trees, tea), allowing plants to survive prolonged dry spells by accessing deep water reserves.\n- **Shallow Soils (< 30 cm)**: Restrict root expansion, cause root lodging during heavy winds, and dry out rapidly.\n\n### 2. Soil Texture & Structure\n- **Texture**: The relative proportion of Sand (0.05–2.0 mm), Silt (0.002–0.05 mm), and Clay (< 0.002 mm) particles. **Loam soils** (balanced sand, silt, and clay) offer ideal infiltration and water retention.\n- **Structure**: How individual particles aggregate into crumbs or granular peds. Porous crumb structures allow healthy root aeration and unhindered seedling emergence.\n\n### 3. Soil pH (Acidity vs Alkalinity)\n- **Optimal Range**: Most agricultural crops thrive between **pH 6.0 and 7.0**.\n- **Extreme Acidity (pH < 5.0)**: Locks up essential macronutrients (especially Phosphorus) and triggers toxic Aluminum/Manganese solubility.\n- **Remedy for Acid Soils**: Application of agricultural lime (Calcium carbonate) to neutralize excess Hydrogen ions ($H^+$)."
                        }
                    },
                    {
                        "type": "comparison_table",
                        "title": "Soil Texture Classes and Agronomic Properties",
                        "content": {
                            "title": "Soil Texture Comparison Matrix",
                            "headers": ["Property", "Sandy Soil", "Loam Soil (Optimal)", "Heavy Clay Soil"],
                            "rows": [
                                ["Water Infiltration Rate", "Very Rapid (> 50 mm/hr)", "Moderate (10–25 mm/hr)", "Very Slow (< 5 mm/hr)"],
                                ["Water Holding Capacity", "Extremely Poor (Drought prone)", "Excellent (Retains capillary water)", "Very High (Prone to waterlogging)"],
                                ["Nutrient Retention (CEC)", "Low (Nutrients leach easily)", "High (Balanced humus and clay)", "Very High (Binds minerals tightly)"],
                                ["Aeration & Root Penetration", "Excellent aeration", "Optimal balance of air and moisture", "Poor aeration when saturated; cracks when dry"],
                                ["Best Suited Enterprises", "Root crops (Carrots, Cassava), Cashews", "All commercial vegetables, Maize, Fruit trees", "Paddy rice, Aquaculture fish ponds, Brick-making"]
                            ]
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "Topography: Slope Gradient, Aspect, and Mechanization",
                        "content": {
                            "title": "The Influence of Slope Geometry on Agriculture",
                            "text": "### 1. Slope Gradient (% Slope)\n- **Flat Plains (0 – 2% Slope)**: Ideal for mechanization, large irrigation pivots, and livestock sheds, but prone to waterlogging if subsoil is impermeable.\n- **Gentle Slopes (2 – 8% Slope)**: Excellent natural drainage and moderate erosion risk; the prime zone for most commercial crop farming.\n- **Steep Slopes (15 – 30%+ Slope)**: Rapid surface runoff velocity, acute sheet and gully erosion hazard, and impossible for standard four-wheel tractors. Requires mandatory physical conservation (stone bench terraces, grass strips, agroforestry).\n\n### 2. Aspect (Slope Compass Orientation)\n- In hilly topography, slopes facing the equator or receiving morning sunshine warm up faster, accelerating photosynthesis and dew evaporation (reducing fungal disease outbreaks).\n- Slopes facing prevailing rain-bearing winds receive significantly higher precipitation (orographic effect) than rain-shadow leeward slopes."
                        }
                    },
                    {
                        "type": "definition_card",
                        "title": "Key Term: Topographical Aspect",
                        "content": {
                            "term": "Slope Aspect",
                            "definition": "The compass direction that a sloped landform faces (e.g. East-facing vs West-facing slope), which dictates solar radiation exposure, microclimate temperature, and prevailing wind impact.",
                            "example": "East-facing slopes receive early morning sunlight that dries dew off coffee leaves quickly, reducing the incidence of Coffee Berry Disease (CBD)."
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "Topographical Catena: Soil Drainage and Water Movement",
                        "content": {
                            "title": "The Slope-to-Valley Soil Sequence",
                            "text": "A **soil catena** is a sequence of distinct soil types occurring down a slope, formed from the same parent rock but differing because of varying relief and drainage:\n\n- **Upper Crest / Ridge**: Shallow, well-drained, coarser soils subject to continuous gravitational leaching.\n- **Mid-Slope**: Deep, fertile, well-drained loams with balanced organic matter; ideal for perennial and annual crops.\n- **Lower Valley Bottom (Depression)**: Heavy, dark, poorly drained clay soils (vertisols) where runoff and silt accumulate. Saturated conditions create anaerobic environments where upland crop roots rot, but provide ideal conditions for paddy rice and aquaculture."
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Topographical Catena and Drainage Suitability Diagram",
                        "content": {
                            "title": "Topographical Catena and Drainage Suitability Diagram",
                            "caption": "Cross-sectional engineering diagram of a soil catena showing the progression from shallow crest soils, to well-drained mid-slope loams, down to waterlogged valley-bottom clay basins."
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "Biotic Factors in Agricultural Ecosystems",
                        "content": {
                            "title": "The Living Web of Soil Biology and Pests",
                            "text": "### 1. Beneficial Biotic Organisms\n- **Soil Decomposers (Earthworms, Fungi, Actinomycetes)**: Macerate organic residues, aerate soil profiles with tunnels, and synthesize stable humus.\n- **Nitrogen-Fixing Bacteria (*Rhizobium*)**: Form symbiotic root nodules on legumes (beans, cowpeas, lucerne), converting atmospheric nitrogen ($N_2$) into ammonium ($NH_4^+$) directly available to crops.\n- **Mycorrhizal Fungi**: Extend root surface area by up to 1000%, dissolving and transporting insoluble phosphorus to plant roots.\n- **Insect Pollinators**: Honeybees, solitary bees, and hoverflies responsible for fruit setting in 75% of cultivated crops.\n\n### 2. Harmful Biotic Threats\n- **Invertebrate Pests**: Stem borers, fall armyworms, root-knot nematodes, and red spider mites that destroy vascular tissue and defoliate crops.\n- **Plant Pathogens**: Fungal spores (*Phytophthora infestans* late blight), bacterial wilts, and viral mosaic diseases.\n- **Invasive Weeds**: Parasitic *Striga hermonthica* (witchweed) in maize and aggressive *Lantana camara* in pastures that deplete moisture and outcompete crops."
                        }
                    },
                    {
                        "type": "callout",
                        "title": "Agronomic Principle: Symbiotic Nitrogen Fixation",
                        "content": {
                            "title": "Free Fertilizer from Legumes",
                            "text": "Inoculating legume seeds with *Rhizobium* bacteria before planting enables plants to fix up to **100 to 200 kg of atmospheric Nitrogen per hectare annually**, dramatically reducing synthetic fertilizer expenses while improving soil crumb structure!"
                        }
                    }
                ],
                [
                    {
                        "type": "mini_activity",
                        "title": "Field Practical: Soil Ribbon Texture and Drainage Test",
                        "content": {
                            "title": "Conducting Field Texture and Infiltration Tests",
                            "task": "1. Collect soil samples from two different school zones (e.g. a hillside slope vs a garden depression).\n2. Moisten a golf-ball-sized soil sample and knead it between your fingers. Try pushing it into a continuous ribbon between your thumb and forefinger:\n   - *Breaks before 2 cm*: Sandy Loam.\n   - *Forms a flexible ribbon 2.5–5 cm*: Loam / Clay Loam.\n   - *Forms a shiny, smooth ribbon > 5 cm*: Heavy Clay.\n3. Dig a 15 cm deep hole, fill it with 1 liter of water, and time how many minutes it takes to drain completely.",
                            "materials": ["Soil Samples", "Water Container", "Ruler", "Stopwatch"],
                            "safety": "Wash hands thoroughly with soap and water after handling soil."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Core Summary: Soil, Topography, and Biotics",
                        "content": {
                            "title": "Key Takeaways",
                            "text": "- **Soil pH (6.0–7.0)** optimizes nutrient availability; lime corrects toxic acidity.\n- **Loam soils** combine optimal aeration, infiltration, and nutrient retention.\n- **Gentle slopes (2–8%)** provide optimal drainage; **steep slopes (>15%)** require terraces.\n- **Valley bottoms** collect waterlogged clay suitable for rice and aquaculture.\n- **Beneficial microbes (*Rhizobium*, Mycorrhizae)** sustain biological soil fertility."
                        }
                    }
                ],
                [
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Soil pH and Topography Bottlenecks",
                        "content": {
                            "question": "A soil chemical test reveals that a farmer's mid-slope field has a pH of 4.6. Despite adding expensive Diammonium Phosphate (DAP) fertilizer, maize crops remain stunted with purplish leaves. What is the biochemical cause of this failure, and what is the proper remedy?",
                            "options": [
                                "The soil lacks clay particles; the farmer should add river sand to dilute soil acidity",
                                "The severe acidity (pH 4.6) causes Phosphorus from the fertilizer to be chemically fixed (locked up) by soluble Aluminum and Iron ions; the farmer must apply agricultural lime (calcium carbonate) to raise the pH to 6.0–6.5",
                                "The stunting is caused by excessive nitrogen fixation; the farmer must spray strong synthetic herbicides",
                                "The slope is too steep for fertilizer to dissolve; the farmer should bulldoze the hillside into a flat basin"
                            ],
                            "answer": "B",
                            "explanation": "At low soil pH (< 5.0), high concentrations of soluble Aluminum ($Al^{3+}$) and Iron ($Fe^{3+}$) chemically react with applied Phosphorus fertilizers, forming insoluble precipitates (Phosphorus fixation) that plant roots cannot absorb. Purplish leaves are a classic symptom of Phosphorus deficiency. Applying agricultural lime neutralizes acidity, raising pH above 6.0 and unlocking Phosphorus for crop uptake."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 5: Community Land-Use Observation
        # =====================================================================
        {
            "unit_order": 5,
            "unit_name": "Community Land-Use Observation",
            "unit_description": "Conducting structured community land-use surveys, mapping parcel classifications (arable, marginal, conservation, infrastructural), and diagnosing environmental degradation (riparian encroachment, gully erosion, deforestation).",
            "lesson_title": "Community Land-Use Patterns and Environmental Stewardship",
            "pages": [
                [
                    {
                        "type": "suggested_image",
                        "title": "Community Agricultural Landscape and Land Fragmentation",
                        "content": {
                            "title": "Community Agricultural Landscape and Land Fragmentation",
                            "caption": "A rural agricultural landscape showing the mosaic of smallholder arable plots, hillside pastures, forest boundaries, and community roads."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Community Land-Use Observation",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Design and execute a structured **community land-use transect walk**.",
                                "Classify community land parcels into **arable, marginal, conservation, and infrastructural zones**.",
                                "Identify critical signs of **land degradation**: riparian cultivation, roadside gullies, deforestation, and non-biodegradable waste.",
                                "Formulate sustainable community land-use remediation proposals."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The Purpose of Land-Use Surveys",
                        "content": {
                            "title": "Connecting Theoretical Agronomy to Local Reality",
                            "text": "A **land-use survey** is a systematic spatial investigation that maps how human populations utilize, manage, and impact the earth's surface. Moving into the local community allows learners to observe the real-world tensions between growing population pressure, economic survival, and environmental conservation."
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "Four Primary Land Categories in Local Communities",
                        "content": {
                            "title": "Spatial Classification Matrix",
                            "text": "During a community transect walk, agricultural land parcels can be classified into four distinct functional categories:\n\n### 1. Arable Agricultural Land\n- Land actively under cultivation for food staples, cash crops, horticulture, or improved fodder pastures.\n- Usually situated on fertile, accessible terrain with reliable rainfall or irrigation access.\n\n### 2. Marginal & Non-Arable Land\n- Rocky ridges, highly eroded slopes (>30%), arid scrubland, and swampy marshes.\n- Unsuitable for mechanical tillage, but sustainably utilized for apiculture, indigenous goat grazing, or protective agroforestry.\n\n### 3. Conservation & Riparian Reserves\n- Gazetted forest reserves, hill catchments, natural wetlands, and riverbank **riparian buffer zones**.\n- Crucial for recharging aquifers, preserving pollinator biodiversity, and stabilizing regional water towers.\n\n### 4. Residential and Infrastructural Land\n- Homesteads, rural markets, road reserves, processing factories, and waste disposal points."
                        }
                    },
                    {
                        "type": "comparison_table",
                        "title": "Land-Use Category Matrix and Vulnerability Profile",
                        "content": {
                            "title": "Community Land-Use Classification Matrix",
                            "headers": ["Category", "Primary Function", "Ecological Value", "Major Vulnerability / Human Threat"],
                            "rows": [
                                ["Arable Farmland", "Crop & intensive livestock production", "Soil organic matter & food supply", "Over-cultivation, nutrient mining, chemical pollution"],
                                ["Marginal Land", "Extensive grazing, apiculture, woodlots", "Erosion buffer & wildlife refuge", "Severe overgrazing, gully formation, bushfires"],
                                ["Riparian & Wetlands", "Water catchment & flood mitigation", "Highest biodiversity & water filtration", "Illegal crop encroachment, river siltation, drainage"],
                                ["Infrastructural", "Settlement, roads, market centers", "Economic logistics & shelter", "Encroachment onto prime agricultural soils"]
                            ]
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "Diagnosing Land Degradation in the Field",
                        "content": {
                            "title": "Visual Indicators of Ecosystem Damage",
                            "text": "When conducting field surveys, agricultural students must recognize the warning signs of environmental degradation:\n\n### 1. Riparian Encroachment\n- **Symptom**: Cultivating annual crops (maize, cabbages, sugarcane) right up to the water edge.\n- **Consequence**: Loss of the natural vegetative root filter, causing steep riverbanks to collapse into the water, silting up rivers and polluting downstream community drinking sources.\n\n### 2. Hillside Soil Erosion & Gully Formation\n- **Symptom**: Downhill ploughing furrows, exposed tree roots, pedestals of soil under stones, and deep roadside chasms.\n- **Consequence**: Irreversible loss of fertile topsoil, leaving sterile subsoil that cannot support crops.\n\n### 3. Deforestation for Fuelwood and Charcoal\n- **Symptom**: Stripping indigenous tree canopies from steep catchment hills.\n- **Consequence**: Increased raindrop splash impact, drying up of local springs, and microclimatic desertification."
                        }
                    },
                    {
                        "type": "callout",
                        "title": "Environmental Law: Riparian Buffer Regulations in Kenya",
                        "content": {
                            "title": "The 6-to-30 Meter Riparian Rule",
                            "text": "Under Kenyan environmental regulations (EMCA / Water Resources Authority), agricultural landowners are legally required to maintain a permanent, uncultivated buffer strip of indigenous trees and grass measuring **at least 6 meters (up to 30 meters depending on river width)** from the highest water mark of any river or stream!"
                        }
                    }
                ],
                [
                    {
                        "type": "step_process",
                        "title": "Protocol for Conducting a Community Transect Walk",
                        "content": {
                            "title": "5-Step Transect Survey Workflow",
                            "steps": [
                                "1. **Establish a 1-Kilometer Transect Route**: Select a safe walking path that crosses diverse topographies (e.g. from an upper ridge, through smallholder farms, down to a river valley).",
                                "2. **Record Parcel Boundaries & Utilities**: Note crops grown, livestock kept, and farming techniques used along the route.",
                                "3. **Audit Soil Conservation Infrastructure**: Check whether sloped fields possess stone terraces, grass filter strips, or cut-off drains.",
                                "4. **Log Degradation Hotspots**: Photograph and geo-tag signs of gully erosion, riparian cultivation, and plastic waste accumulation.",
                                "5. **Interview Community Landholders**: Inquire about land ownership history and changes in soil fertility over the past decade."
                            ]
                        }
                    },
                    {
                        "type": "did_you_know",
                        "title": "Did You Know: Siltation of Hydroelectric Dams",
                        "content": {
                            "title": "Upstream Erosion Shuts Down National Power",
                            "text": "Severe soil erosion caused by poor farming practices in upstream catchment areas washes millions of tons of topsoil into major rivers like the Tana. This silts up hydroelectric dams (such as Masinga), reducing national electricity generation and causing frequent power blackouts!"
                        }
                    }
                ],
                [
                    {
                        "type": "mini_activity",
                        "title": "Field Project: Community Land-Use Transect Mapping",
                        "content": {
                            "title": "Conducting Your Local Transect Survey",
                            "task": "In assigned groups of four, execute the 1-km community transect walk:\n\n1. Compile a structured table with 4 columns: *Parcel ID*, *Observed Land Use*, *Topographic Position*, and *Environmental Issues Spotted*.\n2. Identify the single most severe degradation issue observed along your route.\n3. Draft a 3-point remediation action plan proposing realistic soil conservation or agroforestry solutions that local farmers could implement at low cost.",
                            "materials": ["Clipboards", "Transect Recording Sheet", "Pens", "Digital Camera / Phone"],
                            "safety": "Stay together in designated groups, observe road traffic safety along public roads, and respect private farm fences."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Core Summary: Community Land Stewardship",
                        "content": {
                            "title": "Key Takeaways",
                            "text": "- **Transect walks** reveal spatial land-use patterns across topographical zones.\n- **Riparian buffers (6–30m)** are legally required to prevent river siltation and preserve water quality.\n- **Downhill cultivation** accelerates gully formation and topsoil loss.\n- **Sustainable community zoning** balances arable food production with environmental watershed protection."
                        }
                    }
                ],
                [
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Riparian Conservation Regulations",
                        "content": {
                            "question": "During a community land-use survey, students observe a farmer clearing native riverside reeds to plant tomatoes right up to the flowing stream edge. Which of the following is the most severe long-term environmental and legal consequence of this practice?",
                            "options": [
                                "The tomatoes will grow too large and burst due to excess humidity",
                                "The riverbank will lose its binding root network, causing soil collapse during floods, severe water siltation, downstream dam sedimentation, and violation of environmental protection laws",
                                "The river water will reverse its flow back up the mountain slope",
                                "The tomato roots will turn the freshwater stream into salty sea water"
                            ],
                            "answer": "B",
                            "explanation": "Clearing vegetation from the riparian zone strips away the root matrix that anchors riverbanks. During heavy rains, runoff erodes the bare banks directly into the stream, causing heavy siltation, muddying drinking water, destroying aquatic fish habitats, and accelerating dam sedimentation downstream. It also violates national environmental regulations mandating protected riparian buffers."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 6: Land-Productivity Decision Exercise
        # =====================================================================
        {
            "unit_order": 6,
            "unit_name": "Land-Productivity Decision Exercise",
            "unit_description": "Data-driven farm evaluation, multi-parameter land zoning decision matrix (integrating slope %, soil depth, pH, drainage, and water proximity), and farm layout optimization.",
            "lesson_title": "Agribusiness Farm Zoning and Decision Exercise",
            "pages": [
                [
                    {
                        "type": "suggested_image",
                        "title": "Data-Driven Agricultural Land Planning and Zoning",
                        "content": {
                            "title": "Data-Driven Agricultural Land Planning and Zoning",
                            "caption": "An aerial survey view showing precision-zoned agricultural land with distinct circular center-pivot fields, contoured hillsides, and protected water corridors."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Farm Zoning Decisions",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Master the principle of **optimal land allocation** in commercial agribusiness management.",
                                "Apply a **multi-parameter decision framework** integrating slope gradient, soil depth, drainage, pH, and water availability.",
                                "Allocate farm zones to compatible enterprises (aquaculture, intensive horticulture, pastures, woodlots, farmstead).",
                                "Construct an integrated farm masterplan that maximizes profitability while ensuring zero land degradation."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The Principle of Optimal Land Allocation",
                        "content": {
                            "title": "Aligning Enterprise Economics with Ecological Land Capacity",
                            "text": "In commercial agribusiness, farm profitability is not achieved by forcing random crops onto unsuitable land. **Optimal land allocation** is the disciplined process of dividing a farm into distinct micro-zones and assigning each zone to the enterprise for which it is naturally and economically best suited.\n\n- **Economic Benefit**: Minimizes expensive corrective inputs (e.g. avoiding massive earthmoving or excessive artificial drainage).\n- **Ecological Benefit**: Prevents soil erosion, waterlogging, and chemical leaching before they start."
                        }
                    }
                ],
                [
                    {
                        "type": "step_process",
                        "title": "4-Stage Diagnostic Protocol for Farm Evaluation",
                        "content": {
                            "title": "Conducting a Comprehensive Farm Land Audit",
                            "steps": [
                                "1. **Stage 1: Topographic Slope Survey**: Measure slope percentages across the property to classify flat plains (0–2%), gentle rolling slopes (2–8%), moderate slopes (8–15%), and steep hillsides (>15%).",
                                "2. **Stage 2: Edaphic Soil Profile Analysis**: Dig test pits to evaluate soil depth (shallow vs deep), texture (sand, loam, clay), drainage rate, and chemical pH.",
                                "3. **Stage 3: Water Resource & Hydrology Mapping**: Locate reliable water sources (rivers, boreholes, runoff collection points) and map natural drainage channels and flood plains.",
                                "4. **Stage 4: Infrastructure & Access Logistics**: Identify prevailing windward boundaries, main access roads for product dispatch, and proximity to the farmstead."
                            ]
                        }
                    },
                    {
                        "type": "definition_card",
                        "title": "Key Term: Land Evaluation",
                        "content": {
                            "term": "Land Evaluation",
                            "definition": "The formal assessment of land performance and physical properties when used for specified agricultural purposes, providing a rational basis for farm zoning decisions.",
                            "example": "Testing a 5-acre property to confirm that a low-lying valley has 40% clay content before investing capital in commercial fish ponds."
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "The Farm Zoning Decision Matrix",
                        "content": {
                            "title": "Matching Land Parameters to Agribusiness Enterprises",
                            "text": "By synthesizing topographic and soil data, farm managers allocate acreage using a standardized decision matrix:\n\n### Zone A: Heavy Clay Lowlands (0–2% Slope, Poor Drainage)\n- **Enterprise Suitability**: Aquaculture (earthen fish ponds), paddy rice, arrowroots (*nduma*), or water-harvesting storage pans.\n- *Avoid*: Citrus orchards, potatoes, and livestock sheds (causes severe root rot and foot rot).\n\n### Zone B: Fertile Gentle Slopes (2–8% Slope, Deep Loam, Well-Drained)\n- **Enterprise Suitability**: High-value commercial horticulture (tomatoes, capsicums, cabbages), grain crops (maize, beans), or intensive zero-grazing fodder.\n- *Requirements*: Contour planting, crop rotation, and regular organic manuring.\n\n### Zone C: Steep & Rocky Hillsides (>15% Slope, Shallow Soil)\n- **Enterprise Suitability**: Apiculture (beehives), drought-hardy agroforestry woodlots (*Grevillea*, *Melia volkensii*), and fenced rotational goat pasture.\n- *Requirements*: Mandatory contour stone terracing and vegetative grass barriers.\n\n### Zone D: Windward Farm Boundaries\n- **Enterprise Suitability**: Multi-story windbreak belts (tall timber trees flanked by dense shrubs) to protect delicate horticultural crops from mechanical wind stress."
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Land Allocation Decision Flowchart",
                        "content": {
                            "title": "Land Allocation Decision Flowchart",
                            "caption": "Decision tree algorithm showing how slope percentage, soil drainage class, and soil depth determine the correct agricultural enterprise."
                        }
                    }
                ],
                [
                    {
                        "type": "comparison_table",
                        "title": "Enterprise Compatibility across Farm Land Zones",
                        "content": {
                            "title": "Zone-Enterprise Compatibility Matrix",
                            "headers": ["Land Characteristic", "Highly Compatible Enterprise", "Incompatible Enterprise", "Agronomic Justification"],
                            "rows": [
                                ["Valley Basin (Clay, Waterlogged)", "Aquaculture (Tilapia / Catfish)", "Irish Potatoes / Avocado Orchard", "Clay prevents pond seepage; waterlogging rots potato and avocado roots within days"],
                                ["Gentle Mid-Slope (Deep Loam)", "Commercial Vegetable Horticulture", "Extensive Beef Cattle Grazing", "High-potential fertile loam produces 10x higher profit under intensive vegetables than rough grazing"],
                                ["Steep Rocky Hillside (>20% Slope)", "Modern Apiculture (Beehives) + Woodlot", "Mechanized Tractor Grain Farming", "Beehives require zero soil depth; tractors will tip over and cause massive erosion"],
                                ["Farmstead Boundary (High Wind Exposure)", "Agroforestry Windbreak Belt", "Unsheltered Banana Plantation", "Windbreaks filter gale winds; strong winds snap banana pseudo-stems and shred leaves"]
                            ]
                        }
                    }
                ],
                [
                    {
                        "type": "mini_activity",
                        "title": "Design Challenge: Creating a 5-Acre Farm Masterplan",
                        "content": {
                            "title": "Practical Farm Zoning Simulation",
                            "task": "You have been hired as an agricultural consultant to zone a 5-acre property with the following survey profile:\n\n- **North Zone**: 1 acre of steep (18% slope), rocky hillside.\n- **Center Zone**: 2.5 acres of gently sloping (4% slope), deep, fertile sandy-clay loam.\n- **South Zone**: 1 acre of flat, low-lying heavy clay basin bordering a permanent stream.\n- **West Boundary**: High-wind corridor along the main access road.\n\n**Your Deliverable**: Draw a scaled sketch map allocating the homestead, commercial cabbage patch, tilapia fish pond, 10 beehives, windbreak belt, and a zero-grazing dairy unit. Provide a 1-sentence agronomic justification for each placement.",
                            "materials": ["Graph Paper", "Ruler", "Pencils", "Eraser"],
                            "safety": "Ensure clean, legible technical drawings with standard map keys and compass direction indicators."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Core Summary: Data-Driven Land Allocation",
                        "content": {
                            "title": "Key Takeaways",
                            "text": "- **Optimal land allocation** matches enterprise biology to natural soil and slope properties.\n- **Waterlogged clay basins** are ideal for aquaculture, not root crops.\n- **Gentle loam slopes** maximize return on investment under intensive horticulture.\n- **Steep rocky hillsides** yield high revenue through apiculture without risking soil erosion."
                        }
                    }
                ],
                [
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Resolving a Farm Zoning Dilemma",
                        "content": {
                            "question": "A newly formed youth agribusiness group acquires a 4-acre farm. The lower 1 acre is a flat valley depression with heavy black-cotton clay soil that holds standing water for months, while the upper 3 acres consist of fertile, well-drained loamy slopes. How should they allocate their enterprises to maximize profit and prevent losses?",
                            "options": [
                                "Plant commercial French beans and tomatoes across the entire 4 acres, using tractors in the wet depression",
                                "Construct earthen aquaculture tilapia ponds in the lower 1-acre clay depression, and establish high-value drip-irrigated vegetable horticulture and a dairy shed on the upper 3-acre loamy slopes",
                                "Build a permanent zero-grazing dairy cattle unit in the wet clay depression, and leave the upper slopes uncultivated",
                                "Excavate the upper slopes into sand mines and dump the rocky rubble into the wet depression"
                            ],
                            "answer": "B",
                            "explanation": "Heavy black-cotton clay in a waterlogged depression is completely unsuitable for French beans or animal housing (causes root rot and severe cattle foot rot). However, heavy clay is the gold standard for aquaculture ponds because it holds water with zero seepage. Placing the vegetable horticulture and dairy unit on the well-drained upper loamy slopes ensures excellent root aeration, easy farm management, and maximum total farm profitability."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 7: Importance of Land in Production
        # =====================================================================
        {
            "unit_order": 7,
            "unit_name": "Importance of Land in Production",
            "unit_description": "Multi-dimensional value of agricultural land: economic capital asset, social/cultural livelihood anchor, ecological watershed matrix, and the implications of its non-reproducible, finite supply.",
            "lesson_title": "Economic, Social, and Environmental Value of Land",
            "pages": [
                [
                    {
                        "type": "suggested_image",
                        "title": "Agricultural Production and National Food Security",
                        "content": {
                            "title": "Agricultural Production and National Food Security",
                            "caption": "A bountiful harvest of fresh agricultural produce, representing the critical role of fertile land in sustaining household livelihoods and national food sovereignty."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: The Multi-Dimensional Value of Land",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Analyze the **economic importance of land** as a primary factor of production, capital asset, and collateral.",
                                "Evaluate the **social and cultural significance** of land tenure in Kenyan communities.",
                                "Explain the **environmental ecosystem services** provided by healthy agricultural land (carbon sequestration, water filtration, biodiversity).",
                                "Discuss the economic consequences of land being a **finite, non-reproducible asset** amidst rapid population growth."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The Foundational Role of Land in Human Society",
                        "content": {
                            "title": "More Than Just Soil: The Engine of Economic Life",
                            "text": "Land is unique among all economic factors of production. It is not merely real estate; it is the physical platform that generates food, raw materials, employment, and wealth, while sustaining the biological life-support systems of the planet."
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "Economic Dimensions of Agricultural Land",
                        "content": {
                            "title": "Capital, Raw Materials, and Financial Leverage",
                            "text": "In national economics and agribusiness, land serves four distinct financial functions:\n\n### 1. Primary Factor of Production\n- Without physical land, no agricultural enterprise (crops, livestock, aquaculture, agroforestry) can exist. It provides the biological substrate and physical space for enterprise operations.\n\n### 2. Supplier of Essential Raw Materials\n- Land yields soil minerals, water resources, timber, plant biomass, and natural pasture that supply the agro-processing, food manufacturing, and textile industries.\n\n### 3. Capital Asset & Wealth Generation\n- Landowners generate recurring financial returns through direct agricultural profits, leasehold rent, or royalties.\n- Unlike machinery or vehicles that depreciate with age, well-managed agricultural land with fertile soil **appreciates steadily in financial value** over time.\n\n### 4. Collateral for Financial Credit Expansion\n- Legal Title Deeds represent the most secure and universally accepted collateral for commercial banks and agricultural credit institutions (e.g. Agricultural Finance Corporation - AFC), unlocking capital for farm mechanization."
                        }
                    },
                    {
                        "type": "definition_card",
                        "title": "Key Term: Land as Capital Collateral",
                        "content": {
                            "term": "Collateral Asset",
                            "definition": "A valuable physical property (such as a Freehold Title Deed) pledged by a borrower to a lender to secure a loan, which the lender can legally seize if the borrower defaults.",
                            "example": "A farmer using their 5-acre title deed as security to obtain a 2,000,000 KES bank loan to construct a commercial greenhouse and drill a solar borehole."
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "Social, Cultural, and Environmental Dimensions",
                        "content": {
                            "title": "Identity, Community Security, and Ecological Services",
                            "text": "### 1. Social and Cultural Value\n- **Household Food & Livelihood Security**: In rural Kenya, land is the ultimate safety net; owning a productive parcel guarantees household subsistence even during economic recessions.\n- **Ancestral Heritage & Identity**: Land represents family lineage, burial sites, and community belonging, passed down as a sacred intergenerational trust.\n- **Social Prestige & Empowerment**: Land ownership provides legal standing, independence, and social security, particularly when secured by women and youth groups.\n\n### 2. Environmental & Ecological Value\n- **Hydrological Catchment**: Healthy vegetative land acts as a giant sponge, capturing rainfall, filtering sediments, and steadily recharging underground water aquifers.\n- **Carbon Sequestration**: Agricultural soils and agroforestry woodlots absorb atmospheric carbon dioxide ($CO_2$), mitigating global climate change.\n- **Biodiversity Habitat**: Provides refuge for pollinators (bees), predatory beneficial insects, and soil microorganisms essential for ecological balance."
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Multi-Dimensional Value Matrix of Agricultural Land",
                        "content": {
                            "title": "Multi-Dimensional Value Matrix of Agricultural Land",
                            "caption": "Conceptual framework illustrating the interlocking Economic, Social/Cultural, and Environmental values of agricultural land."
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "Land as a Non-Reproducible and Inelastic Asset",
                        "content": {
                            "title": "The Economic Dilemma of Fixed Supply vs Rising Demand",
                            "text": "A defining economic characteristic of land is that it is **non-reproducible**; human industry cannot manufacture new physical land area on earth. Its total supply is perfectly inelastic.\n\n### The Impact of Demographic Pressure\n- **Population Growth**: As national population expands, the per-capita availability of agricultural land shrinks.\n- **Subdivision & Fragmentation**: Agricultural farms are divided into smaller, economically unviable fragments, threatening national food security.\n- **Urban Sprawl Encroachment**: Rapidly expanding cities and real-estate housing developments pave over prime, high-potential agricultural soils (e.g. historical coffee estates in Kiambu being converted into concrete housing).\n- **The Imperative for Sustainable Intensification**: Because we cannot expand land area, farmers must adopt **intensive conservation agriculture** (drip irrigation, organic manuring, vertical farming) to produce more food from smaller plots."
                        }
                    },
                    {
                        "type": "comparison_table",
                        "title": "Land vs Other Factors of Production",
                        "content": {
                            "title": "Economic Comparison of Production Factors",
                            "headers": ["Economic Characteristic", "Land", "Labor", "Capital (Machinery / Funds)", "Entrepreneurship"],
                            "rows": [
                                ["Physical Supply", "Fixed & Non-Reproducible", "Variable (Population growth)", "Manufacturable & Expandable", "Developable through education"],
                                ["Geographic Mobility", "Completely Immobile (Fixed location)", "Geographically Mobile", "Highly Mobile across borders", "Mobile"],
                                ["Depreciation over Time", "Appreciates if conserved; does not wear out", "Ages and depreciates", "Wears out, rusts, and depreciates", "Subject to health and lifecycle"],
                                ["Economic Reward", "Rent / Capital appreciation", "Wages / Salaries", "Interest on investment", "Net Profit"]
                            ]
                        }
                    }
                ],
                [
                    {
                        "type": "mini_activity",
                        "title": "Classroom Debate: Agricultural Land vs Urban Real Estate",
                        "content": {
                            "title": "Debating Land Protection Policies",
                            "task": "Divide the class into two debate teams to argue the following policy motion:\n\n*\"Motion: The government should legally prohibit the conversion of prime agricultural land into residential real-estate housing schemes.\"*\n\n- **Team Pro (Food Security & Conservation)**: Argue why prime fertile soils must be legally preserved to feed growing urban populations.\n- **Team Con (Urbanization & Housing Rights)**: Argue the economic need for modern housing, commercial hubs, and industrial employment.\n- Record the top 3 arguments presented by each side.",
                            "materials": ["Debate Guidelines", "Notebook", "Timer"],
                            "safety": "Maintain respectful, academic debate etiquette at all times."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Core Summary: The Value of Land",
                        "content": {
                            "title": "Key Takeaways",
                            "text": "- **Economically**, land provides raw materials, appreciates in value, and acts as bankable loan collateral.\n- **Socially**, land ensures household food security, social stability, and ancestral identity.\n- **Environmentally**, healthy land filters fresh water, sequesters carbon, and preserves pollinator biodiversity.\n- **Land is finite and non-reproducible**, making the protection of fertile soils from urban encroachment a vital national priority."
                        }
                    }
                ],
                [
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Economic Uniqueness of Land",
                        "content": {
                            "question": "Which of the following economic characteristics uniquely distinguishes agricultural land from manufactured capital assets like tractors or greenhouses?",
                            "options": [
                                "Land rapidly depreciates in value within 3 years of purchase regardless of management",
                                "Land is completely immobile and its total physical supply on earth is fixed and non-reproducible, meaning it cannot be manufactured when demand increases",
                                "Land can be easily transported to urban markets where crop prices are higher",
                                "Land requires zero labor or capital inputs to generate commercial agricultural profit"
                            ],
                            "answer": "B",
                            "explanation": "Unlike manufactured capital equipment (tractors, tools, greenhouses) which can be industrially produced, relocated, and eventually wear out through mechanical depreciation, physical land is spatially immobile, cannot be manufactured, and possesses a fixed supply. When managed sustainably with soil conservation and organic inputs, agricultural land maintains or increases its fertility and economic value indefinitely."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 8: Access, Utility and Productivity Synthesis
        # =====================================================================
        {
            "unit_order": 8,
            "unit_name": "Access, Utility and Productivity Synthesis",
            "unit_description": "Synthesizing the tripartite relationship between land tenure security, enterprise utility choice, and long-term land productivity. The virtuous cycle of secure tenure vs the vicious cycle of insecure extraction.",
            "lesson_title": "Synthesis: Tenure Security, Land Utility, and Productivity",
            "pages": [
                [
                    {
                        "type": "suggested_image",
                        "title": "Terraced Agricultural Valley: The Fruit of Long-Term Investment",
                        "content": {
                            "title": "Terraced Agricultural Valley: The Fruit of Long-Term Investment",
                            "caption": "A steep agricultural valley in Kenya transformed into highly productive, stabilized bench terraces—a direct outcome of secure land tenure and long-term farmer stewardship."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Synthesis of Land Systems",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Synthesize the direct systemic links between **how land is accessed (tenure)**, **how it is utilized (enterprise)**, and **its ultimate productivity**.",
                                "Analyze the **Virtuous Cycle of Secure Land Tenure** (capital investment, soil conservation, sustained high yields).",
                                "Examine the **Vicious Cycle of Insecure Land Access** (short-term extraction, soil mining, land degradation).",
                                "Formulate innovative leasing and tenure agreements that incentivize sustainable soil conservation on rented farms."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The Tripartite Land System",
                        "content": {
                            "title": "How Ownership Shapes Land Health and Wealth",
                            "text": "Agricultural success is not determined by soil chemistry alone; it is fundamentally driven by the institutional framework of **land tenure**. The legal terms under which a farmer occupies a piece of land directly dictate their time horizon, investment willingness, and environmental stewardship."
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "The Virtuous Cycle of Secure Land Tenure",
                        "content": {
                            "title": "Long-Term Horizons Create Sustainable Wealth",
                            "text": "When a farmer holds secure, long-term title to their land (through registered freehold purchase or formal inheritance with title deed):\n\n1. **Capital Commitment**: The farmer is motivated to invest substantial capital into permanent farm infrastructure (drilling boreholes, installing underground irrigation pipes, building stone terraces, and establishing zero-grazing sheds).\n2. **Soil Stewardship**: They practice regenerative agriculture—applying heavy farmyard compost, rotating crops, planting green manure cover crops, and establishing slow-growing agroforestry windbreaks.\n3. **Compounding Soil Fertility**: The soil organic matter increases, improving crumb structure, cation exchange capacity (CEC), and water retention.\n4. **High Sustainable Yields & Prosperity**: Crop and livestock yields remain high even during droughts; farm profitability rises, and the titled asset serves as collateral for further business expansion."
                        }
                    },
                    {
                        "type": "step_process",
                        "title": "The 4 Stages of the Virtuous Tenure Cycle",
                        "content": {
                            "title": "The Upward Spiral of Secure Land Stewardship",
                            "steps": [
                                "1. **Secure Legal Title Deed**: Provides multi-decade psychological confidence and formal banking collateral.",
                                "2. **Permanent Capital Investment**: Construction of stone terraces, water dams, solar irrigation, and agroforestry orchards.",
                                "3. **Soil Organic Health Compounding**: Build-up of microbial humus, active earthworms, and high drought resilience.",
                                "4. **Sustained High Yields & Wealth**: Maximized farm profits reinvested into continuous enterprise modernization."
                            ]
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "The Vicious Cycle of Insecure Land Access",
                        "content": {
                            "title": "Short-Term Soil Mining and Environmental Collapse",
                            "text": "When land tenure is short-term, uncertain, or contested (e.g. 1-year informal verbal leases or disputed family plots):\n\n1. **Short Time Horizon**: The tenant farmer focuses strictly on extracting maximum cash within a single cropping season.\n2. **Zero Conservation Investment**: The tenant refuses to invest money or labor into stone terracing, lime application, or tree planting because the benefits will be reaped by the landlord in future years.\n3. **Soil Mining & Chemical Exploitation**: The tenant applies cheap, acidifying synthetic fertilizers to force quick yields and cultivates steep slopes without erosion barriers.\n4. **Rapid Land Degradation**: Topsoil washes away in gullies, soil pH plummets, organic matter collapses, and yields decline drastically. The tenant abandons the depleted land, leaving a sterile wasteland."
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Virtuous vs Vicious Agricultural Cycles Diagram",
                        "content": {
                            "title": "Virtuous vs Vicious Agricultural Cycles Diagram",
                            "caption": "Comparative systems diagram contrasting the upward wealth-building loop of secure land tenure with the downward spiral of short-term soil mining on insecure leases."
                        }
                    }
                ],
                [
                    {
                        "type": "comparison_table",
                        "title": "Secure vs Insecure Land Tenure Comparison",
                        "content": {
                            "title": "Systemic Impacts of Land Tenure on Farm Management",
                            "headers": ["Dimension", "Secure Tenure (Title / Long Lease)", "Insecure Tenure (Short / Informal Lease)"],
                            "rows": [
                                ["Planning Timeframe", "Multi-decade / Intergenerational", "Single season (6 to 12 months)"],
                                ["Soil Conservation Strategy", "Permanent stone terraces, agroforestry, heavy compost", "Zero conservation; downhill planting for speed"],
                                ["Enterprise Selection", "Perennial crops (tea, coffee, fruits), high-grade dairy", "Quick annuals only (cabbages, maize, beans)"],
                                ["Infrastructure Investment", "Greenhouses, boreholes, permanent fencing", "Temporary polythene sheets, zero permanent structures"],
                                ["Long-Term Land Condition", "Enhanced fertility, high humus, zero erosion", "Severely eroded topsoil, acidified, nutrient-depleted"]
                            ]
                        }
                    },
                    {
                        "type": "callout",
                        "title": "Agronomic Contract Innovation: Conservation Lease Agreements",
                        "content": {
                            "title": "How Smart Landowners Protect Their Soil on Leased Farms",
                            "text": "Modern agribusiness landowners prevent soil mining by writing **Conservation Clauses** into lease agreements: offering 5-year lease stability and deducting the cost of lime, terracing, and compost manure from the tenant's annual rent!"
                        }
                    }
                ],
                [
                    {
                        "type": "mini_activity",
                        "title": "Case Simulation: Resolving a Tenant-Landowner Conservation Deadlock",
                        "content": {
                            "title": "Drafting a Sustainable Lease Compromise",
                            "task": "Read the following scenario:\n\n*\"Farmer Asha leases 3 acres of sloped land on a 2-year lease. Heavy rainstorms are creating gullies that threaten to wash away the topsoil. Constructing stone terraces and planting Napier grass buffers will cost 35,000 KES and take 3 years to break even. The landowner refuses to build the terraces and threatens to raise the rent if the land looks improved.\"*\n\n**Your Task**: In pairs, act as agricultural mediators and draft a 4-point amended lease agreement that protects the landowner's property while giving Asha the economic incentive to construct the terraces.",
                            "materials": ["Lease Contract Template", "Notebook", "Pen"],
                            "safety": "Focus on win-win legal compromises based on agribusiness economics."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Core Summary: Tenure and Sustainability Synthesis",
                        "content": {
                            "title": "Key Takeaways",
                            "text": "- **Secure tenure** creates a virtuous cycle of capital investment, organic soil building, and high sustainable yields.\n- **Insecure short-term leases** trigger a vicious cycle of soil mining, chemical acidification, and gully erosion.\n- **Innovative long-term leases** with conservation rent-rebates enable tenant farmers to protect rented soils sustainably."
                        }
                    }
                ],
                [
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Systems Impact of Insecure Land Leases",
                        "content": {
                            "question": "Why do farmers operating on short, 1-year informal land leases rarely plant avocado orchards, establish stone terraces, or apply heavy agricultural lime to acidic soils?",
                            "options": [
                                "Avocado trees and stone terraces are illegal to establish on leased land under Kenyan law",
                                "These permanent investments require substantial upfront capital and take 3 to 5 years to generate economic returns; without long-term tenure security, the landlord may terminate the lease before the tenant recoups their investment",
                                "Lime and stone terraces immediately reduce crop yields during the first two seasons",
                                "Short-term tenants lack the physical tools required to dig terrace channels"
                            ],
                            "answer": "B",
                            "explanation": "Permanent soil conservation structures (stone terraces), chemical soil reclamation (liming), and perennial tree crops (avocados, macadamia) require significant capital expenditure and multiple years to reach profitability. On a 1-year insecure lease, a tenant faces the severe financial risk that the landowner will evict them or sharply increase the rent once the land is improved, making short-term soil mining the only rational economic choice under insecure tenure."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 9: Applied Local Case Study
        # =====================================================================
        {
            "unit_order": 9,
            "unit_name": "Applied Local Case Study",
            "unit_description": "Comprehensive diagnostic evaluation of Wekesa's family farm in Nyandarua County. Identifying topographical downhill erosion, extreme soil acidity (pH 4.8), tenure insecurity, and animal husbandry bottlenecks, followed by a multi-phase farm turnaround plan.",
            "lesson_title": "Applied Agribusiness Case Study: Wekesa's Farm Turnaround",
            "pages": [
                [
                    {
                        "type": "suggested_image",
                        "title": "Highland Potato Cultivation on Sloping Farmland",
                        "content": {
                            "title": "Highland Potato Cultivation on Sloping Farmland",
                            "caption": "A smallholder potato farm on an undulating hillside, demonstrating the challenges of managing sloped terrain, soil fertility, and crop yields."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Farm Case Study Diagnostics",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Conduct a multi-parameter diagnostic audit of a real-world Kenyan smallholder farm (**Wekesa's Farm in Nyandarua**).",
                                "Identify critical agronomic bottlenecks: **downhill cultivation erosion, acute soil acidity (pH 4.8), tenure insecurity, and open-mud livestock stress**.",
                                "Formulate an integrated 4-step farm turnaround masterplan (terracing, liming, enterprise diversification, legal succession).",
                                "Evaluate the financial and environmental outcomes of the rehabilitated farm system."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The Power of Applied Case Study Diagnostics",
                        "content": {
                            "title": "From Theory to High-Impact Agronomic Problem-Solving",
                            "text": "Modern agricultural scientists and agribusiness managers must possess the diagnostic capability to visit a struggling farm, identify the root physical and institutional causes of failure, and formulate an integrated turnaround strategy that restores profitability and ecological health."
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "The Case Scenario: Wekesa's 4-Acre Farm in Nyandarua",
                        "content": {
                            "title": "Farm Baseline Survey and Symptoms of Distress",
                            "text": "Wekesa inherited a 4-acre family farm in the high-altitude highlands of **Nyandarua County (elevation 2,400 m)**. A baseline audit reveals the following profile:\n\n### The Land & Soil Parameters\n- **Topography**: Situated on a continuous 12% hillside slope.\n- **Soil Test Results**: Deep clay loam, but **severely acidic at pH 4.8** with severe phosphorus fixation.\n- **Current Cropping Practice**: Cultivating Irish potatoes across all 4 acres, with planting furrows running straight **downhill** along the slope.\n\n### Livestock & Infrastructure\n- Keeps 2 high-grade Holstein Friesian dairy cows in an open, unroofed dirt paddock that turns into deep mud during the rainy season.\n- Cows suffer from chronic foot-rot, mastitis, and produce only 5 liters of milk per day.\n\n### The Legal Status & Financial Crisis\n- The land is still registered under his deceased grandfather's name (no personal title deed).\n- **Yield Collapse**: Potato yields have plummeted from 80 bags/acre to 25 bags/acre over the last 3 years, and local commercial banks refuse to give him farm development loans."
                        }
                    },
                    {
                        "type": "comparison_table",
                        "title": "Wekesa's Farm Baseline vs Optimal Agronomic Standards",
                        "content": {
                            "title": "Diagnostic Farm Audit Matrix",
                            "headers": ["Farm Parameter", "Wekesa's Current Practice", "Agronomic Standard", "Observed Consequence / Defect"],
                            "rows": [
                                ["Slope Cultivation", "Downhill furrows on 12% slope", "Contour planting with stone terraces & grass strips", "Severe sheet & rill erosion; wash-out of seed tubers & fertilizer"],
                                ["Soil Chemistry", "pH 4.8 (Highly Acidic), no lime", "pH 6.0 – 6.5 (Balanced with agricultural lime)", "Phosphorus locked up; high fertilizer costs yield zero response"],
                                ["Enterprise Allocation", "100% monoculture Irish potatoes", "Diversified zoning (potatoes, horticulture, dairy, trees)", "Severe crop disease accumulation (late blight) & total market risk"],
                                ["Livestock Housing", "Open unroofed mud paddock", "Dry zero-grazing unit with concrete floor & cubicles", "Cold stress, foot rot, low milk yield (5 L/day), wasted manure"],
                                ["Land Tenure", "Unregistered inherited land (grandfather's name)", "Formal succession with clean Freehold Title Deed", "Inability to access commercial bank credit or agricultural loans"]
                            ]
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "Root-Cause Analysis of Wekesa's Crisis",
                        "content": {
                            "title": "The Four Interlocking Failure Points",
                            "text": "Wekesa's farm collapse is caused by four critical errors that compound one another:\n\n### 1. Hydrodynamic Topographic Error\nCultivating straight downhill on a 12% slope turns planting furrows into high-velocity water chutes during torrential rains. Runoff accelerates from 0.5 m/s to over 2.5 m/s, stripping fertile topsoil, washing away expensive DAP fertilizer, and exposing potato tubers to sunlight and greening.\n\n### 2. Edaphic Chemical Lockup\nAt pH 4.8, Aluminum ions are highly soluble and bind with inorganic phosphate ions from DAP fertilizer, creating insoluble Aluminum Phosphate. Wekesa is spending money on fertilizer that the potato roots cannot physically absorb!\n\n### 3. Animal Housing & Biosecurity Failure\nExotic Friesian cows in high-altitude cold mud expend all their energy maintaining body heat, while bacteria in the mud infect their hooves (foot rot). Because manure is washed away by rain, none of it is returned to enrich the potato fields.\n\n### 4. Institutional Tenure Deadlock\nWithout a formalized title deed, Wekesa is locked out of commercial agribusiness credit facilities."
                        }
                    },
                    {
                        "type": "common_misconception",
                        "title": "Misconception: Adding More Fertilizer Cures Acid Soil Stunting",
                        "content": {
                            "misconception": "When crops look yellow and stunted in acidic soil, applying heavier doses of DAP fertilizer will fix the problem.",
                            "correction": "Adding more DAP fertilizer actually acidifies the soil further due to ammonium nitrification. Without applying agricultural lime to raise the pH above 6.0, up to 80% of added phosphorus fertilizer remains chemically locked and wasted.",
                            "why_it_matters": "Farmers waste thousands of shillings on fertilizer while their soils become increasingly toxic."
                        }
                    }
                ],
                [
                    {
                        "type": "step_process",
                        "title": "The 4-Step Farm Turnaround Masterplan",
                        "content": {
                            "title": "Wekesa's Integrated Rehabilitation Strategy",
                            "steps": [
                                "1. **Step 1: Topographical Physical Conservation**: Immediately halt downhill cultivation. Construct cross-slope contour stone terraces stabilized with dense **Napier grass and Desmodium strips** to reduce runoff velocity and trap silt.",
                                "2. **Step 2: Chemical Soil Amending**: Broadcast 2 tonnes of **agricultural lime (calcium carbonate)** across the 4 acres to neutralize soil acidity, raising pH from 4.8 to 6.2 and unlocking soil phosphorus reserves.",
                                "3. **Step 3: Farm Enterprise Rezoning**: Divide the 4 acres into 4 productive zones: **2 acres** for contour-planted potatoes with legume rotation; **1 acre** for agroforestry woodlot (*Grevillea*) and pasture; **0.5 acre** for intensive drip-irrigated vegetables; and **0.5 acre** for a modern zero-grazing dairy unit.",
                                "4. **Step 4: Zero-Grazing Unit & Nutrient Loop**: Build a raised, roofed zero-grazing unit using farm timber. Feed cows the terrace Napier grass; collect manure to generate biogas for cooking and compost for the potato fields.",
                                "5. **Step 5: Legal Land Succession**: Lodge succession papers with the Land Registry to secure a valid Freehold Title Deed in his name."
                            ]
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Wekesa's Farm Transformation: Before vs After",
                        "content": {
                            "title": "Wekesa's Farm Transformation: Before vs After",
                            "caption": "Comparative layout showing the transition from a degraded monoculture potato field with downhill erosion to an integrated, terraced, diversified farm with zero-grazing and agroforestry."
                        }
                    }
                ],
                [
                    {
                        "type": "comparison_table",
                        "title": "Projected Economic & Agronomic Outcomes",
                        "content": {
                            "title": "3-Year Turnaround Projection for Wekesa's Farm",
                            "headers": ["Performance Indicator", "Before Transformation (Year 0)", "After Transformation (Year 3)", "Agronomic Driver"],
                            "rows": [
                                ["Potato Yield", "25 bags / acre (100 bags total)", "85 bags / acre (170 bags from 2 acres)", "Lime unlocked soil phosphorus; contour terraces stopped topsoil erosion"],
                                ["Milk Production", "5 Liters / day (10 L total)", "22 Liters / day (44 L total)", "Clean, dry zero-grazing housing eliminated foot rot; high-protein Napier/Desmodium diet"],
                                ["Organic Soil Carbon", "1.1% (Depleted, eroded)", "3.8% (Rich, crumb structure)", "Continuous application of 15 tonnes of zero-grazing compost manure annually"],
                                ["Enterprise Diversity", "1 crop (High risk monoculture)", "4 cash streams (Potatoes, Milk, Vegetables, Timber)", "Multi-utility zoning eliminated price collapse vulnerability"],
                                ["Bank Credit Access", "Zero (Unregistered land)", "Eligible for 1,500,000 KES loan", "Obtained registered Freehold Title Deed in his name"]
                            ]
                        }
                    }
                ],
                [
                    {
                        "type": "mini_activity",
                        "title": "Group Activity: Critiquing Wekesa's Transformation Plan",
                        "content": {
                            "title": "Evaluating Farm Management Interventions",
                            "task": "In groups of four, review Wekesa's 4-step transformation plan:\n\n1. Explain why applying agricultural lime is an essential prerequisite before investing in expensive hybrid seed potatoes.\n2. Calculate how constructing contour Napier grass terraces directly solves the feeding bottleneck for the zero-grazing dairy unit.\n3. Identify the biological circular economy loop created between the dairy cows, the potato fields, and the vegetable garden.",
                            "materials": ["Case Study Handout", "Notebook", "Calculator"],
                            "safety": "Ensure active, collaborative participation by all team members."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Core Summary: Applied Agribusiness Diagnostics",
                        "content": {
                            "title": "Key Takeaways",
                            "text": "- **Downhill cultivation** destroys sloped farmland through rapid runoff and nutrient loss.\n- **Acid soils (pH < 5.0)** lock up phosphorus fertilizers; agricultural lime unlocks soil fertility.\n- **Integrated zoning** creates circular biological loops (manure feeds crops; crop residues feed livestock).\n- **Securing legal title deeds** is essential for accessing agricultural credit and modernizing infrastructure."
                        }
                    }
                ],
                [
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Diagnosing Smallholder Bottlenecks",
                        "content": {
                            "question": "What were the primary twin causes of the 70% decline in Wekesa's potato yields, and why did simply adding more chemical fertilizer fail to solve the problem?",
                            "options": [
                                "Nyandarua County's altitude is too low for potatoes, and dairy cows ate all the potato leaves",
                                "Downhill cultivation on a 12% slope accelerated severe topsoil and fertilizer erosion, while severe soil acidity (pH 4.8) chemically locked up phosphorus fertilizer, making it unabsorbable to roots until lime was applied",
                                "The potato seeds were planted upside down, and the farm received excessive direct equatorial sunlight",
                                "The grandfather's ghost cursed the soil because the land lacked a registered title deed"
                            ],
                            "answer": "B",
                            "explanation": "Wekesa suffered from a double failure: physical soil erosion from downhill furrows washing away topsoil and nutrients, compounded by edaphic chemical lockup (pH 4.8) where aluminum ions bind phosphorus into insoluble compounds. Adding more chemical fertilizer without physical contour terracing and chemical lime amendment only worsened the soil acidity while wasting money."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 10: Module Review, Performance Task & Summative Assessment
        # =====================================================================
        {
            "unit_order": 10,
            "unit_name": "Module Review and Performance Task",
            "unit_description": "Comprehensive synthesis of Topic 1 (Agricultural Land), performance task guidelines for creating a community Sustainable Land Guide Poster, video demonstration, and summative topic assessment MCQs.",
            "lesson_title": "Topic Synthesis, Performance Task, and Summative Assessment",
            "pages": [
                [
                    {
                        "type": "suggested_image",
                        "title": "Sustainable Land Stewardship and Agroforestry Landscape",
                        "content": {
                            "title": "Sustainable Land Stewardship and Agroforestry Landscape",
                            "caption": "A fully restored, resilient agricultural landscape integrating agroforestry tree belts, contour terraces, and diversified farming enterprises."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Topic Consolidation & Assessment",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Consolidate all core concepts of **Agricultural Land: Access, Utility, Natural Factors, and Sustainable Stewardship**.",
                                "Execute the **Topic 1 Performance Task**: Designing a visual 'Sustainable Land Guide Poster' for smallholder farmers.",
                                "Watch and reflect on an authentic documentary showcasing landscape restoration and soil conservation in Kenya.",
                                "Complete the comprehensive **Summative Topic Assessment** covering Sections A and B."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Consolidating Topic 1: The Master Principles of Land",
                        "content": {
                            "title": "The Four Golden Rules of Agricultural Land Management",
                            "text": "As we conclude our study of Agricultural Land, we synthesize four foundational truths:\n\n1. **Land is a finite, immobile, non-reproducible capital asset** that requires sustainable intensification.\n2. **Tenure security governs farmer stewardship**; long-term title enables multi-decade soil and infrastructure investments.\n3. **Natural factors (climate, altitude, soil, topography, biotics) set the biological boundaries**; matching enterprise utility to land parameters maximizes profit.\n4. **Restorative agronomic practices (terracing, liming, agroforestry, zero-grazing)** can turn degraded hillsides into flourishing agribusiness engines."
                        }
                    }
                ],
                [
                    {
                        "type": "comparison_table",
                        "title": "Comprehensive Topic 1 Concept Synthesis Matrix",
                        "content": {
                            "title": "Topic 1 Master Synthesis Matrix",
                            "headers": ["Curricular Dimension", "Core Principle", "Key Agronomic Parameters", "Best Management Practice"],
                            "rows": [
                                ["Land Access", "Tenure dictates time horizon & investment", "Leasing, Inheritance, Buying, Donation", "Secure formal title deeds; write conservation clauses into leases"],
                                ["Land Utility", "Align enterprise with land capacity", "Crops, Livestock, Agroforestry, Horticulture, Fish, Bees", "Zone clay basins for aquaculture, loam slopes for vegetables, rocky hills for bees"],
                                ["Climatic Factors", "Rainfall & thermal lapse rate govern biology", "Annual mm, distribution, -6.5°C/1000m altitude", "Select certified altitude-matched seeds; use drought-tolerant crops in ASALs"],
                                ["Soil & Topography", "Physics & chemistry dictate rooting & erosion", "pH (6.0–6.5), texture, slope %, catena drainage", "Apply agricultural lime to acid soils; build contour terraces on slopes >8%"],
                                ["Biotic Dynamics", "Harness symbiosis; manage threats", "*Rhizobium*, Mycorrhizae, Pollinators vs Pests", "Inoculate legumes; maintain flower borders for bees; rotate crops"]
                            ]
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "Performance Task Guidelines: Sustainable Land Guide Poster",
                        "content": {
                            "title": "Design Challenge: Educating Local Farmers",
                            "text": "To demonstrate your mastery of Grade 10 Agricultural Land management, you will create a visual communication tool:\n\n### Task Specifications\n- **Project Format**: A full-sized visual **'Sustainable Land Guide Poster'** on manila paper or digital slide presentation.\n- **Target Audience**: Smallholder farming families in your local community.\n- **Mandatory Visual Elements**:\n  1. *Contour Farming vs Downhill Farming Diagram*: Highlighting runoff deceleration and erosion prevention.\n  2. *Land Zoning Blueprint*: Showing proper placement of fish ponds in clay depressions, vegetables on gentle slopes, zero-grazing near the house, and beehives on rocky margins.\n  3. *Step-by-Step Soil Rescue Guide*: Explaining how to test soil pH and apply agricultural lime to unlock phosphorus fertilizer.\n  4. *Legal Land Guide*: A brief checklist on how to safely lease or legally transfer inherited land."
                        }
                    },
                    {
                        "type": "step_process",
                        "title": "Rubric Criteria for Performance Poster",
                        "content": {
                            "title": "Assessment Rubric for Performance Task",
                            "steps": [
                                "1. **Agronomic Accuracy (40%)**: All concepts (pH liming, contour terracing, slope zoning) are scientifically accurate and locally applicable.",
                                "2. **Visual Clarity & Design (30%)**: Clean diagrams, responsive labeling, bold key terms, and easy-to-read comparison charts.",
                                "3. **Community Relevance (20%)**: Addresses real-world local challenges (e.g. soil acidity, gully erosion, land subdivision).",
                                "4. **Presentation & Oral Defense (10%)**: Clear verbal communication explaining your poster to peers."
                            ]
                        }
                    }
                ],
                [
                    {
                        "type": "suggested_video",
                        "title": "Sustainable Land Management and Terracing in Kenya",
                        "content": {
                            "title": "Sustainable Land Management and Terracing in Kenya",
                            "description": "Examines authentic community-led landscape restoration, terracing, and water harvesting techniques across dry, degraded Kenyan hillsides.",
                            "url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
                        }
                    },
                    {
                        "type": "mini_activity",
                        "title": "Project Activity: Creating and Exhibiting Your Poster",
                        "content": {
                            "title": "Executing the Performance Task",
                            "task": "Work individually or in pairs to create your 'Sustainable Land Guide Poster' as outlined in the guidelines.\n\n- Use colored marker pens, rulers, and cut-out sample diagrams.\n- Mount your finished poster on the classroom exhibition wall.\n- Conduct a 3-minute oral pitch explaining how your poster will help a local farmer double their food production.",
                            "materials": ["Manila Paper / Digital Slide", "Marker Pens", "Ruler", "Adhesive Tape"],
                            "safety": "Use scissors and cutting tools with care during poster construction."
                        }
                    }
                ],
                [
                    {
                        "type": "knowledge_check",
                        "title": "Summative MCQ 1: Land as an Economic Production Factor",
                        "content": {
                            "question": "Which of the following statements correctly explains why agricultural land is classified as an economically unique factor of production compared to capital machinery?",
                            "options": [
                                "Land depreciates rapidly within 5 years and must be replaced in a factory",
                                "Land is geographically mobile and its supply can be expanded through industrial manufacturing",
                                "Land is completely immobile, non-reproducible in physical supply, and when managed with soil conservation, it does not suffer mechanical depreciation",
                                "Land requires zero capital or labor investment to generate commercial profits"
                            ],
                            "answer": "C",
                            "explanation": "Unlike manufactured capital assets which depreciate, wear out, and can be produced in factories, physical land is spatially fixed (immobile), non-reproducible in supply, and maintains or increases its fertility and economic value indefinitely when managed sustainably."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Summative MCQ 2: Carrying Capacity and Pasture Degradation",
                        "content": {
                            "question": "What happens when a livestock farmer continuously exceeds the carrying capacity of an open communal grazing pasture?",
                            "options": [
                                "The grass roots grow deeper and increase soil fertility automatically",
                                "Overgrazing strips vegetative ground cover and heavy livestock hooves compact soil pores, destroying water infiltration and triggering severe runoff and gully erosion",
                                "The cattle produce double the milk yield due to competitive feeding behavior",
                                "The pasture soil turns into heavy clay suitable for commercial fish farming"
                            ],
                            "answer": "B",
                            "explanation": "Exceeding carrying capacity (overstocking) causes livestock to consume grass down to root crowns, destroying the protective canopy. Concurrently, animal hoof pressure seals soil macro-pores, preventing rainfall infiltration and causing rapid surface runoff, sheet wash, and catastrophic gully erosion."
                        }
                    }
                ],
                [
                    {
                        "type": "knowledge_check",
                        "title": "Summative MCQ 3: Altitude Lapse Rate and Crop Distribution",
                        "content": {
                            "question": "As an agricultural extension officer travels from a lowland coastal farm at sea level (0 m, mean temp 30°C) up to a highland tea zone at 2,000 m elevation, what approximate mean temperature change should they expect, and which crop transition will occur?",
                            "options": [
                                "Temperature increases by 13°C; transition from tea to cotton",
                                "Temperature drops by approx. 13°C (to ~17°C); transition from heat-tolerant coastal crops (coconuts, cashew nuts) to cool-climate highland crops (tea, pyrethrum, Irish potatoes)",
                                "Temperature remains identical because both zones are near the equator",
                                "Temperature drops by 30°C to below freezing, making all crop cultivation impossible"
                            ],
                            "answer": "B",
                            "explanation": "Based on the environmental lapse rate of approx. 6.5°C per 1,000 m elevation gain, ascending 2,000 m causes a temperature drop of approx. 13.0°C ($2 \\times 6.5^\\circ\\text{C}$). The climate transitions from hot coastal conditions (~30°C) suitable for coconuts and cashews to cool highland conditions (~17°C) ideal for tea, pyrethrum, and dairy."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Summative MCQ 4: Managing Severe Soil Acidity",
                        "content": {
                            "question": "A soil chemical assay reveals a pH of 4.5. Why does applying Diammonium Phosphate (DAP) fertilizer fail to improve stunted maize crops, and what is the mandatory soil reclamation step?",
                            "options": [
                                "At pH 4.5, soluble aluminum chemically locks up phosphorus into insoluble compounds; the farmer must apply agricultural lime (calcium carbonate) to raise pH above 6.0 before fertilizer can be absorbed",
                                "The soil contains too much calcium; the farmer must apply sulfuric acid to neutralize it",
                                "The maize crops are stunted due to shade; the farmer must install artificial electric floodlights",
                                "At pH 4.5, earthworms consume all nitrogen; the farmer must spray strong synthetic insecticides"
                            ],
                            "answer": "A",
                            "explanation": "Severe soil acidity (pH < 5.0) mobilizes toxic Aluminum and Iron ions that chemically bond with Phosphorus from fertilizers, forming insoluble precipitates that plant roots cannot absorb. Applying agricultural lime neutralizes acidity, raising pH to the optimal 6.0–6.5 range and unlocking phosphorus for crop uptake."
                        }
                    }
                ],
                [
                    {
                        "type": "knowledge_check",
                        "title": "Summative MCQ 5: Enterprise Selection for Waterlogged Clay Basins",
                        "content": {
                            "question": "A farm layout audit identifies a 2-acre low-lying valley depression composed of heavy clay soil that remains waterlogged for 5 months each year. Which enterprise represents the most viable and profitable use of this specific zone?",
                            "options": [
                                "Commercial avocado and citrus tree orchard",
                                "Earthen tilapia and catfish aquaculture fish ponds, combined with wetland arrowroot (*nduma*) borders",
                                "Extensive dryland finger millet and sorghum cultivation",
                                "Deep underground silage pit storage and dry sheep housing"
                            ],
                            "answer": "B",
                            "explanation": "Heavy clay soils in low-lying depressions have minimal percolation rates and naturally hold water, making them disastrous for avocados, citrus, or dryland grains (causes lethal root rot). However, these exact water-retention properties make clay basins the gold standard for earthen aquaculture fish ponds and moisture-tolerant arrowroots."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Summative MCQ 6: Diagnosing Downhill Cultivation Hazards",
                        "content": {
                            "question": "Why is cultivating crop rows straight downhill on a 15% slope considered a catastrophic agricultural practice on smallholder farms?",
                            "options": [
                                "Downhill rows cause rainwater to flow too slowly, leading to waterlogging on the hillside",
                                "Downhill furrows act as accelerated drainage channels, converting gentle runoff into high-velocity torrents that wash away fertile topsoil, seeds, and fertilizers, creating deep destructive gullies",
                                "Downhill crops receive too much morning sunlight and ripen prematurely",
                                "Downhill cultivation prevents bees from locating crop flowers"
                            ],
                            "answer": "B",
                            "explanation": "Cultivating straight downhill provides unobstructed channels for rainfall runoff. As water flows down the slope, its velocity and kinetic energy multiply ($E = \\frac{1}{2}mv^2$), transforming gentle surface runoff into violent streams that scour topsoil, wash away seeds and fertilizers, and carve deep gullies."
                        }
                    }
                ],
                [
                    {
                        "type": "knowledge_check",
                        "title": "Summative MCQ 7: Long-Term Tenure Security and Soil Conservation",
                        "content": {
                            "question": "How does holding a secure, registered Freehold Title Deed directly motivate a farmer to invest in permanent stone terraces, agroforestry, and zero-grazing units?",
                            "options": [
                                "The government legally confiscates any titled land that does not possess stone terraces within 6 months",
                                "The title deed provides legal certainty that the farmer and their heirs will reap the multi-year economic benefits of improved soil fertility, while serving as collateral to secure bank development loans",
                                "Title deeds automatically reduce the cost of purchasing tractor machinery by 90%",
                                "Freehold titles exempt farmers from paying for commercial seeds and fertilizers"
                            ],
                            "answer": "B",
                            "explanation": "Long-term tenure security (Freehold Title Deed) gives the farmer confidence that their substantial capital and labor investments in soil conservation, terracing, and agroforestry will yield compounding financial returns over decades without risk of sudden landlord eviction, while unlocking commercial bank credit."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Summative MCQ 8: Designing a Circular Agribusiness Loop",
                        "content": {
                            "question": "In Wekesa's rehabilitated 4-acre farm masterplan, how does integrating a zero-grazing dairy unit directly support his commercial potato fields and vegetable garden?",
                            "options": [
                                "The dairy cows walk through the potato fields daily to trample weeds",
                                "The cows consume terrace Napier grass and fodder, and their dung and urine are composted into nutrient-rich organic manure that restores soil crumb structure and fertility in the potato and vegetable plots",
                                "The dairy shed produces milk that is sprayed directly on potato leaves as an insecticide",
                                "The cows produce sound vibrations that frighten destructive crop-eating birds away"
                            ],
                            "answer": "B",
                            "explanation": "A zero-grazing dairy unit closes the biological loop on a smallholder farm: terrace vegetation (Napier grass and Desmodium) provides high-protein livestock feed, while cattle manure and slurry are composted to return vital organic matter, Nitrogen, Potassium, and beneficial microbes back to the crop soils, reducing reliance on synthetic fertilizers."
                        }
                    }
                ],
                [
                    {
                        "type": "summary",
                        "title": "Topic 1 Capstone Summary: Agricultural Land Mastery",
                        "content": {
                            "title": "Mastery Overview: Grade 10 Agricultural Land",
                            "text": "Congratulations on completing **Topic 1: Agricultural Land**!\n\nYou have mastered the core principles of:\n- **Land Access**: Choosing between leasing, inheritance, purchase, and donation based on capital and tenure security.\n- **Land Utilities**: Matching land characteristics to broad-acre crops, livestock, agroforestry, horticulture, aquaculture, and apiculture.\n- **Natural Determinants**: Navigating rainfall regimes, thermal lapse rates, soil pH (6.0–6.5), slope gradients, and soil biology.\n- **Community Stewardship**: Conducting transect walks, protecting riparian buffers, and arresting gully erosion.\n- **Applied Diagnostics**: Turning around degraded farms through contour terracing, agricultural liming, integrated multi-utility zoning, and legal title registration."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Topic 1 Final Takeaway",
                        "content": {
                            "title": "The Agronomist's Credo",
                            "text": "Sustainable agricultural prosperity begins with understanding the land. Protect the soil, respect the natural slope, match the crop to the climate, and manage the land as a sacred trust for generations to come."
                        }
                    }
                ]
            ]
        }
    ]

@transaction.atomic
def ingest_grade10_topic1(replace=False):
    """Executes the complete production ingestion of Grade 10 Agriculture Topic 1."""
    print("=" * 80)
    print("STARTING INGESTION: CBC Grade 10 Agriculture — Topic 1: Agricultural Land")
    print("=" * 80)

    # 1. Resolve Curriculum
    curriculum = Curriculum.objects.filter(name__iexact="CBC").first()
    if not curriculum:
        curriculum = Curriculum.objects.create(name="CBC", description="Competency Based Curriculum")
        print(f"Created Curriculum: {curriculum.name} (ID: {curriculum.id})")
    else:
        print(f"Resolved Curriculum: {curriculum.name} (ID: {curriculum.id})")

    # 2. Resolve Grade 10
    grade = Grade.objects.filter(curriculum=curriculum, name__icontains="10").first()
    if not grade:
        grade = Grade.objects.create(curriculum=curriculum, name="Grade 10", level=10, description="Senior Secondary 1")
        print(f"Created Grade: {grade.name} (ID: {grade.id})")
    else:
        print(f"Resolved Grade: {grade.name} (ID: {grade.id}, Level: {grade.level})")

    # 3. Resolve Subject: Agriculture
    subject = Subject.objects.filter(grade=grade, name__iexact="Agriculture").first()
    if not subject:
        subject = Subject.objects.create(
            grade=grade,
            name="Agriculture",
            description="Grade 10 Applied Agriculture for Senior Secondary CBC"
        )
        print(f"Created Subject: {subject.name} (ID: {subject.id}) under {grade.name}")
    else:
        print(f"Resolved Subject: {subject.name} (ID: {subject.id}) under {grade.name}")

    # 4. Resolve Topic: Agricultural Land
    topic_name = "Agricultural Land"
    topic = Topic.objects.filter(subject=subject, name=topic_name).first()
    if not topic:
        topic = Topic.objects.create(
            subject=subject,
            name=topic_name,
            description="Understanding agricultural land access, utilities, natural productivity factors, community stewardship, and farm zoning.",
            order=1
        )
        print(f"Created Topic 1: {topic.name} (ID: {topic.id})")
    else:
        topic.order = 1
        topic.description = "Understanding agricultural land access, utilities, natural productivity factors, community stewardship, and farm zoning."
        topic.save()
        print(f"Resolved Topic 1: {topic.name} (ID: {topic.id})")

    if replace:
        print("Flag --replace active: Clearing existing LearningUnits and Lessons for Topic 1...")
        topic.learning_units.all().delete()
        topic.lessons.all().delete()

    curriculum_data = build_topic1_curriculum()
    total_units_created = 0
    total_lessons_created = 0
    total_pages_created = 0
    total_blocks_created = 0

    for item in curriculum_data:
        u_order = item["unit_order"]
        u_name = item["unit_name"]
        u_desc = item["unit_description"]
        l_title = item["lesson_title"]
        pages = item["pages"]

        # Resolve or create LearningUnit
        unit, u_created = LearningUnit.objects.get_or_create(
            topic=topic,
            order=u_order,
            defaults={"name": u_name, "description": u_desc}
        )
        if not u_created:
            unit.name = u_name
            unit.description = u_desc
            unit.save()
        total_units_created += 1

        # Resolve or create published Lesson
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
                    "topic_order": 1,
                    "unit_order": u_order
                }
            }
        )
        if not l_created:
            lesson.title = l_title
            lesson.status = "published"
            lesson.version = 1
            lesson.save()

        # Delete existing blocks for this lesson to ensure clean idempotency
        lesson.blocks.all().delete()
        total_lessons_created += 1

        # Ingest Pages and Blocks
        block_order_counter = 1
        for page_idx, page_blocks in enumerate(pages, start=1):
            total_pages_created += 1
            for comp_idx, block_def in enumerate(page_blocks, start=1):
                b_type = block_def["type"]
                b_title = clean_text(block_def.get("title", ""))
                b_content = clean_dict(block_def.get("content", {}))

                LessonBlock.objects.create(
                    lesson=lesson,
                    block_id=f"g10_agri_t1_u{u_order}_p{page_idx}_b{comp_idx}",
                    block_type=b_type,
                    component_type=b_type,
                    title=b_title,
                    content=b_content,
                    order=block_order_counter,
                    page_number=page_idx,
                    component_order=comp_idx,
                    page_title=b_title if comp_idx == 1 else None,
                    metadata={"topic_order": 1, "unit_order": u_order, "page": page_idx}
                )
                block_order_counter += 1
                total_blocks_created += 1

        print(f"  Ingested Unit {u_order}: {u_name} -> Lesson '{l_title}' ({len(pages)} Pages, {block_order_counter - 1} Blocks)")

    print("=" * 80)
    print(f"INGESTION COMPLETE: Topic 1 '{topic.name}'")
    print(f"  Total Units: {total_units_created}")
    print(f"  Total Lessons: {total_lessons_created}")
    print(f"  Total Pages: {total_pages_created}")
    print(f"  Total Blocks: {total_blocks_created}")
    print("=" * 80)

if __name__ == "__main__":
    replace_flag = "--replace" in sys.argv
    ingest_grade10_topic1(replace=replace_flag)