"""
VLearn Grade 10 Biology — Topic 9: Animal Transport
Production Ingestion Engine (5 Comprehensive Lessons)

Curriculum: CBC (Curriculum ID: 5)
Grade: Grade 10 (Grade ID: 5, Level: 10)
Subject: Biology (Subject ID: 35)
Topic: Animal Transport (Topic Order: 9)

Structured into 5 Comprehensive Learning Units & 5 Published Lessons (~47 Concept Cards):
  1. Significance and Types of Animal Transport Systems (9 Pages)
  2. Mammalian Heart, Blood Vessels, and Pumping Mechanism (10 Pages)
  3. Blood Components, Functions, and Blood Clotting (9 Pages)
  4. Human Lymphatic and Immune Systems (10 Pages)
  5. ABO and Rhesus Blood Grouping and Compatibility (9 Pages)

Usage:
  ./venv/bin/python curriculum/ingest_grade10_biology_topic9.py [--replace]
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
    """Removes bracket citations [52, 134], visual prompt text, and cleans double spaces."""
    if not text:
        return ""
    # Remove bracket citations like [52], [52, 134], [image_1]
    text = re.sub(r'\[(?:\d+|image_\d+|S\d+.*?|[\d,\s]+)\]', '', text)
    # Remove internal visual generation tags
    text = re.sub(r'\[VISUAL:\s*[^\]]+\]', '', text, flags=re.IGNORECASE)
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

def build_topic9_curriculum():
    """Returns the comprehensive pedagogical page and block structure for Grade 10 Biology Topic 9."""
    return [
        # =====================================================================
        # LESSON 9.1: Significance and Types of Animal Transport Systems
        # =====================================================================
        {
            "unit_order": 1,
            "unit_name": "Significance and Types of Animal Transport Systems",
            "unit_description": "Why large multicellular animals need circulatory systems: SA:Vol ratio constraints, open vs closed circulatory systems, and single vs double circulation across vertebrate classes.",
            "lesson_title": "Significance and Types of Animal Transport Systems",
            "pages": [
                # Page 1: Learning Focus
                [
                    {
                        "type": "learning_goal",
                        "title": "Learning Focus: Animal Transport Systems",
                        "content": {
                            "title": "Learning Focus: Animal Transport Systems",
                            "goals": [
                                "Explain why large multicellular animals require active transport systems based on surface area-to-volume ratio and metabolic demands.",
                                "Distinguish between open and closed circulatory systems with examples.",
                                "Contrast single and double circulatory pathways across fish, amphibians, reptiles, and mammals.",
                                "Trace the evolutionary progression of heart chambers from 2 to 4 across vertebrate classes."
                            ]
                        }
                    }
                ],
                # Page 2: Why Animals Need Transport Systems
                [
                    {
                        "type": "concept",
                        "title": "Why Large Animals Need Transport Systems",
                        "content": {
                            "heading": "The SA:Vol Problem — Why Diffusion Alone Fails",
                            "body": "Small unicellular organisms like Amoeba have a **large surface area-to-volume (SA:Vol) ratio** — their membrane surface is vast relative to their tiny internal volume, so passive diffusion is fast enough to deliver nutrients and remove wastes.\n\nAs multicellular animals grow larger, two structural constraints arise:\n\n**1. Decreased SA:Vol Ratio:** Internal volume increases exponentially faster than the surface area, leaving deep-seated cells too far from the body surface for diffusion to reach them in time.\n\n**2. High Metabolic Demand:** Active multicellular animals — especially birds and mammals — have high energy requirements to support locomotion, cellular work, and temperature regulation, requiring rapid transport of oxygen and glucose that diffusion cannot provide."
                        }
                    }
                ],
                # Page 3: SA:Vol Math Illustration
                [
                    {
                        "type": "concept",
                        "title": "SA:Vol Ratio Calculations Across Body Sizes",
                        "content": {
                            "heading": "How SA:Vol Ratio Decreases as Body Size Increases",
                            "body": "Consider three cubes representing organisms of increasing size:\n\n| Cube Size | Surface Area | Volume | SA:Vol Ratio |\n|:---|:---|:---|:---|\n| 1 cm | 6 cm² | 1 cm³ | **6:1** |\n| 2 cm | 24 cm² | 8 cm³ | **3:1** |\n| 3 cm | 54 cm² | 27 cm³ | **2:1** |\n\n**Key insight:** As body size increases, the SA:Vol ratio drops sharply. In a cube of 3 cm, diffusion from the outer surface cannot reach the inner cells fast enough to sustain life. This is why a simple single-celled Amoeba survives by diffusion alone, while an elephant requires an elaborate circulatory system pumping blood at high pressure to every organ."
                        }
                    }
                ],
                # Page 4: Open vs Closed Circulatory Systems
                [
                    {
                        "type": "concept",
                        "title": "Open versus Closed Circulatory Systems",
                        "content": {
                            "heading": "Open Circulatory Systems (e.g., Insects)",
                            "body": "**Open Circulatory System:**\n- The heart pumps blood (called **haemolymph**) into short blood vessels that empty into open body cavities called the **haemocoel**.\n- Tissues and organs are directly bathed in haemolymph, allowing slow diffusion of materials.\n- Blood returns to the tubular heart through tiny valve-guarded openings called **ostia** during heart relaxation.\n\n**Critical note:** Insect blood does NOT carry oxygen! Insects use an independent **tracheal system** that delivers oxygen directly to tissues through air-filled pipes. Their haemolymph only transports dissolved nutrients, hormones, and nitrogenous wastes.\n\n**Closed Circulatory System (e.g., Annelids, Vertebrates):**\n- Blood is strictly confined within blood vessels (arteries, capillaries, and veins) under high pressure.\n- Blood does not contact tissue cells directly; exchange occurs across thin capillary walls.\n- Allows faster, targeted, and highly regulated distribution of materials."
                        }
                    }
                ],
                # Page 5: Single vs Double Circulation
                [
                    {
                        "type": "concept",
                        "title": "Single versus Double Circulatory Systems",
                        "content": {
                            "heading": "Circulatory Pathway Types Across Vertebrates",
                            "body": "**Single Circulation (e.g., Bony Fish):**\n- Fish heart has only **2 chambers** — one atrium and one ventricle.\n- Path: Ventricle pumps deoxygenated blood → **Gills** (oxygenation) → **Body tissues** (oxygen delivery) → back to atrium.\n- Blood pressure drops drastically after passing through gill capillaries, resulting in slow flow — adequate for low-metabolic fish.\n\n**Double Circulation (e.g., Mammals, Birds, Reptiles, Amphibians):**\nBlood completes two separate circuits:\n1. **Pulmonary Circuit:** Heart → Pulmonary Artery → Lungs (oxygenation) → Pulmonary Vein → Heart.\n2. **Systemic Circuit:** Heart → Aorta → Body tissues (oxygen delivery) → Vena Cava → Heart.\n\nBy returning to the heart after oxygenation, blood is **re-pressurized** before the systemic circuit, ensuring rapid, high-pressure delivery of nutrients to active tissues."
                        }
                    }
                ],
                # Page 6: Heart Chamber Evolution
                [
                    {
                        "type": "concept",
                        "title": "Evolutionary Progression of Heart Chambers",
                        "content": {
                            "heading": "From 2 to 4 Chambers — A Vertebrate Story",
                            "body": "**Fish (2 Chambers):** 1 atrium + 1 ventricle. Single circulation. Some mixing of oxygenated and deoxygenated blood is acceptable at their low metabolic rate.\n\n**Amphibians (3 Chambers):** 2 atria + 1 ventricle. Left atrium receives oxygenated blood from skin/lungs; right atrium receives deoxygenated blood from body. Partial mixing occurs in the single ventricle.\n\n**Reptiles (3 Chambers + Incomplete Septum):** 2 atria + 1 ventricle with a partial muscular partition significantly reducing mixing. Exception: Crocodilians have a fully 4-chambered heart.\n\n**Mammals and Birds (4 Chambers):** 2 atria + 2 ventricles, completely separated by a solid muscular **septum**. Zero mixing of oxygenated and deoxygenated blood — essential for high metabolic rate and maintaining constant endothermic body temperature."
                        }
                    }
                ],
                # Page 7: Common Misconception
                [
                    {
                        "type": "concept",
                        "title": "Common Misconception: Insect Blood and Oxygen",
                        "content": {
                            "heading": "Misconception: Insect Blood Carries Oxygen Like Human Blood",
                            "body": "**You may think:** Since grasshoppers have blood and a heart, their blood must carry oxygen just like human blood.\n\n**Actually:** Insect blood (haemolymph) is completely devoid of respiratory pigments like haemoglobin and plays **zero role** in oxygen transport. Because insects are highly active, relying on a slow open circulatory system for gas transport would be fatal.\n\nInstead, insects use a highly specialized, air-filled pipe network called the **tracheal system** — a system of rigid tubes called tracheae that branch into microscopic tracheoles — to deliver gaseous oxygen directly from the atmosphere into individual cells, bypassing the circulatory system entirely."
                        }
                    }
                ],
                # Page 8: Key Terms
                [
                    {
                        "type": "key_terms",
                        "title": "Key Terms: Animal Transport Systems",
                        "content": {
                            "terms": [
                                {"term": "Surface Area-to-Volume Ratio (SA:Vol)", "definition": "The relationship between an organism's outer boundary surface and its total internal volume — dictates whether passive diffusion is sufficient for nutrient and gas delivery."},
                                {"term": "Open Circulatory System", "definition": "A system where blood (haemolymph) is pumped into open body cavities (haemocoel) and bathes tissues directly; found in insects."},
                                {"term": "Closed Circulatory System", "definition": "A system where blood remains completely confined within a network of blood vessels; found in vertebrates and annelids."},
                                {"term": "Single Circulation", "definition": "Blood passes through the heart only once per complete circuit; found in fish, where blood goes heart → gills → body → heart."},
                                {"term": "Double Circulation", "definition": "Blood passes through the heart twice per complete circuit via pulmonary and systemic loops; found in mammals, birds, and reptiles."},
                                {"term": "Haemolymph", "definition": "The blood-like fluid in open circulatory systems (e.g., insects) that transports nutrients and wastes but not oxygen."},
                                {"term": "Haemocoel", "definition": "The open body cavity that haemolymph floods and bathes the organs in, in insects and other arthropods."}
                            ]
                        }
                    }
                ],
                # Page 9: Knowledge Check
                [
                    {
                        "type": "assessment",
                        "title": "Knowledge Check: Transport Systems",
                        "content": {
                            "question": "An evolutionary biologist discovers a fossil of an active, warm-blooded prehistoric animal. Based on structure-function relationships, which type of circulatory pathway and heart structure did this animal most likely possess?",
                            "options": [
                                "A closed single circulatory system with a 2-chambered heart",
                                "An open circulatory system with a tubular, multi-chambered heart",
                                "A closed double circulatory system with a 4-chambered heart",
                                "A closed double circulatory system with a 3-chambered heart"
                            ],
                            "correct_index": 2,
                            "explanation": "Warm-bloodedness (endothermy) requires high metabolic rates, which physically demand a closed double circulatory system to provide rapid, high-pressure blood flow. A 4-chambered heart is essential to completely prevent any mixing of oxygenated and deoxygenated blood, maximizing oxygen delivery to active tissues."
                        }
                    }
                ],
            ]
        },

        # =====================================================================
        # LESSON 9.2: Mammalian Heart, Blood Vessels, and Pumping Mechanism
        # =====================================================================
        {
            "unit_order": 2,
            "unit_name": "Mammalian Heart, Blood Vessels, and Pumping Mechanism",
            "unit_description": "Internal anatomy of the 4-chambered mammalian heart, the cardiac cycle (systole and diastole), arterial/capillary/venous structure-function relationships, and nervous/hormonal heart rate regulation.",
            "lesson_title": "Mammalian Heart, Blood Vessels, and Pumping Mechanism",
            "pages": [
                # Page 1: Learning Focus
                [
                    {
                        "type": "learning_goal",
                        "title": "Learning Focus: The Mammalian Heart",
                        "content": {
                            "title": "Learning Focus: The Mammalian Heart",
                            "goals": [
                                "Describe the internal and external physical structure of the mammalian heart.",
                                "Explain the pumping mechanism of the heart during the cardiac cycle — systole and diastole.",
                                "Relate the structures of arteries, capillaries, and veins to their transport roles.",
                                "Safely and ethically observe the structure of a mammalian heart in a laboratory setting."
                            ]
                        }
                    }
                ],
                # Page 2: Heart Anatomy
                [
                    {
                        "type": "concept",
                        "title": "Anatomy of the Mammalian Heart",
                        "content": {
                            "heading": "The 4-Chambered Heart: Structure and Design",
                            "body": "The mammalian heart is divided into left and right halves by a muscular partition called the **septum**. This ensures deoxygenated blood on the right side never mixes with oxygenated blood on the left.\n\n**The four chambers:**\n- **Right Atrium:** Thin-walled upper chamber receiving deoxygenated blood from the body via the **vena cava**.\n- **Right Ventricle:** Pumps deoxygenated blood to the lungs via the **pulmonary artery**.\n- **Left Atrium:** Receives oxygenated blood from the lungs via the **pulmonary vein**.\n- **Left Ventricle:** Has the **thickest muscular wall** (3× thicker than the right ventricle) — must pump oxygenated blood throughout the entire systemic body via the **aorta**."
                        }
                    }
                ],
                # Page 3: Path of Blood Through the Heart
                [
                    {
                        "type": "concept",
                        "title": "The Path of Blood Through the Heart",
                        "content": {
                            "heading": "Step-by-Step Blood Flow Through the 4 Chambers",
                            "body": "1. **Deoxygenated blood** from body tissues enters the **right atrium** via the superior and inferior **vena cava**.\n2. The right atrium contracts, pushing blood through the **tricuspid valve** into the **right ventricle**.\n3. The right ventricle contracts, closing the tricuspid valve and pumping blood through the **semi-lunar valve** into the **pulmonary artery** → lungs.\n4. In the lungs, blood absorbs oxygen and releases carbon dioxide.\n5. **Oxygenated blood** returns from the lungs and enters the **left atrium** via the **pulmonary vein**.\n6. The left atrium contracts, pushing blood through the **bicuspid (mitral) valve** into the **left ventricle**.\n7. The left ventricle contracts powerfully, closing the bicuspid valve and pumping blood through the **semi-lunar valve** into the **aorta** → entire body."
                        }
                    }
                ],
                # Page 4: Cardiac Cycle
                [
                    {
                        "type": "concept",
                        "title": "The Cardiac Cycle: Systole and Diastole",
                        "content": {
                            "heading": "How the Heart Beats: 3 Phases of the Cardiac Cycle",
                            "body": "**Phase 1 — Joint Diastole (Relaxation):**\n- Both atria and ventricles relax.\n- Blood from vena cava and pulmonary veins flows passively into the atria and through open AV valves into the ventricles.\n- Semi-lunar valves remain closed (preventing arterial backflow).\n\n**Phase 2 — Atrial Systole (Atrial Contraction):**\n- Both atria contract simultaneously, squeezing the remaining blood through the AV valves to fully fill the ventricles.\n\n**Phase 3 — Ventricular Systole (Ventricular Contraction):**\n- Ventricle walls contract powerfully.\n- The sharp pressure rise forces the **tricuspid and bicuspid valves to snap shut** — producing the low-pitched **\"lub\"** sound.\n- High pressure then forces the **semi-lunar valves open**, pumping blood into the pulmonary artery and aorta.\n- As ventricles begin to relax, back-pressure in the arteries snaps the **semi-lunar valves shut** — producing the higher-pitched **\"dup\"** sound."
                        }
                    }
                ],
                # Page 5: Blood Vessels Structure-Function
                [
                    {
                        "type": "concept",
                        "title": "Arteries, Capillaries, and Veins: Structure-Function",
                        "content": {
                            "heading": "The Three Types of Blood Vessels",
                            "body": "| Feature | Arteries | Capillaries | Veins |\n|:---|:---|:---|:---|\n| **Function** | Carry blood away from the heart at high pressure. | Site of material exchange between blood and tissue cells. | Return blood to the heart at low pressure. |\n| **Wall Structure** | Very thick: dense elastic fiber and smooth muscle layers. | Microscopic: single layer of endothelial cells only. | Thin walls with little elastic fiber or smooth muscle. |\n| **Lumen Size** | Narrow lumen to maintain high blood pressure. | Extremely narrow — just wide enough for one RBC. | Wide lumen to minimize resistance to slow flow. |\n| **Valves** | None (except semi-lunar valves at heart exit). | None. | Yes — pocket valves throughout to prevent backflow. |"
                        }
                    }
                ],
                # Page 6: Heart Rate Regulation
                [
                    {
                        "type": "concept",
                        "title": "Nervous and Hormonal Control of Heart Rate",
                        "content": {
                            "heading": "How the Brain and Hormones Regulate the Heartbeat",
                            "body": "The resting heart rate (average 72 beats per minute) is constantly modulated to adapt to environmental demands:\n\n**Nervous Regulation:**\nThe medulla oblongata in the brain regulates heart rate via two nerves:\n- **Sympathetic nerve** releases **noradrenaline** → speeds up heart rate during exercise or stress.\n- **Vagus (parasympathetic) nerve** releases **acetylcholine** → slows heart rate during rest and digestion.\n\n**Hormonal Regulation:**\nDuring fear or intense exercise, the adrenal glands secrete the hormone **adrenaline** directly into the blood, causing an immediate rise in heart rate and cardiac output to prepare muscles for rapid action.\n\n**The SAN Pacemaker:**\nThe heart's own internal pacemaker is the **sino-atrial node (SAN)**, a cluster of specialized muscle cells in the right atrial wall that generates rhythmic electrical impulses — initiating each heartbeat automatically, independent of the nervous system."
                        }
                    }
                ],
                # Page 7: Heart Dissection Practical
                [
                    {
                        "type": "concept",
                        "title": "Practical: Mammalian Heart Dissection",
                        "content": {
                            "heading": "Procedure — Observing Heart Structure",
                            "body": "**Objective:** Observe the chambers, valves, wall thickness, and vessels of a mammalian heart.\n\n**Materials:** Fresh sheep or goat heart (from a local butcher), dissecting tray, scalpel, forceps, scissors, blunt seeker, gloves.\n\n**Ethical Safety Rule:** Always handle animal specimens humanely and with respect. Wear protective gloves throughout; wash hands with disinfectant soap afterward.\n\n**Procedure:**\n1. Place the heart on the dissecting tray. Identify the front (ventral) side by the diagonal strip of fat containing the **coronary artery**.\n2. Locate the thick, wide, elastic **aorta** at the top.\n3. Cut down the right side (from superior vena cava → right atrium → right ventricle). Observe the three white flaps of the **tricuspid valve** connected by thread-like **tendinous cords**.\n4. Cut down the left side (from pulmonary veins → left atrium → left ventricle). Compare wall thickness — left ventricle measures ~1.2–1.5 cm; right ventricle measures ~0.3–0.5 cm.\n5. Cut open the base of the aorta to observe the cup-shaped **semi-lunar valves**."
                        }
                    }
                ],
                # Page 8: Common Misconception
                [
                    {
                        "type": "concept",
                        "title": "Common Misconception: Pulse and Blood Vessels",
                        "content": {
                            "heading": "Misconception: The Pulse is Felt in Veins",
                            "body": "**You may think:** Your pulse is caused by blood flowing through your veins.\n\n**Actually:** Your pulse is felt exclusively in **arteries**. It is the physical shockwave of expansion and elastic recoil of arterial walls caused by high-pressure blood being forced out of the left ventricle during ventricular systole.\n\nBlood pressure in veins is extremely low and steady, which is why veins do not have a pulse. To help push venous blood back toward the heart, veins rely on:\n- **Pocket valves** that prevent backflow.\n- **Skeletal muscle contractions** squeezing the vein walls during movement.\n- **Breathing movements** creating negative pressure in the chest cavity that draws blood toward the heart."
                        }
                    }
                ],
                # Page 9: Key Terms
                [
                    {
                        "type": "key_terms",
                        "title": "Key Terms: Heart and Blood Vessels",
                        "content": {
                            "terms": [
                                {"term": "Atrium", "definition": "A thin-walled upper chamber of the heart that receives incoming blood from the veins."},
                                {"term": "Ventricle", "definition": "A thick-walled muscular lower chamber of the heart that pumps blood out into the arteries."},
                                {"term": "AV Valves (Atrioventricular Valves)", "definition": "Flaps of tissue between atria and ventricles (tricuspid on right, bicuspid on left) that prevent backflow during ventricular contraction."},
                                {"term": "Semi-Lunar Valves", "definition": "Half-moon-shaped valves at the exits of the ventricles (base of aorta and pulmonary artery) that prevent blood from flowing back into the heart."},
                                {"term": "Systole", "definition": "The phase of the cardiac cycle where the heart muscle actively contracts, pumping blood out of the chambers."},
                                {"term": "Diastole", "definition": "The phase of the cardiac cycle where the heart muscle relaxes, allowing the chambers to fill with blood."},
                                {"term": "Septum", "definition": "The thick muscular wall dividing the left and right sides of the heart, preventing mixing of oxygenated and deoxygenated blood."}
                            ]
                        }
                    }
                ],
                # Page 10: Knowledge Check
                [
                    {
                        "type": "assessment",
                        "title": "Knowledge Check: Heart Valves and Murmurs",
                        "content": {
                            "question": "During a routine medical check-up, a doctor detects a high-pitched 'gurgling' murmur sound right after the first 'lub' sound of a patient's heartbeat. Based on structure-function relationships, what physical defect is most likely causing this murmur?",
                            "options": [
                                "The semi-lunar valves are failing to close properly.",
                                "The bicuspid or tricuspid valves are failing to seal completely, allowing blood to leak backward into the atria during ventricular systole.",
                                "The muscular septum separating the left and right ventricles has completely closed.",
                                "The coronary artery is blocked by a blood clot."
                            ],
                            "correct_index": 1,
                            "explanation": "The first 'lub' sound is caused by the closure of the bicuspid and tricuspid (AV) valves during ventricular systole. If these valves are damaged or fail to seal completely, high-pressure ventricular contraction forces blood to leak backward into the atria, creating turbulent, audible gurgling — a classic heart murmur."
                        }
                    }
                ],
            ]
        },

        # =====================================================================
        # LESSON 9.3: Blood Components, Functions, and Blood Clotting
        # =====================================================================
        {
            "unit_order": 3,
            "unit_name": "Blood Components, Functions, and Blood Clotting",
            "unit_description": "The four components of blood (plasma, erythrocytes, leucocytes, platelets), red blood cell adaptations for oxygen transport, and the biochemical clotting cascade from thromboplastin to fibrin.",
            "lesson_title": "Blood Components, Functions, and Blood Clotting",
            "pages": [
                # Page 1: Learning Focus
                [
                    {
                        "type": "learning_goal",
                        "title": "Learning Focus: Blood and Clotting",
                        "content": {
                            "title": "Learning Focus: Blood and Clotting",
                            "goals": [
                                "Identify the major components of blood and describe their individual functions.",
                                "Explain the biochemical mechanism of blood clotting in humans, from thromboplastin to fibrin net.",
                                "Relate the structural adaptations of red blood cells to their oxygen transport role.",
                                "Appreciate the role of white blood cells in body defense."
                            ]
                        }
                    }
                ],
                # Page 2: Blood Composition Overview
                [
                    {
                        "type": "concept",
                        "title": "The Four Components of Blood",
                        "content": {
                            "heading": "What Is Blood? A Specialized Fluid Tissue",
                            "body": "Blood is approximately **55% liquid plasma** and **45% formed cellular elements**:\n\n**1. Plasma (55%):**\n- A yellowish fluid of 90% water and 10% dissolved solutes (plasma proteins, glucose, amino acids, carbon dioxide, urea, hormones, and mineral salts).\n- Serves as a universal solvent and transport medium, distributing heat and delivering nutrients to tissues while carrying metabolic wastes to excretory organs.\n\n**2. Red Blood Cells / Erythrocytes (45%):**\nTransport oxygen from the lungs to all respiring body tissues.\n\n**3. White Blood Cells / Leucocytes (<1%):**\nDefend the body against infection by pathogens.\n\n**4. Platelets / Thrombocytes (<1%):**\nTiny, membrane-bound fragments that initiate the blood clotting cascade at wound sites."
                        }
                    }
                ],
                # Page 3: RBC Adaptations
                [
                    {
                        "type": "concept",
                        "title": "Red Blood Cell Adaptations for Oxygen Transport",
                        "content": {
                            "heading": "Why Are Red Blood Cells Perfectly Designed for Oxygen Delivery?",
                            "body": "**Biconcave Shape:** Creates a disc with indentations on both faces, maximizing the surface area-to-volume ratio and dramatically speeding up the rate of oxygen diffusion into and out of the cell.\n\n**Lack of a Nucleus (Enucleation):** Mature red blood cells lose their nucleus entirely to create more internal volume to pack more haemoglobin molecules, maximizing oxygen-carrying capacity.\n\n**Flexible Membrane:** Allows the cell to squeeze through capillaries narrower than its own diameter without rupturing.\n\n**Packed with Haemoglobin:** High concentration of this iron-containing protein allows each cell to bind millions of oxygen molecules. The iron (Fe²⁺) in haemoglobin reversibly binds to oxygen:\n\nHaemoglobin + O₂ ⇌ Oxyhaemoglobin (in lungs)\nOxyhaemoglobin ⇌ Haemoglobin + O₂ (in respiring tissues)"
                        }
                    }
                ],
                # Page 4: White Blood Cells
                [
                    {
                        "type": "concept",
                        "title": "White Blood Cells: Two Lines of Defense",
                        "content": {
                            "heading": "Phagocytes and Lymphocytes — The Immune Defenders",
                            "body": "**Phagocytes (e.g., Macrophages/Neutrophils):**\n- Have lobed, irregular nuclei and flexible cytoplasm.\n- Squeeze through capillary walls via diapedesis to reach infected tissues.\n- Engulf and digest foreign bacteria inside a vacuole using powerful digestive enzymes (lysozymes) — a process called **phagocytosis**.\n- This is a **non-specific** defense — active against any foreign cell regardless of type.\n\n**Lymphocytes:**\n- Have large, round nuclei and produce specific protein keys called **antibodies**.\n- Each lymphocyte recognizes one specific foreign protein marker called an **antigen** on the surface of a pathogen.\n- Once activated, lymphocytes multiply rapidly (clonal expansion) and secrete millions of Y-shaped antibodies.\n- Antibodies neutralize pathogens by agglutination, lysis, or toxin neutralization.\n- This is a **specific** defense — targeted at a particular pathogen."
                        }
                    }
                ],
                # Page 5: Blood Clotting Cascade
                [
                    {
                        "type": "concept",
                        "title": "The Biochemical Blood Clotting Cascade",
                        "content": {
                            "heading": "From Wound to Scab: The 5-Step Clotting Cascade",
                            "body": "When a blood vessel is damaged, a rapid chemical cascade seals the wound:\n\n**Step 1 — Platelet Plug:** Platelets adhere to broken collagen fibers at the wound site, forming a temporary plug.\n\n**Step 2 — Thromboplastin Release:** Damaged tissue cells and ruptured platelets release the enzyme **thromboplastin**.\n\n**Step 3 — Prothrombin Activation:** In the presence of **Calcium ions (Ca²⁺)** and **Vitamin K**, thromboplastin catalyzes the conversion of inactive plasma protein **prothrombin** → active enzyme **thrombin**.\n\n**Step 4 — Fibrin Thread Formation:** Active thrombin converts the soluble plasma protein **fibrinogen** → insoluble, thread-like fibers called **fibrin**.\n\n**Step 5 — Fibrin Net:** Insoluble fibrin fibers weave a sticky mesh across the wound, trapping red blood cells and platelets to form a solid plug that dries into a protective **scab**."
                        }
                    }
                ],
                # Page 6: Clotting Cascade Diagram
                [
                    {
                        "type": "concept",
                        "title": "Clotting Cascade — Visual Summary",
                        "content": {
                            "heading": "The Clotting Cascade: A Chemical Production Line",
                            "body": "```\nDamaged Tissues + Ruptured Platelets\n           ↓\n      Thromboplastin (enzyme released)\n           ↓  (requires Ca²⁺ + Vitamin K)\nProthrombin ────────────→ Thrombin\n(Inactive plasma protein)    (Active enzyme)\n           ↓\nFibrinogen ──────────────→ Fibrin Threads\n(Soluble plasma protein)    (Insoluble mesh)\n           ↓\n  Fibrin Net traps RBCs → Scab forms\n```\n\n**Key cofactors:**\n- **Calcium ions (Ca²⁺):** Essential for the conversion of prothrombin to thrombin. Patients receiving anticoagulant therapy may have chelating agents added to donated blood samples to bind Ca²⁺ and prevent premature clotting.\n- **Vitamin K:** A fat-soluble vitamin produced by gut bacteria, essential for synthesizing prothrombin in the liver."
                        }
                    }
                ],
                # Page 7: Misconception — Agglutination vs Clotting
                [
                    {
                        "type": "concept",
                        "title": "Misconception: Agglutination vs Blood Clotting",
                        "content": {
                            "heading": "Are Agglutination and Blood Clotting the Same Process?",
                            "body": "**You may think:** Agglutination (blood clumping during a mismatched transfusion) and coagulation (blood clotting at a wound) are the same process.\n\n**Actually:** They are completely different biological events:\n\n**Blood Clotting (Coagulation):**\n- A protective enzyme cascade converting soluble fibrinogen into insoluble fibrin nets to seal wounds and prevent blood loss.\n- Initiated by tissue damage and platelet rupture.\n- A normal, life-saving response.\n\n**Agglutination:**\n- An immune antigen-antibody reaction where antibodies in plasma bind to mismatched antigens on donor red blood cells.\n- Causes the donor red blood cells to clump together and block blood vessels.\n- Can cause haemolysis (rupture of clumped cells), releasing free haemoglobin that blocks kidney tubules, leading to acute kidney failure and death."
                        }
                    }
                ],
                # Page 8: Key Terms
                [
                    {
                        "type": "key_terms",
                        "title": "Key Terms: Blood and Clotting",
                        "content": {
                            "terms": [
                                {"term": "Plasma", "definition": "The liquid component of blood (55%): water, plasma proteins, nutrients, hormones, ions, and dissolved wastes."},
                                {"term": "Erythrocyte (Red Blood Cell)", "definition": "A biconcave, enucleated cell packed with haemoglobin, specialized for transporting oxygen from lungs to tissues."},
                                {"term": "Leucocyte (White Blood Cell)", "definition": "A nucleated blood cell involved in defending the body against pathogens via phagocytosis or antibody production."},
                                {"term": "Platelet (Thrombocyte)", "definition": "A tiny, disk-shaped cell fragment that initiates blood clotting by releasing thromboplastin at wound sites."},
                                {"term": "Haemoglobin", "definition": "A red iron-containing protein pigment in red blood cells that reversibly binds to oxygen for transport."},
                                {"term": "Thromboplastin", "definition": "An enzyme released by damaged tissues and ruptured platelets that initiates the clotting cascade."},
                                {"term": "Fibrin", "definition": "The insoluble protein thread produced from fibrinogen by thrombin; forms the mesh net of a blood clot."}
                            ]
                        }
                    }
                ],
                # Page 9: Knowledge Check
                [
                    {
                        "type": "assessment",
                        "title": "Knowledge Check: Blood Clotting",
                        "content": {
                            "question": "A toddler in a rural village is diagnosed with a rare genetic disorder that prevents her liver from synthesizing the plasma protein prothrombin. Which symptom will this child exhibit?",
                            "options": [
                                "Severe muscle cramps during physical play",
                                "Poor oxygen distribution leading to pale skin and fatigue",
                                "Inability to mount immune defenses against bacterial infections",
                                "Persistent, life-threatening bleeding from even minor cuts and bruises"
                            ],
                            "correct_index": 3,
                            "explanation": "Prothrombin is a vital inactive plasma protein in the clotting cascade. Without prothrombin, the body cannot generate active thrombin, which is needed to convert soluble fibrinogen into insoluble fibrin nets. Consequently, the child's blood will be unable to clot, leading to prolonged bleeding (haemophilia-like condition) from even minor injuries."
                        }
                    }
                ],
            ]
        },

        # =====================================================================
        # LESSON 9.4: Human Lymphatic and Immune Systems
        # =====================================================================
        {
            "unit_order": 4,
            "unit_name": "Human Lymphatic and Immune Systems",
            "unit_description": "Formation of tissue fluid and lymph from blood capillaries, the one-way lymphatic drainage system, lymph node structure, and the dual mechanism of human immunity — non-specific phagocytosis and specific antibody production.",
            "lesson_title": "Human Lymphatic and Immune Systems",
            "pages": [
                # Page 1: Learning Focus
                [
                    {
                        "type": "learning_goal",
                        "title": "Learning Focus: Lymphatic System and Immunity",
                        "content": {
                            "title": "Learning Focus: Lymphatic System and Immunity",
                            "goals": [
                                "Explain how tissue fluid and lymph are formed from blood capillaries.",
                                "Describe the structure and function of the human lymphatic system.",
                                "Contrast tissue fluid, lymph, and blood in terms of composition.",
                                "Describe the dual mechanism of human immunity — non-specific phagocytosis and specific antibody-antigen defense."
                            ]
                        }
                    }
                ],
                # Page 2: Formation of Tissue Fluid
                [
                    {
                        "type": "concept",
                        "title": "Formation of Tissue Fluid from Blood Capillaries",
                        "content": {
                            "heading": "How Does Tissue Fluid Form? The Capillary Filtration Process",
                            "body": "As blood flows from arteries into capillaries under high pressure, a physical filtration process occurs:\n\n**Step 1 — Ultrafiltration:** The high hydrostatic pressure at the **arterial end** of capillaries forces water and small dissolved solutes (glucose, oxygen, amino acids, ions) out through tiny capillary pores. Large plasma proteins, red blood cells, and platelets are too large to pass and remain inside the capillary. This leaked fluid is now called **tissue fluid**.\n\n**Step 2 — Material Exchange:** Tissue fluid directly bathes the cells, delivering oxygen and nutrients by diffusion and absorbing carbon dioxide and metabolic wastes.\n\n**Step 3 — Reabsorption:** At the **venous end** of the capillary, the high concentration of remaining plasma proteins creates an osmotic pull (oncotic pressure), drawing about **90%** of the tissue fluid back into the capillary.\n\n**Step 4 — Lymph Entry:** The remaining **10%** of tissue fluid cannot be reabsorbed. To prevent oedema, this fluid drains into open-ended **lymphatic capillaries** and is now called **lymph**."
                        }
                    }
                ],
                # Page 3: Lymphatic System Structure
                [
                    {
                        "type": "concept",
                        "title": "Structure of the Lymphatic System",
                        "content": {
                            "heading": "The Hidden Drainage Network — Structure and Components",
                            "body": "The lymphatic system is a **one-way drainage system** returning excess tissue fluid to the bloodstream. It consists of:\n\n**Lymphatic Capillaries:** Open-ended microscopic vessels that absorb excess tissue fluid. Unlike blood capillaries, they have no tight junctions, allowing fluid, large proteins, and even bacteria to enter.\n\n**Lymphatic Vessels:** Thin-walled tubes with pocket valves (similar to veins) ensuring lymph flows in one direction only — toward the chest.\n\n**Lymph Nodes:** Small, bean-shaped filters clustered at key junctions (neck, armpits, groin). Packed with active **macrophages** (engulfing bacteria) and **lymphocytes** (producing antibodies). As lymph flows through, pathogens are trapped and destroyed.\n\n**Lymphatic Ducts:** The largest lymphatic vessels (thoracic duct and right lymphatic duct) empty lymph back into the blood via the **subclavian veins** in the chest, restoring blood volume."
                        }
                    }
                ],
                # Page 4: Comparison Table
                [
                    {
                        "type": "concept",
                        "title": "Comparing Blood, Tissue Fluid, and Lymph",
                        "content": {
                            "heading": "Chemical Comparison: Blood vs Tissue Fluid vs Lymph",
                            "body": "| Feature | Blood | Tissue Fluid | Lymph |\n|:---|:---|:---|:---|\n| **Location** | Confined within blood vessels. | Spaces surrounding tissue cells. | Confined within lymphatic vessels. |\n| **Red Blood Cells** | Abundant. | Absent (too large to filter through capillary pores). | Absent. |\n| **Plasma Proteins** | High concentration. | Extremely low (only small proteins escape). | Low (reabsorbed proteins). |\n| **Glucose and Oxygen** | High (freshly delivered from intestine/lungs). | Moderate (being consumed by cells). | Low (after cell delivery). |\n| **Fat Content** | Low (except after a fatty meal). | Low. | High after eating — lymph vessels called lacteals absorb dietary fat from the small intestine. |"
                        }
                    }
                ],
                # Page 5: Non-Specific Immunity
                [
                    {
                        "type": "concept",
                        "title": "Non-Specific Immunity: Phagocytosis",
                        "content": {
                            "heading": "First Line Defense — Phagocytosis by Macrophages",
                            "body": "**Non-Specific Immunity (Phagocytosis):**\n\nPhagocytes (macrophages and neutrophils) provide the body's immediate, first-line cellular defense:\n\n1. A phagocyte detects chemical signals released by damaged cells or bacteria.\n2. The phagocyte migrates to the infection site by squeezing through capillary walls — a process called **diapedesis**.\n3. It extends cytoplasmic projections (**pseudopodia**) to flow around the foreign bacterium.\n4. The bacterium is enclosed inside a vesicle called a **phagosome**.\n5. Lysosomes fuse with the phagosome, releasing powerful digestive enzymes (**lysozymes**) that break down the bacterium.\n\n**Why is this defense non-specific?**\nPhagocytes do not need to recognize the specific type of pathogen — they attack any cell that displays non-self surface markers, providing broad-spectrum, immediate protection."
                        }
                    }
                ],
                # Page 6: Specific Immunity
                [
                    {
                        "type": "concept",
                        "title": "Specific Immunity: Antibody Production",
                        "content": {
                            "heading": "Second Line Defense — Targeted Antibody-Antigen Response",
                            "body": "**Specific Immunity (Antibody Production by Lymphocytes):**\n\n1. **Antigen Detection:** B-lymphocytes detect specific foreign proteins called **antigens** on the surface of a specific virus or bacterium.\n2. **Clonal Expansion:** The matching lymphocyte multiplies rapidly, producing thousands of identical copies.\n3. **Antibody Production:** B-lymphocytes differentiate into plasma cells that secrete millions of Y-shaped proteins called **antibodies** into the blood.\n\n**How Antibodies Destroy Pathogens:**\n- **Agglutination:** Antibodies bind to multiple pathogens simultaneously, clumping them together so they cannot infect cells and become easy phagocyte targets.\n- **Lysis:** Antibodies activate complement proteins that rupture the outer membrane of the pathogen, killing it.\n- **Neutralization:** Antibodies bind to and block toxic chemicals (toxins) released by bacteria, rendering them harmless.\n\n**Memory Cells:** Some activated lymphocytes become long-lived memory B-cells, enabling a faster, stronger response upon future exposure to the same pathogen — the basis of **immunity** and **vaccination**."
                        }
                    }
                ],
                # Page 7: Swollen Lymph Nodes Misconception
                [
                    {
                        "type": "concept",
                        "title": "Misconception: Swollen Lymph Nodes Mean Immune Failure",
                        "content": {
                            "heading": "Why Swollen Lymph Nodes During Infection Are Actually Good",
                            "body": "**You may think:** Swollen, painful lymph nodes in your neck during a throat infection mean the infection is spreading uncontrollably and your body is failing.\n\n**Actually:** Swollen lymph nodes are a sign of a **highly active, healthy immune response**!\n\nWhen a pathogen infects your throat, the lymphatic system drains the bacteria to the nearest lymph nodes in your neck. In response:\n- Macrophages inside the nodes rapidly engulf and destroy captured bacteria.\n- Lymphocytes proliferate intensely to produce large quantities of antibodies.\n- This rapid cellular division causes the node to **enlarge, become warm and tender** — but this is active immune combat, not failure.\n\nIf lymph nodes remain persistently enlarged without an active infection, this can signal a malignancy (lymphoma) and should be medically investigated."
                        }
                    }
                ],
                # Page 8: Key Terms
                [
                    {
                        "type": "key_terms",
                        "title": "Key Terms: Lymphatic System and Immunity",
                        "content": {
                            "terms": [
                                {"term": "Tissue Fluid (Intercellular Fluid)", "definition": "Fluid squeezed out of blood capillaries by hydrostatic pressure, bathing and supplying tissue cells with nutrients."},
                                {"term": "Lymph", "definition": "Tissue fluid that has entered the lymphatic capillaries to be returned to the blood circulatory system."},
                                {"term": "Lymph Node", "definition": "A bean-shaped filter organ packed with macrophages and lymphocytes that destroys pathogens in lymph."},
                                {"term": "Antigen", "definition": "A unique protein marker on the surface of a cell or pathogen that triggers an immune response."},
                                {"term": "Antibody", "definition": "A specific Y-shaped protein produced by B-lymphocytes that binds to and neutralizes a matching antigen."},
                                {"term": "Phagocytosis", "definition": "The process by which phagocytes engulf and digest foreign bacteria and debris using lysozyme enzymes."},
                                {"term": "Oedema", "definition": "Swelling of tissues caused by accumulation of tissue fluid when the lymphatic system fails to drain properly."}
                            ]
                        }
                    }
                ],
                # Page 9: Knowledge Check
                [
                    {
                        "type": "assessment",
                        "title": "Knowledge Check: Lymphatic System",
                        "content": {
                            "question": "A patient is diagnosed with a tropical parasitic disease where microscopic worms block her major lymphatic vessels in the groin. What physical symptom will this blockage cause in the patient's legs?",
                            "options": [
                                "Rapid blood clotting leading to deep vein thrombosis",
                                "Severe swelling (oedema) due to tissue fluid accumulating in the leg tissues without draining",
                                "Anaemia caused by a drop in red blood cell production",
                                "Immune deficiency due to a loss of skin barrier function"
                            ],
                            "correct_index": 1,
                            "explanation": "Under normal conditions, the lymphatic system drains the remaining 10% of tissue fluid from intercellular spaces back to the bloodstream. If lymphatic vessels in the groin are physically blocked by parasitic worms (filariasis/elephantiasis), tissue fluid cannot drain, leading to massive fluid accumulation and severe swelling (oedema) in the legs."
                        }
                    }
                ],
                # Page 10: Extra Concept — Vaccination
                [
                    {
                        "type": "concept",
                        "title": "Vaccination: Harnessing Immunological Memory",
                        "content": {
                            "heading": "How Vaccines Train the Immune System Without Causing Disease",
                            "body": "Vaccines exploit the specific immune system's ability to create **immunological memory**:\n\n**How Vaccination Works:**\n1. A vaccine introduces a harmless form of a pathogen — weakened live microorganisms, killed microorganisms, purified antigens, or mRNA instructions — into the body.\n2. The immune system mounts a full specific immune response: lymphocytes produce antibodies and proliferate.\n3. After the infection is cleared, long-lived **memory B-cells** and **memory T-cells** remain in the bloodstream.\n4. Upon future exposure to the actual pathogen, memory cells trigger a **secondary immune response** — antibodies are produced in days rather than weeks, at far higher concentrations.\n5. The pathogen is destroyed before symptoms develop.\n\n**Real-World Example:** The Measles, Mumps, and Rubella (MMR) vaccine introduced to Kenyan children as part of the Kenya Expanded Programme on Immunization (KEPI) has dramatically reduced measles mortality, which was once a leading cause of child death in Kenya."
                        }
                    }
                ],
            ]
        },

        # =====================================================================
        # LESSON 9.5: ABO and Rhesus Blood Grouping and Compatibility
        # =====================================================================
        {
            "unit_order": 5,
            "unit_name": "ABO and Rhesus Blood Grouping and Compatibility",
            "unit_description": "The biological basis of ABO and Rhesus blood grouping systems, blood antigen-antibody pairings, donor-recipient compatibility matrices, and clinical management of Rhesus incompatibility in pregnancy.",
            "lesson_title": "ABO and Rhesus Blood Grouping and Compatibility",
            "pages": [
                # Page 1: Learning Focus
                [
                    {
                        "type": "learning_goal",
                        "title": "Learning Focus: Blood Grouping",
                        "content": {
                            "title": "Learning Focus: Blood Grouping",
                            "goals": [
                                "Explain the biological basis of the ABO and Rhesus blood grouping systems.",
                                "Construct and interpret a blood donor-recipient compatibility matrix.",
                                "Predict the clinical consequences of mismatched blood transfusions.",
                                "Explain the clinical risk of Rhesus incompatibility during pregnancy and its prevention."
                            ]
                        }
                    }
                ],
                # Page 2: ABO System
                [
                    {
                        "type": "concept",
                        "title": "The ABO Blood Grouping System",
                        "content": {
                            "heading": "Blood Groups: Determined by Red Blood Cell Antigens",
                            "body": "Our blood group is genetically determined and is based on the presence or absence of two specific marker proteins (**Antigen A** and **Antigen B**) on the surface membrane of our red blood cells, and corresponding **antibodies** in our plasma:\n\n| Blood Group | Antigens on RBCs | Antibodies in Plasma |\n|:---|:---|:---|\n| **A** | Antigen A | Anti-B antibodies |\n| **B** | Antigen B | Anti-A antibodies |\n| **AB** | Both Antigen A and B | No antibodies |\n| **O** | No antigens (smooth surface) | Both Anti-A and Anti-B antibodies |\n\n**The immunological rule:** The body never makes antibodies against its own antigens. Group A individuals have Antigen A — so they produce Anti-B antibodies (not Anti-A), because Anti-A would destroy their own cells."
                        }
                    }
                ],
                # Page 3: Rhesus Factor
                [
                    {
                        "type": "concept",
                        "title": "The Rhesus (Rh) Factor Blood Grouping System",
                        "content": {
                            "heading": "The D Antigen: Rh-Positive and Rh-Negative",
                            "body": "The Rhesus system is based on an independent red blood cell surface antigen called **Antigen D** (the Rhesus factor):\n\n**Rhesus-Positive (Rh⁺):**\n- Red blood cells possess **Antigen D**.\n- Their plasma does not naturally contain anti-D antibodies (no need — they have the antigen).\n\n**Rhesus-Negative (Rh⁻):**\n- Red blood cells **lack Antigen D**.\n- Rh⁻ individuals do NOT naturally have anti-D antibodies in their plasma.\n- **Critical rule:** If an Rh⁻ person is exposed to Rh⁺ blood (through a mismatched transfusion OR during childbirth), their immune system will synthesize anti-D antibodies — sensitizing them against all future Rh⁺ exposures.\n\n**Combined notation:** Blood is typed using both systems simultaneously (e.g., A⁺, B⁻, O⁺, AB⁺). There are 8 main blood types in total when combining ABO (4 types) × Rh (positive/negative)."
                        }
                    }
                ],
                # Page 4: Transfusion Compatibility
                [
                    {
                        "type": "concept",
                        "title": "Blood Transfusion Compatibility and Agglutination",
                        "content": {
                            "heading": "The Golden Rule of Safe Blood Transfusion",
                            "body": "**The Golden Rule:** The donor's red blood cell antigens must never react with the recipient's plasma antibodies.\n\n**What happens when incompatible blood is transfused?**\n1. The recipient's antibodies immediately bind to the matching antigens on the donor's red blood cells.\n2. **Agglutination** occurs — donor red blood cells clump together.\n3. These clumps block microscopic blood capillaries, preventing oxygen delivery to organs.\n4. The immune system subsequently ruptures the clumped cells (**haemolysis**), releasing massive free haemoglobin that blocks kidney tubules — leading to acute kidney failure and potentially death.\n\n**Donor-Recipient Compatibility Matrix:**\n\n| Recipient Group | Can Safely Receive From |\n|:---|:---|\n| **A** | A and O |\n| **B** | B and O |\n| **AB** | A, B, AB, O — Universal Recipient |\n| **O** | O only — Universal Donor (can give to anyone) |"
                        }
                    }
                ],
                # Page 5: Universal Donor and Recipient
                [
                    {
                        "type": "concept",
                        "title": "Universal Donors and Universal Recipients",
                        "content": {
                            "heading": "O-Negative: The Universal Donor — AB-Positive: The Universal Recipient",
                            "body": "**Universal Donor — O-Negative (O⁻):**\n- O⁻ red blood cells carry **no A, B, or D antigens** on their surface.\n- Therefore, no recipient's plasma antibodies (anti-A, anti-B, or anti-D) can react with them.\n- O⁻ blood can be transfused into any patient in an emergency — critical in trauma situations where blood typing takes too long.\n\n**Universal Recipient — AB-Positive (AB⁺):**\n- AB⁺ plasma contains **no anti-A, anti-B, or anti-D antibodies** (because the body does not make antibodies against its own antigens).\n- Therefore, AB⁺ individuals can receive blood of any type without agglutination.\n\n**Important misconception:** Although O⁻ is the universal donor, O⁻ individuals can **only receive O⁻ blood** — their plasma contains anti-A, anti-B antibodies, and they will produce anti-D antibodies upon Rh⁺ exposure, making any other blood type fatal to them."
                        }
                    }
                ],
                # Page 6: Rhesus Incompatibility in Pregnancy
                [
                    {
                        "type": "concept",
                        "title": "Rhesus Incompatibility in Pregnancy: Erythroblastosis Fetalis",
                        "content": {
                            "heading": "When a Mother's Immune System Attacks Her Own Baby",
                            "body": "**This life-threatening condition follows a specific sequence:**\n\n**First Pregnancy:**\nAn Rh⁻ mother carries an Rh⁺ fetus (Rh⁺ antigen inherited from the Rh⁺ father). During normal pregnancy, the maternal and fetal blood supplies are separated by the placenta. During childbirth, small amounts of fetal Rh⁺ red blood cells escape into the mother's bloodstream. Her immune system identifies the fetal D-antigens as foreign and produces **anti-D antibodies**. Because this happens during delivery, the first baby is born safely before antibodies accumulate in sufficient quantity.\n\n**Second Pregnancy (with another Rh⁺ fetus):**\nThe mother already has anti-D memory cells and antibodies. These anti-D antibodies are small enough (IgG class) to cross the placenta into the fetal bloodstream. They bind to and destroy the fetus's Rh⁺ red blood cells, causing severe fetal anaemia, jaundice, brain damage, or stillbirth — a condition called **erythroblastosis fetalis (haemolytic disease of the newborn)**.\n\n**Prevention:** The Rh⁻ mother is given an **anti-D immunoglobulin injection (RhoGAM)** within 72 hours of delivering an Rh⁺ baby. This injection destroys any circulating fetal Rh⁺ cells in the mother's blood before her immune system can produce anti-D memory cells."
                        }
                    }
                ],
                # Page 7: Misconception — Universal Donor Can Receive Anything
                [
                    {
                        "type": "concept",
                        "title": "Misconception: O-Negative Can Receive Any Blood",
                        "content": {
                            "heading": "The Universal Donor Cannot Receive from Anyone",
                            "body": "**You may think:** Since O-negative is the 'Universal Donor,' they can also receive blood from anyone.\n\n**Actually:** Group O-negative individuals can **only receive blood from other O-negative donors** — they are the most restricted recipients of all!\n\nHere is why:\n- Their plasma contains **both anti-A and anti-B antibodies** — receiving any blood with A or B antigens triggers fatal agglutination.\n- They lack Antigen D (Rh⁻), so exposure to Rh⁺ blood causes their immune system to produce anti-D antibodies, leading to a severe haemolytic transfusion reaction.\n\n**The paradox:** O-negative individuals are universal donors precisely because their red blood cells carry no antigens that can trigger other people's antibodies. But their own plasma is highly reactive to virtually every other blood type — making compatible blood for them very precious and sometimes in short supply."
                        }
                    }
                ],
                # Page 8: Key Terms
                [
                    {
                        "type": "key_terms",
                        "title": "Key Terms: Blood Grouping",
                        "content": {
                            "terms": [
                                {"term": "Antigen", "definition": "A marker protein found on the surface membrane of red blood cells that identifies the blood group."},
                                {"term": "Antibody", "definition": "A defensive Y-shaped protein found in blood plasma that binds to specific matching antigens."},
                                {"term": "Agglutination", "definition": "The clumping of red blood cells caused by antibodies binding to matching foreign antigens on cell membranes — can be fatal in transfusion mismatches."},
                                {"term": "Universal Donor", "definition": "A person with blood type O-negative (O⁻), whose red blood cells lack A, B, and D antigens, making their blood safe to transfuse into any recipient."},
                                {"term": "Universal Recipient", "definition": "A person with blood type AB-positive (AB⁺), whose blood plasma lacks anti-A, anti-B, and anti-D antibodies, allowing them to safely receive any blood type."},
                                {"term": "Erythroblastosis Fetalis", "definition": "A condition where an Rh⁻ mother's anti-D antibodies cross the placenta and destroy the red blood cells of an Rh⁺ fetus, causing severe anaemia and jaundice."},
                                {"term": "RhoGAM (Anti-D Immunoglobulin)", "definition": "An injection given to Rh⁻ mothers within 72 hours of delivering an Rh⁺ baby to destroy fetal Rh⁺ cells before the mother's immune system produces anti-D memory cells."}
                            ]
                        }
                    }
                ],
                # Page 9: Knowledge Check
                [
                    {
                        "type": "assessment",
                        "title": "Knowledge Check: Blood Grouping",
                        "content": {
                            "question": "A patient with blood group B-negative (B⁻) is rushed to a hospital in Nairobi after a severe haemorrhage. The blood bank has several blood units available. Which blood groups can this patient safely receive?",
                            "options": [
                                "B⁺ and AB⁻",
                                "B⁻ and O⁻",
                                "B⁻ and B⁺",
                                "O⁺, O⁻, and B⁻"
                            ],
                            "correct_index": 1,
                            "explanation": "A patient with group B⁻ has B-antigens on their red blood cells and lacks Antigen D. Their plasma contains anti-A antibodies and they will produce anti-D antibodies if exposed to Rh⁺ blood. Therefore, they cannot receive any blood containing A-antigens (A, AB) or the Rhesus factor (Rh⁺ types). They can only safely receive B⁻ or the universal donor O⁻."
                        }
                    }
                ],
            ]
        },
    ]


@transaction.atomic
def ingest_topic9(replace=False):
    """Main ingestion function for Grade 10 Biology Topic 9."""
    print("=" * 70)
    print("VLearn Grade 10 Biology — Topic 9: Animal Transport")
    print("Ingestion Engine v1.0")
    print("=" * 70)

    # Fetch parent objects by known IDs (Grade 10, CBC Biology, Subject ID 35)
    curriculum = Curriculum.objects.get(id=5)
    grade = Grade.objects.get(id=5)
    subject = Subject.objects.get(id=35)

    print(f"Curriculum: {curriculum.name} (ID: {curriculum.id})")
    print(f"Grade: {grade.name} (ID: {grade.id})")
    print(f"Subject: {subject.name} (ID: {subject.id})")

    # Scope isolation guard: ensure the subject belongs to Grade 10 Biology only
    assert subject.grade == grade, "SCOPE ISOLATION ERROR: Subject does not belong to Grade 10!"
    assert "biology" in subject.name.lower(), "SCOPE ISOLATION ERROR: Subject is not Biology!"

    # Create or replace Topic 9
    if replace:
        existing = Topic.objects.filter(subject=subject, order=9)
        if existing.exists():
            print(f"Replacing existing Topic 9: {existing.first().name}")
            for topic in existing:
                for unit in LearningUnit.objects.filter(topic=topic):
                    for lesson in Lesson.objects.filter(unit=unit):
                        LessonBlock.objects.filter(lesson=lesson).delete()
                        lesson.delete()
                    unit.delete()
                topic.delete()

    topic, created = Topic.objects.get_or_create(
        subject=subject,
        order=9,
        defaults={"name": "Animal Transport"}
    )
    if not created:
        if not replace:
            print(f"Topic 9 already exists (ID: {topic.id}). Use --replace to overwrite.")
            return
        topic.name = "Animal Transport"
        topic.save()

    print(f"Topic 9: {topic.name} (ID: {topic.id}) — {'created' if created else 'updated'}")

    curriculum_data = build_topic9_curriculum()
    total_lessons = 0
    total_cards = 0
    total_blocks = 0

    for unit_data in curriculum_data:
        # Create Learning Unit
        unit = LearningUnit.objects.create(
            topic=topic,
            order=unit_data["unit_order"],
            name=unit_data["unit_name"],
            description=unit_data["unit_description"],
        )
        print(f"\n  Unit {unit_data['unit_order']}: {unit.name} (ID: {unit.id})")

        # Create Lesson
        lesson = Lesson.objects.create(
            learning_unit=unit,
            topic=topic,
            title=unit_data["lesson_title"],
            status="published",
        )
        total_lessons += 1
        print(f"    Lesson: {lesson.title} (ID: {lesson.id})")

        pages = unit_data["pages"]
        for page_index, page_blocks in enumerate(pages, start=1):
            for block_data in page_blocks:
                content = clean_dict(block_data.get("content", {}))
                block = LessonBlock.objects.create(
                    lesson=lesson,
                    page_number=page_index,
                    block_type=block_data["type"],
                    title=clean_text(block_data.get("title", "")),
                    content=content,
                    order=1,
                )
                total_blocks += 1
            total_cards += 1

        print(f"    Pages (Concept Cards): {len(pages)} | Blocks: {sum(len(p) for p in pages)}")

    print("\n" + "=" * 70)
    print(f"INGESTION COMPLETE")
    print(f"Topic 9: Animal Transport — ID: {topic.id}")
    print(f"Total Lessons Ingested: {total_lessons}")
    print(f"Total Concept Cards (Pages): {total_cards}")
    print(f"Total LessonBlocks: {total_blocks}")
    print("=" * 70)


if __name__ == "__main__":
    import sys
    replace = "--replace" in sys.argv
    ingest_topic9(replace=replace)
