"""
VLearn CBC Grade 10 Agriculture — Topic 10: General Animal Health
Production Ingestion Engine (Deep Senior Secondary Pedagogical Edition)

Curriculum: CBC (ID: 5)
Grade: Grade 10 (ID: 5, Level: 10)
Subject: Agriculture
Topic: General Animal Health (Topic Order: 10)

Decomposed into 12 Learning Units & 12 Published Lessons:
  1. Benefits of Healthy Animals in Livestock Production (4 Pages, 9 Blocks)
  2. General Signs of Ill Health in Livestock (4 Pages, 9 Blocks)
  3. Identifying Signs of Sickness in Cattle and Goats (4 Pages, 9 Blocks)
  4. Identifying Signs of Sickness in Sheep and Pigs (4 Pages, 9 Blocks)
  5. Identifying Signs of Sickness in Poultry and Rabbits (4 Pages, 9 Blocks)
  6. Preventative Measures I (Nutrition, Housing, and Sanitation) (4 Pages, 9 Blocks)
  7. Preventative Measures II (Biosecurity and Vaccination) (4 Pages, 9 Blocks)
  8. Disease Control Measures (Parasites, Isolation, and Treatment) (4 Pages, 9 Blocks)
  9. Housing, Hygiene, and Waste Management (4 Pages, 9 Blocks)
  10. Routine Health Maintenance and Daily Care (4 Pages, 9 Blocks)
  11. Designing an Animal Health Plan and Awareness Campaign (4 Pages, 9 Blocks)
  12. Sub-strand Review and Performance Task (8 Pages, 17 Blocks)
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

def build_topic10_curriculum():
    """Returns the comprehensive pedagogical page and block structure for Grade 10 Topic 10: General Animal Health."""
    return [
        # =====================================================================
        # LESSON 1: Benefits of Healthy Animals in Livestock Production
        # =====================================================================
        {
            "unit_order": 1,
            "unit_name": "Benefits of Healthy Animals in Livestock Production",
            "unit_description": "Definition of animal health; Feed Conversion Efficiency; high product quality (low somatic cells, pathogen-free eggs); economic impact of morbidity vs mortality.",
            "lesson_title": "The Biological and Economic Dimensions of Optimal Animal Health",
            "pages": [
                [
                    {
                        "type": "suggested_image",
                        "title": "Healthy Grass-Fed Cattle Grazing on Lush Pasture",
                        "content": {
                            "title": "Healthy Grass-Fed Cattle Grazing on Lush Pasture",
                            "caption": "A herd of robust, disease-free beef cattle actively grazing on open rangeland, demonstrating optimal physiological vitality and maximum feed conversion efficiency."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Benefits of Animal Health",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Define **animal health** in terms of physiological balance and bodily homeostasis.",
                                "Analyze the **economic benefits of keeping herds disease-free** (high Feed Conversion Ratio, prolonged longevity).",
                                "Distinguish between **morbidity** (production loss during illness) and **mortality** (death loss).",
                                "Evaluate the relationship between **animal health and consumer food safety**."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Defining Animal Health and Homeostasis",
                        "content": {
                            "title": "The State of Optimal Biological Function",
                            "text": "**Animal health** is a state of complete physical, mental, and physiological equilibrium where all organ systems function with maximum biological efficiency.\n\n- **Beyond the Absence of Disease**: A truly healthy animal is free from latent subclinical infections, pain, nutritional deficiencies, and environmental distress.\n- **Full Genetic Realization**: Only healthy animals can express their full genetic potential for milk yield, meat gain, wool quality, and reproductive fecundity."
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "Economic and Product-Quality Dividends",
                        "content": {
                            "title": "Why Preventative Health Maximizes Agribusiness Profit",
                            "text": "1. **Superior Feed Conversion Efficiency (FCE)**: Healthy digestive systems convert expensive forage and concentrates directly into sellable protein without diverting energy toward fighting fever or repairing inflamed tissues.\n2. **Product Purity & Market Premiums**:\n- *Dairy*: Healthy udders produce milk with low Somatic Cell Counts (SCC $< 200,000\\text{ cells/mL}$) and zero antibiotic residues, qualifying for premium cooperative payouts.\n- *Poultry*: Healthy layers produce uniform, thick-shelled eggs free from *Salmonella* contamination.\n3. **Elimination of Morbidity Losses**: Subclinical disease (morbidity) halts growth, drops milk yield by $30\\text{--}50\\%$, and increases veterinary drug expenditures."
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Positive Feedback Loop of Animal Health & Agribusiness Profit",
                        "content": {
                            "title": "Positive Feedback Loop of Animal Health & Agribusiness Profit",
                            "caption": "Cyclical economic flowchart: 1 High Animal Health -> 2 Maximum Feed Conversion -> 3 Premium Product Quality -> 4 High Farm Revenues & Low Veterinary Costs."
                        }
                    }
                ],
                [
                    {
                        "type": "comparison_table",
                        "title": "Healthy Livestock Enterprise vs Diseased Herd Performance",
                        "content": {
                            "title": "Agribusiness Health Performance Matrix",
                            "headers": ["Production Parameter", "Healthy Livestock Enterprise", "Diseased Herd (Subclinical Infections)"],
                            "rows": [
                                ["Feed Conversion Ratio", "High (efficient conversion to milk/meat)", "Low (feed energy wasted fighting illness)"],
                                ["Daily Milk Yield", "Consistent peak production curve", "Sharp 30–50% drop (morbidity loss)"],
                                ["Product Quality", "Low somatic cell count; zero drug residues", "High somatic cells; condemned antibiotic milk"],
                                ["Veterinary Expenditure", "Minimal (only routine preventative vaccines)", "High emergency curative and antibiotic bills"],
                                ["Net Farmer Margin", "High profit margins and fast ROI", "Severe financial deficits and animal mortality"]
                            ]
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Core Summary: Health Benefits",
                        "content": {
                            "title": "Key Takeaways",
                            "text": "- **Animal health is complete physiological homeostasis**.\n- **Healthy animals maximize Feed Conversion Efficiency**.\n- **Preventative health eliminates morbidity losses** and high vet bills.\n- **Disease-free animals produce premium quality milk and meat**."
                        }
                    }
                ],
                [
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Economic Impact of Animal Health",
                        "content": {
                            "question": "How does maintaining optimal health in a commercial dairy herd directly increase a smallholder farmer's net profit margins?",
                            "options": [
                                "Healthy cows no longer require clean drinking water",
                                "Healthy cows have high feed conversion efficiency, producing maximum clean milk with low somatic cell counts while eliminating emergency veterinary treatment costs",
                                "Healthy cows produce pasteurized milk directly from the udder",
                                "Healthy cows stop eating expensive feed entirely"
                            ],
                            "answer": "B",
                            "explanation": "Healthy cows channel all their feed energy into milk production with high feed conversion efficiency. Furthermore, avoiding subclinical mastitis and other diseases prevents milk discarding, lowers somatic cell counts to earn premium quality bonuses, and eliminates emergency veterinary and antibiotic expenses."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 2: General Signs of Ill Health in Livestock
        # =====================================================================
        {
            "unit_order": 2,
            "unit_name": "General Signs of Ill Health in Livestock",
            "unit_description": "Early detection; anorexia; lethargy & social isolation; abnormal posture (arched back, head pressing, lameness); pyrexia vs hypothermia.",
            "lesson_title": "Universal Clinical Indicators, Behavioral Shifts, and Vital Signs of Sickness",
            "pages": [
                [
                    {
                        "type": "suggested_image",
                        "title": "Veterinarian Conducting Vital Signs Examination on Livestock",
                        "content": {
                            "title": "Veterinarian Conducting Vital Signs Examination on Livestock",
                            "caption": "A veterinary professional checking body temperature, heart rate, and respiration on cattle to diagnose early physiological symptoms of systemic infection."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: General Signs of Ill Health",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Identify **universal behavioral and physical indicators of sickness** across all livestock species.",
                                "Analyze the clinical significance of **anorexia (loss of appetite)** and **lethargy**.",
                                "Recognize **abnormal postures** (arched back, head pressing, lameness).",
                                "Measure and interpret **vital signs (body temperature, pulse, respiration)**."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Universal Behavioral and Clinical Signs of Sickness",
                        "content": {
                            "title": "Spotting the Subtle Shifts in Animal Vitality",
                            "text": "1. **Anorexia & Altered Thirst**: A sudden drop in feed intake is the earliest non-specific indicator of systemic fever, pain, or digestive shutdown.\n2. **Lethargy & Social Isolation**: Herd and flock animals are naturally gregarious. A sick animal stands alone in corners, hangs its head low, droops its ears, and exhibits dull, sunken eyes.\n3. **Abnormal Posture and Gait**:\n- *Arched Back (Kyphosis)*: Indicates severe abdominal pain, hardware disease, or kidney infection.\n- *Head Pressing*: Compulsive pressing of the forehead against walls indicates central nervous system disorders or severe toxicosis.\n- *Lameness*: Refusal to bear weight on a limb indicates hoof rot, joint arthritis, or foot trauma."
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "Vital Signs and Thermoregulation",
                        "content": {
                            "title": "The Objective Physiological Metrics",
                            "text": "- **Body Temperature (Rectal)**:\n  - *Pyrexia (Fever)*: Core temperature elevated ($>39.5^\\circ\\text{C}$ in cattle, $>40.0^\\circ\\text{C}$ in goats/sheep); indicates the immune system is actively fighting viral/bacterial pathogens.\n  - *Hypothermia (Subnormal)*: Temperature below normal ($<38.0^\\circ\\text{C}$); indicates circulatory collapse, severe shock, or acute milk fever (hypocalcemia).\n- **Respiration & Pulse**: Rapid, shallow panting or loud wheezing indicates acute respiratory pneumonia."
                        }
                    },
                    {
                        "type": "comparison_table",
                        "title": "Normal Physiological Vital Signs Across Livestock Species",
                        "content": {
                            "title": "Standard Livestock Vital Signs Reference Table",
                            "headers": ["Species", "Normal Rectal Temp (°C)", "Normal Heart Rate (Beats/min)", "Normal Respiration Rate (Breaths/min)"],
                            "rows": [
                                ["Cattle (Adult)", "38.0 – 39.3 °C", "60 – 80 bpm", "15 – 30 bpm"],
                                ["Goat / Sheep", "38.5 – 40.0 °C", "70 – 90 bpm", "15 – 30 bpm"],
                                ["Pig", "38.5 – 39.5 °C", "60 – 80 bpm", "10 – 20 bpm"],
                                ["Rabbit", "38.5 – 40.0 °C", "130 – 325 bpm", "30 – 60 bpm"],
                                ["Poultry (Chicken)", "40.5 – 42.0 °C", "200 – 400 bpm", "15 – 30 bpm"]
                            ]
                        }
                    }
                ],
                [
                    {
                        "type": "mini_activity",
                        "title": "Classroom Practical: Vital Signs Measurement Lab",
                        "content": {
                            "title": "Taking Livestock Vital Signs Practicum",
                            "task": "1. Under veterinary supervision, restrain a calm goat or sheep in a crush/holding pen.\n2. Lubricate a veterinary digital thermometer and gently insert into the rectum against the mucosal wall for 60 seconds. Record temperature.\n3. Count the rise and fall of the flank over 1 full minute to record resting respiration rate.\n4. Compare your findings against standard physiological reference ranges.",
                            "materials": ["Veterinary Thermometer", "Petroleum Jelly", "Stopwatch", "Goat/Sheep"],
                            "safety": "Keep head restrained; stand at side of animal to avoid kicks."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Core Summary: General Signs",
                        "content": {
                            "title": "Key Takeaways",
                            "text": "- **Anorexia and social isolation are early warnings** of systemic sickness.\n- **Arched back signifies abdominal pain**; head pressing indicates neurological distress.\n- **Fever (pyrexia) indicates infection**; subnormal temp indicates shock or milk fever.\n- **Measure temperature rectally** for accurate clinical diagnosis."
                        }
                    }
                ],
                [
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Diagnostic Meaning of Social Isolation",
                        "content": {
                            "question": "A livestock manager notices a dairy heifer standing completely isolated in the far corner of a paddock with a hunched posture, drooping ears, and unresponsive to feed delivery. What is this clinical observation indicating?",
                            "options": [
                                "The heifer is practicing solitary grazing behavior",
                                "The heifer is exhibiting profound depression and lethargy, signaling acute systemic illness or high fever that requires immediate veterinary clinical examination",
                                "The heifer is waiting for the rain to start",
                                "The heifer has achieved dominant herd status"
                            ],
                            "answer": "B",
                            "explanation": "Cattle are highly gregarious herd animals. When an animal isolates itself, droops its head and ears, and exhibits an arched back, it is showing classical signs of severe lethargy, systemic fever, or acute abdominal pain, demanding immediate physical examination and temperature monitoring."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 3: Identifying Signs of Sickness in Cattle and Goats
        # =====================================================================
        {
            "unit_order": 3,
            "unit_name": "Identifying Signs of Sickness in Cattle and Goats",
            "unit_description": "Ruminant digestion: cessation of cud-chewing (rumen stasis); acute bloat (left flank distension); respiratory discharges; diarrhea/scours; pale mucous membranes (anemia).",
            "lesson_title": "Diagnostic Pathology in Ruminants: Rumen Stasis, Bloat, Scours, and Anemia",
            "pages": [
                [
                    {
                        "type": "suggested_image",
                        "title": "Healthy Dairy Cow Actively Chewing Cud on Meadow",
                        "content": {
                            "title": "Healthy Dairy Cow Actively Chewing Cud on Meadow",
                            "caption": "A dairy cow lying down calmly while ruminating (chewing cud), a paramount clinical sign of active rumen microbial fermentation and digestive health."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Cattle & Goat Health",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Explain the diagnostic importance of **rumination (cud-chewing)** in cattle and goats.",
                                "Diagnose **acute bloat (tympanites)** via left flank abdominal distension.",
                                "Analyze abnormal excretions: **scours (diarrhea), blood, and mucous nasal discharges**.",
                                "Examine **conjunctival and oral mucous membranes** for anemia."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Ruminant Digestive Pathology: Rumen Stasis & Bloat",
                        "content": {
                            "title": "The Rumen as the Primary Health Barometer",
                            "text": "1. **Cessation of Cud-Chewing (Rumen Stasis)**: Healthy ruminants ruminate for 6–8 hours daily. If cud-chewing stops, rumen microbial fermentation has halted due to acute acidosis, fever, or traumatic reticuloperitonitis (hardware disease).\n2. **Acute Bloat (Tympanites)**:\n- **Pathology**: Free gas or stable foam gets trapped in the rumen (located on the **left side** of the abdominal cavity).\n- **Clinical Signs**: Severe, rapid swelling of the **left paralumbar fossa (left flank)** protruding tight as a drum; the animal kicks at its belly, pants with an open mouth, and risks sudden death from asphyxiation as the distended rumen compresses the lungs and diaphragm."
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "Mucous Membranes, Respiration, and Excretions",
                        "content": {
                            "title": "Physical Diagnostic Checkpoints",
                            "text": "3. **Mucous Membrane Color (FAMACHA Check)**:\n- *Healthy*: Salmon pink with rapid capillary refill ($<2\\text{ seconds}$).\n- *Pale / Porcelain White*: Severe **anemia** caused by blood-sucking parasites (*Haemonchus contortus* wireworm, heavy tick loads) or protozoan blood parasites (Anaplasmosis, Babesiosis).\n- *Yellow (Jaundice/Icterus)*: Massive red blood cell destruction or liver failure (e.g., Liver Flukes).\n4. **Feces & Respiratory Discharges**: Watery, foul-smelling diarrhea (scours) indicates bacterial infection (*E. coli*, *Salmonella*) or coccidiosis; purulent crusty nasal discharge indicates pneumonia or IBR."
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Key Clinical Diagnostic Checkpoints on Cattle",
                        "content": {
                            "title": "Key Clinical Diagnostic Checkpoints on Cattle",
                            "caption": "Labeled cow diagnostic diagram: 1 Nose & Eyes (Discharges / Crusts), 2 Eyelid / Gum Mucosa (Pale Anemia Check), 3 Left Flank (Swollen Bloat Triangle), 4 Spine (Arched Pain Posture), 5 Tail & Vent (Scours Fecal Staining)."
                        }
                    }
                ],
                [
                    {
                        "type": "comparison_table",
                        "title": "Ruminant Diagnostic Signs and Associated Pathologies",
                        "content": {
                            "title": "Cattle & Goat Clinical Pathology Matrix",
                            "headers": ["Clinical Observation", "Anatomical Site", "Suspected Pathology / Condition", "Immediate Action Required"],
                            "rows": [
                                ["Left flank swollen tight like drum", "Left paralumbar fossa", "Acute Frothy/Free-Gas Bloat", "Drench with vegetable oil / trocar & cannula emergency puncture"],
                                ["Pale, chalk-white inner eyelid", "Conjunctival mucosa", "Severe Anemia (Wireworm/Ticks)", "Administer targeted anthelmintic drench & iron booster"],
                                ["Absence of cud-chewing >8 hours", "Mouth & Rumen", "Rumen Stasis / Acidosis / Fever", "Check rectal temp; administer rumen buffer / yeast probiotic"],
                                ["Watery yellow/bloody diarrhea", "Hindquarters / Tail", "Calf Scours (E. coli / Coccidiosis)", "Oral rehydration electrolytes + antibiotic/anticoccidial"],
                                ["Purulent nasal discharge & coughing", "Muzzle & Lungs", "Bovine Pneumonia / Respiratory Disease", "Isolate; administer injectable veterinary antibiotics"]
                            ]
                        }
                    },
                    {
                        "type": "suggested_video",
                        "title": "How to Perform a Clinical Health Exam on Cattle",
                        "content": {
                            "title": "How to Perform a Clinical Health Exam on Cattle",
                            "description": "Veterinary demonstration covering rumen motility auscultation, conjunctival mucosa inspection, rectal thermometry, and bloat diagnosis.",
                            "url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
                        }
                    }
                ],
                [
                    {
                        "type": "key_takeaway",
                        "title": "Core Summary: Cattle & Goat Health",
                        "content": {
                            "title": "Key Takeaways",
                            "text": "- **Active cud-chewing confirms rumen health**; absence indicates rumen stasis.\n- **Bloat produces severe swelling of the LEFT flank**.\n- **Pale/white mucous membranes indicate severe anemia** from ticks or wireworms.\n- **Watery diarrhea (scours) requires immediate rehydration**."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Diagnosing Acute Left Flank Swelling",
                        "content": {
                            "question": "A dairy farmer finds a cow exhibiting severe respiratory distress, kicking at its abdomen, and displaying a massive balloon-like swelling on its left flank. What is the diagnosis and anatomical explanation?",
                            "options": [
                                "The cow has twins growing in its left lung",
                                "The cow is suffering from acute bloat (tympanites), where trapped fermentation gases expand the rumen located on the left side of the abdominal cavity",
                                "The cow is storing extra water for the dry season",
                                "The cow's liver has shifted to the left"
                            ],
                            "answer": "B",
                            "explanation": "The rumen occupies the entire left side of the bovine abdominal cavity. When gas or foam gets trapped during acute bloat, the rumen expands rapidly, producing a distinct, drum-like protrusion in the left paralumbar fossa that compresses the diaphragm and causes severe respiratory difficulty."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 4: Identifying Signs of Sickness in Sheep and Pigs
        # =====================================================================
        {
            "unit_order": 4,
            "unit_name": "Identifying Signs of Sickness in Sheep and Pigs",
            "unit_description": "Sheep: stoic behavior, matted fleece loss, bottle jaw (submandibular edema), lagging; Pigs: Erysipelas diamond skin lesions, ASF ear reddening, fever huddling/shivering, thumping.",
            "lesson_title": "Diagnostic Indicators in Sheep and Swine: Bottle Jaw, Fleece Loss, Erysipelas, and African Swine Fever",
            "pages": [
                [
                    {
                        "type": "suggested_image",
                        "title": "Flock of Hair Sheep Grazing on Pasture",
                        "content": {
                            "title": "Flock of Hair Sheep Grazing on Pasture",
                            "caption": "A vigorous flock of meat sheep moving in a tight group across pasture, showing strong flocking instincts and clean, healthy fleece condition."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Sheep & Pig Health",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Identify diagnostic signs in sheep (**bottle jaw, fleece shedding, flock lagging**).",
                                "Explain the physiological mechanism of **submandibular edema (bottle jaw)** caused by internal parasites.",
                                "Diagnose swine pathologies (**diamond skin lesions in Erysipelas, ear reddening in African Swine Fever**).",
                                "Recognize **fever huddling and thumping (pneumonia)** in pigs."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Diagnostic Pathology in Sheep",
                        "content": {
                            "title": "The Stoic Flocking Animal",
                            "text": "1. **Flock Lagging**: Sheep have an intense herd instinct; an individual that trails behind or isolates itself is in an advanced stage of illness.\n2. **Bottle Jaw (Submandibular Edema)**:\n- *Mechanism*: Blood-sucking internal parasites (*Haemonchus contortus* / *Fasciola hepatica*) consume massive amounts of blood, causing extreme hypoproteinemia (loss of albumin in blood).\n- *Symptom*: Low osmotic pressure causes fluid to leak from blood vessels and accumulate gravitationally under the jaw, forming a soft, cold, painless fluid swelling.\n3. **Fleece Breakdown**: Matted, dry, falling fleece with intense wool biting points to sheep scab (*Psoroptes ovis*) or lice."
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "Diagnostic Pathology in Swine",
                        "content": {
                            "title": "Skin, Respiratory, and Febrile Signs in Pigs",
                            "text": "1. **Swine Erysipelas (*Erysipelothrix rhusiopathiae*)**: Characterized by raised, diamond-shaped red/purple skin plaques (Diamond Skin Disease), high fever, and sudden stiffness.\n2. **African Swine Fever (ASF)**: A devastating, lethal viral disease; causes cyanotic dark red/purple discoloration of the ears, snout, belly, and tail, accompanied by vomiting and $100\\%$ flock mortality.\n3. **Fever Huddling & Shivering**: Even on warm days, pigs with high fever pile on top of each other and shiver violently as their internal thermostat resets.\n4. **Thumping**: Rapid, jerky, labored abdominal breathing signaling severe mycoplasmal pneumonia."
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Sheep Bottle Jaw & Submandibular Edema Pathology",
                        "content": {
                            "title": "Sheep Bottle Jaw & Submandibular Edema Pathology",
                            "caption": "Pathology schematic: 1 Haemonchus Worms Ingest Blood in Abomasum -> 2 Severe Blood Albumin Depletion -> 3 Fluid Leaks from Capillaries -> 4 Gravitational Swelling Under Lower Jaw (Bottle Jaw)."
                        }
                    }
                ],
                [
                    {
                        "type": "comparison_table",
                        "title": "Sheep and Swine Specific Clinical Pathologies",
                        "content": {
                            "title": "Sheep & Swine Health Diagnostic Matrix",
                            "headers": ["Species", "Clinical Sign", "Pathological Cause", "Diagnostic Meaning"],
                            "rows": [
                                ["Sheep", "Soft fluid swelling under lower jaw (Bottle Jaw)", "Severe hypoproteinemia from internal parasites", "Advanced Haemonchosis / Liver Fluke infestation"],
                                ["Sheep", "Lagging behind flock & ragged, shedding fleece", "Psoroptic mange mites / chronic malnutrition", "Sheep scab or advanced systemic wasting"],
                                ["Pig", "Raised diamond-shaped purple skin plaques", "Erysipelothrix rhusiopathiae bacterial infection", "Swine Erysipelas (Requires penicillin treatment)"],
                                ["Pig", "Ears and snout turning dark purple/red; bloody diarrhea", "African Swine Fever (ASF) viral infection", "Lethal viral outbreak (Zero cure; quarantine & cull)"],
                                ["Pig", "Piling in corners, shivering on warm afternoon", "Pyrexia (High systemic fever >40.5°C)", "Acute bacterial or viral infectious onset"]
                            ]
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Core Summary: Sheep & Pig Health",
                        "content": {
                            "title": "Key Takeaways",
                            "text": "- **Bottle jaw in sheep results from internal blood parasites** depleting blood proteins.\n- **Lagging behind the flock indicates severe sheep illness**.\n- **Diamond skin lesions diagnose Swine Erysipelas**.\n- **Purple ears and high mortality point to African Swine Fever**."
                        }
                    }
                ],
                [
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Physiological Mechanism of Bottle Jaw",
                        "content": {
                            "question": "A sheep on a smallholder farm has developed a soft, watery, painless swelling beneath its lower jaw (Bottle Jaw) and lags behind the flock. What is the physiological cause of this swelling?",
                            "options": [
                                "The sheep was stung by bees in its mouth",
                                "Heavy infestation of blood-sucking stomach worms (Haemonchus) depletes blood protein, lowering oncotic pressure and causing fluid to pool under the jaw",
                                "The sheep is storing extra cud in its chin",
                                "The sheep has broken its jaw bone while chewing hard maize"
                            ],
                            "answer": "B",
                            "explanation": "Blood-sucking internal parasites (such as *Haemonchus contortus* or liver flukes) deplete serum albumin (blood proteins). This drastically lowers the colloid oncotic pressure within blood vessels, causing liquid plasma to leak into interstitial spaces and pool under the lower jaw due to gravity."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 5: Identifying Signs of Sickness in Poultry and Rabbits
        # =====================================================================
        {
            "unit_order": 5,
            "unit_name": "Identifying Signs of Sickness in Poultry and Rabbits",
            "unit_description": "Poultry: ruffled feathers, gasping/râles, Newcastle green diarrhea vs Coccidiosis bloody feces, pale comb; Rabbits: snuffles (Pasteurella wet paws), ear canker scabs (Psoroptes mites), slobbers.",
            "lesson_title": "Avian and Cuniculture Diagnostics: Newcastle Disease, Coccidiosis, Snuffles, and Ear Canker",
            "pages": [
                [
                    {
                        "type": "suggested_image",
                        "title": "Domestic Rabbit Kept in a Clean Elevated Hutch",
                        "content": {
                            "title": "Domestic Rabbit Kept in a Clean Elevated Hutch",
                            "caption": "A domestic meat rabbit in an elevated wire-mesh hutch, allowing droppings to fall through to prevent coccidial contamination and respiratory irritation."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Poultry & Rabbit Health",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Identify critical poultry pathologies (**Newcastle disease, Coccidiosis, Chronic Respiratory Disease**).",
                                "Differentiate between **greenish-yellow diarrhea (Newcastle)** and **bloody scours (Coccidiosis)**.",
                                "Diagnose rabbit diseases (**Snuffles / Pasteurellosis, Ear Canker, Slobbers**).",
                                "Execute physical health inspections on poultry and rabbits."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Diagnostic Pathology in Poultry",
                        "content": {
                            "title": "Avian Health Indicators",
                            "text": "1. **Posture & Comb**: Sick birds show **ruffled feathers**, drooping wings, closed eyes, and a shriveled, pale/cyanotic comb (healthy combs are bright turgid red).\n2. **Newcastle Disease (ND)**: Acute viral infection. Characterized by **greenish-yellow watery diarrhea**, loud gasping, twisted necks (torticollis / stargazing), and up to $100\\%$ mortality.\n3. **Coccidiosis (*Eimeria* spp.)**: Protozoan intestinal infection of chicks. Produces **bloody diarrhea**, severe huddling under brooders, and rapid dehydration.\n4. **Fowl Pox**: Warty, crusty scabs on the comb, wattles, and eyelids."
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "Diagnostic Pathology in Rabbits (Cuniculture)",
                        "content": {
                            "title": "Respiratory and Parasitic Afflictions of Rabbits",
                            "text": "1. **Snuffles (*Pasteurella multocida*)**: Severe contagious upper respiratory infection. Symptoms include white nasal discharge, loud sneezing, and **matted fur on the inside of the front paws** (caused by the rabbit constantly wiping its wet nose).\n2. **Ear Canker (*Psoroptes cuniculi*)**: Parasitic ear mites. The inside of the ear canal fills with **thick, brown, crusty scabs**; the rabbit shakes its head constantly and scratches its ears.\n3. **Slobbers (Malocclusion)**: Overgrown incisors prevent normal swallowing, causing saliva to soak the chin and dewlap."
                        }
                    },
                    {
                        "type": "comparison_table",
                        "title": "Poultry and Rabbit Diagnostic Pathology Matrix",
                        "content": {
                            "title": "Avian & Cuniculture Disease Matrix",
                            "headers": ["Species", "Key Symptoms", "Primary Diagnosis", "Etiological Agent", "Control Protocol"],
                            "rows": [
                                ["Poultry", "Twisted neck (torticollis), green diarrhea, gasping", "Newcastle Disease", "Avian Paramyxovirus-1", "Mandatory vaccination schedule (Day 14/Week 4)"],
                                ["Poultry", "Bloody diarrhea, hunched posture, ruffled feathers", "Coccidiosis", "Eimeria protozoa", "Anticoccidial drugs in water; keep litter bone dry"],
                                ["Poultry", "Warty crusty nodules on comb, wattles, eyelids", "Fowl Pox", "Avipoxvirus", "Wing-web stab vaccination at 6 weeks"],
                                ["Rabbit", "Sneezing, white nasal discharge, matted front paws", "Snuffles", "Pasteurella multocida (Bacterium)", "Isolate; improve ventilation; veterinary antibiotics"],
                                ["Rabbit", "Thick brown crusty scabs in ears, head shaking", "Ear Canker", "Psoroptes cuniculi (Mite)", "Apply mineral oil drops / acaricide to ears"]
                            ]
                        }
                    }
                ],
                [
                    {
                        "type": "mini_activity",
                        "title": "Practical Lab: Conducting a Physical Health Exam on a Chicken",
                        "content": {
                            "title": "Avian Health Examination Lab",
                            "task": "1. Gently catch a layer or broiler by securing both wings against the body.\n2. Inspect the head: Comb color (bright red = healthy), eyes (clear), and nostrils (dry).\n3. Palpate the crop: Check if soft and pliable (normal) or hard/sour (impacted crop).\n4. Invert bird gently: Inspect the vent area for clean feathers vs white/green/bloody pasty vent.",
                            "materials": ["Chicken", "Protective Gloves", "Inspection Checklist"],
                            "safety": "Handle bird gently to avoid wing dislocation."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Core Summary: Poultry & Rabbit Health",
                        "content": {
                            "title": "Key Takeaways",
                            "text": "- **Newcastle Disease causes twisted necks and green diarrhea**.\n- **Coccidiosis produces bloody droppings** in chicks.\n- **Rabbit snuffles causes matted fur on front paws** from wiping nose.\n- **Ear canker produces thick brown crusty scabs** inside ears."
                        }
                    }
                ],
                [
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Diagnostic Feature of Rabbit Snuffles",
                        "content": {
                            "question": "A student inspects a New Zealand White rabbit and observes loud sneezing, a milky nasal discharge, and heavily matted, wet fur on the inside of both front paws. What is the diagnosis and reason for the matted front paws?",
                            "options": [
                                "The rabbit has dipped its paws in dirty drinking water",
                                "The rabbit has Snuffles (Pasteurellosis); the matted paws occur because the rabbit repeatedly uses its front legs to wipe the nasal discharge from its face",
                                "The rabbit has ear canker",
                                "The rabbit is growing extra swimming webs on its feet"
                            ],
                            "answer": "B",
                            "explanation": "Snuffles is caused by *Pasteurella multocida*. The hallmark diagnostic clue of snuffles is wet, crusty, matted fur on the inside of the rabbit's front paws, caused by the animal constantly wiping the thick mucus discharge away from its nostrils."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 6: Preventative Measures I (Nutrition, Housing, and Sanitation)
        # =====================================================================
        {
            "unit_order": 6,
            "unit_name": "Preventative Measures I (Nutrition, Housing, and Sanitation)",
            "unit_description": "Nutritional defense (Vitamin A, Calcium, clean water); housing design (ventilation sweeping ammonia, dry bedding, space); daily trough cleaning & lime disinfection.",
            "lesson_title": "Primary Preventative Health: Nutritional Defense, Environmental Housing, and Bio-Sanitation",
            "pages": [
                [
                    {
                        "type": "suggested_image",
                        "title": "Modern Well-Ventilated Dairy Barn Interior with Clean Cubicles",
                        "content": {
                            "title": "Modern Well-Ventilated Dairy Barn Interior with Clean Cubicles",
                            "caption": "A well-engineered cattle barn featuring high roof ventilation, clean dry bedding stalls, and unobstructed airflow that sweeps away toxic ammonia fumes."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Nutrition, Housing & Sanitation",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Explain how **balanced nutrition and micronutrients (Vitamin A, Calcium)** fortify immune resistance.",
                                "Analyze housing engineering factors: **continuous airflow, ammonia elimination, dry bedding, and space**.",
                                "Formulate a **standard daily farm bio-sanitation schedule**.",
                                "Evaluate how damp housing causes **foot rot and coccidiosis**."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Nutritional Immunology in Livestock",
                        "content": {
                            "title": "Feeding the Immune System",
                            "text": "- **The First Line of Defense**: Adequate nutrition provides amino acids for antibody synthesis.\n- **Vitamin A**: Crucial for maintaining intact mucosal epithelial linings in the respiratory and gastrointestinal tracts, physically preventing bacterial invasion.\n- **Minerals (Zinc, Selenium, Copper)**: Act as enzymatic cofactors in cellular antioxidant defense.\n- **Clean Water**: Animals require ad libitum clean water; water contaminated with fecal runoff is the primary vector for colibacillosis and salmonellosis."
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "Environmental Housing Engineering & Bio-Sanitation",
                        "content": {
                            "title": "Eliminating Pathogen Reservoirs in Animal Housing",
                            "text": "1. **Cross-Ventilation vs Ammonia Toxicity**: In poorly ventilated barns, urine breaks down into **ammonia gas ($>25\\text{ ppm}$)**. Ammonia paralyzes respiratory cilia, allowing airborne bacteria to cause pneumonia.\n2. **Dry Bedding Rule**: Wet manure-soaked bedding softens hoof horn (triggering **foot rot**) and provides the exact moisture needed for coccidial oocysts to sporulate.\n3. **Stocking Density**: Overcrowding causes chronic social stress, elevating cortisol and triggering rapid cross-infection.\n4. **Bio-Sanitation**: Daily manure scraping, feed trough scrubbing, and applying **agricultural lime (calcium hydroxide)** to dirt floors raises pH to $>11$, destroying bacterial membranes."
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "The 3 Pillars of Preventative Animal Health",
                        "content": {
                            "title": "The 3 Pillars of Preventative Animal Health",
                            "caption": "Triangular defense model: 1 Balanced Nutrition & Clean Water, 2 Engineered Ventilated Housing & Dry Bedding, 3 Daily Bio-Sanitation & Disinfection."
                        }
                    }
                ],
                [
                    {
                        "type": "comparison_table",
                        "title": "Environmental Housing Parameters and Health Impacts",
                        "content": {
                            "title": "Housing Health Engineering Matrix",
                            "headers": ["Housing Factor", "Optimal Standard", "Deficient Condition", "Resulting Pathology"],
                            "rows": [
                                ["Airflow / Ventilation", "Open ridge roof with cross-drafts (<10ppm ammonia)", "Closed, stuffy, damp barn (>25ppm ammonia)", "Ciliary paralysis, respiratory pneumonia"],
                                ["Floor Bedding", "Dry wood shavings / straw (changed weekly)", "Wet, urine-soaked manure mud", "Foot rot (Fusobacterium), coccidiosis"],
                                ["Stocking Space", "Dairy: 8–10 m²/cow; Layers: 0.15 m²/bird", "Severe overcrowding (high stocking density)", "Cortisol stress, cannibalism, rapid contagion"],
                                ["Trough Sanitation", "Scrubbed daily; fresh clean water", "Algae, feed sludge, bird droppings", "Bacterial scours (E. coli, Salmonella)"]
                            ]
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Core Summary: Nutrition & Housing",
                        "content": {
                            "title": "Key Takeaways",
                            "text": "- **Balanced nutrition and Vitamin A maintain mucosal defense**.\n- **Ammonia gas paralyzes respiratory cilia**, causing pneumonia.\n- **Wet bedding softens hooves**, triggering foot rot and coccidiosis.\n- **Agricultural lime disinfects dirt floors** by raising pH."
                        }
                    }
                ],
                [
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Ammonia Gas Pathology in Enclosed Barns",
                        "content": {
                            "question": "Why does poor ventilation in an enclosed goat shed lead to an immediate outbreak of respiratory pneumonia?",
                            "options": [
                                "Goats cannot see each other in poor airflow",
                                "Accumulated ammonia gas from urine irritates and paralyzes the protective cilia lining the respiratory tract, allowing pathogenic bacteria to invade the lungs",
                                "The air gets too rich in pure oxygen",
                                "Lack of airflow causes the goats to lose their horns"
                            ],
                            "answer": "B",
                            "explanation": "Urine decomposition produces ammonia vapor. When ventilation is inadequate, ammonia concentrates in the breathing zone, stripping away the mucosal barrier and paralyzing the mucociliary escalator. With this defense destroyed, environmental bacteria (*Pasteurella*, *Mannheimia*) penetrate deep into lung alveoli, causing pneumonia."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 7: Preventative Measures II (Biosecurity and Vaccination)
        # =====================================================================
        {
            "unit_order": 7,
            "unit_name": "Preventative Measures II (Biosecurity and Vaccination)",
            "unit_description": "Biosecurity barriers (disinfectant footbaths, visitor limits, 30-day quarantine pen 100m away); vaccination biological mechanism (antigens stimulating antibodies); poultry vaccine calendar.",
            "lesson_title": "Biosecurity Barriers, 30-Day Quarantine Protocols, and Immunological Vaccination",
            "pages": [
                [
                    {
                        "type": "suggested_image",
                        "title": "Veterinarian Administering Preventive Livestock Vaccine",
                        "content": {
                            "title": "Veterinarian Administering Preventive Livestock Vaccine",
                            "caption": "A veterinary professional administering an intramuscular preventative vaccine to an animal, conferring active immunological protection against virulent pathogens."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Biosecurity & Vaccination",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Define **farm biosecurity** and implement physical perimeter defense barriers.",
                                "Execute the **30-day quarantine protocol** for newly purchased stock.",
                                "Explain the biological mechanism of **vaccine-induced active immunity (antigens vs antibodies)**.",
                                "Deploy a **standard 6-week commercial poultry vaccination calendar**."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Farm Biosecurity Engineering and Quarantine",
                        "content": {
                            "title": "The Defensive Fortress of the Farm",
                            "text": "1. **Physical Biosecurity Barriers**:\n- **Disinfectant Footbaths**: Placed at every barn entrance containing broad-spectrum virucides/bactericides (e.g., Virkon-S, copper sulfate) to sterilize footwear.\n- **Vehicle Spray Dips**: Disinfect vehicle tires at the main gate to prevent mechanical transport of pathogens from other farms.\n- **Bird and Rodent Proofing**: Wire mesh ($1.5\\text{ cm}$) on poultry houses to exclude wild birds (which carry Avian Influenza and Newcastle).\n2. **The 30-Day Quarantine Rule**: All newly acquired animals must be housed in a separate quarantine pen **at least 100 meters away** from the main herd for **30 days**. This allows incubating subclinical diseases to manifest without infecting the resident herd."
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "Biological Mechanism of Vaccination",
                        "content": {
                            "title": "Training the Immune System for Active Defense",
                            "text": "- **Antigen Introduction**: Vaccines deliver attenuated (weakened), inactivated (killed), or recombinant antigens into a healthy animal.\n- **Antibody Production**: The host's B-lymphocytes recognize the harmless antigen and produce specific, targeted **antibodies** and long-lived **memory cells**.\n- **Active Immunity**: When wild, virulent pathogens attack later, memory cells deploy overwhelming antibody defenses instantly, destroying the pathogen before illness develops.\n- **THE GOLDEN RULE OF VACCINATION**: **NEVER VACCINATE A SICK ANIMAL!** Sickness compromises the immune response, leading to vaccine failure and potential death."
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Farm Biosecurity Perimeter & 30-Day Quarantine Protocol",
                        "content": {
                            "title": "Farm Biosecurity Perimeter & 30-Day Quarantine Protocol",
                            "caption": "Biosecurity perimeter blueprint: 1 Main Gate Wheel Dip, 2 Disinfectant Footbaths at Sheds, 3 Isolated 30-Day Quarantine Pen (100m away), 4 Main Healthy Stock Enclosure."
                        }
                    }
                ],
                [
                    {
                        "type": "comparison_table",
                        "title": "Standard Commercial Poultry Vaccination Schedule (Kenya)",
                        "content": {
                            "title": "Poultry Immunization Protocol (Day 1 to Week 6)",
                            "headers": ["Age / Timing", "Target Disease", "Vaccine Type", "Administration Route"],
                            "rows": [
                                ["Day 1 (Hatchery)", "Marek's Disease", "Live Marek's Vaccine", "Subcutaneous injection (neck)"],
                                ["Day 7 (Week 1)", "Gumboro (IBD - 1st Dose)", "Live Intermediate Gumboro", "Oral via drinking water"],
                                ["Day 14 (Week 2)", "Newcastle Disease (ND - 1st Dose)", "LaSota / Clone 30 Strain", "Eye drop / coarse spray / drinking water"],
                                ["Day 21 (Week 3)", "Gumboro (IBD - 2nd Booster)", "Live Gumboro Booster", "Oral via drinking water"],
                                ["Day 28 (Week 4)", "Newcastle Disease (ND - 2nd Booster)", "LaSota Booster", "Oral via drinking water"],
                                ["Week 6 (Day 42)", "Fowl Pox", "Live Fowl Pox Vaccine", "Wing-web stab puncture"]
                            ]
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Core Summary: Biosecurity & Vaccines",
                        "content": {
                            "title": "Key Takeaways",
                            "text": "- **Biosecurity excludes pathogens** via footbaths, fencing, and vehicle sprays.\n- **Quarantine new animals for 30 days** at least 100m away.\n- **Vaccines stimulate antibody and memory cell production**.\n- **Only vaccinate healthy animals**; never vaccinate sick stock."
                        }
                    }
                ],
                [
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Rationale for 30-Day Quarantine",
                        "content": {
                            "question": "What is the critical scientific and agricultural rationale for isolating a newly purchased dairy cow in a separate pen for 30 days before mixing her with the farm's resident herd?",
                            "options": [
                                "To allow the cow to forget her previous owner",
                                "To monitor the cow through the incubation periods of infectious diseases (such as Foot and Mouth or Brucellosis) that may not be visible upon purchase, protecting the main herd from infection",
                                "To let the cow lose weight before joining the milking herd",
                                "To test if the cow enjoys the farm's specific radio station"
                            ],
                            "answer": "B",
                            "explanation": "Pathogens have incubation periods during which an animal appears completely healthy while harboring the infection. A 30-day quarantine period ensures that any latent pathogens have time to manifest clinically, enabling diagnosis and treatment without risking catastrophic disease outbreaks in the clean resident herd."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 8: Disease Control Measures (Parasites, Isolation, and Treatment)
        # =====================================================================
        {
            "unit_order": 8,
            "unit_name": "Disease Control Measures (Parasites, Isolation, and Treatment)",
            "unit_description": "Endoparasites (roundworms, flukes -> anthelmintics, pasture rotation); Ectoparasites (ticks transmitting ECF -> acaricides); sick animal isolation; vet prescription vs AMR.",
            "lesson_title": "Parasite Control Dynamics, Pasture Rotation, Isolation Protocols, and Veterinary Ethics",
            "pages": [
                [
                    {
                        "type": "suggested_image",
                        "title": "Cattle Tick Acaricide Treatment Application",
                        "content": {
                            "title": "Cattle Tick Acaricide Treatment Application",
                            "caption": "A livestock keeper applying acaricide spray along tick attachment points (ears, underbelly, tail base) to break the vector cycle of East Coast Fever."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Disease Control & Parasites",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Differentiate between **endoparasites (internal)** and **ectoparasites (external)**.",
                                "Explain how **pasture rotation breaks the parasite life cycle** without chemicals.",
                                "Control tick-borne diseases (**East Coast Fever**) using **acaricides**.",
                                "Apply veterinary ethics: **physical isolation, professional diagnosis, and preventing Antimicrobial Resistance (AMR)**."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Endoparasite & Ectoparasite Control Dynamics",
                        "content": {
                            "title": "Targeting Parasites at Every Stage",
                            "text": "1. **Internal Parasites (Endoparasites)**:\n- Roundworms (*Haemonchus*), Tapeworms, and Liver Flukes (*Fasciola*).\n- *Chemical Control*: Oral drenching with **anthelmintics** (Albendazole, Levamisole, Ivermectin).\n- *Biological / Agronomic Control (Pasture Rotation)*: Subdividing pasture into paddocks and spelling them for 4–6 weeks; parasite larvae hatch on empty grass and die of starvation/desiccation before stock returns.\n2. **External Parasites (Ectoparasites)**:\n- Ticks (*Rhipicephalus appendiculatus* transmitting East Coast Fever), Mites, and Lice.\n- *Control*: Plunge dips, spray races, knapsack sprayers, or pour-on **acaricides** (Synthetic pyrethroids, organophosphates)."
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "Sick Animal Isolation & Antibiotic Stewardship",
                        "content": {
                            "title": "Halting Contagion and Preserving Drug Efficacy",
                            "text": "3. **Immediate Isolation**: Move any sick animal to a designated sick bay immediately to halt mechanical disease transmission.\n4. **Professional Veterinary Care vs Antimicrobial Resistance (AMR)**:\n- **NEVER self-prescribe human or livestock antibiotics!**\n- Under-dosing, inappropriate drug selection, or failing to observe **drug withdrawal periods** breeds resistant superbugs (AMR) and leaves toxic residues in commercial milk and meat."
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Parasite Life Cycle & Pasture Rotation Breaking Mechanism",
                        "content": {
                            "title": "Parasite Life Cycle & Pasture Rotation Breaking Mechanism",
                            "caption": "Parasitology schematic: 1 Eggs Shed in Feces -> 2 Larvae Hatch on Grass (3–5 Days) -> 3 Grazing Animal Ingests Larvae -> 4 Pasture Rotation Mechanism: Animals Moved to Paddock B, Larvae in Paddock A Die of Starvation!"
                        }
                    }
                ],
                [
                    {
                        "type": "comparison_table",
                        "title": "Parasite Classification, Impact, and Control Methods",
                        "content": {
                            "title": "Comprehensive Livestock Parasite Matrix",
                            "headers": ["Parasite Type", "Common Examples", "Anatomical Site", "Harm Inflicted", "Control Strategy"],
                            "rows": [
                                ["Endoparasite (Nematode)", "Haemonchus contortus (Wireworm)", "Abomasum (Stomach)", "Severe anemia, bottle jaw, weight loss", "Anthelmintic drench + rotational grazing"],
                                ["Endoparasite (Trematode)", "Fasciola hepatica (Liver Fluke)", "Liver bile ducts", "Liver destruction, chronic jaundice, wasting", "Flukicide drench + fence off swampy snail habitats"],
                                ["Ectoparasite (Arachnid)", "Rhipicephalus (Brown Ear Tick)", "Ears, base of horns, tail", "Transmits lethal East Coast Fever (ECF)", "Weekly acaricide plunge dipping / spraying"],
                                ["Ectoparasite (Arachnid)", "Psoroptes cuniculi (Ear Mite)", "Rabbit inner ear canal", "Crusty ear canker, intense pain, scratching", "Acaricidal ear drops + hutch disinfection"]
                            ]
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Core Summary: Parasites & Disease Control",
                        "content": {
                            "title": "Key Takeaways",
                            "text": "- **Anthelmintics control internal worms**; acaricides control external ticks.\n- **Pasture rotation starves parasite larvae** naturally.\n- **Isolate sick animals immediately** in dedicated sick pens.\n- **Avoid self-prescribing antibiotics** to prevent Antimicrobial Resistance (AMR)."
                        }
                    }
                ],
                [
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Mechanism of Pasture Rotation",
                        "content": {
                            "question": "How does rotational grazing (pasture rotation) effectively control internal roundworms in sheep without requiring continuous chemical deworming?",
                            "options": [
                                "The sheep walk fast enough to shake worms out of their bodies",
                                "Moving stock to clean paddocks and leaving grazed paddocks empty for 4–6 weeks breaks the worm life cycle, as hatched infective larvae on the grass die of starvation and sunlight exposure before animals return",
                                "The different paddocks contain special wild grass that acts as natural antibiotic pills",
                                "It forces internal worms to turn into butterflies and fly away"
                            ],
                            "answer": "B",
                            "explanation": "Internal worm eggs passed in feces hatch on the pasture into infective L3 larvae. If the paddock is spelled (left empty) for 4 to 6 weeks, the larvae exhaust their energy reserves and die from heat and starvation before livestock return, drastically reducing pasture contamination naturally."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 9: Housing, Hygiene, and Waste Management
        # =====================================================================
        {
            "unit_order": 9,
            "unit_name": "Housing, Hygiene, and Waste Management",
            "unit_description": "Daily manure removal; thermophilic composting (>60°C pasteurization); down-slope siting preventing borehole runoff; deep carcass burial with quicklime.",
            "lesson_title": "Sanitation Engineering, Thermophilic Composting, Runoff Control, and Carcass Disposal",
            "pages": [
                [
                    {
                        "type": "suggested_image",
                        "title": "Agricultural Farm Manure Composting Pit and Excavation",
                        "content": {
                            "title": "Agricultural Farm Manure Composting Pit and Excavation",
                            "caption": "A well-managed farm composting facility where livestock manure undergoes high-temperature microbial decomposition, transforming biological waste into pathogen-free organic fertilizer."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Waste Management & Sanitation",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Execute **daily physical manure removal and bio-sanitation**.",
                                "Explain how **thermophilic composting ($>60^\\circ\\text{C}$)** pasteurizes pathogens and weed seeds.",
                                "Design **down-slope manure pits** to prevent borehole and river contamination.",
                                "Execute **safe, biosecure carcass disposal (deep burial with quicklime)**."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Sanitation Routines & Thermophilic Composting",
                        "content": {
                            "title": "Turning Pathogen Reservoirs into Soil Gold",
                            "text": "1. **Daily Waste Scraping**: Scrape manure out of pens daily. Accumulating manure breeds flies (*Musca domestica*), releases eye-irritating ammonia, and houses coccidial oocysts.\n2. **The Science of Thermophilic Composting**:\n- Stacking manure in aerated piles initiates aerobic decomposition by thermophilic microorganisms.\n- Internal pile temperatures reach **$55\\text{--}65^\\circ\\text{C}$ for several weeks**.\n- *Pathogen Pasteurization*: This intense biological heat destroys $100\\%$ of *E. coli*, *Salmonella*, parasite eggs, and weed seeds, converting raw waste into rich, safe humus."
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "Hydrological Runoff Protection & Carcass Disposal",
                        "content": {
                            "title": "Protecting Farm Ecosystems and Public Health",
                            "text": "3. **Hydrological Siting Rules**: Always construct manure pits **down-slope and at least 30 meters away** from clean boreholes, wells, and streams. Rainfall runoff over manure carries nitrogen, phosphorus, and coliform bacteria, causing waterborne epidemics and river eutrophication.\n4. **Carcass Disposal Protocols**:\n- *Deep Burial*: Dig a pit at least **2 meters deep**, place carcass, cover with **quicklime (calcium oxide)** to accelerate decomposition and deter scavengers, and backfill with soil.\n- *Incineration*: Burn completely in a high-temperature incinerator."
                        }
                    },
                    {
                        "type": "comparison_table",
                        "title": "Farm Waste Disposal Protocols and Environmental Impacts",
                        "content": {
                            "title": "Farm Waste Management Matrix",
                            "headers": ["Waste Category", "Recommended Disposal Protocol", "Biological Mechanism", "Hazard of Mismanagement"],
                            "rows": [
                                ["Solid Manure / Dung", "Thermophilic composting pile (>60°C)", "Aerobic microbial heat pasteurizes pathogens", "Fly breeding, ammonia buildup, coccidial spread"],
                                ["Liquid Urine / Slurry", "Biogas digester / sealed slurry tank", "Anaerobic methane digestion & nutrient capture", "Contaminates groundwater; asphyxiating ammonia fumes"],
                                ["Mortality Carcasses", "Deep burial (2m depth) + quicklime layer", "Seals pathogens; quicklime deters scavengers", "Scavengers unearth carcass; spreads lethal Anthrax/Rabies"],
                                ["Medical Waste (Needles/Vials)", "Sharps container + high-temperature incinerator", "Complete thermal destruction of glass/steel/drugs", "Accidental human needle-stick punctures; chemical poisoning"]
                            ]
                        }
                    }
                ],
                [
                    {
                        "type": "mini_activity",
                        "title": "Field Practical: Building and Monitoring a Compost Heat Pile",
                        "content": {
                            "title": "Thermophilic Compost Practicum",
                            "task": "1. Layer cattle/poultry manure with dry maize stover and green foliage in a 1.5m x 1.5m heap.\n2. Water lightly to maintain 50% moisture and cover with dark polythene sheeting.\n3. Insert a long compost soil thermometer into the center on Day 3, 7, and 14.\n4. Record the temperature surge (target: >55°C) to verify pathogen pasteurization.",
                            "materials": ["Manure", "Crop Stover", "Compost Thermometer", "Polythene Sheet"],
                            "safety": "Wear overalls and waterproof gloves during manure handling."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Core Summary: Waste Management",
                        "content": {
                            "title": "Key Takeaways",
                            "text": "- **Scrape manure daily** to prevent fly and parasite breeding.\n- **Compost heat ($>60^\\circ\\text{C}$)** kills pathogens and weed seeds.\n- **Locate manure pits down-slope** from drinking boreholes.\n- **Bury carcasses 2 meters deep** covered with quicklime."
                        }
                    }
                ],
                [
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Biological Benefit of Compost Pile Heat",
                        "content": {
                            "question": "What is the primary biological and agricultural benefit of the intense heat (55–65°C) generated inside a properly aerated livestock manure compost pile?",
                            "options": [
                                "It converts manure into cooking oil",
                                "It naturally pasteurizes the waste, destroying pathogenic bacteria (such as Salmonella and E. coli), killing internal parasite eggs, and sterilizing weed seeds to create safe organic fertilizer",
                                "It melts stones into liquid minerals for plant roots",
                                "It attracts wild snakes to protect the farm from rats"
                            ],
                            "answer": "B",
                            "explanation": "During active aerobic composting, thermophilic microorganisms generate temperatures between 55°C and 65°C. This natural thermal pasteurization destroys pathogenic bacteria, internal worm eggs/oocysts, and weed seeds, ensuring the resulting organic compost is completely safe to apply to food crops."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 10: Routine Health Maintenance and Daily Care
        # =====================================================================
        {
            "unit_order": 10,
            "unit_name": "Routine Health Maintenance and Daily Care",
            "unit_description": "Daily 5-point inspection checklist; hoof trimming preventing foot rot; safe oral drenching technique (horizontal head angle preventing fatal tracheal aspiration).",
            "lesson_title": "Daily Health Inspection Checklists, Hoof Trimming Protocols, and Safe Oral Drenching",
            "pages": [
                [
                    {
                        "type": "suggested_image",
                        "title": "Livestock Drenching and Oral Medication Procedure",
                        "content": {
                            "title": "Livestock Drenching and Oral Medication Procedure",
                            "caption": "A livestock handler administering liquid anthelmintic drench using an automatic dosing gun, maintaining the animal's head in a natural horizontal position."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Routine Care & Drenching",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Execute the **Morning 5-Point Health Inspection Checklist**.",
                                "Demonstrate **hoof trimming protocols** to prevent bacterial foot rot.",
                                "Execute **safe oral drenching technique** (horizontal head angle).",
                                "Explain the lethal hazard of **tracheal aspiration pneumonia during improper drenching**."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The Morning 5-Point Health Checklist",
                        "content": {
                            "title": "The Daily Diagnostic Ritual",
                            "text": "Every morning before feeding, the herd manager must systematically observe all stock:\n1. **Alertness & Posture**: Are all animals standing? Are ears erect and eyes bright?\n2. **Appetite & Cud-Chewing**: Are cows eagerly approaching feed? Are resting cows ruminating?\n3. **Respiration**: Any rapid flank breathing, gasping, or purulent nasal discharges?\n4. **Manure & Urine**: Normal firm pads/pellets? Any watery scours, blood, or dark urine?\n5. **Mobility & Udder**: Any limping or lameness? Any swollen, hot, or asymmetric udder quarters?"
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "Hoof Trimming and Safe Oral Drenching Mechanics",
                        "content": {
                            "title": "Precision Physical Interventions",
                            "text": "1. **Hoof Trimming**: In intensive zero-grazing or bedding systems, hoof keratin grows faster than it wears down. Overgrown, curled hoof walls trap wet mud and manure, creating anaerobic conditions for *Fusobacterium necrophorum* (**foot rot**). Hooves must be trimmed flat using hoof shears.\n2. **The Oral Drenching Rule**:\n- Insert the drenching gun nozzle through the side of the mouth (**diastema**) over the base of the tongue.\n- **THE HORIZONTAL HEAD RULE**: Keep the head in a **natural, level horizontal position**!\n- *DANGER*: If the muzzle is pulled vertically pointing to the sky, the epiglottis cannot close over the windpipe. The liquid medication pours down the **trachea directly into the lungs**, causing immediate drowning or fatal **aspiration pneumonia**!"
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Safe Oral Drenching Head Angle vs Fatal Aspiration Risk",
                        "content": {
                            "title": "Safe Oral Drenching Head Angle vs Fatal Aspiration Risk",
                            "caption": "Anatomical mechanics graphic: 1 Safe Technique (Head Level Horizontal -> Epiglottis Closes Trachea -> Fluid Enters Esophagus & Rumen) vs 2 Lethal Technique (Muzzle Pointed Vertically Up -> Epiglottis Open -> Fluid Floods Lungs -> Fatal Aspiration Pneumonia)."
                        }
                    }
                ],
                [
                    {
                        "type": "comparison_table",
                        "title": "Routine Livestock Care Operations and Safety Protocols",
                        "content": {
                            "title": "Routine Physical Maintenance Chart",
                            "headers": ["Care Operation", "Required Tool", "Correct Anatomical Execution", "Severe Hazard Prevented"],
                            "rows": [
                                ["Oral Drenching", "Calibrated drenching gun", "Nozzle in side diastema; head held HORIZONTAL", "Tracheal aspiration pneumonia / drowning"],
                                ["Hoof Trimming", "Hoof shears / paring knife", "Pare outer overgrown wall level with sole pad", "Interdigital necrobacillosis (Foot Rot) & lameness"],
                                ["Wound Care", "Antiseptic wash & fly spray", "Clean with iodine; spray topical oxytetracycline", "Blowfly maggot strike (Myiasis) & septic shock"],
                                ["Castration (Young stock)", "Elastrator pliers & rubber ring", "Fit ring above both testicles; check both in scrotum", "Tetanus infection; incomplete unilateral castration"]
                            ]
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Core Summary: Routine Care",
                        "content": {
                            "title": "Key Takeaways",
                            "text": "- **Execute the 5-point health checklist** every morning before feeding.\n- **Trim hooves flat** to eliminate anaerobic foot rot pockets.\n- **Hold the head HORIZONTAL during oral drenching**.\n- **Lifting the muzzle vertically causes fatal aspiration pneumonia**."
                        }
                    }
                ],
                [
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Fatal Hazard of Vertical Head Drenching",
                        "content": {
                            "question": "Why is it an extremely dangerous and potentially lethal error for a farm hand to yank a sheep's head vertically pointing straight up to the sky while administering an oral dewormer drench?",
                            "options": [
                                "The sheep will spit the medicine into the handler's eyes",
                                "Holding the muzzle vertically prevents the epiglottis reflex from sealing the larynx, allowing the liquid drench to flood down the trachea into the lungs, causing fatal aspiration pneumonia",
                                "The sheep will lose its wool around its neck",
                                "The drenching gun will bend and break in half"
                            ],
                            "answer": "B",
                            "explanation": "When an animal's neck is forced straight up, it cannot swallow naturally and the epiglottis fails to cover the entrance to the trachea (windpipe). As a result, the chemical liquid pours directly into the bronchial tubes and lungs, causing acute drowning or severe, fatal aspiration pneumonia."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 11: Designing an Animal Health Plan and Awareness Campaign
        # =====================================================================
        {
            "unit_order": 11,
            "unit_name": "Designing an Animal Health Plan and Awareness Campaign",
            "unit_description": "Animal Health Plan architecture (inventory, routines, vaccines, parasite program, biosecurity); 5 Freedoms of Animal Welfare; community advocacy promoting citizenship & patriotism.",
            "lesson_title": "Animal Health Planning Architecture, The 5 Animal Freedoms, and Community Advocacy",
            "pages": [
                [
                    {
                        "type": "suggested_image",
                        "title": "Agricultural Field Advisor Training Community Livestock Keepers",
                        "content": {
                            "title": "Agricultural Field Advisor Training Community Livestock Keepers",
                            "caption": "An agricultural extension specialist training local farmers on herd health calendars, vaccination records, and biosecure farm management."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Health Plans & Advocacy",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Draft a structured, production-cycle **Animal Health Plan**.",
                                "Analyze the international **Five Freedoms of Animal Welfare**.",
                                "Design a **Community Animal Health & Welfare Awareness Campaign**.",
                                "Demonstrate CBC core competencies: **Citizenship, Patriotism, and Community Leadership**."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Components of a Production Animal Health Plan",
                        "content": {
                            "title": "Proactive Management Over Crisis Reaction",
                            "text": "An **Animal Health Plan (AHP)** is a comprehensive written protocol scheduling all prophylactic and management actions for an enterprise:\n1. **Stock Inventory & Identification**: Ear tags, breed, age, and production status.\n2. **Daily Operational Protocols**: Scheduled feeding, water testing, and 5-point inspection.\n3. **Prophylactic Vaccination Calendar**: Pre-scheduled immunization dates matching regional disease threats.\n4. **Strategic Parasite Control**: Rotational acaricide dipping and seasonal anthelmintic drenching intervals.\n5. **Biosecurity & Quarantine Protocols**: Footbath chemical replenishment and 30-day quarantine rules.\n6. **Veterinary Records**: Recording all drug treatments and observing mandatory meat/milk withdrawal periods."
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "The Five Freedoms of Animal Welfare and Community Action",
                        "content": {
                            "title": "Ethical Stewardship and Citizenship in Practice",
                            "text": "Under the CBC framework, students become change agents by advocating for the **Five Freedoms**:\n1. *Freedom from Hunger and Thirst* (Clean water and balanced rations).\n2. *Freedom from Discomfort* (Clean, dry shelter and resting areas).\n3. *Freedom from Pain, Injury, and Disease* (Rapid prevention and treatment).\n4. *Freedom to Express Normal Behavior* (Adequate space and herd companionship).\n5. *Freedom from Fear and Distress* (Gentle, low-stress handling).\n\n- **Community Advocacy**: Conducting educational workshops, designing market posters, and advising smallholders on humane handling develops **Citizenship, Patriotism, and National Economic Self-Reliance**."
                        }
                    },
                    {
                        "type": "comparison_table",
                        "title": "The Five Freedoms of Animal Welfare Implementation",
                        "content": {
                            "title": "Animal Welfare Five Freedoms Matrix",
                            "headers": ["Welfare Freedom", "Biological Meaning", "On-Farm Implementation Strategy", "Agribusiness Benefit"],
                            "rows": [
                                ["1. From Hunger & Thirst", "Continuous access to water and balanced feed", "Clean automated waterers; balanced total mixed rations", "Peak growth rates; zero metabolic deficiency"],
                                ["2. From Discomfort", "Protection from weather extremes and dampness", "Well-ventilated roofing; dry soft bedding cubicles", "Zero pneumonia; healthy clean hooves and udders"],
                                ["3. From Pain & Disease", "Prevention, rapid diagnosis, and treatment", "Strict vaccination, routine drenching, cattle crush", "Low mortality; zero carcass meat bruising"],
                                ["4. Normal Behavior", "Space and environment for natural instincts", "Open exercise paddocks; group social housing", "Zero abnormal stereotypic vices / aggression"],
                                ["5. From Fear & Distress", "Conditions that avoid mental suffering/panic", "Low-stress flight zone handling; no sticks/beating", "Steady oxytocin release; calm cooperative herd"]
                            ]
                        }
                    }
                ],
                [
                    {
                        "type": "mini_activity",
                        "title": "Agribusiness Practical: Drafting a 1-Page Poultry Layer Health Plan",
                        "content": {
                            "title": "Poultry Enterprise Health Plan Design",
                            "task": "1. Working in teams, draft a 1-page operational Health Plan for a 500-layer poultry project.\n2. Detail the full 6-week vaccination timetable (Marek's, Gumboro, Newcastle, Fowl Pox).\n3. Set up the biosecurity protocol (footbaths, visitor log, wire mesh).\n4. Include a daily sanitation checklist and manure composting plan.",
                            "materials": ["Health Plan Template", "Chart Paper", "Markers"],
                            "safety": "Ensure full compliance with KICD curriculum standards."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Core Summary: Health Planning & Welfare",
                        "content": {
                            "title": "Key Takeaways",
                            "text": "- **An Animal Health Plan shifts farming from crisis to prevention**.\n- **Track inventory, vaccinations, drenching, and drug withdrawal times**.\n- **The Five Freedoms ensure ethical, humane livestock production**.\n- **Community advocacy builds Citizenship and agricultural profitability**."
                        }
                    }
                ],
                [
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Components of an Effective Health Plan",
                        "content": {
                            "question": "Which of the following represents the most comprehensive and professionally structured Animal Health Plan for a commercial livestock enterprise?",
                            "options": [
                                "Buying random human medicines only after several cows have died",
                                "A written document detailing stock records, daily bio-sanitation tasks, pre-scheduled vaccination dates, parasite control intervals, biosecurity barriers, and drug withdrawal logs",
                                "Posting the phone number of a cattle buyer on the gate",
                                "Painting the barn fence in bright red paint"
                            ],
                            "answer": "B",
                            "explanation": "A professional Animal Health Plan is structured, written, and proactive. It integrates animal identification, daily management routines, pre-scheduled immunizations, vector and parasite control programs, physical biosecurity protocols, and veterinary drug records to ensure structured disease prevention."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 12: Sub-strand Review and Performance Task
        # =====================================================================
        {
            "unit_order": 12,
            "unit_name": "Sub-strand Review and Performance Task",
            "unit_description": "Synthesis of health, prevention, and disease control; Rabbit Project / Dairy Farm Health Crisis diagnostic audit; 8 Summative Topic Assessment MCQs.",
            "lesson_title": "Synthesis of General Animal Health, Diagnostic Systems, and Summative Assessment",
            "pages": [
                [
                    {
                        "type": "suggested_image",
                        "title": "Panoramic View of a Modern Integrated Livestock Facility",
                        "content": {
                            "title": "Panoramic View of a Modern Integrated Livestock Facility",
                            "caption": "A premier modern livestock farm successfully implementing complete veterinary biosecurity, engineered housing, high-temperature waste composting, and routine preventative health protocols."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Synthesis & Summative Assessment",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Synthesize the **complete General Animal Health framework**.",
                                "Complete the **Kiambu Dairy Farm Health Crisis Diagnostic Audit**.",
                                "Resolve the **School Rabbit Project Outbreak Performance Task**.",
                                "Complete the comprehensive **Summative Topic Assessment** covering all 12 lessons of Topic 10."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Master General Animal Health Operational Synthesis",
                        "content": {
                            "title": "The Unified Framework of Livestock Health & Disease Defense",
                            "text": "1. **Health Foundations**: Homeostasis, FCE, low somatic cells, morbidity vs mortality.\n2. **Diagnostic Mastery**: Early anorexia and lethargy; ruminant bloat and rumen stasis; sheep bottle jaw (hypoproteinemia); swine Erysipelas and ASF; poultry Newcastle vs Coccidiosis; rabbit snuffles and ear canker.\n3. **3 Pillars of Prevention**: Nutritional defense (Vitamin A); engineered ventilation (<10ppm ammonia) and dry bedding; daily bio-sanitation.\n4. **Biosecurity & Immunization**: Footbaths, 30-day quarantine pen (100m away); active antibody production via vaccines; 6-week poultry vaccination calendar.\n5. **Parasite & Waste Control**: Pasture rotation breaking larval life cycles; acaricides against ticks; thermophilic composting ($>60^\\circ\\text{C}$) pasteurizing pathogens; deep carcass burial with quicklime.\n6. **Routine Physical Care**: 5-point daily inspection; hoof trimming against foot rot; horizontal head drenching preventing fatal tracheal aspiration."
                        }
                    }
                ],
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Master General Animal Health & Disease Defense Matrix",
                        "content": {
                            "title": "Master General Animal Health & Disease Defense Matrix",
                            "caption": "Master conceptual architecture: 1 Early Clinical Diagnosis -> 2 Engineered Housing & Nutrition -> 3 Biosecurity & 30-Day Quarantine -> 4 Rotational Parasite Control -> 5 Thermophilic Waste Management -> 6 High Productivity & Food Safety."
                        }
                    },
                    {
                        "type": "comparison_table",
                        "title": "Master General Animal Health Diagnostic and Protocol Matrix",
                        "content": {
                            "title": "Synthesized Animal Health Action Chart",
                            "headers": ["Livestock Species", "Primary Diagnostic Symptoms", "Etiological / Management Cause", "Correct Veterinary / Preventive Protocol"],
                            "rows": [
                                ["Cattle", "Left flank severe swelling; kicking at belly", "Trapped rumen fermentation gases (Bloat)", "Drench with vegetable oil / emergency trocar & cannula puncture"],
                                ["Sheep", "Bottle jaw (fluid chin swelling); lagging", "Hypoproteinemia from Haemonchus worms", "Albendazole anthelmintic drench + 6-week pasture rotation"],
                                ["Swine", "Raised diamond skin plaques; high fever", "Erysipelothrix rhusiopathiae bacterial infection", "Injectable veterinary penicillin + strict pen bio-sanitation"],
                                ["Poultry", "Twisted necks (torticollis); green diarrhea", "Newcastle Disease viral infection", "Mandatory vaccination at Day 14 and Day 28 via drinking water"],
                                ["Rabbits", "White nasal discharge; matted front paws", "Pasteurella multocida (Snuffles)", "Isolate infected stock; improve hutch cross-ventilation"]
                            ]
                        }
                    }
                ],
                [
                    {
                        "type": "mini_activity",
                        "title": "Performance Task: The Kiambu Smallholder Dairy Farm Health Crisis Audit",
                        "content": {
                            "title": "Clinical Consulting Case Study",
                            "task": "A smallholder farm has 3 calves with watery scours, dull sunken eyes, and pneumonia. The calf pen is dark, damp, with 30cm wet manure, located under an overflowing compost heap. The farmer is feeding human amoxicillin pills.\n\n**Your Deliverable**: Write an Emergency Health Audit:\n1. Identify 3 environmental housing errors causing the scours and pneumonia.\n2. Explain why feeding human amoxicillin is dangerous (AMR and toxicity).\n3. Draft a step-by-step emergency sanitation, isolation, and housing reform plan.",
                            "materials": ["Case Handout", "Response Template", "Pen"],
                            "safety": "Ensure rigorous, evidence-based recommendations."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Core Summary: Health Mastery",
                        "content": {
                            "title": "Key Takeaways",
                            "text": "- **Early clinical detection prevents catastrophic herd outbreaks**.\n- **Combine engineered housing, biosecurity, and vaccination**.\n- **Break parasite life cycles with rotational grazing**.\n- **Maintain strict biosecurity to protect farm profit and public health**."
                        }
                    }
                ],
                # Pages 4 to 8: 8 Summative Assessment MCQs
                [
                    {
                        "type": "knowledge_check",
                        "title": "Summative MCQ 1: Biological Rationale for High Feed Conversion",
                        "content": {
                            "question": "From a physiological perspective, why does keeping livestock in an optimal state of health directly maximize their Feed Conversion Efficiency (FCE)?",
                            "options": [
                                "Healthy animals have smaller stomachs that require less forage",
                                "In disease-free animals, nutrient energy is directed fully toward cellular growth, milk synthesis, or egg production, rather than being squandered to generate fever or repair inflamed tissues",
                                "Healthy animals convert water directly into solid bone",
                                "Pathogens in sick animals eat grass faster than the cow"
                            ],
                            "answer": "B",
                            "explanation": "When an animal is diseased or fighting subclinical infections, its metabolic system diverts large amounts of dietary amino acids, glucose, and energy toward synthesizing white blood cells, generating fever, and repairing damaged tissues, severely depressing production efficiency."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Summative MCQ 2: Clinical Meaning of Rumen Stasis",
                        "content": {
                            "question": "A dairy farmer observes that a mature Friesian cow has completely ceased chewing its cud (rumination) for over 10 hours. What does this clinical sign indicate to the herd manager?",
                            "options": [
                                "The cow has decided to sleep during the day",
                                "Rumen motility and microbial fermentation have shut down (rumen stasis), indicating acute digestive acidosis, hardware disease, or severe systemic fever",
                                "The cow's teeth have grown too sharp to chew grass",
                                "The cow is producing cheese in its rumen"
                            ],
                            "answer": "B",
                            "explanation": "Active rumination requires continuous muscular contractions of the rumen and a balanced microbial ecosystem. Cessation of cud-chewing is a severe warning sign that rumen motility has ceased (rumen stasis) due to metabolic acidosis, fever, or traumatic peritonitis."
                        }
                    }
                ],
                [
                    {
                        "type": "knowledge_check",
                        "title": "Summative MCQ 3: Submandibular Edema (Bottle Jaw) Pathophysiology",
                        "content": {
                            "question": "What is the specific pathophysiological mechanism that leads to the development of submandibular edema (Bottle Jaw) in sheep heavily infested with Haemonchus contortus (wireworms)?",
                            "options": [
                                "The worms migrate into the sheep's mouth and block the salivary glands",
                                "The blood-sucking parasites consume massive amounts of red blood cells and serum albumin, causing severe hypoproteinemia that lowers oncotic pressure and allows fluid to leak into dependent tissues under the jaw",
                                "The sheep drinks excessive water to flush out the stomach worms",
                                "The sheep's neck muscles swell from coughing"
                            ],
                            "answer": "B",
                            "explanation": "*Haemonchus contortus* feeds voraciously on blood in the abomasum. This causes severe loss of serum albumin (hypoproteinemia). Because albumin maintains colloid oncotic pressure, its loss causes fluid to escape from blood capillaries into loose interstitial tissues, pooling under the jaw due to gravity."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Summative MCQ 4: Diagnostic Signs of Swine Erysipelas",
                        "content": {
                            "question": "Which of the following clinical signs is diagnostic for Swine Erysipelas (Diamond Skin Disease) in commercial pig production?",
                            "options": [
                                "Loss of all teeth and hooves",
                                "Raised, well-demarcated rhomboid (diamond-shaped) red or purple plaques on the skin, accompanied by high fever and joint stiffness",
                                "The pigs growing white woolly fleece",
                                "Constant sneezing with white bubbles from the snout"
                            ],
                            "answer": "B",
                            "explanation": "Swine Erysipelas, caused by the bacterium *Erysipelothrix rhusiopathiae*, produces classic raised, diamond-shaped erythematous skin plaques on the back and flanks, accompanied by high fever, painful joints, and acute lethargy."
                        }
                    }
                ],
                [
                    {
                        "type": "knowledge_check",
                        "title": "Summative MCQ 5: Diagnostic Clue of Rabbit Snuffles",
                        "content": {
                            "question": "Why does a rabbit suffering from Snuffles (Pasteurellosis) consistently display heavily matted, crusty fur on the inside surface of its front paws?",
                            "options": [
                                "The rabbit walks through wet bedding in the hutch",
                                "The rabbit instinctively uses the inside of its front paws to repeatedly wipe away the persistent purulent nasal discharge from its nose and face",
                                "Mites in the hutch specifically attack rabbit front paws",
                                "The front paws sweat excessively during respiratory infections"
                            ],
                            "answer": "B",
                            "explanation": "Rabbits with upper respiratory *Pasteurella* infections produce thick, mucopurulent nasal discharge. Because rabbits groom themselves frequently, they use their front paws like handkerchiefs to wipe their wet nostrils, resulting in crusty, matted fur on the medial side of their front legs."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Summative MCQ 6: Ammonia Gas Pathology and Housing Ventilation",
                        "content": {
                            "question": "How does poor ventilation in an enclosed livestock shed directly damage the respiratory immune defenses of sheep and calves, leading to severe pneumonia?",
                            "options": [
                                "It makes the animals' blood turn into water",
                                "High concentrations of ammonia gas from decomposing urine paralyze and strip away the protective ciliated epithelium of the respiratory tract, allowing airborne bacteria to colonize the lungs",
                                "It prevents the animals from breathing carbon dioxide",
                                "It causes the lungs to turn into fat"
                            ],
                            "answer": "B",
                            "explanation": "Ammonia vapor from urea breakdown is a severe chemical irritant. When it accumulates in poorly ventilated sheds, it paralyzes the cilia of the respiratory tract (mucociliary escalator), preventing the expulsion of inhaled dust and bacteria and allowing opportunistic pathogens (*Pasteurella*, *Mycoplasma*) to cause pneumonia."
                        }
                    }
                ],
                [
                    {
                        "type": "knowledge_check",
                        "title": "Summative MCQ 7: Biological Principle of the 30-Day Quarantine",
                        "content": {
                            "question": "Why must all newly purchased livestock be placed in an isolated quarantine pen located at least 100 meters away from the main herd for exactly 30 days?",
                            "options": [
                                "To teach the new animals how to walk in a straight line",
                                "To allow sufficient time for any subclinical incubating pathogens (such as Foot and Mouth or Brucellosis) to manifest clinically, preventing catastrophic contamination of the clean resident herd",
                                "To make sure the animal gets used to the farm workers' voices",
                                "To wait for the animal to grow a new coat of hair"
                            ],
                            "answer": "B",
                            "explanation": "Most acute and subacute infectious livestock diseases have incubation periods of 7 to 28 days. A 30-day quarantine guarantees that any latent pathogens carried by the newly introduced animal will manifest and can be diagnosed and treated without exposing the main herd."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Summative MCQ 8: Tracheal Aspiration Danger in Vertical Drenching",
                        "content": {
                            "question": "What is the fatal clinical danger of pulling a goat's muzzle vertically pointing directly toward the sky while administering an oral liquid dewormer?",
                            "options": [
                                "The goat will swallow its tongue",
                                "The vertical angle prevents the epiglottis from closing over the larynx, allowing the liquid drench to flood down the trachea into the lungs, causing acute drowning or fatal chemical aspiration pneumonia",
                                "The medicine will turn into poison inside the stomach",
                                "It permanently stretches the goat's vocal cords"
                            ],
                            "answer": "B",
                            "explanation": "Lifting the muzzle vertically locks the pharynx and prevents the epiglottis from sealing the tracheal opening during swallowing. The liquid medicine pours directly into the lungs instead of the esophagus, causing instant suffocation or severe, fatal aspiration pneumonia."
                        }
                    }
                ],
                # Page 8: Capstone Summary
                [
                    {
                        "type": "summary",
                        "title": "Topic 10 Capstone Summary: General Animal Health Mastery",
                        "content": {
                            "title": "Mastery Overview: Grade 10 General Animal Health, Prevention & Disease Control",
                            "text": "Congratulations on mastering **Topic 10: General Animal Health**!\n\nYou have mastered:\n- **Physiological Foundations**: Health as complete homeostasis, FCE, low somatic cells, morbidity vs mortality.\n- **Universal & Species Diagnostics**: Recognizing anorexia, lethargy; ruminant bloat and rumen stasis; sheep bottle jaw (hypoproteinemia); swine Erysipelas and ASF; poultry Newcastle vs Coccidiosis; rabbit snuffles and ear canker.\n- **The 3 Pillars of Prevention**: Balanced nutrition (Vitamin A); engineered ventilation (<10ppm ammonia) and dry bedding; daily bio-sanitation.\n- **Biosecurity & Immunization**: Disinfectant footbaths, 30-day quarantine pen (100m away); active antibody production via vaccines; 6-week poultry vaccination calendar.\n- **Parasite & Waste Control**: Rotational grazing breaking larval cycles; acaricide dipping against ticks; thermophilic composting ($>60^\\circ\\text{C}$) destroying pathogens; deep carcass burial with quicklime.\n- **Routine Care**: 5-point daily inspection; hoof trimming preventing foot rot; safe horizontal oral drenching.\n- **Health Planning & Advocacy**: Comprehensive AHPs, the Five Freedoms of Animal Welfare, and community leadership."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Topic 10 Final Takeaway",
                        "content": {
                            "title": "The Preventative Animal Health Maxim",
                            "text": "Prevention is always cheaper, more humane, and more profitable than treatment. Implement biosecurity, engineered housing, routine care, and compassionate welfare to guarantee thriving livestock, safe food, and prosperous agribusinesses."
                        }
                    }
                ]
            ]
        }
    ]

@transaction.atomic
def ingest_grade10_topic10(replace=False):
    """Executes the complete production ingestion of Grade 10 Agriculture Topic 10: General Animal Health."""
    print("=" * 80)
    print("STARTING INGESTION: CBC Grade 10 Agriculture — Topic 10: General Animal Health")
    print("=" * 80)

    curriculum = Curriculum.objects.filter(name__iexact="CBC").first()
    grade = Grade.objects.filter(curriculum=curriculum, name__icontains="10").first()
    subject = Subject.objects.filter(grade=grade, name__iexact="Agriculture").first()

    assert curriculum and grade and subject, "Curriculum/Grade/Subject not found!"

    topic_name = "General Animal Health"
    topic = Topic.objects.filter(subject=subject, name=topic_name).first()
    if not topic:
        topic = Topic.objects.create(
            subject=subject,
            name=topic_name,
            description="Comprehensive study of livestock health benefits, diagnostic clinical indicators across species, preventative housing and nutrition, biosecurity barriers, vaccination mechanics, parasite dynamics, thermophilic waste composting, routine care, and welfare health planning.",
            order=10
        )
        print(f"Created Topic 10: {topic.name} (ID: {topic.id})")
    else:
        topic.order = 10
        topic.description = "Comprehensive study of livestock health benefits, diagnostic clinical indicators across species, preventative housing and nutrition, biosecurity barriers, vaccination mechanics, parasite dynamics, thermophilic waste composting, routine care, and welfare health planning."
        topic.save()
        print(f"Resolved Topic 10: {topic.name} (ID: {topic.id})")

    if replace:
        print("Flag --replace active: Clearing existing LearningUnits and Lessons for Topic 10...")
        topic.learning_units.all().delete()
        topic.lessons.all().delete()

    curriculum_data = build_topic10_curriculum()
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
                    "topic_order": 10,
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
                    block_id=f"g10_agri_t10_u{u_order}_p{page_idx}_b{comp_idx}",
                    block_type=b_type,
                    component_type=b_type,
                    title=b_title,
                    content=b_content,
                    order=block_order_counter,
                    page_number=page_idx,
                    component_order=comp_idx,
                    page_title=b_title if comp_idx == 1 else None,
                    metadata={"topic_order": 10, "unit_order": u_order, "page": page_idx}
                )
                block_order_counter += 1
                total_blocks += 1

        print(f"  Ingested Unit {u_order}: {u_name} -> Lesson '{l_title}' ({len(pages)} Pages, {block_order_counter - 1} Blocks)")

    print("=" * 80)
    print(f"INGESTION COMPLETE: Topic 10 '{topic.name}'")
    print(f"  Total Units:   {total_units}")
    print(f"  Total Lessons: {total_lessons}")
    print(f"  Total Pages:   {total_pages}")
    print(f"  Total Blocks:  {total_blocks}")
    print("=" * 80)

if __name__ == "__main__":
    replace_flag = "--replace" in sys.argv
    ingest_grade10_topic10(replace=replace_flag)
