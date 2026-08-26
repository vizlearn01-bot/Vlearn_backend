"""
VLearn CBC Grade 10 Agriculture — Topic 2: Properties of Soil
Production Ingestion Engine (Deep Senior Secondary Pedagogical Edition)

Curriculum: CBC (ID: 5)
Grade: Grade 10 (ID: 5, Level: 10)
Subject: Agriculture
Topic: Properties of Soil (Topic Order: 2)

Decomposed into 12 Learning Units & 12 Published Lessons:
  1. Soil Texture (7 Pages, 13 Blocks)
  2. Soil Structure (7 Pages, 13 Blocks)
  3. Soil Porosity and Density (7 Pages, 13 Blocks)
  4. Soil Color (7 Pages, 13 Blocks)
  5. Soil Sampling and Investigation (7 Pages, 14 Blocks)
  6. Soil pH (7 Pages, 14 Blocks)
  7. Cation Exchange Capacity (7 Pages, 13 Blocks)
  8. Soil Salinity (7 Pages, 14 Blocks)
  9. Organic Matter and Humus (7 Pages, 13 Blocks)
  10. Soil Organisms (7 Pages, 14 Blocks)
  11. Soil Profile and Crop Production (7 Pages, 14 Blocks)
  12. Importance and Synthesis of Soil Properties (9 Pages, 20 Blocks)
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

def build_topic2_curriculum():
    """Returns the comprehensive pedagogical page and block structure for Grade 10 Topic 2: Properties of Soil."""
    return [
        # =====================================================================
        # LESSON 1: Soil Texture
        # =====================================================================
        {
            "unit_order": 1,
            "unit_name": "Soil Texture",
            "unit_description": "Definition of soil texture as relative mineral proportions, USDA particle size boundaries (sand, silt, clay), textural classes, the USDA triangle, and field feel tests.",
            "lesson_title": "Soil Texture and Textural Classes",
            "pages": [
                [
                    {
                        "type": "suggested_image",
                        "title": "Soil Texture Samples: Sand, Silt, and Clay",
                        "content": {
                            "title": "Soil Texture Samples: Sand, Silt, and Clay",
                            "caption": "Comparative laboratory samples of sandy loam, silt loam, and heavy clay soil illustrating the physical differences in grain size and cohesion."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Soil Texture",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Define **soil texture** as the relative percentage of sand, silt, and clay mineral particles.",
                                "State the exact **USDA particle size diameters** for sand ($0.05\\text{--}2.0\\text{ mm}$), silt ($0.002\\text{--}0.05\\text{ mm}$), and clay ($<0.002\\text{ mm}$).",
                                "Interpret the **USDA Soil Textural Triangle** to classify soil samples into textural categories.",
                                "Perform a practical **soil texture ribbon test** by feel."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "What is Soil Texture?",
                        "content": {
                            "title": "The Permanent Mineral Fabric of Soil",
                            "text": "**Soil texture** refers to the relative proportions of different-sized inorganic mineral particles (**sand, silt, and clay**) in a soil sample. These particles originate from the slow physical disintegration and chemical weathering of parent rocks over thousands of years.\n\n- **A Permanent Physical Property**: Unlike soil fertility, organic matter, or soil structure which farmers can alter seasonally, soil texture is a **permanent property**. A farmer cannot easily change the textural class of an open 5-acre field without hauling thousands of tonnes of sand or clay."
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "Mineral Particle Size Classification (USDA)",
                        "content": {
                            "title": "The Three Fundamental Soil Separates",
                            "text": "The United States Department of Agriculture (USDA) establishes strict size boundaries for soil mineral separates:\n\n### 1. Sand ($0.05\\text{ mm}$ to $2.0\\text{ mm}$)\n- The largest soil particles, visible to the naked eye.\n- Individual grains feel rough, hard, and distinctly gritty between the fingers.\n- Creates large macro-pores that provide rapid drainage and high aeration, but has virtually zero capacity to hold water or nutrients.\n\n### 2. Silt ($0.002\\text{ mm}$ to $0.05\\text{ mm}$)\n- Medium-sized particles, invisible without a light microscope.\n- Feels smooth, silky, and floury like talcum powder when dry, and creamy (non-sticky) when wet.\n- Holds moderate water and erodes easily when bare.\n\n### 3. Clay ($< 0.002\\text{ mm}$)\n- The smallest microscopic and colloidal particles.\n- Highly plastic, sticky, and moldable when wet, drying into rock-hard clods that crack under sun exposure.\n- Holds immense amounts of water and dissolved nutrients on its negatively charged surfaces."
                        }
                    },
                    {
                        "type": "definition_card",
                        "title": "Key Term: Soil Separates",
                        "content": {
                            "term": "Soil Separates",
                            "definition": "The individual mineral particle size groups into which soil inorganic material is divided: Sand (0.05–2.0 mm), Silt (0.002–0.05 mm), and Clay (< 0.002 mm).",
                            "example": "A laboratory mechanical sieve test separating sand grains from silt and colloidal clay suspensions."
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "Textural Classes and the USDA Triangle",
                        "content": {
                            "title": "Categorizing Soils for Agribusiness Suitability",
                            "text": "Based on the exact percentages of sand, silt, and clay, agricultural soils are grouped into **textural classes**:\n\n- **Sandy Soils (>70% Sand)**: Coarse and gritty. Drains immediately, highly aerated, but prone to rapid drought and fertilizer leaching.\n- **Clayey Soils (>40% Clay)**: Heavy and dense. Retains huge water volumes and nutrients, but prone to chronic waterlogging, poor aeration, and requires high tractor draft power.\n- **Loamy Soils (Balanced Mix)**: Typically 40% sand, 40% silt, and 20% clay. The **gold standard for commercial agriculture**, offering ideal moisture retention, rapid drainage of excess water, high nutrient holding, and effortless tillage.\n- **The USDA Textural Triangle**: A 3-axis triangular coordinate chart used by agronomists to determine the exact textural class name from laboratory sieve data."
                        }
                    },
                    {
                        "type": "comparison_table",
                        "title": "Comparative Agronomic Profiles of Soil Textures",
                        "content": {
                            "title": "Textural Class Comparison Matrix",
                            "headers": ["Agronomic Factor", "Sandy Soil", "Loam Soil (Optimal)", "Heavy Clay Soil"],
                            "rows": [
                                ["Water Infiltration", "Very Fast (>50 mm/hr)", "Moderate (15–25 mm/hr)", "Extremely Slow (<5 mm/hr)"],
                                ["Available Water Capacity", "Poor (Drought prone)", "Excellent (Capillary storage)", "High total (Water held too tightly)"],
                                ["Nutrient Retention", "Very Low (High leaching)", "High (Balanced organic & clay)", "Extremely High (Strong adsorption)"],
                                ["Tillage & Workability", "Very Easy (Light soil)", "Easy (Crumbly friability)", "Very Difficult (Sticky when wet, hard when dry)"],
                                ["Best Crop Matches", "Groundnuts, Cassava, Watermelons", "Maize, Beans, Vegetables, Coffee", "Paddy Rice, Aquaculture Fish Ponds"]
                            ]
                        }
                    }
                ],
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Simplified USDA Soil Textural Triangle",
                        "content": {
                            "title": "Simplified USDA Soil Textural Triangle",
                            "caption": "Triangular coordinate chart displaying the 12 textural classes with Clay at the apex, Sand at the bottom-left, Silt at the bottom-right, and Loam in the fertile center."
                        }
                    },
                    {
                        "type": "step_process",
                        "title": "Step-by-Step Protocol: Soil Texture Feel Test",
                        "content": {
                            "title": "Field Identification of Soil Texture by Ribbon Test",
                            "steps": [
                                "1. **Moisten Sample**: Take a palm-sized sample of soil, remove gravel, and add water drop by drop until moist like putty.",
                                "2. **Knead and Roll**: Squeeze the soil into a ball. If it fails to form a ball and falls apart, it is **Coarse Sand**.",
                                "3. **Form a Ribbon**: Push the soil ball out between your thumb and forefinger to form a continuous ribbon of uniform thickness (approx. 2 mm).",
                                "4. **Measure Ribbon Length**: \n   - *Breaks before 2.5 cm*: Sandy Loam or Silt Loam.\n   - *Forms a 2.5 to 5.0 cm ribbon*: Clay Loam.\n   - *Forms a flexible ribbon > 5.0 cm that bends into a ring*: Heavy Clay.",
                                "5. **Evaluate Grittiness vs Smoothness**: Rub a pinch of wet soil in your palm. Gritty = Sand dominance; Silky/soapy = Silt dominance; Sticky = Clay dominance."
                            ]
                        }
                    }
                ],
                [
                    {
                        "type": "mini_activity",
                        "title": "Practical Lab: Soil Texture Feel Test",
                        "content": {
                            "title": "Executing the Ribbon Test on School Soils",
                            "task": "Collect three soil samples from distinct zones on the school compound (e.g. flower bed, football pitch pathway, riverbank):\n\n1. Perform the 5-step ribbon test on each sample.\n2. Record ribbon length in millimeters and describe feel (gritty, soapy, or sticky).\n3. Match each sample to its corresponding textural class on the USDA triangle.",
                            "materials": ["3 Soil Samples", "Water Dropper", "Ruler", "White Paper Trays"],
                            "safety": "Wash hands with clean water and soap after completing soil handling."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Core Summary: Soil Texture",
                        "content": {
                            "title": "Key Takeaways",
                            "text": "- **Soil texture** is the permanent relative proportion of sand, silt, and clay.\n- **Sand (0.05–2.0mm)** provides drainage; **Silt (0.002–0.05mm)** feels silky; **Clay (<0.002mm)** provides nutrient retention.\n- **Loams** combine the drainage of sand with the fertility of clay, creating ideal conditions for crops.\n- **Ribbon tests** allow rapid field diagnosis of soil textural classes."
                        }
                    }
                ],
                [
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Matching Texture to Horticultural Crops",
                        "content": {
                            "question": "A farmer in Trans Nzoia is selecting a field to grow commercial French beans, which require high root aeration, moderate constant moisture, and easy root expansion. If laboratory sieve tests reveal the following four parcels, which parcel should the farmer select?",
                            "options": [
                                "Field A: 85% Sand, 10% Silt, 5% Clay",
                                "Field B: 35% Sand, 40% Silt, 25% Clay (Loam / Clay Loam)",
                                "Field C: 15% Sand, 15% Silt, 70% Clay (Heavy Clay)",
                                "Field D: 95% Coarse Gravel with zero fine earth"
                            ],
                            "answer": "B",
                            "explanation": "Field B (Loam/Clay Loam) provides the optimal agricultural balance: 35% sand guarantees good macro-pore drainage and root aeration, while 25% clay and 40% silt supply high cation nutrient retention and capillary water holding. Field A drains too quickly and leaches fertilizer, Field C waterlogs and suffocates delicate bean roots, and Field D cannot hold water or anchor roots."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 2: Soil Structure
        # =====================================================================
        {
            "unit_order": 2,
            "unit_name": "Soil Structure",
            "unit_description": "Definition of soil structure as spatial arrangement of aggregates (peds), structural classifications (granular, crumbly, blocky, platy, prismatic, columnar), and agricultural impacts on aeration and drainage.",
            "lesson_title": "Soil Structure and Aggregate Dynamics",
            "pages": [
                [
                    {
                        "type": "suggested_image",
                        "title": "Soil Aggregates and Crumb Structure",
                        "content": {
                            "title": "Soil Aggregates and Crumb Structure",
                            "caption": "Close-up macroscopic view of fertile crumbly soil aggregates held together by plant roots, microbial glues, and fungal hyphae."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Soil Structure",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Define **soil structure** as the arrangement and binding of soil particles into stable **aggregates (peds)**.",
                                "Identify the six major types of soil structure: **granular, crumbly, blocky, platy, prismatic, and columnar**.",
                                "Explain why **crumbly structure** is the optimal physical condition for crop growth.",
                                "Evaluate management practices that build or destroy structural stability."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Understanding Soil Structure vs Texture",
                        "content": {
                            "title": "The Dynamic Architecture of Soil",
                            "text": "While **texture** tells us *what* particles are present (sand, silt, clay), **soil structure** describes *how* those individual particles are clumped and cemented together into distinct clusters called **aggregates** or **peds**.\n\n- **A Dynamic Property**: Unlike texture, soil structure is highly responsive to human management. A farmer can improve structure within seasons by adding organic compost, or ruin it within hours by plowing wet soil or driving heavy tractors across the field."
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "Six Primary Types of Soil Structure",
                        "content": {
                            "title": "Morphological Classification of Soil Peds",
                            "text": "Soil aggregates form six distinct structural geometries:\n\n### 1. Crumbly (Ideal Agricultural Structure)\n- Small, highly porous, rounded aggregates bound loosely together.\n- Creates an optimal 50:50 balance between solid particles and pore channels, allowing roots to breathe and absorb capillary water with minimal physical resistance.\n\n### 2. Granular\n- Small, rounded, non-porous peds lying loosely in topsoils; common in cultivated garden soils.\n\n### 3. Blocky (Angular & Sub-angular)\n- Cube-like aggregates with sharp or rounded edges ($1.5\\text{--}5.0\\text{ cm}$). Common in B-horizon subsoils; provides moderate drainage along vertical cracks.\n\n### 4. Platy (Compacted & Undesirable)\n- Thin, flat, horizontal plates stacked on top of one another. Forms 'plow pans' or surface crusts that block downward water infiltration and deflect root growth horizontally.\n\n### 5. Prismatic & Columnar\n- Vertically oriented, pillar-like columns found in dense subsoils. Columnar peds feature rounded, salt-capped tops typical of high-sodium saline soils."
                        }
                    },
                    {
                        "type": "comparison_table",
                        "title": "Soil Structure Types and Agronomic Suitability",
                        "content": {
                            "title": "Structural Types Comparison Matrix",
                            "headers": ["Structure Type", "Ped Geometry", "Porosity & Aeration", "Root Penetration", "Agricultural Suitability"],
                            "rows": [
                                ["Crumbly", "Small rounded, highly porous crumbs", "Optimal balance of macro & micro pores", "Effortless deep root penetration", "Superior (Best for all crops)"],
                                ["Granular", "Small rounded, dense grains", "Good aeration in topsoil", "Easy seedling emergence", "Good"],
                                ["Blocky", "Cube-like angular or rounded blocks", "Moderate drainage via ped cracks", "Roots grow along aggregate faces", "Fair (Common in subsoils)"],
                                ["Platy", "Flat horizontal overlapping plates", "Severely blocked vertical flow", "Roots deflected horizontally", "Very Poor (Plow pan barrier)"],
                                ["Columnar", "Tall vertical pillars with rounded tops", "Low aeration; high sodium dispersion", "Restricted root volume", "Poor (Saline sodic soils)"]
                            ]
                        }
                    }
                ],
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Types of Soil Structure Aggregates",
                        "content": {
                            "title": "Types of Soil Structure Aggregates",
                            "caption": "Morphological diagram illustrating Crumbly (porous rounded), Granular (dense rounded), Blocky (angular cubes), Platy (horizontal plates), and Prismatic (vertical columns) peds."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "How Soil Structure Governs Crop Productivity",
                        "content": {
                            "title": "The Agricultural Power of Crumb Aggregates",
                            "text": "A well-developed crumb structure enhances four vital agronomic functions:\n\n1. **Root Respiration**: Continuous macro-pore channels exchange oxygen ($O_2$) and carbon dioxide ($CO_2$) between the atmosphere and root cells.\n2. **Rapid Infiltration**: Water enters aggregates smoothly, preventing surface ponding, sheet runoff, and soil erosion.\n3. **Soil Moisture Retention**: Micro-pores inside the aggregates hold capillary water against gravity for crops during dry spells.\n4. **Erosion Resistance**: Large crumb aggregates are too heavy to be blown away by wind or dislodged by moderate raindrop impacts."
                        }
                    }
                ],
                [
                    {
                        "type": "step_process",
                        "title": "Techniques for Building and Preserving Soil Structure",
                        "content": {
                            "title": "Farmer's Guide to Structural Regeneration",
                            "steps": [
                                "1. **Incorporate Organic Compost & Manure**: Humic glues from decomposed organic matter cement mineral particles into durable water-stable crumbs.",
                                "2. **Practice Minimum Tillage (Conservation Tillage)**: Eliminate excessive disc plowing that shatters structural aggregates into fine dust.",
                                "3. **Maintain Continuous Mulch & Cover Crops**: Plant roots bind aggregates physically, while root exudates and mycorrhizal fungi secrete glomalin to glue peds.",
                                "4. **Never Cultivate Saturated Clay Soils**: Tilling wet soil smears clay particles, creating impervious, cemented platy clods when dry."
                            ]
                        }
                    },
                    {
                        "type": "callout",
                        "title": "Agronomic Fact: Glomalin - The Soil Glue",
                        "content": {
                            "title": "Mycorrhizal Fungi Produce Natural Concrete",
                            "text": "Beneficial mycorrhizal fungi living in symbiotic association with crop roots produce a sticky glycoprotein called **glomalin**. Glomalin coats soil particles, binding them into water-stable crumb aggregates that resist breakdown during heavy rainstorms!"
                        }
                    }
                ],
                [
                    {
                        "type": "mini_activity",
                        "title": "Field Observation: Aggregate Stability Slake Test",
                        "content": {
                            "title": "Observing Soil Aggregate Water Stability",
                            "task": "1. Collect two dry golf-ball-sized soil clumps: one from an undisturbed organic forest/grassland, and one from a continuously plowed, bare path.\n2. Submerge both clumps simultaneously in separate glass jars filled with water on a wire mesh.\n3. Observe: The forest clump maintains its crumb structure, while the path clump dissolves and collapses into mud within seconds, demonstrating loss of organic binding glues.",
                            "materials": ["2 Glass Jars", "Wire Mesh / Screen", "2 Dry Soil Clumps", "Water"],
                            "safety": "Handle glass jars carefully to prevent breakage."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Core Summary: Soil Structure",
                        "content": {
                            "title": "Key Takeaways",
                            "text": "- **Soil structure** is the spatial arrangement of soil particles into aggregates (peds).\n- **Crumbly structure** is the ideal agricultural state, providing high internal porosity and deep root penetration.\n- **Platy structure** creates compacted barriers that cause waterlogging and root deflection.\n- **Organic matter and minimum tillage** are essential for maintaining water-stable aggregates."
                        }
                    }
                ],
                [
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Structural Diagnosis in Maize Farming",
                        "content": {
                            "question": "A farmer in Uasin Gishu notices that after multiple years of intensive mechanized disc plowing, rainwater no longer soaks into the soil and maize roots are growing sideways at a depth of 15 cm. What structural defect has formed, and what is the proper management remedy?",
                            "options": [
                                "The soil has developed a crumbly structure; the farmer should spray synthetic insecticides",
                                "A compacted platy 'plow pan' structure has formed from heavy machinery; the farmer should use a subsoiler (ripper) to shatter the pan, incorporate organic compost, and adopt minimum tillage",
                                "The soil particles have turned into sand; the farmer should haul clay from a riverbed",
                                "The soil has become too porous; the farmer should roll heavy steamrollers across the field"
                            ],
                            "answer": "B",
                            "explanation": "Repeated tractor plowing at the same depth compresses soil particles into horizontal, dense platy layers known as a 'plow pan'. This hardpan blocks vertical water infiltration (causing surface runoff) and physically forces crop roots to deflect sideways. Shattering the hardpan with a deep subsoiler and adding organic compost restores vertical macro-pore channels and crumb aggregate structure."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 3: Soil Porosity and Density
        # =====================================================================
        {
            "unit_order": 3,
            "unit_name": "Soil Porosity and Density",
            "unit_description": "Macro-pores vs micro-pores, particle density ($2.65\\text{ g/cm}^3$) vs bulk density ($1.0\\text{--}1.6+\\text{ g/cm}^3$), soil compaction mechanics, and bulk density agronomic thresholds.",
            "lesson_title": "Soil Porosity, Density, and Compaction Dynamics",
            "pages": [
                [
                    {
                        "type": "suggested_image",
                        "title": "Agricultural Soil Health and Pore Space Dynamics",
                        "content": {
                            "title": "Agricultural Soil Health and Pore Space Dynamics",
                            "caption": "A thriving crop field with loose, porous topsoil showing the visual difference between well-aerated root zones and compacted tractor wheel ruts."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Porosity and Density",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Define **soil porosity** and differentiate between **macro-pores** (drainage/aeration) and **micro-pores** (water storage).",
                                "Distinguish between **particle density** (constant $\\approx 2.65\\text{ g/cm}^3$) and **bulk density** ($1.0\\text{--}1.6+\\text{ g/cm}^3$).",
                                "Calculate soil porosity using bulk and particle density values.",
                                "Analyze the physiological hazards of **soil compaction** and high bulk density on crop root development."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "What is Soil Porosity?",
                        "content": {
                            "title": "The Living Air and Water Channels of Soil",
                            "text": "**Soil porosity** represents the percentage of total soil volume that is not occupied by solid mineral or organic particles, but consists of open voids (pore spaces) filled with air and water.\n\n- **The Ideal 50:50 Soil Matrix**: In a healthy, well-structured agricultural loam, **50% of the volume is solid matter** (45% mineral + 5% organic matter) and **50% is pore space** (ideally 25% air + 25% water at field capacity)."
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "Macro-Pores vs Micro-Pores",
                        "content": {
                            "title": "Capillary Water Retention vs Gravitational Drainage",
                            "text": "Pore spaces are functionally divided into two categories by diameter:\n\n### 1. Macro-Pores (Large Pores, $>0.08\\text{ mm}$)\n- Highly abundant in sandy soils and well-aggregated crumb soils.\n- Allow rapid gravitational water drainage after rains and facilitate unhindered atmospheric gas exchange ($O_2$ in, $CO_2$ out).\n- *Limitation*: Cannot hold water against gravity; water drains away rapidly.\n\n### 2. Micro-Pores (Capillary Pores, $<0.08\\text{ mm}$)\n- Highly abundant in clayey soils and decomposed humus.\n- Act as tiny capillary tubes that hold moisture against gravitational pull, storing plant-available water for roots during dry periods.\n- *Limitation*: When saturated, micro-pores drain very slowly, restricting root aeration if macro-pores are absent."
                        }
                    },
                    {
                        "type": "comparison_table",
                        "title": "Macro-Pores vs Micro-Pores",
                        "content": {
                            "title": "Comparison of Soil Pore Classes",
                            "headers": ["Property", "Macro-Pores (Large)", "Micro-Pores (Capillary)"],
                            "rows": [
                                ["Dominant Soil Type", "Sandy soils and crumb aggregates", "Heavy clay soils and humus"],
                                ["Primary Function", "Gas exchange (aeration) & gravitational drainage", "Capillary water retention for plant roots"],
                                ["Water Movement", "Rapid gravitational percolation", "Slow capillary suction movement"],
                                ["Vulnerability to Compaction", "First to be crushed under tractor tires", "Resistant to compression; remain intact"]
                            ]
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "Particle Density vs Bulk Density",
                        "content": {
                            "title": "Measuring Soil Mass per Unit Volume",
                            "text": "Soil density is evaluated using two fundamental physical metrics:\n\n### 1. Particle Density ($D_p$)\n- The mass per unit volume of the **solid mineral particles only**, excluding all pore spaces.\n- For almost all mineral soils, particle density is a standard geological constant of **$2.65\\text{ g/cm}^3$** (the density of quartz and feldspar).\n\n### 2. Bulk Density ($D_b$)\n- The dry mass per unit volume of the **undisturbed whole soil**, including both solid particles and pore spaces:\n\n$$\\text{Bulk Density } (D_b) = \\frac{\\text{Dry Mass of Soil } (\\text{g})}{\\text{Total Undisturbed Volume } (\\text{cm}^3)}$$\n\n- **Loose Organic Topsoil**: Low bulk density ($1.0\\text{--}1.3\\text{ g/cm}^3$) $\\rightarrow$ High porosity ($>50\\%$).\n- **Compacted Subsoil**: High bulk density ($>1.6\\text{ g/cm}^3$) $\\rightarrow$ Low porosity ($<35\\%$), physically restricting root growth."
                        }
                    },
                    {
                        "type": "definition_card",
                        "title": "Key Formula: Soil Porosity Percentage",
                        "content": {
                            "term": "Porosity Calculation Formula",
                            "definition": "Porosity (\\%) = (1 - (Bulk Density / Particle Density)) * 100",
                            "example": "If Db = 1.325 g/cm3 and Dp = 2.65 g/cm3, then Porosity = (1 - (1.325 / 2.65)) * 100 = 50%."
                        }
                    }
                ],
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Porosity and Bulk Density: Loose vs Compacted Soil",
                        "content": {
                            "title": "Porosity and Bulk Density: Loose vs Compacted Soil",
                            "caption": "Comparative cross-section showing loose organic topsoil (low bulk density 1.1 g/cm3, abundant macro-pores) vs heavily compacted soil (high bulk density 1.7 g/cm3, crushed macro-pores, stunted roots)."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The Agronomic Hazards of Soil Compaction",
                        "content": {
                            "title": "When Bulk Density Crosses the Critical Threshold",
                            "text": "When heavy agricultural equipment or continuous cattle traffic compresses wet soil, macro-pores are crushed, causing bulk density to spike above **$1.6\\text{ g/cm}^3$**:\n\n- **Physical Root Stunting**: Mechanical impedance exceeds root penetration pressure; roots become thick, crooked, and confined to the top few centimeters.\n- **Surface Erosion**: Infiltration capacity plummets; heavy rainfall pools on the surface and washes topsoil away as violent runoff.\n- **Anaerobic Root Rot**: Lack of aeration triggers oxygen starvation, promoting harmful anaerobic pathogens that cause root rots and denitrification."
                        }
                    }
                ],
                [
                    {
                        "type": "mini_activity",
                        "title": "Practical Lab: Measuring Soil Bulk Density",
                        "content": {
                            "title": "Calculating Bulk Density from Core Samples",
                            "task": "1. Drive a metal cylinder of known volume ($V = \\pi r^2 h$, e.g. $100\\text{ cm}^3$) into loose garden soil.\n2. Extract the undisturbed core, place it in an oven at $105^\\circ\\text{C}$ for 24 hours to remove moisture, and weigh the dry soil mass ($M$).\n3. Calculate bulk density: $D_b = M / V$.\n4. Repeat the procedure on a compacted cattle path and compare the calculated bulk densities and porosity percentages.",
                            "materials": ["Metal Core Sampler", "Weighing Balance", "Drying Oven / Sun Pan", "Ruler"],
                            "safety": "Use insulated gloves when handling heated metal core cylinders."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Core Summary: Porosity and Density",
                        "content": {
                            "title": "Key Takeaways",
                            "text": "- **Soil porosity (50%)** is vital for balancing air (macro-pores) and capillary water (micro-pores).\n- **Particle density** is constant at $2.65\\text{ g/cm}^3$; **bulk density** varies from $1.0\\text{ to }1.7+\\text{ g/cm}^3$.\n- **Compaction** crushes macro-pores, elevates bulk density above $1.6\\text{ g/cm}^3$, and stunts root elongation.\n- **Organic amendments and minimum tillage** maintain low bulk density and high aeration."
                        }
                    }
                ],
                [
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Calculating Bulk Density and Impact",
                        "content": {
                            "question": "A core soil sampler with a volume of 200 cm³ is used to extract a soil sample from a commercial tractor transit lane. After oven drying, the dry soil mass is 340 grams. Assuming a standard particle density of 2.65 g/cm³, what is the bulk density and what does this indicate for crop roots?",
                            "options": [
                                "Bulk density is 0.58 g/cm³; the soil is too loose and plants will blow away in the wind",
                                "Bulk density is 1.70 g/cm³; this indicates severe soil compaction that physically blocks root elongation and severely restricts water infiltration",
                                "Bulk density is 2.65 g/cm³; the soil contains zero solid particles",
                                "Bulk density is 540 g/cm³; the soil has transformed into solid diamond rock"
                            ],
                            "answer": "B",
                            "explanation": "Bulk density = Dry mass / Volume = 340 g / 200 cm³ = 1.70 g/cm³. A bulk density of 1.70 g/cm³ exceeds the critical root-limiting threshold (typically > 1.60 g/cm³ for loams and clays). At this high density, macro-pores have been crushed, resulting in low porosity (~35.8%), high surface runoff, oxygen starvation, and severe physical restriction of crop roots."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 4: Soil Color
        # =====================================================================
        {
            "unit_order": 4,
            "unit_name": "Soil Color",
            "unit_description": "Soil color as a diagnostic indicator, influencing factors (organic matter, iron oxidation states Fe3+/Fe2+, drainage catena), interpreting red/brown/grey/mottled colors, and Munsell charts.",
            "lesson_title": "Soil Color and Diagnostic Soil Indicators",
            "pages": [
                [
                    {
                        "type": "suggested_image",
                        "title": "Munsell Soil Color Diagnostic Notation",
                        "content": {
                            "title": "Munsell Soil Color Diagnostic Notation",
                            "caption": "A standardized Munsell Soil Color Chart displaying gradations of hue, value, and chroma used to identify organic matter and drainage conditions."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Soil Color",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Explain why **soil color** serves as a vital diagnostic window into soil fertility and internal drainage.",
                                "Analyze the three primary determinants of soil color: **organic matter (humus)**, **iron oxides**, and **water table fluctuations**.",
                                "Distinguish between **ferric iron ($\\text{Fe}^{3+}$ red/yellow)** and **ferrous iron ($\\text{Fe}^{2+}$ grey/gleying)** oxidation states.",
                                "Interpret red, dark brown, yellow, grey, and **mottled colors** for agribusiness farm decision-making."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Soil Color as an Agronomic Window",
                        "content": {
                            "title": "Reading the Hidden History of Soil",
                            "text": "While color does not directly nourish crops (aside from dark soils absorbing more solar thermal energy), **soil color is the most obvious and powerful visual diagnostic indicator** available to farmers and soil scientists.\n\n- By simply observing the color of topsoils and subsoils, a farmer can immediately deduce organic matter levels, soil aeration status, internal drainage rates, and the depth of the seasonal water table."
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "Determinants of Soil Color",
                        "content": {
                            "title": "Organic Matter and Iron Geochemistry",
                            "text": "Soil color is governed by three primary environmental drivers:\n\n### 1. Organic Matter (Humus Content)\n- Fully decomposed organic matter (humus) is dark brown or jet-black.\n- Humus coats mineral particles, turning topsoils into rich, dark brown colors that signify high microbial activity, high Cation Exchange Capacity, and excellent fertility.\n\n### 2. Iron Oxide Mineral Chemistry\n- Iron ($\text{Fe}$) is widely distributed in mineral soils and changes color depending on aeration:\n  - **Oxidized Ferric Iron ($\\text{Fe}^{3+}$)**: In well-drained, aerated soils, iron forms hematite and goethite, giving soils a brilliant **reddish or yellowish-brown color**.\n  - **Reduced Ferrous Iron ($\\text{Fe}^{2+}$)**: In waterlogged, oxygen-starved soils, anaerobic bacteria reduce iron into soluble $\text{Fe}^{2+}$, stripping the red color and leaving a dull **grey, bluish, or greenish color (gleying)**.\n\n### 3. Drainage & Water Table Fluctuations\n- **Mottled Soils**: Spots of bright orange/red iron in a dull grey background indicate a fluctuating water table that is dry in summer but waterlogged in winter."
                        }
                    },
                    {
                        "type": "comparison_table",
                        "title": "Agricultural Interpretation of Soil Colors",
                        "content": {
                            "title": "Soil Color Interpretation Matrix",
                            "headers": ["Observed Soil Color", "Dominant Chemical / Physical Agent", "Drainage & Aeration Status", "Crop Suitability & Enterprise Advice"],
                            "rows": [
                                ["Dark Brown / Jet Black", "High Organic Matter (Humus)", "Well-aerated, high fertility", "Prime topsoil; ideal for commercial vegetables, maize, and beans"],
                                ["Bright Red / Deep Orange", "Oxidized Ferric Iron ($\\text{Fe}^{3+}$, Hematite)", "Excellent drainage; zero waterlogging", "Ideal for deep-rooted perennial tea, coffee, macadamia, and citrus"],
                                ["Dull Grey / Pale Bluish (Gleyed)", "Reduced Ferrous Iron ($\\text{Fe}^{2+}$, Anaerobic)", "Chronic waterlogging; severe oxygen lack", "Unsuitable for upland crops; ideal for aquaculture ponds and paddy rice"],
                                ["Mottled (Grey with Red Spots)", "Fluctuating seasonal water table", "Seasonally saturated and aerated", "Requires raised planting beds or drainage ditches for perennial crops"],
                                ["Whitish Crust on Surface", "Soluble mineral salts ($\\text{NaCl, CaSO}_4$)", "High evaporation in drylands", "Saline soil hazard; requires leaching with fresh water and gypsum"]
                            ]
                        }
                    }
                ],
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Soil Color Diagnostic Matrix & Iron Oxidation States",
                        "content": {
                            "title": "Soil Color Diagnostic Matrix & Iron Oxidation States",
                            "caption": "Diagnostic color matrix connecting Dark Brown (Humus), Bright Red (Fe3+ Oxidized Aerobic), Grey Gleying (Fe2+ Reduced Anaerobic), and Mottled patches to soil management recommendations."
                        }
                    },
                    {
                        "type": "definition_card",
                        "title": "Key Term: Gleying",
                        "content": {
                            "term": "Gleying (Gley Soil)",
                            "definition": "The development of a dull greenish-grey or bluish-grey soil color caused by the chemical reduction of iron (from Fe3+ to Fe2+) under prolonged anaerobic waterlogged conditions.",
                            "example": "Low-lying swamp soils in valley bottoms exhibiting bluish-grey clay profiles due to standing water."
                        }
                    }
                ],
                [
                    {
                        "type": "mini_activity",
                        "title": "Field Observation: Soil Color Audit",
                        "content": {
                            "title": "Comparing Topsoil, Subsoil, and Wetland Colors",
                            "task": "Collect three soil samples:\n\n1. Sample A: Topsoil (0–10 cm) from an organic vegetable garden.\n2. Sample B: Subsoil (50 cm) from a road excavation or deep pit.\n3. Sample C: Lowland soil from a drainage ditch or valley marsh.\n\nPlace samples side by side in bright natural sunlight on white paper. Note color differences, match with the diagnostic chart, and write an agronomic evaluation of drainage and organic content.",
                            "materials": ["3 Soil Samples", "White Paper", "Hand Lens", "Notepad"],
                            "safety": "Wash hands with soap and water after handling soil."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Core Summary: Soil Color",
                        "content": {
                            "title": "Key Takeaways",
                            "text": "- **Dark brown/black color** indicates high humus content and high biological fertility.\n- **Bright red/orange subsoils** indicate oxidized $\\text{Fe}^{3+}$ and excellent internal drainage.\n- **Dull grey color (gleying)** indicates reduced $\\text{Fe}^{2+}$ and chronic waterlogging.\n- **Mottled soil** warns of a fluctuating water table requiring artificial drainage."
                        }
                    }
                ],
                [
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Diagnosing Subsoil Color in Avocado Orchards",
                        "content": {
                            "question": "An agribusiness investor is surveying a 10-acre parcel in Murang'a to plant commercial Hass avocados. Digging a test pit reveals that below 35 cm depth, the soil changes into a dull, solid grey color with bluish streaks. Why should the investor avoid planting avocados on this parcel?",
                            "options": [
                                "The grey color indicates excessive nitrogen fertilizer that will cause fruit burns",
                                "The solid grey color (gleying) reveals reduced ferrous iron (Fe²⁺) caused by chronic waterlogging and severe oxygen starvation; avocado taproots will rot and die within days of heavy rainfall",
                                "Avocado trees will absorb the grey pigment and turn avocado fruits solid grey",
                                "Grey soil attracts underground termites that consume avocado wood"
                            ],
                            "answer": "B",
                            "explanation": "A solid grey subsoil with bluish streaks (gleying) is conclusive diagnostic evidence of chronic waterlogging and anaerobic conditions. Avocado trees (*Persea americana*) possess extremely sensitive root systems that demand high oxygen levels and succumb to lethal Phytophthora root rot within 48 hours of saturation. Planting avocados in gleyed soil will lead to total crop failure unless massive drainage engineering is installed."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 5: Soil Sampling and Investigation
        # =====================================================================
        {
            "unit_order": 5,
            "unit_name": "Soil Sampling and Investigation",
            "unit_description": "Agronomic rationale for soil testing, sampling tools (auger vs spade), sampling methodologies (zigzag vs grid), V-shaped 20 cm slicing protocol, composite sample preparation, and contaminated zones to avoid.",
            "lesson_title": "Soil Sampling Protocols and Field Investigation",
            "pages": [
                [
                    {
                        "type": "suggested_image",
                        "title": "Soil Sampling Tools and Field Investigation Equipment",
                        "content": {
                            "title": "Soil Sampling Tools and Field Investigation Equipment",
                            "caption": "An agricultural officer using a soil auger, plastic core bucket, sample bags, and labeling markers to collect composite field samples for laboratory assay."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Soil Sampling",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Explain the agricultural and financial importance of **routine laboratory soil testing**.",
                                "Compare field sampling patterns: **randomized zigzag sampling** vs **precision grid sampling**.",
                                "Execute the step-by-step **V-shaped sampling protocol** to collect representative cores at $15\\text{--}20\\text{ cm}$ depth.",
                                "Identify localized anomalous zones (manure heaps, charcoal burning sites, fence lines) that must be strictly avoided during sampling."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Why Soil Sampling is Essential for Agribusiness",
                        "content": {
                            "title": "Precision Farming Replaces Blind Guesswork",
                            "text": "**Soil sampling** is the disciplined collection of small, representative soil portions from an agricultural field to be analyzed in a scientific laboratory for nutrient concentrations, soil pH, organic carbon, and cation exchange capacity.\n\n- **Financial Optimization**: Applying synthetic fertilizers blindly wastes thousands of shillings on unnecessary nutrients while worsening soil acidity. Soil test reports provide precise fertilizer prescriptions and lime requirements."
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "Field Sampling Patterns and Tools",
                        "content": {
                            "title": "Zigzag vs Grid Methods and Equipment Selection",
                            "text": "### 1. Sampling Patterns\n- **Zigzag Method**: The farmer walks across the field following a randomized zigzag path, collecting 15 to 20 sub-samples (cores). Optimal for fields with uniform slope and soil history.\n- **Grid Method**: The farm is divided into equal geometric blocks (e.g. 1-acre grids) with sub-samples taken from each block center. Best for precision agriculture and variable-rate fertilizer application.\n\n### 2. Tool Selection\n- **Soil Auger (T-bar / Dutch Auger)**: The gold-standard tool for extracting uniform, undisturbed cylindrical soil cores quickly.\n- **Spade & Panga**: Used when an auger is unavailable; requires digging a clean V-shaped hole.\n- *Critical Rule*: All buckets, bowls, and sampling tools must be **clean plastic**. Never use galvanized or rusty metal buckets, as they leach Zinc ($Zn$) and Iron ($Fe$), ruining trace mineral assay results."
                        }
                    },
                    {
                        "type": "step_process",
                        "title": "Step-by-Step Protocol: Collecting a Composite Soil Sample",
                        "content": {
                            "title": "The 6-Step Laboratory Sampling Workflow",
                            "steps": [
                                "1. **Clear Surface Litter**: Gently brush away dry grass, mulch, and undecomposed weeds from the sampling spot without scraping away topsoil.",
                                "2. **Dig a V-Shaped Hole**: Using a clean spade, dig a V-shaped hole to a depth of **15 cm to 20 cm** (the active crop root zone).",
                                "3. **Slice a Uniform Core**: Cut a 1.5 cm thick slice of soil from the flat side of the hole. Trim the left and right edges with a clean knife, leaving a 2 cm center strip.",
                                "4. **Combine in Plastic Bucket**: Deposit the center core into a clean plastic bucket. Repeat at 15–20 spots across the field following the zigzag path.",
                                "5. **Mix to Form Composite Sample**: Thoroughly mix all sub-samples together in the bucket. Extract a **500 g representative composite sample** and spread it on clean paper to air-dry in the shade (never use heat/ovens, which volatilize nitrogen).",
                                "6. **Pack, Label, and Dispatch**: Seal the dry sample in a clean plastic bag with a waterproof label indicating farmer name, farm block ID, date, GPS coordinates, and intended crop."
                            ]
                        }
                    }
                ],
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Step-by-Step Zigzag Soil Sampling Protocol",
                        "content": {
                            "title": "Step-by-Step Zigzag Soil Sampling Protocol",
                            "caption": "Field layout flowchart illustrating the randomized zigzag walking path, V-shaped 20 cm spade excavation, center slice trimming, bucket composite mixing, and labeling."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Critical Zones to Avoid During Soil Sampling",
                        "content": {
                            "title": "Preventing Sample Contamination and Skewed Readings",
                            "text": "To guarantee that the laboratory report accurately reflects the average field condition, farmers must **never** take sub-samples from anomalous spots:\n\n- **Old Manure Heaps / Compost Pits**: Extremely high organic matter that falsely inflates nitrogen and phosphorus readings.\n- **Charcoal Burning Sites / Wood Ash Heaps**: Alkaline ash ($K_2CO_3$) drastically spikes soil pH readings from 5.0 to 8.5.\n- **Fence Lines, Footpaths, and Field Headlands**: Subject to livestock urine concentration, compaction, and road gravel dust.\n- **Under Isolated Large Trees**: Bird droppings and dense leaf litter skew local nutrient values.\n- **Wet Drainage Ditches & Furrows**: Minerals have leached away or accumulated artificially."
                        }
                    }
                ],
                [
                    {
                        "type": "mini_activity",
                        "title": "Field Simulation: Conducting a School Farm Soil Sampling",
                        "content": {
                            "title": "Practical Field Soil Sampling Exercise",
                            "task": "In groups of five, execute a complete soil sampling simulation on the school agriculture demonstration plot:\n\n1. Lay out a 10-point zigzag walking path using marker flags.\n2. Practice clearing surface litter, digging 20 cm V-shaped holes, and trimming a 2 cm center core slice.\n3. Composite and thoroughly mix all sub-samples in a plastic bucket.\n4. Package and complete an authentic agricultural laboratory submission label.",
                            "materials": ["Spade / Trowel", "Clean Plastic Bucket", "Plastic Sampling Bags", "Marker Pens", "Ruler"],
                            "safety": "Handle spades carefully to prevent foot injuries. Wash hands after handling soil."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Core Summary: Soil Sampling",
                        "content": {
                            "title": "Key Takeaways",
                            "text": "- **Soil sampling** provides scientific data to optimize fertilizer and lime applications.\n- **Zigzag method** collects 15–20 sub-samples to create a single 500g composite sample.\n- **V-shaped 15–20 cm holes** sample the active root zone accurately.\n- **Always avoid anomalous spots** (ash heaps, manure piles, fence lines) to prevent skewed laboratory results."
                        }
                    }
                ],
                [
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Avoiding Sampling Contamination",
                        "content": {
                            "question": "A farm worker collecting soil samples for a 5-acre maize field decides to take half of the sub-samples from an old charcoal burning heap near the fence because the soil is dark and easy to dig. What error will this cause in the laboratory analysis?",
                            "options": [
                                "The laboratory machines will catch fire due to unburnt charcoal particles",
                                "The sample will give a false, unrepresentative reading of abnormally high pH (alkaline) and inflated potassium levels, leading the agronomy lab to wrongly recommend zero lime for an otherwise acidic field",
                                "The soil test will report that the field is located underwater",
                                "The sample will show 100% clay content regardless of actual texture"
                            ],
                            "answer": "B",
                            "explanation": "Wood ash and charcoal residues are rich in potassium carbonate ($K_2CO_3$) and calcium compounds, which are strongly alkaline. Sampling from charcoal burning sites will drastically spike the composite sample's pH reading (e.g. reading pH 8.0 instead of the field's true pH 4.8). This false reading will deceive agronomists into advising against lime application, resulting in crop stunting and phosphorus fixation across the entire field."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 6: Soil pH
        # =====================================================================
        {
            "unit_order": 6,
            "unit_name": "Soil pH",
            "unit_description": "Definition of soil pH and logarithmic scale (0–14), optimal agricultural range (pH 6.0–7.0), biochemical mechanisms of phosphorus fixation by Al3+/Fe3+, and soil amendments (agricultural lime vs elemental sulfur).",
            "lesson_title": "Soil pH and Nutrient Availability Dynamics",
            "pages": [
                [
                    {
                        "type": "suggested_image",
                        "title": "Spreading Agricultural Lime to Neutralize Acidic Soil",
                        "content": {
                            "title": "Spreading Agricultural Lime to Neutralize Acidic Soil",
                            "caption": "A tractor broadcasting fine white agricultural lime (calcium carbonate) across an acidic field to raise soil pH and unlock bound phosphorus nutrients."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Soil pH",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Define **soil pH** as the negative logarithm of hydrogen ion ($H^+$) concentration on a scale of 0 to 14.",
                                "Explain why the range of **pH 6.0 to 7.0** represents the optimal 'sweet spot' for plant nutrient availability and microbial life.",
                                "Analyze the biochemical mechanism of **phosphorus fixation** in acidic soils ($pH < 5.5$) by soluble aluminum ($Al^{3+}$) and iron ($Fe^{3+}$).",
                                "Formulate soil remediation plans using **agricultural lime** ($CaCO_3$) to raise pH or **elemental sulfur** to lower pH."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "What is Soil pH?",
                        "content": {
                            "title": "The Master Gatekeeper of Soil Chemistry",
                            "text": "**Soil pH** measures the acidity or alkalinity of the soil solution (the film of water surrounding soil particles). It is formally defined as the negative logarithm of hydrogen ion activity:\n\n$$\\text{pH} = -\\log_{10}[H^+]$$\n\n- **The Logarithmic Scale**: Because the scale is logarithmic, a soil at **pH 5.0 is 10 times more acidic than pH 6.0**, and **100 times more acidic than pH 7.0**!\n- **pH 7.0**: Neutral (equal concentrations of $H^+$ and $OH^-$ ions).\n- **pH < 7.0**: Acidic (excess $H^+$ ions).\n- **pH > 7.0**: Alkaline / Basic (excess $OH^-$ ions)."
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "Soil pH and Nutrient Solubility Dynamics",
                        "content": {
                            "title": "How pH Governs Nutrient Uptake",
                            "text": "The pH of the soil solution directly controls whether essential plant nutrients dissolve into absorbable forms or precipitate out into locked, insoluble compounds:\n\n### 1. Strongly Acidic Soils ($pH < 5.0$)\n- **Phosphorus Fixation**: Soluble Aluminum ($Al^{3+}$) and Iron ($Fe^{3+}$) ions bond aggressively with phosphate ions ($H_2PO_4^-$), forming rock-like insoluble precipitates (Aluminum Phosphate). Crops show severe purpling of leaves (phosphorus starvation) despite heavy fertilizer application.\n- **Aluminum Toxicity**: Free $Al^{3+}$ dissolves to toxic levels, burning and stunting young root tips.\n- **Microbial Collapse**: Beneficial nitrogen-fixing bacteria (*Rhizobium*) and nitrifiers die off, halting organic nitrogen cycling.\n\n### 2. Alkaline Soils ($pH > 7.8$)\n- Micronutrients such as **Iron ($Fe$), Zinc ($Zn$), Manganese ($Mn$), and Copper ($Cu$)** precipitate into insoluble oxides, causing acute leaf chlorosis (yellowing).\n- Phosphorus is locked up by excess Calcium ($Ca$), forming insoluble Calcium Phosphate."
                        }
                    },
                    {
                        "type": "comparison_table",
                        "title": "Soil pH Ranges and Agronomic Consequences",
                        "content": {
                            "title": "Soil pH Classification Matrix",
                            "headers": ["pH Range", "Soil Classification", "Nutrient & Microbial Behavior", "Management Action Required"],
                            "rows": [
                                ["< 5.0", "Strongly Acidic", "Severe Phosphorus fixation; toxic $Al^{3+}$/$\\text{Mn}^{2+}$; nitrogen fixation stops", "Mandatory application of agricultural lime ($CaCO_3$ or Dolomite)"],
                                ["5.0 – 5.9", "Moderately Acidic", "Slight nutrient lockup; suitable for tea, coffee, pineapples, Irish potatoes", "Moderate liming or use of non-acidifying CAN fertilizer"],
                                ["6.0 – 7.0", "Slightly Acidic to Neutral (Optimal)", "Maximum solubility of all macro and micronutrients; peak microbial activity", "Ideal state; maintain with organic compost and balanced fertilizers"],
                                ["> 7.8", "Alkaline / Calcareous", "Deficiency of Iron, Zinc, Copper; Phosphorus locked by Calcium", "Apply elemental sulfur, ammonium sulfate, and heavy organic compost"]
                            ]
                        }
                    }
                ],
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Soil pH and Nutrient Availability Scale",
                        "content": {
                            "title": "Soil pH and Nutrient Availability Scale",
                            "caption": "Nutrient availability band chart demonstrating how Nitrogen, Phosphorus, Potassium, Calcium, and trace minerals peak in availability within the pH 6.0–7.0 zone while locking up in extreme acidic or alkaline zones."
                        }
                    },
                    {
                        "type": "step_process",
                        "title": "Soil Remediation: Liming Acidic Soils",
                        "content": {
                            "title": "Protocol for Correcting Soil Acidity",
                            "steps": [
                                "1. **Conduct Laboratory Soil Assay**: Determine exact soil pH and buffer capacity to calculate required liming rate (typically 1.5 to 3.0 tonnes/hectare).",
                                "2. **Select Liming Material**: Choose fine agricultural lime (**Calcium Carbonate - $CaCO_3$**) or **Dolomitic Lime ($CaMg(CO_3)_2$)** if magnesium is also deficient.",
                                "3. **Broadcast Uniformly**: Spread lime evenly across ploughed soil 1 to 2 months before planting to allow adequate reaction time with soil moisture.",
                                "4. **Incorporate Thoroughly**: Harrow or till the soil to mix lime throughout the top 15–20 cm root zone.",
                                "5. **Switch from DAP to CAN/NPK**: Replace acidifying fertilizers like Diammonium Phosphate (DAP) with Calcium Ammonium Nitrate (CAN) or neutral organic compost."
                            ]
                        }
                    }
                ],
                [
                    {
                        "type": "mini_activity",
                        "title": "Laboratory Practical: Soil pH Testing with Indicator Strips",
                        "content": {
                            "title": "Testing Soil pH of Farm Samples",
                            "task": "1. Place 1 tablespoon of dry, pulverized soil in a clean test tube.\n2. Add 2 tablespoons of distilled water (pH 7.0) and shake vigorously for 2 minutes.\n3. Let the soil settle for 10 minutes, then dip a strip of broad-range pH indicator paper into the supernatant liquid.\n4. Match the resulting color against the standard pH color scale. Record the pH and determine whether the soil requires lime, sulfur, or no amendment.",
                            "materials": ["3 Soil Samples", "Distilled Water", "pH Indicator Strips / Universal Indicator", "Test Tubes"],
                            "safety": "Do not taste or ingest chemical reagents."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Core Summary: Soil pH Dynamics",
                        "content": {
                            "title": "Key Takeaways",
                            "text": "- **pH 6.0 to 7.0** optimizes nutrient solubility and beneficial bacterial life.\n- **Acid soils (pH < 5.0)** lock up phosphorus via aluminum/iron precipitation.\n- **Agricultural lime ($CaCO_3$)** neutralizes $H^+$ ions, raises pH, and unlocks phosphorus.\n- **Elemental sulfur** acidifies high-pH alkaline soils into optimal ranges."
                        }
                    }
                ],
                [
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Overcoming Phosphorus Fixation",
                        "content": {
                            "question": "A farmer in Western Kenya applies heavy doses of DAP fertilizer to a maize crop on soil with pH 4.6, but the maize plants remain stunted with distinct purple coloration on the lower leaves. Why did the fertilizer fail, and what is the required corrective intervention?",
                            "options": [
                                "The maize seeds were damaged by cold weather; the farmer should install greenhouses",
                                "At pH 4.6, soluble aluminum and iron chemically bind with the phosphate from DAP, forming insoluble precipitates that roots cannot absorb; the farmer must apply agricultural lime to raise the pH above 6.0 to unlock phosphorus",
                                "The DAP fertilizer evaporated into the air as chlorine gas",
                                "The soil contains too much calcium that killed the maize roots"
                            ],
                            "answer": "B",
                            "explanation": "Purple leaf coloration is the classic symptom of Phosphorus deficiency. In strongly acidic soils (pH < 5.0), high concentrations of soluble Aluminum ($Al^{3+}$) and Iron ($Fe^{3+}$) react with applied phosphate fertilizers to form insoluble Aluminum and Iron Phosphates (Phosphorus Fixation). Applying agricultural lime neutralizes acidity, raising pH above 6.0, releasing the trapped phosphorus, and allowing root uptake."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 7: Cation Exchange Capacity
        # =====================================================================
        {
            "unit_order": 7,
            "unit_name": "Cation Exchange Capacity",
            "unit_description": "Definition of CEC, negative electrical surface charge of clay colloids and humus, nutrient cations (Ca2+, Mg2+, K+, NH4+), electrostatic retention, and fertilizer spoon-feeding on sandy vs clay soils.",
            "lesson_title": "Cation Exchange Capacity (CEC) and Colloid Chemistry",
            "pages": [
                [
                    {
                        "type": "suggested_image",
                        "title": "Clay Soil Colloids and Soil Mineral Particles",
                        "content": {
                            "title": "Clay Soil Colloids and Soil Mineral Particles",
                            "caption": "Fine clay particles on agricultural land demonstrating the microscopic colloidal surface area responsible for electrostatic nutrient cation retention."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Cation Exchange Capacity",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Define **Cation Exchange Capacity (CEC)** as the total capacity of a soil to hold and exchange exchangeable cations.",
                                "Explain the origin of **negative electrical surface charges** on soil colloids (**clay minerals and humus**) .",
                                "Identify the major plant nutrient cations: **Calcium ($\\text{Ca}^{2+}$)**, **Magnesium ($\\text{Mg}^{2+}$)**, **Potassium ($\\text{K}^+$)**, and **Ammonium ($\\text{NH}_4^+$)**.",
                                "Formulate fertilizer application schedules tailored to low-CEC (sandy) vs high-CEC (clay/humus) soils."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "What is Cation Exchange Capacity (CEC)?",
                        "content": {
                            "title": "The Soil's Nutrient Holding Battery",
                            "text": "**Cation Exchange Capacity (CEC)** is a fundamental chemical property that quantifies the soil's ability to electrostatically attract, hold, and exchange positively charged nutrient ions (called **cations**).\n\n- Think of CEC as the **size of the soil's rechargeable nutrient battery**. A high-CEC soil has a massive battery that stores large nutrient reserves safely against rainfall leaching, whereas a low-CEC soil has a tiny battery that quickly depletes."
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "The Role of Soil Colloids (Clay and Humus)",
                        "content": {
                            "title": "Microscopic Magnets in the Root Zone",
                            "text": "Cation exchange occurs exclusively on the surfaces of **soil colloids**—microscopic clay particles and decomposed humus molecules ($<0.002\\text{ mm}$):\n\n### 1. Negative Surface Charges\n- Due to chemical isomorphous substitution and broken edge bonds, clay and humus surfaces carry permanent and pH-dependent **negative electrical charges ($-$)**.\n\n### 2. Electrostatic Adsorption\n- Just like opposite magnetic poles attract, the negative colloid surfaces pull and hold positively charged nutrient cations:\n  - **Calcium ($\\text{Ca}^{2+}$)**, **Magnesium ($\\text{Mg}^{2+}$)**, **Potassium ($\\text{K}^+$)**, **Ammonium ($\\text{NH}_4^+$)**, and trace cations ($\\text{Zn}^{2+}, \\text{Fe}^{2+}, \\text{Cu}^{2+}, \\text{Mn}^{2+}$).\n- **Prevention of Leaching**: Because these nutrients are magnetically bound to colloids, rainwater flowing through macro-pores cannot wash them down into groundwater.\n- **Humus Superiority**: Decomposed organic humus has a CEC of **$100\\text{--}300\\text{ cmol/kg}$**, which is **3 to 10 times higher than the best agricultural clay minerals**!"
                        }
                    },
                    {
                        "type": "comparison_table",
                        "title": "Cation Exchange Capacity across Soil Components",
                        "content": {
                            "title": "CEC Values of Soil Constituents",
                            "headers": ["Soil Constituent", "CEC Range (cmol/kg)", "Surface Electrical Charge", "Nutrient Retention Capacity"],
                            "rows": [
                                ["Humus (Organic Matter)", "100 – 300 cmol/kg", "Extremely High Negative Charge", "Superior (Highest nutrient reservoir on earth)"],
                                ["Vermiculite / Smectite Clay", "80 – 150 cmol/kg", "High Negative Charge", "Excellent (Stores large nutrient reserves)"],
                                ["Kaolinite Clay (Red Soils)", "3 – 15 cmol/kg", "Low Negative Charge", "Moderate (Requires compost enhancement)"],
                                ["Quartz Sand", "1 – 5 cmol/kg", "Negligible / Zero Surface Charge", "Extremely Poor (Nutrients leach instantly)"]
                            ]
                        }
                    }
                ],
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Cation Exchange Capacity & Colloid Attraction Model",
                        "content": {
                            "title": "Cation Exchange Capacity & Colloid Attraction Model",
                            "caption": "Chemical model showing negatively charged clay and humus colloids electrostatically holding Ca2+, Mg2+, K+, and NH4+ cations, exchanging them with H+ ions secreted by root hairs."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Managing Fertilizers in Low-CEC vs High-CEC Soils",
                        "content": {
                            "title": "Agronomic Fertilizer Prescriptions Based on CEC",
                            "text": "A farmer's fertilizer strategy must match the field's CEC capacity:\n\n### Low-CEC Soils (Sandy Soils, $<10\\text{ cmol/kg}$)\n- Cannot hold large fertilizer doses; heavy broadcasting leads to immediate leaching and environmental runoff.\n- **Spoon-Feeding Strategy**: Apply nitrogen and potassium fertilizers in small, frequent split-applications throughout the growing season.\n- **Soil Building**: Heavily incorporate compost, farmyard manure, and biochar to build organic matter and raise the CEC permanently.\n\n### High-CEC Soils (Clay Loam & Humus Rich, $>25\\text{ cmol/kg}$)\n- Hold large nutrient quantities securely without leaching.\n- Farmers can apply baseline fertilizers in single or dual bulk applications with confidence that nutrients will remain available throughout the crop cycle."
                        }
                    }
                ],
                [
                    {
                        "type": "mini_activity",
                        "title": "Scenario Exercise: Designing a Fertilizer Schedule for Low-CEC Sand",
                        "content": {
                            "title": "Agronomic Prescription for Sandy Farmland",
                            "task": "A laboratory soil report for a 2-acre coastal cassava farm reveals a sandy texture with a low CEC of $4.5\\text{ cmol/kg}$.\n\n1. Explain why applying 200 kg of Calcium Ammonium Nitrate (CAN) fertilizer in a single broadcast at planting will result in 70% nutrient wastage.\n2. Design an amended fertilizer management plan detailing split-application timing and organic matter additions to maximize nitrogen uptake efficiency.",
                            "materials": ["Case Study Data Sheet", "Notebook", "Calculator"],
                            "safety": "Maintain focus on agronomic and economic efficiency."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Core Summary: Cation Exchange Capacity",
                        "content": {
                            "title": "Key Takeaways",
                            "text": "- **CEC** measures the soil's capacity to hold positively charged nutrient cations.\n- **Negative charges on clay and humus** prevent nutrient leaching by rainwater.\n- **Humus (100–300 cmol/kg)** is the most potent CEC enhancer in agriculture.\n- **Low-CEC sandy soils** require split fertilizer applications (spoon-feeding) and heavy organic matter inputs."
                        }
                    }
                ],
                [
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Nutrient Leaching in Sandy vs Clay Soils",
                        "content": {
                            "question": "Why do sandy soils suffer from rapid fertilizer leaching compared to clayey or humus-rich loam soils?",
                            "options": [
                                "Sand particles are too hot, causing fertilizer granules to turn into steam",
                                "Sandy soils consist predominantly of coarse quartz grains that lack negative electrical surface charges, leaving them unable to electrostatically bind positively charged nutrient cations (Ca²⁺, Mg²⁺, K⁺, NH₄⁺)",
                                "Sand grains attract positive ions so tightly that plant roots cannot pull them off",
                                "Sandy soils contain too many earthworms that physically consume synthetic fertilizer"
                            ],
                            "answer": "B",
                            "explanation": "Cation retention depends on negative electrical charges found on clay and humus colloids. Quartz sand particles are coarse and chemically inert, carrying virtually zero surface charge (CEC 1–5 cmol/kg). When soluble fertilizers dissolve in rainwater, sandy soils cannot hold the positive cations, allowing rainfall to wash (leach) them deep into groundwater below the root zone."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 8: Soil Salinity
        # =====================================================================
        {
            "unit_order": 8,
            "unit_name": "Soil Salinity",
            "unit_description": "Causes of soil salinity in ASALs and poor irrigation schemes, osmotic potential reversal (physiological drought), sodium clay dispersion, visual diagnostic signs, and reclamation with gypsum (CaSO4) and leaching.",
            "lesson_title": "Soil Salinity, Osmotic Stress, and Reclamation",
            "pages": [
                [
                    {
                        "type": "suggested_image",
                        "title": "Saline Soil Degradation with White Salt Crust",
                        "content": {
                            "title": "Saline Soil Degradation with White Salt Crust",
                            "caption": "An agricultural field in a semi-arid zone exhibiting a white surface salt crust caused by high evaporation and poor irrigation water drainage."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Soil Salinity",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Define **soil salinity** as the concentration of soluble mineral salts ($\\text{NaCl}, \\text{Na}_2\\text{SO}_4, \\text{MgSO}_4$) in the soil.",
                                "Analyze the natural and human causes of salinity in **Arid and Semi-Arid Lands (ASALs)** and irrigation schemes.",
                                "Explain the physiological mechanism of **osmotic potential reversal (physiological drought)** and ion toxicity in crops.",
                                "Formulate reclamation strategies for saline-sodic soils using **agricultural gypsum** ($\\text{CaSO}_4$) and fresh water leaching."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "What is Soil Salinity?",
                        "content": {
                            "title": "The Threat of Salt Accumulation in Farmland",
                            "text": "**Soil salinity** refers to the excessive accumulation of water-soluble mineral salts—predominantly **Sodium Chloride ($\\text{NaCl}$), Sodium Sulfate ($\\text{Na}_2\\text{SO}_4$), Calcium Chloride ($\\text{CaCl}_2$), and Magnesium Sulfate ($\\text{MgSO}_4$)**—in the crop root zone.\n\n- Salinization is a major form of land degradation affecting irrigated valleys and dryland farming in Kenya's ASAL counties (such as Garissa, Turkana, Baringo, and Kajiado)."
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "Causes of Soil Salinity",
                        "content": {
                            "title": "Natural Dryland Dynamics vs Human Irrigation Errors",
                            "text": "### 1. Natural Arid Processes\n- In semi-arid regions, annual evaporation rates far exceed annual rainfall ($>2,500\\text{ mm}$ evaporation vs $<400\\text{ mm}$ rain).\n- Capillary action pulls mineral-rich groundwater upward toward the surface; as pure water evaporates under the scorching sun, dissolved mineral salts crystallize on the topsoil, forming a white crust.\n\n### 2. Human-Induced Salinity (Poor Irrigation Management)\n- **Salty Borehole Water**: Irrigating crops with brackish groundwater containing dissolved sodium.\n- **Lack of Subsurface Drainage**: Applying irrigation water without drainage ditches causes water tables to rise into the root zone, depositing salts.\n- **Insufficient Leaching Fraction**: Applying just enough water for plant use without extra water to wash accumulated salts below the root zone."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The Osmotic Effect and Physiological Drought",
                        "content": {
                            "title": "Why Crops Wilt in Wet Saline Soils",
                            "text": "Salinity damages crops primarily through the **osmotic effect**:\n\n- **Normal Soil**: Root sap has a higher solute concentration than soil water. Through **osmosis**, water flows naturally from low-solute soil into high-solute root hairs.\n- **Saline Soil**: Soluble salts make the soil water extremely concentrated (high osmotic pressure). The osmotic gradient reverses: soil water holds moisture so tightly that root hairs cannot pull it into the plant.\n- **Physiological Drought**: The crop dehydrates, wilts, and dries up even when the field is visibly wet with water!\n- **Sodium Clay Dispersion**: High sodium ($Na^+$) strips calcium bridges, causing clay aggregates to disperse into structureless, impervious cement that suffocates root respiration."
                        }
                    }
                ],
                [
                    {
                        "type": "comparison_table",
                        "title": "Normal Soil vs Saline Soil Comparison",
                        "content": {
                            "title": "Salinity Impact Matrix",
                            "headers": ["Parameter", "Normal Agricultural Soil", "Highly Saline-Sodic Soil"],
                            "rows": [
                                ["Electrical Conductivity (EC)", "< 2.0 dS/m (Safe)", "> 4.0 dS/m (Severe salinity stress)"],
                                ["Osmotic Root Water Flow", "Water flows rapidly into root cells", "Water chemically locked in soil; roots dehydrate"],
                                ["Soil Surface Appearance", "Dark brown crumbly aggregates", "White crystalline salt crust; cracked hardpan"],
                                ["Crop Symptoms", "Vibrant green, turgid leaves", "Burnt leaf tips (marginal necrosis), stunted wilting"],
                                ["Clay Structure", "Aggregated porous crumbs", "Dispersed, sealed, impervious hardpan"]
                            ]
                        }
                    },
                    {
                        "type": "step_process",
                        "title": "Protocol: Reclaiming Saline-Sodic Soils",
                        "content": {
                            "title": "3-Stage Soil Reclamation Workflow",
                            "steps": [
                                "1. **Apply Agricultural Gypsum ($\\text{CaSO}_4 \\cdot 2\\text{H}_2\\text{O}$)**: Broadcast gypsum across the field. Calcium ions ($\\text{Ca}^{2+}$) displace toxic sodium ions ($\\text{Na}^+$) from clay colloid surfaces, restoring crumb structure.",
                                "2. **Flush with Fresh Water (Leaching)**: Flood the field with clean, low-salt fresh water. Displaced sodium reacts with sulfate to form soluble Sodium Sulfate ($\\text{Na}_2\\text{SO}_4$), which dissolves in the leach water.",
                                "3. **Install Deep Drainage Ditches**: Construct subsurface tile drains or open drainage ditches to carry the salty leachate completely away from the farm.",
                                "4. **Plant Salt-Tolerant Halophytes**: Grow deep-rooted halophytes (barley, Rhodes grass, sugar beets) to extract residual salts."
                            ]
                        }
                    }
                ],
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Osmotic Root Flow Model: Normal vs Saline Soil",
                        "content": {
                            "title": "Osmotic Root Flow Model: Normal vs Saline Soil",
                            "caption": "Cellular diagram comparing normal osmotic water inflow into root hair cells versus reversed osmotic tension locking water in saline soil, causing cell dehydration and leaf scorching."
                        }
                    },
                    {
                        "type": "mini_activity",
                        "title": "Lab Experiment: Simulating Salinity and Plant Wilting",
                        "content": {
                            "title": "Observing Salt-Induced Physiological Drought",
                            "task": "1. Grow two healthy potted bean seedlings (15 cm tall).\n2. Water Pot A with pure tap water.\n3. Water Pot B with concentrated salt solution (2 tablespoons of table salt in 1 cup of water).\n4. Observe and record leaf turgidity at 2 hours, 6 hours, and 24 hours. Note how Pot B wilts in wet soil.",
                            "materials": ["2 Potted Bean Seedlings", "Table Salt", "Water", "Measuring Cup"],
                            "safety": "Clean workstation after completing the experiment."
                        }
                    }
                ],
                [
                    {
                        "type": "key_takeaway",
                        "title": "Core Summary: Soil Salinity",
                        "content": {
                            "title": "Key Takeaways",
                            "text": "- **Soil salinity** is the toxic accumulation of soluble salts in the root zone.\n- **Osmotic potential reversal** causes 'physiological drought', where crops wilt in wet soil.\n- **High sodium ($Na^+$)** disperses clay aggregates into impervious cement.\n- **Gypsum ($\\text{CaSO}_4$) + fresh water leaching** displaces sodium and restores soil health."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Mechanism of Physiological Drought",
                        "content": {
                            "question": "Why do tomato crops planted in an irrigated greenhouse in Kajiado wilt and develop burnt leaf margins even when the soil is kept continuously soaked with borehole water?",
                            "options": [
                                "The borehole water contains too much dissolved oxygen that rusts the roots",
                                "The borehole water is brackish and saline; high salt concentrations in the soil create high osmotic pressure that prevents roots from absorbing water, inducing physiological drought despite saturated soil",
                                "The greenhouse roof blocks all magnetic fields needed for root suction",
                                "The tomatoes are absorbing salt and converting it into solid table salt crystals inside stems"
                            ],
                            "answer": "B",
                            "explanation": "Brackish borehole water continuously deposits soluble mineral salts into the root zone. As water evaporates in the warm greenhouse, soil solution salinity skyrockets. The high salt concentration reverses the natural osmotic gradient—soil water holds onto moisture with greater chemical force than root cells can pull, causing acute dehydration, wilting, and sodium toxicity (burnt leaf margins) in wet soil."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 9: Organic Matter and Humus
        # =====================================================================
        {
            "unit_order": 9,
            "unit_name": "Organic Matter and Humus",
            "unit_description": "Definition of SOM vs humus, biochemical decomposition pathway, physical benefits (water-holding sponge, structural aggregation), chemical benefits (CEC powerhouse, nutrient release), and biological stimulation.",
            "lesson_title": "Soil Organic Matter and Humus Dynamics",
            "pages": [
                [
                    {
                        "type": "suggested_image",
                        "title": "Rich Decomposed Organic Compost and Humus",
                        "content": {
                            "title": "Rich Decomposed Organic Compost and Humus",
                            "caption": "A pile of dark, crumbly, mature organic compost ready for field application, showing the transformation of organic matter into stable humus."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Organic Matter and Humus",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Differentiate between raw **Soil Organic Matter (SOM)** and fully decomposed **humus**.",
                                "Explain the biological **decomposition process** driven by soil microbes and earthworms.",
                                "Analyze the **triple benefits of humus**: physical water-holding sponge, chemical CEC powerhouse, and biological food web fuel.",
                                "Evaluate management practices that build stable soil organic carbon."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "What is Soil Organic Matter vs Humus?",
                        "content": {
                            "title": "The Living, Dead, and Very Dead Fractions of Soil",
                            "text": "Soil organic material exists in three distinct biological states:\n\n1. **The Living**: Active plant roots, earthworms, beetles, fungi, and billions of soil bacteria.\n2. **The Dead (Fresh SOM)**: Recently added crop residues, fallen leaves, manure, and dead insects undergoing active microbial breakdown.\n3. **The Very Dead (Humus)**: The dark brown, amorphous, highly stable organic substance that remains after complete biological decomposition. Humus resists further rapid decay and remains in the soil for decades."
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "The Triple Benefits of Humus in Agriculture",
                        "content": {
                            "title": "Physical, Chemical, and Biological Transformation",
                            "text": "Humus is the single most valuable amendment a farmer can build in their soil:\n\n### 1. Physical Benefits (The Soil Sponge)\n- **Immense Water Holding**: Humus acts like a giant biological sponge, holding **up to 6 times its dry weight in capillary water**, protecting crops during mid-season dry spells.\n- **Structural Binding**: Secretes humic glues that cement loose sand grains or dense clay into porous crumb aggregates, improving both drainage and aeration.\n\n### 2. Chemical Benefits (The CEC Powerhouse)\n- **Massive CEC**: Possesses a massive negative surface charge (CEC **$100\\text{--}300\\text{ cmol/kg}$**), creating a huge reservoir that holds $\\text{Ca}^{2+}, \\text{Mg}^{2+}, \\text{K}^+$, and $\\text{NH}_4^+$ safely against leaching.\n- **Slow-Release Nutrients**: Mineralizes slowly over seasons, steadily releasing Nitrogen ($N$), Phosphorus ($P$), Sulfur ($S$), and micronutrients.\n\n### 3. Biological Benefits (The Food Web Engine)\n- Serves as the primary carbon and energy substrate for beneficial soil bacteria, mycorrhizal fungi, and earthworms."
                        }
                    },
                    {
                        "type": "comparison_table",
                        "title": "Fresh Organic Matter vs Stable Humus",
                        "content": {
                            "title": "Comparison of Organic Fractions",
                            "headers": ["Characteristic", "Fresh Soil Organic Matter (SOM)", "Stable Humus"],
                            "rows": [
                                ["Physical State", "Identifiable plant/animal tissue (straw, dung)", "Amorphous, dark brown/black colloidal coating"],
                                ["Decomposition Rate", "Rapid (Weeks to months)", "Very Slow (Decades to centuries)"],
                                ["Water-Holding Capacity", "Moderate", "Extreme (Holds 400–600% of dry mass in water)"],
                                ["Cation Exchange Capacity", "Low to Medium (10–30 cmol/kg)", "Massive (100–300 cmol/kg)"],
                                ["Primary Agricultural Role", "Feeds active decomposers; releases fast nitrogen", "Long-term soil structure, moisture, and CEC battery"]
                            ]
                        }
                    }
                ],
                [
                    {
                        "type": "suggested_diagram",
                        "title": "The Triple Benefits of Humus in Soil",
                        "content": {
                            "title": "The Triple Benefits of Humus in Soil",
                            "caption": "Conceptual model illustrating the Physical (water sponge & crumb binding), Chemical (CEC 100-300 cmol/kg & nutrient release), and Biological (microbial fuel) benefits of humus."
                        }
                    },
                    {
                        "type": "step_process",
                        "title": "How Farmers Build and Maintain Soil Humus",
                        "content": {
                            "title": "Agronomic Practices for Humus Accumulation",
                            "steps": [
                                "1. **Apply Well-Rotted Farmyard Compost**: Incorporate 10–20 tonnes/hectare of mature compost annually to infuse stable humic compounds.",
                                "2. **Retain Crop Residues**: Never burn maize stover or wheat straw; chop and leave residues on the surface as protective mulch.",
                                "3. **Grow Leguminous Green Manures**: Plant fast-growing legumes (Mucuna, Desmodium, Sunn hemp) and incorporate biomass at flowering stage.",
                                "4. **Practice Minimum Tillage**: Avoid deep inversion plowing, which exposes buried humus to excess oxygen, causing microbes to burn it off as $CO_2$ gas."
                            ]
                        }
                    }
                ],
                [
                    {
                        "type": "mini_activity",
                        "title": "Lab Experiment: Humus Flotation and Separation Test",
                        "content": {
                            "title": "Separating Humus from Mineral Soil Separates",
                            "task": "1. Take 1 cup of rich, dark forest topsoil and 1 cup of dry sand.\n2. Place them into two separate glass jars filled with water and stir vigorously for 1 minute.\n3. Allow the jars to settle for 15 minutes.\n4. Observe: Sand settles instantly to the bottom. In the forest soil, dense sand and silt form lower layers, while dark, spongy organic humus floats on top and suspends in the water, demonstrating low density and high colloidal nature.",
                            "materials": ["2 Glass Jars", "Water", "Forest Topsoil Sample", "Sand Sample", "Stirring Rod"],
                            "safety": "Clean and dry glass jars after the experiment."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Core Summary: Organic Matter and Humus",
                        "content": {
                            "title": "Key Takeaways",
                            "text": "- **Humus** is the stable, dark brown colloidal residue of complete organic decomposition.\n- **Physically**, humus holds 6x its weight in water and binds mineral particles into crumbs.\n- **Chemically**, humus boasts a massive CEC ($100\\text{--}300\\text{ cmol/kg}$) that prevents fertilizer leaching.\n- **Never burn crop residues**; retain organic mulch to continuously replenish humus."
                        }
                    }
                ],
                [
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Triple Benefits of Humus",
                        "content": {
                            "question": "Which of the following statements best explains why adding compost manure to a sandy soil simultaneously solves issues of drought vulnerability and fertilizer leaching?",
                            "options": [
                                "Compost manure turns sandy grains into waterproof plastic sheets",
                                "Compost decomposes into humus, which acts like a physical sponge holding up to 6 times its weight in water while providing a massive negative electrical charge (high CEC) that binds nutrient cations against leaching",
                                "Compost poisons soil microbes, preventing them from consuming fertilizer",
                                "Compost causes the sun to shine less intensely on the field"
                            ],
                            "answer": "B",
                            "explanation": "Sandy soils suffer from dual defects: low water-holding capacity (macro-pores drain water) and low CEC (quartz sand lacks negative charges, causing fertilizer leaching). Adding compost creates humus, which physically stores immense capillary moisture like a sponge while chemically providing a high Cation Exchange Capacity (100–300 cmol/kg) that magnetically holds onto dissolved fertilizer cations (Ca²⁺, Mg²⁺, K⁺, NH₄⁺)."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 10: Soil Organisms
        # =====================================================================
        {
            "unit_order": 10,
            "unit_name": "Soil Organisms",
            "unit_description": "Macro-organisms vs micro-organisms, earthworm burrowing dynamics and nutrient-rich castings, symbiotic Rhizobium nitrogen fixation, Mycorrhizal fungal networks, and living soil conservation.",
            "lesson_title": "Soil Organisms and the Biological Food Web",
            "pages": [
                [
                    {
                        "type": "suggested_image",
                        "title": "Earthworm Burrows in a Soil Column",
                        "content": {
                            "title": "Earthworm Burrows in a Soil Column",
                            "caption": "Cross-sectional soil column showing extensive earthworm macro-burrows that serve as highways for plant root expansion, water infiltration, and air circulation."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Soil Organisms",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Categorize soil organisms into **macro-organisms** (earthworms, termites) and **micro-organisms** (bacteria, fungi, actinomycetes).",
                                "Explain how **earthworm castings and burrows** dramatically enhance soil porosity, drainage, and nutrient availability.",
                                "Analyze symbiotic **$\\text{N}_2$ fixation by $\\textit{Rhizobium}$ bacteria** in legume nodules and **Mycorrhizal fungal nutrient absorption**.",
                                "Formulate farm management protocols that foster active soil biodiversity."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The Living Soil Ecosystem",
                        "content": {
                            "title": "Billions of Organisms Beneath Our Feet",
                            "text": "Soil is not dead, inert dirt; it is a complex, living biological universe. A single teaspoon of healthy agricultural topsoil contains **more living microorganisms than there are humans on planet earth**!\n\n- These organisms form the **soil biological food web**, driving the decomposition of organic matter, recycling essential plant nutrients, synthesizing humic glues, and protecting crop roots from soil-borne diseases."
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "Macro-Organisms: Earthworms as Nature's Plow",
                        "content": {
                            "title": "Ecosystem Engineers of Agricultural Land",
                            "text": "### 1. Earthworms (*Lumbricus terrestris*)\n- **Nutrient-Rich Castings**: Earthworms ingest soil particles and organic debris, macerating them in their digestive tracts with calcium enzymes. Their excreted **castings** contain **5x more available Nitrogen, 7x more available Phosphorus, and 11x more Potassium** than the surrounding soil!\n- **Bio-Tillage Highways**: Earthworm burrow tunnels create permanent vertical macro-pores that increase water infiltration rates up to tenfold and serve as frictionless pathways for crop root growth.\n\n### 2. Termites & Beetles\n- Shred coarse woody biomass and harvest deep mineral subsoil, enriching surface layers with clay and organic matter in tropical soils."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Micro-Organisms: Symbiotic Fungi and Bacteria",
                        "content": {
                            "title": "Microscopic Partners in Plant Nutrition",
                            "text": "### 1. Nitrogen-Fixing Bacteria (*Rhizobium*)\n- Form symbiotic root nodules on leguminous crops (beans, cowpeas, desmodium, lucerne).\n- Extract inert atmospheric nitrogen gas ($N_2$) from soil air pores and convert it directly into ammonium ($NH_4^+$) for the host plant, fixing **100 to 200 kg of free Nitrogen per hectare annually**.\n\n### 2. Mycorrhizal Fungi (VAM)\n- Microscopic fungal threads (hyphae) form a symbiotic web extending from crop roots.\n- Hyphae extend root surface area by up to 1000%, dissolving insoluble phosphorus and pumping water to the crop during droughts in exchange for plant photosynthate sugars."
                        }
                    }
                ],
                [
                    {
                        "type": "comparison_table",
                        "title": "Beneficial vs Harmful Soil Organisms",
                        "content": {
                            "title": "Soil Biological Agents Matrix",
                            "headers": ["Organism Group", "Ecological Role", "Primary Agricultural Benefit", "Management Practices to Encourage"],
                            "rows": [
                                ["Earthworms", "Macro-decomposer & burrower", "Produces nutrient-dense castings & aeration channels", "Apply organic mulch, avoid toxic nematicides, zero tillage"],
                                ["*Rhizobium* Bacteria", "Symbiotic nitrogen fixers in legumes", "Fixes 100–200 kg N/ha annually without fertilizer cost", "Inoculate seeds with bio-fertilizers; maintain soil pH > 6.0"],
                                ["Mycorrhizal Fungi", "Symbiotic root extensions", "Pumps phosphorus and water from micro-pores", "Reduce chemical fungicide sprays; avoid excessive tillage"],
                                ["Root-Knot Nematodes", "Microscopic parasitic roundworms", "Harmful: Galls roots, blocks water flow, stunts crops", "Practice crop rotation with marigolds (*Tagetes*); apply compost"]
                            ]
                        }
                    },
                    {
                        "type": "suggested_video",
                        "title": "The Living Soil: Microbes and Farming",
                        "content": {
                            "title": "The Living Soil: Microbes and Farming",
                            "description": "Explores how billions of microscopic bacteria, mycorrhizal fungal hyphae, and earthworms create soil crumb structure and cycle natural nutrients.",
                            "url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
                        }
                    }
                ],
                [
                    {
                        "type": "mini_activity",
                        "title": "Field Practical: Earthworm Population Density Audit",
                        "content": {
                            "title": "Measuring Biological Activity in Farm Soils",
                            "task": "1. Demarcate a $30\\text{ cm} \\times 30\\text{ cm}$ square in an undisturbed, shaded mulch plot under trees.\n2. Carefully excavate the top $15\\text{ cm}$ of soil onto a plastic sheet and count all active earthworms.\n3. Repeat the exact test on a bare, continuously tilled, chemically sprayed field.\n4. Compare worm counts and explain how soil temperature, moisture, and chemical management dictate biological life.",
                            "materials": ["Quadrat Frame / Ruler", "Trowel", "Plastic Sheet", "Notepad"],
                            "safety": "Handle earthworms gently and return them safely to moist soil after counting."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Core Summary: Soil Organisms",
                        "content": {
                            "title": "Key Takeaways",
                            "text": "- **Earthworm castings** are 5–11x richer in N, P, and K than surrounding topsoil.\n- **Earthworm burrows** provide essential vertical drainage and root highways.\n- ***Rhizobium* bacteria** fix up to 200 kg of free atmospheric nitrogen per hectare.\n- **Mycorrhizal fungi** expand root surface area by up to 1000% to harvest phosphorus."
                        }
                    }
                ],
                [
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Biological Nitrogen Fixation",
                        "content": {
                            "question": "A smallholder bean farmer inoculates certified bean seeds with Rhizobium bio-inoculant before planting in a field with pH 6.2. What direct agronomic and economic benefit will this biological practice deliver?",
                            "options": [
                                "The Rhizobium bacteria will physically consume destructive cutworms in the soil",
                                "The symbiotic bacteria will convert inert atmospheric nitrogen gas into plant-available ammonium inside root nodules, dramatically boosting bean yield while cutting synthetic fertilizer expenses",
                                "The bacteria will turn the bean leaves into waterproof solar panels",
                                "The Rhizobium will dissolve all rocks into liquid nitrogen"
                            ],
                            "answer": "B",
                            "explanation": "*Rhizobium* bacteria form a symbiotic relationship with legume roots. They infect root hairs to form nodules where the enzyme nitrogenase converts atmospheric nitrogen gas ($N_2$) into ammonium ($NH_4^+$) that the bean plant uses for protein synthesis. In exchange, the plant provides carbohydrates. This provides free, natural nitrogen, increasing crop yields and saving the farmer significant money on expensive chemical fertilizers."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 11: Soil Profile and Crop Production
        # =====================================================================
        {
            "unit_order": 11,
            "unit_name": "Soil Profile and Crop Production",
            "unit_description": "Definition of soil profile, master horizons (O, A, E, B, C, R), morphological and chemical characteristics per layer, rooting depth restrictions (hardpans, bedrock), and nutrient pumping.",
            "lesson_title": "Soil Profile Horizons and Root Zone Dynamics",
            "pages": [
                [
                    {
                        "type": "suggested_image",
                        "title": "Vertical Soil Profile Horizons in an Excavated Soil Pit",
                        "content": {
                            "title": "Vertical Soil Profile Horizons in an Excavated Soil Pit",
                            "caption": "A deep soil pit showing clear vertical stratigraphic horizons from dark organic topsoil down through the argillic B subsoil to weathered parent bedrock."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Soil Profile",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Define a **soil profile** as a vertical section exposing master horizons (**O, A, E, B, C, R**).",
                                "Describe the unique physical, chemical, and biological properties of each soil horizon.",
                                "Analyze how the depth and density of horizons govern **root penetration, drainage, and water storage**.",
                                "Explain how deep-rooted agroforestry trees act as **'nutrient pumps'** across horizons."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "What is a Soil Profile?",
                        "content": {
                            "title": "The Vertical Stratigraphy of Agricultural Land",
                            "text": "A **soil profile** is a vertical cross-section through the earth's crust, extending from the soil surface down to the solid unweathered bedrock. Over centuries of pedogenesis (soil formation), distinct horizontal layers develop, known as **soil horizons**.\n\n- Examining a soil profile in a test pit allows a farmer to evaluate soil depth, subsoil drainage barriers, and effective rooting volume before investing capital in perennial orchards or tea estates."
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "The Master Horizons of a Soil Profile",
                        "content": {
                            "title": "O, A, E, B, C, and R Horizons Explained",
                            "text": "A mature, fully weathered soil profile consists of six master horizons:\n\n### 1. O Horizon (Organic Surface Layer)\n- Freshly fallen leaves, crop residues, and partially decomposed dark organic litter.\n\n### 2. A Horizon (Topsoil / Zone of Highest Fertility)\n- Mineral layer enriched with dark humus, active earthworms, and high biological activity. The primary feeding zone for crop roots.\n\n### 3. E Horizon (Eluviation / Leaching Layer)\n- Light-colored, sandy layer where clay, iron oxides, and nutrients have been washed downward by percolating rainwater.\n\n### 4. B Horizon (Subsoil / Illuviation Layer)\n- Zone of accumulation. Leached clay, iron, and aluminum from above accumulate here, making it denser, clay-heavy, and lighter in color than topsoil.\n\n### 5. C Horizon (Substratum / Weathered Parent Rock)\n- Partially broken rock fragments with zero organic matter or ped structural aggregation.\n\n### 6. R Horizon (Bedrock)\n- Solid, unweathered parent bedrock (e.g. granite, basalt, volcanic tuff) at the base."
                        }
                    },
                    {
                        "type": "comparison_table",
                        "title": "Master Soil Horizons Comparison",
                        "content": {
                            "title": "Soil Horizon Profile Matrix",
                            "headers": ["Horizon", "Designation", "Physical & Chemical Properties", "Biological & Agronomic Role"],
                            "rows": [
                                ["O Horizon", "Organic Litter", "Dark, undecomposed and fermenting leaves/twigs", "Protects soil from raindrop impact; feeds decomposers"],
                                ["A Horizon", "Topsoil", "Dark brown crumbly loam, rich in humus & nitrogen", "Primary root zone; highest nutrient uptake and aeration"],
                                ["E Horizon", "Eluviated Layer", "Bleached, light-colored sand; heavily leached", "Low nutrient retention; common in acidic forest soils"],
                                ["B Horizon", "Subsoil (Accumulation)", "Dense clay/iron accumulation, reddish or blocky", "Moisture reservoir; deep root anchor for perennial trees"],
                                ["C Horizon", "Parent Material", "Weathered rock fragments, low fertility", "Source of new mineral parent material via weathering"],
                                ["R Horizon", "Bedrock", "Solid continuous impervious rock layer", "Physical barrier limiting maximum possible rooting depth"]
                            ]
                        }
                    }
                ],
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Vertical Soil Profile Horizons (O, A, E, B, C, R)",
                        "content": {
                            "title": "Vertical Soil Profile Horizons (O, A, E, B, C, R)",
                            "caption": "Stratigraphic engineering diagram showing the vertical progression from O organic litter, A dark topsoil, E leached sand, B dense clay subsoil, C weathered rock, down to solid R bedrock."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Profile Depth and Crop Rooting Dynamics",
                        "content": {
                            "title": "Matching Horizon Depth to Enterprise Physiology",
                            "text": "The depth and physical condition of soil horizons dictate crop success:\n\n- **Deep Soils ($>1.5\\text{ m}$ to Bedrock)**: Essential for deep taproot perennials (coffee, tea, macadamia, citrus, fruit trees). Deep roots tap subsoil moisture reserves during droughts and anchor large tree canopies against heavy winds.\n- **Shallow Soils ($<0.3\\text{ m}$ to Bedrock or Hardpan)**: Restrict root expansion; trees fall over in storms and annual crops dry up rapidly. Suited only for shallow-rooted pasture grasses or short-season vegetables.\n- **Claypan in B Horizon**: If the B horizon is an impermeable claypan, rainwater ponds in the A horizon, rotting crop roots."
                        }
                    }
                ],
                [
                    {
                        "type": "mini_activity",
                        "title": "Field Investigation: Examining a Real Soil Profile",
                        "content": {
                            "title": "Soil Profile Pit Observation",
                            "task": "Visit a clean road cutting, quarry edge, or freshly dug foundation pit on or near the school compound:\n\n1. Measure the exact thickness (in cm) of the dark A horizon topsoil versus the lighter B horizon subsoil using a measuring tape.\n2. Note the maximum depth of visible crop and weed roots.\n3. Feel the soil texture of the A horizon versus the B horizon and record the differences in clay content and structural hardness.",
                            "materials": ["Measuring Tape", "Geological Trowel / Knife", "Notepad", "Digital Camera"],
                            "safety": "Never stand beneath unstable, overhanging soil cliffs or deep unsupported trenches."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Core Summary: Soil Profile",
                        "content": {
                            "title": "Key Takeaways",
                            "text": "- **Soil profile** exposes the master horizons: O (litter), A (topsoil), E (leached), B (subsoil), C (parent rock), R (bedrock).\n- **A horizon** is the primary biological and nutrient feeding zone for crops.\n- **Deep profiles (>1.5m)** are mandatory for perennial fruit orchards, coffee, and tea.\n- **Deep tree roots act as nutrient pumps**, pulling minerals from the B horizon to the topsoil."
                        }
                    }
                ],
                [
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Profile Depth for Commercial Macadamia",
                        "content": {
                            "question": "A farmer intends to plant a commercial orchard of 500 macadamia nut trees, which develop a 2-meter deep taproot system and require excellent drainage. Digging test pits reveals solid granite bedrock (R horizon) at a depth of only 25 cm across the property. Why is this land unsuitable for macadamia trees?",
                            "options": [
                                "Macadamia nuts will grow underground and smash into the granite rock",
                                "The shallow bedrock (25 cm) will physically block taproot expansion, causing the heavy trees to topple during storms, while restricting moisture storage and causing fatal waterlogging during rains",
                                "Granite bedrock emits radio waves that prevent macadamia flowering",
                                "Macadamia trees require a solid bedrock at 5 cm depth to anchor properly"
                            ],
                            "answer": "B",
                            "explanation": "Macadamia trees develop extensive, deep taproots extending 1.5 to 2.5 meters deep to anchor large woody canopies and access subsoil moisture during dry spells. A shallow soil profile with bedrock at 25 cm severely restricts root depth, causing heavy trees to blow over in windstorms, restricting nutrient access, and causing rapid topsoil saturation and root death during heavy rains."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 12: Importance and Synthesis of Soil Properties
        # =====================================================================
        {
            "unit_order": 12,
            "unit_name": "Importance and Synthesis of Soil Properties",
            "unit_description": "Holistic synthesis of physical, chemical, and biological soil properties; the regenerative interaction loop; integrated soil management plans; crop-soil matching matrix; performance task; and Summative Topic Assessment.",
            "lesson_title": "Synthesis of Soil Properties and Summative Assessment",
            "pages": [
                [
                    {
                        "type": "suggested_image",
                        "title": "Thriving Sustainable Agricultural Crop Field in Kenya",
                        "content": {
                            "title": "Thriving Sustainable Agricultural Crop Field in Kenya",
                            "caption": "A flourishing, highly productive smallholder farm in Kenya demonstrating the integrated management of soil texture, structure, pH, organic matter, and living organisms."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Soil Synthesis & Assessment",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Synthesize how **physical, chemical, and biological soil properties** interact in a continuous living feedback loop.",
                                "Develop an **Integrated Soil Management Plan** that simultaneously builds soil structure, optimizes pH, boosts CEC, and feeds soil biology.",
                                "Execute the **Topic 2 Performance Task**: Formulating a professional Soil Turnaround Brief for a degraded smallholder farm.",
                                "Complete the comprehensive **Summative Topic Assessment** covering all 12 lessons of Topic 2."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The Soil Properties Interaction Loop",
                        "content": {
                            "title": "Physical, Chemical, and Biological Interconnection",
                            "text": "In nature, soil properties never operate in isolation; they form an inseparable, living ecological matrix:\n\n- **Physical drives Chemical & Biological**: A compacted clay soil with low porosity (physical) creates anaerobic conditions that kill beneficial bacteria (biological) and chemically locks up phosphorus (chemical).\n- **Biological drives Physical & Chemical**: Adding organic compost (biological) produces humic glues that bind mineral particles into porous crumb aggregates (physical) while dramatically raising the soil's Cation Exchange Capacity (chemical) to store nutrients.\n- **Chemical drives Biological & Physical**: Neutralizing acidic soil with lime (chemical) stimulates *Rhizobium* bacteria and earthworms (biological), accelerating root growth and crumb formation (physical)."
                        }
                    }
                ],
                [
                    {
                        "type": "comparison_table",
                        "title": "Crop-Soil Compatibility Matrix",
                        "content": {
                            "title": "Matching Commercial Crops to Soil Profiles",
                            "headers": ["Crop Enterprise", "Optimal Soil Texture", "Optimal Soil pH", "Soil Depth & Drainage Requirements", "Key Agronomic Vulnerability"],
                            "rows": [
                                ["Tea (*Camellia sinensis*)", "Deep Clay Loam / Volcanic", "pH 4.5 – 5.5 (Acidic)", "Very deep (>1.5 m), well-drained, high organic matter", "Intolerant to alkalinity and waterlogging"],
                                ["Hybrid Maize", "Fertile Sandy Clay Loam", "pH 6.0 – 7.0 (Neutral)", "Deep (>1.0 m), high crumb structure, balanced NPK", "Severe stunting under acid phosphorus lockup"],
                                ["Paddy Rice", "Heavy Clay / Vertisol", "pH 5.5 – 7.0", "Flat basin, impermeable subsoil to hold flood water", "Cannot tolerate sandy, rapidly draining soils"],
                                ["French Beans / Cabbages", "Rich Humus Loam", "pH 6.0 – 6.8", "Well-drained, high macro-porosity, high CEC", "Highly sensitive to salinity and waterlogging"],
                                ["Drought-Tolerant Sorghum", "Sandy Loam / Loam", "pH 5.5 – 7.5", "Moderate depth (>0.6 m), tolerant to low organic matter", "Tolerates poor soil but yields best on loams"]
                            ]
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "The 4 Pillars of an Integrated Soil Management Plan",
                        "content": {
                            "title": "Master Strategy for Sustainable Agribusiness",
                            "text": "To achieve long-term soil productivity and commercial profitability, every modern farm must implement four core pillars:\n\n1. **Continuous Organic Carbon Renewal**: Add 10–15 tonnes/ha of compost or manure annually to maintain humus levels ($>3.5\\%$) and high CEC.\n2. **Dynamic pH Management**: Test soil every two seasons; apply agricultural lime to acidic fields to maintain the optimal pH 6.0–6.8 window and unlock phosphorus.\n3. **Soil Conservation & Minimum Tillage**: Keep fields protected under organic mulch or cover crops to prevent erosion, preserve crumb structure, and lower surface soil temperatures.\n4. **Biological Stimulation**: Inoculate legumes with *Rhizobium*, eliminate broad-spectrum chemical drenching, and protect earthworm populations."
                        }
                    },
                    {
                        "type": "suggested_video",
                        "title": "Conducting a Soil Textural Feel Test and Field Analysis",
                        "content": {
                            "title": "Conducting a Soil Textural Feel Test and Field Analysis",
                            "description": "Step-by-step practical extension demonstration showing field texture testing, pH testing, and soil health diagnostics for smallholder farmers.",
                            "url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
                        }
                    }
                ],
                [
                    {
                        "type": "mini_activity",
                        "title": "Performance Task: Soil Rehabilitation and Agribusiness Masterplan",
                        "content": {
                            "title": "Consultancy Brief: Turning Around a Degraded Farm",
                            "task": "You are hired as an agricultural consultant for a 4-acre farm with the following laboratory report:\n- *Texture*: Sandy Clay Loam (55% Sand, 20% Silt, 25% Clay)\n- *Structure*: Compacted platy plow pan at 15 cm depth; Bulk Density = 1.68 g/cm³\n- *Chemical*: pH = 4.7 (Strongly Acidic); CEC = 7.5 cmol/kg (Low); Phosphorus = Extremely Low\n- *Biological*: Earthworm count = Zero; Organic Carbon = 0.9%\n\n**Your Deliverable**: Draft a 1-page structured Soil Turnaround Plan detailing specific physical, chemical, and biological remediation steps over two seasons, including crop selection and fertilizer scheduling.",
                            "materials": ["Laboratory Report Handout", "Consultancy Template", "Calculator", "Pen"],
                            "safety": "Ensure realistic, cost-effective recommendations for smallholder farmers."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Core Summary: Integrated Soil Stewardship",
                        "content": {
                            "title": "Key Takeaways",
                            "text": "- **Soil properties form a living trinity**: physical structure, chemical pH/CEC, and biological organisms.\n- **Healthy soil** has low bulk density ($<1.3\\text{ g/cm}^3$), crumb structure, optimal pH ($6.0\\text{--}7.0$), high CEC, and active earthworms.\n- **Regenerative farming** (liming, composting, minimum tillage, legume rotation) guarantees multi-decade agribusiness prosperity."
                        }
                    }
                ],
                # Pages 5 to 8: 8 Summative Assessment MCQs
                [
                    {
                        "type": "knowledge_check",
                        "title": "Summative MCQ 1: Permanent vs Dynamic Soil Properties",
                        "content": {
                            "question": "Which of the following soil properties is considered permanent and cannot be easily modified by standard seasonal farming operations?",
                            "options": [
                                "Soil organic matter content",
                                "Soil structure (peds and aggregates)",
                                "Soil texture (relative proportions of sand, silt, and clay)",
                                "Soil pH and nutrient concentrations"
                            ],
                            "answer": "C",
                            "explanation": "Soil texture is a permanent physical property determined by parent rock weathering over thousands of years. While a farmer can easily alter soil fertility, structure, organic matter, and pH within seasons through liming, tillage, and composting, the percentage of sand, silt, and clay in an open field remains permanent."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Summative MCQ 2: Particle Size Boundaries (USDA)",
                        "content": {
                            "question": "According to the USDA soil classification system, which particle diameter range correctly identifies silt particles?",
                            "options": [
                                "Greater than 2.0 mm",
                                "0.05 mm to 2.0 mm",
                                "0.002 mm to 0.05 mm",
                                "Less than 0.002 mm"
                            ],
                            "answer": "C",
                            "explanation": "The USDA classifies mineral separates as: Sand = 0.05 mm to 2.0 mm; Silt = 0.002 mm to 0.05 mm; and Clay = less than 0.002 mm."
                        }
                    }
                ],
                [
                    {
                        "type": "knowledge_check",
                        "title": "Summative MCQ 3: Agronomic Superiority of Crumbly Soil Structure",
                        "content": {
                            "question": "Why is a crumbly soil structure considered the ideal physical condition for cultivating commercial crops?",
                            "options": [
                                "Crumbly structure creates solid horizontal plates that block all water infiltration",
                                "Crumbly peds provide high internal porosity, offering an optimal 50:50 balance of macro-pores (for drainage and aeration) and micro-pores (for capillary water storage) while allowing frictionless root elongation",
                                "Crumbly soil dissolves into liquid mud during rainfall, preventing weed emergence",
                                "Crumbly soil repels all beneficial soil bacteria and earthworms"
                            ],
                            "answer": "B",
                            "explanation": "Crumbly soil structure consists of small, porous, rounded aggregates that create an interconnected network of macro-pores (facilitating air exchange and rapid drainage) and micro-pores (retaining capillary water), while minimizing physical resistance for expanding young crop roots."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Summative MCQ 4: Interpreting High Soil Bulk Density",
                        "content": {
                            "question": "A laboratory soil core test reveals a bulk density of 1.72 g/cm³ in a commercial field. What physical condition does this indicate, and what is the primary agronomic consequence?",
                            "options": [
                                "The soil has high organic matter and will produce record yields",
                                "The soil suffers from severe compaction, where macro-pores have been crushed, physically restricting root growth and causing high surface runoff and erosion",
                                "The soil contains zero mineral particles and is composed entirely of water",
                                "The soil has high aeration and requires heavy rolling machinery"
                            ],
                            "answer": "B",
                            "explanation": "A bulk density above 1.60 g/cm³ indicates severe compaction. Compaction crushes macro-pore spaces, reducing total porosity below 35%. This creates high physical resistance that halts root elongation, restricts oxygen diffusion, and blocks water infiltration, triggering heavy surface runoff and erosion."
                        }
                    }
                ],
                [
                    {
                        "type": "knowledge_check",
                        "title": "Summative MCQ 5: Diagnosing Reduced Gleyed Soil Color",
                        "content": {
                            "question": "What does a solid dull grey or bluish-grey color (gleying) in the subsoil indicate about the soil's internal environmental condition?",
                            "options": [
                                "The soil is rich in oxidized ferric iron (Fe³⁺) and has excellent drainage",
                                "The soil suffers from chronic waterlogging and prolonged anaerobic conditions, causing iron to be chemically reduced to its soluble ferrous (Fe²⁺) state",
                                "The soil was treated with high concentrations of white agricultural lime",
                                "The soil contains abundant organic humus that turned grey in sunlight"
                            ],
                            "answer": "B",
                            "explanation": "Gleying (dull grey or pale bluish color) occurs under saturated, waterlogged conditions where oxygen is absent. Anaerobic microorganisms reduce ferric iron ($Fe^{3+}$) to ferrous iron ($Fe^{2+}$), stripping the red/orange iron pigments and leaving a dull grey mineral matrix that indicates chronic waterlogging."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Summative MCQ 6: Biochemical Mechanism of Phosphorus Fixation",
                        "content": {
                            "question": "Why does applying Diammonium Phosphate (DAP) fertilizer to strongly acidic soils (pH 4.5) fail to improve stunted maize crops?",
                            "options": [
                                "At pH 4.5, soluble aluminum (Al³⁺) and iron (Fe³⁺) react with applied phosphate to form insoluble precipitates that crop roots cannot absorb",
                                "Acidic soil causes phosphate to transform into gaseous chlorine",
                                "Maize roots refuse to absorb phosphorus unless the soil is at pH 12.0",
                                "Earthworms consume all phosphate molecules before roots reach them"
                            ],
                            "answer": "A",
                            "explanation": "In strongly acidic soils ($pH < 5.0$), high concentrations of soluble Aluminum ($Al^{3+}$) and Iron ($Fe^{3+}$) chemically react with phosphate ions ($H_2PO_4^-$), precipitating out as insoluble Aluminum and Iron Phosphates (Phosphorus Fixation). Applying agricultural lime to raise pH above 6.0 is essential to unlock phosphorus."
                        }
                    }
                ],
                [
                    {
                        "type": "knowledge_check",
                        "title": "Summative MCQ 7: Cation Exchange Capacity in Sandy vs Humus Soils",
                        "content": {
                            "question": "How does incorporating 15 tonnes of organic compost manure into a coarse sandy soil directly improve its Cation Exchange Capacity (CEC)?",
                            "options": [
                                "Compost turns sand into solid rock with zero pores",
                                "Compost decays into humus, which carries a massive negative electrical surface charge (CEC 100–300 cmol/kg), providing microscopic magnetic sites that bind positive nutrient cations (Ca²⁺, Mg²⁺, K⁺, NH₄⁺) against leaching",
                                "Compost increases the speed at which rainwater leaches fertilizers into rivers",
                                "Compost neutralizes all electrical charges in the universe"
                            ],
                            "answer": "B",
                            "explanation": "Humus is colloidal and possesses an exceptionally high negative electrical surface charge, giving it a CEC of 100 to 300 cmol/kg. Adding compost to low-CEC sand introduces billions of negatively charged binding sites that electrostatically attract and hold positively charged nutrient cations, preventing leaching."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Summative MCQ 8: Reclaiming Saline-Sodic Agricultural Land",
                        "content": {
                            "question": "What is the mandatory scientific chemical step required before flushing a saline-sodic soil with fresh leaching water?",
                            "options": [
                                "Apply concentrated sulfuric acid to dissolve all crop roots",
                                "Apply agricultural gypsum (Calcium Sulfate - CaSO₄) so that Calcium ions (Ca²⁺) displace toxic Sodium ions (Na⁺) from clay surfaces, allowing the sodium to be washed away as soluble sodium sulfate without destroying soil structure",
                                "Apply pure table salt (NaCl) to equalize soil salinity",
                                "Plow the field with heavy tractors when wet to seal the surface"
                            ],
                            "answer": "B",
                            "explanation": "Applying fresh water alone to a sodic soil causes clay particles to disperse and seal the soil into an impervious crust. Applying gypsum ($CaSO_4$) introduces Calcium ($Ca^{2+}$) to displace exchangeable Sodium ($Na^+$) from clay colloids. The displaced sodium forms soluble Sodium Sulfate ($Na_2SO_4$), which is easily leached away by fresh water while Calcium preserves porous crumb structure."
                        }
                    }
                ],
                # Page 9: Topic 2 Capstone Summary & Takeaway
                [
                    {
                        "type": "summary",
                        "title": "Topic 2 Capstone Summary: Properties of Soil Mastery",
                        "content": {
                            "title": "Mastery Overview: Grade 10 Properties of Soil",
                            "text": "Congratulations on completing **Topic 2: Properties of Soil**!\n\nYou have mastered:\n- **Physical Properties**: Permanent soil texture (sand, silt, clay, USDA triangle), crumbly vs platy structure, bulk density ($<1.3\\text{ g/cm}^3$), and diagnostic soil colors.\n- **Chemical Properties**: Soil pH management (lime vs sulfur), phosphorus fixation dynamics, Cation Exchange Capacity (colloidal negative charges), and saline soil reclamation with gypsum.\n- **Biological Properties**: Humus as a physical sponge and CEC powerhouse; earthworm castings and burrows; symbiotic *Rhizobium* $N_2$ fixation; and mycorrhizal fungi.\n- **Soil Profiles**: Master horizons (O, A, E, B, C, R) and root zone depth requirements for agribusiness crops.\n- **Integrated Stewardship**: Designing holistic soil management plans that combine liming, composting, minimum tillage, and crop rotation."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Topic 2 Final Takeaway",
                        "content": {
                            "title": "The Agronomist's Golden Law of Soil",
                            "text": "Feed the soil, and the soil will feed the crop. Protect its structure, balance its chemistry with lime and organic matter, foster its living biology, and the land will reward you with boundless, sustainable harvests."
                        }
                    }
                ]
            ]
        }
    ]

@transaction.atomic
def ingest_grade10_topic2(replace=False):
    """Executes the complete production ingestion of Grade 10 Agriculture Topic 2: Properties of Soil."""
    print("=" * 80)
    print("STARTING INGESTION: CBC Grade 10 Agriculture — Topic 2: Properties of Soil")
    print("=" * 80)

    curriculum = Curriculum.objects.filter(name__iexact="CBC").first()
    grade = Grade.objects.filter(curriculum=curriculum, name__icontains="10").first()
    subject = Subject.objects.filter(grade=grade, name__iexact="Agriculture").first()

    assert curriculum and grade and subject, "Curriculum/Grade/Subject not found!"

    topic_name = "Properties of Soil"
    topic = Topic.objects.filter(subject=subject, name=topic_name).first()
    if not topic:
        topic = Topic.objects.create(
            subject=subject,
            name=topic_name,
            description="Comprehensive theoretical and practical scientific study of soil physical, chemical, and biological properties, soil profile horizons, and integrated soil management.",
            order=2
        )
        print(f"Created Topic 2: {topic.name} (ID: {topic.id})")
    else:
        topic.order = 2
        topic.description = "Comprehensive theoretical and practical scientific study of soil physical, chemical, and biological properties, soil profile horizons, and integrated soil management."
        topic.save()
        print(f"Resolved Topic 2: {topic.name} (ID: {topic.id})")

    if replace:
        print("Flag --replace active: Clearing existing LearningUnits and Lessons for Topic 2...")
        topic.learning_units.all().delete()
        topic.lessons.all().delete()

    curriculum_data = build_topic2_curriculum()
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
                    "topic_order": 2,
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
                    block_id=f"g10_agri_t2_u{u_order}_p{page_idx}_b{comp_idx}",
                    block_type=b_type,
                    component_type=b_type,
                    title=b_title,
                    content=b_content,
                    order=block_order_counter,
                    page_number=page_idx,
                    component_order=comp_idx,
                    page_title=b_title if comp_idx == 1 else None,
                    metadata={"topic_order": 2, "unit_order": u_order, "page": page_idx}
                )
                block_order_counter += 1
                total_blocks += 1

        print(f"  Ingested Unit {u_order}: {u_name} -> Lesson '{l_title}' ({len(pages)} Pages, {block_order_counter - 1} Blocks)")

    print("=" * 80)
    print(f"INGESTION COMPLETE: Topic 2 '{topic.name}'")
    print(f"  Total Units:   {total_units}")
    print(f"  Total Lessons: {total_lessons}")
    print(f"  Total Pages:   {total_pages}")
    print(f"  Total Blocks:  {total_blocks}")
    print("=" * 80)

if __name__ == "__main__":
    replace_flag = "--replace" in sys.argv
    ingest_grade10_topic2(replace=replace_flag)
