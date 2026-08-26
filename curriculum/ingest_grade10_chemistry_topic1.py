"""
VLearn CBC Grade 10 Chemistry — Topic 1: Introduction to Chemistry
Production Ingestion Engine (Senior Secondary Pedagogical Edition)

Curriculum: CBC (ID: 5)
Grade: Grade 10 (ID: 5, Level: 10)
Subject: Chemistry (ID: 5)
Topic: Introduction to Chemistry (Topic Order: 1)

Decomposed into 5 Learning Units & 5 Published Lessons:
  1. Meaning, Scope, and Language of Chemistry (5 Pages, 11 Blocks)
  2. Branches and Careers in Chemistry (5 Pages, 11 Blocks)
  3. Chemistry in Daily Life, Industry, and the Environment (5 Pages, 11 Blocks)
  4. Drugs, Substance Use, Consumer Rights, and Safe Learning (5 Pages, 11 Blocks)
  5. Chemistry Communication and Inquiry Project (5 Pages, 11 Blocks)
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
    text = re.sub(r'\[VISUAL:\s*[A-Z]+\][^\n]*', '', text)
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
    """Returns the comprehensive pedagogical page and block structure for Grade 10 Topic 1: Introduction to Chemistry."""
    return [
        # =====================================================================
        # LESSON 1: Meaning, Scope, and Language of Chemistry
        # =====================================================================
        {
            "unit_order": 1,
            "unit_name": "Meaning, Scope, and Language of Chemistry",
            "unit_description": "Define Chemistry as the study of matter, properties, composition, structure, and energy interactions. Explore the chemical triplet (Macroscopic, Submicroscopic, Symbolic), physical vs chemical changes, and laboratory safety.",
            "lesson_title": "Meaning, Scope, and Language of Chemistry",
            "pages": [
                [
                    {
                        "type": "suggested_image",
                        "title": "Welcome to Chemistry: The Central Science",
                        "content": {
                            "title": "Welcome to Chemistry: The Central Science",
                            "caption": "Laboratory glassware in an active chemical investigation, demonstrating colour changes and transformations of matter."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: What We Will Master Today",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Define **Chemistry** and **matter**, identifying their fundamental role in everything around us.",
                                "Master the **Three Levels of Chemistry**: Macroscopic, Submicroscopic, and Symbolic representations.",
                                "Investigate and classify changes in matter as **Physical Changes** or **Chemical Changes** with experimental evidence.",
                                "Apply laboratory safety precautions and distinguish physical dissolving from irreversible chemical reactions."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "What is Chemistry? The Study of Matter and Transformation",
                        "content": {
                            "title": "The Study of Matter and Transformation",
                            "text": "Have you ever wondered why a wet iron nail turns rusty when left outside, why milk goes sour after a few days, or how a simple chapati rises and turns golden-brown on a hot pan? These are not magic—they are **Chemistry in action**!\n\nAt its heart, Chemistry is about understanding what our world is made of and how it changes. Every single object you see, touch, or breathe is made of 'stuff' that chemists call **matter**."
                        }
                    },
                    {
                        "type": "definition_card",
                        "title": "Core Definition: Chemistry & Matter",
                        "content": {
                            "term": "Chemistry",
                            "definition": "A central branch of natural science that studies matter, its chemical composition, physical and chemical properties, structure, and the transformations it undergoes when interacting with energy.",
                            "example": "Studying how carbon atoms combine with oxygen molecules during combustion to release heat and carbon dioxide gas."
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "Thinking Like a Chemist: The Three Representational Levels",
                        "content": {
                            "title": "The Chemical Triplet",
                            "text": "To truly understand Chemistry, we must learn to connect **three distinct levels of reality** simultaneously:\n\n1. **Macroscopic Level (What We Observe)**: Phenomena we can directly see, smell, measure, or touch in the laboratory or everyday life (e.g. effervescent bubbles rising in water, glowing heat from burning charcoal).\n2. **Submicroscopic Level (What Particles Do)**: The behavior and rearrangement of tiny, discrete particles—atoms, ions, and molecules—that are invisible to the naked eye (e.g. carbon atoms colliding with oxygen molecules to form carbon dioxide).\n3. **Symbolic Level (How We Write It)**: The universal shorthand notation chemists use, including element symbols, chemical formulas, state symbols, and balanced stoichiometric equations (e.g. $\\text{C}(s) + \\text{O}_2(g) \\rightarrow \\text{CO}_2(g)$)."
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "The Three Levels of Chemistry: Combustion of Charcoal",
                        "content": {
                            "title": "The Three Levels of Chemistry: Combustion of Charcoal",
                            "caption": "Connecting macroscopic glowing heat in a jiko, submicroscopic particle collisions, and symbolic chemical notation."
                        }
                    }
                ],
                [
                    {
                        "type": "step_process",
                        "title": "Practical Investigation: Physical vs. Chemical Changes",
                        "content": {
                            "title": "Laboratory Investigation Protocol",
                            "steps": [
                                "1. **Melting Ice**: Place an ice cube in a 100 ml beaker at room temperature. Observe solid ice turning into liquid water. Place it in a freezer to reverse the change.",
                                "2. **Tearing Paper**: Tear a clean sheet of paper into small pieces. Observe that size and shape change, but the substance remains cellulose paper.",
                                "3. **Burning Paper**: Using metal tongs, hold a scrap of paper over a heat-resistant watch glass and ignite with a match. Observe smoke and grey-black ash. Note that ash cannot be converted back into paper.",
                                "4. **Heating Candle Wax**: Light a candle. Observe solid wax melting into liquid wax near the flame, then resolidifying upon cooling. Observe the wick consuming wax to produce carbon dioxide and water vapour."
                            ]
                        }
                    },
                    {
                        "type": "comparison_table",
                        "title": "Comparative Analysis: Physical vs. Chemical Changes",
                        "content": {
                            "headers": ["Feature", "Physical Change", "Chemical Change (Reaction)"],
                            "rows": [
                                ["New Substance Formed", "No new substance is formed", "One or more brand new substances are formed with unique properties"],
                                ["Reversibility", "Usually easily reversible by physical means (e.g., freezing, condensation)", "Usually irreversible or difficult to reverse by physical methods"],
                                ["Energy Shifts", "Relatively small energy changes (latent heat of fusion/vaporization)", "Substantial energy changes (exothermic heat/light release or endothermic absorption)"],
                                ["Mass Changes", "Total mass of the individual substance is conserved in the same state", "Mass of original reactants changes as new products are generated"],
                                ["Examples", "Melting ice, boiling water, dissolving sugar, tearing paper", "Burning wood/paper, rusting iron, souring milk, baking a cake"]
                            ]
                        }
                    }
                ],
                [
                    {
                        "type": "suggested_video",
                        "title": "Laboratory Demonstration: Comparing Physical and Chemical Changes",
                        "content": {
                            "title": "Physical vs Chemical Change in Action",
                            "description": "Watch a laboratory demonstration comparing the reversible physical change of boiling water with the brilliant, irreversible chemical reaction of burning magnesium ribbon in air.",
                            "url": "https://www.youtube.com/watch?v=4ZGULLWEy1c"
                        }
                    },
                    {
                        "type": "common_misconception",
                        "title": "Common Mistake: Dissolving vs. Chemical Reaction",
                        "content": {
                            "misconception": "Dissolving salt or sugar in water is a chemical change because the solid 'disappears'.",
                            "correction": "Dissolving is a purely physical change! The solute particles are simply separated and solvated by polar water molecules. No new chemical bonds are created, and solid crystals can be 100% recovered by physical evaporation.",
                            "why_it_matters": "Confusing physical solvation with chemical bonds leads to errors when writing ionic equations and predicting reaction outcomes."
                        }
                    }
                ],
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check: Rusting Steel Pad",
                        "content": {
                            "question": "Wanjiku left a steel pad in a wet sink overnight. The next morning, she noticed a crumbly reddish-brown coating (rust) on the pad. How should this transformation be classified using the three levels of Chemistry?",
                            "options": [
                                "A physical change because the steel pad merely changed its colour temporarily.",
                                "A chemical change because iron atoms reacted with oxygen and water to form a completely new compound (hydrated iron(III) oxide) that cannot be reversed by physical means.",
                                "A physical change because the water evaporated and left dried iron particles behind.",
                                "A nuclear transformation because the iron nucleus lost protons to form oxygen."
                            ],
                            "answer": "A chemical change because iron atoms reacted with oxygen and water to form a completely new compound (hydrated iron(III) oxide) that cannot be reversed by physical means.",
                            "explanation": "Correct! At the macroscopic level, a new reddish-brown substance appears. At the submicroscopic level, iron atoms transfer electrons to oxygen in the presence of water to form hydrated iron(III) oxide. Because a new chemical substance is formed with new bonds, it is an irreversible chemical change."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check: Identifying Physical Changes",
                        "content": {
                            "question": "Which of the following processes represents a purely physical change?",
                            "options": [
                                "Baking a wheat flour cake in an oven",
                                "Melting yellow sulfur powder in a test tube",
                                "Souring of fresh milk left at room temperature",
                                "Rusting of an iron bicycle frame"
                            ],
                            "answer": "Melting yellow sulfur powder in a test tube",
                            "explanation": "Correct! Melting sulfur is a change of physical state from solid to liquid; no new chemical bonds are broken or created, and liquid sulfur solidifies back to yellow solid upon cooling. Baking, souring milk, and rusting produce entirely new chemical substances."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 2: Branches and Careers in Chemistry
        # =====================================================================
        {
            "unit_order": 2,
            "unit_name": "Branches and Careers in Chemistry",
            "unit_description": "Explore the six primary branches of Chemistry (Organic, Inorganic, Physical, Analytical, Biochemistry, Industrial), career opportunities in Kenyan and global industry, and breaking gender stereotypes in STEM.",
            "lesson_title": "Branches and Careers in Chemistry",
            "pages": [
                [
                    {
                        "type": "suggested_image",
                        "title": "Chemistry: The Central Science",
                        "content": {
                            "title": "Chemistry: The Central Science",
                            "caption": "Modern chemical analytical laboratory equipped with spectrophotometers and precision titration setups."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Chemistry Branches & Careers",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Distinguish the **six major branches of Chemistry**: Organic, Inorganic, Physical, Analytical, Biochemistry, and Industrial.",
                                "Connect specific branches of chemistry to high-impact **career pathways in Kenya** (KEBS, KRA, NEMA, healthcare, agronomy).",
                                "Analyze how modern chemical science operates in industrial manufacturing and consumer protection.",
                                "Debunk outdated gender stereotypes and promote equal participation in STEM fields."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Chemistry as the Central Science",
                        "content": {
                            "title": "Why Chemistry Connects All Natural Sciences",
                            "text": "Chemistry is often celebrated as the **'Central Science'** because it provides the foundational bridge connecting physics (the study of matter, energy, and fundamental forces) with biology (the study of living organisms), geology (the study of earth and rocks), and environmental science.\n\nBecause the scope of chemical interactions is so vast—from single electron transfers in a smartphone battery to the complex enzyme synthesis in human cells—chemists specialize into six core disciplines."
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "The Six Pillars of Chemistry",
                        "content": {
                            "title": "Core Disciplines of Chemical Science",
                            "text": "1. **Organic Chemistry**: The study of carbon-based compounds (excluding simple carbonates, hydrogen carbonates, and carbon oxides), forming the basis of all life, petroleum fuels, plastics, and pharmaceuticals.\n2. **Inorganic Chemistry**: The study of non-carbon elements, minerals, metals, semiconductors, and synthetic coordination complexes.\n3. **Physical Chemistry**: The study of underlying physical principles governing chemical systems, including thermodynamics, reaction kinetics, electrochemistry, and spectroscopy.\n4. **Analytical Chemistry**: The qualitative (identifying *what* is present) and quantitative (determining *how much* is present) analysis of chemical substances.\n5. **Biochemistry**: The chemical processes occurring within living organisms, focusing on macromolecules like proteins, lipids, nucleic acids (DNA/RNA), and metabolic enzymes.\n6. **Industrial Chemistry**: The transformation of raw natural resources (crude oil, limestone, ores) into high-value manufactured products on an industrial scale."
                        }
                    },
                    {
                        "type": "comparison_table",
                        "title": "Summary Matrix: Branches, Core Focus, and Everyday Applications",
                        "content": {
                            "headers": ["Branch", "Core Focus", "Everyday Application", "Sample Career"],
                            "rows": [
                                ["Organic Chemistry", "Carbon compounds, hydrocarbons, polymers", "Plastics, synthetic fabrics, petroleum fuels", "Petrochemical Chemist"],
                                ["Inorganic Chemistry", "Metals, minerals, non-carbon salts", "Mining, computer silicon chips, metallurgy", "Materials Scientist"],
                                ["Physical Chemistry", "Rates, energy shifts, thermodynamics", "Battery design, solar photovoltaics, fuel cells", "Electrochemist"],
                                ["Analytical Chemistry", "Identification and precision measurement", "Water quality testing, pesticide residue monitoring", "Quality Assurance Chemist (KEBS)"],
                                ["Biochemistry", "Macromolecules and living cell pathways", "Vaccines, pharmaceutical drug design, diagnostics", "Clinical Biochemist"],
                                ["Industrial Chemistry", "Large-scale factory synthesis", "Manufacturing soap, cement, paints, fertilizers", "Chemical Process Engineer"]
                            ]
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "Impactful Chemistry Careers in Kenya and Globally",
                        "content": {
                            "title": "Applying Chemistry in the Public and Private Sectors",
                            "text": "Studying Chemistry opens dynamic career opportunities across Kenya's economy:\n\n- **Quality Assurance Chemist at KEBS (Kenya Bureau of Standards)**: Inspects manufactured foods, beverages, construction materials, and cosmetics to verify safety standards and compliance.\n- **Customs & Revenue Chemist at KRA (Kenya Revenue Authority)**: Tests imported goods and chemical raw materials to determine purity, tariff classification, and detect hazardous contraband.\n- **Environmental Chemist at NEMA**: Monitors water quality in lakes, rivers, and aquifers, tracking heavy metal contamination and designing industrial effluent treatment protocols.\n- **Pharmaceutical Formulation Chemist**: Develops life-saving medications, antibiotics, and pediatric suspensions in pharmaceutical manufacturing plants.\n- **Agronomic & Soil Chemist**: Formulates optimized NPK and CAN fertilizers, tests soil acidity/alkalinity for smallholders, and develops environmentally safe biopesticides."
                        }
                    },
                    {
                        "type": "definition_card",
                        "title": "Key Role: Analytical Chemist",
                        "content": {
                            "term": "Analytical Chemist",
                            "definition": "A professional scientist who uses advanced laboratory instruments (chromatography, spectrometry, titrimetry) to determine the exact chemical composition and purity of substances.",
                            "example": "Testing municipal drinking water for parts-per-billion concentrations of lead or bacterial contamination."
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "Breaking Gender Stereotypes: Equal Excellence in Chemistry",
                        "content": {
                            "title": "Women and Men Leading Chemical Innovation",
                            "text": "Historically, outdated social biases suggested that 'hard sciences' like chemical engineering, materials science, and industrial chemistry were fields exclusively suited for men, while women were steered away from physical sciences.\n\nIn modern Kenya, this stereotype has been completely dismantled! Women scientists and chemical engineers lead cutting-edge laboratories, direct major manufacturing enterprises, head environmental regulatory agencies, and pioneer renewable energy research across Africa. Academic ability, curiosity, logical reasoning, and perseverance determine scientific success—not gender."
                        }
                    },
                    {
                        "type": "callout",
                        "title": "Inspiring Future Chemists",
                        "content": {
                            "title": "Science Knows No Gender",
                            "text": "Whether conducting deep molecular analysis in a clinical laboratory or running a 50-tonne cement kiln in an industrial plant, Kenyan women and men contribute equally to scientific innovation. Every learner in Grade 10 has the full potential to become a world-class chemist!"
                        }
                    }
                ],
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check: Environmental Analysis Career",
                        "content": {
                            "question": "Otieno wishes to work with NEMA to test water samples from Lake Victoria, specifically determining the exact parts-per-million concentration of agricultural pesticide residues. Which branch of chemistry will Otieno primarily utilize, and what is his professional title?",
                            "options": [
                                "Organic Chemistry — Organic Farmer",
                                "Analytical Chemistry — Environmental Chemist / Analytical Chemist",
                                "Inorganic Chemistry — Mining Engineer",
                                "Physical Chemistry — Thermochemist"
                            ],
                            "answer": "Analytical Chemistry — Environmental Chemist / Analytical Chemist",
                            "explanation": "Correct! Analytical chemistry is the specialized branch dedicated to identifying substances (qualitative) and measuring their exact concentrations (quantitative). Working on pollution monitoring makes Otieno an Environmental or Analytical Chemist."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check: Industrial Manufacturing",
                        "content": {
                            "question": "Which branch of chemistry focuses on scaling up the reaction between vegetable oils and sodium hydroxide to produce thousands of kilograms of commercial bar soap in a factory?",
                            "options": [
                                "Biochemistry",
                                "Inorganic Chemistry",
                                "Industrial Chemistry",
                                "Geochemistry"
                            ],
                            "answer": "Industrial Chemistry",
                            "explanation": "Correct! Industrial chemistry applies chemical principles and engineering to manufacture commercial goods (like soaps, fertilizers, paints, and cement) on an economic, large-scale industrial level."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 3: Chemistry in Daily Life, Industry, and the Environment
        # =====================================================================
        {
            "unit_order": 3,
            "unit_name": "Chemistry in Daily Life, Industry, and the Environment",
            "unit_description": "Examine how Chemistry supports agriculture, medicine, textiles, energy, household hygiene, and municipal water purification. Practice consumer label analysis and quality standard verification (KEBS).",
            "lesson_title": "Chemistry in Daily Life, Industry, and the Environment",
            "pages": [
                [
                    {
                        "type": "suggested_image",
                        "title": "Chemistry All Around Us",
                        "content": {
                            "title": "Chemistry All Around Us",
                            "caption": "Agricultural fertilizers, medicines, and everyday consumer products synthesized through chemical science."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Chemistry in Society",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Evaluate the crucial contributions of Chemistry in **food security, healthcare, transport, and manufacturing**.",
                                "Explain the multi-stage chemical and physical processes in **municipal water treatment**.",
                                "Conduct practical **consumer label analysis** to locate KEBS marks, expiry dates, and hazard warnings.",
                                "Analyze environmental trade-offs and sustainable green chemistry practices."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "How Chemistry Shapes Modern Living",
                        "content": {
                            "title": "The Invisible Engine of Modern Society",
                            "text": "Imagine waking up in a world without Chemistry: there would be no soaps or toothpaste for personal hygiene, no synthetic fabrics (polyester or nylon) for clothing, no antibiotics or pain relievers in hospitals, no water treatment plants to deliver safe drinking water, and no fertilizers to sustain national food security!\n\nChemical science touches every sphere of modern human existence."
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "Key Sectors Driven by Chemical Science",
                        "content": {
                            "title": "Everyday Sectors and Their Chemical Foundations",
                            "text": "- **Agriculture & Food**: Synthetic fertilizers (DAP, Urea, CAN) supply essential nitrogen, phosphorus, and potassium. Food preservatives prevent microbial decomposition, extending food shelf life.\n- **Healthcare & Pharmaceuticals**: Antacids neutralize excess stomach acid ($\\text{HCl}$). Antibiotics and vaccines protect millions from infectious diseases.\n- **Clothing & Materials**: Petrochemical polymers like polyester, acrylic, and nylon provide durable textiles, colored with chemical dyes that bind strongly to fabric fibers.\n- **Household Products**: Soaps and synthetic detergents break down oils and dirt via saponification and surfactant chemistry.\n- **Energy & Transport**: Fractional distillation of crude oil provides petrol, diesel, and aviation kerosene. Lithium-ion batteries convert chemical potential energy directly into electrical power."
                        }
                    },
                    {
                        "type": "definition_card",
                        "title": "Key Process: Saponification",
                        "content": {
                            "term": "Saponification",
                            "definition": "The chemical reaction in which fats or oils (esters of glycerol and fatty acids) are hydrolyzed with an alkali (like sodium hydroxide or potassium hydroxide) to produce soap and glycerol.",
                            "example": "Reacting palm oil with sodium hydroxide solution to produce solid bar soap."
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "Municipal Water Treatment: A Multi-Stage Chemical Workflow",
                        "content": {
                            "title": "Making Water Safe for Human Consumption",
                            "text": "Access to clean water is essential for public health. Municipal water treatment facilities (such as Nairobi Water and county water companies) employ a 6-stage physical and chemical sequence:\n\n1. **Screening**: Coarse grids trap large floating debris (branches, leaves, plastic).\n2. **Coagulation & Flocculation**: Alum (aluminium sulfate) is added; it neutralizes charges on suspended clay particles, causing them to aggregate into heavier clumps called 'flocs'.\n3. **Sedimentation**: Heavy flocs settle to the floor of large sedimentation basins by gravity.\n4. **Filtration**: Water passes through layers of fine sand and gravel to trap microscopic particles.\n5. **Disinfection (Chlorination)**: Chlorine gas ($\\text{Cl}_2$) or sodium hypochlorite is dosed to eliminate pathogenic bacteria, viruses, and waterborne parasites.\n6. **pH Adjustment & Storage**: Lime or soda ash is added to neutralize acidity and prevent pipe corrosion before distribution."
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Step-by-Step Municipal Water Purification Process",
                        "content": {
                            "title": "Step-by-Step Municipal Water Purification Process",
                            "caption": "From raw river water intake through coagulation, sedimentation, sand filtration, and chlorination to safe tap water."
                        }
                    }
                ],
                [
                    {
                        "type": "step_process",
                        "title": "Practical Activity: Consumer Label Analysis",
                        "content": {
                            "title": "How to Inspect Chemical Product Labels",
                            "steps": [
                                "1. **Check the Mark of Quality**: Look for the official **KEBS Standardization Mark** verifying regulatory testing.",
                                "2. **Verify Expiry & Batch Dates**: Ensure active ingredients have not decomposed into inactive or toxic degradation products.",
                                "3. **Identify Active Ingredients**: Read the chemical names of active compounds (e.g., Sodium Hypochlorite in bleach).",
                                "4. **Read Hazard Symbols & Warnings**: Check for international hazard pictograms (Flammable, Corrosive, Toxic, Irritant) and keep out of reach of children."
                            ]
                        }
                    },
                    {
                        "type": "common_misconception",
                        "title": "Consumer Safety Warning",
                        "content": {
                            "misconception": "If a cleaning product has a pleasant scent, it cannot be toxic or corrosive.",
                            "correction": "Fragrances are often added to mask harsh chemical odors. Corrosive acids (like hydrochloric acid in toilet cleaners) or strong alkalis remain highly dangerous regardless of fragrance. Always wear protective gloves!",
                            "why_it_matters": "Proper understanding of hazard labels prevents severe household chemical burns and accidental poisonings."
                        }
                    }
                ],
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check: Uncertified Product Safety",
                        "content": {
                            "question": "Atieno bought a bottle of liquid disinfectant from an informal street market. The bottle has no KEBS quality mark, no manufacturer address, and no expiry date. What is the correct consumer assessment of this product?",
                            "options": [
                                "It is completely safe as long as it has a strong chemical smell.",
                                "It is unsafe because uncertified chemicals may contain incorrect concentrations or hazardous contaminants; consumers have a right to verified safety and a responsibility to purchase only certified products.",
                                "It should be boiled for 10 minutes to make it safe for skin application.",
                                "It is automatically superior because informal products have fewer synthetic chemicals."
                            ],
                            "answer": "It is unsafe because uncertified chemicals may contain incorrect concentrations or hazardous contaminants; consumers have a right to verified safety and a responsibility to purchase only certified products.",
                            "explanation": "Correct! Without a KEBS mark, the product has not passed standard efficacy or toxicology testing. Products without expiry dates may contain degraded, harmful compounds. Consumers have the right to safety and the responsibility to reject uncertified products."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check: Water Chlorination Purpose",
                        "content": {
                            "question": "Why is chlorine gas or sodium hypochlorite added in the final stages of municipal water purification?",
                            "options": [
                                "To cause suspended clay particles to settle to the bottom of the tank",
                                "To destroy disease-causing pathogenic bacteria and prevent waterborne epidemics (e.g., cholera, typhoid)",
                                "To adjust the water colour and make it completely clear",
                                "To add essential dietary minerals for bone growth"
                            ],
                            "answer": "To destroy disease-causing pathogenic bacteria and prevent waterborne epidemics (e.g., cholera, typhoid)",
                            "explanation": "Correct! Chlorine is a powerful oxidizing disinfectant that destroys the cell membranes and enzymes of harmful pathogenic microorganisms, guaranteeing microbiological safety during distribution."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 4: Drugs, Substance Use, Consumer Rights, and Safe Learning
        # =====================================================================
        {
            "unit_order": 4,
            "unit_name": "Drugs, Substance Use, Consumer Rights, and Safe Learning",
            "unit_description": "Define drugs, prescriptions, and dosages. Analyze the physiological and social hazards of substance abuse, understand consumer rights (PPB regulation), and promote safe learning environments.",
            "lesson_title": "Drugs, Substance Use, Consumer Rights, and Safe Learning",
            "pages": [
                [
                    {
                        "type": "suggested_image",
                        "title": "Responsible Medicine Use",
                        "content": {
                            "title": "Responsible Medicine Use",
                            "caption": "Prescription pharmaceuticals dispensed by a licensed healthcare professional with precise dosage instructions."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Drug Chemistry & Safety",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Define **drug**, **prescription**, **dosage**, and **side effects** from a chemical perspective.",
                                "Analyze the physiological, psychological, and social risks of **drug and substance abuse**.",
                                "Navigate the **safe medicine decision pathway** from clinical diagnosis to safe disposal.",
                                "Promote consumer protection through the **Pharmacy and Poisons Board (PPB)** and foster supportive, stigma-free peer environments."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Understanding the Chemistry of Drugs",
                        "content": {
                            "title": "Medicines vs. Substance Abuse",
                            "text": "Every medicine you take is a precisely synthesized chemical formulation designed to interact with biological receptors in your body to alleviate pain, fight infections, or correct metabolic imbalances.\n\nHowever, because chemical compounds exert powerful physiological effects, using them without professional medical guidance transforms life-saving therapies into dangerous toxins."
                        }
                    },
                    {
                        "type": "definition_card",
                        "title": "Key Terminology: Drugs & Prescriptions",
                        "content": {
                            "term": "Prescription and Dosage",
                            "definition": "A **prescription** is a legal written directive from a licensed medical doctor specifying the exact medicine, strength, and administration route. A **dosage** is the specific quantity and frequency of medication required to produce therapeutic healing without causing toxicity.",
                            "example": "Taking 500 mg of amoxicillin every 8 hours for exactly 7 days to cure a bacterial infection."
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "Physiological and Social Hazards of Substance Abuse",
                        "content": {
                            "title": "How Substance Misuse Impacts the Body and Brain",
                            "text": "When chemical substances (alcohol, tobacco, khat/miraa, cannabis, non-prescribed pharmaceuticals) are misused, they cause severe damage:\n\n- **Addiction & Chemical Dependence**: Substances alter neurotransmitter levels (such as dopamine) in the brain, driving compulsive cravings and severe withdrawal symptoms.\n- **Organ Damage**: Chronic alcohol consumption destroys hepatocytes, causing liver cirrhosis; inhaling tobacco smoke deposits carcinogenic tar and destroys alveolar lung tissue.\n- **Mental Health Breakdown**: Substance misuse exacerbates clinical depression, severe anxiety disorders, paranoia, and cognitive decline.\n- **Social & Academic Ruin**: Leads to school dropouts, financial destitution, interpersonal conflict, and legal repercussions."
                        }
                    },
                    {
                        "type": "definition_card",
                        "title": "Key Term: Side Effects",
                        "content": {
                            "term": "Side Effect",
                            "definition": "A secondary, typically undesirable effect of a chemical drug or medical therapy that occurs alongside its primary therapeutic benefit.",
                            "example": "Drowsiness caused by antihistamines, or mild nausea from an antibiotic."
                        }
                    }
                ],
                [
                    {
                        "type": "suggested_diagram",
                        "title": "The 7-Step Safe Medicine Decision Pathway",
                        "content": {
                            "title": "The 7-Step Safe Medicine Decision Pathway",
                            "caption": "A clinical and consumer decision workflow ensuring responsible medication use and consumer protection."
                        }
                    },
                    {
                        "type": "step_process",
                        "title": "Protocol for Responsible Medication Use",
                        "content": {
                            "title": "Step-by-Step Medication Safety",
                            "steps": [
                                "1. **Medical Consultation**: Always be examined by a qualified physician rather than self-diagnosing.",
                                "2. **Obtain Official Prescription**: Receive a clear dosage and duration schedule.",
                                "3. **Purchase from Licensed Pharmacies**: Ensure facility is certified by the Pharmacy and Poisons Board (PPB).",
                                "4. **Verify Container & Expiry**: Inspect seals, expiration date, and packaging integrity.",
                                "5. **Follow Exact Dosage Schedule**: Never double a missed dose or exceed prescribed limits.",
                                "6. **Complete the Entire Course**: Never stop taking antibiotics prematurely, even if symptoms subside, to prevent drug resistance.",
                                "7. **Safe Storage**: Keep medicines locked in a cool, dry place away from children."
                            ]
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "Consumer Rights and Institutional Protection in Kenya",
                        "content": {
                            "title": "The Pharmacy and Poisons Board (PPB)",
                            "text": "In Kenya, the **Pharmacy and Poisons Board (PPB)** is the national regulatory authority established under Cap 244 of the Laws of Kenya to regulate the manufacture, importation, distribution, and sale of pharmaceuticals and medical devices.\n\n### Your Consumer Rights & Responsibilities:\n- **Right to Safe Healthcare**: Right to receive unadulterated, genuine, and properly labeled medications.\n- **Right to Information**: Right to full disclosure regarding potential side effects and drug interactions.\n- **Responsibility to Seek Help**: If a classmate or friend shows signs of substance abuse, recognize that substance dependence is a medical disorder requiring compassionate clinical intervention, not moral condemnation or social stigmatization."
                        }
                    },
                    {
                        "type": "callout",
                        "title": "Promoting a Stigma-Free School Environment",
                        "content": {
                            "title": "Support, Don't Stigmatize",
                            "text": "Addiction is a complex biological disease. Encourage affected peers to reach out to school guidance counselors, parents, or healthcare workers. Creating a supportive, informed school community saves lives!"
                        }
                    }
                ],
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check: Sharing Prescription Medications",
                        "content": {
                            "question": "Peter has a dry, painful cough. His friend suggests: 'Take my sister's leftover prescription cough syrup, and take a triple dose so you recover before the football match.' Why is this advice dangerous, and what should Peter do?",
                            "options": [
                                "It is good advice because prescription syrup is stronger than over-the-counter medicine.",
                                "It is dangerous because sharing prescriptions bypasses proper diagnosis, different individuals require specific dosages based on physiology, and taking a triple dose risks toxic overdose; Peter should visit a qualified medical professional.",
                                "It is safe provided Peter drinks plenty of milk afterwards.",
                                "It is only dangerous if the syrup has been open for more than one year."
                            ],
                            "answer": "It is dangerous because sharing prescriptions bypasses proper diagnosis, different individuals require specific dosages based on physiology, and taking a triple dose risks toxic overdose; Peter should visit a qualified medical professional.",
                            "explanation": "Correct! Prescription medications must never be shared. A symptom (cough) can arise from viral infections, bacterial pneumonia, or allergies. Self-medicating with another person's prescription and exceeding dosage limits causes severe toxicity and organ damage."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check: National Pharmaceutical Regulator",
                        "content": {
                            "question": "Which national statutory body in Kenya is legally mandated to regulate pharmaceuticals, veterinary drugs, and poison distribution to protect public health?",
                            "options": [
                                "Kenya National Highways Authority (KeNHA)",
                                "Pharmacy and Poisons Board (PPB)",
                                "Kenya Revenue Authority (KRA)",
                                "National Environment Management Authority (NEMA)"
                            ],
                            "answer": "Pharmacy and Poisons Board (PPB)",
                            "explanation": "Correct! The Pharmacy and Poisons Board (PPB) regulates the safety, efficacy, and quality of medicines, medical devices, and health technologies in Kenya."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 5: Chemistry Communication and Inquiry Project
        # =====================================================================
        {
            "unit_order": 5,
            "unit_name": "Chemistry Communication and Inquiry Project",
            "unit_description": "Master scientific inquiry through the Claim-Evidence-Reasoning (CER) framework. Plan, execute, and evaluate a community health awareness campaign with structured peer assessment rubrics.",
            "lesson_title": "Chemistry Communication and Inquiry Project",
            "pages": [
                [
                    {
                        "type": "suggested_image",
                        "title": "Communicating Science to Society",
                        "content": {
                            "title": "Communicating Science to Society",
                            "caption": "Students collaborating on an evidence-based science inquiry poster for peer and community presentation."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Scientific Communication & Inquiry",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Apply the **Claim-Evidence-Reasoning (CER)** framework to structure rigorous scientific arguments.",
                                "Execute a collaborative **Inquiry Project** creating an evidence-based substance abuse awareness poster.",
                                "Evaluate project outcomes using standard **CBC competency rubrics** (Exceeds, Meets, Approaches, Below).",
                                "Synthesize key foundations across Topic 1.1 in preparation for atomic theory and structure."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The Power of Scientific Communication",
                        "content": {
                            "title": "Why Science Must Be Communicated Clearly",
                            "text": "Scientific discovery does not end in the laboratory. The ultimate value of Chemistry comes from sharing findings accurately and ethically with society—helping farmers choose the right fertilizer, guiding doctors on drug efficacy, and educating communities on health risks."
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "Structuring Scientific Arguments with CER",
                        "content": {
                            "title": "The Three Pillars of Scientific Explanation",
                            "text": "Whenever you answer an inquiry question or present experimental results, use the **CER Model**:\n\n1. **Claim**: A precise, direct statement answering the central scientific question (e.g., *'Leaving an unpainted iron gate exposed to coastal air causes a chemical change.'*)\n2. **Evidence**: Objective data, measurements, or observable facts supporting the claim (e.g., *'The shiny grey iron turned into a brittle reddish-brown flaky solid with increased mass, and could not be restored by cooling.'*)\n3. **Reasoning**: A logical justification explaining *how* the scientific principles connect the evidence to the claim (e.g., *'Because iron atoms bonded with oxygen and water to create a completely new chemical compound—hydrated iron(III) oxide—with new physical and chemical properties, this satisfies the definition of a chemical change.'*)"
                        }
                    },
                    {
                        "type": "definition_card",
                        "title": "Key Framework: CER",
                        "content": {
                            "term": "Claim-Evidence-Reasoning (CER)",
                            "definition": "An instructional argumentation structure that trains learners to state a testable conclusion (Claim), substantiate it with empirical observations (Evidence), and justify it using underlying scientific laws (Reasoning).",
                            "example": "Claim: Ice melting is a physical change. Evidence: It reverses to ice upon cooling. Reasoning: No new molecular bonds were formed."
                        }
                    }
                ],
                [
                    {
                        "type": "step_process",
                        "title": "Inquiry Project: Substance Use Awareness Poster",
                        "content": {
                            "title": "Step-by-Step Project Execution",
                            "steps": [
                                "1. **Form Groups & Assign Roles**: Form teams of 3–4 learners. Assign roles: Lead Researcher, Content Writer, Graphic Designer, and Presenter.",
                                "2. **Inquiry Research**: Gather verified data from reputable public health sources (WHO, Ministry of Health, NACADA, PPB).",
                                "3. **Apply the CER Framework**: Formulate 2 key evidence-based arguments debunking common drug myths.",
                                "4. **Design the Poster**: Create a clear, engaging, stigma-free visual layout highlighting physiological consequences, consumer rights, and emergency help lines.",
                                "5. **Class Presentation & Peer Review**: Present the poster in 3 minutes, inviting constructive peer evaluation."
                            ]
                        }
                    },
                    {
                        "type": "comparison_table",
                        "title": "Inquiry Project Rubric (Self & Peer Assessment)",
                        "content": {
                            "headers": ["Assessment Criterion", "Exceeds Expectations", "Meets Expectations", "Needs Improvement"],
                            "rows": [
                                ["Scientific Accuracy", "All facts 100% accurate, cited from official bodies (PPB/NACADA/WHO)", "Accurate with minor omissions; relies on verified sources", "Contains scientific misconceptions or unsubstantiated claims"],
                                ["Use of CER Framework", "Explicit, seamless integration of Claim, Evidence, and Chemical Reasoning", "CER structure present and logically coherent", "Arguments lack supporting empirical evidence or chemical reasoning"],
                                ["Visual Clarity & Design", "Exceptional layout, clean typography, engaging non-sensational graphics", "Clear, legible layout with appropriate illustrations", "Cluttered, difficult to read, or uses sensationalized images"],
                                ["Collaboration & Presentation", "Dynamic team synergy; all members present and answer questions confidently", "Good teamwork and clear verbal presentation", "Unequal participation; presentation lacks structure"]
                            ]
                        }
                    }
                ],
                [
                    {
                        "type": "summary",
                        "title": "Topic 1.1 Master Summary & Key Takeaways",
                        "content": {
                            "title": "Key Foundations Mastered in Topic 1.1",
                            "summary_points": [
                                "**Matter & Chemistry**: Chemistry investigates matter, its properties, composition, structure, and energetic transformations.",
                                "**The Chemical Triplet**: Chemists operate across Macroscopic observations, Submicroscopic particle mechanics, and Symbolic equations.",
                                "**Physical vs. Chemical Changes**: Physical changes alter state/shape without new substances; chemical changes create brand new substances through atomic rearrangement.",
                                "**Branches & Careers**: Organic, Inorganic, Physical, Analytical, Biochemistry, and Industrial Chemistry drive diverse national careers (KEBS, KRA, NEMA, hospitals, manufacturing).",
                                "**Consumer Protection & Safety**: Understanding KEBS marks, PPB regulations, prescription compliance, and evidence-based CER communication safeguards public health."
                            ]
                        }
                    },
                    {
                        "type": "transition",
                        "title": "Looking Ahead: The Subatomic Realm",
                        "content": {
                            "title": "Next Step: Topic 1.2 — The Atom",
                            "text": "Now that you have built a strong foundation in the language and scope of Chemistry, we take a deep dive into the building blocks of all matter: **The Atom**! You will explore Dalton's theory, Rutherford's revolutionary gold foil experiment, subatomic particles, isotopes, and modern $s$ and $p$ orbital notation."
                        }
                    }
                ],
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check: Applying the CER Framework",
                        "content": {
                            "question": "A learner claims: 'Adding effervescent antacid tablets to water is a chemical change.' Which statement provides the most complete and scientifically sound REASONING component of the CER argument?",
                            "options": [
                                "Reasoning: Because bubbles formed immediately and the tablet disappeared from sight.",
                                "Reasoning: Because the reaction between solid sodium hydrogen carbonate and citric acid in water breaks existing bonds to generate new covalent molecules of carbon dioxide gas ($CO_2$), water, and sodium citrate, satisfying the definition of a chemical reaction.",
                                "Reasoning: Because antacids are manufactured by pharmaceutical companies.",
                                "Reasoning: Because the water became cold during the experiment."
                            ],
                            "answer": "Reasoning: Because the reaction between solid sodium hydrogen carbonate and citric acid in water breaks existing bonds to generate new covalent molecules of carbon dioxide gas ($CO_2$), water, and sodium citrate, satisfying the definition of a chemical reaction.",
                            "explanation": "Correct! A complete CER Reasoning component explains *why* the evidence proves the claim by linking observations to submicroscopic chemical principles—specifically the breaking and forming of chemical bonds to create new substances."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check: Scientific Inquiry Quality",
                        "content": {
                            "question": "When designing a public health campaign poster on drug and substance abuse, what approach produces the most effective and respectful learning impact?",
                            "options": [
                                "Using exaggerated, frightening images to shock peers into compliance",
                                "Presenting evidence-based chemical and physiological facts, promoting consumer rights, debunking myths using CER, and listing licensed medical help resources without stigmatizing affected individuals",
                                "Listing rumors and gossip about individuals in the school community",
                                "Focusing solely on punishment and legal penalties"
                            ],
                            "answer": "Presenting evidence-based chemical and physiological facts, promoting consumer rights, debunking myths using CER, and listing licensed medical help resources without stigmatizing affected individuals",
                            "explanation": "Correct! High-quality scientific communication relies on evidence-based health promotion, factual physiological data, and supportive, stigma-free guidance."
                        }
                    }
                ]
            ]
        }
    ]

@transaction.atomic
def ingest_topic1():
    print("=" * 80)
    print("INGESTING GRADE 10 CHEMISTRY — TOPIC 1: INTRODUCTION TO CHEMISTRY")
    print("=" * 80)

    # 1. Resolve Hierarchy
    cbc = Curriculum.objects.filter(name__icontains="CBC").first()
    if not cbc:
        raise ValueError("Curriculum CBC not found!")
    
    grade10 = Grade.objects.filter(curriculum=cbc, level=10).first()
    if not grade10:
        raise ValueError("Grade 10 not found under CBC!")

    chem = Subject.objects.filter(grade=grade10, id=5).first() or Subject.objects.filter(grade=grade10, name__icontains="Chem").first()
    if not chem:
        raise ValueError("Chemistry subject not found under Grade 10 CBC!")

    print(f"Target Subject: [{chem.id}] {chem.name} (Grade: {grade10.name}, Curr: {cbc.name})")

    # 2. Resolve or Create Topic 1
    topic, created = Topic.objects.get_or_create(
        subject=chem,
        order=1,
        defaults={
            "name": "Introduction to Chemistry",
            "description": "Establish Chemistry as the central study of matter, properties, composition, structure, changes, and energy interactions. Explore the chemical triplet, branches, careers, consumer awareness, and scientific inquiry."
        }
    )
    if not created:
        topic.name = "Introduction to Chemistry"
        topic.description = "Establish Chemistry as the central study of matter, properties, composition, structure, changes, and energy interactions. Explore the chemical triplet, branches, careers, consumer awareness, and scientific inquiry."
        topic.save()
    print(f"Resolved Topic 1: [{topic.id}] {topic.name}")

    # 3. Ingest Lessons & Blocks
    curriculum_data = build_topic1_curriculum()

    for unit_data in curriculum_data:
        unit_order = unit_data["unit_order"]
        unit_name = unit_data["unit_name"]
        unit_desc = unit_data["unit_description"]
        lesson_title = unit_data["lesson_title"]
        pages = unit_data["pages"]

        # Resolve Learning Unit
        learning_unit, u_created = LearningUnit.objects.get_or_create(
            topic=topic,
            order=unit_order,
            defaults={
                "name": unit_name,
                "description": unit_desc
            }
        )
        if not u_created:
            learning_unit.name = unit_name
            learning_unit.description = unit_desc
            learning_unit.save()

        # Resolve Lesson (Published, Version 1)
        lesson = Lesson.objects.filter(topic=topic, learning_unit=learning_unit).first()
        if not lesson:
            lesson = Lesson.objects.create(
                topic=topic,
                learning_unit=learning_unit,
                title=lesson_title,
                status="published",
                version=1
            )
            print(f"  [Created Lesson] ID {lesson.id}: {lesson_title}")
        else:
            lesson.title = lesson_title
            lesson.status = "published"
            lesson.version = 1
            lesson.save()
            print(f"  [Updated Lesson] ID {lesson.id}: {lesson_title}")

        # Clear old blocks for idempotent refresh
        lesson.blocks.all().delete()

        # Create structured blocks
        global_order = 0
        for page_idx, page_blocks in enumerate(pages, start=1):
            page_title = page_blocks[0].get("title", f"Page {page_idx}")
            for comp_idx, block_def in enumerate(page_blocks, start=1):
                global_order += 1
                b_type = block_def["type"]
                b_title = block_def["title"]
                b_content = clean_dict(block_def["content"])

                LessonBlock.objects.create(
                    lesson=lesson,
                    block_type=b_type,
                    component_type=b_type,
                    title=b_title,
                    page_number=page_idx,
                    page_title=page_title,
                    component_order=comp_idx,
                    order=global_order,
                    content=b_content
                )

        print(f"    -> Ingested {len(pages)} Pages, {global_order} Blocks for Lesson [{lesson.id}]")

    print("\nSUCCESS: Topic 1 Ingestion Completed Idempotently!")

if __name__ == "__main__":
    ingest_topic1()
