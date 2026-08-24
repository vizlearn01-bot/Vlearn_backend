"""
VLearn CBC Grade 8 Home Science — Topic 4: Caring for the Family
Production Ingestion Engine (Phase 1: Content & Card Architecture)

Curriculum: CBC (Curriculum ID: 5)
Grade: Grade 8 (Level: 8)
Subject: Home Science (ID: 28)
Topic: Caring for the Family (Topic Order: 4)

Decomposed into 7 Learning Units & 7 Published Lessons (56 Total Structured Pages):
  1. Childcare & Prenatal Development (8 Pages)
  2. Providing Family Shelter (8 Pages)
  3. Room & Area Interrelationship (8 Pages)
  4. The Kitchen & The Work Triangle (8 Pages)
  5. Cleaning the Kitchen & Surface Care (8 Pages)
  6. Colour in the Home & Interior Decoration (8 Pages)
  7. Soft Furnishings & Home Crafts (8 Pages)

Features:
  - Standard markdown bullet lists (- ) with proper spacing
  - Bold key terms, concepts, and structured tables
  - Step processes, diagnostic audits, and scenario checks

Usage:
  ./venv/bin/python curriculum/ingest_cbc_grade8_home_science_topic4.py [--replace]
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
    text = re.sub(r'\[(?:\d+|image_\d+|S\d+.*?|[\d,\s]+)\]', '', text)
    # Convert unicode bullets to markdown list items
    text = re.sub(r'^[ \t]*[•\u2022][ \t]*', '- ', text, flags=re.MULTILINE)
    text = re.sub(r'([^\n])[ \t]+[•\u2022][ \t]+', r'\1\n- ', text)
    text = re.sub(r'^([^\n\-\*\d\>#][^\n]*)\n(- |\* )', r'\1\n\n$2', text, flags=re.MULTILINE)
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
    """Returns the comprehensive pedagogical page and block structure for Topic 4: Caring for the Family."""
    return [
        # =====================================================================
        # LESSON 1: Childcare & Prenatal Development
        # =====================================================================
        {
            "unit_order": 1,
            "unit_name": "Childcare & Prenatal Development",
            "unit_description": "Conception to birth stages (Germinal, Embryonic, Fetal), physiological & psychological needs of expectant parents, analyzing traditional beliefs and taboos, baby layette selection, gentle laundering, and sterile storage.",
            "lesson_title": "Childcare & Prenatal Development",
            "pages": [
                # Page 1: Topic Introduction & Visual Hook
                [
                    {
                        "type": "suggested_image",
                        "title": "The 9-Month Invisible Journey",
                        "content": {
                            "title": "The 9-Month Invisible Journey",
                            "caption": "A peacefully resting newborn baby representing the culmination of healthy prenatal care and nurturing family support."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Learning Objectives: Childcare & Prenatal Development",
                        "content": {
                            "title": "What We Will Learn Today",
                            "goals": [
                                "Describe human prenatal development through the **Germinal**, **Embryonic**, and **Fetal** stages.",
                                "Analyze the physiological and emotional needs of **expectant mothers** and **expectant fathers**.",
                                "Scientifically critique **traditional pregnancy taboos** and substitute them with evidence-based nutrition.",
                                "Select, launder, and safely store a newborn baby's **layette** to prevent skin irritation."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The Beginning of Human Life",
                        "content": {
                            "title": "From Conception to Birth",
                            "text": "Every human life begins when a sperm cell unites with an ovum during **conception** to form a single-celled **zygote**.\n\nOver nine months, development progresses through three distinct scientific phases:\n\n- **1. Germinal Stage (Weeks 1–2)**: Rapid cell division and travel down the fallopian tube to implant into the uterine wall.\n- **2. Embryonic Stage (Weeks 3–8)**: The critical organogenesis phase where the heart, brain, spine, arms, and legs form. Highly vulnerable to toxins!\n- **3. Fetal Stage (Week 9 to Birth)**: Rapid physical growth, brain maturation, lung development, and reflex coordination."
                        }
                    }
                ],
                # Page 2: Holistic Needs of Expectant Parents
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Prenatal Growth Stages and Parents' Holistic Needs",
                        "content": {
                            "title": "Prenatal Growth Stages and Parents' Holistic Needs",
                            "caption": "Comparative infographic displaying the 3 prenatal stages alongside maternal physiological needs and paternal psychological/financial support."
                        }
                    },
                    {
                        "type": "comparison_table",
                        "title": "Needs of Expectant Mothers vs. Expectant Fathers",
                        "content": {
                            "title": "Balancing Maternal and Paternal Care",
                            "headers": ["Care Category", "Expectant Mother's Needs", "Expectant Father's Needs"],
                            "rows": [
                                ["Nutritional / Physical", "Iron, folic acid, calcium,Sukuma wiki, eggs, clean water, and 8+ hours of sleep", "Taking over heavy physical tasks (fetching water, splitting firewood) to protect mother"],
                                ["Clothing & Comfort", "Loose, breathable cotton dresses, flat comfortable walking shoes (no high heels)", "Creating a calm, comfortable, and well-ventilated home environment"],
                                ["Medical & Clinical", "Attending at least 4 Antenatal Clinic (ANC) visits for blood pressure and fetal monitoring", "Accompanying the mother to clinics, understanding danger signs, and organizing transport"],
                                ["Psychological & Financial", "Emotional reassurance, reduction of anxiety, family love, and stress relief", "Emotional adaptation, parenting counseling, and setting up emergency birth savings"]
                            ]
                        }
                    }
                ],
                # Page 3: Traditional Beliefs vs. Scientific Truth
                [
                    {
                        "type": "comparison_table",
                        "title": "Scientific Analysis of Traditional Pregnancy Taboos",
                        "content": {
                            "title": "Separating Cultural Myths from Biological Facts",
                            "headers": ["Traditional Taboo / Myth", "Cultural Belief", "Scientific & Biological Reality", "Evidence-Based Advice"],
                            "rows": [
                                ["No Eggs or Organ Meat", "Belief that baby will be born bald or with speech defects", "Eggs and liver provide essential **complete protein**, **choline** for brain development, and **iron**", "Expectant mothers should eat cooked eggs and liver regularly to prevent anemia"],
                                ["No High-Protein Beans", "Belief that beans make the fetus grow too large for delivery", "Legumes supply **folate** and dietary fibre preventing neural tube defects and constipation", "Eat balanced portions of beans, peas, and lentils alongside vegetables"],
                                ["Do Not Look at Monkeys", "Belief that the baby will inherit animal facial features", "Physical appearance is determined strictly by **inherited DNA genetics**, not vision", "Disregard superstition; focus on maternal stress reduction and happiness"],
                                ["Avoiding Heavy Farm Labor", "Traditional rule excusing pregnant women from lifting logs", "Heavy strain can cause uterine bleeding and premature placental abruption", "**Beneficial practice!** Light walking is healthy; heavy lifting must be avoided"]
                            ]
                        }
                    },
                    {
                        "type": "callout",
                        "title": "Cultural Wisdom Rule",
                        "content": {
                            "title": "Preserve the Good, Discard the Harmful",
                            "text": "Not all traditional practices were bad! Beneficial practices like family assistance, rest periods, and warm baths should be celebrated, while restrictive food taboos that starve mothers of protein must be rejected."
                        }
                    }
                ],
                # Page 4: Baby Layette Selection & Gentle Laundering
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Baby Layette Wardrobe and The 5-Step Gentle Laundering Routine",
                        "content": {
                            "title": "Baby Layette Wardrobe and The 5-Step Gentle Laundering Routine",
                            "caption": "Wardrobe displaying safe cotton vests, mittens, blankets, and nappies next to a sterile 5-step laundering cycle."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Caring for the Newborn's Skin",
                        "content": {
                            "title": "The 5 Golden Rules of Layette Laundering",
                            "text": "A newborn baby's skin is ultra-delicate and lacks adult immune defenses. Follow these 5 laundering steps:\n\n- **1. Separate Wash**: Always wash baby clothes separately from adult garments to avoid cross-infection.\n- **2. Mild Bar Soap Only**: Use non-perfumed, mild bar soap or baby soap flakes. Never use harsh powder detergents or bleach!\n- **3. Triple Clean Rinse**: Rinse at least 3 to 4 times in clean soft water until the water is 100% clear with zero soap bubbles.\n- **4. Direct Solar UV Disinfection**: Hang clothes in bright sunlight—natural UV light kills microscopic bacteria and mold.\n- **5. Hot Iron & Clean Storage**: Iron with a warm iron to destroy remaining pathogens, fold neatly, and store in a clean, dust-free chest or drawer."
                        }
                    }
                ],
                # Page 5: Worked Example — Planning the Maternity Hospital Bag
                [
                    {
                        "type": "step_process",
                        "title": "Worked Example: Preparing the Family Childbirth Arrival Kit",
                        "content": {
                            "title": "Step-by-Step Maternity Delivery Preparation",
                            "steps": [
                                {
                                    "step_number": 1,
                                    "title": "Prepare Vital Medical Records",
                                    "description": "Pack the **Antenatal Clinic (ANC) card**, national ID card, and health insurance documents in a waterproof folder."
                                },
                                {
                                    "step_number": 2,
                                    "title": "Pack the Baby Layette Kit",
                                    "description": "Pack 3 soft cotton vests, 2 warm flannel receiving blankets, 4 cotton nappies, 2 pairs of mittens, booties, and a soft baby bonnet."
                                },
                                {
                                    "step_number": 3,
                                    "title": "Pack Mother's Personal Care Items",
                                    "description": "Include loose cotton nightdresses, maternity pads, warm slippers, toiletries (mild soap, toothbrush), and a feeding shawl."
                                },
                                {
                                    "step_number": 4,
                                    "title": "Establish Emergency Transport Logistics",
                                    "description": "Identify a reliable driver or neighbor with a vehicle, confirm phone numbers, and plan the quickest route to the maternity hospital."
                                },
                                {
                                    "step_number": 5,
                                    "title": "Set Aside Family Emergency Funds",
                                    "description": "Ensure cash or mobile money reserves are accessible for medication, hospital fees, or unexpected post-delivery supplies."
                                }
                            ]
                        }
                    }
                ],
                # Page 6: Hands-On Baby Fabric Safety Audit
                [
                    {
                        "type": "mini_activity",
                        "title": "Hands-On: Inspecting Infant Fabric Safety",
                        "content": {
                            "title": "Activity: Audit 3 Baby Articles",
                            "instructions": "Examine three baby garments or bedding items at home or school:\n\n1. **Fabric Feel**: Is it 100% breathable cotton, or is it rough, non-absorbent synthetic nylon?\n2. **Fasteners & Safety**: Check for dangerous loose buttons, sharp metal zippers, or long strangulation cords around the neck.\n3. **Seam Softness**: Are the internal seams flat and soft against delicate skin?\n\nRecord your findings in your Home Science notebook."
                        }
                    }
                ],
                # Page 7: Key Takeaways & Recall Helper
                [
                    {
                        "type": "key_takeaway",
                        "title": "Key Takeaways: Childcare & Prenatal Development",
                        "content": {
                            "title": "Core Ideas to Remember",
                            "takeaways": [
                                "Human prenatal development follows **Germinal (0–2w)**, **Embryonic (3–8w)**, and **Fetal (9–40w)** stages.",
                                "Mothers require **iron-rich nutrition** and **clinic checkups**; fathers provide **emotional support**, **financial planning**, and **heavy duty relief**.",
                                "Traditional taboos prohibiting eggs and beans are harmful and must be replaced with scientific balanced nutrition.",
                                "Baby layettes must be made of **soft cotton**, washed with **mild bar soap**, rinsed thoroughly, and dried in the **sun**."
                            ]
                        }
                    },
                    {
                        "type": "memory_tip",
                        "title": "Prenatal Stages Recall Helper",
                        "content": {
                            "title": "Remember 'G-E-F'",
                            "tip": "**G**erminal (implantation), **E**mbryonic (organs form), **F**etal (growth & maturity)!"
                        }
                    }
                ],
                # Page 8: Knowledge Check
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check: Prenatal Science & Layette Care",
                        "content": {
                            "question": "A grandmother advises an expectant mother not to eat boiled eggs and liver, claiming the child will be born without hair. What is the correct scientific advice?",
                            "options": [
                                "Follow the advice strictly because traditional elders know best.",
                                "Reject the taboo and eat eggs and liver, because they provide complete protein, choline for brain development, and iron to prevent maternal anemia.",
                                "Stop eating all food and drink only plain water.",
                                "Eat only raw cassava and sugar cane."
                            ],
                            "correct_index": 1,
                            "explanation": "Eggs and liver are nutrient-dense sources of complete protein, iron, and choline essential for maternal health and fetal organ development. Hair growth is genetically determined, not affected by eating eggs."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 2: Providing Family Shelter
        # =====================================================================
        {
            "unit_order": 2,
            "unit_name": "Providing Family Shelter",
            "unit_description": "Methods of acquiring shelter (renting, buying, building), house classification (traditional, semi-permanent, modern), designs (bungalow, maisonette, flats), shelter as a constitutional human right (Article 43), and environmental house orientation.",
            "lesson_title": "Providing Family Shelter",
            "pages": [
                # Page 1: Topic Introduction & Visual Hook
                [
                    {
                        "type": "suggested_image",
                        "title": "Rent, Buy, or Build? The Family Shelter Decision",
                        "content": {
                            "title": "Rent, Buy, or Build? The Family Shelter Decision",
                            "caption": "A modern multi-story residential housing development in Nairobi providing secure family living."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Learning Objectives: Providing Family Shelter",
                        "content": {
                            "title": "What We Will Learn Today",
                            "goals": [
                                "Evaluate the 3 primary methods of securing shelter: **renting**, **buying**, and **building**.",
                                "Classify house types (**traditional**, **semi-permanent**, **modern**) and architectural designs (**bungalow**, **maisonette**, **flats**).",
                                "Relate family shelter to **constitutional human rights** (Article 43) and environmental sanitation.",
                                "Apply passive design principles of **solar orientation** and **wind direction** in home planning."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "What is Shelter and Why Does it Matter?",
                        "content": {
                            "title": "The Physical Foundation of Family Life",
                            "text": "A **family shelter** is a physical structure that provides protection from weather, physical security against danger, privacy for family members, and a sanitary living environment.\n\nChoosing how to obtain a house is one of the most critical financial and social decisions a family makes. It determines monthly expenditure, stability, safety, and long-term wealth accumulation."
                        }
                    }
                ],
                # Page 2: Methods of Acquiring Shelter: Renting vs. Buying vs. Building
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Family Shelter Acquisition Models: Renting vs. Buying vs. Building",
                        "content": {
                            "title": "Family Shelter Acquisition Models: Renting vs. Buying vs. Building",
                            "caption": "Comparison dashboard measuring Renting, Buying, and Building across initial capital, design freedom, mobility, and long-term equity."
                        }
                    },
                    {
                        "type": "comparison_table",
                        "title": "Comparing Methods of Providing Shelter",
                        "content": {
                            "title": "Financial and Practical Comparison Matrix",
                            "headers": ["Method", "Initial Capital Needed", "Design Freedom", "Mobility & Flexibility", "Long-Term Equity / Asset"],
                            "rows": [
                                ["Renting", "Low (security deposit + 1 month rent)", "Zero (cannot modify walls or structure without landlord permission)", "High (easy to relocate when changing jobs or schools)", "None (monthly payments are an expense with zero ownership)"],
                                ["Buying", "High (large savings or mortgage deposit + interest)", "Moderate (can remodel interior after purchase)", "Low (selling takes months or years)", "Immediate (gains property value over time; can be inherited)"],
                                ["Building", "Phased (can construct in stages as money becomes available)", "Maximum (complete control over room layout, quality, and materials)", "Lowest (permanently tied to the purchased parcel of land)", "High (creates a custom family asset tailored to needs)"]
                            ]
                        }
                    }
                ],
                # Page 3: House Types, Designs, and Construction Materials
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Architectural House Designs: Bungalow, Maisonette, and Flats",
                        "content": {
                            "title": "Architectural House Designs: Bungalow, Maisonette, and Flats",
                            "caption": "3D isometric cutaways comparing Bungalow (single floor), Maisonette (two levels with internal stairs), and Flats (stacked vertical apartments)."
                        }
                    },
                    {
                        "type": "comparison_table",
                        "title": "Classification of Houses and Designs",
                        "content": {
                            "title": "Materials and Architectural Layouts",
                            "headers": ["Classification Category", "Materials Used", "Key Architectural Design", "Best Suited Context"],
                            "rows": [
                                ["Traditional House", "Clay mud walls, thatched grass, reeds, poles", "Round or rectangular single room", "Rural settings; highly eco-friendly with natural thermal insulation"],
                                ["Semi-Permanent House", "Timber boards, mud plaster, corrugated iron sheets", "Single-story simple layout", "Temporary residential use; moderate cost with medium lifespan"],
                                ["Modern: Bungalow", "Quarry stones, kiln bricks, concrete, tiled roof", "Single-story layout with all rooms on ground floor", "Spacious suburban or rural plots; ideal for elderly and young children"],
                                ["Modern: Maisonette", "Reinforced concrete, stone walls, steel, glass", "Two-story layout with internal staircase separating living from bedrooms", "Medium-sized urban plots; provides distinct vertical privacy"],
                                ["Modern: Flats / Apartments", "Multi-story reinforced concrete columns and masonry", "Vertically stacked residential units with shared staircases/lifts", "Densely populated cities (Nairobi, Mombasa); optimizes scarce urban land"]
                            ]
                        }
                    }
                ],
                # Page 4: Human Rights and Environmental Orientation
                [
                    {
                        "type": "concept_explanation",
                        "title": "Shelter as a Constitutional Human Right",
                        "content": {
                            "title": "Article 43 and Passive Environmental Design",
                            "text": "- **Constitutional Right**: Under **Article 43 of the Constitution of Kenya**, every citizen has the right to accessible and adequate housing, reasonable sanitation, and clean water.\n- **Habitability Standards**: Adequate shelter must have a leak-proof roof, solid walls, lockable doors, and safe toilet facilities separated from cooking areas.\n- **Passive House Orientation**:\n  - **Sun Path**: Orient long walls North-South so roof eaves block blazing midday heat while windows catch gentle morning light.\n  - **Wind Direction**: Place kitchens and pit latrines **downwind** from bedrooms so smoke and odors blow safely away from living areas."
                        }
                    },
                    {
                        "type": "callout",
                        "title": "Eco-Friendly Construction",
                        "content": {
                            "title": "Replanting What We Build With",
                            "text": "When trees are felled to provide timber for roofing rafters, always plant at least two indigenous tree seedlings to protect our water towers and prevent soil erosion."
                        }
                    }
                ],
                # Page 5: Worked Example — Home Safety & Adequacy Audit
                [
                    {
                        "type": "step_process",
                        "title": "Worked Example: Conducting a 5-Point Home Safety and Adequacy Audit",
                        "content": {
                            "title": "The Community Shelter Inspector's Checklist",
                            "steps": [
                                {
                                    "step_number": 1,
                                    "title": "Inspect Structural Integrity",
                                    "description": "Check walls for deep structural cracks, inspect roof trusses for termite damage, and ensure gutters do not pool water."
                                },
                                {
                                    "step_number": 2,
                                    "title": "Verify Basic Sanitation and Water",
                                    "description": "Confirm the toilet/latrine is located at least 15 meters down-slope from any water well to prevent groundwater contamination."
                                },
                                {
                                    "step_number": 3,
                                    "title": "Assess Ventilation and Daylight",
                                    "description": "Ensure every habitable room has opening windows equal to at least 10% of the floor area for cross-ventilation."
                                },
                                {
                                    "step_number": 4,
                                    "title": "Check Security and Privacy",
                                    "description": "Verify that exterior doors have functioning locks and that bedroom windows cannot be peered into from public paths."
                                },
                                {
                                    "step_number": 5,
                                    "title": "Review Environmental Safety",
                                    "description": "Ensure drainage ditches carry storm runoff away from house foundations to prevent dampness and mosquito breeding."
                                }
                            ]
                        }
                    }
                ],
                # Page 6: Hands-On Neighborhood Housing Survey
                [
                    {
                        "type": "mini_activity",
                        "title": "Hands-On: Neighborhood Housing Survey",
                        "content": {
                            "title": "Activity: Survey 3 Houses in Your Community",
                            "instructions": "Observe three different residential buildings in your locality:\n\n1. **Classify Type**: Traditional, semi-permanent, or modern masonry?\n2. **Identify Design**: Bungalow, maisonette, or flat/apartment?\n3. **Assess Orientation**: Do the main windows receive morning sunlight? Is the latrine located downwind?\n\nCompile your notes in a comparative chart in your notebook."
                        }
                    }
                ],
                # Page 7: Key Takeaways & Recall Helper
                [
                    {
                        "type": "key_takeaway",
                        "title": "Key Takeaways: Providing Family Shelter",
                        "content": {
                            "title": "Core Ideas to Remember",
                            "takeaways": [
                                "**Renting** gives flexibility; **buying** gives instant ownership; **building** gives complete design customization.",
                                "A **bungalow** has all rooms on one floor; a **maisonette** has two levels with internal stairs; **flats** save scarce urban land.",
                                "Shelter is a **constitutional human right** requiring physical safety, clean water, and adequate sanitation.",
                                "Orient houses **North-South** for thermal cooling and place kitchens/latrines **downwind**."
                            ]
                        }
                    },
                    {
                        "type": "memory_tip",
                        "title": "House Designs Recall Helper",
                        "content": {
                            "title": "B-M-F Designs",
                            "tip": "**B**ungalow (Base/Ground level), **M**aisonette (Middle stairs / 2 floors), **F**lats (Floors stacked high)!"
                        }
                    }
                ],
                # Page 8: Knowledge Check
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check: Housing Designs & Human Rights",
                        "content": {
                            "question": "A family purchases a plot in an urban center and wants a two-story modern house where bedrooms are upstairs for privacy, connected by an indoor staircase. Which house design should they build?",
                            "options": [
                                "A traditional thatched hut.",
                                "A Maisonette, because it is a two-story modern home with internal stairs linking the ground floor living areas to upper private bedrooms.",
                                "A single-story bungalow.",
                                "A temporary timber shack."
                            ],
                            "correct_index": 1,
                            "explanation": "A maisonette is an architectural design featuring two distinct floor levels joined by an internal staircase, typically positioning public living zones downstairs and private bedrooms upstairs."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 3: Room & Area Interrelationship
        # =====================================================================
        {
            "unit_order": 3,
            "unit_name": "Room & Area Interrelationship",
            "unit_description": "The 7 household functional areas, spatial zoning (Public, Work, Private), the 4 placement rules (Privacy, Hygiene, Safety, Culture), standard architectural floor plan symbols, and floor plan sketching & critique.",
            "lesson_title": "Room & Area Interrelationship",
            "pages": [
                # Page 1: Topic Introduction & Visual Hook
                [
                    {
                        "type": "suggested_image",
                        "title": "Playing Architect: The Giant Floor Plan Puzzle",
                        "content": {
                            "title": "Playing Architect: The Giant Floor Plan Puzzle",
                            "caption": "An architectural ground floor plan blueprint showing the logical connection and spatial circulation of household rooms."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Learning Objectives: Room Interrelationship",
                        "content": {
                            "title": "What We Will Learn Today",
                            "goals": [
                                "Identify the **7 functional areas** of a residential home and map them into **3 activity zones**.",
                                "Apply the **4 Golden Rules of Room Placement**: Privacy, Hygiene, Safety, and Culture.",
                                "Interpret and draw **standard architectural blueprint symbols** for walls, doors, and windows.",
                                "Draft and critique simple house floor plans for optimal spatial flow and sanitary safety."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "What is Room Interrelationship?",
                        "content": {
                            "title": "Organizing Space for Harmony and Health",
                            "text": "A house is not just a random collection of rooms. **Room interrelationship** is the logical spatial positioning and connection of different living areas to ensure family safety, disease prevention, privacy, and smooth daily movement.\n\nA well-designed floor plan prevents bad smells, reduces walking fatigue, keeps private sleeping areas peaceful, and allows quick escape during emergencies."
                        }
                    }
                ],
                # Page 2: The 7 Functional Areas & 3 Activity Zones
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Residential Floor Plan Zoning and The 4 Spatial Placement Rules",
                        "content": {
                            "title": "Residential Floor Plan Zoning and The 4 Spatial Placement Rules",
                            "caption": "Color-coded house layout blueprint mapping Public Zone (blue), Work Zone (green), and Private Zone (pink) with distance arrows."
                        }
                    },
                    {
                        "type": "comparison_table",
                        "title": "The 3 Residential Activity Zones",
                        "content": {
                            "title": "Household Spatial Zoning Breakdown",
                            "headers": ["Zone Name", "Color Code", "Included Rooms / Areas", "Primary Placement Requirements"],
                            "rows": [
                                ["Public / Living Zone", "Blue", "Sitting room, living area, dining room, guest cloakroom", "Near the main entrance; welcoming, well-lit, and isolated from bedroom views"],
                                ["Work / Service Zone", "Green", "Kitchen, food pantry/store, laundry area, garage", "Easily accessible from back entry; positioned adjacent to dining; high ventilation"],
                                ["Private / Quiet Zone", "Pink", "Bedrooms, family bathrooms, dressing area", "Positioned at the quiet rear or upper floor; isolated from guest sightlines and noise"]
                            ]
                        }
                    }
                ],
                # Page 3: The 4 Golden Rules of Room Placement
                [
                    {
                        "type": "concept_explanation",
                        "title": "The 4 Placement Principles",
                        "content": {
                            "title": "Privacy, Hygiene, Safety, and Culture",
                            "text": "- **1. Privacy**: Bedrooms must be positioned away from the front door so visitors in the living room cannot look into sleeping spaces.\n- **2. Hygiene**: Latrines and bathrooms must never open directly into food preparation areas (kitchen/dining). Outdoor latrines must be placed downwind and at least 15m away from water wells.\n- **3. Safety**: The kitchen must have a direct exterior exit in case of grease fires, and should not serve as a general through-corridor for running children.\n- **4. Culture**: Respect local cultural norms regarding parent-child room separation and respectful hosting orientations."
                        }
                    },
                    {
                        "type": "callout",
                        "title": "Critical Sanitary Rule",
                        "content": {
                            "title": "Never Connect a Latrine to a Kitchen!",
                            "text": "Placing a toilet door inside or directly facing a kitchen allows airborne germs, fecal bacteria, and flies to contaminate food, spreading deadly cholera, dysentery, and typhoid."
                        }
                    }
                ],
                # Page 4: Architectural Blueprint Symbols Guide
                [
                    {
                        "type": "comparison_table",
                        "title": "Standard Architectural Floor Plan Symbols",
                        "content": {
                            "title": "How to Read and Draw House Blueprints",
                            "headers": ["Structural Element", "Blueprint Symbol Representation", "Drawing Rule"],
                            "rows": [
                                ["Solid Wall", "Thick double parallel lines (solid fill)", "Shows load-bearing masonry walls separating rooms"],
                                ["Window", "Double thin lines with gaps breaking the wall line", "Indicates glass openings for daylight and ventilation"],
                                ["Swinging Door", "A single line perpendicular to wall with a curved 90° arc", "The arc curve shows the direction the door swings open"],
                                ["Doorway Opening", "A clean gap in the wall without a door panel line", "Shows open archways between living and dining areas"]
                            ]
                        }
                    }
                ],
                # Page 5: Worked Example — Critiquing a Faulty Floor Plan
                [
                    {
                        "type": "step_process",
                        "title": "Worked Example: The Architect's Floor Plan Diagnostic Audit",
                        "content": {
                            "title": "Detecting and Correcting 4 Blueprint Faults",
                            "steps": [
                                {
                                    "step_number": 1,
                                    "title": "Audit Circulation Paths",
                                    "description": "Check if visitors must walk through private bedrooms to reach the bathroom. **Correction**: Create a central hallway accessible to all."
                                },
                                {
                                    "step_number": 2,
                                    "title": "Check Kitchen and Dining Flow",
                                    "description": "Ensure the kitchen is directly adjacent to the dining area so hot food can be served without carrying pots across long living room carpet."
                                },
                                {
                                    "step_number": 3,
                                    "title": "Audit Latrine and Water Separation",
                                    "description": "Verify the outdoor toilet is located downwind and at a lower slope than the fresh water borehole."
                                },
                                {
                                    "step_number": 4,
                                    "title": "Verify Natural Lighting in All Bedrooms",
                                    "description": "Ensure every bedroom has at least one exterior wall with a window for morning light and ventilation."
                                }
                            ]
                        }
                    }
                ],
                # Page 6: Hands-On Floor Plan Sketching Activity
                [
                    {
                        "type": "mini_activity",
                        "title": "Hands-On: Sketching a 3-Room Family Home Plan",
                        "content": {
                            "title": "Activity: Draft Your Family Floor Plan",
                            "instructions": "Using a grid ruler and pencil in your notebook:\n\n1. **Draw Outer Walls**: Sketch a 10cm x 8cm rectangle representing outer stone walls.\n2. **Divide Zones**: Position the Sitting Room and Dining in the front (Public Zone), the Kitchen on the side (Work Zone), and 2 Bedrooms in the rear (Private Zone).\n3. **Add Symbols**: Use standard double lines for walls, window gaps, and door swing arcs.\n\nVerify that no private bedroom door opens directly to the front entrance."
                        }
                    }
                ],
                # Page 7: Key Takeaways & Recall Helper
                [
                    {
                        "type": "key_takeaway",
                        "title": "Key Takeaways: Room & Area Interrelationship",
                        "content": {
                            "title": "Core Ideas to Remember",
                            "takeaways": [
                                "A house is divided into **Public (Living/Dining)**, **Work (Kitchen/Store)**, and **Private (Bedrooms/Bath)** zones.",
                                "The 4 Golden Rules are **Privacy**, **Hygiene**, **Safety**, and **Culture**.",
                                "Always place kitchens adjacent to dining for smooth service, but keep toilets isolated from eating areas.",
                                "Architectural symbols use **double lines for walls**, **gaps for windows**, and **curved arcs for swinging doors**."
                            ]
                        }
                    },
                    {
                        "type": "memory_tip",
                        "title": "Room Placement Rule Helper",
                        "content": {
                            "title": "Remember 'P-H-S-C'",
                            "tip": "**P**rivacy (isolated beds), **H**ygiene (toilet separation), **S**afety (fire exits), **C**ulture (respectful layout)!"
                        }
                    }
                ],
                # Page 8: Knowledge Check
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check: Room Interrelationship & Hygiene",
                        "content": {
                            "question": "An aspiring builder sketches a floor plan where the guest toilet opens directly into the food preparation counter in the kitchen. Why is this a serious design violation?",
                            "options": [
                                "Because it makes the kitchen look too colorful.",
                                "Because it violates hygiene rules by allowing airborne toilet microbes and flies to contaminate food, posing a severe health hazard for cholera and typhoid.",
                                "Because visitors will steal food while washing their hands.",
                                "Because doors cannot be installed on kitchen walls."
                            ],
                            "correct_index": 1,
                            "explanation": "Hygiene mandates that toilets and latrines must be isolated with separate ventilation and doors away from food preparation areas to prevent fecal-oral pathogen contamination."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 4: The Kitchen & The Work Triangle
        # =====================================================================
        {
            "unit_order": 4,
            "unit_name": "The Kitchen & The Work Triangle",
            "unit_description": "The 5 kitchen plans (One-Wall, L-Shaped, U-Shaped, Corridor, Island), 3 work centres (Storage, Washing, Cooking), the ergonomic Work Triangle principle (4m–8m perimeter), and kitchen safety clearances.",
            "lesson_title": "The Kitchen & The Work Triangle",
            "pages": [
                # Page 1: Topic Introduction & Visual Hook
                [
                    {
                        "type": "suggested_image",
                        "title": "Running Miles in the Kitchen: The Power of Ergonomics",
                        "content": {
                            "title": "Running Miles in the Kitchen: The Power of Ergonomics",
                            "caption": "A domestic kitchen showing organized counter arrangements connecting storage, washing, and cooking stations."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Learning Objectives: The Kitchen & Work Triangle",
                        "content": {
                            "title": "What We Will Learn Today",
                            "goals": [
                                "Identify and compare the **5 standard kitchen floor plans**: One-Wall, L-Shaped, U-Shaped, Corridor, and Island.",
                                "Map the **3 kitchen work centres**: Storage (Preparation), Washing (Cleaning), and Cooking (Presentation).",
                                "Apply the **Work Triangle principle** to conserve energy and eliminate cross-traffic hazards.",
                                "Evaluate kitchen clearances and safety guidelines to prevent burn and spill accidents."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The Kitchen as a Workshop",
                        "content": {
                            "title": "Why Kitchen Planning Matters",
                            "text": "The kitchen is the most active workshop in the home. In a poorly planned kitchen, a cook can walk up to **5 kilometers** a day just fetching ingredients and pans!\n\nProper layout design minimizes unnecessary footsteps, speeds up food preparation, prevents dangerous collisions with hot pots, and keeps appliances operating efficiently."
                        }
                    }
                ],
                # Page 2: The 5 Standard Kitchen Floor Plans
                [
                    {
                        "type": "suggested_diagram",
                        "title": "The 5 Standard Kitchen Floor Plans",
                        "content": {
                            "title": "The 5 Standard Kitchen Floor Plans",
                            "caption": "Architectural line blueprints showing One-Wall, L-Shaped, U-Shaped, Corridor, and Island kitchen configurations."
                        }
                    },
                    {
                        "type": "comparison_table",
                        "title": "Comparison of the 5 Kitchen Plans",
                        "content": {
                            "title": "Kitchen Floor Plan Evaluation",
                            "headers": ["Plan Type", "Counter Arrangement", "Key Advantage", "Best Suited Room Size"],
                            "rows": [
                                ["One-Wall Plan", "All counters, sink, and stove aligned on a single straight wall", "Saves maximum floor space; very cheap to install", "Tiny apartments, bedsitters, narrow studio rooms"],
                                ["Corridor (Galley)", "Counters arranged along two parallel walls facing each other", "Compact and highly efficient for a solo cook", "Long, narrow rectangular kitchen spaces"],
                                ["L-Shaped Plan", "Counters wrap around two adjoining perpendicular walls", "Eliminates through-traffic; easily accommodates a dining table", "Small to medium square or open-plan kitchens"],
                                ["U-Shaped Plan", "Counters wrap around three continuous adjoining walls", "The gold standard of efficiency; maximum storage and zero traffic", "Medium to large dedicated family kitchens"],
                                ["Island Plan", "Surrounding wall counters with a freestanding central island unit", "Highly sociable; allows multiple family members to cook together", "Large, spacious modern kitchens"]
                            ]
                        }
                    }
                ],
                # Page 3: The 3 Work Centres & The Work Triangle
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Kitchen Work Centres and The Ergonomic Work Triangle",
                        "content": {
                            "title": "Kitchen Work Centres and The Ergonomic Work Triangle",
                            "caption": "Process schematic connecting Storage (Fridge/Larder) -> Washing (Sink) -> Cooking (Stove) with a dotted work triangle overlay."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The 3 Work Centres",
                        "content": {
                            "title": "Sequential Stages of Food Production",
                            "text": "Every kitchen activity flows across three dedicated stations:\n\n- **1. Storage Centre (Receiving & Prep)**: Refrigerator, food cupboards, pantry, and vegetable bins. Ingredients start here.\n- **2. Washing Centre (Cleaning & Chopping)**: Sink, draining board, trash bin, and chopping board. Positioned in the middle!\n- **3. Cooking Centre (Heat & Serving)**: Cooker, stove, oven, microwave, and heat-resistant serving counters.\n\nConnecting these three stations forms the **Work Triangle**. For maximum comfort, the total perimeter of the triangle should measure **between 4 meters and 8 meters** (12 to 26 feet). No household walkways should ever cut through this triangle!"
                        }
                    }
                ],
                # Page 4: Worked Example — Designing an L-Shaped Kitchen
                [
                    {
                        "type": "step_process",
                        "title": "Worked Example: Calculating and Laying Out an Ergonomic Work Triangle",
                        "content": {
                            "title": "The 4-Step Kitchen Layout Calculation",
                            "steps": [
                                {
                                    "step_number": 1,
                                    "title": "Position the Refrigerator at the Outer Edge",
                                    "description": "Place the fridge at the entrance corner so family members grabbing water do not cross the cooking zone."
                                },
                                {
                                    "step_number": 2,
                                    "title": "Place the Sink Along the Central Wall",
                                    "description": "Position the sink beneath a window for daylight, flanked by 90 cm of prep counter space on each side."
                                },
                                {
                                    "step_number": 3,
                                    "title": "Locate the Cooking Stove Safely",
                                    "description": "Position the stove on the adjoining perpendicular wall, ensuring it is at least 40 cm away from window curtains (fire hazard)."
                                },
                                {
                                    "step_number": 4,
                                    "title": "Measure the Work Triangle Perimeter",
                                    "description": "Measure distances: Fridge to Sink (1.8m) + Sink to Stove (1.5m) + Stove to Fridge (2.2m) = **5.5 meters**. Perfect! (Within 4m–8m limit)."
                                }
                            ]
                        }
                    }
                ],
                # Page 5: Kitchen Safety & Energy Conservation
                [
                    {
                        "type": "concept_explanation",
                        "title": "Critical Kitchen Safety and Energy Rules",
                        "content": {
                            "title": "Preventing Accidents and Power Waste",
                            "text": "- **Never Place Stove Next to Fridge**: The heat from the cooking stove forces the refrigerator compressor to overwork, dramatically increasing electric bills and shortening its lifespan.\n- **Aisle Clearance**: Maintain at least **1.2 meters (4 feet)** of clear walkway between facing counters so oven doors can open fully without trapping the cook.\n- **Fire Extinguisher & Exit Access**: Keep the cooking zone near an exterior door with a readily accessible fire blanket or dry chemical extinguisher."
                        }
                    },
                    {
                        "type": "callout",
                        "title": "Safety Alert",
                        "content": {
                            "title": "Never Place a Gas Stove Below a Window!",
                            "text": "Wind blowing through an open window can blow out the gas flame, causing undetectable gas leaks that trigger massive household explosions, or blow curtains into the burner causing fires."
                        }
                    }
                ],
                # Page 6: Hands-On Kitchen Work Triangle Audit
                [
                    {
                        "type": "mini_activity",
                        "title": "Hands-On: Auditing Your Home Kitchen Work Triangle",
                        "content": {
                            "title": "Activity: Pace Out Your Kitchen Triangle",
                            "instructions": "In your home or school kitchen:\n\n1. **Identify the 3 Stations**: Locate the food storage (fridge/cupboard), washing sink, and cooking stove.\n2. **Pace Distances**: Walk and count normal footsteps between Storage $\\rightarrow$ Sink $\\rightarrow$ Stove $\\rightarrow$ Storage (1 footstep $\\approx$ 0.75m).\n3. **Calculate Perimeter**: Multiply total steps by 0.75m. Is it between 4m and 8m?\n4. **Traffic Check**: Does family foot traffic pass through the middle of your cooking path?\n\nRecord your findings and suggest one ergonomic improvement."
                        }
                    }
                ],
                # Page 7: Key Takeaways & Recall Helper
                [
                    {
                        "type": "key_takeaway",
                        "title": "Key Takeaways: The Kitchen & Work Triangle",
                        "content": {
                            "title": "Core Ideas to Remember",
                            "takeaways": [
                                "The 5 kitchen plans are **One-Wall**, **L-Shaped**, **U-Shaped**, **Corridor**, and **Island**.",
                                "The **3 work centres** are **Storage**, **Washing (Sink in middle)**, and **Cooking**.",
                                "The **Work Triangle perimeter** must measure **4m to 8m** to prevent fatigue and cramp.",
                                "Never place a cooking stove next to a refrigerator or beneath window curtains."
                            ]
                        }
                    },
                    {
                        "type": "memory_tip",
                        "title": "Work Triangle Recall Helper",
                        "content": {
                            "title": "Remember 'S-W-C'",
                            "tip": "**S**torage (Fridge) $\\rightarrow$ **W**ashing (Sink in center) $\\rightarrow$ **C**ooking (Stove)!"
                        }
                    }
                ],
                # Page 8: Knowledge Check
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check: Kitchen Layouts & The Work Triangle",
                        "content": {
                            "question": "Which three kitchen stations form the endpoints of the ergonomic 'Work Triangle'?",
                            "options": [
                                "The Dining Table, Plate Rack, and Trash Bin.",
                                "The Storage Centre (Fridge/Larder), Washing Centre (Sink), and Cooking Centre (Stove).",
                                "The Window, Doorway, and Spice Shelf.",
                                "The Ceiling Fan, Floor Mat, and Microwave."
                            ],
                            "correct_index": 1,
                            "explanation": "The ergonomic work triangle connects the three core functional stations of food production: Storage (refrigerator/pantry), Washing (sink), and Cooking (stove)."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 5: Cleaning the Kitchen & Surface Care
        # =====================================================================
        {
            "unit_order": 5,
            "unit_name": "Cleaning the Kitchen & Surface Care",
            "unit_description": "Loose dirt vs fixed dirt, surface material requirements (Tile, Wood, Cement, Terrazzo), daily vs weekly vs special cleaning schedules, top-to-bottom cleaning sequence, improvised abrasives (wood ash, eggshells), and PPE safety gear.",
            "lesson_title": "Cleaning the Kitchen & Surface Care",
            "pages": [
                # Page 1: Topic Introduction & Visual Hook
                [
                    {
                        "type": "suggested_image",
                        "title": "Dirt Attack! The Chemistry of Kitchen Hygiene",
                        "content": {
                            "title": "Dirt Attack! The Chemistry of Kitchen Hygiene",
                            "caption": "A clean, well-maintained domestic kitchen demonstrating rigorous surface sanitation and food safety."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Learning Objectives: Cleaning the Kitchen",
                        "content": {
                            "title": "What We Will Learn Today",
                            "goals": [
                                "Differentiate between **loose dirt** and **fixed dirt** on household surfaces.",
                                "Select appropriate cleaning agents and methods for **wood**, **tile**, **cement**, and **terrazzo** surfaces.",
                                "Execute an orderly **top-to-bottom weekly kitchen cleaning routine**.",
                                "Fabricate and safely use **improvised local abrasives** (wood ash, crushed eggshells) with proper PPE."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Why Kitchen Cleaning is a Science",
                        "content": {
                            "title": "Hygiene and Material Preservation",
                            "text": "The kitchen is where family food is prepared, making it the most vulnerable area for bacterial contamination by **Salmonella** and **E. coli**.\n\nCleaning is not just about wiping counters; it requires matching the right cleaning method to the surface material so we destroy germs without rotting wood or corroding terrazzo floors."
                        }
                    }
                ],
                # Page 2: Loose Dirt vs. Fixed Dirt & Surface Materials
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Loose Dirt vs. Fixed Dirt and Surface Care Protocols",
                        "content": {
                            "title": "Loose Dirt vs. Fixed Dirt and Surface Care Protocols",
                            "caption": "Split-screen comparing dry flour (loose dirt) vs sticky grease (fixed dirt) alongside care protocols for wood, cement, tile, and terrazzo."
                        }
                    },
                    {
                        "type": "comparison_table",
                        "title": "Kitchen Surface Material Care Protocols",
                        "content": {
                            "title": "Preserving Kitchen Surfaces",
                            "headers": ["Surface Material", "Material Characteristics", "Correct Cleaning Method", "Harmful Practices to Avoid"],
                            "rows": [
                                ["Wooden Counters / Tables", "Porous, absorbs moisture easily", "Wipe with a tightly wrung, damp soapy cloth along the grain; dry immediately", "Never soak in water; pooling water causes wood to swell, warp, and rot"],
                                ["Terrazzo Floors", "Smooth marble chips bonded in cement; highly polished", "Wash with warm water and neutral detergent; buff with a dry mop", "Never use acidic cleaners (vinegar, lemon, strong acid); acid dissolves cement matrix"],
                                ["Glazed Ceramic Tiles", "Hard, non-porous, highly water and stain resistant", "Wipe or mop with warm soapy water; scrub tile grout with a small brush", "Avoid heavy metal abrasive pads that scratch the glossy protective glaze"],
                                ["Cemented Floors", "Tough, durable, but porous; absorbs oil and grease stains", "Scrub with warm water, detergent, and fine sand/crushed eggshells; rinse thoroughly", "Leaving stagnant dirty water on cement leaves dull, slippery film"]
                            ]
                        }
                    }
                ],
                # Page 3: Daily, Weekly, and Special Cleaning Schedules
                [
                    {
                        "type": "comparison_table",
                        "title": "Kitchen Cleaning Schedules and Frequencies",
                        "content": {
                            "title": "Organizing Daily, Weekly, and Special Cleans",
                            "headers": ["Cleaning Cycle", "Frequency", "Tasks Performed", "Primary Objective"],
                            "rows": [
                                ["Daily Cleaning", "After every meal preparation session", "Washing dishes, wiping food prep worktops, sweeping loose crumbs, emptying trash", "Prevents immediate pest attraction (cockroaches, flies) and cross-contamination"],
                                ["Weekly Cleaning", "Once every week (e.g. Saturday)", "Dusting ceiling cobwebs, washing wall tiles, cleaning behind stove, scrubbing floor", "Removes accumulated grease films, deep-cleans floor grime, and sanitizes storage"],
                                ["Special Cleaning", "Every few months / school holidays", "Deep descaling of oven vents, emptying and washing all food cupboards, repainting", "Restores surfaces, inspects pantry for stored grain pests, and preserves fixtures"]
                            ]
                        }
                    }
                ],
                # Page 4: Worked Example — The Top-to-Bottom Weekly Kitchen Clean
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Step-by-Step Top-to-Bottom Weekly Kitchen Clean Workflow",
                        "content": {
                            "title": "Step-by-Step Top-to-Bottom Weekly Kitchen Clean Workflow",
                            "caption": "Sequential flow diagram showing PPE gear, open ventilation, dusting ceiling, wiping walls, scrubbing stove, and mopping floor."
                        }
                    },
                    {
                        "type": "step_process",
                        "title": "Worked Example: The 6-Step Top-to-Bottom Weekly Clean",
                        "content": {
                            "title": "Orderly Kitchen Cleaning Workflow",
                            "steps": [
                                {
                                    "step_number": 1,
                                    "title": "Wear PPE and Open Windows",
                                    "description": "Put on a **clean apron**, **headscarf/hair cover**, and **rubber gloves**. Open all windows for maximum cross-ventilation."
                                },
                                {
                                    "step_number": 2,
                                    "title": "Dust Ceilings and High Cornices",
                                    "description": "Using a long-handled broom covered with a cloth, sweep away cobwebs and loose dust from the ceiling down to high walls."
                                },
                                {
                                    "step_number": 3,
                                    "title": "Wipe High Shelves and Wall Tiles",
                                    "description": "Wipe wall tiles and cabinet surfaces from top to bottom with warm soapy water; rinse and dry with a lint-free cloth."
                                },
                                {
                                    "step_number": 4,
                                    "title": "Scrub Stoves and Worktops",
                                    "description": "Remove stove burners, scrub grease using warm detergent water and scouring paste, and wipe dry."
                                },
                                {
                                    "step_number": 5,
                                    "title": "Scrub and Mop the Floor",
                                    "description": "Sweep away loose debris that fell from above, scrub floor with soapy water, and mop dry from the farthest corner towards the door."
                                },
                                {
                                    "step_number": 6,
                                    "title": "Clean and Store Tools",
                                    "description": "Wash mops, rinse brushes, empty dirty water into drainage, and hang cleaning cloths in the sun to dry."
                                }
                            ]
                        }
                    }
                ],
                # Page 5: Improvised Local Abrasives & Safety Gear
                [
                    {
                        "type": "concept_explanation",
                        "title": "Green Cleaning with Local Abrasives",
                        "content": {
                            "title": "Affordable Household Cleaning Agents",
                            "text": "- **1. Wood Ash**: Sifted white wood ash from clean firewood contains natural potassium carbonate. It cuts through tough burnt grease on aluminum cooking pots instantly!\n- **2. Crushed Eggshells**: Finely ground eggshells act as a mild scouring abrasive for cemented floors and pots without gouging surfaces.\n- **3. Rough Ficus Leaves**: Rough textured leaves act as natural scrubbing pads for stubborn soot.\n- **Mandatory Safety (PPE)**: Always wear a headscarf (prevents hair falling into food prep zones), an apron (protects clothes), and rubber gloves (prevents caustic detergent dermatitis)."
                        }
                    },
                    {
                        "type": "callout",
                        "title": "Top-to-Bottom Golden Rule",
                        "content": {
                            "title": "Why Never Clean Floors First!",
                            "text": "If you scrub the floor first and dust the ceiling cobwebs last, all the falling dust and soot will settle onto your freshly washed floor, forcing you to do the entire job twice!"
                        }
                    }
                ],
                # Page 6: Hands-On Wood Ash Abrasive Activity
                [
                    {
                        "type": "mini_activity",
                        "title": "Hands-On: Fabricating Wood Ash Scouring Paste",
                        "content": {
                            "title": "Activity: Make an Eco-Friendly Kitchen Abrasive",
                            "instructions": "In your home science lab or home kitchen:\n\n1. **Sift Wood Ash**: Sift 2 cups of clean firewood ash through a fine sieve to remove sharp charcoal chunks.\n2. **Mix Paste**: Add 2 tablespoons of liquid soap and just enough water to form a smooth paste.\n3. **Test Clean**: Use a damp cloth to rub the paste onto a greasy blackened cooking pot base. Rinse with warm water.\n\nObserve how the natural alkaline ash cuts grease and compare with commercial scouring powders."
                        }
                    }
                ],
                # Page 7: Key Takeaways & Recall Helper
                [
                    {
                        "type": "key_takeaway",
                        "title": "Key Takeaways: Cleaning the Kitchen & Surface Care",
                        "content": {
                            "title": "Core Ideas to Remember",
                            "takeaways": [
                                "**Loose dirt** (dust, crumbs) sweeps easily; **fixed dirt** (grease, soot) requires soap emulsification and friction.",
                                "Never soak **wood** in water (causes rotting); never use **acids** on terrazzo (dissolves cement).",
                                "Always clean in a **top-to-bottom sequence**: Ceiling $\\rightarrow$ Walls $\\rightarrow$ Worktops $\\rightarrow$ Floor.",
                                "**Sifted wood ash** and **crushed eggshells** are powerful, low-cost local abrasives for heavy grease."
                            ]
                        }
                    },
                    {
                        "type": "memory_tip",
                        "title": "Kitchen Surface Rule Helper",
                        "content": {
                            "title": "Wood vs Terrazzo Rule",
                            "tip": "**No Soaking on Wood** (prevents warp); **No Acid on Terrazzo** (prevents corrosion)!"
                        }
                    }
                ],
                # Page 8: Knowledge Check
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check: Surface Preservation & Cleaning Sequence",
                        "content": {
                            "question": "A student is cleaning a solid wooden kitchen worktop. Which cleaning method correctly preserves the wood from damage?",
                            "options": [
                                "Pouring a full bucket of boiling soapy water over the wood and letting it soak for an hour.",
                                "Wiping along the grain with a tightly wrung, damp soapy cloth and drying immediately with a clean dry towel.",
                                "Scrubbing with strong hydrochloric acid and a wire brush.",
                                "Leaving the spilled milk to dry permanently."
                            ],
                            "correct_index": 1,
                            "explanation": "Wood is porous and easily absorbs moisture, causing it to swell, warp, rot, and harbor bacterial mold. It must be cleaned with minimal dampness along the grain and dried instantly."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 6: Colour in the Home & Interior Decoration
        # =====================================================================
        {
            "unit_order": 6,
            "unit_name": "Colour in the Home & Interior Decoration",
            "unit_description": "Color terminology (Hue, Value, Tint, Shade, Tone, Intensity), the 12-slice Color Wheel, color schemes (Monochromatic, Analogous, Complementary), and color psychology for interior home decoration.",
            "lesson_title": "Colour in the Home & Interior Decoration",
            "pages": [
                # Page 1: Topic Introduction & Visual Hook
                [
                    {
                        "type": "suggested_image",
                        "title": "Paint Your World: The Psychology and Power of Colour",
                        "content": {
                            "title": "Paint Your World: The Psychology and Power of Colour",
                            "caption": "A harmonious living room interior utilizing balanced wall colors, natural lighting, and decorative textile accents."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Learning Objectives: Colour in the Home",
                        "content": {
                            "title": "What We Will Learn Today",
                            "goals": [
                                "Define the 6 core color terms: **Hue**, **Value**, **Tint**, **Shade**, **Tone**, and **Intensity**.",
                                "Construct and interpret the 12-slice **Color Wheel** (Primary, Secondary, Tertiary).",
                                "Design **Monochromatic**, **Analogous**, and **Complementary** interior color schemes.",
                                "Apply color psychology to enhance room lighting, spatial perception, and climate comfort."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Colour as a Design Tool",
                        "content": {
                            "title": "More Than Just Decoration",
                            "text": "Colour is one of the most powerful design elements in home economics. It directly affects:\n\n- **Spatial Perception**: Light colours reflect light, making small rooms look spacious and airy; dark colours absorb light, drawing walls inward.\n- **Thermal Comfort**: Cool blues and greens create psychological cooling in hot coastal homes; warm oranges and yellows make cold highland rooms feel cozy.\n- **Family Mood**: Soft pastels promote restful sleep in bedrooms, while vibrant warm tones stimulate appetite in dining rooms."
                        }
                    }
                ],
                # Page 2: Color Terminology & The 12-Slice Color Wheel
                [
                    {
                        "type": "suggested_diagram",
                        "title": "The 12-Slice Color Wheel: Primaries, Secondaries, Tints and Shades",
                        "content": {
                            "title": "The 12-Slice Color Wheel: Primaries, Secondaries, Tints and Shades",
                            "caption": "Circular color wheel illustrating 3 Primaries, 3 Secondaries, 6 Tertiaries, plus White Tint and Black Shade modifiers."
                        }
                    },
                    {
                        "type": "comparison_table",
                        "title": "Core Color Terminology Breakdown",
                        "content": {
                            "title": "The 6 Essential Color Terms",
                            "headers": ["Term", "Scientific Definition", "How It is Created", "Everyday Example"],
                            "rows": [
                                ["Hue", "The pure name of the color wavelength", "Base pigment (Red, Blue, Yellow)", "Pure Red, Pure Blue, Pure Yellow"],
                                ["Value", "The lightness or darkness of a color", "Varying the amount of light reflected", "Light sky blue has high value; navy blue has low value"],
                                ["Tint", "A lighter value of a pure color hue", "Adding **white** to the pure hue", "Pink is a tint of Red; Baby Blue is a tint of Blue"],
                                ["Shade", "A darker value of a pure color hue", "Adding **black** to the pure hue", "Maroon is a shade of Red; Navy is a shade of Blue"],
                                ["Tone", "A softened, muted value of a color", "Adding **gray** (or complementary color)", "Sage Green, Dusty Rose, Warm Slate"],
                                ["Intensity", "The brightness, purity, or dullness of a hue", "Pure undiluted pigment concentration", "Neon bright yellow (high) vs mustard yellow (low)"]
                            ]
                        }
                    }
                ],
                # Page 3: Interior Color Schemes
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Interior Color Schemes: Monochromatic, Analogous, and Complementary",
                        "content": {
                            "title": "Interior Color Schemes: Monochromatic, Analogous, and Complementary",
                            "caption": "Comparative room renders illustrating Monochromatic (single hue tints/shades), Analogous (neighboring wheel hues), and Complementary (opposite wheel hues)."
                        }
                    },
                    {
                        "type": "comparison_table",
                        "title": "Comparison of Interior Color Schemes",
                        "content": {
                            "title": "3 Color Harmonies in the Home",
                            "headers": ["Scheme Name", "Color Wheel Relationship", "Visual Mood Created", "Best Room Applications"],
                            "rows": [
                                ["Monochromatic Scheme", "Uses one single hue in various tints, shades, and tones", "Soothing, unified, peaceful, and spacious", "Bedrooms, study rooms, small bathrooms"],
                                ["Analogous Scheme", "Uses 3 or 4 colors located next to each other on the wheel", "Harmonious, gentle, natural visual flow", "Living rooms, family sitting lounges"],
                                ["Complementary Scheme", "Uses 2 colors located directly opposite each other on the wheel", "High contrast, bold, vibrant, and energetic", "Creative spaces, dining room accents, children's playrooms"]
                            ]
                        }
                    }
                ],
                # Page 4: Worked Example — Choosing Colors for a Hot Coastal Bedroom
                [
                    {
                        "type": "step_process",
                        "title": "Worked Example: Designing a Cooling Color Scheme for a Coastal Home",
                        "content": {
                            "title": "Step-by-Step Color Selection Workflow",
                            "steps": [
                                {
                                    "step_number": 1,
                                    "title": "Assess Climate and Natural Light",
                                    "description": "The coastal bedroom receives strong, intense morning sun and experiences high humidity."
                                },
                                {
                                    "step_number": 2,
                                    "title": "Select the Dominant Color Family",
                                    "description": "Choose a **cool hue (Blue-Green)** to provide psychological cooling and relaxation."
                                },
                                {
                                    "step_number": 3,
                                    "title": "Apply Light Tints to Large Wall Surfaces",
                                    "description": "Paint walls in a **light tint of seafoam green** (white + green) to reflect daylight and make the room feel breezy."
                                },
                                {
                                    "step_number": 4,
                                    "title": "Add Medium Tone Soft Furnishings",
                                    "description": "Use breathable white sheer curtains with sky-blue cotton bedsheets for harmonious monochromatic tranquility."
                                },
                                {
                                    "step_number": 5,
                                    "title": "Incorporate Subtle Warm Accent Cushions",
                                    "description": "Place two small coral-orange cushions on the bed (complementary contrast) to add a touch of warmth without overwhelming the room."
                                }
                            ]
                        }
                    }
                ],
                # Page 5: Spatial Lighting & Color Psychology
                [
                    {
                        "type": "concept_explanation",
                        "title": "Factors Governing Interior Colour Choices",
                        "content": {
                            "title": "4 Rules for Successful Room Painting",
                            "text": "- **1. Room Size**: Always use light tints on small rooms to make them appear larger. Dark shades make large halls feel intimate and cozy.\n- **2. Natural Lighting**: Rooms with small, dark windows require high-value light tints (cream, pastel yellow) to bounce light. Rooms with blazing sun suit cool, muted tones.\n- **3. Room Function**: Use calm cool colors for sleeping (bedrooms); use appetizing warm colors (peach, warm yellow) for eating areas (dining/kitchen).\n- **4. Existing Furnishings**: Ensure wall paint harmonizes with curtains, carpet, and wooden furniture."
                        }
                    },
                    {
                        "type": "callout",
                        "title": "Design Warning",
                        "content": {
                            "title": "Never Paint a Tiny Dark Room in Dark Red!",
                            "text": "Dark red absorbs all light, making a small room feel like a suffocating, hot, and stressful box. Use light pastels to bounce natural light!"
                        }
                    }
                ],
                # Page 6: Hands-On Color Wheel Mixing Activity
                [
                    {
                        "type": "mini_activity",
                        "title": "Hands-On: Painting a 12-Slice Color Wheel",
                        "content": {
                            "title": "Activity: Mix Primaries to Create Secondaries and Tints",
                            "instructions": "Using watercolor paints in your notebook:\n\n1. **Paint Primaries**: Fill in Red, Yellow, and Blue at 120° angles on a circle.\n2. **Mix Secondaries**: Mix Red+Yellow (Orange), Yellow+Blue (Green), Blue+Red (Violet) in the middle slots.\n3. **Mix Tints & Shades**: On the side, mix Red + White to make Pink (Tint), and Blue + Black to make Navy (Shade).\n\nMount your completed wheel in your Home Science design portfolio."
                        }
                    }
                ],
                # Page 7: Key Takeaways & Recall Helper
                [
                    {
                        "type": "key_takeaway",
                        "title": "Key Takeaways: Colour in the Home",
                        "content": {
                            "title": "Core Ideas to Remember",
                            "takeaways": [
                                "**Hue** is the color name; **Tint** is adding white (lighter); **Shade** is adding black (darker); **Tone** is adding gray.",
                                "**Primary colors** (Red, Yellow, Blue) cannot be made by mixing; **Secondary colors** (Orange, Green, Violet) come from equal primary mixes.",
                                "**Monochromatic** uses 1 hue in different values; **Analogous** uses neighbor hues; **Complementary** uses opposite hues.",
                                "Use **light cool tints** (blue, green) for hot coastal bedrooms and **warm tones** (peach, yellow) for cozy dining spaces."
                            ]
                        }
                    },
                    {
                        "type": "memory_tip",
                        "title": "Tint vs Shade Recall Helper",
                        "content": {
                            "title": "Tint vs Shade Rule",
                            "tip": "**Tint = + White** (Light as day); **Shade = + Black** (Dark as night)!"
                        }
                    }
                ],
                # Page 8: Knowledge Check
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check: Color Schemes & Design Harmony",
                        "content": {
                            "question": "What is created when a painter mixes pure white paint into a pure blue color hue?",
                            "options": [
                                "A dark shade of blue.",
                                "A light tint of blue (such as sky blue or baby blue).",
                                "A secondary color.",
                                "A complementary color scheme."
                            ],
                            "correct_index": 1,
                            "explanation": "A tint is a lighter value of a color hue produced by adding white paint, which increases light reflectance."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 7: Soft Furnishings & Home Crafts
        # =====================================================================
        {
            "unit_order": 7,
            "unit_name": "Soft Furnishings & Home Crafts",
            "unit_description": "Types and functions of soft furnishings (curtains, cushions, pillows, floor mats, bedsheets), fabric selection criteria, step-by-step cushion construction, local stuffing materials, daily care, and small business entrepreneurship.",
            "lesson_title": "Soft Furnishings & Home Crafts",
            "pages": [
                # Page 1: Topic Introduction & Visual Hook
                [
                    {
                        "type": "suggested_image",
                        "title": "The Comfort of Home: The World of Soft Furnishings",
                        "content": {
                            "title": "The Comfort of Home: The World of Soft Furnishings",
                            "caption": "An elegantly furnished living room showcasing decorative scatter cushions, tailored seat covers, and flowing window curtains."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Learning Objectives: Soft Furnishings",
                        "content": {
                            "title": "What We Will Learn Today",
                            "goals": [
                                "Identify core **soft furnishings** (curtains, cushions, pillows, mats, bedsheets) and their functions.",
                                "Evaluate **selection factors** (fabric durability, washability, color harmony, non-slip safety).",
                                "Measure, cut, stitch, and stuff a functional **household cushion** using local materials.",
                                "Apply daily care routines and explore the **economic and entrepreneurial potential** of textile crafts."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "What Are Soft Furnishings?",
                        "content": {
                            "title": "The Textile Heart of the Home",
                            "text": "**Soft furnishings** are textile articles used in household rooms to provide physical comfort, aesthetic elegance, privacy, sound absorption, and floor safety.\n\nWithout soft furnishings, a house feels cold, hard, echoey, and uninviting. Curtains insulate windows, cushions soften wooden chairs, and floor mats collect outdoor dirt at doorways."
                        }
                    }
                ],
                # Page 2: Types, Functions, and Fabric Selection
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Soft Furnishings in the Home: Types, Functions, and Fabric Selection",
                        "content": {
                            "title": "Soft Furnishings in the Home: Types, Functions, and Fabric Selection",
                            "caption": "Isometric living room layout detailing curtains (light control), sofa cushions (ergonomic comfort), floor mats (safety), and table runners."
                        }
                    },
                    {
                        "type": "comparison_table",
                        "title": "Soft Furnishing Types and Primary Functions",
                        "content": {
                            "title": "Household Soft Furnishings Guide",
                            "headers": ["Item", "Recommended Fabrics", "Primary Functions", "Care & Maintenance"],
                            "rows": [
                                ["Window Curtains & Drapes", "Polyester-cotton blends, heavy linen, sheer lace", "Light control, privacy, thermal insulation against cold night drafts, acoustic echo absorption", "Weekly shaking; periodic gentle washing; avoid direct sun bleach"],
                                ["Scatter Cushions & Pillows", "Durable woven cotton, canvas, bark cloth", "Back and neck ergonomic support, decorative color accents on furniture", "Daily plump shaking; washing removable slipcovers regularly"],
                                ["Bedsheets & Pillowcases", "100% breathable cotton, soft percale", "Direct skin comfort during sleep, moisture absorption, mattress hygiene", "Weekly washing in hot soapy water; sun drying and hot ironing"],
                                ["Floor Mats & Rugs", "Tough jute, sisal, heavy cotton with non-slip rubber backing", "Scrapes shoe dirt at doorways, prevents slip accidents, protects floor finishes", "Daily outdoor beating/brushing; vacuuming; spot-cleaning mud stains"],
                                ["Table Runners & Mats", "Linen, embroidered cotton, washable synthetic blends", "Protects dining table from hot dish burns and scratches; enhances meal elegance", "Wiping immediately after meals; gentle hand washing"]
                            ]
                        }
                    }
                ],
                # Page 3: Selection Criteria for Household Textiles
                [
                    {
                        "type": "concept_explanation",
                        "title": "The 4 Selection Rules for Soft Furnishings",
                        "content": {
                            "title": "Choosing Textiles Wisely",
                            "text": "- **1. Functional Utility**: Match fabric to purpose (e.g. choose heavy, tightly woven drapes for bedroom privacy; choose non-slip backed mats for bathroom safety).\n- **2. Durability & Washability**: Living room cushions experience heavy family friction—choose colorfast, pre-shrunk cotton that withstands frequent laundering.\n- **3. Color Harmony**: Select furnishings that match or tastefully accent the room's established color scheme (monochromatic, analogous, or complementary).\n- **4. Cost & Sustainability**: Utilize locally available fabrics, upcycled textile scraps, and natural biodegradable fibers (sisal, cotton)."
                        }
                    },
                    {
                        "type": "callout",
                        "title": "Safety Alert",
                        "content": {
                            "title": "Never Use Slippery Mats on Tiled Floors!",
                            "text": "Floor mats placed on polished tiles or terrazzo MUST have a textured rubber or latex non-slip backing. Loose, slippery mats are a major cause of dangerous household hip fractures and falls!"
                        }
                    }
                ],
                # Page 4: Worked Example — Making a Functional Household Cushion
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Step-by-Step Cushion Construction and Hypoallergenic Stuffing",
                        "content": {
                            "title": "Step-by-Step Cushion Construction and Hypoallergenic Stuffing",
                            "caption": "Process sequence showing fabric measurement (42x42cm), 3-side plain seaming, adding clean dry wool/sponge stuffing, and hand-tied slip-stitching."
                        }
                    },
                    {
                        "type": "step_process",
                        "title": "Worked Example: Constructing a 40cm x 40cm Scatter Cushion",
                        "content": {
                            "title": "5-Step Cushion Construction Workflow",
                            "steps": [
                                {
                                    "step_number": 1,
                                    "title": "Measure and Cut Fabric with Seam Allowance",
                                    "description": "Cut two 42 cm x 42 cm squares of sturdy cotton fabric (allowing 1 cm seam allowance on all four sides)."
                                },
                                {
                                    "step_number": 2,
                                    "title": "Pin and Stitch 3 Sides",
                                    "description": "Place fabric **right sides together**. Pin and stitch a strong plain seam 1 cm from edge along 3 full sides and 5 cm into the 4th side."
                                },
                                {
                                    "step_number": 3,
                                    "title": "Trim Corners and Turn Right Side Out",
                                    "description": "Snip seam allowance corners diagonally to remove bulk, turn the cover right side out, and gently push out corners with a pencil."
                                },
                                {
                                    "step_number": 4,
                                    "title": "Insert Clean Hypoallergenic Stuffing",
                                    "description": "Fill the cushion evenly through the opening using clean dry sheep's wool, shredded foam sponge scraps, or clean dry coconut fiber."
                                },
                                {
                                    "step_number": 5,
                                    "title": "Close Opening with Neat Slip-Stitching",
                                    "description": "Fold the raw edges of the opening inward by 1 cm and stitch closed securely using neat, invisible hand **slip-stitches** or attach button fasteners."
                                }
                            ]
                        }
                    }
                ],
                # Page 5: Safe Stuffing Materials & Entrepreneurship
                [
                    {
                        "type": "concept_explanation",
                        "title": "Local Stuffing Materials & Business Potential",
                        "content": {
                            "title": "From Scrap Fabric to Sustainable Income",
                            "text": "- **Safe Stuffing Materials**:\n  - Clean shredded upholstery sponge scraps (light, springy, washable).\n  - Clean, dry, carded sheep's wool (warm, natural, resilient).\n  - Clean, dry coconut husk fiber or kapok tree floss (hypoallergenic, pest-resistant).\n  - *Never use damp soil, fresh green grass, or unwashed chicken feathers (harbors mold, bacteria, and allergens)!\n- **Entrepreneurial Potential**: Soft furnishings require minimal starting capital. Grade 8 learners can stitch patchwork cushion covers, kitchen aprons, and table runners from tailoring off-cuts to sell at school exhibitions or local markets, generating valuable family income."
                        }
                    }
                ],
                # Page 6: Hands-On Cushion Construction Activity
                [
                    {
                        "type": "mini_activity",
                        "title": "Hands-On: Constructing a Mini Cushion Sampler",
                        "content": {
                            "title": "Activity: Stitch Your Own Cushion",
                            "instructions": "Using two 20cm x 20cm scraps of colorful fabric:\n\n1. **Stitch Sides**: Pin right sides together, stitch 3 sides on a machine or by hand using backstitches.\n2. **Stuff**: Turn right side out and fill with clean sponge scraps or clean wool until firm and soft.\n3. **Close**: Slip-stitch the opening closed by hand.\n\nCalculate your production cost and set a selling price for an entrepreneurship project!"
                        }
                    }
                ],
                # Page 7: Key Takeaways & Recall Helper
                [
                    {
                        "type": "key_takeaway",
                        "title": "Key Takeaways: Soft Furnishings & Home Crafts",
                        "content": {
                            "title": "Core Ideas to Remember",
                            "takeaways": [
                                "**Soft furnishings** provide physical comfort, thermal insulation, privacy, acoustic absorption, and floor safety.",
                                "Choose **colorfast, washable cottons** for cushions and **non-slip rubber backings** for bathroom/doorway mats.",
                                "Construct cushions by stitching **3 sides right-sides-together**, turning inside out, inserting clean stuffing, and **slip-stitching** closed.",
                                "Soft furnishings offer fantastic **entrepreneurial income potential** using affordable local textile scraps."
                            ]
                        }
                    },
                    {
                        "type": "memory_tip",
                        "title": "Cushion Construction Helper",
                        "content": {
                            "title": "Remember 'C-S-T-F-C'",
                            "tip": "**C**ut fabric $\\rightarrow$ **S**titch 3 sides $\\rightarrow$ **T**urn inside-out $\\rightarrow$ **F**ill with stuffing $\\rightarrow$ **C**lose opening!"
                        }
                    }
                ],
                # Page 8: Knowledge Check
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check: Soft Furnishing Selection & Construction",
                        "content": {
                            "question": "Which of the following is a safe, hygienic, and resilient local stuffing material to fill a home-made scatter cushion?",
                            "options": [
                                "Fresh green grass from the garden mixed with damp soil.",
                                "Clean shredded foam sponge scraps or clean dry carded sheep's wool.",
                                "Unwashed chicken feathers and food scraps.",
                                "Heavy stones and gravel."
                            ],
                            "correct_index": 1,
                            "explanation": "Clean shredded foam sponge and clean dry carded wool are lightweight, resilient, hypoallergenic, and hygienic materials that maintain shape without harboring mold or pests."
                        }
                    }
                ]
            ]
        }
    ]

def ingest_cbc_grade8_home_science_topic4(replace=False):
    """Executes the atomic ingestion of CBC Grade 8 Home Science Topic 4."""
    print("=" * 80)
    print("STARTING INGESTION: CBC GRADE 8 HOME SCIENCE — TOPIC 4: CARING FOR THE FAMILY")
    print("=" * 80)

    # 1. Resolve Curriculum
    curriculum = Curriculum.objects.filter(name__iexact="CBC").first()
    assert curriculum, "Curriculum 'CBC' not found!"
    print(f"[*] Found Curriculum: {curriculum.name} (ID: {curriculum.id})")

    # 2. Resolve Grade 8
    grade = Grade.objects.filter(curriculum=curriculum, name="Grade 8").first()
    assert grade, "Grade 'Grade 8' not found under CBC!"
    print(f"[*] Grade 8: ID {grade.id} (Level {grade.level})")

    # 3. Resolve Subject: Home Science
    subject = Subject.objects.filter(grade=grade, name="Home Science").first()
    assert subject, "Subject 'Home Science' not found under Grade 8!"
    print(f"[*] Subject: {subject.name} (ID {subject.id})")

    # 4. Resolve Topic: Caring for the Family (Order: 4)
    topic_name = "Caring for the Family"
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
            description="Comprehensive CBC Grade 8 module covering childcare and prenatal development, providing family shelter, room layout and spatial zoning, kitchen design & work triangle ergonomics, kitchen cleaning & surface care, color theory & schemes, and soft furnishings construction."
        )
        print(f"[+] Created Topic: {topic.name} (ID: {topic.id}, Order: {topic.order})")
    else:
        print(f"[*] Using existing Topic: {topic.name} (ID: {topic.id}, Order: {topic.order})")

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
                lesson.title = lesson_title
                lesson.status = "published"
                lesson.version = 1
                lesson.save()
            else:
                lesson = Lesson.objects.create(
                    topic=topic,
                    learning_unit=learning_unit,
                    title=lesson_title,
                    status="published",
                    version=1
                )
            print(f"\n  [+] Ingesting Lesson {unit_order}: '{lesson.title}' (Lesson ID: {lesson.id})")

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
            print(f"      [OK] Ingested {lesson_page_count} Pages ({len(lesson.blocks.all())} Blocks) for Unit {unit_order}.")

    print("\n" + "=" * 80)
    print("[SUCCESS] CBC Grade 8 Home Science Topic 4 Ingestion Complete!")
    print(f"[*] Total Lessons Ingested: {total_lessons}")
    print(f"[*] Total Pages Ingested:   {total_pages}")
    print(f"[*] Total Blocks Ingested:  {total_blocks}")
    print("=" * 80)

if __name__ == "__main__":
    replace_flag = "--replace" in sys.argv
    ingest_cbc_grade8_home_science_topic4(replace=replace_flag)
